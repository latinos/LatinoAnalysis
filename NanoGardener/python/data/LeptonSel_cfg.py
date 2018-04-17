'''
put this file in LatinoAnalysis/NanoGardener/python/data/
'''

####################### Electrons ##################################

ElectronWP = {

## ------------  

 'VetoObjWP' : { 
           'HLTsafe' : { 
                         'cuts' : { 
                               # Common cuts
                               'True' :
                                [
                                  'False'
                                  #'abs(self.electron_var["Electron_eta"][LF_idx]) < 2.5' ,
                                  #'self.electron_var["Electron_cutBased_HLTPreSel"][LF_idx] == 1 ' ,
                                ] ,             
                                   },
                       } ,
                 } ,
  
 # ------------ 
 'FakeObjWP'  : {

           'HLTsafe' : { 
                         'cuts' : { 
                                # Common cuts
                                'True' :
                                  [
                                   'abs(self.electron_var["Electron_eta"][LF_idx]) < 2.5' ,
                                   'self.electron_var["Electron_cutBased_HLTPreSel"][LF_idx] == 1 ' ,
                                   'ord(self.electron_var["Electron_lostHits"][LF_idx]) < 1',
                                  ] ,             
                                # Barrel
                                'abs(self.electron_var["Electron_eta"][LF_idx]) <= 1.479' :
                                  [
                                    'abs(self.electron_var["Electron_dxy"][LF_idx]) < 0.05' ,
                                    'abs(self.electron_var["Electron_dz"][LF_idx]) < 0.1'  ,
                                  ] ,
                                # EndCap
                                'abs(self.electron_var["Electron_eta"][LF_idx]) > 1.479' :
                                  [
                                    'abs(self.electron_var["Electron_dxy"][LF_idx]) < 0.1' ,
                                    'abs(self.electron_var["Electron_dz"][LF_idx]) < 0.2'  ,
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
                                    'abs(self.electron_var["Electron_eta"][LF_idx]) < 2.5' ,
                                    'self.electron_var["Electron_cutBased_HLTPreSel"][LF_idx] == 1',
                                    'self.electron_var["Electron_cutBased"][LF_idx] == 4', 
                                    'ord(self.electron_var["Electron_lostHits"][LF_idx]) < 1',
                                  ] , 
                                # Barrel
                                'abs(self.electron_var["Electron_eta"][LF_idx]) <= 1.479' :
                                  [
                                    'abs(self.electron_var["Electron_dxy"][LF_idx]) < 0.05' ,
                                    'abs(self.electron_var["Electron_dz"][LF_idx]) < 0.1'  ,
                                  ] ,
                                # EndCap
                                'abs(self.electron_var["Electron_eta"][LF_idx]) > 1.479' :
                                  [
                                    'abs(self.electron_var["Electron_dxy"][LF_idx]) < 0.1' ,
                                    'abs(self.electron_var["Electron_dz"][LF_idx]) < 0.2'  ,
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
                                    'abs(self.electron_var["Electron_eta"][LF_idx]) < 2.5' ,
                                    'self.electron_var["Electron_cutBased_HLTPreSel"][LF_idx] == 1',
                                    'self.electron_var["Electron_cutBased"][LF_idx] == 4',
                                    'ord(self.electron_var["Electron_lostHits"][LF_idx]) < 1',
                                    'self.electron_var["Electron_tightCharge"][LF_idx] == 2',
                                  ] ,
                                # Barrel
                                'abs(self.electron_var["Electron_eta"][LF_idx]) <= 1.479' :
                                  [
                                    'abs(self.electron_var["Electron_dxy"][LF_idx]) < 0.05' ,
                                    'abs(self.electron_var["Electron_dz"][LF_idx]) < 0.1'  ,
                                  ] ,
                                # EndCap
                                'abs(self.electron_var["Electron_eta"][LF_idx]) > 1.479' :
                                  [
                                    'abs(self.electron_var["Electron_dxy"][LF_idx]) < 0.1' ,
                                    'abs(self.electron_var["Electron_dz"][LF_idx]) < 0.2'  ,
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
                                     'abs(self.electron_var["Electron_eta"][LF_idx]) < 2.5' ,
                                     'self.electron_var["Electron_cutBased_HLTPreSel"][LF_idx] == 1',
                                     'self.electron_var["Electron_mvaSpring16GP_WP80"][LF_idx]',
                                     'ord(self.electron_var["Electron_lostHits"][LF_idx]) < 1',
                                   ] ,
                                # Barrel
                                 'abs(self.electron_var["Electron_eta"][LF_idx]) <= 1.479' :
                                   [
                                     'abs(self.electron_var["Electron_dxy"][LF_idx]) < 0.05' ,
                                     'abs(self.electron_var["Electron_dz"][LF_idx]) < 0.1'  ,
                                     'self.electron_var["Electron_pfRelIso03_all"][LF_idx] < 0.0354',
                                   ] ,
                                 # EndCap
                                 'abs(self.electron_var["Electron_eta"][LF_idx]) > 1.479' :
                                   [
                                     'abs(self.electron_var["Electron_dxy"][LF_idx]) < 0.1' ,
                                     'abs(self.electron_var["Electron_dz"][LF_idx]) < 0.2'  ,
                                     'self.electron_var["Electron_pfRelIso03_all"][LF_idx] < 0.0646',
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
                                     'abs(self.electron_var["Electron_eta"][LF_idx]) < 2.5' ,
                                     'self.electron_var["Electron_cutBased_HLTPreSel"][LF_idx] == 1',
                                     'self.electron_var["Electron_mvaSpring16GP_WP80"][LF_idx]',
                                     'ord(self.electron_var["Electron_lostHits"][LF_idx]) < 1',
                                   ] ,
                                # Barrel
                                 'abs(self.electron_var["Electron_eta"][LF_idx]) <= 1.479' :
                                   [
                                     'abs(self.electron_var["Electron_dxy"][LF_idx]) < 0.05' ,
                                     'abs(self.electron_var["Electron_dz"][LF_idx]) < 0.1'  ,
                                     'self.electron_var["Electron_pfRelIso03_all"][LF_idx] < 0.05880',
                                   ] ,
                                 # EndCap
                                 'abs(self.electron_var["Electron_eta"][LF_idx]) > 1.479' :
                                   [
                                     'abs(self.electron_var["Electron_dxy"][LF_idx]) < 0.1' ,
                                     'abs(self.electron_var["Electron_dz"][LF_idx]) < 0.2'  ,
                                     'self.electron_var["Electron_pfRelIso03_all"][LF_idx] < 0.0571',
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
                                     'abs(self.electron_var["Electron_eta"][LF_idx]) < 2.5' ,
                                     'self.electron_var["Electron_cutBased_HLTPreSel"][LF_idx] == 1',
                                     'self.electron_var["Electron_mvaSpring16GP_WP90"][LF_idx]',
                                     'ord(self.electron_var["Electron_lostHits"][LF_idx]) < 1',
                                   ] ,
                                # Barrel
                                 'abs(self.electron_var["Electron_eta"][LF_idx]) <= 1.479' :
                                   [
                                     'abs(self.electron_var["Electron_dxy"][LF_idx]) < 0.05' ,
                                     'abs(self.electron_var["Electron_dz"][LF_idx]) < 0.1'  ,
                                     'self.electron_var["Electron_pfRelIso03_all"][LF_idx] < 0.0354',
                                   ] ,
                                 # EndCap
                                 'abs(self.electron_var["Electron_eta"][LF_idx]) > 1.479' :
                                   [
                                     'abs(self.electron_var["Electron_dxy"][LF_idx]) < 0.1' ,
                                     'abs(self.electron_var["Electron_dz"][LF_idx]) < 0.2'  ,
                                     'self.electron_var["Electron_pfRelIso03_all"][LF_idx] < 0.0646',
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
                                     'abs(self.electron_var["Electron_eta"][LF_idx]) < 2.5' ,
                                     'self.electron_var["Electron_cutBased_HLTPreSel"][LF_idx] == 1',
                                     'self.electron_var["Electron_mvaSpring16GP_WP90"][LF_idx]',
                                     'ord(self.electron_var["Electron_lostHits"][LF_idx]) < 1',
                                   ] ,
                                # Barrel
                                 'abs(self.electron_var["Electron_eta"][LF_idx]) <= 1.479' :
                                   [
                                     'abs(self.electron_var["Electron_dxy"][LF_idx]) < 0.05' ,
                                     'abs(self.electron_var["Electron_dz"][LF_idx]) < 0.1'  ,
                                     'self.electron_var["Electron_pfRelIso03_all"][LF_idx] < 0.05880',
                                   ] ,
                                 # EndCap
                                 'abs(self.electron_var["Electron_eta"][LF_idx]) > 1.479' :
                                   [
                                     'abs(self.electron_var["Electron_dxy"][LF_idx]) < 0.1' ,
                                     'abs(self.electron_var["Electron_dz"][LF_idx]) < 0.2'  ,
                                     'self.electron_var["Electron_pfRelIso03_all"][LF_idx] < 0.0571',
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
                                    'abs(self.electron_var["Electron_eta"][LF_idx]) < 2.5' ,
                                    #'self.electron_var["Electron_cutBased_HLTPreSel"][LF_idx] == 1',
                                    #'self.electron_var["Electron_cutBased"][LF_idx] == 4',
                                    'ord(self.electron_var["Electron_lostHits"][LF_idx]) < 1',
                                    'self.electron_var["Electron_convVeto"][LF_idx]',
                                    'self.electron_var["Electron_tightCharge"][LF_idx] == 2',
                                  ] ,
                                # Barrel
                                'abs(self.electron_var["Electron_eta"][LF_idx]) <= 1.479' :
                                  [
                                    'abs(self.electron_var["Electron_dxy"][LF_idx]) < 0.05' ,
                                    'abs(self.electron_var["Electron_dz"][LF_idx]) < 0.1'  ,
                                    'self.electron_var["Electron_sieie"][LF_idx] < 0.00998',
                                    'self.electron_var["Electron_deltaEtaSC"][LF_idx] < 0.00308',
                                    #'itree.std_vector_electron_dPhiIn"][LF_idx] < 0.0816',
                                    'self.electron_var["Electron_hoe"][LF_idx] < 0.0414',
                                    'self.electron_var["Electron_eInvMinusPInv"][LF_idx] < 0.0129',
                                    '(self.electron_var["Electron_pfRelIso03_all"][LF_idx] - self.ConeOverlapPt(iLep)/self.electron_var["Electron_pt"][LF_idx]) < 0.0588',                                  
                                  ] ,
                                # EndCap
                                'abs(self.electron_var["Electron_eta"][LF_idx]) > 1.479' :
                                  [
                                    'abs(self.electron_var["Electron_dxy"][LF_idx]) < 0.1' ,
                                    'abs(self.electron_var["Electron_dz"][LF_idx]) < 0.2'  ,
                                    'self.electron_var["Electron_sieie"][LF_idx] < 0.0292',
                                    'self.electron_var["Electron_deltaEtaSC"][LF_idx] < 0.00605',
                                    #'itree.std_vector_electron_dPhiIn"][LF_idx] < 0.0394',
                                    'self.electron_var["Electron_hoe"][LF_idx] < 0.0641',
                                    'self.electron_var["Electron_eInvMinusPInv"][LF_idx] < 0.0129',
                                    '(self.electron_var["Electron_pfRelIso03_all"][LF_idx] - self.ConeOverlapPt(iLep)/self.electron_var["Electron_pt"][LF_idx]) < 0.0571', 
                                  ] ,
                                  } ,
                             } ,

                 } ,


}


