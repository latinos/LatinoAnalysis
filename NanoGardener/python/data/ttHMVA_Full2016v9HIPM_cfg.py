# UL era 2016_preVFP (preVFP)

from   collections import OrderedDict
import math

mvaDic = {}


mvaDic['Muon_ttHMVA_2016_preVFP'] = {
    'type'          : 'BDT' ,
    'xmlFile'       : 'LatinoAnalysis/NanoGardener/python/data/ttH-UL-leptonMVA/UL20_mu_TTH-like_2016_preVFP_BDTG.weights.xml' ,
    'spectatorVars' : OrderedDict() ,
    'inputVars'     : OrderedDict() ,
    # 'charVariables' : ['Muon_genPartFlav', 'Muon_jetNDauCharged'],
    'charVariables' : ['Muon_jetNDauCharged'],
}

mvaDic['Muon_ttHMVA_2016_preVFP']['spectatorVars']['event']                 = 'event.event'
mvaDic['Muon_ttHMVA_2016_preVFP']['spectatorVars']['Muon_mvaTTH']           = 'event.Muon_mvaTTH[muonID]'
mvaDic['Muon_ttHMVA_2016_preVFP']['spectatorVars']['Muon_miniPFRelIso_all'] = 'event.Muon_miniPFRelIso_all[muonID]'
mvaDic['Muon_ttHMVA_2016_preVFP']['spectatorVars']['Muon_looseId']          = 'event.Muon_looseId[muonID]'
mvaDic['Muon_ttHMVA_2016_preVFP']['spectatorVars']['Muon_genPartFlav']      = '1' #'event.Muon_genPartFlav[muonID]'
mvaDic['Muon_ttHMVA_2016_preVFP']['spectatorVars']['Muon_isGlobal']         = 'event.Muon_isGlobal[muonID]'
mvaDic['Muon_ttHMVA_2016_preVFP']['spectatorVars']['Muon_isTracker']        = 'event.Muon_isTracker[muonID]'
mvaDic['Muon_ttHMVA_2016_preVFP']['spectatorVars']['Muon_isPFcand']         = 'event.Muon_isPFcand[muonID]'
mvaDic['Muon_ttHMVA_2016_preVFP']['spectatorVars']['Muon_mediumId']         = 'event.Muon_mediumId[muonID]'
mvaDic['Muon_ttHMVA_2016_preVFP']['spectatorVars']['Muon_looseIdBis']       = 'event.Muon_looseId[muonID]'
mvaDic['Muon_ttHMVA_2016_preVFP']['spectatorVars']['Muon_dxy']              = 'event.Muon_dxy[muonID]'
mvaDic['Muon_ttHMVA_2016_preVFP']['spectatorVars']['Muon_dz']               = 'event.Muon_dz[muonID]'


mvaDic['Muon_ttHMVA_2016_preVFP']['inputVars']['Muon_pt']                                                                        = 'event.Muon_pt[muonID]' 
mvaDic['Muon_ttHMVA_2016_preVFP']['inputVars']['Muon_eta']                                                                       = 'event.Muon_eta[muonID]'
mvaDic['Muon_ttHMVA_2016_preVFP']['inputVars']['Muon_pfRelIso03_all']                                                            = 'event.Muon_pfRelIso03_all[muonID]'
mvaDic['Muon_ttHMVA_2016_preVFP']['inputVars']['Muon_miniPFRelIso_chg']                                                          = 'event.Muon_miniPFRelIso_chg[muonID]'
mvaDic['Muon_ttHMVA_2016_preVFP']['inputVars']['Muon_miniRelIsoNeutral := Muon_miniPFRelIso_all - Muon_miniPFRelIso_chg']        = 'event.Muon_miniPFRelIso_all[muonID] - event.Muon_miniPFRelIso_chg[muonID]'
mvaDic['Muon_ttHMVA_2016_preVFP']['inputVars']['Muon_jetNDauCharged']                                                            = 'event.Muon_jetNDauCharged[muonID]'
mvaDic['Muon_ttHMVA_2016_preVFP']['inputVars']['Muon_jetPtRelv2']                                                                = 'event.Muon_jetPtRelv2[muonID]'
mvaDic['Muon_ttHMVA_2016_preVFP']['inputVars']['Muon_jetPtRatio := min(1 / (1 + Muon_jetRelIso), 1.5)']                          = 'min(1. / (1 + event.Muon_jetRelIso[muonID]), 1.5)'
mvaDic['Muon_ttHMVA_2016_preVFP']['inputVars']['Muon_jetBTagDeepFlavB := Muon_jetIdx > -1 ? Jet_btagDeepFlavB[Muon_jetIdx] : 0'] = 'event.Jet_btagDeepFlavB[event.Muon_jetIdx[muonID]] if event.Muon_jetIdx[muonID] > -1 else 0'
mvaDic['Muon_ttHMVA_2016_preVFP']['inputVars']['Muon_sip3d']                                                                     = 'event.Muon_sip3d[muonID]'                        
mvaDic['Muon_ttHMVA_2016_preVFP']['inputVars']['Muon_log_dxy := log(abs(Muon_dxy))']                                             = 'math.log(abs(event.Muon_dxy[muonID]))'
mvaDic['Muon_ttHMVA_2016_preVFP']['inputVars']['Muon_log_dz  := log(abs(Muon_dz))']                                              = 'math.log(abs(event.Muon_dz[muonID]))'
mvaDic['Muon_ttHMVA_2016_preVFP']['inputVars']['Muon_segmentComp']                                                               = 'event.Muon_segmentComp[muonID]'


