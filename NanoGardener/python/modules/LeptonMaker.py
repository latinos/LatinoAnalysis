import ROOT
import os
import re
ROOT.PyConfig.IgnoreCommandLineOptions = True

from PhysicsTools.NanoAODTools.postprocessing.framework.eventloop import Module
from LatinoAnalysis.NanoGardener.data.LeptonMaker_cfg import List_newVar, Lep_var 
from LatinoAnalysis.NanoGardener.data.common_cfg import Type_dict
#from LatinoAnalysis.NanoGardener.data.Trigger_names import TrigNames, SPTrigNames

class LeptonMaker(Module): 
    '''
    put this file in LatinoAnalysis/NanoGardener/python/modules/
    Add extra variables to NANO tree
    '''
    def __init__(self):
        pass

    def beginJob(self): 
        pass

    def endJob(self):
        pass

    def beginFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        self.initReaders(inputTree) # initReaders must be called in beginFile
        self.out = wrappedOutputTree

        # New branches
        for typ in List_newVar:
           for var in List_newVar[typ]:
              if 'Lepton_' in var: self.out.branch(var, typ, lenVar='nLepton')
              #elif 'SPTrigger' in var: self.out.branch(var, typ, len(SPTrigNames))
              #elif 'Trigger' in var: self.out.branch(var, typ, len(TrigNames))
              #else: self.out.branch(var, typ)
        
        # Old branches to reorder
        self.list_old_br = {}
        self.list_old_br['Electron'] = []
        self.list_old_br['Muon'] = []
        self.list_old_br['Jet'] = []
        for br in inputTree.GetListOfBranches():
           bname = br.GetName()
           btype = Type_dict[br.GetListOfLeaves()[0].GetTypeName()] 
           if re.match('\AElectron_', bname):
              self.list_old_br['Electron'].append(bname) 
              self.out.branch(bname, btype, lenVar='nElectron')
           if re.match('\AMuon_', bname):
              self.list_old_br['Muon'].append(bname) 
              self.out.branch(bname, btype, lenVar='nMuon')
           if re.match('\AJet_', bname):
              self.list_old_br['Jet'].append(bname) 
              self.out.branch(bname, btype, lenVar='nJet')


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

        lep_dict = {}
        for lv in Lep_var:
           lep_dict[lv] = [0]*nLep
        lep_dict['instance'] = [0]*nLep

        ele_dict = {}
        for lv in self.list_old_br['Electron']:
           ele_dict[lv] = [0]*nEl
        
        muo_dict = {}
        for lv in self.list_old_br['Muon']:
           muo_dict[lv] = [0]*nMu
        
        jet_dict = {}
        for lv in self.list_old_br['Jet']:
           jet_dict[lv] = [0]*nJt
        
        #--- Electron Loops
        for iEle1 in range(nEl):
           pt_idx = 0
           pt1 = self.electron_var['Electron_pt'][iEle1]
           # Start comparing electrons
           for iEle2 in range(nEl):
              if iEle2 == iEle1: continue
              pt2 = self.electron_var['Electron_pt'][iEle2]
              if pt1 < pt2:
                 pt_idx += 1
           #if pt_idx != iEle1: print('Electrons reordered')
           # Now index is set, fill the vars  
           for var in ele_dict:
              if type(self.electron_var[var][iEle1]) is str:
                 ele_dict[var][pt_idx] = ord(self.electron_var[var][iEle1])
              else:
                 ele_dict[var][pt_idx] = self.electron_var[var][iEle1]        

        #--- Muon Loops
        for iMu1 in range(nMu):
           pt_idx = 0
           pt1 = self.muon_var['Muon_pt'][iMu1]
           # Start comparing muons
           for iMu2 in range(nMu):
              if iMu2 == iMu1: continue
              pt2 = self.muon_var['Muon_pt'][iMu2]
              if pt1 < pt2:
                 pt_idx += 1
           #if pt_idx != iMu1: print('Muons reordered')
           # Now index is set, fill the vars  
           for var in muo_dict:
              if type(self.muon_var[var][iMu1]) is str:
                 muo_dict[var][pt_idx] = ord(self.muon_var[var][iMu1])
              else:
                 muo_dict[var][pt_idx] = self.muon_var[var][iMu1]
        
        #--- Lepton Loops
        for iLep1 in range(nLep):
           pt_idx = 0
           if iLep1 < nEl:
              pt1 = ele_dict['Electron_pt'][iLep1]
              pdgId1 = ele_dict['Electron_pdgId'][iLep1]
           else:
              pt1 = muo_dict['Muon_pt'][iLep1 - nEl]
              pdgId1 = muo_dict['Muon_pdgId'][iLep1 - nEl]
           # Start comparing leptons
           for iLep2 in range(nLep):
              if iLep2 == iLep1: continue
              if iLep2 < nEl:
                 pt2 = ele_dict['Electron_pt'][iLep2]
              else:
                 pt2 = muo_dict['Muon_pt'][iLep2 - nEl]
              if pt1 < pt2:
                 pt_idx += 1
           # Now index is set, fill the vars  
           if abs(pdgId1) == 11:
              for var in lep_dict:
                 if not 'instance' in var:
                    lep_dict[var][pt_idx] = ele_dict['Electron_'+var][iLep1]
                 else:
                    lep_dict[var][pt_idx] = iLep1
           elif abs(pdgId1) == 13:
              for var in lep_dict:
                 if not 'instance' in var and not 'eCorr' in var:
                    lep_dict[var][pt_idx] = muo_dict['Muon_'+var][iLep1 - nEl]
                 elif 'eCorr' in var:
                    lep_dict[var][pt_idx] = 1.
                 else:
                    lep_dict[var][pt_idx] = iLep1 - nEl
        
        #--- Jet Loops
        for iJ1 in range(nJt):
           pt_idx = 0
           pt1 = self.jet_var['Jet_pt'][iJ1]
           # Start comparing jets
           for iJ2 in range(nJt):
              if iJ2 == iJ1: continue
              pt2 = self.jet_var['Jet_pt'][iJ2]
              if pt1 < pt2:
                 pt_idx += 1
           #if pt_idx != iJ1: print('Jets reordered')
           # Now index is set, fill the vars  
           for var in jet_dict:
              if type(self.jet_var[var][iJ1]) is str:
                 jet_dict[var][pt_idx] = ord(self.jet_var[var][iJ1])
              else:
                 jet_dict[var][pt_idx] = self.jet_var[var][iJ1]

        #--- Fill branches
        for var in lep_dict:
           self.out.fillBranch('Lepton_' + var, lep_dict[var])
        
        for var in ele_dict:
           self.out.fillBranch(var, ele_dict[var])
        for var in muo_dict:
           self.out.fillBranch(var, muo_dict[var])
        for var in jet_dict:
           self.out.fillBranch(var, jet_dict[var])

        return True


# define modules using the syntax 'name = lambda : constructor' to avoid having them loaded when not needed

lepMkr = lambda : LeptonMaker()
