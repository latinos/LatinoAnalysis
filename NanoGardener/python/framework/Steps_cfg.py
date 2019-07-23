#!/usr/bin/env python

## --------------------------------- Some predefined sequence Chains -----------------------------------------


# -------------------------------------------- HERE WE GO ----------------------------------------------------

Steps = {

# ------------------------------------------------ CHAINS ----------------------------------------------------

  'MCnofilter' : {
                  'isChain'    : True  ,
                  'do4MC'      : True  ,
                  'do4Data'    : False ,
                  'subTargets' : ['leptonMaker'],
                 },

## ------- MC:

# 'MCl1loose2016': {
#                 'isChain'    : True  ,
#                 'do4MC'      : True  ,
#                 'do4Data'    : False ,
#                 'selection'  : '"(nElectron>0 && Electron_pt[0]>10) || (nMuon>0 && Muon_pt[0]>10)"' , 
#                 'subTargets' : ['baseW', 'leptonMaker','lepSel', 'puW2016', 'l2Kin', 'l3Kin', 'l4Kin', 'btagPerJet2016', 'btagPerEvent'],
#               },

# 'MCl1loose2017': {
#                 'isChain'    : True  ,
#                 'do4MC'      : True  ,
#                 'do4Data'    : False ,
#                 'selection'  : '"((nElectron+nMuon)>0)"' ,
#                 'subTargets' : ['leptonMaker','lepSel', 'puW2017', 'l2Kin', 'l3Kin', 'l4Kin', 'btagPerJet2017', 'btagPerEvent'],
#               },


  'MCl1loose2016' :  {
                  'isChain'    : True  ,
                  'do4MC'      : True  ,
                  'do4Data'    : False ,
                  'selection'  : '"((nElectron+nMuon)>0)"' ,
                  'subTargets' : ['leptonMaker','lepSel','jetSel','CleanJetCut',
                                  'PromptParticlesGenVars','GenVar','GenLeptonMatch', 'HiggsGenVars', 'TopGenVars', 'wwNLL','WGammaStar', 'ggHTheoryUncertainty', 'DressedLeptons'],
                },

  'MCl1loose2016v5' :  {
                  'isChain'    : True  ,
                  'do4MC'      : True  ,
                  'do4Data'    : False ,
                  'selection'  : '"((nElectron+nMuon)>0)"' ,
                  'subTargets' : ['leptonMaker','lepSel','jetSelCustom',
                                  'PromptParticlesGenVars','GenVar','GenLeptonMatch', 'HiggsGenVars', 'TopGenVars', 'wwNLL','WGammaStar', 'ggHTheoryUncertainty', 'DressedLeptons'],
                },

  'MCl2loose2016_hmumu' :  {
                  'isChain'    : True  ,
                  'do4MC'      : True  ,
                  'do4Data'    : False ,
                  'selection'  : '"((nMuon)>1)"' ,
                  'subTargets' : ['leptonMaker','lepSel','jetSel_hmumu_2016','CleanJetCut',
                                  'PromptParticlesGenVars','GenVar','GenLeptonMatch','TriggerObjectMatch', 'HiggsGenVars', 'TopGenVars', 'wwNLL','WGammaStar', 'ggHTheoryUncertainty', 'DressedLeptons'],
                },

  # FIXME: check btagPerJet2016, btagPerEvent
  # FIXME: Cfg 'trigMC','LeptonSF','puW'
  'MCCorr2016' : {
                     'isChain'    : True  ,
                     'do4MC'      : True  ,
                     'do4Data'    : False ,
                     'subTargets' : ['baseW','PrefCorr2016','btagPerJet2016','EmbeddingVeto', 
                                     'rochesterMC','trigMC','LeptonSF','puW','l2Kin', 'l3Kin', 'l4Kin','formulasMC'],
                },

  'MCCorr2016_hmumu' : {
                     'isChain'    : True  ,
                     'do4MC'      : True  ,
                     'do4Data'    : False ,
                     'subTargets' : ['baseW','PrefCorr2016','btagPerJet2016','EmbeddingVeto', 
                                     'rochesterMC','trigMC','LeptonSF','puW','l2Kin', 'formulasMC'],
                },

  'MCCorr2016tmp'  : {
                     'isChain'    : True  ,
                     'do4MC'      : True  ,
                     'do4Data'    : False ,
                     'subTargets' : ['baseW','PrefCorr2016','puW','rochesterMC','l2Kin','formulasMC16tmp'],
                     'onlySample' : ['DYJetsToLL_M-50_ext2'],
                 },

  'MCMonoH2016' : {
                     'isChain'    : True  ,
                     'do4MC'      : True  ,
                     'do4Data'    : False ,
                     'subTargets' : ['MHTrigMC','MHSwitch2016','MonoHiggsMVA','l3Kin','formulasMCMH'],
                 },


### OLD Stuff begin

  'MCl1loose2017v2': {
                  'isChain'    : True  ,
                  'do4MC'      : True  ,
                  'do4Data'    : False ,
                  'selection'  : '"((nElectron+nMuon)>0)"' ,
                  'subTargets' : ['leptonMaker','lepSel', 'puW2017', 'l2Kin', 'l3Kin', 'l4Kin', 'btagPerJet2017', 'btagPerEvent','PrefCorr2017'],
                },

  'MCCorr2017OLD' : {
                 'isChain'    : True  ,
                  'do4MC'      : True  ,
                  'do4Data'    : False ,
                  'subTargets' : ['baseW','PrefCorr2017','jetSel','CleanJetCut', 'btagPerJet2017', 'btagPerEvent' ,
                                  'PromptParticlesGenVars','GenVar','GenLeptonMatch', 'HiggsGenVars', 'TopGenVars', 'wwNLL',
                                  'ggHTheoryUncertainty', 'DressedLeptons', 'WGammaStar',
                                  'rochesterMC','trigMC','LeptonSF','puW','l2Kin', 'l3Kin', 'l4Kin','formulasMC'],
                    },

  'MCCorr2017_SemiLep' : {
                 'isChain'    : True  ,
                  'do4MC'      : True  ,
                  'do4Data'    : False ,
                  'subTargets' : ['jetSel','CleanJetCut', 
                                  'PromptParticlesGenVars','GenVar','GenLeptonMatch', 'HiggsGenVars', 'TopGenVars', 'wwNLL',
                                  'ggHTheoryUncertainty', 'DressedLeptons', 
                                  'rochesterMC','trigMC'],
                    },

### OLD stuff End

  'MCl1loose2017' :  {
                  'isChain'    : True  ,
                  'do4MC'      : True  ,
                  'do4Data'    : False ,
                  'selection'  : '"((nElectron+nMuon)>0)"' ,
                  'subTargets' : ['leptonMaker','lepSel','jetSel','CleanJetCut',
                                  'PromptParticlesGenVars','GenVar','GenLeptonMatch', 'HiggsGenVars', 'TopGenVars', 'wwNLL','WGammaStar', 'ggHTheoryUncertainty', 'DressedLeptons'],
                },

  'MCl1loose2017v5' :  {
                  'isChain'    : True  ,
                  'do4MC'      : True  ,
                  'do4Data'    : False ,
                  'selection'  : '"((nElectron+nMuon)>0)"' ,
                  'subTargets' : ['leptonMaker','lepSel','jetSelCustom',
                                  'PromptParticlesGenVars','GenVar','GenLeptonMatch', 'HiggsGenVars', 'TopGenVars', 'wwNLL','WGammaStar', 'ggHTheoryUncertainty', 'DressedLeptons'],
                },

  'MCCorr2017' : {
                     'isChain'    : True  ,
                     'do4MC'      : True  ,
                     'do4Data'    : False ,
                     'subTargets' : ['baseW','PrefCorr2017','btagPerJet2017','EmbeddingVeto',
                                     'rochesterMC','trigMC','LeptonSF','puW','l2Kin', 'l3Kin', 'l4Kin','formulasMC'],
                },

  'MCCorr2017LP19' : {
                     'isChain'    : True  ,
                     'do4MC'      : True  ,
                     'do4Data'    : False ,
                     'subTargets' : ['baseW','PrefCorr2017','btagPerJet2017','EmbeddingVeto',
                                     'rochesterMCLP19','trigMC','LeptonSF','puW','l2Kin', 'l3Kin', 'l4Kin','formulasMCLP19'],
                },


  'PUFIXLP19' : {
                     'isChain'    : True  ,
                     'do4MC'      : True  ,
                     'do4Data'    : False ,
                     'subTargets' : ['puW','formulasMCLP19'],
  },               

  'MCl1loose2018' :  {
                  'isChain'    : True  ,
                  'do4MC'      : True  ,
                  'do4Data'    : False ,
                  'selection'  : '"((nElectron+nMuon)>0)"' ,
                  'subTargets' : ['leptonMaker','lepSel','jetSel','CleanJetCut',
                                  'PromptParticlesGenVars','GenVar','GenLeptonMatch', 'HiggsGenVars', 'TopGenVars', 'wwNLL','WGammaStar', 'ggHTheoryUncertainty', 'DressedLeptons'],
                },

  'MCl1loose2018v5' :  {
                  'isChain'    : True  ,
                  'do4MC'      : True  ,
                  'do4Data'    : False ,
                  'selection'  : '"((nElectron+nMuon)>0)"' ,
                  'subTargets' : ['leptonMaker','lepSel','jetSelCustom',
                                  'PromptParticlesGenVars','GenVar','GenLeptonMatch', 'HiggsGenVars', 'TopGenVars', 'wwNLL','WGammaStar', 'ggHTheoryUncertainty', 'DressedLeptons'],
                },


  'MCCorr2018' : {
                     'isChain'    : True  ,
                     'do4MC'      : True  ,
                     'do4Data'    : False ,
                     'subTargets' : ['baseW','btagPerJet2018','EmbeddingVeto',
                                     'rochesterMC','trigMC','LeptonSF','puW','l2Kin', 'l3Kin', 'l4Kin','formulasMC'],
                },

## ------- WgStar MC:

  'MCWgStar2017' : { 
                     'isChain'    : True  ,
                     'do4MC'      : True  ,
                     'do4Data'    : False ,
                     'selection'  : '"((nElectron+nMuon)>1)"' ,
                     'subTargets' : ['leptonMaker','WgSSel', 
                                     'PromptParticlesGenVars','GenVar','GenLeptonMatch', 'HiggsGenVars', 'TopGenVars', 'wwNLL','WGammaStar'],
                     'onlySample' : [
                                   'Wg500','Wg_AMCNLOFXFX','WZTo3LNu','Wg_MADGRAPHMLM',
                                   #'Wg500','Wg_AMCNLOFXFX','WZTo3LNu','WgStarLNuEE','WgStarLNuMuMu','Wg_MADGRAPHMLM',
                                   'DYJetsToLL_M-10to50', 'DYJetsToLL_M-50','DYJetsToLL_M-10to50ext3',
                                   'DYJetsToLL_M-5to50-LO','DYJetsToLL_M-50-LO-ext1',
                                   'TTTo2L2Nu', 'ST_tW_antitop', 'ST_tW_top', 'ST_s-channel', 'ST_t-channel_antitop', 'ST_t-channel_top', 'ZZTo2L2Nu',
                                   'ZZTo4L', 'ZZTo2L2Q', 
                                   'WWW', 'WWZ', 'WZZ', 'ZZZ',
                                   'GluGluToWWToENEN',
                                   'GluGluToWWToENMN',
                                   'GluGluToWWToENTN',
                                   'GluGluToWWToMNEN',
                                   'GluGluToWWToMNMN',
                                   'GluGluToWWToMNTN',
                                   'GluGluToWWToTNEN',
                                   'GluGluToWWToTNMN',
                                   'GluGluToWWToTNTN',
                                   'WZTo2L2Q','WZTo3LNu_mllmin01','WZTo3LNu', 'Zg', 
                                 ]
                   },

  'MCWgStarCorr2017' : {
                     'isChain'    : True  ,
                     'do4MC'      : True  ,
                     'do4Data'    : False ,
                     'subTargets' : ['baseW','PrefCorr2017','jetSel','CleanJetCut','btagPerJet2017', 'btagPerEvent',
                                     'rochesterMC','trigMC','LeptonSF','puW','l2Kin', 'l3Kin', 'l4Kin','formulasMC'],
                    },

   'MCWgStarCorr2017LP19' : {
                     'isChain'    : True  ,
                     'do4MC'      : True  ,
                     'do4Data'    : False ,
                     'subTargets' : ['baseW','PrefCorr2017','jetSel','CleanJetCut','btagPerJet2017', 'btagPerEvent',
                                     'rochesterMCLP19','trigMC','LeptonSF','puW','l2Kin', 'l3Kin', 'l4Kin','formulasMCLP19'],
                    }, 

## ------- DATA:
    
  'DATAl1loose2016': {
                  'isChain'    : True  ,
                  'do4MC'      : False ,
                  'do4Data'    : True  ,
                  'selection'  : '"((nElectron+nMuon)>0)"' ,
                  'subTargets' : ['leptonMaker','lepSel','jetSel','CleanJetCut', 'rochesterDATA' , 'l2Kin', 'l3Kin', 'l4Kin','trigData', 'formulasDATA'],
                },

  'DATAl1loose2016v5': {
                  'isChain'    : True  ,
                  'do4MC'      : False ,
                  'do4Data'    : True  ,
                  'selection'  : '"((nElectron+nMuon)>0)"' ,
                  #'subTargets' : ['leptonMaker','lepSel','jetSelCustom', 'rochesterDATA' , 'l2Kin', 'l3Kin', 'l4Kin','trigData','MHTrigData','MHSwitch2016', 'formulasDATA'],
                  'subTargets' : ['leptonMaker','lepSel','jetSelCustom', 'rochesterDATA' , 'l2Kin', 'l3Kin', 'l4Kin','trigData', 'formulasDATA'],
                 },

  'DATAl1loose2017': {
                  'isChain'    : True  ,
                  'do4MC'      : False ,
                  'do4Data'    : True  ,
                  'selection'  : '"((nElectron+nMuon)>0)"' ,
                  'subTargets' : ['leptonMaker','lepSel','jetSel','CleanJetCut', 'rochesterDATA' , 'l2Kin', 'l3Kin', 'l4Kin','trigData', 'formulasDATA'],
                },

  'DATAl1loose2017LP19': {
                  'isChain'    : True  ,
                  'do4MC'      : False ,
                  'do4Data'    : True  ,
                  'selection'  : '"((nElectron+nMuon)>0)"' ,
                  'subTargets' : ['leptonMaker','lepSel','jetSel','CleanJetCut', 'rochesterDATALP19' , 'l2Kin', 'l3Kin', 'l4Kin','trigData', 'formulasDATALP19'],
                },

  'DATAl1loose2017v5': {
                  'isChain'    : True  ,
                  'do4MC'      : False ,
                  'do4Data'    : True  ,
                  'selection'  : '"((nElectron+nMuon)>0)"' ,
                  'subTargets' : ['leptonMaker','lepSel','jetSelCustom', 'rochesterDATA' , 'l2Kin', 'l3Kin', 'l4Kin','trigData','MHTrigData','MHSwitch2017', 'formulasDATA'],
                },


# 'DATAl1loose2017': {
#                 'isChain'    : True  ,
#                 'do4MC'      : False ,
#                 'do4Data'    : True  ,
#                 'selection'  : '"((nElectron+nMuon)>0)"' ,
#                 'subTargets' : ['leptonMaker','lepSel', 'l2Kin', 'l3Kin', 'l4Kin','trigData','formulasDATA'],
#               }, 

  'DATAl1loose2017v2': {
                  'isChain'    : True  ,
                  'do4MC'      : False ,
                  'do4Data'    : True  ,
                  'selection'  : '"((nElectron+nMuon)>0)"' ,
                  'subTargets' : ['leptonMaker','lepSel', 'l2Kin', 'l3Kin', 'l4Kin','trigData','formulasDATA'],
                },

  'DATACorr2017' : {
                  'isChain'    : True  ,
                  'do4MC'      : False ,
                  'do4Data'    : True  ,
                  'subTargets' : ['rochesterDATA','jetSel','CleanJetCut','l2Kin', 'l3Kin', 'l4Kin','formulasDATA'],
                },

  'DATAl1loose2018': {
                  'isChain'    : True  ,
                  'do4MC'      : False ,
                  'do4Data'    : True  ,
                  'selection'  : '"((nElectron+nMuon)>0)"' ,
                  'subTargets' : ['leptonMaker','lepSel','jetSel','CleanJetCut', 'rochesterDATA' , 'l2Kin', 'l3Kin', 'l4Kin','trigData', 'formulasDATA'],
                },

  'DATAl1loose2018v5': {
                  'isChain'    : True  ,
                  'do4MC'      : False ,
                  'do4Data'    : True  ,
                  'selection'  : '"((nElectron+nMuon)>0)"' ,
                  'subTargets' : ['leptonMaker','lepSel','jetSelCustom', 'rochesterDATA' , 'l2Kin', 'l3Kin', 'l4Kin','trigData', 'formulasDATA'],
                },


  'jetSelfix': {
                  'isChain'    : True  ,
                  'do4MC'      : True ,
                  'do4Data'    : True  , 
                  'subTargets' : ['jetSel','l2Kin', 'l3Kin', 'l4Kin']
               },

## ------- WgStar DATA:

    'DATAWgStar2017v2' : { 
                  'isChain'    : True  ,
                  'do4MC'      : False ,
                  'do4Data'    : True  ,
                  'selection'  : '"((nElectron+nMuon)>1)"' ,
                  'subTargets' : ['leptonMaker','WgSSel', 'rochesterDATA','jetSel','CleanJetCut' , 'l2Kin', 'l3Kin', 'l4Kin','trigData','formulasDATA'],
                   },

   'DATAWgStar2017LP19': {
                  'isChain'    : True  ,
                  'do4MC'      : False ,
                  'do4Data'    : True  ,
                  'selection'  : '"((nElectron+nMuon)>0)"' ,
                  'subTargets' : ['leptonMaker','WgSSel','jetSel','CleanJetCut', 'rochesterDATALP19' , 'l2Kin', 'l3Kin', 'l4Kin','trigData', 'formulasDATALP19'],
                },


## ------- EMBEDDING:

    'Embedding2017' : { 
                  'isChain'    : True  ,
                  'do4MC'      : False ,
                  'do4Data'    : True  ,
                  'subTargets' : ['EmbeddingWeights2017','trigMCKeepRun','LeptonSF','formulasEMBED'],
                   },

    'Embedding2016' : { 
                  'isChain'    : True  ,
                  'do4MC'      : False ,
                  'do4Data'    : True  ,
                  'subTargets' : ['EmbeddingWeights2016','trigMCKeepRun','LeptonSF','formulasEMBED'],
                   },

# ------------------------------------------------ MODULES ---------------------------------------------------

## ------- MODULES: MonoHiggs

#### MHTrigs step only works for 2016 and 2017 for now !!!!!!
  'MHTrigData' : { 
                  'isChain'  : False ,
                  'do4MC'    : False ,
                  'do4Data'  : True  ,
                  'import'   : 'LatinoAnalysis.NanoGardener.modules.TrigMaker' ,
                  'declare'  : 'MHTrigData = lambda : TrigMaker("RPLME_CMSSW",True,keepRunP=True,cfg_path="LatinoAnalysis/NanoGardener/python/data/TrigMakerMonoHiggs_cfg.py")',
                  'module'   : 'MHTrigData()',
               },

  'MHTrigMC'   : { 
                  'isChain'  : False ,
                  'do4MC'    : True  ,
                  'do4Data'  : False ,
                  'import'   : 'LatinoAnalysis.NanoGardener.modules.TrigMaker' ,
                  'declare'  : 'MHTrigMC = lambda : TrigMaker("RPLME_CMSSW",False,keepRunP=True,cfg_path="LatinoAnalysis/NanoGardener/python/data/TrigMakerMonoHiggs_cfg.py")',
                  'module'   : 'MHTrigMC()',
               },
####

  'MHSwitch2016' : { 
                  'isChain'  : False ,
                  'do4MC'    : True  ,
                  'do4Data'  : True ,
                  'import'   : 'LatinoAnalysis.NanoGardener.modules.Switch' ,
                  'declare'  : 'MHSwitch2016 = lambda : Switch(cfg_path="LatinoAnalysis/NanoGardener/python/data/switch/MH16_triggerSwitch_cfg.py")',
                  'module'   : 'MHSwitch2016()',
               },

  'MHSwitch2017' : { 
                  'isChain'  : False ,
                  'do4MC'    : True  ,
                  'do4Data'  : True ,
                  'import'   : 'LatinoAnalysis.NanoGardener.modules.Switch' ,
                  'declare'  : 'MHSwitch2017 = lambda : Switch(cfg_path="LatinoAnalysis/NanoGardener/python/data/switch/MH17_triggerSwitch_cfg.py")',
                  'module'   : 'MHSwitch2017()',
               },

  'MonoHiggsMVA' : { 
                  'isChain'  : False ,
                  'do4MC'    : True  ,
                  'do4Data'  : True ,
                  'import'   : 'LatinoAnalysis.NanoGardener.modules.TMVAfiller' ,
                  'declare'  : 'MonoHiggsMVA = lambda : TMVAfiller("data/MonoHiggsMVA_cfg.py")',
                  'module'   : 'MonoHiggsMVA()',
               },


## ------- MODULES: MC Kinematic
  
  'PromptParticlesGenVars' : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.PromptParticlesGenVarsProducer' ,
                  'declare'    : 'PromptParticlesGenVars = lambda : PromptParticlesGenVarsProducer()',
                  'module'     : 'PromptParticlesGenVars()',
                  } , 


  'GenVar'       : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.GenVarProducer' ,
                  'declare'    : 'GenVar = lambda : GenVarProducer()',
                  'module'     : 'GenVar()' ,
                   },

  'GenLeptonMatch' : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.GenLeptonMatchProducer' ,
                  'declare'    : 'GenLeptonMatch = lambda : GenLeptonMatchProducer()',
                  'module'     : 'GenLeptonMatch()' ,
                   },

  'TriggerObjectMatch' : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.TriggerObjectMatchProducer' ,
                  'declare'    : 'TriggerObjectMatch = lambda : TriggerObjectMatchProducer()',
                  'module'     : 'TriggerObjectMatch()' ,
                   },

   'HiggsGenVars' : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.HiggsGenVarsProducer' ,
                  'declare'    : 'HiggsGenVars = lambda : HiggsGenVarsProducer()',
                  'module'     : 'HiggsGenVars()',
                  } ,                 

   'DressedLeptons': {
                   'isChain'    : False ,
                   'do4MC'      : True  ,
                   'do4Data'    : False  ,
                   'import'     : 'LatinoAnalysis.NanoGardener.modules.DressedLeptonProducer' ,
                   'declare'    : 'dressedLeptons = lambda : DressedLeptonProducer(0.3)',
                   'module'     : 'dressedLeptons()' 
                  },

   'ggHTheoryUncertainty':  {
                   'isChain'    : False ,
                   'do4MC'      : True  ,
                   'do4Data'    : False  ,
                   'import'     : 'LatinoAnalysis.NanoGardener.modules.GGHUncertaintyProducer' ,
                   'declare'    : 'ggHUncertaintyProducer = lambda : GGHUncertaintyProducer()',
                   'module'     : 'ggHUncertaintyProducer()',
                   'onlySample' : [
                                  'GluGluHToWWTo2L2NuPowheg_M125_PrivateNano'
                                  ]
                  },    

   'TopGenVars' : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.TopGenVarsProducer' ,
                  'declare'    : 'TopGenVars = lambda : TopGenVarsProducer()',
                  'module'     : 'TopGenVars()',
                  'onlySample' : [
                                  'TTTo2L2Nu',
                                  'TTTo2L2Nu_PSWeights_CP5Down',
                                  'TTTo2L2Nu_PSWeights_CP5Up',
                                  'TTTo2L2Nu_PSWeights',
                                  'TTToSemiLeptonic',
                                  'TTWjets',
                                  'TTZjets',
                                  'ST_s-channel',
                                  'ST_t-channel_antitop',
                                  'ST_t-channel_top',
                                  'ST_tW_antitop',
                                  'ST_tW_top',
                                 ]
                  } ,

    'wwNLL' : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.wwNLLcorrectionWeightProducer' ,
                  'declare'    : 'wwNLL = lambda : wwNLLcorrectionWeightProducer()',
                  'module'     : 'wwNLL()',
                  'onlySample' : ['WW-LO', 'WWTo2L2Nu', 'WWTo2L2Nu_CP5Up', 'WWTo2L2Nu_CP5Down']
                  } ,

    'WGammaStar' : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.WGammaStar',
                  'declare'    : 'wGS = lambda : WGammaStar()',
                  'module'     : 'wGS()',
                  } ,

    'redoWGammaStar' : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.WGammaStar',
                  'declare'    : 'wGS = lambda : WGammaStar()',
                  'module'     : 'wGS()',
                  'onlySample' : ['WZTo3LNu','Wg_MADGRAPHMLM','WZ','WZTo2L2Q'],
                  } ,

    'BWReweight' : { 
                  'isChain'    : False ,
                  'do4MC'      : True ,
                  'do4Data'    : False  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.BWEwkSingletReweighter' ,
                  'declare'    : 'BWEwkSingRew = lambda : BWEwkSingletReweighter(year=RPLME_YEAR)',
                  'module'     : 'BWEwkSingRew()',
                  'onlySample' : ['GluGluHToWWTo2L2Nu_M115', 'GluGluHToWWTo2L2Nu_M120', 'GluGluHToWWTo2L2Nu_M124', 'GluGluHToWWTo2L2Nu_M125', 'GluGluHToWWTo2L2Nu_M126', 'GluGluHToWWTo2L2Nu_M130', 'GluGluHToWWTo2L2Nu_M135', 'GluGluHToWWTo2L2Nu_M140', 'GluGluHToWWTo2L2Nu_M145', 'GluGluHToWWTo2L2Nu_M150', 'GluGluHToWWTo2L2Nu_M155', 'GluGluHToWWTo2L2Nu_M160', 'GluGluHToWWTo2L2Nu_M165', 'GluGluHToWWTo2L2Nu_M170', 'GluGluHToWWTo2L2Nu_M175', 'GluGluHToWWTo2L2Nu_M180', 'GluGluHToWWTo2L2Nu_M190', 'GluGluHToWWTo2L2Nu_M200', 'GluGluHToWWTo2L2Nu_M210', 'GluGluHToWWTo2L2Nu_M230', 'GluGluHToWWTo2L2Nu_M250', 'GluGluHToWWTo2L2Nu_M270', 'GluGluHToWWTo2L2Nu_M300', 'GluGluHToWWTo2L2Nu_M350', 'GluGluHToWWTo2L2Nu_M400', 'GluGluHToWWTo2L2Nu_M450', 'GluGluHToWWTo2L2Nu_M500', 'GluGluHToWWTo2L2Nu_M550', 'GluGluHToWWTo2L2Nu_M600', 'GluGluHToWWTo2L2Nu_M650', 'GluGluHToWWTo2L2Nu_M700', 'GluGluHToWWTo2L2Nu_M750', 'GluGluHToWWTo2L2Nu_M800', 'GluGluHToWWTo2L2Nu_M850', 'GluGluHToWWTo2L2Nu_M900', 'GluGluHToWWTo2L2Nu_M1000', 'GluGluHToWWTo2L2Nu_M1500', 'GluGluHToWWTo2L2Nu_M2000', 'GluGluHToWWTo2L2Nu_M2500', 'GluGluHToWWTo2L2Nu_M3000', 'GluGluHToWWTo2L2Nu_M4000', 'GluGluHToWWTo2L2Nu_M5000',
                                  'VBFHToWWTo2L2Nu_M115', 'VBFHToWWTo2L2Nu_M120', 'VBFHToWWTo2L2Nu_M124', 'VBFHToWWTo2L2Nu_M125', 'VBFHToWWTo2L2Nu_M126', 'VBFHToWWTo2L2Nu_M130', 'VBFHToWWTo2L2Nu_M135', 'VBFHToWWTo2L2Nu_M140', 'VBFHToWWTo2L2Nu_M145', 'VBFHToWWTo2L2Nu_M150', 'VBFHToWWTo2L2Nu_M155', 'VBFHToWWTo2L2Nu_M160', 'VBFHToWWTo2L2Nu_M165', 'VBFHToWWTo2L2Nu_M170', 'VBFHToWWTo2L2Nu_M175', 'VBFHToWWTo2L2Nu_M180', 'VBFHToWWTo2L2Nu_M190', 'VBFHToWWTo2L2Nu_M200', 'VBFHToWWTo2L2Nu_M210', 'VBFHToWWTo2L2Nu_M230', 'VBFHToWWTo2L2Nu_M250', 'VBFHToWWTo2L2Nu_M270', 'VBFHToWWTo2L2Nu_M300', 'VBFHToWWTo2L2Nu_M350', 'VBFHToWWTo2L2Nu_M400', 'VBFHToWWTo2L2Nu_M450', 'VBFHToWWTo2L2Nu_M500', 'VBFHToWWTo2L2Nu_M550', 'VBFHToWWTo2L2Nu_M600', 'VBFHToWWTo2L2Nu_M650', 'VBFHToWWTo2L2Nu_M700', 'VBFHToWWTo2L2Nu_M750', 'VBFHToWWTo2L2Nu_M800', 'VBFHToWWTo2L2Nu_M850', 'VBFHToWWTo2L2Nu_M900', 'VBFHToWWTo2L2Nu_M1000', 'VBFHToWWTo2L2Nu_M1500', 'VBFHToWWTo2L2Nu_M2000', 'VBFHToWWTo2L2Nu_M2500', 'VBFHToWWTo2L2Nu_M3000', 'VBFHToWWTo2L2Nu_M4000', 'VBFHToWWTo2L2Nu_M5000',
                                  'GluGluHToWWTo2L2Nu_JHUGen698_M300', 'GluGluHToWWTo2L2Nu_JHUGen698_M350', 'GluGluHToWWTo2L2Nu_JHUGen698_M400', 'GluGluHToWWTo2L2Nu_JHUGen698_M450', 'GluGluHToWWTo2L2Nu_JHUGen698_M500', 'GluGluHToWWTo2L2Nu_JHUGen698_M550', 'GluGluHToWWTo2L2Nu_JHUGen698_M600', 'GluGluHToWWTo2L2Nu_JHUGen698_M650', 'GluGluHToWWTo2L2Nu_JHUGen698_M700', 'GluGluHToWWTo2L2Nu_JHUGen698_M750', 'GluGluHToWWTo2L2Nu_JHUGen698_M800', 'GluGluHToWWTo2L2Nu_JHUGen698_M850', 'GluGluHToWWTo2L2Nu_JHUGen698_M900', 'GluGluHToWWTo2L2Nu_JHUGen698_M1000', 'GluGluHToWWTo2L2Nu_JHUGen698_M1500', 'GluGluHToWWTo2L2Nu_JHUGen698_M2000', 'GluGluHToWWTo2L2Nu_JHUGen698_M2500', 'GluGluHToWWTo2L2Nu_JHUGen698_M3000', 'GluGluHToWWTo2L2Nu_JHUGen698_M4000', 'GluGluHToWWTo2L2Nu_JHUGen698_M5000', 'GluGluHToWWTo2L2Nu_JHUGen714_M4000', 'GluGluHToWWTo2L2Nu_JHUGen714_M5000',
                                  'VBFHToWWTo2L2Nu_JHUGen698_M300', 'VBFHToWWTo2L2Nu_JHUGen698_M350', 'VBFHToWWTo2L2Nu_JHUGen698_M400', 'VBFHToWWTo2L2Nu_JHUGen698_M450', 'VBFHToWWTo2L2Nu_JHUGen698_M500', 'VBFHToWWTo2L2Nu_JHUGen698_M550', 'VBFHToWWTo2L2Nu_JHUGen698_M600', 'VBFHToWWTo2L2Nu_JHUGen698_M650', 'VBFHToWWTo2L2Nu_JHUGen698_M700', 'VBFHToWWTo2L2Nu_JHUGen698_M750', 'VBFHToWWTo2L2Nu_JHUGen698_M800', 'VBFHToWWTo2L2Nu_JHUGen698_M850', 'VBFHToWWTo2L2Nu_JHUGen698_M900', 'VBFHToWWTo2L2Nu_JHUGen698_M1000', 'VBFHToWWTo2L2Nu_JHUGen698_M1500', 'VBFHToWWTo2L2Nu_JHUGen698_M2000', 'VBFHToWWTo2L2Nu_JHUGen698_M2500', 'VBFHToWWTo2L2Nu_JHUGen698_M3000', 'VBFHToWWTo2L2Nu_JHUGen698_M4000', 'VBFHToWWTo2L2Nu_JHUGen698_M5000', 'VBFHToWWTo2L2Nu_JHUGen714_M4000', 'VBFHToWWTo2L2Nu_JHUGen714_M5000',
                                  'GluGluHToWWToLNuQQ_M115', 'GluGluHToWWToLNuQQ_M120', 'GluGluHToWWToLNuQQ_M124', 'GluGluHToWWToLNuQQ_M125', 'GluGluHToWWToLNuQQ_M126', 'GluGluHToWWToLNuQQ_M130', 'GluGluHToWWToLNuQQ_M135', 'GluGluHToWWToLNuQQ_M140', 'GluGluHToWWToLNuQQ_M145', 'GluGluHToWWToLNuQQ_M150', 'GluGluHToWWToLNuQQ_M155', 'GluGluHToWWToLNuQQ_M160', 'GluGluHToWWToLNuQQ_M165', 'GluGluHToWWToLNuQQ_M170', 'GluGluHToWWToLNuQQ_M175', 'GluGluHToWWToLNuQQ_M180', 'GluGluHToWWToLNuQQ_M190', 'GluGluHToWWToLNuQQ_M200', 'GluGluHToWWToLNuQQ_M210', 'GluGluHToWWToLNuQQ_M230', 'GluGluHToWWToLNuQQ_M250', 'GluGluHToWWToLNuQQ_M270', 'GluGluHToWWToLNuQQ_M300', 'GluGluHToWWToLNuQQ_M350', 'GluGluHToWWToLNuQQ_M400', 'GluGluHToWWToLNuQQ_M450', 'GluGluHToWWToLNuQQ_M500', 'GluGluHToWWToLNuQQ_M550', 'GluGluHToWWToLNuQQ_M600', 'GluGluHToWWToLNuQQ_M650', 'GluGluHToWWToLNuQQ_M700', 'GluGluHToWWToLNuQQ_M750', 'GluGluHToWWToLNuQQ_M800', 'GluGluHToWWToLNuQQ_M850', 'GluGluHToWWToLNuQQ_M900', 'GluGluHToWWToLNuQQ_M1000', 'GluGluHToWWToLNuQQ_M1500', 'GluGluHToWWToLNuQQ_M2000', 'GluGluHToWWToLNuQQ_M2500', 'GluGluHToWWToLNuQQ_M3000', 'GluGluHToWWToLNuQQ_M4000', 'GluGluHToWWToLNuQQ_M5000',
                                  'VBFHToWWToLNuQQ_M115', 'VBFHToWWToLNuQQ_M120', 'VBFHToWWToLNuQQ_M124', 'VBFHToWWToLNuQQ_M125', 'VBFHToWWToLNuQQ_M126', 'VBFHToWWToLNuQQ_M130', 'VBFHToWWToLNuQQ_M135', 'VBFHToWWToLNuQQ_M140', 'VBFHToWWToLNuQQ_M145', 'VBFHToWWToLNuQQ_M150', 'VBFHToWWToLNuQQ_M155', 'VBFHToWWToLNuQQ_M160', 'VBFHToWWToLNuQQ_M165', 'VBFHToWWToLNuQQ_M170', 'VBFHToWWToLNuQQ_M175', 'VBFHToWWToLNuQQ_M180', 'VBFHToWWToLNuQQ_M190', 'VBFHToWWToLNuQQ_M200', 'VBFHToWWToLNuQQ_M210', 'VBFHToWWToLNuQQ_M230', 'VBFHToWWToLNuQQ_M250', 'VBFHToWWToLNuQQ_M270', 'VBFHToWWToLNuQQ_M300', 'VBFHToWWToLNuQQ_M350', 'VBFHToWWToLNuQQ_M400', 'VBFHToWWToLNuQQ_M450', 'VBFHToWWToLNuQQ_M500', 'VBFHToWWToLNuQQ_M550', 'VBFHToWWToLNuQQ_M600', 'VBFHToWWToLNuQQ_M650', 'VBFHToWWToLNuQQ_M700', 'VBFHToWWToLNuQQ_M750', 'VBFHToWWToLNuQQ_M800', 'VBFHToWWToLNuQQ_M850', 'VBFHToWWToLNuQQ_M900', 'VBFHToWWToLNuQQ_M1000', 'VBFHToWWToLNuQQ_M1500', 'VBFHToWWToLNuQQ_M2000', 'VBFHToWWToLNuQQ_M2500', 'VBFHToWWToLNuQQ_M3000', 'VBFHToWWToLNuQQ_M4000', 'VBFHToWWToLNuQQ_M5000']
               },

