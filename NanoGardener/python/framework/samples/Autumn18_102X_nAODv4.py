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
Samples['Wg_AMCNLOFXFX']   = {'nanoAOD' :'/WGToLNuG_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18NanoAOD-102X_upgrade2018_realistic_v15-v1/NANOAODSIM'} 
Samples['ZZTo4L']          = {'nanoAOD' :'/ZZTo4L_TuneCP5_13TeV_powheg_pythia8/RunIIAutumn18NanoAOD-102X_upgrade2018_realistic_v15_ext1-v1/NANOAODSIM'}
Samples['ZZTo2L2Nu']       = {'nanoAOD' :'/ZZTo2L2Nu_TuneCP5_13TeV_powheg_pythia8/RunIIAutumn18NanoAOD-102X_upgrade2018_realistic_v15_ext1-v1/NANOAODSIM'}
Samples['WZ']  = {'nanoAOD' :'/WZ_TuneCP5_13TeV-pythia8/RunIIAutumn18NanoAOD-102X_upgrade2018_realistic_v15-v1/NANOAODSIM'}
Samples['ZZ']  = {'nanoAOD' :'/ZZ_TuneCP5_13TeV-pythia8/RunIIAutumn18NanoAOD-102X_upgrade2018_realistic_v15-v1/NANOAODSIM'}
Samples['WW-LO']  = {'nanoAOD' :'/WW_TuneCP5_13TeV-pythia8/RunIIAutumn18NanoAOD-102X_upgrade2018_realistic_v15-v1/NANOAODSIM'}

#Signals
Samples['VBFHToWWTo2L2NuPowheg_M125']   = {'nanoAOD' : '/VBFHToWWTo2L2Nu_M125_13TeV_powheg2_JHUGenV714_pythia8/RunIIAutumn18NanoAOD-102X_upgrade2018_realistic_v15-v1/NANOAODSIM'}
Samples['VBFHToTauTau_M125'] = {'nanoAOD' : '/VBFHToTauTau_M125_13TeV_powheg_pythia8/RunIIAutumn18NanoAOD-102X_upgrade2018_realistic_v15_ext1-v1/NANOAODSIM'}
Samples['HZJ_HToTauTau_M125'] = {'nanoAOD' : '/ZHToTauTau_M125_13TeV_powheg_pythia8/RunIIAutumn18NanoAOD-102X_upgrade2018_realistic_v15-v1/NANOAODSIM'}
Samples['GluGluHToWWTo2L2NuPowheg_M125'] = {'nanoAOD': '/GluGluHToWWTo2L2Nu_M125_13TeV_powheg2_JHUGenV714_pythia8/RunIIAutumn18NanoAOD-102X_upgrade2018_realistic_v15-v1/NANOAODSIM'}
Samples['GluGluHToWWTo2L2NuPowheg_M125_CP5Down'] = {'nanoAOD': '/GluGluHToWWTo2L2Nu_M125_13TeV_powheg2_JHUGenV714_pythia8-CP5Down/RunIIAutumn18NanoAOD-102X_upgrade2018_realistic_v15-v1/NANOAODSIM'}
Samples['GluGluHToTauTau_M125'] = {'nanoAOD' : '/GluGluHToTauTau_M125_13TeV_powheg_pythia8/RunIIAutumn18NanoAOD-102X_upgrade2018_realistic_v15-v1/NANOAODSIM'}

### WH Exclusive

### WH Inclusive
Samples['HWminusJ_HToWW_M125']     = {'nanoAOD' :'/HWminusJ_HToWW_M125_13TeV_powheg_jhugen724_pythia8_TuneCP5/RunIIAutumn18NanoAOD-102X_upgrade2018_realistic_v15-v1/NANOAODSIM'}
Samples['HWplusJ_HToWW_M125']      = {'nanoAOD' :'/HWplusJ_HToWW_M125_13TeV_powheg_jhugen724_pythia8_TuneCP5/RunIIAutumn18NanoAOD-102X_upgrade2018_realistic_v15-v1/NANOAODSIM'}
Samples['HWminusJ_HToTauTau_M125'] = {'nanoAOD' : '/WminusHToTauTau_M125_13TeV_powheg_pythia8/RunIIAutumn18NanoAOD-102X_upgrade2018_realistic_v15-v1/NANOAODSIM'}
Samples['HWplusJ_HToTauTau_M125']  = {'nanoAOD' :'/WplusHToTauTau_M125_13TeV_powheg_pythia8/RunIIAutumn18NanoAOD-102X_upgrade2018_realistic_v15-v1/NANOAODSIM'}

