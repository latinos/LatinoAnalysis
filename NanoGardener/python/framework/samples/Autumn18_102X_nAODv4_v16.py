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

# Samples[''] = {'nanoAOD' :''}

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Giulio
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Samples['Zg'] = {'nanoAOD' :'/ZGToLLG_01J_5f_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIIAutumn18NanoAODv4-Nano14Dec2018_102X_upgrade2018_realistic_v16_ext1-v1/NANOAODSIM'}
Samples['Wg_AMCNLOFXFX'] = {'nanoAOD' :'/WGToLNuG_01J_5f_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIIAutumn18NanoAODv4-Nano14Dec2018_102X_upgrade2018_realistic_v16_ext1-v1/NANOAODSIM'}
Samples['WZTo3LNu'] = {'nanoAOD' :'/WZTo3LNu_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIIAutumn18NanoAODv4-Nano14Dec2018_102X_upgrade2018_realistic_v16-v1/NANOAODSIM'}
Samples['WZTo3LNu_ext1'] = {'nanoAOD' :'/WZTo3LNu_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIIAutumn18NanoAODv4-Nano14Dec2018_102X_upgrade2018_realistic_v16_ext1-v1/NANOAODSIM'}
Samples['WZTo3LNu_mllmin01'] = {'nanoAOD' :'/WZTo3LNu_mllmin01_NNPDF31_TuneCP5_13TeV_powheg_pythia8/RunIIAutumn18NanoAODv4-Nano14Dec2018_102X_upgrade2018_realistic_v16-v1/NANOAODSIM'}
### ZZTo4L_13TeV_powheg_pythia8 not found. Is this OK?
Samples['ZZTo4L_ext1'] = {'nanoAOD' :'/ZZTo4L_TuneCP5_13TeV_powheg_pythia8/RunIIAutumn18NanoAODv4-Nano14Dec2018_102X_upgrade2018_realistic_v16_ext1-v1/NANOAODSIM'}
Samples['ZZTo4L_ext2'] = {'nanoAOD' :'/ZZTo4L_TuneCP5_13TeV_powheg_pythia8/RunIIAutumn18NanoAODv4-Nano14Dec2018_102X_upgrade2018_realistic_v16_ext2-v1/NANOAODSIM'}
Samples['ZZTo2L2Nu_ext1'] = {'nanoAOD' :'/ZZTo2L2Nu_TuneCP5_13TeV_powheg_pythia8/RunIIAutumn18NanoAODv4-Nano14Dec2018_102X_upgrade2018_realistic_v16_ext1-v1/NANOAODSIM'} 
Samples['WZ'] = {'nanoAOD' :'/WZ_TuneCP5_13TeV-pythia8/RunIIAutumn18NanoAODv4-Nano14Dec2018_102X_upgrade2018_realistic_v16-v1/NANOAODSIM'}
Samples['WZTo2L2Q'] = {'nanoAOD' :'/WZTo2L2Q_13TeV_amcatnloFXFX_madspin_pythia8/RunIIAutumn18NanoAODv4-Nano14Dec2018_102X_upgrade2018_realistic_v16-v1/NANOAODSIM'}
Samples['ZZ'] = {'nanoAOD' :'/ZZ_TuneCP5_13TeV-pythia8/RunIIAutumn18NanoAODv4-Nano14Dec2018_102X_upgrade2018_realistic_v16-v1/NANOAODSIM'}
Samples['ZZTo2L2Q'] = {'nanoAOD' :'/ZZTo2L2Q_13TeV_amcatnloFXFX_madspin_pythia8/RunIIAutumn18NanoAODv4-Nano14Dec2018_102X_upgrade2018_realistic_v16-v1/NANOAODSIM'}
Samples['WWTo2L2Nu'] = {'nanoAOD' :'/WWTo2L2Nu_NNPDF31_TuneCP5_13TeV-powheg-pythia8/RunIIAutumn18NanoAODv4-Nano14Dec2018_102X_upgrade2018_realistic_v16-v1/NANOAODSIM'}
Samples['WWTo2L2Nu_CP5Up'] = {'nanoAOD' :'/WWTo2L2Nu_NNPDF31_TuneCP5Up_13TeV-powheg-pythia8/RunIIAutumn18NanoAODv4-Nano14Dec2018_102X_upgrade2018_realistic_v16-v1/NANOAODSIM'}
Samples['WWTo2L2Nu_CP5Down'] = {'nanoAOD' :'/WWTo2L2Nu_NNPDF31_TuneCP5Down_13TeV-powheg-pythia8/RunIIAutumn18NanoAODv4-Nano14Dec2018_102X_upgrade2018_realistic_v16-v1/NANOAODSIM'}
Samples['WW-LO'] = {'nanoAOD' :'/WW_TuneCP5_13TeV-pythia8/RunIIAutumn18NanoAODv4-Nano14Dec2018_102X_upgrade2018_realistic_v16-v1/NANOAODSIM'}
Samples['ZGToLLG'] = {'nanoAOD' :'/ZGToLLG_01J_5f_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIIAutumn18NanoAODv4-Nano14Dec2018_102X_upgrade2018_realistic_v16_ext1-v1/NANOAODSIM'}
Samples['GluGluToWWToENEN'] = {'nanoAOD' :'/GluGluToWWToENEN_TuneCP5_13TeV_MCFM701_pythia8/RunIIAutumn18NanoAODv4-Nano14Dec2018_102X_upgrade2018_realistic_v16-v1/NANOAODSIM'}
Samples['GluGluToWWToENMN'] = {'nanoAOD' :'/GluGluToWWToENMN_TuneCP5_13TeV_MCFM701_pythia8/RunIIAutumn18NanoAODv4-Nano14Dec2018_102X_upgrade2018_realistic_v16-v1/NANOAODSIM'}
Samples['GluGluToWWToENTN'] = {'nanoAOD' :'/GluGluToWWToENTN_TuneCP5_13TeV_MCFM701_pythia8/RunIIAutumn18NanoAODv4-Nano14Dec2018_102X_upgrade2018_realistic_v16-v1/NANOAODSIM'}
Samples['GluGluToWWToMNEN'] = {'nanoAOD' :'/GluGluToWWToMNEN_TuneCP5_13TeV_MCFM701_pythia8/RunIIAutumn18NanoAODv4-Nano14Dec2018_102X_upgrade2018_realistic_v16-v1/NANOAODSIM'}
Samples['GluGluToWWToMNMN'] = {'nanoAOD' :'/GluGluToWWToMNMN_TuneCP5_13TeV_MCFM701_pythia8/RunIIAutumn18NanoAODv4-Nano14Dec2018_102X_upgrade2018_realistic_v16-v1/NANOAODSIM'}
Samples['GluGluToWWToMNTN'] = {'nanoAOD' :'/GluGluToWWToMNTN_TuneCP5_13TeV_MCFM701_pythia8/RunIIAutumn18NanoAODv4-Nano14Dec2018_102X_upgrade2018_realistic_v16-v1/NANOAODSIM'}
Samples['GluGluToWWToTNEN'] = {'nanoAOD' :'/GluGluToWWToTNEN_TuneCP5_13TeV_MCFM701_pythia8/RunIIAutumn18NanoAODv4-Nano14Dec2018_102X_upgrade2018_realistic_v16-v1/NANOAODSIM'}
Samples['GluGluToWWToTNMN'] = {'nanoAOD' :'/GluGluToWWToTNMN_TuneCP5_13TeV_MCFM701_pythia8/RunIIAutumn18NanoAODv4-Nano14Dec2018_102X_upgrade2018_realistic_v16-v1/NANOAODSIM'}
Samples['GluGluToWWToTNTN'] = {'nanoAOD' :'/GluGluToWWToTNTN_TuneCP5_13TeV_MCFM701_pythia8/RunIIAutumn18NanoAODv4-Nano14Dec2018_102X_upgrade2018_realistic_v16-v1/NANOAODSIM'}

#Signals
Samples['VBFHToWWTo2L2NuPowheg_M125'] = {'nanoAOD' :'/VBFHToWWTo2L2Nu_M125_13TeV_powheg2_JHUGenV714_pythia8/RunIIAutumn18NanoAODv4-Nano14Dec2018_102X_upgrade2018_realistic_v16-v1/NANOAODSIM'}
### Samples['VBFHToWWTo2L2NuPowheg_M125_CP5Up']   = {'nanoAOD' : '' } ### Still missing
### Samples['VBFHToWWTo2L2NuPowheg_M125_CP5Down']   = {'nanoAOD' : '' } ### Still missing
### Samples['HZJ_HToTauTau_M125'] = {'nanoAOD' : '' } ### Still missing
### Samples['VBFHToTauTau_M125']            = {'nanoAOD' : '' } ### Still missing
Samples['GluGluHToWWTo2L2NuPowheg_M125'] = {'nanoAOD' :'/GluGluHToWWTo2L2Nu_M125_13TeV_powheg2_JHUGenV714_pythia8/RunIIAutumn18NanoAODv4-Nano14Dec2018_102X_upgrade2018_realistic_v16-v1/NANOAODSIM'}
Samples['GluGluHToWWTo2L2NuPowheg_M125_CP5Up'] = {'nanoAOD': '/GluGluHToWWTo2L2Nu_M125_13TeV_powheg2_JHUGenV714_pythia8-CP5Up/RunIIAutumn18NanoAODv4-Nano14Dec2018_102X_upgrade2018_realistic_v16-v1/NANOAODSIM'}
Samples['GluGluHToWWTo2L2NuPowheg_M125_CP5Down'] = {'nanoAOD': '/GluGluHToWWTo2L2Nu_M125_13TeV_powheg2_JHUGenV714_pythia8-CP5Down/RunIIAutumn18NanoAODv4-Nano14Dec2018_102X_upgrade2018_realistic_v16-v1/NANOAODSIM'}
### Samples['GluGluHToTauTau_M125']          = {'nanoAOD' :''} ### Still missing
### WH Exclusive 
### Samples['HWminusJ_HToWW_LNu_M125']     = {'nanoAOD' :''} ### Still missing
### Samples['HWplusJ_HToWW_LNu_M125']     = {'nanoAOD' :''} ### Still missing
#### WH Inclusive
Samples['HWminusJ_HToWW_M125']     = {'nanoAOD' :'/HWminusJ_HToWW_M125_13TeV_powheg_jhugen724_pythia8_TuneCP5/RunIIAutumn18NanoAODv4-Nano14Dec2018_102X_upgrade2018_realistic_v16-v1/NANOAODSIM'}
Samples['HWplusJ_HToWW_M125']      = {'nanoAOD' :'/HWplusJ_HToWW_M125_13TeV_powheg_jhugen724_pythia8_TuneCP5/RunIIAutumn18NanoAODv4-Nano14Dec2018_102X_upgrade2018_realistic_v16-v1/NANOAODSIM'}
### Samples['HWminusJ_HToTauTau_M125'] = {'nanoAOD' :''} ### Still missing
### Samples['HWplusJ_HToTauTau_M125']  = {'nanoAOD' :''} ### Still missing
#### ZH exclusive ======== 
Samples['HZJ_HToWWTo2L2Nu_M125'] = {'nanoAOD' : '/HZJ_HToWWTo2L2Nu_M125_13TeV_powheg_jhugen714_pythia8_TuneCP5/RunIIAutumn18NanoAODv4-Nano14Dec2018_102X_upgrade2018_realistic_v16-v1/NANOAODSIM'}
Samples['HZJ_HToWWTo2L2Nu_ZTo2L_M125'] = {'nanoAOD': '/HZJ_HToWWTo2L2Nu_ZTo2L_M125_13TeV_powheg_jhugen714_pythia8_TuneCP5/RunIIAutumn18NanoAODv4-Nano14Dec2018_102X_upgrade2018_realistic_v16-v1/NANOAODSIM'}
#### ZH Inclusive ========
### Samples['HZJ_HToWW_M120']     = {'nanoAOD' :''} ### Still missing
Samples['HZJ_HToWW_M125']     = {'nanoAOD' :'/HZJ_HToWW_M125_13TeV_powheg_jhugen714_pythia8_TuneCP5/RunIIAutumn18NanoAODv4-Nano14Dec2018_102X_upgrade2018_realistic_v16-v1/NANOAODSIM'}
### Samples['HZJ_HToTauTau_M125']     = {'nanoAOD' :''} ### Still missing
#### ggZH Inclusive ======== 
### Samples['GluGluZH_HToWW_M120']     = {'nanoAOD' :''} ### Still missing
Samples['GluGluZH_HToWW_M125'] = {'nanoAOD' :'/GluGluZH_HToWW_M125_13TeV_powheg_pythia8_TuneCP5_PSweights/RunIIAutumn18NanoAODv4-Nano14Dec2018_102X_upgrade2018_realistic_v16-v1/NANOAODSIM'}
### Samples['GluGluZH_HToWW_M130']     = {'nanoAOD' :''} ### Still missing
#### ggZH Exclusive ========
### Samples['GluGluZH_HToWWTo2L2Nu_ZTo2L_M120']     = {'nanoAOD' :''} ### Still missing
Samples['GluGluZH_HToWWTo2L2Nu_ZTo2L_M125'] = {'nanoAOD' :'/GluGluZH_HToWWTo2L2Nu_ZTo2L_M125_13TeV_powheg_pythia8_TuneCP5_PSweights/RunIIAutumn18NanoAODv4-Nano14Dec2018_102X_upgrade2018_realistic_v16-v1/NANOAODSIM'} ##!!!!
### Samples['GluGluZH_HToWWTo2L2Nu_ZTo2L_M130']     = {'nanoAOD' :''} ### Still missing
### Samples['GluGluZH_HToWWTo2L2Nu_M120']     = {'nanoAOD' :''} ### Still missing
Samples['GluGluZH_HToWWTo2L2Nu_M125'] = {'nanoAOD' :'/GluGluZH_HToWWTo2L2Nu_M125_13TeV_powheg_pythia8_TuneCP5_PSweights/RunIIAutumn18NanoAODv4-Nano14Dec2018_102X_upgrade2018_realistic_v16-v1/NANOAODSIM'} ##!!!!
### Samples['GluGluZH_HToWWTo2L2Nu_M130']     = {'nanoAOD' :''} ### Still missing
#### ttH Inclusive ========
Samples['ttHToNonbb_M125']     = {'nanoAOD' :'/ttHToNonbb_M125_TuneCP5_13TeV-powheg-pythia8/RunIIAutumn18NanoAODv4-Nano14Dec2018_102X_upgrade2018_realistic_v16-v1/NANOAODSIM'}

