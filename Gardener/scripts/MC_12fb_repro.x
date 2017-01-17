./mkGardener.py -p  07Jun2016_spring16_mAODv2_12pXfbm1_repro  -s MCl2loose -S Target -b 
./mkGardener.py -p  07Jun2016_spring16_mAODv2_12pXfbm1_repro  -s hadd -i MCl2loose -S Target -b 
./mkGardener.py -p  07Jun2016_spring16_mAODv2_12pXfbm1_repro  -s bSFL2pTEff,l2tight,wwSel -C -i MCl2loose__hadd -S Target -b

./mkGardener.py -p  07Jun2016_spring16_mAODv2_12pXfbm1_repro  -s MCl2vloose -S Target -b
./mkGardener.py -p  07Jun2016_spring16_mAODv2_12pXfbm1_repro  -s hadd -i MCl2vloose -S Target -b
./mkGardener.py -p  07Jun2016_spring16_mAODv2_12pXfbm1_repro  -s bSFL2pTEff,l2tight,wwSel -C -i MCl2vloose__hadd -S Target -b

#./mkGardener.py -p  07Jun2016_spring16_mAODv2_12pXfbm1_repro  -s UEPS -i MCl2loose__hadd__bSFL2pTEff__l2tight -S Target
#./mkGardener.py -p  07Jun2016_spring16_mAODv2_12pXfbm1_repro  -s UEPS -i MCl2loose__hadd__bSFL2pTEff__l2tight__wwSel -S Target
#./mkGardener.py -p  07Jun2016_spring16_mAODv2_12pXfbm1_repro  -s UEPS -i MCl2loose__hadd__bSFL2pTEff__l2tight__sfSel -S Target
#./mkGardener.py -p  07Jun2016_spring16_mAODv2_12pXfbm1_repro  -s UEPS -i MCl2loose__hadd__bSFL2pTEff__l2tight__topSel -S Target
#./mkGardener.py -p  07Jun2016_spring16_mAODv2_12pXfbm1_repro  -s UEPS -i MCl2loose__hadd__bSFL2pTEff__l2tight__vh3lSel -S Target
#./mkGardener.py -p  07Jun2016_spring16_mAODv2_12pXfbm1_repro  -s UEPS -i MCl2loose__hadd__bSFL2pTEff__l2tight__wh2lss1jSel -S Target
 
 
./mkGardener.py -p  07Jun2016_spring16_mAODv2_12pXfbm1_repro  -s dymvaSel -i MCl2loose__hadd__bSFL2pTEff__l2tight -S Target -b
./mkGardener.py -p  07Jun2016_spring16_mAODv2_12pXfbm1_repro  -s hadd -i MCl2loose__hadd__bSFL2pTEff__l2tight__dymvaSel -S Target -b -M
./mkGardener.py -p  07Jun2016_spring16_mAODv2_12pXfbm1_repro  -s dymvaGGH -i MCl2loose__hadd__bSFL2pTEff__l2tight -S Target -b

./mkGardener.py -p  07Jun2016_spring16_mAODv2_12pXfbm1_repro  -s JESup,wwSel -C -i MCl2loose__hadd__bSFL2pTEff__l2tight -S Target -b
./mkGardener.py -p  07Jun2016_spring16_mAODv2_12pXfbm1_repro  -s JESdo,wwSel -C -i MCl2loose__hadd__bSFL2pTEff__l2tight -S Target -b
./mkGardener.py -p  07Jun2016_spring16_mAODv2_12pXfbm1_repro  -s JESMaxup,wwSel -C -i MCl2loose__hadd__bSFL2pTEff__l2tight -S Target -b
./mkGardener.py -p  07Jun2016_spring16_mAODv2_12pXfbm1_repro  -s JESMaxdo,wwSel -C -i MCl2loose__hadd__bSFL2pTEff__l2tight -S Target -b
./mkGardener.py -p  07Jun2016_spring16_mAODv2_12pXfbm1_repro  -s METup,wwSel -C -i MCl2loose__hadd__bSFL2pTEff__l2tight -S Target -b
./mkGardener.py -p  07Jun2016_spring16_mAODv2_12pXfbm1_repro  -s METdo,wwSel -C -i MCl2loose__hadd__bSFL2pTEff__l2tight -S Target -b
./mkGardener.py -p  07Jun2016_spring16_mAODv2_12pXfbm1_repro  -s LepElepTup,wwSel -C -i MCl2loose__hadd__bSFL2pTEff__l2tight -S Target -b
./mkGardener.py -p  07Jun2016_spring16_mAODv2_12pXfbm1_repro  -s LepElepTdo,wwSel -C -i MCl2loose__hadd__bSFL2pTEff__l2tight -S Target -b
./mkGardener.py -p  07Jun2016_spring16_mAODv2_12pXfbm1_repro  -s LepMupTup,wwSel -C -i MCl2loose__hadd__bSFL2pTEff__l2tight -S Target -b
./mkGardener.py -p  07Jun2016_spring16_mAODv2_12pXfbm1_repro  -s LepMupTdo,wwSel -C -i MCl2loose__hadd__bSFL2pTEff__l2tight -S Target -b