#### ZH exclusive ========
Samples['HZJ_HToWWTo2L2Nu_M125'] = {'nanoAOD' : '/HZJ_HToWWTo2L2Nu_M125_13TeV_powheg_jhugen714_pythia8_TuneCP5/RunIIAutumn18NanoAOD-102X_upgrade2018_realistic_v15-v1/NANOAODSIM'}
Samples['HZJ_HToWWTo2L2Nu_ZTo2L_M125'] = {'nanoAOD': '/HZJ_HToWWTo2L2Nu_ZTo2L_M125_13TeV_powheg_jhugen714_pythia8_TuneCP5/RunIIAutumn18NanoAOD-102X_upgrade2018_realistic_v15-v1/NANOAODSIM'}

#### ZH Inclusive ========
Samples['HZJ_HToWW_M125']     = {'nanoAOD' :'/HZJ_HToWW_M125_13TeV_powheg_jhugen714_pythia8_TuneCP5/RunIIAutumn18NanoAOD-102X_upgrade2018_realistic_v15-v1/NANOAODSIM'}
##Samples['HZJ_HToTauTau_M125']     = {'nanoAOD' :'/ZHToTauTau_M125_13TeV_powheg_pythia8/RunIIAutumn18NanoAOD-102X_upgrade2018_realistic_v15-v1/NANOAODSIM'}  --> already defined in signals

#### ggZH Inclusive ========

#### ggZH Exclusive ========

#### ttH Inclusive ========
Samples['ttHToNonbb_M125']  = {'nanoAOD' :'/ttHToNonbb_M125_TuneCP5_13TeV-powheg-pythia8/RunIIAutumn18NanoAOD-102X_upgrade2018_realistic_v15-v1/NANOAODSIM'}

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Alicia
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
### QCD fakes 

### MuEnriched
Samples['QCD_Pt-20to30_MuEnrichedPt5']        = {'nanoAOD' : '/QCD_Pt-20to30_MuEnrichedPt5_TuneCP5_13TeV_pythia8/RunIIAutumn18NanoAOD-102X_upgrade2018_realistic_v15-v1/NANOAODSIM'}
Samples['QCD_Pt-30to50_MuEnrichedPt5']        = {'nanoAOD' :'/QCD_Pt-30to50_MuEnrichedPt5_TuneCP5_13TeV_pythia8/RunIIAutumn18NanoAOD-102X_upgrade2018_realistic_v15-v1/NANOAODSIM'}
Samples['QCD_Pt-50to80_MuEnrichedPt5']        = {'nanoAOD' : '/QCD_Pt-50to80_MuEnrichedPt5_TuneCP5_13TeV_pythia8/RunIIAutumn18NanoAOD-102X_upgrade2018_realistic_v15-v1/NANOAODSIM'}
Samples['QCD_Pt-80to120_MuEnrichedPt5']       = {'nanoAOD' :'/QCD_Pt-80to120_MuEnrichedPt5_TuneCP5_13TeV_pythia8/RunIIAutumn18NanoAOD-102X_upgrade2018_realistic_v15-v1/NANOAODSIM'}
Samples['QCD_Pt-80to120_MuEnrichedPt5_ext1']  = {'nanoAOD' :'/QCD_Pt-80to120_MuEnrichedPt5_TuneCP5_13TeV_pythia8/RunIIAutumn18NanoAOD-102X_upgrade2018_realistic_v15_ext1-v1/NANOAODSIM'}
Samples['QCD_Pt-120to170_MuEnrichedPt5']      = {'nanoAOD' :'/QCD_Pt-120to170_MuEnrichedPt5_TuneCP5_13TeV_pythia8/RunIIAutumn18NanoAOD-102X_upgrade2018_realistic_v15-v1/NANOAODSIM'}
Samples['QCD_Pt-120to170_MuEnrichedPt5_ext1'] = {'nanoAOD' :'/QCD_Pt-120to170_MuEnrichedPt5_TuneCP5_13TeV_pythia8/RunIIAutumn18NanoAOD-102X_upgrade2018_realistic_v15_ext1-v1/NANOAODSIM'}
Samples['QCD_Pt-170to300_MuEnrichedPt5']      = {'nanoAOD' :'/QCD_Pt-170to300_MuEnrichedPt5_TuneCP5_13TeV_pythia8/RunIIAutumn18NanoAOD-102X_upgrade2018_realistic_v15-v1/NANOAODSIM'}
Samples['QCD_Pt-300to470_MuEnrichedPt5_ext3'] = {'nanoAOD' :'/QCD_Pt-300to470_MuEnrichedPt5_TuneCP5_13TeV_pythia8/RunIIAutumn18NanoAOD-102X_upgrade2018_realistic_v15_ext3-v1/NANOAODSIM'}
Samples['QCD_Pt-470to600_MuEnrichedPt5_ext1'] = {'nanoAOD' : '/QCD_Pt-470to600_MuEnrichedPt5_TuneCP5_13TeV_pythia8/RunIIAutumn18NanoAOD-102X_upgrade2018_realistic_v15_ext1-v1/NANOAODSIM'}
Samples['QCD_Pt-470to600_MuEnrichedPt5']     = {'nanoAOD' : '/QCD_Pt-470to600_MuEnrichedPt5_TuneCP5_13TeV_pythia8/RunIIAutumn18NanoAOD-102X_upgrade2018_realistic_v15-v1/NANOAODSIM'}
Samples['QCD_Pt-600to800_MuEnrichedPt5']      = {'nanoAOD' : '/QCD_Pt-600to800_MuEnrichedPt5_TuneCP5_13TeV_pythia8/RunIIAutumn18NanoAOD-102X_upgrade2018_realistic_v15-v1/NANOAODSIM'}
Samples['QCD_Pt-1000toInf_MuEnrichedPt5']     = {'nanoAOD' : '/QCD_Pt-1000toInf_MuEnrichedPt5_TuneCP5_13TeV_pythia8/RunIIAutumn18NanoAOD-102X_upgrade2018_realistic_v15-v1/NANOAODSIM'}

