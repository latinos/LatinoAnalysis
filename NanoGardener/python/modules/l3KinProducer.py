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
from ROOT import TMath

from PhysicsTools.NanoAODTools.postprocessing.framework.datamodel import Collection
from PhysicsTools.NanoAODTools.postprocessing.framework.eventloop import Module
from PhysicsTools.NanoAODTools.postprocessing.modules.common.collectionMerger import collectionMerger
from LatinoAnalysis.NanoGardener.framework.BranchMapping import mappedOutputTree, mappedEvent

import math
from itertools import combinations, permutations
import itertools

class l3KinProducer(Module):
    l3KinDefault = -9999
    Zmass = 91.1876
    Wmass = 80.4
    Topmassleptonic_true = 168.7 #leptonic top mass truth level (from ttbar sample)
    Topmasshadronic_true = 163  #hadronic top mass truth level (from ttbar sample)
    sigmaleptonic = 26.64
    sigmahadronic = 37.73
    newbranches = {
        'WH3l_ZVeto'     : (["F"], {}),
        'WH3l_flagOSSF'  : (["O"], {}),
        'WH3l_njet'      : (["I"], {}),
#       'WH3l_nbjet'     : (["I"], {}),
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
        'WH3l_ptW'       : (["F"], {}),

        # for ZH3l, "l" in these variables *always* refers to the lepton not associated with the Z
        'ZH3l_njet'      : (["F"], {}),
        'ZH3l_Z4lveto'   : (["F"], {}),
        'ZH3l_dmjjmW'    : (["F"], {}),
        'ZH3l_mTlmet'    : (["F"], {}),
        'ZH3l_pdgid_l'   : (["F"], {}),
        'ZH3l_dphilmetjj': (["F"], {}),
        'ZH3l_dphilmetj' : (["F"], {}),
        'ZH3l_pTlmetjj'  : (["F"], {}),
        'ZH3l_pTlmetj'   : (["F"], {}),
        'ZH3l_mTlmetjj'  : (["F"], {}),
        'ZH3l_mTlmetj'  : (["F"], {}),
        'ZH3l_pTZ'       : (["F"], {}),
        'ZH3l_checkmZ'   : (["F"], {}),

        'AZH_mA_minus_mH': (["F"], {}),
        'AZH_Amass':  (["F"], {}),
        'AZH_Hmass' : (["F"], {}),
        'AZH_ChiSquare' : (["F"], {}),
        'AZH_Tophadronic' : (["F"], {}),
        'AZH_Topleptonic' : (["F"], {}),
    }

    def __init__(self, branch_map=''):
        self._branch_map = branch_map

    def beginJob(self):
        pass

    def endJob(self):
        pass

    def beginFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        self.out = mappedOutputTree(wrappedOutputTree, mapname=self._branch_map)

        for nameBranchKey, newBranchOpt in self.newbranches.items() :
            self.out.branch(nameBranchKey, *newBranchOpt[0], **newBranchOpt[1]);

    def endFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        pass

    def _WH3l_isOk(self):
        """If a good WH3l candidate event?"""
        if not self.l3_isOk:
            return False
        sign = lambda a: 1 if a >= 0 else -1
        if abs(sum([sign(l[1]) for l in self.Lepton_4vecId])) > 1:
            return False
        return True

    def WH3l_ZVeto(self):
        """Return min mass difference in OSSF lepton pairs"""
        if not self.WH3l_isOk:
            return -1*self.l3KinDefault

        minmllDiffToZ = -1*self.l3KinDefault
        for iLep, jLep in combinations(self.Lepton_4vecId, 2):
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
        return sum([1 if j.Pt() > 40 and abs(j.Eta()) < 4.7 else 0 for j in self.CleanJet_4vecId])

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

    def WH3l_ptW(self):
        """Return pt of lepton least likely to be from the Higgs (proxy for associated W)"""
        WH3l_ptW = self.l3KinDefault
        if self.WH3l_isOk:
            mindR = -1*self.l3KinDefault
            for iLep, jLep, kLep in permutations(self.Lepton_4vecId, 3):
                if iLep[1]*jLep[1] < 0:
                    dR = iLep[0].DeltaR(jLep[0])
                    if dR < mindR:
                        mindR = dR
                        WH3l_ptW = kLep[0].Pt()
        return WH3l_ptW

    def _ZH3l_setXLepton(self):
        """Find the lepton least likely to be part of the Z pair by invariant mass.  Double-duty as a check for OSSF pair"""
        if not self.WH3l_isOk:
            return False

        minmllDiffToZ = -1*self.l3KinDefault
        self.ZH3l_XLepton = None

        for iLep, jLep, kLep in permutations(self.Lepton_4vecId, 3):
            if iLep[1]+jLep[1] == 0:
                mllDiffToZ = abs((iLep[0]+jLep[0]).M()-self.Zmass)
                if mllDiffToZ < minmllDiffToZ:
                    self.ZH3l_XLepton = kLep
                    self.pTZ = (iLep[0]+jLep[0]).Pt()
                    self.checkZmass = (iLep[0]+jLep[0]).M()
                    minmllDiffToZ = mllDiffToZ
                    self.Zlepton1 = iLep[0]
                    self.Zlepton2 = jLep[0]
        return self.ZH3l_XLepton is not None

    def ZH3l_njet(self):
        """Jet counting.  For validation against ggH -- can eventually be removed"""
        return len(self.ZH3l_CleanJet_4vecId)

    def ZH3l_Z4lveto(self):
        """Return mass difference of 3 leptons to Z"""
        if not self.ZH3l_isOk:
            return self.l3KinDefault
        return abs(self.WH3l_mlll() - self.Zmass)

    def ZH3l_dmjjmW(self):
        """Return mass difference between leading jets and W"""
        if not self.ZH3l_isOk or not len(self.ZH3l_CleanJet_4vecId) >= 2:
            return self.l3KinDefault
        return (self.ZH3l_CleanJet_4vecId[0] + self.ZH3l_CleanJet_4vecId[1]).M() - self.Wmass

    def ZH3l_pdgid_l(self):
        """Signed PDGID of lepton"""
        if not self.ZH3l_isOk:
            return self.l3KinDefault
        return self.ZH3l_XLepton[1]

    def ZH3l_mTlmet(self):
        """https://en.wikipedia.org/wiki/Transverse_mass with m_lepton=0, m_met=0. """
        if not self.ZH3l_isOk:
            return self.l3KinDefault
        lvec = self.ZH3l_XLepton[0]
        mtlmet = math.sqrt(2 * lvec.Pt() * self.MET.Pt() * (1 - math.cos(abs(lvec.DeltaPhi(self.MET)))))
        return mtlmet

    def ZH3l_dphilmetjj(self):
        """Delta phi between dijets and l+MET, i.e., between the Ws"""
        if not self.ZH3l_isOk or not len(self.ZH3l_CleanJet_4vecId) >= 2:
            return self.l3KinDefault
        return abs((self.ZH3l_XLepton[0] + self.MET).DeltaPhi(self.ZH3l_CleanJet_4vecId[0] + self.ZH3l_CleanJet_4vecId[1]))

    def ZH3l_dphilmetj(self):
        """Delta phi between lead jet and l+MET, i.e., between the Ws"""
        if not self.ZH3l_isOk or not len(self.ZH3l_CleanJet_4vecId) >= 1:
            return self.l3KinDefault
        return abs((self.ZH3l_XLepton[0] + self.MET).DeltaPhi(self.ZH3l_CleanJet_4vecId[0]))

    def ZH3l_pTlmetjj(self):
        """pT of dijets and l+MET, i.e., of the WW system"""
        if not self.ZH3l_isOk or not len(self.ZH3l_CleanJet_4vecId) >= 2:
            return self.l3KinDefault
        return (self.ZH3l_XLepton[0] + self.MET + self.ZH3l_CleanJet_4vecId[0] + self.ZH3l_CleanJet_4vecId[1]).Pt()

    def ZH3l_pTlmetj(self):
        """pT of lead jet and l+MET, i.e., of the WW system"""
        if not self.ZH3l_isOk or not len(self.ZH3l_CleanJet_4vecId) >= 1:
            return self.l3KinDefault
        return (self.ZH3l_XLepton[0] + self.MET + self.ZH3l_CleanJet_4vecId[0]).Pt()

    def ZH3l_mTlmetj(self):
        """Return transverse mass of l+met+jet system"""
        if not self.ZH3l_isOk or not len(self.ZH3l_CleanJet_4vecId) >= 1:
            return self.l3KinDefault
        jvec0 = self.ZH3l_CleanJet_4vecId[0]
        lvec = self.ZH3l_XLepton[0]
        WWvec = self.MET + lvec + jvec0;
        sumpt = self.MET.Pt() + lvec.Pt() + jvec0.Pt()
        return math.sqrt(pow(sumpt,2) - pow(WWvec.Px(),2) - pow(WWvec.Py(),2));

    def ZH3l_mTlmetjj(self):
        """Return transverse mass of l+met+dijet system"""
        if not self.ZH3l_isOk or not len(self.ZH3l_CleanJet_4vecId) >= 2:
            return self.l3KinDefault
        jvec0 = self.ZH3l_CleanJet_4vecId[0]
        jvec1 = self.ZH3l_CleanJet_4vecId[1]
        lvec = self.ZH3l_XLepton[0]
        WWvec = self.MET + lvec + jvec0 + jvec1;
        sumpt = self.MET.Pt() + lvec.Pt() + jvec0.Pt() + jvec1.Pt()
        return math.sqrt(pow(sumpt,2) - pow(WWvec.Px(),2) - pow(WWvec.Py(),2));

    def ZH3l_pTZ(self):
        """Return pt of selected Z"""
        if not self.ZH3l_isOk:
            return self.l3KinDefault
        return self.pTZ

    def ZH3l_checkmZ(self):
        """Return pt of selected Z"""
        if not self.ZH3l_isOk:
            return self.l3KinDefault
        return self.checkZmass