### bbH

#Samples['bbHToWWTo2L2Nu_M125_ybyt'] = {'nanoAOD' :'/bbHToWWTo2L2Nu_M-125_4FS_ybyt_13TeV_amcatnlo/RunIISummer16NanoAODv4-PUMoriond17_Nano14Dec2018_102X_mcRun2_asymptotic_v6-v1/NANOAODSIM'}
#Samples['bbHToWWTo2L2Nu_M125_yb2'] = {'nanoAOD' :'/bbHToWWTo2L2Nu_M-125_4FS_yb2_13TeV_amcatnlo/RunIISummer16NanoAOD-PUMoriond17_05Feb2018_94X_mcRun2_asymptotic_v2-v1/NANOAODSIM'}

## ggH HWW dilepton High mass

Samples['GluGluHToWWTo2L2Nu_M115'] = {'nanoAOD' :'/GluGluHToWWTo2L2Nu_M115_13TeV_powheg2_JHUGenV714_pythia8/RunIIAutumn18NanoAODv4-Nano14Dec2018_102X_upgrade2018_realistic_v16-v1/NANOAODSIM'}
Samples['GluGluHToWWTo2L2Nu_M120'] = {'nanoAOD' :'/GluGluHToWWTo2L2Nu_M120_13TeV_powheg2_JHUGenV714_pythia8/RunIIAutumn18NanoAODv4-Nano14Dec2018_102X_upgrade2018_realistic_v16-v1/NANOAODSIM'}
Samples['GluGluHToWWTo2L2Nu_M124'] = {'nanoAOD' :'/GluGluHToWWTo2L2Nu_M124_13TeV_powheg2_JHUGenV714_pythia8/RunIIAutumn18NanoAODv4-Nano14Dec2018_102X_upgrade2018_realistic_v16-v1/NANOAODSIM'}
Samples['GluGluHToWWTo2L2Nu_M125'] = {'nanoAOD' :'/GluGluHToWWTo2L2Nu_M125_13TeV_powheg2_JHUGenV714_pythia8/RunIIAutumn18NanoAODv4-Nano14Dec2018_102X_upgrade2018_realistic_v16-v1/NANOAODSIM'}
Samples['GluGluHToWWTo2L2Nu_M126'] = {'nanoAOD' :'/GluGluHToWWTo2L2Nu_M126_13TeV_powheg2_JHUGenV714_pythia8/RunIIAutumn18NanoAODv4-Nano14Dec2018_102X_upgrade2018_realistic_v16-v1/NANOAODSIM'}
Samples['GluGluHToWWTo2L2Nu_M130'] = {'nanoAOD' :'/GluGluHToWWTo2L2Nu_M130_13TeV_powheg2_JHUGenV714_pythia8/RunIIAutumn18NanoAODv4-Nano14Dec2018_102X_upgrade2018_realistic_v16-v1/NANOAODSIM'}
Samples['GluGluHToWWTo2L2Nu_M135'] = {'nanoAOD' :'/GluGluHToWWTo2L2Nu_M135_13TeV_powheg2_JHUGenV714_pythia8/RunIIAutumn18NanoAODv4-Nano14Dec2018_102X_upgrade2018_realistic_v16-v1/NANOAODSIM'}
Samples['GluGluHToWWTo2L2Nu_M140'] = {'nanoAOD' :'/GluGluHToWWTo2L2Nu_M140_13TeV_powheg2_JHUGenV714_pythia8/RunIIAutumn18NanoAODv4-Nano14Dec2018_102X_upgrade2018_realistic_v16-v1/NANOAODSIM'}
Samples['GluGluHToWWTo2L2Nu_M145'] = {'nanoAOD' :'/GluGluHToWWTo2L2Nu_M145_13TeV_powheg2_JHUGenV714_pythia8/RunIIAutumn18NanoAODv4-Nano14Dec2018_102X_upgrade2018_realistic_v16-v1/NANOAODSIM'}
Samples['GluGluHToWWTo2L2Nu_M150'] = {'nanoAOD' :'/GluGluHToWWTo2L2Nu_M150_13TeV_powheg2_JHUGenV714_pythia8/RunIIAutumn18NanoAODv4-Nano14Dec2018_102X_upgrade2018_realistic_v16-v1/NANOAODSIM'}
Samples['GluGluHToWWTo2L2Nu_M155'] = {'nanoAOD' :'/GluGluHToWWTo2L2Nu_M155_13TeV_powheg2_JHUGenV714_pythia8/RunIIAutumn18NanoAODv4-Nano14Dec2018_102X_upgrade2018_realistic_v16-v1/NANOAODSIM'}
Samples['GluGluHToWWTo2L2Nu_M160'] = {'nanoAOD' :'/GluGluHToWWTo2L2Nu_M160_13TeV_powheg2_JHUGenV714_pythia8/RunIIAutumn18NanoAODv4-Nano14Dec2018_102X_upgrade2018_realistic_v16-v1/NANOAODSIM'}
Samples['GluGluHToWWTo2L2Nu_M165'] = {'nanoAOD' :'/GluGluHToWWTo2L2Nu_M165_13TeV_powheg2_JHUGenV714_pythia8/RunIIAutumn18NanoAODv4-Nano14Dec2018_102X_upgrade2018_realistic_v16-v1/NANOAODSIM'}
Samples['GluGluHToWWTo2L2Nu_M170'] = {'nanoAOD' :'/GluGluHToWWTo2L2Nu_M170_13TeV_powheg2_JHUGenV714_pythia8/RunIIAutumn18NanoAODv4-Nano14Dec2018_102X_upgrade2018_realistic_v16-v1/NANOAODSIM'}
Samples['GluGluHToWWTo2L2Nu_M175'] = {'nanoAOD' :'/GluGluHToWWTo2L2Nu_M175_13TeV_powheg2_JHUGenV714_pythia8/RunIIAutumn18NanoAODv4-Nano14Dec2018_102X_upgrade2018_realistic_v16-v1/NANOAODSIM'}
Samples['GluGluHToWWTo2L2Nu_M180'] = {'nanoAOD' :'/GluGluHToWWTo2L2Nu_M180_13TeV_powheg2_JHUGenV714_pythia8/RunIIAutumn18NanoAODv4-Nano14Dec2018_102X_upgrade2018_realistic_v16-v1/NANOAODSIM'}
Samples['GluGluHToWWTo2L2Nu_M190'] = {'nanoAOD' :'/GluGluHToWWTo2L2Nu_M190_13TeV_powheg2_JHUGenV714_pythia8/RunIIAutumn18NanoAODv4-Nano14Dec2018_102X_upgrade2018_realistic_v16-v1/NANOAODSIM'}
Samples['GluGluHToWWTo2L2Nu_M200'] = {'nanoAOD' :'/GluGluHToWWTo2L2Nu_M200_13TeV_powheg2_JHUGenV714_pythia8/RunIIAutumn18NanoAODv4-Nano14Dec2018_102X_upgrade2018_realistic_v16-v1/NANOAODSIM'}
Samples['GluGluHToWWTo2L2Nu_M210'] = {'nanoAOD' :'/GluGluHToWWTo2L2Nu_M210_13TeV_powheg2_JHUGenV714_pythia8/RunIIAutumn18NanoAODv4-Nano14Dec2018_102X_upgrade2018_realistic_v16-v1/NANOAODSIM'}
Samples['GluGluHToWWTo2L2Nu_M230'] = {'nanoAOD' :'/GluGluHToWWTo2L2Nu_M230_13TeV_powheg2_JHUGenV714_pythia8/RunIIAutumn18NanoAODv4-Nano14Dec2018_102X_upgrade2018_realistic_v16-v1/NANOAODSIM'}
Samples['GluGluHToWWTo2L2Nu_M250'] = {'nanoAOD' :'/GluGluHToWWTo2L2Nu_M250_13TeV_powheg2_JHUGenV714_pythia8/RunIIAutumn18NanoAODv4-Nano14Dec2018_102X_upgrade2018_realistic_v16-v1/NANOAODSIM'}
Samples['GluGluHToWWTo2L2Nu_M270'] = {'nanoAOD' :'/GluGluHToWWTo2L2Nu_M270_13TeV_powheg2_JHUGenV714_pythia8/RunIIAutumn18NanoAODv4-Nano14Dec2018_102X_upgrade2018_realistic_v16-v1/NANOAODSIM'}
Samples['GluGluHToWWTo2L2Nu_M300'] = {'nanoAOD' :'/GluGluHToWWTo2L2Nu_M300_13TeV_powheg2_JHUGenV714_pythia8/RunIIAutumn18NanoAODv4-Nano14Dec2018_102X_upgrade2018_realistic_v16-v1/NANOAODSIM'}
Samples['GluGluHToWWTo2L2Nu_M350'] = {'nanoAOD' :'/GluGluHToWWTo2L2Nu_M350_13TeV_powheg2_JHUGenV714_pythia8/RunIIAutumn18NanoAODv4-Nano14Dec2018_102X_upgrade2018_realistic_v16-v1/NANOAODSIM'}
#Samples['GluGluHToWWTo2L2Nu_M400'] = {'nanoAOD' :'/GluGluHToWWTo2L2Nu_M400_13TeV_powheg2_JHUGenV714_pythia8/RunIIAutumn18NanoAODv4-Nano14Dec2018_102X_upgrade2018_realistic_v16-v1/NANOAODSIM'}
Samples['GluGluHToWWTo2L2Nu_M450'] = {'nanoAOD' :'/GluGluHToWWTo2L2Nu_M450_13TeV_powheg2_JHUGenV714_pythia8/RunIIAutumn18NanoAODv4-Nano14Dec2018_102X_upgrade2018_realistic_v16-v1/NANOAODSIM'}
Samples['GluGluHToWWTo2L2Nu_M500'] = {'nanoAOD' :'/GluGluHToWWTo2L2Nu_M500_13TeV_powheg2_JHUGenV714_pythia8/RunIIAutumn18NanoAODv4-Nano14Dec2018_102X_upgrade2018_realistic_v16-v1/NANOAODSIM'}
Samples['GluGluHToWWTo2L2Nu_M550'] = {'nanoAOD' :'/GluGluHToWWTo2L2Nu_M550_13TeV_powheg2_JHUGenV714_pythia8/RunIIAutumn18NanoAODv4-Nano14Dec2018_102X_upgrade2018_realistic_v16-v1/NANOAODSIM'}
Samples['GluGluHToWWTo2L2Nu_M600'] = {'nanoAOD' :'/GluGluHToWWTo2L2Nu_M600_13TeV_powheg2_JHUGenV714_pythia8/RunIIAutumn18NanoAODv4-Nano14Dec2018_102X_upgrade2018_realistic_v16-v1/NANOAODSIM'}
Samples['GluGluHToWWTo2L2Nu_M650'] = {'nanoAOD' :'/GluGluHToWWTo2L2Nu_M650_13TeV_powheg2_JHUGenV714_pythia8/RunIIAutumn18NanoAODv4-Nano14Dec2018_102X_upgrade2018_realistic_v16-v1/NANOAODSIM'}
Samples['GluGluHToWWTo2L2Nu_M700'] = {'nanoAOD' :'/GluGluHToWWTo2L2Nu_M700_13TeV_powheg2_JHUGenV714_pythia8/RunIIAutumn18NanoAODv4-Nano14Dec2018_102X_upgrade2018_realistic_v16-v1/NANOAODSIM'}
#Samples['GluGluHToWWTo2L2Nu_M750'] = {'nanoAOD' :'/GluGluHToWWTo2L2Nu_M750_13TeV_powheg2_JHUGenV714_pythia8/RunIIAutumn18NanoAODv4-Nano14Dec2018_102X_upgrade2018_realistic_v16-v1/NANOAODSIM'}
Samples['GluGluHToWWTo2L2Nu_M800'] = {'nanoAOD' :'/GluGluHToWWTo2L2Nu_M800_13TeV_powheg2_JHUGenV714_pythia8/RunIIAutumn18NanoAODv4-Nano14Dec2018_102X_upgrade2018_realistic_v16-v1/NANOAODSIM'}
#Samples['GluGluHToWWTo2L2Nu_M900'] = {'nanoAOD' :'/GluGluHToWWTo2L2Nu_M900_13TeV_powheg2_JHUGenV714_pythia8/RunIIAutumn18NanoAODv4-Nano14Dec2018_102X_upgrade2018_realistic_v16-v1/NANOAODSIM'}
Samples['GluGluHToWWTo2L2Nu_M1000'] = {'nanoAOD' :'/GluGluHToWWTo2L2Nu_M1000_13TeV_powheg2_JHUGenV714_pythia8/RunIIAutumn18NanoAODv4-Nano14Dec2018_102X_upgrade2018_realistic_v16-v1/NANOAODSIM'}
Samples['GluGluHToWWTo2L2Nu_M1500'] = {'nanoAOD' :'/GluGluHToWWTo2L2Nu_M1500_13TeV_powheg2_JHUGenV714_pythia8/RunIIAutumn18NanoAODv4-Nano14Dec2018_102X_upgrade2018_realistic_v16-v1/NANOAODSIM'}
Samples['GluGluHToWWTo2L2Nu_M2000'] = {'nanoAOD' :'/GluGluHToWWTo2L2Nu_M2000_13TeV_powheg2_JHUGenV714_pythia8/RunIIAutumn18NanoAODv4-Nano14Dec2018_102X_upgrade2018_realistic_v16-v1/NANOAODSIM'}
Samples['GluGluHToWWTo2L2Nu_M2500'] = {'nanoAOD' :'/GluGluHToWWTo2L2Nu_M2500_13TeV_powheg2_JHUGenV714_pythia8/RunIIAutumn18NanoAODv4-Nano14Dec2018_102X_upgrade2018_realistic_v16-v1/NANOAODSIM'}
Samples['GluGluHToWWTo2L2Nu_M3000'] = {'nanoAOD' :'/GluGluHToWWTo2L2Nu_M3000_13TeV_powheg2_JHUGenV714_pythia8/RunIIAutumn18NanoAODv4-Nano14Dec2018_102X_upgrade2018_realistic_v16-v1/NANOAODSIM'}
#Samples['GluGluHToWWTo2L2Nu_M4000'] = {'nanoAOD' :'/GluGluHToWWTo2L2Nu_M4000_13TeV_powheg2_JHUGenV714_pythia8/RunIIAutumn18NanoAODv4-Nano14Dec2018_102X_upgrade2018_realistic_v16-v1/NANOAODSIM'}
#Samples['GluGluHToWWTo2L2Nu_M5000'] = {'nanoAOD' :'/GluGluHToWWTo2L2Nu_M5000_13TeV_powheg2_JHUGenV714_pythia8/RunIIAutumn18NanoAODv4-Nano14Dec2018_102X_upgrade2018_realistic_v16-v1/NANOAODSIM'}

