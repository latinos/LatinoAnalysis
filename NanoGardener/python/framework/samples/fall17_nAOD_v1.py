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
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Giulio
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Samples['Wg_AMCNLOFXFX']   = {'nanoAOD' :'/WGToLNuG_01J_5f_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIIFall17NanoAOD-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/NANOAODSIM'}
Samples['WZTo3LNu']        = {'nanoAOD' :'/WZTo3LNu_mllmin01_NNPDF31_TuneCP5_13TeV_powheg_pythia8/RunIIFall17NanoAOD-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/NANOAODSIM'}
Samples['ZZTo4L']          = {'nanoAOD' :'/ZZTo4L_13TeV_powheg_pythia8/RunIIFall17NanoAOD-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/NANOAODSIM'}
Samples['ZZTo2L2Nu']       = {'nanoAOD' :'/ZZTo2L2Nu_13TeV_powheg_pythia8/RunIIFall17NanoAOD-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/NANOAODSIM'}
Samples['WZ']              = {'nanoAOD' :'/WZ_TuneCP5_13TeV-pythia8/RunIIFall17NanoAOD-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/NANOAODSIM'}
Samples['WZTo2L2Q']        = {'nanoAOD' :'/WZTo2L2Q_13TeV_amcatnloFXFX_madspin_pythia8/RunIIFall17NanoAOD-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/NANOAODSIM'}
Samples['ZZ']              = {'nanoAOD' :'/ZZ_TuneCP5_13TeV-pythia8/RunIIFall17NanoAOD-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/NANOAODSIM'}
Samples['ZZTo2L2Q']        = {'nanoAOD' :'/ZZTo2L2Q_13TeV_amcatnloFXFX_madspin_pythia8/RunIIFall17NanoAOD-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/NANOAODSIM'}
Samples['WWTo2L2Nu']       = {'nanoAOD': '/WWTo2L2Nu_NNPDF31_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIIFall17NanoAOD-PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/NANOAODSIM'}  
Samples['WWTo2L2Nu_CP5Up'] = {'nanoAOD' :'/WWTo2L2Nu_NNPDF31_TuneCP5Up_13TeV-powheg-pythia8/RunIIFall17NanoAOD-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/NANOAODSIM'}
Samples['WW-LO']           = {'nanoAOD' :'/WW_TuneCP5_13TeV-pythia8/RunIIFall17NanoAOD-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/NANOAODSIM'}

