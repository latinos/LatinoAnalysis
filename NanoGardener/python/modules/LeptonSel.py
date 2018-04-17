import ROOT
import os
import re
import math
ROOT.PyConfig.IgnoreCommandLineOptions = True

from PhysicsTools.NanoAODTools.postprocessing.framework.eventloop import Module
from LatinoAnalysis.NanoGardener.data.LeptonSel_cfg import ElectronWP, MuonWP, LepFilter_dict 
#from LatinoAnalysis.NanoGardener.data.Trigger_names import SPTrigNames

class LeptonSel(Module):
    '''
    put this file in LatinoAnalysis/NanoGardener/python/modules/
    Lepton selection module, 
    LepFilter = 'Loose' requires at least nLF Loose leptons per event
    Other possibilities are 'Veto', 'WgStar'
    Still missing: 
                   - puppi jet
		   - way to delete elements from existing branches (lepton, jet cleaning)
 		   - in electron var, dEtaIn and dPhiIn
                   - in muon var, track iso
    Requirement:   
                   - Adapted arrayReader (remove error for unfound leafcounter)
                   - Input tree needs variables added by VarMaker
    ''' 

    def __init__(self, cmssw, LepFilter = None, nLF = None):
        self.cmssw = cmssw
        if LepFilter not in LepFilter_dict:    raise ValueError('Non existing input tag for LepFilter, possibilities are Loose, Veto os WgStar.')
        if len(ElectronWP[self.cmssw]['VetoObjWP']) > 1:   raise IOError('More then one Electron Veto def given in LeptonSel_cfg')
        if len(ElectronWP[self.cmssw]['FakeObjWP']) > 1:   raise IOError('More then one Electron Loose def given in LeptonSel_cfg')
        if len(ElectronWP[self.cmssw]['WgStarObjWP']) > 1: raise IOError('More then one Electron WgStar def given in LeptonSel_cfg')
        if len(MuonWP[self.cmssw]['VetoObjWP']) > 1:   raise IOError('More then one Muon Veto def given in LeptonSel_cfg')
        if len(MuonWP[self.cmssw]['FakeObjWP']) > 1:   raise IOError('More then one Muon Loose def given in LeptonSel_cfg')
        if len(MuonWP[self.cmssw]['WgStarObjWP']) > 1: raise IOError('More then one Muon WgStar def given in LeptonSel_cfg')
        self.LepFilter = LepFilter
        self.nLF = nLF
        self.Lep_minPt = [8.0]*self.nLF
        self.JC_maxdR = 0.3 
        self.JC_minPtLep = 10.
        self.JC_absEta   = 5.0
        print('LeptonSel: only saving events with at least ' + str(self.nLF) + ' ' + self.LepFilter + ' lepton(s)')

    def beginJob(self): 
        pass

    def endJob(self):
        pass

    def beginFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        self.initReaders(inputTree) # initReaders must be called in beginFile
        #self.lepBr_to_clean = []
        #self.eleBr_to_clean = []
        #self.muBr_to_clean = []
        #for br in tree.GetListOfBranches():
        #   bname = br.GetName()
        #   if re.match('\ALepton_', bname):    self.lepBr_to_clean.append(bname) 
        #   if re.match('\AElectron_', bname):  self.eleBr_to_clean.append(bname)
        #   if re.match('\AMuon_', bname):      self.muBr_to_clean.append(bname)
        #   if re.match('\AJet_', bname):       self.jetBr_to_clean.append(bname)

        self.out = wrappedOutputTree
        self.out.branch('Lepton_isLoose', 'I', lenVar='nLepton')
        self.out.branch('Lepton_isVeto', 'I', lenVar='nLepton')
        self.out.branch('Lepton_isWgs', 'I', lenVar='nLepton')
        
        for wp in ElectronWP[self.cmssw]['TightObjWP']:
           self.out.branch('Electron_isTight_'+wp, 'I', lenVar='nElectron')
        for wp in MuonWP[self.cmssw]['TightObjWP']:
           self.out.branch('Muon_isTight_'+wp, 'I', lenVar='nMuon')
        self.out.branch('Jet_isLepton', 'I', lenVar='nJet')
        if self.cmssw == 'Full2016': self.out.branch('dmZll_veto', 'F') 

        # Cleaning branches
        #for name in self.lepBr_to_clean:
        #   self.out.branch(name, 'F', lenVar='nLepton')
        #for name in self.eleBr_to_clean:
        #   self.out.branch(name, 'F', lenVar='nElectron')
        #for name in self.muBr_to_clean:
        #   self.out.branch(name, 'F', lenVar='nMuon')
        #for name in self.jetBr_to_clean:
        #   self.out.branch(name, 'F', lenVar='nJet')

    def endFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        pass

    def initReaders(self,tree): # this function gets the pointers to Value and ArrayReaders and sets them in the C++ worker class
        b = tree.GetListOfBranches()
        
        self.electron_var = {}
        self.muon_var = {}
        self.lepton_var = {}
        self.jet_var = {}
        for br in b:
           bname = br.GetName()
           if re.match('\ALepton_', bname):    self.lepton_var[bname] = tree.arrayReader(bname)
           if re.match('\AElectron_', bname):  self.electron_var[bname] = tree.arrayReader(bname)
           if re.match('\AMuon_', bname):      self.muon_var[bname] = tree.arrayReader(bname)
           if re.match('\AJet_', bname):       self.jet_var[bname] = tree.arrayReader(bname)
    
        #self.SPTrigger_bits = tree.arrayReader('SPTrigger_bits')

        #self.SPtrigger = {}
        #for i in range(len(SPTrigNames)):
        #   if self.is_SPtrigger[i]: self.SPtrigger[SPTrigNames[i]] = tree.valueReader(SPTrigNames[i])

        self.nLepton = tree.valueReader('nLepton')
        #self.nElectron = tree.valueReader('nElectron')
        #self.nMuon = tree.valueReader('nMuon')
        self.nJet = tree.valueReader('nJet')
        self._ttreereaderversion = tree._ttreereaderversion # self._ttreereaderversion must be set AFTER all calls to tree.valueReader or tree.arrayReader

    #_____Help functions
    def passWP(self, iLep, WPdict):
        LF_idx = self.lepton_var['Lepton_instance'][iLep]
        for part in WPdict['cuts']:
           for cut in WPdict['cuts'][part]:
              if eval(part) and not eval(cut): return False
        return True

    def isAcloseToB(self, a_Eta, a_Phi, b_Eta, b_Phi, drmax) :
        dPhi = ROOT.TMath.Abs(b_Phi - a_Phi)
        if dPhi > ROOT.TMath.Pi() :
           dPhi = 2*ROOT.TMath.Pi() - dPhi
        dR2 = (b_Eta - a_Eta) * (b_Eta - a_Eta) + dPhi * dPhi
        if dR2 < (drmax*drmax):
           return True
        else:
           return False
    
    def ConeOverlapPt(self, iLep):
        pt = 0
        cone_size = 0.4
        for jLep in range(int(self.nLepton)):
           if jLep != iLep:
              if self.isAcloseToB(self.lepton_var['Lepton_eta'][jLep], self.lepton_var['Lepton_phi'][jLep],
                                  self.lepton_var['Lepton_eta'][iLep], self.lepton_var['Lepton_phi'][iLep],
                                  cone_size) :
                 pt += self.lepton_var['Lepton_pt'][jLep]
        return pt

    def jetIsLepton(self, jetEta, jetPhi, lepEta, lepPhi) :
        #dR = ROOT.TMath.Sqrt( ROOT.TMath.Power(lepEta - jetEta, 2) + ROOT.TMath.Power(ROOT.TMath.Abs(ROOT.TMath.Abs(lepPhi - jetPhi)-ROOT.TMath.Pi())-ROOT.TMath.Pi(), 2) )
        dPhi = ROOT.TMath.Abs(lepPhi - jetPhi)
        if dPhi > ROOT.TMath.Pi() :
          dPhi = 2*ROOT.TMath.Pi() - dPhi
        dR2 = (lepEta - jetEta) * (lepEta - jetEta) + dPhi * dPhi
        if dR2 < self.JC_maxdR*self.JC_maxdR:
            return True
        else:
            return False

    #_____Analyze
    def analyze(self, event):
        """process event, return True (go to next module) or False (fail, go to next event)"""

        if event._tree._ttreereaderversion > self._ttreereaderversion: # do this check at every event, as other modules might have read further branches
            self.initReaders(event._tree)
        # do NOT access other branches in python between the check/call to initReaders and the call to C++ worker code
        
        # Fast lepton filter
        if self.nLepton < self.nLF: return False
        #if int(self.nElectron) + int(self.nMuon) < int(self.nLF): return False

        # Tags and variables
        Clean_Tag = LepFilter_dict[self.LepFilter]
        Lep_Tags = {}
        Lep_Tags['isLoose'] = []
        Lep_Tags['isVeto'] = []
        Lep_Tags['isWgs'] = []
        El_Tags = {}
        for wp in ElectronWP[self.cmssw]['TightObjWP']:
           El_Tags[wp] = []
        Mu_Tags = {}
        for wp in MuonWP[self.cmssw]['TightObjWP']:
           Mu_Tags[wp] = []
        JC_Tag = [0]*int(self.nJet)

        Clean_counter = 0

        #------ Lepton Loop
        for iLep in range(int(self.nLepton)):
    
           # Lepton id's
           if abs(self.lepton_var['Lepton_pdgId'][iLep]) == 11:
              for wp in ElectronWP[self.cmssw]['FakeObjWP']:
                 if self.passWP(iLep, ElectronWP[self.cmssw]['FakeObjWP'][wp]):   Lep_Tags['isLoose'].append(1)
                 else: Lep_Tags['isLoose'].append(0)
              for wp in ElectronWP[self.cmssw]['VetoObjWP']:
                 if self.passWP(iLep, ElectronWP[self.cmssw]['VetoObjWP'][wp]):   Lep_Tags['isVeto'].append(1)
                 else: Lep_Tags['isVeto'].append(0)
              for wp in ElectronWP[self.cmssw]['WgStarObjWP']:
                 if self.passWP(iLep, ElectronWP[self.cmssw]['WgStarObjWP'][wp]): Lep_Tags['isWgs'].append(1)
                 else: Lep_Tags['isWgs'].append(0)
              for wp in ElectronWP[self.cmssw]['TightObjWP']:
                 if self.passWP(iLep, ElectronWP[self.cmssw]['TightObjWP'][wp]):  El_Tags[wp].append(1)
                 else: El_Tags[wp].append(0)
           elif abs(self.lepton_var['Lepton_pdgId'][iLep]) == 13:
              for wp in MuonWP[self.cmssw]['FakeObjWP']:
                 if self.passWP(iLep, MuonWP[self.cmssw]['FakeObjWP'][wp]):   Lep_Tags['isLoose'].append(1)
                 else: Lep_Tags['isLoose'].append(0)
              for wp in MuonWP[self.cmssw]['VetoObjWP']:
                 if self.passWP(iLep, MuonWP[self.cmssw]['VetoObjWP'][wp]):   Lep_Tags['isVeto'].append(1)
                 else: Lep_Tags['isVeto'].append(0)
              for wp in MuonWP[self.cmssw]['WgStarObjWP']:
                 if self.passWP(iLep, MuonWP[self.cmssw]['WgStarObjWP'][wp]): Lep_Tags['isWgs'].append(1)
                 else: Lep_Tags['isWgs'].append(0)
              for wp in MuonWP[self.cmssw]['TightObjWP']:
                 if self.passWP(iLep, MuonWP[self.cmssw]['TightObjWP'][wp]):  Mu_Tags[wp].append(1)
                 else: Mu_Tags[wp].append(0)
           else: raise ValueError('Unexpected pdgId in Lepton_pdgId: ' + str(self.lepton_var['Lepton_pdgId'][iLep]))

           if Lep_Tags[Clean_Tag][-1] and Clean_counter < self.nLF:
              if self.lepton_var['Lepton_pt'][iLep] > self.Lep_minPt[Clean_counter]: Clean_counter += 1          

           # Jet lepton filter   
           if self.lepton_var['Lepton_pt'][iLep] < self.JC_minPtLep: continue
           if not Lep_Tags[Clean_Tag][-1]: continue
           Eta_lep = self.lepton_var['Lepton_eta'][iLep]
           Phi_lep = self.lepton_var['Lepton_phi'][iLep]      
           #------ Jet Loop
           for iJet in range(int(self.nJet)):
              Eta_jet = self.jet_var['Jet_eta'][iJet]
              Phi_jet = self.jet_var['Jet_phi'][iJet]
              if self.jetIsLepton(Eta_jet, Phi_jet, Eta_lep, Phi_lep): JC_Tag[iJet] = 1

        # Lepton cleaning
        if Clean_counter < self.nLF: return False

        # MET filter
        #metF_pass = 1
        #for bit in self.SPTrigger_bits:
        #   if bit == 0: 
        #      metF_pass = 0
        #      break
        
        # dmZll
        if self.cmssw == 'Full2016':
           dmZll = 9999.
           for iLep in range(int(self.nLepton)):
              if not Lep_Tags['isVeto'][iLep] == 1: continue
              for jLep in range(int(self.nLepton)):
                 if not Lep_Tags['isVeto'][jLep] == 1: continue
                 if self.lepton_var['Lepton_pt'][jLep] < 10.: break
                 if not self.lepton_var['Lepton_pdgId'][iLep] == -1.*self.lepton_var['Lepton_pdgId'][jLep]: continue
                 temp_dmZll = abs( math.sqrt(2*self.lepton_var['Lepton_pt'][iLep]*self.lepton_var['Lepton_pt'][jLep]*\
                                             (math.cosh(self.lepton_var['Lepton_eta'][iLep]-self.lepton_var['Lepton_eta'][jLep]) - \
                                              math.cos(self.lepton_var['Lepton_phi'][iLep]- self.lepton_var['Lepton_phi'][jLep]))) - 91.1876)
                 if temp_dmZll < dmZll: dmZll = temp_dmZll
           self.out.fillBranch('dmZll_veto', dmZll) 

        # Branch filling
        for key in Lep_Tags:
           self.out.fillBranch('Lepton_' + key, Lep_Tags[key])
        for key in El_Tags:
           self.out.fillBranch('Electron_isTight_' + key, El_Tags[key])
        for key in Mu_Tags:
           self.out.fillBranch('Muon_isTight_' + key, Mu_Tags[key])
       
        #self.out.fillBranch('metFilter', metF_pass)
        self.out.fillBranch('Jet_isLepton', JC_Tag)

        return True

# define modules using the syntax 'name = lambda : constructor' to avoid having them loaded when not needed

lepSel = lambda x,y,z:  LeptonSel(x, y, z)
