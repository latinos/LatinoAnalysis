./mkGardener.py -p  07Jun2016_spring16_mAODv2_6p3fbm1  -s puadder -i MCl2loose -S Target -b
./mkGardener.py -p  07Jun2016_spring16_mAODv2_6p3fbm1  -s puadder -i MCl1loose -S Target -b
./mkGardener.py -p  07Jun2016_spring16_mAODv2_6p3fbm1  -s puadder -i MCl1loose__EpTCorr -S Target -b
./mkGardener.py -p  07Jun2016_spring16_mAODv2_6p3fbm1  -s puadder -i MCl1loose__EpTCorr__hadd -S Target -b
./mkGardener.py -p  07Jun2016_spring16_mAODv2_6p3fbm1  -s puadder -i MCWgStarsel -S Target -b
./mkGardener.py -p  07Jun2016_spring16_mAODv2_6p3fbm1  -s puadder -i MCWgStarsel__hadd -S Target -b
./mkGardener.py -p  07Jun2016_spring16_mAODv2_6p3fbm1  -s puadder -i MCWgStarsel__hadd__EpTCorr -S Target -b

#./mkGardener.py -p  07Jun2016_spring16_mAODv2_4p0fbm1  -s baseW -i MCl2loose -S Target -b -E DYJetsToLL_M-50
#./mkGardener.py -p  07Jun2016_spring16_mAODv2_4p0fbm1  -s baseW -i MCl2loose__hadd -S Target -b

#./mkGardener.py -p  07Jun2016_spring16_mAODv2_4p0fbm1  -s baseW -i MCl1loose -S Target -b
#./mkGardener.py -p  07Jun2016_spring16_mAODv2_4p0fbm1  -s baseW -i MCl1loose__EpTCorr -S Target -b 
#./mkGardener.py -p  07Jun2016_spring16_mAODv2_4p0fbm1  -s baseW -i MCl1loose__EpTCorr__hadd -S Target -b 


#./mkGardener.py -p  07Jun2016_spring16_mAODv2_4p0fbm1  -s baseW -i MCWgStarsel -S Target -b
#./mkGardener.py -p  07Jun2016_spring16_mAODv2_4p0fbm1  -s baseW -i MCWgStarsel__hadd -S Target -b
#./mkGardener.py -p  07Jun2016_spring16_mAODv2_4p0fbm1  -s baseW -i MCWgStarsel__hadd__EpTCorr   -S Target -b

./mkGardener.py -p  07Jun2016_spring16_mAODv2_4p0fbm1  -s MCl2loose -S Target -b
./mkGardener.py -p  07Jun2016_spring16_mAODv2_4p0fbm1  -s hadd -i MCl2loose -S Target -b
./mkGardener.py -p  07Jun2016_spring16_mAODv2_4p0fbm1  -s bSFL2pTEff,l2tight,wwSel -C -i MCl2loose__hadd -S Target -b

#./mkGardener.py -p  07Jun2016_spring16_mAODv2_4p0fbm1  -s UEPS -i MCl2loose__hadd__bSFL2pTEff__l2tight -S Target
#./mkGardener.py -p  07Jun2016_spring16_mAODv2_4p0fbm1  -s UEPS -i MCl2loose__hadd__bSFL2pTEff__l2tight__wwSel -S Target

./mkGardener.py -p  07Jun2016_spring16_mAODv2_4p0fbm1  -s TrigEff -i MCl2loose__hadd__bSFL2pTEff__l2tight__wwSel -S Target -b
./mkGardener.py -p  07Jun2016_spring16_mAODv2_4p0fbm1  -s TrigEff -i MCl2loose__hadd__bSFL2pTEff__l2tight__vh3lSel -S Target -b

./mkGardener.py -p  07Jun2016_spring16_mAODv2_4p0fbm1  -s JESMaxup,wwSel -C -i MCl2loose__hadd__bSFL2pTEff__l2tight -S Target -b
./mkGardener.py -p  07Jun2016_spring16_mAODv2_4p0fbm1  -s JESMaxdo,wwSel -C -i MCl2loose__hadd__bSFL2pTEff__l2tight -S Target -b
./mkGardener.py -p  07Jun2016_spring16_mAODv2_4p0fbm1  -s METup,wwSel -C -i MCl2loose__hadd__bSFL2pTEff__l2tight -S Target -b
./mkGardener.py -p  07Jun2016_spring16_mAODv2_4p0fbm1  -s METdo,wwSel -C -i MCl2loose__hadd__bSFL2pTEff__l2tight -S Target -b
./mkGardener.py -p  07Jun2016_spring16_mAODv2_4p0fbm1  -s LepElepTup,wwSel -C -i MCl2loose__hadd__bSFL2pTEff__l2tight -S Target -b
./mkGardener.py -p  07Jun2016_spring16_mAODv2_4p0fbm1  -s LepElepTdo,wwSel -C -i MCl2loose__hadd__bSFL2pTEff__l2tight -S Target -b
./mkGardener.py -p  07Jun2016_spring16_mAODv2_4p0fbm1  -s LepMupTup,wwSel -C -i MCl2loose__hadd__bSFL2pTEff__l2tight -S Target -b
./mkGardener.py -p  07Jun2016_spring16_mAODv2_4p0fbm1  -s LepMupTdo,wwSel -C -i MCl2loose__hadd__bSFL2pTEff__l2tight -S Target -b

