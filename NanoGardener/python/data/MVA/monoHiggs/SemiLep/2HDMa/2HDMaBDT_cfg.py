from collections import OrderedDict

mvaDic = {}


mvaDic['MHlnjj_2HDMaBDT_Grad21VarSR'] = {
                          'type'      : 'BDT' ,  
                          'xmlFile'   : 'LatinoAnalysis/NanoGardener/python/data/MVA/monoHiggs/SemiLep/2HDMa/UATmva_2HDMaWjetsSReta_2017_BDT_800Trees_Grad_FalseBagged_0.6BagFrac_1BagShrink_GiniIndex_20Cuts_CostComplexity_12PruneStrength_21Var.weights.xml' ,
                          'inputVars' : OrderedDict() ,
                         }
mvaDic['MHlnjj_2HDMaBDT_Grad18VarSR'] = {
                          'type'      : 'BDT' ,  
                          'xmlFile'   : 'LatinoAnalysis/NanoGardener/python/data/MVA/monoHiggs/SemiLep/2HDMa/UATmva_2HDMaWjetsSReta_2017_BDT_1600Trees_Grad_FalseBagged_0.6BagFrac_1BagShrink_GiniIndex_20Cuts_CostComplexity_12PruneStrength_18Var.weights.xml' ,
                          'inputVars' : OrderedDict() ,
                         }

mvaDic['MHlnjj_2HDMaBDT_Grad15VarSR'] = {
                          'type'      : 'BDT' ,  
                          'xmlFile'   : 'LatinoAnalysis/NanoGardener/python/data/MVA/monoHiggs/SemiLep/2HDMa/UATmva_2HDMaWjetsSReta_2017_BDT_700Trees_Grad_FalseBagged_0.6BagFrac_1BagShrink_GiniIndex_20Cuts_CostComplexity_12PruneStrength_15Var.weights.xml' ,
                          'inputVars' : OrderedDict() ,
                         }

mvaDic['MHlnjj_2HDMaBDT_Ada21VarSR'] = {
                          'type'      : 'BDT' ,  
                          'xmlFile'   : 'LatinoAnalysis/NanoGardener/python/data/MVA/monoHiggs/SemiLep/2HDMa/UATmva_2HDMaWjetsSRetaAda_2017_BDT_35Trees_AdaBoost_GiniIndex_20Cuts_CostComplexity_12PruneStrength_21Var.weights.xml' ,
                          'inputVars' : OrderedDict() ,
                         }

mvaDic['MHlnjj_darkHiggsBDT_Grad21VarSR100'] = {
                          'type'      : 'BDT' ,  
                          'xmlFile'   : 'LatinoAnalysis/NanoGardener/python/data/MVA/monoHiggs/SemiLep/2HDMa/UATmva_darkHiggsWjetsSReta_2017_BDT_100Trees_Grad_FalseBagged_0.6BagFrac_1BagShrink_GiniIndex_20Cuts_CostComplexity_12PruneStrength_21Var.weights.xml' ,
                          'inputVars' : OrderedDict() ,
                         }
mvaDic['MHlnjj_darkHiggsBDT_Grad21VarSR600'] = {
                          'type'      : 'BDT' ,  
                          'xmlFile'   : 'LatinoAnalysis/NanoGardener/python/data/MVA/monoHiggs/SemiLep/2HDMa/UATmva_darkHiggsWjetsSReta_2017_BDT_600Trees_Grad_FalseBagged_0.6BagFrac_1BagShrink_GiniIndex_20Cuts_CostComplexity_12PruneStrength_21Var.weights.xml' ,
                          'inputVars' : OrderedDict() ,
                         }
mvaDic['MHlnjj_darkHiggsBDT_Ada21VarSR'] = {
                          'type'      : 'BDT' ,  
                          'xmlFile'   : 'LatinoAnalysis/NanoGardener/python/data/MVA/monoHiggs/SemiLep/2HDMa/UATmva_darkHiggsWjetsSReta_2017_BDT_25Trees_AdaBoost_GiniIndex_20Cuts_CostComplexity_12PruneStrength_21Var.weights.xml' ,
                          'inputVars' : OrderedDict() ,
                         }

#--- Variables