## VBF HWW dilepton High mass

#Samples['VBFHToWWTo2L2Nu_M115'] = {'nanoAOD' :'/VBFHToWWTo2L2Nu_M115_13TeV_powheg2_JHUGenV714_pythia8/RunIIAutumn18NanoAODv4-Nano14Dec2018_102X_upgrade2018_realistic_v16-v1/NANOAODSIM'}
#Samples['VBFHToWWTo2L2Nu_M120'] = {'nanoAOD' :'/VBFHToWWTo2L2Nu_M120_13TeV_powheg2_JHUGenV714_pythia8/RunIIAutumn18NanoAODv4-Nano14Dec2018_102X_upgrade2018_realistic_v16-v1/NANOAODSIM'}
#Samples['VBFHToWWTo2L2Nu_M124'] = {'nanoAOD' :'/VBFHToWWTo2L2Nu_M124_13TeV_powheg2_JHUGenV714_pythia8/RunIIAutumn18NanoAODv4-Nano14Dec2018_102X_upgrade2018_realistic_v16-v1/NANOAODSIM'}
Samples['VBFHToWWTo2L2Nu_M125'] = {'nanoAOD' :'/VBFHToWWTo2L2Nu_M125_13TeV_powheg2_JHUGenV714_pythia8/RunIIAutumn18NanoAODv4-Nano14Dec2018_102X_upgrade2018_realistic_v16-v1/NANOAODSIM'}
#Samples['VBFHToWWTo2L2Nu_M126'] = {'nanoAOD' :'/VBFHToWWTo2L2Nu_M126_13TeV_powheg2_JHUGenV714_pythia8/RunIIAutumn18NanoAODv4-Nano14Dec2018_102X_upgrade2018_realistic_v16-v1/NANOAODSIM'}
#Samples['VBFHToWWTo2L2Nu_M130'] = {'nanoAOD' :'/VBFHToWWTo2L2Nu_M130_13TeV_powheg2_JHUGenV714_pythia8/RunIIAutumn18NanoAODv4-Nano14Dec2018_102X_upgrade2018_realistic_v16-v1/NANOAODSIM'}
#Samples['VBFHToWWTo2L2Nu_M135'] = {'nanoAOD' :'/VBFHToWWTo2L2Nu_M135_13TeV_powheg2_JHUGenV714_pythia8/RunIIAutumn18NanoAODv4-Nano14Dec2018_102X_upgrade2018_realistic_v16-v1/NANOAODSIM'}
#Samples['VBFHToWWTo2L2Nu_M140'] = {'nanoAOD' :'/VBFHToWWTo2L2Nu_M140_13TeV_powheg2_JHUGenV714_pythia8/RunIIAutumn18NanoAODv4-Nano14Dec2018_102X_upgrade2018_realistic_v16-v1/NANOAODSIM'}
#Samples['VBFHToWWTo2L2Nu_M145'] = {'nanoAOD' :'/VBFHToWWTo2L2Nu_M145_13TeV_powheg2_JHUGenV714_pythia8/RunIIAutumn18NanoAODv4-Nano14Dec2018_102X_upgrade2018_realistic_v16-v1/NANOAODSIM'}
#Samples['VBFHToWWTo2L2Nu_M150'] = {'nanoAOD' :'/VBFHToWWTo2L2Nu_M150_13TeV_powheg2_JHUGenV714_pythia8/RunIIAutumn18NanoAODv4-Nano14Dec2018_102X_upgrade2018_realistic_v16-v1/NANOAODSIM'}
#Samples['VBFHToWWTo2L2Nu_M155'] = {'nanoAOD' :'/VBFHToWWTo2L2Nu_M155_13TeV_powheg2_JHUGenV714_pythia8/RunIIAutumn18NanoAODv4-Nano14Dec2018_102X_upgrade2018_realistic_v16-v1/NANOAODSIM'}
#Samples['VBFHToWWTo2L2Nu_M160'] = {'nanoAOD' :'/VBFHToWWTo2L2Nu_M160_13TeV_powheg2_JHUGenV714_pythia8/RunIIAutumn18NanoAODv4-Nano14Dec2018_102X_upgrade2018_realistic_v16-v1/NANOAODSIM'}
#Samples['VBFHToWWTo2L2Nu_M165'] = {'nanoAOD' :'/VBFHToWWTo2L2Nu_M165_13TeV_powheg2_JHUGenV714_pythia8/RunIIAutumn18NanoAODv4-Nano14Dec2018_102X_upgrade2018_realistic_v16-v1/NANOAODSIM'}
Samples['VBFHToWWTo2L2Nu_M170'] = {'nanoAOD' :'/VBFHToWWTo2L2Nu_M170_13TeV_powheg2_JHUGenV714_pythia8/RunIIAutumn18NanoAODv4-Nano14Dec2018_102X_upgrade2018_realistic_v16-v1/NANOAODSIM'}
#Samples['VBFHToWWTo2L2Nu_M175'] = {'nanoAOD' :'/VBFHToWWTo2L2Nu_M175_13TeV_powheg2_JHUGenV714_pythia8/RunIIAutumn18NanoAODv4-Nano14Dec2018_102X_upgrade2018_realistic_v16-v1/NANOAODSIM'}
#Samples['VBFHToWWTo2L2Nu_M180'] = {'nanoAOD' :'/VBFHToWWTo2L2Nu_M180_13TeV_powheg2_JHUGenV714_pythia8/RunIIAutumn18NanoAODv4-Nano14Dec2018_102X_upgrade2018_realistic_v16-v1/NANOAODSIM'}
#Samples['VBFHToWWTo2L2Nu_M190'] = {'nanoAOD' :'/VBFHToWWTo2L2Nu_M190_13TeV_powheg2_JHUGenV714_pythia8/RunIIAutumn18NanoAODv4-Nano14Dec2018_102X_upgrade2018_realistic_v16-v1/NANOAODSIM'}
#Samples['VBFHToWWTo2L2Nu_M200'] = {'nanoAOD' :'/VBFHToWWTo2L2Nu_M200_13TeV_powheg2_JHUGenV714_pythia8/RunIIAutumn18NanoAODv4-Nano14Dec2018_102X_upgrade2018_realistic_v16-v1/NANOAODSIM'}
#Samples['VBFHToWWTo2L2Nu_M210'] = {'nanoAOD' :'/VBFHToWWTo2L2Nu_M210_13TeV_powheg2_JHUGenV714_pythia8/RunIIAutumn18NanoAODv4-Nano14Dec2018_102X_upgrade2018_realistic_v16-v1/NANOAODSIM'}
#Samples['VBFHToWWTo2L2Nu_M230'] = {'nanoAOD' :'/VBFHToWWTo2L2Nu_M230_13TeV_powheg2_JHUGenV714_pythia8/RunIIAutumn18NanoAODv4-Nano14Dec2018_102X_upgrade2018_realistic_v16-v1/NANOAODSIM'}
##Samples['VBFHToWWTo2L2Nu_M250'] = {'nanoAOD' :'/VBFHToWWTo2L2Nu_M250_13TeV_powheg2_JHUGenV714_pythia8/RunIIAutumn18NanoAODv4-Nano14Dec2018_102X_upgrade2018_realistic_v16-v1/NANOAODSIM'}
#Samples['VBFHToWWTo2L2Nu_M270'] = {'nanoAOD' :'/VBFHToWWTo2L2Nu_M270_13TeV_powheg2_JHUGenV714_pythia8/RunIIAutumn18NanoAODv4-Nano14Dec2018_102X_upgrade2018_realistic_v16-v1/NANOAODSIM'}
#Samples['VBFHToWWTo2L2Nu_M300'] = {'nanoAOD' :'/VBFHToWWTo2L2Nu_M300_13TeV_powheg2_JHUGenV714_pythia8/RunIIAutumn18NanoAODv4-Nano14Dec2018_102X_upgrade2018_realistic_v16-v1/NANOAODSIM'}
#Samples['VBFHToWWTo2L2Nu_M350'] = {'nanoAOD' :'/VBFHToWWTo2L2Nu_M350_13TeV_powheg2_JHUGenV714_pythia8/RunIIAutumn18NanoAODv4-Nano14Dec2018_102X_upgrade2018_realistic_v16-v1/NANOAODSIM'}
#Samples['VBFHToWWTo2L2Nu_M400'] = {'nanoAOD' :'/VBFHToWWTo2L2Nu_M400_13TeV_powheg2_JHUGenV714_pythia8/RunIIAutumn18NanoAODv4-Nano14Dec2018_102X_upgrade2018_realistic_v16-v1/NANOAODSIM'}
#Samples['VBFHToWWTo2L2Nu_M450'] = {'nanoAOD' :'/VBFHToWWTo2L2Nu_M450_13TeV_powheg2_JHUGenV714_pythia8/RunIIAutumn18NanoAODv4-Nano14Dec2018_102X_upgrade2018_realistic_v16-v1/NANOAODSIM'}
Samples['VBFHToWWTo2L2Nu_M500'] = {'nanoAOD' :'/VBFHToWWTo2L2Nu_M500_13TeV_powheg2_JHUGenV714_pythia8/RunIIAutumn18NanoAODv4-Nano14Dec2018_102X_upgrade2018_realistic_v16-v1/NANOAODSIM'}
#Samples['VBFHToWWTo2L2Nu_M550'] = {'nanoAOD' :'/VBFHToWWTo2L2Nu_M550_13TeV_powheg2_JHUGenV714_pythia8/RunIIAutumn18NanoAODv4-Nano14Dec2018_102X_upgrade2018_realistic_v16-v1/NANOAODSIM'}
#Samples['VBFHToWWTo2L2Nu_M600'] = {'nanoAOD' :'/VBFHToWWTo2L2Nu_M600_13TeV_powheg2_JHUGenV714_pythia8/RunIIAutumn18NanoAODv4-Nano14Dec2018_102X_upgrade2018_realistic_v16-v1/NANOAODSIM'}
#Samples['VBFHToWWTo2L2Nu_M650'] = {'nanoAOD' :'/VBFHToWWTo2L2Nu_M650_13TeV_powheg2_JHUGenV714_pythia8/RunIIAutumn18NanoAODv4-Nano14Dec2018_102X_upgrade2018_realistic_v16-v1/NANOAODSIM'}
#Samples['VBFHToWWTo2L2Nu_M700'] = {'nanoAOD' :'/VBFHToWWTo2L2Nu_M700_13TeV_powheg2_JHUGenV714_pythia8/RunIIAutumn18NanoAODv4-Nano14Dec2018_102X_upgrade2018_realistic_v16-v1/NANOAODSIM'}
#Samples['VBFHToWWTo2L2Nu_M750'] = {'nanoAOD' :'/VBFHToWWTo2L2Nu_M750_13TeV_powheg2_JHUGenV714_pythia8/RunIIAutumn18NanoAODv4-Nano14Dec2018_102X_upgrade2018_realistic_v16-v1/NANOAODSIM'}
#Samples['VBFHToWWTo2L2Nu_M800'] = {'nanoAOD' :'/VBFHToWWTo2L2Nu_M800_13TeV_powheg2_JHUGenV714_pythia8/RunIIAutumn18NanoAODv4-Nano14Dec2018_102X_upgrade2018_realistic_v16-v1/NANOAODSIM'}
#Samples['VBFHToWWTo2L2Nu_M900'] = {'nanoAOD' :'/VBFHToWWTo2L2Nu_M900_13TeV_powheg2_JHUGenV714_pythia8/RunIIAutumn18NanoAODv4-Nano14Dec2018_102X_upgrade2018_realistic_v16-v1/NANOAODSIM'}
#Samples['VBFHToWWTo2L2Nu_M1000'] = {'nanoAOD' :'/VBFHToWWTo2L2Nu_M1000_13TeV_powheg2_JHUGenV714_pythia8/RunIIAutumn18NanoAODv4-Nano14Dec2018_102X_upgrade2018_realistic_v16-v1/NANOAODSIM'}
#Samples['VBFHToWWTo2L2Nu_M1500'] = {'nanoAOD' :'/VBFHToWWTo2L2Nu_M1500_13TeV_powheg2_JHUGenV714_pythia8/RunIIAutumn18NanoAODv4-Nano14Dec2018_102X_upgrade2018_realistic_v16-v1/NANOAODSIM'}
Samples['VBFHToWWTo2L2Nu_M2000'] = {'nanoAOD' :'/VBFHToWWTo2L2Nu_M2000_13TeV_powheg2_JHUGenV714_pythia8/RunIIAutumn18NanoAODv4-Nano14Dec2018_102X_upgrade2018_realistic_v16-v1/NANOAODSIM'}
#Samples['VBFHToWWTo2L2Nu_M2500'] = {'nanoAOD' :'/VBFHToWWTo2L2Nu_M2500_13TeV_powheg2_JHUGenV714_pythia8/RunIIAutumn18NanoAODv4-Nano14Dec2018_102X_upgrade2018_realistic_v16-v1/NANOAODSIM'}
#Samples['VBFHToWWTo2L2Nu_M3000'] = {'nanoAOD' :'/VBFHToWWTo2L2Nu_M3000_13TeV_powheg2_JHUGenV714_pythia8/RunIIAutumn18NanoAODv4-Nano14Dec2018_102X_upgrade2018_realistic_v16-v1/NANOAODSIM'}
#Samples['VBFHToWWTo2L2Nu_M4000'] = {'nanoAOD' :'/VBFHToWWTo2L2Nu_M4000_13TeV_powheg2_JHUGenV714_pythia8/RunIIAutumn18NanoAODv4-Nano14Dec2018_102X_upgrade2018_realistic_v16-v1/NANOAODSIM'}
#Samples['VBFHToWWTo2L2Nu_M5000'] = {'nanoAOD' :'/VBFHToWWTo2L2Nu_M5000_13TeV_powheg2_JHUGenV714_pythia8/RunIIAutumn18NanoAODv4-Nano14Dec2018_102X_upgrade2018_realistic_v16-v1/NANOAODSIM'}

