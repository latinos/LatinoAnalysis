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

### Vg

#### Wg
#Samples['WGJJ']           = {'nanoAOD' :'/WGJJToLNu_EWK_QCD_TuneCUETP8M1_13TeV-madgraph-pythia8/RunIISummer16NanoAOD-PUMoriond17_05Feb2018_94X_mcRun2_asymptotic_v2-v1/NANOAODSIM'}
Samples['Wg_AMCNLOFXFX']  = {'nanoAOD' :'/WGToLNuG_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/RunIISummer16NanoAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/NANOAODSIM'}
Samples['Wg_AMCNLOFXFX_ext2']  = {'nanoAOD' :'/WGToLNuG_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/RunIISummer16NanoAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext2-v1/NANOAODSIM'}
Samples['Wg_AMCNLOFXFX_ext3']  = {'nanoAOD' :'/WGToLNuG_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/RunIISummer16NanoAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext3-v1/NANOAODSIM'}
#Samples['Wg_MADGRAPHMLM']      = {'nanoAOD' :'/WGToLNuG_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16NanoAOD-PUMoriond17_05Feb2018_94X_mcRun2_asymptotic_v2-v1/NANOAODSIM'}
#Samples['WgStarLNuEE'] = {'nanoAOD' :'/WGstarToLNuEE_012Jets_13TeV-madgraph/RunIISummer16NanoAOD-PUMoriond17_05Feb2018_94X_mcRun2_asymptotic_v2-v1/NANOAODSIM'}
#Samples['WgStarLNuMuMu'] = {'nanoAOD' :'/WGstarToLNuMuMu_012Jets_13TeV-madgraph/RunIISummer16NanoAOD-PUMoriond17_05Feb2018_94X_mcRun2_asymptotic_v2-v1/NANOAODSIM'}

#### Zg 
Samples['Zg']      = {'nanoAOD' :'/ZGTo2LG_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/RunIISummer16NanoAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/NANOAODSIM'}

### WZ
Samples['WZTo3LNu']       = {'nanoAOD' :'/WZTo3LNu_TuneCUETP8M1_13TeV-powheg-pythia8/RunIISummer16NanoAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/NANOAODSIM'}
Samples['WZTo3LNu_mllmin01'] = {'nanoAOD' :'/WZTo3LNu_mllmin01_13TeV-powheg-pythia8_ext1/RunIISummer16NanoAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/NANOAODSIM'}
Samples['WZ_ext1'] = {'nanoAOD' :'/WZ_TuneCUETP8M1_13TeV-pythia8/RunIISummer16NanoAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/NANOAODSIM'}
Samples['WZ'] = {'nanoAOD' :'/WZ_TuneCUETP8M1_13TeV-pythia8/RunIISummer16NanoAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/NANOAODSIM'}
Samples['WZ_AMCNLO'] = {'nanoAOD' :'/WZTo3LNu_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/RunIISummer16NanoAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/NANOAODSIM'}
Samples['WZTo2L2Q']        = {'nanoAOD' :'/WZTo2L2Q_13TeV_amcatnloFXFX_madspin_pythia8/RunIISummer16NanoAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/NANOAODSIM'}
Samples['WZTo1L3Nu']        = {'nanoAOD' :'/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/RunIISummer16NanoAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/NANOAODSIM'}
Samples['WZTo1L1Nu2Q']        = {'nanoAOD' :'/WZTo1L1Nu2Q_13TeV_amcatnloFXFX_madspin_pythia8/RunIISummer16NanoAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/NANOAODSIM'}

### ZZ