#mvaDic['MHlnjj_2HDMaBDT']['inputVars']['mtw1']                     ='event.mtw1'
#mvaDic['MHlnjj_2HDMaBDT']['inputVars']['MHlnjj_dr_ljjVmet']        ='event.MHlnjj_dr_ljjVmet'
#mvaDic['MHlnjj_2HDMaBDT']['inputVars']['MHlnjj_dphi_ljjVmet']      ='event.MHlnjj_dphi_ljjVmet'
#mvaDic['MHlnjj_2HDMaBDT']['inputVars']['MHlnjj_dr_jjVl']           ='event.MHlnjj_dr_jjVl'
#mvaDic['MHlnjj_2HDMaBDT']['inputVars']['MHlnjj_dphi_jjVl']         ='event.MHlnjj_dphi_jjVl'
#mvaDic['MHlnjj_2HDMaBDT']['inputVars']['MHlnjj_dphi_lVmet']        ='event.MHlnjj_dphi_lVmet'
#mvaDic['MHlnjj_2HDMaBDT']['inputVars']['MHlnjj_dr_lVmet']          ='event.MHlnjj_dr_lVmet'
#mvaDic['MHlnjj_2HDMaBDT']['inputVars']['PuppiMET_pt']              ='event.PuppiMET_pt'
#mvaDic['MHlnjj_2HDMaBDT']['inputVars']['MHlnjj_pt_ljj']            ='event.MHlnjj_pt_ljj'
#mvaDic['MHlnjj_2HDMaBDT']['inputVars']['MHlnjj_m_lmetjj']          ='event.MHlnjj_m_lmetjj'
#mvaDic['MHlnjj_2HDMaBDT']['inputVars']['MHlnjj_PTljj_D_PTmet']     ='event.MHlnjj_PTljj_D_PTmet'
#mvaDic['MHlnjj_2HDMaBDT']['inputVars']['MHlnjj_PTljj_D_Mlmetjj']   ='event.MHlnjj_PTljj_D_Mlmetjj'
#mvaDic['MHlnjj_2HDMaBDT']['inputVars']['MHlnjj_MINPTlj_D_PTmet']   ='event.MHlnjj_MINPTlj_D_PTmet'
#mvaDic['MHlnjj_2HDMaBDT']['inputVars']['MHlnjj_MINPTlj_D_Mlmetjj'] ='event.MHlnjj_MINPTlj_D_Mlmetjj'
#mvaDic['MHlnjj_2HDMaBDT']['inputVars']['MHlnjj_dphi_jVj']          ='event.MHlnjj_dphi_jVj'
#mvaDic['MHlnjj_2HDMaBDT']['inputVars']['MHlnjj_dr_jVj']            ='event.MHlnjj_dr_jVj'
#mvaDic['MHlnjj_2HDMaBDT']['inputVars']['MHlnjj_m_jj']              ='event.MHlnjj_m_jj'
#mvaDic['MHlnjj_2HDMaBDT']['inputVars']['MHlnjj_m_ljj']             ='event.MHlnjj_m_ljj'