## ------- MODULES: Object Handling

  'Dummy' : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : True  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.Dummy' ,
                  'module'     : 'Dummy()',
            },

  'leptonMaker': {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : True  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.LeptonMaker' ,
                  'declare'    : 'leptonMaker = lambda : LeptonMaker()' ,
                  'module'     : 'leptonMaker()' ,
               }, 

   'lepSel': {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : True  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.LeptonSel' ,
                  'declare'    : 'leptonSel = lambda : LeptonSel("RPLME_CMSSW", "Loose", 1)' ,
                  'module'     : 'leptonSel()' ,
               },

   'WgSSel' : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : True  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.LeptonSel' ,
                  'declare'    : 'leptonSel = lambda : LeptonSel("RPLME_CMSSW", "WgStar", 2)' ,
                  'module'     : 'leptonSel()' ,
               },             

   'jetSel'  : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : True  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.JetSel' ,
                  # jetid=2,pujetid='loose',minpt=15.0,maxeta=4.7,jetColl="CleanJet"
                  'declare'    : 'jetSel = lambda : JetSel(2,"medium",15.0,4.7,"CleanJet")' ,
                  'module'     : 'jetSel()' ,
               },

   'jetSelCustom' : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : True  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.JetSel' ,
                  # jetid=2,pujetid='loose',minpt=15.0,maxeta=4.7,jetColl="CleanJet"
                  'declare'    : 'jetSel = lambda : JetSel(2,"custom",15.0,4.7,"CleanJet")' ,
                  'module'     : 'jetSel()' ,
               },


   'CleanJetCut' : {
                 'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : True  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.CopyCleanJet',
                  'declare'    : 'cleanJetCut = lambda : CopyCleanJet(newcollectionname="CleanJetCut", cuts=["eta>2.65","eta<3.139"])',
                  'module'     : 'cleanJetCut()',
               }, 

   'susyGen': {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : False ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.SusyGenVarsProducer' ,
                  'module'     : 'SusyGenVarsProducer()' ,
               },


