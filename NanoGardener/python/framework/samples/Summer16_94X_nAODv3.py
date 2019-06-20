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
Samples['WGJJ']           = {'nanoAOD' :'/WGJJToLNu_EWK_QCD_TuneCUETP8M1_13TeV-madgraph-pythia8/RunIISummer16NanoAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/NANOAODSIM'}
Samples['Wg_AMCNLOFXFX']  = {'nanoAOD' :'/WGToLNuG_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/RunIISummer16NanoAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/NANOAODSIM'}
Samples['Wg_AMCNLOFXFX_ext2']  = {'nanoAOD' :'/WGToLNuG_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/RunIISummer16NanoAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext2-v1/NANOAODSIM'}
Samples['Wg_AMCNLOFXFX_ext3']  = {'nanoAOD' :'/WGToLNuG_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/RunIISummer16NanoAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext3-v1/NANOAODSIM'}
Samples['Wg_MADGRAPHMLM']      = {'nanoAOD' :'/WGToLNuG_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16NanoAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/NANOAODSIM'}
Samples['WgStarLNuEE'] = {'nanoAOD' :'/WGstarToLNuEE_012Jets_13TeV-madgraph/RunIISummer16NanoAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/NANOAODSIM'}
Samples['WgStarLNuMuMu'] = {'nanoAOD' :'/WGstarToLNuMuMu_012Jets_13TeV-madgraph/RunIISummer16NanoAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/NANOAODSIM'}

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

### WW

Samples['WWTo2L2Nu']    = {'nanoAOD' :'/WWTo2L2Nu_13TeV-powheg/RunIISummer16NanoAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/NANOAODSIM'}
Samples['GluGluWWTo2L2Nu_MCFM']      = {'nanoAOD' :'/GluGluWWTo2L2Nu_MCFM_13TeV/RunIISummer16NanoAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/NANOAODSIM'}

#### WW PS

Samples['WWTo2L2NuHerwigPS']    = {'nanoAOD' :'/WWTo2L2Nu_13TeV-powheg-herwigpp/RunIISummer16NanoAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/NANOAODSIM'}

#### WW CUET variations 

Samples['WWTo2L2Nu_CUETUp']  = {'nanoAOD' :'/WWTo2L2Nu_13TeV-powheg-CUETP8M1Up/RunIISummer16NanoAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/NANOAODSIM'}
Samples['WWTo2L2Nu_CUETDown']  = {'nanoAOD' :'/WWTo2L2Nu_13TeV-powheg-CUETP8M1Down/RunIISummer16NanoAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/NANOAODSIM'}

Samples['WW-LO'] = {'nanoAOD' :'/WW_TuneCUETP8M1_13TeV-pythia8/RunIISummer16NanoAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/NANOAODSIM'}
Samples['WW-LOext1'] = {'nanoAOD' :'/WW_TuneCUETP8M1_13TeV-pythia8/RunIISummer16NanoAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/NANOAODSIM'}
Samples['WWTo2L2Nu_DoubleScattering'] = {'nanoAOD' :'/WWTo2L2Nu_DoubleScattering_13TeV-pythia8/RunIISummer16NanoAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/NANOAODSIM'}
Samples['WWTo4Q'] = {'nanoAOD' :'/WWTo4Q_13TeV-powheg/RunIISummer16NanoAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/NANOAODSIM'}
Samples['WWToLNuQQ'] = {'nanoAOD' :'/WWToLNuQQ_13TeV-powheg/RunIISummer16NanoAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/NANOAODSIM'}
Samples['WWToLNuQQ_AMCNLOFXFX'] = {'nanoAOD' :'/WWTo1L1Nu2Q_13TeV_amcatnloFXFX_madspin_pythia8/RunIISummer16NanoAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/NANOAODSIM'}
Samples['GluGluWWTo2L2NuHiggs_MCFM'] = {'nanoAOD' :'/GluGluWWTo2L2Nu_HInt_MCFM_13TeV/RunIISummer16NanoAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/NANOAODSIM'}

### VV

Samples['VVTo2L2Nu']         = {'nanoAOD' :'/VVTo2L2Nu_13TeV_amcatnloFXFX_madspin_pythia8/RunIISummer16NanoAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/NANOAODSIM'}
Samples['VVTo2L2Nu_ext1']         = {'nanoAOD' :'/VVTo2L2Nu_13TeV_amcatnloFXFX_madspin_pythia8/RunIISummer16NanoAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/NANOAODSIM'}

### Top
Samples['TTTo2L2Nu'] = {'nanoAOD' :'/TTTo2L2Nu_TuneCUETP8M2_ttHtranche3_13TeV-powheg-pythia8/RunIISummer16NanoAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/NANOAODSIM'}
Samples['TTJets_more'] = {'nanoAOD' :'/TTJets_TuneCUETP8M2T4_13TeV-amcatnloFXFX-pythia8/RunIISummer16NanoAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/NANOAODSIM'}
Samples['TTToSemiLeptonic'] = {'nanoAOD' :'/TTToSemilepton_TuneCUETP8M2_ttHtranche3_13TeV-powheg-pythia8/RunIISummer16NanoAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/NANOAODSIM'}
Samples['TT_TuneCUETP8M2T4'] = {'nanoAOD' :'/TT_TuneCUETP8M2T4_13TeV-powheg-pythia8/RunIISummer16NanoAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/NANOAODSIM'}