mvaDic['MHlnjj_2HDMaBDT_Grad18VarSR']['inputVars']['mtw1']                     ='event.mtw1'
mvaDic['MHlnjj_2HDMaBDT_Grad18VarSR']['inputVars']['MHlnjj_deta_ljjVmet']      ='event.MHlnjj_deta_ljjVmet'
mvaDic['MHlnjj_2HDMaBDT_Grad18VarSR']['inputVars']['MHlnjj_dphi_ljjVmet']      ='event.MHlnjj_dphi_ljjVmet'
mvaDic['MHlnjj_2HDMaBDT_Grad18VarSR']['inputVars']['MHlnjj_deta_jjVl']         ='event.MHlnjj_deta_jjVl'
mvaDic['MHlnjj_2HDMaBDT_Grad18VarSR']['inputVars']['MHlnjj_dphi_jjVl']         ='event.MHlnjj_dphi_jjVl'
mvaDic['MHlnjj_2HDMaBDT_Grad18VarSR']['inputVars']['MHlnjj_dphi_lVmet']        ='event.MHlnjj_dphi_lVmet'
mvaDic['MHlnjj_2HDMaBDT_Grad18VarSR']['inputVars']['MHlnjj_deta_lVmet']        ='event.MHlnjj_deta_lVmet'
mvaDic['MHlnjj_2HDMaBDT_Grad18VarSR']['inputVars']['PuppiMET_pt']              ='event.PuppiMET_pt'
mvaDic['MHlnjj_2HDMaBDT_Grad18VarSR']['inputVars']['MHlnjj_pt_ljj']            ='event.MHlnjj_pt_ljj'
mvaDic['MHlnjj_2HDMaBDT_Grad18VarSR']['inputVars']['MHlnjj_m_lmetjj']          ='event.MHlnjj_m_lmetjj'
mvaDic['MHlnjj_2HDMaBDT_Grad18VarSR']['inputVars']['MHlnjj_PTljj_D_PTmet']     ='event.MHlnjj_PTljj_D_PTmet'
mvaDic['MHlnjj_2HDMaBDT_Grad18VarSR']['inputVars']['MHlnjj_PTljj_D_Mlmetjj']   ='event.MHlnjj_PTljj_D_Mlmetjj'
mvaDic['MHlnjj_2HDMaBDT_Grad18VarSR']['inputVars']['MHlnjj_MINPTlj_D_PTmet']   ='event.MHlnjj_MINPTlj_D_PTmet'
mvaDic['MHlnjj_2HDMaBDT_Grad18VarSR']['inputVars']['MHlnjj_MINPTlj_D_Mlmetjj'] ='event.MHlnjj_MINPTlj_D_Mlmetjj'
mvaDic['MHlnjj_2HDMaBDT_Grad18VarSR']['inputVars']['MHlnjj_dphi_jVj']          ='event.MHlnjj_dphi_jVj'
mvaDic['MHlnjj_2HDMaBDT_Grad18VarSR']['inputVars']['MHlnjj_deta_jVj']           ='event.MHlnjj_deta_jVj'
mvaDic['MHlnjj_2HDMaBDT_Grad18VarSR']['inputVars']['MHlnjj_m_jj']              ='event.MHlnjj_m_jj'
mvaDic['MHlnjj_2HDMaBDT_Grad18VarSR']['inputVars']['MHlnjj_m_ljj']             ='event.MHlnjj_m_ljj'

mvaDic['MHlnjj_2HDMaBDT_Grad15VarSR']['inputVars']['mtw1']                    ='event.mtw1'
mvaDic['MHlnjj_2HDMaBDT_Grad15VarSR']['inputVars']['MHlnjj_deta_ljjVmet']     ='event.MHlnjj_deta_ljjVmet'
mvaDic['MHlnjj_2HDMaBDT_Grad15VarSR']['inputVars']['MHlnjj_deta_jjVl']        ='event.MHlnjj_deta_jjVl'
mvaDic['MHlnjj_2HDMaBDT_Grad15VarSR']['inputVars']['MHlnjj_dphi_jjVl']        ='event.MHlnjj_dphi_jjVl'
mvaDic['MHlnjj_2HDMaBDT_Grad15VarSR']['inputVars']['MHlnjj_dphi_lVmet']       ='event.MHlnjj_dphi_lVmet'
mvaDic['MHlnjj_2HDMaBDT_Grad15VarSR']['inputVars']['MHlnjj_deta_lVmet']       ='event.MHlnjj_deta_lVmet'
mvaDic['MHlnjj_2HDMaBDT_Grad15VarSR']['inputVars']['PuppiMET_pt']             ='event.PuppiMET_pt'
mvaDic['MHlnjj_2HDMaBDT_Grad15VarSR']['inputVars']['MHlnjj_pt_ljj']           ='event.MHlnjj_pt_ljj'
mvaDic['MHlnjj_2HDMaBDT_Grad15VarSR']['inputVars']['MHlnjj_m_lmetjj']         ='event.MHlnjj_m_lmetjj'
mvaDic['MHlnjj_2HDMaBDT_Grad15VarSR']['inputVars']['MHlnjj_PTljj_D_Mlmetjj']  ='event.MHlnjj_PTljj_D_Mlmetjj'
mvaDic['MHlnjj_2HDMaBDT_Grad15VarSR']['inputVars']['MHlnjj_MINPTlj_D_PTmet']  ='event.MHlnjj_MINPTlj_D_PTmet'
mvaDic['MHlnjj_2HDMaBDT_Grad15VarSR']['inputVars']['MHlnjj_m_jj']             ='event.MHlnjj_m_jj'
mvaDic['MHlnjj_2HDMaBDT_Grad15VarSR']['inputVars']['MHlnjj_m_ljj']            ='event.MHlnjj_m_ljj'
mvaDic['MHlnjj_2HDMaBDT_Grad15VarSR']['inputVars']['MHlnjj_MAXPTlj_D_PTmet']  ='event.MHlnjj_MAXPTlj_D_PTmet'
mvaDic['MHlnjj_2HDMaBDT_Grad15VarSR']['inputVars']['MHlnjj_MTljj_D_PTmet']    ='event.MHlnjj_MTljj_D_PTmet'   