## ------- MODULES: Trigger

  'PrefCorr2016' : { 
                 'isChain'    : False ,
                 'do4MC'      : True ,
                 'do4Data'    : False  ,
                 'import'     : 'LatinoAnalysis.NanoGardener.modules.PrefireCorr' ,
                 'declare'    : 'prefCorr2017 = lambda : PrefCorr(jetroot="L1prefiring_jetpt_2016BtoH.root", jetmapname="L1prefiring_jetpt_2016BtoH", photonroot="L1prefiring_photonpt_2016BtoH.root", photonmapname="L1prefiring_photonpt_2016BtoH", UseEMpT=0)',
                 'module'     : 'prefCorr2017()',
               },

  'PrefCorr2017' : { 
                 'isChain'    : False ,
                 'do4MC'      : True ,
                 'do4Data'    : False  ,
                 'import'     : 'LatinoAnalysis.NanoGardener.modules.PrefireCorr' ,
                 'declare'    : 'prefCorr2017 = lambda : PrefCorr(jetroot="L1prefiring_jetpt_2017BtoF.root", jetmapname="L1prefiring_jetpt_2017BtoF", photonroot="L1prefiring_photonpt_2017BtoF.root", photonmapname="L1prefiring_photonpt_2017BtoF", UseEMpT=0)',
                 'module'     : 'prefCorr2017()',
               },

  'trigData' : { 'isChain'    : False ,
                 'do4MC'      : False ,
                 'do4Data'    : True  ,
                 'import'     : 'LatinoAnalysis.NanoGardener.modules.TrigMaker' ,
                 'declare'    : 'trigData = lambda : TrigMaker("RPLME_CMSSW",isData=True,keepRunP=False)',
                 'module'     : 'trigData()',
               },

 
  'trigMC'   : { 'isChain'    : False ,
                 'do4MC'      : True  ,
                 'do4Data'    : False ,
                 'import'     : 'LatinoAnalysis.NanoGardener.modules.TrigMaker' ,
                 'declare'    : 'trigMC = lambda : TrigMaker("RPLME_CMSSW",isData=False,keepRunP=False)',
                 'module'     : 'trigMC()',
               },

 'TrigMC_hmumu'   : { 
                  'isChain'  : False ,
                  'do4MC'    : True  ,
                  'do4Data'  : False ,
                  'import'   : 'LatinoAnalysis.NanoGardener.modules.TrigMaker' ,
                  'declare'  : 'MHTrigMC = lambda : TrigMaker("RPLME_CMSSW",isData=False,keepRunP=True,cfg_path="LatinoAnalysis/NanoGardener/python/data/TrigMaker_hmumu_cfg.py")',
                  'module'   : 'MHTrigMC()',
               },

  'trigMCKeepRun' : { 'isChain'    : False ,
                 'do4MC'      : True  ,
                 'do4Data'    : False ,
                 'import'     : 'LatinoAnalysis.NanoGardener.modules.TrigMaker' ,
                 'declare'    : 'trigMCKR = lambda : TrigMaker("RPLME_CMSSW",isData=False,keepRunP=True)',
                 'module'     : 'trigMCKR()',
               },

