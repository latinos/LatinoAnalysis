
# L2 loose

./mkGardener.py -p  Feb2017_summer16 -s MCl2looseCut -S Target -b -E DYJetsToLL_M-50_HT-1200to1500
./mkGardener.py -p  Feb2017_summer16 -s hadd -i MCl2looseCut -S Target -b
#./mkGardener.py -p  Feb2017_summer16 -s bSFL2pTEffCut,l2tight,vbsSel -C -i MCl2looseCut__hadd -S Target -b

# L2 vloose

./mkGardener.py -p  Feb2017_summer16 -s MCl2vlooseCut -S Target -b -E DYJetsToLL_M-50_HT-1200to1500
./mkGardener.py -p  Feb2017_summer16 -s hadd -i MCl2vlooseCut -S Target -b
#./mkGardener.py -p  Feb2017_summer16 -s bSFL2pTEffCut,l2tight,vbsSel -C -i MCl2vlooseCut__hadd -S Target -b

# L1 loose

./mkGardener.py -p  Feb2017_summer16 -s MCl1looseCut -S Target -b -E DYJetsToLL_M-50_HT-1200to1500
./mkGardener.py -p  Feb2017_summer16 -s fakeSel -i MCl1looseCut -S Target -b
./mkGardener.py -p  Feb2017_summer16 -s hadd -i MCl1looseCut__fakeSel -S Target -b
./mkGardener.py -p  Feb2017_summer16 -s bSFL1pTEffCut -i MCl1looseCut__fakeSel__hadd -S Target -b

# L1 vloose

./mkGardener.py -p  Feb2017_summer16 -s MCl1vlooseCut -S Target -b -E DYJetsToLL_M-50_HT-1200to1500
./mkGardener.py -p  Feb2017_summer16 -s fakeSel -i MCl1vlooseCut -S Target -b
./mkGardener.py -p  Feb2017_summer16 -s hadd -i MCl1vlooseCut__fakeSel -S Target -b
./mkGardener.py -p  Feb2017_summer16 -s bSFL1pTEffCut -i MCl1vlooseCut__fakeSel__hadd -S Target -b



