import copy
from collections import OrderedDict

mvaDic = {}


# 2HDMa
mvaDic['MHlnjj_2HDMaBDT_Grad22Var'] = {
    'type'      : 'BDT',
    'xmlFile'   : 'LatinoAnalysis/NanoGardener/python/data/MVA/monoHiggs/SemiLep/UATmva_2HDMaVWjets_2017_BDT_200Trees_Grad_FalseBagged_0.6BagFrac_1BagShrink_GiniIndex_20Cuts_CostComplexity_12PruneStrength_22Var.weights.xml',
    'inputVars' : OrderedDict(),
}
mvaDic['MHlnjj_2HDMaBDT_Grad15Var'] = {
    'type'      : 'BDT',
    'xmlFile'   : 'LatinoAnalysis/NanoGardener/python/data/MVA/monoHiggs/SemiLep/UATmva_2HDMaVWjets_2017_BDT_700Trees_Grad_FalseBagged_0.6BagFrac_1BagShrink_GiniIndex_20Cuts_CostComplexity_12PruneStrength_15Var.weights.xml',
    'inputVars' : OrderedDict(),
}
mvaDic['MHlnjj_2HDMaBDT_Grad12Var'] = {
    'type'      : 'BDT',
    'xmlFile'   : 'LatinoAnalysis/NanoGardener/python/data/MVA/monoHiggs/SemiLep/UATmva_2HDMaVWjets_2017_BDT_500Trees_Grad_FalseBagged_0.6BagFrac_1BagShrink_GiniIndex_20Cuts_CostComplexity_12PruneStrength_12Var.weights.xml',
    'inputVars' : OrderedDict(),
}

mvaDic['MHlnjj_2HDMaBDT_Ada22Var'] = {
    'type'      : 'BDT',
    'xmlFile'   : 'LatinoAnalysis/NanoGardener/python/data/MVA/monoHiggs/SemiLep/UATmva_2HDMaVWjets_2017_BDT_42Trees_AdaBoost_GiniIndex_20Cuts_CostComplexity_12PruneStrength_22Var.weights.xml',
    'inputVars' : OrderedDict(),
}
mvaDic['MHlnjj_2HDMaBDT_Ada15Var'] = {
    'type'      : 'BDT',
    'xmlFile'   : 'LatinoAnalysis/NanoGardener/python/data/MVA/monoHiggs/SemiLep/UATmva_2HDMaVWjets_2017_BDT_57Trees_AdaBoost_GiniIndex_20Cuts_CostComplexity_12PruneStrength_15Var.weights.xml',
    'inputVars' : OrderedDict(),
}
mvaDic['MHlnjj_2HDMaBDT_Ada12Var'] = {
    'type'      : 'BDT',
    'xmlFile'   : 'LatinoAnalysis/NanoGardener/python/data/MVA/monoHiggs/SemiLep/UATmva_2HDMaVWjets_2017_BDT_52Trees_AdaBoost_GiniIndex_20Cuts_CostComplexity_12PruneStrength_12Var.weights.xml',
    'inputVars' : OrderedDict(),
}

# darkHiggs
mvaDic['MHlnjj_darkHiggsBDT_Ada16Var'] = {
    'type'      : 'BDT',
    'xmlFile'   : 'LatinoAnalysis/NanoGardener/python/data/MVA/monoHiggs/SemiLep/UATmva_darkHiggsVWjets_2017_BDT_55Trees_AdaBoost_GiniIndex_20Cuts_CostComplexity_12PruneStrength_16Var.weights.xml', 
    'inputVars' : OrderedDict(),
}
mvaDic['MHlnjj_darkHiggsBDT_Grad16Var'] = {
    'type'      : 'BDT',
    'xmlFile'   : 'LatinoAnalysis/NanoGardener/python/data/MVA/monoHiggs/SemiLep/UATmva_darkHiggsVWjets_2017_BDT_1200Trees_Grad_FalseBagged_0.6BagFrac_1BagShrink_GiniIndex_20Cuts_CostComplexity_12PruneStrength_16Var.weights.xml', 
    'inputVars' : OrderedDict(),
}



#--- Variables