./mkGardener.py -p  07Jun2016_spring16_mAODv2_4p0fbm1  -s vh3lSel -i MCl2loose__hadd__bSFL2pTEff__l2tight -S Target -b
./mkGardener.py -p  07Jun2016_spring16_mAODv2_4p0fbm1  -s vh3lSel -i MCl2loose__hadd__bSFL2pTEff__l2tight__JESMaxup -S Target -b
./mkGardener.py -p  07Jun2016_spring16_mAODv2_4p0fbm1  -s vh3lSel -i MCl2loose__hadd__bSFL2pTEff__l2tight__JESMaxdo -S Target -b
./mkGardener.py -p  07Jun2016_spring16_mAODv2_4p0fbm1  -s vh3lSel -i MCl2loose__hadd__bSFL2pTEff__l2tight__METup -S Target -b
./mkGardener.py -p  07Jun2016_spring16_mAODv2_4p0fbm1  -s vh3lSel -i MCl2loose__hadd__bSFL2pTEff__l2tight__METdo -S Target -b
./mkGardener.py -p  07Jun2016_spring16_mAODv2_4p0fbm1  -s vh3lSel -i MCl2loose__hadd__bSFL2pTEff__l2tight__LepElepTup -S Target -b
./mkGardener.py -p  07Jun2016_spring16_mAODv2_4p0fbm1  -s vh3lSel -i MCl2loose__hadd__bSFL2pTEff__l2tight__LepElepTdo -S Target -b
./mkGardener.py -p  07Jun2016_spring16_mAODv2_4p0fbm1  -s vh3lSel -i MCl2loose__hadd__bSFL2pTEff__l2tight__LepMupTup -S Target -b
./mkGardener.py -p  07Jun2016_spring16_mAODv2_4p0fbm1  -s vh3lSel -i MCl2loose__hadd__bSFL2pTEff__l2tight__LepMupTdo -S Target -b



./mkGardener.py -p  07Jun2016_spring16_mAODv2_4p0fbm1  -s MCl1loose -S Target -b
./mkGardener.py -p  07Jun2016_spring16_mAODv2_4p0fbm1  -s EpTCorr -i MCl1loose -S Target -b
./mkGardener.py -p  07Jun2016_spring16_mAODv2_4p0fbm1  -s hadd -i MCl1loose__EpTCorr -S Target -b

./mkGardener.py -p  07Jun2016_spring16_mAODv2_4p0fbm1  -s MCWgStarsel -S Target -b
./mkGardener.py -p  07Jun2016_spring16_mAODv2_4p0fbm1  -s hadd -i MCWgStarsel -S Target -b
./mkGardener.py -p  07Jun2016_spring16_mAODv2_4p0fbm1  -s EpTCorr -i MCWgStarsel__hadd -S Target -b


# TEST TTZ
#./mkGardener.py -p  03Mar_25ns_mAODv2_MC -s MCl2loose -S Target -b -T TTZToLLNuNu_M-10
#./mkGardener.py -p  03Mar_25ns_mAODv2_MC -s hadd -i MCl2loose -S Target -b -T TTZToLLNuNu_M-10
#./mkGardener.py -p  03Mar_25ns_mAODv2_MC -s bSFL2pTEff,l2tight -C -i MCl2loose__hadd -S Target -b -T TTZToLLNuNu_M-10


# 
./mkGardener.py -p 22Jan_25ns_mAODv2_MC -s BWEwkSinglet -i MCl2loose__hadd__bSFL2pTEff__l2tight__wwSel -S Target -b
./mkGardener.py -p 22Jan_25ns_mAODv2_MC -s BWEwkSinglet -i MCl2loose__hadd__bSFL2pTEff__l2tight__JESMaxup__wwSel -S Target -b
./mkGardener.py -p 22Jan_25ns_mAODv2_MC -s BWEwkSinglet -i MCl2loose__hadd__bSFL2pTEff__l2tight__JESMaxdo__wwSel -S Target -b
./mkGardener.py -p 22Jan_25ns_mAODv2_MC -s BWEwkSinglet -i MCl2loose__hadd__bSFL2pTEff__l2tight__METup__wwSel -S Target -b
./mkGardener.py -p 22Jan_25ns_mAODv2_MC -s BWEwkSinglet -i MCl2loose__hadd__bSFL2pTEff__l2tight__METdo__wwSel -S Target -b
./mkGardener.py -p 22Jan_25ns_mAODv2_MC -s BWEwkSinglet -i MCl2loose__hadd__bSFL2pTEff__l2tight__LepElepTup__wwSel -S Target -b
./mkGardener.py -p 22Jan_25ns_mAODv2_MC -s BWEwkSinglet -i MCl2loose__hadd__bSFL2pTEff__l2tight__LepElepTdo__wwSel -S Target -b
./mkGardener.py -p 22Jan_25ns_mAODv2_MC -s BWEwkSinglet -i MCl2loose__hadd__bSFL2pTEff__l2tight__LepMupTup__wwSel -S Target -b
./mkGardener.py -p 22Jan_25ns_mAODv2_MC -s BWEwkSinglet -i MCl2loose__hadd__bSFL2pTEff__l2tight__LepMupTdo__wwSel -S Target -b

