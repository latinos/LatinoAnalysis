exclude=GluGluHToZZTo4L_M125_TuneCP5Down,GluGluHToZZTo4L_M125_TuneCP5Up,GluGluHToZZTo4L_M125_minloHJJ,GluGluHToZZTo4L_MiNLOHJJ_M125,GluGluHToZZTo4L_MiNLOHJJ_M125_TuneCP5Down,GluGluHToZZTo4L_MiNLOHJJ_M125_TuneCP5Up,QCD_Pt_15to20_bcToE,QCD_Pt_170to250_bcToE,QCD_Pt_20to30_bcToE,QCD_Pt_250toInf_bcToE,QCD_Pt_30to80_bcToE,QCD_Pt_80to170_bcToE,ST_s-channel_had,ST_t-channel_antitop_hdampDown,ST_t-channel_antitop_hdampUp,ST_t-channel_top_hdampDown,ST_t-channel_top_hdampUp,ST_tW_antitop_noHad_PDF,ST_tW_antitop_noHad_hdampDown,ST_tW_antitop_noHad_hdampUp,ST_tW_top_TuneCP5Down,ST_tW_top_noHad_PDF,ST_tW_top_noHad_hdampDown,ST_tW_top_noHad_hdampUp,TTToSemiLeptonic_hdampDown,TTToSemiLeptonic_hdampUp,WJetsToLNu_Pt-100To250,WJetsToLNu_Pt-250To400,WJetsToLNu_Pt-400To600,WJetsToLNu_Pt-600ToInf,WJetsToLNu_Sherpa,WWW_ext1,WWZ_ext1,WZZ_ext1,ZZZ_ext1,tZq_ll_4f_TuneCP5Down,tZq_ll_4f_TuneCP5Up
#while :
#do

#      mkPostProc.py -p Run2016_UL2016_nAODv9_noHIPM_Full2016v9 -s DATAl1loose2016v9 -b
#      mkPostProc.py -p Run2016_UL2016_nAODv9_noHIPM_Full2016v9 -i DATAl1loose2016v9 -s l2loose -b
#      mkPostProc.py -p Run2016_UL2016_nAODv9_noHIPM_Full2016v9 -i DATAl1loose2016v9__l2loose -s l2tightOR2016v9 -b
#      mkPostProc.py -p Run2016_102X_nAODv7_Full2016v7 -s fakeSel -i DATAl1loose2016v7 -b

#      mkPostProc.py -p Run2016_UL2016_nAODv9_HIPM_Full2016v9 -s DATAl1loose2016v9 -b                            
#      mkPostProc.py -p Run2016_UL2016_nAODv9_HIPM_Full2016v9 -i DATAl1loose2016v9 -s l2loose -b
#      mkPostProc.py -p Run2016_UL2016_nAODv9_HIPM_Full2016v9 -i DATAl1loose2016v9__l2loose -s l2tightOR2016v9 -b


#      mkPostProc.py -p Summer20UL16_106x_nAODv9_noHIPM_Full2016v9 -s MCl1loose2016v9 -b
#      mkPostProc.py -p Summer20UL16_106x_nAODv9_noHIPM_Full2016v9 -i MCl1loose2016v9 -s MCCorr2016v9NoJERInHorn -b -Q nextweek -E $exclude
      mkPostProc.py -p Summer20UL16_106x_nAODv9_noHIPM_Full2016v9 -i MCl1loose2016v9__MCCorr2016v9NoJERInHorn -s l2tightOR2016v9 -b
#
#      mkPostProc.py -p Summer20UL16_106x_nAODv9_HIPM_Full2016v9 -s MCl1loose2016v9 -b
#      mkPostProc.py -p Summer20UL16_106x_nAODv9_HIPM_Full2016v9 -i MCl1loose2016v9 -s MCCorr2016v9NoJERInHorn -b -Q nextweek -E $exclude
      mkPostProc.py -p Summer20UL16_106x_nAODv9_HIPM_Full2016v9 -i MCl1loose2016v9__MCCorr2016v9NoJERInHorn -s l2tightOR2016v9 -b

#done
