import ROOT
ROOT.PyConfig.IgnoreCommandLineOptions = True
import copy

from PhysicsTools.NanoAODTools.postprocessing.framework.datamodel import Collection 
from PhysicsTools.NanoAODTools.postprocessing.framework.eventloop import Module

class DressedLeptonProducer(Module):
    def __init__(self, cone):
        self.cone = cone
    def beginJob(self):
        pass
    def endJob(self):
        pass

    def beginFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        self.out = wrappedOutputTree
        self.ivars = ["pdgId"]
        self.fvars = ["pt", "eta", "phi", "mass"]
        for ivar in self.ivars:
          self.out.branch("DressedLepton_"+ivar, "I", lenVar="nDressedLepton")
        for fvar in self.fvars:
          self.out.branch("DressedLepton_"+fvar, "F", lenVar="nDressedLepton")
        self.allQuantities = self.ivars + self.fvars
    
    def endFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        pass

    def analyze(self, event):
        """process event, return True (go to next module) or False (fail, go to next event)"""
        genPhotons = Collection(event, "PhotonGen")
        genLeptons = Collection(event, "LeptonGen")
        dressedLeptons = Collection(event, "LeptonGen") 
        #Loop over photons, find closest lepton, if it is within cone, add it to the lepton 
        for photon  in genPhotons:
          photonp4 = ROOT.TLorentzVector()
          photonp4.SetPtEtaPhiM(photon.pt, photon.eta, photon.phi, 0)
          minDR = 99999.
          closestLepton = -1.
          for il,genLepton in enumerate(genLeptons):
            dr = genLepton.p4().DeltaR(photonp4)
            if ( abs(genLepton.pdgId) == 11 or abs(genLepton.pdgId) == 13 ) and \
                 genLepton.status == 1 and \
                 dr < minDR :
              minDR = dr
              closestLepton = il
          if minDR < self.cone:
            newp4 = dressedLeptons[il].p4()+photonp4  
            dressedLeptons[il].pt=newp4.Pt()
            dressedLeptons[il].eta=newp4.Eta()
            dressedLeptons[il].phi=newp4.Phi()
            dressedLeptons[il].mass=newp4.M()

        for branch in self.allQuantities:
          out = []
          for obj in dressedLeptons:
            out.append(getattr(obj, branch))
          self.out.fillBranch("DressedLepton_"+branch, out)
 
        return True