## ggH HWW semilepton High mass

#Samples['GluGluHToWWToLNuQQ_M115'] = {'nanoAOD' :'/GluGluHToWWToLNuQQ_M115_13TeV_powheg2_JHUGenV714_pythia8/RunIIAutumn18NanoAODv4-Nano14Dec2018_102X_upgrade2018_realistic_v16-v1/NANOAODSIM'}
#Samples['GluGluHToWWToLNuQQ_M120'] = {'nanoAOD' :'/GluGluHToWWToLNuQQ_M120_13TeV_powheg2_JHUGenV714_pythia8/RunIIAutumn18NanoAODv4-Nano14Dec2018_102X_upgrade2018_realistic_v16-v1/NANOAODSIM'}
#Samples['GluGluHToWWToLNuQQ_M124'] = {'nanoAOD' :'/GluGluHToWWToLNuQQ_M124_13TeV_powheg2_JHUGenV714_pythia8/RunIIAutumn18NanoAODv4-Nano14Dec2018_102X_upgrade2018_realistic_v16-v1/NANOAODSIM'}
Samples['GluGluHToWWToLNuQQ_M125'] = {'nanoAOD' :'/GluGluHToWWToLNuQQ_M125_13TeV_powheg2_JHUGenV714_pythia8/RunIIAutumn18NanoAODv4-Nano14Dec2018_102X_upgrade2018_realistic_v16-v1/NANOAODSIM'}
#Samples['GluGluHToWWToLNuQQ_M126'] = {'nanoAOD' :'/GluGluHToWWToLNuQQ_M126_13TeV_powheg2_JHUGenV714_pythia8/RunIIAutumn18NanoAODv4-Nano14Dec2018_102X_upgrade2018_realistic_v16-v1/NANOAODSIM'}
#Samples['GluGluHToWWToLNuQQ_M130'] = {'nanoAOD' :'/GluGluHToWWToLNuQQ_M130_13TeV_powheg2_JHUGenV714_pythia8/RunIIAutumn18NanoAODv4-Nano14Dec2018_102X_upgrade2018_realistic_v16-v1/NANOAODSIM'}
#Samples['GluGluHToWWToLNuQQ_M135'] = {'nanoAOD' :'/GluGluHToWWToLNuQQ_M135_13TeV_powheg2_JHUGenV714_pythia8/RunIIAutumn18NanoAODv4-Nano14Dec2018_102X_upgrade2018_realistic_v16-v1/NANOAODSIM'}
#Samples['GluGluHToWWToLNuQQ_M140'] = {'nanoAOD' :'/GluGluHToWWToLNuQQ_M140_13TeV_powheg2_JHUGenV714_pythia8/RunIIAutumn18NanoAODv4-Nano14Dec2018_102X_upgrade2018_realistic_v16-v1/NANOAODSIM'}
#Samples['GluGluHToWWToLNuQQ_M145'] = {'nanoAOD' :'/GluGluHToWWToLNuQQ_M145_13TeV_powheg2_JHUGenV714_pythia8/RunIIAutumn18NanoAODv4-Nano14Dec2018_102X_upgrade2018_realistic_v16-v1/NANOAODSIM'}
#Samples['GluGluHToWWToLNuQQ_M150'] = {'nanoAOD' :'/GluGluHToWWToLNuQQ_M150_13TeV_powheg2_JHUGenV714_pythia8/RunIIAutumn18NanoAODv4-Nano14Dec2018_102X_upgrade2018_realistic_v16-v1/NANOAODSIM'}
#Samples['GluGluHToWWToLNuQQ_M155'] = {'nanoAOD' :'/GluGluHToWWToLNuQQ_M155_13TeV_powheg2_JHUGenV714_pythia8/RunIIAutumn18NanoAODv4-Nano14Dec2018_102X_upgrade2018_realistic_v16-v1/NANOAODSIM'}
#Samples['GluGluHToWWToLNuQQ_M160'] = {'nanoAOD' :'/GluGluHToWWToLNuQQ_M160_13TeV_powheg2_JHUGenV714_pythia8/RunIIAutumn18NanoAODv4-Nano14Dec2018_102X_upgrade2018_realistic_v16-v1/NANOAODSIM'}
#Samples['GluGluHToWWToLNuQQ_M165'] = {'nanoAOD' :'/GluGluHToWWToLNuQQ_M165_13TeV_powheg2_JHUGenV714_pythia8/RunIIAutumn18NanoAODv4-Nano14Dec2018_102X_upgrade2018_realistic_v16-v1/NANOAODSIM'}
#Samples['GluGluHToWWToLNuQQ_M170'] = {'nanoAOD' :'/GluGluHToWWToLNuQQ_M170_13TeV_powheg2_JHUGenV714_pythia8/RunIIAutumn18NanoAODv4-Nano14Dec2018_102X_upgrade2018_realistic_v16-v1/NANOAODSIM'}
#Samples['GluGluHToWWToLNuQQ_M175'] = {'nanoAOD' :'/GluGluHToWWToLNuQQ_M175_13TeV_powheg2_JHUGenV714_pythia8/RunIIAutumn18NanoAODv4-Nano14Dec2018_102X_upgrade2018_realistic_v16-v1/NANOAODSIM'}
#Samples['GluGluHToWWToLNuQQ_M180'] = {'nanoAOD' :'/GluGluHToWWToLNuQQ_M180_13TeV_powheg2_JHUGenV714_pythia8/RunIIAutumn18NanoAODv4-Nano14Dec2018_102X_upgrade2018_realistic_v16-v1/NANOAODSIM'}
#Samples['GluGluHToWWToLNuQQ_M190'] = {'nanoAOD' :'/GluGluHToWWToLNuQQ_M190_13TeV_powheg2_JHUGenV714_pythia8/RunIIAutumn18NanoAODv4-Nano14Dec2018_102X_upgrade2018_realistic_v16-v1/NANOAODSIM'}
Samples['GluGluHToWWToLNuQQ_M200'] = {'nanoAOD' :'/GluGluHToWWToLNuQQ_M200_13TeV_powheg2_JHUGenV714_pythia8/RunIIAutumn18NanoAODv4-Nano14Dec2018_102X_upgrade2018_realistic_v16-v1/NANOAODSIM'}
#Samples['GluGluHToWWToLNuQQ_M210'] = {'nanoAOD' :'/GluGluHToWWToLNuQQ_M210_13TeV_powheg2_JHUGenV714_pythia8/RunIIAutumn18NanoAODv4-Nano14Dec2018_102X_upgrade2018_realistic_v16-v1/NANOAODSIM'}
#Samples['GluGluHToWWToLNuQQ_M230'] = {'nanoAOD' :'/GluGluHToWWToLNuQQ_M230_13TeV_powheg2_JHUGenV714_pythia8/RunIIAutumn18NanoAODv4-Nano14Dec2018_102X_upgrade2018_realistic_v16-v1/NANOAODSIM'}
Samples['GluGluHToWWToLNuQQ_M250'] = {'nanoAOD' :'/GluGluHToWWToLNuQQ_M250_13TeV_powheg2_JHUGenV714_pythia8/RunIIAutumn18NanoAODv4-Nano14Dec2018_102X_upgrade2018_realistic_v16-v1/NANOAODSIM'}
#Samples['GluGluHToWWToLNuQQ_M270'] = {'nanoAOD' :'/GluGluHToWWToLNuQQ_M270_13TeV_powheg2_JHUGenV714_pythia8/RunIIAutumn18NanoAODv4-Nano14Dec2018_102X_upgrade2018_realistic_v16-v1/NANOAODSIM'}
Samples['GluGluHToWWToLNuQQ_M300'] = {'nanoAOD' :'/GluGluHToWWToLNuQQ_M300_13TeV_powheg2_JHUGenV714_pythia8/RunIIAutumn18NanoAODv4-Nano14Dec2018_102X_upgrade2018_realistic_v16-v1/NANOAODSIM'}
Samples['GluGluHToWWToLNuQQ_M350'] = {'nanoAOD' :'/GluGluHToWWToLNuQQ_M350_13TeV_powheg2_JHUGenV714_pythia8/RunIIAutumn18NanoAODv4-Nano14Dec2018_102X_upgrade2018_realistic_v16-v1/NANOAODSIM'}
Samples['GluGluHToWWToLNuQQ_M400'] = {'nanoAOD' :'/GluGluHToWWToLNuQQ_M400_13TeV_powheg2_JHUGenV714_pythia8/RunIIAutumn18NanoAODv4-Nano14Dec2018_102X_upgrade2018_realistic_v16-v1/NANOAODSIM'}
#Samples['GluGluHToWWToLNuQQ_M450'] = {'nanoAOD' :'/GluGluHToWWToLNuQQ_M450_13TeV_powheg2_JHUGenV714_pythia8/RunIIAutumn18NanoAODv4-Nano14Dec2018_102X_upgrade2018_realistic_v16-v1/NANOAODSIM'}
Samples['GluGluHToWWToLNuQQ_M500'] = {'nanoAOD' :'/GluGluHToWWToLNuQQ_M500_13TeV_powheg2_JHUGenV714_pythia8/RunIIAutumn18NanoAODv4-Nano14Dec2018_102X_upgrade2018_realistic_v16-v1/NANOAODSIM'}
Samples['GluGluHToWWToLNuQQ_M550'] = {'nanoAOD' :'/GluGluHToWWToLNuQQ_M550_13TeV_powheg2_JHUGenV714_pythia8/RunIIAutumn18NanoAODv4-Nano14Dec2018_102X_upgrade2018_realistic_v16-v1/NANOAODSIM'}
Samples['GluGluHToWWToLNuQQ_M600'] = {'nanoAOD' :'/GluGluHToWWToLNuQQ_M600_13TeV_powheg2_JHUGenV714_pythia8/RunIIAutumn18NanoAODv4-Nano14Dec2018_102X_upgrade2018_realistic_v16-v1/NANOAODSIM'}
Samples['GluGluHToWWToLNuQQ_M650'] = {'nanoAOD' :'/GluGluHToWWToLNuQQ_M650_13TeV_powheg2_JHUGenV714_pythia8/RunIIAutumn18NanoAODv4-Nano14Dec2018_102X_upgrade2018_realistic_v16-v1/NANOAODSIM'}
Samples['GluGluHToWWToLNuQQ_M700'] = {'nanoAOD' :'/GluGluHToWWToLNuQQ_M700_13TeV_powheg2_JHUGenV714_pythia8/RunIIAutumn18NanoAODv4-Nano14Dec2018_102X_upgrade2018_realistic_v16-v1/NANOAODSIM'}
#Samples['GluGluHToWWToLNuQQ_M750'] = {'nanoAOD' :'/GluGluHToWWToLNuQQ_M750_13TeV_powheg2_JHUGenV714_pythia8/RunIIAutumn18NanoAODv4-Nano14Dec2018_102X_upgrade2018_realistic_v16-v1/NANOAODSIM'}
Samples['GluGluHToWWToLNuQQ_M800'] = {'nanoAOD' :'/GluGluHToWWToLNuQQ_M800_13TeV_powheg2_JHUGenV714_pythia8/RunIIAutumn18NanoAODv4-Nano14Dec2018_102X_upgrade2018_realistic_v16-v1/NANOAODSIM'}
Samples['GluGluHToWWToLNuQQ_M900'] = {'nanoAOD' :'/GluGluHToWWToLNuQQ_M900_13TeV_powheg2_JHUGenV714_pythia8/RunIIAutumn18NanoAODv4-Nano14Dec2018_102X_upgrade2018_realistic_v16-v1/NANOAODSIM'}
#Samples['GluGluHToWWToLNuQQ_M1000'] = {'nanoAOD' :'/GluGluHToWWToLNuQQ_M1000_13TeV_powheg2_JHUGenV714_pythia8/RunIIAutumn18NanoAODv4-Nano14Dec2018_102X_upgrade2018_realistic_v16-v1/NANOAODSIM'}
Samples['GluGluHToWWToLNuQQ_M1500'] = {'nanoAOD' :'/GluGluHToWWToLNuQQ_M1500_13TeV_powheg2_JHUGenV714_pythia8/RunIIAutumn18NanoAODv4-Nano14Dec2018_102X_upgrade2018_realistic_v16-v1/NANOAODSIM'}
Samples['GluGluHToWWToLNuQQ_M2000'] = {'nanoAOD' :'/GluGluHToWWToLNuQQ_M2000_13TeV_powheg2_JHUGenV714_pythia8/RunIIAutumn18NanoAODv4-Nano14Dec2018_102X_upgrade2018_realistic_v16-v1/NANOAODSIM'}
Samples['GluGluHToWWToLNuQQ_M2500'] = {'nanoAOD' :'/GluGluHToWWToLNuQQ_M2500_13TeV_powheg2_JHUGenV714_pythia8/RunIIAutumn18NanoAODv4-Nano14Dec2018_102X_upgrade2018_realistic_v16-v1/NANOAODSIM'}
Samples['GluGluHToWWToLNuQQ_M3000'] = {'nanoAOD' :'/GluGluHToWWToLNuQQ_M3000_13TeV_powheg2_JHUGenV714_pythia8/RunIIAutumn18NanoAODv4-Nano14Dec2018_102X_upgrade2018_realistic_v16-v1/NANOAODSIM'}
Samples['GluGluHToWWToLNuQQ_M4000'] = {'nanoAOD' :'/GluGluHToWWToLNuQQ_M4000_13TeV_powheg2_JHUGenV714_pythia8/RunIIAutumn18NanoAODv4-Nano14Dec2018_102X_upgrade2018_realistic_v16-v1/NANOAODSIM'}
#Samples['GluGluHToWWToLNuQQ_M5000'] = {'nanoAOD' :'/GluGluHToWWToLNuQQ_M5000_13TeV_powheg2_JHUGenV714_pythia8/RunIIAutumn18NanoAODv4-Nano14Dec2018_102X_upgrade2018_realistic_v16-v1/NANOAODSIM'}

