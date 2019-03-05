mvaDic = {}


mvaDic['dymva_bdt_0j'] = {
                          'type'      : 'BDT' ,  
                          'xmlFile'   : 'LatinoAnalysis/NanoGardener/python/data/DYSFmva/2017/UATmva_DYmva_2017_0j_BDT_400Trees_AdaBoost_GiniIndex_20Cuts_CostComplexity_12PruneStrength_12Var.weights.xml'   ,
                          'inputVars' : OrderedDict() ,
                         }

#mvaDic['dymva_bdt_1j'] = {
#                          'type'      : 'BDT' ,
#                          'xmlFile'   : 'LatinoAnalysis/NanoGardener/python/data/DYSFmva/2017/UATmva_DYmva_2017_1j_BDT_400Trees_AdaBoost_GiniIndex_20Cuts_CostComplexity_12PruneStrength_12Var.weights.xml'   ,
#                          'inputVars' : OrderedDict() ,
#                         }
#
#mvaDic['dymva_bdt_2j'] = {
#                          'type'      : 'BDT' ,
#                          'xmlFile'   : 'LatinoAnalysis/NanoGardener/python/data/DYSFmva/2017/UATmva_DYmva_2017_2j_BDT_400Trees_AdaBoost_GiniIndex_20Cuts_CostComplexity_12PruneStrength_12Var.weights.xml'   ,
#                          'inputVars' : OrderedDict() ,
#                         }
#
#mvaDic['dymva_bdt_VBF'] = {
#                          'type'      : 'BDT' ,
#                          'xmlFile'   : 'LatinoAnalysis/NanoGardener/python/data/DYSFmva/2017/UATmva_DYmva_2017_VBF_BDT_400Trees_AdaBoost_GiniIndex_20Cuts_CostComplexity_12PruneStrength_12Var.weights.xml'   ,
#                          'inputVars' : OrderedDict() ,
#                         }
#
#
#mvaDic['dymva_dnn_0j'] = {
#                          'type'      : 'PyKeras' ,
#                          'xmlFile'   : 'LatinoAnalysis/NanoGardener/python/data/DYSFmva/2017/TMVAClassification_PyKeras_2017_0j_m1.weights.xml'   ,
#                          'inputVars' : OrderedDict() ,
#                         }
#
#mvaDic['dymva_dnn_1j'] = {
#                          'type'      : 'PyKeras' ,
#                          'xmlFile'   : 'LatinoAnalysis/NanoGardener/python/data/DYSFmva/2017/TMVAClassification_PyKeras_2017_1j_m1.weights.xml'   ,
#                          'inputVars' : OrderedDict() ,
#                         }
#
#mvaDic['dymva_dnn_2j'] = {
#                          'type'      : 'PyKeras' ,
#                          'xmlFile'   : 'LatinoAnalysis/NanoGardener/python/data/DYSFmva/2017/TMVAClassification_PyKeras_2017_2j_m1.weights.xml'   ,
#                          'inputVars' : OrderedDict() ,
#                         }
#
#mvaDic['dymva_dnn_VBF'] = {
#                          'type'      : 'PyKeras' ,
#                          'xmlFile'   : 'LatinoAnalysis/NanoGardener/python/data/DYSFmva/2017/TMVAClassification_PyKeras_2017_VBF_m1.weights.xml'   ,
#                          'inputVars' : OrderedDict() ,
#                         }
#
#--- Variables
#0j
mvaDic['dymva_bdt_0j']['inputVars']['ptll']           = 'event.ptll' 
mvaDic['dymva_bdt_0j']['inputVars']['mth']            = 'event.mth'            
mvaDic['dymva_bdt_0j']['inputVars']['jetpt1_cut']     = 'event.jetpt1_cut'     
mvaDic['dymva_bdt_0j']['inputVars']['uperp']          = 'event.uperp'         
mvaDic['dymva_bdt_0j']['inputVars']['PfMetDivSumMet'] = 'event.PfMetDivSumMet' 
mvaDic['dymva_bdt_0j']['inputVars']['recoil']         = 'event.recoil'         
mvaDic['dymva_bdt_0j']['inputVars']['mpmet']          = 'event.mpmet'          
mvaDic['dymva_bdt_0j']['inputVars']['upara']          = 'event.upara'          
mvaDic['dymva_bdt_0j']['inputVars']['dphilmet1']      = 'event.dphilmet1'      
mvaDic['dymva_bdt_0j']['inputVars']['dphilmet2']      = 'event.dphilmet2'      
mvaDic['dymva_bdt_0j']['inputVars']['dphilljet_cut']  = 'event.dphilljet_cut'  
mvaDic['dymva_bdt_0j']['inputVars']['dphijet1met_cut']= 'event.dphijet1met_cut'

