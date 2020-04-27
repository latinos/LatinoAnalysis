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

    'Full2016v4': {
        
        'VetoObjWP' : { 
            'cutBasedVeto' : { 
                'cuts' : { 
                    'True' :
                        [
                        'electron_col[LF_idx]["pt"]             >  15.' ,
                        'abs(electron_col[LF_idx]["eta"])       <  2.4' ,
                        'electron_col[LF_idx]["cutBased_Fall17_V1"]  >=   1' ,
                        'abs(electron_col[LF_idx]["sip3d"])     <   4.' ,
                        'abs(electron_col[LF_idx]["dxy"])       < 0.05' ,
                        'abs(electron_col[LF_idx]["dz"])        < 0.10' ,
                        #'abs(electron_col[LF_idx]["miniPFRelIso_all"]) < 0.4',     
                        #'abs(electron_col[LF_idx]["eta"]+electron_col[LF_idx]["deltaEtaSC"])<1.4442 or abs(electron_col[LF_idx]["eta"]+electron_col[LF_idx]["deltaEtaSC"])>1.5660' ,
                        ] ,             
                    },
                } ,
            } ,
  
        'FakeObjWP'  : {
            'cutBasedVeto' : { 
                'cuts' : { 
                    'True' :
                        [
                        'electron_col[LF_idx]["pt"]             >  15.' ,
                        'abs(electron_col[LF_idx]["eta"])       <  2.4' ,
                        'electron_col[LF_idx]["cutBased_Fall17_V1"]  >=   1' ,
                        'abs(electron_col[LF_idx]["sip3d"])     <   4.' ,
                        'abs(electron_col[LF_idx]["dxy"])       < 0.05' ,
                        'abs(electron_col[LF_idx]["dz"])        < 0.10' ,
                        #'abs(electron_col[LF_idx]["miniPFRelIso_all"]) < 0.4',
                        #'abs(electron_col[LF_idx]["eta"]+electron_col[LF_idx]["deltaEtaSC"])<1.4442 or abs(electron_col[LF_idx]["eta"]+electron_col[LF_idx]["deltaEtaSC"])>1.5660' ,
                        ] ,
                    },
                } ,
            } ,
        
        'TightObjWP' : {

            'cutBasedMediumMiniIso' : {
                'cuts' : { 
                    'True' :
                        [
                        'electron_col[LF_idx]["pt"]             >  15.' ,
                        'abs(electron_col[LF_idx]["eta"])       <  2.4' ,
                        'electron_col[LF_idx]["cutBased_Fall17_V1"]   >=  3' ,
                        'abs(electron_col[LF_idx]["sip3d"])     <   4.' ,
                        'abs(electron_col[LF_idx]["dxy"])       < 0.05' ,
                        'abs(electron_col[LF_idx]["dz"])        < 0.10' ,
                        'abs(electron_col[LF_idx]["miniPFRelIso_all"]) < 0.1',
                        #'abs(electron_col[LF_idx]["eta"]+electron_col[LF_idx]["deltaEtaSC"])<1.4442 or abs(electron_col[LF_idx]["eta"]+electron_col[LF_idx]["deltaEtaSC"])>1.5660' ,
                        ] ,
                    } ,
                'tkSF':  { 
                    '1-7' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2016v2/EGM2D_BtoH_combineLowEt_RecoSF_Legacy2016.root' ,
                    } ,
                'susySF':  {
                    '1-7' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2016v2/ElectronScaleFactors_Run2016_SUSY.root#Run2016_CutBasedMediumNoIso94XV2#Run2016_Mini' ,  
                    } ,
                'fsSF': {
                    '1-7' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2016v2/detailed_ele_full_fast_sf_17.root#CutBasedMediumNoIso94XV2_sf#MVAVLooseTightIP2DMini_sf' , 
                    },
                #'fakeW' : '/LatinoAnalysis/Gardener/python/data/fake_prompt_rates/80X/lowPtCorrected/36fb_ele_cut_WP_Tight80X/' ,
                } ,

            'cutBasedMediumPOG' : {
                'cuts' : { 
                    'True' :
                        [
                        'electron_col[LF_idx]["pt"]             >  15.' ,
                        'abs(electron_col[LF_idx]["eta"])       <  2.4' ,
                        'electron_col[LF_idx]["cutBased_Fall17_V1"]   >=  3' ,
                        ] ,
                    } ,
                'tkSF':  { 
                    '1-7' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2016v2/EGM2D_BtoH_combineLowEt_RecoSF_Legacy2016.root' ,
                    } ,
                'susySF':  {
                    '1-7' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2016v2/2016LegacyReReco_ElectronMedium_Fall17V2.root#EGamma_SF2D' ,  
                    } ,
                'fsSF': {
                    '1-7' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2016v2/detailed_ele_full_fast_sf_17.root#CutBasedMediumNoIso94XV2_sf#MVAVLooseTightIP2DMini_sf' , 
                    },
                #'fakeW' : '/LatinoAnalysis/Gardener/python/data/fake_prompt_rates/80X/lowPtCorrected/36fb_ele_cut_WP_Tight80X/' ,
                } ,

            'cutBasedTightMiniIso' : {
                'cuts' : { 
                    'True' :
                        [
                        'electron_col[LF_idx]["pt"]             >  15.' ,
                        'abs(electron_col[LF_idx]["eta"])       <  2.4' ,
                        'electron_col[LF_idx]["cutBased_Fall17_V1"]   >=  4' ,
                        'abs(electron_col[LF_idx]["sip3d"])     <   4.' ,
                        'abs(electron_col[LF_idx]["dxy"])       < 0.05' ,
                        'abs(electron_col[LF_idx]["dz"])        < 0.10' ,
                        'abs(electron_col[LF_idx]["miniPFRelIso_all"]) < 0.2',
                        #'abs(electron_col[LF_idx]["eta"]+electron_col[LF_idx]["deltaEtaSC"])<1.4442 or abs(electron_col[LF_idx]["eta"]+electron_col[LF_idx]["deltaEtaSC"])>1.5660' ,
                        ] ,
                    } ,
                'tkSF':  { 
                    '1-7' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2016v2/EGM2D_BtoH_combineLowEt_RecoSF_Legacy2016.root' ,
                    } ,
                'susySF':  {
                    '1-7' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2016v2/ElectronScaleFactors_Run2016_SUSY.root#Run2016_CutBasedTightNoIso94XV2#Run2016_Mini2' ,  
                    } ,
                'fsSF': {
                    '1-7' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2016v2/detailed_ele_full_fast_sf_17.root#CutBasedTightNoIso94XV2_sf#MVAVLooseTightIP2DMini2_sf' , 
                    },
                #'fakeW' : '/LatinoAnalysis/Gardener/python/data/fake_prompt_rates/80X/lowPtCorrected/36fb_ele_cut_WP_Tight80X/' ,
                } ,

            'cutBasedTightIsoTight' : {
                'cuts' : { 
                    'True' :
                        [
                        'electron_col[LF_idx]["pt"]             >  15.' ,
                        'abs(electron_col[LF_idx]["eta"])       <  2.4' ,
                        'electron_col[LF_idx]["cutBased_Fall17_V1"]   >=  4' ,
                        'abs(electron_col[LF_idx]["sip3d"])     <   4.' ,
                        'abs(electron_col[LF_idx]["dxy"])       < 0.05' ,
                        'abs(electron_col[LF_idx]["dz"])        < 0.10' ,
                        'abs(electron_col[LF_idx]["miniPFRelIso_all"]) < 0.1',
                        #'abs(electron_col[LF_idx]["eta"]+electron_col[LF_idx]["deltaEtaSC"])<1.4442 or abs(electron_col[LF_idx]["eta"]+electron_col[LF_idx]["deltaEtaSC"])>1.5660' ,
                        ] ,
                    } ,
                'tkSF':  { 
                    '1-7' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2016v2/EGM2D_BtoH_combineLowEt_RecoSF_Legacy2016.root' ,
                    } ,
                'susySF':  {
                    '1-7' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2016v2/ElectronScaleFactors_Run2016_SUSY.root#Run2016_CutBasedTightNoIso94XV2#Run2016_Mini' ,  
                    } ,
                'fsSF': {
                    '1-7' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2016v2/detailed_ele_full_fast_sf_17.root#CutBasedTightNoIso94XV2_sf#MVAVLooseTightIP2DMini_sf' , 
                    },
                #'fakeW' : '/LatinoAnalysis/Gardener/python/data/fake_prompt_rates/80X/lowPtCorrected/36fb_ele_cut_WP_Tight80X/' ,
                } ,

            'cutBased_mvaWP80' : {
                'cuts' : { 
                    'True' :
                        [
                        'electron_col[LF_idx]["pt"]             >  15.' ,
                        'abs(electron_col[LF_idx]["eta"])       <  2.4' ,
                        'electron_col[LF_idx]["mvaFall17V2Iso_WP80"]   ==  1' ,
                        'abs(electron_col[LF_idx]["sip3d"])     <   4.' ,
                        'abs(electron_col[LF_idx]["dxy"])       < 0.05' ,
                        'abs(electron_col[LF_idx]["dz"])        < 0.10' ,
                        #'abs(electron_col[LF_idx]["miniPFRelIso_all"]) < 0.2',
                        #'abs(electron_col[LF_idx]["eta"]+electron_col[LF_idx]["deltaEtaSC"])<1.4442 or abs(electron_col[LF_idx]["eta"]+electron_col[LF_idx]["deltaEtaSC"])>1.5660' ,
                        ] ,
                    } ,
                'tkSF':  { 
                    '1-7' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2016v2/EGM2D_BtoH_combineLowEt_RecoSF_Legacy2016.root' ,
                    } ,
                'susySF':  {
                    '1-7' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2016v2/2016LegacyReReco_ElectronMVA80_Fall17V2.root#EGamma_SF2D' ,  
                    } ,
                'fsSF': {
                    '1-7' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2016v2/detailed_ele_full_fast_sf_17.root#MVATightTightIP2D3D_sf#MVAVLooseTightIP2DMini4_sf' , 
                    },
                #'fakeW' : '/LatinoAnalysis/Gardener/python/data/fake_prompt_rates/80X/lowPtCorrected/36fb_ele_cut_WP_Tight80X/' ,
                } ,

            'cutBased_mvaWP90' : {
                'cuts' : { 
                    'True' :
                        [
                        'electron_col[LF_idx]["pt"]             >  15.' ,
                        'abs(electron_col[LF_idx]["eta"])       <  2.4' ,
                        'electron_col[LF_idx]["mvaFall17V2Iso_WP90"]   ==  1' ,
                        'abs(electron_col[LF_idx]["sip3d"])     <   4.' ,
                        'abs(electron_col[LF_idx]["dxy"])       < 0.05' ,
                        'abs(electron_col[LF_idx]["dz"])        < 0.10' ,
                        #'abs(electron_col[LF_idx]["miniPFRelIso_all"]) < 0.2',
                        #'abs(electron_col[LF_idx]["eta"]+electron_col[LF_idx]["deltaEtaSC"])<1.4442 or abs(electron_col[LF_idx]["eta"]+electron_col[LF_idx]["deltaEtaSC"])>1.5660' ,
                        ] ,
                    } ,
                'tkSF':  { 
                    '1-7' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2016v2/EGM2D_BtoH_combineLowEt_RecoSF_Legacy2016.root' ,
                    } ,
                'susySF':  {
                    '1-7' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2016v2/2016LegacyReReco_ElectronMVA90_Fall17V2.root#EGamma_SF2D' ,  
                    } ,
                'fsSF': {
                    '1-7' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2016v2/detailed_ele_full_fast_sf_17.root#MVATightTightIP2D3D_sf#MVAVLooseTightIP2DMini4_sf' , 
                    },
                #'fakeW' : '/LatinoAnalysis/Gardener/python/data/fake_prompt_rates/80X/lowPtCorrected/36fb_ele_cut_WP_Tight80X/' ,
                } ,

            },
        
        'WgStarObjWP' : {
            'null' : { 
                'cuts' : { 
                    'True' :
                        [
                        'False' ,
                        ] ,
                    } ,
                } ,
            }, 

        }, 

    'Full2017v4': {
        
        'VetoObjWP' : { 
            'cutBasedVeto' : { 
                'cuts' : { 
                    'True' :
                        [
                        'electron_col[LF_idx]["pt"]             >  15.' ,
                        'abs(electron_col[LF_idx]["eta"])       <  2.4' ,
                        'electron_col[LF_idx]["cutBased_Fall17_V1"]  >=   1' ,
                        'abs(electron_col[LF_idx]["sip3d"])     <   4.' ,
                        'abs(electron_col[LF_idx]["dxy"])       < 0.05' ,
                        'abs(electron_col[LF_idx]["dz"])        < 0.10' ,
                        #'abs(electron_col[LF_idx]["miniPFRelIso_all"]) < 0.4',     
                        #'abs(electron_col[LF_idx]["eta"]+electron_col[LF_idx]["deltaEtaSC"])<1.4442 or abs(electron_col[LF_idx]["eta"]+electron_col[LF_idx]["deltaEtaSC"])>1.5660' ,
                        ] ,             
                    },
                } ,
            } ,
  
        'FakeObjWP'  : {
            'cutBasedVeto' : { 
                'cuts' : { 
                    'True' :
                        [
                        'electron_col[LF_idx]["pt"]             >  15.' ,
                        'abs(electron_col[LF_idx]["eta"])       <  2.4' ,
                        'electron_col[LF_idx]["cutBased_Fall17_V1"]  >=   1' ,
                        'abs(electron_col[LF_idx]["sip3d"])     <   4.' ,
                        'abs(electron_col[LF_idx]["dxy"])       < 0.05' ,
                        'abs(electron_col[LF_idx]["dz"])        < 0.10' ,
                        #'abs(electron_col[LF_idx]["miniPFRelIso_all"]) < 0.4',
                        #'abs(electron_col[LF_idx]["eta"]+electron_col[LF_idx]["deltaEtaSC"])<1.4442 or abs(electron_col[LF_idx]["eta"]+electron_col[LF_idx]["deltaEtaSC"])>1.5660' ,
                        ] ,
                    },
                } ,
            } ,
        
        'TightObjWP' : {

            'cutBasedMediumMiniIso' : {
                'cuts' : { 
                    'True' :
                        [
                        'electron_col[LF_idx]["pt"]             >  15.' ,
                        'abs(electron_col[LF_idx]["eta"])       <  2.4' ,
                        'electron_col[LF_idx]["cutBased_Fall17_V1"]   >=  3' ,
                        'abs(electron_col[LF_idx]["sip3d"])     <   4.' ,
                        'abs(electron_col[LF_idx]["dxy"])       < 0.05' ,
                        'abs(electron_col[LF_idx]["dz"])        < 0.10' ,
                        'abs(electron_col[LF_idx]["miniPFRelIso_all"]) < 0.1',
                        #'abs(electron_col[LF_idx]["eta"]+electron_col[LF_idx]["deltaEtaSC"])<1.4442 or abs(electron_col[LF_idx]["eta"]+electron_col[LF_idx]["deltaEtaSC"])>1.5660' ,
                        ] ,
                    } ,
                'tkSF':  { 
                    '1-1' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/egammaEffi.txt_EGM2D_runB_passingRECO_combineLowEt.root',
                    '2-2' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/egammaEffi.txt_EGM2D_runC_passingRECO_combineLowEt.root',
                    '3-3' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/egammaEffi.txt_EGM2D_runD_passingRECO_combineLowEt.root',
                    '4-4' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/egammaEffi.txt_EGM2D_runE_passingRECO_combineLowEt.root',
                    '5-5' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/egammaEffi.txt_EGM2D_runF_passingRECO_combineLowEt.root',
                  } ,
                'susySF':  {
                    '1-1' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/ElectronScaleFactors_Run2017_SUSY.root#Run2017_CutBasedMediumNoIso94XV2#Run2017_MVAVLooseTightIP2DMini' , 
                    '2-2' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/ElectronScaleFactors_Run2017_SUSY.root#Run2017_CutBasedMediumNoIso94XV2#Run2017_MVAVLooseTightIP2DMini' , 
                    '3-3' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/ElectronScaleFactors_Run2017_SUSY.root#Run2017_CutBasedMediumNoIso94XV2#Run2017_MVAVLooseTightIP2DMini' , 
                    '4-4' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/ElectronScaleFactors_Run2017_SUSY.root#Run2017_CutBasedMediumNoIso94XV2#Run2017_MVAVLooseTightIP2DMini' , 
                    '5-5' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/ElectronScaleFactors_Run2017_SUSY.root#Run2017_CutBasedMediumNoIso94XV2#Run2017_MVAVLooseTightIP2DMini' ,  
                    } ,
                'fsSF': {
                    '1-5' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/detailed_ele_full_fast_sf_17.root#CutBasedMediumNoIso94XV2_sf#MVAVLooseTightIP2DMini_sf' , 
                    },
                } ,

            'cutBasedMediumPOG' : {
                'cuts' : { 
                    'True' :
                        [
                        'electron_col[LF_idx]["pt"]             >  15.' ,
                        'abs(electron_col[LF_idx]["eta"])       <  2.4' ,
                        'electron_col[LF_idx]["cutBased_Fall17_V1"]   >=  3' ,
                        ] ,
                    } ,
                'tkSF':  { 
                    '1-1' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/egammaEffi.txt_EGM2D_runB_passingRECO_combineLowEt.root',
                    '2-2' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/egammaEffi.txt_EGM2D_runC_passingRECO_combineLowEt.root',
                    '3-3' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/egammaEffi.txt_EGM2D_runD_passingRECO_combineLowEt.root',
                    '4-4' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/egammaEffi.txt_EGM2D_runE_passingRECO_combineLowEt.root',
                    '5-5' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/egammaEffi.txt_EGM2D_runF_passingRECO_combineLowEt.root',
                  } ,
                'susySF':  {
                    '1-1' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/2017_ElectronMedium_POG.root#EGamma_SF2D' , 
                    '2-2' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/2017_ElectronMedium_POG.root#EGamma_SF2D' , 
                    '3-3' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/2017_ElectronMedium_POG.root#EGamma_SF2D' , 
                    '4-4' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/2017_ElectronMedium_POG.root#EGamma_SF2D' , 
                    '5-5' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/2017_ElectronMedium_POG.root#EGamma_SF2D' , 
                    } ,
                'fsSF': {
                    '1-5' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/detailed_ele_full_fast_sf_17.root#CutBasedMediumNoIso94XV2_sf#MVAVLooseTightIP2DMini_sf' , 
                    },
                } ,

            'cutBasedTightMiniIso' : {
                'cuts' : { 
                    'True' :
                        [
                        'electron_col[LF_idx]["pt"]             >  15.' ,
                        'abs(electron_col[LF_idx]["eta"])       <  2.4' ,
                        'electron_col[LF_idx]["cutBased_Fall17_V1"]   >=  4' ,
                        'abs(electron_col[LF_idx]["sip3d"])     <   4.' ,
                        'abs(electron_col[LF_idx]["dxy"])       < 0.05' ,
                        'abs(electron_col[LF_idx]["dz"])        < 0.10' ,
                        'abs(electron_col[LF_idx]["miniPFRelIso_all"]) < 0.2',
                        #'abs(electron_col[LF_idx]["eta"]+electron_col[LF_idx]["deltaEtaSC"])<1.4442 or abs(electron_col[LF_idx]["eta"]+electron_col[LF_idx]["deltaEtaSC"])>1.5660' ,
                        ] ,
                    } ,
                'tkSF':  { 
                    '1-1' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/egammaEffi.txt_EGM2D_runB_passingRECO_combineLowEt.root',
                    '2-2' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/egammaEffi.txt_EGM2D_runC_passingRECO_combineLowEt.root',
                    '3-3' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/egammaEffi.txt_EGM2D_runD_passingRECO_combineLowEt.root',
                    '4-4' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/egammaEffi.txt_EGM2D_runE_passingRECO_combineLowEt.root',
                    '5-5' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/egammaEffi.txt_EGM2D_runF_passingRECO_combineLowEt.root',
                  } ,
                'susySF':  {
                    '1-1' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/ElectronScaleFactors_Run2017_SUSY.root#Run2017_CutBasedTightNoIso94XV2#Run2017_MVAVLooseTightIP2DMini2' ,  
                    '2-2' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/ElectronScaleFactors_Run2017_SUSY.root#Run2017_CutBasedTightNoIso94XV2#Run2017_MVAVLooseTightIP2DMini2' ,  
                    '3-3' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/ElectronScaleFactors_Run2017_SUSY.root#Run2017_CutBasedTightNoIso94XV2#Run2017_MVAVLooseTightIP2DMini2' ,  
                    '4-4' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/ElectronScaleFactors_Run2017_SUSY.root#Run2017_CutBasedTightNoIso94XV2#Run2017_MVAVLooseTightIP2DMini2' ,  
                    '5-5' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/ElectronScaleFactors_Run2017_SUSY.root#Run2017_CutBasedTightNoIso94XV2#Run2017_MVAVLooseTightIP2DMini2' ,  
                    } ,
                'fsSF': {
                    '1-5' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/detailed_ele_full_fast_sf_17.root#CutBasedTightNoIso94XV2_sf#MVAVLooseTightIP2DMini2_sf' , 
                    },
                } ,

            'cutBasedTightIsoTight' : {
                'cuts' : { 
                    'True' :
                        [
                        'electron_col[LF_idx]["pt"]             >  15.' ,
                        'abs(electron_col[LF_idx]["eta"])       <  2.4' ,
                        'electron_col[LF_idx]["cutBased_Fall17_V1"]   >=  4' ,
                        'abs(electron_col[LF_idx]["sip3d"])     <   4.' ,
                        'abs(electron_col[LF_idx]["dxy"])       < 0.05' ,
                        'abs(electron_col[LF_idx]["dz"])        < 0.10' ,
                        'abs(electron_col[LF_idx]["miniPFRelIso_all"]) < 0.1',
                        #'abs(electron_col[LF_idx]["eta"]+electron_col[LF_idx]["deltaEtaSC"])<1.4442 or abs(electron_col[LF_idx]["eta"]+electron_col[LF_idx]["deltaEtaSC"])>1.5660' ,
                        ] ,
                    } ,
                'tkSF':  { 
                    '1-1' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/egammaEffi.txt_EGM2D_runB_passingRECO_combineLowEt.root',
                    '2-2' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/egammaEffi.txt_EGM2D_runC_passingRECO_combineLowEt.root',
                    '3-3' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/egammaEffi.txt_EGM2D_runD_passingRECO_combineLowEt.root',
                    '4-4' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/egammaEffi.txt_EGM2D_runE_passingRECO_combineLowEt.root',
                    '5-5' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/egammaEffi.txt_EGM2D_runF_passingRECO_combineLowEt.root',
                  } ,
                'susySF':  {
                    '1-1' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/ElectronScaleFactors_Run2017_SUSY.root#Run2017_CutBasedTightNoIso94XV2#Run2017_MVAVLooseTightIP2DMini' ,  
                    '2-2' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/ElectronScaleFactors_Run2017_SUSY.root#Run2017_CutBasedTightNoIso94XV2#Run2017_MVAVLooseTightIP2DMini' ,  
                    '3-3' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/ElectronScaleFactors_Run2017_SUSY.root#Run2017_CutBasedTightNoIso94XV2#Run2017_MVAVLooseTightIP2DMini' ,  
                    '4-4' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/ElectronScaleFactors_Run2017_SUSY.root#Run2017_CutBasedTightNoIso94XV2#Run2017_MVAVLooseTightIP2DMini' ,  
                    '5-5' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/ElectronScaleFactors_Run2017_SUSY.root#Run2017_CutBasedTightNoIso94XV2#Run2017_MVAVLooseTightIP2DMini' ,  
                    } ,
                'fsSF': {
                    '1-5' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/detailed_ele_full_fast_sf_17.root#CutBasedTightNoIso94XV2_sf#MVAVLooseTightIP2DMini_sf' , 
                    },
                } ,

            'cutBased_mvaWP80' : {
                'cuts' : { 
                    'True' :
                        [
                        'electron_col[LF_idx]["pt"]             >  15.' ,
                        'abs(electron_col[LF_idx]["eta"])       <  2.4' ,
                        'electron_col[LF_idx]["mvaFall17V2Iso_WP80"]   ==  1' ,
                        'abs(electron_col[LF_idx]["sip3d"])     <   4.' ,
                        'abs(electron_col[LF_idx]["dxy"])       < 0.05' ,
                        'abs(electron_col[LF_idx]["dz"])        < 0.10' ,
                        #'abs(electron_col[LF_idx]["miniPFRelIso_all"]) < 0.2',
                        #'abs(electron_col[LF_idx]["eta"]+electron_col[LF_idx]["deltaEtaSC"])<1.4442 or abs(electron_col[LF_idx]["eta"]+electron_col[LF_idx]["deltaEtaSC"])>1.5660' ,
                        ] ,
                    } ,
                'tkSF':  { 
                    '1-1' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/egammaEffi.txt_EGM2D_runB_passingRECO_combineLowEt.root',
                    '2-2' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/egammaEffi.txt_EGM2D_runC_passingRECO_combineLowEt.root',
                    '3-3' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/egammaEffi.txt_EGM2D_runD_passingRECO_combineLowEt.root',
                    '4-4' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/egammaEffi.txt_EGM2D_runE_passingRECO_combineLowEt.root',
                    '5-5' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/egammaEffi.txt_EGM2D_runF_passingRECO_combineLowEt.root',
                    } ,
                'susySF':  {
                    '1-1' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/2017_ElectronMVA80_POG.root#EGamma_SF2D' ,
                    '2-2' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/2017_ElectronMVA80_POG.root#EGamma_SF2D' ,
                    '3-3' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/2017_ElectronMVA80_POG.root#EGamma_SF2D' ,
                    '4-4' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/2017_ElectronMVA80_POG.root#EGamma_SF2D' ,
                    '5-5' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/2017_ElectronMVA80_POG.root#EGamma_SF2D' ,  
                    } ,
                'fsSF': {
                    '1-5' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/detailed_ele_full_fast_sf_17.root#MVATightTightIP2D3D_sf#MVAVLooseTightIP2DMini4_sf' , 
                    },
                } ,

            'cutBased_mvaWP90' : {
                'cuts' : { 
                    'True' :
                        [
                        'electron_col[LF_idx]["pt"]             >  15.' ,
                        'abs(electron_col[LF_idx]["eta"])       <  2.4' ,
                        'electron_col[LF_idx]["mvaFall17V2Iso_WP90"]   ==  1' ,
                        'abs(electron_col[LF_idx]["sip3d"])     <   4.' ,
                        'abs(electron_col[LF_idx]["dxy"])       < 0.05' ,
                        'abs(electron_col[LF_idx]["dz"])        < 0.10' ,
                        #'abs(electron_col[LF_idx]["miniPFRelIso_all"]) < 0.2',
                        #'abs(electron_col[LF_idx]["eta"]+electron_col[LF_idx]["deltaEtaSC"])<1.4442 or abs(electron_col[LF_idx]["eta"]+electron_col[LF_idx]["deltaEtaSC"])>1.5660' ,
                        ] ,
                    } ,
                'tkSF':  { 
                    '1-1' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/egammaEffi.txt_EGM2D_runB_passingRECO_combineLowEt.root',
                    '2-2' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/egammaEffi.txt_EGM2D_runC_passingRECO_combineLowEt.root',
                    '3-3' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/egammaEffi.txt_EGM2D_runD_passingRECO_combineLowEt.root',
                    '4-4' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/egammaEffi.txt_EGM2D_runE_passingRECO_combineLowEt.root',
                    '5-5' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/egammaEffi.txt_EGM2D_runF_passingRECO_combineLowEt.root',
                    } ,
                'susySF':  {
                    '1-1' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/2017_ElectronMVA90_POG.root#EGamma_SF2D' ,
                    '2-2' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/2017_ElectronMVA90_POG.root#EGamma_SF2D' ,
                    '3-3' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/2017_ElectronMVA90_POG.root#EGamma_SF2D' ,
                    '4-4' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/2017_ElectronMVA90_POG.root#EGamma_SF2D' ,
                    '5-5' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/2017_ElectronMVA90_POG.root#EGamma_SF2D' ,  
                    } ,
                'fsSF': {
                    '1-5' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/detailed_ele_full_fast_sf_17.root#MVATightTightIP2D3D_sf#MVAVLooseTightIP2DMini4_sf' , 
                    },
                } ,

            },
        
        'WgStarObjWP' : {
            'null' : { 
                'cuts' : { 
                    'True' :
                        [
                        'False' ,
                        ] ,
                    } ,
                } ,
            }, 

        }, 

    'Full2018v4': {
        
        'VetoObjWP' : { 
            'cutBasedVeto' : { 
                'cuts' : { 
                    'True' :
                        [
                        'electron_col[LF_idx]["pt"]             >  15.' ,
                        'abs(electron_col[LF_idx]["eta"])       <  2.4' ,
                        'electron_col[LF_idx]["cutBased_Fall17_V1"]  >=   1' ,
                        'abs(electron_col[LF_idx]["sip3d"])     <   4.' ,
                        'abs(electron_col[LF_idx]["dxy"])       < 0.05' ,
                        'abs(electron_col[LF_idx]["dz"])        < 0.10' ,
                        #'abs(electron_col[LF_idx]["miniPFRelIso_all"]) < 0.4',     
                        #'abs(electron_col[LF_idx]["eta"]+electron_col[LF_idx]["deltaEtaSC"])<1.4442 or abs(electron_col[LF_idx]["eta"]+electron_col[LF_idx]["deltaEtaSC"])>1.5660' ,
                        ] ,             
                    },
                } ,
            } ,
  
        'FakeObjWP'  : {
            'cutBasedVeto' : { 
                'cuts' : { 
                    'True' :
                        [
                        'electron_col[LF_idx]["pt"]             >  15.' ,
                        'abs(electron_col[LF_idx]["eta"])       <  2.4' ,
                        'electron_col[LF_idx]["cutBased_Fall17_V1"]  >=   1' ,
                        'abs(electron_col[LF_idx]["sip3d"])     <   4.' ,
                        'abs(electron_col[LF_idx]["dxy"])       < 0.05' ,
                        'abs(electron_col[LF_idx]["dz"])        < 0.10' ,
                        #'abs(electron_col[LF_idx]["miniPFRelIso_all"]) < 0.4',
                        #'abs(electron_col[LF_idx]["eta"]+electron_col[LF_idx]["deltaEtaSC"])<1.4442 or abs(electron_col[LF_idx]["eta"]+electron_col[LF_idx]["deltaEtaSC"])>1.5660' ,
                        ] ,
                    },
                } ,
            } ,
        
        'TightObjWP' : {

            'cutBasedMediumMiniIso' : {
                'cuts' : { 
                    'True' :
                        [
                        'electron_col[LF_idx]["pt"]             >  15.' ,
                        'abs(electron_col[LF_idx]["eta"])       <  2.4' ,
                        'electron_col[LF_idx]["cutBased_Fall17_V1"]   >=  3' ,
                        'abs(electron_col[LF_idx]["sip3d"])     <   4.' ,
                        'abs(electron_col[LF_idx]["dxy"])       < 0.05' ,
                        'abs(electron_col[LF_idx]["dz"])        < 0.10' ,
                        'abs(electron_col[LF_idx]["miniPFRelIso_all"]) < 0.1',
                        #'abs(electron_col[LF_idx]["eta"]+electron_col[LF_idx]["deltaEtaSC"])<1.4442 or abs(electron_col[LF_idx]["eta"]+electron_col[LF_idx]["deltaEtaSC"])>1.5660' ,
                        ] ,
                    } ,
                'tkSF':  { 
                    '1-1' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2018/egammaEffi.txt_EGM2D_updatedAll.root',
                    } ,
                'susySF':  {
                    '1-1' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2018/ElectronScaleFactors_Run2018_SUSY.root#Run2018_CutBasedMediumNoIso94XV2#Run2018_Mini' ,  
                    } ,
                'fsSF': {
                    '1-1' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2018/detailed_ele_full_fast_sf_18.root#CutBasedMediumNoIso94XV2_sf#MVAVLooseTightIP2DMini_sf' , 
                    },
                } ,

            'cutBasedMediumPOG' : {
                'cuts' : { 
                    'True' :
                        [
                        'electron_col[LF_idx]["pt"]             >  15.' ,
                        'abs(electron_col[LF_idx]["eta"])       <  2.4' ,
                        'electron_col[LF_idx]["cutBased_Fall17_V1"]   >=  3' ,
                        ] ,
                    } ,
                'tkSF':  { 
                    '1-1' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2018/egammaEffi.txt_EGM2D_updatedAll.root',
                    } ,
                'susySF':  {
                    '1-1' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2018/2018_ElectronMedium_POG.root#EGamma_SF2D' ,  
                    } ,
                'fsSF': {
                    '1-1' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2018/detailed_ele_full_fast_sf_18.root#CutBasedMediumNoIso94XV2_sf#MVAVLooseTightIP2DMini_sf' , 
                    },
                } ,

            'cutBasedTightMiniIso' : {
                'cuts' : { 
                    'True' :
                        [
                        'electron_col[LF_idx]["pt"]             >  15.' ,
                        'abs(electron_col[LF_idx]["eta"])       <  2.4' ,
                        'electron_col[LF_idx]["cutBased_Fall17_V1"]   >=  4' ,
                        'abs(electron_col[LF_idx]["sip3d"])     <   4.' ,
                        'abs(electron_col[LF_idx]["dxy"])       < 0.05' ,
                        'abs(electron_col[LF_idx]["dz"])        < 0.10' ,
                        'abs(electron_col[LF_idx]["miniPFRelIso_all"]) < 0.2',
                        #'abs(electron_col[LF_idx]["eta"]+electron_col[LF_idx]["deltaEtaSC"])<1.4442 or abs(electron_col[LF_idx]["eta"]+electron_col[LF_idx]["deltaEtaSC"])>1.5660' ,
                        ] ,
                    } ,
                'tkSF':  { 
                    '1-1' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2018/egammaEffi.txt_EGM2D_updatedAll.root',
                    } ,
                'susySF':  {
                    '1-1' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2018/ElectronScaleFactors_Run2018_SUSY.root#Run2018_CutBasedTightNoIso94XV2#Run2018_Mini2' ,  
                    } ,
                'fsSF': {
                    '1-1' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2018/detailed_ele_full_fast_sf_18.root#CutBasedTightNoIso94XV2_sf#MVAVLooseTightIP2DMini2_sf' , 
                    },
                } ,

            'cutBasedTightIsoTight' : {
                'cuts' : { 
                    'True' :
                        [
                        'electron_col[LF_idx]["pt"]             >  15.' ,
                        'abs(electron_col[LF_idx]["eta"])       <  2.4' ,
                        'electron_col[LF_idx]["cutBased_Fall17_V1"]   >=  4' ,
                        'abs(electron_col[LF_idx]["sip3d"])     <   4.' ,
                        'abs(electron_col[LF_idx]["dxy"])       < 0.05' ,
                        'abs(electron_col[LF_idx]["dz"])        < 0.10' ,
                        'abs(electron_col[LF_idx]["miniPFRelIso_all"]) < 0.1',
                        #'abs(electron_col[LF_idx]["eta"]+electron_col[LF_idx]["deltaEtaSC"])<1.4442 or abs(electron_col[LF_idx]["eta"]+electron_col[LF_idx]["deltaEtaSC"])>1.5660' ,
                        ] ,
                    } ,
                'tkSF':  { 
                    '1-1' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2018/egammaEffi.txt_EGM2D_updatedAll.root',
                    } ,
                'susySF':  {
                    '1-1' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2018/ElectronScaleFactors_Run2018_SUSY.root#Run2018_CutBasedTightNoIso94XV2#Run2018_Mini' ,  
                    } ,
                'fsSF': {
                    '1-1' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2018/detailed_ele_full_fast_sf_18.root#CutBasedTightNoIso94XV2_sf#MVAVLooseTightIP2DMini_sf' , 
                    },
                } ,

            'cutBased_mvaWP80' : {
                'cuts' : { 
                    'True' :
                        [
                        'electron_col[LF_idx]["pt"]             >  15.' ,
                        'abs(electron_col[LF_idx]["eta"])       <  2.4' ,
                        'electron_col[LF_idx]["mvaFall17V2Iso_WP80"]   ==  1' ,
                        'abs(electron_col[LF_idx]["sip3d"])     <   4.' ,
                        'abs(electron_col[LF_idx]["dxy"])       < 0.05' ,
                        'abs(electron_col[LF_idx]["dz"])        < 0.10' ,
                        #'abs(electron_col[LF_idx]["miniPFRelIso_all"]) < 0.2',
                        #'abs(electron_col[LF_idx]["eta"]+electron_col[LF_idx]["deltaEtaSC"])<1.4442 or abs(electron_col[LF_idx]["eta"]+electron_col[LF_idx]["deltaEtaSC"])>1.5660' ,
                        ] ,
                    } ,
                'tkSF':  { 
                    '1-1' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2018/egammaEffi.txt_EGM2D_updatedAll.root',
                    } ,
                'susySF':  {
                    '1-1' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2018/2018_ElectronMVA80_POG.root#EGamma_SF2D' ,  
                    } ,
                'fsSF': {
                    '1-1' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2018/detailed_ele_full_fast_sf_18.root#MVATightTightIP2D3D_sf#MVAVLooseTightIP2DMini4_sf' , 
                    },
                } ,

            'cutBased_mvaWP90' : {
                'cuts' : { 
                    'True' :
                        [
                        'electron_col[LF_idx]["pt"]             >  15.' ,
                        'abs(electron_col[LF_idx]["eta"])       <  2.4' ,
                        'electron_col[LF_idx]["mvaFall17V2Iso_WP90"]   ==  1' ,
                        'abs(electron_col[LF_idx]["sip3d"])     <   4.' ,
                        'abs(electron_col[LF_idx]["dxy"])       < 0.05' ,
                        'abs(electron_col[LF_idx]["dz"])        < 0.10' ,
                        #'abs(electron_col[LF_idx]["miniPFRelIso_all"]) < 0.2',
                        #'abs(electron_col[LF_idx]["eta"]+electron_col[LF_idx]["deltaEtaSC"])<1.4442 or abs(electron_col[LF_idx]["eta"]+electron_col[LF_idx]["deltaEtaSC"])>1.5660' ,
                        ] ,
                    } ,
                'tkSF':  { 
                    '1-1' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2018/egammaEffi.txt_EGM2D_updatedAll.root',
                    } ,
                'susySF':  {
                    '1-1' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2018/2018_ElectronMVA90_POG.root#EGamma_SF2D' ,  
                    } ,
                'fsSF': {
                    '1-1' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2018/detailed_ele_full_fast_sf_18.root#MVATightTightIP2D3D_sf#MVAVLooseTightIP2DMini4_sf' , 
                    },
                } ,

            },
        
        'WgStarObjWP' : {
            'null' : { 
                'cuts' : { 
                    'True' :
                        [
                        'False' ,
                        ] ,
                    } ,
                } ,
            }, 

        },

    'Full2016v6': {
        
        'VetoObjWP' : { 
            'cutBasedVeto' : { 
                'cuts' : { 
                    'True' :
                        [
                        'electron_col[LF_idx]["pt"]             >  15.' ,
                        'abs(electron_col[LF_idx]["eta"])       <  2.4' ,
                        'electron_col[LF_idx]["cutBased"]  >=   1' ,
                        'abs(electron_col[LF_idx]["sip3d"])     <   4.' ,
                        'abs(electron_col[LF_idx]["dxy"])       < 0.05' ,
                        'abs(electron_col[LF_idx]["dz"])        < 0.10' ,
                        #'abs(electron_col[LF_idx]["miniPFRelIso_all"]) < 0.4',     
                        #'abs(electron_col[LF_idx]["eta"]+electron_col[LF_idx]["deltaEtaSC"])<1.4442 or abs(electron_col[LF_idx]["eta"]+electron_col[LF_idx]["deltaEtaSC"])>1.5660' ,
                        ] ,             
                    },
                } ,
            } ,
  
        'FakeObjWP'  : {
            'cutBasedVeto' : { 
                'cuts' : { 
                    'True' :
                        [
                        'electron_col[LF_idx]["pt"]             >  15.' ,
                        'abs(electron_col[LF_idx]["eta"])       <  2.4' ,
                        'electron_col[LF_idx]["cutBased"]  >=   1' ,
                        'abs(electron_col[LF_idx]["sip3d"])     <   4.' ,
                        'abs(electron_col[LF_idx]["dxy"])       < 0.05' ,
                        'abs(electron_col[LF_idx]["dz"])        < 0.10' ,
                        #'abs(electron_col[LF_idx]["miniPFRelIso_all"]) < 0.4',
                        #'abs(electron_col[LF_idx]["eta"]+electron_col[LF_idx]["deltaEtaSC"])<1.4442 or abs(electron_col[LF_idx]["eta"]+electron_col[LF_idx]["deltaEtaSC"])>1.5660' ,
                        ] ,
                    },
                } ,
            } ,
        
        'TightObjWP' : {

            'cutBasedMediumMiniIso' : {
                'cuts' : { 
                    'True' :
                        [
                        'electron_col[LF_idx]["pt"]             >  15.' ,
                        'abs(electron_col[LF_idx]["eta"])       <  2.4' ,
                        'electron_col[LF_idx]["cutBased"]       >=  3' ,
                        'abs(electron_col[LF_idx]["sip3d"])     <   4.' ,
                        'abs(electron_col[LF_idx]["dxy"])       < 0.05' ,
                        'abs(electron_col[LF_idx]["dz"])        < 0.10' ,
                        'electron_col[LF_idx]["lostHits"]       ==  0',
                        'abs(electron_col[LF_idx]["miniPFRelIso_all"]) < 0.1',
                        #'abs(electron_col[LF_idx]["eta"]+electron_col[LF_idx]["deltaEtaSC"])<1.4442 or abs(electron_col[LF_idx]["eta"]+electron_col[LF_idx]["deltaEtaSC"])>1.5660' ,
                        ] ,
                    } ,
                'tkSF':  { 
                    '1-7' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2016v2/EGM2D_BtoH_combineLowEt_RecoSF_Legacy2016.root' ,
                    } ,
                'susySF':  {
                    '1-7' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2016v2/ElectronScaleFactors_Run2016_SUSY.root#Run2016_CutBasedMediumNoIso94XV2#Run2016_Mini' ,  
                    } ,
                'fsSF': {
                    '1-7' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2016v2/detailed_ele_full_fast_sf_17.root#CutBasedMediumNoIso94XV2_sf#MVAVLooseTightIP2DMini_sf' , 
                    },
                #'fakeW' : '/LatinoAnalysis/Gardener/python/data/fake_prompt_rates/80X/lowPtCorrected/36fb_ele_cut_WP_Tight80X/' ,
                } ,

            'cutBasedMediumPOG' : {
                'cuts' : { 
                    'True' :
                        [
                        'electron_col[LF_idx]["pt"]             >  15.' ,
                        'abs(electron_col[LF_idx]["eta"])       <  2.4' ,
                        'electron_col[LF_idx]["cutBased"]       >=  3' ,
                        'abs(electron_col[LF_idx]["sip3d"])     <   4.' ,
                        'abs(electron_col[LF_idx]["dxy"])       < 0.05' ,
                        'abs(electron_col[LF_idx]["dz"])        < 0.10' ,
                        'electron_col[LF_idx]["lostHits"]       ==  0',
                        ] ,
                    } ,
                'tkSF':  { 
                    '1-7' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2016v2/EGM2D_BtoH_combineLowEt_RecoSF_Legacy2016.root' ,
                    } ,
                'susySF':  {
                    '1-7' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2016v2/2016LegacyReReco_ElectronMedium_Fall17V2.root#EGamma_SF2D' ,  
                    } ,
                'fsSF': {
                    '1-7' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2016v2/detailed_ele_full_fast_sf_17.root#CutBasedMediumNoIso94XV2_sf#MVAVLooseTightIP2DMini_sf' , 
                    },
                #'fakeW' : '/LatinoAnalysis/Gardener/python/data/fake_prompt_rates/80X/lowPtCorrected/36fb_ele_cut_WP_Tight80X/' ,
                } ,

            'cutBasedMediumPOGeta' : {
                'cuts' : { 
                    'True' :
                        [
                        'electron_col[LF_idx]["pt"]             >  15.' ,
                        'abs(electron_col[LF_idx]["eta"])       <  2.4' ,
                        'electron_col[LF_idx]["cutBased"]       >=  3' ,
                        'abs(electron_col[LF_idx]["sip3d"])     <   4.' ,
                        'abs(electron_col[LF_idx]["dxy"])       < 0.05' ,
                        'abs(electron_col[LF_idx]["dz"])        < 0.10' ,
                        'electron_col[LF_idx]["lostHits"]       ==  0',
                        'abs(electron_col[LF_idx]["eta"]+electron_col[LF_idx]["deltaEtaSC"])<1.4442 or abs(electron_col[LF_idx]["eta"]+electron_col[LF_idx]["deltaEtaSC"])>1.5660' ,
                        ] ,
                    } ,
                'tkSF':  { 
                    '1-7' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2016v2/EGM2D_BtoH_combineLowEt_RecoSF_Legacy2016.root' ,
                    } ,
                'susySF':  {
                    '1-7' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2016v2/2016LegacyReReco_ElectronMedium_Fall17V2.root#EGamma_SF2D' ,  
                    } ,
                'fsSF': {
                    '1-7' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2016v2/detailed_ele_full_fast_sf_17.root#CutBasedMediumNoIso94XV2_sf#MVAVLooseTightIP2DMini_sf' , 
                    },
                #'fakeW' : '/LatinoAnalysis/Gardener/python/data/fake_prompt_rates/80X/lowPtCorrected/36fb_ele_cut_WP_Tight80X/' ,
                } ,

            'cutBasedMediumPOGV1' : {
                'cuts' : { 
                    'True' :
                        [
                        'electron_col[LF_idx]["pt"]                 >  15.' ,
                        'abs(electron_col[LF_idx]["eta"])           <  2.4' ,
                        'electron_col[LF_idx]["cutBased_Fall17_V1"] >=  3' ,
                        'abs(electron_col[LF_idx]["sip3d"])         <   4.' ,
                        'abs(electron_col[LF_idx]["dxy"])           < 0.05' ,
                        'abs(electron_col[LF_idx]["dz"])            < 0.10' ,
                        'electron_col[LF_idx]["lostHits"]           ==  0',
                        ] ,
                    } ,
                'tkSF':  { 
                    '1-7' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2016v2/EGM2D_BtoH_combineLowEt_RecoSF_Legacy2016.root' ,
                    } ,
                'susySF':  {
                    '1-7' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2016v2/2016LegacyReReco_ElectronMedium_Fall17V2.root#EGamma_SF2D' ,  
                    } ,
                'fsSF': {
                    '1-7' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2016v2/detailed_ele_full_fast_sf_17.root#CutBasedMediumNoIso94XV2_sf#MVAVLooseTightIP2DMini_sf' , 
                    },
                #'fakeW' : '/LatinoAnalysis/Gardener/python/data/fake_prompt_rates/80X/lowPtCorrected/36fb_ele_cut_WP_Tight80X/' ,
                } ,

            'cutBasedTightMiniIso' : {
                'cuts' : { 
                    'True' :
                        [
                        'electron_col[LF_idx]["pt"]             >  15.' ,
                        'abs(electron_col[LF_idx]["eta"])       <  2.4' ,
                        'electron_col[LF_idx]["cutBased"]       >=  4' ,
                        'abs(electron_col[LF_idx]["sip3d"])     <   4.' ,
                        'abs(electron_col[LF_idx]["dxy"])       < 0.05' ,
                        'abs(electron_col[LF_idx]["dz"])        < 0.10' ,
                        'electron_col[LF_idx]["lostHits"]       ==  0',
                        'abs(electron_col[LF_idx]["miniPFRelIso_all"]) < 0.2',
                        #'abs(electron_col[LF_idx]["eta"]+electron_col[LF_idx]["deltaEtaSC"])<1.4442 or abs(electron_col[LF_idx]["eta"]+electron_col[LF_idx]["deltaEtaSC"])>1.5660' ,
                        ] ,
                    } ,
                'tkSF':  { 
                    '1-7' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2016v2/EGM2D_BtoH_combineLowEt_RecoSF_Legacy2016.root' ,
                    } ,
                'susySF':  {
                    '1-7' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2016v2/ElectronScaleFactors_Run2016_SUSY.root#Run2016_CutBasedTightNoIso94XV2#Run2016_Mini2' ,  
                    } ,
                'fsSF': {
                    '1-7' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2016v2/detailed_ele_full_fast_sf_17.root#CutBasedTightNoIso94XV2_sf#MVAVLooseTightIP2DMini2_sf' , 
                    },
                #'fakeW' : '/LatinoAnalysis/Gardener/python/data/fake_prompt_rates/80X/lowPtCorrected/36fb_ele_cut_WP_Tight80X/' ,
                } ,

            'cutBasedTightIsoTight' : {
                'cuts' : { 
                    'True' :
                        [
                        'electron_col[LF_idx]["pt"]             >  15.' ,
                        'abs(electron_col[LF_idx]["eta"])       <  2.4' ,
                        'electron_col[LF_idx]["cutBased"]       >=  4' ,
                        'abs(electron_col[LF_idx]["sip3d"])     <   4.' ,
                        'abs(electron_col[LF_idx]["dxy"])       < 0.05' ,
                        'abs(electron_col[LF_idx]["dz"])        < 0.10' ,
                        'electron_col[LF_idx]["lostHits"]       ==  0',
                        'abs(electron_col[LF_idx]["miniPFRelIso_all"]) < 0.1',
                        #'abs(electron_col[LF_idx]["eta"]+electron_col[LF_idx]["deltaEtaSC"])<1.4442 or abs(electron_col[LF_idx]["eta"]+electron_col[LF_idx]["deltaEtaSC"])>1.5660' ,
                        ] ,
                    } ,
                'tkSF':  { 
                    '1-7' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2016v2/EGM2D_BtoH_combineLowEt_RecoSF_Legacy2016.root' ,
                    } ,
                'susySF':  {
                    '1-7' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2016v2/ElectronScaleFactors_Run2016_SUSY.root#Run2016_CutBasedTightNoIso94XV2#Run2016_Mini' ,  
                    } ,
                'fsSF': {
                    '1-7' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2016v2/detailed_ele_full_fast_sf_17.root#CutBasedTightNoIso94XV2_sf#MVAVLooseTightIP2DMini_sf' , 
                    },
                #'fakeW' : '/LatinoAnalysis/Gardener/python/data/fake_prompt_rates/80X/lowPtCorrected/36fb_ele_cut_WP_Tight80X/' ,
                } ,

            'cutBasedTightPOG' : {
                'cuts' : { 
                    'True' :
                        [
                        'electron_col[LF_idx]["pt"]             >  15.' ,
                        'abs(electron_col[LF_idx]["eta"])       <  2.4' ,
                        'electron_col[LF_idx]["cutBased"]       >=  4' ,
                        'abs(electron_col[LF_idx]["sip3d"])     <   4.' ,
                        'abs(electron_col[LF_idx]["dxy"])       < 0.05' ,
                        'abs(electron_col[LF_idx]["dz"])        < 0.10' ,
                        'electron_col[LF_idx]["lostHits"]       ==  0',
                        ] ,
                    } ,
                'tkSF':  { 
                    '1-7' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2016v2/EGM2D_BtoH_combineLowEt_RecoSF_Legacy2016.root' ,
                    } ,
                'susySF':  {
                    '1-7' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2016v2/2016LegacyReReco_ElectronTight_Fall17V2.root#EGamma_SF2D' ,  
                    } ,
                'fsSF': {
                    '1-7' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2016v2/detailed_ele_full_fast_sf_17.root#CutBasedTightNoIso94XV2_sf#MVAVLooseTightIP2DMini_sf' , 
                    },
                #'fakeW' : '/LatinoAnalysis/Gardener/python/data/fake_prompt_rates/80X/lowPtCorrected/36fb_ele_cut_WP_Tight80X/' ,
                } ,

            'cutBased_mvaWP80' : {
                'cuts' : { 
                    'True' :
                        [
                        'electron_col[LF_idx]["pt"]             >  15.' ,
                        'abs(electron_col[LF_idx]["eta"])       <  2.4' ,
                        'electron_col[LF_idx]["mvaFall17V2Iso_WP80"]   ==  1' ,
                        'abs(electron_col[LF_idx]["sip3d"])     <   4.' ,
                        'abs(electron_col[LF_idx]["dxy"])       < 0.05' ,
                        'abs(electron_col[LF_idx]["dz"])        < 0.10' ,
                        'electron_col[LF_idx]["lostHits"]       ==  0',
                        #'abs(electron_col[LF_idx]["miniPFRelIso_all"]) < 0.2',
                        #'abs(electron_col[LF_idx]["eta"]+electron_col[LF_idx]["deltaEtaSC"])<1.4442 or abs(electron_col[LF_idx]["eta"]+electron_col[LF_idx]["deltaEtaSC"])>1.5660' ,
                        ] ,
                    } ,
                'tkSF':  { 
                    '1-7' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2016v2/EGM2D_BtoH_combineLowEt_RecoSF_Legacy2016.root' ,
                    } ,
                'susySF':  {
                    '1-7' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2016v2/2016LegacyReReco_ElectronMVA80_Fall17V2.root#EGamma_SF2D' ,  
                    } ,
                'fsSF': {
                    '1-7' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2016v2/detailed_ele_full_fast_sf_17.root#MVATightTightIP2D3D_sf#MVAVLooseTightIP2DMini4_sf' , 
                    },
                #'fakeW' : '/LatinoAnalysis/Gardener/python/data/fake_prompt_rates/80X/lowPtCorrected/36fb_ele_cut_WP_Tight80X/' ,
                } ,

            'cutBased_mvaWP90' : {
                'cuts' : { 
                    'True' :
                        [
                        'electron_col[LF_idx]["pt"]             >  15.' ,
                        'abs(electron_col[LF_idx]["eta"])       <  2.4' ,
                        'electron_col[LF_idx]["mvaFall17V2Iso_WP90"]   ==  1' ,
                        'abs(electron_col[LF_idx]["sip3d"])     <   4.' ,
                        'abs(electron_col[LF_idx]["dxy"])       < 0.05' ,
                        'abs(electron_col[LF_idx]["dz"])        < 0.10' ,
                        'electron_col[LF_idx]["lostHits"]       ==  0',
                        #'abs(electron_col[LF_idx]["miniPFRelIso_all"]) < 0.2',
                        #'abs(electron_col[LF_idx]["eta"]+electron_col[LF_idx]["deltaEtaSC"])<1.4442 or abs(electron_col[LF_idx]["eta"]+electron_col[LF_idx]["deltaEtaSC"])>1.5660' ,
                        ] ,
                    } ,
                'tkSF':  { 
                    '1-7' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2016v2/EGM2D_BtoH_combineLowEt_RecoSF_Legacy2016.root' ,
                    } ,
                'susySF':  {
                    '1-7' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2016v2/2016LegacyReReco_ElectronMVA90_Fall17V2.root#EGamma_SF2D' ,  
                    } ,
                'fsSF': {
                    '1-7' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2016v2/detailed_ele_full_fast_sf_17.root#MVATightTightIP2D3D_sf#MVAVLooseTightIP2DMini4_sf' , 
                    },
                #'fakeW' : '/LatinoAnalysis/Gardener/python/data/fake_prompt_rates/80X/lowPtCorrected/36fb_ele_cut_WP_Tight80X/' ,
                } ,

            },
        
        'WgStarObjWP' : {
            'null' : { 
                'cuts' : { 
                    'True' :
                        [
                        'False' ,
                        ] ,
                    } ,
                } ,
            }, 

        }, 

    'Full2017v6': {
        
        'VetoObjWP' : { 
            'cutBasedVeto' : { 
                'cuts' : { 
                    'True' :
                        [
                        'electron_col[LF_idx]["pt"]             >  15.' ,
                        'abs(electron_col[LF_idx]["eta"])       <  2.4' ,
                        'electron_col[LF_idx]["cutBased"]       >=   1' ,
                        'abs(electron_col[LF_idx]["sip3d"])     <   4.' ,
                        'abs(electron_col[LF_idx]["dxy"])       < 0.05' ,
                        'abs(electron_col[LF_idx]["dz"])        < 0.10' ,
                        #'abs(electron_col[LF_idx]["miniPFRelIso_all"]) < 0.4',     
                        #'abs(electron_col[LF_idx]["eta"]+electron_col[LF_idx]["deltaEtaSC"])<1.4442 or abs(electron_col[LF_idx]["eta"]+electron_col[LF_idx]["deltaEtaSC"])>1.5660' ,
                        ] ,             
                    },
                } ,
            } ,
  
        'FakeObjWP'  : {
            'cutBasedVeto' : { 
                'cuts' : { 
                    'True' :
                        [
                        'electron_col[LF_idx]["pt"]             >  15.' ,
                        'abs(electron_col[LF_idx]["eta"])       <  2.4' ,
                        'electron_col[LF_idx]["cutBased"]       >=   1' ,
                        'abs(electron_col[LF_idx]["sip3d"])     <   4.' ,
                        'abs(electron_col[LF_idx]["dxy"])       < 0.05' ,
                        'abs(electron_col[LF_idx]["dz"])        < 0.10' ,
                        #'abs(electron_col[LF_idx]["miniPFRelIso_all"]) < 0.4',
                        #'abs(electron_col[LF_idx]["eta"]+electron_col[LF_idx]["deltaEtaSC"])<1.4442 or abs(electron_col[LF_idx]["eta"]+electron_col[LF_idx]["deltaEtaSC"])>1.5660' ,
                        ] ,
                    },
                } ,
            } ,
        
        'TightObjWP' : {

            'cutBasedMediumMiniIso' : {
                'cuts' : { 
                    'True' :
                        [
                        'electron_col[LF_idx]["pt"]             >  15.' ,
                        'abs(electron_col[LF_idx]["eta"])       <  2.4' ,
                        'electron_col[LF_idx]["cutBased"]       >=  3' ,
                        'abs(electron_col[LF_idx]["sip3d"])     <   4.' ,
                        'abs(electron_col[LF_idx]["dxy"])       < 0.05' ,
                        'abs(electron_col[LF_idx]["dz"])        < 0.10' ,
                        'electron_col[LF_idx]["lostHits"]       ==  0',
                        'abs(electron_col[LF_idx]["miniPFRelIso_all"]) < 0.1',
                        #'abs(electron_col[LF_idx]["eta"]+electron_col[LF_idx]["deltaEtaSC"])<1.4442 or abs(electron_col[LF_idx]["eta"]+electron_col[LF_idx]["deltaEtaSC"])>1.5660' ,
                        ] ,
                    } ,
                'tkSF':  { 
                    '1-1' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/egammaEffi.txt_EGM2D_runB_passingRECO_combineLowEt.root',
                    '2-2' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/egammaEffi.txt_EGM2D_runC_passingRECO_combineLowEt.root',
                    '3-3' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/egammaEffi.txt_EGM2D_runD_passingRECO_combineLowEt.root',
                    '4-4' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/egammaEffi.txt_EGM2D_runE_passingRECO_combineLowEt.root',
                    '5-5' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/egammaEffi.txt_EGM2D_runF_passingRECO_combineLowEt.root',
                  } ,
                'susySF':  {
                    '1-1' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/ElectronScaleFactors_Run2017_SUSY.root#Run2017_CutBasedMediumNoIso94XV2#Run2017_MVAVLooseTightIP2DMini' , 
                    '2-2' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/ElectronScaleFactors_Run2017_SUSY.root#Run2017_CutBasedMediumNoIso94XV2#Run2017_MVAVLooseTightIP2DMini' , 
                    '3-3' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/ElectronScaleFactors_Run2017_SUSY.root#Run2017_CutBasedMediumNoIso94XV2#Run2017_MVAVLooseTightIP2DMini' , 
                    '4-4' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/ElectronScaleFactors_Run2017_SUSY.root#Run2017_CutBasedMediumNoIso94XV2#Run2017_MVAVLooseTightIP2DMini' , 
                    '5-5' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/ElectronScaleFactors_Run2017_SUSY.root#Run2017_CutBasedMediumNoIso94XV2#Run2017_MVAVLooseTightIP2DMini' ,  
                    } ,
                'fsSF': {
                    '1-5' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/detailed_ele_full_fast_sf_17.root#CutBasedMediumNoIso94XV2_sf#MVAVLooseTightIP2DMini_sf' , 
                    },
                } ,

            'cutBasedMediumPOG' : {
                'cuts' : { 
                    'True' :
                        [
                        'electron_col[LF_idx]["pt"]             >  15.' ,
                        'abs(electron_col[LF_idx]["eta"])       <  2.4' ,
                        'electron_col[LF_idx]["cutBased"]       >=  3' ,
                        'abs(electron_col[LF_idx]["sip3d"])     <   4.' ,
                        'abs(electron_col[LF_idx]["dxy"])       < 0.05' ,
                        'abs(electron_col[LF_idx]["dz"])        < 0.10' ,
                        'electron_col[LF_idx]["lostHits"]       ==  0',
                        ] ,
                    } ,
                'tkSF':  { 
                    '1-1' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/egammaEffi.txt_EGM2D_runB_passingRECO_combineLowEt.root',
                    '2-2' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/egammaEffi.txt_EGM2D_runC_passingRECO_combineLowEt.root',
                    '3-3' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/egammaEffi.txt_EGM2D_runD_passingRECO_combineLowEt.root',
                    '4-4' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/egammaEffi.txt_EGM2D_runE_passingRECO_combineLowEt.root',
                    '5-5' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/egammaEffi.txt_EGM2D_runF_passingRECO_combineLowEt.root',
                  } ,
                'susySF':  {
                    '1-1' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/2017_ElectronMedium_POG.root#EGamma_SF2D' , 
                    '2-2' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/2017_ElectronMedium_POG.root#EGamma_SF2D' , 
                    '3-3' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/2017_ElectronMedium_POG.root#EGamma_SF2D' , 
                    '4-4' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/2017_ElectronMedium_POG.root#EGamma_SF2D' , 
                    '5-5' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/2017_ElectronMedium_POG.root#EGamma_SF2D' , 
                    } ,
                'fsSF': {
                    '1-5' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/detailed_ele_full_fast_sf_17.root#CutBasedMediumNoIso94XV2_sf#MVAVLooseTightIP2DMini_sf' , 
                    },
                } ,

            'cutBasedMediumPOGeta' : {
                'cuts' : { 
                    'True' :
                        [
                        'electron_col[LF_idx]["pt"]             >  15.' ,
                        'abs(electron_col[LF_idx]["eta"])       <  2.4' ,
                        'electron_col[LF_idx]["cutBased"]       >=  3' ,
                        'abs(electron_col[LF_idx]["sip3d"])     <   4.' ,
                        'abs(electron_col[LF_idx]["dxy"])       < 0.05' ,
                        'abs(electron_col[LF_idx]["dz"])        < 0.10' ,
                        'electron_col[LF_idx]["lostHits"]       ==  0',
                        'abs(electron_col[LF_idx]["eta"]+electron_col[LF_idx]["deltaEtaSC"])<1.4442 or abs(electron_col[LF_idx]["eta"]+electron_col[LF_idx]["deltaEtaSC"])>1.5660' ,
                        ] ,
                    } ,
                'tkSF':  { 
                    '1-1' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/egammaEffi.txt_EGM2D_runB_passingRECO_combineLowEt.root',
                    '2-2' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/egammaEffi.txt_EGM2D_runC_passingRECO_combineLowEt.root',
                    '3-3' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/egammaEffi.txt_EGM2D_runD_passingRECO_combineLowEt.root',
                    '4-4' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/egammaEffi.txt_EGM2D_runE_passingRECO_combineLowEt.root',
                    '5-5' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/egammaEffi.txt_EGM2D_runF_passingRECO_combineLowEt.root',
                  } ,
                'susySF':  {
                    '1-1' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/2017_ElectronMedium_POG.root#EGamma_SF2D' , 
                    '2-2' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/2017_ElectronMedium_POG.root#EGamma_SF2D' , 
                    '3-3' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/2017_ElectronMedium_POG.root#EGamma_SF2D' , 
                    '4-4' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/2017_ElectronMedium_POG.root#EGamma_SF2D' , 
                    '5-5' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/2017_ElectronMedium_POG.root#EGamma_SF2D' , 
                    } ,
                'fsSF': {
                    '1-5' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/detailed_ele_full_fast_sf_17.root#CutBasedMediumNoIso94XV2_sf#MVAVLooseTightIP2DMini_sf' , 
                    },
                } ,

            'cutBasedMediumPOGV1' : {
                'cuts' : { 
                    'True' :
                        [
                        'electron_col[LF_idx]["pt"]                 >  15.' ,
                        'abs(electron_col[LF_idx]["eta"])           <  2.4' ,
                        'electron_col[LF_idx]["cutBased_Fall17_V1"] >=  3' ,
                        'abs(electron_col[LF_idx]["sip3d"])         <   4.' ,
                        'abs(electron_col[LF_idx]["dxy"])           < 0.05' ,
                        'abs(electron_col[LF_idx]["dz"])            < 0.10' ,
                        'electron_col[LF_idx]["lostHits"]           ==  0',
                        ] ,
                    } ,
                'tkSF':  { 
                    '1-1' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/egammaEffi.txt_EGM2D_runB_passingRECO_combineLowEt.root',
                    '2-2' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/egammaEffi.txt_EGM2D_runC_passingRECO_combineLowEt.root',
                    '3-3' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/egammaEffi.txt_EGM2D_runD_passingRECO_combineLowEt.root',
                    '4-4' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/egammaEffi.txt_EGM2D_runE_passingRECO_combineLowEt.root',
                    '5-5' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/egammaEffi.txt_EGM2D_runF_passingRECO_combineLowEt.root',
                  } ,
                'susySF':  {
                    '1-1' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/2017_ElectronMedium_POG.root#EGamma_SF2D' , 
                    '2-2' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/2017_ElectronMedium_POG.root#EGamma_SF2D' , 
                    '3-3' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/2017_ElectronMedium_POG.root#EGamma_SF2D' , 
                    '4-4' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/2017_ElectronMedium_POG.root#EGamma_SF2D' , 
                    '5-5' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/2017_ElectronMedium_POG.root#EGamma_SF2D' , 
                    } ,
                'fsSF': {
                    '1-5' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/detailed_ele_full_fast_sf_17.root#CutBasedMediumNoIso94XV2_sf#MVAVLooseTightIP2DMini_sf' , 
                    },
                } ,

            'cutBasedTightMiniIso' : {
                'cuts' : { 
                    'True' :
                        [
                        'electron_col[LF_idx]["pt"]             >  15.' ,
                        'abs(electron_col[LF_idx]["eta"])       <  2.4' ,
                        'electron_col[LF_idx]["cutBased"]       >=  4' ,
                        'abs(electron_col[LF_idx]["sip3d"])     <   4.' ,
                        'abs(electron_col[LF_idx]["dxy"])       < 0.05' ,
                        'abs(electron_col[LF_idx]["dz"])        < 0.10' ,
                        'electron_col[LF_idx]["lostHits"]       ==  0',
                        'abs(electron_col[LF_idx]["miniPFRelIso_all"]) < 0.2',
                        #'abs(electron_col[LF_idx]["eta"]+electron_col[LF_idx]["deltaEtaSC"])<1.4442 or abs(electron_col[LF_idx]["eta"]+electron_col[LF_idx]["deltaEtaSC"])>1.5660' ,
                        ] ,
                    } ,
                'tkSF':  { 
                    '1-1' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/egammaEffi.txt_EGM2D_runB_passingRECO_combineLowEt.root',
                    '2-2' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/egammaEffi.txt_EGM2D_runC_passingRECO_combineLowEt.root',
                    '3-3' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/egammaEffi.txt_EGM2D_runD_passingRECO_combineLowEt.root',
                    '4-4' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/egammaEffi.txt_EGM2D_runE_passingRECO_combineLowEt.root',
                    '5-5' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/egammaEffi.txt_EGM2D_runF_passingRECO_combineLowEt.root',
                  } ,
                'susySF':  {
                    '1-1' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/ElectronScaleFactors_Run2017_SUSY.root#Run2017_CutBasedTightNoIso94XV2#Run2017_MVAVLooseTightIP2DMini2' ,  
                    '2-2' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/ElectronScaleFactors_Run2017_SUSY.root#Run2017_CutBasedTightNoIso94XV2#Run2017_MVAVLooseTightIP2DMini2' ,  
                    '3-3' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/ElectronScaleFactors_Run2017_SUSY.root#Run2017_CutBasedTightNoIso94XV2#Run2017_MVAVLooseTightIP2DMini2' ,  
                    '4-4' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/ElectronScaleFactors_Run2017_SUSY.root#Run2017_CutBasedTightNoIso94XV2#Run2017_MVAVLooseTightIP2DMini2' ,  
                    '5-5' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/ElectronScaleFactors_Run2017_SUSY.root#Run2017_CutBasedTightNoIso94XV2#Run2017_MVAVLooseTightIP2DMini2' ,  
                    } ,
                'fsSF': {
                    '1-5' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/detailed_ele_full_fast_sf_17.root#CutBasedTightNoIso94XV2_sf#MVAVLooseTightIP2DMini2_sf' , 
                    },
                } ,

            'cutBasedTightIsoTight' : {
                'cuts' : { 
                    'True' :
                        [
                        'electron_col[LF_idx]["pt"]             >  15.' ,
                        'abs(electron_col[LF_idx]["eta"])       <  2.4' ,
                        'electron_col[LF_idx]["cutBased"]       >=  4' ,
                        'abs(electron_col[LF_idx]["sip3d"])     <   4.' ,
                        'abs(electron_col[LF_idx]["dxy"])       < 0.05' ,
                        'abs(electron_col[LF_idx]["dz"])        < 0.10' ,
                        'electron_col[LF_idx]["lostHits"]       ==  0',
                        'abs(electron_col[LF_idx]["miniPFRelIso_all"]) < 0.1',
                        #'abs(electron_col[LF_idx]["eta"]+electron_col[LF_idx]["deltaEtaSC"])<1.4442 or abs(electron_col[LF_idx]["eta"]+electron_col[LF_idx]["deltaEtaSC"])>1.5660' ,
                        ] ,
                    } ,
                'tkSF':  { 
                    '1-1' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/egammaEffi.txt_EGM2D_runB_passingRECO_combineLowEt.root',
                    '2-2' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/egammaEffi.txt_EGM2D_runC_passingRECO_combineLowEt.root',
                    '3-3' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/egammaEffi.txt_EGM2D_runD_passingRECO_combineLowEt.root',
                    '4-4' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/egammaEffi.txt_EGM2D_runE_passingRECO_combineLowEt.root',
                    '5-5' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/egammaEffi.txt_EGM2D_runF_passingRECO_combineLowEt.root',
                  } ,
                'susySF':  {
                    '1-1' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/ElectronScaleFactors_Run2017_SUSY.root#Run2017_CutBasedTightNoIso94XV2#Run2017_MVAVLooseTightIP2DMini' ,  
                    '2-2' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/ElectronScaleFactors_Run2017_SUSY.root#Run2017_CutBasedTightNoIso94XV2#Run2017_MVAVLooseTightIP2DMini' ,  
                    '3-3' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/ElectronScaleFactors_Run2017_SUSY.root#Run2017_CutBasedTightNoIso94XV2#Run2017_MVAVLooseTightIP2DMini' ,  
                    '4-4' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/ElectronScaleFactors_Run2017_SUSY.root#Run2017_CutBasedTightNoIso94XV2#Run2017_MVAVLooseTightIP2DMini' ,  
                    '5-5' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/ElectronScaleFactors_Run2017_SUSY.root#Run2017_CutBasedTightNoIso94XV2#Run2017_MVAVLooseTightIP2DMini' ,  
                    } ,
                'fsSF': {
                    '1-5' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/detailed_ele_full_fast_sf_17.root#CutBasedTightNoIso94XV2_sf#MVAVLooseTightIP2DMini_sf' , 
                    },
                } ,

            'cutBasedTightPOG' : {
                'cuts' : { 
                    'True' :
                        [
                        'electron_col[LF_idx]["pt"]             >  15.' ,
                        'abs(electron_col[LF_idx]["eta"])       <  2.4' ,
                        'electron_col[LF_idx]["cutBased"]       >=  4' ,
                        'abs(electron_col[LF_idx]["sip3d"])     <   4.' ,
                        'abs(electron_col[LF_idx]["dxy"])       < 0.05' ,
                        'abs(electron_col[LF_idx]["dz"])        < 0.10' ,
                        'electron_col[LF_idx]["lostHits"]       ==  0',
                        ] ,
                    } ,
                'tkSF':  { 
                    '1-1' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/egammaEffi.txt_EGM2D_runB_passingRECO_combineLowEt.root',
                    '2-2' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/egammaEffi.txt_EGM2D_runC_passingRECO_combineLowEt.root',
                    '3-3' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/egammaEffi.txt_EGM2D_runD_passingRECO_combineLowEt.root',
                    '4-4' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/egammaEffi.txt_EGM2D_runE_passingRECO_combineLowEt.root',
                    '5-5' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/egammaEffi.txt_EGM2D_runF_passingRECO_combineLowEt.root',
                  } ,
                'susySF':  {
                    '1-1' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/2017_ElectronTight_POG.root#EGamma_SF2D' , 
                    '2-2' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/2017_ElectronTight_POG.root#EGamma_SF2D' , 
                    '3-3' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/2017_ElectronTight_POG.root#EGamma_SF2D' , 
                    '4-4' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/2017_ElectronTight_POG.root#EGamma_SF2D' , 
                    '5-5' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/2017_ElectronTight_POG.root#EGamma_SF2D' , 
                    } ,
                'fsSF': {
                    '1-5' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/detailed_ele_full_fast_sf_17.root#CutBasedTightNoIso94XV2_sf#MVAVLooseTightIP2DMini_sf' , 
                    },
                } ,

            'cutBased_mvaWP80' : {
                'cuts' : { 
                    'True' :
                        [
                        'electron_col[LF_idx]["pt"]             >  15.' ,
                        'abs(electron_col[LF_idx]["eta"])       <  2.4' ,
                        'electron_col[LF_idx]["mvaFall17V2Iso_WP80"]   ==  1' ,
                        'abs(electron_col[LF_idx]["sip3d"])     <   4.' ,
                        'abs(electron_col[LF_idx]["dxy"])       < 0.05' ,
                        'abs(electron_col[LF_idx]["dz"])        < 0.10' ,
                        'electron_col[LF_idx]["lostHits"]       ==  0',
                        #'abs(electron_col[LF_idx]["miniPFRelIso_all"]) < 0.2',
                        #'abs(electron_col[LF_idx]["eta"]+electron_col[LF_idx]["deltaEtaSC"])<1.4442 or abs(electron_col[LF_idx]["eta"]+electron_col[LF_idx]["deltaEtaSC"])>1.5660' ,
                        ] ,
                    } ,
                'tkSF':  { 
                    '1-1' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/egammaEffi.txt_EGM2D_runB_passingRECO_combineLowEt.root',
                    '2-2' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/egammaEffi.txt_EGM2D_runC_passingRECO_combineLowEt.root',
                    '3-3' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/egammaEffi.txt_EGM2D_runD_passingRECO_combineLowEt.root',
                    '4-4' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/egammaEffi.txt_EGM2D_runE_passingRECO_combineLowEt.root',
                    '5-5' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/egammaEffi.txt_EGM2D_runF_passingRECO_combineLowEt.root',
                    } ,
                'susySF':  {
                    '1-1' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/2017_ElectronMVA80_POG.root#EGamma_SF2D' ,
                    '2-2' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/2017_ElectronMVA80_POG.root#EGamma_SF2D' ,
                    '3-3' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/2017_ElectronMVA80_POG.root#EGamma_SF2D' ,
                    '4-4' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/2017_ElectronMVA80_POG.root#EGamma_SF2D' ,
                    '5-5' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/2017_ElectronMVA80_POG.root#EGamma_SF2D' ,  
                    } ,
                'fsSF': {
                    '1-5' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/detailed_ele_full_fast_sf_17.root#MVATightTightIP2D3D_sf#MVAVLooseTightIP2DMini4_sf' , 
                    },
                } ,

            'cutBased_mvaWP90' : {
                'cuts' : { 
                    'True' :
                        [
                        'electron_col[LF_idx]["pt"]             >  15.' ,
                        'abs(electron_col[LF_idx]["eta"])       <  2.4' ,
                        'electron_col[LF_idx]["mvaFall17V2Iso_WP90"]   ==  1' ,
                        'abs(electron_col[LF_idx]["sip3d"])     <   4.' ,
                        'abs(electron_col[LF_idx]["dxy"])       < 0.05' ,
                        'abs(electron_col[LF_idx]["dz"])        < 0.10' ,
                        'electron_col[LF_idx]["lostHits"]       ==  0',
                        #'abs(electron_col[LF_idx]["miniPFRelIso_all"]) < 0.2',
                        #'abs(electron_col[LF_idx]["eta"]+electron_col[LF_idx]["deltaEtaSC"])<1.4442 or abs(electron_col[LF_idx]["eta"]+electron_col[LF_idx]["deltaEtaSC"])>1.5660' ,
                        ] ,
                    } ,
                'tkSF':  { 
                    '1-1' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/egammaEffi.txt_EGM2D_runB_passingRECO_combineLowEt.root',
                    '2-2' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/egammaEffi.txt_EGM2D_runC_passingRECO_combineLowEt.root',
                    '3-3' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/egammaEffi.txt_EGM2D_runD_passingRECO_combineLowEt.root',
                    '4-4' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/egammaEffi.txt_EGM2D_runE_passingRECO_combineLowEt.root',
                    '5-5' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/egammaEffi.txt_EGM2D_runF_passingRECO_combineLowEt.root',
                    } ,
                'susySF':  {
                    '1-1' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/2017_ElectronMVA90_POG.root#EGamma_SF2D' ,
                    '2-2' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/2017_ElectronMVA90_POG.root#EGamma_SF2D' ,
                    '3-3' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/2017_ElectronMVA90_POG.root#EGamma_SF2D' ,
                    '4-4' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/2017_ElectronMVA90_POG.root#EGamma_SF2D' ,
                    '5-5' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/2017_ElectronMVA90_POG.root#EGamma_SF2D' ,  
                    } ,
                'fsSF': {
                    '1-5' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/detailed_ele_full_fast_sf_17.root#MVATightTightIP2D3D_sf#MVAVLooseTightIP2DMini4_sf' , 
                    },
                } ,

            },
        
        'WgStarObjWP' : {
            'null' : { 
                'cuts' : { 
                    'True' :
                        [
                        'False' ,
                        ] ,
                    } ,
                } ,
            }, 

        }, 

    'Full2018v6': {
        
        'VetoObjWP' : { 
            'cutBasedVeto' : { 
                'cuts' : { 
                    'True' :
                        [
                        'electron_col[LF_idx]["pt"]             >  15.' ,
                        'abs(electron_col[LF_idx]["eta"])       <  2.4' ,
                        'electron_col[LF_idx]["cutBased"]       >=   1' ,
                        'abs(electron_col[LF_idx]["sip3d"])     <   4.' ,
                        'abs(electron_col[LF_idx]["dxy"])       < 0.05' ,
                        'abs(electron_col[LF_idx]["dz"])        < 0.10' ,
                        #'abs(electron_col[LF_idx]["miniPFRelIso_all"]) < 0.4',     
                        #'abs(electron_col[LF_idx]["eta"]+electron_col[LF_idx]["deltaEtaSC"])<1.4442 or abs(electron_col[LF_idx]["eta"]+electron_col[LF_idx]["deltaEtaSC"])>1.5660' ,
                        ] ,             
                    },
                } ,
            } ,
  
        'FakeObjWP'  : {
            'cutBasedVeto' : { 
                'cuts' : { 
                    'True' :
                        [
                        'electron_col[LF_idx]["pt"]             >  15.' ,
                        'abs(electron_col[LF_idx]["eta"])       <  2.4' ,
                        'electron_col[LF_idx]["cutBased"]       >=   1' ,
                        'abs(electron_col[LF_idx]["sip3d"])     <   4.' ,
                        'abs(electron_col[LF_idx]["dxy"])       < 0.05' ,
                        'abs(electron_col[LF_idx]["dz"])        < 0.10' ,
                        #'abs(electron_col[LF_idx]["miniPFRelIso_all"]) < 0.4',
                        #'abs(electron_col[LF_idx]["eta"]+electron_col[LF_idx]["deltaEtaSC"])<1.4442 or abs(electron_col[LF_idx]["eta"]+electron_col[LF_idx]["deltaEtaSC"])>1.5660' ,
                        ] ,
                    },
                } ,
            } ,
        
        'TightObjWP' : {

            'cutBasedMediumMiniIso' : {
                'cuts' : { 
                    'True' :
                        [
                        'electron_col[LF_idx]["pt"]             >  15.' ,
                        'abs(electron_col[LF_idx]["eta"])       <  2.4' ,
                        'electron_col[LF_idx]["cutBased"]       >=  3' ,
                        'abs(electron_col[LF_idx]["sip3d"])     <   4.' ,
                        'abs(electron_col[LF_idx]["dxy"])       < 0.05' ,
                        'abs(electron_col[LF_idx]["dz"])        < 0.10' ,
                        'electron_col[LF_idx]["lostHits"]       ==  0',
                        'abs(electron_col[LF_idx]["miniPFRelIso_all"]) < 0.1',
                        #'abs(electron_col[LF_idx]["eta"]+electron_col[LF_idx]["deltaEtaSC"])<1.4442 or abs(electron_col[LF_idx]["eta"]+electron_col[LF_idx]["deltaEtaSC"])>1.5660' ,
                        ] ,
                    } ,
                'tkSF':  { 
                    '1-1' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2018/egammaEffi.txt_EGM2D_updatedAll.root',
                    } ,
                'susySF':  {
                    '1-1' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2018/ElectronScaleFactors_Run2018_SUSY.root#Run2018_CutBasedMediumNoIso94XV2#Run2018_Mini' ,  
                    } ,
                'fsSF': {
                    '1-1' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2018/detailed_ele_full_fast_sf_18.root#CutBasedMediumNoIso94XV2_sf#MVAVLooseTightIP2DMini_sf' , 
                    },
                } ,

            'cutBasedMediumPOG' : {
                'cuts' : { 
                    'True' :
                        [
                        'electron_col[LF_idx]["pt"]             >  15.' ,
                        'abs(electron_col[LF_idx]["eta"])       <  2.4' ,
                        'electron_col[LF_idx]["cutBased"]       >=  3' ,
                        'abs(electron_col[LF_idx]["sip3d"])     <   4.' ,
                        'abs(electron_col[LF_idx]["dxy"])       < 0.05' ,
                        'abs(electron_col[LF_idx]["dz"])        < 0.10' ,
                        'electron_col[LF_idx]["lostHits"]       ==  0',
                        ] ,
                    } ,
                'tkSF':  { 
                    '1-1' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2018/egammaEffi.txt_EGM2D_updatedAll.root',
                    } ,
                'susySF':  {
                    '1-1' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2018/2018_ElectronMedium_POG.root#EGamma_SF2D' ,  
                    } ,
                'fsSF': {
                    '1-1' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2018/detailed_ele_full_fast_sf_18.root#CutBasedMediumNoIso94XV2_sf#MVAVLooseTightIP2DMini_sf' , 
                    },
                } ,

            'cutBasedMediumPOGeta' : {
                'cuts' : { 
                    'True' :
                        [
                        'electron_col[LF_idx]["pt"]             >  15.' ,
                        'abs(electron_col[LF_idx]["eta"])       <  2.4' ,
                        'electron_col[LF_idx]["cutBased"]       >=  3' ,
                        'abs(electron_col[LF_idx]["sip3d"])     <   4.' ,
                        'abs(electron_col[LF_idx]["dxy"])       < 0.05' ,
                        'abs(electron_col[LF_idx]["dz"])        < 0.10' ,
                        'electron_col[LF_idx]["lostHits"]       ==  0',
                        'abs(electron_col[LF_idx]["eta"]+electron_col[LF_idx]["deltaEtaSC"])<1.4442 or abs(electron_col[LF_idx]["eta"]+electron_col[LF_idx]["deltaEtaSC"])>1.5660' ,
                        ] ,
                    } ,
                'tkSF':  { 
                    '1-1' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2018/egammaEffi.txt_EGM2D_updatedAll.root',
                    } ,
                'susySF':  {
                    '1-1' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2018/2018_ElectronMedium_POG.root#EGamma_SF2D' ,  
                    } ,
                'fsSF': {
                    '1-1' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2018/detailed_ele_full_fast_sf_18.root#CutBasedMediumNoIso94XV2_sf#MVAVLooseTightIP2DMini_sf' , 
                    },
                } ,

            'cutBasedMediumPOGV1' : {

                'cuts' : { 
                    'True' :
                        [
                        'electron_col[LF_idx]["pt"]             >  15.' ,
                        'abs(electron_col[LF_idx]["eta"])       <  2.4' ,
                        'electron_col[LF_idx]["cutBased_Fall17_V1"]   >=  3' ,
                        'abs(electron_col[LF_idx]["sip3d"])     <   4.' ,
                        'abs(electron_col[LF_idx]["dxy"])       < 0.05' ,
                        'abs(electron_col[LF_idx]["dz"])        < 0.10' ,
                        'electron_col[LF_idx]["lostHits"]       ==  0',
                        ] ,
                    } ,
                'tkSF':  { 
                    '1-1' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2018/egammaEffi.txt_EGM2D_updatedAll.root',
                    } ,
                'susySF':  {
                    '1-1' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2018/2018_ElectronMedium_POG.root#EGamma_SF2D' ,  
                    } ,
                'fsSF': {
                    '1-1' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2018/detailed_ele_full_fast_sf_18.root#CutBasedMediumNoIso94XV2_sf#MVAVLooseTightIP2DMini_sf' , 
                    },
                } ,

            'cutBasedTightMiniIso' : {
                'cuts' : { 
                    'True' :
                        [
                        'electron_col[LF_idx]["pt"]             >  15.' ,
                        'abs(electron_col[LF_idx]["eta"])       <  2.4' ,
                        'electron_col[LF_idx]["cutBased"]       >=  4' ,
                        'abs(electron_col[LF_idx]["sip3d"])     <   4.' ,
                        'abs(electron_col[LF_idx]["dxy"])       < 0.05' ,
                        'abs(electron_col[LF_idx]["dz"])        < 0.10' ,
                        'electron_col[LF_idx]["lostHits"]       ==  0',
                        'abs(electron_col[LF_idx]["miniPFRelIso_all"]) < 0.2',
                        #'abs(electron_col[LF_idx]["eta"]+electron_col[LF_idx]["deltaEtaSC"])<1.4442 or abs(electron_col[LF_idx]["eta"]+electron_col[LF_idx]["deltaEtaSC"])>1.5660' ,
                        ] ,
                    } ,
                'tkSF':  { 
                    '1-1' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2018/egammaEffi.txt_EGM2D_updatedAll.root',
                    } ,
                'susySF':  {
                    '1-1' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2018/ElectronScaleFactors_Run2018_SUSY.root#Run2018_CutBasedTightNoIso94XV2#Run2018_Mini2' ,  
                    } ,
                'fsSF': {
                    '1-1' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2018/detailed_ele_full_fast_sf_18.root#CutBasedTightNoIso94XV2_sf#MVAVLooseTightIP2DMini2_sf' , 
                    },
                } ,

            'cutBasedTightIsoTight' : {
                'cuts' : { 
                    'True' :
                        [
                        'electron_col[LF_idx]["pt"]             >  15.' ,
                        'abs(electron_col[LF_idx]["eta"])       <  2.4' ,
                        'electron_col[LF_idx]["cutBased"]       >=  4' ,
                        'abs(electron_col[LF_idx]["sip3d"])     <   4.' ,
                        'abs(electron_col[LF_idx]["dxy"])       < 0.05' ,
                        'abs(electron_col[LF_idx]["dz"])        < 0.10' ,
                        'electron_col[LF_idx]["lostHits"]       ==  0',
                        'abs(electron_col[LF_idx]["miniPFRelIso_all"]) < 0.1',
                        #'abs(electron_col[LF_idx]["eta"]+electron_col[LF_idx]["deltaEtaSC"])<1.4442 or abs(electron_col[LF_idx]["eta"]+electron_col[LF_idx]["deltaEtaSC"])>1.5660' ,
                        ] ,
                    } ,
                'tkSF':  { 
                    '1-1' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2018/egammaEffi.txt_EGM2D_updatedAll.root',
                    } ,
                'susySF':  {
                    '1-1' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2018/ElectronScaleFactors_Run2018_SUSY.root#Run2018_CutBasedTightNoIso94XV2#Run2018_Mini' ,  
                    } ,
                'fsSF': {
                    '1-1' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2018/detailed_ele_full_fast_sf_18.root#CutBasedTightNoIso94XV2_sf#MVAVLooseTightIP2DMini_sf' , 
                    },
                } ,

            'cutBasedTightPOG' : {
                'cuts' : { 
                    'True' :
                        [
                        'electron_col[LF_idx]["pt"]             >  15.' ,
                        'abs(electron_col[LF_idx]["eta"])       <  2.4' ,
                        'electron_col[LF_idx]["cutBased"]       >=  4' ,
                        'abs(electron_col[LF_idx]["sip3d"])     <   4.' ,
                        'abs(electron_col[LF_idx]["dxy"])       < 0.05' ,
                        'abs(electron_col[LF_idx]["dz"])        < 0.10' ,
                        'electron_col[LF_idx]["lostHits"]       ==  0',
                        ] ,
                    } ,
                'tkSF':  { 
                    '1-1' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2018/egammaEffi.txt_EGM2D_updatedAll.root',
                    } ,
                'susySF':  {
                    '1-1' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2018/2018_ElectronTight_POG.root#EGamma_SF2D' ,  
                    } ,
                'fsSF': {
                    '1-1' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2018/detailed_ele_full_fast_sf_18.root#CutBasedTightNoIso94XV2_sf#MVAVLooseTightIP2DMini_sf' , 
                    },
                } ,

            'cutBased_mvaWP80' : {
                'cuts' : { 
                    'True' :
                        [
                        'electron_col[LF_idx]["pt"]             >  15.' ,
                        'abs(electron_col[LF_idx]["eta"])       <  2.4' ,
                        'electron_col[LF_idx]["mvaFall17V2Iso_WP80"]   ==  1' ,
                        'abs(electron_col[LF_idx]["sip3d"])     <   4.' ,
                        'abs(electron_col[LF_idx]["dxy"])       < 0.05' ,
                        'abs(electron_col[LF_idx]["dz"])        < 0.10' ,
                        'electron_col[LF_idx]["lostHits"]       ==  0',
                        #'abs(electron_col[LF_idx]["miniPFRelIso_all"]) < 0.2',
                        #'abs(electron_col[LF_idx]["eta"]+electron_col[LF_idx]["deltaEtaSC"])<1.4442 or abs(electron_col[LF_idx]["eta"]+electron_col[LF_idx]["deltaEtaSC"])>1.5660' ,
                        ] ,
                    } ,
                'tkSF':  { 
                    '1-1' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2018/egammaEffi.txt_EGM2D_updatedAll.root',
                    } ,
                'susySF':  {
                    '1-1' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2018/2018_ElectronMVA80_POG.root#EGamma_SF2D' ,  
                    } ,
                'fsSF': {
                    '1-1' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2018/detailed_ele_full_fast_sf_18.root#MVATightTightIP2D3D_sf#MVAVLooseTightIP2DMini4_sf' , 
                    },
                } ,

            'cutBased_mvaWP90' : {
                'cuts' : { 
                    'True' :
                        [
                        'electron_col[LF_idx]["pt"]             >  15.' ,
                        'abs(electron_col[LF_idx]["eta"])       <  2.4' ,
                        'electron_col[LF_idx]["mvaFall17V2Iso_WP90"]   ==  1' ,
                        'abs(electron_col[LF_idx]["sip3d"])     <   4.' ,
                        'abs(electron_col[LF_idx]["dxy"])       < 0.05' ,
                        'abs(electron_col[LF_idx]["dz"])        < 0.10' ,
                        'electron_col[LF_idx]["lostHits"]       ==  0',
                        #'abs(electron_col[LF_idx]["miniPFRelIso_all"]) < 0.2',
                        #'abs(electron_col[LF_idx]["eta"]+electron_col[LF_idx]["deltaEtaSC"])<1.4442 or abs(electron_col[LF_idx]["eta"]+electron_col[LF_idx]["deltaEtaSC"])>1.5660' ,
                        ] ,
                    } ,
                'tkSF':  { 
                    '1-1' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2018/egammaEffi.txt_EGM2D_updatedAll.root',
                    } ,
                'susySF':  {
                    '1-1' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2018/2018_ElectronMVA90_POG.root#EGamma_SF2D' ,  
                    } ,
                'fsSF': {
                    '1-1' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2018/detailed_ele_full_fast_sf_18.root#MVATightTightIP2D3D_sf#MVAVLooseTightIP2DMini4_sf' , 
                    },
                } ,

            },
        
        'WgStarObjWP' : {
            'null' : { 
                'cuts' : { 
                    'True' :
                        [
                        'False' ,
                        ] ,
                    } ,
                } ,
            }, 

        },

    'Full2016v7': {
        
        'VetoObjWP' : { 
            'baseele' : { 
                'cuts' : { 
                    'True' :
                        [
                        'electron_col[LF_idx]["pt"]             >  10.' ,
                        'abs(electron_col[LF_idx]["eta"])       <  2.4' ,
                        'abs(electron_col[LF_idx]["sip3d"])     <   4.' ,
                        'abs(electron_col[LF_idx]["dxy"])       < 0.05' ,
                        'abs(electron_col[LF_idx]["dz"])        < 0.10' ,
                        'electron_col[LF_idx]["convVeto"] ==  1',
                        ] ,             
                    },
                } ,
            } ,
  
        'FakeObjWP'  : { 
            'baseele' : { 
                'cuts' : { 
                    'True' :
                        [
                        'electron_col[LF_idx]["pt"]             >  10.' ,
                        'abs(electron_col[LF_idx]["eta"])       <  2.4' ,
                        'abs(electron_col[LF_idx]["sip3d"])     <   4.' ,
                        'abs(electron_col[LF_idx]["dxy"])       < 0.05' ,
                        'abs(electron_col[LF_idx]["dz"])        < 0.10' ,
                        'electron_col[LF_idx]["convVeto"] ==  1',
                        ] ,             
                    },
                } ,
            } ,
        
        'TightObjWP' : {

            'cutBasedVeto' : { 
                'cuts' : { 
                    'True' :
                        [
                        'electron_col[LF_idx]["pt"]             >  10.' ,
                        'abs(electron_col[LF_idx]["eta"])       <  2.4' ,
                        'electron_col[LF_idx]["cutBased"]       >=   1' ,
                        'abs(electron_col[LF_idx]["sip3d"])     <   4.' ,
                        'abs(electron_col[LF_idx]["dxy"])       < 0.05' ,
                        'abs(electron_col[LF_idx]["dz"])        < 0.10' ,
                        ] ,
                    },
                'tkSF':  { 
                    '1-7' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2016v2/EGM2D_BtoH_combineLowEt_RecoSF_Legacy2016.root' ,
                    } ,
                'susySF':  {
                    '1-7' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2016v2/2016_ElectronWPVeto_Fall17V2.root#EGamma_SF2D' ,  
                    } ,
                'fsSF': {
                    #'1-7' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2016v2/detailed_ele_full_fast_sf_17.root#CutBasedVetoNoIso94XV2_sf' , 
                    '1-7' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2016v2/detailed_ele_full_fast_sf_17.root#MVAVLooseTightIP2DMini4_sf' , 
                    },
                } ,

            'cutBasedMedium' : {
                'cuts' : { 
                    'True' :
                        [
                        'electron_col[LF_idx]["pt"]             >  15.' ,
                        'abs(electron_col[LF_idx]["eta"])       <  2.4' ,
                        'electron_col[LF_idx]["cutBased"]       >=  3' ,
                        'abs(electron_col[LF_idx]["sip3d"])     <   4.' ,
                        'abs(electron_col[LF_idx]["dxy"])       < 0.05' ,
                        'abs(electron_col[LF_idx]["dz"])        < 0.10' ,
                        'electron_col[LF_idx]["lostHits"]       ==  0',
                        ] ,
                    } ,
                'tkSF':  { 
                    '1-7' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2016v2/EGM2D_BtoH_combineLowEt_RecoSF_Legacy2016.root' ,
                    } ,
                'susySF':  {
                    '1-7' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2016v2/2016LegacyReReco_ElectronMedium_Fall17V2.root#EGamma_SF2D' ,  
                    } ,
                'fsSF': {
                    '1-7' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2016v2/detailed_ele_full_fast_sf_17.root#CutBasedMediumNoIso94XV2_sf' , 
                    #'1-7' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2016v2/detailed_ele_full_fast_sf_17.root#MVAVLooseTightIP2DMini2_sf' , 
                    },
                } ,

            'cutBasedTight' : {
                'cuts' : { 
                    'True' :
                        [
                        'electron_col[LF_idx]["pt"]             >  15.' ,
                        'abs(electron_col[LF_idx]["eta"])       <  2.4' ,
                        'electron_col[LF_idx]["cutBased"]       >=  4' ,
                        'abs(electron_col[LF_idx]["sip3d"])     <   4.' ,
                        'abs(electron_col[LF_idx]["dxy"])       < 0.05' ,
                        'abs(electron_col[LF_idx]["dz"])        < 0.10' ,
                        'electron_col[LF_idx]["lostHits"]       ==  0',
                        ] ,
                    } ,
                'tkSF':  { 
                    '1-7' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2016v2/EGM2D_BtoH_combineLowEt_RecoSF_Legacy2016.root' ,
                    } ,
                'susySF':  {
                    '1-7' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2016v2/2016LegacyReReco_ElectronTight_Fall17V2.root#EGamma_SF2D' ,  
                    } ,
                'fsSF': {
                    '1-7' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2016v2/detailed_ele_full_fast_sf_17.root#CutBasedTightNoIso94XV2_sf' , 
                    #'1-7' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2016v2/detailed_ele_full_fast_sf_17.root#MVAVLooseTightIP2DMini_sf' , 
                    },
                } ,

            'SusyMVAVLoose' : {
                'cuts' : { 
                    'True' :
                        [
                        'electron_col[LF_idx]["pt"]             >  10.' ,
                        'abs(electron_col[LF_idx]["eta"])       <  2.4' ,
                        'abs(electron_col[LF_idx]["sip3d"])     <   4.' ,
                        'abs(electron_col[LF_idx]["dxy"])       < 0.05' ,
                        'abs(electron_col[LF_idx]["dz"])        < 0.10' ,
                        'electron_col[LF_idx]["convVeto"] ==  1',
                        'electron_col[LF_idx]["miniPFRelIso_all"]<0.4', 
                        ] ,
                    'electron_col[LF_idx]["pt"]<25.  and abs(electron_col[LF_idx]["eta"])<0.8' : [ 'electron_col[LF_idx]["mvaFall17V2noIso"] > 0.887 + 0.088*(electron_col[LF_idx]["pt"] - 25)' ] ,
                    'electron_col[LF_idx]["pt"]<25.  and abs(electron_col[LF_idx]["eta"])>=0.8   and abs(electron_col[LF_idx]["eta"])<1.479' : [ 'electron_col[LF_idx]["mvaFall17V2noIso"] > 0.112 + 0.099*(electron_col[LF_idx]["pt"] - 25)' ] ,
                    'electron_col[LF_idx]["pt"]<25.  and abs(electron_col[LF_idx]["eta"])>=1.479 and abs(electron_col[LF_idx]["eta"])<2.5'   : [ 'electron_col[LF_idx]["mvaFall17V2noIso"] > -0.017 + 0.137*(electron_col[LF_idx]["pt"] - 25)' ] ,
                    'electron_col[LF_idx]["pt"]>=25. and abs(electron_col[LF_idx]["eta"])<0.8' : [ 'electron_col[LF_idx]["mvaFall17V2noIso"] > 0.887' ] ,
                    'electron_col[LF_idx]["pt"]>=25. and abs(electron_col[LF_idx]["eta"])>=0.8   and abs(electron_col[LF_idx]["eta"])<1.479' : [ 'electron_col[LF_idx]["mvaFall17V2noIso"] > 0.112' ] ,
                    'electron_col[LF_idx]["pt"]>=25. and abs(electron_col[LF_idx]["eta"])>=1.479 and abs(electron_col[LF_idx]["eta"])<2.5'   : [ 'electron_col[LF_idx]["mvaFall17V2noIso"] > -0.017' ] ,
                    } ,
                'tkSF':  { 
                    '1-7' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2016v2/EGM2D_BtoH_combineLowEt_RecoSF_Legacy2016.root' ,
                    } ,
                'susySF':  {
                    '1-7' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2016v2/ElectronScaleFactors_Run2016_SUSY.root#Run2016_MVAVLooseIP2D#Run2016_Mini4' ,  
                    } ,
                'fsSF': {
                    '1-7' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2016v2/detailed_ele_full_fast_sf_17.root#MVAVLooseTightIP2DMini4_sf' , 
                    },
                } ,

            'SusyMVATight' : {
                'cuts' : { 
                    'True' :
                        [
                        'electron_col[LF_idx]["pt"]             >  15.' ,
                        'abs(electron_col[LF_idx]["eta"])       <  2.4' ,
                        'abs(electron_col[LF_idx]["sip3d"])     <   4.' ,
                        'abs(electron_col[LF_idx]["dxy"])       < 0.05' ,
                        'abs(electron_col[LF_idx]["dz"])        < 0.10' ,
                        'electron_col[LF_idx]["convVeto"] ==  1',
                        'electron_col[LF_idx]["lostHits"]       ==  0',
                        'electron_col[LF_idx]["miniPFRelIso_all"]<0.2', 
                        ] ,
                    'electron_col[LF_idx]["pt"]<40.  and abs(electron_col[LF_idx]["eta"])<0.8' : [ 'electron_col[LF_idx]["mvaFall17V2noIso"] > 3.447 + 0.063*(electron_col[LF_idx]["pt"] - 25)' ] ,
                    'electron_col[LF_idx]["pt"]<40.  and abs(electron_col[LF_idx]["eta"])>=0.8   and abs(electron_col[LF_idx]["eta"])<1.479' : [ 'electron_col[LF_idx]["mvaFall17V2noIso"] > 2.522 + 0.058*(electron_col[LF_idx]["pt"] - 25)' ] ,
                    'electron_col[LF_idx]["pt"]<40.  and abs(electron_col[LF_idx]["eta"])>=1.479 and abs(electron_col[LF_idx]["eta"])<2.5'   : [ 'electron_col[LF_idx]["mvaFall17V2noIso"] > 1.555 + 0.075*(electron_col[LF_idx]["pt"] - 25)' ] ,
                    'electron_col[LF_idx]["pt"]>=40. and abs(electron_col[LF_idx]["eta"])<0.8' : [ 'electron_col[LF_idx]["mvaFall17V2noIso"] > 4.392' ] ,
                    'electron_col[LF_idx]["pt"]>=40. and abs(electron_col[LF_idx]["eta"])>=0.8   and abs(electron_col[LF_idx]["eta"])<1.479' : [ 'electron_col[LF_idx]["mvaFall17V2noIso"] > 3.392' ] ,
                    'electron_col[LF_idx]["pt"]>=40. and abs(electron_col[LF_idx]["eta"])>=1.479 and abs(electron_col[LF_idx]["eta"])<2.5'   : [ 'electron_col[LF_idx]["mvaFall17V2noIso"] > 2.680' ] ,
                    } ,
                'tkSF':  { 
                    '1-7' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2016v2/EGM2D_BtoH_combineLowEt_RecoSF_Legacy2016.root' ,
                    } ,
                'susySF':  {
                    '1-7' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2016v2/ElectronScaleFactors_Run2016_SUSY.root#Run2016_MVATightTightIP2D3D#Run2016_ConvIHit0#Run2016_Mini2' ,  
                    } ,
                'fsSF': {
                    '1-7' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2016v2/detailed_ele_full_fast_sf_17.root#MVATightTightIP2D3D_sf#ConvIHit0_sf' , 
                    },
                } ,

            'SusyMVATightMiniIsoTight' : {
                'cuts' : { 
                    'True' :
                        [
                        'electron_col[LF_idx]["pt"]             >  15.' ,
                        'abs(electron_col[LF_idx]["eta"])       <  2.4' ,
                        'abs(electron_col[LF_idx]["sip3d"])     <   4.' ,
                        'abs(electron_col[LF_idx]["dxy"])       < 0.05' ,
                        'abs(electron_col[LF_idx]["dz"])        < 0.10' ,
                        'electron_col[LF_idx]["convVeto"] ==  1',
                        'electron_col[LF_idx]["lostHits"]       ==  0',
                        'electron_col[LF_idx]["miniPFRelIso_all"]<0.1', 
                        ] ,
                    'electron_col[LF_idx]["pt"]<40.  and abs(electron_col[LF_idx]["eta"])<0.8' : [ 'electron_col[LF_idx]["mvaFall17V2noIso"] > 3.447 + 0.063*(electron_col[LF_idx]["pt"] - 25)' ] ,
                    'electron_col[LF_idx]["pt"]<40.  and abs(electron_col[LF_idx]["eta"])>=0.8   and abs(electron_col[LF_idx]["eta"])<1.479' : [ 'electron_col[LF_idx]["mvaFall17V2noIso"] > 2.522 + 0.058*(electron_col[LF_idx]["pt"] - 25)' ] ,
                    'electron_col[LF_idx]["pt"]<40.  and abs(electron_col[LF_idx]["eta"])>=1.479 and abs(electron_col[LF_idx]["eta"])<2.5'   : [ 'electron_col[LF_idx]["mvaFall17V2noIso"] > 1.555 + 0.075*(electron_col[LF_idx]["pt"] - 25)' ] ,
                    'electron_col[LF_idx]["pt"]>=40. and abs(electron_col[LF_idx]["eta"])<0.8' : [ 'electron_col[LF_idx]["mvaFall17V2noIso"] > 4.392' ] ,
                    'electron_col[LF_idx]["pt"]>=40. and abs(electron_col[LF_idx]["eta"])>=0.8   and abs(electron_col[LF_idx]["eta"])<1.479' : [ 'electron_col[LF_idx]["mvaFall17V2noIso"] > 3.392' ] ,
                    'electron_col[LF_idx]["pt"]>=40. and abs(electron_col[LF_idx]["eta"])>=1.479 and abs(electron_col[LF_idx]["eta"])<2.5'   : [ 'electron_col[LF_idx]["mvaFall17V2noIso"] > 2.680' ] ,
                    } ,
                'tkSF':  { 
                    '1-7' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2016v2/EGM2D_BtoH_combineLowEt_RecoSF_Legacy2016.root' ,
                    } ,
                'susySF':  {
                    '1-7' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2016v2/ElectronScaleFactors_Run2016_SUSY.root#Run2016_MVATightTightIP2D3D#Run2016_ConvIHit0#Run2016_Mini' ,  
                    } ,
                'fsSF': {
                    '1-7' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2016v2/detailed_ele_full_fast_sf_17.root#MVATightTightIP2D3D_sf#ConvIHit0_sf' , 
                    },
                } ,

            },
        
        'WgStarObjWP' : {
            'null' : { 
                'cuts' : { 
                    'True' :
                        [
                        'False' ,
                        ] ,
                    } ,
                } ,
            }, 

        }, 

    'Full2017v7': {
        
        'VetoObjWP' : { 
            'baseele' : { 
                'cuts' : { 
                    'True' :
                        [
                        'electron_col[LF_idx]["pt"]             >  10.' ,
                        'abs(electron_col[LF_idx]["eta"])       <  2.4' ,
                        'abs(electron_col[LF_idx]["sip3d"])     <   4.' ,
                        'abs(electron_col[LF_idx]["dxy"])       < 0.05' ,
                        'abs(electron_col[LF_idx]["dz"])        < 0.10' ,
                        'electron_col[LF_idx]["convVeto"] ==  1',
                        ] ,             
                    },
                } ,
            } ,
  
        'FakeObjWP'  : { 
            'baseele' : { 
                'cuts' : { 
                    'True' :
                        [
                        'electron_col[LF_idx]["pt"]             >  10.' ,
                        'abs(electron_col[LF_idx]["eta"])       <  2.4' ,
                        'abs(electron_col[LF_idx]["sip3d"])     <   4.' ,
                        'abs(electron_col[LF_idx]["dxy"])       < 0.05' ,
                        'abs(electron_col[LF_idx]["dz"])        < 0.10' ,
                        'electron_col[LF_idx]["convVeto"] ==  1',
                        ] ,             
                    },
                } ,
            } ,
        
        'TightObjWP' : {

            'cutBasedVeto' : { 
                'cuts' : { 
                    'True' :
                        [
                        'electron_col[LF_idx]["pt"]             >  10.' ,
                        'abs(electron_col[LF_idx]["eta"])       <  2.4' ,
                        'electron_col[LF_idx]["cutBased"]       >=   1' ,
                        'abs(electron_col[LF_idx]["sip3d"])     <   4.' ,
                        'abs(electron_col[LF_idx]["dxy"])       < 0.05' ,
                        'abs(electron_col[LF_idx]["dz"])        < 0.10' ,
                        ] ,
                    },
                'tkSF':  { 
                    '1-1' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/egammaEffi.txt_EGM2D_runB_passingRECO_combineLowEt.root',
                    '2-2' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/egammaEffi.txt_EGM2D_runC_passingRECO_combineLowEt.root',
                    '3-3' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/egammaEffi.txt_EGM2D_runD_passingRECO_combineLowEt.root',
                    '4-4' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/egammaEffi.txt_EGM2D_runE_passingRECO_combineLowEt.root',
                    '5-5' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/egammaEffi.txt_EGM2D_runF_passingRECO_combineLowEt.root',
                  } ,
                'susySF':  {
                    '1-1' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/2017_ElectronWPVeto_Fall17V2_POG.root#EGamma_SF2D' , 
                    '2-2' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/2017_ElectronWPVeto_Fall17V2_POG.root#EGamma_SF2D' , 
                    '3-3' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/2017_ElectronWPVeto_Fall17V2_POG.root#EGamma_SF2D' , 
                    '4-4' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/2017_ElectronWPVeto_Fall17V2_POG.root#EGamma_SF2D' , 
                    '5-5' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/2017_ElectronWPVeto_Fall17V2_POG.root#EGamma_SF2D' , 
                    } ,
                'fsSF': {
                    #'1-5' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2016v2/detailed_ele_full_fast_sf_17.root#CutBasedVetoNoIso94XV2_sf' , 
                    '1-5' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2016v2/detailed_ele_full_fast_sf_17.root#MVAVLooseTightIP2DMini4_sf' , 
                    },
                } ,

            'cutBasedMedium' : {
                'cuts' : { 
                    'True' :
                        [
                        'electron_col[LF_idx]["pt"]             >  15.' ,
                        'abs(electron_col[LF_idx]["eta"])       <  2.4' ,
                        'electron_col[LF_idx]["cutBased"]       >=  3' ,
                        'abs(electron_col[LF_idx]["sip3d"])     <   4.' ,
                        'abs(electron_col[LF_idx]["dxy"])       < 0.05' ,
                        'abs(electron_col[LF_idx]["dz"])        < 0.10' ,
                        'electron_col[LF_idx]["lostHits"]       ==  0',
                        ] ,
                    } ,
                'tkSF':  { 
                    '1-1' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/egammaEffi.txt_EGM2D_runB_passingRECO_combineLowEt.root',
                    '2-2' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/egammaEffi.txt_EGM2D_runC_passingRECO_combineLowEt.root',
                    '3-3' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/egammaEffi.txt_EGM2D_runD_passingRECO_combineLowEt.root',
                    '4-4' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/egammaEffi.txt_EGM2D_runE_passingRECO_combineLowEt.root',
                    '5-5' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/egammaEffi.txt_EGM2D_runF_passingRECO_combineLowEt.root',
                  } ,
                'susySF':  {
                    '1-1' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/2017_ElectronMedium_POG.root#EGamma_SF2D' , 
                    '2-2' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/2017_ElectronMedium_POG.root#EGamma_SF2D' , 
                    '3-3' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/2017_ElectronMedium_POG.root#EGamma_SF2D' , 
                    '4-4' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/2017_ElectronMedium_POG.root#EGamma_SF2D' , 
                    '5-5' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/2017_ElectronMedium_POG.root#EGamma_SF2D' , 
                    } ,
                'fsSF': {
                    '1-5' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2016v2/detailed_ele_full_fast_sf_17.root#CutBasedMediumNoIso94XV2_sf' , 
                    #'1-5' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2016v2/detailed_ele_full_fast_sf_17.root#MVAVLooseTightIP2DMini2_sf' , 
                    },
                } ,

            'cutBasedTight' : {
                'cuts' : { 
                    'True' :
                        [
                        'electron_col[LF_idx]["pt"]             >  15.' ,
                        'abs(electron_col[LF_idx]["eta"])       <  2.4' ,
                        'electron_col[LF_idx]["cutBased"]       >=  4' ,
                        'abs(electron_col[LF_idx]["sip3d"])     <   4.' ,
                        'abs(electron_col[LF_idx]["dxy"])       < 0.05' ,
                        'abs(electron_col[LF_idx]["dz"])        < 0.10' ,
                        'electron_col[LF_idx]["lostHits"]       ==  0',
                        ] ,
                    } ,
                'tkSF':  { 
                    '1-1' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/egammaEffi.txt_EGM2D_runB_passingRECO_combineLowEt.root',
                    '2-2' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/egammaEffi.txt_EGM2D_runC_passingRECO_combineLowEt.root',
                    '3-3' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/egammaEffi.txt_EGM2D_runD_passingRECO_combineLowEt.root',
                    '4-4' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/egammaEffi.txt_EGM2D_runE_passingRECO_combineLowEt.root',
                    '5-5' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/egammaEffi.txt_EGM2D_runF_passingRECO_combineLowEt.root',
                  } ,
                'susySF':  {
                    '1-1' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/2017_ElectronTight_POG.root#EGamma_SF2D' , 
                    '2-2' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/2017_ElectronTight_POG.root#EGamma_SF2D' , 
                    '3-3' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/2017_ElectronTight_POG.root#EGamma_SF2D' , 
                    '4-4' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/2017_ElectronTight_POG.root#EGamma_SF2D' , 
                    '5-5' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/2017_ElectronTight_POG.root#EGamma_SF2D' , 
                    } ,
                'fsSF': {
                    '1-5' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/detailed_ele_full_fast_sf_17.root#CutBasedTightNoIso94XV2_sf' , 
                    #'1-5' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/detailed_ele_full_fast_sf_17.root#MVAVLooseTightIP2DMini_sf' , 
                    },
                } ,

            'SusyMVAVLoose' : {
                'cuts' : { 
                    'True' :
                        [
                        'electron_col[LF_idx]["pt"]             >  10.' ,
                        'abs(electron_col[LF_idx]["eta"])       <  2.4' ,
                        'abs(electron_col[LF_idx]["sip3d"])     <   4.' ,
                        'abs(electron_col[LF_idx]["dxy"])       < 0.05' ,
                        'abs(electron_col[LF_idx]["dz"])        < 0.10' ,
                        'electron_col[LF_idx]["convVeto"] ==  1',
                        'electron_col[LF_idx]["miniPFRelIso_all"]<0.4', 
                        ] ,
                    'electron_col[LF_idx]["pt"]<25.  and abs(electron_col[LF_idx]["eta"])<0.8' : [ 'electron_col[LF_idx]["mvaFall17V1noIso"] >  (-0.788 + (0.148/15.)*(electron_col[LF_idx]["pt"]-10.))' ] ,
                    'electron_col[LF_idx]["pt"]<25.  and abs(electron_col[LF_idx]["eta"])>=0.8   and abs(electron_col[LF_idx]["eta"])<1.479' : [ 'electron_col[LF_idx]["mvaFall17V1noIso"] > (-0.85 + (0.075/15.)*(electron_col[LF_idx]["pt"]-10.))' ] ,
                    'electron_col[LF_idx]["pt"]<25.  and abs(electron_col[LF_idx]["eta"])>=1.479 and abs(electron_col[LF_idx]["eta"])<2.5'   : [ 'electron_col[LF_idx]["mvaFall17V1noIso"] > (-0.81 + (0.077/15.)*(electron_col[LF_idx]["pt"]-10.))' ] ,
                    'electron_col[LF_idx]["pt"]>=25. and abs(electron_col[LF_idx]["eta"])<0.8' : [ 'electron_col[LF_idx]["mvaFall17V1noIso"] > -0.64' ] ,
                    'electron_col[LF_idx]["pt"]>=25. and abs(electron_col[LF_idx]["eta"])>=0.8   and abs(electron_col[LF_idx]["eta"])<1.479' : [ 'electron_col[LF_idx]["mvaFall17V1noIso"] > -0.775' ] ,
                    'electron_col[LF_idx]["pt"]>=25. and abs(electron_col[LF_idx]["eta"])>=1.479 and abs(electron_col[LF_idx]["eta"])<2.5'   : [ 'electron_col[LF_idx]["mvaFall17V1noIso"] > -0.733' ] ,
                    } ,
                'tkSF':  { 
                    '1-1' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/egammaEffi.txt_EGM2D_runB_passingRECO_combineLowEt.root',
                    '2-2' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/egammaEffi.txt_EGM2D_runC_passingRECO_combineLowEt.root',
                    '3-3' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/egammaEffi.txt_EGM2D_runD_passingRECO_combineLowEt.root',
                    '4-4' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/egammaEffi.txt_EGM2D_runE_passingRECO_combineLowEt.root',
                    '5-5' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/egammaEffi.txt_EGM2D_runF_passingRECO_combineLowEt.root',
                  } ,
                'susySF':  {
                    '1-1' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/ElectronScaleFactors_Run2017_SUSY.root#Run2017_MVAVLooseIP2D#Run2017_MVAVLooseTightIP2DMini4' ,  
                    '2-2' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/ElectronScaleFactors_Run2017_SUSY.root#Run2017_MVAVLooseIP2D#Run2017_MVAVLooseTightIP2DMini4' ,  
                    '3-3' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/ElectronScaleFactors_Run2017_SUSY.root#Run2017_MVAVLooseIP2D#Run2017_MVAVLooseTightIP2DMini4' ,  
                    '4-4' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/ElectronScaleFactors_Run2017_SUSY.root#Run2017_MVAVLooseIP2D#Run2017_MVAVLooseTightIP2DMini4' ,  
                    '5-5' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/ElectronScaleFactors_Run2017_SUSY.root#Run2017_MVAVLooseIP2D#Run2017_MVAVLooseTightIP2DMini4' , 
                    } ,
                'fsSF': {
                    '1-5' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/detailed_ele_full_fast_sf_17.root#MVAVLooseTightIP2DMini4_sf' , 
                    },
                } ,

            'SusyMVATight' : {
                'cuts' : { 
                    'True' :
                        [
                        'electron_col[LF_idx]["pt"]             >  15.' ,
                        'abs(electron_col[LF_idx]["eta"])       <  2.4' ,
                        'abs(electron_col[LF_idx]["sip3d"])     <   4.' ,
                        'abs(electron_col[LF_idx]["dxy"])       < 0.05' ,
                        'abs(electron_col[LF_idx]["dz"])        < 0.10' ,
                        'electron_col[LF_idx]["convVeto"] ==  1',
                        'electron_col[LF_idx]["lostHits"]       ==  0',
                        'electron_col[LF_idx]["miniPFRelIso_all"]<0.2', 
                        ] ,
                    'electron_col[LF_idx]["pt"]<25.  and abs(electron_col[LF_idx]["eta"])<0.8' : [ 'electron_col[LF_idx]["mvaFall17V1noIso"] > 0.2+0.032*(electron_col[LF_idx]["pt"]-10)' ] ,
                    'electron_col[LF_idx]["pt"]<25.  and abs(electron_col[LF_idx]["eta"])>=0.8   and abs(electron_col[LF_idx]["eta"])<1.479' : [ 'electron_col[LF_idx]["mvaFall17V1noIso"] > 0.1+0.025*(electron_col[LF_idx]["pt"]-10)' ] ,
                    'electron_col[LF_idx]["pt"]<25.  and abs(electron_col[LF_idx]["eta"])>=1.479 and abs(electron_col[LF_idx]["eta"])<2.5'   : [ 'electron_col[LF_idx]["mvaFall17V1noIso"] > -0.1+0.028*(electron_col[LF_idx]["pt"]-10)' ] ,
                    'electron_col[LF_idx]["pt"]>=25. and abs(electron_col[LF_idx]["eta"])<0.8' : [ 'electron_col[LF_idx]["mvaFall17V1noIso"] > 0.68' ] ,
                    'electron_col[LF_idx]["pt"]>=25. and abs(electron_col[LF_idx]["eta"])>=0.8   and abs(electron_col[LF_idx]["eta"])<1.479' : [ 'electron_col[LF_idx]["mvaFall17V1noIso"] > 0.475' ] ,
                    'electron_col[LF_idx]["pt"]>=25. and abs(electron_col[LF_idx]["eta"])>=1.479 and abs(electron_col[LF_idx]["eta"])<2.5'   : [ 'electron_col[LF_idx]["mvaFall17V1noIso"] > 0.32' ] ,
                    } ,
                'tkSF':  { 
                    '1-1' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/egammaEffi.txt_EGM2D_runB_passingRECO_combineLowEt.root',
                    '2-2' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/egammaEffi.txt_EGM2D_runC_passingRECO_combineLowEt.root',
                    '3-3' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/egammaEffi.txt_EGM2D_runD_passingRECO_combineLowEt.root',
                    '4-4' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/egammaEffi.txt_EGM2D_runE_passingRECO_combineLowEt.root',
                    '5-5' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/egammaEffi.txt_EGM2D_runF_passingRECO_combineLowEt.root',
                  } ,
                'susySF':  {
                    '1-1' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/ElectronScaleFactors_Run2017_SUSY.root#Run2017_MVATightTightIP2D3D#Run2017_ConvIHit0#Run2017_MVAVLooseTightIP2DMini2' ,  
                    '2-2' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/ElectronScaleFactors_Run2017_SUSY.root#Run2017_MVATightTightIP2D3D#Run2017_ConvIHit0#Run2017_MVAVLooseTightIP2DMini2' ,  
                    '3-3' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/ElectronScaleFactors_Run2017_SUSY.root#Run2017_MVATightTightIP2D3D#Run2017_ConvIHit0#Run2017_MVAVLooseTightIP2DMini2' ,  
                    '4-4' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/ElectronScaleFactors_Run2017_SUSY.root#Run2017_MVATightTightIP2D3D#Run2017_ConvIHit0#Run2017_MVAVLooseTightIP2DMini2' ,  
                    '5-5' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/ElectronScaleFactors_Run2017_SUSY.root#Run2017_MVATightTightIP2D3D#Run2017_ConvIHit0#Run2017_MVAVLooseTightIP2DMini2' , 
                    } ,
                'fsSF': {
                    '1-5' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/detailed_ele_full_fast_sf_17.root#MVATightTightIP2D3D_sf#ConvIHit0_sf' , 
                    },
                } ,

            'SusyMVATightMiniIsoTight' : {
                'cuts' : { 
                    'True' :
                        [
                        'electron_col[LF_idx]["pt"]             >  15.' ,
                        'abs(electron_col[LF_idx]["eta"])       <  2.4' ,
                        'abs(electron_col[LF_idx]["sip3d"])     <   4.' ,
                        'abs(electron_col[LF_idx]["dxy"])       < 0.05' ,
                        'abs(electron_col[LF_idx]["dz"])        < 0.10' ,
                        'electron_col[LF_idx]["convVeto"] ==  1',
                        'electron_col[LF_idx]["lostHits"]       ==  0',
                        'electron_col[LF_idx]["miniPFRelIso_all"]<0.1', 
                        ] ,
                    'electron_col[LF_idx]["pt"]<25.  and abs(electron_col[LF_idx]["eta"])<0.8' : [ 'electron_col[LF_idx]["mvaFall17V1noIso"] > 0.2+0.032*(electron_col[LF_idx]["pt"]-10)' ] ,
                    'electron_col[LF_idx]["pt"]<25.  and abs(electron_col[LF_idx]["eta"])>=0.8   and abs(electron_col[LF_idx]["eta"])<1.479' : [ 'electron_col[LF_idx]["mvaFall17V1noIso"] > 0.1+0.025*(electron_col[LF_idx]["pt"]-10)' ] ,
                    'electron_col[LF_idx]["pt"]<25.  and abs(electron_col[LF_idx]["eta"])>=1.479 and abs(electron_col[LF_idx]["eta"])<2.5'   : [ 'electron_col[LF_idx]["mvaFall17V1noIso"] > -0.1+0.028*(electron_col[LF_idx]["pt"]-10)' ] ,
                    'electron_col[LF_idx]["pt"]>=25. and abs(electron_col[LF_idx]["eta"])<0.8' : [ 'electron_col[LF_idx]["mvaFall17V1noIso"] > 0.68' ] ,
                    'electron_col[LF_idx]["pt"]>=25. and abs(electron_col[LF_idx]["eta"])>=0.8   and abs(electron_col[LF_idx]["eta"])<1.479' : [ 'electron_col[LF_idx]["mvaFall17V1noIso"] > 0.475' ] ,
                    'electron_col[LF_idx]["pt"]>=25. and abs(electron_col[LF_idx]["eta"])>=1.479 and abs(electron_col[LF_idx]["eta"])<2.5'   : [ 'electron_col[LF_idx]["mvaFall17V1noIso"] > 0.32' ] ,
                    } ,
                'tkSF':  { 
                    '1-1' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/egammaEffi.txt_EGM2D_runB_passingRECO_combineLowEt.root',
                    '2-2' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/egammaEffi.txt_EGM2D_runC_passingRECO_combineLowEt.root',
                    '3-3' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/egammaEffi.txt_EGM2D_runD_passingRECO_combineLowEt.root',
                    '4-4' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/egammaEffi.txt_EGM2D_runE_passingRECO_combineLowEt.root',
                    '5-5' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/egammaEffi.txt_EGM2D_runF_passingRECO_combineLowEt.root',
                  } ,
                'susySF':  {
                    '1-1' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/ElectronScaleFactors_Run2017_SUSY.root#Run2017_MVATightTightIP2D3D#Run2017_ConvIHit0#Run2017_MVAVLooseTightIP2DMini' ,  
                    '2-2' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/ElectronScaleFactors_Run2017_SUSY.root#Run2017_MVATightTightIP2D3D#Run2017_ConvIHit0#Run2017_MVAVLooseTightIP2DMini' ,  
                    '3-3' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/ElectronScaleFactors_Run2017_SUSY.root#Run2017_MVATightTightIP2D3D#Run2017_ConvIHit0#Run2017_MVAVLooseTightIP2DMini' ,  
                    '4-4' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/ElectronScaleFactors_Run2017_SUSY.root#Run2017_MVATightTightIP2D3D#Run2017_ConvIHit0#Run2017_MVAVLooseTightIP2DMini' ,  
                    '5-5' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/ElectronScaleFactors_Run2017_SUSY.root#Run2017_MVATightTightIP2D3D#Run2017_ConvIHit0#Run2017_MVAVLooseTightIP2DMini' , 
                    } ,
                'fsSF': {
                    '1-5' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/detailed_ele_full_fast_sf_17.root#MVATightTightIP2D3D_sf#ConvIHit0_sf' , 
                   }, 
                } ,

            },
        
        'WgStarObjWP' : {
            'null' : { 
                'cuts' : { 
                    'True' :
                        [
                        'False' ,
                        ] ,
                    } ,
                } ,
            }, 

        },

    'Full2018v7': {
        
        'VetoObjWP' : { 
            'baseele' : { 
                'cuts' : { 
                    'True' :
                        [
                        'electron_col[LF_idx]["pt"]             >  10.' ,
                        'abs(electron_col[LF_idx]["eta"])       <  2.4' ,
                        'abs(electron_col[LF_idx]["sip3d"])     <   4.' ,
                        'abs(electron_col[LF_idx]["dxy"])       < 0.05' ,
                        'abs(electron_col[LF_idx]["dz"])        < 0.10' ,
                        'electron_col[LF_idx]["convVeto"] ==  1',
                        ] ,             
                    },
                } ,
            } ,
  
        'FakeObjWP'  : { 
            'baseele' : { 
                'cuts' : { 
                    'True' :
                        [
                        'electron_col[LF_idx]["pt"]             >  10.' ,
                        'abs(electron_col[LF_idx]["eta"])       <  2.4' ,
                        'abs(electron_col[LF_idx]["sip3d"])     <   4.' ,
                        'abs(electron_col[LF_idx]["dxy"])       < 0.05' ,
                        'abs(electron_col[LF_idx]["dz"])        < 0.10' ,
                        'electron_col[LF_idx]["convVeto"] ==  1',
                        ] ,             
                    },
                } ,
            } ,
        
        'TightObjWP' : {

            'cutBasedVeto' : { 
                'cuts' : { 
                    'True' :
                        [
                        'electron_col[LF_idx]["pt"]             >  10.' ,
                        'abs(electron_col[LF_idx]["eta"])       <  2.4' ,
                        'electron_col[LF_idx]["cutBased"]       >=   1' ,
                        'abs(electron_col[LF_idx]["sip3d"])     <   4.' ,
                        'abs(electron_col[LF_idx]["dxy"])       < 0.05' ,
                        'abs(electron_col[LF_idx]["dz"])        < 0.10' ,
                        ] ,
                    },
                'tkSF':  { 
                    '1-1' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2018/egammaEffi.txt_EGM2D_updatedAll.root',
                    } ,
                'susySF':  {
                    '1-1' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2018/2018_ElectronWPVeto_Fall17V2_POG.root#EGamma_SF2D' ,  
                    } ,
                'fsSF': {
                    #'1-1' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2018/detailed_ele_full_fast_sf_18.root#CutBasedVetoNoIso94XV2_sf' , 
                    '1-1' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2018/detailed_ele_full_fast_sf_18.root#MVAVLooseTightIP2DMini4_sf' , 
                    },
                } ,

            'cutBasedMedium' : {
                'cuts' : { 
                    'True' :
                        [
                        'electron_col[LF_idx]["pt"]             >  15.' ,
                        'abs(electron_col[LF_idx]["eta"])       <  2.4' ,
                        'electron_col[LF_idx]["cutBased"]       >=  3' ,
                        'abs(electron_col[LF_idx]["sip3d"])     <   4.' ,
                        'abs(electron_col[LF_idx]["dxy"])       < 0.05' ,
                        'abs(electron_col[LF_idx]["dz"])        < 0.10' ,
                        'electron_col[LF_idx]["lostHits"]       ==  0',
                        ] ,
                    } ,
                'tkSF':  { 
                    '1-1' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2018/egammaEffi.txt_EGM2D_updatedAll.root',
                    } ,
                'susySF':  {
                    '1-1' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2018/2018_ElectronMedium_POG.root#EGamma_SF2D' ,  
                    } ,
                'fsSF': {
                    '1-1' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2018/detailed_ele_full_fast_sf_18.root#CutBasedMediumNoIso94XV2_sf' , 
                    #'1-1' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2018/detailed_ele_full_fast_sf_18.root#MVAVLooseTightIP2DMini2_sf' , 
                    },
                } ,

            'cutBasedTight' : {
                'cuts' : { 
                    'True' :
                        [
                        'electron_col[LF_idx]["pt"]             >  15.' ,
                        'abs(electron_col[LF_idx]["eta"])       <  2.4' ,
                        'electron_col[LF_idx]["cutBased"]       >=  4' ,
                        'abs(electron_col[LF_idx]["sip3d"])     <   4.' ,
                        'abs(electron_col[LF_idx]["dxy"])       < 0.05' ,
                        'abs(electron_col[LF_idx]["dz"])        < 0.10' ,
                        'electron_col[LF_idx]["lostHits"]       ==  0',
                        ] ,
                    } ,
                'tkSF':  { 
                    '1-1' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2018/egammaEffi.txt_EGM2D_updatedAll.root',
                    } ,
                'susySF':  {
                    '1-1' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2018/2018_ElectronTight_POG.root#EGamma_SF2D' ,  
                    } ,
                'fsSF': {
                    '1-1' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2018/detailed_ele_full_fast_sf_18.root#CutBasedTightNoIso94XV2_sf' , 
                    #'1-1' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2018/detailed_ele_full_fast_sf_18.root#MVAVLooseTightIP2DMini_sf' , 
                } ,
            },

            'SusyMVAVLoose' : {
                'cuts' : { 
                    'True' :
                        [
                        'electron_col[LF_idx]["pt"]             >  10.' ,
                        'abs(electron_col[LF_idx]["eta"])       <  2.4' ,
                        'abs(electron_col[LF_idx]["sip3d"])     <   4.' ,
                        'abs(electron_col[LF_idx]["dxy"])       < 0.05' ,
                        'abs(electron_col[LF_idx]["dz"])        < 0.10' ,
                        'electron_col[LF_idx]["convVeto"] ==  1',
                        'electron_col[LF_idx]["miniPFRelIso_all"]<0.4', 
                        ] ,
                    'electron_col[LF_idx]["pt"]<25.  and abs(electron_col[LF_idx]["eta"])<0.8' : [ 'electron_col[LF_idx]["mvaFall17V2noIso"] > 1.204 + 0.066*(electron_col[LF_idx]["pt"] - 25)' ] ,
                    'electron_col[LF_idx]["pt"]<25.  and abs(electron_col[LF_idx]["eta"])>=0.8   and abs(electron_col[LF_idx]["eta"])<1.479' : [ 'electron_col[LF_idx]["mvaFall17V2noIso"] > 0.084 + 0.033*(electron_col[LF_idx]["pt"] - 25)' ] ,
                    'electron_col[LF_idx]["pt"]<25.  and abs(electron_col[LF_idx]["eta"])>=1.479 and abs(electron_col[LF_idx]["eta"])<2.5'   : [ 'electron_col[LF_idx]["mvaFall17V2noIso"] > -0.123 + 0.053*(electron_col[LF_idx]["pt"] - 25)' ] ,
                    'electron_col[LF_idx]["pt"]>=25. and abs(electron_col[LF_idx]["eta"])<0.8' : [ 'electron_col[LF_idx]["mvaFall17V2noIso"] > 1.204' ] ,
                    'electron_col[LF_idx]["pt"]>=25. and abs(electron_col[LF_idx]["eta"])>=0.8   and abs(electron_col[LF_idx]["eta"])<1.479' : [ 'electron_col[LF_idx]["mvaFall17V2noIso"] > 0.084' ] ,
                    'electron_col[LF_idx]["pt"]>=25. and abs(electron_col[LF_idx]["eta"])>=1.479 and abs(electron_col[LF_idx]["eta"])<2.5'   : [ 'electron_col[LF_idx]["mvaFall17V2noIso"] > -0.123' ] ,
                    } ,
                'tkSF':  { 
                    '1-1' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2018/egammaEffi.txt_EGM2D_updatedAll.root',
                    } ,
                'susySF':  {
                    '1-1' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2018/ElectronScaleFactors_Run2018_SUSY.root#Run2018_MVAVLooseIP2D#Run2018_Mini4' ,  
                    } ,
                'fsSF': {
                    '1-1' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2018/detailed_ele_full_fast_sf_18.root#MVAVLooseTightIP2DMini4_sf' , 
                    },
                } ,

            'SusyMVATight' : {
                'cuts' : { 
                    'True' :
                        [
                        'electron_col[LF_idx]["pt"]             >  15.' ,
                        'abs(electron_col[LF_idx]["eta"])       <  2.4' ,
                        'abs(electron_col[LF_idx]["sip3d"])     <   4.' ,
                        'abs(electron_col[LF_idx]["dxy"])       < 0.05' ,
                        'abs(electron_col[LF_idx]["dz"])        < 0.10' ,
                        'electron_col[LF_idx]["convVeto"] ==  1',
                        'electron_col[LF_idx]["lostHits"]       ==  0',
                        'electron_col[LF_idx]["miniPFRelIso_all"]<0.2', 
                        ] ,
                    'electron_col[LF_idx]["pt"]<25.  and abs(electron_col[LF_idx]["eta"])<0.8' : [ 'electron_col[LF_idx]["mvaFall17V2noIso"] >  4.277 + 0.112*(electron_col[LF_idx]["pt"] - 25)' ] ,
                    'electron_col[LF_idx]["pt"]<25.  and abs(electron_col[LF_idx]["eta"])>=0.8   and abs(electron_col[LF_idx]["eta"])<1.479' : [ 'electron_col[LF_idx]["mvaFall17V2noIso"] > 3.152 + 0.060*(electron_col[LF_idx]["pt"] - 25)' ] ,
                    'electron_col[LF_idx]["pt"]<25.  and abs(electron_col[LF_idx]["eta"])>=1.479 and abs(electron_col[LF_idx]["eta"])<2.5'   : [ 'electron_col[LF_idx]["mvaFall17V2noIso"] > 2.359 + 0.087*(electron_col[LF_idx]["pt"] - 25) ' ] ,
                    'electron_col[LF_idx]["pt"]>=25. and abs(electron_col[LF_idx]["eta"])<0.8' : [ 'electron_col[LF_idx]["mvaFall17V2noIso"] > 4.277' ] ,
                    'electron_col[LF_idx]["pt"]>=25. and abs(electron_col[LF_idx]["eta"])>=0.8   and abs(electron_col[LF_idx]["eta"])<1.479' : [ 'electron_col[LF_idx]["mvaFall17V2noIso"] > 3.152' ] ,
                    'electron_col[LF_idx]["pt"]>=25. and abs(electron_col[LF_idx]["eta"])>=1.479 and abs(electron_col[LF_idx]["eta"])<2.5'   : [ 'electron_col[LF_idx]["mvaFall17V2noIso"] > 2.359' ] ,
                    } ,
                'tkSF':  { 
                    '1-1' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2018/egammaEffi.txt_EGM2D_updatedAll.root',
                    } ,
                'susySF':  {
                    '1-1' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2018/ElectronScaleFactors_Run2018_SUSY.root#Run2018_MVATightTightIP2D3D#Run2018_ConvIHit0#Run2018_Mini2' ,  
                    } ,
                'fsSF': {
                    '1-1' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2018/detailed_ele_full_fast_sf_18.root#MVATightTightIP2D3D_sf#ConvIHit0_sf' , 
                    },
                } ,

            'SusyMVATightMiniIsoTight' : {
                'cuts' : { 
                    'True' :
                        [
                        'electron_col[LF_idx]["pt"]             >  15.' ,
                        'abs(electron_col[LF_idx]["eta"])       <  2.4' ,
                        'abs(electron_col[LF_idx]["sip3d"])     <   4.' ,
                        'abs(electron_col[LF_idx]["dxy"])       < 0.05' ,
                        'abs(electron_col[LF_idx]["dz"])        < 0.10' ,
                        'electron_col[LF_idx]["convVeto"] ==  1',
                        'electron_col[LF_idx]["lostHits"]       ==  0',
                        'electron_col[LF_idx]["miniPFRelIso_all"]<0.1', 
                        ] ,
                    'electron_col[LF_idx]["pt"]<25.  and abs(electron_col[LF_idx]["eta"])<0.8' : [ 'electron_col[LF_idx]["mvaFall17V2noIso"] >  4.277 + 0.112*(electron_col[LF_idx]["pt"] - 25)' ] ,
                    'electron_col[LF_idx]["pt"]<25.  and abs(electron_col[LF_idx]["eta"])>=0.8   and abs(electron_col[LF_idx]["eta"])<1.479' : [ 'electron_col[LF_idx]["mvaFall17V2noIso"] > 3.152 + 0.060*(electron_col[LF_idx]["pt"] - 25)' ] ,
                    'electron_col[LF_idx]["pt"]<25.  and abs(electron_col[LF_idx]["eta"])>=1.479 and abs(electron_col[LF_idx]["eta"])<2.5'   : [ 'electron_col[LF_idx]["mvaFall17V2noIso"] > 2.359 + 0.087*(electron_col[LF_idx]["pt"] - 25) ' ] ,
                    'electron_col[LF_idx]["pt"]>=25. and abs(electron_col[LF_idx]["eta"])<0.8' : [ 'electron_col[LF_idx]["mvaFall17V2noIso"] > 4.277' ] ,
                    'electron_col[LF_idx]["pt"]>=25. and abs(electron_col[LF_idx]["eta"])>=0.8   and abs(electron_col[LF_idx]["eta"])<1.479' : [ 'electron_col[LF_idx]["mvaFall17V2noIso"] > 3.152' ] ,
                    'electron_col[LF_idx]["pt"]>=25. and abs(electron_col[LF_idx]["eta"])>=1.479 and abs(electron_col[LF_idx]["eta"])<2.5'   : [ 'electron_col[LF_idx]["mvaFall17V2noIso"] > 2.359' ] ,
                    } ,
                'tkSF':  { 
                    '1-1' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2018/egammaEffi.txt_EGM2D_updatedAll.root',
                    } ,
                'susySF':  {
                    '1-1' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2018/ElectronScaleFactors_Run2018_SUSY.root#Run2018_MVATightTightIP2D3D#Run2018_ConvIHit0#Run2018_Mini' ,  
                    } ,
                'fsSF': {
                    '1-1' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2018/detailed_ele_full_fast_sf_18.root#MVATightTightIP2D3D_sf#ConvIHit0_sf' , 
                    },
                } ,

        },
        
        'WgStarObjWP' : {
            'null' : { 
                'cuts' : { 
                    'True' :
                        [
                        'False' ,
                        ] ,
                    } ,
                } ,
            }, 

        },

}