#****************************************************************************************************************
    def AZH_mA_minus_mH(self):
        if self.AZH_isOk:
            return (self.ZH3l_XLepton[0] + self.AZH_Neutrino_best + self.bJetLeptonic_best + self.bJetHadronic_best + self.WJet1_best + self.WJet2_best + self.Zlepton1 + self.Zlepton2).M()-(self.ZH3l_XLepton[0] + self.AZH_Neutrino_best + self.bJetLeptonic_best + self.bJetHadronic_best + self.WJet1_best + self.WJet2_best).M()
        else:
            return -9999

    def AZH_Amass(self):
        if self.AZH_isOk:
            return (self.ZH3l_XLepton[0] + self.AZH_Neutrino_best + self.bJetLeptonic_best + self.bJetHadronic_best + self.WJet1_best + self.WJet2_best + self.Zlepton1 + self.Zlepton2).M()
        else:
            return -9999

    def AZH_Hmass(self):
        if self.AZH_isOk:
            return (self.ZH3l_XLepton[0] + self.AZH_Neutrino_best + self.bJetLeptonic_best + self.bJetHadronic_best + self.WJet1_best + self.WJet2_best ).M()
        else:
            return -9999

    def AZH_ChiSquare(self):
        if self.AZH_isOk:
            return self.ChisqMin
        else:
            return -9999

    def AZH_Tophadronic(self):
        if self.AZH_isOk:
            return (self.bJetHadronic_best + self.WJet1_best + self.WJet2_best).M()
        else:
            return -9999

    def AZH_Topleptonic(self):
        if self.AZH_isOk:
            return (self.ZH3l_XLepton[0] + self.AZH_Neutrino_best + self.bJetLeptonic_best).M()
        else:
            return -9999


    def analyze(self, event):
        """process event, return True (go to next module) or False (fail, go to next event)"""
        event = mappedEvent(event, mapname=self._branch_map)
        # Order in pt the collection merging muons and electrons
        # lepMerger must be already called
        Lepton = Collection(event, "Lepton")
        self.Lepton_4vecId = []
        for iLep in range(3):
            if len(Lepton) > iLep:
                self.Lepton_4vecId.append((ROOT.TLorentzVector(), Lepton[iLep].pdgId))
                self.Lepton_4vecId[-1][0].SetPtEtaPhiM(Lepton[iLep].pt, Lepton[iLep].eta, Lepton[iLep].phi, 0)

        self.MET = ROOT.TLorentzVector()
        self.MET.SetPtEtaPhiM(event.PuppiMET_pt, 0, event.PuppiMET_phi, 0)

        self.CleanJet_4vecId = []
        self.bJet_4vecId = []

        Jet = Collection(event, "Jet")
        for j in Collection(event, "CleanJet"):
            self.CleanJet_4vecId.append(ROOT.TLorentzVector()) #redefine a new collection with btagDeepB
            self.CleanJet_4vecId[-1].SetPtEtaPhiM(j.pt, j.eta, j.phi, 0)
            self.bJet_4vecId.append((ROOT.TLorentzVector(), Jet[j.jetIdx].btagDeepB))
            self.bJet_4vecId[-1][0].SetPtEtaPhiM(j.pt, j.eta, j.phi, 0)

        self.l3_isOk = False if len(self.Lepton_4vecId) < 3 else True
        self.WH3l_isOk = self._WH3l_isOk()

        self.ZH3l_isOk = self._ZH3l_setXLepton()
        self.ZH3l_CleanJet_4vecId = [ j for j in self.CleanJet_4vecId if j.Pt() > 30 and abs(j.Eta()) < 4.7]
        
        self.AZH_bJet_4vecId = [ j[0] for j in self.bJet_4vecId if j[0].Pt() > 30 and abs(j[0].Eta()) < 4.7 and j[1] > 0.4941]
        self.AZH_isOk = self.ZH3l_isOk and len(self.ZH3l_CleanJet_4vecId) >= 4 and len(self.AZH_bJet_4vecId) >= 2

