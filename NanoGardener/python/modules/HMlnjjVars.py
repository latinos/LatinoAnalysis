import ROOT
import math
ROOT.PyConfig.IgnoreCommandLineOptions = True
import re
import os
from math import sqrt

from PhysicsTools.NanoAODTools.postprocessing.framework.datamodel import Collection
from PhysicsTools.NanoAODTools.postprocessing.framework.eventloop import Module

Wmass=80.4

class HMlnjjVarsClass(Module):
    def __init__(self):
	self.HlnFat_4v  = ROOT.TLorentzVector()
	self.Hlnjj_4v   = ROOT.TLorentzVector()
	self.Wlep_4v   = ROOT.TLorentzVector()
	self.Wfat_4v   = ROOT.TLorentzVector()
	self.Wjj_4v   = ROOT.TLorentzVector()

    def beginJob(self):
        pass

    def endJob(self):
        pass

    def beginFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        self.out = wrappedOutputTree

        #New Branches
        self.out.branch("CHlnjj" , "I")
        self.out.branch("IsFatSig" , "O")
        self.out.branch("IsFatSB"  , "O")
        self.out.branch("IsFatTop" , "O")
        self.out.branch("IsJjSig" , "O")
        self.out.branch("IsJjSB"  , "O")
        self.out.branch("IsJjTop" , "O")

        self.out.branch("WptOvHfatM", "F")
        self.out.branch("WptOvHak4M", "F")

        self.out.branch("HlnFat_mass", "F")
        self.out.branch("Hlnjj_mass" , "F")
        self.out.branch("Wlep_mt" , "F")
        self.out.branch("Hlnjj_mt" , "F")

        #self.out.branch("GenDrAk8Ak4", "F", lenVar="nGenDrAk8Ak4")

    def endFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        pass

    def initReaders(self,tree): # this function gets the pointers to Value and ArrayReaders and sets them in the C++ worker class
        pass
        #self.Leptons   = {}
        #self.Jets      = {}
        #self.FatJets   = {}
        #self.GenDresLepts = {}
        #self.GenAK4s   = {}
        #self.GenAK8s   = {}
        #for br in tree.GetListOfBranches():
        #   bname = br.GetName()
        #   if re.match('\ALepton_', bname):    self.Leptons[bname]     = tree.arrayReader(bname)
        #   if re.match('\ACleanJet_', bname):  self.Jets[bname]        = tree.arrayReader(bname)
        #   if re.match('\AFatJet_', bname):    self.FatJets[bname]     = tree.arrayReader(bname)
        #   if re.match('\AGenDressedLepton_', bname): self.GenDresLepts[bname] = tree.arrayReader(bname)
        #   if re.match('\AGenJet_', bname):    self.GenAK4s[bname]     = tree.arrayReader(bname)
        #   if re.match('\AGenJetAK8_', bname): self.GenAK8s[bname]     = tree.arrayReader(bname)

        #self.nLepton           = tree.valueReader('nLepton')
        #self.nLepton           = tree.valueReader('nLepton')
        #self.nJet              = tree.valueReader('nCleanJet')
        #self.nFatJet           = tree.valueReader('nFatJet')
        #self.nGenDresLept      = tree.valueReader('nGenDressedLepton')
        #self.nGenAK4           = tree.valueReader('nGenJet')
        #self.nGenAK8           = tree.valueReader('nGenJetAK8')
        #self._ttreereaderversion= tree._ttreereaderversion

    def analyze(self, event):
        """process event, return True (go to next module) or False (fail, go to next event)"""
        # do this check at every event, as other modules might have read further branches
        #if event._tree._ttreereaderversion > self._ttreereaderversion: 
        #    self.initReaders(event._tree)
        #nOrgJets = getattr(event, "nJet")
        #OrgJets = Collection(event, "Jet")

	# initialize
	self.HlnFat_4v.SetPtEtaPhiM(0,0,0,0)
	self.Hlnjj_4v.SetPtEtaPhiM(0,0,0,0)
	self.Wlep_4v.SetPtEtaPhiM(0,0,0,0)
	self.Wfat_4v.SetPtEtaPhiM(0,0,0,0)
	self.Wjj_4v.SetPtEtaPhiM(0,0,0,0)

	HlnFat_mass = -999.
	Hlnjj_mass = -999.

	WptOvHfatM = -999
	WptOvHak4M = -999

	Wfat_Sig     = False
	Wfat_SB      = False
	Wfat_Btop    = False

	Wjj_Sig     = False
	Wjj_SB      = False
	Wjj_Btop    = False

	Wlep_mt = -999
	Hlnjj_mt = -999

	IsFatSig = False
	IsFatSB  = False
	IsFatTop = False

	IsJjSig = False
	IsJjSB  = False
	IsJjTop = False

        Lept_col        = Collection(event, 'Lepton')
        #FatJet_col      = Collection(event, 'FatJet')

        CFatJet_col		= Collection(event, 'CleanFatJet')

	CJet_col		= Collection(event, 'CleanJet')
        #CleanJetNotFat_jetIdx   = getattr(event, "CleanJetNotFat_jetIdx")
        CleanJetNotFat_col      = Collection(event, "CleanJetNotFat")


	Jet_col		= Collection(event, 'Jet')

        met_pt         = getattr(event, "MET_pt")

        #IsWlepEvt      = getattr(event, "IsWlepEvt")
        Wlep_pt_PF    = getattr(event, "Wlep_pt_PF")
        Wlep_eta_PF   = getattr(event, "Wlep_eta_PF")
        Wlep_phi_PF   = getattr(event, "Wlep_phi_PF")
        Wlep_mass_PF  = getattr(event,"Wlep_mass_PF")

        Wjj_pt	= getattr(event,"Whad_pt")
        Wjj_eta	= getattr(event,"Whad_eta")
        Wjj_phi	= getattr(event,"Whad_phi")
        Wjj_mass	= getattr(event,"Whad_mass")
        Wjj_ClJet0_idx= getattr(event, "idx_j1")
        Wjj_ClJet1_idx= getattr(event, "idx_j2")

	#if IsWlepEvt != 1: return False
	if Lept_col._len < 1: return False
	CHlnjj  = -999
	if abs(Lept_col[0]['pdgId']) == 11 : CHlnjj = 1
	if abs(Lept_col[0]['pdgId']) == 13 : CHlnjj = 2


	self.Wlep_4v.SetPtEtaPhiM(Wlep_pt_PF,
	                           Wlep_eta_PF,
	                           Wlep_phi_PF,
	                           Wlep_mass_PF
				   )

	# FatJet evet from FatJet module , but need to apply cut further
	for ix in range( CFatJet_col._len ):

	  Wfat_mass = CFatJet_col[ix]['mass']
	  Wfat_pt   = CFatJet_col[ix]['pt']
	  Wfat_eta  = CFatJet_col[ix]['eta']
	  Wfat_phi  = CFatJet_col[ix]['phi']
	  Wfat_tau21= CFatJet_col[ix]['tau21']

	  self.Wfat_4v.SetPtEtaPhiM(Wfat_pt, Wfat_eta, Wfat_phi, Wfat_mass)

	  self.HlnFat_4v = self.Wfat_4v + self.Wlep_4v 
	  HlnFat_mass = self.HlnFat_4v.M()

	  WptOvHfatM = min(Wlep_pt_PF, Wfat_pt)/HlnFat_mass

	  # FatJet Evt Cuts
          # These are already selected in postproduction but to make sure
	  # N-subjettiness tau21 = tau2/tau1
	  cutJ_base = [ Wfat_pt > 200, Wfat_tau21 < 0.45, met_pt > 40, WptOvHfatM > 0.4]
	  if not all(cutJ_base) : continue
	  # Let's stop the loop here, passing cutJ_base, then it become a Sig or a SB for a event.
	  cutJ_SB   = [ Wfat_mass > 40, Wfat_mass < 250]
	  cutJ_Sig  = [ Wfat_mass >= 65, Wfat_mass <= 105]

	  if all(cutJ_Sig): Wfat_Sig = True 
	    
	  if all(cutJ_SB) and not all(cutJ_Sig) : Wfat_SB  = True

	  # b-veto
          # DeepB, bWP='0.2219'
	  for jdx in range( CleanJetNotFat_col._len ):
	    clj_idx = CleanJetNotFat_col[jdx]['jetIdx']
	    jet_idx = CJet_col[ clj_idx ]['jetIdx']
	    if Jet_col[ jet_idx ]['btagDeepB'] > 0.2219:
	      if Jet_col[ jet_idx ]['pt'] > 20:
	        Wfat_Btop = True 

        # W_Ak4 Event ----------------------------
	if (Wfat_Sig == False or Wfat_Btop == True) and (Wjj_mass > -1):
	  # Now it is Wjj event, initialize as all is true

	  self.Wjj_4v.SetPtEtaPhiM(Wjj_pt, Wjj_eta, Wjj_phi, Wjj_mass)
	  self.Hlnjj_4v = self.Wlep_4v + self.Wjj_4v

	  Hlnjj_mass = self.Hlnjj_4v.M()
	  Hlnjj_mt = self.Hlnjj_4v.Mt()
	  WptOvHak4M = min(Wlep_pt_PF, Wjj_pt)/Hlnjj_mass

	  Wlep_mt =  self.Wlep_4v.Mt()

	  cutjj_Base = [ met_pt>30, Wlep_mt>50, Hlnjj_mt > 60, WptOvHak4M > 0.35 ]
	  cutjj_Sig  = [ Wjj_mass > 65 and Wjj_mass < 105 ]
	  cutjj_SB   = [ Wjj_mass > 40 and Wjj_mass < 250 ]

	  if all(cutjj_Base) and all(cutjj_Sig) : Wjj_Sig = True
	  if all(cutjj_Base) and not all(cutjj_Sig) and all(cutjj_SB) : Wjj_SB = True


	  JetIdx0 = CJet_col[Wjj_ClJet0_idx]['jetIdx']
	  JetIdx1 = CJet_col[Wjj_ClJet1_idx]['jetIdx']

	  for jdx in range(Jet_col._len):
	    if jdx == JetIdx0: continue
	    if jdx == JetIdx1: continue
	    if Jet_col[jdx]['pt'] < 20: continue
	    if abs(Jet_col[jdx]['eta']) > 2.4: continue
	    if Jet_col[jdx]['btagDeepB'] > 0.2219: Wjj_Btop = True

	# VBF tag ---------------------------------------
	# Requiring two additional jets with pt > 30 gev, |eta| < 4.7
	# and VBF cuts

	# Save Event ---------------------------------
	# Evet Catagory
	Cat_Fat_Sig = [Wfat_Sig == True, Wfat_Btop == False]
	Cat_Fat_SB  = [Wfat_SB  == True, Wfat_Btop == False]
	Cat_Fat_Btop= [Wfat_Sig == True, Wfat_Btop == True]

	if all(Cat_Fat_Sig) : IsFatSig = True
	if all(Cat_Fat_SB)  : IsFatSB  = True
	if all(Cat_Fat_Btop): IsFatTop = True

	Cat_AK4_Sig = [Wjj_Sig == True, Wjj_Btop == False]
	Cat_AK4_SB  = [Wjj_SB  == True, Wjj_Btop == False]
	Cat_AK4_Btop= [Wjj_Sig == True, Wjj_Btop == True]
	if all(Cat_AK4_Sig) : IsJjSig = True
	if all(Cat_AK4_SB)  : IsJjSB  = True
	if all(Cat_AK4_Btop): IsJjTop = True

	if IsFatSig==False and IsFatSB==False and IsFatTop==False and IsJjSig==False and IsJjSB==False and IsJjTop==False:
	  return False

        self.out.fillBranch( 'CHlnjj' , CHlnjj)
        self.out.fillBranch( 'IsFatSig' , IsFatSig)
        self.out.fillBranch( 'IsFatSB'  , IsFatSB)
        self.out.fillBranch( 'IsFatTop' , IsFatTop)
        self.out.fillBranch( 'IsJjSig' , IsJjSig)
        self.out.fillBranch( 'IsJjSB'  , IsJjSB)
        self.out.fillBranch( 'IsJjTop' , IsJjTop)
        self.out.fillBranch( 'WptOvHfatM' , WptOvHfatM)
        self.out.fillBranch( 'WptOvHak4M' , WptOvHak4M)

        self.out.fillBranch( 'HlnFat_mass' , HlnFat_mass)
        self.out.fillBranch( 'Hlnjj_mass'  , Hlnjj_mass)
        self.out.fillBranch( 'Wlep_mt'   , Wlep_mt)
        self.out.fillBranch( 'Hlnjj_mt'  , Hlnjj_mt)

        return True


    def getDeltaR(self, phi1, eta1, phi2, eta2):
        dphi = phi1 - phi2
        if dphi > ROOT.TMath.Pi(): dphi -= 2*ROOT.TMath.Pi()
        if dphi < -ROOT.TMath.Pi(): dphi += 2*ROOT.TMath.Pi()
        deta = eta1 - eta2
        deltaR = sqrt((deta*deta) + (dphi*dphi))
        return deltaR
    def InvMassCalc(self, pt0, eta0, phi0, mass0, pt1, eta1, phi1, mass1):
        v0 = ROOT.TLorentzVector()
        v1 = ROOT.TLorentzVector()
        v0.SetPtEtaPhiM(pt0, eta0, phi0, mass0)
        v1.SetPtEtaPhiM(pt1, eta1, phi1, mass1)
        InvM01 = (v0 + v1).M()
        return InvM01
    def WlepMetPzCalc(self, leptE, leptPt, leptPz, leptPhi, metPt, metPhi,  ):
        mu = ((Wmass)**2)/2 + leptPt * metPt * math.cos(metPhi-leptPhi)
        ## metPz solution = metPz_1 +-sqrt(metPz_2)
        metPz_1      = mu * leptPz/(leptPt**2)
        metPz_2_pow2 = metPz_1**2 - ( (leptE*metPt)**2 - mu**2 )/(leptPt**2)
        metPz=0
        ##--complex number case
        if metPz_2_pow2 < 0:
            metPz = metPz_1
        ##--real solution    
        else:
            sol1 = metPz_1 + math.sqrt(metPz_2_pow2)
            sol2 = metPz_1 - math.sqrt(metPz_2_pow2)
            if math.fabs(sol1) < math.fabs(sol2):
                metPz = sol1
            else:
                metPz = sol2

        return metPz
 
# define modules using the syntax 'name = lambda : constructor' to avoid having them loaded when not needed                    
HMlnjjVars = lambda : HMlnjjVarsClass()

