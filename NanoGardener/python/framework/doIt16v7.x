Samples=WJetsToLNu_Wpt600ToInf,WJetsToLNu_Wpt100To250,WJetsToLNu_Wpt400To600_ext1,WJetsToLNu_Wpt250To400_ext1,WJetsToLNu_Wpt600ToInf_ext1,WJetsToLNu_Wpt250To400,WWTo4Q_4f,WJetsToLNu_Wpt100To250_ext1,WJetsToLNu_Wpt400To600,WJetsToLNu_Wpt600ToInf,WJetsToLNu_Wpt250To400_ext4,WJetsToLNu_Wpt100To250_ext4


while :
do

#       mkPostProc.py -p Run2016_102X_nAODv7_Full2016v7 -s DATAl1loose2016v7 -b
#      mkPostProc.py -p Run2016_102X_nAODv7_Full2016v7 -s fakeSel -i DATAl1loose2016v7 -b
#      mkPostProc.py -p Run2016_102X_nAODv7_Full2016v7 -s l2loose -i DATAl1loose2016v7 -b
#      mkPostProc.py -p Run2016_102X_nAODv7_Full2016v7 -s l2tightOR2016v7 -i DATAl1loose2016v7__l2loose -b

#      mkPostProc.py -p Run2016_102X_nAODv7_Full2016v7 -s fakeW -i DATAl1loose2016v7__l2loose -b

#      mkPostProc.py -p Run2016_102X_nAODv7_Full2016v7 -s DATAWgStar201Xv7 -b

       mkPostProc.py -p Summer16_102X_nAODv7_Full2016v7 -s MCl1loose2016v7 -b -Q nextweek
       mkPostProc.py -p Summer16_102X_nAODv7_Full2016v7 -s MCCorr2016v7 -i MCl1loose2016v7 -b -Q nextweek -E $Samples
#      mkPostProc.py -p Summer16_102X_nAODv7_Full2016v7 -s fakeSelMC -i MCl1loose2016v7__MCCorr2016v7 -b
#      mkPostProc.py -p Summer16_102X_nAODv7_Full2016v7 -s fakeSelKinMC i MCl1loose2016v7 -b
       mkPostProc.py -p Summer16_102X_nAODv7_Full2016v7 -s l2loose -i MCl1loose2016v7__MCCorr2016v7 -b
       mkPostProc.py -p Summer16_102X_nAODv7_Full2016v7 -s l2tightOR2016v7 -i MCl1loose2016v7__MCCorr2016v7__l2loose -b

#      for iSyst in JESup JESdo METup METdo MupTup MupTdo ElepTup ElepTdo ; do
#        mkPostProc.py -p Summer16_102X_nAODv7_Full2016v7 -s $iSyst -i MCl1loose2016v7__MCCorr2016v7__l2loose__l2tightOR2016v7 -b
#      done

#      for iSyst in JESup_suffix JESdo_suffix ; do
#        mkPostProc.py -p Summer16_102X_nAODv7_Full2016v7 -s $iSyst -i MCl1loose2016v7__MCCorr2016v7__l2loose__l2tightOR2016v7 -b -Q nextweek
#      done
       for iSyst in METup_suffix METdo_suffix MupTup_suffix MupTdo_suffix ElepTup_suffix ElepTdo_suffix ; do
         mkPostProc.py -p Summer16_102X_nAODv7_Full2016v7 -s $iSyst -i MCl1loose2016v7__MCCorr2016v7__l2loose__l2tightOR2016v7 -b -Q nextweek
       done