#Signals
Samples['VBFHToWWTo2L2NuPowheg_M125_private']   = {'srmPrefix' : 'srm://stormfe1.pi.infn.it:8444/srm/managerv2?SFN=/cms', 'paths' :['/store/user/lenzip/VBFHToWWTo2L2Nu_M125_13TeV_powheg_JHUGen_pythia8/2018May8_nanoAODmerged/180613_141155/0000/'] }
Samples['VBFHToTauTau_M125']            = {'nanoAOD' :'/VBFHToTauTau_M125_13TeV_powheg_pythia8/RunIIFall17NanoAOD-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/NANOAODSIM'}
Samples['HZJ_HToTauTau_M125'] = {'nanoAOD' :'/ZHToTauTau_M125_13TeV_powheg_pythia8/RunIIFall17NanoAOD-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/NANOAODSIM'}
Samples['GluGluHToWWTo2L2NuPowheg_M125_private'] = {'srmPrefix' : 'srm://stormfe1.pi.infn.it:8444/srm/managerv2?SFN=/cms', 'paths':['/store/user/lenzip/GluGluHToWWTo2L2Nu_M125_13TeV_powheg_JHUGen_pythia8/2018May9_nanoAODmerged/180613_140914/0000/']}
Samples['GluGluHToTauTau_M125']          = {'nanoAOD' :'/GluGluHToTauTau_M125_13TeV_powheg_pythia8/RunIIFall17NanoAOD-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/NANOAODSIM'}
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


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Alicia
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
### QCD fakes
Samples['QCD_Pt_20to30_bcToE']               = {'nanoAOD' :'/QCD_Pt_20to30_bcToE_TuneCP5_13TeV_pythia8/RunIIFall17NanoAOD-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/NANOAODSIM'}
Samples['QCD_Pt_30to80_bcToE']               = {'nanoAOD' :'/QCD_Pt_30to80_bcToE_TuneCP5_13TeV_pythia8/RunIIFall17NanoAOD-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/NANOAODSIM'}
Samples['QCD_Pt_80to170_bcToE']              = {'nanoAOD' :'/QCD_Pt_80to170_bcToE_TuneCP5_13TeV_pythia8/RunIIFall17NanoAOD-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/NANOAODSIM'}
Samples['QCD_Pt_170to250_bcToE']             = {'nanoAOD' :'/QCD_Pt_170to250_bcToE_TuneCP5_13TeV_pythia8/RunIIFall17NanoAOD-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/NANOAODSIM'}
Samples['QCD_Pt_250toInf_bcToE']             = {'nanoAOD' :'/QCD_Pt_250toInf_bcToE_TuneCP5_13TeV_pythia8/RunIIFall17NanoAOD-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/NANOAODSIM'}
Samples['QCD_Pt-15to20_MuEnrichedPt5']       = {'nanoAOD' :'/QCD_Pt-15to20_MuEnrichedPt5_TuneCP5_13TeV_pythia8/RunIIFall17NanoAOD-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/NANOAODSIM'}
Samples['QCD_Pt-20to30_MuEnrichedPt5']       = {'nanoAOD' :'/QCD_Pt-20to30_MuEnrichedPt5_TuneCP5_13TeV_pythia8/RunIIFall17NanoAOD-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/NANOAODSIM'}
Samples['QCD_Pt-30to50_MuEnrichedPt5']       = {'nanoAOD' :'/QCD_Pt-30to50_MuEnrichedPt5_TuneCP5_13TeV_pythia8/RunIIFall17NanoAOD-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/NANOAODSIM'}
Samples['QCD_Pt-50to80_MuEnrichedPt5']       = {'nanoAOD' :'/QCD_Pt-50to80_MuEnrichedPt5_TuneCP5_13TeV_pythia8/RunIIFall17NanoAOD-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/NANOAODSIM'}
Samples['QCD_Pt-80to120_MuEnrichedPt5']      = {'nanoAOD' :'/QCD_Pt-80to120_MuEnrichedPt5_TuneCP5_13TeV_pythia8/RunIIFall17NanoAOD-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/NANOAODSIM'}
Samples['QCD_Pt-120to170_MuEnrichedPt5']     = {'nanoAOD' :'/QCD_Pt-120to170_MuEnrichedPt5_TuneCP5_13TeV_pythia8/RunIIFall17NanoAOD-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/NANOAODSIM'}
Samples['QCD_Pt-170to300_MuEnrichedPt5']     = {'nanoAOD' :'/QCD_Pt-170to300_MuEnrichedPt5_TuneCP5_13TeV_pythia8/RunIIFall17NanoAOD-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/NANOAODSIM'}
#Samples['QCD_Pt-20toInf_MuEnrichedPt15']   = {'nanoAOD' :'new in mcm'} 
Samples['QCD_Pt-20to30_EMEnriched']        = {'nanoAOD' :'/QCD_Pt-20to30_EMEnriched_TuneCP5_13TeV_pythia8/RunIIFall17NanoAOD-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/NANOAODSIM'}
Samples['QCD_Pt-30to50_EMEnriched']        = {'nanoAOD' :'/QCD_Pt-30to50_EMEnriched_TuneCP5_13TeV_pythia8/RunIIFall17NanoAOD-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/NANOAODSIM'} 
Samples['QCD_Pt-50to80_EMEnriched']        = {'nanoAOD' :'/QCD_Pt-50to80_EMEnriched_TuneCP5_13TeV_pythia8/RunIIFall17NanoAOD-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/NANOAODSIM'} 
Samples['QCD_Pt-30toInf_DoubleEMEnriched'] = {'nanoAOD' :'/QCD_Pt-30toInf_DoubleEMEnriched_MGG-40to80_TuneCP5_13TeV_Pythia8/RunIIFall17NanoAOD-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/NANOAODSIM'}


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Jonatan
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Samples['WWW']  = {'nanoAOD' :'/WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8/RunIIFall17NanoAOD-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/NANOAODSIM'}
Samples['WWZ']  = {'nanoAOD' :'/WWZ_4F_TuneCP5_13TeV-amcatnlo-pythia8/RunIIFall17NanoAOD-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/NANOAODSIM'}
Samples['WZZ']  = {'nanoAOD' :'/WZZ_TuneCP5_13TeV-amcatnlo-pythia8/RunIIFall17NanoAOD-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/NANOAODSIM'}
Samples['ZZZ']  = {'nanoAOD' :'/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/RunIIFall17NanoAOD-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/NANOAODSIM'}
Samples['WWG']  = {'nanoAOD' :'/WWG_TuneCP5_13TeV-amcatnlo-pythia8/RunIIFall17NanoAOD-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/NANOAODSIM'}


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Cedric
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
## TTbar
Samples['TTTo2L2Nu'] = {'nanoAOD' :'/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/RunIIFall17NanoAOD-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/NANOAODSIM'}
Samples['TTToSemileptonic'] = {'nanoAOD' :'/TTToSemiLeptonic_mtop178p5_TuneCP5_13TeV-powheg-pythia8/RunIIFall17NanoAOD-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/NANOAODSIM'}


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Pablo
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
## DY and W + jets
#Samples['DYJetsToLL_M-10to50'] = {'nanoAOD' :'new in mcm'} 
Samples['WJetsToLNu-LO'] = {'nanoAOD' :'/WJetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17NanoAOD-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/NANOAODSIM'}
Samples['WJetsToLNu_HT100_200'] = {'nanoAOD': '/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17NanoAOD-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/NANOAODSIM'}
Samples['WJetsToLNu_HT200_400'] = {'nanoAOD': '/WJetsToLNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17NanoAOD-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/NANOAODSIM'}
Samples['WJetsToLNu_HT400_600'] = {'nanoAOD': '/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17NanoAOD-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/NANOAODSIM'}
Samples['WJetsToLNu_HT600_800'] = {'nanoAOD': '/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17NanoAOD-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/NANOAODSIM'}
Samples['WJetsToLNu_HT800_1200'] = {'nanoAOD': '/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17NanoAOD-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/NANOAODSIM'}
Samples['WJetsToLNu_HT1200_2500'] = {'nanoAOD': '/WJetsToLNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17NanoAOD-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/NANOAODSIM'}
Samples['WJetsToLNu_HT2500_inf'] = {'nanoAOD': '/WJetsToLNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17NanoAOD-PU2017_12Apr2018_94X_mc2017_realistic_v14-v3/NANOAODSIM'}


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Isabel
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Samples['DYJetsToLL_M-5to50-LO']   = {'nanoAOD' :'/DYJetsToLL_M-5to50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17NanoAOD-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/NANOAODSIM'} # not yet valid
Samples['DYJetsToLL_M-50-LO-ext1'] = {'nanoAOD' :'/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17NanoAOD-PU2017RECOSIMstep_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/NANOAODSIM'}
Samples['DYJetsToTT_MuEle_M-50'] = {'nanoAOD': '/DYJetsToTauTau_ForcedMuEleDecay_M-50_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIIFall17NanoAOD-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/NANOAODSIM'}
Samples['DYJetsToLL_M-50']     = {'nanoAOD' :'/DYJetsToLL_M-50_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIIFall17NanoAOD-PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/NANOAODSIM'} 
Samples['DYJetsToLL_M-50_HT-100to200'] = {'nanoAOD': '/DYJetsToLL_M-50_HT-100to200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17NanoAOD-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/NANOAODSIM'}
Samples['DYJetsToLL_M-50_HT-200to400'] = {'nanoAOD': '/DYJetsToLL_M-50_HT-200to400_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17NanoAOD-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/NANOAODSIM'}
Samples['DYJetsToLL_M-50_HT-400to600'] = {'nanoAOD': '/DYJetsToLL_M-50_HT-400to600_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17NanoAOD-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/NANOAODSIM'}
Samples['DYJetsToLL_M-50_HT-600to800'] = {'nanoAOD': '/DYJetsToLL_M-50_HT-600to800_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17NanoAOD-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/NANOAODSIM'}
Samples['DYJetsToLL_M-50_HT-800to1200'] = {'nanoAOD': '/DYJetsToLL_M-50_HT-800to1200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17NanoAOD-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/NANOAODSIM'}
Samples['DYJetsToLL_M-50_HT-1200to2500'] = {'nanoAOD': '/DYJetsToLL_M-50_HT-1200to2500_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17NanoAOD-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/NANOAODSIM'}
Samples['DYJetsToLL_M-50_HT-2500toInf'] = {'nanoAOD': '/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17NanoAOD-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/NANOAODSIM'}