Samples['ZZ']         = {'nanoAOD' :'/ZZ_TuneCUETP8M1_13TeV-pythia8/RunIISummer16NanoAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/NANOAODSIM'}
Samples['ZZTo4L']         = {'nanoAOD' :'/ZZTo4L_13TeV_powheg_pythia8/RunIISummer16NanoAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/NANOAODSIM'}
Samples['ZZTo4L_AMCNLOFXFX']         = {'nanoAOD' :'/ZZTo4L_13TeV-amcatnloFXFX-pythia8/RunIISummer16NanoAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/NANOAODSIM'}
Samples['ZZTo2L2Q']         = {'nanoAOD' :'/ZZTo2L2Q_13TeV_powheg_pythia8/RunIISummer16NanoAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/NANOAODSIM'}
Samples['ZZTo2L2Q_AMCNLOFXFX']         = {'nanoAOD' :'/ZZTo2Q2Nu_13TeV_amcatnloFXFX_madspin_pythia8/RunIISummer16NanoAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/NANOAODSIM'}
Samples['ZZTo2L2Nu']         = {'nanoAOD' :'/ZZTo2L2Nu_13TeV_powheg_pythia8_ext1/RunIISummer16NanoAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/NANOAODSIM'}
Samples['ZZTo2L2Nu_EWK']         = {'nanoAOD' :'/ZZJJ_ZZTo2L2Nu_EWK_13TeV-madgraph-pythia8/RunIISummer16NanoAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/NANOAODSIM'}

#Samples['ZZTo2L2Q']   = {'nanoAOD' :'/ZZTo2L2Q_13TeV_amcatnloFXFX_madspin_pythia8/RunIISummer16NanoAOD-PUMoriond17_05Feb2018_94X_mcRun2_asymptotic_v2-v1/NANOAODSIM'}

### WW

#Samples['WWTo2L2Nu']    = {'nanoAOD' :'/WWTo2L2Nu_13TeV-powheg/RunIISummer16NanoAOD-PUMoriond17_05Feb2018_94X_mcRun2_asymptotic_v2-v1/NANOAODSIM'}
#Samples['GluGluWWTo2L2Nu_MCFM']      = {'nanoAOD' :'/GluGluWWTo2L2Nu_MCFM_13TeV/RunIISummer16NanoAOD-PUMoriond17_05Feb2018_94X_mcRun2_asymptotic_v2-v1/NANOAODSIM'}

#### WW PS >> Sang-il 

#Samples['WWTo2L2NuHerwigPS']    = {'nanoAOD' :'/WWTo2L2Nu_13TeV-powheg-herwigpp/RunIISummer16NanoAOD-PUMoriond17_05Feb2018_94X_mcRun2_asymptotic_v2-v1/NANOAODSIM'}

#### WW CUET variations >> 

#Samples['WWTo2L2Nu_CUETUp']  = {'nanoAOD' :'/WWTo2L2Nu_13TeV-powheg-CUETP8M1Up/RunIISummer16NanoAOD-PUMoriond17_05Feb2018_94X_mcRun2_asymptotic_v2-v1/NANOAODSIM'}
#Samples['WWTo2L2Nu_CUETDown']  = {'nanoAOD' :'/WWTo2L2Nu_13TeV-powheg-CUETP8M1Down/RunIISummer16NanoAOD-PUMoriond17_05Feb2018_94X_mcRun2_asymptotic_v2-v1/NANOAODSIM'}

Samples['WW-LO'] = {'nanoAOD' :'/WW_TuneCUETP8M1_13TeV-pythia8/RunIISummer16NanoAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/NANOAODSIM'}
Samples['WW-LOext1'] = {'nanoAOD' :'/WW_TuneCUETP8M1_13TeV-pythia8/RunIISummer16NanoAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/NANOAODSIM'}
Samples['WWTo2L2Nu_DoubleScattering'] = {'nanoAOD' :'/WWTo2L2Nu_DoubleScattering_13TeV-pythia8/RunIISummer16NanoAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/NANOAODSIM'}
Samples['WWTo4Q'] = {'nanoAOD' :'/WWTo4Q_13TeV-powheg/RunIISummer16NanoAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/NANOAODSIM'}
Samples['WWToLNuQQ'] = {'nanoAOD' :'/WWToLNuQQ_13TeV-powheg/RunIISummer16NanoAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/NANOAODSIM'}
Samples['WWToLNuQQ_AMCNLOFXFX'] = {'nanoAOD' :'/WWTo1L1Nu2Q_13TeV_amcatnloFXFX_madspin_pythia8/RunIISummer16NanoAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/NANOAODSIM'}