## ------- MODULES: JEC

  'JECupdateMC2017': {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.jetRecalib' ,
                  'declare'    : 'jetRecalib2017MC = lambda : jetRecalib(globalTag="Fall17_17Nov2017_V32_MC", jetCollections=["CleanJet"], metCollections=["MET"])',
                  'module'     : 'jetRecalib2017MC()',
                 },    

  'JECupdateDATA2017': {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.jetRecalib' ,
                  'module'     : 'jetRecalib2017RPLME_RUN()', ### <--- TODO
                 },    

## ------- MODULES: MC Weights

  'baseW'    : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.Grafter' ,
                  'module'     : 'Grafter(["baseW/F=RPLME_baseW","Xsec/F=RPLME_XSection"])',
               },  

  'btagPerJet2016': {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'import'     : 'PhysicsTools.NanoAODTools.postprocessing.modules.btv.btagSFProducer' ,
                  'declare'    : 'btagSFProducer2016 = lambda : btagSFProducer(era="Legacy2016", algo="deepcsv")',
                  'module'     : 'btagSFProducer2016()',
                 },

  'btagPerJet2017': {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'import'     : 'PhysicsTools.NanoAODTools.postprocessing.modules.btv.btagSFProducer' ,
                  'declare'    : 'btagSFProducer2017 = lambda : btagSFProducer(era="2017", algo="deepcsv")',
                  'module'     : 'btagSFProducer2017()',
                 },               

  'btagPerJet2018': {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'import'     : 'PhysicsTools.NanoAODTools.postprocessing.modules.btv.btagSFProducer' ,
                  'declare'    : 'btagSFProducer2018 = lambda : btagSFProducer(era="2018", algo="deepcsv")',
                  'module'     : 'btagSFProducer2018()',
                 },

  'btagPerEvent': {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.BTagEventWeightProducer' ,
                  'declare'    : '',
                  'module'     : 'BTagEventWeightProducer()',
        
                },


  'LeptonSF' : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.LeptonSFMaker' ,
                  'declare'    : 'LeptonSF = lambda : LeptonSFMaker("RPLME_CMSSW")',
                  'module'     : 'LeptonSF()',
                },

