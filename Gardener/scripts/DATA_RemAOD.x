
# L2 loose Cut

./mkGardener.py -p Feb2017_Run2016B_RemAOD -s l2looseCut -S Target -b
./mkGardener.py -p Feb2017_Run2016C_RemAOD -s l2looseCut -S Target -b
./mkGardener.py -p Feb2017_Run2016D_RemAOD -s l2looseCut -S Target -b
./mkGardener.py -p Feb2017_Run2016E_RemAOD -s l2looseCut -S Target -b
./mkGardener.py -p Feb2017_Run2016F_RemAOD -s l2looseCut -S Target -b
./mkGardener.py -p Feb2017_Run2016G_RemAOD -s l2looseCut -S Target -b 
./mkGardener.py -p Feb2017_Run2016H_RemAOD -s l2looseCut -S Target -b

./mkGardener.py -p Feb2017_Run2016B_RemAOD -s hadd -i l2looseCut -S Target -b
./mkGardener.py -p Feb2017_Run2016C_RemAOD -s hadd -i l2looseCut -S Target -b
./mkGardener.py -p Feb2017_Run2016D_RemAOD -s hadd -i l2looseCut -S Target -b
./mkGardener.py -p Feb2017_Run2016E_RemAOD -s hadd -i l2looseCut -S Target -b
./mkGardener.py -p Feb2017_Run2016F_RemAOD -s hadd -i l2looseCut -S Target -b
./mkGardener.py -p Feb2017_Run2016G_RemAOD -s hadd -i l2looseCut -S Target -b
./mkGardener.py -p Feb2017_Run2016H_RemAOD -s hadd -i l2looseCut -S Target -b

./mkGardener.py -p Feb2017_Run2016B_RemAOD -s EpTCorr,TrigMakerData,l2tight,vbsSel -C -i l2looseCut__hadd -S Target -b
./mkGardener.py -p Feb2017_Run2016C_RemAOD -s EpTCorr,TrigMakerData,l2tight,vbsSel -C -i l2looseCut__hadd -S Target -b
./mkGardener.py -p Feb2017_Run2016D_RemAOD -s EpTCorr,TrigMakerData,l2tight,vbsSel -C -i l2looseCut__hadd -S Target -b
./mkGardener.py -p Feb2017_Run2016E_RemAOD -s EpTCorr,TrigMakerData,l2tight,vbsSel -C -i l2looseCut__hadd -S Target -b
./mkGardener.py -p Feb2017_Run2016F_RemAOD -s EpTCorr,TrigMakerData,l2tight,vbsSel -C -i l2looseCut__hadd -S Target -b
./mkGardener.py -p Feb2017_Run2016G_RemAOD -s EpTCorr,TrigMakerData,l2tight,vbsSel -C -i l2looseCut__hadd -S Target -b
./mkGardener.py -p Feb2017_Run2016H_RemAOD -s EpTCorr,TrigMakerData,l2tight,vbsSel -C -i l2looseCut__hadd -S Target -b

# FakeWCut

./mkGardener.py -p Feb2017_Run2016B_RemAOD -s fakeWCut -i l2looseCut__hadd__EpTCorr__TrigMakerData -S Target -b
./mkGardener.py -p Feb2017_Run2016C_RemAOD -s fakeWCut -i l2looseCut__hadd__EpTCorr__TrigMakerData -S Target -b
./mkGardener.py -p Feb2017_Run2016D_RemAOD -s fakeWCut -i l2looseCut__hadd__EpTCorr__TrigMakerData -S Target -b
./mkGardener.py -p Feb2017_Run2016E_RemAOD -s fakeWCut -i l2looseCut__hadd__EpTCorr__TrigMakerData -S Target -b
./mkGardener.py -p Feb2017_Run2016F_RemAOD -s fakeWCut -i l2looseCut__hadd__EpTCorr__TrigMakerData -S Target -b
./mkGardener.py -p Feb2017_Run2016G_RemAOD -s fakeWCut -i l2looseCut__hadd__EpTCorr__TrigMakerData -S Target -b
./mkGardener.py -p Feb2017_Run2016H_RemAOD -s fakeWCut -i l2looseCut__hadd__EpTCorr__TrigMakerData -S Target -b

# L2 vloose Cut

./mkGardener.py -p Feb2017_Run2016B_RemAOD -s l2vlooseCut -S Target -b
./mkGardener.py -p Feb2017_Run2016C_RemAOD -s l2vlooseCut -S Target -b
./mkGardener.py -p Feb2017_Run2016D_RemAOD -s l2vlooseCut -S Target -b
./mkGardener.py -p Feb2017_Run2016E_RemAOD -s l2vlooseCut -S Target -b
./mkGardener.py -p Feb2017_Run2016F_RemAOD -s l2vlooseCut -S Target -b
./mkGardener.py -p Feb2017_Run2016G_RemAOD -s l2vlooseCut -S Target -b 
./mkGardener.py -p Feb2017_Run2016H_RemAOD -s l2vlooseCut -S Target -b

