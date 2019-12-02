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

## TrigMaker
from LatinoAnalysis.NanoGardener.data.TrigMaker_cfg import NewVar_MC_dict
_ElepT_branches.extend(NewVar_MC_dict['F'])

## DYMVA and MonoHiggsMVA
from collections import OrderedDict
import os
cmssw_base = os.getenv('CMSSW_BASE')
mvaFiles=["DYMVA_2016_cfg.py", "DYMVA_2017_cfg.py", "DYMVA_2018_cfg.py", "MonoHiggsMVA_cfg.py"]
for mvaFile in mvaFiles:
  mvaFile = cmssw_base+'/src/LatinoAnalysis/NanoGardener/python/data/'+mvaFile
  if os.path.exists(mvaFile):
    handle = open(mvaFile,'r')
    exec(handle)
    handle.close()
    for key in mvaDic.keys():
      if key not in _ElepT_branches: 
        _ElepT_branches.append(key)
      if key not in _MupT_branches:
        _MupT_branches.append(key)   

## formulas MC
formulasFiles=['formulasToAdd_MC_2016.py', 'formulasToAdd_MC_2017.py', 'formulasToAdd_MC_2018.py', 'formulasToAdd_MC_MonoH.py']
for formulaFile in formulasFiles:
  formulasFile_path = cmssw_base+'/src/LatinoAnalysis/NanoGardener/python/data/'+formulaFile
  if os.path.exists(formulasFile_path) :
     handle = open(formulasFile_path,'r')
     exec(handle)
     handle.close()
     for key in formulas.keys():
       if "XS" not in key:
         if key not in _ElepT_branches:
           _ElepT_branches.append(key)
         if key not in _MupT_branches:
           _MupT_branches.append(key)

## LeptonSF
var = {}
execfile(cmssw_base+'/src/LatinoAnalysis/NanoGardener/python/data/LeptonSel_cfg.py', var)
ElectronWP = var['ElectronWP']
MuonWP = var['MuonWP']
wp_sf_pf = ['_IdIsoSF', '_IdIsoSF_Up', '_IdIsoSF_Down', '_IdIsoSF_Syst', '_TotSF', '_TotSF_Up', '_TotSF_Down']
for version in ElectronWP.keys():
  for wp in ElectronWP[version]['TightObjWP']:
    for postfix in wp_sf_pf:
      key = 'Lepton_tightElectron_'+wp + postfix
      if key not in _ElepT_branches:
        _ElepT_branches.append(key)
for version in MuonWP.keys():
  for wp in MuonWP[version]['TightObjWP']:
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