mvaDic['MHlnjj_2HDMaBDT_Ada21VarSR']['inputVars']['mtw1']                     ='event.mtw1'  
mvaDic['MHlnjj_2HDMaBDT_Ada21VarSR']['inputVars']['MHlnjj_deta_ljjVmet']      ='event.MHlnjj_deta_ljjVmet'
mvaDic['MHlnjj_2HDMaBDT_Ada21VarSR']['inputVars']['MHlnjj_dphi_ljjVmet']      ='event.MHlnjj_dphi_ljjVmet'
mvaDic['MHlnjj_2HDMaBDT_Ada21VarSR']['inputVars']['MHlnjj_deta_jjVl']         ='event.MHlnjj_deta_jjVl'
mvaDic['MHlnjj_2HDMaBDT_Ada21VarSR']['inputVars']['MHlnjj_dphi_jjVl']         ='event.MHlnjj_dphi_jjVl'
mvaDic['MHlnjj_2HDMaBDT_Ada21VarSR']['inputVars']['MHlnjj_dphi_lVmet']        ='event.MHlnjj_dphi_lVmet'
mvaDic['MHlnjj_2HDMaBDT_Ada21VarSR']['inputVars']['MHlnjj_deta_lVmet']        ='event.MHlnjj_deta_lVmet'
mvaDic['MHlnjj_2HDMaBDT_Ada21VarSR']['inputVars']['PuppiMET_pt']              ='event.PuppiMET_pt'
mvaDic['MHlnjj_2HDMaBDT_Ada21VarSR']['inputVars']['MHlnjj_pt_ljj']            ='event.MHlnjj_pt_ljj'
mvaDic['MHlnjj_2HDMaBDT_Ada21VarSR']['inputVars']['MHlnjj_m_lmetjj']          ='event.MHlnjj_m_lmetjj'
mvaDic['MHlnjj_2HDMaBDT_Ada21VarSR']['inputVars']['MHlnjj_PTljj_D_PTmet']     ='event.MHlnjj_PTljj_D_PTmet'
mvaDic['MHlnjj_2HDMaBDT_Ada21VarSR']['inputVars']['MHlnjj_PTljj_D_Mlmetjj']   ='event.MHlnjj_PTljj_D_Mlmetjj' 
mvaDic['MHlnjj_2HDMaBDT_Ada21VarSR']['inputVars']['MHlnjj_MINPTlj_D_PTmet']   ='event.MHlnjj_MINPTlj_D_PTmet'
mvaDic['MHlnjj_2HDMaBDT_Ada21VarSR']['inputVars']['MHlnjj_MINPTlj_D_Mlmetjj'] ='event.MHlnjj_MINPTlj_D_Mlmetjj'
mvaDic['MHlnjj_2HDMaBDT_Ada21VarSR']['inputVars']['MHlnjj_dphi_jVj']          ='event.MHlnjj_dphi_jVj'
mvaDic['MHlnjj_2HDMaBDT_Ada21VarSR']['inputVars']['MHlnjj_deta_jVj']          ='event.MHlnjj_deta_jVj'
mvaDic['MHlnjj_2HDMaBDT_Ada21VarSR']['inputVars']['MHlnjj_m_jj']              ='event.MHlnjj_m_jj'
mvaDic['MHlnjj_2HDMaBDT_Ada21VarSR']['inputVars']['MHlnjj_m_ljj']             ='event.MHlnjj_m_ljj'
mvaDic['MHlnjj_2HDMaBDT_Ada21VarSR']['inputVars']['MHlnjj_MAXPTlj_D_PTmet']   ='event.MHlnjj_MAXPTlj_D_PTmet'
mvaDic['MHlnjj_2HDMaBDT_Ada21VarSR']['inputVars']['MHlnjj_MTljj_D_PTmet']     ='event.MHlnjj_MTljj_D_PTmet'
mvaDic['MHlnjj_2HDMaBDT_Ada21VarSR']['inputVars']['MHlnjj_MTljj_D_Mlmetjj']   ='event.MHlnjj_MTljj_D_Mlmetjj'

