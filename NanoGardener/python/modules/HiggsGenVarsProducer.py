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
        self.out.branch("genVPt"      ,  "F");
    def endFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        pass
    def getParentID(self,particle,genParticles):
        if particle.genPartIdxMother is -1: #No parent in record, return ID of original particle
            return particle.pdgId
        elif genParticles[particle.genPartIdxMother].pdgId is particle.pdgId: #'Parent' is self, keep iterating
            return self.getParentID(genParticles[particle.genPartIdxMother],genParticles)
        else: #Found physical parent
            return genParticles[particle.genPartIdxMother].pdgId
    def analyze(self, event):
        """process event, return True (go to next module) or False (fail, go to next event)"""
        genParticles = Collection(event, "GenPart")
        for particle  in genParticles : #Loop for Higgs
          if particle.pdgId == 25 and (particle.statusFlags >> 13 & 1):
            self.out.fillBranch("higgsGenPt", particle.pt)
            self.out.fillBranch("higgsGenEta", particle.eta)
            self.out.fillBranch("higgsGenPhi", particle.phi)
            self.out.fillBranch("higgsGenMass", particle.mass)
            break
        else: # = pdgId 25 not found
          self.out.fillBranch("higgsGenPt", -1.)
          self.out.fillBranch("higgsGenEta", 0.)
          self.out.fillBranch("higgsGenPhi", 0.)
          self.out.fillBranch("higgsGenMass", -1.)
        for particle in genParticles : #Loop for V
            if (abs(particle.pdgId) == 23 or abs(particle.pdgId) == 24) and (particle.statusFlags >> 13 & 1) and self.getParentID(particle,genParticles) != 25 :
                self.out.fillBranch("genVPt", particle.pt)
                break
        else: # V not found
          self.out.fillBranch("genVPt", -1.)

        return True