### Top
Samples['TTTo2L2Nu'] = {'nanoAOD' :'/TTTo2L2Nu_TuneCUETP8M2_ttHtranche3_13TeV-powheg-pythia8/RunIISummer16NanoAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/NANOAODSIM'}
Samples['TTJets_more'] = {'nanoAOD' :'/TTJets_TuneCUETP8M2T4_13TeV-amcatnloFXFX-pythia8/RunIISummer16NanoAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/NANOAODSIM'}
Samples['TTToSemiLeptonic'] = {'nanoAOD' :'/TTToSemilepton_TuneCUETP8M2_ttHtranche3_13TeV-powheg-pythia8/RunIISummer16NanoAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/NANOAODSIM'}

Samples['ST_t-channel_top']     = {'nanoAOD' :'/ST_t-channel_top_4f_inclusiveDecays_13TeV-powhegV2-madspin-pythia8_TuneCUETP8M1/RunIISummer16NanoAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/NANOAODSIM'}
Samples['ST_t-channel_antitop'] = {'nanoAOD' :'/ST_t-channel_antitop_4f_inclusiveDecays_13TeV-powhegV2-madspin-pythia8_TuneCUETP8M1/RunIISummer16NanoAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/NANOAODSIM'}
Samples['ST_tW_antitop']        = {'nanoAOD' :'/ST_tW_antitop_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/RunIISummer16NanoAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/NANOAODSIM'}
Samples['ST_tW_top']            = {'nanoAOD' :'/ST_tW_top_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/RunIISummer16NanoAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/NANOAODSIM'}
#Samples['ST_s-channel']         = {'nanoAOD' :'/ST_s-channel_4f_leptonDecays_13TeV-amcatnlo-pythia8_TuneCUETP8M1/RunIISummer16NanoAOD-PUMoriond17_05Feb2018_94X_mcRun2_asymptotic_v2-v1/NANOAODSIM'}

### ttV

Samples['TTWJetsToLNu'] = {'nanoAOD' :'/TTWJetsToLNu_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/RunIISummer16NanoAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext2-v1/NANOAODSIM'}
Samples['TTWJetsToQQ'] = {'nanoAOD' :'/TTWJetsToQQ_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/RunIISummer16NanoAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/NANOAODSIM'}
Samples['TTZToQQ'] = {'nanoAOD' :'/TTZToQQ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/RunIISummer16NanoAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/NANOAODSIM'}
Samples['TTZjets'] = {'nanoAOD' :'/ttZJets_13TeV_madgraphMLM-pythia8/RunIISummer16NanoAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/NANOAODSIM'}

#### VVV >> Sang-il 
Samples['WWW']  = {'nanoAOD' :'/WWW_4F_TuneCUETP8M1_13TeV-amcatnlo-pythia8/RunIISummer16NanoAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/NANOAODSIM'}
Samples['WWZ']  = {'nanoAOD' :'/WWZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/RunIISummer16NanoAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/NANOAODSIM'}
Samples['WZZ']  = {'nanoAOD' :'/WZZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/RunIISummer16NanoAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/NANOAODSIM'}
Samples['ZZZ']  = {'nanoAOD' :'/ZZZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/RunIISummer16NanoAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/NANOAODSIM'}
#Samples['WWG']  = {'nanoAOD' :'/WWG_TuneCUETP8M1_13TeV-amcatnlo-pythia8/RunIISummer16NanoAOD-PUMoriond17_05Feb2018_94X_mcRun2_asymptotic_v2_ext1-v1/NANOAODSIM'}

