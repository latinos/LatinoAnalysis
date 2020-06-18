#
#
#
#    \ \     / \ \     /      ____| \ \        /  |  /       \  |  |       _ \  
#     \ \   /   \ \   /       __|    \ \  \   /   ' /         \ |  |      |   | 
#      \ \ /     \ \ /        |       \ \  \ /    . \       |\  |  |      |   | 
#       \_/       \_/        _____|    \_/\_/    _|\_\     _| \_| _____| \___/  
#                                                                               
#
#
#
#
# NLO Electroweak corrections for VV samples
#
#
# Based on qq2vvEWKcorrectionsWeight.py, qq2wvEWKcorrectionsWeight.py, and qq2zzEWKcorrectionsWeight.py
# modules of the gardener
#


import ROOT
ROOT.PyConfig.IgnoreCommandLineOptions = True

from PhysicsTools.NanoAODTools.postprocessing.framework.datamodel import Collection 
from PhysicsTools.NanoAODTools.postprocessing.framework.eventloop import Module

import os.path


class vvNLOEWKcorrectionWeightProducer(Module):
    def __init__(self, sample_type='ww'):
        #
        # "sample_type" should be ww, wz, zz
        #
        print ' ------> vvNLOEWKcorrectionWeightProducer Init() ----'
        # change this part into correct path structure... 
        cmssw_base = os.getenv('CMSSW_BASE')
        try:
            ROOT.gROOT.LoadMacro(cmssw_base+'/src/LatinoAnalysis/Gardener/python/variables/qq2vvEWKcorrectionsWeight.C+g')
            ROOT.gROOT.LoadMacro(cmssw_base+'/src/LatinoAnalysis/Gardener/python/variables/qq2wvEWKcorrectionsWeight.C+g')
        except RuntimeError:
            ROOT.gROOT.LoadMacro(cmssw_base+'/src/LatinoAnalysis/Gardener/python/variables/qq2vvEWKcorrectionsWeight.C++g')
            ROOT.gROOT.LoadMacro(cmssw_base+'/src/LatinoAnalysis/Gardener/python/variables/qq2wvEWKcorrectionsWeight.C++g')

        #
        # repsectively for ww, wz, and zz
        #
        self.qq2wwEWKcorrections = ROOT.qq2vvEWKcorrections(cmssw_base+'/src/LatinoAnalysis/Gardener/python/data/ewk/out_qqbww_EW_L8_200_forCMS.dat')
        self.qq2wzEWKcorrections = ROOT.qq2wvEWKcorrections(cmssw_base+'/src/LatinoAnalysis/Gardener/python/data/ewk/WZ_EwkCorrections.dat')
        self.qq2zzEWKcorrections = ROOT.qq2wvEWKcorrections(cmssw_base+'/src/LatinoAnalysis/Gardener/python/data/ewk/ZZ_EwkCorrections.dat')


        self.sample_type = sample_type

        print " sample_type = " , sample_type

      
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
        
        isww = False
        iswz = False
        iszz = False

        if self.sample_type == 'ww' :
          isww = True
        if self.sample_type == 'wz' :
          iswz = True
        if self.sample_type == 'zz' :
          iszz = True
          


        #
        # info in https://cms-nanoaod-integration.web.cern.ch/integration/master-102X/mc102X_doc.html        
        #
        
        #
        # LHE info in nanoaod 
        #
        #      LHEPart [back to top]
        #      Object property  Type    Description
        #      LHEPart_eta      Float_t Pseodorapidity of LHE particles
        #      LHEPart_mass     Float_t Mass of LHE particles
        #      LHEPart_pdgId    Int_t   PDG ID of LHE particles
        #      LHEPart_phi      Float_t Phi of LHE particles
        #      LHEPart_pt       Float_t Pt of LHE particles
        #      nLHEPart UInt_t  
        #


