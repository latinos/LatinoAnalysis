
# -n (dry run)

###################
# KISTI 
###################

#./mkGardener.py -p Apr2017_summer16 -s MCWgStarsel -S Target  -R -b -Q cms -I /xrootd/store/group/hww/RunII/ -O /xrootd/store/group/hww/Full2016_Apr17/

./mkGardener.py -p Apr2017_summer16 -s hadd -i Prod__MCWgStarsel -S Target -R -b -Q cms -I /xrootd/store/group/hww/Full2016_Apr17/ -O /xrootd/store/group/hww/Full2016_Apr17/

#./mkGardener.py -p Apr2017_summer16 -s MCWeights,bSFLpTEffMulti,cleanTauMC,formulasMC -i MCWgStarsel__hadd -C -S Target -b -Q cms -I /pnfs/knu.ac.kr/data/cms/store/user/salee/ -O /pnfs/knu.ac.kr/data/cms/store/user/salee/


###################
# KNU
###################
#./mkGardener.py -p Apr2017_summer16_KNU -s MCWgStarsel -S Target -R -b -Q cms -I /pnfs/knu.ac.kr/data/cms/store/user/spak/ -O /pnfs/knu.ac.kr/data/cms/store/user/salee/
#./mkGardener.py -p Apr2017_summer16_KNU -s hadd -i MCWgStarsel -S Target -b -Q cms -I /pnfs/knu.ac.kr/data/cms/store/user/salee/ -O /pnfs/knu.ac.kr/data/cms/store/user/salee/
#./mkGardener.py -p Apr2017_summer16_KNU -s MCWeights,bSFLpTEffMulti,cleanTauMC,formulasMC -i MCWgStarsel__hadd -C -S Target -b -Q cms -I /pnfs/knu.ac.kr/data/cms/store/user/salee/ -O /pnfs/knu.ac.kr/data/cms/store/user/salee/