# 2HDMa
mvaDic['MHlnjj_2HDMaBDT_Grad22Var']['inputVars']['mtw1']                     = 'event.mtw1'
mvaDic['MHlnjj_2HDMaBDT_Grad22Var']['inputVars']['MHlnjj_deta_ljjVmet']      = 'event.MHlnjj_deta_ljjVmet'
mvaDic['MHlnjj_2HDMaBDT_Grad22Var']['inputVars']['MHlnjj_dphi_ljjVmet']      = 'event.MHlnjj_dphi_ljjVmet'
mvaDic['MHlnjj_2HDMaBDT_Grad22Var']['inputVars']['MHlnjj_deta_jjVl']         = 'event.MHlnjj_deta_jjVl'
mvaDic['MHlnjj_2HDMaBDT_Grad22Var']['inputVars']['MHlnjj_dphi_jjVl']         = 'event.MHlnjj_dphi_jjVl'
mvaDic['MHlnjj_2HDMaBDT_Grad22Var']['inputVars']['MHlnjj_dphi_lVmet']        = 'event.MHlnjj_dphi_lVmet'
mvaDic['MHlnjj_2HDMaBDT_Grad22Var']['inputVars']['MHlnjj_deta_lVmet']        = 'event.MHlnjj_deta_lVmet'
mvaDic['MHlnjj_2HDMaBDT_Grad22Var']['inputVars']['PuppiMET_pt']              = 'event.PuppiMET_pt'
mvaDic['MHlnjj_2HDMaBDT_Grad22Var']['inputVars']['MHlnjj_pt_ljj']            = 'event.MHlnjj_pt_ljj'
mvaDic['MHlnjj_2HDMaBDT_Grad22Var']['inputVars']['MHlnjj_m_lmetjj']          = 'event.MHlnjj_m_lmetjj'
mvaDic['MHlnjj_2HDMaBDT_Grad22Var']['inputVars']['MHlnjj_PTljj_D_PTmet']     = 'event.MHlnjj_PTljj_D_PTmet'
mvaDic['MHlnjj_2HDMaBDT_Grad22Var']['inputVars']['MHlnjj_PTljj_D_Mlmetjj']   = 'event.MHlnjj_PTljj_D_Mlmetjj'
mvaDic['MHlnjj_2HDMaBDT_Grad22Var']['inputVars']['MHlnjj_MINPTlj_D_PTmet']   = 'event.MHlnjj_MINPTlj_D_PTmet'
mvaDic['MHlnjj_2HDMaBDT_Grad22Var']['inputVars']['MHlnjj_MINPTlj_D_Mlmetjj'] = 'event.MHlnjj_MINPTlj_D_Mlmetjj'
mvaDic['MHlnjj_2HDMaBDT_Grad22Var']['inputVars']['MHlnjj_dphi_jVj']          = 'event.MHlnjj_dphi_jVj'
mvaDic['MHlnjj_2HDMaBDT_Grad22Var']['inputVars']['MHlnjj_deta_jVj']          = 'event.MHlnjj_deta_jVj'
mvaDic['MHlnjj_2HDMaBDT_Grad22Var']['inputVars']['MHlnjj_m_jj']              = 'event.MHlnjj_m_jj'
mvaDic['MHlnjj_2HDMaBDT_Grad22Var']['inputVars']['MHlnjj_m_ljj']             = 'event.MHlnjj_m_ljj'
mvaDic['MHlnjj_2HDMaBDT_Grad22Var']['inputVars']['MHlnjj_MAXPTlj_D_PTmet']   = 'event.MHlnjj_MAXPTlj_D_PTmet'
mvaDic['MHlnjj_2HDMaBDT_Grad22Var']['inputVars']['MHlnjj_MAXPTlj_D_Mlmetjj'] = 'event.MHlnjj_MAXPTlj_D_Mlmetjj'
mvaDic['MHlnjj_2HDMaBDT_Grad22Var']['inputVars']['MHlnjj_MTljj_D_PTmet']     = 'event.MHlnjj_MTljj_D_PTmet'
mvaDic['MHlnjj_2HDMaBDT_Grad22Var']['inputVars']['MHlnjj_MTljj_D_Mlmetjj']   = 'event.MHlnjj_MTljj_D_Mlmetjj'

