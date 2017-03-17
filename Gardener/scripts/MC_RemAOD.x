
# L2 loose

./mkGardener.py -p  Feb2017_summer16 -s MCl2looseCut -S Target -b 
./mkGardener.py -p  Feb2017_summer16 -s hadd -i MCl2looseCut -S Target -b
./mkGardener.py -p  Feb2017_summer16 -s bSFL2pTEffCut,l2tight,vbsSel -C -i MCl2looseCut__hadd -S Target -b

# L2 vloose

./mkGardener.py -p  Feb2017_summer16 -s MCl2vlooseCut -S Target -b 
./mkGardener.py -p  Feb2017_summer16 -s hadd -i MCl2vlooseCut -S Target -b
./mkGardener.py -p  Feb2017_summer16 -s bSFL2pTEffCut,l2tight,vbsSel -C -i MCl2vlooseCut__hadd -S Target -b

# L1 loose

./mkGardener.py -p  Feb2017_summer16 -s MCl1looseCut -S Target -b 
./mkGardener.py -p  Feb2017_summer16 -s bSFL1pTEffCut,fakeSel -C -i MCl1looseCut -S Target -b
./mkGardener.py -p  Feb2017_summer16 -s hadd -i MCl1looseCut__bSFL1pTEffCut__fakeSel -S Target -b

# L1 vloose

./mkGardener.py -p  Feb2017_summer16 -s MCl1vlooseCut -S Target -b 
./mkGardener.py -p  Feb2017_summer16 -s bSFL1pTEffCut,fakeSel -C -i MCl1vlooseCut -S Target -b
./mkGardener.py -p  Feb2017_summer16 -s hadd -i MCl1vlooseCut__bSFL1pTEffCut__fakeSel -S Target -b


