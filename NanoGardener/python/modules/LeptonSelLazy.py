import ROOT
import os
import re
import math
ROOT.PyConfig.IgnoreCommandLineOptions = True

from PhysicsTools.NanoAODTools.postprocessing.framework.eventloop import Module
from LatinoAnalysis.NanoGardener.data.LeptonSelLazy_cfg import ElectronWP, MuonWP, LepFilter_dict 
from LatinoAnalysis.NanoGardener.data.common_cfg import Type_dict
from PhysicsTools.NanoAODTools.postprocessing.framework.datamodel import Collection
#from LatinoAnalysis.NanoGardener.data.Trigger_names import SPTrigNames

class LeptonSelLazy(Module):
    '''
    Lepton selection module, 
    LepFilter = 'Loose' requires at least nLF Loose leptons per event
    Other possibilities are 'Veto', 'WgStar'
    Still missing: 
                   - puppi jet
 		   - in electron var, dEtaIn and dPhiIn
                   - in muon var, track iso
    Requirement:   
                   - Input tree needs variables added by LeptonMaker
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
        #self.initReaders(inputTree) # initReaders must be called in beginFile
        self.out = wrappedOutputTree
        
        # New Branches
        self.out.branch('Lepton_isLoose', 'I', lenVar='nLepton')
        self.out.branch('VetoLepton_pt', 'F', lenVar='nVetoLepton')
        self.out.branch('VetoLepton_eta', 'F', lenVar='nVetoLepton')
        self.out.branch('VetoLepton_phi', 'F', lenVar='nVetoLepton')
        self.out.branch('VetoLepton_pdgId', 'I', lenVar='nVetoLepton')
        self.out.branch('VetoLepton_instance', 'I', lenVar='nVetoLepton')
        self.out.branch('Lepton_isWgs', 'I', lenVar='nLepton')
        
        for wp in ElectronWP[self.cmssw]['TightObjWP']:
           self.out.branch('Electron_isTight_'+wp, 'I', lenVar='nElectron')
        for wp in MuonWP[self.cmssw]['TightObjWP']:
           self.out.branch('Muon_isTight_'+wp, 'I', lenVar='nMuon')
        if self.cmssw == 'Full2016': self.out.branch('dmZll_veto', 'F') 

        # Old branches to clean
        self.lepBr_to_clean = []   
        self.eleBr_to_clean = []
        self.muBr_to_clean  = []
        self.jetBr_to_clean = []
        for br in inputTree.GetListOfBranches():
           bname = br.GetName()
           btype = Type_dict[br.GetListOfLeaves()[0].GetTypeName()]
           if re.match('\ALepton_', bname):    
              self.lepBr_to_clean.append(bname)
              self.out.branch(bname, btype, lenVar='nLepton') 
           elif re.match('\AElectron_', bname):  
              self.eleBr_to_clean.append(bname)
              self.out.branch(bname, btype, lenVar='nElectron') 
           elif re.match('\AMuon_', bname):
              self.muBr_to_clean.append(bname)
              self.out.branch(bname, btype, lenVar='nMuon') 
           elif re.match('\AJet_', bname):
              self.jetBr_to_clean.append(bname)
              self.out.branch(bname, btype, lenVar='nJet') 

    def endFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        pass

    #_____Help functions
    def passWP(self, iLep, leptons, electrons, muons, WPdict):
        LF_idx = leptons[iLep].instance
        for part in WPdict['cuts']:
           #print "part", part 
           for cut in WPdict['cuts'][part]:
              #print "cut",cut
              if eval(part) and not eval(cut): 
                #print "failed!", part, cut
                return False
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
    
    def ConeOverlapPt(self, iLep, event):
        myevt=event
        pt = 0
        cone_size = 0.4
        for jLep in range(event.nLepton):
           if jLep != iLep:
              if self.isAcloseToB(myevt.Lepton_eta[jLep], myevt.Lepton_phi[jLep],
                                  myevt.Lepton_eta[iLep], myevt.Lepton_phi[iLep],
                                  cone_size) :
                 pt += myevt.Lepton_pt[jLep]
        return pt

    def jetIsLepton(self, jetEta, jetPhi, lepEta, lepPhi) :
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

        #if event._tree._ttreereaderversion > self._ttreereaderversion: # do this check at every event, as other modules might have read further branches
        #    self.initReaders(event._tree)
        # do NOT access other branches in python between the check/call to initReaders and the call to C++ worker code
        
        # Fast lepton filter
        if event.nLepton < self.nLF: return False

        # Tags and variables
        Clean_Tag = LepFilter_dict[self.LepFilter]
        Clean_TagWP = 'FakeObjWP' #LepFilter_dict[Clean_Tag]
        Lep_Tags = {}
        Lep_Tags['isLoose'] = []
        Lep_Tags['isWgs'] = []
        
        VLep_Tags = {}
        VLep_Tags['VetoLepton_pt'] = []
        VLep_Tags['VetoLepton_eta'] = []
        VLep_Tags['VetoLepton_phi'] = []
        VLep_Tags['VetoLepton_pdgId'] = []
        VLep_Tags['VetoLepton_instance'] = []

        El_Tags = {}
        for wp in ElectronWP[self.cmssw]['TightObjWP']:
           El_Tags[wp] = []
        Mu_Tags = {}
        for wp in MuonWP[self.cmssw]['TightObjWP']:
           Mu_Tags[wp] = []

        # Cleaning aid
        good_lep_idx = []
        good_ele_idx = []
        good_muo_idx = []
        good_jet_idx = range(event.nJet)
        Clean_counter = 0
        
        good_ele_count = 0
        good_muo_count = 0
        new_lep_instance = []

        leptons   = Collection(event, "Lepton")
        jets      = Collection(event, "Jet")
        electrons = Collection(event, "Electron")
        muons     = Collection(event, "Muon")

        #------ Lepton Loop
        for iLep in range(event.nLepton):
           leptons[iLep].ConeOverlapPt = self.ConeOverlapPt(iLep, event)
           # Check lepton hygiene
           isClean_lep = True
           isVeto_lep = True
           if abs(leptons[iLep].pdgId) == 11:
              for wp in ElectronWP[self.cmssw][Clean_TagWP]:
                 if not self.passWP(iLep, leptons, electrons, muons, ElectronWP[self.cmssw][Clean_TagWP][wp]): isClean_lep = False
                 else:
                    new_lep_instance.append(good_ele_count) 
                    good_ele_count += 1
              for wp in ElectronWP[self.cmssw]['VetoObjWP']:
                 if not self.passWP(iLep, leptons, electrons, muons, ElectronWP[self.cmssw]['VetoObjWP'][wp]): isVeto_lep = False
           elif abs(leptons[iLep].pdgId) == 13:
              for wp in MuonWP[self.cmssw][Clean_TagWP]:
                 if not self.passWP(iLep, leptons, electrons, muons, MuonWP[self.cmssw][Clean_TagWP][wp]): isClean_lep = False
                 else:
                    new_lep_instance.append(good_muo_count) 
                    good_muo_count += 1
              for wp in MuonWP[self.cmssw]['VetoObjWP']:
                 if not self.passWP(iLep, leptons, electrons, muons, MuonWP[self.cmssw]['VetoObjWP'][wp]): isVeto_lep = False
           if isVeto_lep:
              VLep_Tags['VetoLepton_pt'].append(leptons[iLep].pt)
              VLep_Tags['VetoLepton_eta'].append(leptons[iLep].eta)
              VLep_Tags['VetoLepton_phi'].append(leptons[iLep].phi)
              VLep_Tags['VetoLepton_pdgId'].append(leptons[iLep].pdgId)
              if isClean_lep: VLep_Tags['VetoLepton_instance'].append(new_lep_instance[-1])
              else: VLep_Tags['VetoLepton_instance'].append(-1)
 
           if not isClean_lep: continue
              
           # Lepton id's
           if abs(leptons[iLep].pdgId) == 11:
              for wp in ElectronWP[self.cmssw]['FakeObjWP']:
                 if self.passWP(iLep, leptons, electrons, muons, ElectronWP[self.cmssw]['FakeObjWP'][wp]):   Lep_Tags['isLoose'].append(1)
                 else: Lep_Tags['isLoose'].append(0)
              for wp in ElectronWP[self.cmssw]['WgStarObjWP']:
                 if self.passWP(iLep, leptons, electrons, muons, ElectronWP[self.cmssw]['WgStarObjWP'][wp]): Lep_Tags['isWgs'].append(1)
                 else: Lep_Tags['isWgs'].append(0)
              for wp in ElectronWP[self.cmssw]['TightObjWP']:
                 if self.passWP(iLep, leptons, electrons, muons, ElectronWP[self.cmssw]['TightObjWP'][wp]):  El_Tags[wp].append(1)
                 else: El_Tags[wp].append(0)
           elif abs(leptons[iLep].pdgId) == 13:
              for wp in MuonWP[self.cmssw]['FakeObjWP']:
                 if self.passWP(iLep, leptons, electrons, muons, MuonWP[self.cmssw]['FakeObjWP'][wp]):   Lep_Tags['isLoose'].append(1)
                 else: Lep_Tags['isLoose'].append(0)
              for wp in MuonWP[self.cmssw]['WgStarObjWP']:
                 if self.passWP(iLep, leptons, electrons, muons, MuonWP[self.cmssw]['WgStarObjWP'][wp]): Lep_Tags['isWgs'].append(1)
                 else: Lep_Tags['isWgs'].append(0)
              for wp in MuonWP[self.cmssw]['TightObjWP']:
                 if self.passWP(iLep, leptons, electrons, muons, MuonWP[self.cmssw]['TightObjWP'][wp]):  Mu_Tags[wp].append(1)
                 else: Mu_Tags[wp].append(0)
           else: raise ValueError('Unexpected pdgId in Lepton_pdgId: ' + str(self.lepton_var['Lepton_pdgId'][iLep]))

           # Cleaning aids
           good_lep_idx.append(iLep)
           if   abs(leptons[iLep].pdgId) == 11: good_ele_idx.append(leptons[iLep].instance) 
           elif abs(leptons[iLep].pdgId) == 13: good_muo_idx.append(leptons[iLep].instance) 
           if Clean_counter < self.nLF:
              if leptons[iLep].pt > self.Lep_minPt[Clean_counter]: Clean_counter += 1          

           # Jet lepton filter   
           if leptons[iLep].pt < self.JC_minPtLep: continue
           Eta_lep = leptons[iLep].eta
           Phi_lep = leptons[iLep].phi     
            

           #------ Jet Loop
           for iJet in good_jet_idx:
              Eta_jet = jets[iJet].eta
              Phi_jet = jets[iJet].phi
              if self.jetIsLepton(Eta_jet, Phi_jet, Eta_lep, Phi_lep):
                 if iLep in good_jet_idx: 
                    good_jet_idx.remove(iJet)

        # Lepton cleaning
        if Clean_counter < self.nLF: return False

        # MET filter (moved to TriggerMaker)
        
        # dmZll
        dmZll = 9999.
        for i in range(len(VLep_Tags['VetoLepton_pt'])):
           for j in range(len(VLep_Tags['VetoLepton_pt'])):
              if i == j: continue
              if VLep_Tags['VetoLepton_pt'][j] < 10.: break
              if not VLep_Tags['VetoLepton_pdgId'][i] == -1.*VLep_Tags['VetoLepton_pdgId'][j]: continue
              temp_dmZll = abs( math.sqrt(2*VLep_Tags['VetoLepton_pt'][i]*VLep_Tags['VetoLepton_pt'][j]*\
                                          (math.cosh(VLep_Tags['VetoLepton_eta'][i]-VLep_Tags['VetoLepton_eta'][j]) - \
                                           math.cos(VLep_Tags['VetoLepton_phi'][i]- VLep_Tags['VetoLepton_phi'][j]))) - 91.1876)
              if temp_dmZll < dmZll: dmZll = temp_dmZll

        # Filling new branches
        for key in Lep_Tags:
           self.out.fillBranch('Lepton_' + key, Lep_Tags[key])
        for key in El_Tags:
           self.out.fillBranch('Electron_isTight_' + key, El_Tags[key])
        for key in Mu_Tags:
           self.out.fillBranch('Muon_isTight_' + key, Mu_Tags[key])

        for name in VLep_Tags:
           self.out.fillBranch(name, VLep_Tags[name])     
 
        self.out.fillBranch('dmZll_veto', dmZll) 

        # Cleaning and filling old branches
        for name in self.lepBr_to_clean:
           if name == 'Lepton_instance': self.out.fillBranch(name, new_lep_instance)
           else:
              temp_v = []
              varname=name.split("_", 1)[1]
              #if self.lepton_var[name]:
              #   if type(self.lepton_var[name][0]) is str: temp_v = [ord(self.lepton_var[name][idx]) for idx in good_lep_idx]
              #   else: temp_v = [self.lepton_var[name][idx] for idx in good_lep_idx]
              temp_v = [getattr(leptons[idx], varname) for idx in good_lep_idx]
              self.out.fillBranch(name, temp_v)
        for name in self.eleBr_to_clean:
           temp_v = []
           varname=name.split("_", 1)[1]
           #if self.electron_var[name]:
              #if type(self.electron_var[name][0]) is str: temp_v = [ord(self.electron_var[name][idx]) for idx in good_ele_idx]
              #else: temp_v = [self.electron_var[name][idx] for idx in good_ele_idx]
           temp_v = [getattr(electrons[idx], varname) for idx in good_ele_idx ]  
           self.out.fillBranch(name, temp_v)
        for name in self.muBr_to_clean:
           temp_v = []
           varname=name.split("_", 1)[1]
           #if self.muon_var[name]:
              #if type(self.muon_var[name][0]) is str: temp_v = [ord(self.muon_var[name][idx]) for idx in good_muo_idx]
              #else: temp_v = [self.muon_var[name][idx] for idx in good_muo_idx]
           temp_v = [getattr(muons[idx], varname) for idx in good_muo_idx ]   
           self.out.fillBranch(name, temp_v)
        for name in self.jetBr_to_clean:
           varname=name.split("_", 1)[1]
           temp_v = []
           #if self.jet_var[name]:
              #if type(self.jet_var[name][0]) is str: temp_v = [ord(self.jet_var[name][idx]) for idx in good_jet_idx]
              #else: temp_v = [self.jet_var[name][idx] for idx in good_jet_idx]
           temp_v = [getattr(jets[idx], varname) for idx in good_jet_idx ]   
           self.out.fillBranch(name, temp_v)
 
        return True

# define modules using the syntax 'name = lambda : constructor' to avoid having them loaded when not needed

lepSelLazy = lambda x,y,z:  LeptonSelLazy(x, y, z)