mvaDic['MHlnjj_2HDMaBDT_Grad21VarSR']['inputVars']['mtw1']                     ='event.mtw1'  
mvaDic['MHlnjj_2HDMaBDT_Grad21VarSR']['inputVars']['MHlnjj_deta_ljjVmet']      ='event.MHlnjj_deta_ljjVmet'
mvaDic['MHlnjj_2HDMaBDT_Grad21VarSR']['inputVars']['MHlnjj_dphi_ljjVmet']      ='event.MHlnjj_dphi_ljjVmet'
mvaDic['MHlnjj_2HDMaBDT_Grad21VarSR']['inputVars']['MHlnjj_deta_jjVl']         ='event.MHlnjj_deta_jjVl'
mvaDic['MHlnjj_2HDMaBDT_Grad21VarSR']['inputVars']['MHlnjj_dphi_jjVl']         ='event.MHlnjj_dphi_jjVl'
mvaDic['MHlnjj_2HDMaBDT_Grad21VarSR']['inputVars']['MHlnjj_dphi_lVmet']        ='event.MHlnjj_dphi_lVmet'
mvaDic['MHlnjj_2HDMaBDT_Grad21VarSR']['inputVars']['MHlnjj_deta_lVmet']        ='event.MHlnjj_deta_lVmet'
mvaDic['MHlnjj_2HDMaBDT_Grad21VarSR']['inputVars']['PuppiMET_pt']              ='event.PuppiMET_pt'
mvaDic['MHlnjj_2HDMaBDT_Grad21VarSR']['inputVars']['MHlnjj_pt_ljj']            ='event.MHlnjj_pt_ljj'
mvaDic['MHlnjj_2HDMaBDT_Grad21VarSR']['inputVars']['MHlnjj_m_lmetjj']          ='event.MHlnjj_m_lmetjj'
mvaDic['MHlnjj_2HDMaBDT_Grad21VarSR']['inputVars']['MHlnjj_PTljj_D_PTmet']     ='event.MHlnjj_PTljj_D_PTmet'
mvaDic['MHlnjj_2HDMaBDT_Grad21VarSR']['inputVars']['MHlnjj_PTljj_D_Mlmetjj']   ='event.MHlnjj_PTljj_D_Mlmetjj' 
mvaDic['MHlnjj_2HDMaBDT_Grad21VarSR']['inputVars']['MHlnjj_MINPTlj_D_PTmet']   ='event.MHlnjj_MINPTlj_D_PTmet'
mvaDic['MHlnjj_2HDMaBDT_Grad21VarSR']['inputVars']['MHlnjj_MINPTlj_D_Mlmetjj'] ='event.MHlnjj_MINPTlj_D_Mlmetjj'
mvaDic['MHlnjj_2HDMaBDT_Grad21VarSR']['inputVars']['MHlnjj_dphi_jVj']          ='event.MHlnjj_dphi_jVj'
mvaDic['MHlnjj_2HDMaBDT_Grad21VarSR']['inputVars']['MHlnjj_deta_jVj']          ='event.MHlnjj_deta_jVj'
mvaDic['MHlnjj_2HDMaBDT_Grad21VarSR']['inputVars']['MHlnjj_m_jj']              ='event.MHlnjj_m_jj'
mvaDic['MHlnjj_2HDMaBDT_Grad21VarSR']['inputVars']['MHlnjj_m_ljj']             ='event.MHlnjj_m_ljj'
mvaDic['MHlnjj_2HDMaBDT_Grad21VarSR']['inputVars']['MHlnjj_MAXPTlj_D_PTmet']   ='event.MHlnjj_MAXPTlj_D_PTmet'
mvaDic['MHlnjj_2HDMaBDT_Grad21VarSR']['inputVars']['MHlnjj_MTljj_D_PTmet']     ='event.MHlnjj_MTljj_D_PTmet'
mvaDic['MHlnjj_2HDMaBDT_Grad21VarSR']['inputVars']['MHlnjj_MTljj_D_Mlmetjj']   ='event.MHlnjj_MTljj_D_Mlmetjj'