mvaDic['MHlnjj_2HDMaBDT_Grad15Var']['inputVars']['mtw1']                     = 'event.mtw1'
mvaDic['MHlnjj_2HDMaBDT_Grad15Var']['inputVars']['MHlnjj_deta_ljjVmet']      = 'event.MHlnjj_deta_ljjVmet'
mvaDic['MHlnjj_2HDMaBDT_Grad15Var']['inputVars']['MHlnjj_dphi_ljjVmet']      = 'event.MHlnjj_dphi_ljjVmet'
mvaDic['MHlnjj_2HDMaBDT_Grad15Var']['inputVars']['MHlnjj_deta_jjVl']         = 'event.MHlnjj_deta_jjVl'
mvaDic['MHlnjj_2HDMaBDT_Grad15Var']['inputVars']['MHlnjj_dphi_jjVl']         = 'event.MHlnjj_dphi_jjVl'
mvaDic['MHlnjj_2HDMaBDT_Grad15Var']['inputVars']['MHlnjj_deta_lVmet']        = 'event.MHlnjj_deta_lVmet'
mvaDic['MHlnjj_2HDMaBDT_Grad15Var']['inputVars']['PuppiMET_pt']              = 'event.PuppiMET_pt'
mvaDic['MHlnjj_2HDMaBDT_Grad15Var']['inputVars']['MHlnjj_pt_ljj']            = 'event.MHlnjj_pt_ljj'
mvaDic['MHlnjj_2HDMaBDT_Grad15Var']['inputVars']['MHlnjj_PTljj_D_Mlmetjj']   = 'event.MHlnjj_PTljj_D_Mlmetjj'
mvaDic['MHlnjj_2HDMaBDT_Grad15Var']['inputVars']['MHlnjj_MINPTlj_D_PTmet']   = 'event.MHlnjj_MINPTlj_D_PTmet'
mvaDic['MHlnjj_2HDMaBDT_Grad15Var']['inputVars']['MHlnjj_MINPTlj_D_Mlmetjj'] = 'event.MHlnjj_MINPTlj_D_Mlmetjj'
mvaDic['MHlnjj_2HDMaBDT_Grad15Var']['inputVars']['MHlnjj_m_jj']              = 'event.MHlnjj_m_jj'
mvaDic['MHlnjj_2HDMaBDT_Grad15Var']['inputVars']['MHlnjj_m_ljj']             = 'event.MHlnjj_m_ljj'
mvaDic['MHlnjj_2HDMaBDT_Grad15Var']['inputVars']['MHlnjj_MAXPTlj_D_PTmet']   = 'event.MHlnjj_MAXPTlj_D_PTmet'
mvaDic['MHlnjj_2HDMaBDT_Grad15Var']['inputVars']['MHlnjj_MTljj_D_Mlmetjj']   = 'event.MHlnjj_MTljj_D_Mlmetjj'

mvaDic['MHlnjj_2HDMaBDT_Grad12Var']['inputVars']['mtw1']                     = 'event.mtw1'
mvaDic['MHlnjj_2HDMaBDT_Grad12Var']['inputVars']['MHlnjj_dphi_ljjVmet']      = 'event.MHlnjj_dphi_ljjVmet'
mvaDic['MHlnjj_2HDMaBDT_Grad12Var']['inputVars']['MHlnjj_dphi_jjVl']         = 'event.MHlnjj_dphi_jjVl'
mvaDic['MHlnjj_2HDMaBDT_Grad12Var']['inputVars']['MHlnjj_deta_lVmet']        = 'event.MHlnjj_deta_lVmet'
mvaDic['MHlnjj_2HDMaBDT_Grad12Var']['inputVars']['PuppiMET_pt']              = 'event.PuppiMET_pt'
mvaDic['MHlnjj_2HDMaBDT_Grad12Var']['inputVars']['MHlnjj_pt_ljj']            = 'event.MHlnjj_pt_ljj'
mvaDic['MHlnjj_2HDMaBDT_Grad12Var']['inputVars']['MHlnjj_PTljj_D_Mlmetjj']   = 'event.MHlnjj_PTljj_D_Mlmetjj'
mvaDic['MHlnjj_2HDMaBDT_Grad12Var']['inputVars']['MHlnjj_MINPTlj_D_Mlmetjj'] = 'event.MHlnjj_MINPTlj_D_Mlmetjj'
mvaDic['MHlnjj_2HDMaBDT_Grad12Var']['inputVars']['MHlnjj_m_jj']              = 'event.MHlnjj_m_jj'
mvaDic['MHlnjj_2HDMaBDT_Grad12Var']['inputVars']['MHlnjj_m_ljj']             = 'event.MHlnjj_m_ljj'
mvaDic['MHlnjj_2HDMaBDT_Grad12Var']['inputVars']['MHlnjj_MAXPTlj_D_PTmet']   = 'event.MHlnjj_MAXPTlj_D_PTmet'
mvaDic['MHlnjj_2HDMaBDT_Grad12Var']['inputVars']['MHlnjj_MTljj_D_Mlmetjj']   = 'event.MHlnjj_MTljj_D_Mlmetjj'

