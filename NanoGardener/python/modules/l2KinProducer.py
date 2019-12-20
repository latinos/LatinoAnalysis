#
#
#     | ___ \   |  / _)        
#     |    ) |  ' /   |  __ \  
#     |   __/   . \   |  |   | 
#    _| _____| _|\_\ _| _|  _| 
#                                                         
#
#



import ROOT
ROOT.PyConfig.IgnoreCommandLineOptions = True

from PhysicsTools.NanoAODTools.postprocessing.framework.datamodel import Collection 
from PhysicsTools.NanoAODTools.postprocessing.framework.eventloop import Module
from PhysicsTools.NanoAODTools.postprocessing.modules.common.collectionMerger import collectionMerger
from LatinoAnalysis.NanoGardener.framework.BranchMapping import mappedOutputTree, mappedEvent

import os.path


class l2KinProducer(Module):
    def __init__(self, branch_map=''):

        # change this part into correct path structure... 
        cmssw_base = os.getenv('CMSSW_BASE')
        try:
            ROOT.gROOT.LoadMacro(cmssw_base+'/src/LatinoAnalysis/Gardener/python/variables/WWVar.C+g')
        except RuntimeError:
            ROOT.gROOT.LoadMacro(cmssw_base+'/src/LatinoAnalysis/Gardener/python/variables/WWVar.C++g')

        self._branch_map = branch_map
                
    def beginJob(self):
        pass

    def endJob(self):
        pass

    def beginFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        self.out = mappedOutputTree(wrappedOutputTree, mapname=self._branch_map)
        self.newbranches = [
           'mll',
           'dphill',
           'yll',
           'ptll',
           'pt1',
           'pt2',
           'mth',
           'mcoll',
           'mcollWW',
           'mTi',
           'mTe',
           'choiMass',
           'mR',
           'mT2',
           'channel',


           'drll',
           'dphilljet',
           'dphilljetjet',
           'dphilljetjet_cut',
           'dphillmet',
           'dphilmet',
           'dphilmet1',
           'dphilmet2',
           'mtw1',
           'mtw2',
           
           'mjj',
           'detajj',
           'njet',
          
           'mllWgSt',
           'drllWgSt',
           'mllThird',
           'mllOneThree',
           'mllTwoThree',
           'drllOneThree',
           'drllTwoThree',
           
           'dphijet1met',  
           'dphijet2met',  
           'dphijjmet',    
           'dphijjmet_cut',    
           'dphilep1jet1', 
           'dphilep1jet2', 
           'dphilep2jet1', 
           'dphilep2jet2',
           'mindetajl',
           'detall',
           'dphijj',
           'maxdphilepjj',
           'dphilep1jj',
           'dphilep2jj',
          
           'ht',
           'vht_pt',
           'vht_phi',
           
           'projpfmet',
           'dphiltkmet',
           'projtkmet',
           'mpmet',
           
           'pTWW',
           'pTHjj',

           'recoil',
           'jetpt1_cut',
           'jetpt2_cut',
           'dphilljet_cut',
           'dphijet1met_cut',
           'dphijet2met_cut',
           'PfMetDivSumMet',
           'upara',
           'uperp',
           'm2ljj20',
           'm2ljj30',
# for VBF training
           'ptTOT_cut',
           'mTOT_cut',
           'OLV1_cut',
           'OLV2_cut',
           'Ceta_cut',
#whss
           'mlljj20_whss',
           'mlljj30_whss',
           'WlepPt_whss',
           'WlepMt_whss'
          ]
        
        for nameBranches in self.newbranches :
          self.out.branch(nameBranches  ,  "F");

    def endFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        pass

    def analyze(self, event):
        """process event, return True (go to next module) or False (fail, go to next event)"""

        event = mappedEvent(event, mapname=self._branch_map)

        #muons = Collection(event, "Muon")
        #electrons = Collection(event, "Electron")
        
        # order in pt the collection merging muons and electrons
        # lepMerger must be already called
        leptons = Collection(event, "Lepton")

        #leptons = electrons
        nLep = len(leptons)
        
        
        lep_pt      = ROOT.std.vector(float)(0)
        lep_eta     = ROOT.std.vector(float)(0)
        lep_phi     = ROOT.std.vector(float)(0)
        lep_flavour = ROOT.std.vector(float)(0)
        
        for lep in leptons :
          lep_pt. push_back(lep.pt)
          lep_eta.push_back(lep.eta)
          lep_phi.push_back(lep.phi)
          lep_flavour.push_back(lep.pdgId)
          # 11 = ele 
          # 13 = mu
          #if lep.tightId == 0 :
          #  lep_flavour.push_back(lep.charge *  11)
          #else: 
          #  lep_flavour.push_back(lep.charge *  13)
          
          # is this really doing its job?
        
           
          
        Jet   = Collection(event, "CleanJet")
        #auxiliary jet collection to access the mass
        OrigJet   = Collection(event, "Jet")
        nJet = len(Jet)

        jet_pt    = ROOT.std.vector(float)(0)
        jet_eta   = ROOT.std.vector(float)(0)
        jet_phi   = ROOT.std.vector(float)(0)
        jet_mass  = ROOT.std.vector(float)(0)

        for jet in Jet :
          jet_pt. push_back(jet.pt)
          jet_eta.push_back(jet.eta)
          jet_phi.push_back(jet.phi)
          jet_mass.push_back(OrigJet[jet.jetIdx].mass)


        WW = ROOT.WW()
        
        WW.setLeptons(lep_pt, lep_eta, lep_phi, lep_flavour)
        WW.setJets   (jet_pt, jet_eta, jet_phi, jet_mass)
       

        #MET_sumEt = event.MET_sumEt
        #MET_phi   = event.MET_phi
        #MET_pt    = event.MET_pt
        MET_sumEt = event.PuppiMET_sumEt
        MET_phi   = event.PuppiMET_phi
        MET_pt    = event.PuppiMET_pt
        
        WW.setMET(MET_pt, MET_phi)
        WW.setSumET(MET_sumEt)
       
        WW.setTkMET(event.TkMET_pt, event.TkMET_phi) 
        
        
        WW.checkIfOk()
            
            
        for nameBranches in self.newbranches :
          self.out.fillBranch(nameBranches  ,  getattr(WW, nameBranches)())

        return True