mvaDic['MHlnjj_darkHiggsBDT_Grad21VarSR100']['inputVars']['mtw1']                     ='event.mtw1'  
mvaDic['MHlnjj_darkHiggsBDT_Grad21VarSR100']['inputVars']['MHlnjj_deta_ljjVmet']      ='event.MHlnjj_deta_ljjVmet'
mvaDic['MHlnjj_darkHiggsBDT_Grad21VarSR100']['inputVars']['MHlnjj_dphi_ljjVmet']      ='event.MHlnjj_dphi_ljjVmet'
mvaDic['MHlnjj_darkHiggsBDT_Grad21VarSR100']['inputVars']['MHlnjj_deta_jjVl']         ='event.MHlnjj_deta_jjVl'
mvaDic['MHlnjj_darkHiggsBDT_Grad21VarSR100']['inputVars']['MHlnjj_dphi_jjVl']         ='event.MHlnjj_dphi_jjVl'
mvaDic['MHlnjj_darkHiggsBDT_Grad21VarSR100']['inputVars']['MHlnjj_dphi_lVmet']        ='event.MHlnjj_dphi_lVmet'
mvaDic['MHlnjj_darkHiggsBDT_Grad21VarSR100']['inputVars']['MHlnjj_deta_lVmet']        ='event.MHlnjj_deta_lVmet'
mvaDic['MHlnjj_darkHiggsBDT_Grad21VarSR100']['inputVars']['PuppiMET_pt']              ='event.PuppiMET_pt'
mvaDic['MHlnjj_darkHiggsBDT_Grad21VarSR100']['inputVars']['MHlnjj_pt_ljj']            ='event.MHlnjj_pt_ljj'
mvaDic['MHlnjj_darkHiggsBDT_Grad21VarSR100']['inputVars']['MHlnjj_m_lmetjj']          ='event.MHlnjj_m_lmetjj'
mvaDic['MHlnjj_darkHiggsBDT_Grad21VarSR100']['inputVars']['MHlnjj_PTljj_D_PTmet']     ='event.MHlnjj_PTljj_D_PTmet'
mvaDic['MHlnjj_darkHiggsBDT_Grad21VarSR100']['inputVars']['MHlnjj_PTljj_D_Mlmetjj']   ='event.MHlnjj_PTljj_D_Mlmetjj' 
mvaDic['MHlnjj_darkHiggsBDT_Grad21VarSR100']['inputVars']['MHlnjj_MINPTlj_D_PTmet']   ='event.MHlnjj_MINPTlj_D_PTmet'
mvaDic['MHlnjj_darkHiggsBDT_Grad21VarSR100']['inputVars']['MHlnjj_MINPTlj_D_Mlmetjj'] ='event.MHlnjj_MINPTlj_D_Mlmetjj'
mvaDic['MHlnjj_darkHiggsBDT_Grad21VarSR100']['inputVars']['MHlnjj_dphi_jVj']          ='event.MHlnjj_dphi_jVj'
mvaDic['MHlnjj_darkHiggsBDT_Grad21VarSR100']['inputVars']['MHlnjj_deta_jVj']          ='event.MHlnjj_deta_jVj'
mvaDic['MHlnjj_darkHiggsBDT_Grad21VarSR100']['inputVars']['MHlnjj_m_jj']              ='event.MHlnjj_m_jj'
mvaDic['MHlnjj_darkHiggsBDT_Grad21VarSR100']['inputVars']['MHlnjj_m_ljj']             ='event.MHlnjj_m_ljj'
mvaDic['MHlnjj_darkHiggsBDT_Grad21VarSR100']['inputVars']['MHlnjj_MAXPTlj_D_PTmet']   ='event.MHlnjj_MAXPTlj_D_PTmet'
mvaDic['MHlnjj_darkHiggsBDT_Grad21VarSR100']['inputVars']['MHlnjj_MTljj_D_PTmet']     ='event.MHlnjj_MTljj_D_PTmet'
mvaDic['MHlnjj_darkHiggsBDT_Grad21VarSR100']['inputVars']['MHlnjj_MTljj_D_Mlmetjj']   ='event.MHlnjj_MTljj_D_Mlmetjj'

