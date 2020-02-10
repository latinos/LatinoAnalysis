import importlib

_ElepT_branches = [
  'Lepton_pt',
  ## l2Kin
  'mll',
  'ptll',
  'pt1',
  'pt2',
  'mth',
  'mcoll',
  'mcollWW',
  'mTi',
  'mTe',
  'choiMass',
  'mR',
  'mT2',
  'mtw1',
  'mtw2',
  'mllWgSt',
  'mllThird',
  'mllOneThree',
  'mllTwoThree',
  'vht_pt',
  'pTWW',
  'pTHjj',
  'recoil',
  'upara',
  'uperp',
  'm2ljj20',
  'm2ljj30',
  'ptTOT_cut',
  'mTOT_cut',
  'mlljj20_whss',
  'mlljj30_whss',
  'WlepPt_whss',
  'WlepMt_whss',
  ## TrigMaker
  'TriggerEmulator',
  # trigger efficiencies - added below
  ## l3kinProducer 
  'WH3l_ZVeto',
  'WH3l_flagOSSF',
  #'WH3l_njet',
  #'WH3l_nbjet',
  'WH3l_mtlmet',
  #'WH3l_dphilmet',
  'WH3l_mOSll',
  #'WH3l_drOSll',
  'WH3l_ptOSll',
  #'WH3l_chlll',
  'WH3l_mlll',
  'WH3l_ptlll',
  'WH3l_ptWWW',
  'WH3l_mtWWW',
  #'WH3l_dphilllmet',
  'WH3l_ptW',
  'ZH3l_njet',
  'ZH3l_Z4lveto',
  'ZH3l_dmjjmW',
  'ZH3l_mTlmet',
  #'ZH3l_pdgid_l',
  #'ZH3l_dphilmetjj',
  #'ZH3l_dphilmetj',
  'ZH3l_pTlmetjj',
  'ZH3l_pTlmetj',
  'ZH3l_mTlmetjj',
  'ZH3l_pTZ',
  'ZH3l_checkmZ',
  ## l4kin producers
  #'pfmetPhi_zh4l',
  'z0Mass_zh4l',
  'z0Pt_zh4l',
  'z1Mass_zh4l',
  'z1Pt_zh4l',
  'zaMass_zh4l',
  'zbMass_zh4l',
  #'flagZ1SF_zh4l',
  #'z0DeltaPhi_zh4l',
  #'z1DeltaPhi_zh4l',
  #'zaDeltaPhi_zh4l',
  #'zbDeltaPhi_zh4l',
  #'minDeltaPhi_zh4l',
  #'z0DeltaR_zh4l',
  #'z1DeltaR_zh4l',
  #'zaDeltaR_zh4l',
  #'zbDeltaR_zh4l',
  'lep1Mt_zh4l',
  'lep2Mt_zh4l',
  'lep3Mt_zh4l',
  'lep4Mt_zh4l',
  'minMt_zh4l',
  'z1Mt_zh4l',
  'mllll_zh4l',
  #'chllll_zh4l',
  #'z1dPhi_lep1MET_zh4l',
  #'z1dPhi_lep2MET_zh4l',
  #'z1mindPhi_lepMET_zh4l',
  ## LeptonSF
  'Lepton_RecoSF',
  'Lepton_RecoSF_Up',
  'Lepton_RecoSF_Down',
]

_MupT_branches = _ElepT_branches

_MET_branches = [
  'MET_pt',
  'MET_phi',
  'PuppiMET_pt',
  'PuppiMET_phi',
  'RawMET_pt',
  'RawMET_phi',
  ## l2Kin
  'mth',
  'mcoll',
  'mcollWW',
  'mTi',
  'choiMass',
  'mR',
  'mT2',
  'mtw1',
  'mtw2',
  'pTWW',
  'pTHjj',
  'recoil',
  'upara',
  'uperp',
  'ptTOT_cut',
  'mTOT_cut',
  'WlepMt_whss',
  'PfMetDivSumMet',
  # trigger efficiencies - added below
  ## l3kinProducer 
  'WH3l_mtlmet',
  'WH3l_dphilmet',
  'WH3l_ptWWW',
  'WH3l_mtWWW',
  'WH3l_dphilllmet',
  'WH3l_ptW',
  'ZH3l_dmjjmW',
  'ZH3l_mTlmet',
  'ZH3l_dphilmetjj',
  'ZH3l_dphilmetj',
  'ZH3l_pTlmetjj',
  'ZH3l_pTlmetj',
  'ZH3l_mTlmetjj',
  ## l4kin producers
  'pfmetPhi_zh4l',
  'lep1Mt_zh4l',
  'lep2Mt_zh4l',
  'lep3Mt_zh4l',
  'lep4Mt_zh4l',
  'minMt_zh4l',
  'z1Mt_zh4l',
  'z1dPhi_lep1MET_zh4l',
  'z1dPhi_lep2MET_zh4l',
  'z1mindPhi_lepMET_zh4l',
]