Samples['ST_t-channel_top']     = {'nanoAOD' :'/ST_t-channel_top_4f_inclusiveDecays_13TeV-powhegV2-madspin-pythia8_TuneCUETP8M1/RunIISummer16NanoAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/NANOAODSIM'}
Samples['ST_t-channel_antitop'] = {'nanoAOD' :'/ST_t-channel_antitop_4f_inclusiveDecays_13TeV-powhegV2-madspin-pythia8_TuneCUETP8M1/RunIISummer16NanoAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/NANOAODSIM'}
Samples['ST_tW_antitop']        = {'nanoAOD' :'/ST_tW_antitop_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/RunIISummer16NanoAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/NANOAODSIM'}
Samples['ST_tW_top']            = {'nanoAOD' :'/ST_tW_top_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1/RunIISummer16NanoAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/NANOAODSIM'}
Samples['ST_s-channel']         = {'nanoAOD' :'/ST_s-channel_4f_leptonDecays_13TeV-amcatnlo-pythia8_TuneCUETP8M1/RunIISummer16NanoAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/NANOAODSIM'}
Samples['ST_tW_antitop_noHad_ext1']            = {'nanoAOD' :'/ST_tW_antitop_5f_NoFullyHadronicDecays_13TeV-powheg_TuneCUETP8M1/RunIISummer16NanoAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/NANOAODSIM'}
Samples['ST_tW_top_noHad_ext1']            = {'nanoAOD' :'/ST_tW_top_5f_NoFullyHadronicDecays_13TeV-powheg_TuneCUETP8M1/RunIISummer16NanoAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/NANOAODSIM'}


### ttV

Samples['TTWJetsToLNu'] = {'nanoAOD' :'/TTWJetsToLNu_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/RunIISummer16NanoAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext2-v1/NANOAODSIM'}
Samples['TTWJetsToQQ'] = {'nanoAOD' :'/TTWJetsToQQ_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/RunIISummer16NanoAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/NANOAODSIM'}
Samples['TTZToQQ'] = {'nanoAOD' :'/TTZToQQ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/RunIISummer16NanoAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/NANOAODSIM'}
Samples['TTZjets'] = {'nanoAOD' :'/ttZJets_13TeV_madgraphMLM-pythia8/RunIISummer16NanoAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/NANOAODSIM'}
Samples['TTZToLLNuNu_M-10_ext2'] = {'nanoAOD' :'/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/RunIISummer16NanoAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext2-v1/NANOAODSIM'}
Samples['TTZToLLNuNu_M-10_ext3'] = {'nanoAOD' :'/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/RunIISummer16NanoAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext3-v1/NANOAODSIM'}

#### VVV >> Sang-il 
Samples['WWW']  = {'nanoAOD' :'/WWW_4F_TuneCUETP8M1_13TeV-amcatnlo-pythia8/RunIISummer16NanoAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/NANOAODSIM'}
Samples['WWZ']  = {'nanoAOD' :'/WWZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/RunIISummer16NanoAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/NANOAODSIM'}
Samples['WZZ']  = {'nanoAOD' :'/WZZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/RunIISummer16NanoAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/NANOAODSIM'}
Samples['ZZZ']  = {'nanoAOD' :'/ZZZ_TuneCUETP8M1_13TeV-amcatnlo-pythia8/RunIISummer16NanoAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/NANOAODSIM'}
Samples['WWG']  = {'nanoAOD' :'/WWG_TuneCUETP8M1_13TeV-amcatnlo-pythia8/RunIISummer16NanoAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v1/NANOAODSIM'}

### W+Jets
Samples['WJetsToLNu']                = {'nanoAOD' :'/WJetsToLNu_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/RunIISummer16NanoAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/NANOAODSIM'}
Samples['WJetsToLNu_ext2']                = {'nanoAOD' :'/WJetsToLNu_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/RunIISummer16NanoAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext2-v1/NANOAODSIM'}
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
Samples['WJetsToLNu_HT2500_inf'] = {'nanoAOD' :'/WJetsToLNu_HT-2500ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16NanoAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/NANOAODSIM'}
Samples['WJetsToLNu_HT2500_inf_ext1'] = {'nanoAOD' :'/WJetsToLNu_HT-2500ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16NanoAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/NANOAODSIM'}

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
Samples['DYJetsToLL_M-50_HT-100to200']                  = {'nanoAOD' :'/DYJetsToLL_M-50_HT-100to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16NanoAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/NANOAODSIM'}
Samples['DYJetsToLL_M-50_HT-100to200_ext1']                  = {'nanoAOD' :'/DYJetsToLL_M-50_HT-100to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16NanoAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/NANOAODSIM'}
Samples['DYJetsToLL_M-50_HT-200to400']                  = {'nanoAOD' :'/DYJetsToLL_M-50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16NanoAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/NANOAODSIM'}
Samples['DYJetsToLL_M-50_HT-200to400_ext1']                  = {'nanoAOD' :'/DYJetsToLL_M-50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16NanoAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/NANOAODSIM'}
Samples['DYJetsToLL_M-50_HT-400to600']                  = {'nanoAOD' :'/DYJetsToLL_M-50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16NanoAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/NANOAODSIM'}
Samples['DYJetsToLL_M-50_HT-400to600_ext1']                  = {'nanoAOD' :'/DYJetsToLL_M-50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16NanoAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/NANOAODSIM'}
Samples['DYJetsToLL_M-50_HT-600to800']                  = {'nanoAOD' :'/DYJetsToLL_M-50_HT-600to800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16NanoAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/NANOAODSIM'}
Samples['DYJetsToLL_M-50_HT-800to1200']                  = {'nanoAOD' :'/DYJetsToLL_M-50_HT-800to1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16NanoAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/NANOAODSIM'}
Samples['DYJetsToLL_M-50_HT-1200to2500']                  = {'nanoAOD' :'/DYJetsToLL_M-50_HT-1200to2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16NanoAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/NANOAODSIM'}
Samples['DYJetsToLL_M-50_HT-2500toinf']                  = {'nanoAOD' :'/DYJetsToLL_M-50_HT-2500toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16NanoAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/NANOAODSIM'}

#### DY->TauTau->MuEle Decay

Samples['DYJetsToTT_MuEle_M-50']                  = {'nanoAOD' :'/DYJetsToTauTau_ForcedMuEleDecay_M-50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/RunIISummer16NanoAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/NANOAODSIM'} 

