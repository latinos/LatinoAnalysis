./mkGardener.py -p  07Jun2016_spring16_mAODv2_4p0fbm1  -s MCl2loose -S Target -b
./mkGardener.py -p  07Jun2016_spring16_mAODv2_4p0fbm1  -s hadd -i MCl2loose -S Target -b
./mkGardener.py -p  07Jun2016_spring16_mAODv2_4p0fbm1  -s bSFL2pTEff,l2tight,wwSel -C -i MCl2loose__hadd -S Target -b

#./mkGardener.py -p  07Jun2016_spring16_mAODv2_4p0fbm1  -s UEPS -i MCl2loose__hadd__bSFL2pTEff__l2tight -S Target
#./mkGardener.py -p  07Jun2016_spring16_mAODv2_4p0fbm1  -s UEPS -i MCl2loose__hadd__bSFL2pTEff__l2tight__wwSel -S Target

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
