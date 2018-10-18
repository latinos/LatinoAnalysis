import ROOT
ROOT.PyConfig.IgnoreCommandLineOptions = True
import re

from PhysicsTools.NanoAODTools.postprocessing.framework.datamodel import Collection 
from PhysicsTools.NanoAODTools.postprocessing.framework.eventloop import Module

class Grafter(Module):
    def __init__(self,variables=[]):
        self.regex = re.compile("([a-zA-Z0-9]*)/([FID])=(.*)")
        self.variables = variables
        self.variablesDecoded = {} 
    def beginJob(self):
        pass
    def endJob(self):
        pass
    def beginFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        self.out = wrappedOutputTree
        self.itree = inputTree
        for s in self.variables:
          r = self.regex.match(s)
          if not r:
              raise RuntimeError('Malformed option '+s)
          name=r.group(1)
          type=r.group(2)
          formula=r.group(3)
          self.variablesDecoded[name] = ROOT.TTreeFormula(name,formula, self.itree)
          self.out.branch(name,  type);
    
    def endFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        pass
    
    def analyze(self, event):
        """process event, return True (go to next module) or False (fail, go to next event)"""

        for var  in self.variablesDecoded.keys():
           self.out.fillBranch(var, self.variablesDecoded[var].EvalInstance())

        return True