### QCD fakes
Samples['QCD_Pt_15to20_bcToE']             = {'nanoAOD' :'/QCD_Pt_15to20_bcToE_TuneCUETP8M1_13TeV_pythia8/RunIISummer16NanoAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/NANOAODSIM'}
Samples['QCD_Pt_20to30_bcToE']             = {'nanoAOD' :'/QCD_Pt_20to30_bcToE_TuneCUETP8M1_13TeV_pythia8/RunIISummer16NanoAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/NANOAODSIM'}
Samples['QCD_Pt_30to80_bcToE']             = {'nanoAOD' :'/QCD_Pt_30to80_bcToE_TuneCUETP8M1_13TeV_pythia8/RunIISummer16NanoAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/NANOAODSIM'}
#Samples['QCD_Pt_80to170_bcToE']            = {'nanoAOD' :'/QCD_Pt_80to170_bcToE_TuneCUETP8M1_13TeV_pythia8/RunIISummer16NanoAOD-PUMoriond17_05Feb2018_backup_94X_mcRun2_asymptotic_v2-v1/NANOAODSIM'}
Samples['QCD_Pt_170to250_bcToE']           = {'nanoAOD' :'/QCD_Pt_170to250_bcToE_TuneCUETP8M1_13TeV_pythia8/RunIISummer16NanoAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/NANOAODSIM'}
Samples['QCD_Pt_250toInf_bcToE']           = {'nanoAOD' :'/QCD_Pt_250toInf_bcToE_TuneCUETP8M1_13TeV_pythia8/RunIISummer16NanoAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/NANOAODSIM'}
Samples['QCD_Pt-15to20_MuEnrichedPt5']     = {'nanoAOD' :'/QCD_Pt-15to20_MuEnrichedPt5_TuneCUETP8M1_13TeV_pythia8/RunIISummer16NanoAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/NANOAODSIM'}
Samples['QCD_Pt-20toInf_MuEnrichedPt15']   = {'nanoAOD' :'/QCD_Pt-20toInf_MuEnrichedPt15_TuneCUETP8M1_13TeV_pythia8/RunIISummer16NanoAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/NANOAODSIM'}
Samples['QCD_Pt-20to30_EMEnriched']        = {'nanoAOD' :'/QCD_Pt-20to30_EMEnriched_TuneCUETP8M1_13TeV_pythia8/RunIISummer16NanoAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/NANOAODSIM'}
Samples['QCD_Pt-30to50_EMEnriched']        = {'nanoAOD' :'/QCD_Pt-30to50_EMEnriched_TuneCUETP8M1_13TeV_pythia8/RunIISummer16NanoAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/NANOAODSIM'}
Samples['QCD_Pt-30to50_EMEnriched_ext1']        = {'nanoAOD' :'/QCD_Pt-30to50_EMEnriched_TuneCUETP8M1_13TeV_pythia8/RunIISummer16NanoAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/NANOAODSIM'}
Samples['QCD_Pt-50to80_EMEnriched']        = {'nanoAOD' :'/QCD_Pt-50to80_EMEnriched_TuneCUETP8M1_13TeV_pythia8/RunIISummer16NanoAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/NANOAODSIM'}
Samples['QCD_Pt-50to80_EMEnriched_ext1']        = {'nanoAOD' :'/QCD_Pt-50to80_EMEnriched_TuneCUETP8M1_13TeV_pythia8/RunIISummer16NanoAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3_ext1-v2/NANOAODSIM'}
Samples['QCD_Pt-30toInf_DoubleEMEnriched'] = {'nanoAOD' :'/QCD_Pt-30toInf_DoubleEMEnriched_MGG-40to80_TuneCUETP8M1_13TeV_Pythia8/RunIISummer16NanoAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/NANOAODSIM'}

### Signals

#### gg->H->WW


#Samples['GluGluHToWWTo2L2Nu_Mlarge'] = {'nanoAOD' :'/GluGluHToWWTo2L2Nu_M125_W10_13TeV_powheg_JHUgen_pythia8/RunIISummer16NanoAOD-PUMoriond17_05Feb2018_94X_mcRun2_asymptotic_v2-v1/NANOAODSIM'}
#Samples['GluGluHToWWTo2L2Nu_alternative_M125'] = {'nanoAOD' :'/GluGluHToWWTo2L2Nu_M125_13TeV_powheg_JHUgen_pythia8/RunIISummer16NanoAOD-PUMoriond17_05Feb2018_94X_mcRun2_asymptotic_v2-v1/NANOAODSIM'}