## ------ Charge Flip

  'ChargeFlip' : {
                 'isChain'     : True ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'subTargets' : ['ChargeFlipDY','ChargeFlipWW','ChargeFlipTop'],
                  'onlySample' : ['DYJetsToLL_M-10to50-LO','DYJetsToLL_M-50','WWTo2L2Nu', 'GluGluToWWToENEN', 'GluGluToWWToENMN', 'GluGluToWWToENTN', 'GluGluToWWToMNEN', 'GluGluToWWToMNMN', 'GluGluToWWToMNTN', 'GluGluToWWToTNEN', 'GluGluToWWToTNMN', 'GluGluToWWToTNTN' , 'TTTo2L2Nu', 'ST_s-channel', 'ST_t-channel_antitop', 'ST_t-channel_top', 'ST_tW_antitop', 'ST_tW_top']
                 },

  'ChargeFlipDY' : {
                 'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.ChargeFlipWeight' ,
                  'declare'    : 'ChargeFlipDY = lambda : ChargeFlipWeight("RPLME_CMSSW","DY")',
                  'module'     : 'ChargeFlipDY()',
                  'onlySample' : ['DYJetsToLL_M-10to50-LO','DYJetsToLL_M-50'],
                 },

   'ChargeFlipWW' : {
                 'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.ChargeFlipWeight' ,
                  'declare'    : 'ChargeFlipWW = lambda : ChargeFlipWeight("RPLME_CMSSW","WW")',
                  'module'     : 'ChargeFlipWW()',
                  'onlySample' : ['WWTo2L2Nu', 'GluGluToWWToENEN', 'GluGluToWWToENMN', 'GluGluToWWToENTN', 'GluGluToWWToMNEN', 'GluGluToWWToMNMN', 'GluGluToWWToMNTN', 'GluGluToWWToTNEN', 'GluGluToWWToTNMN', 'GluGluToWWToTNTN' ]
                 },

   'ChargeFlipTop' : {
                 'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.ChargeFlipWeight' ,
                  'declare'    : 'ChargeFlipTop = lambda : ChargeFlipWeight("RPLME_CMSSW","Top")',
                  'module'     : 'ChargeFlipTop()',
                  'onlySample' : [ 'TTTo2L2Nu', 'ST_s-channel', 'ST_t-channel_antitop', 'ST_t-channel_top', 'ST_tW_antitop', 'ST_tW_top']
                    },

   'ChargeFlipClosure' : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.ChargeFlipWeight' ,
                  'declare'    : 'ChargeFlipClosusre = lambda : ChargeFlipWeight("RPLME_CMSSW","DY",False)',
                  'module'     : 'ChargeFlipClosusre()',
                  'onlySample' : ['DYJetsToLL_M-10to50-LO','DYJetsToLL_M-50'],
                 },

## ------- Pile-Up weights

  'puW'    : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : False ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.runDependentPuW' ,
                  'declare'    : 'puWeight = lambda : runDependentPuW("RPLME_CMSSW")',
                  'module'     : 'puWeight()', 
             } , 

  'puW2016': {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'import'     : 'PhysicsTools.NanoAODTools.postprocessing.modules.common.puWeightProducer' ,
                  'declare'    : 'pufile_mc2016="%s/src/PhysicsTools/NanoAODTools/python/postprocessing/data/pileup/pileup_profile_Summer16.root" % os.environ["CMSSW_BASE"]; pufile_data2016="%s/src/PhysicsTools/NanoAODTools/python/postprocessing/data/pileup/PileupData_GoldenJSON_Full2016.root" % os.environ["CMSSW_BASE"]',
                  'module'     : 'puWeightProducer(pufile_mc2016,pufile_data2016,"pu_mc","pileup",verbose=False)',

                },
              
  'puW2017': {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'import'     : 'PhysicsTools.NanoAODTools.postprocessing.modules.common.puWeightProducer' ,
                  'declare'    : 'pufile_data2017="%s/src/PhysicsTools/NanoAODTools/python/postprocessing/data/pileup/pileup_Cert_294927-306462_13TeV_PromptReco_Collisions17_withVar.root" % os.environ["CMSSW_BASE"]',
                  'module'     : 'puWeightProducer("auto",pufile_data2017,"pu_mc","pileup",verbose=False)',
  },

   'susyW': {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : False ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.SusyWeightsProducer' ,
                  'module'     : 'SusyWeightsProducer("RPLME_CMSSW")' ,
             },

## ------- MODULES: Embedding

  'EmbeddingWeights2017' : { 
                 'isChain'    : False ,
                 'do4MC'      : False ,
                 'do4Data'    : True  ,
                 'import'     : 'LatinoAnalysis.NanoGardener.modules.EmbeddedWeights' ,
                 'declare'    : 'embed = lambda : EmbedWeights(workspacefile="htt_scalefactors_2017_v1.root")',
                 'module'     : 'embed()',
               },

  'EmbeddingWeights2016' : { 
                 'isChain'    : False ,
                 'do4MC'      : False ,
                 'do4Data'    : True  ,
                 'import'     : 'LatinoAnalysis.NanoGardener.modules.EmbeddedWeights' ,
                 'declare'    : 'embed = lambda : EmbedWeights(workspacefile="htt_scalefactors_v16_12_embedded.root")',
                 'module'     : 'embed()',
               },

  'EmbeddingVeto' : { 
                 'isChain'    : False ,
                 'do4MC'      : True ,
                 'do4Data'    : False  ,
                 'import'     : 'LatinoAnalysis.NanoGardener.modules.EmbeddedVeto' ,
                 'declare'    : 'embedveto = lambda : EmbedVeto()',
                 'module'     : 'embedveto()',
               },

## ------- MODULES: Fakes

  'fakeWMC' : {
                  'isChain'    : True  ,
                  'do4MC'      : True  ,
                  'do4Data'    : False ,
                  'subTargets' : ['fakeWstep','formulasFAKE'],
                  'onlySample' : [ 'Zg', 'WZTo3LNu_mllmin01', 'Wg_MADGRAPHMLM', 'WZTo3LNu' ] , 
                   }, 

  'fakeWp2NB'  : {
                  'isChain'    : True ,
                  'do4MC'      : False ,
                  'do4Data'    : True ,
                  'subTargets' : ['fakeWstep','formulasFAKE'],
                   },
  'fakeWelewithiso'  : {
                  'isChain'    : True ,
                  'do4MC'      : False ,
                  'do4Data'    : True ,
                  'subTargets' : ['fakeWstep','formulasFAKE'],
                   },


    'fakeW'  : {
                  'isChain'    : True ,
                  'do4MC'      : False ,
                  'do4Data'    : True ,
                  'subTargets' : ['fakeWstep','formulasFAKE'],
                   },


  'fakeWPUFIXLP19'  : {
                  'isChain'    : True ,
                  'do4MC'      : False ,
                  'do4Data'    : True ,
                  'subTargets' : ['fakeWstep','formulasFAKE'],
                   },


  'fakeWstep'   : {
                  'isChain'    : False ,
                  'do4MC'      : True ,
                  'do4Data'    : True ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.LeptonFakeWMaker',
                  'declare'    : '',
                  'module'     : 'LeptonFakeWMaker("RPLME_CMSSW")',
              },

## ------- MODULES: Rochester corrections

  'rochesterMC'   : {
                  'isChain'    : False ,
                  'do4MC'      : True ,
                  'do4Data'    : False ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.rochester_corrections',
                  'declare'    : 'rochesterMC = lambda : rochester_corr(False,RPLME_YEAR)',
                  'module'     : 'rochesterMC()',
              },

  'rochesterDATA'   : {
                  'isChain'    : False ,
                  'do4MC'      : False ,
                  'do4Data'    : True ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.rochester_corrections',
                  'declare'    : 'rochesterDATA = lambda : rochester_corr(True,RPLME_YEAR)',
                  'module'     : 'rochesterDATA()',
              },

  'rochesterDATALP19'   : {
                  'isChain'    : False ,
                  'do4MC'      : False ,
                  'do4Data'    : True ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.rochester_corrections',
                  'declare'    : 'rochesterDATA = lambda : rochester_corr(True,RPLME_YEAR,"Lepton",[\'MET\',\'PuppiMET\',\'RawMET\',\'TkMET\'])',
                  'module'     : 'rochesterDATA()',
              },

  'rochesterMCLP19'   : {
                  'isChain'    : False ,
                  'do4MC'      : True ,
                  'do4Data'    : False ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.rochester_corrections',
                  'declare'    : 'rochesterMC = lambda : rochester_corr(False,RPLME_YEAR,"Lepton",[\'MET\',\'PuppiMET\',\'RawMET\',\'TkMET\'])',
                  'module'     : 'rochesterMC()',
              },


## ------- MODULES: Kinematic

  'l2Kin'    : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : True  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.l2KinProducer' ,
                  'declare'    : '',
                  'module'     : 'l2KinProducer()' ,
               },  

  'l3Kin'    : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : True  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.l3KinProducer' ,
                  'declare'    : '',
                  'module'     : 'l3KinProducer()' ,
               },  

  'l4Kin'    : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : True  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.l4KinProducer' ,
                  'declare'    : '',
                  'module'     : 'l4KinProducer()' ,
               },  

## ------- MODULES: Adding Formulas

# .... 2016/2017/... : switch in the code RPLME_YEAR

  'formulasMC' : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.GenericFormulaAdder' ,
                  'declare'    : '',
                  'module'     : 'GenericFormulaAdder(\'data/formulasToAdd_MC_RPLME_YEAR.py\')' ,
                 },

  'formulasMCLP19' : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.GenericFormulaAdder' ,
                  'declare'    : '',
                  'module'     : 'GenericFormulaAdder(\'data/formulasToAdd_MC_2017LP19.py\')' ,
                 },

  'formulasMCnoSF' : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.GenericFormulaAdder' ,
                  'declare'    : '',
                  'module'     : 'GenericFormulaAdder(\'data/formulasToAdd_MCnoSF_RPLME_YEAR.py\')' ,
                 },
   
  'formulasMC16tmp' : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.GenericFormulaAdder' ,
                  'declare'    : '',
                  'module'     : 'GenericFormulaAdder(\'data/formulasToAdd_MC_16tmp.py\')' ,
                 },

  'formulasMCMH' : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.GenericFormulaAdder' ,
                  'declare'    : '',
                  'module'     : 'GenericFormulaAdder(\'data/formulasToAdd_MC_MonoH.py\')' ,
                 },


  'formulasDATA' : {
                  'isChain'    : False ,
                  'do4MC'      : False ,
                  'do4Data'    : True   ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.GenericFormulaAdder' ,
                  'declare'    : '',
                  'module'     : 'GenericFormulaAdder(\'data/formulasToAdd_DATA_RPLME_YEAR.py\')' ,
                 },
  'formulasDATALP19' : {
                  'isChain'    : False ,
                  'do4MC'      : False ,
                  'do4Data'    : True   ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.GenericFormulaAdder' ,
                  'declare'    : '',
                  'module'     : 'GenericFormulaAdder(\'data/formulasToAdd_DATA_2017LP19.py\')' ,
                 },



  'formulasFAKE' : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : True  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.GenericFormulaAdder' ,
                  'declare'    : '',
                  'module'     : 'GenericFormulaAdder(\'data/formulasToAdd_FAKE_RPLME_YEAR.py\')' ,
                 },

  'formulasEMBED' : {
                  'isChain'    : False ,
                  'do4MC'      : False  ,
                  'do4Data'    : True  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.GenericFormulaAdder' ,
                  'declare'    : '',
                  'module'     : 'GenericFormulaAdder(\'data/formulasToAdd_EMBED_RPLME_YEAR.py\')' ,
                 },