### EMEnriched
Samples['QCD_Pt-15to20_EMEnriched_ext1'] = {'nanoAOD' : '/QCD_Pt-15to20_EMEnriched_TuneCP5_13TeV_pythia8/RunIIAutumn18NanoAOD-102X_upgrade2018_realistic_v15_ext1-v1/NANOAODSIM'}
Samples['QCD_Pt-20to30_EMEnriched'] = {'nanoAOD' : '/QCD_Pt-20to30_EMEnriched_TuneCP5_13TeV_pythia8/RunIIAutumn18NanoAOD-102X_upgrade2018_realistic_v15-v1/NANOAODSIM'}
Samples['QCD_Pt-30to50_EMEnriched_ext1'] = {'nanoAOD' : '/QCD_Pt-30to50_EMEnriched_TuneCP5_13TeV_pythia8/RunIIAutumn18NanoAOD-102X_upgrade2018_realistic_v15_ext1-v1/NANOAODSIM'}
Samples['QCD_Pt-50to80_EMEnriched'] = {'nanoAOD' : '/QCD_Pt-50to80_EMEnriched_TuneCP5_13TeV_pythia8/RunIIAutumn18NanoAOD-102X_upgrade2018_realistic_v15-v1/NANOAODSIM'}
Samples['QCD_Pt-80to120_EMEnriched'] = {'nanoAOD' : '/QCD_Pt-80to120_EMEnriched_TuneCP5_13TeV_pythia8/RunIIAutumn18NanoAOD-102X_upgrade2018_realistic_v15-v1/NANOAODSIM'}
Samples['QCD_Pt-120to170_EMEnriched'] = {'nanoAOD' : '/QCD_Pt-120to170_EMEnriched_TuneCP5_13TeV_pythia8/RunIIAutumn18NanoAOD-102X_upgrade2018_realistic_v15-v1/NANOAODSIM'}
Samples['QCD_Pt-170to300_EMEnriched'] = {'nanoAOD' : '/QCD_Pt-170to300_EMEnriched_TuneCP5_13TeV_pythia8/RunIIAutumn18NanoAOD-102X_upgrade2018_realistic_v15-v1/NANOAODSIM'}
Samples['QCD_Pt-300toInf_EMEnriched'] = {'nanoAOD' : '/QCD_Pt-300toInf_EMEnriched_TuneCP5_13TeV_pythia8/RunIIAutumn18NanoAOD-102X_upgrade2018_realistic_v15-v1/NANOAODSIM'}

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Yutaro
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
### GJets

