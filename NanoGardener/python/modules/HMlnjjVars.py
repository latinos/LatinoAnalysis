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
    def __init__(self,year):
	self.HlnFat_4v  = ROOT.TLorentzVector()
	self.Hlnjj_4v   = ROOT.TLorentzVector()
	self.Wlep_4v   = ROOT.TLorentzVector()
	self.Wfat_4v   = ROOT.TLorentzVector()
	self.Wjj_4v   = ROOT.TLorentzVector()
        print "@@Year->",year
        self.year=year
        # b-tag WP && tau21 (Wtag)
        self.bWP=0.2217 ##2016legacy
        self.tau21WP=0.4 ##2016 legacy
        if '2016' in str(self.year): 
            self.bWP=0.2217   ##https://twiki.cern.ch/twiki/bin/viewauth/CMS/BtagRecommendation2016Legacy
            self.tau21WP=0.4  ##2016 scale factors and corrections
        elif '2017' in str(self.year): 
            self.bWP=0.1522    ##https://twiki.cern.ch/twiki/bin/viewauth/CMS/BtagRecommendation94X
            self.tau21WP=0.45  ##https://twiki.cern.ch/twiki/bin/viewauth/CMS/JetWtagging#tau21_0_45
        elif '2018' in str(self.year):
            self.bWP=0.1241    ##https://twiki.cern.ch/twiki/bin/viewauth/CMS/BtagRecommendation102X
            self.tau21WP=0.45  ##https://twiki.cern.ch/twiki/bin/viewauth/CMS/JetWtagging#tau21_0_45_HP_0_45_tau21_0_75_LP

        # tau21 cut (High purity)
        

    def beginJob(self):
        pass

    def endJob(self):
        pass

    def beginFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        self.out = wrappedOutputTree

        #New Branches ##For Event

        self.out.branch("Flavlnjj" , "I")

        list_myvar=['IsBoostedSR','IsBoostedSB','IsBoostedTopCR','IsResolvedSR','IsResolvedSB','IsResolvedTopCR']
        self.out.branch("IsBoostedTopCR" , "O")
        self.out.branch("IsBoostedSR" , "O")
        self.out.branch("IsBoostedSB"  , "O")

        self.out.branch("IsResolvedTopCR" , "O")
        self.out.branch("IsResolvedSR" , "O")
        self.out.branch("IsResolvedSB"  , "O")


        ##For Boosted Selection ##For FatJet
        list_myvar=['pt','eta','phi','mass','tau21','WptOvHfatM','HlnFat_mass']
        for myvar in list_myvar: 
            
            self.out.branch("CleanFatJetPassMBoostedSR_"+myvar, 'F', lenVar='nCleanFatJetPassMBoostedSR')
            self.out.branch("CleanFatJetPassMBoostedSB_"+myvar, 'F', lenVar='nCleanFatJetPassMBoostedSB')
            


        

        
        
        


        self.out.branch("WptOvHak4M", "F")        
        self.out.branch("Hlnjj_mass" , "F")
        self.out.branch("Wlep_mt" , "F")
        self.out.branch("Hlnjj_mt" , "F")

        self.out.branch("vbfFat_jj_dEta" , "F")
        self.out.branch("vbfFat_jj_mass" , "F")
        self.out.branch("vbfjj_jj_dEta" , "F")
        self.out.branch("vbfjj_jj_mass" , "F")

        self.out.branch("IsVbfFat" , "O")
        self.out.branch("IsVbfjj" , "O")

        #self.out.branch("GenDrAk8Ak4", "F", lenVar="nGenDrAk8Ak4")

    def endFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        pass

    def initReaders(self,tree): # this function gets the pointers to Value and ArrayReaders and sets them in the C++ worker class
        pass


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

        ##--For FatJet Collection in SR/SB/TopCR
        list_myvar=['pt','eta','phi','mass','tau21','WptOvHfatM','HlnFat_mass']
        CleanFatJetPassMBoostedSR={}
        CleanFatJetPassMBoostedSB={}
        #CleanFatJetPassBoostedTopCR={}
        for myvar in list_myvar:
            CleanFatJetPassMBoostedSR[myvar]=[]
            CleanFatJetPassMBoostedSB[myvar]=[]
            


        Wfat_SR = False
        Wfat_SB = False
        Wfat_Btop = False
        Wjj_Btop = False
	
	Hlnjj_mass = -999.
	WptOvHak4M = -999

	Wjj_SR     = False
	Wjj_SB      = False
	Wjj_Btop    = False

	Wlep_mt = -999
	Hlnjj_mt = -999

        ##Event variable
        EventVar={}
        list_myvar=['IsBoostedSR','IsBoostedSB','IsBoostedTopCR','IsResolvedSR','IsResolvedSB','IsResolvedTopCR','IsVbfFat','IsVbfjj']
        for myvar in list_myvar:
            EventVar[myvar]=False

	vbfFat_jj_dEta = -999
	vbfFat_jj_mass = -999
	vbfjj_jj_dEta = -999
	vbfjj_jj_mass = -999

        IsFatSig = False
        IsFatSB = False
        IsFatTop = False
        
        IsJjSig = False
        IsJjSB = False
        IsJjTop = False

        IsVbfFat = False
        IsVbfjj = False
        


        ##--read vars

        Lept_col        = Collection(event, 'Lepton')

        CFatJet_col		= Collection(event, 'CleanFatJet')

	CJet_col		= Collection(event, 'CleanJet')

        CleanJetNotFat_col      = Collection(event, "CleanJetNotFat")


	Jet_col		= Collection(event, 'Jet')

        met_pt         = getattr(event, "MET_pt")

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



        


	if Lept_col._len < 1: return False
	Flavlnjj  = -999
	if abs(Lept_col[0]['pdgId']) == 11 : Flavlnjj = 1
	if abs(Lept_col[0]['pdgId']) == 13 : Flavlnjj = 2


	self.Wlep_4v.SetPtEtaPhiM(Wlep_pt_PF,
	                           Wlep_eta_PF,
	                           Wlep_phi_PF,
	                           Wlep_mass_PF
				   )

        ##Check btagged event or not

        bWP=self.bWP  
        for jdx in range( CleanJetNotFat_col._len ):
            clj_idx = CleanJetNotFat_col[jdx]['jetIdx']
            jet_idx = CJet_col[ clj_idx ]['jetIdx']
	    if Jet_col[ jet_idx ]['btagDeepB'] > bWP:
	      if Jet_col[ jet_idx ]['pt'] > 20:
	        Wfat_Btop = True 





	# FatJet evet from FatJet module , but need to apply cut further

        
	for ix in range( CFatJet_col._len ):

	  Wfat_mass = CFatJet_col[ix]['mass']
	  Wfat_pt   = CFatJet_col[ix]['pt']
	  Wfat_eta  = CFatJet_col[ix]['eta']
	  Wfat_phi  = CFatJet_col[ix]['phi']
	  Wfat_tau21= CFatJet_col[ix]['tau21']

	  self.Wfat_4v.SetPtEtaPhiM(Wfat_pt, Wfat_eta, Wfat_phi, Wfat_mass)

	  self.HlnFat_4v = self.Wfat_4v + self.Wlep_4v 
	  thisHlnFat_mass = self.HlnFat_4v.M()

	  thisWptOvHfatM = min(Wlep_pt_PF, Wfat_pt)/thisHlnFat_mass

	  # FatJet Evt Cuts
          # These are already selected in postproduction but to make sure
	  # N-subjettiness tau21 = tau2/tau1
          ##https://twiki.cern.ch/twiki/bin/viewauth/CMS/JetWtagging#2016_scale_factors_and_correctio , high purity cut
	  cutJ_base = [ Wfat_pt > 200,abs(Wfat_eta)<2.4, Wfat_tau21 < self.tau21WP, thisWptOvHfatM > 0.4]
          #cutJ_base = [ Wfat_pt > 200 abs(Wfat_eta)<2.4, Wfat_mass < 250, Wfat_mass > 40]
	  if not all(cutJ_base) : continue
	  # Let's stop the loop here, passing cutJ_base, then it become a Sig or a SB for a event.
	  cutJ_SB   = [ Wfat_mass > 40, Wfat_mass < 250]
	  cutJ_SR  = [ Wfat_mass >= 65, Wfat_mass <= 105]
          if all(cutJ_SR): ##pass SR msoftdrop cut
              ##Need to use dic type
              CleanFatJetPassMBoostedSR['pt'].append(Wfat_pt)
              CleanFatJetPassMBoostedSR['mass'].append(Wfat_mass)
              CleanFatJetPassMBoostedSR['eta'].append(Wfat_eta)
              CleanFatJetPassMBoostedSR['phi'].append(Wfat_phi)
              CleanFatJetPassMBoostedSR['tau21'].append(Wfat_tau21)
              CleanFatJetPassMBoostedSR['WptOvHfatM'].append(thisWptOvHfatM)
              CleanFatJetPassMBoostedSR['HlnFat_mass'].append(thisHlnFat_mass)
              
          elif all(cutJ_SB): ##pass SB msoftdrop cut
              
              CleanFatJetPassMBoostedSB['pt'].append(Wfat_pt)
              CleanFatJetPassMBoostedSB['mass'].append(Wfat_mass)
              CleanFatJetPassMBoostedSB['eta'].append(Wfat_eta)
              CleanFatJetPassMBoostedSB['phi'].append(Wfat_phi)
              CleanFatJetPassMBoostedSB['tau21'].append(Wfat_tau21)
              CleanFatJetPassMBoostedSB['WptOvHfatM'].append(thisWptOvHfatM)
              CleanFatJetPassMBoostedSB['HlnFat_mass'].append(thisHlnFat_mass)

        Wfat_SR=(len(CleanFatJetPassMBoostedSR['pt']) > 0 )
        Wfat_SB=(len(CleanFatJetPassMBoostedSB['pt']) > 0 )
        # W_Ak4 Event ----------------------------
	#if (Wfat_SR == False or Wfat_Btop == True) and (Wjj_mass > -1):
        if ( ( not Wfat_SR ) and ((Wjj_ClJet0_idx != -1) or (Wjj_ClJet1_idx != -1)) ) : ##No FatJet passing final boosted cut and no resolved Whad candidate
	  # Now it is Wjj event, initialize as all is true

	  self.Wjj_4v.SetPtEtaPhiM(Wjj_pt, Wjj_eta, Wjj_phi, Wjj_mass)
	  self.Hlnjj_4v = self.Wlep_4v + self.Wjj_4v

	  Hlnjj_mass = self.Hlnjj_4v.M()
	  Hlnjj_mt = self.Hlnjj_4v.Mt()
	  WptOvHak4M = min(Wlep_pt_PF, Wjj_pt)/Hlnjj_mass

          Wlep_mt =  self.Wlep_4v.Mt()

          #cutjj_Base = [ met_pt>30, Wlep_mt>50, Hlnjj_mt > 60, WptOvHak4M > 0.35 ]
          cutjj_Base = [ Wlep_mt>50, Wjj_mass > 40 and Wjj_mass < 250, Hlnjj_mt > 60, WptOvHak4M > 0.35 ]
	  cutjj_SR  = [ Wjj_mass > 65 and Wjj_mass < 105 ]
          cutjj_SB  = [ ( Wjj_mass > 40 and Wjj_mass < 65) or (Wjj_mass > 105 and Wjj_mass < 250 ) ]
            
          if all(cutjj_Base) and all(cutjj_SR) : Wjj_SR = True
	  if all(cutjj_Base) and all(cutjj_SB) : Wjj_SB = True

          JetIdx0 = CJet_col[Wjj_ClJet0_idx]['jetIdx']
          JetIdx1 = CJet_col[Wjj_ClJet1_idx]['jetIdx']
          for jdx in range(Jet_col._len):
	    if jdx == JetIdx0: continue
	    if jdx == JetIdx1: continue
	    if Jet_col[jdx]['pt'] < 20: continue
	    if abs(Jet_col[jdx]['eta']) > 2.4: continue
	    if Jet_col[jdx]['btagDeepB'] > bWP: Wjj_Btop = True







	# Save Event ---------------------------------
	# Evet Catagory
        Cat_Fat_Btop= [Wfat_SR == True, Wfat_Btop == True, met_pt > 40]
        Cat_Fat_Sig = [Wfat_SR == True, Wfat_Btop == False, met_pt > 40]
        Cat_Fat_SB  = [Wfat_SB  == True, Wfat_Btop == False, met_pt > 40]
        

	if all(Cat_Fat_Sig) : IsFatSig = True
	if all(Cat_Fat_SB)  : IsFatSB  = True
	if all(Cat_Fat_Btop): IsFatTop = True

        Cat_AK4_Btop= [Wjj_SR == True, Wjj_Btop == True, met_pt >30]
        Cat_AK4_Sig = [Wjj_SR == True, Wjj_Btop == False, met_pt > 30]
        Cat_AK4_SB  = [Wjj_SB  == True, Wjj_Btop == False, met_pt > 30]

	if all(Cat_AK4_Sig) : IsJjSig = True
	if all(Cat_AK4_SB)  : IsJjSB  = True
	if all(Cat_AK4_Btop): IsJjTop = True

        EventVar['IsBoostedSR'] = IsFatSig
        EventVar['IsBoostedSB'] = IsFatSB
        EventVar['IsBoostedTopCR'] = IsFatTop

        EventVar['IsResolvedSR'] = IsJjSig
        EventVar['IsResolvedSB'] = IsJjSB
        EventVar['IsResolvedTopCR'] = IsJjTop


	# VBF tag ---------------------------------------
	# Requiring two additional jets with pt > 30 gev, |eta| < 4.7
	# and VBF cuts
        
	# lnJ case--------
        lnJ_addJet_pt = []
        lnJ_addJet_eta = []
        lnJ_addJet_phi = []
        lnJ_addJet_mass = []
        lnJ_addJet_jid = []

	nlnJ_addJet = 0
	if IsFatSig or IsFatSB or IsFatTop:
	  for jdx in range(CleanJetNotFat_col._len):
	    clj_i = CleanJetNotFat_col[jdx]['jetIdx']
	    if ( CJet_col[clj_i]['pt'] < 30 ) or ( abs(CJet_col[clj_i]['eta'])>4.7 ): continue
	    lnJ_addJet_pt.append(CJet_col[clj_i]['pt'])
	    lnJ_addJet_eta.append(CJet_col[clj_i]['eta'])
	    lnJ_addJet_phi.append(CJet_col[clj_i]['phi'])
	    lnJ_addJet_mass.append(Jet_col[CJet_col[clj_i]['jetIdx']]['mass'])
	    lnJ_addJet_jid.append(Jet_col[CJet_col[clj_i]['jetIdx']]['jetId'])
	    nlnJ_addJet +=1

	  if nlnJ_addJet > 1:
	    for i in range(nlnJ_addJet):
	      for j in range(nlnJ_addJet):
	        dEta_tmp = abs(lnJ_addJet_eta[i] - lnJ_addJet_eta[j])
		mass_tmp = self.InvMassCalc(lnJ_addJet_pt[i],lnJ_addJet_eta[i],lnJ_addJet_phi[i],lnJ_addJet_mass[i],
		  lnJ_addJet_pt[j],lnJ_addJet_eta[j],lnJ_addJet_phi[j],lnJ_addJet_mass[j])
		if dEta_tmp > 3.5:
		  if mass_tmp > vbfFat_jj_mass:
		    vbfFat_jj_dEta = dEta_tmp
		    vbfFat_jj_mass = mass_tmp
	    if vbfFat_jj_mass > 500:
	      IsVbfFat = True

	# lnjj case ---------
        lnjj_addJet_pt = []
        lnjj_addJet_eta = []
        lnjj_addJet_phi = []
        lnjj_addJet_mass = []
        lnjj_addJet_jid = []
	nlnjj_addJet = 0
	if IsJjSig or IsJjSB or IsJjTop:
	  for ci in range(CJet_col._len):
	    # check if it is used
	    if ci == Wjj_ClJet0_idx : continue
	    if ci == Wjj_ClJet1_idx : continue
	    if ( CJet_col[ci]['pt'] < 30 ) or ( abs(CJet_col[ci]['eta'])>4.7 ): continue
	    lnjj_addJet_pt.append  (CJet_col[ci]['pt'])
	    lnjj_addJet_eta.append (CJet_col[ci]['eta'])
	    lnjj_addJet_phi.append (CJet_col[ci]['phi'])
	    lnjj_addJet_mass.append(Jet_col[CJet_col[ci]['jetIdx']]['mass'])
	    lnjj_addJet_jid.append (Jet_col[CJet_col[ci]['jetIdx']]['jetId'])
	    nlnjj_addJet +=1

	  if nlnjj_addJet > 1:
	    for i in range(nlnjj_addJet):
	      for j in range(nlnjj_addJet):
	        dEta_tmp = abs(lnjj_addJet_eta[i] - lnjj_addJet_eta[j])
		mass_tmp = self.InvMassCalc(lnjj_addJet_pt[i],lnjj_addJet_eta[i],lnjj_addJet_phi[i],lnjj_addJet_mass[i],
		                       lnjj_addJet_pt[j],lnjj_addJet_eta[j],lnjj_addJet_phi[j],lnjj_addJet_mass[j])
		if dEta_tmp > 3.5:
		  if mass_tmp > vbfjj_jj_mass:
		    vbfjj_jj_dEta = dEta_tmp
		    vbfjj_jj_mass = mass_tmp
	    if vbfjj_jj_mass > 500:
	      IsVbfjj = True

        EventVar['IsVbfFat'] = IsVbfFat
        EventVar['IsVbfjj'] = IsVbfjj
        


	if IsFatSig==False and IsFatSB==False and IsFatTop==False and IsJjSig==False and IsJjSB==False and IsJjTop==False:
	  return False
        


        self.out.fillBranch( 'Flavlnjj' , Flavlnjj)
        ##--Event Categorization--##
        list_myvar=['IsBoostedSR','IsBoostedSB','IsBoostedTopCR','IsResolvedSR','IsResolvedSB','IsResolvedTopCR','IsVbfFat','IsVbfjj']
        for myvar in list_myvar:
            self.out.fillBranch( myvar, EventVar[myvar] )

        ##--Boosted FatJet--##
        list_myvar=['pt','eta','phi','mass','tau21','WptOvHfatM','HlnFat_mass']
        for myvar in list_myvar:
            self.out.fillBranch( "CleanFatJetPassMBoostedSR_"+myvar , CleanFatJetPassMBoostedSR[myvar])
            self.out.fillBranch( "CleanFatJetPassMBoostedSB_"+myvar , CleanFatJetPassMBoostedSB[myvar])




        self.out.fillBranch( 'Wlep_mt'   , Wlep_mt)
        self.out.fillBranch( 'Hlnjj_mt'  , Hlnjj_mt)

        self.out.fillBranch( 'vbfFat_jj_dEta'    , vbfFat_jj_dEta)
        self.out.fillBranch( 'vbfFat_jj_mass'  , vbfFat_jj_mass)
        self.out.fillBranch( 'vbfjj_jj_dEta'    , vbfjj_jj_dEta)
        self.out.fillBranch( 'vbfjj_jj_mass'  , vbfjj_jj_mass)

        self.out.fillBranch( 'Hlnjj_mass', Hlnjj_mass )
        self.out.fillBranch( 'WptOvHak4M', WptOvHak4M )

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

