import ROOT
ROOT.PyConfig.IgnoreCommandLineOptions = True
import re
import os

from PhysicsTools.NanoAODTools.postprocessing.framework.datamodel import Collection 
from PhysicsTools.NanoAODTools.postprocessing.framework.eventloop import Module

class GenericFormulaAdder(Module):
    def __init__(self,configfile="data/formulasToAdd_Data.py"):
      cmssw_base = os.getenv('CMSSW_BASE') 
      formulasFile_path = cmssw_base+'/src/LatinoAnalysis/NanoGardener/python/'+configfile
      if os.path.exists(formulasFile_path) :
        handle = open(formulasFile_path,'r')
        exec(handle)
        handle.close()
        setattr(self, "formulas", formulas)
      else:
        raise RuntimeError("cannot find file", formulasFile_path)
    def beginJob(self):
        pass
    def endJob(self):
        pass
    def beginFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        self.out = wrappedOutputTree
        self.itree = inputTree
        for key in self.formulas.keys():
          self.formulas[key] = eval('lambda event:'+self.formulas[key])
          self.out.branch(key,  'F');
    
    def endFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        pass
    
    def analyze(self, event):
        """process event, return True (go to next module) or False (fail, go to next event)"""
        for key in self.formulas.keys():
          self.out.fillBranch(key, self.formulas[key](event))

        return True