Samples['ST_t-channel_top']     = {'nanoAOD' :'/ST_t-channel_top_4f_inclusiveDecays_TuneCP5_13TeV-powhegV2-madspin-pythia8/RunIIFall17NanoAOD-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/NANOAODSIM'}
Samples['ST_t-channel_antitop'] = {'nanoAOD' :'/ST_t-channel_antitop_4f_inclusiveDecays_TuneCP5_13TeV-powhegV2-madspin-pythia8/RunIIFall17NanoAOD-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/NANOAODSIM'}
Samples['ST_tW_top']            = {'nanoAOD' :'/ST_tW_top_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/RunIIFall17NanoAOD-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/NANOAODSIM'}
Samples['ST_tW_antitop']        = {'nanoAOD' :'/ST_tW_antitop_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/RunIIFall17NanoAOD-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/NANOAODSIM'}
Samples['ST_s-channel']         = {'nanoAOD' :'/ST_s-channel_4f_leptonDecays_TuneCP5_13TeV-amcatnlo-pythia8/RunIIFall17NanoAOD-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/NANOAODSIM'}


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Xavier/Kamiel
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
## VBS - signal
samples['WpWpJJ_EWK_QCD'] = {'nanoAOD' :'/WpWpJJ_EWK-QCD_TuneCP5_13TeV-madgraph-pythia8/RunIIFall17NanoAOD-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/NANOAODSIM'}
#samples['WpWpJJ_EWK'] = {'nanoAOD' :'/WpWpJJ_EWK_TuneCUETP8M1_13TeV-madgraph-pythia8/RunIISummer16NanoAOD-PUMoriond17_05Feb2018_94X_mcRun2_asymptotic_v2-v1/NANOAODSIM'}
#samples['WpWpJJ_QCD'] = {'nanoAOD' :'/WpWpJJ_QCD_TuneCUETP8M1_13TeV-madgraph-pythia8/RunIISummer16NanoAOD-PUMoriond17_05Feb2018_94X_mcRun2_asymptotic_v2-v1/NANOAODSIM'}
#samples['WpWpJJ_EWK_aQGC'] = {'nanoAOD' :'/WWJJ_SS_WToLNu_EWK_aQGC-FT-FS-FM_TuneCUETP8M1_13TeV_madgraph-pythia8/RunIISummer16NanoAOD-PUMoriond17_05Feb2018_94X_mcRun2_asymptotic_v2-v1/NANOAODSIM'}