./mkGardener.py -p Feb2017_Run2016B_RemAOD -s hadd -i l2vlooseCut -S Target -b 
./mkGardener.py -p Feb2017_Run2016C_RemAOD -s hadd -i l2vlooseCut -S Target -b 
./mkGardener.py -p Feb2017_Run2016D_RemAOD -s hadd -i l2vlooseCut -S Target -b 
./mkGardener.py -p Feb2017_Run2016E_RemAOD -s hadd -i l2vlooseCut -S Target -b 
./mkGardener.py -p Feb2017_Run2016F_RemAOD -s hadd -i l2vlooseCut -S Target -b 
./mkGardener.py -p Feb2017_Run2016G_RemAOD -s hadd -i l2vlooseCut -S Target -b 
./mkGardener.py -p Feb2017_Run2016H_RemAOD -s hadd -i l2vlooseCut -S Target -b 

./mkGardener.py -p Feb2017_Run2016B_RemAOD -s EpTCorr,TrigMakerData,l2tight,vbsSel -C -i l2vlooseCut__hadd -S Target -b
./mkGardener.py -p Feb2017_Run2016C_RemAOD -s EpTCorr,TrigMakerData,l2tight,vbsSel -C -i l2vlooseCut__hadd -S Target -b
./mkGardener.py -p Feb2017_Run2016D_RemAOD -s EpTCorr,TrigMakerData,l2tight,vbsSel -C -i l2vlooseCut__hadd -S Target -b
./mkGardener.py -p Feb2017_Run2016E_RemAOD -s EpTCorr,TrigMakerData,l2tight,vbsSel -C -i l2vlooseCut__hadd -S Target -b
./mkGardener.py -p Feb2017_Run2016F_RemAOD -s EpTCorr,TrigMakerData,l2tight,vbsSel -C -i l2vlooseCut__hadd -S Target -b
./mkGardener.py -p Feb2017_Run2016G_RemAOD -s EpTCorr,TrigMakerData,l2tight,vbsSel -C -i l2vlooseCut__hadd -S Target -b
./mkGardener.py -p Feb2017_Run2016H_RemAOD -s EpTCorr,TrigMakerData,l2tight,vbsSel -C -i l2vlooseCut__hadd -S Target -b

./mkGardener.py -p Feb2017_Run2016B_RemAOD -s vbsSel -i l2vlooseCut__hadd__EpTCorr__TrigMakerData -S Target -b
./mkGardener.py -p Feb2017_Run2016C_RemAOD -s vbsSel -i l2vlooseCut__hadd__EpTCorr__TrigMakerData -S Target -b
./mkGardener.py -p Feb2017_Run2016D_RemAOD -s vbsSel -i l2vlooseCut__hadd__EpTCorr__TrigMakerData -S Target -b
./mkGardener.py -p Feb2017_Run2016E_RemAOD -s vbsSel -i l2vlooseCut__hadd__EpTCorr__TrigMakerData -S Target -b
./mkGardener.py -p Feb2017_Run2016F_RemAOD -s vbsSel -i l2vlooseCut__hadd__EpTCorr__TrigMakerData -S Target -b
./mkGardener.py -p Feb2017_Run2016G_RemAOD -s vbsSel -i l2vlooseCut__hadd__EpTCorr__TrigMakerData -S Target -b
./mkGardener.py -p Feb2017_Run2016H_RemAOD -s vbsSel -i l2vlooseCut__hadd__EpTCorr__TrigMakerData -S Target -b


# L1 loose Cut

./mkGardener.py -p Feb2017_Run2016B_RemAOD -s l1looseCut -S Target -b
./mkGardener.py -p Feb2017_Run2016C_RemAOD -s l1looseCut -S Target -b
./mkGardener.py -p Feb2017_Run2016D_RemAOD -s l1looseCut -S Target -b
./mkGardener.py -p Feb2017_Run2016E_RemAOD -s l1looseCut -S Target -b
./mkGardener.py -p Feb2017_Run2016F_RemAOD -s l1looseCut -S Target -b
./mkGardener.py -p Feb2017_Run2016G_RemAOD -s l1looseCut -S Target -b 
./mkGardener.py -p Feb2017_Run2016H_RemAOD -s l1looseCut -S Target -b

