#!/usr/bin/env python
import os, sys
import ROOT
ROOT.PyConfig.IgnoreCommandLineOptions = True
from importlib import import_module
from PhysicsTools.NanoAODTools.postprocessing.framework.postprocessor import PostProcessor


from PhysicsTools.NanoAODTools.postprocessing.framework.datamodel import Collection
from PhysicsTools.NanoAODTools.postprocessing.framework.eventloop import Module

if __name__ == '__main__':
    print '''
___________________________________________________________________________________
                    ______     ____
\          //  //  |_____/    |____|   \|/
 \  //\   //  //      //      ||       /|\             
  \//  \ //  //      //___    ||  |-|
   \    \/  //      //____|   ||__| |
___________________________________________________________________________________
'''


class WGammaStar(Module):
    def __init__(self):
        self.pLeptState1 = [0,0,0,0]
        self.lept1_4V = ROOT.TLorentzVector()
        self.lept2_4V = ROOT.TLorentzVector()
        self.tmp4V_1 = ROOT.TLorentzVector()
        self.tmp4V_2 = ROOT.TLorentzVector()
    def beginJob(self,histFile=None,histDirName=None):
	pass
    def Daughters(self,genParticles,pdgid):
        daught_par = [];
        if((pdgid >= 1 and pdgid <= 6) or pdgid ==21):
            for particle in genParticles:
                if(particle.genPartIdxMother < 0) :
                   continue
                if(abs(genParticles[particle.genPartIdxMother].pdgId) == pdgid):
                   daught_par.append(particle)
        else :
            for particle in genParticles:
                if(particle.genPartIdxMother < 0) :
                   continue
                if(particle.status==1 and abs(genParticles[particle.genPartIdxMother].pdgId) == pdgid):
                   daught_par.append(particle)
        return daught_par

    def LeptFromW(self,daughters,isMuon):
        nLeptFromW=0
        daughterLeptonsFromW=[]
        for daughter in daughters:
            if(isMuon and (abs(daughter.pdgId)==13)):
                daughterLeptonsFromW.append(daughter)
                nLeptFromW+=1
            if((not isMuon) and (abs(daughter.pdgId)==11)):
                daughterLeptonsFromW.append(daughter)
                nLeptFromW+=1
        return nLeptFromW,daughterLeptonsFromW
    
    def deltaR (self,eta1,eta2,phi1,phi2):
        deltaEta = eta1 - eta2
        deltaPhi = phi1 - phi2
        while (deltaPhi >= ROOT.TMath.Pi()):
            deltaPhi = deltaPhi - 2*ROOT.TMath.Pi()
        while (deltaPhi < -ROOT.TMath.Pi()) :
            deltaPhi = deltaPhi + 2*ROOT.TMath.Pi()
        dR = ROOT.TMath.Sqrt(deltaEta**2 + deltaPhi**2)
        return dR

    def beginFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        self.out = wrappedOutputTree
        self.newbranchesF = [
        'Gen_ZGstar_mu1_pt',  
        'Gen_ZGstar_mu1_eta', 
        'Gen_ZGstar_mu1_phi', 
        'Gen_ZGstar_mu2_pt',  
        'Gen_ZGstar_mu2_eta',
        'Gen_ZGstar_mu2_phi',
        'Gen_ZGstar_ele1_pt',
        'Gen_ZGstar_ele1_eta',
        'Gen_ZGstar_ele1_phi',
        'Gen_ZGstar_ele2_pt',
        'Gen_ZGstar_ele2_eta',
        'Gen_ZGstar_ele2_phi',
        'Gen_ZGstar_mass',
        'Gen_ZGstar_deltaR'
         ]
        self.newbranchesI = [
        "Gen_ZGstar_MomId",
        "Gen_ZGstar_MomStatus"
        ]
        
        for nameBranchesF in self.newbranchesF :
          self.out.branch(nameBranchesF  ,  "F");
        for nameBranchesI in self.newbranchesI :
          self.out.branch(nameBranchesI  ,  "I");

    def analyze(self, event):
        genParticles = Collection(event, "GenPart")
        pLeptMom = -1
        isMuon = False
        genDiLeptMassZGstar = -9999.0
        _ZGstarDiLept_DelaR = -9999.0
        elec1FromGstar_pt   = -9999.0
        elec1FromGstar_eta  = -9999.0
        elec1FromGstar_phi  = -9999.0
        elec2FromGstar_pt   = -9999.0
        elec2FromGstar_eta  = -9999.0
        elec2FromGstar_phi  = -9999.0
        muon1FromGstar_pt   = -9999.0
        muon1FromGstar_eta  = -9999.0
        muon1FromGstar_phi  = -9999.0
        muon2FromGstar_pt   = -9999.0
        muon2FromGstar_eta  = -9999.0
        muon2FromGstar_phi  = -9999.0
        mom_pdgId           = 9999
        mom_status          = 9999
	for particle  in genParticles :
	  pdg_Id = abs(particle.pdgId)
          if ( pdg_Id == 11 and particle.status == 1)  : 
	    if (particle.genPartIdxMother < 0) :
               continue
            else :
                pLeptMom = particle.genPartIdxMother  #index to mother
                while (abs(genParticles[pLeptMom].pdgId) == 11) : 
	           if (genParticles[pLeptMom].genPartIdxMother < 0) :
                      break
                   else :
                      pLeptMom = genParticles[pLeptMom].genPartIdxMother
            isMuon = False
            mom_pdgId = genParticles[pLeptMom].pdgId
            mom_status = genParticles[pLeptMom].status
          elif(pdg_Id == 13 and particle.status == 1)  : 
	    if (particle.genPartIdxMother < 0) :
               continue
            else :
                pLeptMom = particle.genPartIdxMother  #index to mother
                while (abs(genParticles[pLeptMom].pdgId) == 13) : 
	           if (genParticles[pLeptMom].genPartIdxMother < 0) :
                      break
                   else :
                      pLeptMom = genParticles[pLeptMom].genPartIdxMother
            isMuon = True
            mom_pdgId = genParticles[pLeptMom].pdgId
            mom_status = genParticles[pLeptMom].status
          else :
              continue
          if(abs(genParticles[pLeptMom].pdgId)==24):  
              daughters = self.Daughters(genParticles,24) 
              if(not (len(daughters)==4)) : 
                  continue
              nLeptFromW,daughterLeptonsFromW = self.LeptFromW(daughters,isMuon)
              if((len(daughterLeptonsFromW)==2)) : 
                  if(daughterLeptonsFromW[0].pdgId * daughterLeptonsFromW[1].pdgId > 0):
                      continue
                  self.pLeptState1[0] = daughterLeptonsFromW[0]
                  self.pLeptState1[1] = daughterLeptonsFromW[1]
                  if(isMuon):
                      muon1FromGstar_pt     = self.pLeptState1[0].pt
                      muon1FromGstar_eta    = self.pLeptState1[0].eta
                      muon1FromGstar_phi    = self.pLeptState1[0].phi
                      muon2FromGstar_pt     = self.pLeptState1[1].pt
                      muon2FromGstar_eta    = self.pLeptState1[1].eta
                      muon2FromGstar_phi    = self.pLeptState1[1].phi

                      self.lept1_4V.SetPtEtaPhiM(muon1FromGstar_pt,muon1FromGstar_eta,muon1FromGstar_phi,0.106)
                      self.lept2_4V.SetPtEtaPhiM(muon2FromGstar_pt,muon2FromGstar_eta,muon2FromGstar_phi,0.106)
                  else :
                      elec1FromGstar_pt     = self.pLeptState1[0].pt
                      elec1FromGstar_eta    = self.pLeptState1[0].eta
                      elec1FromGstar_phi    = self.pLeptState1[0].phi
                      elec2FromGstar_pt     = self.pLeptState1[1].pt
                      elec2FromGstar_eta    = self.pLeptState1[1].eta
                      elec2FromGstar_phi    = self.pLeptState1[1].phi
                      self.lept1_4V.SetPtEtaPhiM(elec1FromGstar_pt,elec1FromGstar_eta,elec1FromGstar_phi,0.0005)
                      self.lept2_4V.SetPtEtaPhiM(elec2FromGstar_pt,elec2FromGstar_eta,elec2FromGstar_phi,0.0005)
                  _ZGstarDiLept_DelaR = self.deltaR(self.pLeptState1[0].eta,self.pLeptState1[1].eta,self.pLeptState1[0].phi,self.pLeptState1[1].phi)
                  genDiLeptMassZGstar = (self.lept1_4V + self.lept2_4V).M()
              elif((len(daughterLeptonsFromW)==3)) :
                  self.pLeptState1[0] = daughterLeptonsFromW[0]
                  self.pLeptState1[1] = daughterLeptonsFromW[1]
                  self.pLeptState1[2] = daughterLeptonsFromW[2]
                  genDiLeptMassZGstar = 100000000.0
                  for i in range(0,3):
                      for j in range(0,3):
                          if(i>=j):
                              continue
                          if(self.pLeptState1[i].pdgId*self.pLeptState1[j].pdgId > 0):
                              continue
                          if(isMuon):
                              self.tmp4V_1.SetPtEtaPhiM(self.pLeptState1[i].pt,self.pLeptState1[i].eta,self.pLeptState1[i].phi,0.106)
                              self.tmp4V_2.SetPtEtaPhiM(self.pLeptState1[j].pt,self.pLeptState1[j].eta,self.pLeptState1[j].phi,0.106)
                          else :
                              self.tmp4V_1.SetPtEtaPhiM(self.pLeptState1[i].pt,self.pLeptState1[i].eta,self.pLeptState1[i].phi,0.0005)
                              self.tmp4V_2.SetPtEtaPhiM(self.pLeptState1[j].pt,self.pLeptState1[j].eta,self.pLeptState1[j].phi,0.0005)
                          tmpInvM = (self.tmp4V_1 + self.tmp4V_2).M()
                          if(tmpInvM < genDiLeptMassZGstar):
                              genDiLeptMassZGstar = tmpInvM
                              if(isMuon):
                                  muon1FromGstar_pt     = self.pLeptState1[i].pt
                                  muon1FromGstar_eta    = self.pLeptState1[i].eta
                                  muon1FromGstar_phi    = self.pLeptState1[i].phi
                                  muon2FromGstar_pt     = self.pLeptState1[j].pt
                                  muon2FromGstar_eta    = self.pLeptState1[j].eta
                                  muon2FromGstar_phi    = self.pLeptState1[j].phi
                              else:
                                  elec1FromGstar_pt     = self.pLeptState1[i].pt
                                  elec1FromGstar_eta    = self.pLeptState1[i].eta
                                  elec1FromGstar_phi    = self.pLeptState1[i].phi
                                  elec2FromGstar_pt     = self.pLeptState1[j].pt
                                  elec2FromGstar_eta    = self.pLeptState1[j].eta
                                  elec2FromGstar_phi    = self.pLeptState1[j].phi
                              _ZGstarDiLept_DelaR = self.deltaR(self.pLeptState1[i].eta,self.pLeptState1[j].eta,self.pLeptState1[i].phi,self.pLeptState1[j].phi)
                              genDiLeptMassZGstar = (self.lept1_4V + self.lept2_4V).M()
              else :
                  continue
          elif(abs(genParticles[pLeptMom].pdgId) == 23 or abs(genParticles[pLeptMom].pdgId) == 22) :
              daughters = []
              if(abs(genParticles[pLeptMom].pdgId) == 23):
                  daughters = self.Daughters(genParticles,23)
              else:
                  daughters = self.Daughters(genParticles,22)
              if(len(daughters) != 2):
                  continue
              nLeptFromZ = 0
              for i in range(len(daughters)):
                  if(isMuon and abs(daughters[i].pdgId) == 13):
                      nLeptFromZ+=1
                  if(not isMuon and abs(daughters[i].pdgId) == 11):
                      nLeptFromZ+=1
              
              if(nLeptFromZ == 2):
                  if(daughters[0].pdgId * daughters[1].pdgId > 0):
                      continue
                  self.pLeptState1[0] = daughters[0]
                  self.pLeptState1[1] = daughters[1]
                  if(isMuon):
                      muon1FromGstar_pt     = self.pLeptState1[0].pt
                      muon1FromGstar_eta    = self.pLeptState1[0].eta
                      muon1FromGstar_phi    = self.pLeptState1[0].phi
                      muon2FromGstar_pt     = self.pLeptState1[1].pt
                      muon2FromGstar_eta    = self.pLeptState1[1].eta
                      muon2FromGstar_phi    = self.pLeptState1[1].phi

                      self.lept1_4V.SetPtEtaPhiM(muon1FromGstar_pt,muon1FromGstar_eta,muon1FromGstar_phi,0.106)
                      self.lept2_4V.SetPtEtaPhiM(muon2FromGstar_pt,muon2FromGstar_eta,muon2FromGstar_phi,0.106)
                  else:
                      elec1FromGstar_pt     = self.pLeptState1[0].pt
                      elec1FromGstar_eta    = self.pLeptState1[0].eta
                      elec1FromGstar_phi    = self.pLeptState1[0].phi
                      elec2FromGstar_pt     = self.pLeptState1[1].pt
                      elec2FromGstar_eta    = self.pLeptState1[1].eta
                      elec2FromGstar_phi    = self.pLeptState1[1].phi

                      self.lept1_4V.SetPtEtaPhiM(elec1FromGstar_pt,elec1FromGstar_eta,elec1FromGstar_phi,0.0005)
                      self.lept2_4V.SetPtEtaPhiM(elec2FromGstar_pt,elec2FromGstar_eta,elec2FromGstar_phi,0.0005)

                  genDiLeptMassZGstar = (self.lept1_4V + self.lept2_4V).M()
                  _ZGstarDiLept_DelaR = self.deltaR(self.pLeptState1[0].eta,self.pLeptState1[1].eta,self.pLeptState1[0].phi,self.pLeptState1[1].phi)
              else : 
                  continue

          elif((abs(genParticles[pLeptMom].pdgId) <=6  and abs(genParticles[pLeptMom].pdgId) >= 1) or abs(genParticles[pLeptMom].pdgId) == 21 ) :
              nLeptFromQ = 0
              nWFromQ = 0
              daughters = []
              listLeptFromQ = []
              
              if(abs(genParticles[pLeptMom].pdgId) == 21):
                  daughters = self.Daughters(genParticles,21)
              else :
                  for iMom in range(1,7):
                      if(abs(genParticles[pLeptMom].pdgId) == iMom):
                          daughters = self.Daughters(genParticles,iMom)
                          break
              for i in range(len(daughters)):
                  if(abs(daughters[i].pdgId) == 24):
                      nWFromQ+=1
                  if(isMuon and abs(daughters[i].pdgId) == 13):
                      if(daughters[i].status != 1 ):
                          continue
                      listLeptFromQ.append(daughters[i])
                      nLeptFromQ+=1
                  if(not isMuon and abs(daughters[i].pdgId) == 11):
                      if(daughters[i].status != 1 ):
                          continue
                      listLeptFromQ.append(daughters[i])
                      nLeptFromQ+=1

              if(nLeptFromQ == 2 and nWFromQ == 1):
                  if(listLeptFromQ[0].pdgId * listLeptFromQ[1].pdgId > 0):
                      continue
                  self.pLeptState1[0] = listLeptFromQ[0]
                  self.pLeptState1[1] = listLeptFromQ[1]
                  if(isMuon):
                      muon1FromGstar_pt     = self.pLeptState1[0].pt
                      muon1FromGstar_eta    = self.pLeptState1[0].eta
                      muon1FromGstar_phi    = self.pLeptState1[0].phi
                      muon2FromGstar_pt     = self.pLeptState1[1].pt
                      muon2FromGstar_eta    = self.pLeptState1[1].eta
                      muon2FromGstar_phi    = self.pLeptState1[1].phi

                      self.lept1_4V.SetPtEtaPhiM(muon1FromGstar_pt,muon1FromGstar_eta,muon1FromGstar_phi,0.106)
                      self.lept2_4V.SetPtEtaPhiM(muon2FromGstar_pt,muon2FromGstar_eta,muon2FromGstar_phi,0.106)
                  else:
                      elec1FromGstar_pt     = self.pLeptState1[0].pt
                      elec1FromGstar_eta    = self.pLeptState1[0].eta
                      elec1FromGstar_phi    = self.pLeptState1[0].phi
                      elec2FromGstar_pt     = self.pLeptState1[1].pt
                      elec2FromGstar_eta    = self.pLeptState1[1].eta
                      elec2FromGstar_phi    = self.pLeptState1[1].phi

                      self.lept1_4V.SetPtEtaPhiM(elec1FromGstar_pt,elec1FromGstar_eta,elec1FromGstar_phi,0.0005)
                      self.lept2_4V.SetPtEtaPhiM(elec2FromGstar_pt,elec2FromGstar_eta,elec2FromGstar_phi,0.0005)

                  genDiLeptMassZGstar = (self.lept1_4V + self.lept2_4V).M()
                  _ZGstarDiLept_DelaR = self.deltaR(self.pLeptState1[0].eta,self.pLeptState1[1].eta,self.pLeptState1[0].phi,self.pLeptState1[1].phi)
              else:
                  continue
          else:
              continue
        self.out.fillBranch("Gen_ZGstar_mu1_pt", muon1FromGstar_pt )
        self.out.fillBranch("Gen_ZGstar_mu1_eta",muon1FromGstar_eta )
        self.out.fillBranch("Gen_ZGstar_mu1_phi",muon1FromGstar_phi )
        self.out.fillBranch("Gen_ZGstar_mu2_pt", muon2FromGstar_pt )
        self.out.fillBranch("Gen_ZGstar_mu2_eta",muon2FromGstar_eta )
        self.out.fillBranch("Gen_ZGstar_mu2_phi",muon2FromGstar_phi )
        self.out.fillBranch("Gen_ZGstar_ele1_pt",elec1FromGstar_pt )
        self.out.fillBranch("Gen_ZGstar_ele1_eta",elec1FromGstar_eta )
        self.out.fillBranch("Gen_ZGstar_ele1_phi",elec1FromGstar_phi )
        self.out.fillBranch("Gen_ZGstar_ele2_pt", elec2FromGstar_pt )
        self.out.fillBranch("Gen_ZGstar_ele2_eta",elec2FromGstar_eta )
        self.out.fillBranch("Gen_ZGstar_ele2_phi",elec2FromGstar_phi )
        self.out.fillBranch("Gen_ZGstar_mass",    genDiLeptMassZGstar )
        self.out.fillBranch("Gen_ZGstar_deltaR",  _ZGstarDiLept_DelaR )
        self.out.fillBranch("Gen_ZGstar_MomId",   mom_pdgId )
        self.out.fillBranch("Gen_ZGstar_MomStatus",mom_status )

        return True