./mkGardener.py -p  07Jun2016_spring16_mAODv2_12pXfbm1_repro  -s vh3lSel -i MCl2loose__hadd__bSFL2pTEff__l2tight -S Target -b
./mkGardener.py -p  07Jun2016_spring16_mAODv2_12pXfbm1_repro  -s vh3lSel -i MCl2loose__hadd__bSFL2pTEff__l2tight__JESMaxup -S Target -b
./mkGardener.py -p  07Jun2016_spring16_mAODv2_12pXfbm1_repro  -s vh3lSel -i MCl2loose__hadd__bSFL2pTEff__l2tight__JESMaxdo -S Target -b
./mkGardener.py -p  07Jun2016_spring16_mAODv2_12pXfbm1_repro  -s vh3lSel -i MCl2loose__hadd__bSFL2pTEff__l2tight__METup -S Target -b
./mkGardener.py -p  07Jun2016_spring16_mAODv2_12pXfbm1_repro  -s vh3lSel -i MCl2loose__hadd__bSFL2pTEff__l2tight__METdo -S Target -b
./mkGardener.py -p  07Jun2016_spring16_mAODv2_12pXfbm1_repro  -s vh3lSel -i MCl2loose__hadd__bSFL2pTEff__l2tight__LepElepTup -S Target -b
./mkGardener.py -p  07Jun2016_spring16_mAODv2_12pXfbm1_repro  -s vh3lSel -i MCl2loose__hadd__bSFL2pTEff__l2tight__LepElepTdo -S Target -b
./mkGardener.py -p  07Jun2016_spring16_mAODv2_12pXfbm1_repro  -s vh3lSel -i MCl2loose__hadd__bSFL2pTEff__l2tight__LepMupTup -S Target -b
./mkGardener.py -p  07Jun2016_spring16_mAODv2_12pXfbm1_repro  -s vh3lSel -i MCl2loose__hadd__bSFL2pTEff__l2tight__LepMupTdo -S Target -b
 
./mkGardener.py -p  07Jun2016_spring16_mAODv2_12pXfbm1_repro  -s topSel -i MCl2loose__hadd__bSFL2pTEff__l2tight -S Target -b
./mkGardener.py -p  07Jun2016_spring16_mAODv2_12pXfbm1_repro  -s topSel -i MCl2loose__hadd__bSFL2pTEff__l2tight__JESMaxup -S Target -b
./mkGardener.py -p  07Jun2016_spring16_mAODv2_12pXfbm1_repro  -s topSel -i MCl2loose__hadd__bSFL2pTEff__l2tight__JESMaxdo -S Target -b
./mkGardener.py -p  07Jun2016_spring16_mAODv2_12pXfbm1_repro  -s topSel -i MCl2loose__hadd__bSFL2pTEff__l2tight__METup -S Target -b
./mkGardener.py -p  07Jun2016_spring16_mAODv2_12pXfbm1_repro  -s topSel -i MCl2loose__hadd__bSFL2pTEff__l2tight__METdo -S Target -b
./mkGardener.py -p  07Jun2016_spring16_mAODv2_12pXfbm1_repro  -s topSel -i MCl2loose__hadd__bSFL2pTEff__l2tight__LepElepTup -S Target -b
./mkGardener.py -p  07Jun2016_spring16_mAODv2_12pXfbm1_repro  -s topSel -i MCl2loose__hadd__bSFL2pTEff__l2tight__LepElepTdo -S Target -b
./mkGardener.py -p  07Jun2016_spring16_mAODv2_12pXfbm1_repro  -s topSel -i MCl2loose__hadd__bSFL2pTEff__l2tight__LepMupTup -S Target -b
./mkGardener.py -p  07Jun2016_spring16_mAODv2_12pXfbm1_repro  -s topSel -i MCl2loose__hadd__bSFL2pTEff__l2tight__LepMupTdo -S Target -b

