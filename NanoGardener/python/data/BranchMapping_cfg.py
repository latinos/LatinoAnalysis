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
  ## High Mass Semileptonic
  'HM_Wlep_pt_Puppi',
  'HM_Wlep_eta_Puppi',
  'HM_Wlep_phi_Puppi',
  'HM_Wlep_mass_Puppi',
  'HM_Wlep_mt',
  'HM_Flavlnjj',
  'HM_WptOvHak4M',
  'HM_CleanFatJetPassMBoosted_WptOvHfatM',
  'HM_CleanFatJetPassMBoosted_HlnFat_mass',
  'HM_CleanFatJetPassMBoosted_CFatJetIdx',
  'HM_Hlnjj_mass',
  'HM_Hlnjj_mt',
  'HM_idxWfat_noTau21Cut',
  'HM_HlnFatMass_noTau21Cut',
  ## EFT MEs
  'hm',
  'me_vbf_hsm',
  'me_vbf_hm',
  'me_vbf_hp',
  'me_vbf_hl',
  'me_vbf_mixhm',
  'me_vbf_mixhp',
  'me_wh_hsm',
  'me_wh_hm',
  'me_wh_hp',
  'me_wh_hl',
  'me_wh_mixhm',
  'me_wh_mixhp',
  'me_zh_hsm',
  'me_zh_hm',
  'me_zh_hp',
  'me_zh_hl',
  'me_zh_mixhm',
  'me_zh_mixhp',
  'me_qcd_hsm',
  'pjjSm_wh',
  'pjjTr_wh',
  'pjjSm_zh',
  'pjjTr_zh',
  'meAvg_wh',
  'meAvg_zh',
  ## MonoHiggs Semileptonic
  # deltas
  'MHlnjj_dphi_ljjVmet',
  'MHlnjj_deta_ljjVmet',
  'MHlnjj_dr_ljjVmet',
  # composed objects 
  'MHlnjj_mt_lmet',
  'MHlnjj_mt_lmetjj',
  'MHlnjj_mt_ljj',
  'MHlnjj_pt_lmet',
  'MHlnjj_pt_lmetjj',
  'MHlnjj_pt_ljj',
  'MHlnjj_m_lmet',
  'MHlnjj_m_lmetjj',
  'MHlnjj_m_ljj',
  # single objects
  #'MHlnjj_pt_l',
  # fractions
  'MHlnjj_PTljj_D_PTmet',     
  'MHlnjj_PTljj_D_Mlmetjj',   
  'MHlnjj_MINPTlj_D_PTmet',   
  'MHlnjj_MINPTlj_D_Mlmetjj', 
  'MHlnjj_MAXPTlj_D_PTmet',   
  'MHlnjj_MAXPTlj_D_Mlmetjj', 
  'MHlnjj_MTljj_D_PTmet',     
  'MHlnjj_MTljj_D_Mlmetjj',   
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
  ## High Mass Semileptonic
  'HM_Wlep_pt_Puppi',
  'HM_Wlep_eta_Puppi',
  'HM_Wlep_phi_Puppi',
  'HM_Wlep_mass_Puppi',
  'HM_Wlep_mt',
  'HM_Flavlnjj',
  'HM_IsBoosted',
  'HM_IsResolved',
  'HM_IsBTopTagged',
  'HM_WptOvHak4M',
  'HM_CleanFatJetPassMBoosted_WptOvHfatM',
  'HM_CleanFatJetPassMBoosted_HlnFat_mass',
  'HM_CleanFatJetPassMBoosted_CFatJetIdx',
  'HM_Hlnjj_mass',
  'HM_Hlnjj_mt',
  'HM_vbfFat_jj_dEta',
  'HM_vbfFat_jj_mass',
  'HM_vbfjj_jj_dEta',
  'HM_vbfjj_jj_mass',
  'HM_IsVbfFat',
  'HM_IsVbfjj',
  'HM_idxWfat_noTau21Cut',
  'HM_HlnFatMass_noTau21Cut',
  ## EFT MEs
  'hm',
  'me_vbf_hsm',
  'me_vbf_hm',
  'me_vbf_hp',
  'me_vbf_hl',
  'me_vbf_mixhm',
  'me_vbf_mixhp',
  'me_wh_hsm',
  'me_wh_hm',
  'me_wh_hp',
  'me_wh_hl',
  'me_wh_mixhm',
  'me_wh_mixhp',
  'me_zh_hsm',
  'me_zh_hm',
  'me_zh_hp',
  'me_zh_hl',
  'me_zh_mixhm',
  'me_zh_mixhp',
  'me_qcd_hsm',
  'pjjSm_wh',
  'pjjTr_wh',
  'pjjSm_zh',
  'pjjTr_zh',
  'meAvg_wh',
  'meAvg_zh',
  ## MonoHiggs Semileptonic
  # deltas
  'MHlnjj_dphi_ljjVmet',
  'MHlnjj_dphi_lVmet',
  'MHlnjj_dphi_jjVmet',
  'MHlnjj_deta_ljjVmet',
  'MHlnjj_deta_lVmet',
  'MHlnjj_deta_jjVmet',
  'MHlnjj_dr_ljjVmet',
  'MHlnjj_dr_lVmet',
  'MHlnjj_dr_jjVmet',
  # composed objects 
  'MHlnjj_mt_lmet',
  'MHlnjj_mt_lmetjj',
  'MHlnjj_mt_met',
  'MHlnjj_pt_lmet',
  'MHlnjj_pt_lmetjj',
  'MHlnjj_pt_met',
  'MHlnjj_m_lmet',
  'MHlnjj_m_lmetjj',
  'MHlnjj_m_met',
  # fractions
  'MHlnjj_PTljj_D_PTmet',     
  'MHlnjj_PTljj_D_Mlmetjj',   
  'MHlnjj_MINPTlj_D_PTmet',   
  'MHlnjj_MINPTlj_D_Mlmetjj', 
  'MHlnjj_MAXPTlj_D_PTmet',   
  'MHlnjj_MAXPTlj_D_Mlmetjj', 
  'MHlnjj_MTljj_D_PTmet',     
  'MHlnjj_MTljj_D_Mlmetjj',   
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

  'VBS_category',
  'VBS_jets_maxmjj_massWZ',
  'VBS_jets_maxmjj_maxPt',
  'VBS_jets_maxPt_massWZ',
  'VBS_jets_massWZ_maxmjj',
  'VBS_jets_massWZ_maxPt',
  'VBS_jets_maxmjj',
  'VBS_jets_maxPt',
  'V_jets_maxmjj',
  'V_jets_maxPt',
  'V_jets_maxmjj_massWZ',
  'V_jets_maxmjj_maxPt',
  'V_jets_maxPt_massWZ',
  'V_jets_massWZ_maxmjj',
  'V_jets_massWZ_maxPt',
  'HM_Whad_pt',
  'HM_Whad_eta',
  'HM_Whad_phi',
  'HM_Whad_mass',
  'HM_idx_j1',
  'HM_idx_j2',
  'HM_IsResolved',
  'HM_IsBTopTagged',
  'HM_WptOvHak4M',
  'HM_Hlnjj_mass',
  'HM_Hlnjj_mt',
  'HM_vbfFat_jj_dEta',
  'HM_vbfFat_jj_mass',
  'HM_vbfjj_jj_dEta',
  'HM_vbfjj_jj_mass',
  'HM_largest_nonW_mjj',
  'HM_IsVbfFat',
  'HM_IsVbfjj',
  ## EFT MEs
  'hm',
  'me_vbf_hsm',
  'me_vbf_hm',
  'me_vbf_hp',
  'me_vbf_hl',
  'me_vbf_mixhm',
  'me_vbf_mixhp',
  'me_wh_hsm',
  'me_wh_hm',
  'me_wh_hp',
  'me_wh_hl',
  'me_wh_mixhm',
  'me_wh_mixhp',
  'me_zh_hsm',
  'me_zh_hm',
  'me_zh_hp',
  'me_zh_hl',
  'me_zh_mixhm',
  'me_zh_mixhp',
  'me_qcd_hsm',
  'pjjSm_wh',
  'pjjTr_wh',
  'pjjSm_zh',
  'pjjTr_zh',
  'meAvg_wh',
  'meAvg_zh',
  ## MonoHiggs Semileptonic
  # deltas
  'MHlnjj_dphi_ljjVmet',
  'MHlnjj_dphi_jVj',
  'MHlnjj_dphi_jjVl',
  'MHlnjj_dphi_jjVmet',
  'MHlnjj_deta_ljjVmet',
  'MHlnjj_deta_jVj',
  'MHlnjj_deta_jjVl',
  'MHlnjj_deta_jjVmet',
  'MHlnjj_dr_ljjVmet',
  'MHlnjj_dr_jVj',
  'MHlnjj_dr_jjVl',
  'MHlnjj_dr_jjVmet',
  # composed objects 
  'MHlnjj_mt_lmetjj',
  'MHlnjj_mt_jj',
  'MHlnjj_mt_ljj',
  'MHlnjj_pt_lmetjj',
  'MHlnjj_pt_jj',
  'MHlnjj_pt_ljj',
  'MHlnjj_m_lmetjj',
  'MHlnjj_m_jj',
  'MHlnjj_m_ljj',
  # single objects
  'MHlnjj_pt_j1',
  'MHlnjj_pt_j2',
  'MHlnjj_eta_j1',
  'MHlnjj_eta_j2',
  'MHlnjj_idx_j3',
  # fractions
  'MHlnjj_PTljj_D_PTmet',     
  'MHlnjj_PTljj_D_Mlmetjj',   
  'MHlnjj_MINPTlj_D_PTmet',   
  'MHlnjj_MINPTlj_D_Mlmetjj', 
  'MHlnjj_MAXPTlj_D_PTmet',   
  'MHlnjj_MAXPTlj_D_Mlmetjj', 
  'MHlnjj_MTljj_D_PTmet',     
  'MHlnjj_MTljj_D_Mlmetjj',   
]

