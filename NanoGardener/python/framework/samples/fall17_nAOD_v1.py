'''
Samples = {
              'GluGluHToWWTo2L2Nu_M125' : {
                   'dasInst' : 'prod/global'  ,
                   'nanoAOD' : '/GluGluHToWWTo2L2Nu_M125_13TeV_powheg_pythia8/RunIISummer16NanoAOD-PUMoriond17_05Feb2018_94X_mcRun2_asymptotic_v2-v1/NANOAODSIM' ,
                                          } ,

              'GluGluHToWWTo2L2Nu_M125_Crab' : {
                   'dasInst' : 'prod/global'  ,
                   'nanoAOD' : '/GluGluHToWWTo2L2Nu_M125_13TeV_powheg_pythia8/RunIISummer16NanoAOD-PUMoriond17_05Feb2018_94X_mcRun2_asymptotic_v2-v1/NANOAODSIM' ,
                                          } ,

               'GluGluHToWWTo2L2Nu_M125_Private' : {
                    'dasInst' : 'prod/phys03'  ,
                    'nanoAOD' : '/GluGluHToWWTo2L2Nu_M125_13TeV_powheg_pythia8/ddicroce-GluGluHToWWTo2L2Nu_M125_13TeV_powheg_pythia8_nAOD_private-60fc7d9153a3c626dca414ab6cce3b8f/USER',
                                           } ,

 }
'''

Samples = {}

### Wg
#Samples['WGJJ']           = {'nanoAOD' :'/WGJJToLNu_EWK_QCD_TuneCUETP8M1_13TeV-madgraph-pythia8/RunIISummer16NanoAOD-PUMoriond17_05Feb2018_94X_mcRun2_asymptotic_v2-v1/NANOAODSIM'}
Samples['Wg_AMCNLOFXFX']  = {'nanoAOD' :'/WGToLNuG_01J_5f_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIIFall17NanoAOD-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/NANOAODSIM'}

Samples['WZTo3LNu']       = {'nanoAOD' :'/WZTo3LNu_mllmin01_NNPDF31_TuneCP5_13TeV_powheg_pythia8/RunIIFall17NanoAOD-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/NANOAODSIM'} #not yet valid
Samples['ZZTo4L']         = {'nanoAOD' :'/ZZTo4L_13TeV_powheg_pythia8/RunIIFall17NanoAOD-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/NANOAODSIM'}
#Samples['WWTo2L2Nu_DoubleScattering'] = {'nanoAOD' :'new in mcm'}

### QCD fakes
#Samples['QCD_Pt_20to30_bcToE']             = {'nanoAOD' :'new in mcm'}
Samples['QCD_Pt_30to80_bcToE']             = {'nanoAOD' :'/QCD_Pt_30to80_bcToE_TuneCP5_13TeV_pythia8/RunIIFall17NanoAOD-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/NANOAODSIM'}
Samples['QCD_Pt_80to170_bcToE']            = {'nanoAOD' :'/QCD_Pt_80to170_bcToE_TuneCP5_13TeV_pythia8/RunIIFall17NanoAOD-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/NANOAODSIM'}
Samples['QCD_Pt_170to250_bcToE']           = {'nanoAOD' :'/QCD_Pt_170to250_bcToE_TuneCP5_13TeV_pythia8/RunIIFall17NanoAOD-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/NANOAODSIM'}
Samples['QCD_Pt_250toInf_bcToE']           = {'nanoAOD' :'/QCD_Pt_250toInf_bcToE_TuneCP5_13TeV_pythia8/RunIIFall17NanoAOD-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/NANOAODSIM'}
Samples['QCD_Pt-15to20_MuEnrichedPt5']     = {'nanoAOD' :'/QCD_Pt-15to20_MuEnrichedPt5_TuneCP5_13TeV_pythia8/RunIIFall17NanoAOD-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/NANOAODSIM'}
#Samples['QCD_Pt-20toInf_MuEnrichedPt15']   = {'nanoAOD' :'new in mcm'} 
Samples['QCD_Pt-20to30_EMEnriched']        = {'nanoAOD' :'/QCD_Pt-20to30_EMEnriched_TuneCP5_13TeV_pythia8/RunIIFall17NanoAOD-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/NANOAODSIM'}
Samples['QCD_Pt-30to50_EMEnriched']        = {'nanoAOD' :'/QCD_Pt-30to50_EMEnriched_TuneCP5_13TeV_pythia8/RunIIFall17NanoAOD-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/NANOAODSIM'} 
Samples['QCD_Pt-50to80_EMEnriched']        = {'nanoAOD' :'/QCD_Pt-50to80_EMEnriched_TuneCP5_13TeV_pythia8/RunIIFall17NanoAOD-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/NANOAODSIM'} 
Samples['QCD_Pt-30toInf_DoubleEMEnriched'] = {'nanoAOD' :'/QCD_Pt-30toInf_DoubleEMEnriched_MGG-40to80_TuneCP5_13TeV_Pythia8/RunIIFall17NanoAOD-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/NANOAODSIM'}

