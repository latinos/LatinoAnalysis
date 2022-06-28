# From LeptonSFMaker.py
import ROOT
import os
import re
import math
import time
import copy
ROOT.PyConfig.IgnoreCommandLineOptions = True

from PhysicsTools.NanoAODTools.postprocessing.framework.eventloop import Module
from LatinoAnalysis.NanoGardener.data.LeptonSel_cfg import LepFilter_dict 
from LatinoAnalysis.NanoGardener.data.LeptonMaker_cfg import Lepton_br, Lepton_var 
from LatinoAnalysis.NanoGardener.data.LeptonMaker_cfg import VetoLepton_br, VetoLepton_var 
from LatinoAnalysis.NanoGardener.data.LeptonMaker_cfg import CleanJet_br, CleanJet_var 
from LatinoAnalysis.NanoGardener.data.common_cfg import Type_dict

from PhysicsTools.NanoAODTools.postprocessing.framework.datamodel import Collection
from LatinoAnalysis.NanoGardener.framework.BranchMapping import mappedOutputTree, mappedEvent


# Additional from TMVA filler
import array
from collections import OrderedDict


class LeptonMVAFiller(Module):
    '''
    Produce branches with lepton MVA variables
    '''

    def __init__(self,  mvaCfgFile, branch_map=''):
        ''' Initialize the module with mva configuration file and branch map'''
        
        cmssw_base = os.getenv('CMSSW_BASE')
        mvaFile = cmssw_base+'/src/LatinoAnalysis/NanoGardener/python/'+mvaCfgFile
        self._branch_map = branch_map
        
        # Try to open mvaCfgFile
        if os.path.exists(mvaFile):
            handle = open(mvaFile,'r')
            exec(handle)
            self.mvaDic = mvaDic
            handle.close()
        # print self.mvaDic
        self.mvaDic = mvaDic
        self._branch_map = branch_map

        # Load all MVA xml files (in principle, one for electrons and one for muons)
        # and the corresponding variables
        for iMva in self.mvaDic :
            self.mvaDic[iMva]['reader'] = ROOT.TMVA.Reader("V")
            self.mvaDic[iMva]['spectators'] = []
            self.mvaDic[iMva]['inputs'] = []
            # Load spectator variables
            jVar=0
            for iVar in self.mvaDic[iMva]['spectatorVars'] :
                iVar_copy = iVar # iVar copy is needed since in the training, I used twice Muon_looseID :(
                if 'Bis' in iVar: iVar_copy = iVar.replace('Bis','')
                self.mvaDic[iMva]['spectators'].append(array.array('f',[0]))
                self.mvaDic[iMva]['reader'].AddSpectator(iVar_copy,self.mvaDic[iMva]['spectators'][jVar])
                jVar+=1
            # Load input variables
            jVar=0
            for iVar in self.mvaDic[iMva]['inputVars'] :
                self.mvaDic[iMva]['inputs'].append(array.array('f',[0]))
                self.mvaDic[iMva]['reader'].AddVariable(iVar,self.mvaDic[iMva]['inputs'][jVar])
                jVar+=1
            self.mvaDic[iMva]['reader'].BookMVA(self.mvaDic[iMva]['type'],cmssw_base+'/src/'+self.mvaDic[iMva]['xmlFile'])  


    def beginJob(self):
        pass


    def endJob(self):
        pass


    def beginFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        '''Define input and output trees, and new branches'''

        self.initReaders(inputTree) # initReaders must be called in beginFile
        self.out = mappedOutputTree(wrappedOutputTree, mapname=self._branch_map)

        # New Branch
        self.out.branch('Lepton_mvaTTH_UL', 'F', lenVar='nLepton')


    def endFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        pass


    def initReaders(self,tree):
        '''Define the branches you want to read from input file '''

        # Array reader
        self.electron_var = {}
        self.muon_var     = {}
        self.lepton_var   = {}
        self.jet_var      = {}

        for br in tree.GetListOfBranches():
           bname = br.GetName()
           if re.match('\AElectron_', bname): self.electron_var[bname] = tree.arrayReader(bname)
           if re.match('\AMuon_',     bname): self.muon_var[bname]     = tree.arrayReader(bname)
           if re.match('\ALepton_',   bname): self.lepton_var[bname]   = tree.arrayReader(bname)
           if re.match('\AJet_',      bname): self.jet_var[bname]      = tree.arrayReader(bname)

        # Float/int/double reader
        self.nElectron = tree.valueReader('nElectron')
        self.nMuon     = tree.valueReader('nMuon')
        self.nLepton   = tree.valueReader('nLepton')
        self.nJet      = tree.valueReader('nJet')

        self._ttreereaderversion = tree._ttreereaderversion


    def analyze(self, event):
        '''Process the event and compute the MVA discriminant for each lepton'''

        event = mappedEvent(event, mapname=self._branch_map)

        # Count number of leptons
        nLep = int(event.nLepton)

        # Preparing output
        output_MVA = []
                
        # Loop over leptons
        for iLep in range(0, nLep):

            # Initialize MVA value
            val = 0
            
            # Check lepton flavor
            if abs(event.Lepton_pdgId[iLep]) == 11:
                # ID to locate the Lepton_ object in the Electron_ collection
                eleID = event.Lepton_electronIdx[iLep]
                
                for iMva in self.mvaDic:
                    if "Muon" in iMva: continue
                    # Spectators variables
                    jVar = 0
                    for iVar in self.mvaDic[iMva]['spectatorVars']:
                        iVar_copy = iVar # iVar copy is needed since in the training I used twice Muon_looseID :(
                        if 'Bis' in iVar: iVar_copy = iVar.replace('Bis','')
                        value = 0
                        if any(i in iVar for i in self.mvaDic[iMva]['charVariables']): # special 'ord' treatment for uchar variables
                            var   = self.mvaDic[iMva]['spectatorVars'][iVar]
                            value = ord(eval(var))
                        else: # standard treatment
                            var   = self.mvaDic[iMva]['spectatorVars'][iVar]
                            value = eval(var)
                        self.mvaDic[iMva]['spectators'][jVar][0] = value
                        jVar += 1

                    # Input variables
                    jVar=0
                    for iVar in self.mvaDic[iMva]['inputVars']:
                        iVar_copy = iVar # iVar copy is needed since in the training, I used twice Muon_looseID :(
                        if 'Bis' in iVar: iVar_copy = iVar.replace('Bis','')
                        value = 0
                        if any(i in iVar for i in self.mvaDic[iMva]['charVariables']): # special 'ord' treatment for uchar variables
                            var   = self.mvaDic[iMva]['inputVars'][iVar]
                            value = ord(eval(var))
                        else: # standard treatment
                            var   = self.mvaDic[iMva]['inputVars'][iVar]
                            value = eval(var)
                        self.mvaDic[iMva]['inputs'][jVar][0] = value
                        jVar += 1
                
                    val = self.mvaDic[iMva]['reader'].EvaluateMVA(self.mvaDic[iMva]['type'])
                    output_MVA.append(val)


            elif abs(event.Lepton_pdgId[iLep]) == 13:
                # ID to locate the Lepton_ object in the Muon_ collection
                muonID = event.Lepton_muonIdx[iLep]

                for iMva in self.mvaDic:
                    if "Electron" in iMva: continue
                    # Spectators variables
                    jVar=0
                    for iVar in self.mvaDic[iMva]['spectatorVars']:
                        iVar_copy = iVar # iVar copy is needed since in the training, I used twice Muon_looseID :(
                        if 'Bis' in iVar: iVar_copy = iVar.replace('Bis','')
                        value = 0
                        if any(i in iVar for i in self.mvaDic[iMva]['charVariables']): # special 'ord' treatment for uchar variables
                            var   = self.mvaDic[iMva]['spectatorVars'][iVar]
                            value = ord(eval(var))
                        else: # standard treatment
                            var   = self.mvaDic[iMva]['spectatorVars'][iVar]
                            value = eval(var)
                        self.mvaDic[iMva]['spectators'][jVar][0] = value
                        jVar += 1

                    # Input variables
                    jVar=0
                    for iVar in self.mvaDic[iMva]['inputVars']:
                        iVar_copy = iVar # iVar copy is needed since in the training, I used twice Muon_looseID :(
                        if 'Bis' in iVar: iVar_copy = iVar.replace('Bis','')
                        value = 0
                        if any(i in iVar for i in self.mvaDic[iMva]['charVariables']): # special 'ord' treatment for uchar variables
                            var   = self.mvaDic[iMva]['inputVars'][iVar]
                            value = ord(eval(var))
                        else: # standard treatment
                            var   = self.mvaDic[iMva]['inputVars'][iVar]
                            value = eval(var)
                        self.mvaDic[iMva]['inputs'][jVar][0] = value
                        jVar += 1

                    val = self.mvaDic[iMva]['reader'].EvaluateMVA(self.mvaDic[iMva]['type'])
                    output_MVA.append(val)

            else:
                print("This is not a lepton I can consider")

        # Fill branch
        self.out.fillBranch('Lepton_mvaTTH_UL', output_MVA)

        return True


# define modules using the syntax 'name = lambda : constructor' to avoid having them loaded when not needed
lepMVAFiller = lambda : LeptonMVAFiller()
