
# L2 loose Cut

./mkGardener.py -p Dec2016_Run2016B_ReReco -s l2looseCut -S Target -b
./mkGardener.py -p Dec2016_Run2016C_ReReco -s l2looseCut -S Target -b
./mkGardener.py -p Dec2016_Run2016D_ReReco -s l2looseCut -S Target -b
./mkGardener.py -p Dec2016_Run2016E_ReReco -s l2looseCut -S Target -b
./mkGardener.py -p Dec2016_Run2016F_ReReco -s l2looseCut -S Target -b
./mkGardener.py -p Dec2016_Run2016G_ReReco -s l2looseCut -S Target -b 
./mkGardener.py -p Dec2016_Run2016H_PromptReco -s l2looseCut -S Target -b
./mkGardener.py -p Feb2017_Run2016G_RemAOD_Dec2016Fix -s l2looseCut -S Target -b

./mkGardener.py -p Dec2016_Run2016B_ReReco -s hadd -i l2looseCut -S Target -b
./mkGardener.py -p Dec2016_Run2016C_ReReco -s hadd -i l2looseCut -S Target -b
./mkGardener.py -p Dec2016_Run2016D_ReReco -s hadd -i l2looseCut -S Target -b
./mkGardener.py -p Dec2016_Run2016E_ReReco -s hadd -i l2looseCut -S Target -b
./mkGardener.py -p Dec2016_Run2016F_ReReco -s hadd -i l2looseCut -S Target -b
./mkGardener.py -p Dec2016_Run2016G_ReReco -s hadd -i l2looseCut -S Target -b
./mkGardener.py -p Dec2016_Run2016H_PromptReco -s hadd -i l2looseCut -S Target -b
./mkGardener.py -p Feb2017_Run2016G_RemAOD_Dec2016Fix -s hadd -i l2looseCut -S Target -b

./mkGardener.py -p Dec2016_Run2016B_ReReco -s TrigMakerData,l2tight,vbsSel -C -i l2looseCut__hadd -S Target -b
./mkGardener.py -p Dec2016_Run2016C_ReReco -s TrigMakerData,l2tight,vbsSel -C -i l2looseCut__hadd -S Target -b
./mkGardener.py -p Dec2016_Run2016D_ReReco -s TrigMakerData,l2tight,vbsSel -C -i l2looseCut__hadd -S Target -b
./mkGardener.py -p Dec2016_Run2016E_ReReco -s TrigMakerData,l2tight,vbsSel -C -i l2looseCut__hadd -S Target -b
./mkGardener.py -p Dec2016_Run2016F_ReReco -s TrigMakerData,l2tight,vbsSel -C -i l2looseCut__hadd -S Target -b
./mkGardener.py -p Dec2016_Run2016G_ReReco -s TrigMakerData,l2tight,vbsSel -C -i l2looseCut__hadd -S Target -b
./mkGardener.py -p Dec2016_Run2016H_PromptReco -s TrigMakerData,l2tight,vbsSel -C -i l2looseCut__hadd -S Target -b
./mkGardener.py -p Feb2017_Run2016G_RemAOD_Dec2016Fix -s TrigMakerData,l2tight,vbsSel -C -i l2looseCut__hadd -S Target -b

#./mkGardener.py -p Dec2016_Run2016B_ReReco -s vbsSel -i l2looseCut__hadd__l2tight -S Target -b
#./mkGardener.py -p Dec2016_Run2016C_ReReco -s vbsSel -i l2looseCut__hadd__l2tight -S Target -b
#./mkGardener.py -p Dec2016_Run2016D_ReReco -s vbsSel -i l2looseCut__hadd__l2tight -S Target -b
#./mkGardener.py -p Dec2016_Run2016E_ReReco -s vbsSel -i l2looseCut__hadd__l2tight -S Target -b
#./mkGardener.py -p Dec2016_Run2016F_ReReco -s vbsSel -i l2looseCut__hadd__l2tight -S Target -b
#./mkGardener.py -p Dec2016_Run2016G_ReReco -s vbsSel -i l2looseCut__hadd__l2tight -S Target -b
#./mkGardener.py -p Dec2016_Run2016H_PromptReco -s vbsSel -i l2looseCut__hadd__l2tight -S Target -b


# L2 vloose Cut

./mkGardener.py -p Dec2016_Run2016B_ReReco -s l2vlooseCut -S Target -b
./mkGardener.py -p Dec2016_Run2016C_ReReco -s l2vlooseCut -S Target -b
./mkGardener.py -p Dec2016_Run2016D_ReReco -s l2vlooseCut -S Target -b
./mkGardener.py -p Dec2016_Run2016E_ReReco -s l2vlooseCut -S Target -b
./mkGardener.py -p Dec2016_Run2016F_ReReco -s l2vlooseCut -S Target -b
./mkGardener.py -p Dec2016_Run2016G_ReReco -s l2vlooseCut -S Target -b 
./mkGardener.py -p Dec2016_Run2016H_PromptReco -s l2vlooseCut -S Target -b
./mkGardener.py -p Feb2017_Run2016G_RemAOD_Dec2016Fix -s l2vlooseCut -S Target -b