#signals not yet available
#Samples['VBFHToWWTo2L2Nu_M125']         = {'nanoAOD' :'/VBFHToWWTo2L2Nu_M125_13TeV_powheg_JHUgenv628_pythia8/RunIISummer16NanoAOD-PUMoriond17_05Feb2018_94X_mcRun2_asymptotic_v2-v1/NANOAODSIM'}
Samples['VBFHToWWTo2L2NuPowheg_M125_private']   = {'dasInst' : 'prod/phys03', 'nanoAOD' :'/VBFHToWWTo2L2Nu_M125_13TeV_powheg_JHUGen_pythia8/lenzip-2018May8_nanoAOD-15956cec181df673a06b972feb245baa/USER'}
#Samples['VBFHToWWTo2L2NuAMCNLO_M125']   = {'nanoAOD' :'/VBFHToWWTo2L2Nu_M125_13TeV_amcatnlo_pythia8/RunIISummer16NanoAOD-PUMoriond17_05Feb2018_94X_mcRun2_asymptotic_v2-v1/NANOAODSIM'}
#Samples['VBFHToWWTo2L2NuHerwigPS_M125'] = {'nanoAOD' :'/VBFHToWWTo2L2Nu_M125_13TeV_powheg_JHUgen_herwigpp/RunIISummer16NanoAOD-PUMoriond17_05Feb2018_94X_mcRun2_asymptotic_v2-v1/NANOAODSIM'}
Samples['VBFHToTauTau_M125']            = {'nanoAOD' :'/VBFHToTauTau_M125_13TeV_powheg_pythia8/RunIIFall17NanoAOD-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/NANOAODSIM'}
#Samples['VBFHToWWTo2L2Nu_M125_herwigpp'] = {'nanoAOD' :'/VBFHToWWTo2L2Nu_M125_13TeV_powheg_JHUgen_herwigpp/RunIISummer16NanoAOD-PUMoriond17_05Feb2018_94X_mcRun2_asymptotic_v2-v1/NANOAODSIM'}
#Samples['VBFHToWWTo2L2Nu_M125_CUETDown'] = {'nanoAOD' :'/VBFHToWWTo2L2Nu_M125_13TeV_powheg_JHUgen_pythia8-CUETP8M1Down/RunIISummer16NanoAOD-PUMoriond17_05Feb2018_94X_mcRun2_asymptotic_v2-v1/NANOAODSIM'}
#Samples['VBFHToWWTo2L2Nu_M125_CUETUp']   = {'nanoAOD' :'/VBFHToWWTo2L2Nu_M125_13TeV_powheg_JHUgen_pythia8-CUETP8M1Up/RunIISummer16NanoAOD-PUMoriond17_05Feb2018_94X_mcRun2_asymptotic_v2-v1/NANOAODSIM'}
#Samples['ggZH_HToWW_M125']      = {'nanoAOD' :'/GluGluZH_HToWW_M125_13TeV_powheg_pythia8/RunIISummer16NanoAOD-PUMoriond17_05Feb2018_94X_mcRun2_asymptotic_v2-v1/NANOAODSIM'}
Samples['HZJ_HToTauTau_M125'] = {'nanoAOD' :'/ZHToTauTau_M125_13TeV_powheg_pythia8/RunIIFall17NanoAOD-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/NANOAODSIM'}
#Samples['GluGluHToWWTo2L2Nu_M125']       = {'nanoAOD' :'/GluGluHToWWTo2L2Nu_M125_13TeV_powheg_JHUgenv628_pythia8/RunIISummer16NanoAOD-PUMoriond17_05Feb2018_94X_mcRun2_asymptotic_v2-v1/NANOAODSIM'}
#Samples['GluGluHToWWTo2L2NuAMCNLO_M125'] = {'nanoAOD' :'/GluGluHToWWTo2L2Nu_M125_13TeV_amcatnloFXFX_pythia8/RunIISummer16NanoAOD-PUMoriond17_05Feb2018_94X_mcRun2_asymptotic_v2-v1/NANOAODSIM'}
Samples['GluGluHToWWTo2L2NuPowheg_M125_private'] = {'dasInst' : 'prod/phys03', 'nanoAOD' :'/GluGluHToWWTo2L2Nu_M125_13TeV_powheg_JHUGen_pythia8/lenzip-2018May9_nanoAOD-15956cec181df673a06b972feb245baa/USER'}
Samples['GluGluHToTauTau_M125']          = {'nanoAOD' :'/GluGluHToTauTau_M125_13TeV_powheg_pythia8/RunIIFall17NanoAOD-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/NANOAODSIM'}
#Samples['GluGluHToWWTo2L2Nu_M125_herwigpp'] = {'nanoAOD' :'/GluGluHToWWTo2L2Nu_M125_13TeV_powheg_JHUgen_herwigpp/RunIISummer16NanoAOD-PUMoriond17_05Feb2018_94X_mcRun2_asymptotic_v2-v1/NANOAODSIM'}
#Samples['GluGluHToWWTo2L2Nu_M125_CUETDown'] = {'nanoAOD' :'/GluGluHToWWTo2L2Nu_M125_13TeV_powheg_JHUgen_pythia8-CUETP8M1Down/RunIISummer16NanoAOD-PUMoriond17_05Feb2018_94X_mcRun2_asymptotic_v2-v1/NANOAODSIM'}
#Samples['GluGluHToWWTo2L2Nu_M125_CUETUp']   = {'nanoAOD' :'/GluGluHToWWTo2L2Nu_M125_13TeV_powheg_JHUgen_pythia8-CUETP8M1Up/RunIISummer16NanoAOD-PUMoriond17_05Feb2018_94X_mcRun2_asymptotic_v2-v1/NANOAODSIM'}
#Samples['GluGluHToWWTo2L2Nu_minloHJJ_M125'] = {'nanoAOD' :'/GluGluHToWWTo2L2Nu_M125_13TeV_powheg2_minloHJJ_JHUGenV702_pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v5/NANOCHECKAODSIM'} 

