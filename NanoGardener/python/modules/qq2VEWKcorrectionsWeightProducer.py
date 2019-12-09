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
# Thanks to Raffaele Gerosa and DM team
#
# Inputs from: https://arxiv.org/pdf/1705.04664v2.pdf
# Table: http://lpcc.web.cern.ch/content/dark-matter-wg-documents
# From the pdf which table to be used is described
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

        self.graph_zvv_kfact = ROOT.TGraph(self.cmssw_base+'/src/LatinoAnalysis/Gardener/python/data/ewk/kewk_zvv_for_python.txt');
        self.graph_z_kfact   = ROOT.TGraph(self.cmssw_base+'/src/LatinoAnalysis/Gardener/python/data/ewk/kewk_z_for_python.txt');
        self.graph_w_kfact   = ROOT.TGraph(self.cmssw_base+'/src/LatinoAnalysis/Gardener/python/data/ewk/kewk_w_for_python.txt');
        
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

        ewknloW             = -1
        ewknloWuncertainty  = -1

        lheParticles = Collection(event, "LHEPart")
        
        isw   = False
        isz   = False
        iszvv = False

        if self.sample_type == 'w' :
          isw = True
        if self.sample_type == 'z' :
          isz = True
        if self.sample_type == 'zvv' :
          iszvv = True
          

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

            if vpt > 0. and vpt < 35. :
              vpt = 35.
            if vpt > 2000. :
              vpt = 2000.
    
            if vpt > 0. :
              ewknloW = self.graph_z_kfact.Eval(vpt)
               
              
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

            if vpt > 0. and vpt < 35. :
              vpt = 35.
            if vpt > 2000. :
              vpt = 2000.
    
            if vpt > 0. :
              ewknloW = self.graph_z_kfact.Eval(vpt)
              
          

#
#          __  /                
#             / \ \   / \ \   / 
#            /   \ \ /   \ \ /  
#          ____|  \_/     \_/   
#                               

 
        if iszvv : 
          

          ptl1 = -1
          ptl2 = -1
 
          for particle  in lheParticles :

            # neutrinos
            #          12   14   16

            if abs(particle.pdgId) == 12 or abs(particle.pdgId) == 14 or abs(particle.pdgId) == 16:

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

            if vpt > 0. and vpt < 35. :
              vpt = 35.
            if vpt > 2000. :
              vpt = 2000.
    
            if vpt > 0. :
              ewknloW = self.graph_zvv_kfact.Eval(vpt)
              
          

 
        # now finally fill the branch ...
 
        self.out.fillBranch("ewknloW",               ewknloW)
        self.out.fillBranch("ewknloWuncertainty",    ewknloWuncertainty)

        return True