mvaDic['Electron_ttHMVA_2016_preVFP'] = {
    'type'          : 'BDT' ,
    'xmlFile'       : 'LatinoAnalysis/NanoGardener/python/data/ttH-UL-leptonMVA/UL20_el_TTH-like_2016_preVFP_BDTG.weights.xml' ,
    'spectatorVars' : OrderedDict() ,
    'inputVars'     : OrderedDict() ,
    # 'charVariables' : ['Electron_genPartFlav', 'Electron_jetNDauCharged', 'Electron_lostHits'],
    'charVariables' : ['Electron_jetNDauCharged', 'Electron_lostHits'],
}

mvaDic['Electron_ttHMVA_2016_preVFP']['spectatorVars']['event']                         = 'event.event'
mvaDic['Electron_ttHMVA_2016_preVFP']['spectatorVars']['Electron_mvaTTH']               = 'event.Electron_mvaTTH[eleID]'
mvaDic['Electron_ttHMVA_2016_preVFP']['spectatorVars']['Electron_miniPFRelIso_all']     = 'event.Electron_miniPFRelIso_all[eleID]'
mvaDic['Electron_ttHMVA_2016_preVFP']['spectatorVars']['Electron_mvaFall17V2noIso_WPL'] = 'event.Electron_mvaFall17V2noIso_WPL[eleID]'
mvaDic['Electron_ttHMVA_2016_preVFP']['spectatorVars']['Electron_lostHits']             = 'event.Electron_lostHits[eleID]'
mvaDic['Electron_ttHMVA_2016_preVFP']['spectatorVars']['Electron_genPartFlav']          = '1' # 'event.Electron_genPartFlav[eleID]'
mvaDic['Electron_ttHMVA_2016_preVFP']['spectatorVars']['Electron_dxy']                  = 'event.Electron_dxy[eleID]'
mvaDic['Electron_ttHMVA_2016_preVFP']['spectatorVars']['Electron_dz']                   = 'event.Electron_dz[eleID]'

mvaDic['Electron_ttHMVA_2016_preVFP']['inputVars']['Electron_pt']                                                                                = 'event.Electron_pt[eleID]'
mvaDic['Electron_ttHMVA_2016_preVFP']['inputVars']['Electron_eta']                                                                               = 'event.Electron_eta[eleID]'
mvaDic['Electron_ttHMVA_2016_preVFP']['inputVars']['Electron_pfRelIso03_all']                                                                    = 'event.Electron_pfRelIso03_all[eleID]'
mvaDic['Electron_ttHMVA_2016_preVFP']['inputVars']['Electron_miniPFRelIso_chg']                                                                  = 'event.Electron_miniPFRelIso_chg[eleID]'
mvaDic['Electron_ttHMVA_2016_preVFP']['inputVars']['Electron_miniRelIsoNeutral := Electron_miniPFRelIso_all - Electron_miniPFRelIso_chg']        = 'event.Electron_miniPFRelIso_all[eleID] - event.Electron_miniPFRelIso_chg[eleID]'
mvaDic['Electron_ttHMVA_2016_preVFP']['inputVars']['Electron_jetNDauCharged']                                                                    = 'event.Electron_jetNDauCharged[eleID]'
mvaDic['Electron_ttHMVA_2016_preVFP']['inputVars']['Electron_jetPtRelv2']                                                                        = 'event.Electron_jetPtRelv2[eleID]'
mvaDic['Electron_ttHMVA_2016_preVFP']['inputVars']['Electron_jetPtRatio := min(1 / (1 + Electron_jetRelIso), 1.5)']                              = 'min(1. / (1 + event.Electron_jetRelIso[eleID]), 1.5)'
mvaDic['Electron_ttHMVA_2016_preVFP']['inputVars']['Electron_jetBTagDeepFlavB := Electron_jetIdx > -1 ? Jet_btagDeepFlavB[Electron_jetIdx] : 0'] = 'event.Jet_btagDeepFlavB[event.Electron_jetIdx[eleID]] if event.Electron_jetIdx[eleID] > -1 else 0'
mvaDic['Electron_ttHMVA_2016_preVFP']['inputVars']['Electron_sip3d']                                                                             = 'event.Electron_sip3d[eleID]'
mvaDic['Electron_ttHMVA_2016_preVFP']['inputVars']['Electron_log_dxy := log(abs(Electron_dxy))']                                                 = 'math.log(abs(event.Electron_dxy[eleID]))'
mvaDic['Electron_ttHMVA_2016_preVFP']['inputVars']['Electron_log_dz  := log(abs(Electron_dz))']                                                  = 'math.log(abs(event.Electron_dz[eleID]))'
mvaDic['Electron_ttHMVA_2016_preVFP']['inputVars']['Electron_mvaFall17V2noIso']                                                                  = 'event.Electron_mvaFall17V2noIso[eleID]'
