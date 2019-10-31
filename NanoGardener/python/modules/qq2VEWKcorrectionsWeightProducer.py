#
#
#
#    \ \     /      ____| \ \        /  |  /       \  |  |       _ \  
#     \ \   /       __|    \ \  \   /   ' /         \ |  |      |   | 
#      \ \ /        |       \ \  \ /    . \       |\  |  |      |   | 
#       \_/        _____|    \_/\_/    _|\_\     _| \_| _____| \___/  
#                                                                               
#
#
#
#
# NLO Electroweak corrections for V samples
#
# Credits to Adish Vartak: https://github.com/cmg-xtracks/cmgtools-lite/blob/94X_dev/TTHAnalysis/macros/xtracks/addSumWgt.py
# 
# 


import ROOT
ROOT.PyConfig.IgnoreCommandLineOptions = True

from PhysicsTools.NanoAODTools.postprocessing.framework.datamodel import Collection 
from PhysicsTools.NanoAODTools.postprocessing.framework.eventloop import Module

import os.path


class vNLOEWKcorrectionWeightProducer(Module):
    def __init__(self, sample_type='z'):
        #
        # "sample_type" should be 'z' or 'w'
        #
        print ' ------> vNLOEWKcorrectionWeightProducer Init() ----'
        # change this part into correct path structure... 
        self.cmssw_base = os.getenv('CMSSW_BASE')

        self.kfactorFile = self.open_root (self.cmssw_base+'/src/LatinoAnalysis/Gardener/python/data/ewk/kfactors_V.root')
        
        #
        # TEST: ratio w.r.t. LO ?
        #
        zknum = self.get_root_obj ( self.kfactorFile , "EWKcorr/Z"      )
        zkden = self.get_root_obj ( self.kfactorFile , "ZJets_LO/inv_pt")
        wknum = self.get_root_obj ( self.kfactorFile , "EWKcorr/W"      )
        wkden = self.get_root_obj ( self.kfactorFile , "WJets_LO/inv_pt")
        
        self.zkfact = zknum.Clone("zkfact")
        self.wkfact = wknum.Clone("wkfact")
        self.zkfact.Divide(zkden)
        self.wkfact.Divide(wkden)
        
        #print " self.zkfact = ", self.zkfact
        #print " self.wkfact = ", self.wkfact
        
        self.sample_type = sample_type
        print " sample_type = " , sample_type


    def open_root(self, path):
        r_file = ROOT.TFile.Open(path)
        if not r_file.__nonzero__() or not r_file.IsOpen(): raise NameError('File ' + path + ' not open')
        return r_file


    def get_root_obj(self, root_file, obj_name):
        r_obj = root_file.Get(obj_name)
        if not r_obj.__nonzero__(): raise NameError('Root Object ' + obj_name + ' not found')
        return r_obj


    def beginJob(self):
        pass

    def endJob(self):
        pass

    def beginFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        self.out = wrappedOutputTree
        newbranches = ['ewknloW', 'ewknloWuncertainty']
        #
        # "ewknloWuncertainty" is the absolute uncertainty on "ewknloW"
        #
        for nameBranches in newbranches :
          self.out.branch(nameBranches  ,  "F");


    def endFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        pass


    def analyze(self, event):
        """process event, return True (go to next module) or False (fail, go to next event)"""

        #print " self.zkfact = ", self.zkfact
        #print " self.wkfact = ", self.wkfact

        ewknloW             = -1
        ewknloWuncertainty  = -1

        lheParticles = Collection(event, "LHEPart")
        
        isw = False
        isz = False

        if self.sample_type == 'w' :
          isw = True
        if self.sample_type == 'z' :
          isz = True
          

#
#      Since in nanoAOD no V are saved, since not in status 1, 
#      reconstruct Z and W from its decays.
#      Only leptonic decays are considered, but if needed it can be extended
#

#
#         \ \        / 
#          \ \  \   /  
#           \ \  \ /   
#            \_/\_/    
#
        
        if isw : 
          
          ptl1 = -1
          ptv1 = -1
 
          for particle  in lheParticles :
              
            # lepton = 11, 13, 15
            #          e   mu  tau
            
            if abs(particle.pdgId) == 11 or abs(particle.pdgId) == 13 or abs(particle.pdgId) == 15:
     
              if ptl1 == -1 :
                ptl1   = particle.pt
                etal1  = particle.eta
                phil1  = particle.phi
                idl1   = particle.pdgId

            # neutrinos
            #          12   14   16

            if abs(particle.pdgId) == 12 or abs(particle.pdgId) == 14 or abs(particle.pdgId) == 16:
     
              if ptv1 == -1 :
                ptv1   = particle.pt
                etav1  = particle.eta
                phiv1  = particle.phi
                idv1   = particle.pdgId

         
          #
          # if for any reason I was not able to assign the leptons, set the weight to -2 --> it can be followed up later
          #
          if ptl1 == -1 or ptv1 == -1 :
            ewknloW = -2
          else :  
            l1 = ROOT.TLorentzVector()
            l2 = ROOT.TLorentzVector()
            l1.SetPtEtaPhiM(ptl1, etal1, phil1, 0) # everything massless ... at these energies! ... maybe the tau?
            l2.SetPtEtaPhiM(ptv1, etav1, phiv1, 0)
            
            vpt = (l1+l2).Pt()
            
            ewknloW = 1.0

            if vpt > 0. and vpt < 150.1 :
              vpt = 150.1
            if vpt > 1199.9 :
              vpt = 1199.9
    
            if vpt > 0. :
              bin = self.wkfact.FindBin(vpt)
              ewknloW = self.wkfact.GetBinContent(bin);
              
              
#  
#           __  / 
#              /  
#             /   
#           ____| 
# 
 
        if isz : 
          

          ptl1 = -1
          ptl2 = -1
 
          for particle  in lheParticles :
              
            # lepton = 11, 13, 15
            #          e   mu  tau
            
            if abs(particle.pdgId) == 11 or abs(particle.pdgId) == 13 or abs(particle.pdgId) == 15:
     
              if ptl1 == -1 :
                ptl1   = particle.pt
                etal1  = particle.eta
                phil1  = particle.phi
                idl1   = particle.pdgId
              elif ptl2 == -1 :
                ptl2   = particle.pt
                etal2  = particle.eta
                phil2  = particle.phi
                idl2   = particle.pdgId

          #
          # if for any reason I was not able to assign the leptons, set the weight to -2 --> it can be followed up later
          #
          if ptl1 == -1 or ptl2 == -1 :
            ewknloW = -2
          else :  
            l1 = ROOT.TLorentzVector()
            l2 = ROOT.TLorentzVector()
            l1.SetPtEtaPhiM(ptl1, etal1, phil1, 0) # everything massless ... at these energies! ... maybe the tau?
            l2.SetPtEtaPhiM(ptl2, etal2, phil2, 0) # everything massless ... at these energies! ... maybe the tau?
            
            vpt = (l1+l2).Pt()
            
            ewknloW = 1.0

            if vpt > 0. and vpt < 150.1 :
              vpt = 150.1
            if vpt > 1199.9 :
              vpt = 1199.9
    
            if vpt > 0. :
              bin = self.zkfact.FindBin(vpt)
              ewknloW = self.zkfact.GetBinContent(bin);
          


 
        # now finally fill the branch ...
 
        self.out.fillBranch("ewknloW",               ewknloW)
        self.out.fillBranch("ewknloWuncertainty",    ewknloWuncertainty)

        return True



