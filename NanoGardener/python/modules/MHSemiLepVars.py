import ROOT
import math
ROOT.PyConfig.IgnoreCommandLineOptions = True
import re
import os

from PhysicsTools.NanoAODTools.postprocessing.framework.datamodel import Collection 
from PhysicsTools.NanoAODTools.postprocessing.framework.eventloop import Module

class MHSemiLepVars(Module):
    def __init__(self):
        self.MET  = ROOT.TLorentzVector()
        self.J1   = ROOT.TLorentzVector()
        self.J2   = ROOT.TLorentzVector()
        self.LEP  = ROOT.TLorentzVector()
        self.JJ   = ROOT.TLorentzVector()
        self.LJJ  = ROOT.TLorentzVector()
        self.LMET = ROOT.TLorentzVector()
        self.LMETJJ = ROOT.TLorentzVector()

        self.angle_var = ['dphi', 'deta', 'dr']
        self.angle_obj = ['ljjVmet', 'jVj', 'jjVl', 'lVmet', 'jjVmet']

        self.var = ['mt', 'pz', 'pt', 'm']
        self.obj = ['lmet', 'lmetjj', 'met', 'jj', 'ljj']

        self.el_mass = 0.000511
        self.mu_mass = 0.106

    def beginJob(self):
        pass

    def endJob(self):
        pass

    def beginFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        self.jet_idx_name = ''

        self.out = wrappedOutputTree
        for var in self.angle_var:
            for obj in self.angle_obj:
                self.out.branch('MHlnjj_'+var+'_'+obj, 'F')
        for var in self.var:
            for obj in self.obj:
                self.out.branch('MHlnjj_'+var+'_'+obj, 'F')

        self.out.branch('MHlnjj_pt_l',     'F')
        self.out.branch('MHlnjj_pt_j1',    'F')
        self.out.branch('MHlnjj_pt_j2',    'F')

        self.out.branch('MHlnjj_eta_l',     'F')
        self.out.branch('MHlnjj_eta_j1',    'F')
        self.out.branch('MHlnjj_eta_j2',    'F')

        self.out.branch('MHlnjj_idx_j3',    'I')

        self.out.branch('MHlnjj_PTljj_D_PTmet',     'F')
        self.out.branch('MHlnjj_PTljj_D_Mlmetjj',   'F')
        self.out.branch('MHlnjj_MINPTlj_D_PTmet',   'F')
        self.out.branch('MHlnjj_MINPTlj_D_Mlmetjj', 'F')
        self.out.branch('MHlnjj_MAXPTlj_D_PTmet',   'F')
        self.out.branch('MHlnjj_MAXPTlj_D_Mlmetjj', 'F')
        self.out.branch('MHlnjj_MTljj_D_PTmet',     'F')
        self.out.branch('MHlnjj_MTljj_D_Mlmetjj',   'F')

    def endFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        pass

    def getVec(self, obj):
        obj_split = obj.split('V')
        objl = [None, None]
        for idx in range(len(obj_split)):
            if obj_split[idx] == 'lmetjj': objl[idx] = self.LMETJJ
            elif obj_split[idx] == 'ljj':  objl[idx] = self.LJJ
            elif obj_split[idx] == 'lmet': objl[idx] = self.LMET
            elif obj_split[idx] == 'jj':   objl[idx] = self.JJ
            elif obj_split[idx] == 'j':    
                if idx == 0: objl[idx] = self.J1
                if idx == 1: objl[idx] = self.J2
            elif obj_split[idx] == 'l':    objl[idx] = self.LEP
            elif obj_split[idx] == 'met':  objl[idx] = self.MET

        return objl[0], objl[1]

    def getVal(self, var, obj):
        obj1, obj2 = self.getVec(obj)
        val = None
        if var == 'dphi':   val = abs(obj1.DeltaPhi(obj2)) 
        elif var == 'deta': val = abs(obj1.Eta() - obj2.Eta()) 
        elif var == 'dr':   val = obj1.DeltaR(obj2)
        elif var == 'mt':
            if obj == 'met': val = obj1.Pt()  
            elif 'met' in obj:
                met, temp = self.getVec('met')
                r_obj, temp = self.getVec(obj.replace('met', ''))
                val = math.sqrt( r_obj.M()**2 + 2 * (r_obj.Et()*met.Pt() - r_obj.Pt()*met.Pt()*math.cos(r_obj.DeltaPhi(met))))
            else: 
                obj1, obj2 = self.getVec(obj[0]+'V'+obj[1:])
                val = math.sqrt( obj1.M()**2 + obj2.M()**2 + 2 * (obj1.Et()*obj2.Et() - obj1.Pt()*obj2.Pt()*math.cos(obj1.DeltaPhi(obj2))))
        elif var == 'pz':   val = obj1.Pz()
        elif var == 'pt':   val = obj1.Pt()
        elif var == 'm':    val = obj1.M()
        return val

    def analyze(self, event):
        """process event, return True (go to next module) or False (fail, go to next event)"""
        if self.jet_idx_name=='':
          if hasattr(event, 'idx_j1'): self.jet_idx_name = 'idx_j'
          elif hasattr(event, 'HM_idx_j1'): self.jet_idx_name = 'HM_idx_j'
          else: raise ValueError('MHSemiLepVars: input tree has no variable named "idx_j1" or "HM_idx_j1"')
          print('MHSemiLepVars: jet index string is "'+self.jet_idx_name+'"')

        jets = Collection(event, 'CleanJet')
        org_jets = Collection(event, 'Jet')
        leps = Collection(event, 'Lepton')
        idx_j1 = getattr(event, self.jet_idx_name+'1')
        idx_j2 = getattr(event, self.jet_idx_name+'2')

        if idx_j1 < 0 or idx_j2 < 0:
            for var in self.angle_var:
                for obj in self.angle_obj:
                    self.out.fillBranch('MHlnjj_'+var+'_'+obj, -999.)

            for var in self.var:
                for obj in self.obj:
                    self.out.fillBranch('MHlnjj_'+var+'_'+obj, -999.)

            self.out.fillBranch('MHlnjj_pt_l',     -999.)
            self.out.fillBranch('MHlnjj_pt_j1',    -999.)
            self.out.fillBranch('MHlnjj_pt_j2',    -999.)

            self.out.fillBranch('MHlnjj_eta_l',     -999.)
            self.out.fillBranch('MHlnjj_eta_j1',    -999.)
            self.out.fillBranch('MHlnjj_eta_j2',    -999.)

            self.out.fillBranch('MHlnjj_idx_j3',    -1)

            self.out.fillBranch('MHlnjj_PTljj_D_PTmet',     -999.)
            self.out.fillBranch('MHlnjj_PTljj_D_Mlmetjj',   -999.)
            self.out.fillBranch('MHlnjj_MINPTlj_D_PTmet',   -999.)
            self.out.fillBranch('MHlnjj_MINPTlj_D_Mlmetjj', -999.)
            self.out.fillBranch('MHlnjj_MAXPTlj_D_PTmet',   -999.)
            self.out.fillBranch('MHlnjj_MAXPTlj_D_Mlmetjj', -999.)
            self.out.fillBranch('MHlnjj_MTljj_D_PTmet',     -999.)
            self.out.fillBranch('MHlnjj_MTljj_D_Mlmetjj',   -999.)
             
            return True

        # MET
        self.MET.SetPtEtaPhiM(getattr(event, "PuppiMET_pt"), 0.0, getattr(event, "PuppiMET_phi"), 0.0)
        #self.MET.SetPtEtaPhiE(getattr(event, "PuppiMET_pt"), 0.0, getattr(event, "PuppiMET_phi"), getattr(event, "PuppiMET_sumEt"))
        
        # Jets
        #self.J1.SetPtEtaPhiM(jets[idx_j1].pt, jets[idx_j1].eta, jets[idx_j1].phi, jets[idx_j1].mass)
        #self.J2.SetPtEtaPhiM(jets[idx_j2].pt, jets[idx_j2].eta, jets[idx_j2].phi, jets[idx_j2].mass)
        self.J1.SetPtEtaPhiM(jets[idx_j1].pt, jets[idx_j1].eta, jets[idx_j1].phi, org_jets[jets[idx_j1].jetIdx].mass)
        self.J2.SetPtEtaPhiM(jets[idx_j2].pt, jets[idx_j2].eta, jets[idx_j2].phi, org_jets[jets[idx_j2].jetIdx].mass)
        

        # LEP
        if abs(leps[0].pdgId) == 11:
            self.LEP.SetPtEtaPhiM(leps[0].pt, leps[0].eta, leps[0].phi, self.el_mass)
        elif abs(leps[0].pdgId) == 13:
            self.LEP.SetPtEtaPhiM(leps[0].pt, leps[0].eta, leps[0].phi, self.mu_mass)

        # Constructed objects
        self.JJ = self.J1 + self.J2
        self.LJJ = self.LEP + self.JJ
        self.LMET = self.LEP + self.MET
        self.LMETJJ = self.LMET + self.JJ

        for var in self.angle_var:
            for obj in self.angle_obj:
                self.out.fillBranch('MHlnjj_'+var+'_'+obj, self.getVal(var, obj))

        for var in self.var:
            for obj in self.obj:
                self.out.fillBranch('MHlnjj_'+var+'_'+obj, self.getVal(var, obj))

        self.out.fillBranch('MHlnjj_pt_l',     self.LEP.Pt())
        self.out.fillBranch('MHlnjj_pt_j1',    jets[idx_j1].pt)
        self.out.fillBranch('MHlnjj_pt_j2',    jets[idx_j2].pt)

        self.out.fillBranch('MHlnjj_eta_l',     self.LEP.Eta())
        self.out.fillBranch('MHlnjj_eta_j1',    jets[idx_j1].eta)
        self.out.fillBranch('MHlnjj_eta_j2',    jets[idx_j2].eta)

        self.out.fillBranch('MHlnjj_PTljj_D_PTmet',     self.LJJ.Pt()/self.MET.Pt())
        self.out.fillBranch('MHlnjj_PTljj_D_Mlmetjj',   self.LJJ.Pt()/self.LMETJJ.M())
        self.out.fillBranch('MHlnjj_MINPTlj_D_PTmet',   min(self.LEP.Pt(), self.J2.Pt())/self.MET.Pt())
        self.out.fillBranch('MHlnjj_MINPTlj_D_Mlmetjj', min(self.LEP.Pt(), self.J2.Pt())/self.LMETJJ.M())
        self.out.fillBranch('MHlnjj_MAXPTlj_D_PTmet',   max(self.LEP.Pt(), self.J1.Pt())/self.MET.Pt())
        self.out.fillBranch('MHlnjj_MAXPTlj_D_Mlmetjj', max(self.LEP.Pt(), self.J1.Pt())/self.LMETJJ.M())
        self.out.fillBranch('MHlnjj_MTljj_D_PTmet',     self.getVal('mt', 'ljj')/self.MET.Pt())
        self.out.fillBranch('MHlnjj_MTljj_D_Mlmetjj',   self.getVal('mt', 'ljj')/self.LMETJJ.M())

        all_cj = range(len(jets))
        all_cj.remove(idx_j1)
        all_cj.remove(idx_j2)
        if len(all_cj) > 0: self.out.fillBranch('MHlnjj_idx_j3',    all_cj[0])
        else: self.out.fillBranch('MHlnjj_idx_j3',    -1)
        return True

