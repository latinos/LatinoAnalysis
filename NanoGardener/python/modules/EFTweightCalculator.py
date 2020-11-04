#
#
#
#    ____|  ____| __ __|                     _)         |      |         
#    __|    |        |       \ \  \   /  _ \  |   _` |  __ \   __|   __| 
#    |      __|      |        \ \  \ /   __/  |  (   |  | | |  |   \__ \ 
#   _____| _|       _|         \_/\_/  \___| _| \__, | _| |_| \__| ____/ 
#                                               |___/                    
#  
#
#



import ROOT
ROOT.PyConfig.IgnoreCommandLineOptions = True

from PhysicsTools.NanoAODTools.postprocessing.framework.datamodel import Collection 
from PhysicsTools.NanoAODTools.postprocessing.framework.eventloop import Module
from PhysicsTools.NanoAODTools.postprocessing.modules.common.collectionMerger import collectionMerger
from LatinoAnalysis.NanoGardener.framework.BranchMapping import mappedOutputTree, mappedEvent

import os.path


class EFTweightCalculator(Module):
    def __init__(self, branch_map=''):

        # change this part into correct path structure... 
        cmssw_base = os.getenv('CMSSW_BASE')
        #try:
            #ROOT.gROOT.LoadMacro(cmssw_base+'/src/LatinoAnalysis/Gardener/python/variables/WWVar.C+g')
        #except RuntimeError:
            #ROOT.gROOT.LoadMacro(cmssw_base+'/src/LatinoAnalysis/Gardener/python/variables/WWVar.C++g')

        self._branch_map = branch_map
                
    def beginJob(self):
        pass

    def endJob(self):
        pass

    def beginFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
      
        self.out = mappedOutputTree(wrappedOutputTree, mapname=self._branch_map)
        self.newbranches = [
           'intWeight',
           'bsmWeight'
          ]
        
        for nameBranches in self.newbranches :
          self.out.branch(nameBranches  ,  "F");

    def endFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        pass

    def __init__(self, cmssw, CF_cfg = 'LatinoAnalysis/NanoGardener/python/data/configuration_positions_cfg.py'):

        print "initialize"
        

    def analyze(self, event):
        """process event, return True (go to next module) or False (fail, go to next event)"""

        event = mappedEvent(event, mapname=self._branch_map)

        LHEReweightingWeight = Collection(event, "LHEReweightingWeight")

        #leptons = electrons
        nLHEReweightingWeight = len(LHEReweightingWeight)

        print "nLHEReweightingWeight = ", nLHEReweightingWeight
        #LHEReweightingWeight[0]

        positions = {
          'x1' : 1.0,
          'x2' : -1.0,
          'index1' : 1,   # index of LHEReweightingWeight for x1
          'index2' : 2,   # index of LHEReweightingWeight for x2  
          }

        #x1 = 1.0
        #x2 = -1.0
        #y1 = 1.2345
        #y2 = 2.3456

        x1 = positions['x1']
        x2 = positions['x2']
        y1 = event.LHEReweightingWeight [ positions['index1'] ]
        y2 = event.LHEReweightingWeight [ positions['index2'] ]
        
#
# Int =  ( y1 x2**2 - y2 x1**2 ) / ( x1 x2 (x2 - x1) ) - Y[0] * ( x2 + x1 ) / ( x1 x2 )
#
# Quad = ( x1 y2  - x2 y1 ) / ( x1 x2 (x2 - x1) ) + Y[0] / ( x1 x2 )
#
       
#
# to be saved: Int:  ( y1 x2**2 - y2 x1**2 ) / ( x1 x2 (x2 - x1) ) 
#
# to be saved:  Quad: ( x1 y2  - x2 y1 ) / ( x1 x2 (x2 - x1) ) 
#

        self.out.fillBranch( "intWeight" ,  ( y1 * x2 * x2 - y2 * x1 * x1 ) / ( x1 * x2 * (x2 - x1) ) )
        self.out.fillBranch( "bsmWeight" ,  ( x1 * y2  - x2 * y1 )          / ( x1 * x2 * (x2 - x1) ) )

        #for nameBranches in self.newbranches :
          #self.out.fillBranch(nameBranches  ,  getattr(WW, nameBranches)())

#
# To be done: 
#    - perform parabola fit
#
#

  
        return True






