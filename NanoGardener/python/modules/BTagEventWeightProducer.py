import ROOT
ROOT.PyConfig.IgnoreCommandLineOptions = True

from PhysicsTools.NanoAODTools.postprocessing.framework.datamodel import Collection 
from PhysicsTools.NanoAODTools.postprocessing.framework.eventloop import Module

class BTagEventWeightProducer(Module):
    def __init__(self, collection="Lepton"):
        self.collection = collection
    def beginJob(self):
        pass
    def endJob(self):
        pass

    def beginFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        self.out = wrappedOutputTree
        self.systs_shape_corr = []
        for syst in [ 'jes',
                      'lf', 'hf',
                      'hfstats1', 'hfstats2',
                      'lfstats1', 'lfstats2',
                      'cferr1', 'cferr2' ]:
            self.systs_shape_corr.append("up_%s" % syst)
            self.systs_shape_corr.append("down_%s" % syst)
        self.central_and_systs_shape_corr = [ "central" ]
        self.central_and_systs_shape_corr.extend(self.systs_shape_corr)
        self.branchNames_central_and_systs_shape_corr={}
        for central_or_syst in self.central_and_systs_shape_corr:
            if central_or_syst == "central":
                self.branchNames_central_and_systs_shape_corr[central_or_syst] = "btagWeight"
            else:
                self.branchNames_central_and_systs_shape_corr[central_or_syst] = "btagWeight_%s" % central_or_syst
            self.out.branch(self.branchNames_central_and_systs_shape_corr[central_or_syst],'F')     

                
    
    def endFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        pass

    def analyze(self, event):
        """process event, return True (go to next module) or False (fail, go to next event)"""
        for central_or_syst in self.central_and_systs_shape_corr:
          if central_or_syst == "central":
            weight = 1.
            for i in range(event.nCleanJet):
              #print event.nCleanJet , event.nJet , i , event.CleanJet_jetIdx[i]
              #weight = weight*event.Jet_btagSF_shape[event.CleanJet_jetIdx[i]]
              idx = event.CleanJet_jetIdx[i]
              weight *= event.Jet_btagSF_shape[idx]
          else:
            weight=1.
            for i in range(event.nCleanJet):
              weight = weight*getattr(event, "Jet_btagSF_shape_%s" % central_or_syst)[event.CleanJet_jetIdx[i]]
          self.out.fillBranch(self.branchNames_central_and_systs_shape_corr[central_or_syst], weight)   
        
        return True

