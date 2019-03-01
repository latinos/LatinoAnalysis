mvaDic = {}


mvaDic['dymva_bdt_0j'] = {
                          'type'      : 'BDT' ,  
                          'xmlFile'   : 'LatinoAnalysis/NanoGardener/python/data/DYSFmva/2017/UATmva_DYmva_2017_0j_BDT_400Trees_AdaBoost_GiniIndex_20Cuts_CostComplexity_12PruneStrength_12Var.weights.xml'   ,
                          'inputVars' : OrderedDict() ,
                         }

mvaDic['dymva_bdt_1j'] = {
                          'type'      : 'BDT' ,
                          'xmlFile'   : 'LatinoAnalysis/NanoGardener/python/data/DYSFmva/2017/UATmva_DYmva_2017_1j_BDT_400Trees_AdaBoost_GiniIndex_20Cuts_CostComplexity_12PruneStrength_12Var.weights.xml'   ,
                          'inputVars' : OrderedDict() ,
                         }

mvaDic['dymva_dnn_0j'] = {
                          'type'      : 'PyKeras' ,
                          'xmlFile'   : 'LatinoAnalysis/NanoGardener/python/data/DYSFmva/2017/TMVAClassification_PyKeras_2017_0j_m1.weights.xml'   ,
                          'inputVars' : OrderedDict() ,
                         }

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

mvaDic['dymva_dnn_0j']['inputVars']['ptll']           = 'event.ptll'
mvaDic['dymva_dnn_0j']['inputVars']['mth']            = 'event.mth'
mvaDic['dymva_dnn_0j']['inputVars']['jetpt1_cut']     = 'event.jetpt1_cut'
mvaDic['dymva_dnn_0j']['inputVars']['uperp']          = 'event.uperp'
mvaDic['dymva_dnn_0j']['inputVars']['PfMetDivSumMet'] = 'event.PfMetDivSumMet'
mvaDic['dymva_dnn_0j']['inputVars']['recoil']         = 'event.recoil'
mvaDic['dymva_dnn_0j']['inputVars']['mpmet']          = 'event.mpmet'
mvaDic['dymva_dnn_0j']['inputVars']['upara']          = 'event.upara'
mvaDic['dymva_dnn_0j']['inputVars']['dphilmet1']      = 'event.dphilmet1'
mvaDic['dymva_dnn_0j']['inputVars']['dphilmet2']      = 'event.dphilmet2'
mvaDic['dymva_dnn_0j']['inputVars']['dphilljet_cut']  = 'event.dphilljet_cut'
mvaDic['dymva_dnn_0j']['inputVars']['dphijet1met_cut']= 'event.dphijet1met_cut'

#1j
mvaDic['dymva_bdt_1j']['inputVars']['PV_npvsGood']    = 'event.PV_npvsGood'
mvaDic['dymva_bdt_1j']['inputVars']['ptll']           = 'event.ptll'
mvaDic['dymva_bdt_1j']['inputVars']['mpmet']          = 'event.mpmet'
mvaDic['dymva_bdt_1j']['inputVars']['upara']          = 'event.upara'
mvaDic['dymva_bdt_1j']['inputVars']['PfMetDivSumMet'] = 'event.PfMetDivSumMet'
mvaDic['dymva_bdt_1j']['inputVars']['mtw1']           = 'event.mtw1'
mvaDic['dymva_bdt_1j']['inputVars']['dphilmet1']      = 'event.dphilmet1'
mvaDic['dymva_bdt_1j']['inputVars']['dphilljet_cut']  = 'event.dphilljet_cut'
mvaDic['dymva_bdt_1j']['inputVars']['dphijet1met_cut']= 'event.dphijet1met_cut'
mvaDic['dymva_bdt_1j']['inputVars']['jetpt2_cut']     = 'event.jetpt2_cut'
mvaDic['dymva_bdt_1j']['inputVars']['dphilmet2']      = 'event.dphilmet2'
mvaDic['dymva_bdt_1j']['inputVars']['projpfmet']      = 'event.projpfmet'
