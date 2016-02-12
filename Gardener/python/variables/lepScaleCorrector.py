#     
#     
#        |                   |                          __ __|                                          |                
#        |       _ \  __ \   __|   _ \   __ \       __ \   |         __|   _ \    __|   __|  _ \   __|  __|   _ \    __| 
#        |       __/  |   |  |    (   |  |   |      |   |  |        (     (   |  |     |     __/  (     |    (   |  |    
#       _____| \___|  .__/  \__| \___/  _|  _|      .__/  _|       \___| \___/  _|    _|   \___| \___| \__| \___/  _|    
#                    _|                            _|                                                                    
#     
#      
#      

from LatinoAnalysis.Gardener.gardening import TreeCloner
import numpy
import ROOT
import math
import sys
import optparse
import re
import warnings
import os.path
from collections import OrderedDict
from array import array;

class LeptonPtCorrector(TreeCloner):
    def __init__(self):
       pass

    def help(self):
        return '''Lepton pT corrector'''

    def addOptions(self,parser):
        description = self.help()
        group = optparse.OptionGroup(parser,self.label, description)
        group.add_option('-c','--cmssw',dest='cmssw',help='cmssw version req for met vars',default='763')
        group.add_option('-d','--fileInScale',   dest='FileWithPtScaleData' ,help='file with lep pT scale values to be applied to Data',default=None)
        group.add_option('-m','--fileInSmearing',dest='FileWithPtSmearingMC',help='file with lep pT smearing values to be applied to MC',default=None)
        group.add_option('-w','--isData',dest='isData',help='is data? 1 = data, 0 = mc', default='1')
        parser.add_option_group(group)
        return group

    def checkOptions(self,opts):
        print " >>  checkOptions "
        leppTscaler = {}     
        leppTsmearing = {}     
   
        self.cmssw=opts.cmssw
        cmssw_base = os.getenv('CMSSW_BASE')
        if opts.FileWithPtScaleData == None :
          opts.FileWithPtScaleData = cmssw_base+'/src/LatinoAnalysis/Gardener/python/data/lepton_corrections/76X_16DecRereco_2015_scales.dat'
        print " opts.FileWithPtScaleData = " , opts.FileWithPtScaleData
        if opts.FileWithPtSmearingMC == None :
          opts.FileWithPtSmearingMC = cmssw_base+'/src/LatinoAnalysis/Gardener/python/data/lepton_corrections/76X_16DecRereco_2015_smearings.dat'
        print " opts.FileWithPtSmearingMC = " , opts.FileWithPtSmearingMC

        if os.path.exists(opts.FileWithPtScaleData) :
          print " opts.FileWithPtScaleData = " , opts.FileWithPtScaleData
          handle = open(opts.FileWithPtScaleData,'r')
          exec(handle)
          handle.close()
        else :
          print "nothing ?"


        if os.path.exists(opts.FileWithPtSmearingMC) :
          print " opts.FileWithPtSmearingMC = " , opts.FileWithPtSmearingMC
          handle = open(opts.FileWithPtSmearingMC,'r')
          exec(handle)
          handle.close()
        else :
          print "nothing ?"

        self.leppTscaler = leppTscaler
        self.leppTsmearing = leppTsmearing
        
        self.minpt_mu = 10
        self.maxpt_mu = 200
        self.mineta_mu = -2.4
        self.maxeta_mu = 2.4
        
        self.minpt_ele = 10
        self.maxpt_ele = 100
        self.mineta_ele = -2.5
        self.maxeta_ele = 2.5

        self.isData = opts.isData


    def _getScale (self, kindLep, pt, eta, run):
        # fix underflow and overflow

        if abs(kindLep) == 11 :          
          if pt < self.minpt_ele:
            pt = self.minpt_ele
          if pt > self.maxpt_ele:
            pt = self.maxpt_ele
          
          if eta < self.mineta_ele:
            eta = self.mineta_ele
          if eta > self.maxeta_ele:
            eta = self.maxeta_ele

        if abs(kindLep) == 13 :          
          if pt < self.minpt_mu:
            pt = self.minpt_mu
          if pt > self.maxpt_mu:
            pt = self.maxpt_mu
          
          if eta < self.mineta_mu:
            eta = self.mineta_mu
          if eta > self.maxeta_mu:
            eta = self.maxeta_mu
                
        if kindLep in self.leppTscaler.keys() : 
            # get the scale values in bins of pT and eta
            for point in self.leppTscaler[kindLep] :
              if run >= point[2][0] and run < (point[2][1]+1) : 
                if (pt >= point[0][0] and pt < point[0][1] and eta >= point[1][0] and eta < point[1][1]) :
                  return point[2]
            # default ... it should never happen!
            # print " default ???"
            return 1.0
           
        else:
            return 1.0
    

    def _getSmearing (self, kindLep, pt, eta):
        # fix underflow and overflow

        if abs(kindLep) == 11 :          
          if pt < self.minpt_ele:
            pt = self.minpt_ele
          if pt > self.maxpt_ele:
            pt = self.maxpt_ele
          
          if eta < self.mineta_ele:
            eta = self.mineta_ele
          if eta > self.maxeta_ele:
            eta = self.maxeta_ele

        if abs(kindLep) == 13 :          
          if pt < self.minpt_mu:
            pt = self.minpt_mu
          if pt > self.maxpt_mu:
            pt = self.maxpt_mu
          
          if eta < self.mineta_mu:
            eta = self.mineta_mu
          if eta > self.maxeta_mu:
            eta = self.maxeta_mu
        
        if kindLep in self.leppTsmearing.keys() : 
            # get the scale values in bins of pT and eta
            for point in self.leppTsmearing[kindLep] :
                if (pt >= point[0][0] and pt < point[0][1] and eta >= point[1][0] and eta < point[1][1]) :
                    return point[2]
            # default ... it should never happen!
            # print " default ???"
            return 1.0
           
        else:
            return 1.0


    
    def _corMET (self,met,lpt_org,lpt):
        newmet = met + lpt_org - lpt
        return newmet
    
    
    def changeOrder(self, vectorname, vector, leptonOrderList) :
        # vector is already linked to the otree branch
        # vector name is the "name" of that vector to be modified        
        # take vector and clone vector
        # equivalent of: temp_vector = itree."vector"
        temp_vector = getattr(self.itree, vectorname)
        # remix the order of vector picking from the clone
        for i in range( len(leptonOrderList) ) :
          vector.push_back ( temp_vector[ leptonOrderList[i] ] )
        # set the default value for the remaining
        for i in range( len(temp_vector) - len(leptonOrderList) ) :
          vector.push_back ( -9999. )
          

    def process(self,**kwargs):
        tree  = kwargs['tree']
        input = kwargs['input']
        output = kwargs['output']
                
        # does that work so easily and give new variable itree and otree?
        self.connect(tree,input)

        nentries = self.itree.GetEntries()
        print 'Total number of entries: ',nentries 
        savedevents = 0

        # met branches to be changed

        if self.cmssw == '763' :
            self.metvar1 = 'metPfType1'
            self.metvar2= 'metPfType1Phi' 
        else :
            self.metvar1 = 'pfType1Met'
            self.metvar2= 'pfType1Metphi' 
        self.namesOldBranchesToBeModifiedSimpleVariable = [self.metvar1,self.metvar2]

        self.namesOldBranchesToBeModifiedVector = []
	vectorsToChange = ['std_vector_lepton_']
        for b in self.itree.GetListOfBranches():
	    branchName = b.GetName()
	    for subString in vectorsToChange:
		if subString in branchName:
		    self.namesOldBranchesToBeModifiedVector.append(branchName)
        
        # clone the tree with new branches added
        self.clone(output,self.namesOldBranchesToBeModifiedVector+self.namesOldBranchesToBeModifiedSimpleVariable)
      
        self.oldBranchesToBeModifiedVector = {}
        for bname in self.namesOldBranchesToBeModifiedVector:
          bvector =  ROOT.std.vector(float) ()
          self.oldBranchesToBeModifiedVector[bname] = bvector
         # print "debug 0 ", bname
         # connect branches for vectors
        for bname, bvector in self.oldBranchesToBeModifiedVector.iteritems():
          self.otree.Branch(bname,bvector)            

        self.oldBranchesToBeModifiedSimpleVariable = {}
        for bname in self.namesOldBranchesToBeModifiedSimpleVariable:
          bvariable = numpy.ones(1, dtype=numpy.float32)
          self.oldBranchesToBeModifiedSimpleVariable[bname] = bvariable

        # now actually connect the branches for floats
        for bname, bvariable in self.oldBranchesToBeModifiedSimpleVariable.iteritems():
                        #print " bvariable = ", bvariable
            self.otree.Branch(bname,bvariable,bname+'/F')         
        # input tree  
        itree = self.itree

        print '- Starting eventloop'
        step = 5000
        #step = 1

        for i in xrange(nentries):
            itree.GetEntry(i)

            if i > 0 and i%step == 0.:
              print i,'events processed :: ', nentries
                
            # scale lepton pt
            # Scale Up
            leptonPtChanged = []

            if self.cmssw == '763' :
              oldmet = itree.metPfType1
              oldphi = itree.metPfType1Phi
            else :
              oldmet = itree.pfType1Met
              oldphi = itree.pfType1Metphi
            met_org = ROOT.TLorentzVector()
            met_org.SetPtEtaPhiM(oldmet, 0, oldphi, 0)
            newmet = ROOT.TLorentzVector()
            newmet = met_org

            for i in range(itree.std_vector_lepton_pt.size()):
                #print " i = ", i, " -->  itree.std_vector_lepton_flavour[i] = ", itree.std_vector_lepton_flavour[i]
                #print "    -> ", abs(itree.std_vector_lepton_flavour[i])
                kindLep = 'lep' # ele or mu
                if not (itree.std_vector_lepton_pt[i] > 0):
                    continue
                pt_lep = itree.std_vector_lepton_pt[i]
                eta_lep = itree.std_vector_lepton_eta[i]
                phi_lep = itree.std_vector_lepton_phi[i] 
