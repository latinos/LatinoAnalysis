
## L2 loose
#
./mkGardener.py -p  Apr2017_summer16 -s lep2SelVBS,MCWeights -C -S Target -b  -W 24:00:00
./mkGardener.py -p  Apr2017_summer16 -s MCWeights -i lep2SelVBS -S Target -b -W 8:00:00
./mkGardener.py -p  Apr2017_summer16 -s hadd -i lep2SelVBS__MCWeights -S Target -b -W 8:00:00
./mkGardener.py -p  Apr2017_summer16 -s bSFL2pTEffCut,l2tightVBS -C -i lep2SelVBS__MCWeights__hadd -S Target -b -W 8:00:00
./mkGardener.py -p  Apr2017_summer16 -s l2tightVBS -i lep2SelVBS__MCWeights__hadd__bSFL2pTEffCut -S Target -b -W 8:00:00


for iSkim in vh3lSelVBS vbsSel tightVbsSel ; do
  echo ${iSkim}
  ./mkGardener.py -p  Apr2017_summer16 -s ${iSkim} -i lep2SelVBS__MCWeights__hadd__bSFL2pTEffCut__l2tightVBS -S Target -b -W 1:00:00
done

 for iSkim in vh3lFakeSel vbsSel tightVbsSel; do
   ./mkGardener.py -p Apr2017_summer16 -s ${iSkim} -i lep2SelVBS__MCWeights__hadd__bSFL2pTEffCut -S Target -b -W 1:00:00
 done


for iSyst in JESup JESdo METup METdo LepElepTCutup LepElepTCutdo LepMupTCutup LepMupTCutdo ;  do
  ./mkGardener.py -p  Apr2017_summer16 -s ${iSyst} -i lep2SelVBS__MCWeights__hadd__bSFL2pTEffCut__l2tightVBS -S Target -b -W 8:00:00
  ./mkGardener.py -p  Apr2017_summer16 -s tightVbsSel -i lep2SelVBS__MCWeights__hadd__bSFL2pTEffCut__l2tightVBS__${iSyst} -S Target -b -W 1:00:00
  ./mkGardener.py -p  Apr2017_summer16 -s vh3lSelVBS -i lep2SelVBS__MCWeights__hadd__bSFL2pTEffCut__l2tightVBS__${iSyst} -S Target -b -W 1:00:00
done

