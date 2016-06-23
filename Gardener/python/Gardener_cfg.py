
eosProdBase= '/eos/cms/'
eosTargBaseIn = '/eos/user/x/xjanssen/HWW2015/'
eosTargBaseOut= '/eos/user/x/xjanssen/HWW2015/'


# ---- production to run on
# .... .... this is defined by mkGardener in "-p" "--prods" option

Productions= {

#### 74x / 21Oct & 21OctBis tags / miniAOD v2

  '21Oct_25ns_MC'   : {
                        'isData'  : False ,
                        'samples' : 'LatinoTrees/AnalysisStep/test/crab/samples/samples_spring15_miniaodv2_25ns.py' , 
                      #  'dirExt'  : 'LatinoTrees' ,
                        'dirExt'  : 'split' ,
                        'gDocID'  : '1wH73CYA_T4KMkl1Cw-xLTj8YG7OPqayDnP53N-lZwFQ' ,
                        #'puData'  : '/afs/cern.ch/user/x/xjanssen/public/MyDataPileupHistogram.root',
                        'puData'  : '/afs/cern.ch/user/x/xjanssen/public/Cert_246908-260627_13TeV_PromptReco_Collisions15_25ns_JSON_v2_from256630_PileupHistogram.root' ,
                        #'bigSamples': ['DYJetsToLL_M-10to50'] ,
                        'cmssw' : '74x' ,
                      } ,

  '21Oct_Run2015D_05Oct2015' : {
                        'isData'  : True ,
                        'samples' : 'LatinoTrees/AnalysisStep/test/crab/samples/samples_dataD_05Oct2015_25ns.py' ,
                        #'dirExt'  : 'Run2015D_05Oct2015' ,
                        'dirExt'  : 'split' ,
                        'cmssw' : '74x' ,
                      } ,

  '21Oct_Run2015D_PromptReco' : {
                        'isData'  : True ,
                        'samples' : 'LatinoTrees/AnalysisStep/test/crab/samples/samples_dataD_PromptReco_25ns.py' ,
                        #'dirExt'  : 'Run2015D_PromptReco' ,
                        'dirExt'  : 'split' ,
                        'cmssw' : '74x' ,
                      } ,

  '21OctBis_Run2015D_05Oct2015' : {
                        'isData'  : True ,
                        'samples' : 'LatinoTrees/AnalysisStep/test/crab/samples/samples_dataD_05Oct2015_25ns_21OctBis.py',
                        #'dirExt'  : 'Run2015D_PromptReco' ,
                        'dirExt'  : 'split2' ,
                        'cmssw' : '74x' ,
                      } ,

  '21OctBis_Run2015D_PromptReco_0716pb' : {
                        'isData'  : True ,
                        'samples' : 'LatinoTrees/AnalysisStep/test/crab/samples/samples_dataD_PromptReco_25ns_21OctBis_0716pb.py' ,
                        'dirExt'  : 'split2' ,
                        'cmssw' : '74x' ,
                      } ,

  '21OctBis_Run2015D_PromptReco_0851pb' : {
                        'isData'  : True ,
                        'samples' : 'LatinoTrees/AnalysisStep/test/crab/samples/samples_dataD_PromptReco_25ns_21OctBis_0851pb.py' ,
                        'dirExt'  : 'split2' ,
                        'cmssw' : '74x' ,
                      } ,

#### 76x / StarWars tag / miniAOD v1

  '08Jan_25ns_mAODv1_MC'   : {
                        'isData'  : False ,
                        'samples' : 'LatinoTrees/AnalysisStep/test/crab/samples/samples_fall15_miniaod_25ns.py' ,
                        'dirExt'  : 'LatinoTrees' ,
                        'gDocID'  : '1wH73CYA_T4KMkl1Cw-xLTj8YG7OPqayDnP53N-lZwFQ' ,
                        'puData'  : '/afs/cern.ch/user/x/xjanssen/public/Cert_246908-260627_13TeV_PromptReco_Collisions15_25ns_JSON_v2_from256630_PileupHistogram.root' ,
                        'cmssw'   : '763' ,
                      } ,

#### 76x / StarWars tag (v2) / miniAOD v2

  '18Jan_25ns_mAODv2_MC_TEST'   : {
                        'isData'  : False ,
                        'samples' : 'LatinoTrees/AnalysisStep/test/crab/samples/samples_fall15_miniaodv2_25ns.py' ,
                        'dir'     : '/store/group/phys_higgs/cmshww/amassiro/RunII/18Jan/MC/25ns/',
                        'dirExt'  : 'LatinoTrees' ,
                        #'gDocID'  : '1wH73CYA_T4KMkl1Cw-xLTj8YG7OPqayDnP53N-lZwFQ' ,
                        'puData'  : '/afs/cern.ch/user/x/xjanssen/public/Cert_246908-260627_13TeV_PromptReco_Collisions15_25ns_JSON_v2_from256630_PileupHistogram.root' ,
                        'cmssw'   : '763' ,
                      } ,


#### 76x / StarWars tag (v3) / miniAOD v2

  '22Jan_25ns_mAODv2_MC'   : {
                        'isData'  : False ,
                        'samples' : 'LatinoTrees/AnalysisStep/test/crab/samples/samples_fall15_miniaodv2_25ns.py' ,
                        'dirExt'  : 'LatinoTrees' ,
                        #'gDocID'  : '1wH73CYA_T4KMkl1Cw-xLTj8YG7OPqayDnP53N-lZwFQ' ,
                        'puData'  : '/afs/cern.ch/user/x/xjanssen/public/Cert_246908-260627_13TeV_PromptReco_Collisions15_25ns_JSON_v2_from256630_PileupHistogram.root' ,
                        'cmssw'   : '763' ,
                      } ,

  '22Jan_Run2015D_16Dec2015' : {
                        'isData'  : True ,
                        'samples' : 'LatinoTrees/AnalysisStep/test/crab/samples/samples_dataD_16Dec2015-v1_25ns_StarWars.py' ,
                        'dirExt'  : 'LatinoTrees' ,
                        'cmssw'   : '763' ,
                        'reName'  : { 
                                       'DoubleEG_Run2015D_25ns-16Dec2015-v2'       : 'Run2015D_16Dec2015_DoubleEG' ,
                                       'DoubleMuon_Run2015D_25ns-16Dec2015-v1'     : 'Run2015D_16Dec2015_DoubleMuon' ,
                                       'MuonEG_Run2015D_25ns-16Dec2015-v1'         : 'Run2015D_16Dec2015_MuonEG' , 
                                       'SingleElectron_Run2015D_25ns-16Dec2015-v1' : 'Run2015D_16Dec2015_SingleElectron' ,
                                       'SingleMuon_Run2015D_25ns-16Dec2015-v1'     : 'Run2015D_16Dec2015_SingleMuon' ,
                                      #'MET_Run2015D_25ns-16Dec2015-v1'            : 'Run2015D_16Dec2015_MET' ,
                                      #'SinglePhoton_Run2015D_25ns-16Dec2015-v1'   : 'Run2015D_16Dec2015_SinglePhoton' ,
                                    }
                      } ,

  '22Jan_Run2015C_16Dec2015' : {
                        'isData'  : True ,
                        'samples' : 'LatinoTrees/AnalysisStep/test/crab/samples/samples_dataC_16Dec2015-v1_25ns_StarWars.py',
                        'dirExt'  : 'LatinoTrees' ,
                        'cmssw'   : '763' ,
                        'reName'  : {
                                       'DoubleEG_Run2015C_25ns-16Dec2015-v1'       : 'Run2015C_16Dec2015_DoubleEG' ,
                                       'DoubleMuon_Run2015C_25ns-16Dec2015-v1'     : 'Run2015C_16Dec2015_DoubleMuon' ,
                                       'MuonEG_Run2015C_25ns-16Dec2015-v1'         : 'Run2015C_16Dec2015_MuonEG' ,
                                       'SingleElectron_Run2015C_25ns-16Dec2015-v1' : 'Run2015C_16Dec2015_SingleElectron' ,
                                       'SingleMuon_Run2015C_25ns-16Dec2015-v1'     : 'Run2015C_16Dec2015_SingleMuon' ,
                                   }
                      } ,

  '03Mar_25ns_mAODv2_MC'   : {
                        'isData'  : False ,
                        'samples' : 'LatinoTrees/AnalysisStep/test/crab/samples/samples_fall15_miniaodv2_25ns.py' ,
                        'dir'     : '/store/group/phys_higgs/cmshww/amassiro/RunII/03Mar/MC/25ns/',
                        'dirExt'  : 'LatinoTrees' ,
                        #'gDocID'  : '1wH73CYA_T4KMkl1Cw-xLTj8YG7OPqayDnP53N-lZwFQ' ,
                        'puData'  : '/afs/cern.ch/user/x/xjanssen/public/Cert_246908-260627_13TeV_PromptReco_Collisions15_25ns_JSON_v2_from256630_PileupHistogram.root' ,
                        'cmssw'   : '763' ,
                      } ,


  '03Mar_Run2015D_16Dec2015' : {
                        'isData'  : True ,
                        'samples' : 'LatinoTrees/AnalysisStep/test/crab/samples/samples_dataD_16Dec2015-v1_25ns_StarWars.py' ,
                        'dirExt'  : 'LatinoTrees' ,
                        'cmssw'   : '763' ,
                        'reName'  : {
                                       'DoubleEG_Run2015D_25ns-16Dec2015-v2'       : 'Run2015D_16Dec2015_DoubleEG' ,
                                       'DoubleMuon_Run2015D_25ns-16Dec2015-v1'     : 'Run2015D_16Dec2015_DoubleMuon' ,
                                       'MuonEG_Run2015D_25ns-16Dec2015-v1'         : 'Run2015D_16Dec2015_MuonEG' ,
                                       'SingleElectron_Run2015D_25ns-16Dec2015-v1' : 'Run2015D_16Dec2015_SingleElectron' ,
                                       'SingleMuon_Run2015D_25ns-16Dec2015-v1'     : 'Run2015D_16Dec2015_SingleMuon' ,
                                      #'MET_Run2015D_25ns-16Dec2015-v1'            : 'Run2015D_16Dec2015_MET' ,
                                      #'SinglePhoton_Run2015D_25ns-16Dec2015-v1'   : 'Run2015D_16Dec2015_SinglePhoton' ,
                                    }
                      } ,

  '03Mar_Run2015C_16Dec2015' : {
                        'isData'  : True ,
                        'samples' : 'LatinoTrees/AnalysisStep/test/crab/samples/samples_dataC_16Dec2015-v1_25ns_StarWars.py',
                        'dirExt'  : 'LatinoTrees' ,
                        'cmssw'   : '763' ,
                        'reName'  : {
                                       'DoubleEG_Run2015C_25ns-16Dec2015-v1'       : 'Run2015C_16Dec2015_DoubleEG' ,
                                       'DoubleMuon_Run2015C_25ns-16Dec2015-v1'     : 'Run2015C_16Dec2015_DoubleMuon' ,
                                       'MuonEG_Run2015C_25ns-16Dec2015-v1'         : 'Run2015C_16Dec2015_MuonEG' ,
                                       'SingleElectron_Run2015C_25ns-16Dec2015-v1' : 'Run2015C_16Dec2015_SingleElectron' ,
                                       'SingleMuon_Run2015C_25ns-16Dec2015-v1'     : 'Run2015C_16Dec2015_SingleMuon' ,
                                   }
                      } ,

# 80X 2016 DAT/MC --> REM: Still using 763 post-processing  --> MoneyMonster tag

  '13May2016_25ns_Spring16_MC'   : {
                        'isData'  : False ,
                        'samples' : 'LatinoTrees/AnalysisStep/test/crab/samples/samples_spring16_miniaod.py' ,
                        'dir'     : '/store/group/phys_higgs/cmshww/amassiro/RunII/2016/May13/MC/25ns/',
                        'dirExt'  : 'LatinoTrees' ,
                        'cmssw'   : '763' ,
                        #'gDocID'  : '1wH73CYA_T4KMkl1Cw-xLTj8YG7OPqayDnP53N-lZwFQ' ,
                        #'puData'  : '/afs/cern.ch/user/x/xjanssen/public/Cert_246908-260627_13TeV_PromptReco_Collisions15_25ns_JSON_v2_from256630_PileupHistogram.root' ,
                      } ,

  '20May2016_Run2016B_PromptReco' : {
                        'isData'  : True ,        
                        'samples' : 'LatinoTrees/AnalysisStep/test/crab/samples/samples_data_2016_PromptReco.py',
                        'dir'     : '/store/group/phys_higgs/cmshww/amassiro/RunII/2016/May20/data/25ns/',
                        'dirExt'  : 'LatinoTrees' ,
                        'cmssw'   : '763' ,
                        'reName'  : {
                                       'DoubleEG_Run2016B-PromptReco-v2'          : 'Run2016B_PromptReco_DoubleEG',
                                       'DoubleMuon_Run2016B-PromptReco-v2'        : 'Run2016B_PromptReco_DoubleMuon',
                                       'MuonEG_Run2016B-PromptReco-v2'            : 'Run2016B_PromptReco_MuonEG',
                                       'SingleElectron_Run2016B-PromptReco-v2'    : 'Run2016B_PromptReco_SingleElectron',   
                                       'SingleMuon_Run2016B-PromptReco-v2'        : 'Run2016B_PromptReco_SingleMuon',
                                    },
                     },


# 80X 2016 DATA/MC: 3June2016_NinjaTurtles_v3 Tag / mAODv2

  '07Jun2016_spring16__mAODv2'   : {
                        'isData'  : False ,
                        'samples' : 'LatinoTrees/AnalysisStep/test/crab/samples/samples_spring16_miniaod_v2.py' ,
                        'dir'     : '/store/group/phys_higgs/cmshww/amassiro/RunII/2016/Jun07/MC/v2/',
                        'dirExt'  : 'LatinoTrees' ,
                        'cmssw'   : 'ICHEP2016' ,
                        # [FIXME] Partial PU data only, missing latest runs
                        'puData'  : '/afs/cern.ch/user/x/xjanssen/public/PileupHistogram_805_15Jun.root' , 
                       },

  '07Jun2016_Run2016B_PromptReco' : {
                        'isData'  : True ,
                        'samples' : 'LatinoTrees/AnalysisStep/test/crab/samples/samples_data_2016_PromptReco.py',
                        'dir'     : '/store/group/phys_higgs/cmshww/amassiro/RunII/2016/Jun07/data/25ns/',
                        'dirExt'  : 'LatinoTrees' ,
                        'cmssw'   : 'ICHEP2016' ,
                        'reName'  : {
                                       'DoubleEG_Run2016B-PromptReco-v2'          : 'Run2016B_PromptReco_DoubleEG',
                                       'DoubleMuon_Run2016B-PromptReco-v2'        : 'Run2016B_PromptReco_DoubleMuon',
                                       'MuonEG_Run2016B-PromptReco-v2'            : 'Run2016B_PromptReco_MuonEG',
                                       'SingleElectron_Run2016B-PromptReco-v2'    : 'Run2016B_PromptReco_SingleElectron',
                                       'SingleMuon_Run2016B-PromptReco-v2'        : 'Run2016B_PromptReco_SingleMuon',
                                    },
                       },
            


}



