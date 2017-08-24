#
#
#       ___|                    _ \                        _)         |      |        |   |  |   |  |   | 
#      |       _ \  __ \       |   |   _ \ \ \  \   /  _ \  |   _` |  __ \   __|      |   |  |   |  |   | 
#      |   |   __/  |   |      __ <    __/  \ \  \ /   __/  |  (   |  | | |  |        ___ |  ___ |  ___ | 
#     \____| \___| _|  _|     _| \_\ \___|   \_/\_/  \___| _| \__, | _| |_| \__|     _|  _| _|  _| _|  _| 
#                                                             |___/                                       
#
#    
#
#    See https://indico.cern.ch/event/628841/contributions/2687185/attachments/1505951/2346737/Aug-09-VHBSM_Massironi.pdf
#    and links inside the slides
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

class genReweightHHHMaker(TreeCloner) :
    def __init__(self) :
       pass

    def help(self) :
        return '''Gen level reweight with HHH anomalous coupling'''

    def addOptions(self,parser) :
        description = self.help()
        group = optparse.OptionGroup(parser,self.label, description)
        group.add_option('-c', '--cmssw', dest='cmssw',   help='cmssw version (naming convention may change)', default='763', type='string')
        group.add_option('-g', '--productionkind',   dest='productionkind',  help='kind of production mechanism (wph, wpm, zh)', default='wph', type='string')
        parser.add_option_group(group)
        return group

    def checkOptions(self,opts) :
        self.cmssw = opts.cmssw
        print " cmssw =", self.cmssw
        
        self.productionkind = opts.productionkind
        print " productionkind =", self.productionkind
        
        

    def process(self,**kwargs) :
        tree   = kwargs['tree']
        input  = kwargs['input']
        output = kwargs['output']

        self.connect(tree,input)

        nentries = self.itree.GetEntries()
        print ' - Input entries:', nentries 
        savedentries = 0

        # Create branches for otree, the ones that will be modified
        self.weightVariables = [ 'weightHHH' ]

        # Clone the tree with new branches added
        self.clone(output, self.weightVariables)
      
        # Now actually connect the branches
        weightHHH    = numpy.ones(1, dtype=numpy.float32)
 
        self.otree.Branch('weightHHH',     weightHHH,    'weightHHH/F')
       
        # Input tree  
        itree = self.itree

        cmssw_base = os.getenv('CMSSW_BASE')
        
        #----------------------------------------------------------------------------------------------------

        nameFileWithWeights = ""
        if self.productionkind == "wph" :
          nameFileWithWeights = cmssw_base+'/src/LatinoAnalysis/Gardener/python/data/hhh/ratio.wp.root'
        elif self.productionkind == "wmh" :
          nameFileWithWeights = cmssw_base+'/src/LatinoAnalysis/Gardener/python/data/hhh/ratio.wm.root'
        elif self.productionkind == "zh" :
          nameFileWithWeights = cmssw_base+'/src/LatinoAnalysis/Gardener/python/data/hhh/ratio.z.root'
        
        fileWithWeights = self._openRootFile(nameFileWithWeights)  
        graph_weights = self._getRootObj(fileWithWeights, 'gr_ratio')
       

 
        #-----------------------------------------------------------------------
        print ' - Starting event loop'
        step = 500

        for i in xrange(nentries) :
          itree.GetEntry(i)

          weightHHH[0] = 1.
                   
          # itree.HTXS_ptHiggs
          # itree.higgsLHEpt
            
          weightHHH[0] = graph_weights.Eval( min(itree.higgsLHEpt,400) )
          
          self.otree.Fill()
          savedentries+=1
          
        self.disconnect()
        print ' - Event loop completed'
        print ' - Saved entries:', savedentries