### W+Jets
#Samples['WJetsToLNu']                = {'nanoAOD' :'/WJetsToLNu_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/RunIISummer16NanoAOD-PUMoriond17_05Feb2018_94X_mcRun2_asymptotic_v2-v1/NANOAODSIM'}
Samples['WJetsToLNu-LO'] = {'nanoAOD' :'/WJetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16NanoAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/NANOAODSIM'}
Samples['WJetsToLNu-LO_ext2'] = {'nanoAOD' :'/WJetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16NanoAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext2-v2/NANOAODSIM'}
Samples['WJetsToLNu_HT70_100'] = {'nanoAOD': '/WJetsToLNu_HT-70To100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16NanoAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/NANOAODSIM'}
Samples['WJetsToLNu_HT100_200'] = {'nanoAOD': '/WJetsToLNu_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16NanoAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/NANOAODSIM'}
Samples['WJetsToLNu_HT100_200_ext1'] = {'nanoAOD': '/WJetsToLNu_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16NanoAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/NANOAODSIM'}
Samples['WJetsToLNu_HT200_400'] = {'nanoAOD':'/WJetsToLNu_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16NanoAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/NANOAODSIM'}
Samples['WJetsToLNu_HT200_400_ext1'] = {'nanoAOD':'/WJetsToLNu_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16NanoAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/NANOAODSIM'}
Samples['WJetsToLNu_HT200_400_ext2'] = {'nanoAOD':'/WJetsToLNu_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16NanoAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext2-v2/NANOAODSIM'}
Samples['WJetsToLNu_HT400_600'] = {'nanoAOD':'/WJetsToLNu_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16NanoAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/NANOAODSIM'}
Samples['WJetsToLNu_HT400_600_ext1'] = {'nanoAOD':'/WJetsToLNu_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16NanoAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/NANOAODSIM'}
Samples['WJetsToLNu_HT600_800'] = {'nanoAOD':'/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16NanoAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/NANOAODSIM'}
Samples['WJetsToLNu_HT600_800_ext1'] = {'nanoAOD':'/WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16NanoAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/NANOAODSIM'}
Samples['WJetsToLNu_HT800_1200'] = {'nanoAOD':'/WJetsToLNu_HT-800To1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16NanoAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/NANOAODSIM'}
Samples['WJetsToLNu_HT800_1200_ext1'] = {'nanoAOD':'/WJetsToLNu_HT-800To1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16NanoAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/NANOAODSIM'}
Samples['WJetsToLNu_HT1200_2500'] = {'nanoAOD' :'/WJetsToLNu_HT-1200To2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16NanoAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/NANOAODSIM'}
Samples['WJetsToLNu_HT1200_2500_ext1'] = {'nanoAOD' :'/WJetsToLNu_HT-1200To2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16NanoAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/NANOAODSIM'}
Samples['WJetsToLNu_HT2500_inf'] = {'/WJetsToLNu_HT-2500ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16NanoAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/NANOAODSIM'}
Samples['WJetsToLNu_HT2500_inf_ext1'] = {'/WJetsToLNu_HT-2500ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16NanoAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/NANOAODSIM'}

### DY+Jets
Samples['DYJetsToLL_M-10to50-LO']           = {'nanoAOD' :'/DYJetsToLL_M-10to50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16NanoAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/NANOAODSIM'}
Samples['DYJetsToLL_M-50-LO_ext1']          = {'nanoAOD' :'/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16NanoAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/NANOAODSIM'}
Samples['DYJetsToLL_M-50-LO_ext2']          = {'nanoAOD' :'/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16NanoAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext2-v2/NANOAODSIM'}
Samples['DYJetsToLL_M-10to50']              = {'nanoAOD' :'/DYJetsToLL_M-10to50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/RunIISummer16NanoAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/NANOAODSIM'}
Samples['DYJetsToLL_M-10to50_ext1']              = {'nanoAOD' :'/DYJetsToLL_M-10to50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/RunIISummer16NanoAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/NANOAODSIM'}
Samples['DYJetsToLL_M-50_ext2']                  = {'nanoAOD' :'/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/RunIISummer16NanoAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext2-v1/NANOAODSIM'}

#### DY Variations

Samples['DYJetsToLL_M-50-UEup']                  = {'nanoAOD' :'/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8_CUETP8M1Up/RunIISummer16NanoAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/NANOAODSIM'}
Samples['DYJetsToLL_M-50-UEdo']                  = {'nanoAOD' :'/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8_CUETP8M1Down/RunIISummer16NanoAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/NANOAODSIM'}
Samples['DYJetsToLL_M-50-PSup']                  = {'nanoAOD' :'/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8_UpPS/RunIISummer16NanoAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/NANOAODSIM'}
Samples['DYJetsToLL_M-50-PSdo']                  = {'nanoAOD' :'/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8_DownPS/RunIISummer16NanoAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/NANOAODSIM'}