mvaDic['MHlnjj_2HDMaBDT_Ada22Var']['inputVars'] = copy.deepcopy(mvaDic['MHlnjj_2HDMaBDT_Grad22Var']['inputVars'])
mvaDic['MHlnjj_2HDMaBDT_Ada15Var']['inputVars'] = copy.deepcopy(mvaDic['MHlnjj_2HDMaBDT_Grad15Var']['inputVars'])
mvaDic['MHlnjj_2HDMaBDT_Ada12Var']['inputVars'] = copy.deepcopy(mvaDic['MHlnjj_2HDMaBDT_Grad12Var']['inputVars'])

# darkHiggs
mvaDic['MHlnjj_darkHiggsBDT_Ada16Var']['inputVars']['mtw1']                   = 'event.mtw1'
mvaDic['MHlnjj_darkHiggsBDT_Ada16Var']['inputVars']['MHlnjj_deta_ljjVmet']    = 'event.MHlnjj_deta_ljjVmet'
mvaDic['MHlnjj_darkHiggsBDT_Ada16Var']['inputVars']['MHlnjj_deta_jjVl']       = 'event.MHlnjj_deta_jjVl'
mvaDic['MHlnjj_darkHiggsBDT_Ada16Var']['inputVars']['MHlnjj_dphi_jjVl']       = 'event.MHlnjj_dphi_jjVl'
mvaDic['MHlnjj_darkHiggsBDT_Ada16Var']['inputVars']['MHlnjj_deta_lVmet']      = 'event.MHlnjj_deta_lVmet'
mvaDic['MHlnjj_darkHiggsBDT_Ada16Var']['inputVars']['PuppiMET_pt']            = 'event.PuppiMET_pt'
mvaDic['MHlnjj_darkHiggsBDT_Ada16Var']['inputVars']['MHlnjj_m_lmetjj']        = 'event.MHlnjj_m_lmetjj'
mvaDic['MHlnjj_darkHiggsBDT_Ada16Var']['inputVars']['MHlnjj_PTljj_D_PTmet']   = 'event.MHlnjj_PTljj_D_PTmet'
mvaDic['MHlnjj_darkHiggsBDT_Ada16Var']['inputVars']['MHlnjj_PTljj_D_Mlmetjj'] = 'event.MHlnjj_PTljj_D_Mlmetjj'
mvaDic['MHlnjj_darkHiggsBDT_Ada16Var']['inputVars']['MHlnjj_MINPTlj_D_PTmet'] = 'event.MHlnjj_MINPTlj_D_PTmet'
mvaDic['MHlnjj_darkHiggsBDT_Ada16Var']['inputVars']['MHlnjj_deta_jVj']        = 'event.MHlnjj_deta_jVj'
mvaDic['MHlnjj_darkHiggsBDT_Ada16Var']['inputVars']['MHlnjj_m_jj']            = 'event.MHlnjj_m_jj'
mvaDic['MHlnjj_darkHiggsBDT_Ada16Var']['inputVars']['MHlnjj_m_ljj']           = 'event.MHlnjj_m_ljj'
mvaDic['MHlnjj_darkHiggsBDT_Ada16Var']['inputVars']['MHlnjj_MAXPTlj_D_PTmet'] = 'event.MHlnjj_MAXPTlj_D_PTmet'
mvaDic['MHlnjj_darkHiggsBDT_Ada16Var']['inputVars']['MHlnjj_MTljj_D_PTmet']   = 'event.MHlnjj_MTljj_D_PTmet'
mvaDic['MHlnjj_darkHiggsBDT_Ada16Var']['inputVars']['MHlnjj_MTljj_D_Mlmetjj'] = 'event.MHlnjj_MTljj_D_Mlmetjj'

mvaDic['MHlnjj_darkHiggsBDT_Grad16Var']['inputVars'] = copy.deepcopy(mvaDic['MHlnjj_darkHiggsBDT_Ada16Var']['inputVars'])