#
#         \ \        / \ \        / 
#          \ \  \   /   \ \  \   /  
#           \ \  \ /     \ \  \ /   
#            \_/\_/       \_/\_/    
#
        
        if isww : 
          
          ptl1 = -1
          ptl2 = -1
          
          ptv1 = -1
          ptv2 = -1
          
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

            # neutrinos
            #          12   14   16

            if abs(particle.pdgId) == 12 or abs(particle.pdgId) == 14 or abs(particle.pdgId) == 16:
     
              if ptv1 == -1 :
                ptv1   = particle.pt
                etav1  = particle.eta
                phiv1  = particle.phi
                idv1   = particle.pdgId
              elif ptv2 == -1 :
                ptv2   = particle.pt
                etav2  = particle.eta
                phiv2  = particle.phi
                idv2   = particle.pdgId

      
          #
          # if the code was unable to find 2 leptons -> 
          # WW and not 2 leptons means it is semileptonic decay WW>lvjj.
          # Then associate the pair "2" to the two quarks from W
          #
          if ptl2 == -1 :
            #
            # find the two quarks from W 
            #
            # It can be written in a more python-like manner, more performing ...
            #
            #
            #print " it is semileptonic "
            
            temp_ptq1 = -1
            temp_ptq2 = -1
            temp_ptq3 = -1
            temp_ptq4 = -1
            temp_etaq1 = -1
            temp_etaq2 = -1
            temp_etaq3 = -1
            temp_etaq4 = -1
            temp_phiq1 = -1
            temp_phiq2 = -1
            temp_phiq3 = -1
            temp_phiq4 = -1
            temp_idq1 = -1
            temp_idq2 = -1
            temp_idq3 = -1
            temp_idq4 = -1

            temp_m12 = -1
            temp_m13 = -1
            temp_m14 = -1
            temp_m23 = -1
            temp_m24 = -1
            temp_m34 = -1

            q1 = ROOT.TLorentzVector()
            q2 = ROOT.TLorentzVector()
            q3 = ROOT.TLorentzVector()
            q4 = ROOT.TLorentzVector()

            num_quarks = 0
            for particle  in lheParticles :      
              # quarks
              #          1, 2, 3, 4, 5, 6
              if abs(particle.pdgId) <= 6 and abs(particle.pdgId) >=1 and particle.pt != 0:
                num_quarks+=1
  
            for particle  in lheParticles :      
              # quarks
              #          1, 2, 3, 4, 5, 6
              if abs(particle.pdgId) <= 6 and abs(particle.pdgId) >=1 and particle.pt != 0:
             
                if temp_ptq1 == -1 :
                  temp_ptq1   = particle.pt
                  temp_etaq1  = particle.eta
                  temp_phiq1  = particle.phi
                  temp_idq1   = particle.pdgId
                  q1.SetPtEtaPhiM(temp_ptq1, temp_etaq1, temp_phiq1, 0) # fine approx massless quarks for check
                elif temp_ptq2 == -1 :
                  temp_ptq2   = particle.pt
                  temp_etaq2  = particle.eta
                  temp_phiq2  = particle.phi
                  temp_idq2   = particle.pdgId
                  q2.SetPtEtaPhiM(temp_ptq2, temp_etaq2, temp_phiq2, 0) # fine approx massless quarks for check
                elif temp_ptq3 == -1 :
                  temp_ptq3   = particle.pt
                  temp_etaq3  = particle.eta
                  temp_phiq3  = particle.phi
                  temp_idq3   = particle.pdgId
                  q3.SetPtEtaPhiM(temp_ptq3, temp_etaq3, temp_phiq3, 0) # fine approx massless quarks for check
                elif temp_ptq4 == -1 :
                  temp_ptq4   = particle.pt
                  temp_etaq4  = particle.eta
                  temp_phiq4  = particle.phi
                  temp_idq4   = particle.pdgId
                  q4.SetPtEtaPhiM(temp_ptq4, temp_etaq4, temp_phiq4, 0) # fine approx massless quarks for check
            
            # easy life ...
            if num_quarks == 2:
              
                ptl2   = temp_ptq1  
                etal2  = temp_etaq1 
                phil2  = temp_phiq1 
                idl2   = temp_idq1  

                ptv2   = temp_ptq2  
                etav2  = temp_etaq2 
                phiv2  = temp_phiq2 
                idv2   = temp_idq2  

            # W mass = 80.385
            # more complex: 3 combinations
            elif num_quarks == 3:
              temp_m12 = abs( (q1+q2).M() - 80.385 )
              temp_m13 = abs( (q1+q3).M() - 80.385 )
              temp_m23 = abs( (q1+q3).M() - 80.385 )
             
              if (temp_m12 <= temp_m13) and (temp_m12 <= temp_m23) :
                
                ptl2   = temp_ptq1  
                etal2  = temp_etaq1 
                phil2  = temp_phiq1 
                idl2   = temp_idq1  

                ptv2   = temp_ptq2  
                etav2  = temp_etaq2 
                phiv2  = temp_phiq2 
                idv2   = temp_idq2  
             
              elif (temp_m13 <= temp_m23) and (temp_m13 <= temp_m12) :
                
                ptl2   = temp_ptq1  
                etal2  = temp_etaq1 
                phil2  = temp_phiq1 
                idl2   = temp_idq1  

                ptv2   = temp_ptq3  
                etav2  = temp_etaq3 
                phiv2  = temp_phiq3 
                idv2   = temp_idq3  
                
              elif (temp_m23 <= temp_m13) and (temp_m23 <= temp_m12) :
                
                ptl2   = temp_ptq2  
                etal2  = temp_etaq2 
                phil2  = temp_phiq2 
                idl2   = temp_idq2  

                ptv2   = temp_ptq3  
                etav2  = temp_etaq3 
                phiv2  = temp_phiq3 
                idv2   = temp_idq3  
              
            # W mass = 80.385
            # and now the nightmare: 6 combinations
            elif num_quarks == 5:
              temp_m12 = abs( (q1+q2).M() - 80.385 )
              temp_m13 = abs( (q1+q3).M() - 80.385 )
              temp_m14 = abs( (q1+q4).M() - 80.385 )
              temp_m23 = abs( (q2+q3).M() - 80.385 )
              temp_m24 = abs( (q2+q4).M() - 80.385 )
              temp_m34 = abs( (q3+q4).M() - 80.385 )
             
              list_of_mass_combinations = [temp_m12, temp_m13, temp_m14, temp_m23, temp_m24, temp_m34]
              the_smallest_mass_combination = list_of_mass_combinations.index(min(list_of_mass_combinations))
              
              if the_smallest_mass_combination == 0 : 

                ptl2   = temp_ptq1  
                etal2  = temp_etaq1 
                phil2  = temp_phiq1 
                idl2   = temp_idq1  

                ptv2   = temp_ptq2  
                etav2  = temp_etaq2 
                phiv2  = temp_phiq2 
                idv2   = temp_idq2  
             
              elif the_smallest_mass_combination == 1 :
                
                ptl2   = temp_ptq1  
                etal2  = temp_etaq1 
                phil2  = temp_phiq1 
                idl2   = temp_idq1  

                ptv2   = temp_ptq3  
                etav2  = temp_etaq3 
                phiv2  = temp_phiq3 
                idv2   = temp_idq3  
            
              elif the_smallest_mass_combination == 2 :
                
                ptl2   = temp_ptq1  
                etal2  = temp_etaq1 
                phil2  = temp_phiq1 
                idl2   = temp_idq1  

                ptv2   = temp_ptq4  
                etav2  = temp_etaq4 
                phiv2  = temp_phiq4 
                idv2   = temp_idq4  
            
              elif the_smallest_mass_combination == 3 :
                
                ptl2   = temp_ptq2  
                etal2  = temp_etaq2 
                phil2  = temp_phiq2 
                idl2   = temp_idq2  

                ptv2   = temp_ptq3  
                etav2  = temp_etaq3 
                phiv2  = temp_phiq3 
                idv2   = temp_idq3  
            
              elif the_smallest_mass_combination == 4 :
                
                ptl2   = temp_ptq2  
                etal2  = temp_etaq2 
                phil2  = temp_phiq2 
                idl2   = temp_idq2  

                ptv2   = temp_ptq4  
                etav2  = temp_etaq4 
                phiv2  = temp_phiq4 
                idv2   = temp_idq4  
            
              elif the_smallest_mass_combination == 5 :
                
                ptl2   = temp_ptq3  
                etal2  = temp_etaq3 
                phil2  = temp_phiq3 
                idl2   = temp_idq3  

                ptv2   = temp_ptq4  
                etav2  = temp_etaq4 
                phiv2  = temp_phiq4 
                idv2   = temp_idq4  
            
            #print " num_quarks = " , num_quarks
            
          #else :
            #print " it is NOT semileptonic "



          #  Generator [back to top]
          #  Object property Type    Description
          #  Generator_binvar        Float_t MC generation binning value
          #  Generator_id1   Int_t   id of first parton
          #  Generator_id2   Int_t   id of second parton
          #  Generator_scalePDF      Float_t Q2 scale for PDF
          #  Generator_weight        Float_t MC generator weight
          #  Generator_x1    Float_t x1 fraction of proton momentum carried by the first parton
          #  Generator_x2    Float_t x2 fraction of proton momentum carried by the second parton
          #  Generator_xpdf1 Float_t x*pdf(x) for the first parton
          #  Generator_xpdf2 Float_t x*pdf(x) for the second parton
         
          x1 = event.Generator_x1
          x2 = event.Generator_x2

          id1 = event.Generator_id1
          id2 = event.Generator_id2
         
          #float ptl1 , float etal1 , float phil1 , float idl1 , // lepton from 1st W
          #float ptl2 , float etal2 , float phil2 , float idl2 , // lepton from 2nd W
          #float ptv1 , float etav1 , float phiv1 ,              // neutrino from 1st W
          #float ptv2 , float etav2 , float phiv2 ,              // neutrino from 2nd W
          #float x1   , float x2 ,                               // parton x-Bjorken
          #int   id1  , int   id2 ,                              // parton PDG id's
         
          #
          # if for any reason I was not able to assign the leptons, set the weight to -2 --> it can be followed up later
          #
          if ptl1 == -1 or ptl2 == -1 or ptv1 == -1 or ptv2 == -1 :
            ewknloW = -2
            #print " ewknloW ==  -2 ??? "
          else :         
            #
            # After lookig carefully at the referenced paper arXiv:1401.3964,
            # in order to have the "t" Mandelstam variable defined in the standard way for qq>WW
            # we check the charge of q1 and W1, such that charge (q1) has the same sign of the charge (W1)
            # https://en.wikipedia.org/wiki/Mandelstam_variables
            #
            #   d 1  -1/3          ~d -1  +1/3
            #   u 2  +2/3          ~u -2  -2/3
            #   s 3  -1/3          ~s -3  +1/3
            #   c 4  +2/3          ~c -4  -2/3
            #   b 5  -1/3          ~b -5  +1/3
            #   t 6  +2/3          ~t -6  -2/3
            #
            # W+   >     u ~d,    c ~s,    t ~b      --> sum id =  1
            # W-   >    ~u  d,   ~c  s,   ~t  b      --> sum id = -1
            
            swap = False
            #                                                    <---              fully leptonic            --->     <---     semileptonic                  --->
            #            u              c              t    > 0            e-               mu-              tau-             W+ is the other -> 1 is W-         < 0
            if ((id1 ==  2) or (id1 ==  4) or (id1 ==  6)) and  ((idl1 ==  11) or (idl1 ==  13) or (idl1 ==  15)  or             (idl2+idv2 ==  1)               ) :
              swap = True
            #           ~u             ~c             ~t    < 0            e+               mu+              tau+             W- is the other -> -1 is W+         > 0
            if ((id1 == -2) or (id1 == -4) or (id1 == -6)) and  ((idl1 == -11) or (idl1 == -13) or (idl1 == -15)  or             (idl2+idv2 == -1)               ) :
              swap = True
            #            d              s              b    < 0            e+               mu+              tau+             W- is the other -> -1 is W+         > 0
            if ((id1 ==  1) or (id1 ==  3) or (id1 ==  5)) and  ((idl1 == -11) or (idl1 == -13) or (idl1 == -15)  or             (idl2+idv2 == -1)               ) :
              swap = True
            #           ~d             ~s             ~b    > 0            e-               mu-              tau-             W+ is the other -> 1 is W-         < 0
            if ((id1 == -1) or (id1 == -3) or (id1 == -5)) and  ((idl1 ==  11) or (idl1 ==  13) or (idl1 ==  15)  or             (idl2+idv2 == 1)                ) :  
              swap = True
                         
            if swap :
              ptl1, etal1, phil1, idl1, ptl2, etal2, phil2, idl2  =  ptl2, etal2, phil2, idl2, ptl1, etal1, phil1, idl1
              ptv1, etav1, phiv1, idv1, ptv2, etav2, phiv2, idv2  =  ptv2, etav2, phiv2, idv2, ptv1, etav1, phiv1, idv1
              
            ewknloW = self.qq2wwEWKcorrections.getqq2WWEWKCorr(ptl1, etal1, phil1, idl1, ptl2, etal2, phil2, idl2, ptv1, etav1, phiv1, ptv2, etav2, phiv2, x1, x2, id1, id2)

