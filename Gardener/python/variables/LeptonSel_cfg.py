

####################### Electrons ##################################

ElectonWP = {}

# --------------------------- 2015  - 74x --------------------------

# --------------------------- 2015  - 76x --------------------------

# --------------------------- ICHEP2016 ----------------------------

# --------------------------- Full2016 -----------------------------

ElectonWP['Full2016'] = {

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
                                    'abs(itree.std_vector_lepton_eta[]) < 2.5' :
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
                                   'itree.std_vector_lepton_chargedHadronIso[] + muonIso) / self.itree.std_vector_lepton_pt[] < 0.4',
                                   'itree.std_vector_lepton_trackIso[]/self.itree.std_vector_lepton_pt[] < 0.4' ,
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
                                   'itree.std_vector_lepton_chargedHadronIso[] + muonIso) / self.itree.std_vector_lepton_pt[] < 0.15',
                                   'itree.std_vector_lepton_trackIso[]/self.itree.std_vector_lepton_pt[] < 0.4' ,
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


