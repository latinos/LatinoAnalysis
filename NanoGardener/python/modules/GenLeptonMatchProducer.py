import ROOT
ROOT.PyConfig.IgnoreCommandLineOptions = True

from PhysicsTools.NanoAODTools.postprocessing.framework.datamodel import Collection 
from PhysicsTools.NanoAODTools.postprocessing.framework.eventloop import Module

class GenLeptonMatchProducer(Module):
    def __init__(self, collection="Lepton"):
        self.collection = collection
    def beginJob(self):
        pass
    def endJob(self):
        pass

    def beginFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        self.out = wrappedOutputTree
        self.out.branch("Lepton_genmatched", "O", lenVar="nLepton")
        self.out.branch("Lepton_promptgenmatched", "O", lenVar="nLepton")
    
    def endFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        pass

    def analyze(self, event):
        """process event, return True (go to next module) or False (fail, go to next event)"""
        leptons = Collection(event, self.collection)
        genLeptons = Collection(event, "LeptonGen")
        for lepton  in leptons:
          lepp4 = ROOT.TLorentzVector()
          lepp4.SetPtEtaPhiM(lepton.pt, lepton.eta, lepton.phi, 0)
          lepton.isMatched = False
          lepton.isPromptMatched = False
          for genLepton in genLeptons:
            if ( abs(genLepton.pdgId) == 11 or abs(genLepton.pdgId) == 13 ) and \
                 genLepton.status == 1 and \
                 genLepton.p4().DeltaR(lepp4) < 0.3 :
              lepton.isMatched = True
              if genLepton.isPrompt or genLepton.isDirectPromptTauDecayProduct:
                lepton.isPromptMatched = True
                
        outGenMatched = []
        outPromptGenMatched = []
        for lepton in leptons:
          outGenMatched.append(lepton.isMatched)    
          outPromptGenMatched.append(lepton.isPromptMatched)
        self.out.fillBranch("Lepton_genmatched", outGenMatched)
        self.out.fillBranch("Lepton_promptgenmatched", outPromptGenMatched)
        return True

