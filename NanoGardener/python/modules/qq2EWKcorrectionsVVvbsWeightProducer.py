#
#
#
#     ____| \ \        /  |  /       \  |  |       _ \        _|                  \ \     /  __ )   ___|      \ \     / \ \     / 
#     __|    \ \  \   /   ' /         \ |  |      |   |      |     _ \    __|      \ \   /   __ \ \___ \       \ \   /   \ \   /  
#     |       \ \  \ /    . \       |\  |  |      |   |      __|  (   |  |          \ \ /    |   |      |       \ \ /     \ \ /   
#    _____|    \_/\_/    _|\_\     _| \_| _____| \___/      _|   \___/  _|           \_/    ____/ _____/         \_/       \_/    
#                                                                                                                                                    
#
#
#
#
# Inputs: 
#   - WZ VBS: Matthieu Pellen (-> Guillelmo Gomez Ceballos):  https://inspirehep.net/literature/1727600
#
#


import ROOT
ROOT.PyConfig.IgnoreCommandLineOptions = True

from PhysicsTools.NanoAODTools.postprocessing.framework.datamodel import Collection 
from PhysicsTools.NanoAODTools.postprocessing.framework.eventloop import Module

import os.path


class vvVBSNLOEWKcorrectionWeightProducer(Module):
    def __init__(self, sample_type='z'):
        #
        # "sample_type" should be 'z' or 'w'
        #
        print ' ------> vvVBSNLOEWKcorrectionWeightProducer Init() ----'
        # change this part into correct path structure... 
        self.cmssw_base = os.getenv('CMSSW_BASE')

        self.graph_WZvbs_kfact   = ROOT.TGraph(self.cmssw_base+'/src/LatinoAnalysis/Gardener/python/data/ewk/VBSWZ_EWK_NLO_LO_CMS_mjj_forPython.txt');     
        self.graph_ssWWvbs_kfact = ROOT.TGraph(self.cmssw_base+'/src/LatinoAnalysis/Gardener/python/data/ewk/VBSssWW_QCDEWK_NLO_LO_CMS_mjj_forPython.txt');     
        self.graph_osWWvbs_kfact = ROOT.TGraph(self.cmssw_base+'/src/LatinoAnalysis/Gardener/python/data/ewk/VBSosWW_EWK_NLO_LO_CMS_mjj_forPython.txt');     
        
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
        
        isVBSWZ   = False
        isVBSssWW = False
        isVBSosWW = False
        
        if self.sample_type == 'vbswz' :
          isVBSWZ = True
        if self.sample_type == 'vbsssww' :
          isVBSssWW = True
        if self.sample_type == 'vbsosww' :
          isVBSosWW = True
          


#
#         \ \     /  __ )   ___|      \ \        / __  / 
#          \ \   /   __ \ \___ \       \ \  \   /     /  
#           \ \ /    |   |      |       \ \  \ /     /   
#            \_/    ____/ _____/         \_/\_/    ____| 
#                                                        
  
  
        if isVBSWZ : 
          
          #
          # NB: it assumes W>lvll
          #     At LHE level only quarks are from VBS scattering
          #
          
          # look for the two quarks to make mjj 
          ptq1 = -1
          ptq2 = -1
 
          for particle  in lheParticles :
              
            # quarks = 1, 2, 3, 4, 5, 6
            #
            # LHEPart_status    Int_t   LHE particle status; -1:incoming, 1:outgoing
            #
            if (abs(particle.pdgId) >= 1 and abs(particle.pdgId) <= 6) and (particle.status==1) :
     
              if ptq1 == -1 :
                ptq1   = particle.pt
                etaq1  = particle.eta
                phiq1  = particle.phi
                idq1   = particle.pdgId
              elif ptq2 == -1 :
                ptq2   = particle.pt
                etaq2  = particle.eta
                phiq2  = particle.phi
                idq2   = particle.pdgId
              else :
                print "another quark?? A third quark?? pt = ", particle.pt,  "  ptq1 = ", ptq1, "  ptq2 = ", ptq2, "  idq1 = ", idq1, "  idq2 = ", idq1
                

          #
          # if for any reason I was not able to assign the quarks, set the weight to -2 --> it can be followed up later
          #
          if ptq1 == -1 or ptq2 == -1 :
            ewknloW = -2
          else :  
            q1 = ROOT.TLorentzVector()
            q2 = ROOT.TLorentzVector()
            q1.SetPtEtaPhiM(ptq1, etaq1, phiq1, 0) # everything massless ... at these energies! ... maybe the b? ... but no, at reco all is massless
            q2.SetPtEtaPhiM(ptq2, etaq2, phiq2, 0)
            
            mjj = (q1+q2).Mag()
            
            ewknloW = 1.0

            if mjj > 2900. :
              mjj = 2940.
            if mjj < 540. :
              mjj = 540.
    
            if mjj > 540. :
              ewknloW = self.graph_WZvbs_kfact.Eval(mjj)
              ewknloWuncertainty = 0.01   # it's ~1% flat, from the plots
      
      
      

