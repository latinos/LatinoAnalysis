import ROOT
ROOT.PyConfig.IgnoreCommandLineOptions = True
import re
import os

from PhysicsTools.NanoAODTools.postprocessing.framework.eventloop import Module
from PhysicsTools.NanoAODTools.postprocessing.framework.datamodel import Collection 
from LatinoAnalysis.NanoGardener.data.LeptonMaker_cfg import CleanJet_br, CleanJet_var 

class CopyCleanJet(Module):
    def __init__(self, newcollectionname="CleanJetCut", cuts=["pt<50","eta>2.65","eta<3.139"]):
    # Cuts work with "pt", "eta" and "phi"
    # Cutting on eta will actually cut on abs(eta)
        self.newcollectionname = newcollectionname
        self.cuts = cuts

    def beginJob(self):
        pass

    def endJob(self):
        pass

    def beginFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        self.out = wrappedOutputTree
        for typ in CleanJet_br:
            for var in CleanJet_br[typ]:
                if 'CleanJet_' in var:
                    var = self.newcollectionname + var[8:]
                    self.out.branch(var, typ, lenVar='n'+self.newcollectionname)
        CleanJet_var.append('jetIdx')

    def endFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        pass

    def analyze(self, event):
        """process event, return True (go to next module) or False (fail, go to next event)"""

        cleanjets = Collection(event,"CleanJet")
        ncleanjets = getattr(event, "nCleanJet")

        # Copy CleanJet collection
        jet_dict = {}
        for jv in CleanJet_var:
           jet_dict[jv] = [0]*ncleanjets

        for i in range(ncleanjets):
            for var in jet_dict:
                jet_dict[var][i] = getattr(event, "CleanJet_"+var)[i]

        # Apply additional cuts
        JetSatisfiesCut = [0]*ncleanjets
        for cut in self.cuts:
            cutparts = []
            for symbol in ["<", ">", "<=", ">=", "=="]:
                if symbol in cut:
                    cutparts = [cut.split(symbol)[0], symbol, cut.split(symbol)[1]]
                    break
            if cutparts == []:
                print "Error identifying cut",cut
                continue
            for i in range(ncleanjets):
                variable = "jet_dict[cutparts[0]][i]"
                if cutparts[0] == "eta": variable = "abs(" + variable + ")"
                if eval(variable + cutparts[1] + cutparts[2]): JetSatisfiesCut[i] += 1

        goodIdx = []
        for i in range(ncleanjets):
            if JetSatisfiesCut[i] < len(self.cuts): goodIdx.append(i) # Currently hardcoded: Will remove all jets which pass all given cuts

        for var in jet_dict:
           cutvar = [jet_dict[var][i] for i in goodIdx]
           self.out.fillBranch( self.newcollectionname + '_' + var, cutvar)
        return True