#Samples['GluGluHToWWTo2L2Nu_M115'] = {'nanoAOD' :'/GluGluHToWWTo2L2Nu_M115_13TeV_powheg_JHUgenv628_pythia8/RunIISummer16NanoAOD-PUMoriond17_05Feb2018_94X_mcRun2_asymptotic_v2-v1/NANOAODSIM'}
#Samples['GluGluHToWWTo2L2Nu_M120'] = {'nanoAOD' :'/GluGluHToWWTo2L2Nu_M120_13TeV_powheg_JHUgenv628_pythia8/RunIISummer16NanoAOD-PUMoriond17_05Feb2018_94X_mcRun2_asymptotic_v2-v1/NANOAODSIM'}
#Samples['GluGluHToWWTo2L2Nu_M124'] = {'nanoAOD' :'/GluGluHToWWTo2L2Nu_M124_13TeV_powheg_JHUgenv628_pythia8/RunIISummer16NanoAOD-PUMoriond17_05Feb2018_94X_mcRun2_asymptotic_v2-v1/NANOAODSIM'}
Samples['GluGluHToWWTo2L2Nu_M125']       = {'nanoAOD' :'/GluGluHToWWTo2L2Nu_M125_13TeV_powheg_JHUgenv628_pythia8/RunIISummer16NanoAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/NANOAODSIM'}
#Samples['GluGluHToWWTo2L2Nu_M126'] = {'nanoAOD' :'/GluGluHToWWTo2L2Nu_M126_13TeV_powheg_JHUgenv628_pythia8/RunIISummer16NanoAOD-PUMoriond17_05Feb2018_94X_mcRun2_asymptotic_v2-v1/NANOAODSIM'}
#Samples['GluGluHToWWTo2L2Nu_M130'] = {'nanoAOD' :'/GluGluHToWWTo2L2Nu_M130_13TeV_powheg_JHUgenv628_pythia8/RunIISummer16NanoAOD-PUMoriond17_05Feb2018_94X_mcRun2_asymptotic_v2-v1/NANOAODSIM'}
#Samples['GluGluHToWWTo2L2Nu_M135'] = {'nanoAOD' :'/GluGluHToWWTo2L2Nu_M135_13TeV_powheg_JHUgenv628_pythia8/RunIISummer16NanoAOD-PUMoriond17_05Feb2018_94X_mcRun2_asymptotic_v2-v1/NANOAODSIM'}
#Samples['GluGluHToWWTo2L2Nu_M140'] = {'nanoAOD' :'/GluGluHToWWTo2L2Nu_M140_13TeV_powheg_JHUgenv628_pythia8/RunIISummer16NanoAOD-PUMoriond17_05Feb2018_94X_mcRun2_asymptotic_v2-v1/NANOAODSIM'}
#Samples['GluGluHToWWTo2L2Nu_M145'] = {'nanoAOD' :'/GluGluHToWWTo2L2Nu_M145_13TeV_powheg_JHUgenv628_pythia8/RunIISummer16NanoAOD-PUMoriond17_05Feb2018_94X_mcRun2_asymptotic_v2-v1/NANOAODSIM'}
#Samples['GluGluHToWWTo2L2Nu_M150'] = {'nanoAOD' :'/GluGluHToWWTo2L2Nu_M150_13TeV_powheg_JHUgenv628_pythia8/RunIISummer16NanoAOD-PUMoriond17_05Feb2018_94X_mcRun2_asymptotic_v2-v1/NANOAODSIM'}
#Samples['GluGluHToWWTo2L2Nu_M155'] = {'nanoAOD' :'/GluGluHToWWTo2L2Nu_M155_13TeV_powheg_JHUgenv628_pythia8/RunIISummer16NanoAOD-PUMoriond17_05Feb2018_94X_mcRun2_asymptotic_v2-v1/NANOAODSIM'}
#Samples['GluGluHToWWTo2L2Nu_M160'] = {'nanoAOD' :'/GluGluHToWWTo2L2Nu_M160_13TeV_powheg_JHUgenv628_pythia8/RunIISummer16NanoAOD-PUMoriond17_05Feb2018_94X_mcRun2_asymptotic_v2-v1/NANOAODSIM'}
#Samples['GluGluHToWWTo2L2Nu_M165'] = {'nanoAOD' :'/GluGluHToWWTo2L2Nu_M165_13TeV_powheg_JHUgenv628_pythia8/RunIISummer16NanoAOD-PUMoriond17_05Feb2018_94X_mcRun2_asymptotic_v2-v1/NANOAODSIM'}
#Samples['GluGluHToWWTo2L2Nu_M170'] = {'nanoAOD' :'/GluGluHToWWTo2L2Nu_M170_13TeV_powheg_JHUgenv628_pythia8/RunIISummer16NanoAOD-PUMoriond17_05Feb2018_94X_mcRun2_asymptotic_v2-v1/NANOAODSIM'}
#Samples['GluGluHToWWTo2L2Nu_M175'] = {'nanoAOD' :'/GluGluHToWWTo2L2Nu_M175_13TeV_powheg_JHUgenv628_pythia8/RunIISummer16NanoAOD-PUMoriond17_05Feb2018_94X_mcRun2_asymptotic_v2-v1/NANOAODSIM'}
#Samples['GluGluHToWWTo2L2Nu_M180'] = {'nanoAOD' :'/GluGluHToWWTo2L2Nu_M180_13TeV_powheg_JHUgenv628_pythia8/RunIISummer16NanoAOD-PUMoriond17_05Feb2018_94X_mcRun2_asymptotic_v2-v1/NANOAODSIM'}
#Samples['GluGluHToWWTo2L2Nu_M190'] = {'nanoAOD' :'/GluGluHToWWTo2L2Nu_M190_13TeV_powheg_JHUgenv628_pythia8/RunIISummer16NanoAOD-PUMoriond17_05Feb2018_94X_mcRun2_asymptotic_v2-v1/NANOAODSIM'}
#Samples['GluGluHToWWTo2L2Nu_M200'] = {'nanoAOD' :'/GluGluHToWWTo2L2Nu_M200_13TeV_powheg_JHUgenv628_pythia8/RunIISummer16NanoAOD-PUMoriond17_05Feb2018_94X_mcRun2_asymptotic_v2-v1/NANOAODSIM'}
Samples['GluGluHToWWTo2L2Nu_M210'] = {'nanoAOD' :'/GluGluHToWWTo2L2Nu_M210_13TeV_powheg_JHUgenv628_pythia8/RunIISummer16NanoAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/NANOAODSIM'}
Samples['GluGluHToWWTo2L2Nu_M230'] = {'nanoAOD' :'/GluGluHToWWTo2L2Nu_M230_13TeV_powheg_JHUgenv628_pythia8/RunIISummer16NanoAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/NANOAODSIM'}
Samples['GluGluHToWWTo2L2Nu_M250'] = {'nanoAOD' :'/GluGluHToWWTo2L2Nu_M250_13TeV_powheg_JHUgenv628_pythia8/RunIISummer16NanoAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/NANOAODSIM'}
Samples['GluGluHToWWTo2L2Nu_M270'] = {'nanoAOD' :'/GluGluHToWWTo2L2Nu_M270_13TeV_powheg_JHUgenv628_pythia8/RunIISummer16NanoAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/NANOAODSIM'}
Samples['GluGluHToWWTo2L2Nu_JHUGen698_M300'] = {'nanoAOD' :'/GluGluHToWWTo2L2Nu_M300_13TeV_powheg_JHUgenv698_pythia8/RunIISummer16NanoAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/NANOAODSIM'}
Samples['GluGluHToWWTo2L2Nu_JHUGen698_M400'] = {'nanoAOD' :'/GluGluHToWWTo2L2Nu_M400_13TeV_powheg_JHUgenv698_pythia8/RunIISummer16NanoAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/NANOAODSIM'}
Samples['GluGluHToWWTo2L2Nu_JHUGen698_M450'] = {'nanoAOD' :'/GluGluHToWWTo2L2Nu_M450_13TeV_powheg_JHUgenv698_pythia8/RunIISummer16NanoAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/NANOAODSIM'}
Samples['GluGluHToWWTo2L2Nu_JHUGen698_M500'] = {'nanoAOD' :'/GluGluHToWWTo2L2Nu_M500_13TeV_powheg_JHUgenv698_pythia8/RunIISummer16NanoAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/NANOAODSIM'}
Samples['GluGluHToWWTo2L2Nu_JHUGen698_M550'] = {'nanoAOD' :'/GluGluHToWWTo2L2Nu_M550_13TeV_powheg_JHUgenv698_pythia8/RunIISummer16NanoAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/NANOAODSIM'}
Samples['GluGluHToWWTo2L2Nu_JHUGen698_M600'] = {'nanoAOD' :'/GluGluHToWWTo2L2Nu_M600_13TeV_powheg_JHUgenv698_pythia8/RunIISummer16NanoAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/NANOAODSIM'}
Samples['GluGluHToWWTo2L2Nu_JHUGen698_M650'] = {'nanoAOD' :'/GluGluHToWWTo2L2Nu_M650_13TeV_powheg_JHUgenv698_pythia8/RunIISummer16NanoAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/NANOAODSIM'}
Samples['GluGluHToWWTo2L2Nu_JHUGen698_M700'] = {'nanoAOD' :'/GluGluHToWWTo2L2Nu_M700_13TeV_powheg_JHUgenv698_pythia8/RunIISummer16NanoAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/NANOAODSIM'}
Samples['GluGluHToWWTo2L2Nu_JHUGen698_M750'] = {'nanoAOD' :'/GluGluHToWWTo2L2Nu_M750_13TeV_powheg_JHUgenv698_pythia8/RunIISummer16NanoAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/NANOAODSIM'}
Samples['GluGluHToWWTo2L2Nu_JHUGen698_M800'] = {'nanoAOD' :'/GluGluHToWWTo2L2Nu_M800_13TeV_powheg_JHUgenv698_pythia8/RunIISummer16NanoAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/NANOAODSIM'}
Samples['GluGluHToWWTo2L2Nu_JHUGen698_M900'] = {'nanoAOD' :'/GluGluHToWWTo2L2Nu_M900_13TeV_powheg_JHUgenv698_pythia8/RunIISummer16NanoAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/NANOAODSIM'}
Samples['GluGluHToWWTo2L2Nu_JHUGen698_M1000'] = {'nanoAOD' :'/GluGluHToWWTo2L2Nu_M1000_13TeV_powheg_JHUgenv698_pythia8/RunIISummer16NanoAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/NANOAODSIM'}
Samples['GluGluHToWWTo2L2Nu_JHUGen698_M1500'] = {'nanoAOD' :'/GluGluHToWWTo2L2Nu_M1500_13TeV_powheg_JHUgenv698_pythia8/RunIISummer16NanoAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/NANOAODSIM'}
Samples['GluGluHToWWTo2L2Nu_JHUGen698_M2000'] = {'nanoAOD' :'/GluGluHToWWTo2L2Nu_M2000_13TeV_powheg_JHUgenv698_pythia8/RunIISummer16NanoAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/NANOAODSIM'}
Samples['GluGluHToWWTo2L2Nu_JHUGen698_M2500'] = {'nanoAOD' :'/GluGluHToWWTo2L2Nu_M2500_13TeV_powheg_JHUgenv698_pythia8/RunIISummer16NanoAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/NANOAODSIM'}
Samples['GluGluHToWWTo2L2Nu_JHUGen698_M3000'] = {'nanoAOD' :'/GluGluHToWWTo2L2Nu_M3000_13TeV_powheg_JHUgenv698_pythia8/RunIISummer16NanoAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/NANOAODSIM'}