#------------#AZH Neutrino Pz Solution--------------------------------------------------------------------------------------------------------------------
        if self.ZH3l_isOk:
          self.Zeta = 0.5 * pow(self.Wmass,2) + self.MET.Pt()*self.ZH3l_XLepton[0].Pt()*math.cos(self.ZH3l_XLepton[0].DeltaPhi(self.MET)) 
          self.A = (pow(self.Zeta,2)*pow(self.ZH3l_XLepton[0].Pz(),2)) / pow(self.ZH3l_XLepton[0].Pt(),4)  -  (pow(self.MET.Pt(),2)*pow(self.ZH3l_XLepton[0].E(),2) - pow(self.Zeta,2)) / pow(self.ZH3l_XLepton[0].Pt(),2)
          A = math.sqrt(self.A) if self.A> 0  else 0
          self.AZH_Neutrino1 = ROOT.TLorentzVector()
          self.AZH_Neutrino2 = ROOT.TLorentzVector()
          self.Pznu1 = (self.Zeta * self.ZH3l_XLepton[0].Pz())/pow(self.ZH3l_XLepton[0].Pt(),2) + A
          self.Pznu2 = (self.Zeta * self.ZH3l_XLepton[0].Pz())/pow(self.ZH3l_XLepton[0].Pt(),2) - A
          self.Enu1 = math.sqrt( pow(self.MET.Pt(),2) + pow(self.Pznu1,2) )
          self.Enu2 = math.sqrt( pow(self.MET.Pt(),2) + pow(self.Pznu2,2) )
          self.AZH_Neutrino1.SetPxPyPzE(self.MET.Px(),self.MET.Py(),self.Pznu1,self.Enu1)
          self.AZH_Neutrino2.SetPxPyPzE(self.MET.Px(),self.MET.Py(),self.Pznu2,self.Enu2)

