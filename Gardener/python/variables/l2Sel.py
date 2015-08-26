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

    def changeOrder(self, vector, goodleptonslist) :
        # take vector and clone vector
        # equivalent of: temp_vector = itree."vector"
        temp_vector = getattr(self.itree, vector)
        # remix the order of vector picking from the clone
        for i in range( len(goodleptonslist) ) :
          # otree."vector"[i] = temp_vector[goodleptonslist[i]] <--- that is the "itree" in the correct position
          setattr(self.otree, vector + "[" + str(i) + "]", temp_vector[ goodleptonslist[i] ])
        # set the default value for the remaining
        for i in range( len(temp_vector) - len(goodleptonslist) ) :
          setattr(self.otree, vector + "[" + str(i) + "]", -9999.) # default value!
         
        pass
                    
    def process(self,**kwargs):
        tree  = kwargs['tree']
        input = kwargs['input']
        output = kwargs['output']

        # does that work so easily and give new variable itree and otree?
        self.connect(tree,input)
        newbranches = []
        self.clone(output,newbranches)

        nentries = self.itree.GetEntries()
        print 'Total number of entries: ',nentries 

        # input tree and output tree
        itree     = self.itree
        otree     = self.otree

        #----------------------------------------------------------------------------------------------------
        print '- Starting eventloop'
        step = 5000

        for i in xrange(nentries):

            itree.GetEntry(i)

            if i > 0 and i%step == 0.:
                print i,'events processed.'

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
                   and itree.std_vector_lepton_flavour[iLep] == 11 
                  ) :
                isGoodLepton = True

              if ( itree.std_vector_lepton_isMediumMuon[iLep] == 1 
                   and (itree.std_vector_lepton_chargedHadronIso[iLep] + itree.std_vector_lepton_neutralHadronIso[iLep] + itree.std_vector_lepton_photonIso[iLep])/itree.std_vector_lepton_pt[iLep] < 0.20 
                   and itree.std_vector_lepton_flavour[iLep] == 13 
                  ) :
                isGoodLepton = True
              
              if isGoodLepton :
                if goodLep1 < 0: 
                  goodLep1 = iLep
                elif goodLep2 < 0 :
                  goodLep2 = iLep
                goodLeps.append(iLep)
            
            # require at least 2 good leptons
            if goodLep1 > 0 and goodLep2 > 0 :

              otree.pt1 = itree.std_vector_lepton_pt[goodLep1]
              otree.pt2 = itree.std_vector_lepton_pt[goodLep2]
              otree.phi1 = itree.std_vector_lepton_pt[goodLep1]
              otree.phi2 = itree.std_vector_lepton_pt[goodLep2]
            
              # now filter the leptons list
              # [ x, - , - , x , x , x , - , - ]
              # [ x  x   x   x   -   -   -   - ]
            
              self.changeOrder( "std_vector_lepton_pt" , goodLeps)
              self.changeOrder( "std_vector_lepton_eta", goodLeps)
              self.changeOrder( "std_vector_lepton_phi", goodLeps)
            
            #for iLep in xrange(len(goodLeps)) :
              #itree.std_vector_lepton_pt[iLep] = itree.std_vector_lepton_pt[ goodLeps[iLep] ]
            #for iLep in xrange(len(itree.std_vector_lepton_pt) - len(goodLeps)) :
              #itree.std_vector_lepton_pt[iLep] = -10. 
              

              
              otree.Fill()

        self.disconnect()
        print '- Eventloop completed'
