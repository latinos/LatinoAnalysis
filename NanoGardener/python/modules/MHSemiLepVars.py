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
        self.out = wrappedOutputTree
        for var in self.angle_var:
            for obj in self.angle_obj:
                self.out.branch('MHlnjj_'+var+'_'+obj, 'F')
        for var in self.var:
            for obj in self.obj:
                self.out.branch('MHlnjj_'+var+'_'+obj, 'F')

        self.out.branch('MHlnjj_PTljj_D_PTmet',     'F')
        self.out.branch('MHlnjj_PTljj_D_Mlmetjj',   'F')
        self.out.branch('MHlnjj_MINPTlj_D_PTmet',   'F')
        self.out.branch('MHlnjj_MINPTlj_D_Mlmetjj', 'F')

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
        elif var == 'mt':   val = obj1.Mt()
        elif var == 'pz':   val = obj1.Pz()
        elif var == 'pt':   val = obj1.Pt()
        elif var == 'm':    val = obj1.M()
        return val

    def analyze(self, event):
        """process event, return True (go to next module) or False (fail, go to next event)"""

        jets = Collection(event, 'Jet')
        leps = Collection(event, 'Lepton')

        if event.idx_j1 < 0 or event.idx_j2 < 0:
            for var in self.angle_var:
                for obj in self.angle_obj:
                    self.out.fillBranch('MHlnjj_'+var+'_'+obj, -999.)

            for var in self.var:
                for obj in self.obj:
                    self.out.fillBranch('MHlnjj_'+var+'_'+obj, -999.)

            self.out.fillBranch('MHlnjj_PTljj_D_PTmet',     -999.)
            self.out.fillBranch('MHlnjj_PTljj_D_Mlmetjj',   -999.)
            self.out.fillBranch('MHlnjj_MINPTlj_D_PTmet',   -999.)
            self.out.fillBranch('MHlnjj_MINPTlj_D_Mlmetjj', -999.)
             
            return True

        # MET
        self.MET.SetPtEtaPhiM(getattr(event, "PuppiMET_pt"), 0.0, getattr(event, "PuppiMET_phi"), 0.0)
        #self.MET.SetPtEtaPhiE(getattr(event, "PuppiMET_pt"), 0.0, getattr(event, "PuppiMET_phi"), getattr(event, "PuppiMET_sumEt"))
        
        # Jets
        self.J1.SetPtEtaPhiM(jets[event.idx_j1].pt, jets[event.idx_j1].eta, jets[event.idx_j1].phi, jets[event.idx_j1].mass)
        self.J2.SetPtEtaPhiM(jets[event.idx_j2].pt, jets[event.idx_j2].eta, jets[event.idx_j2].phi, jets[event.idx_j2].mass)

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

        self.out.fillBranch('MHlnjj_PTljj_D_PTmet',     self.LJJ.Pt()/self.MET.Pt())
        self.out.fillBranch('MHlnjj_PTljj_D_Mlmetjj',   self.LJJ.Pt()/self.LMETJJ.M())
        self.out.fillBranch('MHlnjj_MINPTlj_D_PTmet',   min(self.LEP.Pt(), self.J2.Pt())/self.MET.Pt())
        self.out.fillBranch('MHlnjj_MINPTlj_D_Mlmetjj', min(self.LEP.Pt(), self.J2.Pt())/self.LMETJJ.M())

        return True