MuonWP = {

    'Full2016v4': {

        'VetoObjWP' : { 
            'loose' : {
                'cuts' : { 
                    'True' :
                        [
                        'muon_col[LF_idx]["pt"]             >  15.' ,
                        'abs(muon_col[LF_idx]["eta"])       <  2.4' ,  
                        'muon_col[LF_idx]["looseId"]        ==   1' ,
                        'abs(muon_col[LF_idx]["sip3d"])     <   4.' ,
                        'abs(muon_col[LF_idx]["dxy"])       < 0.05' ,
                        'abs(muon_col[LF_idx]["dz"])        < 0.10' ,
                        #'muon_col[LF_idx]["pfRelIso03_all"] < 0.40' , # SUS-17-010
                        #'muon_col[LF_idx]["miniIsoId"] >= 1' ,
                        'muon_col[LF_idx]["pfRelIso04_all"] < 0.25' , 
                        ]
                    } ,
                }
            } ,
        
        'FakeObjWP'  : {
            'loose' : {
                'cuts' : { 
                    'True' :
                        [
                        'muon_col[LF_idx]["pt"]             >  15.' ,
                        'abs(muon_col[LF_idx]["eta"])       <  2.4' ,
                        'muon_col[LF_idx]["looseId"]        ==   1' , 
                        'abs(muon_col[LF_idx]["sip3d"])     <   4.' ,
                        'abs(muon_col[LF_idx]["dxy"])       < 0.05' ,
                        'abs(muon_col[LF_idx]["dz"])        < 0.10' ,
                        #'muon_col[LF_idx]["pfRelIso03_all"] < 0.40' , # SUS-17-010
                        #'muon_col[LF_idx]["miniIsoId"] >= 1' ,
                        'muon_col[LF_idx]["pfRelIso04_all"] < 0.25' , 
                        ] ,
                    } ,    
                } ,
            } ,

        'TightObjWP' :  {

            'medium' : {
                'cuts' : { 
                    'True' :
                        [
                        'muon_col[LF_idx]["pt"]             >  15.' ,
                        'abs(muon_col[LF_idx]["eta"])       <  2.4' ,  
                        'muon_col[LF_idx]["mediumId"]       ==   1' ,
                        'abs(muon_col[LF_idx]["sip3d"])     <   4.' ,
                        'abs(muon_col[LF_idx]["dxy"])       < 0.05' ,
                        'abs(muon_col[LF_idx]["dz"])        < 0.10' ,
                        #'muon_col[LF_idx]["pfRelIso03_all"] < 0.12' , # SUS-17-010
                        'muon_col[LF_idx]["miniIsoId"] >= 2' ,
                        ] ,
                    } ,
                'tkSF':  { 
                    '1-4' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2016/trackerSF_Moriond17_MuoPOG_BCDEF.root' ,
                    '5-7' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2016/trackerSF_Moriond17_MuoPOG_GH.root' ,
                    } ,
                'tkSFerror': 0.01,
                'susySF':  {
                    '1-4' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2016v2/Muon_2016BCDEF_ID_POG.root#NUM_MediumID_DEN_genTracks_eta_pt&LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2016v2/Muon_2016_MiniIso_SUSY.root#TnP_MC_NUM_MiniIso02Cut_DEN_MediumID_PAR_pt_eta' ,
                    '5-7' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2016v2/Muon_2016GH_ID_POG.root#NUM_MediumID_DEN_genTracks_eta_pt&LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2016v2/Muon_2016_MiniIso_SUSY.root#TnP_MC_NUM_MiniIso02Cut_DEN_MediumID_PAR_pt_eta'  , 
                     } ,
                'fsSF': {
                    '1-7' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2016v2/detailed_mu_full_fast_sf_17.root#miniIso02_MediumId_sf' , 
                    },
                #'fakeW' : '/LatinoAnalysis/Gardener/python/data/fake_prompt_rates/80X/lowPtCorrected/36fb_muon/' ,
              } ,

            'mediumIsoTight' : {
                'cuts' : { 
                    'True' :
                        [
                        'muon_col[LF_idx]["pt"]             >  15.' ,
                        'abs(muon_col[LF_idx]["eta"])       <  2.4' ,  
                        'muon_col[LF_idx]["mediumId"]       ==   1' ,
                        'abs(muon_col[LF_idx]["sip3d"])     <   4.' ,
                        'abs(muon_col[LF_idx]["dxy"])       < 0.05' ,
                        'abs(muon_col[LF_idx]["dz"])        < 0.10' ,
                        #'muon_col[LF_idx]["pfRelIso03_all"] < 0.12' , # SUS-17-010
                        'muon_col[LF_idx]["miniIsoId"] >= 3' ,
                        ] ,
                    } ,
                'tkSF':  { 
                    '1-4' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2016/trackerSF_Moriond17_MuoPOG_BCDEF.root' ,
                    '5-7' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2016/trackerSF_Moriond17_MuoPOG_GH.root' ,
                    } ,
                'tkSFerror': 0.01,
                'susySF':  {
                    '1-4' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2016v2/Muon_2016BCDEF_ID_POG.root#NUM_MediumID_DEN_genTracks_eta_pt&LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2016v2/Muon_2016_MiniIso_SUSY.root#TnP_MC_NUM_MiniIso02Cut_DEN_MediumID_PAR_pt_eta' ,
                    '5-7' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2016v2/Muon_2016GH_ID_POG.root#NUM_MediumID_DEN_genTracks_eta_pt&LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2016v2/Muon_2016_MiniIso_SUSY.root#TnP_MC_NUM_MiniIso02Cut_DEN_MediumID_PAR_pt_eta'  , 
                     } ,
                'fsSF': {
                    '1-7' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2016v2/detailed_mu_full_fast_sf_17.root#miniIso01_MediumId_sf' , 
                    },
                #'fakeW' : '/LatinoAnalysis/Gardener/python/data/fake_prompt_rates/80X/lowPtCorrected/36fb_muon/' ,
              } ,

            'mediumRelIsoTight' : {
                'cuts' : { 
                    'True' :
                        [
                        'muon_col[LF_idx]["pt"]             >  15.' ,
                        'abs(muon_col[LF_idx]["eta"])       <  2.4' ,  
                        'muon_col[LF_idx]["mediumId"]       ==   1' ,
                        'abs(muon_col[LF_idx]["sip3d"])     <   4.' ,
                        'abs(muon_col[LF_idx]["dxy"])       < 0.05' ,
                        'abs(muon_col[LF_idx]["dz"])        < 0.10' ,
                        'muon_col[LF_idx]["pfRelIso04_all"] < 0.15' , 
                        ] ,
                    } ,
                'tkSF':  { 
                    '1-4' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2016/trackerSF_Moriond17_MuoPOG_BCDEF.root' ,
                    '5-7' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2016/trackerSF_Moriond17_MuoPOG_GH.root' ,
                    } ,
                'tkSFerror': 0.01,
                'susySF':  {
                    '1-4' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2016v2/Muon_2016BCDEF_ID_POG.root#NUM_MediumID_DEN_genTracks_eta_pt&LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2016v2/Muon_2016BCDEF_ISO_POG.root#NUM_TightRelIso_DEN_MediumID_eta_pt' ,
                    '5-7' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2016v2/Muon_2016GH_ID_POG.root#NUM_MediumID_DEN_genTracks_eta_pt&LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2016v2/Muon_2016GH_ISO_POG.root#NUM_TightRelIso_DEN_MediumID_eta_pt' , 
                     } ,
                'fsSF': {
                    '1-7' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2016v2/detailed_mu_full_fast_sf_17.root#miniIso01_MediumId_sf' , 
                    },
                #'fakeW' : '/LatinoAnalysis/Gardener/python/data/fake_prompt_rates/80X/lowPtCorrected/36fb_muon/' ,
              } ,

            'mediumSUS17010' : {
                'cuts' : { 
                    'True' :
                        [
                        'muon_col[LF_idx]["pt"]             >  15.' ,
                        'abs(muon_col[LF_idx]["eta"])       <  2.4' ,  
                        'muon_col[LF_idx]["mediumId"]       ==   1' ,
                        'abs(muon_col[LF_idx]["sip3d"])     <   4.' ,
                        'abs(muon_col[LF_idx]["dxy"])       < 0.05' ,
                        'abs(muon_col[LF_idx]["dz"])        < 0.10' ,
                        'muon_col[LF_idx]["pfRelIso03_all"] < 0.12' ,
                        ] ,
                    } ,
                'tkSF':  { 
                    '1-4' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2016/trackerSF_Moriond17_MuoPOG_BCDEF.root' ,
                    '5-7' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2016/trackerSF_Moriond17_MuoPOG_GH.root' ,
                    } ,
                'tkSFerror': 0.01,
                'susySF':  {
                    '1-4' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2016v2/Muon_2016BCDEF_ID_POG.root#NUM_MediumID_DEN_genTracks_eta_pt&LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2016v2/Muon_2016BCDEF_ISO_POG.root#NUM_TightRelIso_DEN_MediumID_eta_pt' ,
                    '5-7' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2016v2/Muon_2016GH_ID_POG.root#NUM_MediumID_DEN_genTracks_eta_pt&LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2016v2/Muon_2016GH_ISO_POG.root#NUM_TightRelIso_DEN_MediumID_eta_pt' , 
                     } ,
                'fsSF': {
                    '1-7' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2016v2/detailed_mu_full_fast_sf_17.root#miniIso01_MediumId_sf' , 
                    },
                #'fakeW' : '/LatinoAnalysis/Gardener/python/data/fake_prompt_rates/80X/lowPtCorrected/36fb_muon/' ,
              } ,

        } ,
        
        'WgStarObjWP' : {
            'null' : { 
                'cuts' : { 
                    'True' :
                    [
                        'False' ,
                    ] ,
                } ,
            } ,
        }, 
        
    },

    'Full2017v4': {

        'VetoObjWP' : { 
            'loose' : {
                'cuts' : { 
                    'True' :
                        [
                        'muon_col[LF_idx]["pt"]             >  15.' ,
                        'abs(muon_col[LF_idx]["eta"])       <  2.4' , 
                        'muon_col[LF_idx]["looseId"]        ==   1' , 
                        'abs(muon_col[LF_idx]["sip3d"])     <   4.' ,
                        'abs(muon_col[LF_idx]["dxy"])       < 0.05' ,
                        'abs(muon_col[LF_idx]["dz"])        < 0.10' ,
                        #'muon_col[LF_idx]["pfRelIso03_all"] < 0.40' , # SUS-17-010
                        #'muon_col[LF_idx]["miniIsoId"] >= 1' ,
                        'muon_col[LF_idx]["pfRelIso04_all"] < 0.25' , 
                        ]
                    } ,
                }
            } ,
        
        'FakeObjWP'  : {
            'loose' : {
                'cuts' : { 
                    'True' :
                        [
                        'muon_col[LF_idx]["pt"]             >  15.' ,
                        'abs(muon_col[LF_idx]["eta"])       <  2.4' , 
                        'muon_col[LF_idx]["looseId"]        ==   1' , 
                        'abs(muon_col[LF_idx]["sip3d"])     <   4.' ,
                        'abs(muon_col[LF_idx]["dxy"])       < 0.05' ,
                        'abs(muon_col[LF_idx]["dz"])        < 0.10' ,
                        #'muon_col[LF_idx]["pfRelIso03_all"] < 0.40' , # SUS-17-010
                        #'muon_col[LF_idx]["miniIsoId"] >= 1' ,
                        'muon_col[LF_idx]["pfRelIso04_all"] < 0.25' , 
                        ] ,
                    } ,    
                } ,
            } ,

        'TightObjWP' :  {

            'medium' : {
                'cuts' : { 
                    'True' :
                        [
                        'muon_col[LF_idx]["pt"]             >  15.' ,
                        'abs(muon_col[LF_idx]["eta"])       <  2.4' ,  
                        'muon_col[LF_idx]["mediumId"]       ==   1' ,
                        'abs(muon_col[LF_idx]["sip3d"])     <   4.' ,
                        'abs(muon_col[LF_idx]["dxy"])       < 0.05' ,
                        'abs(muon_col[LF_idx]["dz"])        < 0.10' ,
                        #'muon_col[LF_idx]["pfRelIso03_all"] < 0.12' , # SUS-17-010
                        'muon_col[LF_idx]["miniIsoId"] >= 2' ,
                        ] ,
                    } ,
                'susySF':  {
                    '1-5' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/RunBCDEF_SF_ID_syst.root#NUM_MediumID_DEN_genTracks_pt_abseta&LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/Muon_2017_MiniIso_SUSY.root#TnP_MC_NUM_MiniIso02Cut_DEN_MediumID_PAR_pt_eta' ,
                     } ,
                'fsSF': {
                    '1-5' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/detailed_mu_full_fast_sf_17.root#miniIso02_MediumId_sf' , 
                    },
              } ,

            'mediumIsoTight' : {
                'cuts' : { 
                    'True' :
                        [
                        'muon_col[LF_idx]["pt"]             >  15.' ,
                        'abs(muon_col[LF_idx]["eta"])       <  2.4' ,  
                        'muon_col[LF_idx]["mediumId"]       ==   1' ,
                        'abs(muon_col[LF_idx]["sip3d"])     <   4.' ,
                        'abs(muon_col[LF_idx]["dxy"])       < 0.05' ,
                        'abs(muon_col[LF_idx]["dz"])        < 0.10' ,
                        #'muon_col[LF_idx]["pfRelIso03_all"] < 0.12' , # SUS-17-010
                        'muon_col[LF_idx]["miniIsoId"] >= 3' ,
                        ] ,
                    } ,
                'susySF':  {
                    '1-5' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/RunBCDEF_SF_ID_syst.root#NUM_MediumID_DEN_genTracks_pt_abseta&LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/Muon_2017_MiniIso_SUSY.root#TnP_MC_NUM_MiniIso02Cut_DEN_MediumID_PAR_pt_eta' ,
                     } ,
                'fsSF': {
                    '1-5' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/detailed_mu_full_fast_sf_17.root#miniIso01_MediumId_sf' , 
                    },
              } ,

            'mediumRelIsoTight' : {
                'cuts' : { 
                    'True' :
                        [
                        'muon_col[LF_idx]["pt"]             >  15.' ,
                        'abs(muon_col[LF_idx]["eta"])       <  2.4' ,  
                        'muon_col[LF_idx]["mediumId"]       ==   1' ,
                        'abs(muon_col[LF_idx]["sip3d"])     <   4.' ,
                        'abs(muon_col[LF_idx]["dxy"])       < 0.05' ,
                        'abs(muon_col[LF_idx]["dz"])        < 0.10' ,
                        'muon_col[LF_idx]["pfRelIso04_all"] < 0.15' , 
                        ] ,
                    } ,
                'susySF':  {
                    '1-5' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/RunBCDEF_SF_ID_syst.root#NUM_MediumID_DEN_genTracks_pt_abseta&LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/RunBCDEF_SF_ISO_syst.root#NUM_TightRelIso_DEN_MediumID_pt_abseta' ,
                     } ,
                'fsSF': {
                    '1-5' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/detailed_mu_full_fast_sf_17.root#miniIso01_MediumId_sf' , 
                    },
              } ,

            'mediumSUS17010' : {
                'cuts' : { 
                    'True' :
                        [
                        'muon_col[LF_idx]["pt"]             >  15.' ,
                        'abs(muon_col[LF_idx]["eta"])       <  2.4' ,  
                        'muon_col[LF_idx]["mediumId"]       ==   1' ,
                        'abs(muon_col[LF_idx]["sip3d"])     <   4.' ,
                        'abs(muon_col[LF_idx]["dxy"])       < 0.05' ,
                        'abs(muon_col[LF_idx]["dz"])        < 0.10' ,
                        'muon_col[LF_idx]["pfRelIso03_all"] < 0.12' , 
                        ] ,
                    } ,
                'susySF':  {
                    '1-5' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/RunBCDEF_SF_ID_syst.root#NUM_MediumID_DEN_genTracks_pt_abseta&LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/RunBCDEF_SF_ISO_syst.root#NUM_TightRelIso_DEN_MediumID_pt_abseta' ,
                     } ,
                'fsSF': {
                    '1-5' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/detailed_mu_full_fast_sf_17.root#miniIso01_MediumId_sf' , 
                    },
              } ,
            
         } ,
        
        'WgStarObjWP' : {
            'null' : { 
                'cuts' : { 
                    'True' :
                    [
                        'False' ,
                    ] ,
                } ,
            } ,
        }, 

    },

    'Full2018v4': {

        'VetoObjWP' : { 
            'loose' : {
                'cuts' : { 
                    'True' :
                        [
                        'muon_col[LF_idx]["pt"]             >  15.' ,
                        'abs(muon_col[LF_idx]["eta"])       <  2.4' , 
                        'muon_col[LF_idx]["looseId"]        ==   1' ,
                        'abs(muon_col[LF_idx]["sip3d"])     <   4.' , 
                        'abs(muon_col[LF_idx]["dxy"])       < 0.05' ,
                        'abs(muon_col[LF_idx]["dz"])        < 0.10' ,
                        #'muon_col[LF_idx]["pfRelIso03_all"] < 0.40' , # SUS-17-010
                        #'muon_col[LF_idx]["miniIsoId"] >= 1' ,
                        'muon_col[LF_idx]["pfRelIso04_all"] < 0.25' , 
                        ]
                    } ,
                }
            } ,
        
        'FakeObjWP'  : {
            'loose' : {
                'cuts' : { 
                    'True' :
                        [
                        'muon_col[LF_idx]["pt"]             >  15.' ,
                        'abs(muon_col[LF_idx]["eta"])       <  2.4' , 
                        'muon_col[LF_idx]["looseId"]        ==   1' , 
                        'abs(muon_col[LF_idx]["sip3d"])     <   4.' ,
                        'abs(muon_col[LF_idx]["dxy"])       < 0.05' ,
                        'abs(muon_col[LF_idx]["dz"])        < 0.10' ,
                        #'muon_col[LF_idx]["pfRelIso03_all"] < 0.40' , # SUS-17-010
                        #'muon_col[LF_idx]["miniIsoId"] >= 1' ,
                        'muon_col[LF_idx]["pfRelIso04_all"] < 0.25' , 
                        ] ,
                    } ,    
                } ,
            } ,

        'TightObjWP' :  {

            'medium' : {
                'cuts' : { 
                    'True' :
                        [
                        'muon_col[LF_idx]["pt"]             >  15.' ,
                        'abs(muon_col[LF_idx]["eta"])       <  2.4' ,  
                        'muon_col[LF_idx]["mediumId"]       ==   1' ,
                        'abs(muon_col[LF_idx]["sip3d"])     <   4.' ,
                        'abs(muon_col[LF_idx]["dxy"])       < 0.05' ,
                        'abs(muon_col[LF_idx]["dz"])        < 0.10' ,
                        #'muon_col[LF_idx]["pfRelIso03_all"] < 0.12' , # SUS-17-010
                        'muon_col[LF_idx]["miniIsoId"] >= 2' ,
                        ] ,
                    } ,
                'susySF':  {
                    '1-1' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2018/RunABCD_SF_ID.root#NUM_MediumID_DEN_TrackerMuons_pt_abseta&LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/Muon_2017_MiniIso_SUSY.root#TnP_MC_NUM_MiniIso02Cut_DEN_MediumID_PAR_pt_eta' ,
                     } ,
                'fsSF': {
                    '1-1' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2018/detailed_mu_full_fast_sf_18.root#miniIso02_MediumId_sf' , 
                    },
              } ,

            'mediumIsoTight' : {
                'cuts' : { 
                    'True' :
                        [
                        'muon_col[LF_idx]["pt"]             >  15.' ,
                        'abs(muon_col[LF_idx]["eta"])       <  2.4' ,  
                        'muon_col[LF_idx]["mediumId"]       ==   1' ,
                        'abs(muon_col[LF_idx]["sip3d"])     <   4.' ,
                        'abs(muon_col[LF_idx]["dxy"])       < 0.05' ,
                        'abs(muon_col[LF_idx]["dz"])        < 0.10' ,
                        #'muon_col[LF_idx]["pfRelIso03_all"] < 0.12' , # SUS-17-010
                        'muon_col[LF_idx]["miniIsoId"] >= 3' ,
                        ] ,
                    } ,
                'susySF':  {
                    '1-1' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2018/RunABCD_SF_ID.root#NUM_MediumID_DEN_TrackerMuons_pt_abseta&LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/Muon_2017_MiniIso_SUSY.root#TnP_MC_NUM_MiniIso02Cut_DEN_MediumID_PAR_pt_eta' ,
                     } ,
                'fsSF': {
                    '1-1' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2018/detailed_mu_full_fast_sf_18.root#miniIso01_MediumId_sf' , 
                    },
              } ,

            'mediumRelIsoTight' : {
                'cuts' : { 
                    'True' :
                        [
                        'muon_col[LF_idx]["pt"]             >  15.' ,
                        'abs(muon_col[LF_idx]["eta"])       <  2.4' ,  
                        'muon_col[LF_idx]["mediumId"]       ==   1' ,
                        'abs(muon_col[LF_idx]["sip3d"])     <   4.' ,
                        'abs(muon_col[LF_idx]["dxy"])       < 0.05' ,
                        'abs(muon_col[LF_idx]["dz"])        < 0.10' ,
                        'muon_col[LF_idx]["pfRelIso04_all"] < 0.15' , 
                        ] ,
                    } ,
                'susySF':  {
                    '1-1' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2018/RunABCD_SF_ID.root#NUM_MediumID_DEN_TrackerMuons_pt_abseta&LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2018/RunABCD_SF_ISO.root#NUM_TightRelIso_DEN_MediumID_pt_abseta' ,
                     } ,
                'fsSF': {
                    '1-1' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2018/detailed_mu_full_fast_sf_18.root#miniIso01_MediumId_sf' , 
                    },
              } ,

            'mediumSUS17010' : {
                'cuts' : { 
                    'True' :
                        [
                        'muon_col[LF_idx]["pt"]             >  15.' ,
                        'abs(muon_col[LF_idx]["eta"])       <  2.4' ,  
                        'muon_col[LF_idx]["mediumId"]       ==   1' ,
                        'abs(muon_col[LF_idx]["sip3d"])     <   4.' ,
                        'abs(muon_col[LF_idx]["dxy"])       < 0.05' ,
                        'abs(muon_col[LF_idx]["dz"])        < 0.10' ,
                        'muon_col[LF_idx]["pfRelIso03_all"] < 0.12' ,
                        ] ,
                    } ,
                'susySF':  {
                    '1-1' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2018/RunABCD_SF_ID.root#NUM_MediumID_DEN_TrackerMuons_pt_abseta&LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2018/RunABCD_SF_ISO.root#NUM_TightRelIso_DEN_MediumID_pt_abseta' ,
                     } ,
                'fsSF': {
                    '1-1' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2018/detailed_mu_full_fast_sf_18.root#miniIso01_MediumId_sf' , 
                    },
              } ,
            
         } ,
        
        'WgStarObjWP' : {
            'null' : { 
                'cuts' : { 
                    'True' :
                    [
                        'False' ,
                    ] ,
                } ,
            } ,
        }, 

    },

    'Full2016v7': {

        'VetoObjWP' : { 
            'loosenoiso' : {
                'cuts' : { 
                    'True' :
                        [
                        'muon_col[LF_idx]["pt"]             >  10.' ,
                        'abs(muon_col[LF_idx]["eta"])       <  2.4' ,  
                        'muon_col[LF_idx]["looseId"]        ==   1' ,
                        'abs(muon_col[LF_idx]["sip3d"])     <   4.' ,
                        'abs(muon_col[LF_idx]["dxy"])       < 0.05' ,
                        'abs(muon_col[LF_idx]["dz"])        < 0.10' ,
                        ]
                    } ,
                }
            } ,
        
        'FakeObjWP'  : {
            'loosenoiso' : {
                'cuts' : { 
                    'True' :
                        [
                        'muon_col[LF_idx]["pt"]             >  10.' ,
                        'abs(muon_col[LF_idx]["eta"])       <  2.4' ,
                        'muon_col[LF_idx]["looseId"]        ==   1' , 
                        'abs(muon_col[LF_idx]["sip3d"])     <   4.' ,
                        'abs(muon_col[LF_idx]["dxy"])       < 0.05' ,
                        'abs(muon_col[LF_idx]["dz"])        < 0.10' ,
                        ] ,
                    } ,    
                } ,
            } ,

        'TightObjWP' :  {

            'looseIsoVeryLoose' : {
                'cuts' : { 
                    'True' :
                        [
                        'muon_col[LF_idx]["pt"]             >  10.' ,
                        'abs(muon_col[LF_idx]["eta"])       <  2.4' ,  
                        'muon_col[LF_idx]["looseId"]        ==   1' ,
                        'abs(muon_col[LF_idx]["sip3d"])     <   4.' ,
                        'abs(muon_col[LF_idx]["dxy"])       < 0.05' ,
                        'abs(muon_col[LF_idx]["dz"])        < 0.10' ,
                        'muon_col[LF_idx]["pfIsoId"]        >=   1' , 
                        ]
                    } ,
                'tkSF':  { 
                    '1-4' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2016/trackerSF_Moriond17_MuoPOG_BCDEF.root' ,
                    '5-7' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2016/trackerSF_Moriond17_MuoPOG_GH.root' ,
                    } ,
                'tkSFerror': 0.01,
                'susySF':  {
                    '1-4' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2016v2/Muon_2016BCDEF_ID_POG.root#NUM_LooseID_DEN_genTracks_eta_pt&LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2016v2/Muon_2016BCDEF_ISO_POG.root#NUM_LooseRelIso_DEN_LooseID_eta_pt' ,
                    '5-7' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2016v2/Muon_2016GH_ID_POG.root#NUM_LooseID_DEN_genTracks_eta_pt&LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2016v2/Muon_2016GH_ISO_POG.root#NUM_LooseRelIso_DEN_LooseID_eta_pt'  , 
                     } ,
                'fsSF': {
                    '1-7' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2016v2/detailed_mu_full_fast_sf_17.root#miniIso04_LooseId_sf' , 
                    },
                },

            'looseIsoLoose' : {
                'cuts' : { 
                    'True' :
                        [
                        'muon_col[LF_idx]["pt"]             >  10.' ,
                        'abs(muon_col[LF_idx]["eta"])       <  2.4' ,  
                        'muon_col[LF_idx]["looseId"]        ==   1' ,
                        'abs(muon_col[LF_idx]["sip3d"])     <   4.' ,
                        'abs(muon_col[LF_idx]["dxy"])       < 0.05' ,
                        'abs(muon_col[LF_idx]["dz"])        < 0.10' ,
                        'muon_col[LF_idx]["pfIsoId"]        >=   2' , 
                        ]
                    } ,
                'tkSF':  { 
                    '1-4' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2016/trackerSF_Moriond17_MuoPOG_BCDEF.root' ,
                    '5-7' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2016/trackerSF_Moriond17_MuoPOG_GH.root' ,
                    } ,
                'tkSFerror': 0.01,
                'susySF':  {
                    '1-4' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2016v2/Muon_2016BCDEF_ID_POG.root#NUM_LooseID_DEN_genTracks_eta_pt&LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2016v2/Muon_2016BCDEF_ISO_POG.root#NUM_LooseRelIso_DEN_LooseID_eta_pt' ,
                    '5-7' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2016v2/Muon_2016GH_ID_POG.root#NUM_LooseID_DEN_genTracks_eta_pt&LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2016v2/Muon_2016GH_ISO_POG.root#NUM_LooseRelIso_DEN_LooseID_eta_pt'  , 
                     } ,
                'fsSF': {
                    '1-7' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2016v2/detailed_mu_full_fast_sf_17.root#miniIso04_LooseId_sf' , 
                    },
                },

            'looseMiniIsoLoose' : {
                'cuts' : { 
                    'True' :
                        [
                        'muon_col[LF_idx]["pt"]             >  10.' ,
                        'abs(muon_col[LF_idx]["eta"])       <  2.4' ,  
                        'muon_col[LF_idx]["looseId"]        ==   1' ,
                        'abs(muon_col[LF_idx]["sip3d"])     <   4.' ,
                        'abs(muon_col[LF_idx]["dxy"])       < 0.05' ,
                        'abs(muon_col[LF_idx]["dz"])        < 0.10' ,
                        'muon_col[LF_idx]["miniPFRelIso_all"] < 0.4' ,
                        ]
                    } ,
                'tkSF':  { 
                    '1-4' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2016/trackerSF_Moriond17_MuoPOG_BCDEF.root' ,
                    '5-7' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2016/trackerSF_Moriond17_MuoPOG_GH.root' ,
                    } ,
                'tkSFerror': 0.01,
                'susySF':  {
                    '1-4' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2016v2/Muon_2016BCDEF_ID_POG.root#NUM_LooseID_DEN_genTracks_eta_pt&LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2016v2/Muon_2016_NUM_MiniIsoLoose_DENOM_LooseID_SUSY.root#SF' ,
                    '5-7' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2016v2/Muon_2016GH_ID_POG.root#NUM_LooseID_DEN_genTracks_eta_pt&LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2016v2/Muon_2016_NUM_MiniIsoLoose_DENOM_LooseID_SUSY.root#SF'  , 
                     } ,
                'fsSF': {
                    '1-7' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2016v2/detailed_mu_full_fast_sf_17.root#miniIso04_LooseId_sf' , 
                    },
                },

            'mediumMiniIsoMedium' : {
                'cuts' : { 
                    'True' :
                        [
                        'muon_col[LF_idx]["pt"]             >  15.' ,
                        'abs(muon_col[LF_idx]["eta"])       <  2.4' ,  
                        'muon_col[LF_idx]["mediumId"]       ==   1' ,
                        'abs(muon_col[LF_idx]["sip3d"])     <   4.' ,
                        'abs(muon_col[LF_idx]["dxy"])       < 0.05' ,
                        'abs(muon_col[LF_idx]["dz"])        < 0.10' ,
                        'muon_col[LF_idx]["miniPFRelIso_all"] < 0.2' ,
                        ] ,
                    } ,
                'tkSF':  { 
                    '1-4' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2016/trackerSF_Moriond17_MuoPOG_BCDEF.root' ,
                    '5-7' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2016/trackerSF_Moriond17_MuoPOG_GH.root' ,
                    } ,
                'tkSFerror': 0.01,
                'susySF':  {
                    '1-4' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2016v2/Muon_2016BCDEF_ID_POG.root#NUM_MediumID_DEN_genTracks_eta_pt&LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2016v2/Muon_2016_MiniIso_SUSY.root#TnP_MC_NUM_MiniIso02Cut_DEN_MediumID_PAR_pt_eta&LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2016v2/Muon_2016_NUM_TightIP2D_DENOM_MediumID_SUSY.root#SF&LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2016v2/Muon_2016_NUM_TightIP3D_DENOM_MediumID_SUSY.root#SF' ,
                    '5-7' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2016v2/Muon_2016GH_ID_POG.root#NUM_MediumID_DEN_genTracks_eta_pt&LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2016v2/Muon_2016_MiniIso_SUSY.root#TnP_MC_NUM_MiniIso02Cut_DEN_MediumID_PAR_pt_eta&LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2016v2/Muon_2016_NUM_TightIP2D_DENOM_MediumID_SUSY.root#SF&LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2016v2/Muon_2016_NUM_TightIP3D_DENOM_MediumID_SUSY.root#SF'  , 
                     } ,
                'fsSF': {
                    '1-7' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2016v2/detailed_mu_full_fast_sf_17.root#miniIso02_MediumId_sf' , 
                    },
              } ,

            'mediumMiniIsoTight' : {
                'cuts' : { 
                    'True' :
                        [
                        'muon_col[LF_idx]["pt"]             >  15.' ,
                        'abs(muon_col[LF_idx]["eta"])       <  2.4' ,  
                        'muon_col[LF_idx]["mediumId"]       ==   1' ,
                        'abs(muon_col[LF_idx]["sip3d"])     <   4.' ,
                        'abs(muon_col[LF_idx]["dxy"])       < 0.05' ,
                        'abs(muon_col[LF_idx]["dz"])        < 0.10' ,
                        'muon_col[LF_idx]["miniPFRelIso_all"] < 0.1' ,
                        ] ,
                    } ,
                'tkSF':  { 
                    '1-4' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2016/trackerSF_Moriond17_MuoPOG_BCDEF.root' ,
                    '5-7' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2016/trackerSF_Moriond17_MuoPOG_GH.root' ,
                    } ,
                'tkSFerror': 0.01,
                'susySF':  {
                    '1-4' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2016v2/Muon_2016BCDEF_ID_POG.root#NUM_MediumID_DEN_genTracks_eta_pt&LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2016v2/Muon_2016_MiniIso_SUSY.root#TnP_MC_NUM_MiniIso02Cut_DEN_MediumID_PAR_pt_eta&LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2016v2/Muon_2016_NUM_TightIP2D_DENOM_MediumID_SUSY.root#SF&LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2016v2/Muon_2016_NUM_TightIP3D_DENOM_MediumID_SUSY.root#SF' ,
                    '5-7' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2016v2/Muon_2016GH_ID_POG.root#NUM_MediumID_DEN_genTracks_eta_pt&LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2016v2/Muon_2016_MiniIso_SUSY.root#TnP_MC_NUM_MiniIso02Cut_DEN_MediumID_PAR_pt_eta&LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2016v2/Muon_2016_NUM_TightIP2D_DENOM_MediumID_SUSY.root#SF&LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2016v2/Muon_2016_NUM_TightIP3D_DENOM_MediumID_SUSY.root#SF'  , 
                     } ,
                'fsSF': {
                    '1-7' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2016v2/detailed_mu_full_fast_sf_17.root#miniIso01_MediumId_sf' , 
                    },
              } ,

            'mediumRelIsoTight' : {
                'cuts' : { 
                    'True' :
                        [
                        'muon_col[LF_idx]["pt"]             >  15.' ,
                        'abs(muon_col[LF_idx]["eta"])       <  2.4' ,  
                        'muon_col[LF_idx]["mediumId"]       ==   1' ,
                        'abs(muon_col[LF_idx]["sip3d"])     <   4.' ,
                        'abs(muon_col[LF_idx]["dxy"])       < 0.05' ,
                        'abs(muon_col[LF_idx]["dz"])        < 0.10' ,
                        'muon_col[LF_idx]["pfRelIso04_all"] < 0.15' , 
                        ] ,
                    } ,
                'tkSF':  { 
                    '1-4' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2016/trackerSF_Moriond17_MuoPOG_BCDEF.root' ,
                    '5-7' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2016/trackerSF_Moriond17_MuoPOG_GH.root' ,
                    } ,
                'tkSFerror': 0.01,
                'susySF':  {
                    '1-4' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2016v2/Muon_2016BCDEF_ID_POG.root#NUM_MediumID_DEN_genTracks_eta_pt&LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2016v2/Muon_2016BCDEF_ISO_POG.root#NUM_TightRelIso_DEN_MediumID_eta_pt&LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2016v2/Muon_2016_NUM_TightIP2D_DENOM_MediumID_SUSY.root#SF&LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2016v2/Muon_2016_NUM_TightIP3D_DENOM_MediumID_SUSY.root#SF' ,
                    '5-7' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2016v2/Muon_2016GH_ID_POG.root#NUM_MediumID_DEN_genTracks_eta_pt&LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2016v2/Muon_2016GH_ISO_POG.root#NUM_TightRelIso_DEN_MediumID_eta_pt&LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2016v2/Muon_2016_NUM_TightIP2D_DENOM_MediumID_SUSY.root#SF&LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2016v2/Muon_2016_NUM_TightIP3D_DENOM_MediumID_SUSY.root#SF' , 
                     } ,
                'fsSF': {
                    '1-7' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2016v2/detailed_mu_full_fast_sf_17.root#miniIso01_MediumId_sf' , 
                    },
                #'fakeW' : '/LatinoAnalysis/Gardener/python/data/fake_prompt_rates/80X/lowPtCorrected/36fb_muon/' ,
              } ,

        } ,
        
        'WgStarObjWP' : {
            'null' : { 
                'cuts' : { 
                    'True' :
                    [
                        'False' ,
                    ] ,
                } ,
            } ,
        }, 
        
    },

    'Full2017v7': {

        'VetoObjWP' : { 
            'loosenoiso' : {
                'cuts' : { 
                    'True' :
                        [
                        'muon_col[LF_idx]["pt"]             >  10.' ,
                        'abs(muon_col[LF_idx]["eta"])       <  2.4' , 
                        'muon_col[LF_idx]["looseId"]        ==   1' , 
                        'abs(muon_col[LF_idx]["sip3d"])     <   4.' ,
                        'abs(muon_col[LF_idx]["dxy"])       < 0.05' ,
                        'abs(muon_col[LF_idx]["dz"])        < 0.10' ,
                        ]
                    } ,
                }
            } ,
        
        'FakeObjWP'  : {
            'loosenoiso' : {
                'cuts' : { 
                    'True' :
                        [
                        'muon_col[LF_idx]["pt"]             >  10.' ,
                        'abs(muon_col[LF_idx]["eta"])       <  2.4' , 
                        'muon_col[LF_idx]["looseId"]        ==   1' , 
                        'abs(muon_col[LF_idx]["sip3d"])     <   4.' ,
                        'abs(muon_col[LF_idx]["dxy"])       < 0.05' ,
                        'abs(muon_col[LF_idx]["dz"])        < 0.10' ,
                        ] ,
                    } ,    
                } ,
            } ,

        'TightObjWP' :  {

            'looseIsoVeryLoose' : {
                'cuts' : { 
                    'True' :
                        [
                        'muon_col[LF_idx]["pt"]             >  10.' ,
                        'abs(muon_col[LF_idx]["eta"])       <  2.4' ,  
                        'muon_col[LF_idx]["looseId"]        ==   1' ,
                        'abs(muon_col[LF_idx]["sip3d"])     <   4.' ,
                        'abs(muon_col[LF_idx]["dxy"])       < 0.05' ,
                        'abs(muon_col[LF_idx]["dz"])        < 0.10' ,
                        'muon_col[LF_idx]["pfIsoId"]        >=   1' , 
                        ]
                    } ,
                'susySF':  {
                    '1-5' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/RunBCDEF_SF_ID_syst.root#NUM_LooseID_DEN_genTracks_pt_abseta&LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/RunBCDEF_SF_ISO_syst.root#NUM_LooseRelIso_DEN_LooseID_pt_abseta' ,
                     } ,
                'fsSF': {
                    '1-5' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/detailed_mu_full_fast_sf_17.root#miniIso04_LooseId_sf' , 
                    },
                },

            'looseIsoLoose' : {
                'cuts' : { 
                    'True' :
                        [
                        'muon_col[LF_idx]["pt"]             >  10.' ,
                        'abs(muon_col[LF_idx]["eta"])       <  2.4' ,  
                        'muon_col[LF_idx]["looseId"]        ==   1' ,
                        'abs(muon_col[LF_idx]["sip3d"])     <   4.' ,
                        'abs(muon_col[LF_idx]["dxy"])       < 0.05' ,
                        'abs(muon_col[LF_idx]["dz"])        < 0.10' ,
                        'muon_col[LF_idx]["pfIsoId"]        >=   2' , 
                        ]
                    } ,
                'susySF':  {
                    '1-5' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/RunBCDEF_SF_ID_syst.root#NUM_LooseID_DEN_genTracks_pt_abseta&LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/RunBCDEF_SF_ISO_syst.root#NUM_LooseRelIso_DEN_LooseID_pt_abseta' ,
                     } ,
                'fsSF': {
                    '1-5' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/detailed_mu_full_fast_sf_17.root#miniIso04_LooseId_sf' , 
                    },
                },

            'looseMiniIsoLoose' : {
                'cuts' : { 
                    'True' :
                        [
                        'muon_col[LF_idx]["pt"]             >  10.' ,
                        'abs(muon_col[LF_idx]["eta"])       <  2.4' ,  
                        'muon_col[LF_idx]["looseId"]        ==   1' ,
                        'abs(muon_col[LF_idx]["sip3d"])     <   4.' ,
                        'abs(muon_col[LF_idx]["dxy"])       < 0.05' ,
                        'abs(muon_col[LF_idx]["dz"])        < 0.10' ,
                        'muon_col[LF_idx]["miniPFRelIso_all"] < 0.4' ,
                        ]
                    } ,
                'susySF':  {
                    '1-5' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/RunBCDEF_SF_ID_syst.root#NUM_LooseID_DEN_genTracks_pt_abseta&LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/Muon_2017_NUM_MiniIso04Cut_DEN_LooseID_SUSY.root#TnP_MC_NUM_MiniIso04Cut_DEN_LooseID_PAR_pt_eta' ,
                     } ,
                'fsSF': {
                    '1-5' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/detailed_mu_full_fast_sf_17.root#miniIso04_LooseId_sf' , 
                    },
                },

            'mediumMiniIsoMedium' : {
                'cuts' : { 
                    'True' :
                        [
                        'muon_col[LF_idx]["pt"]             >  15.' ,
                        'abs(muon_col[LF_idx]["eta"])       <  2.4' ,  
                        'muon_col[LF_idx]["mediumId"]       ==   1' ,
                        'abs(muon_col[LF_idx]["sip3d"])     <   4.' ,
                        'abs(muon_col[LF_idx]["dxy"])       < 0.05' ,
                        'abs(muon_col[LF_idx]["dz"])        < 0.10' ,
                        'muon_col[LF_idx]["miniPFRelIso_all"] < 0.2' ,
                        ] ,
                    } ,
                'susySF':  {
                    '1-5' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/RunBCDEF_SF_ID_syst.root#NUM_MediumID_DEN_genTracks_pt_abseta&LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/Muon_2017_NUM_MiniIso02Cut_DEN_MediumID_SUSY.root#TnP_MC_NUM_MiniIso02Cut_DEN_MediumID_PAR_pt_eta' ,
                     } ,
                'fsSF': {
                    '1-5' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/detailed_mu_full_fast_sf_17.root#miniIso02_MediumId_sf' , 
                    },
              } ,

            'mediumMiniIsoTight' : {
                'cuts' : { 
                    'True' :
                        [
                        'muon_col[LF_idx]["pt"]             >  15.' ,
                        'abs(muon_col[LF_idx]["eta"])       <  2.4' ,  
                        'muon_col[LF_idx]["mediumId"]       ==   1' ,
                        'abs(muon_col[LF_idx]["sip3d"])     <   4.' ,
                        'abs(muon_col[LF_idx]["dxy"])       < 0.05' ,
                        'abs(muon_col[LF_idx]["dz"])        < 0.10' ,
                        'muon_col[LF_idx]["miniPFRelIso_all"] < 0.1' ,
                        ] ,
                    } ,
                'susySF':  {
                    '1-5' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/RunBCDEF_SF_ID_syst.root#NUM_MediumID_DEN_genTracks_pt_abseta&LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/Muon_2017_NUM_MiniIso02Cut_DEN_MediumID_SUSY.root#TnP_MC_NUM_MiniIso02Cut_DEN_MediumID_PAR_pt_eta' ,
                     } ,
                'fsSF': {
                    '1-5' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/detailed_mu_full_fast_sf_17.root#miniIso01_MediumId_sf' , 
                    },
              } ,

            'mediumRelIsoTight' : {
                'cuts' : { 
                    'True' :
                        [
                        'muon_col[LF_idx]["pt"]             >  15.' ,
                        'abs(muon_col[LF_idx]["eta"])       <  2.4' ,  
                        'muon_col[LF_idx]["mediumId"]       ==   1' ,
                        'abs(muon_col[LF_idx]["sip3d"])     <   4.' ,
                        'abs(muon_col[LF_idx]["dxy"])       < 0.05' ,
                        'abs(muon_col[LF_idx]["dz"])        < 0.10' ,
                        'muon_col[LF_idx]["pfRelIso04_all"] < 0.15' , 
                        ] ,
                    } ,
                'susySF':  {
                    '1-5' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/RunBCDEF_SF_ID_syst.root#NUM_MediumID_DEN_genTracks_pt_abseta&LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/RunBCDEF_SF_ISO_syst.root#NUM_TightRelIso_DEN_MediumID_pt_abseta' ,
                     } ,
                'fsSF': {
                    '1-5' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/detailed_mu_full_fast_sf_17.root#miniIso01_MediumId_sf' , 
                    },
              } ,
            
         } ,
        
        'WgStarObjWP' : {
            'null' : { 
                'cuts' : { 
                    'True' :
                    [
                        'False' ,
                    ] ,
                } ,
            } ,
        }, 

    },

    'Full2018v7': {

        'VetoObjWP' : { 
            'loosenoiso' : {
                'cuts' : { 
                    'True' :
                        [
                        'muon_col[LF_idx]["pt"]             >  10.' ,
                        'abs(muon_col[LF_idx]["eta"])       <  2.4' , 
                        'muon_col[LF_idx]["looseId"]        ==   1' ,
                        'abs(muon_col[LF_idx]["sip3d"])     <   4.' , 
                        'abs(muon_col[LF_idx]["dxy"])       < 0.05' ,
                        'abs(muon_col[LF_idx]["dz"])        < 0.10' ,
                        ]
                    } ,
                }
            } ,
        
        'FakeObjWP'  : {
            'loosenoiso' : {
                'cuts' : { 
                    'True' :
                        [
                        'muon_col[LF_idx]["pt"]             >  10.' ,
                        'abs(muon_col[LF_idx]["eta"])       <  2.4' , 
                        'muon_col[LF_idx]["looseId"]        ==   1' , 
                        'abs(muon_col[LF_idx]["sip3d"])     <   4.' ,
                        'abs(muon_col[LF_idx]["dxy"])       < 0.05' ,
                        'abs(muon_col[LF_idx]["dz"])        < 0.10' , 
                        ] ,
                    } ,    
                } ,
            } ,

        'TightObjWP' :  {

            'looseIsoVeryLoose' : {
                'cuts' : { 
                    'True' :
                        [
                        'muon_col[LF_idx]["pt"]             >  10.' ,
                        'abs(muon_col[LF_idx]["eta"])       <  2.4' ,  
                        'muon_col[LF_idx]["looseId"]        ==   1' ,
                        'abs(muon_col[LF_idx]["sip3d"])     <   4.' ,
                        'abs(muon_col[LF_idx]["dxy"])       < 0.05' ,
                        'abs(muon_col[LF_idx]["dz"])        < 0.10' ,
                        'muon_col[LF_idx]["pfIsoId"]        >=   1' , 
                        ]
                    } ,
                'susySF':  {
                    '1-1' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2018/RunABCD_SF_ID.root#NUM_LooseID_DEN_TrackerMuons_pt_abseta&LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/RunABCD_SF_ISO.root#NUM_LooseRelIso_DEN_LooseID_pt_abseta' ,
                     } ,
                'fsSF': {
                    '1-1' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2018/detailed_mu_full_fast_sf_18.root#miniIso04_LooseId_sf' , 
                    },
                },

            'looseIsoLoose' : {
                'cuts' : { 
                    'True' :
                        [
                        'muon_col[LF_idx]["pt"]             >  10.' ,
                        'abs(muon_col[LF_idx]["eta"])       <  2.4' ,  
                        'muon_col[LF_idx]["looseId"]        ==   1' ,
                        'abs(muon_col[LF_idx]["sip3d"])     <   4.' ,
                        'abs(muon_col[LF_idx]["dxy"])       < 0.05' ,
                        'abs(muon_col[LF_idx]["dz"])        < 0.10' ,
                        'muon_col[LF_idx]["pfIsoId"]        >=   2' , 
                        ]
                    } ,
                'susySF':  {
                    '1-1' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2018/RunABCD_SF_ID.root#NUM_LooseID_DEN_TrackerMuons_pt_abseta&LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/RunABCD_SF_ISO.root#NUM_LooseRelIso_DEN_LooseID_pt_abseta' ,
                     } ,
                'fsSF': {
                    '1-1' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2018/detailed_mu_full_fast_sf_18.root#miniIso04_LooseId_sf' , 
                    },
                },

            'looseMiniIsoLoose' : {
                'cuts' : { 
                    'True' :
                        [
                        'muon_col[LF_idx]["pt"]             >  10.' ,
                        'abs(muon_col[LF_idx]["eta"])       <  2.4' ,  
                        'muon_col[LF_idx]["looseId"]        ==   1' ,
                        'abs(muon_col[LF_idx]["sip3d"])     <   4.' ,
                        'abs(muon_col[LF_idx]["dxy"])       < 0.05' ,
                        'abs(muon_col[LF_idx]["dz"])        < 0.10' ,
                        'muon_col[LF_idx]["miniPFRelIso_all"] < 0.4' ,
                        ]
                    } ,
                'susySF':  {
                    '1-1' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2018/RunABCD_SF_ID.root#NUM_LooseID_DEN_TrackerMuons_pt_abseta&LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/Muon_2017_NUM_MiniIso04Cut_DEN_LooseID_SUSY.root#TnP_MC_NUM_MiniIso04Cut_DEN_LooseID_PAR_pt_eta' ,
                     } ,
                'fsSF': {
                    '1-1' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2018/detailed_mu_full_fast_sf_18.root#miniIso04_LooseId_sf' , 
                    },
                },

            'mediumMiniIsoMedium' : {
                'cuts' : { 
                    'True' :
                        [
                        'muon_col[LF_idx]["pt"]             >  15.' ,
                        'abs(muon_col[LF_idx]["eta"])       <  2.4' ,  
                        'muon_col[LF_idx]["mediumId"]       ==   1' ,
                        'abs(muon_col[LF_idx]["sip3d"])     <   4.' ,
                        'abs(muon_col[LF_idx]["dxy"])       < 0.05' ,
                        'abs(muon_col[LF_idx]["dz"])        < 0.10' ,
                        'muon_col[LF_idx]["miniPFRelIso_all"] < 0.2' ,
                        ] ,
                    } ,
                'susySF':  {
                    '1-1' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2018/RunABCD_SF_ID.root#NUM_MediumID_DEN_TrackerMuons_pt_abseta&LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/Muon_2017_NUM_MiniIso02Cut_DEN_MediumID_SUSY.root#TnP_MC_NUM_MiniIso02Cut_DEN_MediumID_PAR_pt_eta' ,
                     } ,
                'fsSF': {
                    '1-1' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2018/detailed_mu_full_fast_sf_18.root#miniIso02_MediumId_sf' , 
                    },
              } ,

            'mediumMiniIsoTight' : {
                'cuts' : { 
                    'True' :
                        [
                        'muon_col[LF_idx]["pt"]             >  15.' ,
                        'abs(muon_col[LF_idx]["eta"])       <  2.4' ,  
                        'muon_col[LF_idx]["mediumId"]       ==   1' ,
                        'abs(muon_col[LF_idx]["sip3d"])     <   4.' ,
                        'abs(muon_col[LF_idx]["dxy"])       < 0.05' ,
                        'abs(muon_col[LF_idx]["dz"])        < 0.10' ,
                        'muon_col[LF_idx]["miniPFRelIso_all"] < 0.1' ,
                        ] ,
                    } ,
                'susySF':  {
                    '1-1' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2018/RunABCD_SF_ID.root#NUM_MediumID_DEN_TrackerMuons_pt_abseta&LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2017/Muon_2017_NUM_MiniIso02Cut_DEN_MediumID_SUSY.root#TnP_MC_NUM_MiniIso02Cut_DEN_MediumID_PAR_pt_eta' ,
                     } ,
                'fsSF': {
                    '1-1' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2018/detailed_mu_full_fast_sf_18.root#miniIso01_MediumId_sf' , 
                    },
              } ,

            'mediumRelIsoTight' : {
                'cuts' : { 
                    'True' :
                        [
                        'muon_col[LF_idx]["pt"]             >  15.' ,
                        'abs(muon_col[LF_idx]["eta"])       <  2.4' ,  
                        'muon_col[LF_idx]["mediumId"]       ==   1' ,
                        'abs(muon_col[LF_idx]["sip3d"])     <   4.' ,
                        'abs(muon_col[LF_idx]["dxy"])       < 0.05' ,
                        'abs(muon_col[LF_idx]["dz"])        < 0.10' ,
                        'muon_col[LF_idx]["pfRelIso04_all"] < 0.15' , 
                        ] ,
                    } ,
                'susySF':  {
                    '1-1' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2018/RunABCD_SF_ID.root#NUM_MediumID_DEN_TrackerMuons_pt_abseta&LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2018/RunABCD_SF_ISO.root#NUM_TightRelIso_DEN_MediumID_pt_abseta' ,
                     } ,
                'fsSF': {
                    '1-1' : 'LatinoAnalysis/NanoGardener/python/data/scale_factor/Full2018/detailed_mu_full_fast_sf_18.root#miniIso01_MediumId_sf' , 
                    },
              } ,
            
         } ,
        
        'WgStarObjWP' : {
            'null' : {
                'cuts' : { 
                    'True' :
                    [
                        'False' ,
                    ] ,
                } ,
            } ,
        }, 

    },
    
}

MuonWP['Full2016v6'] = MuonWP['Full2016v4']
MuonWP['Full2017v6'] = MuonWP['Full2017v4']
MuonWP['Full2018v6'] = MuonWP['Full2018v4']

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

