import ROOT
ROOT.PyConfig.IgnoreCommandLineOptions = True

from PhysicsTools.NanoAODTools.postprocessing.framework.datamodel import Collection 
from PhysicsTools.NanoAODTools.postprocessing.framework.eventloop import Module

class TriggerObjectMatchProducer2017(Module):
    def __init__(self, collection="Muon"):
        self.collection = collection
    def beginJob(self):
        pass
    def endJob(self):
        pass

    def beginFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        self.out = wrappedOutputTree
        self.out.branch("Muon_isTriggMatched", "O", lenVar="nMuon")      

    def endFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        pass

    def analyze(self, event):
        """process event, return True (go to next module) or False (fail, go to next event)"""
        muons = Collection(event, self.collection)
        trigObjects = Collection(event, "TrigObj") 
        HLT_IsoMu27 = getattr(event, "HLT_IsoMu27")
        nTrigObj = getattr(event, "nTrigObj")

        cont = 0
        lepCont = 0
        lep_matched = []
        muon_isMatched = 0
        # Loop over all leptons if the event pass HLT selection
        for muon in muons :
            if muon_isMatched == 0:
                if (HLT_IsoMu27 == 0) : 
                    # print 'matching value: ' + str(muon_isMatched)
                    lep_matched.append(muon_isMatched)
                    continue
                #print '-------------'
                #print 'Muon number ' + str(lepCont)
                if abs(muon.pdgId) != 13 : 
                    #print 'matching value: ' + str(muon_isMatched)
                    lep_matched.append(muon_isMatched)
                    continue
                lepp4 = ROOT.TLorentzVector()
                lepp4.SetPtEtaPhiM(muon.pt, muon.eta, muon.phi, 0)
                lepCont = lepCont + 1
                # Loop over all trigger objects
                for trigObject in trigObjects:
                    if trigObject.id != 13 : 
                        #print 'matching value: ' + str(muon_isMatched)
                        lep_matched.append(muon_isMatched)
                        continue
                    trigObjp4 = ROOT.TLorentzVector()
                    trigObjp4.SetPtEtaPhiM(trigObject.pt, trigObject.eta, trigObject.phi, 0)
                    cont = cont + 1
                    if abs(muon.pdgId) != 13 or trigObjp4.DeltaR(lepp4) > 0.1 : 
                        #print 'matching value: ' + str(muon_isMatched)
                        lep_matched.append(muon_isMatched)
                        continue
                    #print (trigObjp4.DeltaR(lepp4))
                    #print 'Filter bit:' + str(trigObject.filterBits)
                    
                    # from https://cms-nanoaod-integration.web.cern.ch/integration/master-102X/mc102X_doc.html#MET
                    # muons trigger bits: Iso = 2, 1Mu = 8
                    if (HLT_IsoMu27 == 0 or (trigObject.filterBits & 10 != 10)) : 
                        #print 'matching value: ' + str(muon_isMatched)
                        lep_matched.append(muon_isMatched)
                        continue
                    #print 'This is matched with trigObj ' + str(cont)
                    muon_isMatched = 1
                    #print 'matching value: ' + str(muon_isMatched)
                    lep_matched.append(muon_isMatched)
                    break
            # one trigger-matched muon per event is enough
            elif muon_isMatched == 1:
                #print 'matching value: 0' #+ str(muon_isMatched)
                lep_matched.append(0)

        outTriggMatched = []
        matchCont = 0
        #print 'Event summary:'
        for muon in muons:
            outTriggMatched.append(lep_matched[matchCont])    
            #print lep_matched[matchCont]
            matchCont = matchCont + 1
        self.out.fillBranch("Muon_isTriggMatched", outTriggMatched)
        return True
