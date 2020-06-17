
import ROOT
import math 
import ctypes
ROOT.PyConfig.IgnoreCommandLineOptions = True

from PhysicsTools.NanoAODTools.postprocessing.framework.datamodel import Collection 
from PhysicsTools.NanoAODTools.postprocessing.framework.eventloop import Module
from PhysicsTools.NanoAODTools.postprocessing.modules.common.collectionMerger import collectionMerger
from LatinoAnalysis.NanoGardener.framework.BranchMapping import mappedOutputTree, mappedEvent

import os.path

class JJH_EFTVars(Module):
    def __init__(self, branch_map=''):
        
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

        self._branch_map = branch_map

    def beginJob(self):
        pass

    def endJob(self):
        pass

    def beginFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        self.out = mappedOutputTree(wrappedOutputTree, mapname=self._branch_map)
        self.newbranches = [
          'hm',
          'me_vbf_hsm','me_vbf_hm','me_vbf_hp','me_vbf_hl','me_vbf_mixhm','me_vbf_mixhp',
          'me_wh_hsm','me_wh_hm','me_wh_hp','me_wh_hl','me_wh_mixhm','me_wh_mixhp',
          'me_zh_hsm','me_zh_hm','me_zh_hp','me_zh_hl','me_zh_mixhm','me_zh_mixhp',
          'me_qcd_hsm',
          'pjjSm_wh','pjjTr_wh','pjjSm_zh','pjjTr_zh','meAvg_wh','meAvg_zh'
          ]
        
        for nameBranches in self.newbranches :
          self.out.branch(nameBranches  ,  "F");

    def endFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        pass

    def analyze(self, event):
        """process event, return True (go to next module) or False (fail, go to next event)"""

        event = mappedEvent(event, mapname=self._branch_map)

        Lepton = Collection(event, "Lepton")
        nLepton = len(Lepton)

        Jet   = Collection(event, "CleanJet")
        nJet = len(Jet)

        OrigJet = Collection(event, "Jet")

        hm = -999
        me_vbf_hsm = -999 
        me_vbf_hm = -999 
        me_vbf_hp = -999 
        me_vbf_hl = -999 
        me_vbf_mixhm = -999 
        me_vbf_mixhp = -999
        me_wh_hsm = -999 
        me_wh_hm = -999 
        me_wh_hp = -999 
        me_wh_hl = -999 
        me_wh_mixhm = -999 
        me_wh_mixhp = -999
        me_zh_hsm = -999 
        me_zh_hm = -999 
        me_zh_hp = -999 
        me_zh_hl = -999 
        me_zh_mixhm = -999 
        me_zh_mixhp = -999
        me_qcd_hsm = -999 

        pjjSm_wh = -999 
        pjjTr_wh = -999
        pjjSm_zh = -999 
        pjjTr_zh = -999
        meAvg_wh = -999
        meAvg_zh = -999

        if nJet > 1 and nLepton > 1 :
         
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

         indx_j1 = 0
         indx_j2 = 1 

         J1 = ROOT.TLorentzVector()
         J2 = ROOT.TLorentzVector() 
         indx_oj1 = Jet[indx_j1].jetIdx
         indx_oj2 = Jet[indx_j2].jetIdx
         J1.SetPtEtaPhiM(Jet[indx_j1].pt, Jet[indx_j1].eta, Jet[indx_j1].phi, OrigJet[indx_oj1].mass)
         J2.SetPtEtaPhiM(Jet[indx_j2].pt, Jet[indx_j2].eta, Jet[indx_j2].phi, OrigJet[indx_oj2].mass)

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

         ME_VBF = ROOT.melaHiggsEFT(self.mela, ROOT.TVar.JHUGen, ROOT.TVar.JJVBF, 0, 1) 
         me_vbf_hsm   = ME_VBF[0]
         me_vbf_hm    = ME_VBF[1]
         me_vbf_hp    = ME_VBF[2]
         me_vbf_hl    = ME_VBF[3]
         me_vbf_mixhm = ME_VBF[4]
         me_vbf_mixhp = ME_VBF[5] 

         ME_WH = ROOT.melaHiggsEFT(self.mela, ROOT.TVar.JHUGen, ROOT.TVar.Had_WH, 0, 1)
         me_wh_hsm   = ME_WH[0]
         me_wh_hm    = ME_WH[1]
         me_wh_hp    = ME_WH[2]
         me_wh_hl    = ME_WH[3]
         me_wh_mixhm = ME_WH[4]
         me_wh_mixhp = ME_WH[5] 

         pjjSm_wh    = ME_WH[7] 
         pjjTr_wh    = ME_WH[8] 
         meAvg_wh    = ME_WH[9] 
   
         ME_ZH = ROOT.melaHiggsEFT(self.mela, ROOT.TVar.JHUGen, ROOT.TVar.Had_ZH, 0, 1)
         me_zh_hsm   = ME_ZH[0]
         me_zh_hm    = ME_ZH[1]
         me_zh_hp    = ME_ZH[2]
         me_zh_hl    = ME_ZH[3]
         me_zh_mixhm = ME_ZH[4]
         me_zh_mixhp = ME_ZH[5] 

         pjjSm_zh    = ME_ZH[7] 
         pjjTr_zh    = ME_ZH[8] 
         meAvg_zh    = ME_ZH[9] 

         ME_QCD = ROOT.melaHiggsEFT(self.mela, ROOT.TVar.JHUGen, ROOT.TVar.JJQCD, 1, 1)
         me_qcd_hsm   = ME_QCD[0]

         self.mela.resetInputEvent()


        self.out.fillBranch( 'hm',          hm )

        self.out.fillBranch( 'me_vbf_hsm',  me_vbf_hsm )
        self.out.fillBranch( 'me_vbf_hm',   me_vbf_hm )
        self.out.fillBranch( 'me_vbf_hp',   me_vbf_hp ) 
        self.out.fillBranch( 'me_vbf_hl',   me_vbf_hl )
        self.out.fillBranch( 'me_vbf_mixhm',me_vbf_mixhm )
        self.out.fillBranch( 'me_vbf_mixhp',me_vbf_mixhp ) 

        self.out.fillBranch( 'me_wh_hsm',   me_wh_hsm )
        self.out.fillBranch( 'me_wh_hm',    me_wh_hm )
        self.out.fillBranch( 'me_wh_hp',    me_wh_hp ) 
        self.out.fillBranch( 'me_wh_hl',    me_wh_hl )
        self.out.fillBranch( 'me_wh_mixhm', me_wh_mixhm )
        self.out.fillBranch( 'me_wh_mixhp', me_wh_mixhp ) 
        self.out.fillBranch( 'me_zh_hsm',   me_zh_hsm )
        self.out.fillBranch( 'me_zh_hm',    me_zh_hm )
        self.out.fillBranch( 'me_zh_hp',    me_zh_hp ) 
        self.out.fillBranch( 'me_zh_hl',    me_zh_hl )
        self.out.fillBranch( 'me_zh_mixhm', me_zh_mixhm )
        self.out.fillBranch( 'me_zh_mixhp', me_zh_mixhp ) 
        self.out.fillBranch( 'me_qcd_hsm',  me_qcd_hsm )

        self.out.fillBranch( 'pjjSm_wh', pjjSm_wh )
        self.out.fillBranch( 'pjjTr_wh', pjjTr_wh )
        self.out.fillBranch( 'pjjSm_zh', pjjSm_zh )
        self.out.fillBranch( 'pjjTr_zh', pjjTr_zh )
        self.out.fillBranch( 'meAvg_wh', meAvg_wh )
        self.out.fillBranch( 'meAvg_zh', meAvg_zh )

        return True






