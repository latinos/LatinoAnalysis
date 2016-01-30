
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
                        'dirExt'  : 'LatinoTrees' ,
                      #  'dirExt'  : 'split' ,
                        'gDocID'  : '1wH73CYA_T4KMkl1Cw-xLTj8YG7OPqayDnP53N-lZwFQ' ,
                        #'puData'  : '/afs/cern.ch/user/x/xjanssen/public/MyDataPileupHistogram.root',
                        'puData'  : '/afs/cern.ch/user/x/xjanssen/public/Cert_246908-260627_13TeV_PromptReco_Collisions15_25ns_JSON_v2_from256630_PileupHistogram.root' ,
                        #'bigSamples': ['DYJetsToLL_M-10to50'] ,
                      } ,

  '21Oct_Run2015D_05Oct2015' : {
                        'isData'  : True ,
                        'samples' : 'LatinoTrees/AnalysisStep/test/crab/samples/samples_dataD_05Oct2015_25ns.py' ,
                        #'dirExt'  : 'Run2015D_05Oct2015' ,
                        'dirExt'  : 'split' ,
                      } ,

  '21Oct_Run2015D_PromptReco' : {
                        'isData'  : True ,
                        'samples' : 'LatinoTrees/AnalysisStep/test/crab/samples/samples_dataD_PromptReco_25ns.py' ,
                        #'dirExt'  : 'Run2015D_PromptReco' ,
                        'dirExt'  : 'split' ,
                      } ,

  '21OctBis_Run2015D_05Oct2015' : {
                        'isData'  : True ,
                        'samples' : 'LatinoTrees/AnalysisStep/test/crab/samples/samples_dataD_05Oct2015_25ns_21OctBis.py',
                        #'dirExt'  : 'Run2015D_PromptReco' ,
                        'dirExt'  : 'split2' ,
                      } ,

  '21OctBis_Run2015D_PromptReco_0716pb' : {
                        'isData'  : True ,
                        'samples' : 'LatinoTrees/AnalysisStep/test/crab/samples/samples_dataD_PromptReco_25ns_21OctBis_0716pb.py' ,
                        'dirExt'  : 'split2' ,
                      } ,

  '21OctBis_Run2015D_PromptReco_0851pb' : {
                        'isData'  : True ,
                        'samples' : 'LatinoTrees/AnalysisStep/test/crab/samples/samples_dataD_PromptReco_25ns_21OctBis_0851pb.py' ,
                        'dirExt'  : 'split2' ,
                      } ,

#### 76x / StarWars tag / miniAOD v1

  '08Jan_25ns_mAODv1_MC'   : {
                        'isData'  : False ,
                        'samples' : 'LatinoTrees/AnalysisStep/test/crab/samples/samples_fall15_miniaod_25ns.py' ,
                        'dirExt'  : 'LatinoTrees' ,
                        'gDocID'  : '1wH73CYA_T4KMkl1Cw-xLTj8YG7OPqayDnP53N-lZwFQ' ,
                        'puData'  : '/afs/cern.ch/user/x/xjanssen/public/Cert_246908-260627_13TeV_PromptReco_Collisions15_25ns_JSON_v2_from256630_PileupHistogram.root' ,
                      } ,

#### 76x / StarWars tag (v2) / miniAOD v2

  '18Jan_25ns_mAODv2_MC_TEST'   : {
                        'isData'  : False ,
                        'samples' : 'LatinoTrees/AnalysisStep/test/crab/samples/samples_fall15_miniaodv2_25ns.py' ,
                        'dir'     : '/store/group/phys_higgs/cmshww/amassiro/RunII/18Jan/MC/25ns/',
                        'dirExt'  : 'LatinoTrees' ,
                        #'gDocID'  : '1wH73CYA_T4KMkl1Cw-xLTj8YG7OPqayDnP53N-lZwFQ' ,
                        'puData'  : '/afs/cern.ch/user/x/xjanssen/public/Cert_246908-260627_13TeV_PromptReco_Collisions15_25ns_JSON_v2_from256630_PileupHistogram.root' ,
                      } ,


