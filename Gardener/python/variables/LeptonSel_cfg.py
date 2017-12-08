

####################### Electrons ##################################

ElectronWP = {}

# --------------------------- 2015  - 74x --------------------------

# --------------------------- 2015  - 76x --------------------------

# --------------------------- ICHEP2016 ----------------------------

# --------------------------- Full2016 -----------------------------

ElectronWP['Full2016'] = {

  'Variables' : {
 
         'relPFIsoRhoCorr' : '(itree.std_vector_lepton_chargedHadronIso[] + max(itree.std_vector_lepton_neutralHadronIso[]+itree.std_vector_lepton_photonIso[]-itree.jetRho*itree.std_vector_electron_effectiveArea[],0))/itree.std_vector_lepton_pt[]',
         'pt_to_be_removed_from_overlap' : 'self.isoConeOverlapRemoval(itree,iLep)'
               },

## ------------  

#'VetoObjWP' : { 
#          'HLTsafe' : { 
#                         'cuts' : { 
#                               # Common cuts
#                               'True' :
#                                [
#                                  'abs(itree.std_vector_lepton_eta[]) < 2.5' ,
#                                  'itree.std_vector_lepton_eleIdHLT[] ' ,
#                                ] ,             
#                                   },
#                      } ,
#                } ,
  
 # ------------ 
 'FakeObjWP'  : {

           'HLTsafe' : { 
                         'cuts' : { 
                                # Common cuts
                                'True' :
                                 [
                                   'abs(itree.std_vector_lepton_eta[]) < 2.5' ,
                                   'itree.std_vector_lepton_eleIdHLT[] ' ,
                                   'itree.std_vector_electron_expectedMissingInnerHits[] < 1',
                                 ] ,             
                                # Barrel
                                'abs(itree.std_vector_lepton_eta[]) <= 1.479' :
                                  [
                                    'abs(itree.std_vector_lepton_d0[]) < 0.05' ,
                                    'abs(itree.std_vector_lepton_dz[]) < 0.1'  ,
                                  ] ,
                                # EndCap
                                'abs(itree.std_vector_lepton_eta[]) > 1.479' :
                                  [
                                    'abs(itree.std_vector_lepton_d0[]) < 0.1' ,
                                    'abs(itree.std_vector_lepton_dz[]) < 0.2'  ,
                                  ] ,
                                   },
                       } ,

                 } ,

 # ------------ 
 'TightObjWP' : {

         'cut_WP_Tight80X' : {
                         'cuts' : { 
                                # Common cuts
                                'True' :
                                  [
                                    'abs(itree.std_vector_lepton_eta[]) < 2.5' ,
                                    'itree.std_vector_lepton_eleIdHLT[]',
                                    'itree.std_vector_lepton_eleIdTight[]', 
                                    'itree.std_vector_electron_expectedMissingInnerHits[] < 1',
                                  ] , 
                                # Barrel
                                'abs(itree.std_vector_lepton_eta[]) <= 1.479' :
                                  [
                                    'abs(itree.std_vector_lepton_d0[]) < 0.05' ,
                                    'abs(itree.std_vector_lepton_dz[]) < 0.1'  ,
                                  ] ,
                                # EndCap
                                'abs(itree.std_vector_lepton_eta[]) > 1.479' :
                                  [
                                    'abs(itree.std_vector_lepton_d0[]) < 0.1' ,
                                    'abs(itree.std_vector_lepton_dz[]) < 0.2'  ,
                                  ] ,
                                  } ,
                         'tkSF':  { 
                                    '1-7' : 'LatinoAnalysis/Gardener/python/data/idiso/Full2016/egammaEffi.txt_EGM2D.root' ,
                                  } ,
                         'wpSF':  {
                                    '1-7' : 'LatinoAnalysis/Gardener/python/data/idiso/Full2016/electrons_cut_WP_Tight80X.txt' ,  
                                  } ,
                         'fakeW' : '/LatinoAnalysis/Gardener/python/data/fake_prompt_rates/80X/lowPtCorrected/36fb_ele_cut_WP_Tight80X/',
                             } ,


         'cut_WP_Tight80X_SS' : {
                         'cuts' : { 
                                # Common cuts
                                'True' :
                                  [
                                    'abs(itree.std_vector_lepton_eta[]) < 2.5' ,
                                    'itree.std_vector_lepton_eleIdHLT[]',
                                    'itree.std_vector_lepton_eleIdTight[]',
                                    'itree.std_vector_electron_expectedMissingInnerHits[] < 1',
                                    'itree.std_vector_electron_tripleChargeAgreement[]',
                                  ] ,
                                # Barrel
                                'abs(itree.std_vector_lepton_eta[]) <= 1.479' :
                                  [
                                    'abs(itree.std_vector_lepton_d0[]) < 0.05' ,
                                    'abs(itree.std_vector_lepton_dz[]) < 0.1'  ,
                                  ] ,
                                # EndCap
                                'abs(itree.std_vector_lepton_eta[]) > 1.479' :
                                  [
                                    'abs(itree.std_vector_lepton_d0[]) < 0.1' ,
                                    'abs(itree.std_vector_lepton_dz[]) < 0.2'  ,
                                  ] ,
                                  } ,
                         'tkSF':  { 
                                    '1-7' : 'LatinoAnalysis/Gardener/python/data/idiso/Full2016/egammaEffi.txt_EGM2D.root' ,
                                  } ,
                         'wpSF':  {
                                    '1-7' : 'LatinoAnalysis/Gardener/python/data/idiso/Full2016/electrons_cut_WP_Tight80X_SS.txt' ,
                                  } ,
                         'fakeW' : '/LatinoAnalysis/Gardener/python/data/fake_prompt_rates/80X/lowPtCorrected/36fb_ele_cut_WP_Tight80X_SS/',
                             } ,


          'mva_80p_Iso2015':  {
                         'cuts' : { 
                                # Common cuts 
                                'True' :
                                   [
                                     'abs(itree.std_vector_lepton_eta[]) < 2.5' ,
                                     'itree.std_vector_lepton_eleIdHLT[]',
                                     'itree.std_vector_lepton_eleIdMvaWp80[]',
                                     'itree.std_vector_electron_expectedMissingInnerHits[] < 1',
                                   ] ,
                                # Barrel
                                 'abs(itree.std_vector_lepton_eta[]) <= 1.479' :
                                   [
                                     'abs(itree.std_vector_lepton_d0[]) < 0.05' ,
                                     'abs(itree.std_vector_lepton_dz[]) < 0.1'  ,
                                     'relPFIsoRhoCorr < 0.0354',
                                   ] ,
                                 # EndCap
                                 'abs(itree.std_vector_lepton_eta[]) > 1.479' :
                                   [
                                     'abs(itree.std_vector_lepton_d0[]) < 0.1' ,
                                     'abs(itree.std_vector_lepton_dz[]) < 0.2'  ,
                                     'relPFIsoRhoCorr < 0.0646',
                                   ] ,
                                  } ,
                         'tkSF':  { 
                                    '1-7' : 'LatinoAnalysis/Gardener/python/data/idiso/Full2016/egammaEffi.txt_EGM2D.root' ,
                                  } ,
                         'wpSF':  {
                                    '1-7' : 'LatinoAnalysis/Gardener/python/data/idiso/Full2016/electrons_mva_80p_Iso2015.txt' ,
                                  } ,
                         'fakeW' : '/LatinoAnalysis/Gardener/python/data/fake_prompt_rates/80X/lowPtCorrected/36fb_ele_mva_80p_Iso2015/',
                              } ,
 
          'mva_80p_Iso2016':  {
                         'cuts' : { 
                                # Common cuts 
                                'True' :
                                   [
                                     'abs(itree.std_vector_lepton_eta[]) < 2.5' ,
                                     'itree.std_vector_lepton_eleIdHLT[]',
                                     'itree.std_vector_lepton_eleIdMvaWp80[]',
                                     'itree.std_vector_electron_expectedMissingInnerHits[] < 1',
                                   ] ,
                                # Barrel
                                 'abs(itree.std_vector_lepton_eta[]) <= 1.479' :
                                   [
                                     'abs(itree.std_vector_lepton_d0[]) < 0.05' ,
                                     'abs(itree.std_vector_lepton_dz[]) < 0.1'  ,
                                     'relPFIsoRhoCorr < 0.05880',
                                   ] ,
                                 # EndCap
                                 'abs(itree.std_vector_lepton_eta[]) > 1.479' :
                                   [
                                     'abs(itree.std_vector_lepton_d0[]) < 0.1' ,
                                     'abs(itree.std_vector_lepton_dz[]) < 0.2'  ,
                                     'relPFIsoRhoCorr < 0.0571',
                                   ] ,
                                  } ,
                         'tkSF':  { 
                                    '1-7' : 'LatinoAnalysis/Gardener/python/data/idiso/Full2016/egammaEffi.txt_EGM2D.root' ,
                                  } ,
                         'wpSF':  {
                                    '1-7' : 'LatinoAnalysis/Gardener/python/data/idiso/Full2016/electrons_mva_80p_Iso2016.txt' ,
                                  } ,
                         'fakeW' : '/LatinoAnalysis/Gardener/python/data/fake_prompt_rates/80X/lowPtCorrected/36fb_ele_mva_80p_Iso2016/',
                              } ,
 
          'mva_90p_Iso2015':  {
                         'cuts' : { 
                                # Common cuts 
                                'True' :
                                   [
                                     'abs(itree.std_vector_lepton_eta[]) < 2.5' ,
                                     'itree.std_vector_lepton_eleIdHLT[]',
                                     'itree.std_vector_lepton_eleIdMvaWp90[]',
                                     'itree.std_vector_electron_expectedMissingInnerHits[] < 1',
                                   ] ,
                                # Barrel
                                 'abs(itree.std_vector_lepton_eta[]) <= 1.479' :
                                   [
                                     'abs(itree.std_vector_lepton_d0[]) < 0.05' ,
                                     'abs(itree.std_vector_lepton_dz[]) < 0.1'  ,
                                     'relPFIsoRhoCorr < 0.0354',
                                   ] ,
                                 # EndCap
                                 'abs(itree.std_vector_lepton_eta[]) > 1.479' :
                                   [
                                     'abs(itree.std_vector_lepton_d0[]) < 0.1' ,
                                     'abs(itree.std_vector_lepton_dz[]) < 0.2'  ,
                                     'relPFIsoRhoCorr < 0.0646',
                                   ] ,
                                  } ,
                         'tkSF':  { 
                                    '1-7' : 'LatinoAnalysis/Gardener/python/data/idiso/Full2016/egammaEffi.txt_EGM2D.root' ,
                                  } ,
                         'wpSF':  {
                                    '1-7' : 'LatinoAnalysis/Gardener/python/data/idiso/Full2016/electrons_mva_90p_Iso2015.txt' ,
                                  } ,
                         'fakeW' : '/LatinoAnalysis/Gardener/python/data/fake_prompt_rates/80X/lowPtCorrected/36fb_ele_mva_90p_Iso2015/',
                              } ,
 
          'mva_90p_Iso2016':  {
                         'cuts' : { 
                                # Common cuts 
                                'True' :
                                   [
                                     'abs(itree.std_vector_lepton_eta[]) < 2.5' ,
                                     'itree.std_vector_lepton_eleIdHLT[]',
                                     'itree.std_vector_lepton_eleIdMvaWp90[]',
                                     'itree.std_vector_electron_expectedMissingInnerHits[] < 1',
                                   ] ,
                                # Barrel
                                 'abs(itree.std_vector_lepton_eta[]) <= 1.479' :
                                   [
                                     'abs(itree.std_vector_lepton_d0[]) < 0.05' ,
                                     'abs(itree.std_vector_lepton_dz[]) < 0.1'  ,
                                     'relPFIsoRhoCorr < 0.05880',
                                   ] ,
                                 # EndCap
                                 'abs(itree.std_vector_lepton_eta[]) > 1.479' :
                                   [
                                     'abs(itree.std_vector_lepton_d0[]) < 0.1' ,
                                     'abs(itree.std_vector_lepton_dz[]) < 0.2'  ,
                                     'relPFIsoRhoCorr < 0.0571',
                                   ] ,
                                  } ,
                         'tkSF':  { 
                                    '1-7' : 'LatinoAnalysis/Gardener/python/data/idiso/Full2016/egammaEffi.txt_EGM2D.root' ,
                                  } ,
                         'wpSF':  {
                                    '1-7' : 'LatinoAnalysis/Gardener/python/data/idiso/Full2016/electrons_mva_90p_Iso2016.txt' ,
                                  } ,
                         'fakeW' : '/LatinoAnalysis/Gardener/python/data/fake_prompt_rates/80X/lowPtCorrected/36fb_ele_mva_90p_Iso2016/',
                              } ,
 
                  } ,
 
 # ------------ 
 'WgStarObjWP' : {

         'cut_WP_Tight80X' : {
                         'cuts' : { 
                                # Common cuts
                                'True' :
                                  [
                                    'abs(itree.std_vector_lepton_eta[]) < 2.5' ,
                                    #'itree.std_vector_lepton_eleIdHLT[]',
                                    #'itree.std_vector_lepton_eleIdTight[]',
                                    'itree.std_vector_electron_expectedMissingInnerHits[] < 1',
                                    'itree.std_vector_electron_passConversionVeto[]',
                                    'itree.std_vector_electron_tripleChargeAgreement[]',
                                  ] ,
                                # Barrel
                                'abs(itree.std_vector_lepton_eta[]) <= 1.479' :
                                  [
                                    'abs(itree.std_vector_lepton_d0[]) < 0.05' ,
                                    'abs(itree.std_vector_lepton_dz[]) < 0.1'  ,
                                    'itree.std_vector_electron_full5x5_sigmaIetaIeta[] < 0.00998',
                                    'itree.std_vector_electron_dEtaIn[] < 0.00308',
                                    'itree.std_vector_electron_dPhiIn[] < 0.0816',
                                    'itree.std_vector_electron_hOverE[] < 0.0414',
                                    'itree.std_vector_electron_ooEmooP[] < 0.0129',
                                    '(itree.std_vector_lepton_chargedHadronIso[] -pt_to_be_removed_from_overlap + max(itree.std_vector_lepton_neutralHadronIso[]+itree.std_vector_lepton_photonIso[]-itree.jetRho*itree.std_vector_electron_effectiveArea[],0))/itree.std_vector_lepton_pt[] < 0.0588',
                                  ] ,
                                # EndCap
                                'abs(itree.std_vector_lepton_eta[]) > 1.479' :
                                  [
                                    'abs(itree.std_vector_lepton_d0[]) < 0.1' ,
                                    'abs(itree.std_vector_lepton_dz[]) < 0.2'  ,
                                    'itree.std_vector_electron_full5x5_sigmaIetaIeta[] < 0.0292',
                                    'itree.std_vector_electron_dEtaIn[] < 0.00605',
                                    'itree.std_vector_electron_dPhiIn[] < 0.0394',
                                    'itree.std_vector_electron_hOverE[] < 0.0641',
                                    'itree.std_vector_electron_ooEmooP[] < 0.0129',
                                    '(itree.std_vector_lepton_chargedHadronIso[] -pt_to_be_removed_from_overlap + max(itree.std_vector_lepton_neutralHadronIso[]+itree.std_vector_lepton_photonIso[]-itree.jetRho*itree.std_vector_electron_effectiveArea[],0))/itree.std_vector_lepton_pt[] < 0.0571',
                                  ] ,
                                  } ,
                             } ,

                 } ,


}


