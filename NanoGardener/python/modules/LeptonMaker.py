import ROOT
import os
import re
ROOT.PyConfig.IgnoreCommandLineOptions = True

from PhysicsTools.NanoAODTools.postprocessing.framework.eventloop import Module
from LatinoAnalysis.NanoGardener.data.LeptonMaker_cfg import Lepton_br, Lepton_var 
from LatinoAnalysis.NanoGardener.data.LeptonMaker_cfg import VetoLepton_br, VetoLepton_var 
from LatinoAnalysis.NanoGardener.data.LeptonMaker_cfg import CleanJet_br, CleanJet_var 
from LatinoAnalysis.NanoGardener.data.common_cfg import Type_dict

class LeptonMaker(Module): 
    '''
    put this file in LatinoAnalysis/NanoGardener/python/modules/
    Add extra variables to NANO tree
    '''
    def __init__(self, min_lep_pt = [10]):
        self.min_lep_pt = min_lep_pt
        self.min_lep_pt_idx = range(len(min_lep_pt))
        print_str = ''
        for idx in self.min_lep_pt_idx:
            print_str += 'Lepton_pt[' + str(idx) + '] > ' + str(min_lep_pt[idx])
            if not idx == self.min_lep_pt_idx[-1]: print_str += ', '
        print('LeptonMaker: ' + print_str)

    def beginJob(self): 
        pass

    def endJob(self):
        pass

    def beginFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        self.initReaders(inputTree) # initReaders must be called in beginFile
        self.out = wrappedOutputTree

        # New branches
        for typ in Lepton_br:
           for var in Lepton_br[typ]:
              if 'Lepton_' in var: self.out.branch(var, typ, lenVar='nLepton')
        for typ in VetoLepton_br:
           for var in VetoLepton_br[typ]:
              if 'VetoLepton_' in var: self.out.branch(var, typ, lenVar='nVetoLepton')
        for typ in CleanJet_br:
           for var in CleanJet_br[typ]:
              if 'CleanJet_' in var: self.out.branch(var, typ, lenVar='nCleanJet')

    def endFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        pass

    def initReaders(self,tree): # this function gets the pointers to Value and ArrayReaders and sets them in the C++ worker class
        self.electron_var = {}
        self.muon_var = {}
        self.jet_var = {}
        for br in tree.GetListOfBranches():
           bname = br.GetName()
           if re.match('\AElectron_', bname):  self.electron_var[bname] = tree.arrayReader(bname)
           if re.match('\AMuon_', bname):      self.muon_var[bname] = tree.arrayReader(bname)
           if re.match('\AJet_', bname):       self.jet_var[bname] = tree.arrayReader(bname)

        self.nElectron = tree.valueReader('nElectron')
        self.nMuon = tree.valueReader('nMuon')
        self.nJet = tree.valueReader('nJet')
        self._ttreereaderversion = tree._ttreereaderversion # self._ttreereaderversion must be set AFTER all calls to tree.valueReader or tree.arrayReader

    def analyze(self, event):
        """process event, return True (go to next module) or False (fail, go to next event)"""

        if event._tree._ttreereaderversion > self._ttreereaderversion: # do this check at every event, as other modules might have read further branches
            self.initReaders(event._tree)
        # do NOT access other branches in python between the check/call to initReaders and the call to C++ worker code
        
        #--- Set vars
        nEl = int(self.nElectron)
        nMu = int(self.nMuon)
        nJt = int(self.nJet)
        nLep = nMu + nEl

        if nLep < len(self.min_lep_pt): return False

        lep_dict = {}
        for lv in Lepton_var:
           lep_dict[lv] = [0]*nLep
        lep_dict['electronIdx'] = [-1]*nLep
        lep_dict['muonIdx'] = [-1]*nLep
        
        jet_dict = {}
        for jv in CleanJet_var:
           jet_dict[jv] = [0]*nJt
        jet_dict['jetIdx'] = [0]*nJt
        
        #--- Lepton Loops
        for iLep1 in range(nLep):
           pt_idx = 0
           if iLep1 < nEl:
              pt1 = self.electron_var['Electron_pt'][iLep1]
              pdgId1 = self.electron_var['Electron_pdgId'][iLep1]
           else:
              pt1 = self.muon_var['Muon_pt'][iLep1 - nEl]
              pdgId1 = self.muon_var['Muon_pdgId'][iLep1 - nEl]
           # Start comparing leptons
           for iLep2 in range(nLep):
              if iLep2 == iLep1: continue
              if iLep2 < nEl:
                 pt2 = self.electron_var['Electron_pt'][iLep2]
              else:
                 pt2 = self.muon_var['Muon_pt'][iLep2 - nEl]
              if pt1 < pt2 or (pt1==pt2 and iLep1>iLep2):
                 pt_idx += 1
                

           # Pt filter
           if pt_idx in self.min_lep_pt_idx and pt1 < self.min_lep_pt[pt_idx]: return False
           
           # Now index is set, fill the vars  
           if abs(pdgId1) == 11:
              for var in lep_dict:
                 if not 'Idx' in var:
                    lep_dict[var][pt_idx] = self.electron_var['Electron_'+var][iLep1]
                 elif 'electronIdx' in var:
                    lep_dict[var][pt_idx] = iLep1
           elif abs(pdgId1) == 13:
              for var in lep_dict:
                 if not 'Idx' in var and not 'eCorr' in var:
                    lep_dict[var][pt_idx] = self.muon_var['Muon_'+var][iLep1 - nEl]
                 elif 'eCorr' in var:
                    lep_dict[var][pt_idx] = 1.
                 elif 'muonIdx' in var:
                    lep_dict[var][pt_idx] = iLep1 - nEl
        #--- Jet Loops
        for iJ1 in range(nJt):
           pt_idx = 0
           pt1 = self.jet_var['Jet_pt'][iJ1]
           # Start comparing jets
           for iJ2 in range(nJt):
              if iJ2 == iJ1: continue
              pt2 = self.jet_var['Jet_pt'][iJ2]
              if pt1 < pt2 or (pt1==pt2 and iJ1>iJ2):
                 pt_idx += 1
           # Now index is set, fill the vars  
           for var in jet_dict:
              if not 'Idx' in var:
                 jet_dict[var][pt_idx] = self.jet_var['Jet_' + var][iJ1]
              else:
                 jet_dict[var][pt_idx] = iJ1

        #--- Fill branches
        for var in lep_dict:
           self.out.fillBranch('Lepton_' + var, lep_dict[var])
           if var in VetoLepton_var + ['electronIdx', 'muonIdx']:
              self.out.fillBranch('VetoLepton_' + var, lep_dict[var])
        for var in jet_dict:
           self.out.fillBranch( 'CleanJet_' + var, jet_dict[var])

        return True


# define modules using the syntax 'name = lambda : constructor' to avoid having them loaded when not needed

lepMkr = lambda : LeptonMaker()
