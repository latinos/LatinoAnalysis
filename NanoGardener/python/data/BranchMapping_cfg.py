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
]

## TrigMaker
from LatinoAnalysis.NanoGardener.data.TrigMaker_cfg import NewVar_MC_dict
_ElepT_branches.extend(NewVar_MC_dict['F'])

branch_mapping = {}

branch_mapping['ElepTup'] = {
  'branches': _ElepT_branches,
  'suffix': '_ElepTup'
}

branch_mapping['ElepTdo'] = {
  'branches': _ElepT_branches,
  'suffix': '_ElepTdo'
}