#### DY HT samples

Samples['DYJetsToLL_M-5to50_HT-70to100']                  = {'nanoAOD' :'/DYJetsToLL_M-5to50_HT-70to100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16NanoAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/NANOAODSIM'}
Samples['DYJetsToLL_M-5to50_HT-100to200']                  = {'nanoAOD' :'/DYJetsToLL_M-5to50_HT-100to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16NanoAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/NANOAODSIM'}
Samples['DYJetsToLL_M-5to50_HT-100to200_ext1']                  = {'nanoAOD' :'/DYJetsToLL_M-5to50_HT-100to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16NanoAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/NANOAODSIM'}
Samples['DYJetsToLL_M-5to50_HT-200to400']                  = {'nanoAOD' :'/DYJetsToLL_M-5to50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16NanoAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/NANOAODSIM'}
Samples['DYJetsToLL_M-5to50_HT-200to400_ext1']                  = {'nanoAOD' :'/DYJetsToLL_M-5to50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16NanoAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/NANOAODSIM'}
Samples['DYJetsToLL_M-5to50_HT-400to600']                  = {'nanoAOD' :'/DYJetsToLL_M-5to50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16NanoAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/NANOAODSIM'}
Samples['DYJetsToLL_M-5to50_HT-400to600_ext1']                  = {'nanoAOD' :'/DYJetsToLL_M-5to50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16NanoAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/NANOAODSIM'}
Samples['DYJetsToLL_M-5to50_HT-600toinf']                  = {'nanoAOD' :'/DYJetsToLL_M-5to50_HT-600toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16NanoAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/NANOAODSIM'}

Samples['DYJetsToLL_M-50_HT-70to100']                  = {'nanoAOD' :'/DYJetsToLL_M-50_HT-70to100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16NanoAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/NANOAODSIM'}
Samples['DYJetsToLL_M-50_HT-100to200']                  = {'/DYJetsToLL_M-50_HT-100to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16NanoAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/NANOAODSIM'}
Samples['DYJetsToLL_M-50_HT-100to200_ext1']                  = {'nanoAOD' :'/DYJetsToLL_M-50_HT-100to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16NanoAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/NANOAODSIM'}
Samples['DYJetsToLL_M-50_HT-200to400']                  = {'nanoAOD' :'/DYJetsToLL_M-50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16NanoAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/NANOAODSIM'}
Samples['DYJetsToLL_M-50_HT-200to400_ext1']                  = {'nanoAOD' :'/DYJetsToLL_M-50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16NanoAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/NANOAODSIM'}
Samples['DYJetsToLL_M-50_HT-400to600']                  = {'nanoAOD' :'/DYJetsToLL_M-50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16NanoAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/NANOAODSIM'}
Samples['DYJetsToLL_M-50_HT-400to600_ext1']                  = {'nanoAOD' :'/DYJetsToLL_M-50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16NanoAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/NANOAODSIM'}
Samples['DYJetsToLL_M-50_HT-600to800']                  = {'nanoAOD' :'/DYJetsToLL_M-50_HT-600to800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16NanoAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/NANOAODSIM'}
Samples['DYJetsToLL_M-50_HT-800to1200']                  = {'nanoAOD' :'/DYJetsToLL_M-50_HT-800to1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16NanoAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/NANOAODSIM'}
Samples['DYJetsToLL_M-50_HT-1200to2500']                  = {'nanoAOD' :'/DYJetsToLL_M-50_HT-1200to2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16NanoAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/NANOAODSIM'}
Samples['DYJetsToLL_M-50_HT-2500toinf']                  = {'nanoAOD' :'/DYJetsToLL_M-50_HT-2500toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16NanoAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/NANOAODSIM'}

############# updated untill here