#     
#      \ \     /  __ )   ___|                                              _)                   \ \        / \ \        / 
#       \ \   /   __ \ \___ \        __|   _` |  __ `__ \    _ \       __|  |   _` |  __ \       \ \  \   /   \ \  \   /  
#        \ \ /    |   |      |     \__ \  (   |  |   |   |   __/     \__ \  |  (   |  |   |       \ \  \ /     \ \  \ /   
#         \_/    ____/ _____/      ____/ \__,_| _|  _|  _| \___|     ____/ _| \__, | _|  _|        \_/\_/       \_/\_/    
#                                                                             |___/                                       

        if isVBSssWW : 
          
          #
          # NB: it assumes W>lvll
          #     At LHE level only quarks are from VBS scattering
          #
          # What to do for W>qq ?
          # Will these corrections still hold?
          #    --> FIXME: it needs to be checked, since q charge is different than l/v charge, IF in the calculation W decay was considered
          #
          
          # look for the two quarks to make mjj 
          ptq1 = -1
          ptq2 = -1
 
          for particle  in lheParticles :
              
            # quarks = 1, 2, 3, 4, 5, 6
            #
            # LHEPart_status    Int_t   LHE particle status; -1:incoming, 1:outgoing
            #
            if (abs(particle.pdgId) >= 1 and abs(particle.pdgId) <= 6) and (particle.status==1) :
     
              if ptq1 == -1 :
                ptq1   = particle.pt
                etaq1  = particle.eta
                phiq1  = particle.phi
                idq1   = particle.pdgId
              elif ptq2 == -1 :
                ptq2   = particle.pt
                etaq2  = particle.eta
                phiq2  = particle.phi
                idq2   = particle.pdgId
              else :
                print "another quark?? A third quark?? pt = ", particle.pt,  "  ptq1 = ", ptq1, "  ptq2 = ", ptq2, "  idq1 = ", idq1, "  idq2 = ", idq1
                

          #
          # if for any reason I was not able to assign the quarks, set the weight to -2 --> it can be followed up later
          #
          if ptq1 == -1 or ptq2 == -1 :
            ewknloW = -2
          else :  
            q1 = ROOT.TLorentzVector()
            q2 = ROOT.TLorentzVector()
            q1.SetPtEtaPhiM(ptq1, etaq1, phiq1, 0) # everything massless ... at these energies! ... maybe the b? ... but no, at reco all is massless
            q2.SetPtEtaPhiM(ptq2, etaq2, phiq2, 0)
            
            mjj = (q1+q2).Mag()
            
            ewknloW = 1.0

            if mjj > 1920. :
              mjj = 1920.
            if mjj < 525. :
              mjj = 525.
    
            if mjj > 525. :
              ewknloW = self.graph_ssWWvbs_kfact.Eval(mjj)
              ewknloWuncertainty = 0.025   # it's ~2.5% flat, from the plots
      


#     
#       \ \     /  __ )   ___|                       \ \        / \ \        / 
#        \ \   /   __ \ \___ \        _ \    __|      \ \  \   /   \ \  \   /  
#         \ \ /    |   |      |      (   | \__ \       \ \  \ /     \ \  \ /   
#          \_/    ____/ _____/      \___/  ____/        \_/\_/       \_/\_/    
#                                                                              

        if isVBSosWW : 
          
          #
          # NB: it assumes W>lvll
          #     At LHE level only quarks are from VBS scattering
          #
          # What to do for W>qq ?
          # Will these corrections still hold?
          #    --> FIXME: it needs to be checked, since q charge is different than l/v charge, IF in the calculation W decay was considered
          #
          
          # look for the two quarks to make mjj 
          ptq1 = -1
          ptq2 = -1
 
          for particle  in lheParticles :
              
            # quarks = 1, 2, 3, 4, 5, 6
            #
            # LHEPart_status    Int_t   LHE particle status; -1:incoming, 1:outgoing
            #
            if (abs(particle.pdgId) >= 1 and abs(particle.pdgId) <= 6) and (particle.status==1) :
     
              if ptq1 == -1 :
                ptq1   = particle.pt
                etaq1  = particle.eta
                phiq1  = particle.phi
                idq1   = particle.pdgId
              elif ptq2 == -1 :
                ptq2   = particle.pt
                etaq2  = particle.eta
                phiq2  = particle.phi
                idq2   = particle.pdgId
              else :
                print "another quark?? A third quark?? pt = ", particle.pt,  "  ptq1 = ", ptq1, "  ptq2 = ", ptq2, "  idq1 = ", idq1, "  idq2 = ", idq1
                

          #
          # if for any reason I was not able to aosign the quarks, set the weight to -2 --> it can be followed up later
          #
          if ptq1 == -1 or ptq2 == -1 :
            ewknloW = -2
          else :  
            q1 = ROOT.TLorentzVector()
            q2 = ROOT.TLorentzVector()
            q1.SetPtEtaPhiM(ptq1, etaq1, phiq1, 0) # everything massless ... at these energies! ... maybe the b? ... but no, at reco all is massless
            q2.SetPtEtaPhiM(ptq2, etaq2, phiq2, 0)
            
            mjj = (q1+q2).Mag()
            
            ewknloW = 1.0

            if mjj > 1920. :
              mjj = 1920.
            if mjj < 525. :
              mjj = 525.
    
            if mjj > 525. :
              ewknloW = self.graph_osWWvbs_kfact.Eval(mjj)
              ewknloWuncertainty = 0.01   # it's ~1% flat, from the plots  FIXME maybe to be estimated from corrections w.r.t. other variables?
      

 
        # now finally fill the branch ...
        #print ewknloW
        self.out.fillBranch("ewknloW",               ewknloW)
        self.out.fillBranch("ewknloWuncertainty",    ewknloWuncertainty)

        return True



