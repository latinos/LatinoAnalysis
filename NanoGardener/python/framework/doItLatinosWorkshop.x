
while :
do

      mkPostProc.py -p Summer20UL18_106x_nAODv9_Full2018v9_LatinosWorkshopExercise -s MCl1loose2018v9_WS -b -T DYJetsToLL_M-50 -Q tomorrow 
      mkPostProc.py -p Summer20UL18_106x_nAODv9_Full2018v9_LatinosWorkshopExercise -i MCl1loose2018v9_WS -s MCCorr2018v9_WS -b -T DYJetsToLL_M-50 -Q nextweek 

      for iSyst in ElepTdo_suffix_WS ElepTup_suffix_WS ; do
        mkPostProc.py -p Summer20UL18_106x_nAODv9_Full2018v9_LatinosWorkshopExercise -s $iSyst -i MCl1loose2018v9_WS__MCCorr2018v9_WS -b -T DYJetsToLL_M-50 -Q nextweek 
      done
      sleep 300
done