./mkGardener.py -p Dec2016_Run2016B_ReReco -s hadd -i l2vlooseCut -S Target -b 
./mkGardener.py -p Dec2016_Run2016C_ReReco -s hadd -i l2vlooseCut -S Target -b 
./mkGardener.py -p Dec2016_Run2016D_ReReco -s hadd -i l2vlooseCut -S Target -b 
./mkGardener.py -p Dec2016_Run2016E_ReReco -s hadd -i l2vlooseCut -S Target -b 
./mkGardener.py -p Dec2016_Run2016F_ReReco -s hadd -i l2vlooseCut -S Target -b 
./mkGardener.py -p Dec2016_Run2016G_ReReco -s hadd -i l2vlooseCut -S Target -b 
./mkGardener.py -p Dec2016_Run2016H_PromptReco -s hadd -i l2vlooseCut -S Target -b 
./mkGardener.py -p Feb2017_Run2016G_RemAOD_Dec2016Fix -s hadd -i l2vlooseCut -S Target -b 

./mkGardener.py -p Dec2016_Run2016B_ReReco -s TrigMakerData,l2tight,vbsSel -C -i l2vlooseCut__hadd -S Target -b
./mkGardener.py -p Dec2016_Run2016C_ReReco -s TrigMakerData,l2tight,vbsSel -C -i l2vlooseCut__hadd -S Target -b
./mkGardener.py -p Dec2016_Run2016D_ReReco -s TrigMakerData,l2tight,vbsSel -C -i l2vlooseCut__hadd -S Target -b
./mkGardener.py -p Dec2016_Run2016E_ReReco -s TrigMakerData,l2tight,vbsSel -C -i l2vlooseCut__hadd -S Target -b
./mkGardener.py -p Dec2016_Run2016F_ReReco -s TrigMakerData,l2tight,vbsSel -C -i l2vlooseCut__hadd -S Target -b
./mkGardener.py -p Dec2016_Run2016G_ReReco -s TrigMakerData,l2tight,vbsSel -C -i l2vlooseCut__hadd -S Target -b
./mkGardener.py -p Dec2016_Run2016H_PromptReco -s TrigMakerData,l2tight,vbsSel -C -i l2vlooseCut__hadd -S Target -b
./mkGardener.py -p Feb2017_Run2016G_RemAOD_Dec2016Fix -s TrigMakerData,l2tight,vbsSel -C -i l2vlooseCut__hadd -S Target -b

./mkGardener.py -p Dec2016_Run2016B_ReReco -s vbsSel -i l2vlooseCut__hadd__TrigMakerData -S Target -b
./mkGardener.py -p Dec2016_Run2016C_ReReco -s vbsSel -i l2vlooseCut__hadd__TrigMakerData -S Target -b
./mkGardener.py -p Dec2016_Run2016D_ReReco -s vbsSel -i l2vlooseCut__hadd__TrigMakerData -S Target -b
./mkGardener.py -p Dec2016_Run2016E_ReReco -s vbsSel -i l2vlooseCut__hadd__TrigMakerData -S Target -b
./mkGardener.py -p Dec2016_Run2016F_ReReco -s vbsSel -i l2vlooseCut__hadd__TrigMakerData -S Target -b
./mkGardener.py -p Dec2016_Run2016G_ReReco -s vbsSel -i l2vlooseCut__hadd__TrigMakerData -S Target -b
./mkGardener.py -p Dec2016_Run2016H_PromptReco -s vbsSel -i l2vlooseCut__hadd__TrigMakerData -S Target -b
./mkGardener.py -p Feb2017_Run2016G_RemAOD_Dec2016Fix -s vbsSel -i l2vlooseCut__hadd__TrigMakerData -S Target -b


# L1 loose Cut

./mkGardener.py -p Dec2016_Run2016B_ReReco -s l1looseCut -S Target -b
./mkGardener.py -p Dec2016_Run2016C_ReReco -s l1looseCut -S Target -b
./mkGardener.py -p Dec2016_Run2016D_ReReco -s l1looseCut -S Target -b
./mkGardener.py -p Dec2016_Run2016E_ReReco -s l1looseCut -S Target -b
./mkGardener.py -p Dec2016_Run2016F_ReReco -s l1looseCut -S Target -b
./mkGardener.py -p Dec2016_Run2016G_ReReco -s l1looseCut -S Target -b 
./mkGardener.py -p Dec2016_Run2016H_PromptReco -s l1looseCut -S Target -b
./mkGardener.py -p Feb2017_Run2016G_RemAOD_Dec2016Fix -s l1looseCut -S Target -b