####################### Muons ######################################

MuonWP = {

## ------------  
 'VetoObjWP' : { 
      'HLTsafe' : {
                         'cuts' : { 
                                # Common cuts
                                'True' :
                                 [
                                   'abs(self.muon_var["Muon_eta"][LF_idx]) < 2.4' , 
                                   'self.muon_var["Muon_pt"][LF_idx] > 10.0' ,
                                 ]
                                  } ,
                   }
               } ,

 # ------------ 
 'FakeObjWP'  : {

      'HLTsafe' : {
                         'cuts' : { 
                                # Common cuts
                                'True' :
                                 [
                                   'abs(self.muon_var["Muon_eta"][LF_idx]) < 2.4' , 
                                   'self.muon_var["Muon_tightId"][LF_idx] == 1' ,
                                   'abs(self.muon_var["Muon_dz"][LF_idx]) < 0.1' ,
                                   'self.muon_var["Muon_pfRelIso04_all"][LF_idx] < 0.4',
                                   #'self.muon_var["Muon_trackIso"][LF_idx]/self.muon_var["Muon_pt"][LF_idx] < 0.4' ,
                                 ] ,
                                 # dxy for pT < 20 GeV
                                 'self.muon_var["Muon_pt"][LF_idx] <= 20.0' :
                                 [
                                    'abs(self.muon_var["Muon_dxy"][LF_idx]) < 0.01 ' ,
                                 ] ,
                                 # dxy for pT > 20 GeV
                                 'self.muon_var["Muon_pt"][LF_idx] > 20.0' :
                                 [
                                    'abs(self.muon_var["Muon_dxy"][LF_idx]) < 0.02 ' ,
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
                                   'abs(self.muon_var["Muon_eta"][LF_idx]) < 2.4' ,
                                   'self.muon_var["Muon_tightId"][LF_idx] == 1' ,
                                   'abs(self.muon_var["Muon_dz"][LF_idx]) < 0.1' ,
                                   'self.muon_var["Muon_pfRelIso04_all"][LF_idx] < 0.15',
                                   #'self.muon_var["Muon_trackIso"][LF_idx]/self.muon_var["Muon_pt"][LF_idx] < 0.4' ,
                                 ] ,
                                 # dxy for pT < 20 GeV
                                 'self.muon_var["Muon_pt"][LF_idx] <= 20.0' :
                                 [
                                    'abs(self.muon_var["Muon_dxy"][LF_idx]) < 0.01 ' ,
                                 ] ,
                                 # dxy for pT > 20 GeV
                                 'self.muon_var["Muon_pt"][LF_idx] > 20.0' :
                                 [
                                    'abs(self.muon_var["Muon_dxy"][LF_idx]) < 0.02 ' ,
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
                                   'abs(self.muon_var["Muon_eta"][LF_idx]) < 2.4' ,
                                   'self.muon_var["Muon_tightId"][LF_idx] == 1' ,
                                   'abs(self.muon_var["Muon_dz"][LF_idx]) < 0.1' ,
                                   '(self.muon_var["Muon_pfRelIso04_all"][LF_idx] - self.ConeOverlapPt(iLep)/self.muon_var["Muon_pt"][LF_idx]) < 0.15',
                                   ##'self.muon_var["Muon_trackIso"][LF_idx]/self.muon_var["Muon_pt"][LF_idx] < 0.4' ,
                                 ] ,
                                 # dxy for pT < 20 GeV
                                 'self.muon_var["Muon_pt"][LF_idx] <= 20.0' :
                                 [
                                    'abs(self.muon_var["Muon_dxy"][LF_idx]) < 0.01 ' ,
                                 ] ,
                                 # dxy for pT > 20 GeV
                                 'self.muon_var["Muon_pt"][LF_idx] > 20.0' :
                                 [
                                    'abs(self.muon_var["Muon_dxy"][LF_idx]) < 0.02 ' ,
                                 ] ,
                                  } ,
                       } ,
 
                 }, 

}



LepFilter_dict = {
   'Loose': 'isLoose',
   'Veto': 'isVeto',
   'WgStar': 'isWgs'
}
