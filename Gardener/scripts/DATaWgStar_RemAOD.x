# options: n(dryRun)
for Run in B C D E F G H; do 
  #./mkGardener.py -p Apr2017_Run2016${Run}_RemAOD_KNU -s WgStarsel -S Target -b -Q cms -I /pnfs/knu.ac.kr/data/cms/store/user/spak/ -O /pnfs/knu.ac.kr/data/cms/store/user/salee/
  #./mkGardener.py -p Apr2017_Run2016${Run}_RemAOD_KNU -s hadd -i WgStarsel  -S Target  -b -Q cms -I /pnfs/knu.ac.kr/data/cms/store/user/salee/ -O /pnfs/knu.ac.kr/data/cms/store/user/salee/
  ./mkGardener.py -p Apr2017_Run2016${Run}_RemAOD_KNU -s EpTCorr,TrigMakerData,cleanTauData,formulasDATA -i WgStarsel__hadd -C -S Target -b -Q cms -I /pnfs/knu.ac.kr/data/cms/store/user/salee/ -O /pnfs/knu.ac.kr/data/cms/store/user/salee/
done
