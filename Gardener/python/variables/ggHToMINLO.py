#
#
#
#       _ \    _ \ \ \        /  |   |  ____|   ___|      |                \  | _ _|   \  |  |       _ \  
#      |   |  |   | \ \  \   /   |   |  __|    |          __|   _ \       |\/ |   |     \ |  |      |   | 
#      ___/   |   |  \ \  \ /    ___ |  |      |   |      |    (   |      |   |   |   |\  |  |      |   | 
#     _|     \___/    \_/\_/    _|  _| _____| \____|     \__| \___/      _|  _| ___| _| \_| _____| \___/  
#                                                                                                         
#    
#
#    See https://twiki.cern.ch/twiki/bin/viewauth/CMS/HiggsWG/SignalModelingTools
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

class ggHtoMINLOMaker(TreeCloner) :
    def __init__(self) :
       pass

    def help(self) :
        return '''ggH reweight to MINLO'''

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
        self.weightVariables = [ 'weight2MINLO' ]

        # Clone the tree with new branches added
        self.clone(output, self.weightVariables)
      
        # Now actually connect the branches
        weight2MINLO    = numpy.ones(1, dtype=numpy.float32)
 
        self.otree.Branch('weight2MINLO',     weight2MINLO,    'weight2MINLO/F')
       
        # Input tree  
        itree = self.itree

        cmssw_base = os.getenv('CMSSW_BASE')
        
        #----------------------------------------------------------------------------------------------------

        nameFileWithWeights = cmssw_base+'/src/LatinoAnalysis/Gardener/python/data/powheg2minlo/NNLOPS_reweight.root'
        fileWithWeights = self._openRootFile(nameFileWithWeights)  
        graph_weights_0jet = self._getRootObj(fileWithWeights, 'gr_NNLOPSratio_pt_powheg_0jet')
        graph_weights_1jet = self._getRootObj(fileWithWeights, 'gr_NNLOPSratio_pt_powheg_1jet')
        graph_weights_2jet = self._getRootObj(fileWithWeights, 'gr_NNLOPSratio_pt_powheg_2jet')
        graph_weights_3jet = self._getRootObj(fileWithWeights, 'gr_NNLOPSratio_pt_powheg_3jet')


 
        #-----------------------------------------------------------------------
        print ' - Starting event loop'
        step = 500

        for i in xrange(nentries) :
          itree.GetEntry(i)

          weight2MINLO[0] = 1.
          
          #Njets30 = 0.
          #for ijet in range(itree.std_vector_partonGen_pt.size()) :
            #if itree.std_vector_partonGen_pt[ijet] > 30 :
              #Njets30 += 1
          
          Njets30_HTXS = 0.
          for ijet in range(itree.std_vector_HTXS_ptjet25GeV.size()) :
            if itree.std_vector_HTXS_ptjet25GeV[ijet] > 30 :
              Njets30_HTXS += 1

          #if Njets30_HTXS != Njets30 :
            #print " Njets30_HTXS = ", Njets30_HTXS, " ::  Njets30 = ", Njets30
            
          
          
          if (Njets30_HTXS==0):
            weight2MINLO[0] = graph_weights_0jet.Eval( min(itree.HTXS_ptHiggs,125.0) )
          elif (Njets30_HTXS==1):
            weight2MINLO[0] = graph_weights_1jet.Eval( min(itree.HTXS_ptHiggs,625.0) )
          elif (Njets30_HTXS==2):
            weight2MINLO[0] = graph_weights_2jet.Eval( min(itree.HTXS_ptHiggs,800.0) )
          elif (Njets30_HTXS>=3):
            weight2MINLO[0] = graph_weights_3jet.Eval( min(itree.HTXS_ptHiggs,925.0) )
          else:
            weight2MINLO[0] = 1.0

          #print " Njets30_HTXS = " , Njets30_HTXS , " --> weight2MINLO[0] = ", weight2MINLO[0]
       
          self.otree.Fill()
          savedentries+=1
          
        self.disconnect()
        print ' - Event loop completed'
        print ' - Saved entries:', savedentries