./mkGardener.py -p  07Jun2016_spring16_mAODv2_12pXfbm1_repro  -s sfSel -i MCl2loose__hadd__bSFL2pTEff__l2tight -S Target -b
./mkGardener.py -p  07Jun2016_spring16_mAODv2_12pXfbm1_repro  -s sfSel -i MCl2loose__hadd__bSFL2pTEff__l2tight__JESMaxup -S Target -b
./mkGardener.py -p  07Jun2016_spring16_mAODv2_12pXfbm1_repro  -s sfSel -i MCl2loose__hadd__bSFL2pTEff__l2tight__JESMaxdo -S Target -b
./mkGardener.py -p  07Jun2016_spring16_mAODv2_12pXfbm1_repro  -s sfSel -i MCl2loose__hadd__bSFL2pTEff__l2tight__METup -S Target -b
./mkGardener.py -p  07Jun2016_spring16_mAODv2_12pXfbm1_repro  -s sfSel -i MCl2loose__hadd__bSFL2pTEff__l2tight__METdo -S Target -b
./mkGardener.py -p  07Jun2016_spring16_mAODv2_12pXfbm1_repro  -s sfSel -i MCl2loose__hadd__bSFL2pTEff__l2tight__LepElepTup -S Target -b
./mkGardener.py -p  07Jun2016_spring16_mAODv2_12pXfbm1_repro  -s sfSel -i MCl2loose__hadd__bSFL2pTEff__l2tight__LepElepTdo -S Target -b
./mkGardener.py -p  07Jun2016_spring16_mAODv2_12pXfbm1_repro  -s sfSel -i MCl2loose__hadd__bSFL2pTEff__l2tight__LepMupTup -S Target -b
./mkGardener.py -p  07Jun2016_spring16_mAODv2_12pXfbm1_repro  -s sfSel -i MCl2loose__hadd__bSFL2pTEff__l2tight__LepMupTdo -S Target -b

./mkGardener.py -p  07Jun2016_spring16_mAODv2_12pXfbm1_repro  -s wh2lss1jSel -i MCl2loose__hadd__bSFL2pTEff__l2tight -S Target -b
./mkGardener.py -p  07Jun2016_spring16_mAODv2_12pXfbm1_repro  -s wh2lss1jSel -i MCl2loose__hadd__bSFL2pTEff__l2tight__JESMaxup -S Target -b
./mkGardener.py -p  07Jun2016_spring16_mAODv2_12pXfbm1_repro  -s wh2lss1jSel -i MCl2loose__hadd__bSFL2pTEff__l2tight__JESMaxdo -S Target -b
./mkGardener.py -p  07Jun2016_spring16_mAODv2_12pXfbm1_repro  -s wh2lss1jSel -i MCl2loose__hadd__bSFL2pTEff__l2tight__METup -S Target -b
./mkGardener.py -p  07Jun2016_spring16_mAODv2_12pXfbm1_repro  -s wh2lss1jSel -i MCl2loose__hadd__bSFL2pTEff__l2tight__METdo -S Target -b
./mkGardener.py -p  07Jun2016_spring16_mAODv2_12pXfbm1_repro  -s wh2lss1jSel -i MCl2loose__hadd__bSFL2pTEff__l2tight__LepElepTup -S Target -b
./mkGardener.py -p  07Jun2016_spring16_mAODv2_12pXfbm1_repro  -s wh2lss1jSel -i MCl2loose__hadd__bSFL2pTEff__l2tight__LepElepTdo -S Target -b
./mkGardener.py -p  07Jun2016_spring16_mAODv2_12pXfbm1_repro  -s wh2lss1jSel -i MCl2loose__hadd__bSFL2pTEff__l2tight__LepMupTup -S Target -b
./mkGardener.py -p  07Jun2016_spring16_mAODv2_12pXfbm1_repro  -s wh2lss1jSel -i MCl2loose__hadd__bSFL2pTEff__l2tight__LepMupTdo -S Target -b

./mkGardener.py -p  07Jun2016_spring16_mAODv2_12pXfbm1_repro  -s wh2lss1jDYSel,chFlipProba -C -i MCl2loose__hadd__bSFL2pTEff__l2tight -S Target -b
./mkGardener.py -p  07Jun2016_spring16_mAODv2_12pXfbm1_repro  -s wh2lss1jDYSel,chFlipProba -C -i MCl2loose__hadd__bSFL2pTEff__l2tight__JESMaxup -S Target -b
./mkGardener.py -p  07Jun2016_spring16_mAODv2_12pXfbm1_repro  -s wh2lss1jDYSel,chFlipProba -C -i MCl2loose__hadd__bSFL2pTEff__l2tight__JESMaxdo -S Target -b
./mkGardener.py -p  07Jun2016_spring16_mAODv2_12pXfbm1_repro  -s wh2lss1jDYSel,chFlipProba -C -i MCl2loose__hadd__bSFL2pTEff__l2tight__METup -S Target -b
./mkGardener.py -p  07Jun2016_spring16_mAODv2_12pXfbm1_repro  -s wh2lss1jDYSel,chFlipProba -C -i MCl2loose__hadd__bSFL2pTEff__l2tight__METdo -S Target -b
./mkGardener.py -p  07Jun2016_spring16_mAODv2_12pXfbm1_repro  -s wh2lss1jDYSel,chFlipProba -C -i MCl2loose__hadd__bSFL2pTEff__l2tight__LepElepTup -S Target -b
./mkGardener.py -p  07Jun2016_spring16_mAODv2_12pXfbm1_repro  -s wh2lss1jDYSel,chFlipProba -C -i MCl2loose__hadd__bSFL2pTEff__l2tight__LepElepTdo -S Target -b
./mkGardener.py -p  07Jun2016_spring16_mAODv2_12pXfbm1_repro  -s wh2lss1jDYSel,chFlipProba -C -i MCl2loose__hadd__bSFL2pTEff__l2tight__LepMupTup -S Target -b
./mkGardener.py -p  07Jun2016_spring16_mAODv2_12pXfbm1_repro  -s wh2lss1jDYSel,chFlipProba -C -i MCl2loose__hadd__bSFL2pTEff__l2tight__LepMupTdo -S Target -b

