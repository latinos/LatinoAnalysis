import ROOT
import os
ROOT.PyConfig.IgnoreCommandLineOptions = True

from PhysicsTools.NanoAODTools.postprocessing.framework.eventloop import Module
from LatinoAnalysis.NanoGardener.data.LeptonMaker_cfg import List_newVar, Lep_var 
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
        for typ in List_newVar:
           for var in List_newVar[typ]:
              if 'Lepton_' in var: self.out.branch(var, typ, lenVar='nLepton')
              elif 'SPTrigger' in var: self.out.branch(var, typ, len(SPTrigNames))
              elif 'Trigger' in var: self.out.branch(var, typ, len(TrigNames))
              else: self.out.branch(var, typ)

    def endFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        pass

    def initReaders(self,tree): # this function gets the pointers to Value and ArrayReaders and sets them in the C++ worker class
        self.electron_var = {}
        self.muon_var = {}
        for lv in Lep_var:
           self.electron_var['Electron_'+lv] = tree.arrayReader('Electron_'+lv)
           if lv == 'eCorr': continue
           self.muon_var['Muon_'+lv] = tree.arrayReader('Muon_'+lv)

        #self.is_trigger = []
        #self.is_SPtrigger = []
        #b = tree.GetListOfBranches()

        #for name in TrigNames:
        #   if b.FindObject(name): self.is_trigger.append(True)
        #   else: self.is_trigger.append(False)

        #for name in SPTrigNames:
        #   if b.FindObject(name): self.is_SPtrigger.append(True)
        #   else: self.is_SPtrigger.append(False)

        #self.trigger = {}
        #self.SPtrigger = {}
        #for i in range(len(TrigNames)):
        #   if self.is_trigger[i]: self.trigger[TrigNames[i]] = tree.valueReader(TrigNames[i])
        #for i in range(len(SPTrigNames)):
        #   if self.is_SPtrigger[i]: self.SPtrigger[SPTrigNames[i]] = tree.valueReader(SPTrigNames[i])

        self.nElectron = tree.valueReader('nElectron')
        self.nMuon = tree.valueReader('nMuon')
        self._ttreereaderversion = tree._ttreereaderversion # self._ttreereaderversion must be set AFTER all calls to tree.valueReader or tree.arrayReader

    def analyze(self, event):
        """process event, return True (go to next module) or False (fail, go to next event)"""

        if event._tree._ttreereaderversion > self._ttreereaderversion: # do this check at every event, as other modules might have read further branches
            self.initReaders(event._tree)
        # do NOT access other branches in python between the check/call to initReaders and the call to C++ worker code
        
        # Set vars
        nEl = int(self.nElectron)
        nMu = int(self.nMuon)
        nLep = nMu + nEl

        temp_dict = {}
        for lv in Lep_var:
           temp_dict[lv] = [0]*nLep
        temp_dict['instance'] = [0]*nLep

        #--- Start looping leptons
        for iLep1 in range(nLep):
           pt_idx = 0
           if iLep1 < nEl:
              pt1 = self.electron_var['Electron_pt'][iLep1]
              pdgId1 = self.electron_var['Electron_pdgId'][iLep1]
           else:
              pt1 = self.muon_var['Muon_pt'][iLep1 - nEl]
              pdgId1 = self.muon_var['Muon_pdgId'][iLep1 - nEl]
           
           # Start comparing lepton to other leptons
           for iLep2 in range(nLep):
              if iLep2 == iLep1:
                 continue
              if iLep2 < nEl:
                 pt2 = self.electron_var['Electron_pt'][iLep2]
              else:
                 pt2 = self.muon_var['Muon_pt'][iLep2 - nEl]
              if pt1 < pt2:
                 pt_idx += 1

           # Now index is set, fill the vars  
           if abs(pdgId1) == 11:
              for var in temp_dict:
                 if not 'instance' in var:
                    temp_dict[var][pt_idx] = self.electron_var['Electron_'+var][iLep1]
                 else:
                    temp_dict[var][pt_idx] = iLep1
           elif abs(pdgId1) == 13:
              for var in temp_dict:
                 if not 'instance' in var and not 'eCorr' in var:
                    temp_dict[var][pt_idx] = self.muon_var['Muon_'+var][iLep1 - nEl]
                 elif 'eCorr' in var:
                    temp_dict[var][pt_idx] = 1.
                 else:
                    temp_dict[var][pt_idx] = iLep1 - nEl
        #--- Lepton loop complete

        # Fill branches
        for var in temp_dict:
           self.out.fillBranch('Lepton_' + var, temp_dict[var])
        
        #Trig = []
        #SPTrig = []
        #for i in range(len(TrigNames)):
        #   if self.is_trigger[i]: Trig.append(int(self.trigger[TrigNames[i]]))
        #   else: Trig.append(-1)       
        #for i in range(len(SPTrigNames)):
        #   if self.is_SPtrigger[i]: SPTrig.append(int(self.SPtrigger[SPTrigNames[i]]))
        #   else: SPTrig.append(-1)       
 
        #self.out.fillBranch('nLepton', nLep)
        #self.out.fillBranch('Trigger_bits', Trig)
        #self.out.fillBranch('SPTrigger_bits', SPTrig)

        return True


# define modules using the syntax 'name = lambda : constructor' to avoid having them loaded when not needed

lepMkr = lambda : LeptonMaker()