#Samples=DYJetsToLL_M-50-LO_ext1,DYJetsToLL_M-50-LO_ext2,DYJetsToLL_M-50-PSup,DYJetsToLL_M-50_HT-100to200,DYJetsToLL_M-50_HT-200to400_ext1,DYJetsToLL_M-50_HT-600to800,DYJetsToLL_M-50_ext2,DYJetsToLL_M-5to50_HT-200to400,DYJetsToLL_M-5to50_HT-400to600,DYJetsToTT_MuEle_M-50_ext1,GJetsDR04_HT200To400,GluGluHToWWTo2L2Nu_Mlarge,GluGluHToZZTo4L_M125,GluGluZH_HToTauTau_ZTo2L_M125,H0L1_ToWWTo2L2Nu,H0L1f05_ToWWTo2L2Nu,H0M_ToWWTo2L2Nu,H0Mf05_ToWWTo2L2Nu,H0PM_ToWWTo2L2Nu,QCD_Pt-120to170_EMEnriched,QCD_Pt-50to80_EMEnriched_ext1,ST_t-channel_antitop,ST_t-channel_top,TTJets_DiLept,TTJets_DiLept_ext1,TTJets_more,TTTo2L2Nu,TTWJetsToQQ,TTZToLLNuNu_M-10_ext2,TT_TuneCUETP8M2T4,VBFHToWWTo2L2Nu_JHUGen698_M2500,VBFHToWWTo2L2Nu_JHUGen698_M500,VBFHToWWTo2L2Nu_M126,VBF_H0L1f05_ToWWTo2L2Nu,VBF_H0Mf05_ToWWTo2L2Nu,VBF_H0PM_ToWWTo2L2Nu,VVTo2L2Nu_ext1,WH_H0L1_ToWWTo2L2Nu,WH_H0L1f05_ToWWTo2L2Nu,WJetsToLNu_HT100_200_ext1,WJetsToLNu_HT100_200_ext2,WJetsToLNu_HT200_400_ext2,WJetsToLNu_ext2,WLLJJToLNu_M-50_QCD_2Jet,WLLJJToLNu_M-50_QCD_3Jet,WLLJJ_WToLNu_EWK,WZTo1L1Nu2Q,WZTo2L2Q,WZTo3LNu_AMCNLO,WZTo3LNu_ext1,WZTo3LNu_mllmin01_ext1,WpWmJJ_EWK_QCD_noTop,WpWpJJ_EWK_POWHEG,ZH_H0L1_ToWWTo2L2Nu,ZH_H0M_ToWWTo2L2Nu,ZH_H0PHf05_ToWWTo2L2Nu,ZH_H0PM_ToWWTo2L2Nu,ZZTo2L2Nu,ZZTo2L2Nu_ext1,ZZTo4L,ZZTo4L_ext1,ggZZ2e2m,ggZZ2m2t,ggZZ4m,tZq_ll_4f,tZq_ll_4f_PSweightsu
#      for iSyst in JESTotalup_suffix JESAbsoluteup_suffix JESBBEC1up_suffix JESEC2up_suffix JESHFup_suffix JESFlavorQCDup_suffix JESRelativeup_suffix ; do
#        mkPostProc.py -p Summer16_102X_nAODv7_Full2016v7 -s $iSyst -i MCl1loose2016v7__MCCorr2016v7__l2loose__l2tightOR2016v7 -b -Q nextweek -T $Samples
#      done
#Samples=DYJetsToLL_M-10to50-LO,DYJetsToLL_M-50-LO_ext1,DYJetsToLL_M-50-LO_ext2,DYJetsToLL_M-50-UEup,DYJetsToLL_M-50_HT-100to200,DYJetsToLL_M-50_HT-100to200_ext1,DYJetsToLL_M-50_HT-1200to2500,DYJetsToLL_M-50_HT-200to400_ext1,DYJetsToLL_M-50_HT-400to600_ext1,DYJetsToLL_M-50_HT-600to800,DYJetsToLL_M-50_HT-70to100,DYJetsToLL_M-50_ext2,DYJetsToLL_M-5to50_HT-100to200,DYJetsToLL_M-5to50_HT-200to400,DYJetsToLL_M-5to50_HT-600toinf,DYJetsToLL_M-5to50_HT-600toinf_ext1,DYJetsToTT_MuEle_M-50_ext1,EWK_LLJJ_MLL-50_MJJ-120,GGHjjToWWTo2L2Nu_minloHJJ_M125,GJetsDR04_HT100To200,GJetsDR04_HT600ToInf,GluGluHToWWTo2L2NuAMCNLO_M125,GluGluHToWWTo2L2Nu_JHUGen698_M3000,GluGluHToWWTo2L2Nu_JHUGen698_M400,GluGluHToWWTo2L2Nu_JHUGen698_M650,GluGluHToWWTo2L2Nu_JHUGen698_M700,GluGluHToWWTo2L2Nu_JHUGen698_M900,GluGluHToWWTo2L2Nu_M125_CUETDown,GluGluHToWWTo2L2Nu_M125_CUETUp,GluGluHToWWTo2L2Nu_M125_minloHJ_NNLOPS,GluGluHToWWTo2L2Nu_M140,GluGluHToWWTo2L2Nu_M165,GluGluHToWWTo2L2Nu_M180,GluGluHToWWTo2L2Nu_M230,GluGluHToWWTo2L2Nu_M270,GluGluHToWWTo2L2Nu_Mlarge,GluGluHToZZTo4L_M125,GluGluZH_HToTauTau_ZTo2L_M125,H0L1_ToWWTo2L2Nu,H0L1f05_ToWWTo2L2Nu,H0M_ToWWTo2L2Nu,H0Mf05_ToWWTo2L2Nu,H0PH_ToWWTo2L2Nu,H0PHf05_ToWWTo2L2Nu,H0PM_ToWWTo2L2Nu,HWminusJ_HToWW_M120,HWminusJ_HToWW_M125,HWplusJ_HToWW_LNu_M120,HWplusJ_HToWW_LNu_M125,HZJ_HToWWTo2L2Nu_ZTo2L_M120,HZJ_HToWWTo2L2Nu_ZTo2L_M125,HZJ_HToWWTo2L2Nu_ZTo2L_M130,QCD_Pt-120to170_EMEnriched,QCD_Pt-170to300_EMEnriched,QCD_Pt-80to120_EMEnriched,QCD_Pt-80to120_EMEnriched_ext1,ST_tW_antitop,ST_tW_antitop_noHad,ST_tW_top_noHad_ext1,TTJets_DiLept,TTJets_DiLept_ext1,TTTo2L2Nu,TTToSemiLeptonic,TTWJetsToQQ,TTZToLLNuNu_M-10_ext1,TTZToLLNuNu_M-10_ext2,TTZToLLNuNu_M-10_ext3,TTZjets,TT_TuneCUETP8M2T4,VBFHToTauTau_M125,VBFHToWWTo2L2NuAMCNLO_M125,VBFHToWWTo2L2NuPowheg_M125,VBFHToWWTo2L2Nu_JHUGen698_M1000,VBFHToWWTo2L2Nu_JHUGen698_M2000,VBFHToWWTo2L2Nu_JHUGen698_M300,VBFHToWWTo2L2Nu_JHUGen698_M350,VBFHToWWTo2L2Nu_JHUGen698_M600,VBFHToWWTo2L2Nu_JHUGen698_M800,VBFHToWWTo2L2Nu_JHUGen714_M4000,VBFHToWWTo2L2Nu_M125_CUETDown,VBFHToWWTo2L2Nu_M165,VBFHToWWTo2L2Nu_M170,VBFHToWWTo2L2Nu_M180,VBFHToWWTo2L2Nu_M230,VBF_H0L1_ToWWTo2L2Nu,VBF_H0M_ToWWTo2L2Nu,VBF_H0Mf05_ToWWTo2L2Nu,VBF_H0PH_ToWWTo2L2Nu,VBF_H0PHf05_ToWWTo2L2Nu,VBF_H0PM_ToWWTo2L2Nu,VVTo2L2Nu,VVTo2L2Nu_ext1,WH_H0L1f05_ToWWTo2L2Nu,WH_H0M_ToWWTo2L2Nu,WH_H0Mf05_ToWWTo2L2Nu,WH_H0PH_ToWWTo2L2Nu,WH_H0PHf05_ToWWTo2L2Nu,WH_H0PM_ToWWTo2L2Nu,WJetsToLNu,WJetsToLNu-LO_ext2,WJetsToLNu_HT200_400,WJetsToLNu_HT200_400_ext1,WJetsToLNu_HT200_400_ext2,WJetsToLNu_HT800_1200_ext1,WJetsToLNu_ext2,WLLJJToLNu_M-4To50_QCD_2Jet,WLLJJToLNu_M-4To50_QCD_3Jet,WLLJJToLNu_M-50_QCD_1Jet,WLLJJToLNu_M-50_QCD_2Jet,WLLJJToLNu_M-50_QCD_3Jet,WLLJJ_WToLNu_EWK,WW-LO,WW-LO_ext1,WWG,WWTo2L2Nu_CUETUp,WWToLNuQQ,WWZ,WZTo1L1Nu2Q,WZTo2L2Q,WZTo3LNu,WZTo3LNu_AMCNLO,WZTo3LNu_ext1,WZTo3LNu_mllmin01_ext1,WZ_ext1,Wg_AMCNLOFXFX_ext1,Wg_AMCNLOFXFX_ext2,Wg_AMCNLOFXFX_ext3,WpWmJJ_EWK_QCD_noTop,WpWpJJ_QCD,ZH_H0L1_ToWWTo2L2Nu,ZH_H0L1f05_ToWWTo2L2Nu,ZH_H0M_ToWWTo2L2Nu,ZH_H0Mf05_ToWWTo2L2Nu,ZH_H0PH_ToWWTo2L2Nu,ZH_H0PHf05_ToWWTo2L2Nu,ZH_H0PM_ToWWTo2L2Nu,ZZTo2L2Nu,ZZTo2L2Nu_ext1,ZZTo2L2Q_AMCNLOFXFX,ZZTo4L,ZZTo4L_ext1,Zg_ext1,bbHToWWTo2L2Nu_M125_yb2,bbHToWWTo2L2Nu_M125_ybyt,ggZZ2e2m,ggZZ2m2n,ggZZ4e,ggZZ4m,tZq_ll_4f,tZq_ll_4f_PSweights,ttH_H0Mf05_ToWWTo2L2Nu
#      for iSyst in JESTotaldo_suffix JESAbsolutedo_suffix JESBBEC1do_suffix JESEC2do_suffix JESHFdo_suffix JESFlavorQCDdo_suffix JESRelativedo_suffix ; do
#        mkPostProc.py -p Summer16_102X_nAODv7_Full2016v7 -s $iSyst -i MCl1loose2016v7__MCCorr2016v7__l2loose__l2tightOR2016v7 -b -Q nextweek -T $Samples
#      done



       for iSyst in JESTotalup_suffix JESAbsoluteup_suffix JESBBEC1up_suffix JESEC2up_suffix JESFlavorQCDup_suffix JESHFup_suffix JESRelativeup_suffix ; do
        mkPostProc.py -p Summer16_102X_nAODv7_Full2016v7 -s $iSyst -i MCl1loose2016v7__MCCorr2016v7__l2loose__l2tightOR2016v7 -b 
       done
       for iSyst in JESTotaldo_suffix JESAbsolutedo_suffix JESBBEC1do_suffix JESEC2do_suffix JESFlavorQCDdo_suffix JESHFdo_suffix JESRelativedo_suffix ; do
        mkPostProc.py -p Summer16_102X_nAODv7_Full2016v7 -s $iSyst -i MCl1loose2016v7__MCCorr2016v7__l2loose__l2tightOR2016v7 -b
       done