Samples['WWW']  = {'nanoAOD' :'/WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8/RunIIFall17NanoAOD-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/NANOAODSIM'}
Samples['WWZ']  = {'nanoAOD' :'/WWZ_4F_TuneCP5_13TeV-amcatnlo-pythia8/RunIIFall17NanoAOD-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/NANOAODSIM'}
Samples['WZZ']  = {'nanoAOD' :'/WZZ_TuneCP5_13TeV-amcatnlo-pythia8/RunIIFall17NanoAOD-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/NANOAODSIM'}
Samples['ZZZ']  = {'nanoAOD' :'/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/RunIIFall17NanoAOD-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/NANOAODSIM'}
Samples['WWG']  = {'nanoAOD' :'/WWG_TuneCP5_13TeV-amcatnlo-pythia8/RunIIFall17NanoAOD-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/NANOAODSIM'}

#Samples['Wg_MADGRAPHMLM']      = {'nanoAOD' :'not available'}
#Samples['WgStarLNuEE'] = {'nanoAOD' :'not available'}
#Samples['WgStarLNuMuMu'] = {'nanoAOD' :'not available'}

Samples['WWTo2L2Nu']    = {'nanoAOD': '/WWTo2L2Nu_NNPDF31_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIIFall17NanoAOD-PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/NANOAODSIM'}  
Samples['WW-LO']        = {'nanoAOD' :'/WW_TuneCP5_13TeV-pythia8/RunIIFall17NanoAOD-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/NANOAODSIM'}
#Samples['WWTo2L2NuHerwigPS']    = {'nanoAOD' :'needed with PS weights?'}
#Samples['WWTo2L2Nu_CP5Up']      = {'nanoAOD' :'new in mcm'}
#Samples['WWTo2L2Nu_CP5Down']    = {'nanoAOD' :'new in mcm'}
#Samples['GluGluWWTo2L2Nu_MCFM']      = {'nanoAOD' :'missing, production problems with mcfm'}


#Samples['Zg']      = {'nanoAOD' :'not available'}

#### WZ
Samples['WZ']          = {'nanoAOD' :'/WZ_TuneCP5_13TeV-pythia8/RunIIFall17NanoAOD-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/NANOAODSIM'}
#Samples['WZTo2L2Q']    = {'nanoAOD' :'new in mcm'}

## TTbar
Samples['TTTo2L2Nu'] = {'nanoAOD' :'/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/RunIIFall17NanoAOD-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/NANOAODSIM'}

