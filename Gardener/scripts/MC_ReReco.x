
# L2 loose

./mkGardener.py -p  Dec2016_summer16_mAODv2 -s MCl2looseCut -S Target -b -E DYJetsToLL_M-50_HT-1200to1500,TTJets_more
./mkGardener.py -p  Dec2016_summer16_mAODv2 -s hadd -i MCl2looseCut -S Target -b
./mkGardener.py -p  Dec2016_summer16_mAODv2 -s bSFLepEffCut,l2tight,vbsSel -C -i MCl2looseCut__hadd -S Target -b
#./mkGardener.py -p  Dec2016_summer16_mAODv2 -s LepSFCut,l2tight -C -i MCl2looseCut__hadd -S Target -b -T TTTo2L2Nu,WWTo2L2Nu

# L2 vloose

./mkGardener.py -p  Dec2016_summer16_mAODv2 -s MCl2vlooseCut -S Target -b -E DYJetsToLL_M-50_HT-1200to1500,TTJets_more
./mkGardener.py -p  Dec2016_summer16_mAODv2 -s hadd -i MCl2vlooseCut -S Target -b
./mkGardener.py -p  Dec2016_summer16_mAODv2 -s bSFLepEffCut,l2tight,vbsSel -C -i MCl2vlooseCut__hadd -S Target -b

# L1 loose

./mkGardener.py -p  Dec2016_summer16_mAODv2 -s MCl1looseCut -S Target -b -E DYJetsToLL_M-50_HT-1200to1500,TTJets_more
./mkGardener.py -p  Dec2016_summer16_mAODv2 -s fakeSel -i MCl1looseCut -S Target -b
./mkGardener.py -p  Dec2016_summer16_mAODv2 -s hadd -i MCl1looseCut__fakeSel -S Target -b

# L1 vloose

./mkGardener.py -p  Dec2016_summer16_mAODv2 -s MCl1vlooseCut -S Target -b -E DYJetsToLL_M-50_HT-1200to1500,TTJets_more
./mkGardener.py -p  Dec2016_summer16_mAODv2 -s fakeSel -i MCl1vlooseCut -S Target -b
./mkGardener.py -p  Dec2016_summer16_mAODv2 -s hadd -i MCl1vlooseCut__fakeSel -S Target -b



