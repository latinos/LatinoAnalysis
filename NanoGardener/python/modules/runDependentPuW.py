import ROOT
ROOT.PyConfig.IgnoreCommandLineOptions = True
import re
import os

from PhysicsTools.NanoAODTools.postprocessing.framework.datamodel import Collection 
from PhysicsTools.NanoAODTools.postprocessing.framework.eventloop import Module

class runDependentPuW(Module):
    def __init__(self , cmssw, PUWeight_cfg = 'LatinoAnalysis/NanoGardener/python/data/PUWeight_cfg.py' ):
        self.cmssw = cmssw
        cmssw_base = os.getenv('CMSSW_BASE')
        var = {}
        execfile(cmssw_base+'/src/'+PUWeight_cfg, var)
        self.PUWeightCfg = var['PUCfg'][self.cmssw]

        print self.PUWeightCfg

    def beginJob(self):
        pass
    def endJob(self):
        pass
    def beginFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        pass 
    def endFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        pass
    def analyze(self, event):
        """process event, return True (go to next module) or False (fail, go to next event)"""
        return True