## VBF HWW semilepton High mass

#Samples['VBFHToWWToLNuQQ_M115'] = {'nanoAOD' :'/VBFHToWWToLNuQQ_M115_13TeV_powheg_JHUGen_pythia8/RunIIAutumn18NanoAODv4-Nano14Dec2018_102X_upgrade2018_realistic_v16-v1/NANOAODSIM'}
#Samples['VBFHToWWToLNuQQ_M120'] = {'nanoAOD' :'/VBFHToWWToLNuQQ_M120_13TeV_powheg_JHUGen_pythia8/RunIIAutumn18NanoAODv4-Nano14Dec2018_102X_upgrade2018_realistic_v16-v1/NANOAODSIM'}
#Samples['VBFHToWWToLNuQQ_M124'] = {'nanoAOD' :'/VBFHToWWToLNuQQ_M124_13TeV_powheg_JHUGen_pythia8/RunIIAutumn18NanoAODv4-Nano14Dec2018_102X_upgrade2018_realistic_v16-v1/NANOAODSIM'}
Samples['VBFHToWWToLNuQQ_M125'] = {'nanoAOD' :'/VBFHToWWToLNuQQ_M125_13TeV_powheg_JHUGen_pythia8/RunIIAutumn18NanoAODv4-Nano14Dec2018_102X_upgrade2018_realistic_v16-v1/NANOAODSIM'}
#Samples['VBFHToWWToLNuQQ_M126'] = {'nanoAOD' :'/VBFHToWWToLNuQQ_M126_13TeV_powheg_JHUGen_pythia8/RunIIAutumn18NanoAODv4-Nano14Dec2018_102X_upgrade2018_realistic_v16-v1/NANOAODSIM'}
#Samples['VBFHToWWToLNuQQ_M130'] = {'nanoAOD' :'/VBFHToWWToLNuQQ_M130_13TeV_powheg_JHUGen_pythia8/RunIIAutumn18NanoAODv4-Nano14Dec2018_102X_upgrade2018_realistic_v16-v1/NANOAODSIM'}
#Samples['VBFHToWWToLNuQQ_M135'] = {'nanoAOD' :'/VBFHToWWToLNuQQ_M135_13TeV_powheg_JHUGen_pythia8/RunIIAutumn18NanoAODv4-Nano14Dec2018_102X_upgrade2018_realistic_v16-v1/NANOAODSIM'}
#Samples['VBFHToWWToLNuQQ_M140'] = {'nanoAOD' :'/VBFHToWWToLNuQQ_M140_13TeV_powheg_JHUGen_pythia8/RunIIAutumn18NanoAODv4-Nano14Dec2018_102X_upgrade2018_realistic_v16-v1/NANOAODSIM'}
#Samples['VBFHToWWToLNuQQ_M145'] = {'nanoAOD' :'/VBFHToWWToLNuQQ_M145_13TeV_powheg_JHUGen_pythia8/RunIIAutumn18NanoAODv4-Nano14Dec2018_102X_upgrade2018_realistic_v16-v1/NANOAODSIM'}
#Samples['VBFHToWWToLNuQQ_M150'] = {'nanoAOD' :'/VBFHToWWToLNuQQ_M150_13TeV_powheg_JHUGen_pythia8/RunIIAutumn18NanoAODv4-Nano14Dec2018_102X_upgrade2018_realistic_v16-v1/NANOAODSIM'}
#Samples['VBFHToWWToLNuQQ_M155'] = {'nanoAOD' :'/VBFHToWWToLNuQQ_M155_13TeV_powheg_JHUGen_pythia8/RunIIAutumn18NanoAODv4-Nano14Dec2018_102X_upgrade2018_realistic_v16-v1/NANOAODSIM'}
#Samples['VBFHToWWToLNuQQ_M160'] = {'nanoAOD' :'/VBFHToWWToLNuQQ_M160_13TeV_powheg_JHUGen_pythia8/RunIIAutumn18NanoAODv4-Nano14Dec2018_102X_upgrade2018_realistic_v16-v1/NANOAODSIM'}
#Samples['VBFHToWWToLNuQQ_M165'] = {'nanoAOD' :'/VBFHToWWToLNuQQ_M165_13TeV_powheg_JHUGen_pythia8/RunIIAutumn18NanoAODv4-Nano14Dec2018_102X_upgrade2018_realistic_v16-v1/NANOAODSIM'}
#Samples['VBFHToWWToLNuQQ_M170'] = {'nanoAOD' :'/VBFHToWWToLNuQQ_M170_13TeV_powheg_JHUGen_pythia8/RunIIAutumn18NanoAODv4-Nano14Dec2018_102X_upgrade2018_realistic_v16-v1/NANOAODSIM'}
#Samples['VBFHToWWToLNuQQ_M175'] = {'nanoAOD' :'/VBFHToWWToLNuQQ_M175_13TeV_powheg_JHUGen_pythia8/RunIIAutumn18NanoAODv4-Nano14Dec2018_102X_upgrade2018_realistic_v16-v1/NANOAODSIM'}
#Samples['VBFHToWWToLNuQQ_M180'] = {'nanoAOD' :'/VBFHToWWToLNuQQ_M180_13TeV_powheg_JHUGen_pythia8/RunIIAutumn18NanoAODv4-Nano14Dec2018_102X_upgrade2018_realistic_v16-v1/NANOAODSIM'}
#Samples['VBFHToWWToLNuQQ_M190'] = {'nanoAOD' :'/VBFHToWWToLNuQQ_M190_13TeV_powheg_JHUGen_pythia8/RunIIAutumn18NanoAODv4-Nano14Dec2018_102X_upgrade2018_realistic_v16-v1/NANOAODSIM'}
#Samples['VBFHToWWToLNuQQ_M200'] = {'nanoAOD' :'/VBFHToWWToLNuQQ_M200_13TeV_powheg_JHUGen_pythia8/RunIIAutumn18NanoAODv4-Nano14Dec2018_102X_upgrade2018_realistic_v16-v1/NANOAODSIM'}
#Samples['VBFHToWWToLNuQQ_M210'] = {'nanoAOD' :'/VBFHToWWToLNuQQ_M210_13TeV_powheg_JHUGen_pythia8/RunIIAutumn18NanoAODv4-Nano14Dec2018_102X_upgrade2018_realistic_v16-v1/NANOAODSIM'}
#Samples['VBFHToWWToLNuQQ_M230'] = {'nanoAOD' :'/VBFHToWWToLNuQQ_M230_13TeV_powheg_JHUGen_pythia8/RunIIAutumn18NanoAODv4-Nano14Dec2018_102X_upgrade2018_realistic_v16-v1/NANOAODSIM'}
#Samples['VBFHToWWToLNuQQ_M250'] = {'nanoAOD' :'/VBFHToWWToLNuQQ_M250_13TeV_powheg_JHUGen_pythia8/RunIIAutumn18NanoAODv4-Nano14Dec2018_102X_upgrade2018_realistic_v16-v1/NANOAODSIM'}
#Samples['VBFHToWWToLNuQQ_M270'] = {'nanoAOD' :'/VBFHToWWToLNuQQ_M270_13TeV_powheg_JHUGen_pythia8/RunIIAutumn18NanoAODv4-Nano14Dec2018_102X_upgrade2018_realistic_v16-v1/NANOAODSIM'}
#Samples['VBFHToWWToLNuQQ_M300'] = {'nanoAOD' :'/VBFHToWWToLNuQQ_M300_13TeV_powheg_JHUGen_pythia8/RunIIAutumn18NanoAODv4-Nano14Dec2018_102X_upgrade2018_realistic_v16-v1/NANOAODSIM'}
#Samples['VBFHToWWToLNuQQ_M350'] = {'nanoAOD' :'/VBFHToWWToLNuQQ_M350_13TeV_powheg_JHUGen_pythia8/RunIIAutumn18NanoAODv4-Nano14Dec2018_102X_upgrade2018_realistic_v16-v1/NANOAODSIM'}
#Samples['VBFHToWWToLNuQQ_M400'] = {'nanoAOD' :'/VBFHToWWToLNuQQ_M400_13TeV_powheg_JHUGen_pythia8/RunIIAutumn18NanoAODv4-Nano14Dec2018_102X_upgrade2018_realistic_v16-v1/NANOAODSIM'}
#Samples['VBFHToWWToLNuQQ_M450'] = {'nanoAOD' :'/VBFHToWWToLNuQQ_M450_13TeV_powheg_JHUGen_pythia8/RunIIAutumn18NanoAODv4-Nano14Dec2018_102X_upgrade2018_realistic_v16-v1/NANOAODSIM'}
#Samples['VBFHToWWToLNuQQ_M500'] = {'nanoAOD' :'/VBFHToWWToLNuQQ_M500_13TeV_powheg_JHUGen_pythia8/RunIIAutumn18NanoAODv4-Nano14Dec2018_102X_upgrade2018_realistic_v16-v1/NANOAODSIM'}
#Samples['VBFHToWWToLNuQQ_M550'] = {'nanoAOD' :'/VBFHToWWToLNuQQ_M550_13TeV_powheg_JHUGen_pythia8/RunIIAutumn18NanoAODv4-Nano14Dec2018_102X_upgrade2018_realistic_v16-v1/NANOAODSIM'}
#Samples['VBFHToWWToLNuQQ_M600'] = {'nanoAOD' :'/VBFHToWWToLNuQQ_M600_13TeV_powheg_JHUGen_pythia8/RunIIAutumn18NanoAODv4-Nano14Dec2018_102X_upgrade2018_realistic_v16-v1/NANOAODSIM'}
#Samples['VBFHToWWToLNuQQ_M650'] = {'nanoAOD' :'/VBFHToWWToLNuQQ_M650_13TeV_powheg_JHUGen_pythia8/RunIIAutumn18NanoAODv4-Nano14Dec2018_102X_upgrade2018_realistic_v16-v1/NANOAODSIM'}
#Samples['VBFHToWWToLNuQQ_M700'] = {'nanoAOD' :'/VBFHToWWToLNuQQ_M700_13TeV_powheg_JHUGen_pythia8/RunIIAutumn18NanoAODv4-Nano14Dec2018_102X_upgrade2018_realistic_v16-v1/NANOAODSIM'}
#Samples['VBFHToWWToLNuQQ_M750'] = {'nanoAOD' :'/VBFHToWWToLNuQQ_M750_13TeV_powheg_JHUGen_pythia8/RunIIAutumn18NanoAODv4-Nano14Dec2018_102X_upgrade2018_realistic_v16-v1/NANOAODSIM'}
#Samples['VBFHToWWToLNuQQ_M800'] = {'nanoAOD' :'/VBFHToWWToLNuQQ_M800_13TeV_powheg_JHUGen_pythia8/RunIIAutumn18NanoAODv4-Nano14Dec2018_102X_upgrade2018_realistic_v16-v1/NANOAODSIM'}
#Samples['VBFHToWWToLNuQQ_M900'] = {'nanoAOD' :'/VBFHToWWToLNuQQ_M900_13TeV_powheg_JHUGen_pythia8/RunIIAutumn18NanoAODv4-Nano14Dec2018_102X_upgrade2018_realistic_v16-v1/NANOAODSIM'}
#Samples['VBFHToWWToLNuQQ_M1000'] = {'nanoAOD' :'/VBFHToWWToLNuQQ_M1000_13TeV_powheg_JHUGen_pythia8/RunIIAutumn18NanoAODv4-Nano14Dec2018_102X_upgrade2018_realistic_v16-v1/NANOAODSIM'}
#Samples['VBFHToWWToLNuQQ_M1500'] = {'nanoAOD' :'/VBFHToWWToLNuQQ_M1500_13TeV_powheg_JHUGen_pythia8/RunIIAutumn18NanoAODv4-Nano14Dec2018_102X_upgrade2018_realistic_v16-v1/NANOAODSIM'}
#Samples['VBFHToWWToLNuQQ_M2000'] = {'nanoAOD' :'/VBFHToWWToLNuQQ_M2000_13TeV_powheg_JHUGen_pythia8/RunIIAutumn18NanoAODv4-Nano14Dec2018_102X_upgrade2018_realistic_v16-v1/NANOAODSIM'}
#Samples['VBFHToWWToLNuQQ_M2500'] = {'nanoAOD' :'/VBFHToWWToLNuQQ_M2500_13TeV_powheg_JHUGen_pythia8/RunIIAutumn18NanoAODv4-Nano14Dec2018_102X_upgrade2018_realistic_v16-v1/NANOAODSIM'}
#Samples['VBFHToWWToLNuQQ_M3000'] = {'nanoAOD' :'/VBFHToWWToLNuQQ_M3000_13TeV_powheg_JHUGen_pythia8/RunIIAutumn18NanoAODv4-Nano14Dec2018_102X_upgrade2018_realistic_v16-v1/NANOAODSIM'}
#Samples['VBFHToWWToLNuQQ_M4000'] = {'nanoAOD' :'/VBFHToWWToLNuQQ_M4000_13TeV_powheg_JHUGen_pythia8/RunIIAutumn18NanoAODv4-Nano14Dec2018_102X_upgrade2018_realistic_v16-v1/NANOAODSIM'}
#Samples['VBFHToWWToLNuQQ_M5000'] = {'nanoAOD' :'/VBFHToWWToLNuQQ_M5000_13TeV_powheg_JHUGen_pythia8/RunIIAutumn18NanoAODv4-Nano14Dec2018_102X_upgrade2018_realistic_v16-v1/NANOAODSIM'}


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Alicia
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
### QCD bcToE
### Samples['QCD_Pt_20to30_bcToE']               = {'nanoAOD' :''} ### Still missing
### Samples['QCD_Pt_30to80_bcToE']               = {'nanoAOD' :''} ### Still missing
### Samples['QCD_Pt_80to170_bcToE']              = {'nanoAOD' :''} ### Still missing
### Samples['QCD_Pt_170to250_bcToE']             = {'nanoAOD' :''} ### Still missing
### Samples['QCD_Pt_250toInf_bcToE']             = {'nanoAOD' :''} ### Still missing
### QCD MuEnrichedPt5
Samples['QCD_Pt-15to20_MuEnrichedPt5']       = {'nanoAOD' :'/QCD_Pt-15to20_MuEnrichedPt5_TuneCP5_13TeV_pythia8/RunIIAutumn18NanoAODv4-Nano14Dec2018_102X_upgrade2018_realistic_v16-v1/NANOAODSIM'}
Samples['QCD_Pt-20to30_MuEnrichedPt5']       = {'nanoAOD' :'/QCD_Pt-20to30_MuEnrichedPt5_TuneCP5_13TeV_pythia8/RunIIAutumn18NanoAODv4-Nano14Dec2018_102X_upgrade2018_realistic_v16-v1/NANOAODSIM'}
Samples['QCD_Pt-30to50_MuEnrichedPt5']       = {'nanoAOD' :'/QCD_Pt-30to50_MuEnrichedPt5_TuneCP5_13TeV_pythia8/RunIIAutumn18NanoAODv4-Nano14Dec2018_102X_upgrade2018_realistic_v16-v1/NANOAODSIM'}
Samples['QCD_Pt-50to80_MuEnrichedPt5']       = {'nanoAOD' :'/QCD_Pt-50to80_MuEnrichedPt5_TuneCP5_13TeV_pythia8/RunIIAutumn18NanoAODv4-Nano14Dec2018_102X_upgrade2018_realistic_v16-v1/NANOAODSIM'}
Samples['QCD_Pt-80to120_MuEnrichedPt5']      = {'nanoAOD' :'/QCD_Pt-80to120_MuEnrichedPt5_TuneCP5_13TeV_pythia8/RunIIAutumn18NanoAODv4-Nano14Dec2018_102X_upgrade2018_realistic_v16-v1/NANOAODSIM'}
Samples['QCD_Pt-80to120_MuEnrichedPt5_ext1']      = {'nanoAOD' :'/QCD_Pt-80to120_MuEnrichedPt5_TuneCP5_13TeV_pythia8/RunIIAutumn18NanoAODv4-Nano14Dec2018_102X_upgrade2018_realistic_v16_ext1-v1/NANOAODSIM'}
Samples['QCD_Pt-120to170_MuEnrichedPt5']     = {'nanoAOD' :'/QCD_Pt-120to170_MuEnrichedPt5_TuneCP5_13TeV_pythia8/RunIIAutumn18NanoAODv4-Nano14Dec2018_102X_upgrade2018_realistic_v16-v1/NANOAODSIM'}
Samples['QCD_Pt-120to170_MuEnrichedPt5_ext1']     = {'nanoAOD' :'/QCD_Pt-120to170_MuEnrichedPt5_TuneCP5_13TeV_pythia8/RunIIAutumn18NanoAODv4-Nano14Dec2018_102X_upgrade2018_realistic_v16_ext1-v2/NANOAODSIM'}
Samples['QCD_Pt-170to300_MuEnrichedPt5']     = {'nanoAOD' :'/QCD_Pt-170to300_MuEnrichedPt5_TuneCP5_13TeV_pythia8/RunIIAutumn18NanoAODv4-Nano14Dec2018_102X_upgrade2018_realistic_v16-v1/NANOAODSIM'}
Samples['QCD_Pt-300to470_MuEnrichedPt5']     = {'nanoAOD' :'/QCD_Pt-300to470_MuEnrichedPt5_TuneCP5_13TeV_pythia8/RunIIAutumn18NanoAODv4-Nano14Dec2018_102X_upgrade2018_realistic_v16-v1/NANOAODSIM'}
Samples['QCD_Pt-300to470_MuEnrichedPt5_ext3']     = {'nanoAOD' :'/QCD_Pt-300to470_MuEnrichedPt5_TuneCP5_13TeV_pythia8/RunIIAutumn18NanoAODv4-Nano14Dec2018_102X_upgrade2018_realistic_v16_ext3-v1/NANOAODSIM'}
Samples['QCD_Pt-470to600_MuEnrichedPt5']     = {'nanoAOD' :'/QCD_Pt-470to600_MuEnrichedPt5_TuneCP5_13TeV_pythia8/RunIIAutumn18NanoAODv4-Nano14Dec2018_102X_upgrade2018_realistic_v16-v1/NANOAODSIM'}
Samples['QCD_Pt-470to600_MuEnrichedPt5_ext1']     = {'nanoAOD' :'/QCD_Pt-470to600_MuEnrichedPt5_TuneCP5_13TeV_pythia8/RunIIAutumn18NanoAODv4-Nano14Dec2018_102X_upgrade2018_realistic_v16_ext1-v1/NANOAODSIM'}
Samples['QCD_Pt-600to800_MuEnrichedPt5']     = {'nanoAOD' :'/QCD_Pt-600to800_MuEnrichedPt5_TuneCP5_13TeV_pythia8/RunIIAutumn18NanoAODv4-Nano14Dec2018_102X_upgrade2018_realistic_v16-v1/NANOAODSIM'}
Samples['QCD_Pt-800to1000_MuEnrichedPt5']     = {'nanoAOD' :'/QCD_Pt-800to1000_MuEnrichedPt5_TuneCP5_13TeV_pythia8/RunIIAutumn18NanoAODv4-Nano14Dec2018_102X_upgrade2018_realistic_v16_ext3-v1/NANOAODSIM'}
Samples['QCD_Pt-1000toInf_MuEnrichedPt5']     = {'nanoAOD' :'/QCD_Pt-1000toInf_MuEnrichedPt5_TuneCP5_13TeV_pythia8/RunIIAutumn18NanoAODv4-Nano14Dec2018_102X_upgrade2018_realistic_v16-v1/NANOAODSIM'}
### QCD EMEnriched
Samples['QCD_Pt-15to20_EMEnriched']        = {'nanoAOD' :'/QCD_Pt-15to20_EMEnriched_TuneCP5_13TeV_pythia8/RunIIAutumn18NanoAODv4-Nano14Dec2018_102X_upgrade2018_realistic_v16_ext1-v1/NANOAODSIM'}
Samples['QCD_Pt-20to30_EMEnriched']        = {'nanoAOD' :'/QCD_Pt-20to30_EMEnriched_TuneCP5_13TeV_pythia8/RunIIAutumn18NanoAODv4-Nano14Dec2018_102X_upgrade2018_realistic_v16-v1/NANOAODSIM'}
Samples['QCD_Pt-30to50_EMEnriched']        = {'nanoAOD' :'/QCD_Pt-30to50_EMEnriched_TuneCP5_13TeV_pythia8/RunIIAutumn18NanoAODv4-Nano14Dec2018_102X_upgrade2018_realistic_v16_ext1-v1/NANOAODSIM'}
Samples['QCD_Pt-50to80_EMEnriched']        = {'nanoAOD' :'/QCD_Pt-50to80_EMEnriched_TuneCP5_13TeV_pythia8/RunIIAutumn18NanoAODv4-Nano14Dec2018_102X_upgrade2018_realistic_v16-v1/NANOAODSIM'}
Samples['QCD_Pt-80to120_EMEnriched']        = {'nanoAOD' :'/QCD_Pt-80to120_EMEnriched_TuneCP5_13TeV_pythia8/RunIIAutumn18NanoAODv4-Nano14Dec2018_102X_upgrade2018_realistic_v16-v1/NANOAODSIM'}
Samples['QCD_Pt-120to170_EMEnriched']        = {'nanoAOD' :'/QCD_Pt-120to170_EMEnriched_TuneCP5_13TeV_pythia8/RunIIAutumn18NanoAODv4-Nano14Dec2018_102X_upgrade2018_realistic_v16-v1/NANOAODSIM'}
Samples['QCD_Pt-170to300_EMEnriched']        = {'nanoAOD' :'/QCD_Pt-170to300_EMEnriched_TuneCP5_13TeV_pythia8/RunIIAutumn18NanoAODv4-Nano14Dec2018_102X_upgrade2018_realistic_v16-v1/NANOAODSIM'}
Samples['QCD_Pt-300toInf_EMEnriched']        = {'nanoAOD' :'/QCD_Pt-300toInf_EMEnriched_TuneCP5_13TeV_pythia8/RunIIAutumn18NanoAODv4-Nano14Dec2018_102X_upgrade2018_realistic_v16-v1/NANOAODSIM'}
### QCD DoubleEMEnriched

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Yutaro
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
### GJets

