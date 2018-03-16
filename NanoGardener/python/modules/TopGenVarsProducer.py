import ROOT
ROOT.PyConfig.IgnoreCommandLineOptions = True

from PhysicsTools.NanoAODTools.postprocessing.framework.datamodel import Collection 
from PhysicsTools.NanoAODTools.postprocessing.framework.eventloop import Module

class TopGenVarsProducer(Module):
    def __init__(self):
        pass
    def beginJob(self):
        pass
    def endJob(self):
        pass
    def beginFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        self.out = wrappedOutputTree
        self.out.branch("topGenPt"  ,  "F");
        self.out.branch("topGenEta" ,  "F");
        self.out.branch("topGenPhi" ,  "F");
        self.out.branch("topGenMass",  "F");
        self.out.branch("antitopGenPt"  ,  "F");
        self.out.branch("antitopGenEta" ,  "F");
        self.out.branch("antitopGenPhi" ,  "F");
        self.out.branch("antitopGenMass",  "F");
    def endFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        pass
    def analyze(self, event):
        """process event, return True (go to next module) or False (fail, go to next event)"""
        genParticles = Collection(event, "GenPart")
        for particle  in genParticles :
          if particle.pdgId == 6 and (particle.statusFlags >> 13 & 1):
            self.out.fillBranch("topGenPt",  particle.pt)
            self.out.fillBranch("topGenEta", particle.eta)
            self.out.fillBranch("topGenPhi", particle.phi)
            self.out.fillBranch("topGenMass", particle.mass)
          elif particle.pdgId == -6 and (particle.statusFlags >> 13 & 1):  
            self.out.fillBranch("antitopGenPt",  particle.pt)
            self.out.fillBranch("antitopGenEta", particle.eta)
            self.out.fillBranch("antitopGenPhi", particle.phi)
            self.out.fillBranch("antitopGenMass", particle.mass) 
        return True


# define modules using the syntax 'name = lambda : constructor' to avoid having them loaded when not needed

topGenVarsProducer = lambda : TopGenVarsProducer() 
 
