#
#
#     | ___ /   |  / _)         
#     |   _ \   ' /   |  __ \   
#     |    ) |  . \   |  |   |  
#    _| ____/  _|\_\ _| _|  _|  
#                                                                                    
#
#




import ROOT
ROOT.PyConfig.IgnoreCommandLineOptions = True

from PhysicsTools.NanoAODTools.postprocessing.framework.datamodel import Collection 
from PhysicsTools.NanoAODTools.postprocessing.framework.eventloop import Module
from PhysicsTools.NanoAODTools.postprocessing.modules.common.collectionMerger import collectionMerger


import os.path



class l3KinProducer(Module):
    def __init__(self):

        # change this part into correct path structure... 
        cmssw_base = os.getenv('CMSSW_BASE')
        try:
            ROOT.gROOT.LoadMacro(cmssw_base+'/src/LatinoAnalysis/Gardener/python/variables/WWWVar.C+g')
        except RuntimeError:
            ROOT.gROOT.LoadMacro(cmssw_base+'/src/LatinoAnalysis/Gardener/python/variables/WWWVar.C++g')


      
    def beginJob(self):
        pass

    def endJob(self):
        pass

    def beginFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        self.out = wrappedOutputTree
        self.newbranches = [
           'mllmin3l',
           'zveto_3l',
           'pt1',
           'pt2',
           'pt3',
           'eta1',
           'eta2',
           'eta3',
           'phi1',
           'phi2',
           'phi3',
   #        'channel',
           'drllmin3l',
           'njet_3l',
           'nbjet_3l',
           'chlll',
           'pfmet',
           'mlll',
           'flagOSSF',
           'mtwww',
           'mtw1_wh3l',
           'mtw2_wh3l',
           'mtw3_wh3l',
           'minmtw_wh3l',
           'mindphi_lmet',
           'dphilllmet',
           'ptlll',
           'pTWWW',
           'dphilmet1_wh3l',
           'dphilmet2_wh3l',
           'dphilmet3_wh3l',
           'ptbest'
        ]
        
        for nameBranches in self.newbranches :
          self.out.branch(nameBranches  ,  "F");

    def endFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        pass

    def analyze(self, event):
        """process event, return True (go to next module) or False (fail, go to next event)"""

        muons = Collection(event, "Muon")
        electrons = Collection(event, "Electron")

        
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
        
        for lep in leptons :
          lep_pt. push_back(lep.pt)
          lep_eta.push_back(lep.eta)
          lep_phi.push_back(lep.phi)
          lep_ch.push_back(lep.charge)
          # 11 = ele 
          # 13 = mu
          if lep.tightId == 0 :
            lep_flavour.push_back(lep.charge *  11)
          else: 
            lep_flavour.push_back(lep.charge *  13)
          
          # is this really doing its job?
        
           
          
        Jet   = Collection(event, "Jet")
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
          jet_mass.push_back(jet.mass)
          jet_cmvav2.push_back(jet.btagCMVA)



        WWW = ROOT.WWW()

        WWW.setLeptons(lep_pt, lep_eta, lep_phi, lep_ch, lep_flavour)
        WWW.setJets(jet_pt, jet_eta, jet_phi, jet_mass, jet_cmvav2)
         
        MET_phi   = event.MET_phi
        MET_pt    = event.MET_pt
        
        WWW.setMET(MET_pt, MET_phi)

        WWW.setTkMET(event.TkMET_pt, event.TkMET_phi) 

        WWW.checkIfOk()

            
        for nameBranches in self.newbranches :
          self.out.fillBranch(nameBranches  ,  getattr(WWW, nameBranches)());


        return True