_JES_branches = ['CleanJet_pt']
# since JES affects MET...
_JES_branches  += _MET_branches
# and some more stuff
_JES_branches += [
  'njet',
  'dphilljet',
  'dphilljetjet',
  'dphilljetjet_cut',
  'mjj',
  'detajj',
  'dphijet1met',
  'dphijet2met',
  'dphijjmet',
  'dphijjmet_cut',
  'dphilep1jet1',
  'dphilep1jet2',
  'dphilep2jet1',
  'dphilep2jet2',
  'mindetajl',
  'dphijj',
  'maxdphilepjj',
  'dphilep1jj',
  'dphilep2jj',
  'ht',
  'vht_pt',
  'vht_phi',
  'pTHjj',
  'jetpt1_cut',
  'jetpt2_cut',
  'dphilljet_cut',
  'dphijet1met_cut',
  'dphijet2met_cut',
  'upara',
  'uperp',
  'm2ljj20',
  'm2ljj30',
  'ptTOT_cut',
  'mTOT_cut',
  'OLV1_cut',
  'OLV2_cut',
  'Ceta_cut',
  'mlljj20_whss',
  'mlljj30_whss',
]

## TrigMaker
from LatinoAnalysis.NanoGardener.data.TrigMaker_cfg import NewVar_MC_dict
_ElepT_branches.extend(NewVar_MC_dict['F'])
_MupT_branches.extend(NewVar_MC_dict['F'])

## DYMVA and MonoHiggsMVA
for cfg in ["DYMVA_2016_cfg", "DYMVA_2017_cfg", "DYMVA_2018_cfg", "MonoHiggsMVA_cfg"]:
  mod = importlib.import_module('LatinoAnalysis.NanoGardener.data.' + cfg)
  for key in mod.mvaDic.iterkeys():
    if key not in _ElepT_branches: 
      _ElepT_branches.append(key)
    if key not in _MupT_branches:  
      _MupT_branches.append(key)
    if key not in _MET_branches: 
      _MET_branches.append(key)
    if key not in _JES_branches: 
      _JES_branches.append(key)

## formulas MC
for cfg in ['formulasToAdd_MC_2016', 'formulasToAdd_MC_2017', 'formulasToAdd_MC_2018', 'formulasToAdd_MC_MonoH']:
  mod = importlib.import_module('LatinoAnalysis.NanoGardener.data.' + cfg)
  for key in mod.formulas.iterkeys():
    if "XS" not in key and key not in _ElepT_branches:
      _ElepT_branches.append(key)
    if "XS" not in key and key not in _MupT_branches:
      _MupT_branches.append(key)
# DO MET VARIATIONS AFFECT FORMULAS?

## LeptonSF
var = importlib.import_module("LatinoAnalysis.NanoGardener.data.LeptonSel_cfg")
wp_sf_pf = ['_IdIsoSF', '_IdIsoSF_Up', '_IdIsoSF_Down', '_IdIsoSF_Syst', '_TotSF', '_TotSF_Up', '_TotSF_Down']
for version in var.ElectronWP.keys():
  for wp in var.ElectronWP[version]['TightObjWP']:
    for postfix in wp_sf_pf:
      key = 'Lepton_tightElectron_'+wp + postfix
      if key not in _ElepT_branches:
        _ElepT_branches.append(key)
for version in var.MuonWP.keys():
  for wp in var.MuonWP[version]['TightObjWP']:
    for postfix in wp_sf_pf:
      if key not in _MupT_branches:
        _MupT_branches.append(key)  


branch_mapping = {}

branch_mapping['ElepTup'] = {
  'branches': _ElepT_branches,
  'suffix': '_ElepTup'
}

branch_mapping['ElepTdo'] = {
  'branches': _ElepT_branches,
  'suffix': '_ElepTdo'
}

branch_mapping['MupTup'] = {
  'branches': _MupT_branches,
  'suffix': '_MupTup'
}

branch_mapping['MupTdo'] = {
  'branches': _MupT_branches,
  'suffix': '_MupTdo'
}

branch_mapping['METup'] = {
  'branches': _MET_branches,
  'suffix': '_METup'
}

branch_mapping['METdo'] = {
  'branches': _MET_branches,
  'suffix': '_METdo'
}

branch_mapping['JESup'] = {
  'branches': _JES_branches,
  'suffix': '_JESup'
}

branch_mapping['JESdo'] = {
  'branches': _JES_branches,
  'suffix': '_JESdo'
}

# JES 11 sources
for source in ["Absolute", "Absolute_2016", "Absolute_2017", "Absolute_2018",
               "BBEC1", "BBEC1_2016", "BBEC1_2017", "BBEC1_2018",
               "EC2", "EC2_2016", "EC2_2017", "EC2_2018",
               "FlavorQCD",
               "HF", "HF_2016", "HF_2017", "HF_2018",
               "RelativeBal",
               "RelativeSample_2016", "RelativeSample_2017", "RelativeSample_2018"]:
  branch_mapping['JES'+source+"do"] = {
    'branches': _JES_branches,
    'suffix': '_JES'+source+'do'
  }
  branch_mapping['JES'+source+"up"] = {
    'branches': _JES_branches,
    'suffix': '_JES'+source+'up'
  } 