mvaDic['MHlnjj_darkHiggsBDT_Grad21VarSR600']['inputVars']['mtw1']                     ='event.mtw1'  
mvaDic['MHlnjj_darkHiggsBDT_Grad21VarSR600']['inputVars']['MHlnjj_deta_ljjVmet']      ='event.MHlnjj_deta_ljjVmet'
mvaDic['MHlnjj_darkHiggsBDT_Grad21VarSR600']['inputVars']['MHlnjj_dphi_ljjVmet']      ='event.MHlnjj_dphi_ljjVmet'
mvaDic['MHlnjj_darkHiggsBDT_Grad21VarSR600']['inputVars']['MHlnjj_deta_jjVl']         ='event.MHlnjj_deta_jjVl'
mvaDic['MHlnjj_darkHiggsBDT_Grad21VarSR600']['inputVars']['MHlnjj_dphi_jjVl']         ='event.MHlnjj_dphi_jjVl'
mvaDic['MHlnjj_darkHiggsBDT_Grad21VarSR600']['inputVars']['MHlnjj_dphi_lVmet']        ='event.MHlnjj_dphi_lVmet'
mvaDic['MHlnjj_darkHiggsBDT_Grad21VarSR600']['inputVars']['MHlnjj_deta_lVmet']        ='event.MHlnjj_deta_lVmet'
mvaDic['MHlnjj_darkHiggsBDT_Grad21VarSR600']['inputVars']['PuppiMET_pt']              ='event.PuppiMET_pt'
mvaDic['MHlnjj_darkHiggsBDT_Grad21VarSR600']['inputVars']['MHlnjj_pt_ljj']            ='event.MHlnjj_pt_ljj'
mvaDic['MHlnjj_darkHiggsBDT_Grad21VarSR600']['inputVars']['MHlnjj_m_lmetjj']          ='event.MHlnjj_m_lmetjj'
mvaDic['MHlnjj_darkHiggsBDT_Grad21VarSR600']['inputVars']['MHlnjj_PTljj_D_PTmet']     ='event.MHlnjj_PTljj_D_PTmet'
mvaDic['MHlnjj_darkHiggsBDT_Grad21VarSR600']['inputVars']['MHlnjj_PTljj_D_Mlmetjj']   ='event.MHlnjj_PTljj_D_Mlmetjj' 
mvaDic['MHlnjj_darkHiggsBDT_Grad21VarSR600']['inputVars']['MHlnjj_MINPTlj_D_PTmet']   ='event.MHlnjj_MINPTlj_D_PTmet'
mvaDic['MHlnjj_darkHiggsBDT_Grad21VarSR600']['inputVars']['MHlnjj_MINPTlj_D_Mlmetjj'] ='event.MHlnjj_MINPTlj_D_Mlmetjj'
mvaDic['MHlnjj_darkHiggsBDT_Grad21VarSR600']['inputVars']['MHlnjj_dphi_jVj']          ='event.MHlnjj_dphi_jVj'
mvaDic['MHlnjj_darkHiggsBDT_Grad21VarSR600']['inputVars']['MHlnjj_deta_jVj']          ='event.MHlnjj_deta_jVj'
mvaDic['MHlnjj_darkHiggsBDT_Grad21VarSR600']['inputVars']['MHlnjj_m_jj']              ='event.MHlnjj_m_jj'
mvaDic['MHlnjj_darkHiggsBDT_Grad21VarSR600']['inputVars']['MHlnjj_m_ljj']             ='event.MHlnjj_m_ljj'
mvaDic['MHlnjj_darkHiggsBDT_Grad21VarSR600']['inputVars']['MHlnjj_MAXPTlj_D_PTmet']   ='event.MHlnjj_MAXPTlj_D_PTmet'
mvaDic['MHlnjj_darkHiggsBDT_Grad21VarSR600']['inputVars']['MHlnjj_MTljj_D_PTmet']     ='event.MHlnjj_MTljj_D_PTmet'
mvaDic['MHlnjj_darkHiggsBDT_Grad21VarSR600']['inputVars']['MHlnjj_MTljj_D_Mlmetjj']   ='event.MHlnjj_MTljj_D_Mlmetjj'