## -------- DYMVA

  'DYMVA' : {
            #     'prebash'    : ['source /cvmfs/sft.cern.ch/lcg/views/LCG_92/x86_64-centos7-gcc62-opt/setup.sh'] ,
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : True  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.TMVAfiller' ,
                  'declare'    : 'DYMVA = lambda : TMVAfiller(\'data/DYMVA_RPLME_YEAR_cfg.py\')' ,
                  'module'     : 'DYMVA()',
            } ,


# ------------------------------------ SYSTEMATICS ----------------------------------------------------------------

## ------- JES

  'JESBaseTestV8' : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.JECMaker' ,
                  'declare'    : 'JES = lambda : JECMaker(globalTag="Fall17_17Nov2017_V8_MC", types=["Total"], jetFlav="AK4PFchs")',
                  'module'     : 'JES()',
                  'onlySample' : [ 'WWTo2L2Nu' ] ,
               },

  'JESBase' : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.JECMaker' ,
                  'declare'    : 'JES = lambda : JECMaker(globalTag="RPLME_JESGT", types=["Total"], jetFlav="AK4PFchs")',
                  'module'     : 'JES()',
               },

  'do_JESup' : {  
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.PtCorrApplier', 
                  'declare'    : 'JESUp = lambda : PtCorrApplier(Coll="CleanJet", CorrSrc="jecUncertTotal", kind="Up", doMET=True, METobjects = ["MET","PuppiMET","RawMET"])', 
                  'module'     : 'JESUp()' 
               },

  'do_JESdo' : {  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.PtCorrApplier', 
                  'declare'    : 'JESDo = lambda : PtCorrApplier(Coll="CleanJet", CorrSrc="jecUncertTotal", kind="Do", doMET=True, METobjects = ["MET","PuppiMET","RawMET"])', 
                  'module'     : 'JESDo()' 
               },

   # What about B-Tag weights ? They are done on top of the Jet Collection, not the CleanJet, so they don't catch th jet pT update !!!!

   'JESup' :   {  
                  'isChain'    : True ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'subTargets' : ['JESBase','do_JESup','l2Kin', 'l3Kin', 'l4Kin','formulasMC'],
               },

   'JESdo' :   {
                  'isChain'    : True ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'subTargets' : ['JESBase','do_JESdo','l2Kin', 'l3Kin', 'l4Kin','formulasMC'],
               },


   'JESupLP19' :   {
                  'isChain'    : True ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'subTargets' : ['JESBase','do_JESup','l2Kin', 'l3Kin', 'l4Kin','formulasMCLP19'],
               },

   'JESdoLP19' :   {
                  'isChain'    : True ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'subTargets' : ['JESBase','do_JESdo','l2Kin', 'l3Kin', 'l4Kin','formulasMCLP19'],
               },


## ------- MET

  'do_METup' : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.MetUnclustered',
                  'declare'    : 'METup = lambda : MetUnclusteredTreeMaker(kind="Up",metCollections=["MET", "PuppiMET", "RawMET"])',
                  'module'     : 'METup()',
                },

  'do_METdo' : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.MetUnclustered',
                  'declare'    : 'METDo = lambda : MetUnclusteredTreeMaker(kind="Dn",metCollections=["MET", "PuppiMET", "RawMET"])',
                  'module'     : 'METDo()',
                },

   'METup' :   {
                  'isChain'    : True ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'subTargets' : ['do_METup','l2Kin', 'l3Kin', 'l4Kin','formulasMC'],
               },

   'METdo' :   {
                  'isChain'    : True ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'subTargets' : ['do_METdo','l2Kin', 'l3Kin', 'l4Kin','formulasMC'],
               },

   'METupLP19' :   {
                  'isChain'    : True ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'subTargets' : ['do_METup','l2Kin', 'l3Kin', 'l4Kin','formulasMCLP19'],
               },

   'METdoLP19' :   {
                  'isChain'    : True ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'subTargets' : ['do_METdo','l2Kin', 'l3Kin', 'l4Kin','formulasMCLP19'],
               },

## ------- e-Scale

  'do_ElepTup' : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.LepPtScaleUncertainty',
                  'declare'    : 'ElepTup = lambda : LeppTScalerTreeMaker(kind="Up", lepFlavor="ele", version="RPLME_CMSSW" , metCollections = ["MET", "PuppiMET", "RawMET", "TkMET"])',
                  'module'     : 'ElepTup()',
                },

  'do_ElepTdo' : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.LepPtScaleUncertainty',
                  'declare'    : 'ElepTup = lambda : LeppTScalerTreeMaker(kind="Dn", lepFlavor="ele", version="RPLME_CMSSW" , metCollections = ["MET", "PuppiMET", "RawMET", "TkMET"])',
                  'module'     : 'ElepTup()',
                },

  'ElepTup' :   {
                  'isChain'    : True ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'subTargets' : ['do_ElepTup','trigMCKeepRun','LeptonSF','l2Kin', 'l3Kin', 'l4Kin','formulasMC'],
               },

  'ElepTdo' :   {
                  'isChain'    : True ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'subTargets' : ['do_ElepTdo','trigMCKeepRun','LeptonSF','l2Kin', 'l3Kin', 'l4Kin','formulasMC'],
               },

  'ElepTupLP19' :   {
                  'isChain'    : True ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'subTargets' : ['do_ElepTup','trigMCKeepRun','LeptonSF','l2Kin', 'l3Kin', 'l4Kin','formulasMCLP19'],
               },

  'ElepTdoLP19' :   {
                  'isChain'    : True ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'subTargets' : ['do_ElepTdo','trigMCKeepRun','LeptonSF','l2Kin', 'l3Kin', 'l4Kin','formulasMCLP19'],
               },

  'EmbElepTup' :   {
                  'isChain'    : True ,
                  'do4MC'      : False  ,
                  'do4Data'    : True  ,
                  'subTargets' : ['do_ElepTup','trigMCKeepRun','LeptonSF','l2Kin', 'l3Kin', 'l4Kin','formulasEMBED'],
               },

  'EmbElepTdo' :   {
                  'isChain'    : True ,
                  'do4MC'      : False  ,
                  'do4Data'    : True  ,
                  'subTargets' : ['do_ElepTdo','trigMCKeepRun','LeptonSF','l2Kin', 'l3Kin', 'l4Kin','formulasEMBED'],
               },

## ------- mu-Scale

  'do_MupTup' : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.LepPtScaleUncertainty',
                  'declare'    : 'MupTup = lambda : LeppTScalerTreeMaker(kind="Up", lepFlavor="mu", version="RPLME_CMSSW" , metCollections = ["MET", "PuppiMET", "RawMET", "TkMET"])',
                  'module'     : 'MupTup()',
                },

  'do_MupTdo' : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.LepPtScaleUncertainty',
                  'declare'    : 'MupTup = lambda : LeppTScalerTreeMaker(kind="Dn", lepFlavor="mu", version="RPLME_CMSSW" , metCollections = ["MET", "PuppiMET", "RawMET", "TkMET"])',
                  'module'     : 'MupTup()',
                },

  'MupTup' :   {
                  'isChain'    : True ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'subTargets' : ['do_MupTup','trigMCKeepRun','LeptonSF','l2Kin', 'l3Kin', 'l4Kin','formulasMC'],
               },

  'MupTdo' :   {
                  'isChain'    : True ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'subTargets' : ['do_MupTdo','trigMCKeepRun','LeptonSF','l2Kin', 'l3Kin', 'l4Kin','formulasMC'],
               },

  'MupTupLP19' :   {
                  'isChain'    : True ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'subTargets' : ['do_MupTup','trigMCKeepRun','LeptonSF','l2Kin', 'l3Kin', 'l4Kin','formulasMCLP19'],
               },

  'MupTdoLP19' :   {
                  'isChain'    : True ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'subTargets' : ['do_MupTdo','trigMCKeepRun','LeptonSF','l2Kin', 'l3Kin', 'l4Kin','formulasMCLP19'],
               },


  'EmbMupTup' :   {
                  'isChain'    : True ,
                  'do4MC'      : False  ,
                  'do4Data'    : True  ,
                  'subTargets' : ['do_MupTup','trigMCKeepRun','LeptonSF','l2Kin', 'l3Kin', 'l4Kin','formulasEMBED'],
               },

  'EmbMupTdo' :   {
                  'isChain'    : True ,
                  'do4MC'      : False  ,
                  'do4Data'    : True  ,
                  'subTargets' : ['do_MupTdo','trigMCKeepRun','LeptonSF','l2Kin', 'l3Kin', 'l4Kin','formulasEMBED'],
               },

# ------------------------------------ SKIMS : CUTS ONLY ----------------------------------------------------------

  'TrgwSel'   : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'selection'  : '"((TriggerEffWeight_2l_u/TriggerEffWeight_2l)>10)"' ,
                  #'onlySample' : [ 'WWTo2L2Nu' ] ,
                 },

  'wwSel'     : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : True  ,
                  'selection'  : '"(mll>12 && ptll>30 && (MET_pt > 20 || PuppiMET_pt>20) && Alt$(Lepton_pt[0],0.)>20 && Alt$(Lepton_pt[1],0.)>10 && Alt$(Lepton_pt[2],0.)<10 && Alt$(Lepton_pdgId[0]*Lepton_pdgId[1],0)==-11*13)"',
                  #'onlySample' : [ 'WWTo2L2Nu' ] ,
                 },