#                print "pt eta",pt_lep,eta_lep,phi_lep

                new_pt_lep = pt_lep
                
                if abs(itree.std_vector_lepton_flavour[i]) == 13:
                    kindLep = 'mu'
                elif abs(itree.std_vector_lepton_flavour[i]) == 11:
                    kindLep = 'ele'
                else:
                    print "not a el or muon"

                # scale the data and smear the MC
                if self.isData : 
                  wt = self._getScale(kindLep,pt_lep,abs(eta_lep), itree.run)
                  new_pt_lep = itree.std_vector_lepton_pt[i] * wt
                  leptonPtChanged.append( itree.std_vector_lepton_pt[i] * wt )
                else :
                  smearing = self._getSmearing(kindLep,pt_lep,abs(eta_lep))
                  wt = -1
                  while wt < 0 :
                    wt = ROOT.gRandom.Gaus(1, smearing)
                  new_pt_lep = itree.std_vector_lepton_pt[i] * wt
                  leptonPtChanged.append( itree.std_vector_lepton_pt[i] * wt )
                  
                l1 = ROOT.TLorentzVector()
                l1_org = ROOT.TLorentzVector()
                l1_org.SetPtEtaPhiM(pt_lep,    eta_lep, phi_lep,0)
                l1.SetPtEtaPhiM    (new_pt_lep,eta_lep,phi_lep,0)
             
                newmet = self._corMET(newmet,l1_org,l1)

            leptonOrder = sorted(range(len(leptonPtChanged)), key=lambda k: leptonPtChanged[k], reverse=True) 




            for bname, bvector in self.oldBranchesToBeModifiedVector.iteritems():
                bvector.clear()
             
                if 'std_vector_lepton_pt' in bname:
                    for i in range( len(leptonOrder) ) :
                        bvector.push_back ( leptonPtChanged[leptonOrder[i]] )
                    for i in range( len(getattr(self.itree, bname)) - len(leptonOrder) ) :
                        bvector.push_back ( -9999. )
                else:
                    self.changeOrder( bname, bvector, leptonOrder)

            # update met
            self.oldBranchesToBeModifiedSimpleVariable[self.metvar1][0] = numpy.float32(newmet.Pt())
            self.oldBranchesToBeModifiedSimpleVariable[self.metvar2][0] = numpy.float32(newmet.Phi())

            self.otree.Fill()
            savedevents += 1
            
            
        self.disconnect()
        print '- Eventloop completed'
        print '- Saved:', savedevents, 'events'

