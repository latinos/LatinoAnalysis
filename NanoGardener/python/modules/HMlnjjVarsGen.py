import ROOT
import math
ROOT.PyConfig.IgnoreCommandLineOptions = True
import re
import os
from math import sqrt

from PhysicsTools.NanoAODTools.postprocessing.framework.datamodel import Collection
from PhysicsTools.NanoAODTools.postprocessing.framework.eventloop import Module

Wmass=80.4

class HMlnjjVarsGen(Module):

    def __init__(self,dataMc):
        self.DataMc = dataMc
	self.GenH_v4  = ROOT.TLorentzVector()
	self.gSingleLept_v4 = ROOT.TLorentzVector()
	self.gMet_v4  = ROOT.TLorentzVector()
	self.gW_Lept_v4 = ROOT.TLorentzVector()
	self.gW_Ak8_v4 = ROOT.TLorentzVector()
	self.gW_Ak4_v4 = ROOT.TLorentzVector()

    def beginJob(self):
        pass

    def endJob(self):
        pass

    def beginFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        self.out = wrappedOutputTree

        #New Branches
        if self.DataMc == 'MC':
          self.out.branch("GenEvtFlag", "I")
          self.out.branch("GenDrAk8Ak4", "F", lenVar="nGenDrAk8Ak4")
          self.out.branch("GenDrAk8Lept", "F")
          self.out.branch("GenW_Lept_pt", "F")
          self.out.branch("GenW_Lept_eta", "F")
          self.out.branch("GenW_Lept_phi", "F")
          self.out.branch("GenW_Lept_mass", "F")
          self.out.branch("GenW_Ak8_mass", "F")
          self.out.branch("GenW_Ak4_mass", "F")
          self.out.branch("GenH_pt", "F")
          self.out.branch("GenH_eta", "F")
          self.out.branch("GenH_phi", "F")
          self.out.branch("GenH_mass", "F")

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
	self.GenH_v4.SetPtEtaPhiM(0,0,0,0)
	self.gSingleLept_v4.SetPtEtaPhiM(0,0,0,0)
	self.gMet_v4.SetPtEtaPhiM(0,0,0,0)
	self.gW_Lept_v4.SetPtEtaPhiM(0,0,0,0)
	self.gW_Ak8_v4.SetPtEtaPhiM(0,0,0,0)
	self.gW_Ak4_v4.SetPtEtaPhiM(0,0,0,0)

        Lept_col        = Collection(event, 'Lepton')
        CleanJet_col    = Collection(event, 'CleanJet')
        FatJet_col      = Collection(event, 'FatJet')

        if self.DataMc == 'MC':
          genSemiLeptFatJetEvt = False
          genSemiLeptResolvEvt = False
	  genIsAk8_B_evt = False
	  genIsAk4_B_evt = False
          # accepted jet idx
          fidJetIdx = []
          gAk4_idx0 = 999
          gAk4_idx1 = 999
          dRAk8Ak4_list = []
          dRAk8Lept = -999
          dRAk4Lept = [-1] *2
          GenDressedLept_col    = Collection(event, 'GenDressedLepton')
          GenAK4_col            = Collection(event, 'GenJet')
          GenAK8_col            = Collection(event, 'GenJetAK8')
          gMet_pt   = getattr(event, "GenMET_pt")
          gMet_phi  = getattr(event, "GenMET_phi")
          # For single lepton evt
          singleLeptEvt = False
          gSingleLept_id  = -999
          gSingleLept_pt  = -1000
          gSingleLept_eta = -999
          gSingleLept_phi = -999

          for idx in range(GenDressedLept_col._len):
            gLept_id = GenDressedLept_col[idx]['pdgId']
            gLept_pt = GenDressedLept_col[idx]['pt']
            gLept_eta = GenDressedLept_col[idx]['eta']
            gLept_phi = GenDressedLept_col[idx]['phi']
            if not singleLeptEvt:
              if gLept_pt > 30:
                if abs(gLept_id) == 11:
                  if abs(gLept_eta) < 2.1:
                    singleLeptEvt = True
                    gSingleLept_id = gLept_id
                    gSingleLept_pt = gLept_pt
                    gSingleLept_eta = gLept_eta
                    gSingleLept_phi = gLept_phi
                    continue
                elif abs(gLept_id) == 13:
                  if abs(gLept_eta) < 2.4:
                    singleLeptEvt = True
                    gSingleLept_id = gLept_id
                    gSingleLept_pt = gLept_pt
                    gSingleLept_eta = gLept_eta
                    gSingleLept_phi = gLept_phi
                    continue
                else:
                  continue
            # check additional lepton
            if singleLeptEvt == True :
              if abs(gLept_id) == 11:
                if abs(gLept_eta) < 2.1 and gLept_pt > 15:
                  singleLeptEvt = False
                  break
              elif abs(gLept_id) == 13:
                if abs(gLept_eta) < 2.4 and gLept_pt > 10:
                  singleLeptEvt = False
                  break
              else : pass
          # Only for single lepton evt ##############################
          if singleLeptEvt :
            # Wleptonic decay recon
            gSingleLept_px = gSingleLept_pt*math.cos(gSingleLept_phi)
            gSingleLept_py = gSingleLept_pt*math.sin(gSingleLept_phi)
            gSingleLept_pz = gSingleLept_pt*math.sinh(gSingleLept_eta) ##pz = pt*sinh(eta)
            gSingleLept_E  = gSingleLept_pt*math.cosh(gSingleLept_eta) ## p = pt*cosh(eta)
            self.gSingleLept_v4.SetPxPyPzE(gSingleLept_px, gSingleLept_py, gSingleLept_pz, gSingleLept_E)
            gMet_px = gMet_pt*math.cos(gMet_phi)
            gMet_py = gMet_pt*math.sin(gMet_phi)
            gMet_pz = self.WlepMetPzCalc( gSingleLept_E, gSingleLept_pt, gSingleLept_pz, gSingleLept_phi,
                gMet_pt, gMet_phi)
            gMet_E  = math.sqrt(gMet_pz**2 + gMet_pt**2)
            self.gMet_v4.SetPxPyPzE(gMet_px, gMet_py, gMet_pz, gMet_E)

            # Check if Boosted Evt ########################
            for igAk8 in range(GenAK8_col._len):
	      if genIsAk8_B_evt : break
              if genSemiLeptFatJetEvt : break
              gW_Ak8_pt    = GenAK8_col[igAk8]['pt']
              gW_Ak8_eta   = GenAK8_col[igAk8]['eta']
              gW_Ak8_phi   = GenAK8_col[igAk8]['phi']
              gW_Ak8_mass  = GenAK8_col[igAk8]['mass']
              if gW_Ak8_pt < 200: continue
              if abs(gW_Ak8_eta) > 2.4: continue
              genSemiLeptFatJetEvt = True

              dRAk8Lept = self.getDeltaR(gW_Ak8_phi,  gW_Ak8_eta, gSingleLept_phi, gSingleLept_eta)

              for igAk4 in range(GenAK4_col._len):
                gAk4_pt 	= GenAK4_col[igAk4]['pt']
                gAk4_eta        = GenAK4_col[igAk4]['eta']
                gAk4_phi        = GenAK4_col[igAk4]['phi']
                gAk4_id         = GenAK4_col[igAk4]['partonFlavour']
                if abs(gAk4_eta) > 2.4: continue
                dRAk8Ak4 = self.getDeltaR(gW_Ak8_phi,  gW_Ak8_eta, gAk4_phi, gAk4_eta)
	        # b-veto for W_Ak8 evet
		if dRAk8Ak4 > 0.8 and abs(gAk4_id) == 5 and gAk4_pt > 20:
		  genIsAk8_B_evt = True
		  genSemiLeptFatJetEvt = False
		  break
                elif gAk4_pt > 30:
                  dRAk8Ak4_list.append( dRAk8Ak4 )
		else: pass

            # Check if Resolved Evt ####################################
            if not genSemiLeptFatJetEvt and not genIsAk8_B_evt:
              for idx in range(GenAK4_col._len):
                gAk4_0_pt               = GenAK4_col[idx]['pt']
                gAk4_0_eta      = GenAK4_col[idx]['eta']
                if gAk4_0_pt < 30: continue
                if abs(gAk4_0_eta) > 2.4: continue
                fidJetIdx.append(idx)
              # Pairing Ak4s
              dM = 9999.
              for idx in fidJetIdx:
                for jdx in fidJetIdx:
                  if jdx <= idx: continue
                  gAk4_0_pt     = GenAK4_col[idx]['pt']
                  gAk4_0_eta    = GenAK4_col[idx]['eta']
                  gAk4_0_phi    = GenAK4_col[idx]['phi']
                  gAk4_0_mass   = GenAK4_col[idx]['mass']

                  gAk4_1_pt     = GenAK4_col[jdx]['pt']
                  gAk4_1_eta    = GenAK4_col[jdx]['eta']
                  gAk4_1_phi    = GenAK4_col[jdx]['phi']
                  gAk4_1_mass   = GenAK4_col[jdx]['mass']
                  WhadMass = self.InvMassCalc(gAk4_0_pt, gAk4_0_eta, gAk4_0_phi, gAk4_0_mass,
                                              gAk4_1_pt, gAk4_1_eta, gAk4_1_phi, gAk4_1_mass)
                  if abs(WhadMass - Wmass) < dM:
                    genSemiLeptResolvEvt = True
                    dM = abs(WhadMass - Wmass)
                    gAk4_idx0 = idx
                    gAk4_idx1 = jdx
	      # Check if b-event
              for idx in range(GenAK4_col._len):
                gAk4_0_pt       = GenAK4_col[idx]['pt']
                gAk4_0_eta      = GenAK4_col[idx]['eta']
                gAk4_0_id       = GenAK4_col[idx]['partonFlavour']
		if idx == gAk4_idx0 or idx == gAk4_idx1: continue
                if gAk4_0_pt < 20: continue
                if abs(gAk4_0_eta) > 2.4: continue
                if abs(gAk4_0_id) == 5:
		  genIsAk4_B_evt = True
                  genSemiLeptResolvEvt = False
		  break

              if genSemiLeptResolvEvt:
                gResJet_0_pt    = GenAK4_col[gAk4_idx0]['pt']
                gResJet_0_eta   = GenAK4_col[gAk4_idx0]['eta']
                gResJet_0_phi   = GenAK4_col[gAk4_idx0]['phi']
                gResJet_0_mass  = GenAK4_col[gAk4_idx0]['mass']
                gW_Ak4_v4_0 = ROOT.TLorentzVector()
                gW_Ak4_v4_0.SetPtEtaPhiM(gResJet_0_pt, gResJet_0_eta, gResJet_0_phi, gResJet_0_mass)
                gResJet_1_pt    = GenAK4_col[gAk4_idx1]['pt']
                gResJet_1_eta   = GenAK4_col[gAk4_idx1]['eta']
                gResJet_1_phi   = GenAK4_col[gAk4_idx1]['phi']
                gResJet_1_mass  = GenAK4_col[gAk4_idx1]['mass']
                gW_Ak4_v4_1 = ROOT.TLorentzVector()
                gW_Ak4_v4_1.SetPtEtaPhiM(gResJet_1_pt, gResJet_1_eta, gResJet_1_phi, gResJet_1_mass)
		self.gW_Ak4_v4 = gW_Ak4_v4_0 + gW_Ak4_v4_1
                dRAk4Lept[0] = self.getDeltaR(gResJet_0_phi,  gResJet_0_eta, gSingleLept_phi, gSingleLept_eta)
                dRAk4Lept[1] = self.getDeltaR(gResJet_0_phi,  gResJet_0_eta, gSingleLept_phi, gSingleLept_eta)


          if genSemiLeptFatJetEvt or  genSemiLeptResolvEvt:
            # wLeptonic 4 vector
            self.gW_Lept_v4 = self.gSingleLept_v4 + self.gMet_v4
            gW_Lept_dict = {}
            gW_Lept_dict['pt']   = self.gW_Lept_v4.Pt()
            gW_Lept_dict['eta']  = self.gW_Lept_v4.Eta()
            gW_Lept_dict['phi']  = self.gW_Lept_v4.Phi()
            gW_Lept_dict['mass'] = self.gW_Lept_v4.M()
            for var in gW_Lept_dict:
              self.out.fillBranch( 'GenW_Lept_' + var, gW_Lept_dict[var])

          if genSemiLeptFatJetEvt:
            # H+ mass recon
            #gW_Ak8_px = gAk8_pt*math.cos(gAk8_phi)
            #gW_Ak8_py = gAk8_pt*math.sin(gAk8_phi)
            #gW_Ak8_pz = gAk8_pt*math.sinh(gAk8_eta) ##pz = pt*sinh(eta)
            self.gW_Ak8_v4.SetPtEtaPhiM(gW_Ak8_pt, gW_Ak8_eta, gW_Ak8_phi, gW_Ak8_mass)

            self.GenH_v4 = self.gW_Lept_v4 + self.gW_Ak8_v4
            self.out.fillBranch("GenEvtFlag", 1)
            self.out.fillBranch("GenDrAk8Lept", dRAk8Lept)
            self.out.fillBranch("GenH_pt",  self.GenH_v4.Pt() )
            self.out.fillBranch("GenH_eta", self.GenH_v4.Eta() )
            self.out.fillBranch("GenH_phi", self.GenH_v4.Phi() )
            self.out.fillBranch("GenH_mass",self.GenH_v4.M() )
            self.out.fillBranch("GenW_Ak8_mass", gW_Ak8_mass )

          elif genSemiLeptResolvEvt:
            self.GenH_v4 = self.gW_Lept_v4 + self.gW_Ak4_v4

            self.out.fillBranch("GenEvtFlag", 2)
            self.out.fillBranch("GenH_pt",  self.GenH_v4.Pt() )
            self.out.fillBranch("GenH_eta", self.GenH_v4.Eta() )
            self.out.fillBranch("GenH_phi", self.GenH_v4.Phi() )
            self.out.fillBranch("GenH_mass",self.GenH_v4.M() )
            self.out.fillBranch("GenW_Ak4_mass", self.gW_Ak4_v4.M())
	  else :
            self.out.fillBranch("GenEvtFlag", 0)


          self.out.fillBranch("GenDrAk8Ak4", dRAk8Ak4_list)


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
HMlnjjVarsGen = lambda : HMlnjjVarsGen()