#### 76x / StarWars tag (v3) / miniAOD v2

  '22Jan_25ns_mAODv2_MC'   : {
                        'isData'  : False ,
                        'samples' : 'LatinoTrees/AnalysisStep/test/crab/samples/samples_fall15_miniaodv2_25ns.py' ,
                        'dirExt'  : 'LatinoTrees' ,
                        #'gDocID'  : '1wH73CYA_T4KMkl1Cw-xLTj8YG7OPqayDnP53N-lZwFQ' ,
                        'puData'  : '/afs/cern.ch/user/x/xjanssen/public/Cert_246908-260627_13TeV_PromptReco_Collisions15_25ns_JSON_v2_from256630_PileupHistogram.root' ,
                      } ,

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
                  'subTargets' : ['puadder','baseW','wwNLL','l2sel']
                },

  'bSFL2Eff'   :   {
                  'isChain'    : True ,
                  'do4MC'      : True ,
                  'do4Data'    : False,
                  'subTargets' : ['puadder','bPogSF','TrigEff','IdIsoSC','l2kin'],
                  'onlySample' : ['DYJetsToLL_M-10to50','DYJetsToLL_M-50','WJetsToLNu','TTTo2L2Nu','TTJets',
                                  'ST_t-channel','ST_tW_antitop','ST_tW_top','WWTo2L2Nu','WZTo3LNu',
                                  'WZZ','ZZZ','GluGluWWTo2L2Nu_MCFM',
                                  'GluGluHToTauTau_M125', 'GluGluHToWWTo2L2Nu_M125',
                                  'HWminusJ_HToTauTau_M125', 'HWminusJ_HToWW_M125',
                                  'HWplusJ_HToTauTau_M125', 'HWplusJ_HToWW_M125',
                                  'HZJ_HToTauTau_M125', 'HZJ_HToWW_M125',
                                  'VBFHToTauTau_M125', 'VBFHToWWTo2L2Nu_M125',
                                 ] ,
                },

  'JESup'     :  {
                  'isChain'    : True ,
                  'do4MC'      : True ,
                  'do4Data'    : False,
                  'subTargets' : ['do_JESup','bPogSF','l2kin'],
                  'onlySample' : ['DYJetsToLL_M-10to50','DYJetsToLL_M-50','WJetsToLNu','TTTo2L2Nu','TTJets',
                                  'ST_t-channel','ST_tW_antitop','ST_tW_top','WWTo2L2Nu','WZTo3LNu',
                                  'WZZ','ZZZ','GluGluWWTo2L2Nu_MCFM',
                                  'GluGluHToTauTau_M125', 'GluGluHToWWTo2L2Nu_M125',
                                  'HWminusJ_HToTauTau_M125', 'HWminusJ_HToWW_M125',
                                  'HWplusJ_HToTauTau_M125', 'HWplusJ_HToWW_M125',
                                  'HZJ_HToTauTau_M125', 'HZJ_HToWW_M125',
                                  'VBFHToTauTau_M125', 'VBFHToWWTo2L2Nu_M125',
                                 ] ,
                },

  'JESdo'     :  {
                  'isChain'    : True ,
                  'do4MC'      : True ,
                  'do4Data'    : False,
                  'subTargets' : ['do_JESdo','bPogSF','l2kin'],
                  'onlySample' : ['DYJetsToLL_M-10to50','DYJetsToLL_M-50','WJetsToLNu','TTTo2L2Nu','TTJets',
                                  'ST_t-channel','ST_tW_antitop','ST_tW_top','WWTo2L2Nu','WZTo3LNu',
                                  'WZZ','ZZZ','GluGluWWTo2L2Nu_MCFM',
                                  'GluGluHToTauTau_M125', 'GluGluHToWWTo2L2Nu_M125',
                                  'HWminusJ_HToTauTau_M125', 'HWminusJ_HToWW_M125',
                                  'HWplusJ_HToTauTau_M125', 'HWplusJ_HToWW_M125',
                                  'HZJ_HToTauTau_M125', 'HZJ_HToWW_M125',
                                  'VBFHToTauTau_M125', 'VBFHToWWTo2L2Nu_M125',
                                 ] ,
                },

  'LeppTup':  {
                  'isChain'    : True ,
                  'do4MC'      : True ,
                  'do4Data'    : False,
                  'subTargets' : ['do_LeppTup','TrigEff','IdIsoSC','l2kin'],
                  'onlySample' : ['DYJetsToLL_M-10to50','DYJetsToLL_M-50','WJetsToLNu','TTTo2L2Nu','TTJets',
                                  'ST_t-channel','ST_tW_antitop','ST_tW_top','WWTo2L2Nu','WZTo3LNu',
                                  'WZZ','ZZZ','GluGluWWTo2L2Nu_MCFM',
                                  'GluGluHToTauTau_M125', 'GluGluHToWWTo2L2Nu_M125',
                                  'HWminusJ_HToTauTau_M125', 'HWminusJ_HToWW_M125',
                                  'HWplusJ_HToTauTau_M125', 'HWplusJ_HToWW_M125',
                                  'HZJ_HToTauTau_M125', 'HZJ_HToWW_M125',
                                  'VBFHToTauTau_M125', 'VBFHToWWTo2L2Nu_M125',
                                 ] ,
              },

  'LeppTdo':  {
                  'isChain'    : True ,
                  'do4MC'      : True ,
                  'do4Data'    : False,
                  'subTargets' : ['do_LeppTdo','TrigEff','IdIsoSC','l2kin'],
                  'onlySample' : ['DYJetsToLL_M-10to50','DYJetsToLL_M-50','WJetsToLNu','TTTo2L2Nu','TTJets',
                                  'ST_t-channel','ST_tW_antitop','ST_tW_top','WWTo2L2Nu','WZTo3LNu',
                                  'WZZ','ZZZ','GluGluWWTo2L2Nu_MCFM',
                                  'GluGluHToTauTau_M125', 'GluGluHToWWTo2L2Nu_M125',
                                  'HWminusJ_HToTauTau_M125', 'HWminusJ_HToWW_M125',
                                  'HWplusJ_HToTauTau_M125', 'HWplusJ_HToWW_M125',
                                  'HZJ_HToTauTau_M125', 'HZJ_HToWW_M125',
                                  'VBFHToTauTau_M125', 'VBFHToWWTo2L2Nu_M125',
                                 ] ,
              },

   'METup':  {
                  'isChain'    : True ,
                  'do4MC'      : True ,
                  'do4Data'    : False,
                  'subTargets' : ['do_METup','l2kin'],
                  'onlySample' : ['DYJetsToLL_M-10to50','DYJetsToLL_M-50','WJetsToLNu','TTTo2L2Nu','TTJets',
                                  'ST_t-channel','ST_tW_antitop','ST_tW_top','WWTo2L2Nu','WZTo3LNu',
                                  'WZZ','ZZZ','GluGluWWTo2L2Nu_MCFM',
                                  'GluGluHToTauTau_M125', 'GluGluHToWWTo2L2Nu_M125',
                                  'HWminusJ_HToTauTau_M125', 'HWminusJ_HToWW_M125',
                                  'HWplusJ_HToTauTau_M125', 'HWplusJ_HToWW_M125',
                                  'HZJ_HToTauTau_M125', 'HZJ_HToWW_M125',
                                  'VBFHToTauTau_M125', 'VBFHToWWTo2L2Nu_M125',
                                 ] ,
              },

   'METdo':  {
                  'isChain'    : True ,
                  'do4MC'      : True ,
                  'do4Data'    : False,
                  'subTargets' : ['do_METdo','l2kin'],
                  'onlySample' : ['DYJetsToLL_M-10to50','DYJetsToLL_M-50','WJetsToLNu','TTTo2L2Nu','TTJets',
                                  'ST_t-channel','ST_tW_antitop','ST_tW_top','WWTo2L2Nu','WZTo3LNu',
                                  'WZZ','ZZZ','GluGluWWTo2L2Nu_MCFM',
                                  'GluGluHToTauTau_M125', 'GluGluHToWWTo2L2Nu_M125',
                                  'HWminusJ_HToTauTau_M125', 'HWminusJ_HToWW_M125',
                                  'HWplusJ_HToTauTau_M125', 'HWplusJ_HToWW_M125',
                                  'HZJ_HToTauTau_M125', 'HZJ_HToWW_M125',
                                  'VBFHToTauTau_M125', 'VBFHToWWTo2L2Nu_M125',
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
                  'command'    : 'gardener.py adder -v \'baseW/F=RPLME_baseW\' '

                } ,

  'wwNLL'     : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : False ,
                  'onlySample' : ['WWTo2L2Nu'] ,
                  'command'    : 'gardener.py wwNLLcorrections -m \'powheg\' '
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

  'l2loose'    : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : True  ,
                  'command'    : 'gardener.py l2selfiller --kind 2 --cmssw RPLME_CMSSW'
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
               },

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
   
  'bPogSF'   :{
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'command'    : 'gardener.py btagPogScaleFactors '
              },

  'do_LeppTup'    : {
                   'isChain'    : False ,
                   'do4MC'      : True  ,
                   'do4Data'    : False ,
                   'command'    : 'gardener.py LeppTScalerTreeMaker --mu_Scl 1 --eEB_Scl 2 --eEE_Scl 5'
                 } ,
  
  'do_LeppTdo'    : {
                   'isChain'    : False ,
                   'do4MC'      : True  ,
                   'do4Data'    : False ,
                   'command'    : 'gardener.py LeppTScalerTreeMaker --mu_Scl -1 --eEB_Scl -2 --eEE_Scl -5'
                 } ,
  
  
  'do_METup'        : {
                   'isChain'    : False ,
                   'do4MC'      : True  ,
                   'do4Data'    : False ,
                   'command'    : 'gardener.py metUncertainty --kind=Up '
                 } ,
  
  
  'do_METdo'        : {
                   'isChain'    : False ,
                   'do4MC'      : True  ,
                   'do4Data'    : False ,
                   'command'    : 'gardener.py metUncertainty --kind=Dn '
                 } ,
  

}

