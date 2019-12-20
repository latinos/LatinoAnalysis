from collections import OrderedDict

mvaDic = {}


mvaDic['Mucca2HDMFull'] = {
                          'type'      : 'BDT' ,  
                          'xmlFile'   : 'LatinoAnalysis/NanoGardener/python/data/MVA/monoHiggs/TMVAClassification_BDT7.weights.xml' ,
                          'inputVars' : OrderedDict() ,
                         }

#mvaDic['dymva_dnn_0j'] = {
#                          'type'      : 'PyKeras' ,
#                          'xmlFile'   : 'LatinoAnalysis/NanoGardener/python/data/DYSFmva/2017/TMVAClassification_PyKeras_2017_0j.weights.xml'   ,
#                          'inputVars' : OrderedDict() ,
#                         }

#--- Variables
#Mucca2HDMFull
mvaDic['Mucca2HDMFull']['inputVars']['mth']                     = 'event.mth' 
mvaDic['Mucca2HDMFull']['inputVars']['mtw2']                    = 'event.mtw2' 
#mvaDic['Mucca2HDMFull']['inputVars']['metTtrk']                 = 'event.metTtrk' 
mvaDic['Mucca2HDMFull']['inputVars']['metTtrk']                 = 'event.TkMET_pt' 
mvaDic['Mucca2HDMFull']['inputVars']['drll']                    = 'event.drll' 
mvaDic['Mucca2HDMFull']['inputVars']['ptll']                    = 'event.ptll' 
mvaDic['Mucca2HDMFull']['inputVars']['mpmet']                   = 'event.mpmet' 
mvaDic['Mucca2HDMFull']['inputVars']['mtw1']                    = 'event.mtw1' 
mvaDic['Mucca2HDMFull']['inputVars']['mll']                     = 'event.mll' 
mvaDic['Mucca2HDMFull']['inputVars']['dphilmet']                = 'event.dphilmet' 
mvaDic['Mucca2HDMFull']['inputVars']['dphilmet1']               = 'event.dphilmet1' 
mvaDic['Mucca2HDMFull']['inputVars']['dphilmet2']               = 'event.dphilmet2' 
#mvaDic['Mucca2HDMFull']['inputVars']['Lepton_pt[0]']            = 'event.Lepton_pt[0]' 
mvaDic['Mucca2HDMFull']['inputVars']['std_vector_lepton_pt[0]'] = 'event.Lepton_pt[0]' 
#mvaDic['Mucca2HDMFull']['inputVars']['metPfType1']              = 'event.metPfType1' 
mvaDic['Mucca2HDMFull']['inputVars']['metPfType1']              = 'event.MET_pt' 
mvaDic['Mucca2HDMFull']['inputVars']['dphill']                  = 'event.dphill' 
#mvaDic['Mucca2HDMFull']['inputVars']['Lepton_pt[1]']            = 'event.Lepton_pt[1]' 
mvaDic['Mucca2HDMFull']['inputVars']['std_vector_lepton_pt[1]'] = 'event.Lepton_pt[1]' 


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
#mvaDic['dymva_dnn_0j']['inputVars']['PV_npvsGood']    = 'event.PV_npvsGood'

