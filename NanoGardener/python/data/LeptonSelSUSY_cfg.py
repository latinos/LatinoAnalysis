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

            'cutBasedMedium' : {
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
                    '1-7' : 'LatinoAnalysis/Gardener/python/data/idiso/Full2016/egammaEffi.txt_EGM2D.root' ,
                    } ,
                'wpSF':  {
                    '1-7' : 'LatinoAnalysis/Gardener/python/data/idiso/Full2016/electrons_cut_WP_Tight80X.txt' ,  
                    } ,
                'fakeW' : '/LatinoAnalysis/Gardener/python/data/fake_prompt_rates/80X/lowPtCorrected/36fb_ele_cut_WP_Tight80X/' ,
                } ,

            'cutBasedTight' : {
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
                    '1-7' : 'LatinoAnalysis/Gardener/python/data/idiso/Full2016/egammaEffi.txt_EGM2D.root' ,
                    } ,
                'wpSF':  {
                    '1-7' : 'LatinoAnalysis/Gardener/python/data/idiso/Full2016/electrons_cut_WP_Tight80X.txt' ,  
                    } ,
                'fakeW' : '/LatinoAnalysis/Gardener/python/data/fake_prompt_rates/80X/lowPtCorrected/36fb_ele_cut_WP_Tight80X/' ,
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
                    '1-7' : 'LatinoAnalysis/Gardener/python/data/idiso/Full2016/egammaEffi.txt_EGM2D.root' ,
                    } ,
                'wpSF':  {
                    '1-7' : 'LatinoAnalysis/Gardener/python/data/idiso/Full2016/electrons_cut_WP_Tight80X.txt' ,  
                    } ,
                'fakeW' : '/LatinoAnalysis/Gardener/python/data/fake_prompt_rates/80X/lowPtCorrected/36fb_ele_cut_WP_Tight80X/' ,
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
                    '1-7' : 'LatinoAnalysis/Gardener/python/data/idiso/Full2016/egammaEffi.txt_EGM2D.root' ,
                    } ,
                'wpSF':  {
                    '1-7' : 'LatinoAnalysis/Gardener/python/data/idiso/Full2016/electrons_cut_WP_Tight80X.txt' ,  
                    } ,
                'fakeW' : '/LatinoAnalysis/Gardener/python/data/fake_prompt_rates/80X/lowPtCorrected/36fb_ele_cut_WP_Tight80X/' ,
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
                    '1-7' : 'LatinoAnalysis/Gardener/python/data/idiso/Full2016/egammaEffi.txt_EGM2D.root' ,
                    } ,
                'wpSF':  {
                    '1-7' : 'LatinoAnalysis/Gardener/python/data/idiso/Full2016/electrons_cut_WP_Tight80X.txt' ,  
                    } ,
                'fakeW' : '/LatinoAnalysis/Gardener/python/data/fake_prompt_rates/80X/lowPtCorrected/36fb_ele_cut_WP_Tight80X/' ,
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
                        'abs(muon_col[LF_idx]["sip3d"])     <   4.' ,
                        'abs(muon_col[LF_idx]["dxy"])       < 0.05' ,
                        'abs(muon_col[LF_idx]["dz"])        < 0.10' ,
                        #'muon_col[LF_idx]["pfRelIso03_all"] < 0.40' , # SUS-17-010
                        'muon_col[LF_idx]["miniIsoId"] >= 1' ,
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
                        'abs(muon_col[LF_idx]["sip3d"])     <   4.' ,
                        'abs(muon_col[LF_idx]["dxy"])       < 0.05' ,
                        'abs(muon_col[LF_idx]["dz"])        < 0.10' ,
                        #'muon_col[LF_idx]["pfRelIso03_all"] < 0.40' , # SUS-17-010
                        'muon_col[LF_idx]["miniIsoId"] >= 1' ,
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
                'fakeW' : '/LatinoAnalysis/Gardener/python/data/fake_prompt_rates/80X/lowPtCorrected/36fb_muon/' ,
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
                'fakeW' : '/LatinoAnalysis/Gardener/python/data/fake_prompt_rates/80X/lowPtCorrected/36fb_muon/' ,
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

