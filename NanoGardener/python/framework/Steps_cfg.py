#!/usr/bin/env python


Steps = {

# ------------------------------------------------ CHAINS ----------------------------------------------------

## ------- MC:

  'MCl1loose2016': {
                  'isChain'    : True  ,
                  'do4MC'      : True  ,
                  'do4Data'    : False ,
                  'selection'  : '"(nElectron>0 && Electron_pt[0]>10) || (nMuon>0 && Muon_pt[0]>10)"' , 
                  'subTargets' : ['baseW', 'leptonMaker','lepSel', 'puW2016', 'l2Kin', 'l3Kin', 'l4Kin', 'btagPerJet2016', 'btagPerEvent'],
                },

  'MCl1loose2017': {
                  'isChain'    : True  ,
                  'do4MC'      : True  ,
                  'do4Data'    : False ,
                  'selection'  : '"((nElectron+nMuon)>0)"' ,
                  'subTargets' : ['leptonMaker','lepSel', 'puW2017', 'l2Kin', 'l3Kin', 'l4Kin', 'btagPerJet2017', 'btagPerEvent'],
                },

  'MCformulas': {
                  'isChain'    : True  ,
                  'do4MC'      : True ,
                  'do4Data'    : False  ,           
                  'subTargets' : ['baseW','trigMC','formulasMC'],
                },             

## ------- DATA:
    
  'DATAl1loose2016': {
                  'isChain'    : True  ,
                  'do4MC'      : False ,
                  'do4Data'    : True  ,
                  'selection'  : '"(nElectron>0 && Electron_pt[0]>10) || (nMuon>0 && Muon_pt[0]>10)"' , 
                  'subTargets' : ['leptonMaker','lepSel', 'l2Kin', 'l3Kin', 'l4Kin'],
                },

  'DATAl1loose2017': {
                  'isChain'    : True  ,
                  'do4MC'      : False ,
                  'do4Data'    : True  ,
                  'selection'  : '"((nElectron+nMuon)>0)"' ,
                  'subTargets' : ['leptonMaker','lepSel', 'l2Kin', 'l3Kin', 'l4Kin','trigData','formulasDATA'],
                }, 
   
   'DATAformulas' : {
                  'isChain'    : True  ,
                  'do4MC'      : False ,
                  'do4Data'    : True  ,           
                  'subTargets' : ['trigData','formulasDATA'],
                },

# ------------------------------------------------ MODULES ---------------------------------------------------

  
## ------- MODULES: Object Handling

  'lepMergerHWW' : { 
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : True  ,
                  'import'     : 'PhysicsTools.NanoAODTools.postprocessing.modules.common.collectionMerger' ,
                  'declare'    : 'lepMergerHWW = lambda : collectionMerger( input  = ["Electron","Muon"], output = "Lepton", reverse = True)' ,
                  'module'     : 'lepMergerHWW()' ,
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
             

## ------- MODULES: Trigger

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

  'wwNLL'    : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.wwNLLcorrectionWeightProducer' ,
                  'module)'     : 'wwNLLcorrectionWeightProducer()',  
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

  'formulasMC' : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.GenericFormulaAdder' ,
                  'declare'    : '',
                  'module'     : 'GenericFormulaAdder(\'data/formulasToAdd_MC.py\')' ,
                 },
   
  'formulasDATA' : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  ,
                  'import'     : 'LatinoAnalysis.NanoGardener.modules.GenericFormulaAdder' ,
                  'declare'    : '',
                  'module'     : 'GenericFormulaAdder(\'data/formulasToAdd_DATA.py\')' ,
                 },


# ------------------------------------ SKIMS : CUTS ONLY ----------------------------------------------------------

## ------- Fake Study:

  'fakeSel'    : {
                  'isChain'    : False ,
                  'do4MC'      : False  ,
                  'do4Data'    : True  ,
                  'selection'  : '"(MET_pt < 20 && mtw1 < 20)"' ,
                 },

  'fakeSelMC'  : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : False  , 
                  'selection'  : '"(MET_pt < 20 && mtw1 < 20)"' , 
                  'onlySample' : [
                                  #### DY
                                  'DYJetsToLL_M-10to50','DYJetsToLL_M-50','DYJetsToLL_M-10to50ext3','DYJetsToLL_M-50-LO','DYJetsToLL_M-50-LO-ext1',
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
                                  'TT','TTJets',
                                 ] ,               
                 },

## ------- 2-Leptons: Loose / tightOR

  'l2loose'   : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : True  , 
                  'selection'  : '"(nLepton>=2)"' , 
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

## ------- Analysis Skims:

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
                                    'GluGluHToWWTo2L2Nu_M125_CUETDown' , 'VBFHToWWTo2L2Nu_M125_CUETDown' , 'WWTo2L2Nu_CUETDown' ,
                                    'GluGluHToWWTo2L2Nu_M125_CUETUp'   , 'VBFHToWWTo2L2Nu_M125_CUETUp'   , 'WWTo2L2Nu_CUETUp'   ,
                                    'GluGluHToWWTo2L2NuHerwigPS_M125'  , 'VBFHToWWTo2L2NuHerwigPS_M125'  , 'WWTo2L2NuHerwigPS'  ,
                                    'GluGluHToWWTo2L2Nu_M125_herwigpp' ,
                                 ] ,
                  'cpMap' : {
                              'UEdo' : {
                                          'GluGluHToWWTo2L2Nu_M125_CUETDown' : ['GluGluHToWWTo2L2Nu_M125' ,'GluGluHToWWTo2L2NuPowheg_M125'],
                                          'VBFHToWWTo2L2Nu_M125_CUETDown'    : ['VBFHToWWTo2L2Nu_M125','VBFHToWWTo2L2Nu_alternative_M125']    ,
                                          'WWTo2L2Nu_CUETDown'               : ['WWTo2L2Nu'] ,
                                       },
                              'UEup' : {
                                          'GluGluHToWWTo2L2Nu_M125_CUETUp'   : ['GluGluHToWWTo2L2Nu_M125' ,'GluGluHToWWTo2L2NuPowheg_M125'],
                                          'VBFHToWWTo2L2Nu_M125_CUETUp'      : ['VBFHToWWTo2L2Nu_M125','VBFHToWWTo2L2Nu_alternative_M125']    ,
                                          'WWTo2L2Nu_CUETUp'                 : ['WWTo2L2Nu'] ,
                                       },
                              'PS'   : {
                                          'GluGluHToWWTo2L2NuHerwigPS_M125'  : ['GluGluHToWWTo2L2Nu_M125' ,'GluGluHToWWTo2L2NuPowheg_M125'],
                                          'GluGluHToWWTo2L2Nu_M125_herwigpp' : ['GluGluHToWWTo2L2Nu_M125' ,'GluGluHToWWTo2L2NuPowheg_M125'],
                                          'VBFHToWWTo2L2NuHerwigPS_M125'     : ['VBFHToWWTo2L2Nu_M125','VBFHToWWTo2L2Nu_alternative_M125'] ,
                                          'WWTo2L2NuHerwigPS'                : ['WWTo2L2Nu'] ,
                                       },
                            },
               },

} 
