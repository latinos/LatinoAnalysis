#
#
#     |  |  |    |  / _)          
#     |  |  |    ' /   |  __ \    
#     | ___ __|  . \   |  |   |   
#    _|    _|   _|\_\ _| _|  _|   
#                                                                                     
#
#



import ROOT
ROOT.PyConfig.IgnoreCommandLineOptions = True

from PhysicsTools.NanoAODTools.postprocessing.framework.datamodel import Collection 
from PhysicsTools.NanoAODTools.postprocessing.framework.eventloop import Module
from PhysicsTools.NanoAODTools.postprocessing.modules.common.collectionMerger import collectionMerger


import os.path



class l4KinProducer(Module):
    def __init__(self):

        # change this part into correct path structure... 
        cmssw_base = os.getenv('CMSSW_BASE')
        try:
            ROOT.gROOT.LoadMacro(cmssw_base+'/src/LatinoAnalysis/Gardener/python/variables/ZWWVar.C+g')
        except RuntimeError:
            ROOT.gROOT.LoadMacro(cmssw_base+'/src/LatinoAnalysis/Gardener/python/variables/ZWWVar.C++g')


      
    def beginJob(self):
        pass

    def endJob(self):
        pass

    def beginFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        self.out = wrappedOutputTree
        self.newbranches = [
            'pfmetPhi_zh4l',
            'z0Mass_zh4l',
            'z0Pt_zh4l',
            'z1Mass_zh4l',
            'z1Pt_zh4l',
            'zaMass_zh4l',
            'zbMass_zh4l',
            'flagZ1SF_zh4l',
            'z0DeltaPhi_zh4l',
            'z1DeltaPhi_zh4l',
            'zaDeltaPhi_zh4l',
            'zbDeltaPhi_zh4l',
            'minDeltaPhi_zh4l',
            'z0DeltaR_zh4l',
            'z1DeltaR_zh4l',
            'zaDeltaR_zh4l',
            'zbDeltaR_zh4l',
            'lep1Mt_zh4l',
            'lep2Mt_zh4l',
            'lep3Mt_zh4l',
            'lep4Mt_zh4l',
            'minMt_zh4l',
            'z1Mt_zh4l',
            'mllll_zh4l',
            'chllll_zh4l',
            'z1dPhi_lep1MET_zh4l',
            'z1dPhi_lep2MET_zh4l',
            'z1mindPhi_lepMET_zh4l',
          ]
        
        for nameBranches in self.newbranches :
          self.out.branch(nameBranches  ,  "F");

    def endFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        pass

    def analyze(self, event):
        """process event, return True (go to next module) or False (fail, go to next event)"""

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
        lep_ch      = ROOT.std.vector(float)(0)
        lep_isLooseLepton = ROOT.std.vector(float)(0)
        
        for lep in leptons :
          lep_pt. push_back(lep.pt)
          lep_eta.push_back(lep.eta)
          lep_phi.push_back(lep.phi)
          lep_ch.push_back(-lep.pdgId/abs(lep.pdgId))
          lep_isLooseLepton.push_back(1) # FIXME
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

        jet_pt     = ROOT.std.vector(float)(0)
        jet_eta    = ROOT.std.vector(float)(0)
        jet_phi    = ROOT.std.vector(float)(0)
        jet_mass   = ROOT.std.vector(float)(0)
        jet_cmvav2 = ROOT.std.vector(float)(0)

        for jet in Jet :
          jet_pt. push_back(jet.pt)
          jet_eta.push_back(jet.eta)
          jet_phi.push_back(jet.phi)
          jet_mass.push_back(OrigJet[jet.jetIdx].mass)
          jet_cmvav2.push_back(OrigJet[jet.jetIdx].btagCMVA)


        ZWW = ROOT.ZWW()

        ZWW.setLepton(lep_pt, lep_eta, lep_phi, lep_flavour, lep_ch, lep_isLooseLepton)
        ZWW.setJet(jet_pt, jet_eta, jet_phi, jet_mass, jet_cmvav2)
         
        MET_phi   = event.PuppiMET_phi
        MET_pt    = event.PuppiMET_pt
        
        ZWW.setMET(MET_pt, MET_phi)

        ZWW.isAllOk()

            
        for nameBranches in self.newbranches :
          self.out.fillBranch(nameBranches  ,  getattr(ZWW, nameBranches)());


        return True