./mkGardener.py -p  07Jun2016_spring16_mAODv2_12pXfbm1_repro  -s vbsSel -i MCl2loose__hadd__bSFL2pTEff__l2tight -S Target -b
./mkGardener.py -p  07Jun2016_spring16_mAODv2_12pXfbm1_repro  -s vbsSel -i MCl2loose__hadd__bSFL2pTEff__l2tight__JESMaxup -S Target -b
./mkGardener.py -p  07Jun2016_spring16_mAODv2_12pXfbm1_repro  -s vbsSel -i MCl2loose__hadd__bSFL2pTEff__l2tight__JESMaxdo -S Target -b
./mkGardener.py -p  07Jun2016_spring16_mAODv2_12pXfbm1_repro  -s vbsSel -i MCl2loose__hadd__bSFL2pTEff__l2tight__METup -S Target -b
./mkGardener.py -p  07Jun2016_spring16_mAODv2_12pXfbm1_repro  -s vbsSel -i MCl2loose__hadd__bSFL2pTEff__l2tight__METdo -S Target -b
./mkGardener.py -p  07Jun2016_spring16_mAODv2_12pXfbm1_repro  -s vbsSel -i MCl2loose__hadd__bSFL2pTEff__l2tight__LepElepTup -S Target -b
./mkGardener.py -p  07Jun2016_spring16_mAODv2_12pXfbm1_repro  -s vbsSel -i MCl2loose__hadd__bSFL2pTEff__l2tight__LepElepTdo -S Target -b
./mkGardener.py -p  07Jun2016_spring16_mAODv2_12pXfbm1_repro  -s vbsSel -i MCl2loose__hadd__bSFL2pTEff__l2tight__LepMupTup -S Target -b
./mkGardener.py -p  07Jun2016_spring16_mAODv2_12pXfbm1_repro  -s vbsSel -i MCl2loose__hadd__bSFL2pTEff__l2tight__LepMupTdo -S Target -b

 
./mkGardener.py -p  07Jun2016_spring16_mAODv2_12pXfbm1_repro  -s MCl1loose -S Target -b
./mkGardener.py -p  07Jun2016_spring16_mAODv2_12pXfbm1_repro  -s EpTCorr -i MCl1loose -S Target -b
./mkGardener.py -p  07Jun2016_spring16_mAODv2_12pXfbm1_repro  -s hadd -i MCl1loose__EpTCorr -S Target -b
./mkGardener.py -p  07Jun2016_spring16_mAODv2_12pXfbm1_repro  -s fakeSel -i MCl1loose__EpTCorr -S Target -b
./mkGardener.py -p  07Jun2016_spring16_mAODv2_12pXfbm1_repro  -s hadd -i MCl1loose__EpTCorr__fakeSel -S Target -b

./mkGardener.py -p  07Jun2016_spring16_mAODv2_12pXfbm1_repro  -s MCl1vloose -S Target -b
./mkGardener.py -p  07Jun2016_spring16_mAODv2_12pXfbm1_repro  -s EpTCorr -i MCl1vloose -S Target -b
./mkGardener.py -p  07Jun2016_spring16_mAODv2_12pXfbm1_repro  -s hadd -i MCl1vloose__EpTCorr -S Target -b
./mkGardener.py -p  07Jun2016_spring16_mAODv2_12pXfbm1_repro  -s fakeSel -i MCl1vloose__EpTCorr -S Target -b
./mkGardener.py -p  07Jun2016_spring16_mAODv2_12pXfbm1_repro  -s hadd -i MCl1vloose__EpTCorr__fakeSel -S Target -b

./mkGardener.py -p  07Jun2016_spring16_mAODv2_12pXfbm1_repro  -s MCWgStarsel -S Target -b
./mkGardener.py -p  07Jun2016_spring16_mAODv2_12pXfbm1_repro  -s hadd -i MCWgStarsel -S Target -b
./mkGardener.py -p  07Jun2016_spring16_mAODv2_12pXfbm1_repro  -s EpTCorr -i MCWgStarsel__hadd -S Target -b

