#
#
#     | ___ \   |  / _)        
#     |    ) |  ' /   |  __ \  
#     |   __/   . \   |  |   | 
#    _| _____| _|\_\ _| _|  _| 
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

class L2KinFiller(TreeCloner):
    def __init__(self):
       pass

    def help(self):
        return '''Calculate kinematic variables, event base and not single object based. They are all simple float variables like mll, dphill, ... '''

    def addOptions(self,parser):
        description = self.help()
        group = optparse.OptionGroup(parser,self.label, description)
        group.add_option('-c', '--cmssw', dest='cmssw', help='cmssw version (naming convention may change)', default='763', type='string')
        group.add_option("-m" , "--met" , dest="met", help="PFMET correction" , default=False  , action="store_true")
        parser.add_option_group(group)
        return group

    def checkOptions(self,opts):

        self.cmssw = opts.cmssw
        print " cmssw = ", self.cmssw
        self.met = opts.met
        print " MET CORR = ", self.met

                    
    def process(self,**kwargs):
        tree  = kwargs['tree']
        input = kwargs['input']
        output = kwargs['output']

        # does that work so easily and give new variable itree and otree?
        self.connect(tree,input)

        nentries = self.itree.GetEntries()
        print 'Total number of entries: ',nentries 
        savedentries = 0

        #
        # create branches for otree, the ones that will be modified!
        # These variables NEED to be defined as functions in WWVar.C
        # e.g. mll, dphill, ...
        # if you add a new variable here, be sure it IS defined in WWVar.C
        #
        self.namesOldBranchesToBeModifiedSimpleVariable = [
           'mll',
           'dphill',
           'yll',
           'ptll',
           'pt1',
           'pt2',
           'mth',
           'mcoll',
           'mcollWW',
           'mTi',
           'mTe',
           'choiMass',
           'mR',
           'mT2',
           'channel',


           'drll',
           'dphilljet',
           'dphilljetjet',
           'dphilljetjet_cut',
           'dphillmet',
           'dphilmet',
           'dphilmet1',
           'dphilmet2',
           'mtw1',
           'mtw2',
           
           'mjj',
           'detajj',
           'njet',
          
	   'mllWgSt',
	   'drllWgSt',
           'mllThird',
           'mllOneThree',
           'mllTwoThree',
           'drllOneThree',
           'drllTwoThree',
           
           'dphijet1met',  
           'dphijet2met',  
           'dphijjmet',    
           'dphijjmet_cut',    
           'dphilep1jet1', 
           'dphilep1jet2', 
           'dphilep2jet1', 
           'dphilep2jet2', 
           'maxdphilepjj',
           'dphilep1jj',           
           'dphilep2jj',           
           'ht',
           'vht_pt',
           'vht_phi',
           
           'projpfmet',
           'dphiltkmet',
           'projtkmet',
           'mpmet',
           
           'pTWW',

           'recoil',
           'jetpt1_cut',
           'jetpt2_cut',
           'dphilljet_cut',
           'dphijet1met_cut',
           'dphijet2met_cut',
           'PfMetDivSumMet',
           'upara',
           'uperp',
           'm2ljj20',
           'm2ljj30',
# for VBF training
           'ptTOT_cut',
           'mTOT_cut',
           'OLV1_cut',
           'OLV2_cut',
           'Ceta_cut',
#whss
           'mlljj20_whss',
           'mlljj30_whss'
           ]
        
        # clone the tree
        self.clone(output, self.namesOldBranchesToBeModifiedSimpleVariable)

        self.oldBranchesToBeModifiedSimpleVariable = {}
        for bname in self.namesOldBranchesToBeModifiedSimpleVariable:
          bvariable = numpy.ones(1, dtype=numpy.float32)
          self.oldBranchesToBeModifiedSimpleVariable[bname] = bvariable

        # now actually connect the branches
        for bname, bvariable in self.oldBranchesToBeModifiedSimpleVariable.iteritems():
            #print " bname   = ", bname
            #print " bvariable = ", bvariable
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

        #for i in xrange(2000):
        for i in xrange(nentries):

            itree.GetEntry(i)

            if i > 0 and i%step == 0.:
                print i,'events processed :: ', nentries

            WW = ROOT.WW()
            WW.setLeptons(itree.std_vector_lepton_pt, itree.std_vector_lepton_eta, itree.std_vector_lepton_phi, itree.std_vector_lepton_flavour)
            WW.setJets   (itree.std_vector_jet_pt,       itree.std_vector_jet_eta,    itree.std_vector_jet_phi,    itree.std_vector_jet_mass)
            
            sumet = 0.1
            if self.cmssw == '74x' :
                met = itree.pfType1Met          # formerly pfType1Met
                metphi = itree.pfType1Metphi    # formerly pfType1Metphi
                sumet  = 0.000000001

            else : 
              if self.met :
                met = itree.corrMetPfType1
                metphi = itree.corrMetPfType1Phi
                sumet = itree.metPfType1SumEt
              else:
                met = itree.metPfType1      
                metphi = itree.metPfType1Phi
                sumet = itree.metPfType1SumEt

              WW.setTkMET(itree.metTtrk, itree.metTtrkPhi) # before in 74x we were missing this variable  
                
            WW.setMET(met, metphi)
            WW.setSumET(sumet)
            WW.checkIfOk()

 
            # now fill the variables like "mll", "dphill", ...
            for bname, bvariable in self.oldBranchesToBeModifiedSimpleVariable.iteritems():
              bvariable[0] = getattr(WW, bname)()
              
            otree.Fill()
            savedentries+=1

        self.disconnect()
        print '- Eventloop completed'
        print '   Saved: ', savedentries, ' events'