## ------- Fake Study:

  'fakeSel'    : {
                  'isChain'    : False ,
                  'do4MC'      : False  ,
                  'do4Data'    : True  ,
                  'selection'  : '"((MET_pt < 20 || PuppiMET_pt < 20) && mtw1 < 20)"' ,
                 },


  'fakeSelKinMC'  : {
                  'isChain'    : True ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  , 
                  'selection'  : '"(MET_pt < 20 || PuppiMET_pt < 20)"' , 
                  'onlySample' : [
                                  #### DY
                                  'DYJetsToLL_M-10to50','DYJetsToLL_M-50','DYJetsToLL_M-10to50ext3','DYJetsToLL_M-50-LO','DYJetsToLL_M-50-LO-ext1','DYJetsToLL_M-10to50-LO',
                                  'DYJetsToTT_MuEle_M-50','DYJetsToLL_M-50_ext2','DYJetsToLL_M-10to50-LO-ext1',
                                   # ... Low Mass HT
                                  'DYJetsToLL_M-4to50_HT-100to200',
                                  'DYJetsToLL_M-4to50_HT-100to200-ext1',
                                  'DYJetsToLL_M-4to50_HT-200to400',
                                  'DYJetsToLL_M-4to50_HT-200to400-ext1',
                                  'DYJetsToLL_M-4to50_HT-400to600',
                                  'DYJetsToLL_M-4to50_HT-400to600-ext1',
                                  'DYJetsToLL_M-4to50_HT-600toInf',
                                  'DYJetsToLL_M-4to50_HT-600toInf-ext1',
                                   # ... high Mass HT
                                  'DYJetsToLL_M-50_HT-100to200',
                                  'DYJetsToLL_M-50_HT-200to400',
                                  'DYJetsToLL_M-50_HT-400to600',
                                  'DYJetsToLL_M-50_HT-600to800',
                                  'DYJetsToLL_M-50_HT-800to1200',
                                  'DYJetsToLL_M-50_HT-1200to2500',
                                  'DYJetsToLL_M-50_HT-2500toInf',
 
                                  ####
                                  'WJetsToLNu-LO',
                                  'WJetsToLNu','WJetsToLNu_HT100_200','WJetsToLNu_HT200_400','WJetsToLNu_HT400_600','WJetsToLNu_HT600_800',
                                  'WJetsToLNu_HT800_1200','WJetsToLNu_HT1200_2500','WJetsToLNu_HT2500_inf',
                                  ####
                                  'QCD_Pt-15to20_EMEnriched', 'QCD_Pt-20to30_EMEnriched', 'QCD_Pt-30to50_EMEnriched', 'QCD_Pt-50to80_EMEnriched','QCD_Pt-50to80_EMEnriched_ext1',
                                  'QCD_Pt-20toInf_MuEnrichedPt15','QCD_Pt-30toInf_DoubleEMEnriched','QCD_Pt-15to20_MuEnrichedPt5',
                                  ####
                                  'QCD_Pt_15to20_bcToE','QCD_Pt_20to30_bcToE','QCD_Pt_30to80_bcToE','QCD_Pt_80to170_bcToE',
                                  'QCD_Pt_170to250_bcToE','QCD_Pt_250toInf_bcToE',
                                  ####
                                  'TT','TTJets','TTTo2L2Nu',
                                 ] ,               
                    'subTargets' : ['baseW','rochesterMC','trigMC','puW','l2Kin', 'l3Kin', 'l4Kin','formulasMCnoSF'] ,
                 },



  'fakeSelMC'  : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  , 
                  'selection'  : '"((MET_pt < 20 || PuppiMET_pt < 20) && mtw1 < 20)"' , 
                  'onlySample' : [
                                  #### DY
                                  'DYJetsToLL_M-10to50','DYJetsToLL_M-50','DYJetsToLL_M-10to50ext3','DYJetsToLL_M-50-LO','DYJetsToLL_M-50-LO-ext1','DYJetsToLL_M-10to50-LO',
                                  'DYJetsToTT_MuEle_M-50','DYJetsToLL_M-50_ext2','DYJetsToLL_M-10to50-LO-ext1',
                                   # ... Low Mass HT
                                  'DYJetsToLL_M-4to50_HT-100to200',
                                  'DYJetsToLL_M-4to50_HT-100to200-ext1',
                                  'DYJetsToLL_M-4to50_HT-200to400',
                                  'DYJetsToLL_M-4to50_HT-200to400-ext1',
                                  'DYJetsToLL_M-4to50_HT-400to600',
                                  'DYJetsToLL_M-4to50_HT-400to600-ext1',
                                  'DYJetsToLL_M-4to50_HT-600toInf',
                                  'DYJetsToLL_M-4to50_HT-600toInf-ext1',
                                   # ... high Mass HT
                                  'DYJetsToLL_M-50_HT-100to200',
                                  'DYJetsToLL_M-50_HT-200to400',
                                  'DYJetsToLL_M-50_HT-400to600',
                                  'DYJetsToLL_M-50_HT-600to800',
                                  'DYJetsToLL_M-50_HT-800to1200',
                                  'DYJetsToLL_M-50_HT-1200to2500',
                                  'DYJetsToLL_M-50_HT-2500toInf',
 
                                  ####
                                  'WJetsToLNu','WJetsToLNu_HT100_200','WJetsToLNu_HT200_400','WJetsToLNu_HT400_600','WJetsToLNu_HT600_800',
                                  'WJetsToLNu_HT800_1200','WJetsToLNu_HT1200_2500','WJetsToLNu_HT2500_inf',
                                  ####
                                  'QCD_Pt-15to20_EMEnriched', 'QCD_Pt-20to30_EMEnriched', 'QCD_Pt-30to50_EMEnriched', 'QCD_Pt-50to80_EMEnriched','QCD_Pt-50to80_EMEnriched_ext1',
                                  'QCD_Pt-20toInf_MuEnrichedPt15','QCD_Pt-30toInf_DoubleEMEnriched','QCD_Pt-15to20_MuEnrichedPt5',
                                  ####
                                  'QCD_Pt_15to20_bcToE','QCD_Pt_20to30_bcToE','QCD_Pt_30to80_bcToE','QCD_Pt_80to170_bcToE',
                                  'QCD_Pt_170to250_bcToE','QCD_Pt_250toInf_bcToE',
                                  ####
                                  'GJetsDR04_HT100To200', 'GJetsDR04_HT200To400', 'GJetsDR04_HT400To600', 'GJetsDR04_HT600ToInf', 'GJets_HT40To100', 'GJets_HT40To100-ext1',
                                  ####
                                  'TT','TTJets','TTTo2L2Nu',
                                  ###
                                  'GJetsDR04_HT40To100', 'GJetsDR04_HT100To200', 'GJetsDR04_HT200To400', 'GJetsDR04_HT400To600', 'GJetsDR04_HT600ToInf',
                                  'GJets_HT40To100-ext1',
                                 ] ,               
                 },

## ------- 2-Leptons: Loose / tightOR

#  'l2loose'   : {
#                  'isChain'    : False ,
#                  'do4MC'      : True  ,
#                  'do4Data'    : True  , 
#                  'selection'  : '"(nLepton>=2)"' , 
#                 },

# Run MVA after 2 lepton selection !
   'l2loose' :  {
                  'isChain'    : True  ,
                  'do4MC'      : True  ,
                  'do4Data'    : True  ,
                  'selection'  : '"(nLepton>=2)"' ,
                  'subTargets' : ['DYMVA','MonoHiggsMVA']
                },
 

#muWP='cut_Tight80x'
#eleWPlist = ['cut_WP_Tight80X','cut_WP_Tight80X_SS','mva_90p_Iso2016','mva_90p_Iso2016_SS']

  'l2tightOR2016' : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : True  ,
                  'selection'  : '" (nLepton>=2 && Lepton_pt[0]>18 && Lepton_pt[1]>8 ) \
                                    && (    Lepton_isTightElectron_cut_WP_Tight80X[0] > 0.5        \
                                         || Lepton_isTightElectron_cut_WP_Tight80X_SS[0] > 0.5     \
                                         || Lepton_isTightElectron_mva_90p_Iso2016[0] > 0.5        \
                                         || Lepton_isTightElectron_mva_90p_Iso2016_SS[0] > 0.5     \
                                         || Lepton_isTightMuon_cut_Tight80x[0] > 0.5             ) \
                                    && (    Lepton_isTightElectron_cut_WP_Tight80X[1] > 0.5        \
                                         || Lepton_isTightElectron_cut_WP_Tight80X_SS[1] > 0.5     \
                                         || Lepton_isTightElectron_mva_90p_Iso2016[1] > 0.5        \
                                         || Lepton_isTightElectron_mva_90p_Iso2016_SS[1] > 0.5     \
                                         || Lepton_isTightMuon_cut_Tight80x[1] > 0.5             ) \
                                  "' ,
                 },

  'l2tightOR2016v5' : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : True  ,
                  'selection'  : '" (nLepton>=2 && Lepton_pt[0]>18 && Lepton_pt[1]>8 ) \
                                    && (    Lepton_isTightElectron_cut_WP_Tight80X[0] > 0.5        \
                                         || Lepton_isTightElectron_cut_WP_Tight80X_SS[0] > 0.5     \
                                         || Lepton_isTightElectron_mva_90p_Iso2016[0] > 0.5        \
                                         || Lepton_isTightElectron_mva_90p_Iso2016_SS[0] > 0.5     \
                                         || Lepton_isTightMuon_cut_Tight80x[0] > 0.5             ) \
                                    && (    Lepton_isTightElectron_cut_WP_Tight80X[1] > 0.5        \
                                         || Lepton_isTightElectron_cut_WP_Tight80X_SS[1] > 0.5     \
                                         || Lepton_isTightElectron_mva_90p_Iso2016[1] > 0.5        \
                                         || Lepton_isTightElectron_mva_90p_Iso2016_SS[1] > 0.5     \
                                         || Lepton_isTightMuon_cut_Tight80x[1] > 0.5             ) \
                                  "' ,
                 },

  'l2tightOR2017' : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : True  ,
                  'selection'  : '" (nLepton>=2 && Lepton_pt[0]>18 && Lepton_pt[1]>8 ) \
                                    && (    Lepton_isTightElectron_mvaFall17Iso_WP90[0] > 0.5        \
                                         || Lepton_isTightElectron_mvaFall17Iso_WP90_SS[0] > 0.5     \
                                         || Lepton_isTightMuon_cut_Tight_HWWW[0] > 0.5             ) \
                                    && (    Lepton_isTightElectron_mvaFall17Iso_WP90[1] > 0.5        \
                                         || Lepton_isTightElectron_mvaFall17Iso_WP90_SS[1] > 0.5     \
                                         || Lepton_isTightMuon_cut_Tight_HWWW[1] > 0.5             ) \
                                  "' , 
                 },

  'l2tightOR2017v4' : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : True  ,
                  'selection'  : '" (nLepton>=2 && Lepton_pt[0]>18 && Lepton_pt[1]>8 ) \
                                    && (    Lepton_isTightElectron_mvaFall17V1Iso_WP90[0] > 0.5        \
                                         || Lepton_isTightElectron_mvaFall17V2Iso_WP90[0] > 0.5        \
                                         || Lepton_isTightElectron_mvaFall17V1Iso_WP90_SS[0] > 0.5     \
                                         || Lepton_isTightElectron_mvaFall17V2Iso_WP90_SS[0] > 0.5     \
                                         || Lepton_isTightMuon_cut_Tight_HWWW[0] > 0.5             ) \
                                    && (    Lepton_isTightElectron_mvaFall17V1Iso_WP90[1] > 0.5        \
                                         || Lepton_isTightElectron_mvaFall17V2Iso_WP90[0] > 0.5        \
                                         || Lepton_isTightElectron_mvaFall17V1Iso_WP90_SS[1] > 0.5     \
                                         || Lepton_isTightElectron_mvaFall17V2Iso_WP90_SS[1] > 0.5     \
                                         || Lepton_isTightMuon_cut_Tight_HWWW[1] > 0.5             ) \
                                  "' ,
                 },

  'l2tightOR2017v5' : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : True  ,
                  'selection'  : '" (nLepton>=2 && Lepton_pt[0]>18 && Lepton_pt[1]>8 ) \
                                    && (    Lepton_isTightElectron_mvaFall17V1Iso_WP90[0] > 0.5        \
                                         || Lepton_isTightElectron_mvaFall17V2Iso_WP90[0] > 0.5        \
                                         || Lepton_isTightElectron_mvaFall17V1Iso_WP90_SS[0] > 0.5     \
                                         || Lepton_isTightElectron_mvaFall17V2Iso_WP90_SS[0] > 0.5     \
                                         || Lepton_isTightMuon_cut_Tight_HWWW[0] > 0.5             ) \
                                    && (    Lepton_isTightElectron_mvaFall17V1Iso_WP90[1] > 0.5        \
                                         || Lepton_isTightElectron_mvaFall17V2Iso_WP90[0] > 0.5        \
                                         || Lepton_isTightElectron_mvaFall17V1Iso_WP90_SS[1] > 0.5     \
                                         || Lepton_isTightElectron_mvaFall17V2Iso_WP90_SS[1] > 0.5     \
                                         || Lepton_isTightMuon_cut_Tight_HWWW[1] > 0.5             ) \
                                  "' ,
                 },


  'l2tightOR2018' : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : True  ,
                  'selection'  : '" (nLepton>=2 && Lepton_pt[0]>18 && Lepton_pt[1]>8 ) \
                                    && (    Lepton_isTightElectron_mvaFall17Iso_WP90[0] > 0.5        \
                                         || Lepton_isTightElectron_mvaFall17Iso_WP90_SS[0] > 0.5     \
                                         || Lepton_isTightMuon_cut_Tight_HWWW[0] > 0.5             ) \
                                    && (    Lepton_isTightElectron_mvaFall17Iso_WP90[1] > 0.5        \
                                         || Lepton_isTightElectron_mvaFall17Iso_WP90_SS[1] > 0.5     \
                                         || Lepton_isTightMuon_cut_Tight_HWWW[1] > 0.5             ) \
                                  "' ,
                 },

  'l2tightOR2018v4' : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : True  ,
                  'selection'  : '" (nLepton>=2 && Lepton_pt[0]>18 && Lepton_pt[1]>8 ) \
                                    && (    Lepton_isTightElectron_mvaFall17V1Iso_WP90[0] > 0.5        \
                                         || Lepton_isTightElectron_mvaFall17V2Iso_WP90[0] > 0.5        \
                                         || Lepton_isTightElectron_mvaFall17V1Iso_WP90_SS[0] > 0.5     \
                                         || Lepton_isTightElectron_mvaFall17V2Iso_WP90_SS[0] > 0.5     \
                                         || Lepton_isTightMuon_cut_Tight_HWWW[0] > 0.5             ) \
                                    && (    Lepton_isTightElectron_mvaFall17V1Iso_WP90[1] > 0.5        \
                                         || Lepton_isTightElectron_mvaFall17V2Iso_WP90[0] > 0.5        \
                                         || Lepton_isTightElectron_mvaFall17V1Iso_WP90_SS[1] > 0.5     \
                                         || Lepton_isTightElectron_mvaFall17V2Iso_WP90_SS[1] > 0.5     \
                                         || Lepton_isTightMuon_cut_Tight_HWWW[1] > 0.5             ) \
                                  "' ,
                 },

  'l2tightOR2018v5' : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : True  ,
                  'selection'  : '" (nLepton>=2 && Lepton_pt[0]>18 && Lepton_pt[1]>8 ) \
                                    && (    Lepton_isTightElectron_mvaFall17V1Iso_WP90[0] > 0.5        \
                                         || Lepton_isTightElectron_mvaFall17V2Iso_WP90[0] > 0.5        \
                                         || Lepton_isTightElectron_mvaFall17V1Iso_WP90_SS[0] > 0.5     \
                                         || Lepton_isTightElectron_mvaFall17V2Iso_WP90_SS[0] > 0.5     \
                                         || Lepton_isTightMuon_cut_Tight_HWWW[0] > 0.5             ) \
                                    && (    Lepton_isTightElectron_mvaFall17V1Iso_WP90[1] > 0.5        \
                                         || Lepton_isTightElectron_mvaFall17V2Iso_WP90[0] > 0.5        \
                                         || Lepton_isTightElectron_mvaFall17V1Iso_WP90_SS[1] > 0.5     \
                                         || Lepton_isTightElectron_mvaFall17V2Iso_WP90_SS[1] > 0.5     \
                                         || Lepton_isTightMuon_cut_Tight_HWWW[1] > 0.5             ) \
                                  "' ,
                 },