./mkGardener.py -p Feb2017_Run2016B_RemAOD -s EpTCorr,fakeSel -C -i l1looseCut -S Target -b
./mkGardener.py -p Feb2017_Run2016C_RemAOD -s EpTCorr,fakeSel -C -i l1looseCut -S Target -b
./mkGardener.py -p Feb2017_Run2016D_RemAOD -s EpTCorr,fakeSel -C -i l1looseCut -S Target -b
./mkGardener.py -p Feb2017_Run2016E_RemAOD -s EpTCorr,fakeSel -C -i l1looseCut -S Target -b
./mkGardener.py -p Feb2017_Run2016F_RemAOD -s EpTCorr,fakeSel -C -i l1looseCut -S Target -b
./mkGardener.py -p Feb2017_Run2016G_RemAOD -s EpTCorr,fakeSel -C -i l1looseCut -S Target -b
./mkGardener.py -p Feb2017_Run2016H_RemAOD -s EpTCorr,fakeSel -C -i l1looseCut -S Target -b

./mkGardener.py -p Feb2017_Run2016B_RemAOD -s hadd -i l1looseCut__EpTCorr__fakeSel -S Target -b
./mkGardener.py -p Feb2017_Run2016C_RemAOD -s hadd -i l1looseCut__EpTCorr__fakeSel -S Target -b
./mkGardener.py -p Feb2017_Run2016D_RemAOD -s hadd -i l1looseCut__EpTCorr__fakeSel -S Target -b
./mkGardener.py -p Feb2017_Run2016E_RemAOD -s hadd -i l1looseCut__EpTCorr__fakeSel -S Target -b
./mkGardener.py -p Feb2017_Run2016F_RemAOD -s hadd -i l1looseCut__EpTCorr__fakeSel -S Target -b
./mkGardener.py -p Feb2017_Run2016G_RemAOD -s hadd -i l1looseCut__EpTCorr__fakeSel -S Target -b
./mkGardener.py -p Feb2017_Run2016H_RemAOD -s hadd -i l1looseCut__EpTCorr__fakeSel -S Target -b

# L1 vloose Cut

./mkGardener.py -p Feb2017_Run2016B_RemAOD -s l1vlooseCut -S Target -b
./mkGardener.py -p Feb2017_Run2016C_RemAOD -s l1vlooseCut -S Target -b
./mkGardener.py -p Feb2017_Run2016D_RemAOD -s l1vlooseCut -S Target -b
./mkGardener.py -p Feb2017_Run2016E_RemAOD -s l1vlooseCut -S Target -b
./mkGardener.py -p Feb2017_Run2016F_RemAOD -s l1vlooseCut -S Target -b
./mkGardener.py -p Feb2017_Run2016G_RemAOD -s l1vlooseCut -S Target -b 
./mkGardener.py -p Feb2017_Run2016H_RemAOD -s l1vlooseCut -S Target -b

./mkGardener.py -p Feb2017_Run2016B_RemAOD -s EpTCorr,fakeSel -C -i l1vlooseCut -S Target -b
./mkGardener.py -p Feb2017_Run2016C_RemAOD -s EpTCorr,fakeSel -C -i l1vlooseCut -S Target -b
./mkGardener.py -p Feb2017_Run2016D_RemAOD -s EpTCorr,fakeSel -C -i l1vlooseCut -S Target -b
./mkGardener.py -p Feb2017_Run2016E_RemAOD -s EpTCorr,fakeSel -C -i l1vlooseCut -S Target -b
./mkGardener.py -p Feb2017_Run2016F_RemAOD -s EpTCorr,fakeSel -C -i l1vlooseCut -S Target -b
./mkGardener.py -p Feb2017_Run2016G_RemAOD -s EpTCorr,fakeSel -C -i l1vlooseCut -S Target -b
./mkGardener.py -p Feb2017_Run2016H_RemAOD -s EpTCorr,fakeSel -C -i l1vlooseCut -S Target -b

./mkGardener.py -p Feb2017_Run2016B_RemAOD -s hadd -i l1vlooseCut__EpTCorr__fakeSel -S Target -b
./mkGardener.py -p Feb2017_Run2016C_RemAOD -s hadd -i l1vlooseCut__EpTCorr__fakeSel -S Target -b
./mkGardener.py -p Feb2017_Run2016D_RemAOD -s hadd -i l1vlooseCut__EpTCorr__fakeSel -S Target -b
./mkGardener.py -p Feb2017_Run2016E_RemAOD -s hadd -i l1vlooseCut__EpTCorr__fakeSel -S Target -b
./mkGardener.py -p Feb2017_Run2016F_RemAOD -s hadd -i l1vlooseCut__EpTCorr__fakeSel -S Target -b
./mkGardener.py -p Feb2017_Run2016G_RemAOD -s hadd -i l1vlooseCut__EpTCorr__fakeSel -S Target -b
./mkGardener.py -p Feb2017_Run2016H_RemAOD -s hadd -i l1vlooseCut__EpTCorr__fakeSel -S Target -b