# ---- Steps
# .... .... this is defined by mkGardener in "-s" "--steps" option
# .... .... if it is a "chain", it means that the intermediate steps are NOT saved
# .... ....    e.g. 'puadder','baseW','wwNLL' ---> only after all steps the folder will be saved on eos

Steps= {

# ... Chains

  'MC' :       {
                  'isChain'    : True ,
                  'do4MC'      : True , 
                  'do4Data'    : False,
                  'subTargets' : ['puadder','baseW','wwNLL']
                },

  'MCl2sel' :       {
                  'isChain'    : True ,
                  'do4MC'      : True ,
                  'do4Data'    : False,
                  'subTargets' : ['puadder','baseW','wwNLL','l2sel','genVariables']
                },

  'MCl2loose' :       {
                  'isChain'    : True ,
                  'do4MC'      : True ,
                  'do4Data'    : False,
                  'subTargets' : ['l2loose','puadder','baseW','wwNLL','genVariables','genMatchVariables','BWEwkSinglet'],
                },

  'MCl2loose16' :       {
                  'isChain'    : True ,
                  'do4MC'      : True ,
                  'do4Data'    : False,
                  'subTargets' : ['l2loose','puadder','baseW','wwNLL','genVariables','genMatchVariables','l2kin','l3kin','BWEwkSinglet'],
                },


  'l2loose16'  :       {
                  'isChain'    : True ,
                  'do4MC'      : False ,
                  'do4Data'    : True,
                  'subTargets' : ['l2loose','l2kin','l3kin'],
                },


# 'l1loose16'  :       {
#                 'isChain'    : True ,
#                 'do4MC'      : False ,
#                 'do4Data'    : True,
#                 'subTargets' : ['l1loose','l2kin'],
#               },



  'MCl2vloose' :       {
                  'isChain'    : True ,
                  'do4MC'      : True ,
                  'do4Data'    : False,
                  'subTargets' : ['l2vloose','puadder','baseW','wwNLL','genVariables','genMatchVariables','BWEwkSinglet'],
		  'onlySample' : [ 
			   	  # VBS
				  'DYJetsToLL_M-50','DYJetsToLL_M-10to50ext3',
 			  	  'WpWpJJ_EWK','WpWpJJ_EWK_QCD','WpWpJJ_QCD','WW_DoubleScattering','WLLJJToLNu_M-4to60_EWK_QCD','WLLJJToLNu_M-60_EWK_QCD','WGJJ',
                                  'TTToSemiLeptonic',
                                 ] ,
                },



  'MCl1loose' :       {
                  'isChain'    : True ,
                  'do4MC'      : True ,
                  'do4Data'    : False,
                  'subTargets' : ['l1loose','puadder','baseW','wwNLL','genVariables','genMatchVariables','BWEwkSinglet'],
                  'onlySample' : [
                                  #### DY 
                                  'DYJetsToLL_M-10to50','DYJetsToLL_M-50','DYJetsToLL_M-10to50ext3',',DYJetsToLL_M-50-LO',
                                  ####
                                  'WJetsToLNu','WJetsToLNu_HT100_200','WJetsToLNu_HT200_400','WJetsToLNu_HT400_600','WJetsToLNu_HT600_800',
                                  'WJetsToLNu_HT800_1200','WJetsToLNu_HT1200_2500','WJetsToLNu_HT2500_inf',
                                  ####
                                  'QCD_Pt-15to20_EMEnriched', 'QCD_Pt-20to30_EMEnriched', 'QCD_Pt-30to50_EMEnriched', 'QCD_Pt-50to80_EMEnriched',
                                  'QCD_Pt-20toInf_MuEnrichedPt15',
                                  ####
                                  'QCD_Pt_15to20_bcToE','QCD_Pt_20to30_bcToE','QCD_Pt_30to80_bcToE','QCD_Pt_80to170_bcToE',
                                  'QCD_Pt_170to250_bcToE','QCD_Pt_250toInf_bcToE',
                                  ####
                                  'TT','TTJets',
 
                                 ] ,

                },

  'MCl1vloose' :       {
                  'isChain'    : True ,
                  'do4MC'      : True ,
                  'do4Data'    : False,
                  'subTargets' : ['l1vloose','puadder','baseW','wwNLL','genVariables','genMatchVariables','BWEwkSinglet'],
                  'onlySample' : [
                                  #### DY 
                                  'DYJetsToLL_M-10to50','DYJetsToLL_M-50','DYJetsToLL_M-10to50ext3',',DYJetsToLL_M-50-LO',
                                  ####
                                  'WJetsToLNu','WJetsToLNu_HT100_200','WJetsToLNu_HT200_400','WJetsToLNu_HT400_600','WJetsToLNu_HT600_800',
                                  'WJetsToLNu_HT800_1200','WJetsToLNu_HT1200_2500','WJetsToLNu_HT2500_inf',
                                  ####
                                  'QCD_Pt-15to20_EMEnriched', 'QCD_Pt-20to30_EMEnriched', 'QCD_Pt-30to50_EMEnriched', 'QCD_Pt-50to80_EMEnriched',
                                  'QCD_Pt-20toInf_MuEnrichedPt15',
                                  ####
                                  'QCD_Pt_15to20_bcToE','QCD_Pt_20to30_bcToE','QCD_Pt_30to80_bcToE','QCD_Pt_80to170_bcToE',
                                  'QCD_Pt_170to250_bcToE','QCD_Pt_250toInf_bcToE',
                                  ####
                                  'TT','TTJets',
                                 ] ,
                },


  'MCWgStarsel' : {
                  'isChain'    : True ,
                  'do4MC'      : True ,
                  'do4Data'    : False,
                  'subTargets' : ['do_WgStarsel','puadder','baseW','wwNLL','genVariables','genMatchVariables'],
                  'onlySample' : [
                                   'Wg500','Wg_AMCNLOFXFX','WZTo3LNu','WgStarLNuEE','WgStarLNuMuMu',
                                   'DYJetsToLL_M-10to50','DYJetsToLL_M-50','DYJetsToLL_M-10to50ext3', 
                                   'WZTo2L2Q',
                                 ]
                },

  'WgStarsel' : {
                  'isChain'    : True ,
                  'do4MC'      : False ,
                  'do4Data'    : True,
                  'subTargets' : ['do_WgStarsel'],
                  'onlySample' : [
                                   'Run2015C_16Dec2015_DoubleMuon' , 'Run2015C_16Dec2015_SingleElectron' , 'Run2015C_16Dec2015_SingleMuon',
                                   'Run2015D_16Dec2015_DoubleMuon' , 'Run2015D_16Dec2015_SingleElectron' , 'Run2015D_16Dec2015_SingleMuon',
                                 ]
                },


  'bSFL2Eff'   :   {
                  'isChain'    : True ,
                  'do4MC'      : True ,
                  'do4Data'    : True ,
                  'subTargets' : ['bPogSF','TrigEff','IdIsoSC'],
                },
      

  'EpTCorr'       :  {
                  'isChain'    : True ,
                  'do4MC'      : True ,
                  'do4Data'    : True ,
                  'subTargets' : ['do_lpTCorrMC','do_lpTCorrData','l2kin','l3kin'],
                },

  'bSFKinFix'    : {
                  'isChain'    : True ,
                  'do4MC'      : True ,
                  'do4Data'    : False ,
                  'subTargets' : ['bPogSF','genMatchVariables'],
                },

  'KinFix'    : {
                  'isChain'    : True ,
                  'do4MC'      : True ,
                  'do4Data'    : False ,
                  'subTargets' : ['genMatchVariables'],
                },


  'filterjson'   : {
                  'isChain'    : True ,
                  'do4MC'      : False ,
                  'do4Data'    : True ,
                  'subTargets' : ['tagjson', 'selectjson'],
                } ,

  'LepEff'       :  {
                  'isChain'    : True ,
                  'do4MC'      : True ,
                  'do4Data'    : False ,
                  'subTargets' : ['TrigEff','IdIsoSC']
                    }, 


  'bSFL2pTEff'   :   {
                  'isChain'    : True ,
                  'do4MC'      : True ,
                  'do4Data'    : True ,
                  'subTargets' : ['do_lpTCorrMC','do_lpTCorrData','bPogSF','TrigEff','IdIsoSC','l2kin','l3kin'],
                  'onlySample' : [
                                  # DY 
                                  'DYJetsToLL_M-10to50','DYJetsToLL_M-50','DYJetsToLL_M-10to50ext3', 'DYJetsToLL_M-50-LO' ,
                                  'DY2JetsToLL', 'DY3JetsToLL', 'DY4JetsToLL',
                                  'DYJetsToLL_M-50_HT-100to200_MLM' , 'DYJetsToLL_M-50_HT-100to200_MLM_ext' , 
                                  'DYJetsToLL_M-50_HT-200to400_MLM' , 
                                  'DYJetsToLL_M-50_HT-400to600_MLM' ,
                                  'DYJetsToLL_M-50_HT-600toInf_MLM' ,
                                  # WJets
                                  'WJetsToLNu',
                                  # Top
                                  'TTTo2L2Nu','TTWJetsToLNu',
                                  'ST_t-channel_antitop','ST_t-channel_top',
                                  'ST_tW_antitop','ST_tW_top',
                                  'TTToSemiLeptonic','TT',
                                  # VV (including WW) 
                                  'WWTo2L2Nu','GluGluWWTo2L2Nu_MCFM','GluGluWWTo2L2NuHiggs_MCFM',
                                  'WZTo3LNu',
                                  'ZZ','Zg',
                                  'ZZTo2L2Nu','ZZTo2L2Q','ZZTo4L',
                                  'Wg_AMCNLOFXFX', 
                                  'Wg_MADGRAPHMLM',
                                  'WZTo2L2Q',
                                  # VVV
                                  'WZZ','ZZZ','WWZ',
                                  # Higgs 
                                  'GluGluHToTauTau_M125', 'GluGluHToWWTo2L2Nu_M125','GluGluHToWWTo2L2NuPowheg_M125',
                                  'GluGluHToWWTo2L2Nu_alternative_M125','VBFHToWWTo2L2Nu_alternative_M125',
                                  'HWminusJ_HToTauTau_M125', 'HWminusJ_HToWW_M125',
                                  'HWplusJ_HToTauTau_M125', 'HWplusJ_HToWW_M125',
                                  'HZJ_HToTauTau_M125', 'HZJ_HToWW_M125',
                                  'VBFHToTauTau_M125', 'VBFHToWWTo2L2Nu_M125',
                                  'ggZH_HToWW_M125', # missing ggZHToTauTau
                                  'ttHJetToNonbb_M125',
                                  # ... ggH High Mass
                                  'GluGluHToWWTo2L2Nu_M130',
                                  'GluGluHToWWTo2L2Nu_M135',
                                  'GluGluHToWWTo2L2Nu_M140',
                                  'GluGluHToWWTo2L2Nu_M145',
                                  'GluGluHToWWTo2L2Nu_M150',
                                  'GluGluHToWWTo2L2Nu_M155',
                                  'GluGluHToWWTo2L2Nu_M160',
                                  'GluGluHToWWTo2L2Nu_M165',
                                  'GluGluHToWWTo2L2Nu_M170',
                                  'GluGluHToWWTo2L2Nu_M175',
                                  'GluGluHToWWTo2L2Nu_M180',
                                  'GluGluHToWWTo2L2Nu_M190',
                                  'GluGluHToWWTo2L2Nu_M200',
                                  'GluGluHToWWTo2L2Nu_M210',
                                  'GluGluHToWWTo2L2Nu_M230',
                                  'GluGluHToWWTo2L2Nu_M250',
                                  'GluGluHToWWTo2L2Nu_M270',
                                  'GluGluHToWWTo2L2Nu_M300',
                                  'GluGluHToWWTo2L2Nu_M350',
                                  'GluGluHToWWTo2L2Nu_M400',
                                  'GluGluHToWWTo2L2Nu_M450',
                                  'GluGluHToWWTo2L2Nu_M500',
                                  'GluGluHToWWTo2L2Nu_M550',
                                  'GluGluHToWWTo2L2Nu_M600',
                                  'GluGluHToWWTo2L2Nu_M650',
                                  'GluGluHToWWTo2L2Nu_M700',
                                  'GluGluHToWWTo2L2Nu_M750',
                                  'GluGluHToWWTo2L2Nu_M750_NWA',
                                  'GluGluHToWWTo2L2Nu_M800',
                                  'GluGluHToWWTo2L2Nu_M900',
                                  'GluGluHToWWTo2L2Nu_M1000',
                                  # ... VBF High Mass
                                  'VBFHToWWTo2L2Nu_M130',
                                  'VBFHToWWTo2L2Nu_M135',
                                  'VBFHToWWTo2L2Nu_M140',
                                  'VBFHToWWTo2L2Nu_M145',
                                  'VBFHToWWTo2L2Nu_M150',
                                  'VBFHToWWTo2L2Nu_M155',
                                  'VBFHToWWTo2L2Nu_M160',
                                  'VBFHToWWTo2L2Nu_M165',
                                  'VBFHToWWTo2L2Nu_M170',
                                  'VBFHToWWTo2L2Nu_M175',
                                  'VBFHToWWTo2L2Nu_M180',
                                  'VBFHToWWTo2L2Nu_M190',
                                  'VBFHToWWTo2L2Nu_M200',
                                  'VBFHToWWTo2L2Nu_M210',
                                  'VBFHToWWTo2L2Nu_M230',
                                  'VBFHToWWTo2L2Nu_M250',
                                  'VBFHToWWTo2L2Nu_M270',
                                  'VBFHToWWTo2L2Nu_M300',
                                  'VBFHToWWTo2L2Nu_M350',
                                  'VBFHToWWTo2L2Nu_M400',
                                  'VBFHToWWTo2L2Nu_M450',
                                  'VBFHToWWTo2L2Nu_M500',
                                  'VBFHToWWTo2L2Nu_M550',
                                  'VBFHToWWTo2L2Nu_M600',
                                  'VBFHToWWTo2L2Nu_M650',
                                  'VBFHToWWTo2L2Nu_M700',
                                  'VBFHToWWTo2L2Nu_M750',
                                  'VBFHToWWTo2L2Nu_M750_NWA',
                                  'VBFHToWWTo2L2Nu_M800',
                                  'VBFHToWWTo2L2Nu_M900',
                                  'VBFHToWWTo2L2Nu_M1000',
                                  # PS
                                  'GluGluHToWWTo2L2NuHerwigPS_M125','VBFHToWWTo2L2NuHerwigPS_M125','WWTo2L2NuHerwigPS',
                                  # UE
                                  'GluGluHToWWTo2L2Nu_M125_CUETDown',
                                  'GluGluHToWWTo2L2Nu_M125_CUETUp',
                                  'VBFHToWWTo2L2Nu_M125_CUETDown',
                                  'VBFHToWWTo2L2Nu_M125_CUETUp',
                                  'WWTo2L2Nu_CUETDown',
                                  'WWTo2L2Nu_CUETUp',
 			  # VBS
 			  'WpWpJJ_EWK','WpWpJJ_EWK_QCD','WpWpJJ_QCD','WW_DoubleScattering','WLLJJToLNu_M-4to60_EWK_QCD','WLLJJToLNu_M-60_EWK_QCD',
                          'WGJJ','EWKZ2Jets','TTToSemiLeptonic'
                                 ] ,
                },


  'JESup'     :  {
                  'isChain'    : True ,
                  'do4MC'      : True ,
                  'do4Data'    : False,
                  'subTargets' : ['do_JESup','bPogSF','l2kin','l3kin'],
                  'onlySample' : [
                                  # DY 
                                  'DYJetsToLL_M-10to50','DYJetsToLL_M-50','DYJetsToLL_M-10to50ext3',
                                  'DY2JetsToLL', 'DY3JetsToLL', 'DY4JetsToLL',
                                  'DYJetsToLL_M-50_HT-100to200_MLM' , 'DYJetsToLL_M-50_HT-100to200_MLM_ext' , 
                                  'DYJetsToLL_M-50_HT-200to400_MLM' , 
                                  'DYJetsToLL_M-50_HT-400to600_MLM' ,
                                  'DYJetsToLL_M-50_HT-600toInf_MLM' ,
                                  # Top
                                  'TTTo2L2Nu','TT',
                                  'ST_t-channel_antitop','ST_t-channel_top',
                                  'ST_tW_antitop','ST_tW_top',
                                  # VV (including WW) 
                                  'WWTo2L2Nu','GluGluWWTo2L2Nu_MCFM','GluGluWWTo2L2NuHiggs_MCFM',
                                  'WZTo3LNu',
                                  'ZZ','Zg',
                                  'ZZTo2L2Nu','ZZTo2L2Q','ZZTo4L',
                                  'Wg_AMCNLOFXFX','WgStarLNuEE','WgStarLNuMuMu',
                                  'Wg_MADGRAPHMLM',
                                  # VVV
                                  'WZZ','ZZZ','WWZ',
                                  # Higgs 
                                  'GluGluHToTauTau_M125', 'GluGluHToWWTo2L2Nu_M125','GluGluHToWWTo2L2NuPowheg_M125',
                                  'GluGluHToWWTo2L2Nu_alternative_M125','VBFHToWWTo2L2Nu_alternative_M125',
                                  'HWminusJ_HToTauTau_M125', 'HWminusJ_HToWW_M125',
                                  'HWplusJ_HToTauTau_M125', 'HWplusJ_HToWW_M125',
                                  'HZJ_HToTauTau_M125', 'HZJ_HToWW_M125',
                                  'VBFHToTauTau_M125', 'VBFHToWWTo2L2Nu_M125',
                                  'ggZH_HToWW_M125', # missing ggZHToTauTau
                                  'ttHJetToNonbb_M125','TTWJetsToLNu',

                                  # ... ggH High Mass
                                  'GluGluHToWWTo2L2Nu_M130',
                                  'GluGluHToWWTo2L2Nu_M135',
                                  'GluGluHToWWTo2L2Nu_M140',
                                  'GluGluHToWWTo2L2Nu_M145',
                                  'GluGluHToWWTo2L2Nu_M150',
                                  'GluGluHToWWTo2L2Nu_M155',
                                  'GluGluHToWWTo2L2Nu_M160',
                                  'GluGluHToWWTo2L2Nu_M165',
                                  'GluGluHToWWTo2L2Nu_M170',
                                  'GluGluHToWWTo2L2Nu_M175',
                                  'GluGluHToWWTo2L2Nu_M180',
                                  'GluGluHToWWTo2L2Nu_M190',
                                  'GluGluHToWWTo2L2Nu_M200',
                                  'GluGluHToWWTo2L2Nu_M210',
                                  'GluGluHToWWTo2L2Nu_M230',
                                  'GluGluHToWWTo2L2Nu_M250',
                                  'GluGluHToWWTo2L2Nu_M270',
                                  'GluGluHToWWTo2L2Nu_M300',
                                  'GluGluHToWWTo2L2Nu_M350',
                                  'GluGluHToWWTo2L2Nu_M400',
                                  'GluGluHToWWTo2L2Nu_M450',
                                  'GluGluHToWWTo2L2Nu_M500',
                                  'GluGluHToWWTo2L2Nu_M550',
                                  'GluGluHToWWTo2L2Nu_M600',
                                  'GluGluHToWWTo2L2Nu_M650',
                                  'GluGluHToWWTo2L2Nu_M700',
                                  'GluGluHToWWTo2L2Nu_M750',
                                  'GluGluHToWWTo2L2Nu_M750_NWA',
                                  'GluGluHToWWTo2L2Nu_M800',
                                  'GluGluHToWWTo2L2Nu_M900',
                                  'GluGluHToWWTo2L2Nu_M1000',
                                  # ... VBF High Mass
                                  'VBFHToWWTo2L2Nu_M130',
                                  'VBFHToWWTo2L2Nu_M135',
                                  'VBFHToWWTo2L2Nu_M140',
                                  'VBFHToWWTo2L2Nu_M145',
                                  'VBFHToWWTo2L2Nu_M150',
                                  'VBFHToWWTo2L2Nu_M155',
                                  'VBFHToWWTo2L2Nu_M160',
                                  'VBFHToWWTo2L2Nu_M165',
                                  'VBFHToWWTo2L2Nu_M170',
                                  'VBFHToWWTo2L2Nu_M175',
                                  'VBFHToWWTo2L2Nu_M180',
                                  'VBFHToWWTo2L2Nu_M190',
                                  'VBFHToWWTo2L2Nu_M200',
                                  'VBFHToWWTo2L2Nu_M210',
                                  'VBFHToWWTo2L2Nu_M230',
                                  'VBFHToWWTo2L2Nu_M250',
                                  'VBFHToWWTo2L2Nu_M270',
                                  'VBFHToWWTo2L2Nu_M300',
                                  'VBFHToWWTo2L2Nu_M350',
                                  'VBFHToWWTo2L2Nu_M400',
                                  'VBFHToWWTo2L2Nu_M450',
                                  'VBFHToWWTo2L2Nu_M500',
                                  'VBFHToWWTo2L2Nu_M550',
                                  'VBFHToWWTo2L2Nu_M600',
                                  'VBFHToWWTo2L2Nu_M650',
                                  'VBFHToWWTo2L2Nu_M700',
                                  'VBFHToWWTo2L2Nu_M750',
                                  'VBFHToWWTo2L2Nu_M750_NWA',
                                  'VBFHToWWTo2L2Nu_M800',
                                  'VBFHToWWTo2L2Nu_M900',
                                  'VBFHToWWTo2L2Nu_M1000',
                                 ] ,
                },

  'JESdo'     :  {
                  'isChain'    : True ,
                  'do4MC'      : True ,
                  'do4Data'    : False,
                  'subTargets' : ['do_JESdo','bPogSF','l2kin','l3kin'],
                  'onlySample' : [
                                  # DY 
                                  'DYJetsToLL_M-10to50','DYJetsToLL_M-50','DYJetsToLL_M-10to50ext3',
                                  'DY2JetsToLL', 'DY3JetsToLL', 'DY4JetsToLL',
                                  'DYJetsToLL_M-50_HT-100to200_MLM' , 'DYJetsToLL_M-50_HT-100to200_MLM_ext' , 
                                  'DYJetsToLL_M-50_HT-200to400_MLM' , 
                                  'DYJetsToLL_M-50_HT-400to600_MLM' ,
                                  'DYJetsToLL_M-50_HT-600toInf_MLM' ,
                                  # Top
                                  'TTTo2L2Nu','TT',
                                  'ST_t-channel_antitop','ST_t-channel_top',
                                  'ST_tW_antitop','ST_tW_top',
                                  # VV (including WW) 
                                  'WWTo2L2Nu','GluGluWWTo2L2Nu_MCFM','GluGluWWTo2L2NuHiggs_MCFM',
                                  'WZTo3LNu',
                                  'ZZ','Zg',
                                  'ZZTo2L2Nu','ZZTo2L2Q','ZZTo4L',
                                  'Wg_AMCNLOFXFX','WgStarLNuEE','WgStarLNuMuMu',
                                  'Wg_MADGRAPHMLM',
                                  # VVV
                                  'WZZ','ZZZ','WWZ',
                                  # Higgs 
                                  'GluGluHToTauTau_M125', 'GluGluHToWWTo2L2Nu_M125','GluGluHToWWTo2L2NuPowheg_M125',
                                  'GluGluHToWWTo2L2Nu_alternative_M125','VBFHToWWTo2L2Nu_alternative_M125',
                                  'HWminusJ_HToTauTau_M125', 'HWminusJ_HToWW_M125',
                                  'HWplusJ_HToTauTau_M125', 'HWplusJ_HToWW_M125',
                                  'HZJ_HToTauTau_M125', 'HZJ_HToWW_M125',
                                  'VBFHToTauTau_M125', 'VBFHToWWTo2L2Nu_M125',
                                  'ggZH_HToWW_M125', # missing ggZHToTauTau
                                  'ttHJetToNonbb_M125','TTWJetsToLNu',

                                  # ... ggH High Mass
                                  'GluGluHToWWTo2L2Nu_M130',
                                  'GluGluHToWWTo2L2Nu_M135',
                                  'GluGluHToWWTo2L2Nu_M140',
                                  'GluGluHToWWTo2L2Nu_M145',
                                  'GluGluHToWWTo2L2Nu_M150',
                                  'GluGluHToWWTo2L2Nu_M155',
                                  'GluGluHToWWTo2L2Nu_M160',
                                  'GluGluHToWWTo2L2Nu_M165',
                                  'GluGluHToWWTo2L2Nu_M170',
                                  'GluGluHToWWTo2L2Nu_M175',
                                  'GluGluHToWWTo2L2Nu_M180',
                                  'GluGluHToWWTo2L2Nu_M190',
                                  'GluGluHToWWTo2L2Nu_M200',
                                  'GluGluHToWWTo2L2Nu_M210',
                                  'GluGluHToWWTo2L2Nu_M230',
                                  'GluGluHToWWTo2L2Nu_M250',
                                  'GluGluHToWWTo2L2Nu_M270',
                                  'GluGluHToWWTo2L2Nu_M300',
                                  'GluGluHToWWTo2L2Nu_M350',
                                  'GluGluHToWWTo2L2Nu_M400',
                                  'GluGluHToWWTo2L2Nu_M450',
                                  'GluGluHToWWTo2L2Nu_M500',
                                  'GluGluHToWWTo2L2Nu_M550',
                                  'GluGluHToWWTo2L2Nu_M600',
                                  'GluGluHToWWTo2L2Nu_M650',
                                  'GluGluHToWWTo2L2Nu_M700',
                                  'GluGluHToWWTo2L2Nu_M750',
                                  'GluGluHToWWTo2L2Nu_M750_NWA',
                                  'GluGluHToWWTo2L2Nu_M800',
                                  'GluGluHToWWTo2L2Nu_M900',
                                  'GluGluHToWWTo2L2Nu_M1000',
                                  # ... VBF High Mass
                                  'VBFHToWWTo2L2Nu_M130',
                                  'VBFHToWWTo2L2Nu_M135',
                                  'VBFHToWWTo2L2Nu_M140',
                                  'VBFHToWWTo2L2Nu_M145',
                                  'VBFHToWWTo2L2Nu_M150',
                                  'VBFHToWWTo2L2Nu_M155',
                                  'VBFHToWWTo2L2Nu_M160',
                                  'VBFHToWWTo2L2Nu_M165',
                                  'VBFHToWWTo2L2Nu_M170',
                                  'VBFHToWWTo2L2Nu_M175',
                                  'VBFHToWWTo2L2Nu_M180',
                                  'VBFHToWWTo2L2Nu_M190',
                                  'VBFHToWWTo2L2Nu_M200',
                                  'VBFHToWWTo2L2Nu_M210',
                                  'VBFHToWWTo2L2Nu_M230',
                                  'VBFHToWWTo2L2Nu_M250',
                                  'VBFHToWWTo2L2Nu_M270',
                                  'VBFHToWWTo2L2Nu_M300',
                                  'VBFHToWWTo2L2Nu_M350',
                                  'VBFHToWWTo2L2Nu_M400',
                                  'VBFHToWWTo2L2Nu_M450',
                                  'VBFHToWWTo2L2Nu_M500',
                                  'VBFHToWWTo2L2Nu_M550',
                                  'VBFHToWWTo2L2Nu_M600',
                                  'VBFHToWWTo2L2Nu_M650',
                                  'VBFHToWWTo2L2Nu_M700',
                                  'VBFHToWWTo2L2Nu_M750',
                                  'VBFHToWWTo2L2Nu_M750_NWA',
                                  'VBFHToWWTo2L2Nu_M800',
                                  'VBFHToWWTo2L2Nu_M900',
                                  'VBFHToWWTo2L2Nu_M1000',
                                 ] ,
                },


  'JESMaxup'     :  {
                  'isChain'    : True ,
                  'do4MC'      : True ,
                  'do4Data'    : False,
                  'subTargets' : ['do_JESMaxup','bPogSF','l2kin','l3kin'],
                  'onlySample' : [
                                  # DY 
                                  'DYJetsToLL_M-10to50','DYJetsToLL_M-50','DYJetsToLL_M-10to50ext3','DYJetsToLL_M-50-LO',
                                  'DY2JetsToLL', 'DY3JetsToLL', 'DY4JetsToLL',
                                  'DYJetsToLL_M-50_HT-100to200_MLM' , 'DYJetsToLL_M-50_HT-100to200_MLM_ext' , 
                                  'DYJetsToLL_M-50_HT-200to400_MLM' , 
                                  'DYJetsToLL_M-50_HT-400to600_MLM' ,
                                  'DYJetsToLL_M-50_HT-600toInf_MLM' ,
                                  # Top
                                  'TTTo2L2Nu','TT',
                                  'ST_t-channel_antitop','ST_t-channel_top',
                                  'ST_tW_antitop','ST_tW_top',
                                  # VV (including WW) 
                                  'WWTo2L2Nu','GluGluWWTo2L2Nu_MCFM','GluGluWWTo2L2NuHiggs_MCFM',
                                  'WZTo3LNu',
                                  'ZZ','Zg',
                                  'ZZTo2L2Nu','ZZTo2L2Q','ZZTo4L',
                                  'Wg_AMCNLOFXFX','WgStarLNuEE','WgStarLNuMuMu',
                                  'Wg_MADGRAPHMLM',
                                  # VVV
                                  'WZZ','ZZZ','WWZ',
                                  # Higgs 
                                  'GluGluHToTauTau_M125', 'GluGluHToWWTo2L2Nu_M125','GluGluHToWWTo2L2NuPowheg_M125',
                                  'GluGluHToWWTo2L2Nu_alternative_M125','VBFHToWWTo2L2Nu_alternative_M125',
                                  'HWminusJ_HToTauTau_M125', 'HWminusJ_HToWW_M125',
                                  'HWplusJ_HToTauTau_M125', 'HWplusJ_HToWW_M125',
                                  'HZJ_HToTauTau_M125', 'HZJ_HToWW_M125',
                                  'VBFHToTauTau_M125', 'VBFHToWWTo2L2Nu_M125',
                                  'ggZH_HToWW_M125', # missing ggZHToTauTau
                                  'ttHJetToNonbb_M125','TTWJetsToLNu',

                                  # ... ggH High Mass
                                  'GluGluHToWWTo2L2Nu_M130',
                                  'GluGluHToWWTo2L2Nu_M135',
                                  'GluGluHToWWTo2L2Nu_M140',
                                  'GluGluHToWWTo2L2Nu_M145',
                                  'GluGluHToWWTo2L2Nu_M150',
                                  'GluGluHToWWTo2L2Nu_M155',
                                  'GluGluHToWWTo2L2Nu_M160',
                                  'GluGluHToWWTo2L2Nu_M165',
                                  'GluGluHToWWTo2L2Nu_M170',
                                  'GluGluHToWWTo2L2Nu_M175',
                                  'GluGluHToWWTo2L2Nu_M180',
                                  'GluGluHToWWTo2L2Nu_M190',
                                  'GluGluHToWWTo2L2Nu_M200',
                                  'GluGluHToWWTo2L2Nu_M210',
                                  'GluGluHToWWTo2L2Nu_M230',
                                  'GluGluHToWWTo2L2Nu_M250',
                                  'GluGluHToWWTo2L2Nu_M270',
                                  'GluGluHToWWTo2L2Nu_M300',
                                  'GluGluHToWWTo2L2Nu_M350',
                                  'GluGluHToWWTo2L2Nu_M400',
                                  'GluGluHToWWTo2L2Nu_M450',
                                  'GluGluHToWWTo2L2Nu_M500',
                                  'GluGluHToWWTo2L2Nu_M550',
                                  'GluGluHToWWTo2L2Nu_M600',
                                  'GluGluHToWWTo2L2Nu_M650',
                                  'GluGluHToWWTo2L2Nu_M700',
                                  'GluGluHToWWTo2L2Nu_M750',
                                  'GluGluHToWWTo2L2Nu_M750_NWA',
                                  'GluGluHToWWTo2L2Nu_M800',
                                  'GluGluHToWWTo2L2Nu_M900',
                                  'GluGluHToWWTo2L2Nu_M1000',
                                  # ... VBF High Mass
                                  'VBFHToWWTo2L2Nu_M130',
                                  'VBFHToWWTo2L2Nu_M135',
                                  'VBFHToWWTo2L2Nu_M140',
                                  'VBFHToWWTo2L2Nu_M145',
                                  'VBFHToWWTo2L2Nu_M150',
                                  'VBFHToWWTo2L2Nu_M155',
                                  'VBFHToWWTo2L2Nu_M160',
                                  'VBFHToWWTo2L2Nu_M165',
                                  'VBFHToWWTo2L2Nu_M170',
                                  'VBFHToWWTo2L2Nu_M175',
                                  'VBFHToWWTo2L2Nu_M180',
                                  'VBFHToWWTo2L2Nu_M190',
                                  'VBFHToWWTo2L2Nu_M200',
                                  'VBFHToWWTo2L2Nu_M210',
                                  'VBFHToWWTo2L2Nu_M230',
                                  'VBFHToWWTo2L2Nu_M250',
                                  'VBFHToWWTo2L2Nu_M270',
                                  'VBFHToWWTo2L2Nu_M300',
                                  'VBFHToWWTo2L2Nu_M350',
                                  'VBFHToWWTo2L2Nu_M400',
                                  'VBFHToWWTo2L2Nu_M450',
                                  'VBFHToWWTo2L2Nu_M500',
                                  'VBFHToWWTo2L2Nu_M550',
                                  'VBFHToWWTo2L2Nu_M600',
                                  'VBFHToWWTo2L2Nu_M650',
                                  'VBFHToWWTo2L2Nu_M700',
                                  'VBFHToWWTo2L2Nu_M750',
                                  'VBFHToWWTo2L2Nu_M750_NWA',
                                  'VBFHToWWTo2L2Nu_M800',
                                  'VBFHToWWTo2L2Nu_M900',
                                  'VBFHToWWTo2L2Nu_M1000',
                                 ] ,
                },

  'JESMaxdo'     :  {
                  'isChain'    : True ,
                  'do4MC'      : True ,
                  'do4Data'    : False,
                  'subTargets' : ['do_JESMaxdo','bPogSF','l2kin','l3kin'],
                  'onlySample' : [
                                  # DY 
                                  'DYJetsToLL_M-10to50','DYJetsToLL_M-50','DYJetsToLL_M-10to50ext3','DYJetsToLL_M-50-LO',
                                  'DY2JetsToLL', 'DY3JetsToLL', 'DY4JetsToLL',
                                  'DYJetsToLL_M-50_HT-100to200_MLM' , 'DYJetsToLL_M-50_HT-100to200_MLM_ext' , 
                                  'DYJetsToLL_M-50_HT-200to400_MLM' , 
                                  'DYJetsToLL_M-50_HT-400to600_MLM' ,
                                  'DYJetsToLL_M-50_HT-600toInf_MLM' ,
                                  # Top
                                  'TTTo2L2Nu','TT',
                                  'ST_t-channel_antitop','ST_t-channel_top',
                                  'ST_tW_antitop','ST_tW_top',
                                  # VV (including WW) 
                                  'WWTo2L2Nu','GluGluWWTo2L2Nu_MCFM','GluGluWWTo2L2NuHiggs_MCFM',
                                  'WZTo3LNu',
                                  'ZZ','Zg',
                                  'ZZTo2L2Nu','ZZTo2L2Q','ZZTo4L',
                                  'Wg_AMCNLOFXFX','WgStarLNuEE','WgStarLNuMuMu',
                                  'Wg_MADGRAPHMLM',
                                  # VVV
                                  'WZZ','ZZZ','WWZ',
                                  # Higgs 
                                  'GluGluHToTauTau_M125', 'GluGluHToWWTo2L2Nu_M125','GluGluHToWWTo2L2NuPowheg_M125',
                                  'GluGluHToWWTo2L2Nu_alternative_M125','VBFHToWWTo2L2Nu_alternative_M125',
                                  'HWminusJ_HToTauTau_M125', 'HWminusJ_HToWW_M125',
                                  'HWplusJ_HToTauTau_M125', 'HWplusJ_HToWW_M125',
                                  'HZJ_HToTauTau_M125', 'HZJ_HToWW_M125',
                                  'VBFHToTauTau_M125', 'VBFHToWWTo2L2Nu_M125',
                                  'ggZH_HToWW_M125', # missing ggZHToTauTau
                                  'ttHJetToNonbb_M125','TTWJetsToLNu',
                                  # ... ggH High Mass
                                  'GluGluHToWWTo2L2Nu_M130',
                                  'GluGluHToWWTo2L2Nu_M135',
                                  'GluGluHToWWTo2L2Nu_M140',
                                  'GluGluHToWWTo2L2Nu_M145',
                                  'GluGluHToWWTo2L2Nu_M150',
                                  'GluGluHToWWTo2L2Nu_M155',
                                  'GluGluHToWWTo2L2Nu_M160',
                                  'GluGluHToWWTo2L2Nu_M165',
                                  'GluGluHToWWTo2L2Nu_M170',
                                  'GluGluHToWWTo2L2Nu_M175',
                                  'GluGluHToWWTo2L2Nu_M180',
                                  'GluGluHToWWTo2L2Nu_M190',
                                  'GluGluHToWWTo2L2Nu_M200',
                                  'GluGluHToWWTo2L2Nu_M210',
                                  'GluGluHToWWTo2L2Nu_M230',
                                  'GluGluHToWWTo2L2Nu_M250',
                                  'GluGluHToWWTo2L2Nu_M270',
                                  'GluGluHToWWTo2L2Nu_M300',
                                  'GluGluHToWWTo2L2Nu_M350',
                                  'GluGluHToWWTo2L2Nu_M400',
                                  'GluGluHToWWTo2L2Nu_M450',
                                  'GluGluHToWWTo2L2Nu_M500',
                                  'GluGluHToWWTo2L2Nu_M550',
                                  'GluGluHToWWTo2L2Nu_M600',
                                  'GluGluHToWWTo2L2Nu_M650',
                                  'GluGluHToWWTo2L2Nu_M700',
                                  'GluGluHToWWTo2L2Nu_M750',
                                  'GluGluHToWWTo2L2Nu_M750_NWA',
                                  'GluGluHToWWTo2L2Nu_M800',
                                  'GluGluHToWWTo2L2Nu_M900',
                                  'GluGluHToWWTo2L2Nu_M1000',
                                  # ... VBF High Mass
                                  'VBFHToWWTo2L2Nu_M130',
                                  'VBFHToWWTo2L2Nu_M135',
                                  'VBFHToWWTo2L2Nu_M140',
                                  'VBFHToWWTo2L2Nu_M145',
                                  'VBFHToWWTo2L2Nu_M150',
                                  'VBFHToWWTo2L2Nu_M155',
                                  'VBFHToWWTo2L2Nu_M160',
                                  'VBFHToWWTo2L2Nu_M165',
                                  'VBFHToWWTo2L2Nu_M170',
                                  'VBFHToWWTo2L2Nu_M175',
                                  'VBFHToWWTo2L2Nu_M180',
                                  'VBFHToWWTo2L2Nu_M190',
                                  'VBFHToWWTo2L2Nu_M200',
                                  'VBFHToWWTo2L2Nu_M210',
                                  'VBFHToWWTo2L2Nu_M230',
                                  'VBFHToWWTo2L2Nu_M250',
                                  'VBFHToWWTo2L2Nu_M270',
                                  'VBFHToWWTo2L2Nu_M300',
                                  'VBFHToWWTo2L2Nu_M350',
                                  'VBFHToWWTo2L2Nu_M400',
                                  'VBFHToWWTo2L2Nu_M450',
                                  'VBFHToWWTo2L2Nu_M500',
                                  'VBFHToWWTo2L2Nu_M550',
                                  'VBFHToWWTo2L2Nu_M600',
                                  'VBFHToWWTo2L2Nu_M650',
                                  'VBFHToWWTo2L2Nu_M700',
                                  'VBFHToWWTo2L2Nu_M750',
                                  'VBFHToWWTo2L2Nu_M750_NWA',
                                  'VBFHToWWTo2L2Nu_M800',
                                  'VBFHToWWTo2L2Nu_M900',
                                  'VBFHToWWTo2L2Nu_M1000',
                                 ] ,
                },

  'lpTCorr' : {
                 'isChain'    : True ,
                  'do4MC'      : True ,
                  'do4Data'    : False,
                  'subTargets' : ['do_lpTCorrMC','do_lpTCorrData','l2kin','l3kin'],
               },



  'LepElepTup':  {
                  'isChain'    : True ,
                  'do4MC'      : True ,
                  'do4Data'    : False,
                  'subTargets' : ['do_LepElepTup','TrigEff','IdIsoSC','l2kin','l3kin'],
                  'onlySample' : [
                                  # DY 
                                  'DYJetsToLL_M-10to50','DYJetsToLL_M-50','DYJetsToLL_M-10to50ext3','DYJetsToLL_M-50-LO',
                                  'DY2JetsToLL', 'DY3JetsToLL', 'DY4JetsToLL',
                                  'DYJetsToLL_M-50_HT-100to200_MLM' , 'DYJetsToLL_M-50_HT-100to200_MLM_ext' , 
                                  'DYJetsToLL_M-50_HT-200to400_MLM' , 
                                  'DYJetsToLL_M-50_HT-400to600_MLM' ,
                                  'DYJetsToLL_M-50_HT-600toInf_MLM' ,
                                  # Top
                                  'TTTo2L2Nu','TT',
                                  'ST_t-channel_antitop','ST_t-channel_top',
                                  'ST_tW_antitop','ST_tW_top',
                                  # VV (including WW) 
                                  'WWTo2L2Nu','GluGluWWTo2L2Nu_MCFM','GluGluWWTo2L2NuHiggs_MCFM','GluGluHToWWTo2L2NuPowheg_M125',
                                  'WZTo3LNu',
                                  'ZZ','Zg',
                                  'ZZTo2L2Nu','ZZTo2L2Q','ZZTo4L',
                                  'Wg_AMCNLOFXFX','WgStarLNuEE','WgStarLNuMuMu',
                                  'Wg_MADGRAPHMLM',
                                  # VVV
                                  'WZZ','ZZZ','WWZ','WWW',
                                  # Higgs 
                                  'GluGluHToTauTau_M125', 'GluGluHToWWTo2L2Nu_M125','GluGluHToWWTo2L2NuPowheg_M125',
                                  'GluGluHToWWTo2L2Nu_alternative_M125','VBFHToWWTo2L2Nu_alternative_M125',
                                  'HWminusJ_HToTauTau_M125', 'HWminusJ_HToWW_M125',
                                  'HWplusJ_HToTauTau_M125', 'HWplusJ_HToWW_M125',
                                  'HZJ_HToTauTau_M125', 'HZJ_HToWW_M125',
                                  'VBFHToTauTau_M125', 'VBFHToWWTo2L2Nu_M125',
                                  'ggZH_HToWW_M125', # missing ggZHToTauTau
                                  'ttHJetToNonbb_M125','TTWJetsToLNu',
                                  # ... ggH High Mass
                                  'GluGluHToWWTo2L2Nu_M130',
                                  'GluGluHToWWTo2L2Nu_M135',
                                  'GluGluHToWWTo2L2Nu_M140',
                                  'GluGluHToWWTo2L2Nu_M145',
                                  'GluGluHToWWTo2L2Nu_M150',
                                  'GluGluHToWWTo2L2Nu_M155',
                                  'GluGluHToWWTo2L2Nu_M160',
                                  'GluGluHToWWTo2L2Nu_M165',
                                  'GluGluHToWWTo2L2Nu_M170',
                                  'GluGluHToWWTo2L2Nu_M175',
                                  'GluGluHToWWTo2L2Nu_M180',
                                  'GluGluHToWWTo2L2Nu_M190',
                                  'GluGluHToWWTo2L2Nu_M200',
                                  'GluGluHToWWTo2L2Nu_M210',
                                  'GluGluHToWWTo2L2Nu_M230',
                                  'GluGluHToWWTo2L2Nu_M250',
                                  'GluGluHToWWTo2L2Nu_M270',
                                  'GluGluHToWWTo2L2Nu_M300',
                                  'GluGluHToWWTo2L2Nu_M350',
                                  'GluGluHToWWTo2L2Nu_M400',
                                  'GluGluHToWWTo2L2Nu_M450',
                                  'GluGluHToWWTo2L2Nu_M500',
                                  'GluGluHToWWTo2L2Nu_M550',
                                  'GluGluHToWWTo2L2Nu_M600',
                                  'GluGluHToWWTo2L2Nu_M650',
                                  'GluGluHToWWTo2L2Nu_M700',
                                  'GluGluHToWWTo2L2Nu_M750',
                                  'GluGluHToWWTo2L2Nu_M750_NWA',
                                  'GluGluHToWWTo2L2Nu_M800',
                                  'GluGluHToWWTo2L2Nu_M900',
                                  'GluGluHToWWTo2L2Nu_M1000',
                                  # ... VBF High Mass
                                  'VBFHToWWTo2L2Nu_M130',
                                  'VBFHToWWTo2L2Nu_M135',
                                  'VBFHToWWTo2L2Nu_M140',
                                  'VBFHToWWTo2L2Nu_M145',
                                  'VBFHToWWTo2L2Nu_M150',
                                  'VBFHToWWTo2L2Nu_M155',
                                  'VBFHToWWTo2L2Nu_M160',
                                  'VBFHToWWTo2L2Nu_M165',
                                  'VBFHToWWTo2L2Nu_M170',
                                  'VBFHToWWTo2L2Nu_M175',
                                  'VBFHToWWTo2L2Nu_M180',
                                  'VBFHToWWTo2L2Nu_M190',
                                  'VBFHToWWTo2L2Nu_M200',
                                  'VBFHToWWTo2L2Nu_M210',
                                  'VBFHToWWTo2L2Nu_M230',
                                  'VBFHToWWTo2L2Nu_M250',
                                  'VBFHToWWTo2L2Nu_M270',
                                  'VBFHToWWTo2L2Nu_M300',
                                  'VBFHToWWTo2L2Nu_M350',
                                  'VBFHToWWTo2L2Nu_M400',
                                  'VBFHToWWTo2L2Nu_M450',
                                  'VBFHToWWTo2L2Nu_M500',
                                  'VBFHToWWTo2L2Nu_M550',
                                  'VBFHToWWTo2L2Nu_M600',
                                  'VBFHToWWTo2L2Nu_M650',
                                  'VBFHToWWTo2L2Nu_M700',
                                  'VBFHToWWTo2L2Nu_M750',
                                  'VBFHToWWTo2L2Nu_M750_NWA',
                                  'VBFHToWWTo2L2Nu_M800',
                                  'VBFHToWWTo2L2Nu_M900',
                                  'VBFHToWWTo2L2Nu_M1000',
                                 ] ,
              },

  'LepElepTdo':  {
                  'isChain'    : True ,
                  'do4MC'      : True ,
                  'do4Data'    : False,
                  'subTargets' : ['do_LepElepTdo','TrigEff','IdIsoSC','l2kin','l3kin'],
                  'onlySample' : [
                                  # DY 
                                  'DYJetsToLL_M-10to50','DYJetsToLL_M-50','DYJetsToLL_M-10to50ext3','DYJetsToLL_M-50-LO',
                                  'DY2JetsToLL', 'DY3JetsToLL', 'DY4JetsToLL',
                                  'DYJetsToLL_M-50_HT-100to200_MLM' , 'DYJetsToLL_M-50_HT-100to200_MLM_ext' , 
                                  'DYJetsToLL_M-50_HT-200to400_MLM' , 
                                  'DYJetsToLL_M-50_HT-400to600_MLM' ,
                                  'DYJetsToLL_M-50_HT-600toInf_MLM' ,
                                  # Top
                                  'TTTo2L2Nu','TT',
                                  'ST_t-channel_antitop','ST_t-channel_top',
                                  'ST_tW_antitop','ST_tW_top',
                                  # VV (including WW) 
                                  'WWTo2L2Nu','GluGluWWTo2L2Nu_MCFM','GluGluWWTo2L2NuHiggs_MCFM',
                                  'WZTo3LNu',
                                  'ZZ','Zg',
                                  'ZZTo2L2Nu','ZZTo2L2Q','ZZTo4L',
                                  'Wg_AMCNLOFXFX','WgStarLNuEE','WgStarLNuMuMu',
                                  'Wg_MADGRAPHMLM',
                                  # VVV
                                  'WZZ','ZZZ','WWZ','WWW',
                                  # Higgs 
                                  'GluGluHToTauTau_M125', 'GluGluHToWWTo2L2Nu_M125','GluGluHToWWTo2L2NuPowheg_M125',
                                  'GluGluHToWWTo2L2Nu_alternative_M125','VBFHToWWTo2L2Nu_alternative_M125',
                                  'HWminusJ_HToTauTau_M125', 'HWminusJ_HToWW_M125',
                                  'HWplusJ_HToTauTau_M125', 'HWplusJ_HToWW_M125',
                                  'HZJ_HToTauTau_M125', 'HZJ_HToWW_M125',
                                  'VBFHToTauTau_M125', 'VBFHToWWTo2L2Nu_M125',
                                  'ggZH_HToWW_M125', # missing ggZHToTauTau
                                  'ttHJetToNonbb_M125','TTWJetsToLNu',

                                  # ... ggH High Mass
                                  'GluGluHToWWTo2L2Nu_M130',
                                  'GluGluHToWWTo2L2Nu_M135',
                                  'GluGluHToWWTo2L2Nu_M140',
                                  'GluGluHToWWTo2L2Nu_M145',
                                  'GluGluHToWWTo2L2Nu_M150',
                                  'GluGluHToWWTo2L2Nu_M155',
                                  'GluGluHToWWTo2L2Nu_M160',
                                  'GluGluHToWWTo2L2Nu_M165',
                                  'GluGluHToWWTo2L2Nu_M170',
                                  'GluGluHToWWTo2L2Nu_M175',
                                  'GluGluHToWWTo2L2Nu_M180',
                                  'GluGluHToWWTo2L2Nu_M190',
                                  'GluGluHToWWTo2L2Nu_M200',
                                  'GluGluHToWWTo2L2Nu_M210',
                                  'GluGluHToWWTo2L2Nu_M230',
                                  'GluGluHToWWTo2L2Nu_M250',
                                  'GluGluHToWWTo2L2Nu_M270',
                                  'GluGluHToWWTo2L2Nu_M300',
                                  'GluGluHToWWTo2L2Nu_M350',
                                  'GluGluHToWWTo2L2Nu_M400',
                                  'GluGluHToWWTo2L2Nu_M450',
                                  'GluGluHToWWTo2L2Nu_M500',
                                  'GluGluHToWWTo2L2Nu_M550',
                                  'GluGluHToWWTo2L2Nu_M600',
                                  'GluGluHToWWTo2L2Nu_M650',
                                  'GluGluHToWWTo2L2Nu_M700',
                                  'GluGluHToWWTo2L2Nu_M750',
                                  'GluGluHToWWTo2L2Nu_M750_NWA',
                                  'GluGluHToWWTo2L2Nu_M800',
                                  'GluGluHToWWTo2L2Nu_M900',
                                  'GluGluHToWWTo2L2Nu_M1000',
                                  # ... VBF High Mass
                                  'VBFHToWWTo2L2Nu_M130',
                                  'VBFHToWWTo2L2Nu_M135',
                                  'VBFHToWWTo2L2Nu_M140',
                                  'VBFHToWWTo2L2Nu_M145',
                                  'VBFHToWWTo2L2Nu_M150',
                                  'VBFHToWWTo2L2Nu_M155',
                                  'VBFHToWWTo2L2Nu_M160',
                                  'VBFHToWWTo2L2Nu_M165',
                                  'VBFHToWWTo2L2Nu_M170',
                                  'VBFHToWWTo2L2Nu_M175',
                                  'VBFHToWWTo2L2Nu_M180',
                                  'VBFHToWWTo2L2Nu_M190',
                                  'VBFHToWWTo2L2Nu_M200',
                                  'VBFHToWWTo2L2Nu_M210',
                                  'VBFHToWWTo2L2Nu_M230',
                                  'VBFHToWWTo2L2Nu_M250',
                                  'VBFHToWWTo2L2Nu_M270',
                                  'VBFHToWWTo2L2Nu_M300',
                                  'VBFHToWWTo2L2Nu_M350',
                                  'VBFHToWWTo2L2Nu_M400',
                                  'VBFHToWWTo2L2Nu_M450',
                                  'VBFHToWWTo2L2Nu_M500',
                                  'VBFHToWWTo2L2Nu_M550',
                                  'VBFHToWWTo2L2Nu_M600',
                                  'VBFHToWWTo2L2Nu_M650',
                                  'VBFHToWWTo2L2Nu_M700',
                                  'VBFHToWWTo2L2Nu_M750',
                                  'VBFHToWWTo2L2Nu_M750_NWA',
                                  'VBFHToWWTo2L2Nu_M800',
                                  'VBFHToWWTo2L2Nu_M900',
                                  'VBFHToWWTo2L2Nu_M1000',
                                 ] ,
              },


  'LepMupTup':  {
                  'isChain'    : True ,
                  'do4MC'      : True ,
                  'do4Data'    : False,
                  'subTargets' : ['do_LepMupTup','TrigEff','IdIsoSC','l2kin','l3kin'],
                  'onlySample' : [
                                  # DY 
                                  'DYJetsToLL_M-10to50','DYJetsToLL_M-50','DYJetsToLL_M-10to50ext3','DYJetsToLL_M-50-LO',
                                  'DY2JetsToLL', 'DY3JetsToLL', 'DY4JetsToLL',
                                  'DYJetsToLL_M-50_HT-100to200_MLM' , 'DYJetsToLL_M-50_HT-100to200_MLM_ext' , 
                                  'DYJetsToLL_M-50_HT-200to400_MLM' , 
                                  'DYJetsToLL_M-50_HT-400to600_MLM' ,
                                  'DYJetsToLL_M-50_HT-600toInf_MLM' ,
                                  # Top
                                  'TTTo2L2Nu','TT',
                                  'ST_t-channel_antitop','ST_t-channel_top',
                                  'ST_tW_antitop','ST_tW_top',
                                  # VV (including WW) 
                                  'WWTo2L2Nu','GluGluWWTo2L2Nu_MCFM','GluGluWWTo2L2NuHiggs_MCFM',
                                  'WZTo3LNu',
                                  'ZZ','Zg',
                                  'ZZTo2L2Nu','ZZTo2L2Q','ZZTo4L',
                                  'Wg_AMCNLOFXFX','WgStarLNuEE','WgStarLNuMuMu',
                                  'Wg_MADGRAPHMLM',
                                  # VVV
                                  'WZZ','ZZZ','WWZ','WWW',
                                  # Higgs 
                                  'GluGluHToTauTau_M125', 'GluGluHToWWTo2L2Nu_M125','GluGluHToWWTo2L2NuPowheg_M125',
                                  'GluGluHToWWTo2L2Nu_alternative_M125','VBFHToWWTo2L2Nu_alternative_M125',
                                  'HWminusJ_HToTauTau_M125', 'HWminusJ_HToWW_M125',
                                  'HWplusJ_HToTauTau_M125', 'HWplusJ_HToWW_M125',
                                  'HZJ_HToTauTau_M125', 'HZJ_HToWW_M125',
                                  'VBFHToTauTau_M125', 'VBFHToWWTo2L2Nu_M125',
                                  'ggZH_HToWW_M125', # missing ggZHToTauTau
                                  'ttHJetToNonbb_M125','TTWJetsToLNu',

                                  # ... ggH High Mass
                                  'GluGluHToWWTo2L2Nu_M130',
                                  'GluGluHToWWTo2L2Nu_M135',
                                  'GluGluHToWWTo2L2Nu_M140',
                                  'GluGluHToWWTo2L2Nu_M145',
                                  'GluGluHToWWTo2L2Nu_M150',
                                  'GluGluHToWWTo2L2Nu_M155',
                                  'GluGluHToWWTo2L2Nu_M160',
                                  'GluGluHToWWTo2L2Nu_M165',
                                  'GluGluHToWWTo2L2Nu_M170',
                                  'GluGluHToWWTo2L2Nu_M175',
                                  'GluGluHToWWTo2L2Nu_M180',
                                  'GluGluHToWWTo2L2Nu_M190',
                                  'GluGluHToWWTo2L2Nu_M200',
                                  'GluGluHToWWTo2L2Nu_M210',
                                  'GluGluHToWWTo2L2Nu_M230',
                                  'GluGluHToWWTo2L2Nu_M250',
                                  'GluGluHToWWTo2L2Nu_M270',
                                  'GluGluHToWWTo2L2Nu_M300',
                                  'GluGluHToWWTo2L2Nu_M350',
                                  'GluGluHToWWTo2L2Nu_M400',
                                  'GluGluHToWWTo2L2Nu_M450',
                                  'GluGluHToWWTo2L2Nu_M500',
                                  'GluGluHToWWTo2L2Nu_M550',
                                  'GluGluHToWWTo2L2Nu_M600',
                                  'GluGluHToWWTo2L2Nu_M650',
                                  'GluGluHToWWTo2L2Nu_M700',
                                  'GluGluHToWWTo2L2Nu_M750',
                                  'GluGluHToWWTo2L2Nu_M750_NWA',
                                  'GluGluHToWWTo2L2Nu_M800',
                                  'GluGluHToWWTo2L2Nu_M900',
                                  'GluGluHToWWTo2L2Nu_M1000',
                                  # ... VBF High Mass
                                  'VBFHToWWTo2L2Nu_M130',
                                  'VBFHToWWTo2L2Nu_M135',
                                  'VBFHToWWTo2L2Nu_M140',
                                  'VBFHToWWTo2L2Nu_M145',
                                  'VBFHToWWTo2L2Nu_M150',
                                  'VBFHToWWTo2L2Nu_M155',
                                  'VBFHToWWTo2L2Nu_M160',
                                  'VBFHToWWTo2L2Nu_M165',
                                  'VBFHToWWTo2L2Nu_M170',
                                  'VBFHToWWTo2L2Nu_M175',
                                  'VBFHToWWTo2L2Nu_M180',
                                  'VBFHToWWTo2L2Nu_M190',
                                  'VBFHToWWTo2L2Nu_M200',
                                  'VBFHToWWTo2L2Nu_M210',
                                  'VBFHToWWTo2L2Nu_M230',
                                  'VBFHToWWTo2L2Nu_M250',
                                  'VBFHToWWTo2L2Nu_M270',
                                  'VBFHToWWTo2L2Nu_M300',
                                  'VBFHToWWTo2L2Nu_M350',
                                  'VBFHToWWTo2L2Nu_M400',
                                  'VBFHToWWTo2L2Nu_M450',
                                  'VBFHToWWTo2L2Nu_M500',
                                  'VBFHToWWTo2L2Nu_M550',
                                  'VBFHToWWTo2L2Nu_M600',
                                  'VBFHToWWTo2L2Nu_M650',
                                  'VBFHToWWTo2L2Nu_M700',
                                  'VBFHToWWTo2L2Nu_M750',
                                  'VBFHToWWTo2L2Nu_M750_NWA',
                                  'VBFHToWWTo2L2Nu_M800',
                                  'VBFHToWWTo2L2Nu_M900',
                                  'VBFHToWWTo2L2Nu_M1000',
                                 ] ,
              },

  'LepMupTdo':  {
                  'isChain'    : True ,
                  'do4MC'      : True ,
                  'do4Data'    : False,
                  'subTargets' : ['do_LepMupTdo','TrigEff','IdIsoSC','l2kin','l3kin'],
                  'onlySample' : [
                                  # DY 
                                  'DYJetsToLL_M-10to50','DYJetsToLL_M-50','DYJetsToLL_M-10to50ext3','DYJetsToLL_M-50-LO',
                                  'DY2JetsToLL', 'DY3JetsToLL', 'DY4JetsToLL',
                                  'DYJetsToLL_M-50_HT-100to200_MLM' , 'DYJetsToLL_M-50_HT-100to200_MLM_ext' , 
                                  'DYJetsToLL_M-50_HT-200to400_MLM' , 
                                  'DYJetsToLL_M-50_HT-400to600_MLM' ,
                                  'DYJetsToLL_M-50_HT-600toInf_MLM' ,
                                  # Top
                                  'TTTo2L2Nu','TT',
                                  'ST_t-channel_antitop','ST_t-channel_top',
                                  'ST_tW_antitop','ST_tW_top',
                                  # VV (including WW) 
                                  'WWTo2L2Nu','GluGluWWTo2L2Nu_MCFM','GluGluWWTo2L2NuHiggs_MCFM',
                                  'GluGluHToWWTo2L2Nu_alternative_M125','VBFHToWWTo2L2Nu_alternative_M125',
                                  'WZTo3LNu',
                                  'ZZ','Zg',
                                  'ZZTo2L2Nu','ZZTo2L2Q','ZZTo4L',
                                  'Wg_AMCNLOFXFX','WgStarLNuEE','WgStarLNuMuMu',
                                  'Wg_MADGRAPHMLM',
                                  # VVV
                                  'WZZ','ZZZ','WWZ','WWW',
                                  # Higgs 
                                  'GluGluHToTauTau_M125', 'GluGluHToWWTo2L2Nu_M125','GluGluHToWWTo2L2NuPowheg_M125',
                                  'GluGluHToWWTo2L2Nu_alternative_M125','VBFHToWWTo2L2Nu_alternative_M125',
                                  'HWminusJ_HToTauTau_M125', 'HWminusJ_HToWW_M125',
                                  'HWplusJ_HToTauTau_M125', 'HWplusJ_HToWW_M125',
                                  'HZJ_HToTauTau_M125', 'HZJ_HToWW_M125',
                                  'VBFHToTauTau_M125', 'VBFHToWWTo2L2Nu_M125',
                                  'ggZH_HToWW_M125', # missing ggZHToTauTau
                                  'ttHJetToNonbb_M125','TTWJetsToLNu',
                                  # ... ggH High Mass
                                  'GluGluHToWWTo2L2Nu_M130',
                                  'GluGluHToWWTo2L2Nu_M135',
                                  'GluGluHToWWTo2L2Nu_M140',
                                  'GluGluHToWWTo2L2Nu_M145',
                                  'GluGluHToWWTo2L2Nu_M150',
                                  'GluGluHToWWTo2L2Nu_M155',
                                  'GluGluHToWWTo2L2Nu_M160',
                                  'GluGluHToWWTo2L2Nu_M165',
                                  'GluGluHToWWTo2L2Nu_M170',
                                  'GluGluHToWWTo2L2Nu_M175',
                                  'GluGluHToWWTo2L2Nu_M180',
                                  'GluGluHToWWTo2L2Nu_M190',
                                  'GluGluHToWWTo2L2Nu_M200',
                                  'GluGluHToWWTo2L2Nu_M210',
                                  'GluGluHToWWTo2L2Nu_M230',
                                  'GluGluHToWWTo2L2Nu_M250',
                                  'GluGluHToWWTo2L2Nu_M270',
                                  'GluGluHToWWTo2L2Nu_M300',
                                  'GluGluHToWWTo2L2Nu_M350',
                                  'GluGluHToWWTo2L2Nu_M400',
                                  'GluGluHToWWTo2L2Nu_M450',
                                  'GluGluHToWWTo2L2Nu_M500',
                                  'GluGluHToWWTo2L2Nu_M550',
                                  'GluGluHToWWTo2L2Nu_M600',
                                  'GluGluHToWWTo2L2Nu_M650',
                                  'GluGluHToWWTo2L2Nu_M700',
                                  'GluGluHToWWTo2L2Nu_M750',
                                  'GluGluHToWWTo2L2Nu_M750_NWA',
                                  'GluGluHToWWTo2L2Nu_M800',
                                  'GluGluHToWWTo2L2Nu_M900',
                                  'GluGluHToWWTo2L2Nu_M1000',
                                  # ... VBF High Mass
                                  'VBFHToWWTo2L2Nu_M130',
                                  'VBFHToWWTo2L2Nu_M135',
                                  'VBFHToWWTo2L2Nu_M140',
                                  'VBFHToWWTo2L2Nu_M145',
                                  'VBFHToWWTo2L2Nu_M150',
                                  'VBFHToWWTo2L2Nu_M155',
                                  'VBFHToWWTo2L2Nu_M160',
                                  'VBFHToWWTo2L2Nu_M165',
                                  'VBFHToWWTo2L2Nu_M170',
                                  'VBFHToWWTo2L2Nu_M175',
                                  'VBFHToWWTo2L2Nu_M180',
                                  'VBFHToWWTo2L2Nu_M190',
                                  'VBFHToWWTo2L2Nu_M200',
                                  'VBFHToWWTo2L2Nu_M210',
                                  'VBFHToWWTo2L2Nu_M230',
                                  'VBFHToWWTo2L2Nu_M250',
                                  'VBFHToWWTo2L2Nu_M270',
                                  'VBFHToWWTo2L2Nu_M300',
                                  'VBFHToWWTo2L2Nu_M350',
                                  'VBFHToWWTo2L2Nu_M400',
                                  'VBFHToWWTo2L2Nu_M450',
                                  'VBFHToWWTo2L2Nu_M500',
                                  'VBFHToWWTo2L2Nu_M550',
                                  'VBFHToWWTo2L2Nu_M600',
                                  'VBFHToWWTo2L2Nu_M650',
                                  'VBFHToWWTo2L2Nu_M700',
                                  'VBFHToWWTo2L2Nu_M750',
                                  'VBFHToWWTo2L2Nu_M750_NWA',
                                  'VBFHToWWTo2L2Nu_M800',
                                  'VBFHToWWTo2L2Nu_M900',
                                  'VBFHToWWTo2L2Nu_M1000',
                                 ] ,
              },
                  
                  

   'METup':  {
                  'isChain'    : True ,
                  'do4MC'      : True ,
                  'do4Data'    : False,
                  'subTargets' : ['do_METup','l2kin','l3kin'],
                  'onlySample' : [
                                  # DY 
                                  'DYJetsToLL_M-10to50','DYJetsToLL_M-50','DYJetsToLL_M-10to50ext3','DYJetsToLL_M-50-LO',
                                  'DY2JetsToLL', 'DY3JetsToLL', 'DY4JetsToLL',
                                  'DYJetsToLL_M-50_HT-100to200_MLM' , 'DYJetsToLL_M-50_HT-100to200_MLM_ext' , 
                                  'DYJetsToLL_M-50_HT-200to400_MLM' , 
                                  'DYJetsToLL_M-50_HT-400to600_MLM' ,
                                  'DYJetsToLL_M-50_HT-600toInf_MLM' ,
                                  # Top
                                  'TTTo2L2Nu','TT',
                                  'ST_t-channel_antitop','ST_t-channel_top',
                                  'ST_tW_antitop','ST_tW_top',
                                  # VV (including WW) 
                                  'WWTo2L2Nu','GluGluWWTo2L2Nu_MCFM','GluGluWWTo2L2NuHiggs_MCFM',
                                  'WZTo3LNu',
                                  'ZZ','Zg',
                                  'ZZTo2L2Nu','ZZTo2L2Q','ZZTo4L',
                                  'Wg_AMCNLOFXFX','WgStarLNuEE','WgStarLNuMuMu',
                                  'Wg_MADGRAPHMLM',
                                  # VVV
                                  'WZZ','ZZZ','WWZ','WWW',
                                  # Higgs 
                                  'GluGluHToTauTau_M125', 'GluGluHToWWTo2L2Nu_M125','GluGluHToWWTo2L2NuPowheg_M125',
                                  'GluGluHToWWTo2L2Nu_alternative_M125','VBFHToWWTo2L2Nu_alternative_M125',
                                  'HWminusJ_HToTauTau_M125', 'HWminusJ_HToWW_M125',
                                  'HWplusJ_HToTauTau_M125', 'HWplusJ_HToWW_M125',
                                  'HZJ_HToTauTau_M125', 'HZJ_HToWW_M125',
                                  'VBFHToTauTau_M125', 'VBFHToWWTo2L2Nu_M125',
                                  'ggZH_HToWW_M125', # missing ggZHToTauTau
                                  'ttHJetToNonbb_M125','TTWJetsToLNu',
                                  # ... ggH High Mass
                                  'GluGluHToWWTo2L2Nu_M130',
                                  'GluGluHToWWTo2L2Nu_M135',
                                  'GluGluHToWWTo2L2Nu_M140',
                                  'GluGluHToWWTo2L2Nu_M145',
                                  'GluGluHToWWTo2L2Nu_M150',
                                  'GluGluHToWWTo2L2Nu_M155',
                                  'GluGluHToWWTo2L2Nu_M160',
                                  'GluGluHToWWTo2L2Nu_M165',
                                  'GluGluHToWWTo2L2Nu_M170',
                                  'GluGluHToWWTo2L2Nu_M175',
                                  'GluGluHToWWTo2L2Nu_M180',
                                  'GluGluHToWWTo2L2Nu_M190',
                                  'GluGluHToWWTo2L2Nu_M200',
                                  'GluGluHToWWTo2L2Nu_M210',
                                  'GluGluHToWWTo2L2Nu_M230',
                                  'GluGluHToWWTo2L2Nu_M250',
                                  'GluGluHToWWTo2L2Nu_M270',
                                  'GluGluHToWWTo2L2Nu_M300',
                                  'GluGluHToWWTo2L2Nu_M350',
                                  'GluGluHToWWTo2L2Nu_M400',
                                  'GluGluHToWWTo2L2Nu_M450',
                                  'GluGluHToWWTo2L2Nu_M500',
                                  'GluGluHToWWTo2L2Nu_M550',
                                  'GluGluHToWWTo2L2Nu_M600',
                                  'GluGluHToWWTo2L2Nu_M650',
                                  'GluGluHToWWTo2L2Nu_M700',
                                  'GluGluHToWWTo2L2Nu_M750',
                                  'GluGluHToWWTo2L2Nu_M750_NWA',
                                  'GluGluHToWWTo2L2Nu_M800',
                                  'GluGluHToWWTo2L2Nu_M900',
                                  'GluGluHToWWTo2L2Nu_M1000',
                                  # ... VBF High Mass
                                  'VBFHToWWTo2L2Nu_M130',
                                  'VBFHToWWTo2L2Nu_M135',
                                  'VBFHToWWTo2L2Nu_M140',
                                  'VBFHToWWTo2L2Nu_M145',
                                  'VBFHToWWTo2L2Nu_M150',
                                  'VBFHToWWTo2L2Nu_M155',
                                  'VBFHToWWTo2L2Nu_M160',
                                  'VBFHToWWTo2L2Nu_M165',
                                  'VBFHToWWTo2L2Nu_M170',
                                  'VBFHToWWTo2L2Nu_M175',
                                  'VBFHToWWTo2L2Nu_M180',
                                  'VBFHToWWTo2L2Nu_M190',
                                  'VBFHToWWTo2L2Nu_M200',
                                  'VBFHToWWTo2L2Nu_M210',
                                  'VBFHToWWTo2L2Nu_M230',
                                  'VBFHToWWTo2L2Nu_M250',
                                  'VBFHToWWTo2L2Nu_M270',
                                  'VBFHToWWTo2L2Nu_M300',
                                  'VBFHToWWTo2L2Nu_M350',
                                  'VBFHToWWTo2L2Nu_M400',
                                  'VBFHToWWTo2L2Nu_M450',
                                  'VBFHToWWTo2L2Nu_M500',
                                  'VBFHToWWTo2L2Nu_M550',
                                  'VBFHToWWTo2L2Nu_M600',
                                  'VBFHToWWTo2L2Nu_M650',
                                  'VBFHToWWTo2L2Nu_M700',
                                  'VBFHToWWTo2L2Nu_M750',
                                  'VBFHToWWTo2L2Nu_M750_NWA',
                                  'VBFHToWWTo2L2Nu_M800',
                                  'VBFHToWWTo2L2Nu_M900',
                                  'VBFHToWWTo2L2Nu_M1000',
                                 ] ,
              },

   'METdo':  {
                  'isChain'    : True ,
                  'do4MC'      : True ,
                  'do4Data'    : False,
                  'subTargets' : ['do_METdo','l2kin','l3kin'],
                  'onlySample' : [
                                  # DY 
                                  'DYJetsToLL_M-10to50','DYJetsToLL_M-50','DYJetsToLL_M-10to50ext3','DYJetsToLL_M-50-LO',
                                  'DY2JetsToLL', 'DY3JetsToLL', 'DY4JetsToLL',
                                  'DYJetsToLL_M-50_HT-100to200_MLM' , 'DYJetsToLL_M-50_HT-100to200_MLM_ext' , 
                                  'DYJetsToLL_M-50_HT-200to400_MLM' , 
                                  'DYJetsToLL_M-50_HT-400to600_MLM' ,
                                  'DYJetsToLL_M-50_HT-600toInf_MLM' ,
                                  # Top
                                  'TTTo2L2Nu','TT',
                                  'ST_t-channel_antitop','ST_t-channel_top',
                                  'ST_tW_antitop','ST_tW_top',
                                  # VV (including WW) 
                                  'WWTo2L2Nu','GluGluWWTo2L2Nu_MCFM','GluGluWWTo2L2NuHiggs_MCFM',
                                  'GluGluHToWWTo2L2Nu_alternative_M125','VBFHToWWTo2L2Nu_alternative_M125',
                                  'WZTo3LNu',
                                  'ZZ','Zg',
                                  'ZZTo2L2Nu','ZZTo2L2Q','ZZTo4L',
                                  'Wg_AMCNLOFXFX','WgStarLNuEE','WgStarLNuMuMu',
                                  'Wg_MADGRAPHMLM',
                                  # VVV
                                  'WZZ','ZZZ','WWZ','WWW',
                                  # Higgs 
                                  'GluGluHToTauTau_M125', 'GluGluHToWWTo2L2Nu_M125','GluGluHToWWTo2L2NuPowheg_M125',
                                  'HWminusJ_HToTauTau_M125', 'HWminusJ_HToWW_M125',
                                  'HWplusJ_HToTauTau_M125', 'HWplusJ_HToWW_M125',
                                  'HZJ_HToTauTau_M125', 'HZJ_HToWW_M125',
                                  'VBFHToTauTau_M125', 'VBFHToWWTo2L2Nu_M125',
                                  'ggZH_HToWW_M125', # missing ggZHToTauTau
                                  'ttHJetToNonbb_M125','TTWJetsToLNu',
                                  # ... ggH High Mass
                                  'GluGluHToWWTo2L2Nu_M130',
                                  'GluGluHToWWTo2L2Nu_M135',
                                  'GluGluHToWWTo2L2Nu_M140',
                                  'GluGluHToWWTo2L2Nu_M145',
                                  'GluGluHToWWTo2L2Nu_M150',
                                  'GluGluHToWWTo2L2Nu_M155',
                                  'GluGluHToWWTo2L2Nu_M160',
                                  'GluGluHToWWTo2L2Nu_M165',
                                  'GluGluHToWWTo2L2Nu_M170',
                                  'GluGluHToWWTo2L2Nu_M175',
                                  'GluGluHToWWTo2L2Nu_M180',
                                  'GluGluHToWWTo2L2Nu_M190',
                                  'GluGluHToWWTo2L2Nu_M200',
                                  'GluGluHToWWTo2L2Nu_M210',
                                  'GluGluHToWWTo2L2Nu_M230',
                                  'GluGluHToWWTo2L2Nu_M250',
                                  'GluGluHToWWTo2L2Nu_M270',
                                  'GluGluHToWWTo2L2Nu_M300',
                                  'GluGluHToWWTo2L2Nu_M350',
                                  'GluGluHToWWTo2L2Nu_M400',
                                  'GluGluHToWWTo2L2Nu_M450',
                                  'GluGluHToWWTo2L2Nu_M500',
                                  'GluGluHToWWTo2L2Nu_M550',
                                  'GluGluHToWWTo2L2Nu_M600',
                                  'GluGluHToWWTo2L2Nu_M650',
                                  'GluGluHToWWTo2L2Nu_M700',
                                  'GluGluHToWWTo2L2Nu_M750',
                                  'GluGluHToWWTo2L2Nu_M750_NWA',
                                  'GluGluHToWWTo2L2Nu_M800',
                                  'GluGluHToWWTo2L2Nu_M900',
                                  'GluGluHToWWTo2L2Nu_M1000',
                                  # ... VBF High Mass
                                  'VBFHToWWTo2L2Nu_M130',
                                  'VBFHToWWTo2L2Nu_M135',
                                  'VBFHToWWTo2L2Nu_M140',
                                  'VBFHToWWTo2L2Nu_M145',
                                  'VBFHToWWTo2L2Nu_M150',
                                  'VBFHToWWTo2L2Nu_M155',
                                  'VBFHToWWTo2L2Nu_M160',
                                  'VBFHToWWTo2L2Nu_M165',
                                  'VBFHToWWTo2L2Nu_M170',
                                  'VBFHToWWTo2L2Nu_M175',
                                  'VBFHToWWTo2L2Nu_M180',
                                  'VBFHToWWTo2L2Nu_M190',
                                  'VBFHToWWTo2L2Nu_M200',
                                  'VBFHToWWTo2L2Nu_M210',
                                  'VBFHToWWTo2L2Nu_M230',
                                  'VBFHToWWTo2L2Nu_M250',
                                  'VBFHToWWTo2L2Nu_M270',
                                  'VBFHToWWTo2L2Nu_M300',
                                  'VBFHToWWTo2L2Nu_M350',
                                  'VBFHToWWTo2L2Nu_M400',
                                  'VBFHToWWTo2L2Nu_M450',
                                  'VBFHToWWTo2L2Nu_M500',
                                  'VBFHToWWTo2L2Nu_M550',
                                  'VBFHToWWTo2L2Nu_M600',
                                  'VBFHToWWTo2L2Nu_M650',
                                  'VBFHToWWTo2L2Nu_M700',
                                  'VBFHToWWTo2L2Nu_M750',
                                  'VBFHToWWTo2L2Nu_M750_NWA',
                                  'VBFHToWWTo2L2Nu_M800',
                                  'VBFHToWWTo2L2Nu_M900',
                                  'VBFHToWWTo2L2Nu_M1000',
                                 ] ,
              },

# ... Individual Steps

  'mcwghtcount':{ 
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : False ,
                  'command'    : 'gardener.py mcweightscounter '
                },

# 'mcweights' : {
#                 'isChain'    : False ,
#                 'do4MC'      : True  ,
#                 'do4Data'    : False ,
#                 'command'    : 'gardener.py mcweightsfiller '
#               } ,


  'tagjson'   : {
                  'isChain'    : False ,
                  'do4MC'      : False ,
                  'do4Data'    : True ,
                  #'command'    : 'gardener.py  filterjson --json=/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions16/13TeV/Cert_271036-273450_13TeV_PromptReco_Collisions16_JSON_NoL1T.txt'
                  'command'    : 'gardener.py  filterjson --json=/user/xjanssen/HWW2015/pudata/Cert_271036-273450_13TeV_PromptReco_Collisions16_JSON_NoL1T.txt'
                } ,


  'selectjson'   : {
                  'isChain'    : False ,
                  'do4MC'      : False ,
                  'do4Data'    : True ,
                  'command'    : 'gardener.py filter -f \'isJsonOk>0.5\' '
                } ,



  'puadder'   : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : False ,
                  'command'    : 'gardener.py puadder --data=RPLME_puData --HistName=pileup --branch=puW --kind=trpu '
                } ,

  'baseW'     : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : False ,
                  'command'    : 'gardener.py adder -v \'baseW/F=RPLME_baseW\' -v \'Xsec/F=RPLME_XSection\' '

                } ,

  'wwNLL'     : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : False ,
                  'onlySample' : ['WWTo2L2Nu','WWTo2L2NuHerwigPS','WWTo2L2Nu_CUETUp','WWTo2L2Nu_CUETDown'] ,
                  'command'    : 'gardener.py wwNLLcorrections -m \'powheg\' --cmssw RPLME_CMSSW'
                },

  'genVariables'  : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : False ,
                  'command'    : 'gardener.py genvariablesfiller ',
                  'onlySample' : [
                                  # DY 
                                  'DYJetsToLL_M-10to50','DYJetsToLL_M-50','DYJetsToLL_M-10to50ext3','DYJetsToLL_M-50-LO',
                                  'DY2JetsToLL', 'DY3JetsToLL', 'DY4JetsToLL',
                                  'DYJetsToLL_M-50_HT-100to200_MLM' , 'DYJetsToLL_M-50_HT-100to200_MLM_ext' , 
                                  'DYJetsToLL_M-50_HT-200to400_MLM' , 
                                  'DYJetsToLL_M-50_HT-400to600_MLM' ,
                                  'DYJetsToLL_M-50_HT-600toInf_MLM' ,
                                  ]

                },


  'genMatchVariables'  : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : False ,
                  'command'    : 'gardener.py genmatchvarfiller ',
                },


  'BWEwkSinglet' : {
                  'isChain'    : False ,
                  'do4MC'      : True ,
                  'do4Data'    : False,
      
                  'onlySample' : [
                                  # ... ggH High Mass
                                  'GluGluHToWWTo2L2Nu_M200',
                                  'GluGluHToWWTo2L2Nu_M210',
                                  'GluGluHToWWTo2L2Nu_M230',
                                  'GluGluHToWWTo2L2Nu_M250',
                                  'GluGluHToWWTo2L2Nu_M270',
                                  'GluGluHToWWTo2L2Nu_M300',
                                  'GluGluHToWWTo2L2Nu_M350',
                                  'GluGluHToWWTo2L2Nu_M400',
                                  'GluGluHToWWTo2L2Nu_M450',
                                  'GluGluHToWWTo2L2Nu_M500',
                                  'GluGluHToWWTo2L2Nu_M550',
                                  'GluGluHToWWTo2L2Nu_M600',
                                  'GluGluHToWWTo2L2Nu_M650',
                                  'GluGluHToWWTo2L2Nu_M700',
                                  'GluGluHToWWTo2L2Nu_M750',
                                  #'GluGluHToWWTo2L2Nu_M750_NWA',
                                  'GluGluHToWWTo2L2Nu_M800',
                                  'GluGluHToWWTo2L2Nu_M900',
                                  'GluGluHToWWTo2L2Nu_M1000',
                                  # ... VBF High Mass
                                  'VBFHToWWTo2L2Nu_M200',
                                  'VBFHToWWTo2L2Nu_M210',
                                  'VBFHToWWTo2L2Nu_M230',
                                  'VBFHToWWTo2L2Nu_M250',
                                  'VBFHToWWTo2L2Nu_M270',
                                  'VBFHToWWTo2L2Nu_M300',
                                  'VBFHToWWTo2L2Nu_M350',
                                  'VBFHToWWTo2L2Nu_M400',
                                  'VBFHToWWTo2L2Nu_M450',
                                  'VBFHToWWTo2L2Nu_M500',
                                  'VBFHToWWTo2L2Nu_M550',
                                  'VBFHToWWTo2L2Nu_M600',
                                  'VBFHToWWTo2L2Nu_M650',
                                  'VBFHToWWTo2L2Nu_M700',
                                  'VBFHToWWTo2L2Nu_M750',
                                  #'VBFHToWWTo2L2Nu_M750_NWA',
                                  'VBFHToWWTo2L2Nu_M800',
                                  'VBFHToWWTo2L2Nu_M900',
                                  'VBFHToWWTo2L2Nu_M1000', 
                                 ],
                  'command'    : 'gardener.py BWEwkSingletReweighter -p "latino_(GluGlu|VBF)HToWWTo2L2Nu_M([0-9]+)*"',
                 },

  'l2sel'    : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : True  ,
                  'command'    : 'gardener.py l2selfiller --kind 1 --cmssw RPLME_CMSSW'
               },

  'l2kin'    : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : True  ,
                  'command'    : 'gardener.py l2kinfiller --cmssw RPLME_CMSSW'
               },



  'l3kin'    : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : True  ,
                  'command'    : 'gardener.py l3kinfiller --cmssw RPLME_CMSSW'
               },


  'l2loose'    : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : True  ,
                  'command'    : 'gardener.py l2selfiller --kind 2 --cmssw RPLME_CMSSW --selection 1'
               },

 'l2vloose'    : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : True  ,
                  'command'    : 'gardener.py l2selfiller --kind 4 --cmssw RPLME_CMSSW --selection 1'
               },


  'l2tight'    : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : True  ,
                  'command'    : 'gardener.py filter -f \'std_vector_lepton_isTightLepton[0]>0.5 && std_vector_lepton_isTightLepton[1]>0.5\' '
               },

  'l1loose'    : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : True  ,
                  'command'    : 'gardener.py l1selfiller --kind 2 --cmssw RPLME_CMSSW'
               },

  'l1vloose'    : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : True  ,
                  'command'    : 'gardener.py l1selfiller --kind 4 --cmssw RPLME_CMSSW'
               },


  'do_WgStarsel' : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : True  ,
                  'command'    : 'gardener.py l2selfiller --kind 3 --cmssw RPLME_CMSSW'
               },


  'IdIsoSC'  : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'command'    : 'gardener.py idisofiller'
               },

  'TrigEff'  : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'command'    : 'gardener.py efftfiller'
               },


  'hadd'     : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : True  ,
                  'bigSamples' : ['DYJetsToLL_M-50','DY2JetsToLL','ZZTo2L2Q','DYJetsToLL_M-50-LO',
                                  'WZTo2L2Q','TTToSemiLeptonic'
                                 ],
               },

  'UEPS'     : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'onlySample' : [ 
                                    'GluGluHToWWTo2L2Nu_M125_CUETDown' , 'VBFHToWWTo2L2Nu_M125_CUETDown' , 'WWTo2L2Nu_CUETDown' ,
                                    'GluGluHToWWTo2L2Nu_M125_CUETUp'   , 'VBFHToWWTo2L2Nu_M125_CUETUp'   , 'WWTo2L2Nu_CUETUp'   ,
                                    'GluGluHToWWTo2L2NuHerwigPS_M125'  , 'VBFHToWWTo2L2NuHerwigPS_M125'  , 'WWTo2L2NuHerwigPS'  ,
                                 ] ,
                  'cpMap' : {
                              'UEdo' : { 
                                          'GluGluHToWWTo2L2Nu_M125_CUETDown' : ['GluGluHToWWTo2L2Nu_M125' ,'GluGluHToWWTo2L2NuPowheg_M125'],
                                          'VBFHToWWTo2L2Nu_M125_CUETDown'    : ['VBFHToWWTo2L2Nu_M125']    ,
                                          'WWTo2L2Nu_CUETDown'               : ['WWTo2L2Nu'] , 
                                       },
                              'UEup' : {
                                          'GluGluHToWWTo2L2Nu_M125_CUETUp'   : ['GluGluHToWWTo2L2Nu_M125' ,'GluGluHToWWTo2L2NuPowheg_M125'],
                                          'VBFHToWWTo2L2Nu_M125_CUETUp'      : ['VBFHToWWTo2L2Nu_M125']    ,
                                          'WWTo2L2Nu_CUETUp'                 : ['WWTo2L2Nu'] ,
                                       },
                              'PS'   : {    
                                          'GluGluHToWWTo2L2NuHerwigPS_M125'  : ['GluGluHToWWTo2L2Nu_M125' ,'GluGluHToWWTo2L2NuPowheg_M125'],
                                          'VBFHToWWTo2L2NuHerwigPS_M125'     : ['VBFHToWWTo2L2Nu_M125'] ,
                                          'WWTo2L2NuHerwigPS'                : ['WWTo2L2Nu'] ,
                                       },
                            },
               },

  'do_lpTCorrMC'  : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : False ,
                  'command'    : 'gardener.py letPtCorrector --isData=0 --cmssw=RPLME_CMSSW'
                } ,

  'do_lpTCorrData'  : {
                  'isChain'    : False ,
                  'do4MC'      : False  ,
                  'do4Data'    : True ,
                  'command'    : 'gardener.py letPtCorrector --isData=1 --cmssw=RPLME_CMSSW'
                } ,


  'do_JESup'    : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : False ,
                  'command'    : 'gardener.py JESTreeMaker -k 1 '
                } ,

  'do_JESdo'    : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : False ,
                  'command'    : 'gardener.py JESTreeMaker -k -1 '
                } ,
  
  'do_JESMaxup'    : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : False ,
                  'command'    : 'gardener.py JESTreeMaker -k 1 --maxUncertainty '
                } ,

  'do_JESMaxdo'    : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : False ,
                  'command'    : 'gardener.py JESTreeMaker -k -1 --maxUncertainty'
                } ,

 
  'bPogSF'   :{
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  #'command'    : 'gardener.py btagPogScaleFactors '
                  # --> switch to multiple bTag algo SF:
                  'command'    : 'gardener.py allBtagPogScaleFactors '
              },

  'do_LepElepTup'    : {
                   'isChain'    : False ,
                   'do4MC'      : True  ,
                   'do4Data'    : False ,
                   'command'    : 'gardener.py LeppTScalerTreeMaker --lepFlavourToChange ele    -v 1.0'
                 } ,
  
  'do_LepElepTdo'    : {
                   'isChain'    : False ,
                   'do4MC'      : True  ,
                   'do4Data'    : False ,
                   'command'    : 'gardener.py LeppTScalerTreeMaker --lepFlavourToChange ele   -v -1.0'
                 } ,
  
  'do_LepMupTup'    : {
                   'isChain'    : False ,
                   'do4MC'      : True  ,
                   'do4Data'    : False ,
                   'command'    : 'gardener.py LeppTScalerTreeMaker --lepFlavourToChange mu    -v 1.0'
                 } ,
  
  'do_LepMupTdo'    : {
                   'isChain'    : False ,
                   'do4MC'      : True  ,
                   'do4Data'    : False ,
                   'command'    : 'gardener.py LeppTScalerTreeMaker --lepFlavourToChange mu   -v -1.0'
                 } ,
  
  'do_METup'        : {
                   'isChain'    : False ,
                   'do4MC'      : True  ,
                   'do4Data'    : False ,
                   'command'    : 'gardener.py metUncertainty --kind=Up --cmssw=RPLME_CMSSW --lepton no   --jetresolution no   --unclustered no  '
                 } ,
  
  'do_METdo'        : {
                   'isChain'    : False ,
                   'do4MC'      : True  ,
                   'do4Data'    : False ,
                   'command'    : 'gardener.py metUncertainty --kind=Dn --cmssw=RPLME_CMSSW --lepton no   --jetresolution no   --unclustered no '
                 } ,
  
  
   'Mucca'       :  {
                  'isChain'    : True ,
                  'do4MC'      : True ,
                  'do4Data'    : True ,
                  'subTargets' : [
                                  'do_Mucca_1',
                                  'do_Mucca_2',
                                  'do_Mucca_3',
                                  'do_Mucca_4',
                                  'do_Mucca_5'
                                  ],
                },

   'do_Mucca_1'        : {
                   'isChain'    : False ,
                   'do4MC'      : True  ,
                   'do4Data'    : True ,
                   'command'    : 'gardener.py muccaMvaVarFiller --kind 1'
                 } ,
  
   'do_Mucca_2'        : {
                   'isChain'    : False ,
                   'do4MC'      : True  ,
                   'do4Data'    : True ,
                   'command'    : 'gardener.py muccaMvaVarFiller --kind 2'
                 } ,

   'do_Mucca_3'        : {
                   'isChain'    : False ,
                   'do4MC'      : True  ,
                   'do4Data'    : True ,
                   'command'    : 'gardener.py muccaMvaVarFiller --kind 3'
                 } ,

   'do_Mucca_4'        : {
                   'isChain'    : False ,
                   'do4MC'      : True  ,
                   'do4Data'    : True ,
                   'command'    : 'gardener.py muccaMvaVarFiller --kind 4'
                 } ,

   'do_Mucca_5'        : {
                   'isChain'    : False ,
                   'do4MC'      : True  ,
                   'do4Data'    : True ,
                   'command'    : 'gardener.py muccaMvaVarFiller --kind 5'
                 } ,




   # fix datasets names
  'fixdataset_Herwig_nuisance':  {
               'isChain'    : False ,
               'do4MC'      : True ,
               'do4Data'    : False,
               'onlySample' : [
                               #  qqWW
                               'WWTo2L2NuHerwigPS',
                               # ggH
                               'GluGluHToWWTo2L2NuHerwigPS_M125' ,
                               # VBF
                               'VBFHToWWTo2L2NuHerwigPS_M125'
                              ] ,
               'command'    : 'gardener.py adder -v \'dataset/F=42\'  '
           },


  'wwSel'    : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : True  ,
                  'command'    : 'gardener.py filter -f \' mll>12 && std_vector_lepton_pt[0]>20 && std_vector_lepton_pt[1]>10 && std_vector_lepton_pt[2]<10 && metPfType1 > 20 && ptll > 30 && (std_vector_lepton_flavour[0] * std_vector_lepton_flavour[1] == -11*13) \' '
           },

  'vh3lSel'   : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : True  ,
                  'command'    : 'gardener.py filter -f \' std_vector_lepton_isTightLepton[0] > 0.5  && std_vector_lepton_isTightLepton[1] > 0.5  && std_vector_lepton_isTightLepton[2] > 0.5 && std_vector_lepton_pt[0] > 20. && std_vector_lepton_pt[1] > 10. && std_vector_lepton_pt[2] > 10.\' '
           },

}

