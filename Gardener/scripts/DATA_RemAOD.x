  
for Run in B C D E F G H; do 
 
  # L2 loose Cut
  
# ./mkGardener.py -p Feb2017_Run2016${Run}_RemAOD -s l2looseCut -S Target -b
# ./mkGardener.py -p Feb2017_Run2016${Run}_RemAOD -s hadd -i l2looseCut -S Target -b
# ./mkGardener.py -p Feb2017_Run2016${Run}_RemAOD -s EpTCorr,TrigMakerData,l2tight,vbsSel -C -i l2looseCut__hadd -S Target -b
 
  # Fix 
  ./mkGardener.py -p Feb2017_Run2016${Run}_RemAOD -s dymvaHiggs -i l2looseCut__hadd__EpTCorr -S Target -b
  ./mkGardener.py -p Feb2017_Run2016${Run}_RemAOD -s dymvaHiggs -i l2looseCut__hadd__EpTCorr__TrigMakerData -S Target -b
  ./mkGardener.py -p Feb2017_Run2016${Run}_RemAOD -s dymvaHiggs -i l2looseCut__hadd__EpTCorr__TrigMakerData__l2tight -S Target -b
  
  # FakeWCut
  
# ./mkGardener.py -p Feb2017_Run2016${Run}_RemAOD -s fakeWCut -i l2looseCut__hadd__EpTCorr__TrigMakerData -S Target -b

  # Fix
  ./mkGardener.py -p Feb2017_Run2016${Run}_RemAOD -s dymvaHiggs -i l2looseCut__hadd__EpTCorr__TrigMakerData__fakeWCut -S Target -b
  
  # L2 vloose Cut
  
# ./mkGardener.py -p Feb2017_Run2016${Run}_RemAOD -s l2vlooseCut -S Target -b
# ./mkGardener.py -p Feb2017_Run2016${Run}_RemAOD -s hadd -i l2vlooseCut -S Target -b 
# ./mkGardener.py -p Feb2017_Run2016${Run}_RemAOD -s EpTCorr,TrigMakerData,l2tight,vbsSel -C -i l2vlooseCut__hadd -S Target -b
# ./mkGardener.py -p Feb2017_Run2016${Run}_RemAOD -s vbsSel -i l2vlooseCut__hadd__EpTCorr__TrigMakerData -S Target -b
 
  # L1 loose Cut
  
# ./mkGardener.py -p Feb2017_Run2016${Run}_RemAOD -s l1looseCut -S Target -b
# ./mkGardener.py -p Feb2017_Run2016${Run}_RemAOD -s EpTCorr,fakeSel -C -i l1looseCut -S Target -b
# ./mkGardener.py -p Feb2017_Run2016${Run}_RemAOD -s hadd -i l1looseCut__EpTCorr__fakeSel -S Target -b
  
  # L1 vloose Cut
  
# ./mkGardener.py -p Feb2017_Run2016${Run}_RemAOD -s l1vlooseCut -S Target -b
# ./mkGardener.py -p Feb2017_Run2016${Run}_RemAOD -s EpTCorr,fakeSel -C -i l1vlooseCut -S Target -b
# ./mkGardener.py -p Feb2017_Run2016${Run}_RemAOD -s hadd -i l1vlooseCut__EpTCorr__fakeSel -S Target -b
 
done 
