

####################### Electrons ##################################

ElectronWP = {}

# --------------------------- 2015  - 74x --------------------------

# --------------------------- 2015  - 76x --------------------------

# --------------------------- ICHEP2016 ----------------------------

# --------------------------- Full2016 -----------------------------

ElectronWP['Full2016'] = {

 'Variables' : {

        'relPFIsoRhoCorr' : '(itree.std_vector_lepton_chargedHadronIso[] + max(itree.std_vector_lepton_neutralHadronIso[]+itree.std_vector_lepton_photonIso[]-itree.jetRho*itree.std_vector_electron_effectiveArea[],0))/itree.std_vector_lepton_pt[]',

               },

## ------------  
#'LooseObjWP' : { 
#          'HLTsafe' : { 
#                               # Common cuts
#                               'True' :
#                                [
#                                  'abs(itree.std_vector_lepton_eta[]) < 2.5' ,
#                                  'itree.std_vector_lepton_eleIdHLT[] ' ,
#                                ] ,             
#                      } ,
#                } ,
  
 # ------------ 
 'FakeObjWP'  : {

           'HLTsafe' : { 
                                # Common cuts
                                'True' :
                                 [
                                   'abs(itree.std_vector_lepton_eta[]) < 2.5' ,
                                   'itree.std_vector_lepton_eleIdHLT[] ' ,
                                 ] ,             
                       } ,

                 } ,

 # ------------ 
 'TightObjWP' : {

         'cut_WP_Tight80X' : {
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
                                    'itree.std_vector_lepton_d0[] < 0.05' ,
                                    'itree.std_vector_lepton_dz[] < 0.1'  ,
                                  ] ,
                                # EndCap
                                'abs(itree.std_vector_lepton_eta[]) > 1.479' :
                                  [
                                    'itree.std_vector_lepton_d0[] < 0.1' ,
                                    'itree.std_vector_lepton_dz[] < 0.2'  ,
                                  ] ,
                             } ,

         'mva_80p_Iso2015':  {
                               # Common cuts 
                               'True' :
                                  [
                                    'abs(itree.std_vector_lepton_eta[]) < 2.5' ,
                                    'itree.std_vector_lepton_eleIdHLT[]',
                                    'itree.std_vector_lepton_eleIdMvaWp80[]',
                                  ] ,
                               # Barrel
                                'abs(itree.std_vector_lepton_eta[]) <= 1.479' :
                                  [
                                    'itree.std_vector_lepton_d0[] < 0.05' ,
                                    'itree.std_vector_lepton_dz[] < 0.1'  ,
                                    'relPFIsoRhoCorr < 0.0354',
                                  ] ,
                                # EndCap
                                'abs(itree.std_vector_lepton_eta[]) > 1.479' :
                                  [
                                    'itree.std_vector_lepton_d0[] < 0.1' ,
                                    'itree.std_vector_lepton_dz[] < 0.2'  ,
                                    'relPFIsoRhoCorr < 0.0646',
                                  ] ,
                             } ,

         'mva_80p_Iso2016':  {
                               # Common cuts 
                               'True' :
                                  [
                                    'abs(itree.std_vector_lepton_eta[]) < 2.5' ,
                                    'itree.std_vector_lepton_eleIdHLT[]',
                                    'itree.std_vector_lepton_eleIdMvaWp80[]',
                                  ] ,
                               # Barrel
                                'abs(itree.std_vector_lepton_eta[]) <= 1.479' :
                                  [
                                    'itree.std_vector_lepton_d0[] < 0.05' ,
                                    'itree.std_vector_lepton_dz[] < 0.1'  ,
                                    'relPFIsoRhoCorr < 0.05880',
                                  ] ,
                                # EndCap
                                'abs(itree.std_vector_lepton_eta[]) > 1.479' :
                                  [
                                    'itree.std_vector_lepton_d0[] < 0.1' ,
                                    'itree.std_vector_lepton_dz[] < 0.2'  ,
                                    'relPFIsoRhoCorr < 0.0571',
                                  ] ,
                             } ,

         'mva_90p_Iso2015':  {
                               # Common cuts 
                               'True' :
                                  [
                                    'abs(itree.std_vector_lepton_eta[]) < 2.5' ,
                                    'itree.std_vector_lepton_eleIdHLT[]',
                                    'itree.std_vector_lepton_eleIdMvaWp90[]',
                                  ] ,
                               # Barrel
                                'abs(itree.std_vector_lepton_eta[]) <= 1.479' :
                                  [
                                    'itree.std_vector_lepton_d0[] < 0.05' ,
                                    'itree.std_vector_lepton_dz[] < 0.1'  ,
                                    'relPFIsoRhoCorr < 0.0354',
                                  ] ,
                                # EndCap
                                'abs(itree.std_vector_lepton_eta[]) > 1.479' :
                                  [
                                    'itree.std_vector_lepton_d0[] < 0.1' ,
                                    'itree.std_vector_lepton_dz[] < 0.2'  ,
                                    'relPFIsoRhoCorr < 0.0646',
                                  ] ,
                             } ,

         'mva_90p_Iso2016':  {
                               # Common cuts 
                               'True' :
                                  [
                                    'abs(itree.std_vector_lepton_eta[]) < 2.5' ,
                                    'itree.std_vector_lepton_eleIdHLT[]',
                                    'itree.std_vector_lepton_eleIdMvaWp90[]',
                                  ] ,
                               # Barrel
                                'abs(itree.std_vector_lepton_eta[]) <= 1.479' :
                                  [
                                    'itree.std_vector_lepton_d0[] < 0.05' ,
                                    'itree.std_vector_lepton_dz[] < 0.1'  ,
                                    'relPFIsoRhoCorr < 0.05880',
                                  ] ,
                                # EndCap
                                'abs(itree.std_vector_lepton_eta[]) > 1.479' :
                                  [
                                    'itree.std_vector_lepton_d0[] < 0.1' ,
                                    'itree.std_vector_lepton_dz[] < 0.2'  ,
                                    'relPFIsoRhoCorr < 0.0571',
                                  ] ,
                             } ,

                 } 

 # ------------ 
 'WgStarObjWP' : {

         'cut_WP_Tight80X' : {
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
                                    'itree.std_vector_lepton_d0[] < 0.05' ,
                                    'itree.std_vector_lepton_dz[] < 0.1'  ,
                                  ] ,
                                # EndCap
                                'abs(itree.std_vector_lepton_eta[]) > 1.479' :
                                  [
                                    'itree.std_vector_lepton_d0[] < 0.1' ,
                                    'itree.std_vector_lepton_dz[] < 0.2'  ,
                                  ] ,
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
#'LooseObjWP' : { 
#                } ,

 # ------------ 
 'FakeObjWP'  : {

      'cut_Tight80x_LooseIso' : {
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

 # ------------ 
 'TightObjWP' :  {

      'cut_Tight80x' : {
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

                 } ,

 # -------------
 'WgStarObjWP' : {
     'cut_Tight80x' : { 
                                # Common cuts
                                'True' :
                                 [
                                   'abs(itree.std_vector_lepton_eta[]) < 2.4' ,
                                   'itree.std_vector_lepton_isTightMuon[] == 1' ,
                                   'abs(itree.std_vector_lepton_dz[]) < 0.1' ,
                                   '(itree.std_vector_lepton_chargedHadronIso[] + muonIso - pt_to_be_removed_from_overlap ) / itree.std_vector_lepton_pt[] < 0.15',
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
 
                 }, 

}
