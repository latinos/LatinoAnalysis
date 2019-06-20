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
        toppt   = 0.
        topeta  = 0.
        topphi  = 0.
        topmass = 0.
        atoppt   = 0.
        atopeta  = 0.
        atopphi  = 0.
        atopmass = 0.   
        for particle  in genParticles :
          if particle.pdgId == 6 and (particle.statusFlags >> 13 & 1):
            toppt = particle.pt
            topeta = particle.eta
            topphi = particle.phi
            topmass = particle.mass
          elif particle.pdgId == -6 and (particle.statusFlags >> 13 & 1):  
            atoppt = particle.pt
            atopeta = particle.eta
            atopphi = particle.phi
            atopmass = particle.mass
        self.out.fillBranch("topGenPt",  toppt)
        self.out.fillBranch("topGenEta", topeta)
        self.out.fillBranch("topGenPhi", topphi)
        self.out.fillBranch("topGenMass", topmass)
        self.out.fillBranch("antitopGenPt",  atoppt)
        self.out.fillBranch("antitopGenEta", atopeta)
        self.out.fillBranch("antitopGenPhi", atopphi)
        self.out.fillBranch("antitopGenMass", atopmass)

            
        return True
