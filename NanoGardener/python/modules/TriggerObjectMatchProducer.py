import ROOT
ROOT.PyConfig.IgnoreCommandLineOptions = True

from PhysicsTools.NanoAODTools.postprocessing.framework.datamodel import Collection 
from PhysicsTools.NanoAODTools.postprocessing.framework.eventloop import Module

class TriggerObjectMatchProducer(Module):
    def __init__(self, collection="Lepton"):
        self.collection = collection
    def beginJob(self):
        pass
    def endJob(self):
        pass

    def beginFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        self.out = wrappedOutputTree
        #        self.out.branch("Lepton_genmatched", "O", lenVar="nLepton")
        #        self.out.branch("Lepton_promptgenmatched", "O", lenVar="nLepton")
        self.out.branch("Lepton_triggmatched", "O", lenVar="nLepton")        

    def endFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        pass

    def analyze(self, event):
        """process event, return True (go to next module) or False (fail, go to next event)"""
        leptons = Collection(event, self.collection)
        trigObjects = Collection(event, "TrigObj") 
        HLT_IsoMu24 = getattr(event, "HLT_IsoMu24")
        for lepton  in leptons:
          lepp4 = ROOT.TLorentzVector()
          lepp4.SetPtEtaPhiM(lepton.pt, lepton.eta, lepton.phi, 0)
          lepton.isMatched = False
          for trigObject in trigObjects:
            trigObjp4 = ROOT.TLorentzVector()
            trigObjp4.SetPtEtaPhiM(trigObject.pt, trigObject.eta, trigObject.phi, 0)
            # print (trigObjp4.DeltaR(lepp4))
            # print trigObject.id
            ##            if ( abs(trigObject.id) == 13 ) and trigObjp4.DeltaR(lepp4) < 0.3 :
            if trigObjp4.DeltaR(lepp4) < 0.3:  
                lepton.isMatched = True
                # print 'True!'
                # print trigObject.id
                # print str(trigObject.pt)  + ',' + str(lepton.pt)
                # print str(trigObject.phi) + ',' + str(lepton.phi)
                # print str(trigObject.eta) + ',' + str(lepton.eta)
                # print HLT_IsoMu24
                # print trigObject.filterBits
                print ''

        outTriggMatched = []
        for lepton in leptons:
            outTriggMatched.append(lepton.isMatched)    
        self.out.fillBranch("Lepton_triggmatched", outTriggMatched)
        return True

