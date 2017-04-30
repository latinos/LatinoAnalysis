
## L2 loose
#
#./mkGardener.py -p  Feb2017_summer16 -s MCl2looseCut -S Target -b 
#./mkGardener.py -p  Feb2017_summer16 -s hadd -i MCl2looseCut -S Target -b
#./mkGardener.py -p  Feb2017_summer16 -s bSFL2pTEffCut,l2tight -C -i MCl2looseCut__hadd -S Target -b
#
#for iSkim in wwSel topSel vh3lSel sfSel vbsSel ; do
#  echo ${iSkim}
#  ./mkGardener.py -p  Feb2017_summer16 -s ${iSkim} -i MCl2looseCut__hadd__bSFL2pTEffCut__l2tight -S Target -b
#done
#
#for iSyst in JESup JESdo METup METdo LepElepTCutup LepElepTCutdo LepMupTCutup LepMupTCutdo ;  do
#  ./mkGardener.py -p  Feb2017_summer16 -s ${iSyst} -i MCl2looseCut__hadd__bSFL2pTEffCut__l2tight -S Target -b
#  for iSkim in wwSel topSel vh3lSel sfSel vbsSel ; do
#    ./mkGardener.py -p  Feb2017_summer16 -s ${iSkim} -i MCl2looseCut__hadd__bSFL2pTEffCut__l2tight__${iSyst} -S Target -b
#  done
#done

## L2 vloose
#
#./mkGardener.py -p  Feb2017_summer16 -s MCl2vlooseCut -S Target -b 
#./mkGardener.py -p  Feb2017_summer16 -s hadd -i MCl2vlooseCut -S Target -b
#./mkGardener.py -p  Feb2017_summer16 -s bSFL2pTEffCut,l2tight,vbsSel -C -i MCl2vlooseCut__hadd -S Target -b
#
#for iSyst in JESup JESdo METup METdo LepElepTCutup LepElepTCutdo LepMupTCutup LepMupTCutdo ;  do
#  ./mkGardener.py -p  Feb2017_summer16 -s ${iSyst} -i MCl2vlooseCut__hadd__bSFL2pTEffCut__l2tight -S Target -b
#done
#
## L1 loose
#
#./mkGardener.py -p  Feb2017_summer16 -s MCl1looseCut -S Target -b 
#./mkGardener.py -p  Feb2017_summer16 -s bSFL1pTEffCut,fakeSel -C -i MCl1looseCut -S Target -b
 ./mkGardener.py -p  Feb2017_summer16 -s hadd -i MCl1looseCut__bSFL1pTEffCut -S Target -b
#./mkGardener.py -p  Feb2017_summer16 -s hadd -i MCl1looseCut__bSFL1pTEffCut__fakeSel -S Target -b
#
## L1 vloose
#
#./mkGardener.py -p  Feb2017_summer16 -s MCl1vlooseCut -S Target -b 
#./mkGardener.py -p  Feb2017_summer16 -s bSFL1pTEffCut,fakeSel -C -i MCl1vlooseCut -S Target -b
#./mkGardener.py -p  Feb2017_summer16 -s hadd -i MCl1vlooseCut__bSFL1pTEffCut__fakeSel -S Target -b
#
#
