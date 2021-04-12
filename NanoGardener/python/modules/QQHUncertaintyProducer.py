import ROOT
ROOT.PyConfig.IgnoreCommandLineOptions = True

import os

from PhysicsTools.NanoAODTools.postprocessing.framework.datamodel import Collection 
from PhysicsTools.NanoAODTools.postprocessing.framework.eventloop import Module

class QQHUncertaintyProducer(Module):
    def __init__(self):
        self.uncertaintyVariables = [ 
          "qqH_YIELD",
          "qqH_PTH200",
          "qqH_Mjj60",
          "qqH_Mjj120",
          "qqH_Mjj350",
          "qqH_Mjj700",
          "qqH_Mjj1000",
          "qqH_Mjj1500",
          "qqH_PTH25",
          "qqH_JET01",
          "qqH_EWK",
         ]
        cmssw_base = os.getenv('CMSSW_BASE')
        try:
            ROOT.gROOT.LoadMacro(cmssw_base+'/src/LatinoAnalysis/NanoGardener/python/modules/qqhuncertainty.cc+g')
        except RuntimeError:
            ROOT.gROOT.LoadMacro(cmssw_base+'/src/LatinoAnalysis/NanoGardener/python/modules/qqhuncertainty.cc++g')
        #----------------------------------------------------------------------------------------------------

    
  
    def beginJob(self):
        pass
    def endJob(self):
        pass
    def beginFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        self.out = wrappedOutputTree
        for unc in self.uncertaintyVariables:
          self.out.branch(unc,     "F")
    

    def endFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        pass
    def analyze(self, event):
        """process event, return True (go to next module) or False (fail, go to next event)"""
        
        allUnc = ROOT.get_all_qqH_uncertainties(int(event.HTXS_stage1_1_fine_cat_pTjet30GeV))
        
        for iunc,unc in enumerate(self.uncertaintyVariables):
          self.out.fillBranch(unc, allUnc[iunc])
        return True