_Fatjet_syst_branches = [
  'nCleanFatJet',
  'nCleanJetNotFat',
  'CleanFatJet_pt',
  'CleanFatJet_eta',
  'CleanFatJet_phi',
  'CleanFatJet_mass',
  'CleanFatJet_tau21',
  'CleanFatJet_jetIdx',
  'CleanJetNotFat_jetIdx',
  'CleanJetNotFat_deltaR',

  'VBS_category',
  'VBS_jets_maxmjj_massWZ',
  'VBS_jets_maxmjj_maxPt',
  'VBS_jets_maxPt_massWZ',
  'VBS_jets_massWZ_maxmjj',
  'VBS_jets_massWZ_maxPt',
  'VBS_jets_maxmjj',
  'VBS_jets_maxPt',
  'V_jets_maxmjj',
  'V_jets_maxPt',
  'V_jets_maxmjj_massWZ',
  'V_jets_maxmjj_maxPt',
  'V_jets_maxPt_massWZ',
  'V_jets_massWZ_maxmjj',
  'V_jets_massWZ_maxPt',
  'HM_Whad_pt',
  'HM_Whad_eta',
  'HM_Whad_phi',
  'HM_Whad_mass',
  'HM_idx_j1',
  'HM_idx_j2',
  'HM_IsBoosted',
  'HM_IsBTopTagged',
  'HM_WptOvHak4M',
  'HM_nCleanFatJetPassMBoosted',
  'HM_CleanFatJetPassMBoosted_pt',
  'HM_CleanFatJetPassMBoosted_eta',
  'HM_CleanFatJetPassMBoosted_phi',
  'HM_CleanFatJetPassMBoosted_mass',
  'HM_CleanFatJetPassMBoosted_tau21',
  'HM_CleanFatJetPassMBoosted_WptOvHfatM',
  'HM_CleanFatJetPassMBoosted_HlnFat_mass',
  'HM_CleanFatJetPassMBoosted_CFatJetIdx',
  'HM_vbfFat_jj_dEta',
  'HM_vbfFat_jj_mass',
  'HM_IsVbfFat',
  'HM_idxWfat_noTau21Cut',
  'HM_HlnFatMass_noTau21Cut'
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

for cfg in ["DYMVA_2016_alt_cfg", "DYMVA_2017_alt_cfg", "DYMVA_2018_alt_cfg"]:
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
for cfg in ['formulasToAdd_MC_Full2016v6', 'formulasToAdd_MC_Full2016v7', 'formulasToAdd_MC_Full2017v6', 'formulasToAdd_MC_Full2017v7', 'formulasToAdd_MC_Full2018v6', 'formulasToAdd_MC_Full2018v7', 'formulasToAdd_MC_MonoH']:
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

branch_mapping["fatjetJMSup"] = {
  'branches': _Fatjet_syst_branches,
  'suffix': '_fatjetJMSup'
}

branch_mapping["fatjetJMSdo"] = {
  'branches': _Fatjet_syst_branches,
  'suffix': '_fatjetJMSdo'
}

branch_mapping["fatjetJMRup"] = {
  'branches': _Fatjet_syst_branches,
  'suffix': '_fatjetJMRup'
}

branch_mapping["fatjetJMRdo"] = {
  'branches': _Fatjet_syst_branches,
  'suffix': '_fatjetJMRdo'
}

branch_mapping["fatjetJERup"] = {
  'branches': _Fatjet_syst_branches,
  'suffix': '_fatjetJERup'
}

branch_mapping["fatjetJERdo"] = {
  'branches': _Fatjet_syst_branches,
  'suffix': '_fatjetJERdo'
}

branch_mapping["fatjetJESup"] = {
  'branches': _Fatjet_syst_branches,
  'suffix': '_fatjetJESup'
}

branch_mapping["fatjetJESdo"] = {
  'branches': _Fatjet_syst_branches,
  'suffix': '_fatjetJESdo'
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
  branch_mapping['fatjetJES'+source+"do"] = {
    'branches': _Fatjet_syst_branches,
    'suffix': '_fatjetJES'+source+'do'
  }
  branch_mapping['fatjetJES'+source+"up"] = {
    'branches': _Fatjet_syst_branches,
    'suffix': '_fatjetJES'+source+'up'
  }
