import ROOT
ROOT.PyConfig.IgnoreCommandLineOptions = True
import re
import os

from PhysicsTools.NanoAODTools.postprocessing.framework.datamodel import Collection 
from PhysicsTools.NanoAODTools.postprocessing.framework.eventloop import Module

class EmbedVeto(Module):
    def __init__(self):
        pass

    def beginJob(self):
        pass

    def endJob(self):
        pass

    def beginFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        self.out = wrappedOutputTree
        self.out.branch("embed_tautauveto", "F")

    def endFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        pass

    def analyze(self, event):
        """process event, return True (go to next module) or False (fail, go to next event)"""

        taus = 0
        for lep in range(2):
          pdgid = abs(getattr(event, 'Lepton_pdgId')[lep])
          if pdgid == 11:
            idx = getattr(event, 'Lepton_electronIdx')[lep]
            genflav = ord(getattr(event, 'Electron_genPartFlav')[idx])
          elif pdgid == 13:
            idx = getattr(event, 'Lepton_muonIdx')[lep]
            genflav = ord(getattr(event, 'Muon_genPartFlav')[idx])
          if genflav == 15: taus += 1

        if taus == 2:
          self.out.fillBranch("embed_tautauveto", 0.0)
        else:
          self.out.fillBranch("embed_tautauveto", 1.0)
        return True