## ------- Analysis Skims:

  'trainDYMVA'   : {
                 'isChain'    : False ,
                 'do4MC'      : True  ,
                 'do4Data'    : True  ,
                 'selection'  : '"(mll>12 && Lepton_pt[0]>20 && Lepton_pt[1]>10 && (nLepton>=2 && Alt$(Lepton_pt[2],0)<10) \
                                   && abs(Lepton_eta[0])<2.5 && abs(Lepton_eta[1])<2.5 && LepCut2l==1 \
                                   && ptll>30 && PuppiMET_pt > 20 && fabs(91.1876 - mll) > 15 \
                                   && ((Lepton_pdgId[0]*Lepton_pdgId[1] == -11*11) || (Lepton_pdgId[0]*Lepton_pdgId[1] == -13*13)))"' ,
                 'onlySample' : [
                                 #### DY
                                 'DYJetsToLL_M-10to50-LO',
                                 'DYJetsToLL_M-50-LO-ext1',
                                 #### Higgs
                                 'GluGluHToWWTo2L2NuPowheg_M125_private','VBFHToWWTo2L2NuPowheg_M125_private',
                                ] ,
                 },

# ------------------------------------ SPECIAL STEPS: HADD & UEPS -------------------------------------------------

## ------- HADD 

  'hadd'     : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : True  ,
                  'SizeMax'    : 5e9 ,
                 #'bigSamples' : ['DYJetsToLL_M-50','DY2JetsToLL','ZZTo2L2Q','DYJetsToLL_M-50-LO',
                 #                'DYJetsToLL_M-50-LO-ext1',
                 #                'WZTo2L2Q','TTToSemiLepton','TTToSemiLeptonic','TTTo2L2Nu_ext1','TTJetsDiLep-LO-ext1','TTTo2L2Nu',
                 #                'DYJetsToEE_Pow',
                 #                'DY1JetsToLL',
                 #                #'TTJets',
                 #               ],
               },

## ------- UEPS 

  'UEPS'     : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'onlySample' : [
                                    'GluGluHToWWTo2L2NuPowheg_M125_CP5Up', 'VBFHToWWTo2L2NuPowheg_M125_CP5Up', 'WWTo2L2Nu_CP5Up',
                                    'GluGluHToWWTo2L2NuPowheg_M125_CP5Down', 'VBFHToWWTo2L2NuPowheg_M125_CP5Down', 'WWTo2L2Nu_CP5Down',
                                    'GluGluHToWWTo2L2Nu_M125_CUETDown' , 'VBFHToWWTo2L2Nu_M125_CUETDown' , 'WWTo2L2Nu_CUETDown' ,
                                    'GluGluHToWWTo2L2Nu_M125_CUETUp'   , 'VBFHToWWTo2L2Nu_M125_CUETUp'   , 'WWTo2L2Nu_CUETUp'   ,
                                    'GluGluHToWWTo2L2NuHerwigPS_M125'  , 'VBFHToWWTo2L2NuHerwigPS_M125'  , 'WWTo2L2NuHerwigPS'  ,
                                    'GluGluHToWWTo2L2Nu_M125_herwigpp' , 'VBFHToWWTo2L2Nu_M125_herwigpp',
                                 ] ,
                  'cpMap' : {
                              'UEdo' : {
                                          'GluGluHToWWTo2L2NuPowheg_M125_CP5Down' : ['GluGluHToWWTo2L2NuPowheg_M125_PrivateNano' ,'GluGluHToWWTo2L2NuPowheg_M125'],
                                          'VBFHToWWTo2L2NuPowheg_M125_CP5Down'    : ['VBFHToWWTo2L2NuPowheg_M125_PrivateNano','VBFHToWWTo2L2NuPowheg_M125']    ,
                                          'WWTo2L2Nu_CP5Down'               : ['WWTo2L2Nu_PrivateNano', 'WWTo2L2Nu'] ,
                                          'GluGluHToWWTo2L2Nu_M125_CUETDown' : ['GluGluHToWWTo2L2Nu_M125' ,'GluGluHToWWTo2L2NuPowheg_M125'],
                                          'VBFHToWWTo2L2Nu_M125_CUETDown'    : ['VBFHToWWTo2L2Nu_M125', 'VBFHToWWTo2L2NuPowheg_M125', 'VBFHToWWTo2L2Nu_alternative_M125']    ,
                                          'WWTo2L2Nu_CUETDown'               : ['WWTo2L2Nu'] , 
                                       },
                              'UEup' : {
                                          'GluGluHToWWTo2L2NuPowheg_M125_CP5Up' : ['GluGluHToWWTo2L2NuPowheg_M125_PrivateNano' ,'GluGluHToWWTo2L2NuPowheg_M125'],
                                          'VBFHToWWTo2L2NuPowheg_M125_CP5Up'    : ['VBFHToWWTo2L2NuPowheg_M125_PrivateNano','VBFHToWWTo2L2NuPowheg_M125']    ,
                                          'WWTo2L2Nu_CP5Up'               : ['WWTo2L2Nu_PrivateNano', 'WWTo2L2Nu'] ,
                                          'GluGluHToWWTo2L2Nu_M125_CUETUp'   : ['GluGluHToWWTo2L2Nu_M125' ,'GluGluHToWWTo2L2NuPowheg_M125'],
                                          'VBFHToWWTo2L2Nu_M125_CUETUp'      : ['VBFHToWWTo2L2Nu_M125', 'VBFHToWWTo2L2NuPowheg_M125', 'VBFHToWWTo2L2Nu_alternative_M125']    ,
                                          'WWTo2L2Nu_CUETUp'                 : ['WWTo2L2Nu'] ,
                                       },
                              'PS'   : {
                                          'GluGluHToWWTo2L2NuHerwigPS_M125'  : ['GluGluHToWWTo2L2Nu_M125' ,'GluGluHToWWTo2L2NuPowheg_M125'],
                                          'GluGluHToWWTo2L2Nu_M125_herwigpp' : ['GluGluHToWWTo2L2Nu_M125' ,'GluGluHToWWTo2L2NuPowheg_M125'], 
                                          'VBFHToWWTo2L2NuHerwigPS_M125'     : ['VBFHToWWTo2L2Nu_M125', 'VBFHToWWTo2L2NuPowheg_M125', 'VBFHToWWTo2L2Nu_alternative_M125'] ,
                                          'VBFHToWWTo2L2Nu_M125_herwigpp'    : ['VBFHToWWTo2L2Nu_M125', 'VBFHToWWTo2L2NuPowheg_M125', 'VBFHToWWTo2L2Nu_alternative_M125'] ,
                                          'WWTo2L2NuHerwigPS'                : ['WWTo2L2Nu'] ,
                                       },
                            },
               },

}