#mvaDic['dymva_dnn_0j']['inputVars']['ptll']           = 'event.ptll'
#mvaDic['dymva_dnn_0j']['inputVars']['mth']            = 'event.mth'
#mvaDic['dymva_dnn_0j']['inputVars']['jetpt1_cut']     = 'event.jetpt1_cut'
#mvaDic['dymva_dnn_0j']['inputVars']['uperp']          = 'event.uperp'
#mvaDic['dymva_dnn_0j']['inputVars']['PfMetDivSumMet'] = 'event.PfMetDivSumMet'
#mvaDic['dymva_dnn_0j']['inputVars']['recoil']         = 'event.recoil'
#mvaDic['dymva_dnn_0j']['inputVars']['mpmet']          = 'event.mpmet'
#mvaDic['dymva_dnn_0j']['inputVars']['upara']          = 'event.upara'
#mvaDic['dymva_dnn_0j']['inputVars']['dphilmet1']      = 'event.dphilmet1'
#mvaDic['dymva_dnn_0j']['inputVars']['dphilmet2']      = 'event.dphilmet2'
#mvaDic['dymva_dnn_0j']['inputVars']['dphilljet_cut']  = 'event.dphilljet_cut'
#mvaDic['dymva_dnn_0j']['inputVars']['dphijet1met_cut']= 'event.dphijet1met_cut'
#
##1j
#mvaDic['dymva_bdt_1j']['inputVars']['PV_npvsGood']    = 'event.PV_npvsGood'
#mvaDic['dymva_bdt_1j']['inputVars']['ptll']           = 'event.ptll'
#mvaDic['dymva_bdt_1j']['inputVars']['mpmet']          = 'event.mpmet'
#mvaDic['dymva_bdt_1j']['inputVars']['upara']          = 'event.upara'
#mvaDic['dymva_bdt_1j']['inputVars']['PfMetDivSumMet'] = 'event.PfMetDivSumMet'
#mvaDic['dymva_bdt_1j']['inputVars']['mtw1']           = 'event.mtw1'
#mvaDic['dymva_bdt_1j']['inputVars']['dphilmet1']      = 'event.dphilmet1'
#mvaDic['dymva_bdt_1j']['inputVars']['dphilljet_cut']  = 'event.dphilljet_cut'
#mvaDic['dymva_bdt_1j']['inputVars']['dphijet1met_cut']= 'event.dphijet1met_cut'
#mvaDic['dymva_bdt_1j']['inputVars']['jetpt2_cut']     = 'event.jetpt2_cut'
#mvaDic['dymva_bdt_1j']['inputVars']['dphilmet2']      = 'event.dphilmet2'
#mvaDic['dymva_bdt_1j']['inputVars']['projpfmet']      = 'event.projpfmet'
#
#mvaDic['dymva_dnn_1j']['inputVars']['PV_npvsGood']    = 'event.PV_npvsGood'
#mvaDic['dymva_dnn_1j']['inputVars']['ptll']           = 'event.ptll'
#mvaDic['dymva_dnn_1j']['inputVars']['mpmet']          = 'event.mpmet'
#mvaDic['dymva_dnn_1j']['inputVars']['upara']          = 'event.upara'
#mvaDic['dymva_dnn_1j']['inputVars']['PfMetDivSumMet'] = 'event.PfMetDivSumMet'
#mvaDic['dymva_dnn_1j']['inputVars']['mtw1']           = 'event.mtw1'
#mvaDic['dymva_dnn_1j']['inputVars']['dphilmet1']      = 'event.dphilmet1'
#mvaDic['dymva_dnn_1j']['inputVars']['dphilljet_cut']  = 'event.dphilljet_cut'
#mvaDic['dymva_dnn_1j']['inputVars']['dphijet1met_cut']= 'event.dphijet1met_cut'
#mvaDic['dymva_dnn_1j']['inputVars']['jetpt2_cut']     = 'event.jetpt2_cut'
#mvaDic['dymva_dnn_1j']['inputVars']['dphilmet2']      = 'event.dphilmet2'
#mvaDic['dymva_dnn_1j']['inputVars']['projpfmet']      = 'event.projpfmet'
#
##2j
#mvaDic['dymva_bdt_2j']['inputVars']['PV_npvsGood']     = 'event.PV_npvsGood'
#mvaDic['dymva_bdt_2j']['inputVars']['upara']           = 'event.upara'
#mvaDic['dymva_bdt_2j']['inputVars']['mth']             = 'event.mth'
#mvaDic['dymva_bdt_2j']['inputVars']['ptTOT_cut']       = 'event.ptTOT_cut'
#mvaDic['dymva_bdt_2j']['inputVars']['uperp']           = 'event.uperp'
#mvaDic['dymva_bdt_2j']['inputVars']['dphilljet_cut']   = 'event.dphilljet_cut'
#mvaDic['dymva_bdt_2j']['inputVars']['ptll']            = 'event.ptll'
#mvaDic['dymva_bdt_2j']['inputVars']['PfMetDivSumMet']  = 'event.PfMetDivSumMet'
#mvaDic['dymva_bdt_2j']['inputVars']['mpmet']           = 'event.mpmet'
#mvaDic['dymva_bdt_2j']['inputVars']['dphilljetjet_cut']= 'event.dphilljetjet_cut'
#mvaDic['dymva_bdt_2j']['inputVars']['dphijet1met_cut'] = 'event.dphijet1met_cut'
#mvaDic['dymva_bdt_2j']['inputVars']['dphijet2met_cut'] = 'event.dphijet2met_cut'
#
#mvaDic['dymva_dnn_2j']['inputVars']['PV_npvsGood']     = 'event.PV_npvsGood'
#mvaDic['dymva_dnn_2j']['inputVars']['upara']           = 'event.upara'
#mvaDic['dymva_dnn_2j']['inputVars']['mth']             = 'event.mth'
#mvaDic['dymva_dnn_2j']['inputVars']['ptTOT_cut']       = 'event.ptTOT_cut'
#mvaDic['dymva_dnn_2j']['inputVars']['uperp']           = 'event.uperp'
#mvaDic['dymva_dnn_2j']['inputVars']['dphilljet_cut']   = 'event.dphilljet_cut'
#mvaDic['dymva_dnn_2j']['inputVars']['ptll']            = 'event.ptll'
#mvaDic['dymva_dnn_2j']['inputVars']['PfMetDivSumMet']  = 'event.PfMetDivSumMet'
#mvaDic['dymva_dnn_2j']['inputVars']['mpmet']           = 'event.mpmet'
#mvaDic['dymva_dnn_2j']['inputVars']['dphilljetjet_cut']= 'event.dphilljetjet_cut'
#mvaDic['dymva_dnn_2j']['inputVars']['dphijet1met_cut'] = 'event.dphijet1met_cut'
#mvaDic['dymva_dnn_2j']['inputVars']['dphijet2met_cut'] = 'event.dphijet2met_cut'
#
##VBF
#mvaDic['dymva_bdt_VBF']['inputVars']['PfMetDivSumMet'] = 'event.PfMetDivSumMet'
#mvaDic['dymva_bdt_VBF']['inputVars']['mtw2']           = 'event.mtw2'
#mvaDic['dymva_bdt_VBF']['inputVars']['dphijet2met_cut']= 'event.dphijet2met_cut'
#mvaDic['dymva_bdt_VBF']['inputVars']['ptTOT_cut']      = 'event.ptTOT_cut'
#mvaDic['dymva_bdt_VBF']['inputVars']['mTOT_cut']       = 'event.mTOT_cut'
#mvaDic['dymva_bdt_VBF']['inputVars']['Ceta_cut']       = 'event.Ceta_cut'
#mvaDic['dymva_bdt_VBF']['inputVars']['jetpt2_cut']     = 'event.jetpt2_cut'
#mvaDic['dymva_bdt_VBF']['inputVars']['projtkmet']      = 'event.projtkmet'
#mvaDic['dymva_bdt_VBF']['inputVars']['PuppiMET_pt']    = 'event.PuppiMET_pt'
#mvaDic['dymva_bdt_VBF']['inputVars']['dphilmet1']      = 'event.dphilmet1'
#mvaDic['dymva_bdt_VBF']['inputVars']['dphillmet']      = 'event.dphillmet'
#mvaDic['dymva_bdt_VBF']['inputVars']['dphilmet2']      = 'event.dphilmet2'
#
#mvaDic['dymva_dnn_VBF']['inputVars']['PfMetDivSumMet'] = 'event.PfMetDivSumMet'
#mvaDic['dymva_dnn_VBF']['inputVars']['mtw2']           = 'event.mtw2'
#mvaDic['dymva_dnn_VBF']['inputVars']['dphijet2met_cut']= 'event.dphijet2met_cut'
#mvaDic['dymva_dnn_VBF']['inputVars']['ptTOT_cut']      = 'event.ptTOT_cut'
#mvaDic['dymva_dnn_VBF']['inputVars']['mTOT_cut']       = 'event.mTOT_cut'
#mvaDic['dymva_dnn_VBF']['inputVars']['Ceta_cut']       = 'event.Ceta_cut'
#mvaDic['dymva_dnn_VBF']['inputVars']['jetpt2_cut']     = 'event.jetpt2_cut'
#mvaDic['dymva_dnn_VBF']['inputVars']['projtkmet']      = 'event.projtkmet'
#mvaDic['dymva_dnn_VBF']['inputVars']['PuppiMET_pt']    = 'event.PuppiMET_pt'
#mvaDic['dymva_dnn_VBF']['inputVars']['dphilmet1']      = 'event.dphilmet1'
#mvaDic['dymva_dnn_VBF']['inputVars']['dphillmet']      = 'event.dphillmet'
#mvaDic['dymva_dnn_VBF']['inputVars']['dphilmet2']      = 'event.dphilmet2'