####################### Muons ######################################

MuonWP    = {}

# --------------------------- Full2016 -----------------------------

MuonWP['Full2016'] = {

 'Variables' : {

        'muonIso' : 'max( itree.std_vector_lepton_photonIso[] + itree.std_vector_lepton_neutralHadronIso[] - 0.5 * itree.std_vector_lepton_sumPUPt[] , 0 )' ,
        'pt_to_be_removed_from_overlap' : 'self.isoConeOverlapRemoval(itree,iLep)'

               }, 

## ------------  
 'VetoObjWP' : { 
      'vetoMuon' : {
                         'cuts' : { 
                                # Common cuts
                                'True' :
                                 [
                                   'abs(itree.std_vector_lepton_eta[]) < 2.4' , 
                                   'itree.std_vector_lepton_pt[] > 10.0' ,
                                 ]
                                  } ,
                   }
               } ,

 # ------------ 
 'FakeObjWP'  : {

      'cut_Tight80x_LooseIso' : {
                         'cuts' : { 
                                # Common cuts
                                'True' :
                                 [
                                   'abs(itree.std_vector_lepton_eta[]) < 2.4' , 
                                   'itree.std_vector_lepton_isTightMuon[] == 1' ,
                                   'abs(itree.std_vector_lepton_dz[]) < 0.1' ,
                                   '(itree.std_vector_lepton_chargedHadronIso[] + muonIso) / itree.std_vector_lepton_pt[] < 0.4',
                                   'itree.std_vector_lepton_trackIso[]/itree.std_vector_lepton_pt[] < 0.4' ,
                                 ] ,
                                 # dxy for pT < 20 GeV
                                 'itree.std_vector_lepton_pt[] <= 20.0' :
                                 [
                                    'abs(itree.std_vector_lepton_d0[]) < 0.01 ' ,
                                 ] ,
                                 # dxy for pT > 20 GeV
                                 'itree.std_vector_lepton_pt[] > 20.0' :
                                 [
                                    'abs(itree.std_vector_lepton_d0[]) < 0.02 ' ,
                                 ] ,
                                  } ,

                       } ,
                 
                 } ,

 # ------------ 
 'TightObjWP' :  {

      'cut_Tight80x' : {
                         'cuts' : { 
                                # Common cuts
                                'True' :
                                 [ 
                                   'abs(itree.std_vector_lepton_eta[]) < 2.4' ,
                                   'itree.std_vector_lepton_isTightMuon[] == 1' ,
                                   'abs(itree.std_vector_lepton_dz[]) < 0.1' ,
                                   '(itree.std_vector_lepton_chargedHadronIso[] + muonIso) / itree.std_vector_lepton_pt[] < 0.15',
                                   'itree.std_vector_lepton_trackIso[]/itree.std_vector_lepton_pt[] < 0.4' ,
                                 ] ,
                                 # dxy for pT < 20 GeV
                                 'itree.std_vector_lepton_pt[] <= 20.0' :
                                 [
                                    'abs(itree.std_vector_lepton_d0[]) < 0.01 ' ,
                                 ] ,
                                 # dxy for pT > 20 GeV
                                 'itree.std_vector_lepton_pt[] > 20.0' :
                                 [
                                    'abs(itree.std_vector_lepton_d0[]) < 0.02 ' ,
                                 ] ,
                                  } ,
                         'tkSF':  { 
                                    '1-4' : 'LatinoAnalysis/Gardener/python/data/idiso/Full2016/trackerSF_Moriond17_MuoPOG_BCDEF.root' ,
                                    '5-7' : 'LatinoAnalysis/Gardener/python/data/idiso/Full2016/trackerSF_Moriond17_MuoPOG_GH.root' ,
                                  } ,
                         'idSF':  {
                                    '1-4' : [ 'LatinoAnalysis/Gardener/python/data/idiso/Full2016/Tight_Run2016BCDEF_PTvsETA_HWW.txt' ,
                                              'LatinoAnalysis/Gardener/python/data/idiso/Full2016/TightID_DY_madgraphLikeRun2016BCDEF_PTvsETA_HWW.txt' ] ,
                                    '5-7' : [ 'LatinoAnalysis/Gardener/python/data/idiso/Full2016/Tight_Run2016GH_PTvsETA_HWW.txt' ,
                                              'LatinoAnalysis/Gardener/python/data/idiso/Full2016/TightID_DY_madgraphLikeRun2016GH_PTvsETA_HWW.txt' ] ,
                                  } ,
                         'isoSF':  {
                                    '1-4' : [ 'LatinoAnalysis/Gardener/python/data/idiso/Full2016/ISOTight_Run2016BCDEF_PTvsETA_HWW.txt' ,
                                              'LatinoAnalysis/Gardener/python/data/idiso/Full2016/ISOTight_DY_madgraphLikeRun2016BCDEF_PTvsETA_HWW.txt' ] ,
                                    '5-7' : [ 'LatinoAnalysis/Gardener/python/data/idiso/Full2016/ISOTight_Run2016GH_PTvsETA_HWW.txt' ,
                                              'LatinoAnalysis/Gardener/python/data/idiso/Full2016/ISOTight_DY_madgraphLikeRun2016GH_PTvsETA_HWW.txt' ] , 
                                  } ,
                         'fakeW' : '/LatinoAnalysis/Gardener/python/data/fake_prompt_rates/80X/lowPtCorrected/36fb_muon/',

                       } ,

                 } ,

 # -------------
 'WgStarObjWP' : {
     'cut_Tight80x' : { 
                         'cuts' : { 
                                # Common cuts
                                'True' :
                                 [
                                   'abs(itree.std_vector_lepton_eta[]) < 2.4' ,
                                   'itree.std_vector_lepton_isTightMuon[] == 1' ,
                                   'abs(itree.std_vector_lepton_dz[]) < 0.1' ,
                                   '(itree.std_vector_lepton_chargedHadronIso[] + muonIso - pt_to_be_removed_from_overlap ) / itree.std_vector_lepton_pt[] < 0.15',
                                   #'itree.std_vector_lepton_trackIso[]/itree.std_vector_lepton_pt[] < 0.4' ,
                                 ] ,
                                 # dxy for pT < 20 GeV
                                 'itree.std_vector_lepton_pt[] <= 20.0' :
                                 [
                                    'abs(itree.std_vector_lepton_d0[]) < 0.01 ' ,
                                 ] ,
                                 # dxy for pT > 20 GeV
                                 'itree.std_vector_lepton_pt[] > 20.0' :
                                 [
                                    'abs(itree.std_vector_lepton_d0[]) < 0.02 ' ,
                                 ] ,
                                  } ,
                       } ,
 
                 }, 

}