#Samples['GJetsDR04_HT40To100'] = {'nanoAOD': ''}
Samples['GJetsDR04_HT100To200'] = {'nanoAOD': '/GJets_DR-0p4_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18NanoAODv4-Nano14Dec2018_102X_upgrade2018_realistic_v16-v1/NANOAODSIM'}
Samples['GJetsDR04_HT200To400'] = {'nanoAOD': '/GJets_DR-0p4_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18NanoAODv4-Nano14Dec2018_102X_upgrade2018_realistic_v16-v1/NANOAODSIM'}
Samples['GJetsDR04_HT400To600'] = {'nanoAOD': '/GJets_DR-0p4_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18NanoAODv4-Nano14Dec2018_102X_upgrade2018_realistic_v16-v1/NANOAODSIM'}
Samples['GJetsDR04_HT600ToInf'] = {'nanoAOD': '/GJets_DR-0p4_HT-600ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18NanoAODv4-Nano14Dec2018_102X_upgrade2018_realistic_v16-v1/NANOAODSIM'}
Samples['GJets_HT40To100'] = {'nanoAOD': '/GJets_HT-40To100_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18NanoAODv4-Nano14Dec2018_102X_upgrade2018_realistic_v16-v1/NANOAODSIM'}
#Samples['GJets_HT40To100-ext1'] = {'nanoAOD': ''}

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Jonatan
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Samples['WWW']  = {'nanoAOD' :'/WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8/RunIIAutumn18NanoAODv4-Nano14Dec2018_102X_upgrade2018_realistic_v16_ext1-v1/NANOAODSIM'}
Samples['WWZ']  = {'nanoAOD' :'/WWZ_TuneCP5_13TeV-amcatnlo-pythia8/RunIIAutumn18NanoAODv4-Nano14Dec2018_102X_upgrade2018_realistic_v16_ext1-v1/NANOAODSIM'} 
Samples['WZZ']  = {'nanoAOD' :'/WZZ_TuneCP5_13TeV-amcatnlo-pythia8/RunIIAutumn18NanoAODv4-Nano14Dec2018_102X_upgrade2018_realistic_v16_ext1-v1/NANOAODSIM'}
Samples['ZZZ']  = {'nanoAOD' :'/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/RunIIAutumn18NanoAODv4-Nano14Dec2018_102X_upgrade2018_realistic_v16_ext1-v1/NANOAODSIM'}
Samples['WWG']  = {'nanoAOD' :'/WWG_TuneCP5_13TeV-amcatnlo-pythia8/RunIIAutumn18NanoAODv4-Nano14Dec2018_102X_upgrade2018_realistic_v16_ext1-v1/NANOAODSIM'}
Samples['Wg_MADGRAPHMLM'] = {'nanoAOD': '/WGToLNuG_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18NanoAODv4-Nano14Dec2018_102X_upgrade2018_realistic_v16-v1/NANOAODSIM'}

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Cedric
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
### TTbar 
Samples['TTTo2L2Nu'] = {'nanoAOD' :'/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/RunIIAutumn18NanoAODv4-Nano14Dec2018_102X_upgrade2018_realistic_v16-v1/NANOAODSIM'}
Samples['TTTo2L2Nu_CP5Up'] = {'nanoAOD' :'/TTTo2L2Nu_TuneCP5up_13TeV-powheg-pythia8/RunIIAutumn18NanoAODv4-Nano14Dec2018_102X_upgrade2018_realistic_v16-v1/NANOAODSIM'}
Samples['TTTo2L2Nu_CP5Down'] = {'nanoAOD' :'/TTTo2L2Nu_TuneCP5down_13TeV-powheg-pythia8/RunIIAutumn18NanoAODv4-Nano14Dec2018_102X_upgrade2018_realistic_v16-v1/NANOAODSIM'}
### Samples['TTTo2L2Nu_PSWeights'] = {'nanoAOD' :''} ### still missing
### Samples['TTTo2L2Nu_PSWeights_CP5Up'] = {'nanoAOD' :''} ### still missing
### Samples['TTTo2L2Nu_PSWeights_CP5Down'] = {'nanoAOD' :''} ### still missing
Samples['TTToSemiLeptonic'] = {'nanoAOD' :'/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8/RunIIAutumn18NanoAODv4-Nano14Dec2018_102X_upgrade2018_realistic_v16-v1/NANOAODSIM'}
Samples['TTZjets'] = {'nanoAOD' :'/ttZJets_TuneCP5_13TeV_madgraphMLM_pythia8/RunIIAutumn18NanoAODv4-Nano14Dec2018_102X_upgrade2018_realistic_v16_ext1-v1/NANOAODSIM'}
Samples['TTWjets'] = {'nanoAOD' :'/ttWJets_TuneCP5_13TeV_madgraphMLM_pythia8/RunIIAutumn18NanoAODv4-Nano14Dec2018_102X_upgrade2018_realistic_v16_ext1-v1/NANOAODSIM'}

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Pablo
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
## W + jets


