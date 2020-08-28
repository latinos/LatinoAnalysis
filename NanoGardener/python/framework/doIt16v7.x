Samples=WJetsToLNu_Wpt600ToInf,WJetsToLNu_Wpt100To250,WJetsToLNu_Wpt400To600_ext1,WJetsToLNu_Wpt250To400_ext1,WJetsToLNu_Wpt600ToInf_ext1,WJetsToLNu_Wpt250To400,WWTo4Q_4f,WJetsToLNu_Wpt100To250_ext1,WJetsToLNu_Wpt400To600,WJetsToLNu_Wpt600ToInf,WJetsToLNu_Wpt250To400_ext4,WJetsToLNu_Wpt100To250_ext4


while :
do

       mkPostProc.py -p Run2016_102X_nAODv7_Full2016v7 -s DATAl1loose2016v7 -b
#      mkPostProc.py -p Run2016_102X_nAODv7_Full2016v7 -s fakeSel -i DATAl1loose2016v7 -b
#      mkPostProc.py -p Run2016_102X_nAODv7_Full2016v7 -s l2loose -i DATAl1loose2016v7 -b
#      mkPostProc.py -p Run2016_102X_nAODv7_Full2016v7 -s l2tightOR2016v7 -i DATAl1loose2016v7__l2loose -b

#      mkPostProc.py -p Run2016_102X_nAODv7_Full2016v7 -s fakeW -i DATAl1loose2016v7__l2loose -b

#      mkPostProc.py -p Run2016_102X_nAODv7_Full2016v7 -s DATAWgStar2016v7 -b

       mkPostProc.py -p Summer16_102X_nAODv7_Full2016v7 -s MCl1loose2016v7 -b -Q nextweek
#      mkPostProc.py -p Summer16_102X_nAODv7_Full2016v7 -s MCCorr2016v7 -i MCl1loose2016v7 -b -Q nextweek -E $Samples
#      mkPostProc.py -p Summer16_102X_nAODv7_Full2016v7 -s fakeSelMC -i MCl1loose2016v7__MCCorr2016v7 -b
#      mkPostProc.py -p Summer16_102X_nAODv7_Full2016v7 -s fakeSelKinMC i MCl1loose2016v7 -b
#      mkPostProc.py -p Summer16_102X_nAODv7_Full2016v7 -s l2loose -i MCl1loose2016v7__MCCorr2016v7 -b
#      mkPostProc.py -p Summer16_102X_nAODv7_Full2016v7 -s l2tightOR2016v7 -i MCl1loose2016v7__MCCorr2016v7__l2loose -b

#      for iSyst in JESup JESdo METup METdo MupTup MupTdo ElepTup ElepTdo ; do
#        mkPostProc.py -p Summer16_102X_nAODv7_Full2016v7 -s $iSyst -i MCl1loose2016v7__MCCorr2016v7__l2loose__l2tightOR2016v7 -b
#      done

#      for iSyst in JESup_suffix JESdo_suffix ; do
#        mkPostProc.py -p Summer16_102X_nAODv7_Full2016v7 -s $iSyst -i MCl1loose2016v7__MCCorr2016v7__l2loose__l2tightOR2016v7 -b -Q nextweek
#      done
#      for iSyst in METup_suffix METdo_suffix MupTup_suffix MupTdo_suffix ElepTup_suffix ElepTdo_suffix ; do
#        mkPostProc.py -p Summer16_102X_nAODv7_Full2016v7 -s $iSyst -i MCl1loose2016v7__MCCorr2016v7__l2loose__l2tightOR2016v7 -b -Q nextweek
#      done


#      mkPostProc.py -p Summer16_102X_nAODv7_Full2016v7 -s MCWgStar201Xv5 -b
#      mkPostProc.py -p Summer16_102X_nAODv7_Full2016v7 -s MCWgStarCorr2016v7 -i MCWgStar201Xv5 -b


       echo "Press [CTRL+C] to stop.."
       sleep 1200

done