#Samples['GluGluHToWWTo2L2NuAMCNLO_M125'] = {'nanoAOD' :'/GluGluHToWWTo2L2Nu_M125_13TeV_amcatnloFXFX_pythia8/RunIISummer16NanoAOD-PUMoriond17_05Feb2018_94X_mcRun2_asymptotic_v2-v1/NANOAODSIM'}
#Samples['GluGluHToWWTo2L2NuPowheg_M125'] = {'nanoAOD' :'/GluGluHToWWTo2L2Nu_M125_13TeV_powheg_pythia8/RunIISummer16NanoAOD-PUMoriond17_05Feb2018_94X_mcRun2_asymptotic_v2-v1/NANOAODSIM'}
Samples['GluGluHToTauTau_M125']          = {'nanoAOD' :'/GluGluHToTauTau_M125_13TeV_powheg_pythia8/RunIISummer16NanoAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/NANOAODSIM'}
Samples['GluGluHToWWTo2L2Nu_M125_herwigpp'] = {'nanoAOD' :'/GluGluHToWWTo2L2Nu_M125_13TeV_powheg_JHUgen_herwigpp/RunIISummer16NanoAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/NANOAODSIM'}
Samples['GluGluHToWWTo2L2Nu_M125_CUETDown'] = {'nanoAOD' :'GluGluHToWWTo2L2Nu_M125_13TeV_powheg_JHUgen_pythia8-CUETP8M1Down/RunIISummer16NanoAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/NANOAODSIM'}
Samples['GluGluHToWWTo2L2Nu_M125_CUETUp']   = {'nanoAOD' :'/GluGluHToWWTo2L2Nu_M125_13TeV_powheg_JHUgen_pythia8-CUETP8M1Up/RunIISummer16NanoAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/NANOAODSIM'}
Samples['GluGluHToWWTo2L2Nu_M125_minloHJ_NNLOPS'] = {'nanoAOD' :'/GluGluHToWWTo2L2Nu_M125_13TeV_powheg_minloHJ_NNLOPS_JHUGenV702_pythia8/RunIISummer16NanoAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/NANOAODSIM'}

#### VBF ===============

