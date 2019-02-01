import ROOT
ROOT.PyConfig.IgnoreCommandLineOptions = True

import os

from PhysicsTools.NanoAODTools.postprocessing.framework.datamodel import Collection 
from PhysicsTools.NanoAODTools.postprocessing.framework.eventloop import Module

class GGHUncertaintyProducer(Module):
    def __init__(self):
        self.uncertaintyVariables = [ 'ggH_mu', 'ggH_res', 'ggH_mig01', 'ggH_mig12', 'ggH_pT60', 'ggH_pT120', 'ggH_VBF2j', 'ggH_VBF3j', 'ggH_qmtop' ]
        cmssw_base = os.getenv('CMSSW_BASE')
        try:
            ROOT.gROOT.LoadMacro(cmssw_base+'/src/LatinoAnalysis/Gardener/python/variables/ggHUncertainty.C+g')
        except RuntimeError:
            ROOT.gROOT.LoadMacro(cmssw_base+'/src/LatinoAnalysis/Gardener/python/variables/ggHUncertainty.C++g')
        #----------------------------------------------------------------------------------------------------

        self.ggHUncertainty = ROOT.ggHUncertainty()
    
  
    def beginJob(self):
        pass
    def endJob(self):
        pass
    def beginFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        self.out = wrappedOutputTree
        self.out.branch('ggH_mu',     "F")
        self.out.branch('ggH_res',    "F")
        self.out.branch('ggH_mig01',  "F")
        self.out.branch('ggH_mig12',  "F")
        self.out.branch('ggH_pT60',   "F")
        self.out.branch('ggH_pT120',  "F")
        self.out.branch('ggH_VBF2j',  "F")
        self.out.branch('ggH_VBF3j',  "F")
        self.out.branch('ggH_qmtop',  "F")
    

    def endFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        pass
    def analyze(self, event):
        """process event, return True (go to next module) or False (fail, go to next event)"""
        
        allUnc = self.ggHUncertainty.qcd_ggF_uncertSF_2017 (int(event.HTXS_njets30), 
                                                            event.HTXS_Higgs_pt, 
                                                            int(event.HTXS_stage_1_pTjet30))
          
        self.out.fillBranch("ggH_mu",    allUnc[0])
        self.out.fillBranch("ggH_res",   allUnc[1])
        self.out.fillBranch("ggH_mig01", allUnc[2])
        self.out.fillBranch("ggH_mig12", allUnc[3])
        self.out.fillBranch("ggH_pT60",  allUnc[4])
        self.out.fillBranch("ggH_pT120", allUnc[5])
        self.out.fillBranch("ggH_VBF2j", allUnc[6])
        self.out.fillBranch("ggH_VBF3j", allUnc[7])
        self.out.fillBranch("ggH_qmtop", allUnc[8])
        return True