#Samples['GJetsDR04_HT40To100'] = {'nanoAOD': ''}
#Samples['GJetsDR04_HT100To200'] = {'nanoAOD': ''}
#Samples['GJetsDR04_HT200To400'] = {'nanoAOD': ''}
#Samples['GJetsDR04_HT400To600'] = {'nanoAOD': ''}
#Samples['GJetsDR04_HT600ToInf'] = {'nanoAOD': ''}
#Samples['GJets_HT40To100'] = {'nanoAOD': ''}
#Samples['GJets_HT40To100-ext1'] = {'nanoAOD': ''}

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Jonatan
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Samples['ZZZ']  = {'nanoAOD' :'/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/RunIIAutumn18NanoAOD-102X_upgrade2018_realistic_v15_ext1-v1/NANOAODSIM'}
Samples['Wg_MADGRAPHMLM'] = {'nanoAOD': '/WGToLNuG_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18NanoAOD-102X_upgrade2018_realistic_v15-v1/NANOAODSIM'}

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Cedric
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
## TTbar
Samples['TTTo2L2Nu'] = {'nanoAOD' :'/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/RunIIAutumn18NanoAOD-102X_upgrade2018_realistic_v15-v1/NANOAODSIM'}
Samples['TTTo2L2Nu_CP5Down'] = {'nanoAOD' :'/TTTo2L2Nu_TuneCP5down_13TeV-powheg-pythia8/RunIIAutumn18NanoAOD-102X_upgrade2018_realistic_v15-v1/NANOAODSIM'}
Samples['TTTo2L2Nu_CP5Up'] = {'nanoAOD' :'/TTTo2L2Nu_TuneCP5up_13TeV-powheg-pythia8/RunIIAutumn18NanoAOD-102X_upgrade2018_realistic_v15-v1/NANOAODSIM'}
Samples['TTToSemiLeptonic'] = {'nanoAOD' : '/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8/RunIIAutumn18NanoAOD-102X_upgrade2018_realistic_v15-v1/NANOAODSIM'}
Samples['TTWjets'] = {'nanoAOD' :'/ttWJets_TuneCP5_13TeV_madgraphMLM_pythia8/RunIIAutumn18NanoAOD-102X_upgrade2018_realistic_v15_ext1-v1/NANOAODSIM'}

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Pablo
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
## W + jets
Samples['WJetsToLNu_HT70_100'] = {'nanoAOD': '/WJetsToLNu_HT-70To100_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18NanoAOD-102X_upgrade2018_realistic_v15-v1/NANOAODSIM'}
Samples['WJetsToLNu_HT400_600'] = {'nanoAOD': '/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18NanoAOD-102X_upgrade2018_realistic_v15-v1/NANOAODSIM'}
Samples['WJetsToLNu_HT600_800'] = {'nanoAOD': '/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18NanoAOD-102X_upgrade2018_realistic_v15-v1/NANOAODSIM'}
Samples['WJetsToLNu_HT800_1200'] = {'nanoAOD': '/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18NanoAOD-102X_upgrade2018_realistic_v15-v1/NANOAODSIM'}
Samples['WJetsToLNu_HT2500_inf'] = {'nanoAOD': '/WJetsToLNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18NanoAOD-102X_upgrade2018_realistic_v15-v1/NANOAODSIM'}

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Isabel
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# DY
Samples['DYJetsToLL_M-10to50-LO']           = {'nanoAOD': '/DYJetsToLL_M-10to50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18NanoAOD-102X_upgrade2018_realistic_v15-v1/NANOAODSIM'}
Samples['DYJetsToLL_M-50-LO-ext1'] = {'nanoAOD' :'/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18NanoAOD-102X_upgrade2018_realistic_v15-v1/NANOAODSIM'}
Samples['DYJetsToLL_M-50']     = {'nanoAOD' :'/DYJetsToLL_M-50_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIIAutumn18NanoAOD-102X_upgrade2018_realistic_v15-v1/NANOAODSIM'}

# DY HT Bins - PSweights
Samples['DYJetsToLL_M-50_HT-70to100_PSWeights']     = {'nanoAOD':'/DYJetsToLL_M-50_HT-70to100_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIIAutumn18NanoAOD-102X_upgrade2018_realistic_v15-v1/NANOAODSIM'}
Samples['DYJetsToLL_M-50_HT-100to200_PSWeights']     = {'nanoAOD':'/DYJetsToLL_M-50_HT-100to200_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIIAutumn18NanoAOD-102X_upgrade2018_realistic_v15-v1/NANOAODSIM'}
Samples['DYJetsToLL_M-50_HT-400to600_PSWeights']     = {'nanoAOD':'/DYJetsToLL_M-50_HT-400to600_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIIAutumn18NanoAOD-102X_upgrade2018_realistic_v15-v7/NANOAODSIM'}
Samples['DYJetsToLL_M-50_HT-600to800_PSWeights']     = {'nanoAOD':'/DYJetsToLL_M-50_HT-600to800_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIIAutumn18NanoAOD-102X_upgrade2018_realistic_v15-v1/NANOAODSIM'}
Samples['DYJetsToLL_M-50_HT-800to1200_PSWeights']    = {'nanoAOD':'/DYJetsToLL_M-50_HT-800to1200_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIIAutumn18NanoAOD-102X_upgrade2018_realistic_v15-v1/NANOAODSIM'}