#Samples['VBFHToWWTo2L2Nu_M115'] = {'nanoAOD' :'/VBFHToWWTo2L2Nu_M115_13TeV_powheg_JHUgenv628_pythia8/RunIISummer16NanoAOD-PUMoriond17_05Feb2018_94X_mcRun2_asymptotic_v2-v1/NANOAODSIM'}
#Samples['VBFHToWWTo2L2Nu_M120'] = {'nanoAOD' :'/VBFHToWWTo2L2Nu_M120_13TeV_powheg_JHUgenv628_pythia8/RunIISummer16NanoAOD-PUMoriond17_05Feb2018_94X_mcRun2_asymptotic_v2-v1/NANOAODSIM'}
#Samples['VBFHToWWTo2L2Nu_M124'] = {'nanoAOD' :'/VBFHToWWTo2L2Nu_M124_13TeV_powheg_JHUgenv628_pythia8/RunIISummer16NanoAOD-PUMoriond17_05Feb2018_94X_mcRun2_asymptotic_v2-v1/NANOAODSIM'}
Samples['VBFHToWWTo2L2Nu_M125']  = {'nanoAOD' :'/VBFHToWWTo2L2Nu_M125_13TeV_powheg_JHUgenv628_pythia8/RunIISummer16NanoAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/NANOAODSIM'}
#Samples['VBFHToWWTo2L2Nu_M126'] = {'nanoAOD' :'/VBFHToWWTo2L2Nu_M126_13TeV_powheg_JHUgenv628_pythia8/RunIISummer16NanoAOD-PUMoriond17_05Feb2018_94X_mcRun2_asymptotic_v2-v1/NANOAODSIM'}
#Samples['VBFHToWWTo2L2Nu_M130'] = {'nanoAOD' :'/VBFHToWWTo2L2Nu_M130_13TeV_powheg_JHUgenv628_pythia8/RunIISummer16NanoAOD-PUMoriond17_05Feb2018_94X_mcRun2_asymptotic_v2-v1/NANOAODSIM'}
#Samples['VBFHToWWTo2L2Nu_M135'] = {'nanoAOD' :'/VBFHToWWTo2L2Nu_M135_13TeV_powheg_JHUgenv628_pythia8/RunIISummer16NanoAOD-PUMoriond17_05Feb2018_94X_mcRun2_asymptotic_v2-v1/NANOAODSIM'}
#Samples['VBFHToWWTo2L2Nu_M140'] = {'nanoAOD' :'/VBFHToWWTo2L2Nu_M140_13TeV_powheg_JHUgenv628_pythia8/RunIISummer16NanoAOD-PUMoriond17_05Feb2018_94X_mcRun2_asymptotic_v2-v1/NANOAODSIM'}
#Samples['VBFHToWWTo2L2Nu_M145'] = {'nanoAOD' :'/VBFHToWWTo2L2Nu_M145_13TeV_powheg_JHUgenv628_pythia8/RunIISummer16NanoAOD-PUMoriond17_05Feb2018_94X_mcRun2_asymptotic_v2-v1/NANOAODSIM'}
#Samples['VBFHToWWTo2L2Nu_M150'] = {'nanoAOD' :'/VBFHToWWTo2L2Nu_M150_13TeV_powheg_JHUgenv628_pythia8/RunIISummer16NanoAOD-PUMoriond17_05Feb2018_94X_mcRun2_asymptotic_v2-v1/NANOAODSIM'}
#Samples['VBFHToWWTo2L2Nu_M155'] = {'nanoAOD' :'/VBFHToWWTo2L2Nu_M155_13TeV_powheg_JHUgenv628_pythia8/RunIISummer16NanoAOD-PUMoriond17_05Feb2018_94X_mcRun2_asymptotic_v2-v1/NANOAODSIM'}
#Samples['VBFHToWWTo2L2Nu_M160'] = {'nanoAOD' :'/VBFHToWWTo2L2Nu_M160_13TeV_powheg_JHUgenv628_pythia8/RunIISummer16NanoAOD-PUMoriond17_05Feb2018_94X_mcRun2_asymptotic_v2-v1/NANOAODSIM'}
#Samples['VBFHToWWTo2L2Nu_M165'] = {'nanoAOD' :'/VBFHToWWTo2L2Nu_M165_13TeV_powheg_JHUgenv628_pythia8/RunIISummer16NanoAOD-PUMoriond17_05Feb2018_94X_mcRun2_asymptotic_v2-v1/NANOAODSIM'}
#Samples['VBFHToWWTo2L2Nu_M170'] = {'nanoAOD' :'/VBFHToWWTo2L2Nu_M170_13TeV_powheg_JHUgenv628_pythia8/RunIISummer16NanoAOD-PUMoriond17_05Feb2018_94X_mcRun2_asymptotic_v2-v1/NANOAODSIM'}
#Samples['VBFHToWWTo2L2Nu_M175'] = {'nanoAOD' :'/VBFHToWWTo2L2Nu_M175_13TeV_powheg_JHUgenv628_pythia8/RunIISummer16NanoAOD-PUMoriond17_05Feb2018_94X_mcRun2_asymptotic_v2-v1/NANOAODSIM'}
#Samples['VBFHToWWTo2L2Nu_M180'] = {'nanoAOD' :'/VBFHToWWTo2L2Nu_M180_13TeV_powheg_JHUgenv628_pythia8/RunIISummer16NanoAOD-PUMoriond17_05Feb2018_94X_mcRun2_asymptotic_v2-v1/NANOAODSIM'}
Samples['VBFHToWWTo2L2Nu_M190'] = {'nanoAOD' :'/VBFHToWWTo2L2Nu_M190_13TeV_powheg_JHUgenv628_pythia8/RunIISummer16NanoAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/NANOAODSIM'}
Samples['VBFHToWWTo2L2Nu_M200'] = {'nanoAOD' :'/VBFHToWWTo2L2Nu_M200_13TeV_powheg_JHUgenv628_pythia8/RunIISummer16NanoAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/NANOAODSIM'}
Samples['VBFHToWWTo2L2Nu_M210'] = {'nanoAOD' :'/VBFHToWWTo2L2Nu_M210_13TeV_powheg_JHUgenv628_pythia8/RunIISummer16NanoAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/NANOAODSIM'}
Samples['VBFHToWWTo2L2Nu_M230'] = {'nanoAOD' :'/VBFHToWWTo2L2Nu_M230_13TeV_powheg_JHUgenv628_pythia8/RunIISummer16NanoAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/NANOAODSIM'}
Samples['VBFHToWWTo2L2Nu_M250'] = {'nanoAOD' :'/VBFHToWWTo2L2Nu_M250_13TeV_powheg_JHUgenv628_pythia8/RunIISummer16NanoAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/NANOAODSIM'}
Samples['VBFHToWWTo2L2Nu_M270'] = {'nanoAOD' :'/VBFHToWWTo2L2Nu_M270_13TeV_powheg_JHUgenv628_pythia8/RunIISummer16NanoAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/NANOAODSIM'}

