S=WZTo3LNu_noPSweights,ZTo2L_ZTo2J_QCD_LO,ttHToNonbb_M125_alternative,ggZZ2m2t_v3

while :
do

       mkPostProc.py -p Run2017_102X_nAODv7_Full2017v7 -s DATAl1loose2017v7 -b
#      mkPostProc.py -p Run2017_102X_nAODv7_Full2017v7 -s fakeSel -i DATAl1loose2017v7 -b
#      mkPostProc.py -p Run2017_102X_nAODv7_Full2017v7 -s l2loose -i DATAl1loose2017v7 -b
#      mkPostProc.py -p Run2017_102X_nAODv7_Full2017v7 -s l2tightOR2017v7 -i DATAl1loose2017v7__l2loose -b

#      mkPostProc.py -p Run2017_102X_nAODv7_Full2017v7 -s fakeW -i DATAl1loose2017v7__l2loose -b

#      mkPostProc.py -p Run2017_102X_nAODv7_Full2017v7 -s DATAWgStar2017v7 -b

       mkPostProc.py -p Fall2017_102X_nAODv7_Full2017v7 -s MCl1loose2017v7 -b -Q nextweek
#      mkPostProc.py -p Fall2017_102X_nAODv7_Full2017v7 -s MCCorr2017v7 -i MCl1loose2017v7 -b -Q nextweek -E $S
#      mkPostProc.py -p Fall2017_102X_nAODv7_Full2017v7 -s fakeSelKinMC -i MCl1loose2017v7 -b -Q nextweek -E WZTo3LNu_noPSweights
#      mkPostProc.py -p Fall2017_102X_nAODv7_Full2017v7 -s fakeSelMC -i MCl1loose2017v7__MCCorr2017v7 -b
#      mkPostProc.py -p Fall2017_102X_nAODv7_Full2017v7 -s l2loose -i MCl1loose2017v7__MCCorr2017v7 -b
#      mkPostProc.py -p Fall2017_102X_nAODv7_Full2017v7 -s l2tightOR2017v7 -i MCl1loose2017v7__MCCorr2017v7__l2loose -b

#      for iSyst in JESup JESdo METup METdo MupTup MupTdo ElepTup ElepTdo ; do
#        mkPostProc.py -p Fall2017_102X_nAODv7_Full2017v7 -s $iSyst -i MCl1loose2017v7__MCCorr2017v7__l2loose__l2tightOR2017v7 -b -Q nextweek
#      done  

#      for iSyst in JESup_suffix JESdo_suffix ; do
#        mkPostProc.py -p Fall2017_102X_nAODv7_Full2017v7 -s $iSyst -i MCl1loose2017v7__MCCorr2017v7__l2loose__l2tightOR2017v7 -b -Q nextweek
#      done

#      for iSyst in METup_suffix METdo_suffix MupTup_suffix MupTdo_suffix ElepTup_suffix ElepTdo_suffix ; do
#        mkPostProc.py -p Fall2017_102X_nAODv7_Full2017v7 -s $iSyst -i MCl1loose2017v7__MCCorr2017v7__l2loose__l2tightOR2017v7 -b -Q nextweek
#      done

#      mkPostProc.py -p Fall2017_102X_nAODv7_Full2017v7 -s MCWgStar201Xv7 -b
#      mkPostProc.py -p Fall2017_102X_nAODv7_Full2017v7 -s MCWgStarCorr2017v7 -i MCWgStar201Xv7 -b

       echo "Press [CTRL+C] to stop.."
       sleep 1200

done
