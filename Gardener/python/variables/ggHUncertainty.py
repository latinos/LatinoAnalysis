#
#
#
#                 |   |                                      |          _)         |          
#    _` |   _` |  |   |      |   |  __ \    __|   _ \   __|  __|   _` |  |  __ \   __|  |   | 
#   (   |  (   |  ___ |      |   |  |   |  (      __/  |     |    (   |  |  |   |  |    |   | 
#  \__, | \__, | _|  _|     \__,_| _|  _| \___| \___| _|    \__| \__,_| _| _|  _| \__| \__, | 
#  |___/  |___/                                                                        ____/  
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
from array import array;

class ggHUncertaintyMaker(TreeCloner) :
    def __init__(self) :
       pass

    def help(self) :
        return '''ggH 2017 uncertainty matrix'''

    def addOptions(self,parser) :
        description = self.help()
        group = optparse.OptionGroup(parser,self.label, description)
        group.add_option('-c', '--cmssw', dest='cmssw', help='cmssw version (naming convention may change)', default='763', type='string')
        parser.add_option_group(group)
        return group

    def checkOptions(self,opts) :
        self.cmssw = opts.cmssw
        print " cmssw =", self.cmssw

    def process(self,**kwargs) :
        tree   = kwargs['tree']
        input  = kwargs['input']
        output = kwargs['output']

        self.connect(tree,input)

        nentries = self.itree.GetEntries()
        print ' - Input entries:', nentries 
        savedentries = 0

        # Create branches for otree, the ones that will be modified
        self.uncertaintyVariables = [ 'ggH_mu', 'ggH_res', 'ggH_mig01', 'ggH_mig12', 'ggH_pT60', 'ggH_pT120', 'ggH_VBF2j', 'ggH_VBF3j', 'ggH_qmtop' ]

        # Clone the tree with new branches added
        self.clone(output, self.uncertaintyVariables)
      
        # Now actually connect the branches
        ggH_mu    = numpy.ones(1, dtype=numpy.float32)
        ggH_res   = numpy.ones(1, dtype=numpy.float32)
        ggH_mig01 = numpy.ones(1, dtype=numpy.float32)
        ggH_mig12 = numpy.ones(1, dtype=numpy.float32)
        ggH_pT60  = numpy.ones(1, dtype=numpy.float32)
        ggH_pT120 = numpy.ones(1, dtype=numpy.float32)
        ggH_VBF2j = numpy.ones(1, dtype=numpy.float32)
        ggH_VBF3j = numpy.ones(1, dtype=numpy.float32)
        ggH_qmtop = numpy.ones(1, dtype=numpy.float32)
       
        self.otree.Branch('ggH_mu',     ggH_mu,    'ggH_mu/F')
        self.otree.Branch('ggH_res',    ggH_res,   'ggH_res/F')
        self.otree.Branch('ggH_mig01',  ggH_mig01, 'ggH_mig01/F')
        self.otree.Branch('ggH_mig12',  ggH_mig12, 'ggH_mig12/F')
        self.otree.Branch('ggH_pT60',   ggH_pT60,  'ggH_pT60/F')
        self.otree.Branch('ggH_pT120',  ggH_pT120, 'ggH_pT120/F')
        self.otree.Branch('ggH_VBF2j',  ggH_VBF2j, 'ggH_VBF2j/F')
        self.otree.Branch('ggH_VBF3j',  ggH_VBF3j, 'ggH_VBF3j/F')
        self.otree.Branch('ggH_qmtop',  ggH_qmtop, 'ggH_qmtop/F')

        # Input tree  
        itree = self.itree

        cmssw_base = os.getenv('CMSSW_BASE')
        try:
            ROOT.gROOT.LoadMacro(cmssw_base+'/src/LatinoAnalysis/Gardener/python/variables/ggHUncertainty.C+g')
        except RuntimeError:
            ROOT.gROOT.LoadMacro(cmssw_base+'/src/LatinoAnalysis/Gardener/python/variables/ggHUncertainty.C++g')
        #----------------------------------------------------------------------------------------------------

        ggHUncertainty = ROOT.ggHUncertainty()

 
        #-----------------------------------------------------------------------
        print ' - Starting event loop'
        step = 500

        for i in xrange(nentries) :
          itree.GetEntry(i)

          ggH_mu    [0] = 1.
          ggH_res   [0] = 1.
          ggH_mig01 [0] = 1.
          ggH_mig12 [0] = 1.
          ggH_VBF2j [0] = 1.
          ggH_VBF3j [0] = 1.
          ggH_pT60  [0] = 1.
          ggH_pT120 [0] = 1.
          ggH_qmtop [0] = 1.
      
          Njets30 = 0.
          for ijet in range(itree.std_vector_partonGen_pt.size()) :
            if itree.std_vector_partonGen_pt[ijet] > 30 :
              Njets30 += 1
          
      
          allUnc = ggHUncertainty.qcd_ggF_uncertSF_2017 (int(Njets30), itree.HTXS_ptHiggs, int(itree.HTXS_stage1_pTjet30GeV))

          ggH_mu    [0] = allUnc[0]
          ggH_res   [0] = allUnc[1]
          ggH_mig01 [0] = allUnc[2]
          ggH_mig12 [0] = allUnc[3]
          ggH_VBF2j [0] = allUnc[4]
          ggH_VBF3j [0] = allUnc[5]
          ggH_pT60  [0] = allUnc[6]
          ggH_pT120 [0] = allUnc[7]
          ggH_qmtop [0] = allUnc[8]


          
          if (i > 0 and i%step == 0.):
                print i,'events processed ::', nentries, ' ggH_mu:', ggH_mu[0], " int(Njets30): ", int(Njets30) , "  itree.HTXS_ptHiggs: ", itree.HTXS_ptHiggs, "  int(itree.HTXS_stage1_pTjet30GeV): ", int(itree.HTXS_stage1_pTjet30GeV)
                
                
      
          self.otree.Fill()
          savedentries+=1
          
        self.disconnect()
        print ' - Event loop completed'
        print ' - Saved entries:', savedentries
