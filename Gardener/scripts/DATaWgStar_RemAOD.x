# options: n(dryRun)

for Run in B C D E F G H; do 
  #./mkGardener.py -p Apr2017_Run2016${Run}_RemAOD -s WgStarsel -S Target  -R -b -Q cms -I /xrootd/store/group/hww/RunII/ -O /xrootd/store/group/hww/Full2016_Apr17/
  #./mkGardener.py -p Apr2017_Run2016${Run}_RemAOD -s hadd -i Prod__WgStarsel   -S Target -R -b -Q cms -I /xrootd/store/group/hww/Full2016_Apr17/ -O /xrootd/store/group/hww/Full2016_Apr17/
  ./mkGardener.py -p Apr2017_Run2016${Run}_RemAOD -s EpTCorr,TrigMakerData,cleanTauData,formulasDATA -i Prod__WgStarsel__hadd -C -S Target R -b -Q cms -I /xrootd/store/group/hww/Full2016_Apr17/ -O /xrootd/store/group/hww/Full2016_Apr17/
done
