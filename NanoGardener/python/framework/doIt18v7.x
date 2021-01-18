samples=QCD_HT700to1000,QCD_HT1500to2000,QCD_HT1000to1500,QCD_HT200to300,QCD_HT300to500,QCD_HT2000toInf,HWminusJ_HToTauTau_M125,TT_DiLept_1Jet
samples=TT_DiLept_1Jet,ggZZ4t_CP5,GJetsDR04_HT200To400,ggZZ2m2t_CP5
while :
do

       mkPostProc.py -p Run2018_102X_nAODv7_Full2018v7 -s DATAl1loose2018v7 -b
#      mkPostProc.py -p Run2018_102X_nAODv7_Full2018v7 -s fakeSel -i DATAl1loose2018v7 -b
#      mkPostProc.py -p Run2018_102X_nAODv7_Full2018v7 -s l2loose -i DATAl1loose2018v7 -b
#      mkPostProc.py -p Run2018_102X_nAODv7_Full2018v7 -s l2tightOR2018v7 -i DATAl1loose2018v7__l2loose -b

#      mkPostProc.py -p Run2018_102X_nAODv7_Full2018v7 -s fakeW -i DATAl1loose2018v7__l2loose -b

#      mkPostProc.py -p Run2018_102X_nAODv7_Full2018v7 -s DATAWgStar201Xv7 -b

       mkPostProc.py -p Autumn18_102X_nAODv7_Full2018v7 -s MCl1loose2018v7 -b 
#      mkPostProc.py -p Autumn18_102X_nAODv7_Full2018v7 -s MCCorr2018v7 -i MCl1loose2018v7 -b -E $samples
#      mkPostProc.py -p Autumn18_102X_nAODv7_Full2018v7 -s fakeSelKinMC -i MCl1loose2018v7 -b -E $samples
#      mkPostProc.py -p Autumn18_102X_nAODv7_Full2018v7 -s fakeSelMC -i MCl1loose2018v7__MCCorr2018v7 -b
#      mkPostProc.py -p Autumn18_102X_nAODv7_Full2018v7 -s l2loose -i MCl1loose2018v7__MCCorr2018v7 -b
#      mkPostProc.py -p Autumn18_102X_nAODv7_Full2018v7 -s l2tightOR2018v7 -i MCl1loose2018v7__MCCorr2018v7__l2loose -b

#      for iSyst in JESup_suffix JESdo_suffix ; do
#        mkPostProc.py -p Autumn18_102X_nAODv7_Full2018v7 -s $iSyst -i MCl1loose2018v7__MCCorr2018v7__l2loose__l2tightOR2018v7 -b -Q nextweek
#      done

#      for iSyst in JERup_suffix JERdo_suffix METup_suffix METdo_suffix MupTup_suffix MupTdo_suffix ElepTup_suffix ElepTdo_suffix ; do
#        mkPostProc.py -p Autumn18_102X_nAODv7_Full2018v7 -s $iSyst -i MCl1loose2018v7__MCCorr2018v7__l2loose__l2tightOR2018v7 -b  -Q nextweek
#      done

#      mkPostProc.py -p Autumn18_102X_nAODv7_Full2018v7 -s MCWgStar201Xv7 -b
#      mkPostProc.py -p Autumn18_102X_nAODv7_Full2018v7 -s MCWgStarCorr2018v7 -i MCWgStar201Xv7 -b

# recoilDY
       mkPostProc.py -p Autumn18_102X_nAODv7_Full2018v7 -s recoilDY -i MCl1loose2018v7__MCCorr2018v7__l2loose__l2tightOR2018v7 -b
       for iSyst in JESup_suffix JESdo_suffix JERup_suffix JERdo_suffix METup_suffix METdo_suffix MupTup_suffix MupTdo_suffix ElepTup_suffix ElepTdo_suffix ; do 
         mkPostProc.py -p Autumn18_102X_nAODv7_Full2018v7 -s $iSyst -i MCl1loose2018v7__MCCorr2018v7__l2loose__l2tightOR2018v7__recoilDY -b  -Q nextweek
       done


for iSyst in JESTotalup_suffix JESAbsoluteup_suffix JESBBEC1up_suffix JESEC2up_suffix JESFlavorQCDup_suffix JESHFup_suffix JESRelativeup_suffix ; do
  mkPostProc.py -p Autumn18_102X_nAODv7_Full2018v7 -s $iSyst -i MCl1loose2018v7__MCCorr2018v7__l2loose__l2tightOR2018v7__recoilDY -b 
done
for iSyst in JESTotaldo_suffix JESAbsolutedo_suffix JESBBEC1do_suffix JESEC2do_suffix JESFlavorQCDdo_suffix JESHFdo_suffix JESRelativedo_suffix ; do
  mkPostProc.py -p Autumn18_102X_nAODv7_Full2018v7 -s $iSyst -i MCl1loose2018v7__MCCorr2018v7__l2loose__l2tightOR2018v7__recoilDY -b 
done


       echo "Press [CTRL+C] to stop.."
       sleep 1200

done