# Single Top
Samples['ST_tW_top'] = {'nanoAOD' :'/ST_tW_top_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/RunIIAutumn18NanoAOD-102X_upgrade2018_realistic_v15_ext1-v1/NANOAODSIM'}
Samples['ST_tW_antitop'] = {'nanoAOD' :'/ST_tW_antitop_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/RunIIAutumn18NanoAOD-102X_upgrade2018_realistic_v15_ext1-v1/NANOAODSIM'}


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Xavier/Kamiel
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
## VBS - signal

Samples['WpWpJJ_EWK_QCD'] = {'nanoAOD' : '/WpWpJJ_EWK-QCD_TuneCP5_13TeV-madgraph-pythia8/RunIIAutumn18NanoAOD-102X_upgrade2018_realistic_v15-v1/NANOAODSIM'}
Samples['WpWpJJ_QCD'] = {'nanoAOD' : '/WpWpJJ_QCD_TuneCP5_13TeV-madgraph-pythia8/RunIIAutumn18NanoAOD-102X_upgrade2018_realistic_v15-v1/NANOAODSIM'}
Samples['WpWmJJ_EWK_QCD_noTop_noHiggs'] = {'nanoAOD' :'/WWJJToLNuLNu_EWK_QCD_noTop-noHiggs_13TeV-madgraph-pythia8/RunIIAutumn18NanoAOD-102X_upgrade2018_realistic_v15-v1/NANOAODSIM'}

# Check these samples: 'TuneCP5' is missing here
# Samples['WpWmJJ_QCD_noTop'] = {'nanoAOD' : '/WWJJToLNuLNu_QCD_noTop_13TeV-madgraph-pythia8/RunIIAutumn18NanoAOD-102X_upgrade2018_realistic_v15-v1/NANOAODSIM'}
# Samples['WpWmJJ_EWK_QCD_noTop'] = {'nanoAOD' : '/WWJJToLNuLNu_EWK_QCD_noTop_13TeV-madgraph-pythia8/RunIIAutumn18NanoAOD-102X_upgrade2018_realistic_v15-v1/NANOAODSIM'}
# Samples['WpWmJJ_EWK_QCD_noTop_noHiggs'] = {'nanoAOD' : '/WWJJToLNuLNu_EWK_QCD_noTop-noHiggs_13TeV-madgraph-pythia8/RunIIAutumn18NanoAOD-102X_upgrade2018_realistic_v15-v1/NANOAODSIM'}

## VBS - specific backgrounds
Samples['WLLJJToLNu_M-50_QCD_2Jet']          = {'nanoAOD' :'/WZTo3LNu_2Jets_MLL-50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18NanoAOD-102X_upgrade2018_realistic_v15-v1/NANOAODSIM'}

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# TEST samples for Jet efficiencies (Xavier)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Samples["QCD_HT50to100"]  = {'nanoAOD' :'/QCD_HT50to100_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18NanoAOD-102X_upgrade2018_realistic_v15-v1/NANOAODSIM'}
Samples["QCD_HT100to200"]  = {'nanoAOD' :'/QCD_HT100to200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18NanoAOD-102X_upgrade2018_realistic_v15-v1/NANOAODSIM'}
Samples["QCD_HT200to300"]  = {'nanoAOD' :'/QCD_HT200to300_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18NanoAOD-102X_upgrade2018_realistic_v15-v1/NANOAODSIM'}
Samples["QCD_HT300to500"]  = {'nanoAOD' :'/QCD_HT300to500_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18NanoAOD-102X_upgrade2018_realistic_v15-v1/NANOAODSIM'}
Samples["QCD_HT500to700"]  = {'nanoAOD' :'/QCD_HT500to700_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18NanoAOD-102X_upgrade2018_realistic_v15-v1/NANOAODSIM'}
Samples["QCD_HT700to1000"]  = {'nanoAOD' :'/QCD_HT700to1000_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18NanoAOD-102X_upgrade2018_realistic_v15-v1/NANOAODSIM'}
Samples["QCD_HT1000to1500"]  = {'nanoAOD' :'/QCD_HT1000to1500_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18NanoAOD-102X_upgrade2018_realistic_v15-v1/NANOAODSIM'}
Samples["QCD_HT1500to2000"]  = {'nanoAOD' :'/QCD_HT1500to2000_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18NanoAOD-102X_upgrade2018_realistic_v15-v1/NANOAODSIM'}
Samples["QCD_HT2000toInf"]  = {'nanoAOD' :'/QCD_HT2000toInf_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18NanoAOD-102X_upgrade2018_realistic_v15-v1/NANOAODSIM'}

