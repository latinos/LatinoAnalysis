import ROOT
import os
import re
import math
ROOT.PyConfig.IgnoreCommandLineOptions = True

from PhysicsTools.NanoAODTools.postprocessing.framework.eventloop import Module
from LatinoAnalysis.NanoGardener.data.LeptonSel_cfg import LepFilter_dict 
from LatinoAnalysis.NanoGardener.data.LeptonMaker_cfg import Lepton_br, Lepton_var 
from LatinoAnalysis.NanoGardener.data.LeptonMaker_cfg import VetoLepton_br, VetoLepton_var 
from LatinoAnalysis.NanoGardener.data.LeptonMaker_cfg import CleanJet_br, CleanJet_var 
from LatinoAnalysis.NanoGardener.data.common_cfg import Type_dict

from PhysicsTools.NanoAODTools.postprocessing.framework.datamodel import Collection

class LeptonSel(Module):
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

    def __init__(self, cmssw, LepFilter = 'Loose', nLF = 1, WP_path = 'LatinoAnalysis/NanoGardener/python/data/LeptonSel_cfg.py'):
        self.cmssw = cmssw
        if LepFilter not in ['Loose', 'Veto', 'WgStar']:   raise ValueError('Non existing input tag for LepFilter, possibilities are Loose, Veto os WgStar.')
        if LepFilter == 'WgStar': self.doWgS = True
        else: self.doWgS = False

        #WP_file = open(WP_path, 'r')
        cmssw_base = os.getenv('CMSSW_BASE') 
        var = {}
        execfile(cmssw_base+'/src/'+WP_path, var)
        self.ElectronWP = var['ElectronWP']
        self.MuonWP = var['MuonWP']

        if len(self.ElectronWP[self.cmssw]['VetoObjWP']) > 1:   raise IOError('More then one Electron Veto def given in LeptonSel_cfg')
        if len(self.ElectronWP[self.cmssw]['FakeObjWP']) > 1:   raise IOError('More then one Electron Loose def given in LeptonSel_cfg')
        if len(self.ElectronWP[self.cmssw]['WgStarObjWP']) > 1: raise IOError('More then one Electron WgStar def given in LeptonSel_cfg')
        if len(self.MuonWP[self.cmssw]['VetoObjWP']) > 1:   raise IOError('More then one Muon Veto def given in LeptonSel_cfg')
        if len(self.MuonWP[self.cmssw]['FakeObjWP']) > 1:   raise IOError('More then one Muon Loose def given in LeptonSel_cfg')
        if len(self.MuonWP[self.cmssw]['WgStarObjWP']) > 1: raise IOError('More then one Muon WgStar def given in LeptonSel_cfg')
        self.LepFilter = LepFilter
        self.nLF = nLF
        self.Lep_minPt = [8.0]*self.nLF
        self.JC_maxdR = 0.3 
        self.JC_minPtLep = 10.
        self.JC_absEta   = 5.0

        print('LeptonSel: keeping only '+ self.LepFilter + ' lepton(s), and saving only events with at least ' + str(self.nLF) + ' ' + self.LepFilter + ' lepton(s)')


    def beginJob(self): 
        pass

    def endJob(self):
        pass

    def beginFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        self.initReaders(inputTree) # initReaders must be called in beginFile
        self.out = wrappedOutputTree
        
        # New Branches
        self.out.branch('Lepton_isLoose', 'I', lenVar='nLepton')
        self.out.branch('Lepton_isVeto', 'I', lenVar='nLepton')
        if self.doWgS: self.out.branch('Lepton_isWgs', 'I', lenVar='nLepton')
        self.out.branch('dmZll_veto', 'F') 
        
        for wp in self.ElectronWP[self.cmssw]['TightObjWP']:
           self.out.branch('Lepton_isTightElectron_'+wp, 'I', lenVar='nLepton')
           print 'LeptonSel: ElecWP -> Lepton_isTightElectron_'+wp 
        for wp in self.MuonWP[self.cmssw]['TightObjWP']:
           self.out.branch('Lepton_isTightMuon_'+wp, 'I', lenVar='nLepton')
           print 'LeptonSel: MuWP -> Lepton_isTightMuon_'+wp

        # Old branches to clean
        self.lepBr_to_clean = Lepton_var   
        self.vetlepBr_to_clean = VetoLepton_var   
        self.jetBr_to_clean = CleanJet_var   

        for typ in Lepton_br:
           for name in Lepton_br[typ]:
              self.out.branch(name, typ, lenVar='nLepton')
        for typ in VetoLepton_br:
           for name in VetoLepton_br[typ]:
              self.out.branch(name, typ, lenVar='nVetoLepton')
        for typ in CleanJet_br:
           for name in CleanJet_br[typ]:
              self.out.branch(name, typ, lenVar='nCleanJet')

    def endFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        pass

    def initReaders(self,tree): # this function gets the pointers to Value and ArrayReaders and sets them in the C++ worker class
        self._ttreereaderversion = tree._ttreereaderversion # self._ttreereaderversion must be set AFTER all calls to tree.valueReader or tree.arrayReader
        pass

    #_____Help functions
    def passWP(self, lepton_col, electron_col, muon_col, iLep, WPdict):
        if abs(lepton_col[iLep]['pdgId']) == 11:
           LF_idx = lepton_col[iLep]['electronIdx']
        else:   
           LF_idx = lepton_col[iLep]['muonIdx']
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

    def passWgS(self, lepton_col, electron_col, muon_col):
        nLep = len(lepton_col)
        passWG = [True]*nLep
        
        # First check the ID
        for iLep in range(nLep):
            if abs(lepton_col[iLep]['pdgId']) == 11:
                for wp in self.ElectronWP[self.cmssw]['WgStarObjWP']: 
                    WPdict = self.ElectronWP[self.cmssw]['WgStarObjWP'][wp]
            else:
                for wp in self.MuonWP[self.cmssw]['WgStarObjWP']: 
                    WPdict = self.MuonWP[self.cmssw]['WgStarObjWP'][wp]
            if not self.passWP(lepton_col, electron_col, muon_col, iLep, WPdict): passWG[iLep] = False

        # Now check the isolation     
        looping = True
        while looping:
            looping = False
            for iLep in range(nLep):
                if not passWG[iLep]: continue
                if abs(lepton_col[iLep]['pdgId']) == 11:
                    LF_idx = lepton_col[iLep]['electronIdx']
                    curr_col = electron_col
                    for wp in self.ElectronWP[self.cmssw]['WgStarObjWP']: 
                        WPdict = self.ElectronWP[self.cmssw]['WgStarObjWP'][wp]
                else:
                    LF_idx = lepton_col[iLep]['muonIdx']
                    curr_col = muon_col
                    for wp in self.MuonWP[self.cmssw]['WgStarObjWP']: 
                        WPdict = self.MuonWP[self.cmssw]['WgStarObjWP'][wp]
                pt = 0
                cone_size = WPdict['iso'][1]
                for jLep in range(nLep):
                    if not passWG[jLep]: continue
                    if iLep == jLep: continue
                    if self.isAcloseToB(lepton_col[jLep]['eta'], lepton_col[jLep]['phi'], lepton_col[iLep]['eta'], lepton_col[iLep]['phi'], cone_size) :
                        pt += lepton_col[jLep]['pt']
                rel_pt = pt/lepton_col[iLep]['pt']
                mod_iso = curr_col[LF_idx][WPdict['iso'][0]] - rel_pt
                for part in WPdict['cuts_iso']:
                    cut_val = eval(WPdict['cuts_iso'][part][0])
                    if cut_val is not None:
                        if not (mod_iso < cut_val): 
                            passWG[iLep] = False
                            # Only keep looping if something changed
                            looping = True
        return passWG
    
    #def ConeOverlapPt(self, lepton_col, iLep):
    #    pt = 0
    #    cone_size = 0.4
    #    for jLep in range(len(lepton_col)):
    #       if jLep != iLep:
    #          if self.isAcloseToB(lepton_col[jLep]['eta'], lepton_col[jLep]['phi'],
    #                              lepton_col[iLep]['eta'], lepton_col[iLep]['phi'],
    #                              cone_size) :
    #             pt += lepton_col[jLep]['pt']
    #    return pt

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

        if event._tree._ttreereaderversion > self._ttreereaderversion: # do this check at every event, as other modules might have read further branches
            self.initReaders(event._tree)
        # do NOT access other branches in python between the check/call to initReaders and the call to C++ worker code
       
        lepton_col   = Collection(event, 'Lepton')
        vetolepton_col   = Collection(event, 'VetoLepton')
        electron_col = Collection(event, 'Electron')
        muon_col     = Collection(event, 'Muon')
        jet_col      = Collection(event, 'CleanJet')
        nLep = len(lepton_col) 
        nJet = len(jet_col)
        
        # Fast lepton filter
        if nLep < self.nLF: return False

        # Tags and variables
        Clean_Tag = LepFilter_dict[self.LepFilter]
        Clean_TagWP = LepFilter_dict[Clean_Tag]

        Lep_Tags = {}
        Lep_Tags['isLoose'] = []
        Lep_Tags['isVeto'] = []
        
        for wp in self.ElectronWP[self.cmssw]['TightObjWP']:
           Lep_Tags['isTightElectron_' + wp] = []
        for wp in self.MuonWP[self.cmssw]['TightObjWP']:
           Lep_Tags['isTightMuon_' + wp] = []

        # Cleaning aid
        good_lep_idx = []
        good_vetlep_idx = []
        good_jet_idx = range(nJet)
        Clean_counter = 0

        if self.doWgS:
            Lep_Tags['isWgs'] = []
            Lep_Wgs = self.passWgS(lepton_col, electron_col, muon_col)

        #------ Lepton Loop
        for iLep in range(nLep):
           
           # Check lepton hygiene
           isClean_lep = True
           isVeto_lep = True
           if abs(lepton_col[iLep]['pdgId']) == 11:
              if self.doWgS: isClean_lep = Lep_Wgs[iLep]
              else:
                for wp in self.ElectronWP[self.cmssw][Clean_TagWP]:
                   if not self.passWP(lepton_col, electron_col, muon_col, iLep, self.ElectronWP[self.cmssw][Clean_TagWP][wp]): isClean_lep = False
              for wp in self.ElectronWP[self.cmssw]['VetoObjWP']:
                 if not self.passWP(lepton_col, electron_col, muon_col, iLep, self.ElectronWP[self.cmssw]['VetoObjWP'][wp]): isVeto_lep = False
           elif abs(lepton_col[iLep]['pdgId']) == 13:
              if self.doWgS: isClean_lep = Lep_Wgs[iLep]
              else:
                for wp in self.MuonWP[self.cmssw][Clean_TagWP]:
                   if not self.passWP(lepton_col, electron_col, muon_col, iLep, self.MuonWP[self.cmssw][Clean_TagWP][wp]): isClean_lep = False
              for wp in self.MuonWP[self.cmssw]['VetoObjWP']:
                 if not self.passWP(lepton_col, electron_col, muon_col, iLep, self.MuonWP[self.cmssw]['VetoObjWP'][wp]): isVeto_lep = False

           # Filter illegal lepton pgdId's 
           else: 
              isClean_lep = False
              isVeto_lep = False

           if isVeto_lep:
              good_vetlep_idx.append(iLep)
              Lep_Tags['isVeto'].append(1)
           else:
              Lep_Tags['isVeto'].append(0)
 
           if not isClean_lep: continue
              
           # Lepton id's
           if self.doWgS: Lep_Tags['isWgs'].append(1)
           if abs(lepton_col[iLep]['pdgId']) == 11:
              for wp in self.ElectronWP[self.cmssw]['FakeObjWP']:
                 if self.passWP(lepton_col, electron_col, muon_col, iLep, self.ElectronWP[self.cmssw]['FakeObjWP'][wp]):   Lep_Tags['isLoose'].append(1)
                 else: Lep_Tags['isLoose'].append(0)
              for wp in self.ElectronWP[self.cmssw]['TightObjWP']:
                 if self.passWP(lepton_col, electron_col, muon_col, iLep, self.ElectronWP[self.cmssw]['TightObjWP'][wp]):  Lep_Tags['isTightElectron_' + wp].append(1)
                 else: Lep_Tags['isTightElectron_' + wp].append(0)
              for wp in self.MuonWP[self.cmssw]['TightObjWP']:
                 Lep_Tags['isTightMuon_' + wp].append(0)
           elif abs(lepton_col[iLep]['pdgId']) == 13:
              for wp in self.MuonWP[self.cmssw]['FakeObjWP']:
                 if self.passWP(lepton_col, electron_col, muon_col, iLep, self.MuonWP[self.cmssw]['FakeObjWP'][wp]):   Lep_Tags['isLoose'].append(1)
                 else: Lep_Tags['isLoose'].append(0)
              for wp in self.MuonWP[self.cmssw]['TightObjWP']:
                 if self.passWP(lepton_col, electron_col, muon_col, iLep, self.MuonWP[self.cmssw]['TightObjWP'][wp]):  Lep_Tags['isTightMuon_' + wp].append(1)
                 else: Lep_Tags['isTightMuon_' + wp].append(0)
              for wp in self.ElectronWP[self.cmssw]['TightObjWP']:
                 Lep_Tags['isTightElectron_' + wp].append(0)
           #else: raise ValueError('Unexpected Lepton_pdgId occured: Lepton_pdgId = ' + str(lepton_col[iLep]['pdgId']))

           # Cleaning aids
           good_lep_idx.append(iLep)
           if Clean_counter < self.nLF:
              if lepton_col[iLep]['pt'] > self.Lep_minPt[Clean_counter]: Clean_counter += 1          

           # Jet lepton filter   
           if lepton_col[iLep]['pt'] < self.JC_minPtLep: continue
           Eta_lep = lepton_col[iLep]['eta']
           Phi_lep = lepton_col[iLep]['phi']      
           #------ Jet Loop
           for iJet in good_jet_idx:
              Eta_jet = jet_col[iJet]['eta']
              Phi_jet = jet_col[iJet]['phi']
              if abs(Eta_jet) > self.JC_absEta:
                 if iJet in good_jet_idx: 
                    good_jet_idx.remove(iJet)
              if self.jetIsLepton(Eta_jet, Phi_jet, Eta_lep, Phi_lep):
                 if iJet in good_jet_idx: 
                    good_jet_idx.remove(iJet)

        # Lepton cleaning
        if Clean_counter < self.nLF: return False

        # MET filter (moved to TriggerMaker)
        
        # dmZll
        dmZll = 9999.
        for i in range(len(vetolepton_col)):
           if i not in good_vetlep_idx: continue
           for j in range(len(vetolepton_col)):
              if j not in good_vetlep_idx: continue
              if i == j: continue
              if vetolepton_col[j]['pt'] < 10.: break
              if not vetolepton_col[i]['pdgId'] == -1.*vetolepton_col[j]['pdgId']: continue
              temp_dmZll = abs( math.sqrt(2*vetolepton_col[i]['pt']*vetolepton_col[j]['pt']*\
                                          (math.cosh(vetolepton_col[i]['eta']-vetolepton_col[j]['eta']) - \
                                           math.cos(vetolepton_col[i]['phi']- vetolepton_col[j]['phi']))) - 91.1876)
              if temp_dmZll < dmZll: dmZll = temp_dmZll

        # Filling new branches
        for key in Lep_Tags:
           self.out.fillBranch('Lepton_' + key, Lep_Tags[key])
        self.out.fillBranch('dmZll_veto', dmZll) 

        # Cleaning and filling old branches
        for typ in Lepton_br:
           for name in Lepton_br[typ]:
              temp_v = []
              temp_v = [lepton_col[idx][name[7:]] for idx in good_lep_idx]
              self.out.fillBranch(name, temp_v)
        for typ in VetoLepton_br:
           for name in VetoLepton_br[typ]:
              temp_v = []
              temp_v = [vetolepton_col[idx][name[11:]] for idx in good_vetlep_idx]
              self.out.fillBranch(name, temp_v)
        for typ in CleanJet_br:
           for name in CleanJet_br[typ]:
              temp_v = []
              temp_v = [jet_col[idx][name[9:]] for idx in good_jet_idx]
              self.out.fillBranch(name, temp_v)
 
        return True

# define modules using the syntax 'name = lambda : constructor' to avoid having them loaded when not needed

lepSel = lambda x,y,z:  LeptonSel(x, y, z)