Samples['VBFHToWWTo2L2Nu_JHUGen698_M300']         = {'nanoAOD' :'/VBFHToWWTo2L2Nu_M300_13TeV_powheg_JHUgenv698_pythia8/RunIISummer16NanoAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/NANOAODSIM'}
Samples['VBFHToWWTo2L2Nu_JHUGen698_M350']         = {'nanoAOD' :'/VBFHToWWTo2L2Nu_M350_13TeV_powheg_JHUgenv698_pythia8/RunIISummer16NanoAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/NANOAODSIM'}
Samples['VBFHToWWTo2L2Nu_JHUGen698_M400']         = {'nanoAOD' :'/VBFHToWWTo2L2Nu_M400_13TeV_powheg_JHUgenv698_pythia8/RunIISummer16NanoAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/NANOAODSIM'}
Samples['VBFHToWWTo2L2Nu_JHUGen698_M450']         = {'nanoAOD' :'/VBFHToWWTo2L2Nu_M450_13TeV_powheg_JHUgenv698_pythia8/RunIISummer16NanoAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/NANOAODSIM'}
Samples['VBFHToWWTo2L2Nu_JHUGen698_M500']         = {'nanoAOD' :'/VBFHToWWTo2L2Nu_M500_13TeV_powheg_JHUgenv698_pythia8/RunIISummer16NanoAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/NANOAODSIM'}
Samples['VBFHToWWTo2L2Nu_JHUGen698_M550']         = {'nanoAOD' :'/VBFHToWWTo2L2Nu_M550_13TeV_powheg_JHUgenv698_pythia8/RunIISummer16NanoAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/NANOAODSIM'}
Samples['VBFHToWWTo2L2Nu_JHUGen698_M600']         = {'nanoAOD' :'/VBFHToWWTo2L2Nu_M600_13TeV_powheg_JHUgenv698_pythia8/RunIISummer16NanoAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/NANOAODSIM'}
Samples['VBFHToWWTo2L2Nu_JHUGen698_M650']         = {'nanoAOD' :'/VBFHToWWTo2L2Nu_M650_13TeV_powheg_JHUgenv698_pythia8/RunIISummer16NanoAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/NANOAODSIM'}
Samples['VBFHToWWTo2L2Nu_JHUGen698_M700']         = {'nanoAOD' :'/VBFHToWWTo2L2Nu_M700_13TeV_powheg_JHUgenv698_pythia8/RunIISummer16NanoAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/NANOAODSIM'}
Samples['VBFHToWWTo2L2Nu_JHUGen698_M750']         = {'nanoAOD' :'/VBFHToWWTo2L2Nu_M750_13TeV_powheg_JHUgenv698_pythia8/RunIISummer16NanoAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/NANOAODSIM'}
Samples['VBFHToWWTo2L2Nu_JHUGen698_M800']         = {'nanoAOD' :'/VBFHToWWTo2L2Nu_M800_13TeV_powheg_JHUgenv698_pythia8/RunIISummer16NanoAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/NANOAODSIM'}
Samples['VBFHToWWTo2L2Nu_JHUGen698_M900']         = {'nanoAOD' :'/VBFHToWWTo2L2Nu_M900_13TeV_powheg_JHUgenv698_pythia8/RunIISummer16NanoAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/NANOAODSIM'}
Samples['VBFHToWWTo2L2Nu_JHUGen698_M1000']         = {'nanoAOD' :'/VBFHToWWTo2L2Nu_M1000_13TeV_powheg_JHUgenv698_pythia8/RunIISummer16NanoAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/NANOAODSIM'}
Samples['VBFHToWWTo2L2Nu_JHUGen698_M1500']         = {'nanoAOD' :'/VBFHToWWTo2L2Nu_M1500_13TeV_powheg_JHUgenv698_pythia8/RunIISummer16NanoAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/NANOAODSIM'}
Samples['VBFHToWWTo2L2Nu_JHUGen698_M2000']         = {'nanoAOD' :'/VBFHToWWTo2L2Nu_M2000_13TeV_powheg_JHUgenv698_pythia8/RunIISummer16NanoAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/NANOAODSIM'}
Samples['VBFHToWWTo2L2Nu_JHUGen698_M2500']         = {'nanoAOD' :'/VBFHToWWTo2L2Nu_M2500_13TeV_powheg_JHUgenv698_pythia8/RunIISummer16NanoAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/NANOAODSIM'}
Samples['VBFHToWWTo2L2Nu_JHUGen698_M3000']         = {'nanoAOD' :'/VBFHToWWTo2L2Nu_M3000_13TeV_powheg_JHUgenv698_pythia8/RunIISummer16NanoAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/NANOAODSIM'}