./mkGardener.py -p Dec2016_Run2016B_ReReco -s fakeSel -i l1looseCut -S Target -b
./mkGardener.py -p Dec2016_Run2016C_ReReco -s fakeSel -i l1looseCut -S Target -b
./mkGardener.py -p Dec2016_Run2016D_ReReco -s fakeSel -i l1looseCut -S Target -b
./mkGardener.py -p Dec2016_Run2016E_ReReco -s fakeSel -i l1looseCut -S Target -b
./mkGardener.py -p Dec2016_Run2016F_ReReco -s fakeSel -i l1looseCut -S Target -b
./mkGardener.py -p Dec2016_Run2016G_ReReco -s fakeSel -i l1looseCut -S Target -b
./mkGardener.py -p Dec2016_Run2016H_PromptReco -s fakeSel -i l1looseCut -S Target -b
./mkGardener.py -p Feb2017_Run2016G_RemAOD_Dec2016Fix -s fakeSel -i l1looseCut -S Target -b

./mkGardener.py -p Dec2016_Run2016B_ReReco -s hadd -i l1looseCut__fakeSel -S Target -b
./mkGardener.py -p Dec2016_Run2016C_ReReco -s hadd -i l1looseCut__fakeSel -S Target -b
./mkGardener.py -p Dec2016_Run2016D_ReReco -s hadd -i l1looseCut__fakeSel -S Target -b
./mkGardener.py -p Dec2016_Run2016E_ReReco -s hadd -i l1looseCut__fakeSel -S Target -b
./mkGardener.py -p Dec2016_Run2016F_ReReco -s hadd -i l1looseCut__fakeSel -S Target -b
./mkGardener.py -p Dec2016_Run2016G_ReReco -s hadd -i l1looseCut__fakeSel -S Target -b
./mkGardener.py -p Dec2016_Run2016H_PromptReco -s hadd -i l1looseCut__fakeSel -S Target -b
./mkGardener.py -p Feb2017_Run2016G_RemAOD_Dec2016Fix -s hadd -i l1looseCut__fakeSel -S Target -b

# L1 vloose Cut

./mkGardener.py -p Dec2016_Run2016B_ReReco -s l1vlooseCut -S Target -b
./mkGardener.py -p Dec2016_Run2016C_ReReco -s l1vlooseCut -S Target -b
./mkGardener.py -p Dec2016_Run2016D_ReReco -s l1vlooseCut -S Target -b
./mkGardener.py -p Dec2016_Run2016E_ReReco -s l1vlooseCut -S Target -b
./mkGardener.py -p Dec2016_Run2016F_ReReco -s l1vlooseCut -S Target -b
./mkGardener.py -p Dec2016_Run2016G_ReReco -s l1vlooseCut -S Target -b 
./mkGardener.py -p Dec2016_Run2016H_PromptReco -s l1vlooseCut -S Target -b
./mkGardener.py -p Feb2017_Run2016G_RemAOD_Dec2016Fix -s l1vlooseCut -S Target -b

./mkGardener.py -p Dec2016_Run2016B_ReReco -s fakeSel -i l1vlooseCut -S Target -b
./mkGardener.py -p Dec2016_Run2016C_ReReco -s fakeSel -i l1vlooseCut -S Target -b
./mkGardener.py -p Dec2016_Run2016D_ReReco -s fakeSel -i l1vlooseCut -S Target -b
./mkGardener.py -p Dec2016_Run2016E_ReReco -s fakeSel -i l1vlooseCut -S Target -b
./mkGardener.py -p Dec2016_Run2016F_ReReco -s fakeSel -i l1vlooseCut -S Target -b
./mkGardener.py -p Dec2016_Run2016G_ReReco -s fakeSel -i l1vlooseCut -S Target -b
./mkGardener.py -p Dec2016_Run2016H_PromptReco -s fakeSel -i l1vlooseCut -S Target -b
./mkGardener.py -p Feb2017_Run2016G_RemAOD_Dec2016Fix -s fakeSel -i l1vlooseCut -S Target -b

./mkGardener.py -p Dec2016_Run2016B_ReReco -s hadd -i l1vlooseCut__fakeSel -S Target -b
./mkGardener.py -p Dec2016_Run2016C_ReReco -s hadd -i l1vlooseCut__fakeSel -S Target -b
./mkGardener.py -p Dec2016_Run2016D_ReReco -s hadd -i l1vlooseCut__fakeSel -S Target -b
./mkGardener.py -p Dec2016_Run2016E_ReReco -s hadd -i l1vlooseCut__fakeSel -S Target -b
./mkGardener.py -p Dec2016_Run2016F_ReReco -s hadd -i l1vlooseCut__fakeSel -S Target -b
./mkGardener.py -p Dec2016_Run2016G_ReReco -s hadd -i l1vlooseCut__fakeSel -S Target -b
./mkGardener.py -p Dec2016_Run2016H_PromptReco -s hadd -i l1vlooseCut__fakeSel -S Target -b
./mkGardener.py -p Feb2017_Run2016G_RemAOD_Dec2016Fix -s hadd -i l1vlooseCut__fakeSel -S Target -b

