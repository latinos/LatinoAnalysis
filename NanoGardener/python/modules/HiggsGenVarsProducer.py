import ROOT
ROOT.PyConfig.IgnoreCommandLineOptions = True

from PhysicsTools.NanoAODTools.postprocessing.framework.datamodel import Collection 
from PhysicsTools.NanoAODTools.postprocessing.framework.eventloop import Module

class HiggsGenVarsProducer(Module):
    def __init__(self):
        pass
    def beginJob(self):
        pass
    def endJob(self):
        pass
    def beginFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        self.out = wrappedOutputTree
        self.out.branch("higgsGenPt"  ,  "F");
        self.out.branch("higgsGenEta" ,  "F");
        self.out.branch("higgsGenPhi" ,  "F");
        self.out.branch("higgsGenMass",  "F");
    def endFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        pass
    def analyze(self, event):
        """process event, return True (go to next module) or False (fail, go to next event)"""
        genParticles = Collection(event, "GenPart")
        for particle  in genParticles :
          if particle.pdgId == 25 and (particle.statusFlags >> 13 & 1):
            self.out.fillBranch("higgsGenPt", particle.pt)
            self.out.fillBranch("higgsGenEta", particle.eta)
            self.out.fillBranch("higgsGenPhi", particle.phi)
            self.out.fillBranch("higgsGenMass", particle.mass)
        return True