#Samples['WJetsToLNu']={'nanoAOD':'/WJetsToLNu_13TeV_amcatnloFXFX_pythia8/'}
Samples['WJetsToLNu-LO'] = {'nanoAOD' :'/WJetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18NanoAODv4-Nano14Dec2018_102X_upgrade2018_realistic_v16-v1/NANOAODSIM'}
Samples['WJetsToLNu_HT70_100'] = {'nanoAOD': '/WJetsToLNu_HT-70To100_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18NanoAODv4-Nano14Dec2018_102X_upgrade2018_realistic_v16-v1/NANOAODSIM'}
Samples['WJetsToLNu_HT100_200'] = {'nanoAOD': '/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18NanoAODv4-Nano14Dec2018_102X_upgrade2018_realistic_v16-v1/NANOAODSIM'}
Samples['WJetsToLNu_HT200_400'] = {'nanoAOD': '/WJetsToLNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18NanoAODv4-Nano14Dec2018_102X_upgrade2018_realistic_v16-v1/NANOAODSIM'}
Samples['WJetsToLNu_HT400_600'] = {'nanoAOD': '/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18NanoAODv4-Nano14Dec2018_102X_upgrade2018_realistic_v16-v1/NANOAODSIM'}
Samples['WJetsToLNu_HT600_800'] = {'nanoAOD': '/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18NanoAODv4-Nano14Dec2018_102X_upgrade2018_realistic_v16-v1/NANOAODSIM'}
Samples['WJetsToLNu_HT800_1200'] = {'nanoAOD': '/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18NanoAODv4-Nano14Dec2018_102X_upgrade2018_realistic_v16-v1/NANOAODSIM'}
Samples['WJetsToLNu_HT1200_2500'] = {'nanoAOD': '/WJetsToLNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18NanoAODv4-Nano14Dec2018_102X_upgrade2018_realistic_v16-v1/NANOAODSIM'}
Samples['WJetsToLNu_HT2500_inf'] = {'nanoAOD': '/WJetsToLNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18NanoAODv4-Nano14Dec2018_102X_upgrade2018_realistic_v16-v1/NANOAODSIM'}

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Isabel
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ 
## DY M-4to50_HT
### --> DYJetsToLL_M-4to50_HT-XXXto200 are still missing
Samples['DYJetsToLL_M-4to50_HT-200to400']   = {'nanoAOD': '/DYJetsToLL_M-4to50_HT-200to400_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIIAutumn18NanoAODv4-Nano14Dec2018_102X_upgrade2018_realistic_v16-v1/NANOAODSIM'}
Samples['DYJetsToLL_M-4to50_HT-400to600']   = {'nanoAOD': '/DYJetsToLL_M-4to50_HT-400to600_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIIAutumn18NanoAODv4-Nano14Dec2018_102X_upgrade2018_realistic_v16-v1/NANOAODSIM'}
Samples['DYJetsToLL_M-4to50_HT-600toInf']   = {'nanoAOD': '/DYJetsToLL_M-4to50_HT-600toInf_TuneCP5_PSWeights_13TeV-madgraphMLM-pythia8/RunIIAutumn18NanoAODv4-Nano14Dec2018_102X_upgrade2018_realistic_v16-v1/NANOAODSIM'}
## DY M-10to50-LO
Samples['DYJetsToLL_M-10to50-LO']   = {'nanoAOD' :'/DYJetsToLL_M-10to50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18NanoAODv4-Nano14Dec2018_102X_upgrade2018_realistic_v16-v1/NANOAODSIM'}
## DY M-50-LO
Samples['DYJetsToLL_M-50-LO']     = {'nanoAOD' :'/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18NanoAODv4-Nano14Dec2018_102X_upgrade2018_realistic_v16-v2/NANOAODSIM'}
## DY TT_MuEle_M-50
### Samples['DYJetsToTT_MuEle_M-50'] = {'nanoAOD': ''} ### still missing
## DY M-50_HT
Samples['DYJetsToLL_M-50_HT-70to100'] = {'nanoAOD': '/DYJetsToLL_M-50_HT-70to100_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIIAutumn18NanoAODv4-Nano14Dec2018_102X_upgrade2018_realistic_v16-v1/NANOAODSIM'}
Samples['DYJetsToLL_M-50_HT-100to200'] = {'nanoAOD': '/DYJetsToLL_M-50_HT-100to200_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIIAutumn18NanoAODv4-Nano14Dec2018_102X_upgrade2018_realistic_v16-v1/NANOAODSIM'}
Samples['DYJetsToLL_M-50_HT-200to400'] = {'nanoAOD': '/DYJetsToLL_M-50_HT-200to400_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIIAutumn18NanoAODv4-Nano14Dec2018_102X_upgrade2018_realistic_v16-v1/NANOAODSIM'}
Samples['DYJetsToLL_M-50_HT-400to600'] = {'nanoAOD': '/DYJetsToLL_M-50_HT-400to600_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIIAutumn18NanoAODv4-Nano14Dec2018_102X_upgrade2018_realistic_v16-v1/NANOAODSIM'}
Samples['DYJetsToLL_M-50_HT-600to800'] = {'nanoAOD': '/DYJetsToLL_M-50_HT-600to800_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIIAutumn18NanoAODv4-Nano14Dec2018_102X_upgrade2018_realistic_v16-v1/NANOAODSIM'}
Samples['DYJetsToLL_M-50_HT-800to1200'] = {'nanoAOD': '/DYJetsToLL_M-50_HT-800to1200_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIIAutumn18NanoAODv4-Nano14Dec2018_102X_upgrade2018_realistic_v16-v1/NANOAODSIM'}
Samples['DYJetsToLL_M-50_HT-2500toInf'] = {'nanoAOD': '/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIIAutumn18NanoAODv4-Nano14Dec2018_102X_upgrade2018_realistic_v16-v1/NANOAODSIM'}
## DY M-50
Samples['DYJetsToLL_M-50'] = {'nanoAOD': '/DYJetsToLL_M-50_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIIAutumn18NanoAODv4-Nano14Dec2018_102X_upgrade2018_realistic_v16-v1/NANOAODSIM'}

