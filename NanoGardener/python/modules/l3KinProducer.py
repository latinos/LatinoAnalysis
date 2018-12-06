# vim: set sts=4 sw=4 fdm=syntax fdl=2 et:
#
#     | ___ /   |  / _)         
#     |   _ \   ' /   |  __ \   
#     |    ) |  . \   |  |   |  
#    _| ____/  _|\_\ _| _|  _|  
#
#

import ROOT
ROOT.PyConfig.IgnoreCommandLineOptions = True

from PhysicsTools.NanoAODTools.postprocessing.framework.datamodel import Collection
from PhysicsTools.NanoAODTools.postprocessing.framework.eventloop import Module
from PhysicsTools.NanoAODTools.postprocessing.modules.common.collectionMerger import collectionMerger

import math
from itertools import combinations

class l3KinProducer(Module):
    l3KinDefault = -9999

    def __init__(self):
        pass

    def beginJob(self):
        pass

    def endJob(self):
        pass

    def beginFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        self.out = wrappedOutputTree
        self.newbranches = {
            'WH3l_ZVeto'     : (["F"], {}),
            'WH3l_flagOSSF'  : (["O"], {}),
            'WH3l_njet'      : (["I"], {}),
            'WH3l_nbjet'     : (["I"], {}),
            'WH3l_mtlmet'    : (["F"], {'n':3}),
            'WH3l_dphilmet'  : (["F"], {'n':3}),
            'WH3l_mOSll'     : (["F"], {'n':3}),
            'WH3l_drOSll'    : (["F"], {'n':3}),
            'WH3l_ptOSll'    : (["F"], {'n':3}),
            'WH3l_chlll'     : (["I"], {}),
            'WH3l_mlll'      : (["F"], {}),
            'WH3l_ptlll'     : (["F"], {}),
            'WH3l_ptWWW'     : (["F"], {}),
            'WH3l_mtWWW'     : (["F"], {}),
            'WH3l_dphilllmet': (["F"], {}),
        }

        for nameBranchKey, newBranchOpt in self.newbranches.items() :
            self.out.branch(nameBranchKey, *newBranchOpt[0], **newBranchOpt[1]);

    def endFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        pass

    def _WH3l_isOk(self):
        """If a good WH3l candidate event?"""
        if len(self.Lepton_4vecId) < 3:
            return False
        sign = lambda a: 1 if a >= 0 else -1
        if abs(sum([sign(l[1]) for l in self.Lepton_4vecId])) > 1:
            return False
        return True

    def WH3l_ZVeto(self):
        """Return min mass difference in OSSF lepton pairs"""
        if not self.WH3l_isOk:
            return -1*self.l3KinDefault

        Zmass=91.1876
        minmllDiffToZ = -1*self.l3KinDefault
        for iLep, jLep in combinations(self.Lepton_4vecId,2):
            if iLep[1]+jLep[1] == 0:
                mllDiffToZ = abs((iLep[0]+jLep[0]).M()-Zmass)
                minmllDiffToZ = mllDiffToZ if mllDiffToZ < minmllDiffToZ else minmllDiffToZ
        return minmllDiffToZ

    def WH3l_flagOSSF(self):
        """Return True if OSSF lepton pair is found"""
        if not self.WH3l_isOk:
            return False

        for iLep, jLep in combinations(self.Lepton_4vecId,2):
            if iLep[1]+jLep[1] == 0:
                return True

        return False

    def WH3l_njet(self):
        if not self.WH3l_isOk:
            return self.l3KinDefault
        return sum([ 1 if j.pt > 40 and abs(j.eta) < 4.7 else 0 for j in self.CleanJet ])
    
    def WH3l_nbjet(self):
        if not self.WH3l_isOk:
            return self.l3KinDefault
        return sum([ 1 if j.pt > 20 and j.pt < 40 and abs(j.eta) < 4.7 and self.Jet[j.jetIdx].btagCMVA > -0.5884 else 0 for j in self.CleanJet ])

    def WH3l_mtlmet(self):
        """https://en.wikipedia.org/wiki/Transverse_mass with m_lepton=0, m_met=0. """
        if not self.WH3l_isOk:
            return [self.l3KinDefault]*3
        calc_mtlmet = lambda lvec, mvec: math.sqrt(2 * lvec.Pt() * mvec.Pt() * (1 - math.cos(abs(lvec.DeltaPhi(mvec))))) if lvec.Pt() > 0 else self.l3KinDefault
        return [ calc_mtlmet(l[0], self.MET) for l in self.Lepton_4vecId ]

    def WH3l_dphilmet(self):
        """Return dphi between lepton and MET"""
        if not self.WH3l_isOk:
            return [self.l3KinDefault]*3
        return [ abs(l[0].DeltaPhi(self.MET)) for l in self.Lepton_4vecId ]

    def WH3l_mOSll(self):
        """Return mass of OS lepton pair"""
        if not self.WH3l_isOk:
            return [self.l3KinDefault]*3
        return [ (iLep[0]+jLep[0]).M() if iLep[1]*jLep[1] < 0 else self.l3KinDefault for iLep, jLep in combinations(self.Lepton_4vecId,2)]

    def WH3l_drOSll(self):
        """Return dr of OS lepton pair"""
        if not self.WH3l_isOk:
            return [self.l3KinDefault]*3
        return [ iLep[0].DeltaR(jLep[0]) if iLep[1]*jLep[1] < 0 else self.l3KinDefault for iLep, jLep in combinations(self.Lepton_4vecId,2)]

    def WH3l_ptOSll(self):
        """Return pt of OS lepton pair"""
        if not self.WH3l_isOk:
            return [self.l3KinDefault]*3
        return [ (iLep[0]+jLep[0]).Pt() if iLep[1]*jLep[1] < 0 else self.l3KinDefault for iLep, jLep in combinations(self.Lepton_4vecId,2)]

    def WH3l_chlll(self):
        """Return charge sum of leptons"""
        if not self.WH3l_isOk:
            return self.l3KinDefault
        sign = lambda a: 1 if a >= 0 else -1
        return sum([ sign(l[1]) for l in self.Lepton_4vecId])

    def WH3l_mlll(self):
        """Return invariant of leptons"""
        if not self.WH3l_isOk:
            return self.l3KinDefault
        return (self.Lepton_4vecId[0][0]+self.Lepton_4vecId[1][0]+self.Lepton_4vecId[2][0]).M()

    def WH3l_ptlll(self):
        """Return pt of leptons"""
        if not self.WH3l_isOk:
            return self.l3KinDefault
        return (self.Lepton_4vecId[0][0]+self.Lepton_4vecId[1][0]+self.Lepton_4vecId[2][0]).Pt()

    def WH3l_ptWWW(self):
        """Return pt of WH"""
        if not self.WH3l_isOk:
            return self.l3KinDefault
        return (self.Lepton_4vecId[0][0]+self.Lepton_4vecId[1][0]+self.Lepton_4vecId[2][0]+self.MET).Pt()

    def WH3l_mtWWW(self):
        """Return mt of WH"""
        if not self.WH3l_isOk:
            return self.l3KinDefault
        return math.sqrt(2*self.WH3l_ptlll()*self.MET.Pt()*(1. - math.cos(self.WH3l_dphilllmet())))

    def WH3l_dphilllmet(self):
        """Return mt of WH"""
        if not self.WH3l_isOk:
            return self.l3KinDefault
        return abs((self.Lepton_4vecId[0][0]+self.Lepton_4vecId[1][0]+self.Lepton_4vecId[2][0]).DeltaPhi(self.MET))

    def analyze(self, event):
        """process event, return True (go to next module) or False (fail, go to next event)"""

        # Order in pt the collection merging muons and electrons
        # lepMerger must be already called
        Lepton = Collection(event, "Lepton")
        self.Lepton_4vecId = []
        for iLep in range(3):
            if len(Lepton) > iLep:
                self.Lepton_4vecId.append( (ROOT.TLorentzVector(), Lepton[iLep].pdgId) )
                self.Lepton_4vecId[-1][0].SetPtEtaPhiM(Lepton[iLep].pt, Lepton[iLep].eta, Lepton[iLep].phi, 0)

        self.MET = ROOT.TLorentzVector()
        self.MET.SetPtEtaPhiM(event.MET_pt, 0, event.MET_phi, 0)

        self.CleanJet = Collection(event, "CleanJet")
        #auxiliary jet collection to access the mass
        self.Jet = Collection(event, "Jet")

        self.WH3l_isOk = self._WH3l_isOk()

        for nameBranchKey in self.newbranches.keys():
            self.out.fillBranch(nameBranchKey, getattr(self, nameBranchKey)());

        return True

