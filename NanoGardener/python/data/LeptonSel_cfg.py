LepFilter_dict = {
   'Loose': 'isLoose',
   'Veto': 'isVeto',
   'WgStar': 'isWgs',
   'isLoose': 'FakeObjWP',
   'isVeto': 'VetoObjWP',
   'isWgs': 'WgStarObjWP'
}



####################### Electron WP ##################################

ElectronWP = {  



###____________________Full2018v6__________________________ For nAODv4
'Full2018v6': {


## ------------  

 'VetoObjWP' : { 
           'HLTsafe' : { 
                         'cuts' : { 
                               # Common cuts
                               'True' :
                                [
                                  'False'
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
                                   'abs(electron_col[LF_idx]["eta"]) < 2.5' ,
                                   'electron_col[LF_idx]["cutBased_Fall17_V1"] >= 3',
                                   'electron_col[LF_idx]["convVeto"] == 1',
                                  ] ,             
                                # Barrel
                                'abs(electron_col[LF_idx]["eta"]) <= 1.479' :
                                  [
                                   'abs(electron_col[LF_idx]["dxy"]) < 0.05' ,
                                   'abs(electron_col[LF_idx]["dz"]) < 0.1'  ,
                                  ] ,
                                # EndCap
                                'abs(electron_col[LF_idx]["eta"]) > 1.479' :
                                  [
                                   'electron_col[LF_idx]["sieie"] < 0.03 ' ,                           
                                   'abs(electron_col[LF_idx]["eInvMinusPInv"]) < 0.014' ,
                                   'abs(electron_col[LF_idx]["dxy"]) < 0.1' ,
                                   'abs(electron_col[LF_idx]["dz"]) < 0.2'  ,
                                  ] ,
                                   },
                       } ,

                 } ,
 
# ------------ 
'TightObjWP' : {

          # ----- cut

          'cutFall17V1Iso_Tight' :  {  
                         'cuts' : { 
                                # Common cuts 
                                'True' :
                                   [
                                     'abs(electron_col[LF_idx]["eta"]) < 2.5' ,
                                     'electron_col[LF_idx]["cutBased_Fall17_V1"] >= 4',
                                     'electron_col[LF_idx]["convVeto"] == 1',
                                     'electron_col[LF_idx]["pfRelIso03_all"] < 0.06',
                                   ] ,
                                # Barrel
                                 'abs(electron_col[LF_idx]["eta"]) <= 1.479' :
                                   [
                                     'abs(electron_col[LF_idx]["dxy"]) < 0.05' ,
                                     'abs(electron_col[LF_idx]["dz"]) < 0.1'  ,
                                   ] ,
                                 # EndCap
                                 'abs(electron_col[LF_idx]["eta"]) > 1.479' :
                                   [
                                     'abs(electron_col[LF_idx]["dxy"]) < 0.1' ,
                                     'abs(electron_col[LF_idx]["dz"]) < 0.2'  ,
                                   ] ,
                                  } ,
                         'tkSF':  { 
                                    '1-1' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2018v6/egammaEffi.txt_EGM2D_updatedAll.root',
                                  } ,
                          'wpSF':  {
                                    '1-1' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2018v6/egammaEffi_passingTight102XHWW_runABCD.txt',
                                   } ,
                         # FIXME : Update 2018
                       #  'fakeW' : '/LatinoAnalysis/NanoGardener/python/data/fake_prompt_rates/Full2018v5/mvaFall17V1Iso_WP90/',
                               } ,

          'cutFall17V1Iso_Tight_SS' :  { 
                         'cuts' : {
                                # Common cuts 
                                'True' :
                                   [
                                     'abs(electron_col[LF_idx]["eta"]) < 2.5' ,
                                     'electron_col[LF_idx]["cutBased_Fall17_V1"] >= 4',
                                     'electron_col[LF_idx]["convVeto"] == 1',
                                     'electron_col[LF_idx]["pfRelIso03_all"] < 0.06',
                                     'electron_col[LF_idx]["tightCharge"] == 2',
                                   ] ,
                                # Barrel
                                 'abs(electron_col[LF_idx]["eta"]) <= 1.479' :
                                   [
                                     'abs(electron_col[LF_idx]["dxy"]) < 0.05' ,
                                     'abs(electron_col[LF_idx]["dz"]) < 0.1'  ,
                                   ] ,
                                 # EndCap
                                 'abs(electron_col[LF_idx]["eta"]) > 1.479' :
                                   [
                                     'abs(electron_col[LF_idx]["dxy"]) < 0.1' ,
                                     'abs(electron_col[LF_idx]["dz"]) < 0.2'  ,
                                   ] ,
                                  } ,
                         'tkSF':  {
                                    '1-1' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2018v6/egammaEffi.txt_EGM2D_updatedAll.root',
                                  } ,
                          'wpSF':  {
                                    '1-1' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2018v6/egammaEffi_passingTight102XSSHWW_runABCD.txt',
                                   } ,
                         # FIXME : Update 2018
                       #  'fakeW' : '/LatinoAnalysis/NanoGardener/python/data/fake_prompt_rates/Full2018v5/mvaFall17V1Iso_WP90/',
                               } ,


          # ----- cut V2

          'cutFall17V2Iso_Tight' :  {  
                         'cuts' : { 
                                # Common cuts 
                                'True' :
                                   [
                                     'abs(electron_col[LF_idx]["eta"]) < 2.5' ,
                                     'electron_col[LF_idx]["cutBased"] >= 4',
                                     'electron_col[LF_idx]["convVeto"] == 1',
                                     'electron_col[LF_idx]["pfRelIso03_all"] < 0.06',
                                   ] ,
                                # Barrel
                                 'abs(electron_col[LF_idx]["eta"]) <= 1.479' :
                                   [
                                     'abs(electron_col[LF_idx]["dxy"]) < 0.05' ,
                                     'abs(electron_col[LF_idx]["dz"]) < 0.1'  ,
                                   ] ,
                                 # EndCap
                                 'abs(electron_col[LF_idx]["eta"]) > 1.479' :
                                   [
                                     'abs(electron_col[LF_idx]["dxy"]) < 0.1' ,
                                     'abs(electron_col[LF_idx]["dz"]) < 0.2'  ,
                                   ] ,
                                  } ,
                         'tkSF':  { 
                                    '1-1' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2018v6/egammaEffi.txt_EGM2D_updatedAll.root',
                                  } ,
                         'wpSF':  {
                                    '1-1' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2018v6/egammaEffi_passingTight102XV2HWW_2018runABCD.txt',
                                  } ,
                         # FIXME : Update 2018
                       #  'fakeW' : '/LatinoAnalysis/NanoGardener/python/data/fake_prompt_rates/Full2018v5/mvaFall17V1Iso_WP90/',
                               } ,

          'cutFall17V2Iso_Tight_SS' :  { 
                         'cuts' : {
                                # Common cuts 
                                'True' :
                                   [
                                     'abs(electron_col[LF_idx]["eta"]) < 2.5' ,
                                     'electron_col[LF_idx]["cutBased"] >= 4',
                                     'electron_col[LF_idx]["convVeto"] == 1',
                                     'electron_col[LF_idx]["pfRelIso03_all"] < 0.06',
                                     'electron_col[LF_idx]["tightCharge"] == 2',
                                   ] ,
                                # Barrel
                                 'abs(electron_col[LF_idx]["eta"]) <= 1.479' :
                                   [
                                     'abs(electron_col[LF_idx]["dxy"]) < 0.05' ,
                                     'abs(electron_col[LF_idx]["dz"]) < 0.1'  ,
                                   ] ,
                                 # EndCap
                                 'abs(electron_col[LF_idx]["eta"]) > 1.479' :
                                   [
                                     'abs(electron_col[LF_idx]["dxy"]) < 0.1' ,
                                     'abs(electron_col[LF_idx]["dz"]) < 0.2'  ,
                                   ] ,
                                  } ,
                         'tkSF':  {
                                    '1-1' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2018v6/egammaEffi.txt_EGM2D_updatedAll.root',
                                  } ,
                         'wpSF':  {
                                    '1-1' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2018v6/egammaEffi_passingTight102XV2SSHWW_2018runABCD.txt',
                                  } ,
                         # FIXME : Uddpdate 2018
                       #  'fakeW' : '/LatinoAnalysis/NanoGardener/python/data/fake_prompt_rates/Full2018v5/mvaFall17V1Iso_WP90/',
                               } ,

          # ----- mvaFall17V1Iso

          'mvaFall17V1Iso_WP90':  {
                         'cuts' : { 
                                # Common cuts 
                                'True' :
                                   [
                                     'abs(electron_col[LF_idx]["eta"]) < 2.5' ,
                                     'electron_col[LF_idx]["mvaFall17V1Iso_WP90"]',
                                     'electron_col[LF_idx]["convVeto"] == 1',
                                     'electron_col[LF_idx]["pfRelIso03_all"] < 0.06',
                                   ] ,
                                # Barrel
                                 'abs(electron_col[LF_idx]["eta"]) <= 1.479' :
                                   [
                                     'abs(electron_col[LF_idx]["dxy"]) < 0.05' ,
                                     'abs(electron_col[LF_idx]["dz"]) < 0.1'  ,
                                   ] ,
                                 # EndCap
                                 'abs(electron_col[LF_idx]["eta"]) > 1.479' :
                                   [
                                     'abs(electron_col[LF_idx]["dxy"]) < 0.1' ,
                                     'abs(electron_col[LF_idx]["dz"]) < 0.2'  ,
                                   ] ,
                                  } ,
                         'tkSF':  { 
                                    '1-1' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2018v6/egammaEffi.txt_EGM2D_updatedAll.root',
                                  } ,
                         'wpSF':  {
                                    '1-1' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2018v6/egammaEffi_passingMVA102Xwp90isoHWWiso0p06_2018runABCD.txt',
                                  } ,
                         # FIXME : Update 2018
                         'fakeW' : '/LatinoAnalysis/NanoGardener/python/data/fake_prompt_rates/Full2018v5/mvaFall17V1Iso_WP90/',
                              } ,
 
          'mvaFall17V1Iso_WP90_SS':  {
                         'cuts' : { 
                                # Common cuts 
                                'True' :
                                   [
                                     'abs(electron_col[LF_idx]["eta"]) < 2.5' ,
                                     'electron_col[LF_idx]["mvaFall17V1Iso_WP90"]',
                                     'electron_col[LF_idx]["convVeto"] == 1',
                                     'electron_col[LF_idx]["pfRelIso03_all"] < 0.06', 
                                     'electron_col[LF_idx]["tightCharge"] == 2',
                                   ] ,
                                # Barrel
                                 'abs(electron_col[LF_idx]["eta"]) <= 1.479' :
                                   [
                                     'abs(electron_col[LF_idx]["dxy"]) < 0.05' ,
                                     'abs(electron_col[LF_idx]["dz"]) < 0.1'  ,
                                   ] ,
                                 # EndCap
                                 'abs(electron_col[LF_idx]["eta"]) > 1.479' :
                                   [
                                     'abs(electron_col[LF_idx]["dxy"]) < 0.1' ,
                                     'abs(electron_col[LF_idx]["dz"]) < 0.2'  ,
                                   ] ,
                                  } ,
                         # FIXME : Update 2018 
                         'tkSF':  { 
                                    '1-1' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2018v6/egammaEffi.txt_EGM2D_updatedAll.root',
                                  } ,
                         'wpSF':  {
                                    '1-1' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2018v6/egammaEffi_passingMVA102Xwp90isoSSHWWiso0p06_2018runABCD.txt',
                                  } ,
                         # FIXME update         
                         'fakeW' : '/LatinoAnalysis/NanoGardener/python/data/fake_prompt_rates/Full2018v6/mvaFall17V1Iso_WP90_SS/',
                              } ,


          # ----- mvaFall17V2Iso

          'mvaFall17V2Iso_WP90':  {
                         'cuts' : { 
                                # Common cuts 
                                'True' :
                                   [
                                     'abs(electron_col[LF_idx]["eta"]) < 2.5' ,
                                     'electron_col[LF_idx]["mvaFall17V2Iso_WP90"]',
                                     'electron_col[LF_idx]["convVeto"] == 1',
                                     'electron_col[LF_idx]["pfRelIso03_all"] < 0.06',
                                   ] ,
                                # Barrel
                                 'abs(electron_col[LF_idx]["eta"]) <= 1.479' :
                                   [
                                     'abs(electron_col[LF_idx]["dxy"]) < 0.05' ,
                                     'abs(electron_col[LF_idx]["dz"]) < 0.1'  ,
                                   ] ,
                                 # EndCap
                                 'abs(electron_col[LF_idx]["eta"]) > 1.479' :
                                   [
                                     'abs(electron_col[LF_idx]["dxy"]) < 0.1' ,
                                     'abs(electron_col[LF_idx]["dz"]) < 0.2'  ,
                                   ] ,
                                  } ,
                         # FIXME : Update 2018
                         'tkSF':  { 
                                    '1-1' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2018v6/egammaEffi.txt_EGM2D_updatedAll.root',
                                  } ,
                         'wpSF':  {
                                    '1-1' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2018v6/egammaEffi_passingMVA102Xwp90V2isoHWWiso0p06_2018runABCD.txt',
                                  } ,
                         # FIXME update
                         #'fakeW' : '/LatinoAnalysis/NanoGardener/python/data/fake_prompt_rates/Full2018v5/mvaFall17V2Iso_WP90/',
                         'fakeW' : '/LatinoAnalysis/NanoGardener/python/data/fake_prompt_rates/Full2018CutBased/',
                              } ,
 
          'mvaFall17V2Iso_WP90_SS':  {
                         'cuts' : { 
                                # Common cuts 
                                'True' :
                                   [
                                     'abs(electron_col[LF_idx]["eta"]) < 2.5' ,
                                     'electron_col[LF_idx]["mvaFall17V2Iso_WP90"]',
                                     'electron_col[LF_idx]["convVeto"] == 1',
                                     'electron_col[LF_idx]["pfRelIso03_all"] < 0.06',
                                     'electron_col[LF_idx]["tightCharge"] == 2',
                                   ] ,
                                # Barrel
                                 'abs(electron_col[LF_idx]["eta"]) <= 1.479' :
                                   [
                                     'abs(electron_col[LF_idx]["dxy"]) < 0.05' ,
                                     'abs(electron_col[LF_idx]["dz"]) < 0.1'  ,
                                   ] ,
                                 # EndCap
                                 'abs(electron_col[LF_idx]["eta"]) > 1.479' :
                                   [
                                     'abs(electron_col[LF_idx]["dxy"]) < 0.1' ,
                                     'abs(electron_col[LF_idx]["dz"]) < 0.2'  ,
                                   ] ,
                                  } ,
                         # FIXME : Update 2018 
                         'tkSF':  { 
                                    '1-1' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2018v6/egammaEffi.txt_EGM2D_updatedAll.root',
                                  } ,
                         'wpSF':  {
                                    '1-1' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2018v6/egammaEffi_passingMVA102Xwp90V2isoSSHWWiso0p06_2018runABCD.txt',
                                  } ,
                         # FIXME update         
                         'fakeW' : '/LatinoAnalysis/NanoGardener/python/data/fake_prompt_rates/Full2018v5/mvaFall17V2Iso_WP90_SS/',
                              } ,

             },

 # ------------ 
 'WgStarObjWP' : {

         'mvaFall17V1Iso_WP90' : {
                         'cuts' : { 
                                # Common cuts
                                'True' :
                                  [
                                     'abs(electron_col[LF_idx]["eta"]) < 2.5' ,
                                     'electron_col[LF_idx]["cutBased_Fall17_V1"] >= 3',
                                     'electron_col[LF_idx]["mvaFall17V1noIso_WP90"]',
                                     'electron_col[LF_idx]["convVeto"] == 1',
                                  ] ,
                                # Barrel
                                'abs(electron_col[LF_idx]["eta"]) <= 1.479' :
                                  [
                                     'abs(electron_col[LF_idx]["dxy"]) < 0.05' ,
                                     'abs(electron_col[LF_idx]["dz"]) < 0.1'  ,
                                  ] ,
                                # EndCap
                                'abs(electron_col[LF_idx]["eta"]) > 1.479' :
                                  [
                                    'electron_col[LF_idx]["sieie"] < 0.03 ' ,                           
                                    'abs(electron_col[LF_idx]["eInvMinusPInv"]) < 0.014' ,
                                    'abs(electron_col[LF_idx]["dxy"]) < 0.1' ,
                                    'abs(electron_col[LF_idx]["dz"]) < 0.2'  ,
                                  ] ,
                                  } ,
                         'cuts_iso': {
                                # Common cuts
                                'True' :
                                [
                                  '0.06',
                                ],
                                # Barrel
                                'abs(electron_col[LF_idx]["eta"]) <= 1.479' :
                                [
                                  'None' 
                                ],
                                # EndCap
                                'abs(electron_col[LF_idx]["eta"]) > 1.479' :
                                [
                                  'None' 
                                ],
                                  },
                         'iso': ['pfRelIso03_all', 0.3],
                         # FIXME: Update for 2018
                         'tkSF':  {
                                    '1-1' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2018v5/egammaEffi.txt_EGM2D_updatedAll.root',
                                  } ,
                         'wpSF':  {
                                    '1-1' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2018v5/egammaEffi_passingMVA102Xwp90isoSSHWWiso0p06_2018runABCD.txt',
                                  } ,
                             } ,

                 } ,

},

###____________________Full2018v5__________________________ For nAODv4
'Full2018v5': {


## ------------  

 'VetoObjWP' : { 
           'HLTsafe' : { 
                         'cuts' : { 
                               # Common cuts
                               'True' :
                                [
                                  'False'
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
                                   'abs(electron_col[LF_idx]["eta"]) < 2.5' ,
                                   'electron_col[LF_idx]["cutBased_Fall17_V1"] >= 3',
                                   'electron_col[LF_idx]["convVeto"] == 1',
                                  ] ,             
                                # Barrel
                                'abs(electron_col[LF_idx]["eta"]) <= 1.479' :
                                  [
                                   'abs(electron_col[LF_idx]["dxy"]) < 0.05' ,
                                   'abs(electron_col[LF_idx]["dz"]) < 0.1'  ,
                                  ] ,
                                # EndCap
                                'abs(electron_col[LF_idx]["eta"]) > 1.479' :
                                  [
                                   'electron_col[LF_idx]["sieie"] < 0.03 ' ,                           
                                   'abs(electron_col[LF_idx]["eInvMinusPInv"]) < 0.014' ,
                                   'abs(electron_col[LF_idx]["dxy"]) < 0.1' ,
                                   'abs(electron_col[LF_idx]["dz"]) < 0.2'  ,
                                  ] ,
                                   },
                       } ,

                 } ,
 
# ------------ 
'TightObjWP' : {

          # ----- mvaFall17V1Iso

          'mvaFall17V1Iso_WP90':  {
                         'cuts' : { 
                                # Common cuts 
                                'True' :
                                   [
                                     'abs(electron_col[LF_idx]["eta"]) < 2.5' ,
                                     'electron_col[LF_idx]["mvaFall17V1Iso_WP90"]',
                                     'electron_col[LF_idx]["convVeto"] == 1',
                                     'electron_col[LF_idx]["pfRelIso03_all"] < 0.06',
                                   ] ,
                                # Barrel
                                 'abs(electron_col[LF_idx]["eta"]) <= 1.479' :
                                   [
                                     'abs(electron_col[LF_idx]["dxy"]) < 0.05' ,
                                     'abs(electron_col[LF_idx]["dz"]) < 0.1'  ,
                                   ] ,
                                 # EndCap
                                 'abs(electron_col[LF_idx]["eta"]) > 1.479' :
                                   [
                                     'abs(electron_col[LF_idx]["dxy"]) < 0.1' ,
                                     'abs(electron_col[LF_idx]["dz"]) < 0.2'  ,
                                   ] ,
                                  } ,
                         # FIXME : Update 2018
                         'tkSF':  { 
                                    '1-1' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2018v5/egammaEffi.txt_EGM2D_updatedAll.root',
                                  } ,
                         'wpSF':  {
                                    '1-1' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2018v5/egammaEffi_passingMVA102Xwp90isoHWWiso0p06_2018runABCD.txt' ,
                                  } ,
                         'fakeW' : '/LatinoAnalysis/NanoGardener/python/data/fake_prompt_rates/Full2018v5/mvaFall17V1Iso_WP90/',
                              } ,
 
          'mvaFall17V1Iso_WP90_SS':  {
                         'cuts' : { 
                                # Common cuts 
                                'True' :
                                   [
                                     'abs(electron_col[LF_idx]["eta"]) < 2.5' ,
                                     'electron_col[LF_idx]["mvaFall17V1Iso_WP90"]',
                                     'electron_col[LF_idx]["convVeto"] == 1',
                                     'electron_col[LF_idx]["pfRelIso03_all"] < 0.06', 
                                     'electron_col[LF_idx]["tightCharge"] == 2',
                                   ] ,
                                # Barrel
                                 'abs(electron_col[LF_idx]["eta"]) <= 1.479' :
                                   [
                                     'abs(electron_col[LF_idx]["dxy"]) < 0.05' ,
                                     'abs(electron_col[LF_idx]["dz"]) < 0.1'  ,
                                   ] ,
                                 # EndCap
                                 'abs(electron_col[LF_idx]["eta"]) > 1.479' :
                                   [
                                     'abs(electron_col[LF_idx]["dxy"]) < 0.1' ,
                                     'abs(electron_col[LF_idx]["dz"]) < 0.2'  ,
                                   ] ,
                                  } ,
                         # FIXME : Update 2018 
                         'tkSF':  { 
                                    '1-1' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2018v5/egammaEffi.txt_EGM2D_updatedAll.root',
                                  } ,
                         'wpSF':  {
                                    '1-1' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2018v5/egammaEffi_passingMVA102Xwp90isoSSHWWiso0p06_2018runABCD.txt',
                                  } ,
                         # FIXME update         
                         'fakeW' : '/LatinoAnalysis/NanoGardener/python/data/fake_prompt_rates/Full2018v5/mvaFall17V1Iso_WP90_SS/',
                              } ,


          # ----- mvaFall17V2Iso

          'mvaFall17V2Iso_WP90':  {
                         'cuts' : { 
                                # Common cuts 
                                'True' :
                                   [
                                     'abs(electron_col[LF_idx]["eta"]) < 2.5' ,
                                     'electron_col[LF_idx]["mvaFall17V2Iso_WP90"]',
                                     'electron_col[LF_idx]["convVeto"] == 1',
                                     'electron_col[LF_idx]["pfRelIso03_all"] < 0.06',
                                   ] ,
                                # Barrel
                                 'abs(electron_col[LF_idx]["eta"]) <= 1.479' :
                                   [
                                     'abs(electron_col[LF_idx]["dxy"]) < 0.05' ,
                                     'abs(electron_col[LF_idx]["dz"]) < 0.1'  ,
                                   ] ,
                                 # EndCap
                                 'abs(electron_col[LF_idx]["eta"]) > 1.479' :
                                   [
                                     'abs(electron_col[LF_idx]["dxy"]) < 0.1' ,
                                     'abs(electron_col[LF_idx]["dz"]) < 0.2'  ,
                                   ] ,
                                  } ,
                         # FIXME : Update 2018
                         'tkSF':  { 
                                    '1-1' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2018v5/egammaEffi.txt_EGM2D_updatedAll.root',
                                  } ,
                         'wpSF':  {
                                    '1-1' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2018v5/egammaEffi_passingMVA102Xwp90isoHWWiso0p06_2018runABCD.txt' ,
                                  } ,
                         # FIXME update
                         #'fakeW' : '/LatinoAnalysis/NanoGardener/python/data/fake_prompt_rates/Full2018v5/mvaFall17V2Iso_WP90/',
                         'fakeW' : '/LatinoAnalysis/NanoGardener/python/data/fake_prompt_rates/Full2018CutBased/',
                              } ,
 
          'mvaFall17V2Iso_WP90_SS':  {
                         'cuts' : { 
                                # Common cuts 
                                'True' :
                                   [
                                     'abs(electron_col[LF_idx]["eta"]) < 2.5' ,
                                     'electron_col[LF_idx]["mvaFall17V2Iso_WP90"]',
                                     'electron_col[LF_idx]["convVeto"] == 1',
                                     'electron_col[LF_idx]["pfRelIso03_all"] < 0.06',
                                     'electron_col[LF_idx]["tightCharge"] == 2',
                                   ] ,
                                # Barrel
                                 'abs(electron_col[LF_idx]["eta"]) <= 1.479' :
                                   [
                                     'abs(electron_col[LF_idx]["dxy"]) < 0.05' ,
                                     'abs(electron_col[LF_idx]["dz"]) < 0.1'  ,
                                   ] ,
                                 # EndCap
                                 'abs(electron_col[LF_idx]["eta"]) > 1.479' :
                                   [
                                     'abs(electron_col[LF_idx]["dxy"]) < 0.1' ,
                                     'abs(electron_col[LF_idx]["dz"]) < 0.2'  ,
                                   ] ,
                                  } ,
                         # FIXME : Update 2018 
                         'tkSF':  { 
                                    '1-1' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2018v5/egammaEffi.txt_EGM2D_updatedAll.root',
                                  } ,
                         'wpSF':  {
                                    '1-1' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2018v5/egammaEffi_passingMVA102Xwp90isoSSHWWiso0p06_2018runABCD.txt',
                                  } ,
                         # FIXME update         
                         'fakeW' : '/LatinoAnalysis/NanoGardener/python/data/fake_prompt_rates/Full2018v5/mvaFall17V2Iso_WP90_SS/',
                              } ,

             },

 # ------------ 
 'WgStarObjWP' : {

         'mvaFall17V1Iso_WP90' : {
                         'cuts' : { 
                                # Common cuts
                                'True' :
                                  [
                                     'abs(electron_col[LF_idx]["eta"]) < 2.5' ,
                                     'electron_col[LF_idx]["cutBased_Fall17_V1"] >= 3',
                                     'electron_col[LF_idx]["mvaFall17V1noIso_WP90"]',
                                     'electron_col[LF_idx]["convVeto"] == 1',
                                  ] ,
                                # Barrel
                                'abs(electron_col[LF_idx]["eta"]) <= 1.479' :
                                  [
                                     'abs(electron_col[LF_idx]["dxy"]) < 0.05' ,
                                     'abs(electron_col[LF_idx]["dz"]) < 0.1'  ,
                                  ] ,
                                # EndCap
                                'abs(electron_col[LF_idx]["eta"]) > 1.479' :
                                  [
                                    'electron_col[LF_idx]["sieie"] < 0.03 ' ,                           
                                    'abs(electron_col[LF_idx]["eInvMinusPInv"]) < 0.014' ,
                                    'abs(electron_col[LF_idx]["dxy"]) < 0.1' ,
                                    'abs(electron_col[LF_idx]["dz"]) < 0.2'  ,
                                  ] ,
                                  } ,
                         'cuts_iso': {
                                # Common cuts
                                'True' :
                                [
                                  '0.06',
                                ],
                                # Barrel
                                'abs(electron_col[LF_idx]["eta"]) <= 1.479' :
                                [
                                  'None' 
                                ],
                                # EndCap
                                'abs(electron_col[LF_idx]["eta"]) > 1.479' :
                                [
                                  'None' 
                                ],
                                  },
                         'iso': ['pfRelIso03_all', 0.3],
                         # FIXME: Update for 2018
                         'tkSF':  {
                                    '1-1' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2018v5/egammaEffi.txt_EGM2D_updatedAll.root',
                                  } ,
                         'wpSF':  {
                                    '1-1' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2018v5/egammaEffi_passingMVA102Xwp90isoSSHWWiso0p06_2018runABCD.txt',
                                  } ,
                             } ,

                 } ,

},


###____________________Full2018v4__________________________ For nAODv4
'Full2018v4': {


## ------------  

 'VetoObjWP' : { 
           'HLTsafe' : { 
                         'cuts' : { 
                               # Common cuts
                               'True' :
                                [
                                  'False'
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
                                   'abs(electron_col[LF_idx]["eta"]) < 2.5' ,
                                   'electron_col[LF_idx]["cutBased_Fall17_V1"] >= 1',
                                  ] ,             
                                # Barrel
                                'abs(electron_col[LF_idx]["eta"]) <= 1.479' :
                                  [
                                   'abs(electron_col[LF_idx]["dxy"]) < 0.05' ,
                                   'abs(electron_col[LF_idx]["dz"]) < 0.1'  ,
                                  ] ,
                                # EndCap
                                'abs(electron_col[LF_idx]["eta"]) > 1.479' :
                                  [
                                   'electron_col[LF_idx]["sieie"] < 0.03 ' ,                           
                                   'abs(electron_col[LF_idx]["eInvMinusPInv"]) < 0.014' ,
                                   'abs(electron_col[LF_idx]["dxy"]) < 0.1' ,
                                   'abs(electron_col[LF_idx]["dz"]) < 0.2'  ,
                                  ] ,
                                   },
                       } ,

                 } ,
 
# ------------ 
'TightObjWP' : {

          # ----- mvaFall17V1Iso

          'mvaFall17V1Iso_WP90':  {
                         'cuts' : { 
                                # Common cuts 
                                'True' :
                                   [
                                     'abs(electron_col[LF_idx]["eta"]) < 2.5' ,
                                     'electron_col[LF_idx]["mvaFall17V1Iso_WP90"]',
                                     'electron_col[LF_idx]["convVeto"] == 1',
                                   ] ,
                                # Barrel
                                 'abs(electron_col[LF_idx]["eta"]) <= 1.479' :
                                   [
                                     'abs(electron_col[LF_idx]["dxy"]) < 0.05' ,
                                     'abs(electron_col[LF_idx]["dz"]) < 0.1'  ,
                                   ] ,
                                 # EndCap
                                 'abs(electron_col[LF_idx]["eta"]) > 1.479' :
                                   [
                                     'abs(electron_col[LF_idx]["dxy"]) < 0.1' ,
                                     'abs(electron_col[LF_idx]["dz"]) < 0.2'  ,
                                   ] ,
                                  } ,
                         # FIXME : Update 2018
                         'tkSF':  { 
                                    '1-1' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2018/egammaEffi.txt_EGM2D_updatedAll.root',
                                  } ,
                         'wpSF':  {
                                    '1-1' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2018/egammaEffi_passingMVA102Xwp90isoHWW_runABCD.txt' ,
                                  } ,
                         'fakeW' : '/LatinoAnalysis/NanoGardener/python/data/fake_prompt_rates/Full2018/',
                              } ,
 
          'mvaFall17V1Iso_WP90_SS':  {
                         'cuts' : { 
                                # Common cuts 
                                'True' :
                                   [
                                     'abs(electron_col[LF_idx]["eta"]) < 2.5' ,
                                     'electron_col[LF_idx]["mvaFall17V1Iso_WP90"]',
                                     'electron_col[LF_idx]["convVeto"] == 1',
                                     'electron_col[LF_idx]["tightCharge"] == 2',
                                   ] ,
                                # Barrel
                                 'abs(electron_col[LF_idx]["eta"]) <= 1.479' :
                                   [
                                     'abs(electron_col[LF_idx]["dxy"]) < 0.05' ,
                                     'abs(electron_col[LF_idx]["dz"]) < 0.1'  ,
                                   ] ,
                                 # EndCap
                                 'abs(electron_col[LF_idx]["eta"]) > 1.479' :
                                   [
                                     'abs(electron_col[LF_idx]["dxy"]) < 0.1' ,
                                     'abs(electron_col[LF_idx]["dz"]) < 0.2'  ,
                                   ] ,
                                  } ,
                         # FIXME : Update 2018 
                         'tkSF':  { 
                                    '1-1' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2018/egammaEffi.txt_EGM2D_updatedAll.root',
                                  } ,
                         'wpSF':  {
                                    '1-1' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2018/egammaEffi_passingMVA102Xwp90isoSSHWW_runABCD.txt',
                                  } ,
                         # FIXME update         
                         'fakeW' : '/LatinoAnalysis/NanoGardener/python/data/fake_prompt_rates/Full2018/',
                              } ,


          # ----- mvaFall17V2Iso

          'mvaFall17V2Iso_WP90':  {
                         'cuts' : { 
                                # Common cuts 
                                'True' :
                                   [
                                     'abs(electron_col[LF_idx]["eta"]) < 2.5' ,
                                     'electron_col[LF_idx]["mvaFall17V2Iso_WP90"]',
                                     'electron_col[LF_idx]["convVeto"] == 1',
                                   ] ,
                                # Barrel
                                 'abs(electron_col[LF_idx]["eta"]) <= 1.479' :
                                   [
                                     'abs(electron_col[LF_idx]["dxy"]) < 0.05' ,
                                     'abs(electron_col[LF_idx]["dz"]) < 0.1'  ,
                                   ] ,
                                 # EndCap
                                 'abs(electron_col[LF_idx]["eta"]) > 1.479' :
                                   [
                                     'abs(electron_col[LF_idx]["dxy"]) < 0.1' ,
                                     'abs(electron_col[LF_idx]["dz"]) < 0.2'  ,
                                   ] ,
                                  } ,
                         # FIXME : Update 2018
                         'tkSF':  { 
                                    '1-1' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2018/egammaEffi.txt_EGM2D_updatedAll.root',
                                  } ,
                         'wpSF':  {
                                    '1-1' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2018/egammaEffi_passingMVA102Xwp90isoHWW_runABCD.txt' ,
                                  } ,
                         # FIXME update
                         'fakeW' : '/LatinoAnalysis/NanoGardener/python/data/fake_prompt_rates/Full2018/',
                              } ,
 
          'mvaFall17V2Iso_WP90_SS':  {
                         'cuts' : { 
                                # Common cuts 
                                'True' :
                                   [
                                     'abs(electron_col[LF_idx]["eta"]) < 2.5' ,
                                     'electron_col[LF_idx]["mvaFall17V2Iso_WP90"]',
                                     'electron_col[LF_idx]["convVeto"] == 1',
                                     'electron_col[LF_idx]["tightCharge"] == 2',
                                   ] ,
                                # Barrel
                                 'abs(electron_col[LF_idx]["eta"]) <= 1.479' :
                                   [
                                     'abs(electron_col[LF_idx]["dxy"]) < 0.05' ,
                                     'abs(electron_col[LF_idx]["dz"]) < 0.1'  ,
                                   ] ,
                                 # EndCap
                                 'abs(electron_col[LF_idx]["eta"]) > 1.479' :
                                   [
                                     'abs(electron_col[LF_idx]["dxy"]) < 0.1' ,
                                     'abs(electron_col[LF_idx]["dz"]) < 0.2'  ,
                                   ] ,
                                  } ,
                         # FIXME : Update 2018 
                         'tkSF':  { 
                                    '1-1' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2018/egammaEffi.txt_EGM2D_updatedAll.root',
                                  } ,
                         'wpSF':  {
                                    '1-1' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2018/egammaEffi_passingMVA102Xwp90isoHWW_runABCD.txt',
                                  } ,
                         # FIXME update         
                         'fakeW' : '/LatinoAnalysis/NanoGardener/python/data/fake_prompt_rates/Full2018/',
                              } ,

             },

 # ------------ 
 'WgStarObjWP' : {

         'mvaFall17V1Iso_WP90' : {
                         'cuts' : { 
                                # Common cuts
                                'True' :
                                  [
                                     'abs(electron_col[LF_idx]["eta"]) < 2.5' ,
                                     'electron_col[LF_idx]["mvaFall17V1noIso_WP90"]',
                                     'electron_col[LF_idx]["convVeto"] == 1',
                                  ] ,
                                # Barrel
                                'abs(electron_col[LF_idx]["eta"]) <= 1.479' :
                                  [
                                     'abs(electron_col[LF_idx]["dxy"]) < 0.05' ,
                                     'abs(electron_col[LF_idx]["dz"]) < 0.1'  ,
                                  ] ,
                                # EndCap
                                'abs(electron_col[LF_idx]["eta"]) > 1.479' :
                                  [
                                     'abs(electron_col[LF_idx]["dxy"]) < 0.1' ,
                                     'abs(electron_col[LF_idx]["dz"]) < 0.2'  ,
                                  ] ,
                                  } ,
                         'cuts_iso': {
                                # Common cuts
                                'True' :
                                [
                                  'None',
                                ],
                                # Barrel
                                'abs(electron_col[LF_idx]["eta"]) <= 1.479' :
                                [
                                  '0.25' 
                                ],
                                # EndCap
                                'abs(electron_col[LF_idx]["eta"]) > 1.479' :
                                [
                                  '0.2' 
                                ],
                                  },
                         'iso': ['pfRelIso03_all', 0.3],
                         # FIXME: Update for 2018
                         'tkSF':  {
                                    '1-1' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2018/egammaEffi.txt_EGM2D_updatedAll.root',
                                  } ,
                         'wpSF':  {
                                    '1-1' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2018/egammaEffi_passingMVA102Xwp90isoHWW_runABCD.txt' ,
                                  } ,
                             } ,

                 } ,

},



###____________________Full2018__________________________
'Full2018': {


## ------------  

 'VetoObjWP' : { 
           'HLTsafe' : { 
                         'cuts' : { 
                               # Common cuts
                               'True' :
                                [
                                  'False'
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
                                   'abs(electron_col[LF_idx]["eta"]) < 2.5' ,
                                   'electron_col[LF_idx]["cutBased"] >= 1',
                                  ] ,             
                                # Barrel
                                'abs(electron_col[LF_idx]["eta"]) <= 1.479' :
                                  [
                                   'abs(electron_col[LF_idx]["dxy"]) < 0.05' ,
                                   'abs(electron_col[LF_idx]["dz"]) < 0.1'  ,
                                  ] ,
                                # EndCap
                                'abs(electron_col[LF_idx]["eta"]) > 1.479' :
                                  [
                                   'electron_col[LF_idx]["sieie"] < 0.03 ' ,                           
                                   'abs(electron_col[LF_idx]["eInvMinusPInv"]) < 0.014' ,
                                   'abs(electron_col[LF_idx]["dxy"]) < 0.1' ,
                                   'abs(electron_col[LF_idx]["dz"]) < 0.2'  ,
                                  ] ,
                                   },
                       } ,

                 } ,
 
# ------------ 
'TightObjWP' : {

          'mvaFall17Iso_WP90':  {
                         'cuts' : { 
                                # Common cuts 
                                'True' :
                                   [
                                     'abs(electron_col[LF_idx]["eta"]) < 2.5' ,
                                     'electron_col[LF_idx]["mvaFall17V1Iso_WP90"]',
                                     'electron_col[LF_idx]["convVeto"] == 1',
                                   ] ,
                                # Barrel
                                 'abs(electron_col[LF_idx]["eta"]) <= 1.479' :
                                   [
                                     'abs(electron_col[LF_idx]["dxy"]) < 0.05' ,
                                     'abs(electron_col[LF_idx]["dz"]) < 0.1'  ,
                                   ] ,
                                 # EndCap
                                 'abs(electron_col[LF_idx]["eta"]) > 1.479' :
                                   [
                                     'abs(electron_col[LF_idx]["dxy"]) < 0.1' ,
                                     'abs(electron_col[LF_idx]["dz"]) < 0.2'  ,
                                   ] ,
                                  } ,
                         # FIXME : Update 2018
                         'tkSF':  { 
                                    '1-1' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/egammaEffi.txt_EGM2D_runB_passingRECO_combineLowEt.root',
                                  } ,
                         'wpSF':  {
                                    '1-1' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/egammaEffi_passingMVA94Xwp90isoHWW_runB.txt' ,
                                  } ,
                         'fakeW' : '/LatinoAnalysis/NanoGardener/python/data/fake_prompt_rates/Full2017/',
                              } ,
 
          'mvaFall17Iso_WP90_SS':  {
                         'cuts' : { 
                                # Common cuts 
                                'True' :
                                   [
                                     'abs(electron_col[LF_idx]["eta"]) < 2.5' ,
                                     'electron_col[LF_idx]["mvaFall17V1Iso_WP90"]',
                                     'electron_col[LF_idx]["convVeto"] == 1',
                                     'electron_col[LF_idx]["tightCharge"] == 2',
                                   ] ,
                                # Barrel
                                 'abs(electron_col[LF_idx]["eta"]) <= 1.479' :
                                   [
                                     'abs(electron_col[LF_idx]["dxy"]) < 0.05' ,
                                     'abs(electron_col[LF_idx]["dz"]) < 0.1'  ,
                                   ] ,
                                 # EndCap
                                 'abs(electron_col[LF_idx]["eta"]) > 1.479' :
                                   [
                                     'abs(electron_col[LF_idx]["dxy"]) < 0.1' ,
                                     'abs(electron_col[LF_idx]["dz"]) < 0.2'  ,
                                   ] ,
                                  } ,
                         # FIXME : Update 2018 
                         'tkSF':  { 
                                    '1-1' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/egammaEffi.txt_EGM2D_runB_passingRECO_combineLowEt.root',
                                  } ,
                         'wpSF':  {
                                    '1-1' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/egammaEffi_passingMVA94Xwp90isoSSHWW_runB.txt',
                                  } ,
                         'fakeW' : '/LatinoAnalysis/NanoGardener/python/data/fake_prompt_rates/Full2017/',
                              } ,

             },

 # ------------ 
 'WgStarObjWP' : {

         'mvaFall17Iso_WP90' : {
                         'cuts' : { 
                                # Common cuts
                                'True' :
                                  [
                                     'abs(electron_col[LF_idx]["eta"]) < 2.5' ,
                                     'electron_col[LF_idx]["mvaFall17noIso_WP90"]',
                                     'electron_col[LF_idx]["convVeto"] == 1',
                                  ] ,
                                # Barrel
                                'abs(electron_col[LF_idx]["eta"]) <= 1.479' :
                                  [
                                     'abs(electron_col[LF_idx]["dxy"]) < 0.05' ,
                                     'abs(electron_col[LF_idx]["dz"]) < 0.1'  ,
                                  ] ,
                                # EndCap
                                'abs(electron_col[LF_idx]["eta"]) > 1.479' :
                                  [
                                     'abs(electron_col[LF_idx]["dxy"]) < 0.1' ,
                                     'abs(electron_col[LF_idx]["dz"]) < 0.2'  ,
                                  ] ,
                                  } ,
                         'cuts_iso': {
                                # Common cuts
                                'True' :
                                [
                                  'None',
                                ],
                                # Barrel
                                'abs(electron_col[LF_idx]["eta"]) <= 1.479' :
                                [
                                  '0.25' 
                                ],
                                # EndCap
                                'abs(electron_col[LF_idx]["eta"]) > 1.479' :
                                [
                                  '0.2' 
                                ],
                                  },
                         'iso': ['pfRelIso03_all', 0.3],
                         # FIXME: Update for 2018
                         'tkSF':  {
                                    '1-1' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/egammaEffi.txt_EGM2D_runB_passingRECO_combineLowEt.root',
                                  } ,
                         'wpSF':  {
                                    '1-1' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/egammaEffi_passingMVA94Xwp90isoHWW_runB.txt' ,
                                  } ,
                             } ,

                 } ,

},


###____________________Full2017v4__________________________
'Full2017v4': {


## ------------  

 'VetoObjWP' : { 
           'HLTsafe' : { 
                         'cuts' : { 
                               # Common cuts
                               'True' :
                                [
                                  'False'
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
                                   'abs(electron_col[LF_idx]["eta"]) < 2.5' ,
                                   'electron_col[LF_idx]["cutBased_Fall17_V1"] >= 1',
                                  ] ,             
                                # Barrel
                                'abs(electron_col[LF_idx]["eta"]) <= 1.479' :
                                  [
                                   'abs(electron_col[LF_idx]["dxy"]) < 0.05' ,
                                   'abs(electron_col[LF_idx]["dz"]) < 0.1'  ,
                                  ] ,
                                # EndCap
                                'abs(electron_col[LF_idx]["eta"]) > 1.479' :
                                  [
                                   'electron_col[LF_idx]["sieie"] < 0.03 ' ,                           
                                   'abs(electron_col[LF_idx]["eInvMinusPInv"]) < 0.014' ,
                                   'abs(electron_col[LF_idx]["dxy"]) < 0.1' ,
                                   'abs(electron_col[LF_idx]["dz"]) < 0.2'  ,
                                  ] ,
                                   },
                       } ,

                 } ,
 
# ------------ 
'TightObjWP' : {

          # ----- mvaFall17V1Iso

          'mvaFall17V1Iso_WP90':  {
                         'cuts' : { 
                                # Common cuts 
                                'True' :
                                   [
                                     'abs(electron_col[LF_idx]["eta"]) < 2.5' ,
                                     'electron_col[LF_idx]["mvaFall17V1Iso_WP90"]',
                                     'electron_col[LF_idx]["convVeto"] == 1',
                                   ] ,
                                # Barrel
                                 'abs(electron_col[LF_idx]["eta"]) <= 1.479' :
                                   [
                                     'abs(electron_col[LF_idx]["dxy"]) < 0.05' ,
                                     'abs(electron_col[LF_idx]["dz"]) < 0.1'  ,
                                   ] ,
                                 # EndCap
                                 'abs(electron_col[LF_idx]["eta"]) > 1.479' :
                                   [
                                     'abs(electron_col[LF_idx]["dxy"]) < 0.1' ,
                                     'abs(electron_col[LF_idx]["dz"]) < 0.2'  ,
                                   ] ,
                                  } ,
                         'tkSF':  { 
                                    '1-1' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/egammaEffi.txt_EGM2D_runB_passingRECO_combineLowEt.root',
                                    '2-2' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/egammaEffi.txt_EGM2D_runC_passingRECO_combineLowEt.root',
                                    '3-3' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/egammaEffi.txt_EGM2D_runD_passingRECO_combineLowEt.root',
                                    '4-4' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/egammaEffi.txt_EGM2D_runE_passingRECO_combineLowEt.root',
                                    '5-5' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/egammaEffi.txt_EGM2D_runF_passingRECO_combineLowEt.root',
                                  } ,
                         'wpSF':  {
                                    '1-1' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/egammaEffi_passingMVA94Xwp90isoHWW_runB.txt' ,
                                    '2-2' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/egammaEffi_passingMVA94Xwp90isoHWW_runC.txt' ,
                                    '3-3' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/egammaEffi_passingMVA94Xwp90isoHWW_runD.txt' ,
                                    '4-4' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/egammaEffi_passingMVA94Xwp90isoHWW_runE.txt' ,
                                    '5-5' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/egammaEffi_passingMVA94Xwp90isoHWW_runF.txt' ,
                                  } ,
                         'fakeW' : '/LatinoAnalysis/NanoGardener/python/data/fake_prompt_rates/Full2017v2p2NewBinning/',
                              } ,
 
          'mvaFall17V1Iso_WP90_SS':  {
                         'cuts' : { 
                                # Common cuts 
                                'True' :
                                   [
                                     'abs(electron_col[LF_idx]["eta"]) < 2.5' ,
                                     'electron_col[LF_idx]["mvaFall17V1Iso_WP90"]',
                                     'electron_col[LF_idx]["convVeto"] == 1',
                                     'electron_col[LF_idx]["tightCharge"] == 2',
                                   ] ,
                                # Barrel
                                 'abs(electron_col[LF_idx]["eta"]) <= 1.479' :
                                   [
                                     'abs(electron_col[LF_idx]["dxy"]) < 0.05' ,
                                     'abs(electron_col[LF_idx]["dz"]) < 0.1'  ,
                                   ] ,
                                 # EndCap
                                 'abs(electron_col[LF_idx]["eta"]) > 1.479' :
                                   [
                                     'abs(electron_col[LF_idx]["dxy"]) < 0.1' ,
                                     'abs(electron_col[LF_idx]["dz"]) < 0.2'  ,
                                   ] ,
                                  } ,
                         'tkSF':  { 
                                    '1-1' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/egammaEffi.txt_EGM2D_runB_passingRECO_combineLowEt.root',
                                    '2-2' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/egammaEffi.txt_EGM2D_runC_passingRECO_combineLowEt.root',
                                    '3-3' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/egammaEffi.txt_EGM2D_runD_passingRECO_combineLowEt.root',
                                    '4-4' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/egammaEffi.txt_EGM2D_runE_passingRECO_combineLowEt.root',
                                    '5-5' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/egammaEffi.txt_EGM2D_runF_passingRECO_combineLowEt.root',
                                  } ,
                         'wpSF':  {
                                    '1-1' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/egammaEffi_passingMVA94Xwp90isoSSHWW_runB.txt',
                                    '2-2' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/egammaEffi_passingMVA94Xwp90isoSSHWW_runC.txt',
                                    '3-3' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/egammaEffi_passingMVA94Xwp90isoSSHWW_runD.txt',
                                    '4-4' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/egammaEffi_passingMVA94Xwp90isoSSHWW_runE.txt',
                                    '5-5' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/egammaEffi_passingMVA94Xwp90isoSSHWW_runF.txt',
                                  } ,
                         'fakeW' : '/LatinoAnalysis/NanoGardener/python/data/fake_prompt_rates/Full2017v2p2NewBinning/',
                              } ,


          # ----- mvaFall17V2Iso

          'mvaFall17V2Iso_WP90':  {
                         'cuts' : { 
                                # Common cuts 
                                'True' :
                                   [
                                     'abs(electron_col[LF_idx]["eta"]) < 2.5' ,
                                     'electron_col[LF_idx]["mvaFall17V2Iso_WP90"]',
                                     'electron_col[LF_idx]["convVeto"] == 1',
                                   ] ,
                                # Barrel
                                 'abs(electron_col[LF_idx]["eta"]) <= 1.479' :
                                   [
                                     'abs(electron_col[LF_idx]["dxy"]) < 0.05' ,
                                     'abs(electron_col[LF_idx]["dz"]) < 0.1'  ,
                                   ] ,
                                 # EndCap
                                 'abs(electron_col[LF_idx]["eta"]) > 1.479' :
                                   [
                                     'abs(electron_col[LF_idx]["dxy"]) < 0.1' ,
                                     'abs(electron_col[LF_idx]["dz"]) < 0.2'  ,
                                   ] ,
                                  } ,
                         'tkSF':  { 
                                    '1-1' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/egammaEffi.txt_EGM2D_runB_passingRECO_combineLowEt.root',
                                    '2-2' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/egammaEffi.txt_EGM2D_runC_passingRECO_combineLowEt.root',
                                    '3-3' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/egammaEffi.txt_EGM2D_runD_passingRECO_combineLowEt.root',
                                    '4-4' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/egammaEffi.txt_EGM2D_runE_passingRECO_combineLowEt.root',
                                    '5-5' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/egammaEffi.txt_EGM2D_runF_passingRECO_combineLowEt.root',
                                  } ,
                         'wpSF':  {
                                    '1-1' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/egammaEffi_passingMVA94Xwp90isoHWW_runB.txt' ,
                                    '2-2' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/egammaEffi_passingMVA94Xwp90isoHWW_runC.txt' ,
                                    '3-3' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/egammaEffi_passingMVA94Xwp90isoHWW_runD.txt' ,
                                    '4-4' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/egammaEffi_passingMVA94Xwp90isoHWW_runE.txt' ,
                                    '5-5' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/egammaEffi_passingMVA94Xwp90isoHWW_runF.txt' ,
                                  } ,
                         'fakeW' : '/LatinoAnalysis/NanoGardener/python/data/fake_prompt_rates/Full2017v2p2NewBinning/',
                              } ,
 
          'mvaFall17V2Iso_WP90_SS':  {
                         'cuts' : { 
                                # Common cuts 
                                'True' :
                                   [
                                     'abs(electron_col[LF_idx]["eta"]) < 2.5' ,
                                     'electron_col[LF_idx]["mvaFall17V2Iso_WP90"]',
                                     'electron_col[LF_idx]["convVeto"] == 1',
                                     'electron_col[LF_idx]["tightCharge"] == 2',
                                   ] ,
                                # Barrel
                                 'abs(electron_col[LF_idx]["eta"]) <= 1.479' :
                                   [
                                     'abs(electron_col[LF_idx]["dxy"]) < 0.05' ,
                                     'abs(electron_col[LF_idx]["dz"]) < 0.1'  ,
                                   ] ,
                                 # EndCap
                                 'abs(electron_col[LF_idx]["eta"]) > 1.479' :
                                   [
                                     'abs(electron_col[LF_idx]["dxy"]) < 0.1' ,
                                     'abs(electron_col[LF_idx]["dz"]) < 0.2'  ,
                                   ] ,
                                  } ,
                         'tkSF':  { 
                                    '1-1' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/egammaEffi.txt_EGM2D_runB_passingRECO_combineLowEt.root',
                                    '2-2' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/egammaEffi.txt_EGM2D_runC_passingRECO_combineLowEt.root',
                                    '3-3' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/egammaEffi.txt_EGM2D_runD_passingRECO_combineLowEt.root',
                                    '4-4' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/egammaEffi.txt_EGM2D_runE_passingRECO_combineLowEt.root',
                                    '5-5' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/egammaEffi.txt_EGM2D_runF_passingRECO_combineLowEt.root',
                                  } ,
                         'wpSF':  {
                                    '1-1' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/egammaEffi_passingMVA94Xwp90isoSSHWW_runB.txt',
                                    '2-2' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/egammaEffi_passingMVA94Xwp90isoSSHWW_runC.txt',
                                    '3-3' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/egammaEffi_passingMVA94Xwp90isoSSHWW_runD.txt',
                                    '4-4' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/egammaEffi_passingMVA94Xwp90isoSSHWW_runE.txt',
                                    '5-5' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/egammaEffi_passingMVA94Xwp90isoSSHWW_runF.txt',
                                  } ,
                         'fakeW' : '/LatinoAnalysis/NanoGardener/python/data/fake_prompt_rates/Full2017v2p2NewBinning/',
                              } ,

             },

 # ------------ 
 'WgStarObjWP' : {

         'mvaFall17Iso_WP90' : {
                         'cuts' : { 
                                # Common cuts
                                'True' :
                                  [
                                     'abs(electron_col[LF_idx]["eta"]) < 2.5' ,
                                     'electron_col[LF_idx]["mvaFall17noIso_WP90"]',
                                     'electron_col[LF_idx]["convVeto"] == 1',
                                  ] ,
                                # Barrel
                                'abs(electron_col[LF_idx]["eta"]) <= 1.479' :
                                  [
                                     'abs(electron_col[LF_idx]["dxy"]) < 0.05' ,
                                     'abs(electron_col[LF_idx]["dz"]) < 0.1'  ,
                                  ] ,
                                # EndCap
                                'abs(electron_col[LF_idx]["eta"]) > 1.479' :
                                  [
                                     'abs(electron_col[LF_idx]["dxy"]) < 0.1' ,
                                     'abs(electron_col[LF_idx]["dz"]) < 0.2'  ,
                                  ] ,
                                  } ,
                         'cuts_iso': {
                                # Common cuts
                                'True' :
                                [
                                  'None',
                                ],
                                # Barrel
                                'abs(electron_col[LF_idx]["eta"]) <= 1.479' :
                                [
                                  '0.25' 
                                ],
                                # EndCap
                                'abs(electron_col[LF_idx]["eta"]) > 1.479' :
                                [
                                  '0.2' 
                                ],
                                  },
                         'iso': ['pfRelIso03_all', 0.3],
                         'tkSF':  {
                                    '1-1' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/egammaEffi.txt_EGM2D_runB_passingRECO_combineLowEt.root',
                                    '2-2' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/egammaEffi.txt_EGM2D_runC_passingRECO_combineLowEt.root',
                                    '3-3' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/egammaEffi.txt_EGM2D_runD_passingRECO_combineLowEt.root',
                                    '4-4' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/egammaEffi.txt_EGM2D_runE_passingRECO_combineLowEt.root',
                                    '5-5' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/egammaEffi.txt_EGM2D_runF_passingRECO_combineLowEt.root',
                                  } ,
                         'wpSF':  {
                                    '1-1' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/egammaEffi_passingMVA94Xwp90isoHWW_runB.txt' ,
                                    '2-2' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/egammaEffi_passingMVA94Xwp90isoHWW_runC.txt' ,
                                    '3-3' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/egammaEffi_passingMVA94Xwp90isoHWW_runD.txt' ,
                                    '4-4' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/egammaEffi_passingMVA94Xwp90isoHWW_runE.txt' ,
                                    '5-5' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/egammaEffi_passingMVA94Xwp90isoHWW_runF.txt' ,
                                  } ,
                             } ,

                 } ,

},


###____________________Full2017v5__________________________
'Full2017v5': {


## ------------  

 'VetoObjWP' : { 
           'HLTsafe' : { 
                         'cuts' : { 
                               # Common cuts
                               'True' :
                                [
                                  'False'
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
                                   'abs(electron_col[LF_idx]["eta"]) < 2.5' ,
                                   'electron_col[LF_idx]["cutBased_Fall17_V1"] >= 3',
                                   'electron_col[LF_idx]["convVeto"] == 1', 
                                  ] ,             
                                # Barrel
                                'abs(electron_col[LF_idx]["eta"]) <= 1.479' :
                                  [
                                   'abs(electron_col[LF_idx]["dxy"]) < 0.05' ,
                                   'abs(electron_col[LF_idx]["dz"]) < 0.1'  ,
                                  ] ,
                                # EndCap
                                'abs(electron_col[LF_idx]["eta"]) > 1.479' :
                                  [
                                   'electron_col[LF_idx]["sieie"] < 0.03 ' ,                           
                                   'abs(electron_col[LF_idx]["eInvMinusPInv"]) < 0.014' ,
                                   'abs(electron_col[LF_idx]["dxy"]) < 0.1' ,
                                   'abs(electron_col[LF_idx]["dz"]) < 0.2'  ,
                                  ] ,
                                   },
                       } ,

                 } ,
 
# ------------ 
'TightObjWP' : {

          # ----- mvaFall17V1Iso

          'mvaFall17V1Iso_WP90':  {
                         'cuts' : { 
                                # Common cuts 
                                'True' :
                                   [
                                     'abs(electron_col[LF_idx]["eta"]) < 2.5' ,
                                     'electron_col[LF_idx]["mvaFall17V1Iso_WP90"]',
                                     'electron_col[LF_idx]["convVeto"] == 1',
                                     'electron_col[LF_idx]["pfRelIso03_all"] < 0.06',
                                   ] ,
                                # Barrel
                                 'abs(electron_col[LF_idx]["eta"]) <= 1.479' :
                                   [
                                     'abs(electron_col[LF_idx]["dxy"]) < 0.05' ,
                                     'abs(electron_col[LF_idx]["dz"]) < 0.1'  ,
                                   ] ,
                                 # EndCap
                                 'abs(electron_col[LF_idx]["eta"]) > 1.479' :
                                   [
                                     'abs(electron_col[LF_idx]["dxy"]) < 0.1' ,
                                     'abs(electron_col[LF_idx]["dz"]) < 0.2'  ,
                                   ] ,
                                  } ,
                         'tkSF':  { 
                                    '1-1' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017v5/egammaEffi.txt_EGM2D_runB_passingRECO_combineLowEt.root',
                                    '2-2' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017v5/egammaEffi.txt_EGM2D_runC_passingRECO_combineLowEt.root',
                                    '3-3' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017v5/egammaEffi.txt_EGM2D_runD_passingRECO_combineLowEt.root',
                                    '4-4' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017v5/egammaEffi.txt_EGM2D_runE_passingRECO_combineLowEt.root',
                                    '5-5' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017v5/egammaEffi.txt_EGM2D_runF_passingRECO_combineLowEt.root',
                                  } ,
                         'wpSF':  {
                                    '1-1' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017v5/egammaEffi_passingMVA102Xwp90isoHWWiso0p06_2017runB.txt' ,
                                    '2-2' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017v5/egammaEffi_passingMVA102Xwp90isoHWWiso0p06_2017runC.txt' ,
                                    '3-3' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017v5/egammaEffi_passingMVA102Xwp90isoHWWiso0p06_2017runD.txt' ,
                                    '4-4' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017v5/egammaEffi_passingMVA102Xwp90isoHWWiso0p06_2017runE.txt' ,
                                    '5-5' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017v5/egammaEffi_passingMVA102Xwp90isoHWWiso0p06_2017runF.txt' ,
                                  } ,
                         'fakeW' : '/LatinoAnalysis/NanoGardener/python/data/fake_prompt_rates/Full2017v5/mvaFall17V1Iso_WP90/',
                              } ,
 
          'mvaFall17V1Iso_WP90_SS':  {
                         'cuts' : { 
                                # Common cuts 
                                'True' :
                                   [
                                     'abs(electron_col[LF_idx]["eta"]) < 2.5' ,
                                     'electron_col[LF_idx]["mvaFall17V1Iso_WP90"]',
                                     'electron_col[LF_idx]["convVeto"] == 1',
                                     'electron_col[LF_idx]["pfRelIso03_all"] < 0.06', 
                                     'electron_col[LF_idx]["tightCharge"] == 2',
                                   ] ,
                                # Barrel
                                 'abs(electron_col[LF_idx]["eta"]) <= 1.479' :
                                   [
                                     'abs(electron_col[LF_idx]["dxy"]) < 0.05' ,
                                     'abs(electron_col[LF_idx]["dz"]) < 0.1'  ,
                                   ] ,
                                 # EndCap
                                 'abs(electron_col[LF_idx]["eta"]) > 1.479' :
                                   [
                                     'abs(electron_col[LF_idx]["dxy"]) < 0.1' ,
                                     'abs(electron_col[LF_idx]["dz"]) < 0.2'  ,
                                   ] ,
                                  } ,
                         'tkSF':  { 
                                    '1-1' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017v5/egammaEffi.txt_EGM2D_runB_passingRECO_combineLowEt.root',
                                    '2-2' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017v5/egammaEffi.txt_EGM2D_runC_passingRECO_combineLowEt.root',
                                    '3-3' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017v5/egammaEffi.txt_EGM2D_runD_passingRECO_combineLowEt.root',
                                    '4-4' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017v5/egammaEffi.txt_EGM2D_runE_passingRECO_combineLowEt.root',
                                    '5-5' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017v5/egammaEffi.txt_EGM2D_runF_passingRECO_combineLowEt.root',
                                  } ,
                         'wpSF':  {
                                    '1-1' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017v5/egammaEffi_passingMVA102Xwp90isoSSHWWiso0p06_2017runB.txt',
                                    '2-2' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017v5/egammaEffi_passingMVA102Xwp90isoSSHWWiso0p06_2017runC.txt',
                                    '3-3' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017v5/egammaEffi_passingMVA102Xwp90isoSSHWWiso0p06_2017runD.txt',
                                    '4-4' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017v5/egammaEffi_passingMVA102Xwp90isoSSHWWiso0p06_2017runE.txt',
                                    '5-5' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017v5/egammaEffi_passingMVA102Xwp90isoSSHWWiso0p06_2017runF.txt',
                                  } ,
                         'fakeW' : '/LatinoAnalysis/NanoGardener/python/data/fake_prompt_rates/Full2017v5/mvaFall17V1Iso_WP90_SS/',
                              } ,


          # ----- mvaFall17V2Iso

          'mvaFall17V2Iso_WP90':  {
                         'cuts' : { 
                                # Common cuts 
                                'True' :
                                   [
                                     'abs(electron_col[LF_idx]["eta"]) < 2.5' ,
                                     'electron_col[LF_idx]["mvaFall17V2Iso_WP90"]',
                                     'electron_col[LF_idx]["convVeto"] == 1',
                                     'electron_col[LF_idx]["pfRelIso03_all"] < 0.06', 
                                   ] ,
                                # Barrel
                                 'abs(electron_col[LF_idx]["eta"]) <= 1.479' :
                                   [
                                     'abs(electron_col[LF_idx]["dxy"]) < 0.05' ,
                                     'abs(electron_col[LF_idx]["dz"]) < 0.1'  ,
                                   ] ,
                                 # EndCap
                                 'abs(electron_col[LF_idx]["eta"]) > 1.479' :
                                   [
                                     'abs(electron_col[LF_idx]["dxy"]) < 0.1' ,
                                     'abs(electron_col[LF_idx]["dz"]) < 0.2'  ,
                                   ] ,
                                  } ,
                         'tkSF':  { 
                                    '1-1' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017v5/egammaEffi.txt_EGM2D_runB_passingRECO_combineLowEt.root',
                                    '2-2' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017v5/egammaEffi.txt_EGM2D_runC_passingRECO_combineLowEt.root',
                                    '3-3' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017v5/egammaEffi.txt_EGM2D_runD_passingRECO_combineLowEt.root',
                                    '4-4' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017v5/egammaEffi.txt_EGM2D_runE_passingRECO_combineLowEt.root',
                                    '5-5' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017v5/egammaEffi.txt_EGM2D_runF_passingRECO_combineLowEt.root',
                                  } ,
                         'wpSF':  {
                                    '1-1' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017v5/egammaEffi_passingMVA102Xwp90isoHWWiso0p06_2017runB.txt' ,
                                    '2-2' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017v5/egammaEffi_passingMVA102Xwp90isoHWWiso0p06_2017runC.txt' ,
                                    '3-3' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017v5/egammaEffi_passingMVA102Xwp90isoHWWiso0p06_2017runD.txt' ,
                                    '4-4' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017v5/egammaEffi_passingMVA102Xwp90isoHWWiso0p06_2017runE.txt' ,
                                    '5-5' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017v5/egammaEffi_passingMVA102Xwp90isoHWWiso0p06_2017runF.txt' ,
                                  } ,
                        #'fakeW' : '/LatinoAnalysis/NanoGardener/python/data/fake_prompt_rates/Full2017v5/mvaFall17V2Iso_WP90',
                        'fakeW' : '/LatinoAnalysis/NanoGardener/python/data/fake_prompt_rates/Full2017CutBased/',
                              } ,
 
          'mvaFall17V2Iso_WP90_SS':  {
                         'cuts' : { 
                                # Common cuts 
                                'True' :
                                   [
                                     'abs(electron_col[LF_idx]["eta"]) < 2.5' ,
                                     'electron_col[LF_idx]["mvaFall17V2Iso_WP90"]',
                                     'electron_col[LF_idx]["convVeto"] == 1',
                                     'electron_col[LF_idx]["pfRelIso03_all"] < 0.06',
                                     'electron_col[LF_idx]["tightCharge"] == 2',
                                   ] ,
                                # Barrel
                                 'abs(electron_col[LF_idx]["eta"]) <= 1.479' :
                                   [
                                     'abs(electron_col[LF_idx]["dxy"]) < 0.05' ,
                                     'abs(electron_col[LF_idx]["dz"]) < 0.1'  ,
                                   ] ,
                                 # EndCap
                                 'abs(electron_col[LF_idx]["eta"]) > 1.479' :
                                   [
                                     'abs(electron_col[LF_idx]["dxy"]) < 0.1' ,
                                     'abs(electron_col[LF_idx]["dz"]) < 0.2'  ,
                                   ] ,
                                  } ,
                         'tkSF':  { 
                                    '1-1' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017v5/egammaEffi.txt_EGM2D_runB_passingRECO_combineLowEt.root',
                                    '2-2' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017v5/egammaEffi.txt_EGM2D_runC_passingRECO_combineLowEt.root',
                                    '3-3' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017v5/egammaEffi.txt_EGM2D_runD_passingRECO_combineLowEt.root',
                                    '4-4' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017v5/egammaEffi.txt_EGM2D_runE_passingRECO_combineLowEt.root',
                                    '5-5' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017v5/egammaEffi.txt_EGM2D_runF_passingRECO_combineLowEt.root',
                                  } ,
                         'wpSF':  {
                                    '1-1' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017v5/egammaEffi_passingMVA102Xwp90isoSSHWWiso0p06_2017runB.txt',
                                    '2-2' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017v5/egammaEffi_passingMVA102Xwp90isoSSHWWiso0p06_2017runC.txt',
                                    '3-3' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017v5/egammaEffi_passingMVA102Xwp90isoSSHWWiso0p06_2017runD.txt',
                                    '4-4' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017v5/egammaEffi_passingMVA102Xwp90isoSSHWWiso0p06_2017runE.txt',
                                    '5-5' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017v5/egammaEffi_passingMVA102Xwp90isoSSHWWiso0p06_2017runF.txt',
                                  } ,
                         'fakeW' : '/LatinoAnalysis/NanoGardener/python/data/fake_prompt_rates/Full2017v5/mvaFall17V2Iso_WP90_SS/',
                              } ,

             },

 # ------------ 
 'WgStarObjWP' : {

         'mvaFall17Iso_WP90' : {
                         'cuts' : { 
                                # Common cuts
                                'True' :
                                  [
                                     'abs(electron_col[LF_idx]["eta"]) < 2.5' ,
                                     'electron_col[LF_idx]["cutBased_Fall17_V1"] >= 3',
                                     'electron_col[LF_idx]["mvaFall17V1noIso_WP90"]',
                                     'electron_col[LF_idx]["convVeto"] == 1',
                                  ] ,
                                # Barrel
                                'abs(electron_col[LF_idx]["eta"]) <= 1.479' :
                                  [
                                     'abs(electron_col[LF_idx]["dxy"]) < 0.05' ,
                                     'abs(electron_col[LF_idx]["dz"]) < 0.1'  ,
                                  ] ,
                                # EndCap
                                'abs(electron_col[LF_idx]["eta"]) > 1.479' :
                                  [
                                   'electron_col[LF_idx]["sieie"] < 0.03 ' ,
                                   'abs(electron_col[LF_idx]["eInvMinusPInv"]) < 0.014' ,
                                   'abs(electron_col[LF_idx]["dxy"]) < 0.1' ,
                                   'abs(electron_col[LF_idx]["dz"]) < 0.2'  ,
                                  ] ,
                                  } ,
                         'cuts_iso': {
                                # Common cuts
                                'True' :
                                [
                                  '0.06',
                                ],
                                # Barrel
                                'abs(electron_col[LF_idx]["eta"]) <= 1.479' :
                                [
                                  'None' 
                                ],
                                # EndCap
                                'abs(electron_col[LF_idx]["eta"]) > 1.479' :
                                [
                                  'None' 
                                ],
                                  },
                         'iso': ['pfRelIso03_all', 0.3],
                         'tkSF':  {
                                    '1-1' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017v5/egammaEffi.txt_EGM2D_runB_passingRECO_combineLowEt.root',
                                    '2-2' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017v5/egammaEffi.txt_EGM2D_runC_passingRECO_combineLowEt.root',
                                    '3-3' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017v5/egammaEffi.txt_EGM2D_runD_passingRECO_combineLowEt.root',
                                    '4-4' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017v5/egammaEffi.txt_EGM2D_runE_passingRECO_combineLowEt.root',
                                    '5-5' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017v5/egammaEffi.txt_EGM2D_runF_passingRECO_combineLowEt.root',
                                  } ,
                         'wpSF':  {
                                    '1-1' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017v5/egammaEffi_passingMVA102Xwp90isoHWWiso0p06_2017runB.txt' ,
                                    '2-2' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017v5/egammaEffi_passingMVA102Xwp90isoHWWiso0p06_2017runC.txt' ,
                                    '3-3' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017v5/egammaEffi_passingMVA102Xwp90isoHWWiso0p06_2017runD.txt' ,
                                    '4-4' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017v5/egammaEffi_passingMVA102Xwp90isoHWWiso0p06_2017runE.txt' ,
                                    '5-5' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017v5/egammaEffi_passingMVA102Xwp90isoHWWiso0p06_2017runF.txt' ,
                                  } ,
                             } ,

                 } ,

},


###____________________Full2017v6__________________________
'Full2017v6': {


## ------------  

 'VetoObjWP' : { 
           'HLTsafe' : { 
                         'cuts' : { 
                               # Common cuts
                               'True' :
                                [
                                  'False'
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
                                   'abs(electron_col[LF_idx]["eta"]) < 2.5' ,
                                   'electron_col[LF_idx]["cutBased_Fall17_V1"] >= 3',
                                   'electron_col[LF_idx]["convVeto"] == 1', 
                                  ] ,             
                                # Barrel
                                'abs(electron_col[LF_idx]["eta"]) <= 1.479' :
                                  [
                                   'abs(electron_col[LF_idx]["dxy"]) < 0.05' ,
                                   'abs(electron_col[LF_idx]["dz"]) < 0.1'  ,
                                  ] ,
                                # EndCap
                                'abs(electron_col[LF_idx]["eta"]) > 1.479' :
                                  [
                                   'electron_col[LF_idx]["sieie"] < 0.03 ' ,                           
                                   'abs(electron_col[LF_idx]["eInvMinusPInv"]) < 0.014' ,
                                   'abs(electron_col[LF_idx]["dxy"]) < 0.1' ,
                                   'abs(electron_col[LF_idx]["dz"]) < 0.2'  ,
                                  ] ,
                                   },
                       } ,

                 } ,
 
# ------------ 
'TightObjWP' : {

          # ----- cut
 
         'cutFall17V1Iso_Tight': {
                         'cuts' : { 
                                # Common cuts 
                                'True' :
                                   [
                                     'abs(electron_col[LF_idx]["eta"]) < 2.5' ,
                                     'electron_col[LF_idx]["cutBased_Fall17_V1"] >= 4',
                                     'electron_col[LF_idx]["convVeto"] == 1',
                                     'electron_col[LF_idx]["pfRelIso03_all"] < 0.06',
                                   ] ,
                                # Barrel
                                 'abs(electron_col[LF_idx]["eta"]) <= 1.479' :
                                   [
                                     'abs(electron_col[LF_idx]["dxy"]) < 0.05' ,
                                     'abs(electron_col[LF_idx]["dz"]) < 0.1'  ,
                                   ] ,
                                 # EndCap
                                 'abs(electron_col[LF_idx]["eta"]) > 1.479' :
                                   [
                                     'abs(electron_col[LF_idx]["dxy"]) < 0.1' ,
                                     'abs(electron_col[LF_idx]["dz"]) < 0.2'  ,
                                   ] ,
                                  } ,
                         'tkSF':  {
                                    '1-1' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017v6/egammaEffi.txt_EGM2D_runB_passingRECO_combineLowEt.root',
                                    '2-2' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017v6/egammaEffi.txt_EGM2D_runC_passingRECO_combineLowEt.root',
                                    '3-3' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017v6/egammaEffi.txt_EGM2D_runD_passingRECO_combineLowEt.root',
                                    '4-4' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017v6/egammaEffi.txt_EGM2D_runE_passingRECO_combineLowEt.root',
                                    '5-5' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017v6/egammaEffi.txt_EGM2D_runF_passingRECO_combineLowEt.root',
                                  } ,
                         'wpSF':  {
                                   '1-1' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017v6/egammaEffi_passingTight102XHWW_2017runB.txt' ,
                                   '2-2' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017v6/egammaEffi_passingTight102XHWW_2017runC.txt' ,
                                   '3-3' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017v6/egammaEffi_passingTight102XHWW_2017runD.txt' ,
                                   '4-4' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017v6/egammaEffi_passingTight102XHWW_2017runE.txt' ,
                                   '5-5' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017v6/egammaEffi_passingTight102XHWW_2017runF.txt' ,
                                 } ,
                         #fakeW' : '/LatinoAnalysis/NanoGardener/python/data/fake_prompt_rates/Full2017v6/mvaFall17V1Iso_WP90/',
                              } ,           

        'cutFall17V1Iso_Tight_SS': {
                         'cuts' : {
                                # Common cuts 
                                'True' :
                                   [
                                     'abs(electron_col[LF_idx]["eta"]) < 2.5' ,
                                     'electron_col[LF_idx]["cutBased_Fall17_V1"] >= 4',
                                     'electron_col[LF_idx]["convVeto"] == 1',
                                     'electron_col[LF_idx]["pfRelIso03_all"] < 0.06',
                                     'electron_col[LF_idx]["tightCharge"] == 2',
                                   ] ,
                                # Barrel
                                 'abs(electron_col[LF_idx]["eta"]) <= 1.479' :
                                   [
                                     'abs(electron_col[LF_idx]["dxy"]) < 0.05' ,
                                     'abs(electron_col[LF_idx]["dz"]) < 0.1'  ,
                                   ] ,
                                 # EndCap
                                 'abs(electron_col[LF_idx]["eta"]) > 1.479' :
                                   [
                                     'abs(electron_col[LF_idx]["dxy"]) < 0.1' ,
                                     'abs(electron_col[LF_idx]["dz"]) < 0.2'  ,
                                   ] ,
                                  } ,
                         'tkSF':  {
                                    '1-1' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017v6/egammaEffi.txt_EGM2D_runB_passingRECO_combineLowEt.root',
                                    '2-2' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017v6/egammaEffi.txt_EGM2D_runC_passingRECO_combineLowEt.root',
                                    '3-3' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017v6/egammaEffi.txt_EGM2D_runD_passingRECO_combineLowEt.root',
                                    '4-4' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017v6/egammaEffi.txt_EGM2D_runE_passingRECO_combineLowEt.root',
                                    '5-5' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017v6/egammaEffi.txt_EGM2D_runF_passingRECO_combineLowEt.root',
                                  } ,
                         'wpSF':  {
                                   '1-1' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017v6/egammaEffi_passingTight102XSSHWW_2017runB.txt' ,
                                   '2-2' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017v6/egammaEffi_passingTight102XSSHWW_2017runC.txt' ,
                                   '3-3' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017v6/egammaEffi_passingTight102XSSHWW_2017runD.txt' ,
                                   '4-4' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017v6/egammaEffi_passingTight102XSSHWW_2017runE.txt' ,
                                   '5-5' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017v6/egammaEffi_passingTight102XSSHWW_2017runF.txt' ,
                                 } ,
                         #fakeW' : '/LatinoAnalysis/NanoGardener/python/data/fake_prompt_rates/Full2017v6/mvaFall17V1Iso_WP90/',
                              } ,


          # ----- cut V2
 
         'cutFall17V2Iso_Tight': {
                         'cuts' : { 
                                # Common cuts 
                                'True' :
                                   [
                                     'abs(electron_col[LF_idx]["eta"]) < 2.5' ,
                                     'electron_col[LF_idx]["cutBased"] >= 4',
                                     'electron_col[LF_idx]["convVeto"] == 1',
                                     'electron_col[LF_idx]["pfRelIso03_all"] < 0.06',
                                   ] ,
                                # Barrel
                                 'abs(electron_col[LF_idx]["eta"]) <= 1.479' :
                                   [
                                     'abs(electron_col[LF_idx]["dxy"]) < 0.05' ,
                                     'abs(electron_col[LF_idx]["dz"]) < 0.1'  ,
                                   ] ,
                                 # EndCap
                                 'abs(electron_col[LF_idx]["eta"]) > 1.479' :
                                   [
                                     'abs(electron_col[LF_idx]["dxy"]) < 0.1' ,
                                     'abs(electron_col[LF_idx]["dz"]) < 0.2'  ,
                                   ] ,
                                  } ,
                         'tkSF':  {
                                    '1-1' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017v6/egammaEffi.txt_EGM2D_runB_passingRECO_combineLowEt.root',
                                    '2-2' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017v6/egammaEffi.txt_EGM2D_runC_passingRECO_combineLowEt.root',
                                    '3-3' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017v6/egammaEffi.txt_EGM2D_runD_passingRECO_combineLowEt.root',
                                    '4-4' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017v6/egammaEffi.txt_EGM2D_runE_passingRECO_combineLowEt.root',
                                    '5-5' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017v6/egammaEffi.txt_EGM2D_runF_passingRECO_combineLowEt.root',
                                  } ,
                         'wpSF':  {
                                   '1-1' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017v6/egammaEffi_passingTight102XV2HWW_2017runB.txt' ,
                                   '2-2' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017v6/egammaEffi_passingTight102XV2HWW_2017runC.txt' ,
                                   '3-3' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017v6/egammaEffi_passingTight102XV2HWW_2017runD.txt' ,
                                   '4-4' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017v6/egammaEffi_passingTight102XV2HWW_2017runE.txt' ,
                                   '5-5' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017v6/egammaEffi_passingTight102XV2HWW_2017runF.txt' ,
                                 } ,
                         #fakeW' : '/LatinoAnalysis/NanoGardener/python/data/fake_prompt_rates/Full2017v6/mvaFall17V1Iso_WP90/',
                              } ,           

        'cutFall17V2Iso_Tight_SS': {
                         'cuts' : {
                                # Common cuts 
                                'True' :
                                   [
                                     'abs(electron_col[LF_idx]["eta"]) < 2.5' ,
                                     'electron_col[LF_idx]["cutBased"] >= 4',
                                     'electron_col[LF_idx]["convVeto"] == 1',
                                     'electron_col[LF_idx]["pfRelIso03_all"] < 0.06',
                                     'electron_col[LF_idx]["tightCharge"] == 2',
                                   ] ,
                                # Barrel
                                 'abs(electron_col[LF_idx]["eta"]) <= 1.479' :
                                   [
                                     'abs(electron_col[LF_idx]["dxy"]) < 0.05' ,
                                     'abs(electron_col[LF_idx]["dz"]) < 0.1'  ,
                                   ] ,
                                 # EndCap
                                 'abs(electron_col[LF_idx]["eta"]) > 1.479' :
                                   [
                                     'abs(electron_col[LF_idx]["dxy"]) < 0.1' ,
                                     'abs(electron_col[LF_idx]["dz"]) < 0.2'  ,
                                   ] ,
                                  } ,
                         'tkSF':  {
                                    '1-1' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017v6/egammaEffi.txt_EGM2D_runB_passingRECO_combineLowEt.root',
                                    '2-2' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017v6/egammaEffi.txt_EGM2D_runC_passingRECO_combineLowEt.root',
                                    '3-3' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017v6/egammaEffi.txt_EGM2D_runD_passingRECO_combineLowEt.root',
                                    '4-4' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017v6/egammaEffi.txt_EGM2D_runE_passingRECO_combineLowEt.root',
                                    '5-5' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017v6/egammaEffi.txt_EGM2D_runF_passingRECO_combineLowEt.root',
                                  } ,
                         'wpSF':  {
                                   '1-1' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017v6/egammaEffi_passingTight102XV2SSHWW_2017runB.txt' ,
                                   '2-2' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017v6/egammaEffi_passingTight102XV2SSHWW_2017runC.txt' ,
                                   '3-3' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017v6/egammaEffi_passingTight102XV2SSHWW_2017runD.txt' ,
                                   '4-4' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017v6/egammaEffi_passingTight102XV2SSHWW_2017runE.txt' ,
                                   '5-5' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017v6/egammaEffi_passingTight102XV2SSHWW_2017runF.txt' ,
                                 } ,
                         #fakeW' : '/LatinoAnalysis/NanoGardener/python/data/fake_prompt_rates/Full2017v6/mvaFall17V1Iso_WP90/',
                              } ,
          # ----- mvaFall17V1Iso

          'mvaFall17V1Iso_WP90':  {
                         'cuts' : { 
                                # Common cuts 
                                'True' :
                                   [
                                     'abs(electron_col[LF_idx]["eta"]) < 2.5' ,
                                     'electron_col[LF_idx]["mvaFall17V1Iso_WP90"]',
                                     'electron_col[LF_idx]["convVeto"] == 1',
                                     'electron_col[LF_idx]["pfRelIso03_all"] < 0.06',
                                   ] ,
                                # Barrel
                                 'abs(electron_col[LF_idx]["eta"]) <= 1.479' :
                                   [
                                     'abs(electron_col[LF_idx]["dxy"]) < 0.05' ,
                                     'abs(electron_col[LF_idx]["dz"]) < 0.1'  ,
                                   ] ,
                                 # EndCap
                                 'abs(electron_col[LF_idx]["eta"]) > 1.479' :
                                   [
                                     'abs(electron_col[LF_idx]["dxy"]) < 0.1' ,
                                     'abs(electron_col[LF_idx]["dz"]) < 0.2'  ,
                                   ] ,
                                  } ,
                         'tkSF':  { 
                                    '1-1' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017v6/egammaEffi.txt_EGM2D_runB_passingRECO_combineLowEt.root',
                                    '2-2' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017v6/egammaEffi.txt_EGM2D_runC_passingRECO_combineLowEt.root',
                                    '3-3' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017v6/egammaEffi.txt_EGM2D_runD_passingRECO_combineLowEt.root',
                                    '4-4' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017v6/egammaEffi.txt_EGM2D_runE_passingRECO_combineLowEt.root',
                                    '5-5' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017v6/egammaEffi.txt_EGM2D_runF_passingRECO_combineLowEt.root',
                                  } ,
                         'wpSF':  {
                                    '1-1' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017v6/egammaEffi_passingMVA102Xwp90isoHWWiso0p06_2017runB.txt' ,
                                    '2-2' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017v6/egammaEffi_passingMVA102Xwp90isoHWWiso0p06_2017runC.txt' ,
                                    '3-3' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017v6/egammaEffi_passingMVA102Xwp90isoHWWiso0p06_2017runD.txt' ,
                                    '4-4' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017v6/egammaEffi_passingMVA102Xwp90isoHWWiso0p06_2017runE.txt' ,
                                    '5-5' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017v6/egammaEffi_passingMVA102Xwp90isoHWWiso0p06_2017runF.txt' ,
                                  } ,
                         'fakeW' : '/LatinoAnalysis/NanoGardener/python/data/fake_prompt_rates/Full2017v6/mvaFall17V1Iso_WP90/',
                              } ,
 
          'mvaFall17V1Iso_WP90_SS':  {
                         'cuts' : { 
                                # Common cuts 
                                'True' :
                                   [
                                     'abs(electron_col[LF_idx]["eta"]) < 2.5' ,
                                     'electron_col[LF_idx]["mvaFall17V1Iso_WP90"]',
                                     'electron_col[LF_idx]["convVeto"] == 1',
                                     'electron_col[LF_idx]["pfRelIso03_all"] < 0.06', 
                                     'electron_col[LF_idx]["tightCharge"] == 2',
                                   ] ,
                                # Barrel
                                 'abs(electron_col[LF_idx]["eta"]) <= 1.479' :
                                   [
                                     'abs(electron_col[LF_idx]["dxy"]) < 0.05' ,
                                     'abs(electron_col[LF_idx]["dz"]) < 0.1'  ,
                                   ] ,
                                 # EndCap
                                 'abs(electron_col[LF_idx]["eta"]) > 1.479' :
                                   [
                                     'abs(electron_col[LF_idx]["dxy"]) < 0.1' ,
                                     'abs(electron_col[LF_idx]["dz"]) < 0.2'  ,
                                   ] ,
                                  } ,
                         'tkSF':  { 
                                    '1-1' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017v6/egammaEffi.txt_EGM2D_runB_passingRECO_combineLowEt.root',
                                    '2-2' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017v6/egammaEffi.txt_EGM2D_runC_passingRECO_combineLowEt.root',
                                    '3-3' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017v6/egammaEffi.txt_EGM2D_runD_passingRECO_combineLowEt.root',
                                    '4-4' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017v6/egammaEffi.txt_EGM2D_runE_passingRECO_combineLowEt.root',
                                    '5-5' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017v6/egammaEffi.txt_EGM2D_runF_passingRECO_combineLowEt.root',
                                  } ,
                         'wpSF':  {
                                    '1-1' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017v6/egammaEffi_passingMVA102Xwp90isoSSHWWiso0p06_2017runB.txt',
                                    '2-2' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017v6/egammaEffi_passingMVA102Xwp90isoSSHWWiso0p06_2017runC.txt',
                                    '3-3' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017v6/egammaEffi_passingMVA102Xwp90isoSSHWWiso0p06_2017runD.txt',
                                    '4-4' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017v6/egammaEffi_passingMVA102Xwp90isoSSHWWiso0p06_2017runE.txt',
                                    '5-5' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017v6/egammaEffi_passingMVA102Xwp90isoSSHWWiso0p06_2017runF.txt',
                                  } ,
                         'fakeW' : '/LatinoAnalysis/NanoGardener/python/data/fake_prompt_rates/Full2017v6/mvaFall17V1Iso_WP90_SS/',
                              } ,


          # ----- mvaFall17V2Iso

          'mvaFall17V2Iso_WP90':  {
                         'cuts' : { 
                                # Common cuts 
                                'True' :
                                   [
                                     'abs(electron_col[LF_idx]["eta"]) < 2.5' ,
                                     'electron_col[LF_idx]["mvaFall17V2Iso_WP90"]',
                                     'electron_col[LF_idx]["convVeto"] == 1',
                                     'electron_col[LF_idx]["pfRelIso03_all"] < 0.06', 
                                   ] ,
                                # Barrel
                                 'abs(electron_col[LF_idx]["eta"]) <= 1.479' :
                                   [
                                     'abs(electron_col[LF_idx]["dxy"]) < 0.05' ,
                                     'abs(electron_col[LF_idx]["dz"]) < 0.1'  ,
                                   ] ,
                                 # EndCap
                                 'abs(electron_col[LF_idx]["eta"]) > 1.479' :
                                   [
                                     'abs(electron_col[LF_idx]["dxy"]) < 0.1' ,
                                     'abs(electron_col[LF_idx]["dz"]) < 0.2'  ,
                                   ] ,
                                  } ,
                         'tkSF':  { 
                                    '1-1' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017v6/egammaEffi.txt_EGM2D_runB_passingRECO_combineLowEt.root',
                                    '2-2' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017v6/egammaEffi.txt_EGM2D_runC_passingRECO_combineLowEt.root',
                                    '3-3' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017v6/egammaEffi.txt_EGM2D_runD_passingRECO_combineLowEt.root',
                                    '4-4' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017v6/egammaEffi.txt_EGM2D_runE_passingRECO_combineLowEt.root',
                                    '5-5' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017v6/egammaEffi.txt_EGM2D_runF_passingRECO_combineLowEt.root',
                                  } ,
                         'wpSF':  {
                                    '1-1' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017v6/egammaEffi_passingMVA102Xwp90V2isoHWWiso0p06_2017runB.txt' ,
                                    '2-2' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017v6/egammaEffi_passingMVA102Xwp90V2isoHWWiso0p06_2017runC.txt' ,
                                    '3-3' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017v6/egammaEffi_passingMVA102Xwp90V2isoHWWiso0p06_2017runD.txt' ,
                                    '4-4' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017v6/egammaEffi_passingMVA102Xwp90V2isoHWWiso0p06_2017runE.txt' ,
                                    '5-5' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017v6/egammaEffi_passingMVA102Xwp90V2isoHWWiso0p06_2017runF.txt' ,
                                  } ,
                        'fakeW' : '/LatinoAnalysis/NanoGardener/python/data/fake_prompt_rates/Full2017v6/mvaFall17V2Iso_WP90',
                              } ,
 
          'mvaFall17V2Iso_WP90_SS':  {
                         'cuts' : { 
                                # Common cuts 
                                'True' :
                                   [
                                     'abs(electron_col[LF_idx]["eta"]) < 2.5' ,
                                     'electron_col[LF_idx]["mvaFall17V2Iso_WP90"]',
                                     'electron_col[LF_idx]["convVeto"] == 1',
                                     'electron_col[LF_idx]["pfRelIso03_all"] < 0.06',
                                     'electron_col[LF_idx]["tightCharge"] == 2',
                                   ] ,
                                # Barrel
                                 'abs(electron_col[LF_idx]["eta"]) <= 1.479' :
                                   [
                                     'abs(electron_col[LF_idx]["dxy"]) < 0.05' ,
                                     'abs(electron_col[LF_idx]["dz"]) < 0.1'  ,
                                   ] ,
                                 # EndCap
                                 'abs(electron_col[LF_idx]["eta"]) > 1.479' :
                                   [
                                     'abs(electron_col[LF_idx]["dxy"]) < 0.1' ,
                                     'abs(electron_col[LF_idx]["dz"]) < 0.2'  ,
                                   ] ,
                                  } ,
                         'tkSF':  { 
                                    '1-1' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017v6/egammaEffi.txt_EGM2D_runB_passingRECO_combineLowEt.root',
                                    '2-2' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017v6/egammaEffi.txt_EGM2D_runC_passingRECO_combineLowEt.root',
                                    '3-3' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017v6/egammaEffi.txt_EGM2D_runD_passingRECO_combineLowEt.root',
                                    '4-4' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017v6/egammaEffi.txt_EGM2D_runE_passingRECO_combineLowEt.root',
                                    '5-5' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017v6/egammaEffi.txt_EGM2D_runF_passingRECO_combineLowEt.root',
                                  } ,
                         'wpSF':  {
                                    '1-1' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017v6/egammaEffi_passingMVA102Xwp90V2isoSSHWWiso0p06_2017runB.txt',
                                    '2-2' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017v6/egammaEffi_passingMVA102Xwp90V2isoSSHWWiso0p06_2017runC.txt',
                                    '3-3' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017v6/egammaEffi_passingMVA102Xwp90V2isoSSHWWiso0p06_2017runD.txt',
                                    '4-4' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017v6/egammaEffi_passingMVA102Xwp90V2isoSSHWWiso0p06_2017runE.txt',
                                    '5-5' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017v6/egammaEffi_passingMVA102Xwp90V2isoSSHWWiso0p06_2017runF.txt',
                                  } ,
                         'fakeW' : '/LatinoAnalysis/NanoGardener/python/data/fake_prompt_rates/Full2017v6/mvaFall17V2Iso_WP90_SS/',
                              } ,

             },

 # ------------ 
 'WgStarObjWP' : {

         'mvaFall17Iso_WP90' : {
                         'cuts' : { 
                                # Common cuts
                                'True' :
                                  [
                                     'abs(electron_col[LF_idx]["eta"]) < 2.5' ,
                                     'electron_col[LF_idx]["cutBased_Fall17_V1"] >= 3',
                                     'electron_col[LF_idx]["mvaFall17V1noIso_WP90"]',
                                     'electron_col[LF_idx]["convVeto"] == 1',
                                  ] ,
                                # Barrel
                                'abs(electron_col[LF_idx]["eta"]) <= 1.479' :
                                  [
                                     'abs(electron_col[LF_idx]["dxy"]) < 0.05' ,
                                     'abs(electron_col[LF_idx]["dz"]) < 0.1'  ,
                                  ] ,
                                # EndCap
                                'abs(electron_col[LF_idx]["eta"]) > 1.479' :
                                  [
                                   'electron_col[LF_idx]["sieie"] < 0.03 ' ,
                                   'abs(electron_col[LF_idx]["eInvMinusPInv"]) < 0.014' ,
                                   'abs(electron_col[LF_idx]["dxy"]) < 0.1' ,
                                   'abs(electron_col[LF_idx]["dz"]) < 0.2'  ,
                                  ] ,
                                  } ,
                         'cuts_iso': {
                                # Common cuts
                                'True' :
                                [
                                  '0.06',
                                ],
                                # Barrel
                                'abs(electron_col[LF_idx]["eta"]) <= 1.479' :
                                [
                                  'None' 
                                ],
                                # EndCap
                                'abs(electron_col[LF_idx]["eta"]) > 1.479' :
                                [
                                  'None' 
                                ],
                                  },
                         'iso': ['pfRelIso03_all', 0.3],
                         'tkSF':  {
                                    '1-1' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017v5/egammaEffi.txt_EGM2D_runB_passingRECO_combineLowEt.root',
                                    '2-2' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017v5/egammaEffi.txt_EGM2D_runC_passingRECO_combineLowEt.root',
                                    '3-3' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017v5/egammaEffi.txt_EGM2D_runD_passingRECO_combineLowEt.root',
                                    '4-4' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017v5/egammaEffi.txt_EGM2D_runE_passingRECO_combineLowEt.root',
                                    '5-5' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017v5/egammaEffi.txt_EGM2D_runF_passingRECO_combineLowEt.root',
                                  } ,
                         'wpSF':  {
                                    '1-1' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017v5/egammaEffi_passingMVA102Xwp90isoHWWiso0p06_2017runB.txt' ,
                                    '2-2' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017v5/egammaEffi_passingMVA102Xwp90isoHWWiso0p06_2017runC.txt' ,
                                    '3-3' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017v5/egammaEffi_passingMVA102Xwp90isoHWWiso0p06_2017runD.txt' ,
                                    '4-4' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017v5/egammaEffi_passingMVA102Xwp90isoHWWiso0p06_2017runE.txt' ,
                                    '5-5' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017v5/egammaEffi_passingMVA102Xwp90isoHWWiso0p06_2017runF.txt' ,
                                  } ,
                             } ,

                 } ,

},

###____________________Full2017v2LP19__________________________
'Full2017v2LP19': {


## ------------  

 'VetoObjWP' : { 
           'HLTsafe' : { 
                         'cuts' : { 
                               # Common cuts
                               'True' :
                                [
                                  'False'
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
                                   'abs(electron_col[LF_idx]["eta"]) < 2.5' ,
                                   'electron_col[LF_idx]["cutBased"] >= 3',
                                   'electron_col[LF_idx]["convVeto"] == 1',
                                  ] ,             
                                # Barrel
                                'abs(electron_col[LF_idx]["eta"]) <= 1.479' :
                                  [
                                   'abs(electron_col[LF_idx]["dxy"]) < 0.05' ,
                                   'abs(electron_col[LF_idx]["dz"]) < 0.1'  ,
                                  ] ,
                                # EndCap
                                'abs(electron_col[LF_idx]["eta"]) > 1.479' :
                                  [
                                   'electron_col[LF_idx]["sieie"] < 0.03 ' ,                           
                                   'abs(electron_col[LF_idx]["eInvMinusPInv"]) < 0.014' ,
                                   'abs(electron_col[LF_idx]["dxy"]) < 0.1' ,
                                   'abs(electron_col[LF_idx]["dz"]) < 0.2'  ,
                                  ] ,
                                   },
                       } ,

                 } ,
 
# ------------ 
'TightObjWP' : {

          'mvaFall17Iso_WP90':  {
                         'cuts' : { 
                                # Common cuts 
                                'True' :
                                   [
                                     'abs(electron_col[LF_idx]["eta"]) < 2.5' ,
                                     'electron_col[LF_idx]["mvaFall17Iso_WP90"]',
                                     'electron_col[LF_idx]["cutBased"]>=3',
                                     'electron_col[LF_idx]["convVeto"] == 1',
                                     'electron_col[LF_idx]["pfRelIso03_all"] < 0.06',
                                   ] ,
                                # Barrel
                                 'abs(electron_col[LF_idx]["eta"]) <= 1.479' :
                                   [
                                     'abs(electron_col[LF_idx]["dxy"]) < 0.05' ,
                                     'abs(electron_col[LF_idx]["dz"]) < 0.1'  ,
                                   ] ,
                                 # EndCap
                                 'abs(electron_col[LF_idx]["eta"]) > 1.479' :
                                   [
                                     'electron_col[LF_idx]["sieie"] < 0.03 ' ,             
                                     'abs(electron_col[LF_idx]["eInvMinusPInv"]) < 0.014' ,
                                     'abs(electron_col[LF_idx]["dxy"]) < 0.1' ,
                                     'abs(electron_col[LF_idx]["dz"]) < 0.2'  ,
                                   ] ,
                                  } ,
                         'tkSF':  { 
                                    '1-1' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/egammaEffi.txt_EGM2D_runB_passingRECO_combineLowEt.root',
                                    '2-2' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/egammaEffi.txt_EGM2D_runC_passingRECO_combineLowEt.root',
                                    '3-3' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/egammaEffi.txt_EGM2D_runD_passingRECO_combineLowEt.root',
                                    '4-4' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/egammaEffi.txt_EGM2D_runE_passingRECO_combineLowEt.root',
                                    '5-5' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/egammaEffi.txt_EGM2D_runF_passingRECO_combineLowEt.root',
                                  } ,
                         'wpSF':  {
                                    '1-1' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017v2LP19/egammaEffi_passingMVA94Xwp90isoHWWiso0p06_runB.txt' ,
                                    '2-2' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017v2LP19/egammaEffi_passingMVA94Xwp90isoHWWiso0p06_runCD.txt' ,
                                    '3-3' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017v2LP19/egammaEffi_passingMVA94Xwp90isoHWWiso0p06_runCD.txt' ,
                                    '4-4' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017v2LP19/egammaEffi_passingMVA94Xwp90isoHWWiso0p06_runE.txt' ,
                                    '5-5' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017v2LP19/egammaEffi_passingMVA94Xwp90isoHWWiso0p06_runF.txt' ,
                                  } ,
                         'fakeW' : '/LatinoAnalysis/NanoGardener/python/data/fake_prompt_rates/Full2017LP19/',
                              } ,
 
          'mvaFall17Iso_WP90_SS':  {
                         'cuts' : { 
                                # Common cuts 
                                'True' :
                                   [
                                     'abs(electron_col[LF_idx]["eta"]) < 2.5' ,
                                     'electron_col[LF_idx]["mvaFall17Iso_WP90"]',
                                     'electron_col[LF_idx]["cutBased"]>=3',
                                     'electron_col[LF_idx]["convVeto"] == 1',
                                     'electron_col[LF_idx]["pfRelIso03_all"] < 0.06',  
                                     'electron_col[LF_idx]["tightCharge"] == 2',
                                   ] ,
                                # Barrel
                                 'abs(electron_col[LF_idx]["eta"]) <= 1.479' :
                                   [
                                     'abs(electron_col[LF_idx]["dxy"]) < 0.05' ,
                                     'abs(electron_col[LF_idx]["dz"]) < 0.1'  ,
                                   ] ,
                                 # EndCap
                                 'abs(electron_col[LF_idx]["eta"]) > 1.479' :
                                   [
                                     'electron_col[LF_idx]["sieie"] < 0.03 ' ,             
                                     'abs(electron_col[LF_idx]["eInvMinusPInv"]) < 0.014' ,
                                     'abs(electron_col[LF_idx]["dxy"]) < 0.1' ,
                                     'abs(electron_col[LF_idx]["dz"]) < 0.2'  ,
                                   ] ,
                                  } ,
                         'tkSF':  { 
                                    '1-1' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/egammaEffi.txt_EGM2D_runB_passingRECO_combineLowEt.root',
                                    '2-2' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/egammaEffi.txt_EGM2D_runC_passingRECO_combineLowEt.root',
                                    '3-3' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/egammaEffi.txt_EGM2D_runD_passingRECO_combineLowEt.root',
                                    '4-4' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/egammaEffi.txt_EGM2D_runE_passingRECO_combineLowEt.root',
                                    '5-5' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/egammaEffi.txt_EGM2D_runF_passingRECO_combineLowEt.root',
                                  } ,
                         'wpSF':  {
                                    '1-1' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/egammaEffi_passingMVA94Xwp90isoSSHWW_runB.txt',
                                    '2-2' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/egammaEffi_passingMVA94Xwp90isoSSHWW_runC.txt',
                                    '3-3' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/egammaEffi_passingMVA94Xwp90isoSSHWW_runD.txt',
                                    '4-4' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/egammaEffi_passingMVA94Xwp90isoSSHWW_runE.txt',
                                    '5-5' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/egammaEffi_passingMVA94Xwp90isoSSHWW_runF.txt',
                                  } ,
                         'fakeW' : '/LatinoAnalysis/NanoGardener/python/data/fake_prompt_rates/Full2017LP19/',
                              } ,

             },

 # ------------ 
 'WgStarObjWP' : {

         'mvaFall17Iso_WP90' : {
                         'cuts' : { 
                                # Common cuts
                                'True' :
                                  [
                                     'abs(electron_col[LF_idx]["eta"]) < 2.5' ,
                                     'electron_col[LF_idx]["mvaFall17noIso_WP90"]',
                                     'electron_col[LF_idx]["convVeto"] == 1',
                                     'electron_col[LF_idx]["cutBased"]>=3',
                                  ] ,
                                # Barrel
                                'abs(electron_col[LF_idx]["eta"]) <= 1.479' :
                                  [
                                     'abs(electron_col[LF_idx]["dxy"]) < 0.05' ,
                                     'abs(electron_col[LF_idx]["dz"]) < 0.1'  ,
                                  ] ,
                                # EndCap
                                'abs(electron_col[LF_idx]["eta"]) > 1.479' :
                                  [
                                     'electron_col[LF_idx]["sieie"] < 0.03 ' ,             
                                     'abs(electron_col[LF_idx]["eInvMinusPInv"]) < 0.014' ,
                                     'abs(electron_col[LF_idx]["dxy"]) < 0.1' ,
                                     'abs(electron_col[LF_idx]["dz"]) < 0.2'  ,
                                  ] ,
                                  } ,
                         'cuts_iso': {
                                # Common cuts
                                'True' :
                                [
                                  'None',
                                ],
                                # Barrel
                                'abs(electron_col[LF_idx]["eta"]) <= 1.479' :
                                [
                                  '0.25' 
                                ],
                                # EndCap
                                'abs(electron_col[LF_idx]["eta"]) > 1.479' :
                                [
                                  '0.2' 
                                ],
                                  },
                         'iso': ['pfRelIso03_all', 0.3],
                         'tkSF':  {
                                    '1-1' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/egammaEffi.txt_EGM2D_runB_passingRECO_combineLowEt.root',
                                    '2-2' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/egammaEffi.txt_EGM2D_runC_passingRECO_combineLowEt.root',
                                    '3-3' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/egammaEffi.txt_EGM2D_runD_passingRECO_combineLowEt.root',
                                    '4-4' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/egammaEffi.txt_EGM2D_runE_passingRECO_combineLowEt.root',
                                    '5-5' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/egammaEffi.txt_EGM2D_runF_passingRECO_combineLowEt.root',
                                  } ,
                         'wpSF':  {
                                    '1-1' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/egammaEffi_passingMVA94Xwp90isoHWW_runB.txt' ,
                                    '2-2' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/egammaEffi_passingMVA94Xwp90isoHWW_runC.txt' ,
                                    '3-3' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/egammaEffi_passingMVA94Xwp90isoHWW_runD.txt' ,
                                    '4-4' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/egammaEffi_passingMVA94Xwp90isoHWW_runE.txt' ,
                                    '5-5' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/egammaEffi_passingMVA94Xwp90isoHWW_runF.txt' ,
                                  } ,
                             } ,

                 } ,

},

###____________________Full2017v2__________________________
'Full2017v2': {


## ------------  

 'VetoObjWP' : { 
           'HLTsafe' : { 
                         'cuts' : { 
                               # Common cuts
                               'True' :
                                [
                                  'False'
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
                                   'abs(electron_col[LF_idx]["eta"]) < 2.5' ,
                                   'electron_col[LF_idx]["cutBased"] >= 1',
                                  ] ,             
                                # Barrel
                                'abs(electron_col[LF_idx]["eta"]) <= 1.479' :
                                  [
                                   'abs(electron_col[LF_idx]["dxy"]) < 0.05' ,
                                   'abs(electron_col[LF_idx]["dz"]) < 0.1'  ,
                                  ] ,
                                # EndCap
                                'abs(electron_col[LF_idx]["eta"]) > 1.479' :
                                  [
                                   'electron_col[LF_idx]["sieie"] < 0.03 ' ,                           
                                   'abs(electron_col[LF_idx]["eInvMinusPInv"]) < 0.014' ,
                                   'abs(electron_col[LF_idx]["dxy"]) < 0.1' ,
                                   'abs(electron_col[LF_idx]["dz"]) < 0.2'  ,
                                  ] ,
                                   },
                       } ,

                 } ,
 
# ------------ 
'TightObjWP' : {

          'mvaFall17Iso_WP90':  {
                         'cuts' : { 
                                # Common cuts 
                                'True' :
                                   [
                                     'abs(electron_col[LF_idx]["eta"]) < 2.5' ,
                                     'electron_col[LF_idx]["mvaFall17Iso_WP90"]',
                                     'electron_col[LF_idx]["convVeto"] == 1',
                                   ] ,
                                # Barrel
                                 'abs(electron_col[LF_idx]["eta"]) <= 1.479' :
                                   [
                                     'abs(electron_col[LF_idx]["dxy"]) < 0.05' ,
                                     'abs(electron_col[LF_idx]["dz"]) < 0.1'  ,
                                   ] ,
                                 # EndCap
                                 'abs(electron_col[LF_idx]["eta"]) > 1.479' :
                                   [
                                     'abs(electron_col[LF_idx]["dxy"]) < 0.1' ,
                                     'abs(electron_col[LF_idx]["dz"]) < 0.2'  ,
                                   ] ,
                                  } ,
                         'tkSF':  { 
                                    '1-1' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/egammaEffi.txt_EGM2D_runB_passingRECO_combineLowEt.root',
                                    '2-2' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/egammaEffi.txt_EGM2D_runC_passingRECO_combineLowEt.root',
                                    '3-3' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/egammaEffi.txt_EGM2D_runD_passingRECO_combineLowEt.root',
                                    '4-4' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/egammaEffi.txt_EGM2D_runE_passingRECO_combineLowEt.root',
                                    '5-5' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/egammaEffi.txt_EGM2D_runF_passingRECO_combineLowEt.root',
                                  } ,
                         'wpSF':  {
                                    '1-1' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/egammaEffi_passingMVA94Xwp90isoHWW_runB.txt' ,
                                    '2-2' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/egammaEffi_passingMVA94Xwp90isoHWW_runC.txt' ,
                                    '3-3' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/egammaEffi_passingMVA94Xwp90isoHWW_runD.txt' ,
                                    '4-4' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/egammaEffi_passingMVA94Xwp90isoHWW_runE.txt' ,
                                    '5-5' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/egammaEffi_passingMVA94Xwp90isoHWW_runF.txt' ,
                                  } ,
                         'fakeW' : '/LatinoAnalysis/NanoGardener/python/data/fake_prompt_rates/Full2017v2p2NewBinning/',
                              } ,
 
          'mvaFall17Iso_WP90_SS':  {
                         'cuts' : { 
                                # Common cuts 
                                'True' :
                                   [
                                     'abs(electron_col[LF_idx]["eta"]) < 2.5' ,
                                     'electron_col[LF_idx]["mvaFall17Iso_WP90"]',
                                     'electron_col[LF_idx]["convVeto"] == 1',
                                     'electron_col[LF_idx]["tightCharge"] == 2',
                                   ] ,
                                # Barrel
                                 'abs(electron_col[LF_idx]["eta"]) <= 1.479' :
                                   [
                                     'abs(electron_col[LF_idx]["dxy"]) < 0.05' ,
                                     'abs(electron_col[LF_idx]["dz"]) < 0.1'  ,
                                   ] ,
                                 # EndCap
                                 'abs(electron_col[LF_idx]["eta"]) > 1.479' :
                                   [
                                     'abs(electron_col[LF_idx]["dxy"]) < 0.1' ,
                                     'abs(electron_col[LF_idx]["dz"]) < 0.2'  ,
                                   ] ,
                                  } ,
                         'tkSF':  { 
                                    '1-1' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/egammaEffi.txt_EGM2D_runB_passingRECO_combineLowEt.root',
                                    '2-2' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/egammaEffi.txt_EGM2D_runC_passingRECO_combineLowEt.root',
                                    '3-3' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/egammaEffi.txt_EGM2D_runD_passingRECO_combineLowEt.root',
                                    '4-4' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/egammaEffi.txt_EGM2D_runE_passingRECO_combineLowEt.root',
                                    '5-5' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/egammaEffi.txt_EGM2D_runF_passingRECO_combineLowEt.root',
                                  } ,
                         'wpSF':  {
                                    '1-1' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/egammaEffi_passingMVA94Xwp90isoSSHWW_runB.txt',
                                    '2-2' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/egammaEffi_passingMVA94Xwp90isoSSHWW_runC.txt',
                                    '3-3' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/egammaEffi_passingMVA94Xwp90isoSSHWW_runD.txt',
                                    '4-4' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/egammaEffi_passingMVA94Xwp90isoSSHWW_runE.txt',
                                    '5-5' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/egammaEffi_passingMVA94Xwp90isoSSHWW_runF.txt',
                                  } ,
                         'fakeW' : '/LatinoAnalysis/NanoGardener/python/data/fake_prompt_rates/Full2017v2p2NewBinning/',
                              } ,

             },

 # ------------ 
 'WgStarObjWP' : {

         'mvaFall17Iso_WP90' : {
                         'cuts' : { 
                                # Common cuts
                                'True' :
                                  [
                                     'abs(electron_col[LF_idx]["eta"]) < 2.5' ,
                                     'electron_col[LF_idx]["mvaFall17noIso_WP90"]',
                                     'electron_col[LF_idx]["convVeto"] == 1',
                                  ] ,
                                # Barrel
                                'abs(electron_col[LF_idx]["eta"]) <= 1.479' :
                                  [
                                     'abs(electron_col[LF_idx]["dxy"]) < 0.05' ,
                                     'abs(electron_col[LF_idx]["dz"]) < 0.1'  ,
                                  ] ,
                                # EndCap
                                'abs(electron_col[LF_idx]["eta"]) > 1.479' :
                                  [
                                     'abs(electron_col[LF_idx]["dxy"]) < 0.1' ,
                                     'abs(electron_col[LF_idx]["dz"]) < 0.2'  ,
                                  ] ,
                                  } ,
                         'cuts_iso': {
                                # Common cuts
                                'True' :
                                [
                                  'None',
                                ],
                                # Barrel
                                'abs(electron_col[LF_idx]["eta"]) <= 1.479' :
                                [
                                  '0.25' 
                                ],
                                # EndCap
                                'abs(electron_col[LF_idx]["eta"]) > 1.479' :
                                [
                                  '0.2' 
                                ],
                                  },
                         'iso': ['pfRelIso03_all', 0.3],
                         'tkSF':  {
                                    '1-1' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/egammaEffi.txt_EGM2D_runB_passingRECO_combineLowEt.root',
                                    '2-2' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/egammaEffi.txt_EGM2D_runC_passingRECO_combineLowEt.root',
                                    '3-3' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/egammaEffi.txt_EGM2D_runD_passingRECO_combineLowEt.root',
                                    '4-4' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/egammaEffi.txt_EGM2D_runE_passingRECO_combineLowEt.root',
                                    '5-5' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/egammaEffi.txt_EGM2D_runF_passingRECO_combineLowEt.root',
                                  } ,
                         'wpSF':  {
                                    '1-1' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/egammaEffi_passingMVA94Xwp90isoHWW_runB.txt' ,
                                    '2-2' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/egammaEffi_passingMVA94Xwp90isoHWW_runC.txt' ,
                                    '3-3' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/egammaEffi_passingMVA94Xwp90isoHWW_runD.txt' ,
                                    '4-4' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/egammaEffi_passingMVA94Xwp90isoHWW_runE.txt' ,
                                    '5-5' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/egammaEffi_passingMVA94Xwp90isoHWW_runF.txt' ,
                                  } ,
                             } ,

                 } ,

},

###____________________Full2017__________________________
'Full2017': {


## ------------  

 'VetoObjWP' : { 
           'HLTsafe' : { 
                         'cuts' : { 
                               # Common cuts
                               'True' :
                                [
                                  'False'
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
                                   'abs(electron_col[LF_idx]["eta"]) < 2.5' ,
                                   'electron_col[LF_idx]["lostHits"] < 2',
                                   'electron_col[LF_idx]["convVeto"] == 1',
                                   'abs(electron_col[LF_idx]["eInvMinusPInv"]) < 0.013' ,
                                   '(electron_col[LF_idx]["dr03TkSumPt"]/electron_col[LF_idx]["pt"]) < 0.08',
                                  ] ,             
                                # Barrel
                                'abs(electron_col[LF_idx]["eta"]) <= 1.479' :
                                  [
                                   'electron_col[LF_idx]["sieie"] < 0.011'  ,
                                   'abs(electron_col[LF_idx]["deltaEtaSC"]) < 0.004'  ,
                                   'electron_col[LF_idx]["hoe"] < 0.06' ,
                                   'electron_col[LF_idx]["pfRelIso03_all"] < 0.04',
                                   '(electron_col[LF_idx]["dr03EcalRecHitSumEt"]/electron_col[LF_idx]["pt"]) < 0.15',
                                   '(electron_col[LF_idx]["dr03HcalDepth1TowerSumEt"]/electron_col[LF_idx]["pt"]) < 0.12',
                                   'abs(electron_col[LF_idx]["dxy"]) < 0.05' ,
                                   'abs(electron_col[LF_idx]["dz"]) < 0.1'  ,
                                  ] ,
                                # EndCap
                                'abs(electron_col[LF_idx]["eta"]) > 1.479' :
                                  [
                                   'electron_col[LF_idx]["sieie"] < 0.03'  ,
                                   'abs(electron_col[LF_idx]["deltaEtaSC"]) < 0.006'  ,
                                   'electron_col[LF_idx]["hoe"] < 0.07' ,
                                   'electron_col[LF_idx]["pfRelIso03_all"] < 0.12',
                                   '(electron_col[LF_idx]["dr03EcalRecHitSumEt"]/electron_col[LF_idx]["pt"]) < 0.13',
                                   '(electron_col[LF_idx]["dr03HcalDepth1TowerSumEt"]/electron_col[LF_idx]["pt"]) < 0.08',
                                   'abs(electron_col[LF_idx]["dxy"]) < 0.1' ,
                                   'abs(electron_col[LF_idx]["dz"]) < 0.2'  ,
                                  ] ,
                                   },
                       } ,

                 } ,
 
# ------------ 
'TightObjWP' : {

          'mvaFall17Iso_WP90':  {
                         'cuts' : { 
                                # Common cuts 
                                'True' :
                                   [
                                     'abs(electron_col[LF_idx]["eta"]) < 2.5' ,
                                     'electron_col[LF_idx]["mvaFall17Iso_WP90"]',
                                     'electron_col[LF_idx]["lostHits"] < 1',
                                   ] ,
                                # Barrel
                                 'abs(electron_col[LF_idx]["eta"]) <= 1.479' :
                                   [
                                     'abs(electron_col[LF_idx]["dxy"]) < 0.05' ,
                                     'abs(electron_col[LF_idx]["dz"]) < 0.1'  ,
                                   ] ,
                                 # EndCap
                                 'abs(electron_col[LF_idx]["eta"]) > 1.479' :
                                   [
                                     'abs(electron_col[LF_idx]["dxy"]) < 0.1' ,
                                     'abs(electron_col[LF_idx]["dz"]) < 0.2'  ,
                                   ] ,
                                  } ,
                         'tkSF':  { 
                                    '1-5' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/egammaEffi.txt_EGM2D_runBCDEF_passingRECO_combined.root',
                                  } ,
                         'wpSF':  {
                                    '1-5' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/egammaEffi_passingMVA94Xwp90isoHWW.txt' ,
                                  } ,
                         'fakeW' : '/LatinoAnalysis/NanoGardener/python/data/fake_prompt_rates/Full2017/',
                              } ,
 
          'mvaFall17Iso_WP90_SS':  {
                         'cuts' : { 
                                # Common cuts 
                                'True' :
                                   [
                                     'abs(electron_col[LF_idx]["eta"]) < 2.5' ,
                                     'electron_col[LF_idx]["mvaFall17Iso_WP90"]',
                                     'electron_col[LF_idx]["lostHits"] < 1',
                                     'electron_col[LF_idx]["tightCharge"] == 2',
                                   ] ,
                                # Barrel
                                 'abs(electron_col[LF_idx]["eta"]) <= 1.479' :
                                   [
                                     'abs(electron_col[LF_idx]["dxy"]) < 0.05' ,
                                     'abs(electron_col[LF_idx]["dz"]) < 0.1'  ,
                                   ] ,
                                 # EndCap
                                 'abs(electron_col[LF_idx]["eta"]) > 1.479' :
                                   [
                                     'abs(electron_col[LF_idx]["dxy"]) < 0.1' ,
                                     'abs(electron_col[LF_idx]["dz"]) < 0.2'  ,
                                   ] ,
                                  } ,
                         'tkSF':  { 
                                    '1-5' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/egammaEffi.txt_EGM2D_runBCDEF_passingRECO_combined.root' ,
                                  } ,
                         'wpSF':  {
                                    '1-5' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/egammaEffi_passingMVA94Xwp90isoSSHWW.txt' ,
                                  } ,
                         'fakeW' : '/LatinoAnalysis/NanoGardener/python/data/fake_prompt_rates/Full2017/',
                              } ,

             },

 # ------------ 
 'WgStarObjWP' : {

         'mvaFall17Iso_WP90' : {
                         'cuts' : { 
                                # Common cuts
                                'True' :
                                  [
                                     'abs(electron_col[LF_idx]["eta"]) < 2.5' ,
                                     'electron_col[LF_idx]["mvaFall17noIso_WP90"]',
                                     'electron_col[LF_idx]["lostHits"] < 1',
                                  ] ,
                                # Barrel
                                'abs(electron_col[LF_idx]["eta"]) <= 1.479' :
                                  [
                                     'abs(electron_col[LF_idx]["dxy"]) < 0.05' ,
                                     'abs(electron_col[LF_idx]["dz"]) < 0.1'  ,
                                  ] ,
                                # EndCap
                                'abs(electron_col[LF_idx]["eta"]) > 1.479' :
                                  [
                                     'abs(electron_col[LF_idx]["dxy"]) < 0.1' ,
                                     'abs(electron_col[LF_idx]["dz"]) < 0.2'  ,
                                  ] ,
                                  } ,
                         'cuts_iso': {
                                # Common cuts
                                'True' :
                                [
                                  'None',
                                ],
                                # Barrel
                                'abs(electron_col[LF_idx]["eta"]) <= 1.479' :
                                [
                                  '0.25' 
                                ],
                                # EndCap
                                'abs(electron_col[LF_idx]["eta"]) > 1.479' :
                                [
                                  '0.2' 
                                ],
                                  },
                         'iso': ['pfRelIso03_all', 0.3],
                             } ,

                 } ,

},

###____________________Study2017__________________________
'Study2017': {

## ------------  

 'VetoObjWP' : { 
           'HLTsafe' : { 
                         'cuts' : { 
                               # Common cuts
                               'True' :
                                [
                                  'False'
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
                                   #'abs(electron_col[LF_idx]["eta"]) < 2.5' ,
                                   'electron_col[LF_idx]["lostHits"] < 2',
                                   'electron_col[LF_idx]["convVeto"] == 1',
                                   'abs(electron_col[LF_idx]["eInvMinusPInv"]) < 0.013' ,
                                   #'electron_col[LF_idx]["pfRelIso03_all"] < 0.06',
                                   'electron_col[LF_idx]["dr03TkSumPt"] < 0.1',
                                   '(electron_col[LF_idx]["dr03HcalDepth1TowerSumEt"]/electron_col[LF_idx]["pt"]) < 0.12',
                                  ] ,             
                                # Barrel
                                'abs(electron_col[LF_idx]["eta"]) <= 1.479' :
                                  [
                                   #'abs(electron_col[LF_idx]["dxy"]) < 0.05' ,
                                   #'abs(electron_col[LF_idx]["dz"]) < 0.1'  ,
                                   'abs(electron_col[LF_idx]["deltaEtaSC"]) < 0.004'  ,
                                   'electron_col[LF_idx]["sieie"] < 0.011'  ,
                                   'electron_col[LF_idx]["hoe"] < 0.06' ,
                                   '(electron_col[LF_idx]["dr03EcalRecHitSumEt"]/electron_col[LF_idx]["pt"]) < 0.15',
                                  ] ,
                                # EndCap
                                'abs(electron_col[LF_idx]["eta"]) > 1.479' :
                                  [
                                   #'abs(electron_col[LF_idx]["dxy"]) < 0.1' ,
                                   #'abs(electron_col[LF_idx]["dz"]) < 0.2'  ,
                                   'electron_col[LF_idx]["sieie"] < 0.03'  ,
                                   'electron_col[LF_idx]["hoe"] < 0.07' ,
                                   '(electron_col[LF_idx]["dr03EcalRecHitSumEt"]/electron_col[LF_idx]["pt"]) < 0.13',
                                  ] ,
                                   },
                       } ,

                 } ,

 # ------------ 
 'TightObjWP' : {

         'TightFall17' : {
                         'cuts' : { 
                                # Common cuts
                                'True' :
                                  [
                                    'abs(electron_col[LF_idx]["eta"]) < 2.5' ,
                                    'electron_col[LF_idx]["cutBased"] == 4', 
                                    'electron_col[LF_idx]["lostHits"] < 1',
                                  ] , 
                                # Barrel
                                'abs(electron_col[LF_idx]["eta"]) <= 1.479' :
                                  [
                                    'abs(electron_col[LF_idx]["dxy"]) < 0.05' ,
                                    'abs(electron_col[LF_idx]["dz"]) < 0.1'  ,
                                  ] ,
                                # EndCap
                                'abs(electron_col[LF_idx]["eta"]) > 1.479' :
                                  [
                                    'abs(electron_col[LF_idx]["dxy"]) < 0.1' ,
                                    'abs(electron_col[LF_idx]["dz"]) < 0.2'  ,
                                  ] ,
                                  } ,
                          },

          'mvaFall17noIso_WPL':  {
                         'cuts' : { 
                                # Common cuts 
                                'True' :
                                   [
                                     #'abs(electron_col[LF_idx]["eta"]) < 2.5' ,
                                     'electron_col[LF_idx]["mvaFall17noIso_WPL"]',
                                     #'electron_col[LF_idx]["lostHits"] < 1',
                                   ] ,
                                # Barrel
                                 'abs(electron_col[LF_idx]["eta"]) <= 1.479' :
                                   [
                                     #'abs(electron_col[LF_idx]["dxy"]) < 0.05' ,
                                     #'abs(electron_col[LF_idx]["dz"]) < 0.1'  ,
                                   ] ,
                                 # EndCap
                                 'abs(electron_col[LF_idx]["eta"]) > 1.479' :
                                   [
                                     #'abs(electron_col[LF_idx]["dxy"]) < 0.1' ,
                                     #'abs(electron_col[LF_idx]["dz"]) < 0.2'  ,
                                   ] ,
                                  } ,
                              } ,
 
          'mvaFall17Iso_WPL':  {
                         'cuts' : { 
                                # Common cuts 
                                'True' :
                                   [
                                     #'abs(electron_col[LF_idx]["eta"]) < 2.5' ,
                                     'electron_col[LF_idx]["mvaFall17Iso_WPL"]',
                                     #'electron_col[LF_idx]["lostHits"] < 1',
                                   ] ,
                                # Barrel
                                 'abs(electron_col[LF_idx]["eta"]) <= 1.479' :
                                   [
                                     #'abs(electron_col[LF_idx]["dxy"]) < 0.05' ,
                                     #'abs(electron_col[LF_idx]["dz"]) < 0.1'  ,
                                   ] ,
                                 # EndCap
                                 'abs(electron_col[LF_idx]["eta"]) > 1.479' :
                                   [
                                     #'abs(electron_col[LF_idx]["dxy"]) < 0.1' ,
                                     #'abs(electron_col[LF_idx]["dz"]) < 0.2'  ,
                                   ] ,
                                  } ,
                              } ,
 
         'mvaFall17noIso_WP80' : {
                         'cuts' : { 
                                # Common cuts
                                'True' :
                                  [
                                    #'abs(electron_col[LF_idx]["eta"]) < 2.5' ,
                                    'electron_col[LF_idx]["mvaFall17noIso_WP80"]',
                                    #'electron_col[LF_idx]["cutBased"] == 4', 
                                    #'electron_col[LF_idx]["lostHits"] < 1',
                                  ] , 
                                # Barrel
                                'abs(electron_col[LF_idx]["eta"]) <= 1.479' :
                                  [
                                    #'abs(electron_col[LF_idx]["dxy"]) < 0.05' ,
                                    #'abs(electron_col[LF_idx]["dz"]) < 0.1'  ,
                                  ] ,
                                # EndCap
                                'abs(electron_col[LF_idx]["eta"]) > 1.479' :
                                  [
                                    #'abs(electron_col[LF_idx]["dxy"]) < 0.1' ,
                                    #'abs(electron_col[LF_idx]["dz"]) < 0.2'  ,
                                  ] ,
                                  } ,
                             } ,


          'mvaFall17Iso_WP80':  {
                         'cuts' : { 
                                # Common cuts 
                                'True' :
                                   [
                                     #'abs(electron_col[LF_idx]["eta"]) < 2.5' ,
                                     'electron_col[LF_idx]["mvaFall17Iso_WP80"]',
                                     #'electron_col[LF_idx]["lostHits"] < 1',
                                   ] ,
                                # Barrel
                                 'abs(electron_col[LF_idx]["eta"]) <= 1.479' :
                                   [
                                     #'abs(electron_col[LF_idx]["dxy"]) < 0.05' ,
                                     #'abs(electron_col[LF_idx]["dz"]) < 0.1'  ,
                                   ] ,
                                 # EndCap
                                 'abs(electron_col[LF_idx]["eta"]) > 1.479' :
                                   [
                                     #'abs(electron_col[LF_idx]["dxy"]) < 0.1' ,
                                     #'abs(electron_col[LF_idx]["dz"]) < 0.2'  ,
                                   ] ,
                                  } ,
                              } ,
 
          'mvaFall17noIso_WP90':  {
                         'cuts' : { 
                                # Common cuts 
                                'True' :
                                   [
                                     #'abs(electron_col[LF_idx]["eta"]) < 2.5' ,
                                     'electron_col[LF_idx]["mvaFall17noIso_WP90"]',
                                     #'electron_col[LF_idx]["lostHits"] < 1',
                                   ] ,
                                # Barrel
                                 'abs(electron_col[LF_idx]["eta"]) <= 1.479' :
                                   [
                                     #'abs(electron_col[LF_idx]["dxy"]) < 0.05' ,
                                     #'abs(electron_col[LF_idx]["dz"]) < 0.1'  ,
                                   ] ,
                                 # EndCap
                                 'abs(electron_col[LF_idx]["eta"]) > 1.479' :
                                   [
                                     #'abs(electron_col[LF_idx]["dxy"]) < 0.1' ,
                                     #'abs(electron_col[LF_idx]["dz"]) < 0.2'  ,
                                   ] ,
                                  } ,
                              } ,
 
          'mvaFall17Iso_WP90':  {
                         'cuts' : { 
                                # Common cuts 
                                'True' :
                                   [
                                     #'abs(electron_col[LF_idx]["eta"]) < 2.5' ,
                                     'electron_col[LF_idx]["mvaFall17Iso_WP90"]',
                                     #'electron_col[LF_idx]["lostHits"] < 1',
                                   ] ,
                                # Barrel
                                 'abs(electron_col[LF_idx]["eta"]) <= 1.479' :
                                   [
                                     #'abs(electron_col[LF_idx]["dxy"]) < 0.05' ,
                                     #'abs(electron_col[LF_idx]["dz"]) < 0.1'  ,
                                   ] ,
                                 # EndCap
                                 'abs(electron_col[LF_idx]["eta"]) > 1.479' :
                                   [
                                     #'abs(electron_col[LF_idx]["dxy"]) < 0.1' ,
                                     #'abs(electron_col[LF_idx]["dz"]) < 0.2'  ,
                                   ] ,
                                  } ,
                              } ,
 
                  } ,
 
 # ------------ 
 'WgStarObjWP' : {

         'cut_WP_Tight80X' : {
                         'cuts' : { 
                                # Common cuts
                                'True' :
                                  [
                                    'False'
                                    #'abs(electron_col[LF_idx]["eta"]) < 2.5' ,
                                    ##'electron_col[LF_idx]["cutBased_HLTPreSel"] == 1',
                                    ##'electron_col[LF_idx]["cutBased"] == 4',
                                    #'electron_col[LF_idx]["lostHits"] < 1',
                                    #'electron_col[LF_idx]["convVeto"]',
                                    #'electron_col[LF_idx]["tightCharge"] == 2',
                                  ] ,
                                # Barrel
                                'abs(electron_col[LF_idx]["eta"]) <= 1.479' :
                                  [
                                    #'abs(electron_col[LF_idx]["dxy"]) < 0.05' ,
                                    #'abs(electron_col[LF_idx]["dz"]) < 0.1'  ,
                                    #'electron_col[LF_idx]["sieie"] < 0.00998',
                                    ##'electron_col[LF_idx]["deltaEtaSC"] < 0.00308',
                                    ##'itree.std_vector_electron_dPhiIn"][LF_idx] < 0.0816',
                                    #'electron_col[LF_idx]["hoe"] < 0.0414',
                                    #'electron_col[LF_idx]["eInvMinusPInv"] < 0.0129',
                                    #'(electron_col[LF_idx]["pfRelIso03_all"] - self.ConeOverlapPt(lepton_col, iLep)/electron_col[LF_idx]["pt"]) < 0.0588',                                  
                                  ] ,
                                # EndCap
                                'abs(electron_col[LF_idx]["eta"]) > 1.479' :
                                  [
                                    #'abs(electron_col[LF_idx]["dxy"]) < 0.1' ,
                                    #'abs(electron_col[LF_idx]["dz"]) < 0.2'  ,
                                    #'electron_col[LF_idx]["sieie"] < 0.0292',
                                    ##'electron_col[LF_idx]["deltaEtaSC"] < 0.00605',
                                    ##'itree.std_vector_electron_dPhiIn"][LF_idx] < 0.0394',
                                    #'electron_col[LF_idx]["hoe"] < 0.0641',
                                    #'electron_col[LF_idx]["eInvMinusPInv"] < 0.0129',
                                    #'(electron_col[LF_idx]["pfRelIso03_all"] - self.ConeOverlapPt(lepton_col, iLep)/electron_col[LF_idx]["pt"]) < 0.0571', 
                                  ] ,
                                  } ,
                             } ,

                 } ,
},



###____________________Full2016v4________ : for nAODv4
'Full2016v4': {

## ------------
 'VetoObjWP' : {
           'HLTsafe' : {
                         'cuts' : {
                               # Common cuts
                               'True' :
                                [
                                  'False'
                                  #'abs(electron_col[LF_idx]["eta"]) < 2.5' ,
                                  #'electron_col[LF_idx]["cutBased_HLTPreSel"] == 1 ' ,
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
                                   'abs(electron_col[LF_idx]["eta"]) < 2.5' ,
                                   'electron_col[LF_idx]["cutBased_HLTPreSel"] == 1 ' ,
                                   'electron_col[LF_idx]["lostHits"] < 1',
                                  ] ,             
                                # Barrel
                                'abs(electron_col[LF_idx]["eta"]) <= 1.479' :
                                  [
                                    'abs(electron_col[LF_idx]["dxy"]) < 0.05' ,
                                    'abs(electron_col[LF_idx]["dz"]) < 0.1'  ,
                                  ] ,
                                # EndCap
                                'abs(electron_col[LF_idx]["eta"]) > 1.479' :
                                  [
                                    'abs(electron_col[LF_idx]["dxy"]) < 0.1' ,
                                    'abs(electron_col[LF_idx]["dz"]) < 0.2'  ,
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
                                    'abs(electron_col[LF_idx]["eta"]) < 2.5' ,
                                    'electron_col[LF_idx]["cutBased_HLTPreSel"] == 1',
                                    'electron_col[LF_idx]["cutBased_Sum16"] == 4', 
                                    'electron_col[LF_idx]["lostHits"] < 1',
                                  ] , 
                                # Barrel
                                'abs(electron_col[LF_idx]["eta"]) <= 1.479' :
                                  [
                                    'abs(electron_col[LF_idx]["dxy"]) < 0.05' ,
                                    'abs(electron_col[LF_idx]["dz"]) < 0.1'  ,
                                  ] ,
                                # EndCap
                                'abs(electron_col[LF_idx]["eta"]) > 1.479' :
                                  [
                                    'abs(electron_col[LF_idx]["dxy"]) < 0.1' ,
                                    'abs(electron_col[LF_idx]["dz"]) < 0.2'  ,
                                  ] ,
                                  } ,
                         'tkSF':  { 
                                    '1-7' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2016v2/EGM2D_BtoH_combineLowEt_RecoSF_Legacy2016.root' ,
                                  } ,
                         'wpSF':  {
                                    '1-7' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2016v2/egammaEffi_passingTight80XHWW.txt' ,  
                                  } ,
                         'fakeW' : '/LatinoAnalysis/NanoGardener/python/data/fake_prompt_rates/Full2016/Tight80X/',
                             } ,

         'cut_WP_Tight80X_SS' : {
                         'cuts' : { 
                                # Common cuts
                                'True' :
                                  [
                                    'abs(electron_col[LF_idx]["eta"]) < 2.5' ,
                                    'electron_col[LF_idx]["cutBased_HLTPreSel"] == 1',
                                    'electron_col[LF_idx]["cutBased_Sum16"] == 4',
                                    'electron_col[LF_idx]["lostHits"] < 1',
                                    'electron_col[LF_idx]["tightCharge"] == 2',
                                  ] ,
                                # Barrel
                                'abs(electron_col[LF_idx]["eta"]) <= 1.479' :
                                  [
                                    'abs(electron_col[LF_idx]["dxy"]) < 0.05' ,
                                    'abs(electron_col[LF_idx]["dz"]) < 0.1'  ,
                                  ] ,
                                # EndCap
                                'abs(electron_col[LF_idx]["eta"]) > 1.479' :
                                  [
                                    'abs(electron_col[LF_idx]["dxy"]) < 0.1' ,
                                    'abs(electron_col[LF_idx]["dz"]) < 0.2'  ,
                                  ] ,
                                  } ,
                         'tkSF':  { 
                                    '1-7' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2016v2/EGM2D_BtoH_combineLowEt_RecoSF_Legacy2016.root' ,
                                  } ,
                         'wpSF':  {
                                    '1-7' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2016v2/egammaEffi_passingTight80XSSHWW.txt' ,
                                  } ,
                         'fakeW' : '/LatinoAnalysis/NanoGardener/python/data/fake_prompt_rates/Full2016/Tight80X_SS/',
                             } ,

          'mva_90p_Iso2016':  {
                         'cuts' : { 
                                # Common cuts 
                                'True' :
                                   [
                                     'abs(electron_col[LF_idx]["eta"]) < 2.5' ,
                                     'electron_col[LF_idx]["cutBased_HLTPreSel"] == 1',
                                     'electron_col[LF_idx]["mvaSpring16GP_WP90"]',
                                     'electron_col[LF_idx]["lostHits"] < 1',  
                                   ] ,
                                # Barrel
                                 'abs(electron_col[LF_idx]["eta"]) <= 1.479' :
                                   [
                                     'abs(electron_col[LF_idx]["dxy"]) < 0.05' ,
                                     'abs(electron_col[LF_idx]["dz"]) < 0.1'  ,
                                     'electron_col[LF_idx]["pfRelIso03_all"] < 0.05880',
                                   ] ,
                                 # EndCap
                                 'abs(electron_col[LF_idx]["eta"]) > 1.479' :
                                   [
                                     'abs(electron_col[LF_idx]["dxy"]) < 0.1' ,
                                     'abs(electron_col[LF_idx]["dz"]) < 0.2'  ,
                                     'electron_col[LF_idx]["pfRelIso03_all"] < 0.0571',
                                   ] ,
                                  } ,
                         'tkSF':  { 
                                    '1-7' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2016v2/EGM2D_BtoH_combineLowEt_RecoSF_Legacy2016.root' ,
                                  } ,
                         'wpSF':  {
                                    '1-7' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2016v2/egammaEffi_passingMVA80Xwp90HWW.txt' ,
                                  } ,
                         'fakeW' : '/LatinoAnalysis/NanoGardener/python/data/fake_prompt_rates/Full2016/mva90pIso2016/',
                              } ,

          'mva_90p_Iso2016_SS':  {
                         'cuts' : {
                                # Common cuts
                                'True' :
                                   [
                                     'abs(electron_col[LF_idx]["eta"]) < 2.5' ,
                                     'electron_col[LF_idx]["cutBased_HLTPreSel"] == 1',
                                     'electron_col[LF_idx]["mvaSpring16GP_WP90"]',
                                     'electron_col[LF_idx]["lostHits"] < 1',
                                     'electron_col[LF_idx]["tightCharge"] == 2',
                                   ] ,
                                # Barrel
                                 'abs(electron_col[LF_idx]["eta"]) <= 1.479' :
                                   [
                                     'abs(electron_col[LF_idx]["dxy"]) < 0.05' ,
                                     'abs(electron_col[LF_idx]["dz"]) < 0.1'  ,
                                     'electron_col[LF_idx]["pfRelIso03_all"] < 0.05880',
                                   ] ,
                                 # EndCap
                                 'abs(electron_col[LF_idx]["eta"]) > 1.479' :
                                   [
                                     'abs(electron_col[LF_idx]["dxy"]) < 0.1' ,
                                     'abs(electron_col[LF_idx]["dz"]) < 0.2'  ,
                                     'electron_col[LF_idx]["pfRelIso03_all"] < 0.0571',
                                   ] ,
                                  } ,
                         'tkSF':  {
                                    '1-7' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2016v2/EGM2D_BtoH_combineLowEt_RecoSF_Legacy2016.root' ,
                                  } ,
                         'wpSF':  {
                                    '1-7' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2016v2/egammaEffi_passingMVA80Xwp90SSHWW.txt' ,
                                  } ,
                         'fakeW' : '/LatinoAnalysis/NanoGardener/python/data/fake_prompt_rates/Full2016/mva90pIso2016_SS/',
                              } ,

                } ,

 # ------------ 
 'WgStarObjWP' : {

          'mva_90p_Iso2016':  {
                         'cuts' : {
                                # Common cuts
                                'True' :
                                   [
                                     'abs(electron_col[LF_idx]["eta"]) < 2.5' ,
                                     'electron_col[LF_idx]["cutBased_HLTPreSel"] == 1',
                                     'electron_col[LF_idx]["mvaSpring16GP_WP90"]',
                                     'electron_col[LF_idx]["lostHits"] < 1',
                                   ] ,
                                # Barrel
                                 'abs(electron_col[LF_idx]["eta"]) <= 1.479' :
                                   [
                                     'abs(electron_col[LF_idx]["dxy"]) < 0.05' ,
                                     'abs(electron_col[LF_idx]["dz"]) < 0.1'  ,
                                   ] ,
                                 # EndCap
                                 'abs(electron_col[LF_idx]["eta"]) > 1.479' :
                                   [
                                     'abs(electron_col[LF_idx]["dxy"]) < 0.1' ,
                                     'abs(electron_col[LF_idx]["dz"]) < 0.2'  ,
                                   ] ,
                                  } ,
                        'cuts_iso': {
                                # Common cuts
                                'True' :
                                [
                                  'None',
                                ],
                                # Barrel
                                'abs(electron_col[LF_idx]["eta"]) <= 1.479' :
                                [
                                 '0.05880'
                                ],
                                # EndCap
                                'abs(electron_col[LF_idx]["eta"]) > 1.479' :
                                [
                                 '0.0571'
                                ],
                                  },
                         'iso': ['pfRelIso03_all', 0.3],
                         'tkSF':  { 
                                    '1-7' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2016v2/EGM2D_BtoH_combineLowEt_RecoSF_Legacy2016.root' ,
                                  } ,
                         'wpSF':  {
                                    '1-7' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2016v2/egammaEffi_passingMVA80Xwp90HWW.txt' ,
                                  } ,
                         'fakeW' : '/LatinoAnalysis/NanoGardener/python/data/fake_prompt_rates/Full2016/mva90pIso2016/',        
                              } ,

                } ,
},


###____________________Full2016v5_mh ________ : for nAODv4 + monoH loose WP without tracker Iso
'Full2016v5_mh': {

## ------------
 'VetoObjWP' : {
           'HLTsafe' : {
                         'cuts' : {
                               # Common cuts
                               'True' :
                                [
                                  'False'
                                  #'abs(electron_col[LF_idx]["eta"]) < 2.5' ,
                                  #'electron_col[LF_idx]["cutBased_HLTPreSel"] == 1 ' ,
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
                                   'abs(electron_col[LF_idx]["eta"]) < 2.5' ,
                                   'electron_col[LF_idx]["cutBased_Fall17_V1"] >= 3',
                                   'electron_col[LF_idx]["convVeto"] == 1', 
                                  ] ,             
                                # Barrel
                                'abs(electron_col[LF_idx]["eta"]) <= 1.479' :
                                  [
                                   'abs(electron_col[LF_idx]["dxy"]) < 0.05' ,
                                   'abs(electron_col[LF_idx]["dz"]) < 0.1'  ,
                                  ] ,
                                # EndCap
                                'abs(electron_col[LF_idx]["eta"]) > 1.479' :
                                  [
                                   'electron_col[LF_idx]["sieie"] < 0.03 ' ,                           
                                   'abs(electron_col[LF_idx]["eInvMinusPInv"]) < 0.014' ,
                                   'abs(electron_col[LF_idx]["dxy"]) < 0.1' ,
                                   'abs(electron_col[LF_idx]["dz"]) < 0.2'  ,
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
                                    'abs(electron_col[LF_idx]["eta"]) < 2.5' ,
                                    'electron_col[LF_idx]["cutBased_HLTPreSel"] == 1',
                                    'electron_col[LF_idx]["cutBased_Sum16"] == 4', 
                                    'electron_col[LF_idx]["lostHits"] < 1',
                                  ] , 
                                # Barrel
                                'abs(electron_col[LF_idx]["eta"]) <= 1.479' :
                                  [
                                    'abs(electron_col[LF_idx]["dxy"]) < 0.05' ,
                                    'abs(electron_col[LF_idx]["dz"]) < 0.1'  ,
                                  ] ,
                                # EndCap
                                'abs(electron_col[LF_idx]["eta"]) > 1.479' :
                                  [
                                    'abs(electron_col[LF_idx]["dxy"]) < 0.1' ,
                                    'abs(electron_col[LF_idx]["dz"]) < 0.2'  ,
                                  ] ,
                                  } ,
                         'tkSF':  { 
                                    '1-7' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2016v2/EGM2D_BtoH_combineLowEt_RecoSF_Legacy2016.root' ,
                                  } ,
                         'wpSF':  {
                                    '1-7' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2016v2/egammaEffi_passingTight80XHWW.txt' ,  
                                  } ,
                         'fakeW' : '/LatinoAnalysis/NanoGardener/python/data/fake_prompt_rates/Full2016/Tight80X/',
                             } ,

         'cut_WP_Tight80X_SS' : {
                         'cuts' : { 
                                # Common cuts
                                'True' :
                                  [
                                    'abs(electron_col[LF_idx]["eta"]) < 2.5' ,
                                    'electron_col[LF_idx]["cutBased_HLTPreSel"] == 1',
                                    'electron_col[LF_idx]["cutBased_Sum16"] == 4',
                                    'electron_col[LF_idx]["lostHits"] < 1',
                                    'electron_col[LF_idx]["tightCharge"] == 2',
                                  ] ,
                                # Barrel
                                'abs(electron_col[LF_idx]["eta"]) <= 1.479' :
                                  [
                                    'abs(electron_col[LF_idx]["dxy"]) < 0.05' ,
                                    'abs(electron_col[LF_idx]["dz"]) < 0.1'  ,
                                  ] ,
                                # EndCap
                                'abs(electron_col[LF_idx]["eta"]) > 1.479' :
                                  [
                                    'abs(electron_col[LF_idx]["dxy"]) < 0.1' ,
                                    'abs(electron_col[LF_idx]["dz"]) < 0.2'  ,
                                  ] ,
                                  } ,
                         'tkSF':  { 
                                    '1-7' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2016v2/EGM2D_BtoH_combineLowEt_RecoSF_Legacy2016.root' ,
                                  } ,
                         'wpSF':  {
                                    '1-7' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2016v2/egammaEffi_passingTight80XSSHWW.txt' ,
                                  } ,
                         'fakeW' : '/LatinoAnalysis/NanoGardener/python/data/fake_prompt_rates/Full2016/Tight80X_SS/',
                             } ,

          'mva_90p_Iso2016':  {
                         'cuts' : { 
                                # Common cuts 
                                'True' :
                                   [
                                     'abs(electron_col[LF_idx]["eta"]) < 2.5' ,
                                     'electron_col[LF_idx]["cutBased_HLTPreSel"] == 1',
                                     'electron_col[LF_idx]["mvaSpring16GP_WP90"]',
                                     'electron_col[LF_idx]["lostHits"] < 1',  
                                   ] ,
                                # Barrel
                                 'abs(electron_col[LF_idx]["eta"]) <= 1.479' :
                                   [
                                     'abs(electron_col[LF_idx]["dxy"]) < 0.05' ,
                                     'abs(electron_col[LF_idx]["dz"]) < 0.1'  ,
                                     'electron_col[LF_idx]["pfRelIso03_all"] < 0.05880',
                                   ] ,
                                 # EndCap
                                 'abs(electron_col[LF_idx]["eta"]) > 1.479' :
                                   [
                                     'abs(electron_col[LF_idx]["dxy"]) < 0.1' ,
                                     'abs(electron_col[LF_idx]["dz"]) < 0.2'  ,
                                     'electron_col[LF_idx]["pfRelIso03_all"] < 0.0571',
                                   ] ,
                                  } ,
                         'tkSF':  { 
                                    '1-7' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2016v2/EGM2D_BtoH_combineLowEt_RecoSF_Legacy2016.root' ,
                                  } ,
                         'wpSF':  {
                                    '1-7' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2016v2/egammaEffi_passingMVA80Xwp90HWW.txt' ,
                                  } ,
                         'fakeW' : '/LatinoAnalysis/NanoGardener/python/data/fake_prompt_rates/MonoHiggs/',
                              } ,

          'mva_90p_Iso2016_SS':  {
                         'cuts' : {
                                # Common cuts
                                'True' :
                                   [
                                     'abs(electron_col[LF_idx]["eta"]) < 2.5' ,
                                     'electron_col[LF_idx]["cutBased_HLTPreSel"] == 1',
                                     'electron_col[LF_idx]["mvaSpring16GP_WP90"]',
                                     'electron_col[LF_idx]["lostHits"] < 1',
                                     'electron_col[LF_idx]["tightCharge"] == 2',
                                   ] ,
                                # Barrel
                                 'abs(electron_col[LF_idx]["eta"]) <= 1.479' :
                                   [
                                     'abs(electron_col[LF_idx]["dxy"]) < 0.05' ,
                                     'abs(electron_col[LF_idx]["dz"]) < 0.1'  ,
                                     'electron_col[LF_idx]["pfRelIso03_all"] < 0.05880',
                                   ] ,
                                 # EndCap
                                 'abs(electron_col[LF_idx]["eta"]) > 1.479' :
                                   [
                                     'abs(electron_col[LF_idx]["dxy"]) < 0.1' ,
                                     'abs(electron_col[LF_idx]["dz"]) < 0.2'  ,
                                     'electron_col[LF_idx]["pfRelIso03_all"] < 0.0571',
                                   ] ,
                                  } ,
                         'tkSF':  {
                                    '1-7' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2016v2/EGM2D_BtoH_combineLowEt_RecoSF_Legacy2016.root' ,
                                  } ,
                         'wpSF':  {
                                    '1-7' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2016v2/egammaEffi_passingMVA80Xwp90SSHWW.txt' ,
                                  } ,
                         'fakeW' : '/LatinoAnalysis/NanoGardener/python/data/fake_prompt_rates/Full2016/mva90pIso2016_SS/',
                              } ,

                } ,

 # ------------ 
 'WgStarObjWP' : {

          'mva_90p_Iso2016':  {
                         'cuts' : {
                                # Common cuts
                                'True' :
                                   [
                                     'abs(electron_col[LF_idx]["eta"]) < 2.5' ,
                                     'electron_col[LF_idx]["cutBased_HLTPreSel"] == 1',
                                     'electron_col[LF_idx]["mvaSpring16GP_WP90"]',
                                     'electron_col[LF_idx]["lostHits"] < 1',
                                   ] ,
                                # Barrel
                                 'abs(electron_col[LF_idx]["eta"]) <= 1.479' :
                                   [
                                     'abs(electron_col[LF_idx]["dxy"]) < 0.05' ,
                                     'abs(electron_col[LF_idx]["dz"]) < 0.1'  ,
                                   ] ,
                                 # EndCap
                                 'abs(electron_col[LF_idx]["eta"]) > 1.479' :
                                   [
                                     'abs(electron_col[LF_idx]["dxy"]) < 0.1' ,
                                     'abs(electron_col[LF_idx]["dz"]) < 0.2'  ,
                                   ] ,
                                  } ,
                        'cuts_iso': {
                                # Common cuts
                                'True' :
                                [
                                  'None',
                                ],
                                # Barrel
                                'abs(electron_col[LF_idx]["eta"]) <= 1.479' :
                                [
                                 '0.05880'
                                ],
                                # EndCap
                                'abs(electron_col[LF_idx]["eta"]) > 1.479' :
                                [
                                 '0.0571'
                                ],
                                  },
                         'iso': ['pfRelIso03_all', 0.3],
                         'tkSF':  { 
                                    '1-7' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2016v2/EGM2D_BtoH_combineLowEt_RecoSF_Legacy2016.root' ,
                                  } ,
                         'wpSF':  {
                                    '1-7' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2016v2/egammaEffi_passingMVA80Xwp90HWW.txt' ,
                                  } ,
                         'fakeW' : '/LatinoAnalysis/NanoGardener/python/data/fake_prompt_rates/Full2016/mva90pIso2016/',        
                              } ,

                } ,
},


###____________________Full2016v2_hmumu________ : for nAODv4
'Full2016v2_hmumu': {

## ------------
 'VetoObjWP' : {
           'HLTsafe' : {
                         'cuts' : {
                               # Common cuts
                               'True' :
                                [
                                    ##'False'
                                    'abs(electron_col[LF_idx]["eta"]) < 2.5' ,
                                    'electron_col[LF_idx]["mvaFall17V2noIso_WPL"]',
                                    #'electron_col[LF_idx]["cutBased_HLTPreSel"] == 1 ' ,
                                ] ,
                         },
                       } ,
                 } ,



 # ------------ 
 'WgStarObjWP' : {
          'mva_WPL_NoIso2016':  {
                         'cuts' : { 
                                # Common cuts 
                                'True' :
                                   [
                                     'abs(electron_col[LF_idx]["eta"]) < 2.5' ,
                                     'electron_col[LF_idx]["mvaFall17V2noIso_WPL"]',
                                   ] ,
                                  } ,
                         'tkSF':  { 
                                    '1-7' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2016v2/EGM2D_BtoH_combineLowEt_RecoSF_Legacy2016.root' ,
                                  } ,
                              } ,
     },


 # ------------ 
'FakeObjWP' : {
          'mva_WPL_NoIso2016':  {
                         'cuts' : { 
                                # Common cuts 
                                'True' :
                                   [
                                     'abs(electron_col[LF_idx]["eta"]) < 2.5' ,
                                     'electron_col[LF_idx]["mvaFall17V2noIso_WPL"]',
                                   ] ,
                                  } ,
                         'tkSF':  { 
                                    '1-7' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2016v2/EGM2D_BtoH_combineLowEt_RecoSF_Legacy2016.root' ,
                                  } ,
                              } ,
     },


 # ------------ 
 'TightObjWP' : {

          'mva_WPL_NoIso2016':  {
                         'cuts' : { 
                                # Common cuts 
                                'True' :
                                   [
                                     'abs(electron_col[LF_idx]["eta"]) < 2.5' ,
                                     'electron_col[LF_idx]["mvaFall17V2noIso_WPL"]',
                                   ] ,
                                  } ,
                         'tkSF':  { 
                                    '1-7' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2016v2/EGM2D_BtoH_combineLowEt_RecoSF_Legacy2016.root' ,
                                  } ,
                              } ,
     },
},

###____________________Full2016v2________ : for nAODv3 (and nAODv2)
'Full2016v2': {

## ------------
 'VetoObjWP' : {
           'HLTsafe' : {
                         'cuts' : {
                               # Common cuts
                               'True' :
                                [
                                  'False'
                                  #'abs(electron_col[LF_idx]["eta"]) < 2.5' ,
                                  #'electron_col[LF_idx]["cutBased_HLTPreSel"] == 1 ' ,
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
                                   'abs(electron_col[LF_idx]["eta"]) < 2.5' ,
                                   'electron_col[LF_idx]["cutBased_HLTPreSel"] == 1 ' ,
                                   'electron_col[LF_idx]["lostHits"] < 1',
                                  ] ,             
                                # Barrel
                                'abs(electron_col[LF_idx]["eta"]) <= 1.479' :
                                  [
                                    'abs(electron_col[LF_idx]["dxy"]) < 0.05' ,
                                    'abs(electron_col[LF_idx]["dz"]) < 0.1'  ,
                                  ] ,
                                # EndCap
                                'abs(electron_col[LF_idx]["eta"]) > 1.479' :
                                  [
                                    'abs(electron_col[LF_idx]["dxy"]) < 0.1' ,
                                    'abs(electron_col[LF_idx]["dz"]) < 0.2'  ,
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
                                    'abs(electron_col[LF_idx]["eta"]) < 2.5' ,
                                    'electron_col[LF_idx]["cutBased_HLTPreSel"] == 1',
                                    'electron_col[LF_idx]["cutBased"] == 4', 
                                    'electron_col[LF_idx]["lostHits"] < 1',
                                  ] , 
                                # Barrel
                                'abs(electron_col[LF_idx]["eta"]) <= 1.479' :
                                  [
                                    'abs(electron_col[LF_idx]["dxy"]) < 0.05' ,
                                    'abs(electron_col[LF_idx]["dz"]) < 0.1'  ,
                                  ] ,
                                # EndCap
                                'abs(electron_col[LF_idx]["eta"]) > 1.479' :
                                  [
                                    'abs(electron_col[LF_idx]["dxy"]) < 0.1' ,
                                    'abs(electron_col[LF_idx]["dz"]) < 0.2'  ,
                                  ] ,
                                  } ,
                         'tkSF':  { 
                                    '1-7' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2016v2/EGM2D_BtoH_combineLowEt_RecoSF_Legacy2016.root' ,
                                  } ,
                         'wpSF':  {
                                    '1-7' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2016v2/egammaEffi_passingTight80XHWW.txt' ,  
                                  } ,
                    # FIXME
                    #    'fakeW' : '/LatinoAnalysis/Gardener/python/data/fake_prompt_rates/80X/lowPtCorrected/36fb_ele_cut_WP_Tight80X/',
                             } ,

         'cut_WP_Tight80X_SS' : {
                         'cuts' : { 
                                # Common cuts
                                'True' :
                                  [
                                    'abs(electron_col[LF_idx]["eta"]) < 2.5' ,
                                    'electron_col[LF_idx]["cutBased_HLTPreSel"] == 1',
                                    'electron_col[LF_idx]["cutBased"] == 4',
                                    'electron_col[LF_idx]["lostHits"] < 1',
                                    'electron_col[LF_idx]["tightCharge"] == 2',
                                  ] ,
                                # Barrel
                                'abs(electron_col[LF_idx]["eta"]) <= 1.479' :
                                  [
                                    'abs(electron_col[LF_idx]["dxy"]) < 0.05' ,
                                    'abs(electron_col[LF_idx]["dz"]) < 0.1'  ,
                                  ] ,
                                # EndCap
                                'abs(electron_col[LF_idx]["eta"]) > 1.479' :
                                  [
                                    'abs(electron_col[LF_idx]["dxy"]) < 0.1' ,
                                    'abs(electron_col[LF_idx]["dz"]) < 0.2'  ,
                                  ] ,
                                  } ,
                         'tkSF':  { 
                                    '1-7' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2016v2/EGM2D_BtoH_combineLowEt_RecoSF_Legacy2016.root' ,
                                  } ,
                         'wpSF':  {
                                    '1-7' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2016v2/egammaEffi_passingTight80XSSHWW.txt' ,
                                  } ,
                     # FIXME
                     #   'fakeW' : '/LatinoAnalysis/Gardener/python/data/fake_prompt_rates/80X/lowPtCorrected/36fb_ele_cut_WP_Tight80X_SS/',
                             } ,

          'mva_90p_Iso2016':  {
                         'cuts' : { 
                                # Common cuts 
                                'True' :
                                   [
                                     'abs(electron_col[LF_idx]["eta"]) < 2.5' ,
                                     'electron_col[LF_idx]["cutBased_HLTPreSel"] == 1',
                                     'electron_col[LF_idx]["mvaSpring16GP_WP90"]',
                                     'electron_col[LF_idx]["lostHits"] < 1',  
                                   ] ,
                                # Barrel
                                 'abs(electron_col[LF_idx]["eta"]) <= 1.479' :
                                   [
                                     'abs(electron_col[LF_idx]["dxy"]) < 0.05' ,
                                     'abs(electron_col[LF_idx]["dz"]) < 0.1'  ,
                                     'electron_col[LF_idx]["pfRelIso03_all"] < 0.05880',
                                   ] ,
                                 # EndCap
                                 'abs(electron_col[LF_idx]["eta"]) > 1.479' :
                                   [
                                     'abs(electron_col[LF_idx]["dxy"]) < 0.1' ,
                                     'abs(electron_col[LF_idx]["dz"]) < 0.2'  ,
                                     'electron_col[LF_idx]["pfRelIso03_all"] < 0.0571',
                                   ] ,
                                  } ,
                         'tkSF':  { 
                                    '1-7' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2016v2/EGM2D_BtoH_combineLowEt_RecoSF_Legacy2016.root' ,
                                  } ,
                         'wpSF':  {
                                    '1-7' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2016v2/egammaEffi_passingMVA80Xwp90HWW.txt' ,
                                  } ,
                     # FIXME
                     #   'fakeW' : '/LatinoAnalysis/Gardener/python/data/fake_prompt_rates/80X/lowPtCorrected/36fb_ele_mva_90p_Iso2016/',
                              } ,

          'mva_90p_Iso2016_SS':  {
                         'cuts' : {
                                # Common cuts
                                'True' :
                                   [
                                     'abs(electron_col[LF_idx]["eta"]) < 2.5' ,
                                     'electron_col[LF_idx]["cutBased_HLTPreSel"] == 1',
                                     'electron_col[LF_idx]["mvaSpring16GP_WP90"]',
                                     'electron_col[LF_idx]["lostHits"] < 1',
                                     'electron_col[LF_idx]["tightCharge"] == 2',
                                   ] ,
                                # Barrel
                                 'abs(electron_col[LF_idx]["eta"]) <= 1.479' :
                                   [
                                     'abs(electron_col[LF_idx]["dxy"]) < 0.05' ,
                                     'abs(electron_col[LF_idx]["dz"]) < 0.1'  ,
                                     'electron_col[LF_idx]["pfRelIso03_all"] < 0.05880',
                                   ] ,
                                 # EndCap
                                 'abs(electron_col[LF_idx]["eta"]) > 1.479' :
                                   [
                                     'abs(electron_col[LF_idx]["dxy"]) < 0.1' ,
                                     'abs(electron_col[LF_idx]["dz"]) < 0.2'  ,
                                     'electron_col[LF_idx]["pfRelIso03_all"] < 0.0571',
                                   ] ,
                                  } ,
                         'tkSF':  {
                                    '1-7' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2016v2/EGM2D_BtoH_combineLowEt_RecoSF_Legacy2016.root' ,
                                  } ,
                         'wpSF':  {
                                    '1-7' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2016v2/egammaEffi_passingMVA80Xwp90SSHWW.txt' ,
                                  } ,
                     # FIXME
                     #   'fakeW' : '/LatinoAnalysis/Gardener/python/data/fake_prompt_rates/80X/lowPtCorrected/36fb_ele_mva_90p_Iso2016/',
                              } ,

                } ,

 # ------------ 
 'WgStarObjWP' : {

          'mva_90p_Iso2016':  {
                         'cuts' : {
                                # Common cuts
                                'True' :
                                   [
                                     'abs(electron_col[LF_idx]["eta"]) < 2.5' ,
                                     'electron_col[LF_idx]["cutBased_HLTPreSel"] == 1',
                                     'electron_col[LF_idx]["mvaSpring16GP_WP90"]',
                                     'electron_col[LF_idx]["lostHits"] < 1',
                                   ] ,
                                # Barrel
                                 'abs(electron_col[LF_idx]["eta"]) <= 1.479' :
                                   [
                                     'abs(electron_col[LF_idx]["dxy"]) < 0.05' ,
                                     'abs(electron_col[LF_idx]["dz"]) < 0.1'  ,
                                     'electron_col[LF_idx]["pfRelIso03_all"] < 0.05880',
                                   ] ,
                                 # EndCap
                                 'abs(electron_col[LF_idx]["eta"]) > 1.479' :
                                   [
                                     'abs(electron_col[LF_idx]["dxy"]) < 0.1' ,
                                     'abs(electron_col[LF_idx]["dz"]) < 0.2'  ,
                                     'electron_col[LF_idx]["pfRelIso03_all"] < 0.0571',
                                   ] ,
                                  } ,
                        'cuts_iso': {
                                # Common cuts
                                'True' :
                                [
                                  'None',
                                ],
                                # Barrel
                                'abs(electron_col[LF_idx]["eta"]) <= 1.479' :
                                # FIXME : 
                                [
                                 # '0.25' 
                                 '0.05880'
                                ],
                                # EndCap
                                'abs(electron_col[LF_idx]["eta"]) > 1.479' :
                                # FIXME
                                [
                                 # '0.2' 
                                 '0.0571'
                                ],
                                  },
                         'iso': ['pfRelIso03_all', 0.3],
                         'tkSF':  { 
                                    '1-7' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2016v2/EGM2D_BtoH_combineLowEt_RecoSF_Legacy2016.root' ,
                                  } ,
                         'wpSF':  {
                                    '1-7' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2016v2/egammaEffi_passingMVA80Xwp90HWW.txt' ,
                                  } ,
                     # FIXME
                     #   'fakeW' : '/LatinoAnalysis/Gardener/python/data/fake_prompt_rates/80X/lowPtCorrected/36fb_ele_mva_90p_Iso2016/',
                              } ,

                } ,
},

###____________________Full2016__________________________
'Full2016': {

## ------------  

 'VetoObjWP' : { 
           'HLTsafe' : { 
                         'cuts' : { 
                               # Common cuts
                               'True' :
                                [
                                  'False'
                                  #'abs(electron_col[LF_idx]["eta"]) < 2.5' ,
                                  #'electron_col[LF_idx]["cutBased_HLTPreSel"] == 1 ' ,
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
                                   'abs(electron_col[LF_idx]["eta"]) < 2.5' ,
                                   'electron_col[LF_idx]["cutBased_HLTPreSel"] == 1 ' ,
                                   'electron_col[LF_idx]["lostHits"] < 1',
                                  ] ,             
                                # Barrel
                                'abs(electron_col[LF_idx]["eta"]) <= 1.479' :
                                  [
                                    'abs(electron_col[LF_idx]["dxy"]) < 0.05' ,
                                    'abs(electron_col[LF_idx]["dz"]) < 0.1'  ,
                                  ] ,
                                # EndCap
                                'abs(electron_col[LF_idx]["eta"]) > 1.479' :
                                  [
                                    'abs(electron_col[LF_idx]["dxy"]) < 0.1' ,
                                    'abs(electron_col[LF_idx]["dz"]) < 0.2'  ,
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
                                    'abs(electron_col[LF_idx]["eta"]) < 2.5' ,
                                    'electron_col[LF_idx]["cutBased_HLTPreSel"] == 1',
                                    'electron_col[LF_idx]["cutBased"] == 4', 
                                    'electron_col[LF_idx]["lostHits"] < 1',
                                  ] , 
                                # Barrel
                                'abs(electron_col[LF_idx]["eta"]) <= 1.479' :
                                  [
                                    'abs(electron_col[LF_idx]["dxy"]) < 0.05' ,
                                    'abs(electron_col[LF_idx]["dz"]) < 0.1'  ,
                                  ] ,
                                # EndCap
                                'abs(electron_col[LF_idx]["eta"]) > 1.479' :
                                  [
                                    'abs(electron_col[LF_idx]["dxy"]) < 0.1' ,
                                    'abs(electron_col[LF_idx]["dz"]) < 0.2'  ,
                                  ] ,
                                  } ,
                         'tkSF':  { 
                                    '1-7' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2016/egammaEffi.txt_EGM2D.root' ,
                                  } ,
                         'wpSF':  {
                                    '1-7' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2016/electrons_cut_WP_Tight80X.txt' ,  
                                  } ,
                         'fakeW' : '/LatinoAnalysis/Gardener/python/data/fake_prompt_rates/80X/lowPtCorrected/36fb_ele_cut_WP_Tight80X/',
                             } ,


         'cut_WP_Tight80X_SS' : {
                         'cuts' : { 
                                # Common cuts
                                'True' :
                                  [
                                    'abs(electron_col[LF_idx]["eta"]) < 2.5' ,
                                    'electron_col[LF_idx]["cutBased_HLTPreSel"] == 1',
                                    'electron_col[LF_idx]["cutBased"] == 4',
                                    'electron_col[LF_idx]["lostHits"] < 1',
                                    'electron_col[LF_idx]["tightCharge"] == 2',
                                  ] ,
                                # Barrel
                                'abs(electron_col[LF_idx]["eta"]) <= 1.479' :
                                  [
                                    'abs(electron_col[LF_idx]["dxy"]) < 0.05' ,
                                    'abs(electron_col[LF_idx]["dz"]) < 0.1'  ,
                                  ] ,
                                # EndCap
                                'abs(electron_col[LF_idx]["eta"]) > 1.479' :
                                  [
                                    'abs(electron_col[LF_idx]["dxy"]) < 0.1' ,
                                    'abs(electron_col[LF_idx]["dz"]) < 0.2'  ,
                                  ] ,
                                  } ,
                         'tkSF':  { 
                                    '1-7' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2016/egammaEffi.txt_EGM2D.root' ,
                                  } ,
                         'wpSF':  {
                                    '1-7' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2016/electrons_cut_WP_Tight80X_SS.txt' ,
                                  } ,
                         'fakeW' : '/LatinoAnalysis/Gardener/python/data/fake_prompt_rates/80X/lowPtCorrected/36fb_ele_cut_WP_Tight80X_SS/',
                             } ,


          'mva_80p_Iso2015':  {
                         'cuts' : { 
                                # Common cuts 
                                'True' :
                                   [
                                     'abs(electron_col[LF_idx]["eta"]) < 2.5' ,
                                     'electron_col[LF_idx]["cutBased_HLTPreSel"] == 1',
                                     'electron_col[LF_idx]["mvaSpring16GP_WP80"]',
                                     'electron_col[LF_idx]["lostHits"] < 1',
                                   ] ,
                                # Barrel
                                 'abs(electron_col[LF_idx]["eta"]) <= 1.479' :
                                   [
                                     'abs(electron_col[LF_idx]["dxy"]) < 0.05' ,
                                     'abs(electron_col[LF_idx]["dz"]) < 0.1'  ,
                                     'electron_col[LF_idx]["pfRelIso03_all"] < 0.0354',
                                   ] ,
                                 # EndCap
                                 'abs(electron_col[LF_idx]["eta"]) > 1.479' :
                                   [
                                     'abs(electron_col[LF_idx]["dxy"]) < 0.1' ,
                                     'abs(electron_col[LF_idx]["dz"]) < 0.2'  ,
                                     'electron_col[LF_idx]["pfRelIso03_all"] < 0.0646',
                                   ] ,
                                  } ,
                         'tkSF':  { 
                                    '1-7' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2016/egammaEffi.txt_EGM2D.root' ,
                                  } ,
                         'wpSF':  {
                                    '1-7' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2016/electrons_mva_80p_Iso2015.txt' ,
                                  } ,
                         'fakeW' : '/LatinoAnalysis/Gardener/python/data/fake_prompt_rates/80X/lowPtCorrected/36fb_ele_mva_80p_Iso2015/',
                              } ,
 
          'mva_80p_Iso2016':  {
                         'cuts' : { 
                                # Common cuts 
                                'True' :
                                   [
                                     'abs(electron_col[LF_idx]["eta"]) < 2.5' ,
                                     'electron_col[LF_idx]["cutBased_HLTPreSel"] == 1',
                                     'electron_col[LF_idx]["mvaSpring16GP_WP80"]',
                                     'electron_col[LF_idx]["lostHits"] < 1',
                                   ] ,
                                # Barrel
                                 'abs(electron_col[LF_idx]["eta"]) <= 1.479' :
                                   [
                                     'abs(electron_col[LF_idx]["dxy"]) < 0.05' ,
                                     'abs(electron_col[LF_idx]["dz"]) < 0.1'  ,
                                     'electron_col[LF_idx]["pfRelIso03_all"] < 0.05880',
                                   ] ,
                                 # EndCap
                                 'abs(electron_col[LF_idx]["eta"]) > 1.479' :
                                   [
                                     'abs(electron_col[LF_idx]["dxy"]) < 0.1' ,
                                     'abs(electron_col[LF_idx]["dz"]) < 0.2'  ,
                                     'electron_col[LF_idx]["pfRelIso03_all"] < 0.0571',
                                   ] ,
                                  } ,
                         'tkSF':  { 
                                    '1-7' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2016/egammaEffi.txt_EGM2D.root' ,
                                  } ,
                         'wpSF':  {
                                    '1-7' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2016/electrons_mva_80p_Iso2016.txt' ,
                                  } ,
                         'fakeW' : '/LatinoAnalysis/Gardener/python/data/fake_prompt_rates/80X/lowPtCorrected/36fb_ele_mva_80p_Iso2016/',
                              } ,
 
          'mva_90p_Iso2015':  {
                         'cuts' : { 
                                # Common cuts 
                                'True' :
                                   [
                                     'abs(electron_col[LF_idx]["eta"]) < 2.5' ,
                                     'electron_col[LF_idx]["cutBased_HLTPreSel"] == 1',
                                     'electron_col[LF_idx]["mvaSpring16GP_WP90"]',
                                     'electron_col[LF_idx]["lostHits"] < 1',
                                   ] ,
                                # Barrel
                                 'abs(electron_col[LF_idx]["eta"]) <= 1.479' :
                                   [
                                     'abs(electron_col[LF_idx]["dxy"]) < 0.05' ,
                                     'abs(electron_col[LF_idx]["dz"]) < 0.1'  ,
                                     'electron_col[LF_idx]["pfRelIso03_all"] < 0.0354',
                                   ] ,
                                 # EndCap
                                 'abs(electron_col[LF_idx]["eta"]) > 1.479' :
                                   [
                                     'abs(electron_col[LF_idx]["dxy"]) < 0.1' ,
                                     'abs(electron_col[LF_idx]["dz"]) < 0.2'  ,
                                     'electron_col[LF_idx]["pfRelIso03_all"] < 0.0646',
                                   ] ,
                                  } ,
                         'tkSF':  { 
                                    '1-7' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2016/egammaEffi.txt_EGM2D.root' ,
                                  } ,
                         'wpSF':  {
                                    '1-7' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2016/electrons_mva_90p_Iso2015.txt' ,
                                  } ,
                         'fakeW' : '/LatinoAnalysis/Gardener/python/data/fake_prompt_rates/80X/lowPtCorrected/36fb_ele_mva_90p_Iso2015/',
                              } ,
 
          'mva_90p_Iso2016':  {
                         'cuts' : { 
                                # Common cuts 
                                'True' :
                                   [
                                     'abs(electron_col[LF_idx]["eta"]) < 2.5' ,
                                     'electron_col[LF_idx]["cutBased_HLTPreSel"] == 1',
                                     'electron_col[LF_idx]["mvaSpring16GP_WP90"]',
                                     'electron_col[LF_idx]["lostHits"] < 1',
                                   ] ,
                                # Barrel
                                 'abs(electron_col[LF_idx]["eta"]) <= 1.479' :
                                   [
                                     'abs(electron_col[LF_idx]["dxy"]) < 0.05' ,
                                     'abs(electron_col[LF_idx]["dz"]) < 0.1'  ,
                                     'electron_col[LF_idx]["pfRelIso03_all"] < 0.05880',
                                   ] ,
                                 # EndCap
                                 'abs(electron_col[LF_idx]["eta"]) > 1.479' :
                                   [
                                     'abs(electron_col[LF_idx]["dxy"]) < 0.1' ,
                                     'abs(electron_col[LF_idx]["dz"]) < 0.2'  ,
                                     'electron_col[LF_idx]["pfRelIso03_all"] < 0.0571',
                                   ] ,
                                  } ,
                         'tkSF':  { 
                                    '1-7' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2016/egammaEffi.txt_EGM2D.root' ,
                                  } ,
                         'wpSF':  {
                                    '1-7' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2016/electrons_mva_90p_Iso2016.txt' ,
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
                                    'abs(electron_col[LF_idx]["eta"]) < 2.5' ,
                                    #'electron_col[LF_idx]["cutBased_HLTPreSel"] == 1',
                                    #'electron_col[LF_idx]["cutBased"] == 4',
                                    'electron_col[LF_idx]["lostHits"] < 1',
                                    'electron_col[LF_idx]["convVeto"]',
                                    'electron_col[LF_idx]["tightCharge"] == 2',
                                  ] ,
                                # Barrel
                                'abs(electron_col[LF_idx]["eta"]) <= 1.479' :
                                  [
                                    'abs(electron_col[LF_idx]["dxy"]) < 0.05' ,
                                    'abs(electron_col[LF_idx]["dz"]) < 0.1'  ,
                                    'electron_col[LF_idx]["sieie"] < 0.00998',
                                    #'electron_col[LF_idx]["deltaEtaSC"] < 0.00308',
                                    #'itree.std_vector_electron_dPhiIn"][LF_idx] < 0.0816',
                                    'electron_col[LF_idx]["hoe"] < 0.0414',
                                    'electron_col[LF_idx]["eInvMinusPInv"] < 0.0129',
                                    #'(electron_col[LF_idx]["pfRelIso03_all"] - self.ConeOverlapPt(lepton_col, iLep)/electron_col[LF_idx]["pt"]) < 0.0588',                                  
                                  ] ,
                                # EndCap
                                'abs(electron_col[LF_idx]["eta"]) > 1.479' :
                                  [
                                    'abs(electron_col[LF_idx]["dxy"]) < 0.1' ,
                                    'abs(electron_col[LF_idx]["dz"]) < 0.2'  ,
                                    'electron_col[LF_idx]["sieie"] < 0.0292',
                                    #'electron_col[LF_idx]["deltaEtaSC"] < 0.00605',
                                    #'itree.std_vector_electron_dPhiIn"][LF_idx] < 0.0394',
                                    'electron_col[LF_idx]["hoe"] < 0.0641',
                                    'electron_col[LF_idx]["eInvMinusPInv"] < 0.0129',
                                    #'(electron_col[LF_idx]["pfRelIso03_all"] - self.ConeOverlapPt(lepton_col, iLep)/electron_col[LF_idx]["pt"]) < 0.0571', 
                                  ] ,
                                  } ,
                         'cuts_iso': {
                                # Common cuts
                                'True' :
                                [
                                  'None',
                                ],
                                # Barrel
                                'abs(electron_col[LF_idx]["eta"]) <= 1.479' :
                                [
                                  '0.0588' 
                                ],
                                # EndCap
                                'abs(electron_col[LF_idx]["eta"]) > 1.479' :
                                [
                                  '0.0571' 
                                ],
                                  },
                         'iso': ['pfRelIso03_all', 0.3],
                             } ,

                 } ,
},


}

