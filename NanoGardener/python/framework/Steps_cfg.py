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

  # FIXME: check btagPerJet2016, btagPerEvent
  # FIXME: Cfg 'trigMC','LeptonSF','puW'
  'MCCorr2016' : {
                     'isChain'    : True  ,
                     'do4MC'      : True  ,
                     'do4Data'    : False ,
                     'subTargets' : ['baseW','PrefCorr2016','btagPerJet2016', 
                                     'rochesterMC','trigMC','LeptonSF','puW','l2Kin', 'l3Kin', 'l4Kin','formulasMC'],
                },

  'MCCorr2016tmp'  : {
                     'isChain'    : True  ,
                     'do4MC'      : True  ,
                     'do4Data'    : False ,
                     'subTargets' : ['baseW','PrefCorr2016','puW','rochesterMC','l2Kin','formulasMC16tmp'],
                     'onlySample' : ['DYJetsToLL_M-50_ext2'],
                 },

  'MCl1loose2017v2': {
                  'isChain'    : True  ,
                  'do4MC'      : True  ,
                  'do4Data'    : False ,
                  'selection'  : '"((nElectron+nMuon)>0)"' ,
                  'subTargets' : ['leptonMaker','lepSel', 'puW2017', 'l2Kin', 'l3Kin', 'l4Kin', 'btagPerJet2017', 'btagPerEvent','PrefCorr2017'],
                },

  'MCCorr2017' : {
                 'isChain'    : True  ,
                  'do4MC'      : True  ,
                  'do4Data'    : False ,
                  'subTargets' : ['baseW','PrefCorr2017','jetSel','CleanJetCut', 'btagPerJet2017', 'btagPerEvent' ,
                                  'PromptParticlesGenVars','GenVar','GenLeptonMatch', 'HiggsGenVars', 'TopGenVars', 'wwNLL',
                                  'ggHTheoryUncertainty', 'DressedLeptons', 'WGammaStar',
                                  'rochesterMC','trigMC','LeptonSF','puW','l2Kin', 'l3Kin', 'l4Kin','formulasMC'],
                    },


  'MCl1loose2018' :  {
                  'isChain'    : True  ,
                  'do4MC'      : True  ,
                  'do4Data'    : False ,
                  'selection'  : '"((nElectron+nMuon)>0)"' ,
                  'subTargets' : ['leptonMaker','lepSel','jetSel','CleanJetCut',
                                  'PromptParticlesGenVars','GenVar','GenLeptonMatch', 'HiggsGenVars', 'TopGenVars', 'wwNLL','WGammaStar', 'ggHTheoryUncertainty', 'DressedLeptons'],
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
                                   'DYJetsToLL_M-10to50','DYJetsToLL_M-50','DYJetsToLL_M-10to50ext3',
                                   'DYJetsToLL_M-5to50-LO','DYJetsToLL_M-50-LO-ext1',
                                   'WZTo2L2Q','WZTo3LNu_mllmin01_ext1','WZTo3LNu',
                                 ]
                   },

  'MCWgStarCorr2017' : {
                     'isChain'    : True  ,
                     'do4MC'      : True  ,
                     'do4Data'    : False ,
                     'subTargets' : ['baseW','PrefCorr2017','jetSel','CleanJetCut','btagPerJet2017', 'btagPerEvent',
                                     'rochesterMC','trigMC','LeptonSF','puW','l2Kin', 'l3Kin', 'l4Kin','formulasMC'],
                    },

## ------- DATA:
    
  'DATAl1loose2016': {
                  'isChain'    : True  ,
                  'do4MC'      : False ,
                  'do4Data'    : True  ,
                  'selection'  : '"(nElectron>0 && Electron_pt[0]>10) || (nMuon>0 && Muon_pt[0]>10)"' , 
                  'subTargets' : ['leptonMaker','lepSel','jetSel','CleanJetCut', 'rochesterDATA' , 'l2Kin', 'l3Kin', 'l4Kin','trigData', 'formulasDATA'],
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
                  'selection'  : '"(nElectron>0 && Electron_pt[0]>10) || (nMuon>0 && Muon_pt[0]>10)"' , 
                  #'subTargets' : ['leptonMaker','lepSel','jetSel','CleanJetCut', 'rochesterDATA' , 'l2Kin', 'l3Kin', 'l4Kin','trigData', 'formulasDATA'],
                  'subTargets' : ['leptonMaker','lepSel','jetSel','CleanJetCut', 'l2Kin', 'l3Kin', 'l4Kin','trigData', 'formulasDATA'], ## removing rochesterDATA
                },

## ------- WgStar DATA:

    'DATAWgStar2017v2' : { 
                  'isChain'    : True  ,
                  'do4MC'      : False ,
                  'do4Data'    : True  ,
                  'selection'  : '"((nElectron+nMuon)>1)"' ,
                  'subTargets' : ['leptonMaker','WgSSel', 'rochesterDATA','jetSel','CleanJetCut' , 'l2Kin', 'l3Kin', 'l4Kin','trigData','formulasDATA'],
                   },

# ------------------------------------------------ MODULES ---------------------------------------------------

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

