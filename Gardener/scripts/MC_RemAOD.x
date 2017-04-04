
# L2 loose

./mkGardener.py -p  Feb2017_summer16 -s MCl2looseCut -S Target -b 
./mkGardener.py -p  Feb2017_summer16 -s hadd -i MCl2looseCut -S Target -b
./mkGardener.py -p  Feb2017_summer16 -s bSFL2pTEffCut,l2tight,vbsSel -C -i MCl2looseCut__hadd -S Target -b

./mkGardener.py -p  Feb2017_summer16 -s JESup -i MCl2looseCut__hadd__bSFL2pTEffCut__l2tight -S Target -b
./mkGardener.py -p  Feb2017_summer16 -s JESdo -i MCl2looseCut__hadd__bSFL2pTEffCut__l2tight -S Target -b
./mkGardener.py -p  Feb2017_summer16 -s METup -i MCl2looseCut__hadd__bSFL2pTEffCut__l2tight -S Target -b
./mkGardener.py -p  Feb2017_summer16 -s METdo -i MCl2looseCut__hadd__bSFL2pTEffCut__l2tight -S Target -b
./mkGardener.py -p  Feb2017_summer16 -s LepElepTCutup -i MCl2looseCut__hadd__bSFL2pTEffCut__l2tight -S Target -b
./mkGardener.py -p  Feb2017_summer16 -s LepElepTCutdo -i MCl2looseCut__hadd__bSFL2pTEffCut__l2tight -S Target -b
./mkGardener.py -p  Feb2017_summer16 -s LepMupTCutup -i MCl2looseCut__hadd__bSFL2pTEffCut__l2tight -S Target -b
./mkGardener.py -p  Feb2017_summer16 -s LepMupTCutdo -i MCl2looseCut__hadd__bSFL2pTEffCut__l2tight -S Target -b


./mkGardener.py -p  Feb2017_summer16 -s dymvaHiggs -i MCl2looseCut__hadd__bSFL2pTEffCut  -S Target -b
./mkGardener.py -p  Feb2017_summer16 -s dymvaHiggs -i MCl2looseCut__hadd__bSFL2pTEffCut__l2tight -S Target -b
./mkGardener.py -p  Feb2017_summer16 -s dymvaHiggs -i MCl2looseCut__hadd__bSFL2pTEffCut__l2tight__JESup -S Target -b
./mkGardener.py -p  Feb2017_summer16 -s dymvaHiggs -i MCl2looseCut__hadd__bSFL2pTEffCut__l2tight__JESdo -S Target -b
./mkGardener.py -p  Feb2017_summer16 -s dymvaHiggs -i MCl2looseCut__hadd__bSFL2pTEffCut__l2tight__METup -S Target -b
./mkGardener.py -p  Feb2017_summer16 -s dymvaHiggs -i MCl2looseCut__hadd__bSFL2pTEffCut__l2tight__METdo -S Target -b
./mkGardener.py -p  Feb2017_summer16 -s dymvaHiggs -i MCl2looseCut__hadd__bSFL2pTEffCut__l2tight__LepElepTCutup -S Target -b
./mkGardener.py -p  Feb2017_summer16 -s dymvaHiggs -i MCl2looseCut__hadd__bSFL2pTEffCut__l2tight__LepElepTCutdo -S Target -b
/mkGardener.py -p  Feb2017_summer16 -s dymvaHiggs -i MCl2looseCut__hadd__bSFL2pTEffCut__l2tight__LepMupTCutup -S Target -b
./mkGardener.py -p  Feb2017_summer16 -s dymvaHiggs -i MCl2looseCut__hadd__bSFL2pTEffCut__l2tight__LepMupTCutdo -S Target -b


# L2 vloose

./mkGardener.py -p  Feb2017_summer16 -s MCl2vlooseCut -S Target -b 
./mkGardener.py -p  Feb2017_summer16 -s hadd -i MCl2vlooseCut -S Target -b
./mkGardener.py -p  Feb2017_summer16 -s bSFL2pTEffCut,l2tight,vbsSel -C -i MCl2vlooseCut__hadd -S Target -b

./mkGardener.py -p  Feb2017_summer16 -s JESup -i MCl2vlooseCut__hadd__bSFL2pTEffCut__l2tight -S Target -b
./mkGardener.py -p  Feb2017_summer16 -s JESdo -i MCl2vlooseCut__hadd__bSFL2pTEffCut__l2tight -S Target -b
./mkGardener.py -p  Feb2017_summer16 -s METup -i MCl2vlooseCut__hadd__bSFL2pTEffCut__l2tight -S Target -b
./mkGardener.py -p  Feb2017_summer16 -s METdo -i MCl2vlooseCut__hadd__bSFL2pTEffCut__l2tight -S Target -b
./mkGardener.py -p  Feb2017_summer16 -s LepElepTCutup -i MCl2vlooseCut__hadd__bSFL2pTEffCut__l2tight -S Target -b
./mkGardener.py -p  Feb2017_summer16 -s LepElepTCutdo -i MCl2vlooseCut__hadd__bSFL2pTEffCut__l2tight -S Target -b
./mkGardener.py -p  Feb2017_summer16 -s LepMupTCutup -i MCl2vlooseCut__hadd__bSFL2pTEffCut__l2tight -S Target -b
./mkGardener.py -p  Feb2017_summer16 -s LepMupTCutdo -i MCl2vlooseCut__hadd__bSFL2pTEffCut__l2tight -S Target -b

# L1 loose

./mkGardener.py -p  Feb2017_summer16 -s MCl1looseCut -S Target -b 
./mkGardener.py -p  Feb2017_summer16 -s bSFL1pTEffCut,fakeSel -C -i MCl1looseCut -S Target -b
./mkGardener.py -p  Feb2017_summer16 -s hadd -i MCl1looseCut__bSFL1pTEffCut__fakeSel -S Target -b

# L1 vloose

./mkGardener.py -p  Feb2017_summer16 -s MCl1vlooseCut -S Target -b 
./mkGardener.py -p  Feb2017_summer16 -s bSFL1pTEffCut,fakeSel -C -i MCl1vlooseCut -S Target -b
./mkGardener.py -p  Feb2017_summer16 -s hadd -i MCl1vlooseCut__bSFL1pTEffCut__fakeSel -S Target -b