#-----------------------------------------------------------------------------------------------------------------------------------------------------------
          self.WJet1_best = None
          self.WJet2_best = None
          self.bJetHadronic_best = None
          self.bJetLeptonic_best = None
          self.AZH_Neutrino_best = None
          self.ChisqMin = 99999
          self.Chisq = 0
          for AZH_Neutrino in [self.AZH_Neutrino1, self.AZH_Neutrino2]:
            for bJetPair in combinations(self.AZH_bJet_4vecId, 2):
                WJets = [ j for j in self.ZH3l_CleanJet_4vecId if j not in bJetPair]
                for i in range(2): 
                 for WJet1, WJet2 in combinations(WJets, 2):
                    bJetHadronic = bJetPair[i]
                    bJetLeptonic = bJetPair[1-i]
                    WMassLeptonic = (self.ZH3l_XLepton[0] + AZH_Neutrino).M()
                    WMassHadronic = (WJet1 + WJet2).M()
                    TopMassLeptonic = (self.ZH3l_XLepton[0] + AZH_Neutrino + bJetLeptonic).M()
                    TopMassHadronic = (WJet1 + WJet2 + bJetHadronic).M()
                    self.Chisq = TMath.Power((TopMassLeptonic-self.Topmassleptonic_true)/self.sigmaleptonic,2) + TMath.Power((TopMassHadronic-self.Topmasshadronic_true)/self.sigmahadronic,2) #Modify this reduced Chisq to add W information
                    if self.Chisq < self.ChisqMin:
                        self.ChisqMin = self.Chisq
                        self.WJet1_best = WJet1
                        self.WJet2_best = WJet2
                        self.bJetHadronic_best = bJetHadronic
                        self.bJetLeptonic_best = bJetLeptonic
                        self.AZH_Neutrino_best = AZH_Neutrino 
        for nameBranchKey in self.newbranches.keys():
            self.out.fillBranch(nameBranchKey, getattr(self, nameBranchKey)());

        return True