#  
#          \ \        / __  / 
#           \ \  \   /     /  
#            \ \  \ /     /   
#             \_/\_/    ____| 
# 
 
        if iswz : 
          
          temp_ptl1 = -1
          temp_ptl2 = -1
          temp_ptl3 = -1
          temp_etal1 = -1
          temp_etal2 = -1
          temp_etal3 = -1
          temp_phil1 = -1
          temp_phil2 = -1
          temp_phil3 = -1
          temp_idl1 = -1
          temp_idl2 = -1
          temp_idl3 = -1
          
          temp_ptv1 = -1
          temp_ptv2 = -1
          temp_ptv3 = -1
          temp_etav1 = -1
          temp_etav2 = -1
          temp_etav3 = -1
          temp_phiv1 = -1
          temp_phiv2 = -1
          temp_phiv3 = -1
          temp_idlv1 = -1
          temp_idlv2 = -1
          temp_idlv3 = -1

          temp_ptq1 = -1
          temp_ptq2 = -1
          temp_etaq1 = -1
          temp_etaq2 = -1
          temp_phiq1 = -1
          temp_phiq2 = -1
          temp_idq1 = -1
          temp_idq2 = -1

          #print " ~~ new event "
          
          for particle  in lheParticles :
              
            #print " particle.pdgId = " , particle.pdgId
            
            
            # lepton = 11, 13, 15
            #          e   mu  tau
            
            if abs(particle.pdgId) == 11 or abs(particle.pdgId) == 13 or abs(particle.pdgId) == 15:
     
              if temp_ptl1 == -1 :
                temp_ptl1   = particle.pt
                temp_etal1  = particle.eta
                temp_phil1  = particle.phi
                temp_idl1   = particle.pdgId
              elif temp_ptl2 == -1 :
                temp_ptl2   = particle.pt
                temp_etal2  = particle.eta
                temp_phil2  = particle.phi
                temp_idl2   = particle.pdgId
              elif temp_ptl3 == -1 :
                temp_ptl3   = particle.pt
                temp_etal3  = particle.eta
                temp_phil3  = particle.phi
                temp_idl3   = particle.pdgId

            # neutrinos
            #          12   14   16

            if abs(particle.pdgId) == 12 or abs(particle.pdgId) == 14 or abs(particle.pdgId) == 16:
     
              if temp_ptv1 == -1 :
                temp_ptv1   = particle.pt
                temp_etav1  = particle.eta
                temp_phiv1  = particle.phi
                temp_idv1   = particle.pdgId
              elif temp_ptv2 == -1 :
                temp_ptv2   = particle.pt
                temp_etav2  = particle.eta
                temp_phiv2  = particle.phi
                temp_idv2   = particle.pdgId
              elif temp_ptv3 == -1 :
                temp_ptv3   = particle.pt
                temp_etav3  = particle.eta
                temp_phiv3  = particle.phi
                temp_idv3   = particle.pdgId


            # quarks
            #          1, 2, 3, 4, 5, 6

            #                                                           incoming quarks have 0 pt (otherwise 2 incoming quarks are in this list)
            if abs(particle.pdgId) <= 6 and abs(particle.pdgId) >=1 and particle.pt != 0:
     
              if temp_ptq1 == -1 :
                temp_ptq1   = particle.pt
                temp_etaq1  = particle.eta
                temp_phiq1  = particle.phi
                temp_idq1   = particle.pdgId
              elif temp_ptq2 == -1 :
                temp_ptq2   = particle.pt
                temp_etaq2  = particle.eta
                temp_phiq2  = particle.phi
                temp_idq2   = particle.pdgId

          
          
          x1 = event.Generator_x1
          x2 = event.Generator_x2
 
          id1 = event.Generator_id1
          id2 = event.Generator_id2


          ptl1  = 0.
          etal1 = 0.
          phil1 = 0.
          idl1  = 0.
          
          ptl2  = 0.
          etal2 = 0.
          phil2 = 0.
          idl2  = 0.

          ptv1   = 0
          etav1  = 0
          phiv1  = 0
          idv1   = 0.
          
          ptv2   = 0.
          etav2  = 0.
          phiv2  = 0.
          idv2   = 0.


          # 1 should be the W
          # 2 should be the Z
          
          if temp_ptv2 > 0 :
            # W>lv  and   Z>vv
            ptl1  = temp_ptl1
            etal1 = temp_etal1
            phil1 = temp_phil1
            idl1  = temp_idl1
            
            if (abs(temp_idv1) == (abs(idl1)+1)) :
                  
              ptv1  = temp_ptv1
              etav1 = temp_etav1
              phiv1 = temp_phiv1
              idv1  = temp_idv1
             
              ptl2  = temp_ptv2
              etal2 = temp_etav2
              phil2 = temp_phiv2
              idl2  = temp_idv2
             
              ptv2  = temp_ptv3
              etav2 = temp_etav3
              phiv2 = temp_phiv3
              idv2  = temp_idv3    
           
            elif (abs(temp_idv2) == (abs(idl1)+1)) :
                    
              ptv1  = temp_ptv2
              etav1 = temp_etav2
              phiv1 = temp_phiv2
              idv1  = temp_idv2
             
              ptl2  = temp_ptv1
              etal2 = temp_etav1
              phil2 = temp_phiv1
              idl2  = temp_idv1
             
              ptv2  = temp_ptv3
              etav2 = temp_etav3
              phiv2 = temp_phiv3
              idv2  = temp_idv3    
           
            elif (abs(temp_idv3) == (abs(idl1)+1)) :
                    
              ptv1  = temp_ptv3
              etav1 = temp_etav3
              phiv1 = temp_phiv3
              idv1  = temp_idv3
             
              ptl2  = temp_ptv1
              etal2 = temp_etav1
              phil2 = temp_phiv1
              idl2  = temp_idv1
             
              ptv2  = temp_ptv2
              etav2 = temp_etav2
              phiv2 = temp_phiv2
              idv2  = temp_idv2   
           

           
          elif temp_ptv1>0 and temp_ptl1>0 and temp_ptl2>0 :
           
            # W>lv  and   Z>ll
 
            # assign the 3 leptons and the neutrino to the correct vector boson
            #
            # 1) the neutrino is hte first position
            #
            ptv1  = temp_ptv1
            etav1 = temp_etav1
            phiv1 = temp_phiv1
            idv1  = temp_idv1
            #
            # 2) look for a lepton with the correct charge and the invariant mass close to W
            #
            v1 = ROOT.TLorentzVector()
            v1.SetPtEtaPhiM(ptv1, etav1, phiv1, 0)
              
            if (abs(idv1) == (abs(temp_idl1)+1)) :
              
              l1 = ROOT.TLorentzVector()
              l1.SetPtEtaPhiM(temp_ptl1, temp_etal1, temp_phil1, 0)
              
              mass = (l1+v1).M()                
              #print " mass = ", mass
              
              if abs (mass - 80.385) < 3 :
                
                ptl1  = temp_ptl1
                etal1 = temp_etal1
                phil1 = temp_phil1
                idl1  = temp_idl1
                
                ptl2  = temp_ptl2
                etal2 = temp_etal2
                phil2 = temp_phil2
                idl2  = temp_idl2
               
                ptv2  = temp_ptl3
                etav2 = temp_etal3
                phiv2 = temp_phil3
                idv2  = temp_idl3    
                               

              
            elif (abs(idv1) == (abs(temp_idl2)+1)) :
              
              l1 = ROOT.TLorentzVector()
              l1.SetPtEtaPhiM(temp_ptl2, temp_etal2, temp_phil2, 0)
              
              mass = (l1+v1).M()                
              #print " mass 2 = ", mass
              
              if abs (mass - 80.385) < 3 :
                
                ptl1  = temp_ptl2
                etal1 = temp_etal2
                phil1 = temp_phil2
                idl1  = temp_idl2
                
                ptl2  = temp_ptl1
                etal2 = temp_etal1
                phil2 = temp_phil1
                idl2  = temp_idl1
               
                ptv2  = temp_ptl3
                etav2 = temp_etal3
                phiv2 = temp_phil3
                idv2  = temp_idl3    


            else :
                    
              ptl1  = temp_ptl3
              etal1 = temp_etal3
              phil1 = temp_phil3
              idl1  = temp_idl3

              ptl2  = temp_ptl1
              etal2 = temp_etal1
              phil2 = temp_phil1
              idl2  = temp_idl1
             
              ptv2  = temp_ptl2
              etav2 = temp_etal2
              phiv2 = temp_phil2
              idv2  = temp_idl2    

           
          elif temp_ptq1 > 0 and temp_ptq2 > 0 and temp_ptl1>0 and temp_ptl2>0 :   # ---> "temp_ptq1 > 0" alone is not safe because of NLO (additional quarks!)

            # W>qq  and   Z>ll

            ptl1  = temp_ptq1
            etal1 = temp_etaq1
            phil1 = temp_phiq1
            idl1  = temp_idq1
            
            ptv1  = temp_ptq2
            etav1 = temp_etaq2
            phiv1 = temp_phiq2
            idv1  = temp_idq2
            
            ptl2  = temp_ptl1
            etal2 = temp_etal1
            phil2 = temp_phil1
            idl2  = temp_idl1
           
            ptv2  = temp_ptl2
            etav2 = temp_etal2
            phiv2 = temp_phil2
            idv2  = temp_idl2   

          
          
          elif temp_ptq1 > 0 and temp_ptq2 > 0 and temp_ptl1>0 and temp_ptv1>0 : 

            # W>lv  and   Z>qq

            ptl1  = temp_ptl1
            etal1 = temp_etal1
            phil1 = temp_phil1
            idl1  = temp_idl1
            
            ptv1  = temp_ptv1
            etav1 = temp_etav1
            phiv1 = temp_phiv1
            idv1  = temp_idv1
            
            ptl2  = temp_ptq1
            etal2 = temp_etaq1
            phil2 = temp_phiq1
            idl2  = temp_idq1
           
            ptv2  = temp_ptq2
            etav2 = temp_etaq2
            phiv2 = temp_phiq2
            idv2  = temp_idq2   



            
          if ptl1 == -1 or ptl2 == -1 or ptv1 == -1 or ptv2 == -1 :
            ewknloW = -2
          else :       
            results_value_and_error = self.qq2wzEWKcorrections.getqq2WVEWKCorr(ptl1, etal1, phil1, idl1, ptl2, etal2, phil2, idl2, ptv1, etav1, phiv1, idv1, ptv2, etav2, phiv2, idv2, x1, x2, id1, id2,    1)
            ewknloW = results_value_and_error[0]
            ewknloWuncertainty = results_value_and_error[1]


