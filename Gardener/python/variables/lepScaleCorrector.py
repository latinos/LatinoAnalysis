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
        group.add_option('--fileInScaleEle',   dest='FileWithPtScaleDataEle' ,help='file with lep pT scale values to be applied to Data for Ele',default=None)
        group.add_option('--fileInSmearingEle',dest='FileWithPtSmearingMCEle',help='file with lep pT smearing values to be applied to MC for Ele',default=None)
        group.add_option('-w','--isData',dest='isData',help='is data? 1 = data, 0 = mc', default=1)
        parser.add_option_group(group)
        return group

    def checkOptions(self,opts):
        print " >>  checkOptions "
   
        #
        # check inputs from https://twiki.cern.ch/twiki/bin/viewauth/CMS/EGMSmearer
        #    https://github.com/ECALELFS/ScalesSmearings/blob/master/80X_10JunGoldplusDCS_approval_scales.dat
        #    https://github.com/ECALELFS/ScalesSmearings/blob/master/80X_10JunGoldplusDCS_approval_smearings.dat
        #
        # from Giuseppe: /afs/cern.ch/user/g/gfasanel/public/test_2016B/80X_DCS05July_plus_Golden22_scales.dat
        #
         
        self.cmssw = opts.cmssw
        cmssw_base = os.getenv('CMSSW_BASE')
        if opts.cmssw == 'Full2016' :
          if opts.FileWithPtScaleDataEle == None :
            opts.FileWithPtScaleDataEle = cmssw_base+'/src/LatinoAnalysis/Gardener/python/data/lepton_corrections/Moriond17_23Jan_ele_scales.dat'
          print " opts.FileWithPtScaleDataEle = " , opts.FileWithPtScaleDataEle
          if opts.FileWithPtSmearingMCEle == None :
            opts.FileWithPtSmearingMCEle = cmssw_base+'/src/LatinoAnalysis/Gardener/python/data/lepton_corrections/Moriond17_23Jan_ele_smearings.dat'
          print " opts.FileWithPtSmearingMCEle = " , opts.FileWithPtSmearingMCEle
        elif opts.cmssw == 'ICHEP2016' :
          if opts.FileWithPtScaleDataEle == None :
            opts.FileWithPtScaleDataEle = cmssw_base+'/src/LatinoAnalysis/Gardener/python/data/lepton_corrections/80X_DCS05July_plus_Golden22_scales.dat'
            #opts.FileWithPtScaleDataEle = cmssw_base+'/src/LatinoAnalysis/Gardener/python/data/lepton_corrections/80X_28JunPrompt_2016_scales.dat'
          print " opts.FileWithPtScaleDataEle = " , opts.FileWithPtScaleDataEle
          if opts.FileWithPtSmearingMCEle == None :
            opts.FileWithPtSmearingMCEle = cmssw_base+'/src/LatinoAnalysis/Gardener/python/data/lepton_corrections/80X_28JunPrompt_2016_smearings.dat'
          print " opts.FileWithPtSmearingMCEle = " , opts.FileWithPtSmearingMCEle
        else :    # 2015 numbers re-reco
          if opts.FileWithPtScaleDataEle == None :
            opts.FileWithPtScaleDataEle = cmssw_base+'/src/LatinoAnalysis/Gardener/python/data/lepton_corrections/76X_16DecRereco_2015_scales.dat'
          print " opts.FileWithPtScaleDataEle = " , opts.FileWithPtScaleDataEle
          if opts.FileWithPtSmearingMCEle == None :
            opts.FileWithPtSmearingMCEle = cmssw_base+'/src/LatinoAnalysis/Gardener/python/data/lepton_corrections/76X_16DecRereco_2015_smearings.dat'
          print " opts.FileWithPtSmearingMCEle = " , opts.FileWithPtSmearingMCEle
          




        file_FileWithPtScaleDataEle  = open (opts.FileWithPtScaleDataEle)
        file_FileWithPtSmearingMCEle = open (opts.FileWithPtSmearingMCEle)
        
        self.leppTscaler = {}
        self.leppTscaler['ele']   =    [line.rstrip().split() for line in file_FileWithPtScaleDataEle]
        #  e.g.        [ eta  ]    string              [     run    ]   scale   boh? uncertainties?
        #               0    1    lowR9                254790  256629  1.0028  0.0007 0.0001 0.0002 


        self.leppTsmearing = {}
        self.leppTsmearing['ele']   =    [line.rstrip().split() for line in file_FileWithPtSmearingMCEle if '#' not in line ]
        #  e.g.
        #       # category             Emean    err   Emean    rho            err   rho       
        #       0   1   highR9         0        0            0.0080     0.0005       

        #print " leppTsmearing = ", self.leppTsmearing
     
        self.isData = float(opts.isData)
        print " self.isData = ", self.isData

    def _getScale (self, kindLep, pt, eta, run, r9_lep):
        
        if kindLep in self.leppTscaler.keys() : 
          for point in self.leppTscaler[kindLep] :
            if kindLep == 'ele':
              if (point[2] == 'highR9' and r9_lep>=0.94) or (point[2] == 'lowR9' and r9_lep<0.94):  # FIXME new               
              # use only high R9 for electrons
              #if point[2] == 'highR9': 
                if run >= float(point[3])  and run < (float(point[4])+1) : 
                  if ( abs(eta) >= float(point[0]) and abs(eta) < float(point[1]) ) :
                    return float(point[5])
        
        # default ... it should never happen!
        # print " default ???"
        return 1.0
         
         

    def _getSmearing (self, kindLep, pt, eta):

        #print " kindLep = ", kindLep
        if kindLep in self.leppTsmearing.keys() : 
          for point in self.leppTsmearing[kindLep] :
            if kindLep == 'ele':
              # use only high R9 for electrons
              if point[2] == 'highR9': 
                #print " ", point[0], " - ", point[1] , " :: ", eta, " ---> ", point[5]
                if ( abs(eta) >= float(point[0]) and abs(eta) < float(point[1]) ) :
                  return float(point[5])
        # default ... it should never happen!
        # print " default ???"
        return 0.0
  
  
    
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

        if self.cmssw == '74x' :
            self.metvar1 = 'pfType1Met'
            self.metvar2= 'pfType1Metphi' 
        else :
            self.metvar1 = 'metPfType1'
            self.metvar2= 'metPfType1Phi' 
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

            if self.cmssw == '74x' :
              oldmet = itree.pfType1Met
              oldphi = itree.pfType1Metphi
            else :
              oldmet = itree.metPfType1
              oldphi = itree.metPfType1Phi
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

                if not self.isData == 1 : 
                  r9_lep = 0.                                  # FIXME new
                else:
                  r9_lep  = itree.std_vector_electron_R9[i]   # FIXME new
                #print "pt eta phi r9 = ",pt_lep, ' ' , eta_lep, ' ' , phi_lep, ' ' , r9_lep

                new_pt_lep = pt_lep
                
                if abs(itree.std_vector_lepton_flavour[i]) == 13:
                    kindLep = 'mu'
                elif abs(itree.std_vector_lepton_flavour[i]) == 11:
                    kindLep = 'ele'
                else:
                    print "not a el or muon"

                # scale the data and smear the MC
                if self.isData == 1 : 
                  #r9_lep = 0.                                  # FIXME new
                  r9_lep  = itree.std_vector_electron_R9[i]   # FIXME new
                  wt = self._getScale(kindLep, pt_lep, eta_lep, itree.run, r9_lep)
                  #print " wt = ", wt
                  new_pt_lep = itree.std_vector_lepton_pt[i] * wt
                  leptonPtChanged.append( itree.std_vector_lepton_pt[i] * wt )
                  #print " wt = ", wt
                else :
                  #print " seariously you are smearing? "
                  smearing = self._getSmearing(kindLep, pt_lep, eta_lep)
                  wt = -1
                  if smearing != 0:
                    while wt < 0 :
                      wt = ROOT.gRandom.Gaus(1, smearing)
                  else:
                    wt = 1
                  new_pt_lep = itree.std_vector_lepton_pt[i] * wt
                  leptonPtChanged.append( itree.std_vector_lepton_pt[i] * wt )
                  #print " wt = ", wt, " smearing = ", smearing
                  
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

