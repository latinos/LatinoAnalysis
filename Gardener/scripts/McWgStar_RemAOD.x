
# -n (dry run)

###################
# KISTI 
###################

#./mkGardener.py -p Apr2017_summer16 -s MCWgStarsel -S Target  -R -b -Q cms -I /xrootd/store/group/hww/RunII/ -O /xrootd/store/group/hww/Full2016_Apr17/

#./mkGardener.py -p Apr2017_summer16 -s hadd -i Prod__MCWgStarsel -S Target -R -b -Q cms -I /xrootd/store/group/hww/Full2016_Apr17/ -O /xrootd/store/group/hww/Full2016_Apr17/

./mkGardener.py -p Apr2017_summer16 -s MCWeights,bSFLpTEffMulti,cleanTauMC,LepTrgFix,formulasMC -i Prod__MCWgStarsel__hadd -C -S Target -R -b -Q cms -I /xrootd/store/group/hww/Full2016_Apr17/ -O /xrootd/store/group/hww/Full2016_Apr17/

#./mkGardener.py -p Apr2017_summer16 -s formulasMC -i Prod__MCWgStarsel__hadd__MCWeights__bSFLpTEffMulti__cleanTauMC__LepTrgFix -C -S Target -R -b -Q cms -I /xrootd/store/group/hww/Full2016_Apr17/ -O /xrootd/store/group/hww/Full2016_Apr17/


###############
# Test
###############
#./mkGardener.py -p Apr2017_summer16 -s formulasMC -i Prod__MCWgStarsel__hadd__MCWeights__bSFLpTEffMulti__cleanTauMC__LepTrgFix -C -S Target -R -Q cms -I /xrootd/store/group/hww/Full2016_Apr17_Test/ -O /xrootd/store/group/hww/Full2016_Apr17_Test/

#./mkGardener.py -p Apr2017_summer16 -s LepTrgFix -i Prod__MCWgStarsel__hadd__MCWeights__bSFLpTEffMulti__cleanTauMC -C -S Target -R -Q cms -I /xrootd/store/group/hww/Full2016_Apr17_Test/ -O /xrootd/store/group/hww/Full2016_Apr17_Test/

#./mkGardener.py -p Apr2017_summer16 -s bSFLpTEffMulti,cleanTauMC -i Prod__MCWgStarsel__hadd__MCWeights -C -S Target -R -Q cms -I /xrootd/store/group/hww/Full2016_Apr17_Test/ -O /xrootd/store/group/hww/Full2016_Apr17_Test/

#./mkGardener.py -p Apr2017_summer16 -s MCWeights,bSFLpTEffMulti,cleanTauMC,LepTrgFix,formulasMC -i Prod__MCWgStarsel__hadd -C -S Target -R -Q cms -I /xrootd/store/group/hww/Full2016_Apr17_Test/ -O /xrootd/store/group/hww/Full2016_Apr17_Test/

#./mkGardener.py -p Apr2017_summer16 -s bSFLpTEffMulti,cleanTauMC,LepTrgFix,formulasMC -i Prod__MCWgStarsel__hadd__MCWeights -C -S Target -R -Q cms -I /xrootd/store/group/hww/Full2016_Apr17_Test/ -O /xrootd/store/group/hww/Full2016_Apr17_Test/


###################
# KNU
###################
#./mkGardener.py -p Apr2017_summer16_KNU -s MCWgStarsel -S Target -R -b -Q cms -I /pnfs/knu.ac.kr/data/cms/store/user/spak/ -O /pnfs/knu.ac.kr/data/cms/store/user/salee/
#./mkGardener.py -p Apr2017_summer16_KNU -s hadd -i MCWgStarsel -S Target -b -Q cms -I /pnfs/knu.ac.kr/data/cms/store/user/salee/ -O /pnfs/knu.ac.kr/data/cms/store/user/salee/
#./mkGardener.py -p Apr2017_summer16_KNU -s MCWeights,bSFLpTEffMulti,cleanTauMC,formulasMC -i MCWgStarsel__hadd -C -S Target -b -Q cms -I /pnfs/knu.ac.kr/data/cms/store/user/salee/ -O /pnfs/knu.ac.kr/data/cms/store/user/salee/