#
#          __  / __  / 
#             /     /  
#            /     /   
#          ____| ____| 
#

        if iszz :             


          temp_ptl1 = -1
          temp_ptl2 = -1
          temp_ptl3 = -1
          temp_ptl4 = -1
          
          temp_ptv1 = -1
          temp_ptv2 = -1

          temp_etal1 = -1
          temp_etal2 = -1
          temp_etal3 = -1
          temp_etal4 = -1
          
          temp_etav1 = -1
          temp_etav2 = -1

          temp_phil1 = -1
          temp_phil2 = -1
          temp_phil3 = -1
          temp_phil4 = -1
          
          temp_phiv1 = -1
          temp_phiv2 = -1

          temp_idl1 = -1
          temp_idl2 = -1
          temp_idl3 = -1
          temp_idl4 = -1
          
          temp_idv1 = -1
          temp_idv2 = -1



          temp_ptq1 = -1
          temp_ptq2 = -1
 
          temp_etaq1 = -1
          temp_etaq2 = -1
          
          temp_phiq1 = -1
          temp_phiq2 = -1
          
          temp_idq1 = -1
          temp_idq2 = -1
 
          
          for particle  in lheParticles :
              
            # lepton = 11, 13, 15
            #          e   mu  tau
            
            if abs(particle.pdgId) == 11 or abs(particle.pdgId) == 13 or abs(particle.pdgId) == 15:
     
              if temp_ptl1 == -1 :
                temp_ptl1   = particle.pt
                temp_etal1  = particle.eta
                temp_phil1  = particle.phi
                temp_idl1   = particle.pdgId
              elif temp_ptl2 == -1 :
                temp_ptl2   = particle.pt
                temp_etal2  = particle.eta
                temp_phil2  = particle.phi
                temp_idl2   = particle.pdgId
              elif temp_ptl3 == -1 :
                temp_ptl3   = particle.pt
                temp_etal3  = particle.eta
                temp_phil3  = particle.phi
                temp_idl3   = particle.pdgId
              elif temp_ptl4 == -1 :
                temp_ptl4   = particle.pt
                temp_etal4  = particle.eta
                temp_phil4  = particle.phi
                temp_idl4   = particle.pdgId

            # neutrinos
            #          12   14   16

            if abs(particle.pdgId) == 12 or abs(particle.pdgId) == 14 or abs(particle.pdgId) == 16:
     
              if temp_ptv1 == -1 :
                temp_ptv1   = particle.pt
                temp_etav1  = particle.eta
                temp_phiv1  = particle.phi
                temp_idv1   = particle.pdgId
              elif temp_ptv2 == -1 :
                temp_ptv2   = particle.pt
                temp_etav2  = particle.eta
                temp_phiv2  = particle.phi
                temp_idv2   = particle.pdgId


            # quarks
            #          1, 2, 3, 4, 5, 6

            #                                                           incoming quarks have 0 pt (otherwise 2 incoming quarks are in this list)
            if abs(particle.pdgId) <= 6 and abs(particle.pdgId) >=1 and particle.pt != 0:
     
              if temp_ptq1 == -1 :
                temp_ptq1   = particle.pt
                temp_etaq1  = particle.eta
                temp_phiq1  = particle.phi
                temp_idq1   = particle.pdgId
              elif temp_ptq2 == -1 :
                temp_ptq2   = particle.pt
                temp_etaq2  = particle.eta
                temp_phiq2  = particle.phi
                temp_idq2   = particle.pdgId


          x1 = event.Generator_x1
          x2 = event.Generator_x2
 
          id1 = event.Generator_id1
          id2 = event.Generator_id2

          
          ptl1  = 0.
          etal1 = 0.
          phil1 = 0.
          idl1  = 0.
          
          ptl2  = 0.
          etal2 = 0.
          phil2 = 0.
          idl2  = 0.

          ptv1   = 0
          etav1  = 0
          phiv1  = 0
          idv1   = 0.
          
          ptv2   = 0.
          etav2  = 0.
          phiv2  = 0.
          idv2   = 0.


          # 1 should be the first Z
          # 2 should be the second Z

          # assign the 4 leptons according to flavour and mass

          if temp_ptl1 > 0 and temp_ptl3 > 0 :
            # Z>ll and Z>ll

            if (abs(temp_idl1) == abs(temp_idl2)) :

              l1 = ROOT.TLorentzVector()
              l1.SetPtEtaPhiM(temp_ptl1, temp_etal1, temp_phil1, 0) # fine approx massless leptons for check

              l2 = ROOT.TLorentzVector()
              l2.SetPtEtaPhiM(temp_ptl2, temp_etal2, temp_phil2, 0) # fine approx massless leptons for check
                            
              mass = (l1+l2).M()                
       
              if abs (mass - 91.1876) < 3 :
                
                ptl1  = temp_ptl1
                etal1 = temp_etal1
                phil1 = temp_phil1
                idl1  = temp_idl1
                
                ptv1  = temp_ptl2
                etav1 = temp_etal2
                phiv1 = temp_phil2
                idv1  = temp_idl2
                
                ptl2  = temp_ptl3
                etal2 = temp_etal3
                phil2 = temp_phil3
                idl2  = temp_idl3
               
                ptv2  = temp_ptl4
                etav2 = temp_etal4
                phiv2 = temp_phil4
                idv2  = temp_idl4   


            if (abs(temp_idl1) == abs(temp_idl3)) :

              l1 = ROOT.TLorentzVector()
              l1.SetPtEtaPhiM(temp_ptl1, temp_etal1, temp_phil1, 0) # fine approx massless leptons for check

              l2 = ROOT.TLorentzVector()
              l2.SetPtEtaPhiM(temp_ptl3, temp_etal3, temp_phil3, 0) # fine approx massless leptons for check
                            
              mass = (l1+l2).M()                
       
              if abs (mass - 91.1876) < 3 :
                
                ptl1  = temp_ptl1
                etal1 = temp_etal1
                phil1 = temp_phil1
                idl1  = temp_idl1
                
                ptv1  = temp_ptl3
                etav1 = temp_etal3
                phiv1 = temp_phil3
                idv1  = temp_idl3
                
                ptl2  = temp_ptl2
                etal2 = temp_etal2
                phil2 = temp_phil2
                idl2  = temp_idl2
               
                ptv2  = temp_ptl4
                etav2 = temp_etal4
                phiv2 = temp_phil4
                idv2  = temp_idl4   
                               

            if (abs(temp_idl1) == abs(temp_idl4)) :

              l1 = ROOT.TLorentzVector()
              l1.SetPtEtaPhiM(temp_ptl1, temp_etal1, temp_phil1, 0) # fine approx massless leptons for check

              l2 = ROOT.TLorentzVector()
              l2.SetPtEtaPhiM(temp_ptl4, temp_etal4, temp_phil4, 0) # fine approx massless leptons for check
                            
              mass = (l1+l2).M()                
       
              if abs (mass - 91.1876) < 3 :
                
                ptl1  = temp_ptl1
                etal1 = temp_etal1
                phil1 = temp_phil1
                idl1  = temp_idl1
                
                ptv1  = temp_ptl4
                etav1 = temp_etal4
                phiv1 = temp_phil4
                idv1  = temp_idl4
                
                ptl2  = temp_ptl2
                etal2 = temp_etal2
                phil2 = temp_phil2
                idl2  = temp_idl2
               
                ptv2  = temp_ptl3
                etav2 = temp_etal3
                phiv2 = temp_phil3
                idv2  = temp_idl3  
                               


          elif temp_ptl1 > 0 and temp_ptv1 > 0 :
            # Z>ll and Z>vv
            
            ptl1  = temp_ptl1
            etal1 = temp_etal1
            phil1 = temp_phil1
            idl1  = temp_idl1
            
            ptv1  = temp_ptl2
            etav1 = temp_etal2
            phiv1 = temp_phil2
            idv1  = temp_idl2
            
            ptl2  = temp_ptv1
            etal2 = temp_etav1
            phil2 = temp_phiv1
            idl2  = temp_idv1
           
            ptv2  = temp_ptv2
            etav2 = temp_etav2
            phiv2 = temp_phiv2
            idv2  = temp_idv2   



          elif temp_ptl1 > 0 and temp_ptq1 > 0 and temp_ptq2 > 0 :
            # Z>ll and Z>qq
            
            ptl1  = temp_ptl1
            etal1 = temp_etal1
            phil1 = temp_phil1
            idl1  = temp_idl1
            
            ptv1  = temp_ptl2
            etav1 = temp_etal2
            phiv1 = temp_phil2
            idv1  = temp_idl2
            
            ptl2  = temp_ptq1
            etal2 = temp_etaq1
            phil2 = temp_phiq1
            idl2  = temp_idq1
           
            ptv2  = temp_ptq2
            etav2 = temp_etaq2
            phiv2 = temp_phiq2
            idv2  = temp_idq2   



          if ptl1 == -1 or ptl2 == -1 or ptv1 == -1 or ptv2 == -1 :
            ewknloW = -2
          else :                       
            results_value_and_error = self.qq2zzEWKcorrections.getqq2WVEWKCorr(ptl1, etal1, phil1, idl1, ptl2, etal2, phil2, idl2, ptv1, etav1, phiv1, idv1, ptv2, etav2, phiv2, idv2, x1, x2, id1, id2,    0)
            ewknloW = results_value_and_error[0]
            ewknloWuncertainty = results_value_and_error[1]
          



 
        # now finally fill the branch ...
        self.out.fillBranch("ewknloW",               ewknloW)
        self.out.fillBranch("ewknloWuncertainty",    ewknloWuncertainty)

        return True



