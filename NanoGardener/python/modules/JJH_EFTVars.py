
import ROOT
import math 
import ctypes
ROOT.PyConfig.IgnoreCommandLineOptions = True

from PhysicsTools.NanoAODTools.postprocessing.framework.datamodel import Collection 
from PhysicsTools.NanoAODTools.postprocessing.framework.eventloop import Module
from PhysicsTools.NanoAODTools.postprocessing.modules.common.collectionMerger import collectionMerger

import os.path

class JJH_EFTVars(Module):
    def __init__(self):
        
        self.cmssw_base = os.getenv('CMSSW_BASE')
        self.cmssw_arch = os.getenv('SCRAM_ARCH')

        ROOT.gSystem.AddIncludePath("-I"+self.cmssw_base+"/interface/")
        ROOT.gSystem.AddIncludePath("-I"+self.cmssw_base+"/src/")
        ROOT.gSystem.Load("libZZMatrixElementMELA.so")
        ROOT.gSystem.Load(self.cmssw_base+"/src/ZZMatrixElement/MELA/data/"+self.cmssw_arch+"/libmcfm_706.so")

        try:
            ROOT.gROOT.LoadMacro(self.cmssw_base+'/src/LatinoAnalysis/Gardener/python/variables/melaHiggsEFT.C+g')
        except RuntimeError:
            ROOT.gROOT.LoadMacro(self.cmssw_base+'/src/LatinoAnalysis/Gardener/python/variables/melaHiggsEFT.C++g')
      
        self.mela = ROOT.Mela(13, 125,  ROOT.TVar.SILENT) 
        self.UseHMJetPair = False

    def beginJob(self):
        pass

    def endJob(self):
        pass

    def beginFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        self.out = wrappedOutputTree
        self.newbranches = [
          'hm','hpt','jj_mass','jj_deta',
          'me_vbf_hsm','me_vbf_hm','me_vbf_hp','me_vbf_hl','me_vbf_mixhm','me_vbf_mixhp',
          'me_qcd_hsm'
          ]
        

        for nameBranches in self.newbranches :
          self.out.branch(nameBranches  ,  "F");

    def endFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        pass

    def analyze(self, event):
        """process event, return True (go to next module) or False (fail, go to next event)"""

        Lepton = Collection(event, "Lepton")
        nLepton = len(Lepton)

        Jet   = Collection(event, "CleanJet")
        nJet = len(Jet)
 
        OrigJet = Collection(event, "Jet")
        nOrigJet = len(OrigJet)

        hm = -999
        hpt = -999
        j1_pt = -999
        j2_pt = -999
        jj_mass = -999
        jj_deta = -999
        me_vbf_hsm = -999 
        me_vbf_hm = -999 
        me_vbf_hp = -999 
        me_vbf_hl = -999 
        me_vbf_mixhm = -999 
        me_vbf_mixhp = -999
        me_qcd_hsm = -999  
            
        if nJet > 1 and nLepton > 1:

         L1 = ROOT.TLorentzVector()
         L2 = ROOT.TLorentzVector()
         L1.SetPtEtaPhiM(Lepton[0].pt, Lepton[0].eta, Lepton[0].phi, 0)
         L2.SetPtEtaPhiM(Lepton[1].pt, Lepton[1].eta, Lepton[1].phi, 0)

         LL = ROOT.TLorentzVector()
         LL = L1 + L2

         MET_phi   = event.PuppiMET_phi
         MET_pt    = event.PuppiMET_pt

         NuNu = ROOT.TLorentzVector()
         nunu_px = MET_pt*math.cos(MET_phi)
         nunu_py = MET_pt*math.sin(MET_phi)
         nunu_pz = LL.Pz()                                                                                                                  
         nunu_m  = 30.0                                                                                                                                                                                      
         nunu_e  = math.sqrt(nunu_px*nunu_px + nunu_py*nunu_py + nunu_pz*nunu_pz + nunu_m*nunu_m)
         NuNu.SetPxPyPzE(nunu_px, nunu_py, nunu_pz, nunu_e)

         Higgs = ROOT.TLorentzVector()
         Higgs = LL + NuNu
         hm  = Higgs.M()
         hpt = Higgs.Pt()

         indx_j1 = 0
         indx_j2 = 1 

         if nJet > 2 and self.UseHMJetPair :
          max_mass = 0          
          tJ1 = ROOT.TLorentzVector()  
          tJ2 = ROOT.TLorentzVector()  
          for i in range(nJet):
           for j in range(nJet):
            oi = Jet[i].jetIdx
            oj = Jet[j].jetIdx
            tJ1.SetPtEtaPhiM(Jet[i].pt, Jet[i].eta, Jet[i].phi, OrigJet[oi].mass)
            tJ2.SetPtEtaPhiM(Jet[j].pt, Jet[j].eta, Jet[j].phi, OrigJet[oj].mass)
            tMass = (tJ1 + tJ2).M()
            if tMass > max_mass:
             max_mass = tMass
             indx_j1 = i
             indx_j2 = j    

         J1 = ROOT.TLorentzVector()
         J2 = ROOT.TLorentzVector() 
         indx_oj1 = Jet[indx_j1].jetIdx
         indx_oj2 = Jet[indx_j2].jetIdx
         J1.SetPtEtaPhiM(Jet[indx_j1].pt, Jet[indx_j1].eta, Jet[indx_j1].phi, OrigJet[indx_oj1].mass)
         J2.SetPtEtaPhiM(Jet[indx_j2].pt, Jet[indx_j2].eta, Jet[indx_j2].phi, OrigJet[indx_oj2].mass)
 
         j1_pt = J1.Pt()
         j2_pt = J2.Pt()
         jj_mass = (J1 + J2).M()
         jj_deta = abs(J1.Eta() - J2.Eta())

         daughter_coll = ROOT.SimpleParticleCollection_t() 
         associated_coll = ROOT.SimpleParticleCollection_t()

         daughter = ROOT.SimpleParticle_t(25, Higgs)
         associated1 = ROOT.SimpleParticle_t(0, J1)
         associated2 = ROOT.SimpleParticle_t(0, J2)

         daughter_coll.push_back(daughter)                                                           
         associated_coll.push_back(associated1)
         associated_coll.push_back(associated2)

         self.mela.setCandidateDecayMode(ROOT.TVar.CandidateDecay_Stable)   
         self.mela.setInputEvent(daughter_coll, associated_coll, 0, 0)
         self.mela.setCurrentCandidateFromIndex(0)
        
         ME_VBF = ROOT.melaHiggsEFT(self.mela, ROOT.TVar.JHUGen, ROOT.TVar.JJVBF, 1) 
         me_vbf_hsm   = ME_VBF[0]
         me_vbf_hm    = ME_VBF[1]
         me_vbf_hp    = ME_VBF[2]
         me_vbf_hl    = ME_VBF[3]
         me_vbf_mixhm = ME_VBF[4]
         me_vbf_mixhp = ME_VBF[5] 

         ME_QCD = ROOT.melaHiggsEFT(self.mela, ROOT.TVar.JHUGen, ROOT.TVar.JJQCD, 1)
         me_qcd_hsm   = ME_QCD[0]

         ######### VH also possible ########
         # ME_WH = ROOT.melaHiggsEFT(self.mela, ROOT.TVar.JHUGen, ROOT.TVar.Had_WH, 1)
         # ME_ZH = ROOT.melaHiggsEFT(self.mela, ROOT.TVar.JHUGen, ROOT.TVar.Had_ZH, 1)

         self.mela.resetInputEvent()
       
      #  else:
      #   return False         
      #  if j1_pt < 30 or j2_pt < 30 :
      #    return False 

        self.out.fillBranch( 'hm',         hm )
        self.out.fillBranch( 'hpt',        hpt )
        self.out.fillBranch( 'jj_mass',    jj_mass )
        self.out.fillBranch( 'jj_deta',    jj_deta )
        self.out.fillBranch( 'me_vbf_hsm',  me_vbf_hsm )
        self.out.fillBranch( 'me_vbf_hm',   me_vbf_hm )
        self.out.fillBranch( 'me_vbf_hp',   me_vbf_hp ) 
        self.out.fillBranch( 'me_vbf_hl',   me_vbf_hl )
        self.out.fillBranch( 'me_vbf_mixhm',me_vbf_mixhm )
        self.out.fillBranch( 'me_vbf_mixhp',me_vbf_mixhp ) 
        self.out.fillBranch( 'me_qcd_hsm',  me_qcd_hsm )

        return True