### QCD fakes
Samples['QCD_Pt_20to30_bcToE']             = {'nanoAOD' :'/QCD_Pt_20to30_bcToE_TuneCUETP8M1_13TeV_pythia8/RunIISummer16NanoAOD-PUMoriond17_05Feb2018_94X_mcRun2_asymptotic_v2-v1/NANOAODSIM'}
Samples['QCD_Pt_30to80_bcToE']             = {'nanoAOD' :'/QCD_Pt_30to80_bcToE_TuneCUETP8M1_13TeV_pythia8/RunIISummer16NanoAOD-PUMoriond17_05Feb2018_94X_mcRun2_asymptotic_v2-v1/NANOAODSIM'}
Samples['QCD_Pt_80to170_bcToE']            = {'nanoAOD' :'/QCD_Pt_80to170_bcToE_TuneCUETP8M1_13TeV_pythia8/RunIISummer16NanoAOD-PUMoriond17_05Feb2018_backup_94X_mcRun2_asymptotic_v2-v1/NANOAODSIM'}
Samples['QCD_Pt_170to250_bcToE']           = {'nanoAOD' :'/QCD_Pt_170to250_bcToE_TuneCUETP8M1_13TeV_pythia8/RunIISummer16NanoAOD-PUMoriond17_05Feb2018_94X_mcRun2_asymptotic_v2-v1/NANOAODSIM'}
Samples['QCD_Pt_250toInf_bcToE']           = {'nanoAOD' :'/QCD_Pt_250toInf_bcToE_TuneCUETP8M1_13TeV_pythia8/RunIISummer16NanoAOD-PUMoriond17_05Feb2018_94X_mcRun2_asymptotic_v2-v1/NANOAODSIM'}
#Samples['QCD_Pt-15to20_MuEnrichedPt5']     = {'nanoAOD' :'/QCD_Pt-15to20_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/RunIISummer16NanoAOD-PUMoriond17_05Feb2018_94X_mcRun2_asymptotic_v2-v1/NANOAODSIM'} #missing
#Samples['QCD_Pt-20toInf_MuEnrichedPt15']   = {'nanoAOD' :'/QCD_Pt-20toInf_MuEnrichedPt15_TuneCUETP8M1_13TeV_pythia8/RunIISummer16NanoAOD-PUMoriond17_05Feb2018_94X_mcRun2_asymptotic_v2-v1/NANOAODSIM'} #missing
Samples['QCD_Pt-20to30_EMEnriched']        = {'nanoAOD' :'/QCD_Pt-20to30_EMEnriched_TuneCUETP8M1_13TeV_pythia8/RunIISummer16NanoAOD-PUMoriond17_05Feb2018_94X_mcRun2_asymptotic_v2-v1/NANOAODSIM'}
#Samples['QCD_Pt-30to50_EMEnriched']        = {'nanoAOD' :'/QCD_Pt-30to50_EMEnriched_TuneCUETP8M1_13TeV_pythia8/RunIISummer16NanoAOD-PUMoriond17_05Feb2018_94X_mcRun2_asymptotic_v2-v1/NANOAODSIM'} #missing
#Samples['QCD_Pt-50to80_EMEnriched']        = {'nanoAOD' :'/QCD_Pt-50to80_EMEnriched_TuneCUETP8M1_13TeV_pythia8/RunIISummer16NanoAOD-PUMoriond17_05Feb2018_94X_mcRun2_asymptotic_v2-v1/NANOAODSIM'} #missing
Samples['QCD_Pt-30toInf_DoubleEMEnriched'] = {'nanoAOD' :'/QCD_Pt-30toInf_DoubleEMEnriched_MGG-40to80_TuneCUETP8M1_13TeV_Pythia8/RunIISummer16NanoAOD-PUMoriond17_05Feb2018_94X_mcRun2_asymptotic_v2-v1/NANOAODSIM'}