## DY and W + jets
Samples['DYJetsToLL_M-5to50-LO']   = {'nanoAOD' :'/DYJetsToLL_M-5to50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17NanoAOD-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/NANOAODSIM'} # not yet valid
Samples['DYJetsToLL_M-50-LO-ext1'] = {'nanoAOD' :'/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17NanoAOD-PU2017RECOSIMstep_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/NANOAODSIM'}
Samples['DYJetsToLL_M-10to50']     = {'nanoAOD' :'/DYJetsToLL_M-50_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIIFall17NanoAOD-PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/NANOAODSIM'} 
#Samples['DYJetsToLL_M-50']         = {'nanoAOD' :'new in mcm'} 
Samples['WJetsToLNu-LO']            = {'nanoAOD' :'/WJetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17NanoAOD-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/NANOAODSIM'}


Samples['ST_t-channel_top']     = {'nanoAOD' :'/ST_t-channel_top_4f_inclusiveDecays_TuneCP5_13TeV-powhegV2-madspin-pythia8/RunIIFall17NanoAOD-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/NANOAODSIM'}
Samples['ST_t-channel_antitop'] = {'nanoAOD' :'/ST_t-channel_antitop_4f_inclusiveDecays_TuneCP5_13TeV-powhegV2-madspin-pythia8/RunIIFall17NanoAOD-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/NANOAODSIM'}
Samples['ST_tW_top']            = {'nanoAOD' :'/ST_tW_top_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/RunIIFall17NanoAOD-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/NANOAODSIM'}
Samples['ST_tW_antitop']        = {'nanoAOD' :'/ST_tW_antitop_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/RunIIFall17NanoAOD-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/NANOAODSIM'}
Samples['ST_s-channel']         = {'nanoAOD' :'/ST_s-channel_4f_leptonDecays_TuneCP5_13TeV-amcatnlo-pythia8/RunIIFall17NanoAOD-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/NANOAODSIM'}

Samples['ZZ']         = {'nanoAOD' :'/ZZ_TuneCP5_13TeV-pythia8/RunIIFall17NanoAOD-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/NANOAODSIM'}
#Samples['ZZTo2L2Q']   = {'nanoAOD' :'new in mcm'}
#Samples['ZZTo2L2Nu']  = {'nanoAOD' :'new in mcm'}

### WH Exclusive

#Samples['HWminusJ_HToWW_LNu_M125']     = {'nanoAOD' :'/HWminusJ_HToWWTo2L2Nu_WToLNu_M125_13TeV_powheg_pythia8/RunIISummer16NanoAOD-PUMoriond17_05Feb2018_94X_mcRun2_asymptotic_v2-v1/NANOAODSIM'}
#Samples['HWplusJ_HToWW_LNu_M125']     = {'nanoAOD' :'/HWplusJ_HToWWTo2L2Nu_WToLNu_M125_13TeV_powheg_pythia8/RunIISummer16NanoAOD-PUMoriond17_05Feb2018_94X_mcRun2_asymptotic_v2-v1/NANOAODSIM'}

#### WH Inclusive============

#Samples['HWminusJ_HToWW_M125']     = {'nanoAOD' :'/HWminusJ_HToWW_M125_13TeV_powheg_pythia8/RunIISummer16NanoAOD-PUMoriond17_05Feb2018_94X_mcRun2_asymptotic_v2-v1/NANOAODSIM'}
#Samples['HWplusJ_HToWW_M125']      = {'nanoAOD' :'/HWplusJ_HToWW_M125_13TeV_powheg_pythia8/RunIISummer16NanoAOD-PUMoriond17_05Feb2018_94X_mcRun2_asymptotic_v2-v1/NANOAODSIM'}
#Samples['HWminusJ_HToTauTau_M125'] = {'nanoAOD' :'/WminusHToTauTau_M125_13TeV_powheg_pythia8/RunIISummer16NanoAOD-PUMoriond17_05Feb2018_94X_mcRun2_asymptotic_v2-v1/NANOAODSIM'}
#Samples['HWplusJ_HToTauTau_M125']  = {'nanoAOD' :'/WplusHToTauTau_M125_13TeV_powheg_pythia8/RunIISummer16NanoAOD-PUMoriond17_05Feb2018_94X_mcRun2_asymptotic_v2-v1/NANOAODSIM'}


#### ZH Inclusive ======== 
#Samples['HZJ_HToWW_M125']     = {'nanoAOD' :'/HZJ_HToWW_M125_13TeV_powheg_pythia8/RunIISummer16NanoAOD-PUMoriond17_05Feb2018_94X_mcRun2_asymptotic_v2-v1/NANOAODSIM'}