## ------- MODULES: Object Handling

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
                  'declare'    : 'jetSel = lambda : JetSel(2,"loose",15.0,4.7,"CleanJet")' ,
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
                 'declare'    : 'trigData = lambda : TrigMaker("RPLME_CMSSW",True)',
                 'module'     : 'trigData()',
               },

 
  'trigMC'   : { 'isChain'    : False ,
                 'do4MC'      : True  ,
                 'do4Data'    : False ,
                 'import'     : 'LatinoAnalysis.NanoGardener.modules.TrigMaker' ,
                 'declare'    : 'trigMC = lambda : TrigMaker("RPLME_CMSSW",False,False)',
                 'module'     : 'trigMC()',
               },

  'trigMCKeepRun' : { 'isChain'    : False ,
                 'do4MC'      : True  ,
                 'do4Data'    : False ,
                 'import'     : 'LatinoAnalysis.NanoGardener.modules.TrigMaker' ,
                 'declare'    : 'trigMCKR = lambda : TrigMaker("RPLME_CMSSW",False,True)',
                 'module'     : 'trigMCKR()',
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
                  'module'     : 'btagSFProducer(era="2016", algo="cmva")',
                 },

  'btagPerJet2017': {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'import'     : 'PhysicsTools.NanoAODTools.postprocessing.modules.btv.btagSFProducer' ,
                  'declare'    : 'btagSFProducer2017 = lambda : btagSFProducer(era="2017", algo="deepcsv")',
                  'module'     : 'btagSFProducer2017()',
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

   'LeptonSF_Fix' : {
                  'isChain'    : True ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'subTargets' : ['LeptonSF','formulasMC'],
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

## ------- MODULES: Fakes

  'fakeW_New'  : {
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

  'fakeWstep'   : {
                  'isChain'    : False ,
                  'do4MC'      : False ,
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
   
  'formulasMC16tmp' : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.GenericFormulaAdder' ,
                  'declare'    : '',
                  'module'     : 'GenericFormulaAdder(\'data/formulasToAdd_MC_16tmp.py\')' ,
                 },


  'formulasDATA' : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.GenericFormulaAdder' ,
                  'declare'    : '',
                  'module'     : 'GenericFormulaAdder(\'data/formulasToAdd_DATA_RPLME_YEAR.py\')' ,
                 },

  'formulasFAKE' : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.GenericFormulaAdder' ,
                  'declare'    : '',
                  'module'     : 'GenericFormulaAdder(\'data/formulasToAdd_FAKE_RPLME_YEAR.py\')' ,
                 },

## -------- DYMVA

  'DYMVA' : {
                  'prebash'    : ['source /cvmfs/sft.cern.ch/lcg/views/LCG_92/x86_64-slc6-gcc62-opt/setup.sh'] ,   
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : True  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.TMVAfiller' ,
                  #'declare'    : 'DYMVA = lambda : TMVAfiller(\'data/DYMVA_cfg.py\')' ,
                  #'declare'    : 'DYMVA = lambda : TMVAfiller(\'data/DYMVA_2017_BDT_cfg.py\')' ,
                  'declare'    : 'DYMVA = lambda : TMVAfiller(\'data/DYMVA_2017_cfg.py\')' ,
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

  'fakeSelMC'  : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  , 
                  'selection'  : '"((MET_pt < 20 || PuppiMET_pt < 20) && mtw1 < 20)"' , 
                  'onlySample' : [
                                  #### DY
                                  'DYJetsToLL_M-10to50','DYJetsToLL_M-50','DYJetsToLL_M-10to50ext3','DYJetsToLL_M-50-LO','DYJetsToLL_M-50-LO-ext1','DYJetsToLL_M-10to50-LO',
                                  'DYJetsToTT_MuEle_M-50','DYJetsToLL_M-50_ext2',
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
                                  'TT','TTJets','TTTo2L2Nu',
                                 ] ,               
                 },

## ------- 2-Leptons: Loose / tightOR

  'l2loose'   : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : True  , 
                  'selection'  : '"(nLepton>=2)"' , 
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
                                    'GluGluHToWWTo2L2NuPowheg_M125_CP5Down', 'VBFHToWWTo2L2NuPowheg_M125_CP5Down', 'WWTo2L2Nu_CP5Down'
                                 ] ,
                  'cpMap' : {
                              'UEdo' : {
                                          'GluGluHToWWTo2L2NuPowheg_M125_CP5Down' : ['GluGluHToWWTo2L2NuPowheg_M125_PrivateNano' ,'GluGluHToWWTo2L2NuPowheg_M125'],
                                          'VBFHToWWTo2L2NuPowheg_M125_CP5Down'    : ['VBFHToWWTo2L2NuPowheg_M125_PrivateNano','VBFHToWWTo2L2NuPowheg_M125']    ,
                                          'WWTo2L2Nu_CP5Down'               : ['WWTo2L2Nu_PrivateNano', 'WWTo2L2Nu'] ,
                                       },
                              'UEup' : {
                                          'GluGluHToWWTo2L2NuPowheg_M125_CP5Up' : ['GluGluHToWWTo2L2NuPowheg_M125_PrivateNano' ,'GluGluHToWWTo2L2NuPowheg_M125'],
                                          'VBFHToWWTo2L2NuPowheg_M125_CP5Up'    : ['VBFHToWWTo2L2NuPowheg_M125_PrivateNano','VBFHToWWTo2L2NuPowheg_M125']    ,
                                          'WWTo2L2Nu_CP5Up'               : ['WWTo2L2Nu_PrivateNano', 'WWTo2L2Nu'] ,
                                       },
                              'PS'   : {
                                       },
                            },
               },

} 