## Single top
Samples['ST_t-channel_top']     = {'nanoAOD' :'/ST_t-channel_top_4f_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8/RunIIAutumn18NanoAODv4-Nano14Dec2018_102X_upgrade2018_realistic_v16-v1/NANOAODSIM'}
Samples['ST_t-channel_antitop'] = {'nanoAOD' :'/ST_t-channel_antitop_4f_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8/RunIIAutumn18NanoAODv4-Nano14Dec2018_102X_upgrade2018_realistic_v16-v1/NANOAODSIM'}
Samples['ST_tW_top_ext1']       = {'nanoAOD' :'/ST_tW_top_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/RunIIAutumn18NanoAODv4-Nano14Dec2018_102X_upgrade2018_realistic_v16_ext1-v1/NANOAODSIM'}
Samples['ST_tW_antitop_ext1']   = {'nanoAOD' :'/ST_tW_antitop_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/RunIIAutumn18NanoAODv4-Nano14Dec2018_102X_upgrade2018_realistic_v16_ext1-v1/NANOAODSIM'}
Samples['ST_s-channel_ext1']    = {'nanoAOD' :'/ST_s-channel_4f_leptonDecays_TuneCP5_13TeV-madgraph-pythia8/RunIIAutumn18NanoAODv4-Nano14Dec2018_102X_upgrade2018_realistic_v16_ext1-v1/NANOAODSIM'}

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Xavier/Kamiel
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
## VBS - signal
Samples['WpWpJJ_EWK_QCD'] = {'nanoAOD' :'/WpWpJJ_EWK-QCD_TuneCP5_13TeV-madgraph-pythia8/RunIIAutumn18NanoAODv4-Nano14Dec2018_102X_upgrade2018_realistic_v16-v1/NANOAODSIM'}
Samples['WpWpJJ_EWK'] = {'nanoAOD' :'/WpWpJJ_EWK_TuneCP5_13TeV-madgraph-pythia8/RunIIAutumn18NanoAODv4-Nano14Dec2018_102X_upgrade2018_realistic_v16-v1/NANOAODSIM'}
Samples['WpWpJJ_QCD'] = {'nanoAOD' :'/WpWpJJ_QCD_TuneCP5_13TeV-madgraph-pythia8/RunIIAutumn18NanoAODv4-Nano14Dec2018_102X_upgrade2018_realistic_v16-v1/NANOAODSIM'}
Samples['WpWmJJ_EWK'] = {'nanoAOD' :'/WWJJToLNuLNu_EWK_TuneCP5_13TeV-madgraph-pythia8/RunIIAutumn18NanoAODv4-Nano14Dec2018_102X_upgrade2018_realistic_v16_ext1-v1/NANOAODSIM'}
### Samples['WpWmJJ_QCD_noTop'] = {'nanoAOD' :''} ### still missing
Samples['WpWmJJ_EWK_QCD_noHiggs'] = {'nanoAOD' :'/WWJJToLNuLNu_EWK_QCD_noHiggs_TuneCP5_13TeV-madgraph-pythia8/RunIIAutumn18NanoAODv4-Nano14Dec2018_102X_upgrade2018_realistic_v16_ext1-v1/NANOAODSIM'}
### Samples['WpWmJJ_EWK_QCD_noTop_noHiggs'] = {'nanoAOD' :''} ### still missing

## VBS - specific backgrounds
Samples['WLLJJToLNu_M-60_EWK_4F']          = {'nanoAOD' :'/WLLJJ_WToLNu_EWK_TuneCP5_13TeV_madgraph-madspin-pythia8/RunIIAutumn18NanoAODv4-Nano14Dec2018_102X_upgrade2018_realistic_v16-v1/NANOAODSIM'}
Samples['WLLJJToLNu_M-50_QCD_0Jet']          = {'nanoAOD' :'/WZTo3LNu_0Jets_MLL-50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18NanoAODv4-Nano14Dec2018_102X_upgrade2018_realistic_v16-v1/NANOAODSIM'}
Samples['WLLJJToLNu_M-50_QCD_1Jet']          = {'nanoAOD' :'/WZTo3LNu_1Jets_MLL-50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18NanoAODv4-Nano14Dec2018_102X_upgrade2018_realistic_v16-v1/NANOAODSIM'}
Samples['WLLJJToLNu_M-50_QCD_2Jet']          = {'nanoAOD' :'/WZTo3LNu_2Jets_MLL-50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18NanoAODv4-Nano14Dec2018_102X_upgrade2018_realistic_v16-v1/NANOAODSIM'}
Samples['WLLJJToLNu_M-50_QCD_3Jet']          = {'nanoAOD' :'/WZTo3LNu_3Jets_MLL-50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18NanoAODv4-Nano14Dec2018_102X_upgrade2018_realistic_v16-v1/NANOAODSIM'}
Samples['WLLJJToLNu_M-4To60_EWK_4F']          = {'nanoAOD' :'/WLLJJ_WToLNu_EWK_TuneCP5_13TeV_madgraph-madspin-pythia8/RunIIAutumn18NanoAODv4-Nano14Dec2018_102X_upgrade2018_realistic_v16-v1/NANOAODSIM'}
Samples['WLLJJToLNu_M-4To50_QCD_0Jet']          = {'nanoAOD' :'/WZTo3LNu_0Jets_MLL-4to50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18NanoAODv4-Nano14Dec2018_102X_upgrade2018_realistic_v16-v1/NANOAODSIM'}
Samples['WLLJJToLNu_M-4To50_QCD_1Jet']          = {'nanoAOD' :'/WZTo3LNu_1Jets_MLL-4to50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18NanoAODv4-Nano14Dec2018_102X_upgrade2018_realistic_v16-v1/NANOAODSIM'}
Samples['WLLJJToLNu_M-4To50_QCD_2Jet']          = {'nanoAOD' :'/WZTo3LNu_2Jets_MLL-4to50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18NanoAODv4-Nano14Dec2018_102X_upgrade2018_realistic_v16-v1/NANOAODSIM'}
Samples['WLLJJToLNu_M-4To50_QCD_3Jet']          = {'nanoAOD' :'/WZTo3LNu_3Jets_MLL-4to50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18NanoAODv4-Nano14Dec2018_102X_upgrade2018_realistic_v16-v1/NANOAODSIM'}

Samples['TTZToLLNuNu_M-10']                = {'nanoAOD' :'/TTZToLLNuNu_M-10_TuneCP5_13TeV-amcatnlo-pythia8/RunIIAutumn18NanoAODv4-Nano14Dec2018_102X_upgrade2018_realistic_v16_ext1-v1/NANOAODSIM'}
Samples['TTWJetsToLNu']                    = {'nanoAOD' :'/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/RunIIAutumn18NanoAODv4-Nano14Dec2018_102X_upgrade2018_realistic_v16_ext1-v1/NANOAODSIM'}
Samples['WWTo2L2Nu_DoubleScattering'] = {'nanoAOD' :'/WWTo2L2Nu_DoubleScattering_13TeV-pythia8/RunIIAutumn18NanoAODv4-Nano14Dec2018_102X_upgrade2018_realistic_v16-v1/NANOAODSIM'}
Samples['tZq_ll'] = {'nanoAOD' :'/tZq_ll_4f_ckm_NLO_TuneCP5_13TeV-madgraph-pythia8/RunIIAutumn18NanoAODv4-Nano14Dec2018_102X_upgrade2018_realistic_v16_ext1-v1/NANOAODSIM'}

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# TEST samples for Jet efficiencies (Xavier) 
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Samples["QCD_HT200to300"]  = {'nanoAOD' :'/QCD_HT200to300_BGenFilter_TuneCP5_13TeV-madgraph-pythia8/RunIIAutumn18NanoAODv4-Nano14Dec2018_102X_upgrade2018_realistic_v16-v1/NANOAODSIM'}
Samples["QCD_HT300to500"]  = {'nanoAOD' :'/QCD_HT300to500_BGenFilter_TuneCP5_13TeV-madgraph-pythia8/RunIIAutumn18NanoAODv4-Nano14Dec2018_102X_upgrade2018_realistic_v16-v1/NANOAODSIM'}
Samples["QCD_HT700to1000"]  = {'nanoAOD' :'/QCD_HT700to1000_BGenFilter_TuneCP5_13TeV-madgraph-pythia8/RunIIAutumn18NanoAODv4-Nano14Dec2018_102X_upgrade2018_realistic_v16-v1/NANOAODSIM'}
Samples["QCD_HT1000to1500"]  = {'nanoAOD' :'/QCD_HT1000to1500_BGenFilter_TuneCP5_13TeV-madgraph-pythia8/RunIIAutumn18NanoAODv4-Nano14Dec2018_102X_upgrade2018_realistic_v16-v1/NANOAODSIM'}
Samples["QCD_HT1500to2000"]  = {'nanoAOD' :'/QCD_HT1500to2000_BGenFilter_TuneCP5_13TeV-madgraph-pythia8/RunIIAutumn18NanoAODv4-Nano14Dec2018_102X_upgrade2018_realistic_v16-v1/NANOAODSIM'}
Samples["QCD_HT2000toInf"]  = {'nanoAOD' :'/QCD_HT2000toInf_BGenFilter_TuneCP5_13TeV-madgraph-pythia8/RunIIAutumn18NanoAODv4-Nano14Dec2018_102X_upgrade2018_realistic_v16-v1/NANOAODSIM'}

