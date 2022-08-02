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
        # print self.ZH3l_XLepton
        # print (self.ZH3l_XLepton is not None)
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
        if self.passSelection:
            return (self.hadronicTopJet1 + self.hadronicTopJet2 + self.hadronicTopJet3 + self.leptonicTopJet1 + self.neutrino + self.ZH3l_XLepton[0] + self.Zlepton1+self.Zlepton2).M()-(self.hadronicTopJet1 + self.hadronicTopJet2 + self.hadronicTopJet3 + self.leptonicTopJet1 + self.neutrino + self.ZH3l_XLepton[0]).M()
        else:
            return -9999

    def AZH_Amass(self):
        if self.passSelection:
            return (self.hadronicTopJet1 + self.hadronicTopJet2 + self.hadronicTopJet3 + self.leptonicTopJet1 + self.neutrino + self.ZH3l_XLepton[0] + self.Zlepton1 + self.Zlepton2).M()
        else:
            return -9999

    def AZH_Hmass(self):
        if self.passSelection:
            return (self.hadronicTopJet1 + self.hadronicTopJet2 + self.hadronicTopJet3 + self.leptonicTopJet1 + self.neutrino + self.ZH3l_XLepton[0]).M()
        else:
            return -9999

    def AZH_ChiSquare(self):
        if self.passSelection:
            return self.bestChiSquare
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

        Jet = Collection(event, "Jet")
        for j in Collection(event, "CleanJet"):
            self.CleanJet_4vecId.append(ROOT.TLorentzVector())
            self.CleanJet_4vecId[-1].SetPtEtaPhiM(j.pt, j.eta, j.phi, 0)

        self.l3_isOk = False if len(self.Lepton_4vecId) < 3 else True
        self.WH3l_isOk = self._WH3l_isOk()

        self.ZH3l_isOk = self._ZH3l_setXLepton()
        self.ZH3l_CleanJet_4vecId = [ j for j in self.CleanJet_4vecId if j.Pt() > 30 and abs(j.Eta()) < 4.7]


        #the main version of the code has the btag appended to the cleanJEt4 vecID, but this UL version does not
        #AZH code originally written based on main version assuming tag, so a new vector is created below for our AZH studies which currently needs the btag
        #also, AZH code uses the btagDeep not the one used in the main version
        self.CleanJet_4vecId_AZH = []
        for j in Collection(event, "CleanJet"):
            self.CleanJet_4vecId_AZH.append((ROOT.TLorentzVector(), Jet[j.jetIdx].btagDeepB))
            self.CleanJet_4vecId_AZH[-1][0].SetPtEtaPhiM(j.pt, j.eta, j.phi, 0)

        #****For azh studies
        self.AZH_CleanJet_4vecId = []
        self.jetCut_AZH = []
        self.bJetCollection = []
        self.pass4JetCut = False
        self.passBJetCut = False
        self.passSelection = False

        if self.ZH3l_isOk:
            self.jetCut_AZH = [ j for j in self.CleanJet_4vecId_AZH if j[0].Pt() > 30 and abs(j[0].Eta()) < 4.7]
            self.AZH_CleanJet_4vecId = [ j for j in self.jetCut_AZH if len(self.jetCut_AZH) >= 4]
            if len(self.AZH_CleanJet_4vecId) >= 4: self.pass4JetCut = True
            if self.pass4JetCut:
                self.bJetCollection = [ j for j in self.AZH_CleanJet_4vecId if j[1] > 0.4941]
                if len(self.bJetCollection) >=2:
                    self.passBJetCut = True
        #require: >= 4 jets, >= 2-btagged jets, OSSF (opp sign same flavor lepton), also jets have pt > 30 and abs. eta < 4.7
        if self.ZH3l_isOk and self.pass4JetCut and self.passBJetCut and self.ZH3l_XLepton[0] != -9999:
            self.passSelection = True
        else:
            self.passSelection = False

        #CHISQUARE**********************************************************************************************************
        self.bestChiSquare = 99999
        if self.passSelection:
            self.hadronicTopJet1 = ROOT.TLorentzVector()
            self.hadronicTopJet2 = ROOT.TLorentzVector()
            self.hadronicTopJet3 = ROOT.TLorentzVector()
            self.leptonicTopJet1 = ROOT.TLorentzVector()
            self.neutrino = ROOT.TLorentzVector()
            #NEUTRINO**********************************************************************************************************
            self.neutrino1 = ROOT.TLorentzVector()
            self.neutrino2 = ROOT.TLorentzVector()
            self.neutrinopz1 = 0
            self.neutrinopz2 = 0
            self.neutrinoEnergy1 = 0
            self.neutrinoEnergy2 = 0
            zeta = 0.5 * pow(80.4,2) + self.MET.Pt()*self.ZH3l_XLepton[0].Pt()*math.cos(self.ZH3l_XLepton[0].DeltaPhi(self.MET))
            sol = (pow(zeta,2)*pow(self.ZH3l_XLepton[0].Pz(),2)) / pow(self.ZH3l_XLepton[0].Pt(),4)  -  (pow(self.MET.Pt(),2)*pow(self.ZH3l_XLepton[0].E(),2) - pow(zeta,2)) / pow(self.ZH3l_XLepton[0].Pt(),2)
            if sol > 0:
                sol = math.sqrt(sol)
            else:
                sol = 0
            self.neutrinopz1 = (zeta * self.ZH3l_XLepton[0].Pz())/pow(self.ZH3l_XLepton[0].Pt(),2) + sol
            self.neutrinopz2 = (zeta * self.ZH3l_XLepton[0].Pz())/pow(self.ZH3l_XLepton[0].Pt(),2) - sol
            self.neutrinoEnergy1 = math.sqrt( pow(self.MET.Pt(),2) + pow(self.neutrinopz1,2) )
            self.neutrinoEnergy2 = math.sqrt( pow(self.MET.Pt(),2) + pow(self.neutrinopz2,2) )
            self.neutrino1.SetPxPyPzE(self.MET.Px(),self.MET.Py(),self.neutrinopz1,self.neutrinoEnergy1)
            self.neutrino2.SetPxPyPzE(self.MET.Px(),self.MET.Py(),self.neutrinopz2,self.neutrinoEnergy2)

            #get all the jet combinations**********************************************************************************************************
            self.hadronicTopJet1Nu1 = ROOT.TLorentzVector()
            self.hadronicTopJet2Nu1 = ROOT.TLorentzVector()
            self.hadronicTopJet3Nu1 = ROOT.TLorentzVector()
            self.hadronicTopJet1Nu2 = ROOT.TLorentzVector()
            self.hadronicTopJet2Nu2 = ROOT.TLorentzVector()
            self.hadronicTopJet2Nu2 = ROOT.TLorentzVector()
            self.leptonicJet1Nu1 = ROOT.TLorentzVector()
            self.leptonicJet1Nu2 = ROOT.TLorentzVector()

            #generator values from ttbar sample, put in generator values (note: still need to add scale factors)
            self.mtrue1 = 168.7 #leptonic top
            self.mtrue2 = 163   #hadronic top
            self.sigma1 = 26.64
            self.sigma2 = 37.73
            
            self.bestChiSquareNu1 = 9999
            self.bestChiSquareNu2 = 9999
            self.leptonicBJetExistsNu1 = -9999
            self.hadronicBJetExistsNu1 = -9999
            self.leptonicBJetExistsNu2 = -9999
            self.hadronicBJetExistsNu2 = -9999

            for i, j in enumerate(self.AZH_CleanJet_4vecId):
                self.tempjets = self.AZH_CleanJet_4vecId[:]
                if i < len(self.tempjets):
                    del self.tempjets[i]
                    combinationsOf3Jets = list(combinations(self.tempjets,3))
                    self.tempjets = self.AZH_CleanJet_4vecId
                    for k in combinationsOf3Jets:
                        self.leptonicsum = 0
                        self.hadronicsum = 0
                        self.leptonicsum = (j[0] + self.neutrino1 + self.ZH3l_XLepton[0]).M()
                        if j[1] > 0.4941:
                            self.leptonicBJetExistsNu1 = 1
                        self.hadronicsum = (k[0][0] + k[1][0] + k[2][0]).M()
                        if k[0][1] or k[1][1] or k[2][1] > 0.4941:
                            self.hadronicBJetExistsNu1 = 1
                        self.tempChiSquare = TMath.Power((self.leptonicsum-self.mtrue1)/self.sigma1,2) + TMath.Power((self.hadronicsum-self.mtrue2)/self.sigma2,2)
                        if self.tempChiSquare < self.bestChiSquareNu1 and self.leptonicBJetExistsNu1 != -9999 and self.hadronicBJetExistsNu1 != -9999:
                            self.bestChiSquareNu1 = self.tempChiSquare
                            self.hadronicTopJet1Nu1 = k[0][0]
                            self.hadronicTopJet2Nu1 = k[1][0]
                            self.hadronicTopJet3Nu1 = k[2][0]
                            self.leptonicJet1Nu1 = j[0]
            #loop again for second neutrino
            for i, j in enumerate(self.AZH_CleanJet_4vecId):
                self.tempjetsNu2 = self.AZH_CleanJet_4vecId[:]
                if i < len(self.tempjetsNu2):
                    del self.tempjetsNu2[i]
                    combinationsOf3JetsNu2 = list(combinations(self.tempjetsNu2,3))
                    self.tempjetsNu2 = self.AZH_CleanJet_4vecId
                    for k in combinationsOf3JetsNu2:
                        self.leptonicsumNu2 = 0
                        self.hadronicsumNu2 = 0
                        self.leptonicsumNu2 = (j[0] + self.neutrino2 + self.ZH3l_XLepton[0]).M()
                        if j[1] > 0.4941:
                            self.leptonicBJetExistsNu2 = 1
                        self.hadronicsumNu2 = (k[0][0] + k[1][0] + k[2][0]).M()
                        if k[0][1] or k[1][1] or k[2][1] > 0.4941:
                            self.hadronicBJetExistsNu2 = 1
                        self.tempChiSquareNu2 = TMath.Power((self.leptonicsumNu2-self.mtrue1)/self.sigma1,2) + TMath.Power((self.hadronicsumNu2-self.mtrue2)/self.sigma2,2)
                        if self.tempChiSquareNu2 < self.bestChiSquareNu2 and self.leptonicBJetExistsNu2 != -9999 and self.hadronicBJetExistsNu2 != -9999:
                            self.bestChiSquareNu2 = self.tempChiSquareNu2
                            self.hadronicTopJet1Nu2 = k[0][0]
                            self.hadronicTopJet2Nu2 = k[1][0]
                            self.hadronicTopJet3Nu2 = k[2][0]
                            self.leptonicJet1Nu2 = j[0]

            if self.bestChiSquareNu1 <= self.bestChiSquareNu2:
                self.hadronicTopJet1 = self.hadronicTopJet1Nu1
                self.hadronicTopJet2 = self.hadronicTopJet2Nu1
                self.hadronicTopJet3 = self.hadronicTopJet3Nu1
                self.leptonicTopJet1 = self.leptonicJet1Nu1
                self.neutrino = self.neutrino1
                self.bestChiSquare = self.bestChiSquareNu1
            else:
                self.hadronicTopJet1 = self.hadronicTopJet1Nu2
                self.hadronicTopJet2 = self.hadronicTopJet2Nu2
                self.hadronicTopJet3 = self.hadronicTopJet3Nu2
                self.leptonicTopJet1 = self.leptonicJet1Nu2
                self.neutrino = self.neutrino2
                self.bestChiSquare = self.bestChiSquareNu2

            #print('************************************************')
            #print('bestChiSquare',self.bestChiSquare)

        for nameBranchKey in self.newbranches.keys():
            self.out.fillBranch(nameBranchKey, getattr(self, nameBranchKey)());

        return True
