
import ROOT
import math 
import ctypes
ROOT.PyConfig.IgnoreCommandLineOptions = True

from PhysicsTools.NanoAODTools.postprocessing.framework.datamodel import Collection 
from PhysicsTools.NanoAODTools.postprocessing.framework.eventloop import Module
from PhysicsTools.NanoAODTools.postprocessing.modules.common.collectionMerger import collectionMerger

import os.path

class EFTReweighter(Module):
    def __init__(self, sample):
        print '####################', sample
        self.sample = sample
        self.cmssw_base = os.getenv('CMSSW_BASE')
        self.cmssw_arch = os.getenv('SCRAM_ARCH')

        ROOT.gSystem.AddIncludePath("-I"+self.cmssw_base+"/interface/")
        ROOT.gSystem.AddIncludePath("-I"+self.cmssw_base+"/src/")
        ROOT.gSystem.Load("libZZMatrixElementMELA.so")
        ROOT.gSystem.Load(self.cmssw_base+"/src/ZZMatrixElement/MELA/data/"+self.cmssw_arch+"/libmcfm_707.so")

        try:
            ROOT.gROOT.LoadMacro(self.cmssw_base+'/src/LatinoAnalysis/Gardener/python/variables/melaHiggsEFT.C+g')
        except RuntimeError:
            ROOT.gROOT.LoadMacro(self.cmssw_base+'/src/LatinoAnalysis/Gardener/python/variables/melaHiggsEFT.C++g')
      
        self.mela = ROOT.Mela(13, 125,  ROOT.TVar.SILENT) 

    def beginJob(self):
        pass

    def endJob(self):
        pass

    def beginFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):

        if "VBF_H0" in self.sample :
          self.productionProcess = "VBF"
          self.XHProcess = True
        elif "ZH_H0" in self.sample :
          self.productionProcess = "ZH"
          self.XHProcess = True
        elif "WH_H0" in self.sample :
          self.productionProcess = "WH"
          self.XHProcess = True
        elif "H0" in self.sample :
          self.productionProcess = "GluGlu"
          self.XHProcess = False
        else:
          raise NameError(self.sample, "is an unrecognised simulation")

        print("Running MELA EFT reweighter with " + self.productionProcess + " sample")

        self.out = wrappedOutputTree
        self.newbranches = ['gen_dme_hsm','gen_dme_hm','gen_dme_hp','gen_dme_hl','gen_dme_mixhm','gen_dme_mixhp','gen_dme_mixhl' ]

        if self.XHProcess == True:
         self.newbranches += ['gen_pme_hsm','gen_pme_hm','gen_pme_hp','gen_pme_hl','gen_pme_mixhm','gen_pme_mixhp','gen_pme_mixhl' ]
        
        for nameBranches in self.newbranches :
          self.out.branch(nameBranches  ,  "F");

    def endFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        pass

    def analyze(self, event):
        """process event, return True (go to next module) or False (fail, go to next event)"""

        gen_dme_hsm   = -999
        gen_dme_hm    = -999
        gen_dme_hp    = -999
        gen_dme_hl    = -999
        gen_dme_mixhm = -999
        gen_dme_mixhp = -999 
        gen_dme_mixhl = -999 

        gen_pme_hsm   = -999
        gen_pme_hm    = -999
        gen_pme_hp    = -999
        gen_pme_hl    = -999
        gen_pme_mixhm = -999
        gen_pme_mixhp = -999 
        gen_pme_mixhl = -999 

        self.LHE = Collection(event,"LHEPart")
        Gen = Collection(event,"GenPart")

        daughters   = ROOT.vector('TLorentzVector')()
        daughterIDs = ROOT.vector('int')()

        HFinalStateIdx = []
        for gid,gen in enumerate(Gen):
          if abs(gen.pdgId) >= 21: continue 
          mid = event.GenPart_genPartIdxMother[gid]
          if mid == -1: continue
          if abs(event.GenPart_pdgId[mid]) != 24: continue 
          if self.FromH(event, gid) == False: continue
          HFinalStateIdx.append(gid) 

        if len(HFinalStateIdx) != 4:      
         HFinalStateIdx = self.RemoveGammaW(event, HFinalStateIdx)

        if len(HFinalStateIdx) != 4: 
         HFinalStateIdx = self.RemoveAddHadron(event, HFinalStateIdx)

        LHEHFinalState = self.getLHE(event, HFinalStateIdx) 

        if len(LHEHFinalState)!=4:
          print "SOMETHING WENT WRONG!, WW final state", len(LHEHFinalState), LHEHFinalState

        for ipart in LHEHFinalState:
          d = ROOT.TLorentzVector()
          d.SetPtEtaPhiM(LHEHFinalState[ipart][0], LHEHFinalState[ipart][1], LHEHFinalState[ipart][2], 0.)
          daughters.push_back(d)
          daughterIDs.push_back(LHEHFinalState[ipart][3])                            

        mothers = ROOT.vector('TLorentzVector')()
        motherIDs = ROOT.vector('int')()
        incoming1=ROOT.TLorentzVector()
        incoming1.SetPxPyPzE(0.,0., event.Generator_x1*6500, event.Generator_x1*6500)
        incoming2=ROOT.TLorentzVector()
        incoming2.SetPxPyPzE(0.,0.,-1*event.Generator_x2*6500, event.Generator_x2*6500)
        mothers.push_back(incoming1)
        mothers.push_back(incoming2)
        genid1 = int(event.Generator_id1)
        genid2 = int(event.Generator_id2)
        motherIDs.push_back(genid1)
        motherIDs.push_back(genid2)       

        adds   = ROOT.vector('TLorentzVector')()
        addIDs = ROOT.vector('int')()

        if self.productionProcess == "ZH" or  self.productionProcess == "WH": 

         VFinalStateIdx = []
         for gid,gen in enumerate(Gen):
          if abs(gen.pdgId) >= 21: continue 
          if self.FromH(event, gid) == True: continue 
          mid = event.GenPart_genPartIdxMother[gid]
          if mid == -1: continue

          if abs(event.GenPart_pdgId[mid]) == 23 and self.productionProcess == "ZH": 
           VFinalStateIdx.append(gid) 
           if abs(gen.pdgId) in [1,2,3,4,5]:
            self.productionMela = ROOT.TVar.Had_ZH
           elif abs(gen.pdgId) in [11,12,13,14,15,16,17,18]:
            self.productionMela = ROOT.TVar.Lep_ZH

          if abs(event.GenPart_pdgId[mid]) == 24 and self.productionProcess == "WH": 
           VFinalStateIdx.append(gid) 
           if abs(gen.pdgId) in [1,2,3,4,5]:
            self.productionMela = ROOT.TVar.Had_WH
           elif abs(gen.pdgId) in [11,12,13,14,15,16,17,18]:
            self.productionMela = ROOT.TVar.Lep_WH
         
         if len(VFinalStateIdx) != 2 and self.productionProcess == "WH":      
          VFinalStateIdx = self.RemoveGammaW(event, VFinalStateIdx)

         if len(VFinalStateIdx) != 2: 
          VFinalStateIdx = self.RemoveAddHadron(event, VFinalStateIdx)

         LHEVFinalState = self.getLHE(event, VFinalStateIdx) 

         if len(LHEVFinalState)!=2:
          print "SOMETHING WENT WRONG!, V final state ", len(LHEVFinalState), VFinalStateIdx

         for ipart in LHEVFinalState:
          add = ROOT.TLorentzVector()
          add.SetPtEtaPhiM(LHEVFinalState[ipart][0], LHEVFinalState[ipart][1], LHEVFinalState[ipart][2], 0.)
          adds.push_back(add)
          addIDs.push_back(LHEVFinalState[ipart][3]) 

        elif self.productionProcess == "VBF" : 

         self.productionMela = ROOT.TVar.JJVBF

         LHEjetIdx = []
         for idx,part in enumerate(self.LHE):
          if abs(part.pdgId) in [1,2,3,4,5,21]:
           LHEjetIdx.append(idx)

         LHEjetIdx = self.pTorder(event, LHEjetIdx)

         for ijet in LHEjetIdx:
          add = ROOT.TLorentzVector()
          add.SetPtEtaPhiM(event.LHEPart_pt[ijet], event.LHEPart_eta[ijet], event.LHEPart_phi[ijet], 0.)
          adds.push_back(add)
          addIDs.push_back(int(event.LHEPart_pdgId[ijet]))
        
         if len(adds) !=2 : 
          print "Number of additional particles does not equal 2! Setup is not appropiate for this VBF simulation"
         

        daughter_coll = ROOT.SimpleParticleCollection_t() 
        associated_coll = ROOT.SimpleParticleCollection_t()        
        mother_coll = ROOT.SimpleParticleCollection_t()

        for idx, dau in enumerate(daughters):
         daughter_coll.push_back(ROOT.SimpleParticle_t(daughterIDs[idx], dau)) 
        
        for idx, par in enumerate(adds):
         associated_coll.push_back(ROOT.SimpleParticle_t(addIDs[idx], par))
        
        for idx, mot in enumerate(mothers):
         mother_coll.push_back(ROOT.SimpleParticle_t(motherIDs[idx], mot))
                                 
        self.mela.setCandidateDecayMode(ROOT.TVar.CandidateDecay_WW)   
        self.mela.setInputEvent(daughter_coll, associated_coll, mother_coll, 1)
        self.mela.setCurrentCandidateFromIndex(0)
        
        DME = [1, 1, 1, 1, 1, 1, 1] 
        PME = [1, 1, 1, 1, 1, 1, 1]

        if self.XHProcess == True:

         DME = ROOT.melaHiggsEFT(self.mela, ROOT.TVar.JHUGen, ROOT.TVar.ZZINDEPENDENT, 0, 0) 
         PME = ROOT.melaHiggsEFT(self.mela, ROOT.TVar.JHUGen, self.productionMela, 0, 0) 
  
        elif self.productionProcess == "GluGlu" :

         DME = ROOT.melaHiggsEFT(self.mela, ROOT.TVar.JHUGen, ROOT.TVar.ZZINDEPENDENT, 1, 0) 

        gen_dme_hsm   = DME[0]
        gen_dme_hm    = DME[1]
        gen_dme_hp    = DME[2]
        gen_dme_hl    = DME[3]
        gen_dme_mixhm = DME[4]
        gen_dme_mixhp = DME[5] 
        gen_dme_mixhl = DME[6] 

        gen_pme_hsm   = PME[0]
        gen_pme_hm    = PME[1]
        gen_pme_hp    = PME[2]
        gen_pme_hl    = PME[3]
        gen_pme_mixhm = PME[4]
        gen_pme_mixhp = PME[5] 
        gen_pme_mixhl = PME[6] 

        self.out.fillBranch( 'gen_dme_hsm',    gen_dme_hsm )
        self.out.fillBranch( 'gen_dme_hm',     gen_dme_hm )
        self.out.fillBranch( 'gen_dme_hp',     gen_dme_hp )
        self.out.fillBranch( 'gen_dme_hl',     gen_dme_hl )
        self.out.fillBranch( 'gen_dme_mixhm',  gen_dme_mixhm )
        self.out.fillBranch( 'gen_dme_mixhp',  gen_dme_mixhp )
        self.out.fillBranch( 'gen_dme_mixhl',  gen_dme_mixhl )

        if self.XHProcess == True:

         self.out.fillBranch( 'gen_pme_hsm',    gen_pme_hsm )
         self.out.fillBranch( 'gen_pme_hm',     gen_pme_hm )
         self.out.fillBranch( 'gen_pme_hp',     gen_pme_hp )
         self.out.fillBranch( 'gen_pme_hl',     gen_pme_hl )
         self.out.fillBranch( 'gen_pme_mixhm',  gen_pme_mixhm )
         self.out.fillBranch( 'gen_pme_mixhp',  gen_pme_mixhp )
         self.out.fillBranch( 'gen_pme_mixhl',  gen_pme_mixhl )

        self.mela.resetInputEvent()

        return True   

    def pTorder(self, event, oldlist):
      order = []
      for i in oldlist:
        order.append(0)
      for i,pone in enumerate(oldlist):
        for j,ptwo in enumerate(oldlist):
          if pone==ptwo: continue
          if event.LHEPart_pt[pone] > event.LHEPart_pt[ptwo]: order[i] += 1
          if (event.LHEPart_pt[pone] == event.LHEPart_pt[ptwo]) and (i<j):
            order[j] += 1
      newlist = [oldlist[i] for i in order]
      return newlist

    def FromH(self, event, pid): # Iterate over mothers to find Higgs
      while event.GenPart_genPartIdxMother[pid] != -1:
	pid = event.GenPart_genPartIdxMother[pid]
	if event.GenPart_pdgId[pid] == 25: return True
      return False

    def RemoveGammaW(self, event, FinalStateIdx): # Remove W -> gamma W -> e+ e- W   
       removethis = []
       for pi1,p1 in enumerate(FinalStateIdx):
        for pi2,p2 in enumerate(FinalStateIdx):
         if pi1>=pi2: continue
         if event.GenPart_genPartIdxMother[p1] != event.GenPart_genPartIdxMother[p2]: continue
         if event.GenPart_pdgId[p1] + event.GenPart_pdgId[p2] == 0:
          if p1 not in removethis: removethis.append(p1)
          if p2 not in removethis: removethis.append(p2)
       for rem in removethis:
        FinalStateIdx.remove(rem)
       return FinalStateIdx

    def RemoveAddHadron(self, event, FinalStateIdx): # Remove rare additonal hadrons
        removethis = []
        for pi1,p1 in enumerate(FinalStateIdx):
         mom_id = event.GenPart_genPartIdxMother[p1]
         NumWithThisID = 0
         for pi2,p2 in enumerate(FinalStateIdx):
          if event.GenPart_genPartIdxMother[p2] == mom_id: NumWithThisID += 1
         if NumWithThisID != 2:
          for pi2,p2 in enumerate(FinalStateIdx):
           if (event.GenPart_genPartIdxMother[p2] == mom_id) and (p2 not in removethis):
            removethis.append(p2)
        for rem in removethis:
         FinalStateIdx.remove(rem)
        return FinalStateIdx

    def getLHE(self, event, genlist): # Particles in LHE collection have higher precision -> Find LHE particles with closest match to GenParticles
      LHElist = {}
      for gid in genlist:
        pt = event.GenPart_pt[gid]
        eta = event.GenPart_eta[gid]
        phi = event.GenPart_phi[gid]
        pdgid = event.GenPart_pdgId[gid]
        deltaR = 9999
        LHEid = -1
        for lid,lhe in enumerate(self.LHE):
          if lhe.pdgId != pdgid: continue
          dphi = phi-lhe.phi
          if dphi > math.pi: dphi -= 2*math.pi
          if dphi < -math.pi: dphi += 2*math.pi
          deta = eta-lhe.eta
          dR = math.sqrt((deta)*(deta)+(dphi)*(dphi))
          if deltaR > dR:
            deltaR = dR
            LHEid = lid
            LHEpt = lhe.pt
            LHEeta = lhe.eta
            LHEphi = lhe.phi
            LHEpdg = lhe.pdgId
        if LHEid==-1: # VERY rare, use placeholder key value
          LHElist[pdgid+100*(len(LHElist)+1)]=[pt, eta, phi, pdgid]
        elif deltaR > 0.2: # Use GenPart information if direction is too different
          LHElist[LHEid]=[pt, eta, phi, pdgid]
        else:
          LHElist[LHEid]=[LHEpt, LHEeta, LHEphi, pdgid]
        
      return LHElist
    

      