#Samples['VBFHToWWTo2L2NuPowheg_M125']   = {'nanoAOD' :'/VBFHToWWTo2L2Nu_M125_13TeV_powheg_pythia8/RunIISummer16NanoAOD-PUMoriond17_05Feb2018_94X_mcRun2_asymptotic_v2-v1/NANOAODSIM'}
#Samples['VBFHToWWTo2L2NuAMCNLO_M125']   = {'nanoAOD' :'/VBFHToWWTo2L2Nu_M125_13TeV_amcatnlo_pythia8/RunIISummer16NanoAOD-PUMoriond17_05Feb2018_94X_mcRun2_asymptotic_v2-v1/NANOAODSIM'}
Samples['VBFHToTauTau_M125']            = {'nanoAOD' :'/VBFHToTauTau_M125_13TeV_powheg_pythia8/RunIISummer16NanoAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/NANOAODSIM'}
Samples['VBFHToWWTo2L2Nu_M125_herwigpp'] = {'nanoAOD' :'/VBFHToWWTo2L2Nu_M125_13TeV_powheg_JHUgen_herwigpp/RunIISummer16NanoAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/NANOAODSIM'}
#Samples['VBFHToWWTo2L2Nu_alternative_M125']         = {'nanoAOD' :'/VBFHToWWTo2L2Nu_M125_13TeV_powheg_JHUgen_pythia8/RunIISummer16NanoAOD-PUMoriond17_05Feb2018_94X_mcRun2_asymptotic_v2-v1/NANOAODSIM'}
Samples['VBFHToWWTo2L2Nu_M125_CUETDown'] = {'nanoAOD' :'/VBFHToWWTo2L2Nu_M125_13TeV_powheg_JHUgen_pythia8-CUETP8M1Down/RunIISummer16NanoAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/NANOAODSIM'}
Samples['VBFHToWWTo2L2Nu_M125_CUETUp']   = {'nanoAOD' :'/VBFHToWWTo2L2Nu_M125_13TeV_powheg_JHUgen_pythia8-CUETP8M1Up/RunIISummer16NanoAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/NANOAODSIM'}

#### ggZH
Samples['ggZH_HToWW_M125']      = {'nanoAOD' :'/GluGluZH_HToWW_M125_13TeV_powheg_pythia8/RunIISummer16NanoAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/NANOAODSIM'}

#### ZH tautau 
Samples['HZJ_HToTauTau_M125'] = {'nanoAOD' :'/ZHToTauTau_M125_13TeV_powheg_pythia8/RunIISummer16NanoAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/NANOAODSIM'}

#### WH Exclusive

#Samples['HWminusJ_HToWW_LNu_M125']     = {'nanoAOD' :'/HWminusJ_HToWWTo2L2Nu_WToLNu_M125_13TeV_powheg_pythia8/RunIISummer16NanoAOD-PUMoriond17_05Feb2018_94X_mcRun2_asymptotic_v2-v1/NANOAODSIM'}
#Samples['HWplusJ_HToWW_LNu_M125']     = {'nanoAOD' :'/HWplusJ_HToWWTo2L2Nu_WToLNu_M125_13TeV_powheg_pythia8/RunIISummer16NanoAOD-PUMoriond17_05Feb2018_94X_mcRun2_asymptotic_v2-v1/NANOAODSIM'}

#### WH Inclusive============

Samples['HWminusJ_HToWW_M125']     = {'nanoAOD' :'/HWminusJ_HToWW_M125_13TeV_powheg_pythia8/RunIISummer16NanoAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/NANOAODSIM'}
Samples['HWplusJ_HToWW_M125']      = {'nanoAOD' :'/HWplusJ_HToWW_M125_13TeV_powheg_pythia8/RunIISummer16NanoAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/NANOAODSIM'}
Samples['HWminusJ_HToTauTau_M125'] = {'nanoAOD' :'/WminusHToTauTau_M125_13TeV_powheg_pythia8/RunIISummer16NanoAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/NANOAODSIM'}
Samples['HWplusJ_HToTauTau_M125']  = {'nanoAOD' :'/WplusHToTauTau_M125_13TeV_powheg_pythia8/RunIISummer16NanoAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/NANOAODSIM'}

#### ZH Inclusive ======== 

Samples['HZJ_HToWW_M125']     = {'nanoAOD' :'/HZJ_HToWW_M125_13TeV_powheg_pythia8/RunIISummer16NanoAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/NANOAODSIM'}
Samples['ggZZ4t'] = {'nanoAOD' :'/GluGluToContinToZZTo4tau_13TeV_MCFM701_pythia8/RunIISummer16NanoAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/NANOAODSIM'}
Samples['ggZZ4m'] = {'nanoAOD' :'/GluGluToContinToZZTo4mu_13TeV_MCFM701_pythia8/RunIISummer16NanoAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/NANOAODSIM'}
Samples['ggZZ4e'] = {'nanoAOD' :'/GluGluToContinToZZTo4e_13TeV_MCFM701_pythia8/RunIISummer16NanoAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/NANOAODSIM'}
Samples['ggZZ2m2t'] = {'nanoAOD' :'/GluGluToContinToZZTo2mu2tau_13TeV_MCFM701_pythia8/RunIISummer16NanoAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/NANOAODSIM'}
Samples['ggZZ2e2t'] = {'nanoAOD' :'/GluGluToContinToZZTo2e2tau_13TeV_MCFM701_pythia8/RunIISummer16NanoAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/NANOAODSIM'}
Samples['ggZZ2e2m'] = {'nanoAOD' :'/GluGluToContinToZZTo2e2mu_13TeV_MCFM701_pythia8/RunIISummer16NanoAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/NANOAODSIM'}
Samples['GluGluHToZZTo4L_M125'] = {'nanoAOD' :'/GluGluHToZZTo4L_M125_13TeV_powheg2_JHUgenV6_pythia8/RunIISummer16NanoAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/NANOAODSIM'}

#### bbH

Samples['bbHToWWTo2L2Nu_M125_ybyt'] = {'nanoAOD' :'/bbHToWWTo2L2Nu_M-125_4FS_ybyt_13TeV_amcatnlo/RunIISummer16NanoAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/NANOAODSIM'}
#Samples['bbHToWWTo2L2Nu_M125_yb2'] = {'nanoAOD' :'/bbHToWWTo2L2Nu_M-125_4FS_yb2_13TeV_amcatnlo/RunIISummer16NanoAOD-PUMoriond17_05Feb2018_94X_mcRun2_asymptotic_v2-v1/NANOAODSIM'}