#      mkPostProc.py -p Summer16_102X_nAODv7_Full2016v7 -s MCWgStar201Xv7 -b
#      mkPostProc.py -p Summer16_102X_nAODv7_Full2016v7 -s MCWgStarCorr2016v7 -i MCWgStar201Xv7 -b


#### recoil DY

       mkPostProc.py -p Summer16_102X_nAODv7_Full2016v7 -s recoilDY -i MCl1loose2016v7__MCCorr2016v7__l2loose__l2tightOR2016v7 -b
       for iSyst in JESup_suffix JESdo_suffix METup_suffix METdo_suffix MupTup_suffix MupTdo_suffix ElepTup_suffix ElepTdo_suffix ; do
         mkPostProc.py -p Summer16_102X_nAODv7_Full2016v7 -s $iSyst -i MCl1loose2016v7__MCCorr2016v7__l2loose__l2tightOR2016v7__recoilDY -b -Q nextweek
       done
       for iSyst in JESTotalup_suffix JESAbsoluteup_suffix JESBBEC1up_suffix JESEC2up_suffix JESFlavorQCDup_suffix JESHFup_suffix JESRelativeup_suffix ; do
        mkPostProc.py -p Summer16_102X_nAODv7_Full2016v7 -s $iSyst -i MCl1loose2016v7__MCCorr2016v7__l2loose__l2tightOR2016v7__recoilDY -b 
       done
       for iSyst in JESTotaldo_suffix JESAbsolutedo_suffix JESBBEC1do_suffix JESEC2do_suffix JESFlavorQCDdo_suffix JESHFdo_suffix JESRelativedo_suffix ; do
        mkPostProc.py -p Summer16_102X_nAODv7_Full2016v7 -s $iSyst -i MCl1loose2016v7__MCCorr2016v7__l2loose__l2tightOR2016v7__recoilDY -b
       done
 
       echo "Press [CTRL+C] to stop.."
       sleep 1200



done
