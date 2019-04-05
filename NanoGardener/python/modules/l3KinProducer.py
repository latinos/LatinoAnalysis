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
    Zmass = 91.1876
    Wmass = 80.4
    newbranches = {
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

        'ZH3l_njet'      : (["F"], {}),
        'ZH3l_z4lveto'   : (["F"], {}),
        'ZH3l_dmjjmW'    : (["F"], {}),
        'ZH3l_mtW_notZ'  : (["F"], {}),
        'ZH3l_dphilmetjj': (["F"], {}),
        'ZH3l_mTlmetjj'  : (["F"], {}),
        'ZH3l_ptZ'       : (["F"], {}),
        'ZH3l_checkmZ'   : (["F"], {}),
    }

    def __init__(self):
        pass

    def beginJob(self):
        pass

    def endJob(self):
        pass

    def beginFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        self.out = wrappedOutputTree

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

    def _ZH3l_setNotZLepton(self):
        """Find the lepton least likely to be part of the Z pair by invariant mass"""
        if not self.WH3l_isOk:
            return False

        minmllDiffToZ = -1*self.l3KinDefault

        lep0 = self.Lepton_4vecId[0] 
        lep1 = self.Lepton_4vecId[1] 
        lep2 = self.Lepton_4vecId[2] 

        """There is probably a smarter way to do this but this will work"""
        if lep0[1]+lep1[1] == 0:
            mllDiffToZ = abs((lep0[0]+lep1[0]).M()-self.Zmass)
            if mllDiffToZ < minmllDiffToZ: 
                self.notZLepton = lep2
                self.pTZ = (lep0[0]+lep1[0]).Pt()
                self.checkZmass = (lep0[0]+lep1[0]).M()
                minmllDiffToZ = mllDiffToZ 

        if lep1[1]+lep2[1] == 0:
            mllDiffToZ = abs((lep1[0]+lep2[0]).M()-self.Zmass)
            if mllDiffToZ < minmllDiffToZ: 
                self.notZLepton = lep0
                self.pTZ = (lep1[0]+lep2[0]).Pt()
                self.checkZmass = (lep1[0]+lep2[0]).M()
                minmllDiffToZ = mllDiffToZ 

        if lep2[1]+lep0[1] == 0:
            mllDiffToZ = abs((lep2[0]+lep0[0]).M()-self.Zmass)
            if mllDiffToZ < minmllDiffToZ: 
                self.notZLepton = lep1
                self.pTZ = (lep2[0]+lep0[0]).Pt()
                self.checkZmass = (lep2[0]+lep0[0]).M()
                minmllDiffToZ = mllDiffToZ 


        return True

    def _ZH3l_setJets(self):
        """Internal use only.  Should match ggH analysis jet counting"""
        if not self.WH3l_isOk:
            return self.l3KinDefault
        tmp_ZH3l_njet = sum([ 1 if j[0] > 30 and abs(j[1]) < 4.7 else 0 for j in self.CleanJet ])
        if tmp_ZH3l_njet < 2:
            return tmp_ZH3l_njet

        j0 = self.CleanJet[0]
        j1 = self.CleanJet[1]
        self.j4vec0 = ROOT.TLorentzVector()
        self.j4vec1 = ROOT.TLorentzVector()
        self.j4vec0.SetPtEtaPhiM(j0[0], j0[1], j0[2], 0)
        self.j4vec1.SetPtEtaPhiM(j1[0], j1[1], j1[2], 0)
    
        return tmp_ZH3l_njet

    def WH3l_ZVeto(self):
        """Return min mass difference in OSSF lepton pairs"""
        if not self.WH3l_isOk:
            return -1*self.l3KinDefault

        minmllDiffToZ = -1*self.l3KinDefault
        for iLep, jLep in combinations(self.Lepton_4vecId,2):
            if iLep[1]+jLep[1] == 0:
                mllDiffToZ = abs((iLep[0]+jLep[0]).M()-self.Zmass)
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
        return sum([ 1 if j[0] > 40 and abs(j[1]) < 4.7 else 0 for j in self.CleanJet ])
    
    def WH3l_nbjet(self):
        if not self.WH3l_isOk:
            return self.l3KinDefault
        return sum([ 1 if j[0] > 20 and j[0] < 40 and abs(j[1]) < 4.7 and j[3] > -0.5884 else 0 for j in self.CleanJet ])

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


    def ZH3l_njet(self):
        """Jet counting.  For validation against ggH -- can eventually be removed"""
        if not self.WH3l_isOk:
            return self.l3KinDefault
        return self._ZH3l_njet

    def ZH3l_z4lveto(self):
        """Return mass difference of 3 leptons to Z"""
        if not self.WH3l_isOk:
            return self.l3KinDefault
        return abs(self.WH3l_mlll() - self.Zmass)

    def ZH3l_dmjjmW(self):
        """Return mass difference between leading jets and W"""
        if not self.WH3l_isOk or not self._ZH3l_njet >= 2:
            return self.l3KinDefault
        return ((self.j4vec0 + self.j4vec1).M() - self.Wmass)

    def ZH3l_mtW_notZ(self):
        """https://en.wikipedia.org/wiki/Transverse_mass with m_lepton=0, m_met=0. """
        if not self.WH3l_isOk:
            return self.l3KinDefault

        lvec = self.notZLepton[0]
        mvec = self.MET
        mtlmet = math.sqrt(2 * lvec.Pt() * mvec.Pt() * (1 - math.cos(abs(lvec.DeltaPhi(mvec))))) 
        return mtlmet

    def ZH3l_dphilmetjj(self):
        """Delta phi between dijets and l+MET, i.e., between the Ws"""
        if not self.WH3l_isOk or not self._ZH3l_njet >= 2:
            return self.l3KinDefault
        return abs((self.notZLepton[0] + self.MET).DeltaPhi(self.j4vec0 + self.j4vec1))

    def ZH3l_mTlmetjj(self):
        """Return pt of selected Z"""
        if not self.WH3l_isOk or not self._ZH3l_njet >= 2:
            return self.l3KinDefault
        WWvec = self.MET + self.notZLepton[0] + self.j4vec0 + self.j4vec1;
        sumpt = self.MET.Pt() + self.notZLepton[0].Pt() + self.j4vec0.Pt() + self.j4vec1.Pt()
        return math.sqrt(pow(sumpt,2) - pow(WWvec.Px(),2) - pow(WWvec.Py(),2));

    def ZH3l_ptZ(self):
        """Return pt of selected Z"""
        if not self.WH3l_isOk:
            return self.l3KinDefault
        return self.pTZ

    def ZH3l_checkmZ(self):
        """Return pt of selected Z"""
        if not self.WH3l_isOk:
            return self.l3KinDefault
        return self.checkZmass


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
        self.MET.SetPtEtaPhiM(event.PuppiMET_pt, 0, event.PuppiMET_phi, 0)

        self.CleanJet = []
        Jet = Collection(event, "Jet")
        for j in Collection(event, "CleanJet"):
            self.CleanJet.append((j.pt, j.eta, j.phi, Jet[j.jetIdx].btagCMVA))

        self.WH3l_isOk = self._WH3l_isOk()

        self._ZH3l_setNotZLepton()
        self._ZH3l_njet = self._ZH3l_setJets()

        for nameBranchKey in self.newbranches.keys():
            self.out.fillBranch(nameBranchKey, getattr(self, nameBranchKey)());

        return True

