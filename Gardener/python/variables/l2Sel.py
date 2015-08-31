#
#
#      |     ___ \  
#      |        ) | 
#      |       __/  
#     _____| _____| 
#                                
#
#


from LatinoAnalysis.Gardener.gardening import TreeCloner
import numpy
import ROOT
import sys
import optparse
import re
import warnings
import os.path
from array import array;

class L2SelFiller(TreeCloner):
    def __init__(self):
       pass

    def help(self):
        return '''Apply id/iso and filter lepton collection'''

    def addOptions(self,parser):
        pass

    def checkOptions(self,opts):
        pass

    def changeOrder(self, vectorname, vector, goodleptonslist) :
        # vector is already linked to the otree branch
        # vector name is the "name" of that vector to be modified
        
        #for i in range( len(getattr(self.otree, vectorname)) ) :
          #pass
          #print " --> before ", vectorname, "[", i, "] = ", getattr(self.otree, vectorname)[i]

        # take vector and clone vector
        # equivalent of: temp_vector = itree."vector"
        temp_vector = getattr(self.itree, vectorname)
        # remix the order of vector picking from the clone
        for i in range( len(goodleptonslist) ) :
          #print " --> [", i, " :: ", len(goodleptonslist) ,"] :::>> ", len(temp_vector), " --> ", goodleptonslist[i]      
          # otree."vectorname"[i] = temp_vector[goodleptonslist[i]] <--- that is the "itree" in the correct position
          # setattr(self.otree, vector + "[" + str(i) + "]", temp_vector[ goodleptonslist[i] ])
          vector.push_back ( temp_vector[ goodleptonslist[i] ] )
          #vector.push_back ( 10000. )
        # set the default value for the remaining
        for i in range( len(temp_vector) - len(goodleptonslist) ) :
          vector.push_back ( -9999. )
          
        #for i in range( len(getattr(self.otree, vectorname)) ) :
          #pass
          #print " --> after[ " , len(goodleptonslist), "] ", vectorname, "[", i, "] = ", getattr(self.otree, vectorname)[i]
         
                    
    def process(self,**kwargs):
        tree  = kwargs['tree']
        input = kwargs['input']
        output = kwargs['output']

        # does that work so easily and give new variable itree and otree?
        self.connect(tree,input)

        nentries = self.itree.GetEntries()
        print 'Total number of entries: ',nentries 


        # create branches for otree, the ones that will be modified!
        # see: https://root.cern.ch/phpBB3/viewtopic.php?t=12507
        
        self.namesOldBranchesToBeModifiedVector = [
           'std_vector_lepton_pt',
           'std_vector_lepton_phi',
           'std_vector_lepton_eta',
           'std_vector_lepton_flavour',
           'std_vector_lepton_isMediumMuon',
           'std_vector_lepton_isTightMuon',
           'std_vector_lepton_muSIP3D',
           'std_vector_lepton_elSIP3D',
           'std_vector_lepton_ch'
           ]
        
        self.namesOldBranchesToBeModifiedSimpleVariable = [
           'mll',
           'dphill',
           'yll',
           'ptll',
           'pt1',
           'pt2',
           'mth'
         ]

        self.clone(output,self.namesOldBranchesToBeModifiedVector + self.namesOldBranchesToBeModifiedSimpleVariable)

        self.oldBranchesToBeModifiedVector = {}
        for bname in self.namesOldBranchesToBeModifiedVector:
          bvector =  ROOT.std.vector(float) ()
          self.oldBranchesToBeModifiedVector[bname] = bvector

        # now actually connect the branches
        for bname, bvector in self.oldBranchesToBeModifiedVector.iteritems():
            print " bname   = ", bname
            print " bvector = ", bvector
            self.otree.Branch(bname,bvector)


        self.oldBranchesToBeModifiedSimpleVariable = {}
        for bname in self.namesOldBranchesToBeModifiedSimpleVariable:
          bvariable = numpy.ones(1, dtype=numpy.float32)
          self.oldBranchesToBeModifiedSimpleVariable[bname] = bvariable

        # now actually connect the branches
        for bname, bvariable in self.oldBranchesToBeModifiedSimpleVariable.iteritems():
            print " bname   = ", bname
            print " bvariable = ", bvariable
            self.otree.Branch(bname,bvariable,bname+'/F')



        # input tree and output tree
        itree     = self.itree
        otree     = self.otree


        # change this part into correct path structure... 
        cmssw_base = os.getenv('CMSSW_BASE')
        try:
            ROOT.gROOT.LoadMacro(cmssw_base+'/src/LatinoAnalysis/Gardener/python/variables/WWVar.C+g')
        except RuntimeError:
            ROOT.gROOT.LoadMacro(cmssw_base+'/src/LatinoAnalysis/Gardener/python/variables/WWVar.C++g')


        #----------------------------------------------------------------------------------------------------
        print '- Starting eventloop'
        step = 5000


        #for i in xrange(10000):
        for i in xrange(nentries):

            itree.GetEntry(i)

            if i > 0 and i%step == 0.:
                print i,'events processed :: ', nentries

            # apply lepton id and isolation
            # and filter out unwanted leptons
            # putting pt of those leptons to -10 GeV

            goodLeps = []
            goodLep1 = -1
            goodLep2 = -1
            
            for iLep in xrange(len(itree.std_vector_lepton_pt)) :
              isGoodLepton = False
              # id definition
              if ( itree.std_vector_lepton_eleIdMedium[iLep] == 1
                   and abs(itree.std_vector_lepton_flavour[iLep]) == 11 
                  ) :
                isGoodLepton = True

              if ( itree.std_vector_lepton_isMediumMuon[iLep] == 1 
                   and (itree.std_vector_lepton_chargedHadronIso[iLep] + 
                        itree.std_vector_lepton_neutralHadronIso[iLep] + 
                        itree.std_vector_lepton_photonIso[iLep]
                        ) / itree.std_vector_lepton_pt[iLep] < 0.20 
                   and abs(itree.std_vector_lepton_flavour[iLep]) == 13 
                  ) :
                isGoodLepton = True
              
              if isGoodLepton :
                if goodLep1 < 0: 
                  goodLep1 = iLep
                elif goodLep2 < 0 :
                  goodLep2 = iLep
                goodLeps.append(iLep)
            
            
            #print " goodLep1 = ", goodLep1, 
            #print " goodLep2 = ", goodLep2
            
            # require at least 2 good leptons
            if goodLep1 >= 0 and goodLep2 >= 0 :
            
              # now filter the leptons list
              # [ x, - , - , x , x , x , - , - ]
              # [ x  x   x   x   -   -   -   - ]
              for bname, bvector in self.oldBranchesToBeModifiedVector.iteritems():
                bvector.clear()
             
              for bname, bvector in self.oldBranchesToBeModifiedVector.iteritems():
                self.changeOrder( bname, bvector , goodLeps)


              pt1 = itree.std_vector_lepton_pt[goodLep1]
              pt2 = itree.std_vector_lepton_pt[goodLep2]

              eta1 = itree.std_vector_lepton_eta[goodLep1]
              eta2 = itree.std_vector_lepton_eta[goodLep2]
              
              phi1 = itree.std_vector_lepton_phi[goodLep1]
              phi2 = itree.std_vector_lepton_phi[goodLep2]
              
              
              met = itree.pfType1Met
              metphi = itree.pfType1Metphi
             
              WW = ROOT.WW(pt1, pt2, eta1, eta2, phi1, phi2, met, metphi)
                          
              for bname, bvariable in self.oldBranchesToBeModifiedSimpleVariable.iteritems():
                bvariable[0] = getattr(WW, bname)()
                
                
              # now you have to filter the jets from the lepton collection
              # FIXME
              
              
                #if bname == 'mll' :
                  #bvariable[0] = WW.mll()
                
              #otree.pt1 = itree.std_vector_lepton_pt[goodLep1]
              #otree.pt2 = itree.std_vector_lepton_pt[goodLep2]
              #otree.phi1 = itree.std_vector_lepton_pt[goodLep1]
              #otree.phi2 = itree.std_vector_lepton_pt[goodLep2]


              #self.changeOrder( "std_vector_lepton_eta", goodLeps)
              #self.changeOrder( "std_vector_lepton_phi", goodLeps)
            
            #for iLep in xrange(len(goodLeps)) :
              #itree.std_vector_lepton_pt[iLep] = itree.std_vector_lepton_pt[ goodLeps[iLep] ]
            #for iLep in xrange(len(itree.std_vector_lepton_pt) - len(goodLeps)) :
              #itree.std_vector_lepton_pt[iLep] = -10. 
              

              
              otree.Fill()

        self.disconnect()
        print '- Eventloop completed'