## VBS - specific backgrounds

samples['WLLJJToLNu_M-60_EWK_4F']          = {'nanoAOD' :'/WLLJJ_WToLNu_EWK_TuneCP5_13TeV_madgraph-madspin-pythia8/RunIIFall17NanoAOD-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/NANOAODSIM'}
samples['WLLJJToLNu_M-50_QCD_0Jet']          = {'nanoAOD' :'/WZTo3LNu_0Jets_MLL-50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17NanoAOD-PU2017_12Apr2018_94X_mc2017_realistic_v14-v3/NANOAODSIM'}
samples['WLLJJToLNu_M-50_QCD_1Jet']          = {'nanoAOD' :'/WZTo3LNu_1Jets_MLL-50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17NanoAOD-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/NANOAODSIM'}
samples['WLLJJToLNu_M-50_QCD_2Jet']          = {'nanoAOD' :'/WZTo3LNu_2Jets_MLL-50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17NanoAOD-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/NANOAODSIM'}
samples['WLLJJToLNu_M-50_QCD_3Jet']          = {'nanoAOD' :'/WZTo3LNu_3Jets_MLL-50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17NanoAOD-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/NANOAODSIM'}
samples['WLLJJToLNu_M-4To60_EWK_4F']          = {'nanoAOD' :'/WLLJJ_WToLNu_EWK_TuneCP5_13TeV_madgraph-madspin-pythia8/RunIIFall17NanoAOD-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/NANOAODSIM'}
#samples['WLLJJToLNu_M-4To50_QCD_0Jet']          = {'nanoAOD' :''} 
#samples['WLLJJToLNu_M-4To50_QCD_1Jet']          = {'nanoAOD' :''} 
#samples['WLLJJToLNu_M-4To50_QCD_2Jet']          = {'nanoAOD' :''} 
#samples['WLLJJToLNu_M-4To50_QCD_3Jet']          = {'nanoAOD' :''} 
#samples['WZJJ_EWK_QCD']                 = {'nanoAOD' :''} 