mvaDic['MHlnjj_darkHiggsBDT_Ada21VarSR']['inputVars']['mtw1']                     ='event.mtw1'  
mvaDic['MHlnjj_darkHiggsBDT_Ada21VarSR']['inputVars']['MHlnjj_deta_ljjVmet']      ='event.MHlnjj_deta_ljjVmet'
mvaDic['MHlnjj_darkHiggsBDT_Ada21VarSR']['inputVars']['MHlnjj_dphi_ljjVmet']      ='event.MHlnjj_dphi_ljjVmet'
mvaDic['MHlnjj_darkHiggsBDT_Ada21VarSR']['inputVars']['MHlnjj_deta_jjVl']         ='event.MHlnjj_deta_jjVl'
mvaDic['MHlnjj_darkHiggsBDT_Ada21VarSR']['inputVars']['MHlnjj_dphi_jjVl']         ='event.MHlnjj_dphi_jjVl'
mvaDic['MHlnjj_darkHiggsBDT_Ada21VarSR']['inputVars']['MHlnjj_dphi_lVmet']        ='event.MHlnjj_dphi_lVmet'
mvaDic['MHlnjj_darkHiggsBDT_Ada21VarSR']['inputVars']['MHlnjj_deta_lVmet']        ='event.MHlnjj_deta_lVmet'
mvaDic['MHlnjj_darkHiggsBDT_Ada21VarSR']['inputVars']['PuppiMET_pt']              ='event.PuppiMET_pt'
mvaDic['MHlnjj_darkHiggsBDT_Ada21VarSR']['inputVars']['MHlnjj_pt_ljj']            ='event.MHlnjj_pt_ljj'
mvaDic['MHlnjj_darkHiggsBDT_Ada21VarSR']['inputVars']['MHlnjj_m_lmetjj']          ='event.MHlnjj_m_lmetjj'
mvaDic['MHlnjj_darkHiggsBDT_Ada21VarSR']['inputVars']['MHlnjj_PTljj_D_PTmet']     ='event.MHlnjj_PTljj_D_PTmet'
mvaDic['MHlnjj_darkHiggsBDT_Ada21VarSR']['inputVars']['MHlnjj_PTljj_D_Mlmetjj']   ='event.MHlnjj_PTljj_D_Mlmetjj' 
mvaDic['MHlnjj_darkHiggsBDT_Ada21VarSR']['inputVars']['MHlnjj_MINPTlj_D_PTmet']   ='event.MHlnjj_MINPTlj_D_PTmet'
mvaDic['MHlnjj_darkHiggsBDT_Ada21VarSR']['inputVars']['MHlnjj_MINPTlj_D_Mlmetjj'] ='event.MHlnjj_MINPTlj_D_Mlmetjj'
mvaDic['MHlnjj_darkHiggsBDT_Ada21VarSR']['inputVars']['MHlnjj_dphi_jVj']          ='event.MHlnjj_dphi_jVj'
mvaDic['MHlnjj_darkHiggsBDT_Ada21VarSR']['inputVars']['MHlnjj_deta_jVj']          ='event.MHlnjj_deta_jVj'
mvaDic['MHlnjj_darkHiggsBDT_Ada21VarSR']['inputVars']['MHlnjj_m_jj']              ='event.MHlnjj_m_jj'
mvaDic['MHlnjj_darkHiggsBDT_Ada21VarSR']['inputVars']['MHlnjj_m_ljj']             ='event.MHlnjj_m_ljj'
mvaDic['MHlnjj_darkHiggsBDT_Ada21VarSR']['inputVars']['MHlnjj_MAXPTlj_D_PTmet']   ='event.MHlnjj_MAXPTlj_D_PTmet'
mvaDic['MHlnjj_darkHiggsBDT_Ada21VarSR']['inputVars']['MHlnjj_MTljj_D_PTmet']     ='event.MHlnjj_MTljj_D_PTmet'
mvaDic['MHlnjj_darkHiggsBDT_Ada21VarSR']['inputVars']['MHlnjj_MTljj_D_Mlmetjj']   ='event.MHlnjj_MTljj_D_Mlmetjj'