Samples['VBFHToWWTo2L2Nu_M125']         = {'nanoAOD' :'/VBFHToWWTo2L2Nu_M125_13TeV_powheg_JHUgenv628_pythia8/RunIISummer16NanoAOD-PUMoriond17_05Feb2018_94X_mcRun2_asymptotic_v2-v1/NANOAODSIM'}
Samples['VBFHToWWTo2L2NuPowheg_M125']   = {'nanoAOD' :'/VBFHToWWTo2L2Nu_M125_13TeV_powheg_pythia8/RunIISummer16NanoAOD-PUMoriond17_05Feb2018_94X_mcRun2_asymptotic_v2-v1/NANOAODSIM'}
Samples['VBFHToWWTo2L2NuAMCNLO_M125']   = {'nanoAOD' :'/VBFHToWWTo2L2Nu_M125_13TeV_amcatnlo_pythia8/RunIISummer16NanoAOD-PUMoriond17_05Feb2018_94X_mcRun2_asymptotic_v2-v1/NANOAODSIM'}
Samples['VBFHToWWTo2L2NuHerwigPS_M125'] = {'nanoAOD' :'/VBFHToWWTo2L2Nu_M125_13TeV_powheg_JHUgen_herwigpp/RunIISummer16NanoAOD-PUMoriond17_05Feb2018_94X_mcRun2_asymptotic_v2-v1/NANOAODSIM'}

Samples['VBFHToTauTau_M125']            = {'nanoAOD' :'/VBFHToTauTau_M125_13TeV_powheg_pythia8/RunIISummer16NanoAOD-PUMoriond17_05Feb2018_94X_mcRun2_asymptotic_v2-v1/NANOAODSIM'}
Samples['VBFHToWWTo2L2Nu_M125_herwigpp'] = {'nanoAOD' :'/VBFHToWWTo2L2Nu_M125_13TeV_powheg_JHUgen_herwigpp/RunIISummer16NanoAOD-PUMoriond17_05Feb2018_94X_mcRun2_asymptotic_v2-v1/NANOAODSIM'}
Samples['VBFHToWWTo2L2Nu_M125_CUETDown'] = {'nanoAOD' :'/VBFHToWWTo2L2Nu_M125_13TeV_powheg_JHUgen_pythia8-CUETP8M1Down/RunIISummer16NanoAOD-PUMoriond17_05Feb2018_94X_mcRun2_asymptotic_v2-v1/NANOAODSIM'}
Samples['VBFHToWWTo2L2Nu_M125_CUETUp']   = {'nanoAOD' :'/VBFHToWWTo2L2Nu_M125_13TeV_powheg_JHUgen_pythia8-CUETP8M1Up/RunIISummer16NanoAOD-PUMoriond17_05Feb2018_94X_mcRun2_asymptotic_v2-v1/NANOAODSIM'}


#### ggZH >> Sang-il 
Samples['ggZH_HToWW_M125']      = {'nanoAOD' :'/GluGluZH_HToWW_M125_13TeV_powheg_pythia8/RunIISummer16NanoAOD-PUMoriond17_05Feb2018_94X_mcRun2_asymptotic_v2-v1/NANOAODSIM'}

#### ZH tautau >> Sang-il 
Samples['HZJ_HToTauTau_M125'] = {'nanoAOD' :'/ZHToTauTau_M125_13TeV_powheg_pythia8/RunIISummer16NanoAOD-PUMoriond17_05Feb2018_94X_mcRun2_asymptotic_v2-v1/NANOAODSIM'}








