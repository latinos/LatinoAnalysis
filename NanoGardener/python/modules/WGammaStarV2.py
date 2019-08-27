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


class WGammaStarV2(Module):
    def __init__(self):
        self.pLeptState1 = [0,0,0,0]
        self.lept1_4V = ROOT.TLorentzVector()
        self.lept2_4V = ROOT.TLorentzVector()
        self.tmp4V_1 = ROOT.TLorentzVector()
        self.tmp4V_2 = ROOT.TLorentzVector()
    def beginJob(self,histFile=None,histDirName=None):
	pass
    def Daughters(self,p,idx,genParticles, daughters):
        if p.status == 1 or (abs(p.pdgId)==15):
          daughters.append(p)
        else:  
          for i,part in enumerate(genParticles):
            if part.genPartIdxMother == idx:
              self.Daughters(part, i, genParticles, daughters) 
                 
    def printParticle(self, p):
      print p.pdgId,p.status,p.pt

    def findGStarPair (self, leptons):
      # get the charged leptons
      charged = [l for l in leptons if abs(l.pdgId)==11 or abs(l.pdgId)==13 or abs(l.pdgId)==15]
      pairs = []
      #form the opposite sign same flavor pairs
      for i in range(len(charged)-1):
        for j in range(i+1, len(charged)):
          if charged[i].pdgId*charged[j].pdgId == -(charged[i].pdgId)**2:
            pairs.append([charged[i], charged[j]])

      #find the smallest mass
      if len(pairs) == 0:
        return None
      gstarmass = 999999.
      for p in pairs:
        tmp4V_1 = ROOT.TLorentzVector()
        tmp4V_2 = ROOT.TLorentzVector()

        if abs(p[0].pdgId)==11:
          tmp4V_1.SetPtEtaPhiM(p[0].pt,p[0].eta,p[0].phi,0.0005)
          tmp4V_2.SetPtEtaPhiM(p[1].pt,p[1].eta,p[1].phi,0.0005)
        elif abs(p[0].pdgId)==13:
          tmp4V_1.SetPtEtaPhiM(p[0].pt,p[0].eta,p[0].phi,0.106)
          tmp4V_2.SetPtEtaPhiM(p[1].pt,p[1].eta,p[1].phi,0.106)
        if (tmp4V_1+tmp4V_2).M() < gstarmass:
          gstarmass = (tmp4V_1+tmp4V_2).M()
          gstar = p

      return gstar  




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
        ('Gen_ZGstar_mu1_pt',  "pt of the leading muon from G* candidate"),  
        ('Gen_ZGstar_mu1_eta', "eta of the leading muon from G* candidate"),
        ('Gen_ZGstar_mu1_phi', "phi of the leading muon from G* candidate"), 
        ('Gen_ZGstar_mu2_pt',  "pt of the subleading muon from G* candidate"),  
        ('Gen_ZGstar_mu2_eta', "eta of the subleading muon from G* candidate"),
        ('Gen_ZGstar_mu2_phi', "phi of the subleading muon from G* candidate"), 
        ('Gen_ZGstar_ele1_pt', "pt of the leading electron from G* candidate"),  
        ('Gen_ZGstar_ele1_eta',"eta of the leading electron from G* candidate"),
        ('Gen_ZGstar_ele1_phi',"phi of the leading electron from G* candidate"), 
        ('Gen_ZGstar_ele2_pt', "pt of the subleading electron from G* candidate"), 
        ('Gen_ZGstar_ele2_eta',"eta of the subleading electron from G* candidate"),
        ('Gen_ZGstar_ele2_phi',"phi of the subleading electron from G* candidate"),
        ('Gen_ZGstar_mass',    "G* candidate mass"),
        ('Gen_ZGstar_deltaR',   "deltaR between leptons from G* candidate"),
         ]
        self.newbranchesI = [
        ("Gen_ZGstar_MomId", "Id of the mother particle of the G*"),
        ("Gen_ZGstar_MomStatus", "how the G* is born: \
0= from a hard process photon:\
1= from a Z candidate decaying to a lepton pair, with Z boson in event history:\
2= from a Z to 4 leptons decay, with Z boson in event history: \
3= from lepton pair in the eventhistorym without a Z boson in the event history: \
4= from a W boson decaying to 3 charged leptons: \
5= from a photon in the parton shower")
        ]
        
        for nameBranchesF in self.newbranchesF :
          self.out.branch(nameBranchesF[0]  ,  "F", title=nameBranchesF[1]);
        for nameBranchesI in self.newbranchesI :
          self.out.branch(nameBranchesI[0]  ,  "I", title=nameBranchesI[1]);

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
        fromG_HP = False #foton from hard process
        fromZ = False
        fromW = False
        fromG_PS = False # foton from PS
        gstar = None
        statuses = ['fromG_HP', 'fromZ_ll_inhistory', "fromZ_llll", 'fromZ_ll_decay', 'fromW3l', 'fromG_PS']
        fromHardProcessLeptons = []
        # Photon from hard process takes precedence on Z takes precedence on from W, which takes precedence on from gamma from PS
	for i,particle  in enumerate(genParticles) :
	  pdg_Id = abs(particle.pdgId)
          daughters=[]
          if pdg_Id == 22 and (particle.statusFlags >> 7 & 1): # hard process
            # this is out gstar candidate, cleanup everything
            fromG_HP = True
            fromG_PS = False
            fromZ = False
            fromG_PS = False
            gstar = None
            self.Daughters(particle, i, genParticles, daughters)
            gstar = self.findGStarPair(daughters)
            if (gstar != None):
              mom_pdgId = particle.pdgId
              mom_status = 0
            #if there was a photon from the hard process in the event, that is the only one we want to look, nothing else matters
            # otherwise in Zg sample the Z will end up to be the gamma* candidate, but that is not what we want
            #so if a photon from hard process is aroung, if we don't have a gamma* candidate at this point, we can as well move to next event.
            break  

          if pdg_Id==23 and not fromG_HP:
              self.Daughters(particle, i, genParticles, daughters)
              #in this case  dughters can be simply two as in Z/gamma*->ll, or 4 in case you have radiation off a lepton
              # Z/gamma*->llgamma* ->llll
              gstar = self.findGStarPair(daughters)
              if (gstar != None):
                fromZ = True
                mom_pdgId = particle.pdgId;
                if len(daughters)==2:
                  mom_status = 1
                else:
                  mom_status = 2

          if pdg_Id==24 and not fromG_HP and not fromZ:
              self.Daughters(particle, i, genParticles, daughters) 
              # if the mom is a W, it we are in terested in W->l nu gamma* -> l nu l+ l- --> 4 daugthers
              if(not (len(daughters)==4)) : 
                  continue
              gstar = self.findGStarPair(daughters)
              if (gstar != None):
                fromW = True    
                mom_pdgId=particle.pdgId
                mom_status = 4

          if pdg_Id==22 and (not (particle.statusFlags >> 8 & 1)) and not fromG_HP and not fromZ and not fromW:
             self.Daughters(particle, i, genParticles, daughters)
             if(not (len(daughters)==2)) :
               continue
             gstar = self.findGStarPair(daughters)
             if (gstar != None):
              fromG = True  
              mom_pdgId=particle.pdgId  
              mom_status = 5
          #keep arounf a list of all prompt leptons
          if (((pdg_Id==11 or pdg_Id==13) and particle.status == 1 ) or pdg_Id==15) and (particle.statusFlags & 1):
            fromHardProcessLeptons.append(particle)
        
        #if there are not gammaStar from Z, still look through the prompt lepton pairs, as there may be a Z missing in event history, this has precedence on Ws and gamma
        if not fromZ and not fromG_HP:
          gstar = self.findGStarPair(fromHardProcessLeptons)
          fromZ = True
          if (gstar != None):
            mom_pdgId = 23
            mom_status = 3
        if gstar != None:
          #print "this is pdg id", pdg_Id, "daughters:"
          #for d in daughters:
          #  self.printParticle(d)
          #print "gstar identified as: "
          #self.printParticle(gstar[0])
          #self.printParticle(gstar[1])
          self.pLeptState1[0] = gstar[0]
          self.pLeptState1[1] = gstar[1]
          if abs(self.pLeptState1[0].pdgId)==13:
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