#ElectronWP['Study2017'] = ElectronWP['Full2016']
ElectronWP['Full2016v5']=ElectronWP['Full2016v4']
ElectronWP['Full2016v6']=ElectronWP['Full2016v4']

####################### Muon WP ######################################

MuonWP = {

###____________________Full2018__________________________
'Full2018': {

## ------------  
 'VetoObjWP' : { 
      'HLTsafe' : {
                         'cuts' : { 
                                # Common cuts
                                'True' :
                                 [
                                   'abs(muon_col[LF_idx]["eta"]) < 2.4' , 
                                   'muon_col[LF_idx]["pt"] > 10.0' ,
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
                                   'abs(muon_col[LF_idx]["eta"]) < 2.4' , 
                                   'muon_col[LF_idx]["tightId"] == 1' ,
                                   'abs(muon_col[LF_idx]["dz"]) < 0.1' ,
                                   'muon_col[LF_idx]["pfRelIso04_all"] < 0.4',
                                 ] ,
                                 # dxy for pT < 20 GeV
                                 'muon_col[LF_idx]["pt"] <= 20.0' :
                                 [
                                    'abs(muon_col[LF_idx]["dxy"]) < 0.01 ' ,
                                 ] ,
                                 # dxy for pT > 20 GeV
                                 'muon_col[LF_idx]["pt"] > 20.0' :
                                 [
                                    'abs(muon_col[LF_idx]["dxy"]) < 0.02 ' ,
                                 ] ,
                                  } ,

                       } ,
                 
                 } ,

 # ------------ 
 'TightObjWP' :  {

      'cut_Tight_HWWW' : {
                         'cuts' : { 
                                # Common cuts
                                'True' :
                                 [ 
                                   'abs(muon_col[LF_idx]["eta"]) < 2.4' ,
                                   'muon_col[LF_idx]["tightId"] == 1' ,
                                   'abs(muon_col[LF_idx]["dz"]) < 0.1' ,
                                   'muon_col[LF_idx]["pfRelIso04_all"] < 0.15',
                                 ] ,
                                 # dxy for pT < 20 GeV
                                 'muon_col[LF_idx]["pt"] <= 20.0' :
                                 [
                                    'abs(muon_col[LF_idx]["dxy"]) < 0.01 ' ,
                                 ] ,
                                 # dxy for pT > 20 GeV
                                 'muon_col[LF_idx]["pt"] > 20.0' :
                                 [
                                    'abs(muon_col[LF_idx]["dxy"]) < 0.02 ' ,
                                 ] ,
                                  } ,
                         'idSF':  {
                                    '1-1' : [ 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2018/ID_TH2_SFs_pt_eta.root'],
                                  } ,
                         'isoSF': {
                                    '1-1' : [ 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2018/ISO_TH2_SFs_pt_eta.root'],
                                  } ,
                         'fakeW' : '/LatinoAnalysis/NanoGardener/python/data/fake_prompt_rates/Full2018/',


                       } ,

                 } ,

 # -------------
 'WgStarObjWP' : {
     'cut_Tight_HWW' : { 
                         'cuts' : { 
                                # Common cuts
                                'True' :
                                 [
                                   'abs(muon_col[LF_idx]["eta"]) < 2.4' ,
                                   'muon_col[LF_idx]["tightId"] == 1' ,
                                   'abs(muon_col[LF_idx]["dz"]) < 0.1' ,
                                   #'(muon_col[LF_idx]["pfRelIso04_all"] - self.ConeOverlapPt(lepton_col, iLep)/muon_col[LF_idx]["pt"]) < 0.15',
                                   ##'muon_col[LF_idx]["trackIso"]/muon_col[LF_idx]["pt"] < 0.4' ,
                                 ] ,
                                 # dxy for pT < 20 GeV
                                 'muon_col[LF_idx]["pt"] <= 20.0' :
                                 [
                                    'abs(muon_col[LF_idx]["dxy"]) < 0.01 ' ,
                                 ] ,
                                 # dxy for pT > 20 GeV
                                 'muon_col[LF_idx]["pt"] > 20.0' :
                                 [
                                    'abs(muon_col[LF_idx]["dxy"]) < 0.02 ' ,
                                 ] ,
                                  } ,
                         'cuts_iso': {
                                # Common cuts
                                'True' :
                                [
                                  '0.15',
                                ],
                                # Low pt
                                'muon_col[LF_idx]["pt"] <= 20.0' :
                                [
                                  'None' 
                                ],
                                # High pt
                                'muon_col[LF_idx]["pt"] > 20.0' :
                                [
                                  'None' 
                                ],
                                  },
                         'iso': ['pfRelIso04_all', 0.4],
                         'idSF':  {
                                    '1-1' : [ 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2018/ID_TH2_SFs_pt_eta.root'],
                                  } ,
                         'isoSF': {
                                    '1-1' : [ 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2018/ISO_TH2_SFs_pt_eta.root'],
                                  } ,
                       } ,
 
                 }, 
},

###____________________Full2017v2_________________________
###____________________Full2017__________________________ (copy after as identical)
'Full2017v2': {

## ------------  
 'VetoObjWP' : { 
      'HLTsafe' : {
                         'cuts' : { 
                                # Common cuts
                                'True' :
                                 [
                                   'abs(muon_col[LF_idx]["eta"]) < 2.4' , 
                                   'muon_col[LF_idx]["pt"] > 10.0' ,
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
                                   'abs(muon_col[LF_idx]["eta"]) < 2.4' , 
                                   'muon_col[LF_idx]["tightId"] == 1' ,
                                   'abs(muon_col[LF_idx]["dz"]) < 0.1' ,
                                   'muon_col[LF_idx]["pfRelIso04_all"] < 0.4',
                                 ] ,
                                 # dxy for pT < 20 GeV
                                 'muon_col[LF_idx]["pt"] <= 20.0' :
                                 [
                                    'abs(muon_col[LF_idx]["dxy"]) < 0.01 ' ,
                                 ] ,
                                 # dxy for pT > 20 GeV
                                 'muon_col[LF_idx]["pt"] > 20.0' :
                                 [
                                    'abs(muon_col[LF_idx]["dxy"]) < 0.02 ' ,
                                 ] ,
                                  } ,

                       } ,
                 
                 } ,

 # ------------ 
 'TightObjWP' :  {

      'cut_Tight_HWWW' : {
                         'cuts' : { 
                                # Common cuts
                                'True' :
                                 [ 
                                   'abs(muon_col[LF_idx]["eta"]) < 2.4' ,
                                   'muon_col[LF_idx]["tightId"] == 1' ,
                                   'abs(muon_col[LF_idx]["dz"]) < 0.1' ,
                                   'muon_col[LF_idx]["pfRelIso04_all"] < 0.15',
                                 ] ,
                                 # dxy for pT < 20 GeV
                                 'muon_col[LF_idx]["pt"] <= 20.0' :
                                 [
                                    'abs(muon_col[LF_idx]["dxy"]) < 0.01 ' ,
                                 ] ,
                                 # dxy for pT > 20 GeV
                                 'muon_col[LF_idx]["pt"] > 20.0' :
                                 [
                                    'abs(muon_col[LF_idx]["dxy"]) < 0.02 ' ,
                                 ] ,
                                  } ,
                         # Negligible, POG recommended to set to 1.
                         #'tkSF':  { 
                         #           '1-5' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/muon_tracker_eff_Full2017.root' ,
                         #         } ,
                         #'tkSFerror': 0.01,
                         'idSF':  {
                                    '1-5' : [ 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/muonID_cut_Tight_HWW_combined.root'],
                                  } ,
                         'isoSF': {
                                    '1-5' : [ 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/muonISO_cut_Tight_HWW_combined.root'],
                                  } ,
                         'fakeW' : '/LatinoAnalysis/NanoGardener/python/data/fake_prompt_rates/Full2017v2p2NewBinning/',


                       } ,

                 } ,

 # -------------
 'WgStarObjWP' : {
     'cut_Tight_HWW' : { 
                         'cuts' : { 
                                # Common cuts
                                'True' :
                                 [
                                   'abs(muon_col[LF_idx]["eta"]) < 2.4' ,
                                   'muon_col[LF_idx]["tightId"] == 1' ,
                                   'abs(muon_col[LF_idx]["dz"]) < 0.1' ,
                                   #'(muon_col[LF_idx]["pfRelIso04_all"] - self.ConeOverlapPt(lepton_col, iLep)/muon_col[LF_idx]["pt"]) < 0.15',
                                   ##'muon_col[LF_idx]["trackIso"]/muon_col[LF_idx]["pt"] < 0.4' ,
                                 ] ,
                                 # dxy for pT < 20 GeV
                                 'muon_col[LF_idx]["pt"] <= 20.0' :
                                 [
                                    'abs(muon_col[LF_idx]["dxy"]) < 0.01 ' ,
                                 ] ,
                                 # dxy for pT > 20 GeV
                                 'muon_col[LF_idx]["pt"] > 20.0' :
                                 [
                                    'abs(muon_col[LF_idx]["dxy"]) < 0.02 ' ,
                                 ] ,
                                  } ,
                         'cuts_iso': {
                                # Common cuts
                                'True' :
                                [
                                  '0.15',
                                ],
                                # Low pt
                                'muon_col[LF_idx]["pt"] <= 20.0' :
                                [
                                  'None' 
                                ],
                                # High pt
                                'muon_col[LF_idx]["pt"] > 20.0' :
                                [
                                  'None' 
                                ],
                                  },
                         'iso': ['pfRelIso04_all', 0.4],
                         # Negligible, POG recommended to set to 1.
                         #'tkSF':  {
                         #           '1-5' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/muon_tracker_eff_Full2017.root' ,
                         #         } ,
                         #'tkSFerror': 0.01,
                         'idSF':  {
                                    '1-5' : [ 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/muonID_cut_Tight_HWW_combined.root'],
                                  } ,
                         'isoSF': {
                                    '1-5' : [ 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/muonISO_cut_Tight_HWW_combined.root'],
                                  } ,
                       } ,
 
                 }, 
},

##____________________Study2017_________________________
'Study2017': {

## ------------  
 'VetoObjWP' : { 
      'HLTsafe' : {
                         'cuts' : { 
                                # Common cuts
                                'True' :
                                 [
                                   'abs(muon_col[LF_idx]["eta"]) < 2.4' , 
                                   'muon_col[LF_idx]["pt"] > 10.0' ,
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
                                   'abs(muon_col[LF_idx]["eta"]) < 2.4' , 
                                   #'muon_col[LF_idx]["mediumId"] == 1' ,
                                   'muon_col[LF_idx]["pfRelIso03_all"] < 0.4',
                                 ] ,
                                  } ,

                       } ,
                 
                 } ,

 # ------------ 
 'TightObjWP' :  {

      'cut_Medium80x' : {
                         'cuts' : { 
                                # Common cuts
                                'True' :
                                 [ 
                                   'abs(muon_col[LF_idx]["eta"]) < 2.4' ,
                                   'muon_col[LF_idx]["mediumId"] == 1' ,
                                   'muon_col[LF_idx]["pfRelIso03_all"] < 0.15',
                                 ] ,
                                  } ,
                       },
      'cut_Tight80x' : {
                         'cuts' : { 
                                # Common cuts
                                'True' :
                                 [ 
                                   'abs(muon_col[LF_idx]["eta"]) < 2.4' ,
                                   'muon_col[LF_idx]["tightId"] == 1' ,
                                   'muon_col[LF_idx]["pfRelIso03_all"] < 0.15',
                                 ] ,
                                  } ,
                       },
      'cut_Medium80x_HWWW' : {
                         'cuts' : { 
                                # Common cuts
                                'True' :
                                 [ 
                                   'abs(muon_col[LF_idx]["eta"]) < 2.4' ,
                                   'muon_col[LF_idx]["mediumId"] == 1' ,
                                   'abs(muon_col[LF_idx]["dz"]) < 0.1' ,
                                   'muon_col[LF_idx]["pfRelIso03_all"] < 0.15',
                                   #'muon_col[LF_idx]["trackIso"]/muon_col[LF_idx]["pt"] < 0.4' ,
                                 ] ,
                                 # dxy for pT < 20 GeV
                                 'muon_col[LF_idx]["pt"] <= 20.0' :
                                 [
                                    'abs(muon_col[LF_idx]["dxy"]) < 0.01 ' ,
                                 ] ,
                                 # dxy for pT > 20 GeV
                                 'muon_col[LF_idx]["pt"] > 20.0' :
                                 [
                                    'abs(muon_col[LF_idx]["dxy"]) < 0.02 ' ,
                                 ] ,
                                  } ,

                       } ,
      'cut_Tight80x_HWWW' : {
                         'cuts' : { 
                                # Common cuts
                                'True' :
                                 [ 
                                   'abs(muon_col[LF_idx]["eta"]) < 2.4' ,
                                   'muon_col[LF_idx]["tightId"] == 1' ,
                                   'abs(muon_col[LF_idx]["dz"]) < 0.1' ,
                                   'muon_col[LF_idx]["pfRelIso03_all"] < 0.15',
                                   #'muon_col[LF_idx]["trackIso"]/muon_col[LF_idx]["pt"] < 0.4' ,
                                 ] ,
                                 # dxy for pT < 20 GeV
                                 'muon_col[LF_idx]["pt"] <= 20.0' :
                                 [
                                    'abs(muon_col[LF_idx]["dxy"]) < 0.01 ' ,
                                 ] ,
                                 # dxy for pT > 20 GeV
                                 'muon_col[LF_idx]["pt"] > 20.0' :
                                 [
                                    'abs(muon_col[LF_idx]["dxy"]) < 0.02 ' ,
                                 ] ,
                                  } ,
                       } ,

                 } ,

 # -------------
 'WgStarObjWP' : {
     'cut_Tight80x' : { 
                         'cuts' : { 
                                # Common cuts
                                'True' :
                                 [
                                   'False' ,
                                 ] ,
                                  } ,
                       } ,
 
                 }, 
},

###____________________Full2016v2__________________________

'Full2016v2': {

## ------------  
 'VetoObjWP' : { 
      'HLTsafe' : {
                         'cuts' : { 
                                # Common cuts
                                'True' :
                                 [
                                   'abs(muon_col[LF_idx]["eta"]) < 2.4' , 
                                   'muon_col[LF_idx]["pt"] > 10.0' ,
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
                                   'abs(muon_col[LF_idx]["eta"]) < 2.4' , 
                                   'muon_col[LF_idx]["tightId"] == 1' ,
                                   'abs(muon_col[LF_idx]["dz"]) < 0.1' ,
                                   'muon_col[LF_idx]["pfRelIso04_all"] < 0.4',
                                   #'muon_col[LF_idx]["trackIso"]/muon_col[LF_idx]["pt"] < 0.4' ,
                                 ] ,
                                 # dxy for pT < 20 GeV
                                 'muon_col[LF_idx]["pt"] <= 20.0' :
                                 [
                                    'abs(muon_col[LF_idx]["dxy"]) < 0.01 ' ,
                                 ] ,
                                 # dxy for pT > 20 GeV
                                 'muon_col[LF_idx]["pt"] > 20.0' :
                                 [
                                    'abs(muon_col[LF_idx]["dxy"]) < 0.02 ' ,
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
                                   'abs(muon_col[LF_idx]["eta"]) < 2.4' ,
                                   'muon_col[LF_idx]["tightId"] == 1' ,
                                   'abs(muon_col[LF_idx]["dz"]) < 0.1' ,
                                   'muon_col[LF_idx]["pfRelIso04_all"] < 0.15',
                                   #'muon_col[LF_idx]["trackIso"]/muon_col[LF_idx]["pt"] < 0.4' ,
                                 ] ,
                                 # dxy for pT < 20 GeV
                                 'muon_col[LF_idx]["pt"] <= 20.0' :
                                 [
                                    'abs(muon_col[LF_idx]["dxy"]) < 0.01 ' ,
                                 ] ,
                                 # dxy for pT > 20 GeV
                                 'muon_col[LF_idx]["pt"] > 20.0' :
                                 [
                                    'abs(muon_col[LF_idx]["dxy"]) < 0.02 ' ,
                                 ] ,
                                  } ,
                         'idSF':  {
                                    '1-7' : [ 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2016v2/muonID_TH2_SFs_pt_eta.root' ] ,
                                  } ,
                         'isoSF':  {
                                    '1-7' : [ 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2016v2/muonISO_TH2_SFs_pt_eta.root' ] ,
                                   } ,
                         'fakeW' : '/LatinoAnalysis/NanoGardener/python/data/fake_prompt_rates/Full2016/mva90pIso2016/', 

                       } ,

                 } ,

 # -------------
 'WgStarObjWP' : {
     'cut_Tight80x' : { 
                         'cuts' : { 
                                # Common cuts
                                'True' :
                                 [
                                   'abs(muon_col[LF_idx]["eta"]) < 2.4' ,
                                   'muon_col[LF_idx]["tightId"] == 1' ,
                                   'abs(muon_col[LF_idx]["dz"]) < 0.1' ,
                                   ##'muon_col[LF_idx]["trackIso"]/muon_col[LF_idx]["pt"] < 0.4' ,
                                 ] ,
                                 # dxy for pT < 20 GeV
                                 'muon_col[LF_idx]["pt"] <= 20.0' :
                                 [
                                    'abs(muon_col[LF_idx]["dxy"]) < 0.01 ' ,
                                 ] ,
                                 # dxy for pT > 20 GeV
                                 'muon_col[LF_idx]["pt"] > 20.0' :
                                 [
                                    'abs(muon_col[LF_idx]["dxy"]) < 0.02 ' ,
                                 ] ,
                                  } ,

                         'cuts_iso': {
                                # Common cuts
                                'True' :
                                [
                                  '0.15',
                                ],
                                # Low pt
                                'muon_col[LF_idx]["pt"] <= 20.0' :
                                [
                                  'None' 
                                ],
                                # High pt
                                'muon_col[LF_idx]["pt"] > 20.0' :
                                [
                                  'None' 
                                ],
                                  },
                         'iso': ['pfRelIso04_all', 0.4],
                         'idSF':  {
                                    '1-7' : [ 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2016v2/muonID_TH2_SFs_pt_eta.root' ] ,
                                  } ,
                         'isoSF':  {
                                    '1-7' : [ 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2016v2/muonISO_TH2_SFs_pt_eta.root' ] ,
                                   } ,
                         'fakeW' : '/LatinoAnalysis/NanoGardener/python/data/fake_prompt_rates/Full2016/Tight80X/',         
                       } ,
 
                 }, 

},

###____________________Full2016v2_hmumu__________________________

'Full2016v2_hmumu': {

    ## ------------  
    'VetoObjWP' : { 
        'HLTsafe' : {
            'cuts' : { 
                # Common cuts
                'True' :
                [
                    'abs(muon_col[LF_idx]["eta"]) < 2.4' , 
                    'muon_col[LF_idx]["pt"] > 10.0' ,
                ]
            } ,
        }
    } ,

# ------------ 
'FakeObjWP' :  {

        'cut_Tight80x' : {
            'cuts' : { 
                # Common cuts
                'True' :
                [ 
                    'abs(muon_col[LF_idx]["eta"]) < 2.4' ,
                    'muon_col[LF_idx]["mediumId"] == 1' ,
                    ##'abs(muon_col[LF_idx]["dz"]) < 0.1' ,
                    'muon_col[LF_idx]["pfRelIso04_all"] < 0.25',
                    #'muon_col[LF_idx]["trackIso"]/muon_col[LF_idx]["pt"] < 0.4' ,
                ] ,
            } ,
            'idSF':  {
                '1-5' : [ 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2016v2_hmumu/muonID_Medium_TH2_SFs_pt_eta_Run2016BF.root' ] ,
                '6-7' : [ 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2016v2_hmumu/muonID_Medium_TH2_SFs_pt_eta_Run2016GH.root' ] ,
            } ,
            'isoSF':  {
                '1-5' : [ 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2016v2_hmumu/muonISO_Loose_TH2_SFs_pt_eta_Run2016BF.root' ] ,
                '6-7' : [ 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2016v2_hmumu/muonISO_Loose_TH2_SFs_pt_eta_Run2016GH.root' ] ,
            } ,
        } ,
    } ,

# ------------ 
    'WgStarObjWP' :  {
        'cut_Tight80x' : {
            'cuts' : { 
                # Common cuts
                'True' :
                [ 
                    'abs(muon_col[LF_idx]["eta"]) < 2.4' ,
                    'muon_col[LF_idx]["mediumId"] == 1' ,
                    ##'abs(muon_col[LF_idx]["dz"]) < 0.1' ,
                    'muon_col[LF_idx]["pfRelIso04_all"] < 0.25',
                    #'muon_col[LF_idx]["trackIso"]/muon_col[LF_idx]["pt"] < 0.4' ,
                ] ,
            } ,
            'idSF':  {
                '1-5' : [ 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2016v2_hmumu/muonID_Medium_TH2_SFs_pt_eta_Run2016BF.root' ] ,
                '6-7' : [ 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2016v2_hmumu/muonID_Medium_TH2_SFs_pt_eta_Run2016GH.root' ] ,
            } ,
            'isoSF':  {
                '1-5' : [ 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2016v2_hmumu/muonISO_Loose_TH2_SFs_pt_eta_Run2016BF.root' ] ,
                '6-7' : [ 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2016v2_hmumu/muonISO_Loose_TH2_SFs_pt_eta_Run2016GH.root' ] ,
            } ,
        } ,
    } ,

# ------------ 
    'TightObjWP' :  {

        ### POG Medium WP
        'cut_Medium80x' : {
            'cuts' : { 
                # Common cuts
                'True' :
                [ 
                    'abs(muon_col[LF_idx]["eta"]) < 2.4' ,
                    'muon_col[LF_idx]["mediumId"] == 1' ,
                    ##'abs(muon_col[LF_idx]["dz"]) < 0.1' ,
                    'muon_col[LF_idx]["pfRelIso04_all"] < 0.25',
                    #'muon_col[LF_idx]["trackIso"]/muon_col[LF_idx]["pt"] < 0.4' ,
                ] ,
            } ,
            'idSF':  {    
                '1-5' : [ 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2016v2_hmumu/muonID_Medium_TH2_SFs_pt_eta_Run2016BF.root' ] ,
                '6-7' : [ 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2016v2_hmumu/muonID_Medium_TH2_SFs_pt_eta_Run2016GH.root' ] ,
            } ,
            'isoSF':  {
                '1-5' : [ 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2016v2_hmumu/muonISO_Loose_TH2_SFs_pt_eta_Run2016BF.root' ] ,
                '6-7' : [ 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2016v2_hmumu/muonISO_Loose_TH2_SFs_pt_eta_Run2016GH.root' ] ,
            } ,
        } ,

        ### POG Tight WP
        'cut_Tight80x' : {
            'cuts' : { 
                # Common cuts
                'True' :
                [ 
                    'abs(muon_col[LF_idx]["eta"]) < 2.4' ,
                    'muon_col[LF_idx]["tightId"] == 1' ,
                    ##'abs(muon_col[LF_idx]["dz"]) < 0.1' ,
                    'muon_col[LF_idx]["pfRelIso04_all"] < 0.15',
                    #'muon_col[LF_idx]["trackIso"]/muon_col[LF_idx]["pt"] < 0.4' ,
                ] ,
            } ,### have to updatre SFs!!!!
            'idSF':  {
                '1-5' : [ 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2016v2_hmumu/muonID_Tight_TH2_SFs_pt_eta_Run2016BF.root' ] ,
                '6-7' : [ 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2016v2_hmumu/muonID_Tight_TH2_SFs_pt_eta_Run2016GH.root' ] ,
            } ,
            'isoSF':  {
                '1-5' : [ 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2016v2_hmumu/muonISO_Tight_TH2_SFs_pt_eta_Run2016BF.root' ] ,
                '6-7' : [ 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2016v2_hmumu/muonISO_Tight_TH2_SFs_pt_eta_Run2016GH.root' ] ,
            } ,
        } ,
    } ,
},
    

###____________________Full2016__________________________

'Full2016': {

## ------------  
 'VetoObjWP' : { 
      'HLTsafe' : {
                         'cuts' : { 
                                # Common cuts
                                'True' :
                                 [
                                   'abs(muon_col[LF_idx]["eta"]) < 2.4' , 
                                   'muon_col[LF_idx]["pt"] > 10.0' ,
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
                                   'abs(muon_col[LF_idx]["eta"]) < 2.4' , 
                                   'muon_col[LF_idx]["tightId"] == 1' ,
                                   'abs(muon_col[LF_idx]["dz"]) < 0.1' ,
                                   'muon_col[LF_idx]["pfRelIso04_all"] < 0.4',
                                   #'muon_col[LF_idx]["trackIso"]/muon_col[LF_idx]["pt"] < 0.4' ,
                                 ] ,
                                 # dxy for pT < 20 GeV
                                 'muon_col[LF_idx]["pt"] <= 20.0' :
                                 [
                                    'abs(muon_col[LF_idx]["dxy"]) < 0.01 ' ,
                                 ] ,
                                 # dxy for pT > 20 GeV
                                 'muon_col[LF_idx]["pt"] > 20.0' :
                                 [
                                    'abs(muon_col[LF_idx]["dxy"]) < 0.02 ' ,
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
                                   'abs(muon_col[LF_idx]["eta"]) < 2.4' ,
                                   'muon_col[LF_idx]["tightId"] == 1' ,
                                   'abs(muon_col[LF_idx]["dz"]) < 0.1' ,
                                   'muon_col[LF_idx]["pfRelIso04_all"] < 0.15',
                                   #'muon_col[LF_idx]["trackIso"]/muon_col[LF_idx]["pt"] < 0.4' ,
                                 ] ,
                                 # dxy for pT < 20 GeV
                                 'muon_col[LF_idx]["pt"] <= 20.0' :
                                 [
                                    'abs(muon_col[LF_idx]["dxy"]) < 0.01 ' ,
                                 ] ,
                                 # dxy for pT > 20 GeV
                                 'muon_col[LF_idx]["pt"] > 20.0' :
                                 [
                                    'abs(muon_col[LF_idx]["dxy"]) < 0.02 ' ,
                                 ] ,
                                  } ,
                         'tkSF':  { 
                                    '1-4' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2016/trackerSF_Moriond17_MuoPOG_BCDEF.root' ,
                                    '5-7' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2016/trackerSF_Moriond17_MuoPOG_GH.root' ,
                                  } ,
                         'tkSFerror': 0.01,
                         'idSF':  {
                                    '1-4' : [ 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2016/Tight_Run2016BCDEF_PTvsETA_HWW.txt' ,
                                              'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2016/TightID_DY_madgraphLikeRun2016BCDEF_PTvsETA_HWW.txt' ] ,
                                    '5-7' : [ 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2016/Tight_Run2016GH_PTvsETA_HWW.txt' ,
                                              'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2016/TightID_DY_madgraphLikeRun2016GH_PTvsETA_HWW.txt' ] ,
                                  } ,
                         'isoSF':  {
                                    '1-4' : [ 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2016/ISOTight_Run2016BCDEF_PTvsETA_HWW.txt' ,
                                              'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2016/ISOTight_DY_madgraphLikeRun2016BCDEF_PTvsETA_HWW.txt' ] ,
                                    '5-7' : [ 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2016/ISOTight_Run2016GH_PTvsETA_HWW.txt' ,
                                              'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2016/ISOTight_DY_madgraphLikeRun2016GH_PTvsETA_HWW.txt' ] , 
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
                                   'abs(muon_col[LF_idx]["eta"]) < 2.4' ,
                                   'muon_col[LF_idx]["tightId"] == 1' ,
                                   'abs(muon_col[LF_idx]["dz"]) < 0.1' ,
                                   #'(muon_col[LF_idx]["pfRelIso04_all"] - self.ConeOverlapPt(lepton_col, iLep)/muon_col[LF_idx]["pt"]) < 0.15',
                                   ##'muon_col[LF_idx]["trackIso"]/muon_col[LF_idx]["pt"] < 0.4' ,
                                 ] ,
                                 # dxy for pT < 20 GeV
                                 'muon_col[LF_idx]["pt"] <= 20.0' :
                                 [
                                    'abs(muon_col[LF_idx]["dxy"]) < 0.01 ' ,
                                 ] ,
                                 # dxy for pT > 20 GeV
                                 'muon_col[LF_idx]["pt"] > 20.0' :
                                 [
                                    'abs(muon_col[LF_idx]["dxy"]) < 0.02 ' ,
                                 ] ,
                                  } ,
                         'cuts_iso': {
                                # Common cuts
                                'True' :
                                [
                                  '0.15',
                                ],
                                # Low pt
                                'muon_col[LF_idx]["pt"] <= 20.0' :
                                [
                                  'None' 
                                ],
                                # High pt
                                'muon_col[LF_idx]["pt"] > 20.0' :
                                [
                                  'None' 
                                ],
                                  },
                         'iso': ['pfRelIso04_all', 0.4],
                       } ,
 
                 }, 
},

}

# ... ans copy Full2017v2 in Full2017 (unchanfed WP's) 
MuonWP['Full2017'] = MuonWP['Full2017v2']
MuonWP['Full2017v2LP19'] = MuonWP['Full2017v2']
MuonWP['Full2017v2LP19']['TightObjWP']['cut_Tight_HWWW']['fakeW']='/LatinoAnalysis/NanoGardener/python/data/fake_prompt_rates/Full2017LP19/'
# .... and copy Full2016v2 in Full2017v4 (only Electron WP names were changed)
MuonWP['Full2016v4'] = MuonWP['Full2016v2']
MuonWP['Full2017v4'] = MuonWP['Full2017v2']
MuonWP['Full2018v4'] = MuonWP['Full2018']
# .... and copy Full2016v2 in Full2017v5 (only Electron WP names were changed)
MuonWP['Full2016v5'] = MuonWP['Full2016v2']
MuonWP['Full2016v5_mh'] = MuonWP['Full2016v2']
MuonWP['Full2016v5_mh']['TightObjWP']['cut_Tight80x']['fakeW']='/LatinoAnalysis/NanoGardener/python/data/fake_prompt_rates/MonoHiggs/' 
# still using same fakes: MuonWP['Full2016v5']['TightObjWP']['cut_Tight80x']['fakeW']='/LatinoAnalysis/NanoGardener/python/data/fake_prompt_rates/Full2016v5/'
MuonWP['Full2017v5'] = MuonWP['Full2017v2']
MuonWP['Full2017v5']['TightObjWP']['cut_Tight_HWWW']['fakeW']='/LatinoAnalysis/NanoGardener/python/data/fake_prompt_rates/Full2017v5/mvaFall17V1Iso_WP90/'
MuonWP['Full2018v5'] = MuonWP['Full2018']
MuonWP['Full2018v5']['TightObjWP']['cut_Tight_HWWW']['fakeW']='/LatinoAnalysis/NanoGardener/python/data/fake_prompt_rates/Full2018v5/mvaFall17V1Iso_WP90/'
# and cloning MuonWP for Full201Xv6
MuonWP['Full2016v6'] = MuonWP['Full2016v2']
MuonWP['Full2017v6'] = MuonWP['Full2017v2']
MuonWP['Full2017v6']['TightObjWP']['cut_Tight_HWWW']['fakeW']='/LatinoAnalysis/NanoGardener/python/data/fake_prompt_rates/Full2017v5/mvaFall17V1Iso_WP90/'
MuonWP['Full2018v6'] = MuonWP['Full2018']
MuonWP['Full2018v6']['TightObjWP']['cut_Tight_HWWW']['fakeW']='/LatinoAnalysis/NanoGardener/python/data/fake_prompt_rates/Full2018v5/mvaFall17V1Iso_WP90/'
 
if __name__ == '__main__':
    print('_______________LepFilter_dict___________')
    print(LepFilter_dict)
    print('') 
    print('_______________ElectronWP_______________')
    print('')
    for key in ElectronWP:
        print('__________' + key + '__________')
        print('')
        for typ in ElectronWP[key]:
            print('_____' + typ + '_____')
            for entr in ElectronWP[key][typ]:
                print(entr + ' =')
                print(ElectronWP[key][typ][entr]['cuts'])
                print('')
                for info in ElectronWP[key][typ][entr]:
                    if not (info == 'cuts'):
                        print(info)
                        print(ElectronWP[key][typ][entr][info])
                        print('')
    print('_______________MuonWP___________________')
    print('')
    for key in MuonWP:
        print('__________' + key + '__________')
        print('')
        for typ in MuonWP[key]:
            print('_____' + typ + '_____')
            for entr in MuonWP[key][typ]:
                print(entr + ' =')
                print(MuonWP[key][typ][entr]['cuts'])
                print('')
                for info in MuonWP[key][typ][entr]:
                    if not (info == 'cuts'):
                        print(info)
                        print(MuonWP[key][typ][entr][info])
                        print('')