#Samples['GluGluHToWWTo2L2Nu_M125']       = {'nanoAOD' :'/GluGluHToWWTo2L2Nu_M125_13TeV_powheg_JHUgenv628_pythia8/RunIISummer16NanoAOD-PUMoriond17_05Feb2018_94X_mcRun2_asymptotic_v2-v1/NANOAODSIM'} #missing
Samples['GluGluHToWWTo2L2NuAMCNLO_M125'] = {'nanoAOD' :'/GluGluHToWWTo2L2Nu_M125_13TeV_amcatnloFXFX_pythia8/RunIISummer16NanoAOD-PUMoriond17_05Feb2018_94X_mcRun2_asymptotic_v2-v1/NANOAODSIM'}
Samples['GluGluHToWWTo2L2NuPowheg_M125'] = {'nanoAOD' :'/GluGluHToWWTo2L2Nu_M125_13TeV_powheg_pythia8/RunIISummer16NanoAOD-PUMoriond17_05Feb2018_94X_mcRun2_asymptotic_v2-v1/NANOAODSIM'}
Samples['GluGluHToTauTau_M125']          = {'nanoAOD' :'/GluGluHToTauTau_M125_13TeV_powheg_pythia8/RunIISummer16NanoAOD-PUMoriond17_05Feb2018_94X_mcRun2_asymptotic_v2-v1/NANOAODSIM'}
Samples['GluGluHToWWTo2L2Nu_M125_herwigpp'] = {'nanoAOD' :'/GluGluHToWWTo2L2Nu_M125_13TeV_powheg_JHUgen_herwigpp/RunIISummer16NanoAOD-PUMoriond17_05Feb2018_94X_mcRun2_asymptotic_v2-v1/NANOAODSIM'}
Samples['GluGluHToWWTo2L2Nu_M125_CUETDown'] = {'nanoAOD' :'/GluGluHToWWTo2L2Nu_M125_13TeV_powheg_JHUgen_pythia8-CUETP8M1Down/RunIISummer16NanoAOD-PUMoriond17_05Feb2018_94X_mcRun2_asymptotic_v2-v1/NANOAODSIM'}
Samples['GluGluHToWWTo2L2Nu_M125_CUETUp']   = {'nanoAOD' :'/GluGluHToWWTo2L2Nu_M125_13TeV_powheg_JHUgen_pythia8-CUETP8M1Up/RunIISummer16NanoAOD-PUMoriond17_05Feb2018_94X_mcRun2_asymptotic_v2-v1/NANOAODSIM'}
#Samples['GluGluHToWWTo2L2Nu_minloHJJ_M125'] = {'nanoAOD' :'/GluGluHToWWTo2L2Nu_M125_13TeV_powheg2_minloHJJ_JHUGenV702_pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v5/NANOCHECKAODSIM'} #missing


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Po-Hsun
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


### WH Exclusive

Samples['HWminusJ_HToWW_LNu_M125']     = {'nanoAOD' :'/HWminusJ_HToWWTo2L2Nu_WToLNu_M125_13TeV_powheg_pythia8/RunIISummer16NanoAOD-PUMoriond17_05Feb2018_94X_mcRun2_asymptotic_v2-v1/NANOAODSIM'}

Samples['HWplusJ_HToWW_LNu_M125']     = {'nanoAOD' :'/HWplusJ_HToWWTo2L2Nu_WToLNu_M125_13TeV_powheg_pythia8/RunIISummer16NanoAOD-PUMoriond17_05Feb2018_94X_mcRun2_asymptotic_v2-v1/NANOAODSIM'}

#### WH Inclusive============

Samples['HWminusJ_HToWW_M125']     = {'nanoAOD' :'/HWminusJ_HToWW_M125_13TeV_powheg_pythia8/RunIISummer16NanoAOD-PUMoriond17_05Feb2018_94X_mcRun2_asymptotic_v2-v1/NANOAODSIM'}
Samples['HWplusJ_HToWW_M125']      = {'nanoAOD' :'/HWplusJ_HToWW_M125_13TeV_powheg_pythia8/RunIISummer16NanoAOD-PUMoriond17_05Feb2018_94X_mcRun2_asymptotic_v2-v1/NANOAODSIM'}
Samples['HWminusJ_HToTauTau_M125'] = {'nanoAOD' :'/WminusHToTauTau_M125_13TeV_powheg_pythia8/RunIISummer16NanoAOD-PUMoriond17_05Feb2018_94X_mcRun2_asymptotic_v2-v1/NANOAODSIM'}
Samples['HWplusJ_HToTauTau_M125']  = {'nanoAOD' :'/WplusHToTauTau_M125_13TeV_powheg_pythia8/RunIISummer16NanoAOD-PUMoriond17_05Feb2018_94X_mcRun2_asymptotic_v2-v1/NANOAODSIM'}


#### ZH Inclusive ======== 
Samples['HZJ_HToWW_M125']     = {'nanoAOD' :'/HZJ_HToWW_M125_13TeV_powheg_pythia8/RunIISummer16NanoAOD-PUMoriond17_05Feb2018_94X_mcRun2_asymptotic_v2-v1/NANOAODSIM'}
