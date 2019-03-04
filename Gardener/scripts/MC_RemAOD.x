
#XJ # Doing first common Lepton Selection with nLep > =1 +  pTCorr and trigger bits
#XJ ./mkGardener.py -p Apr2017_summer16 -s lepSel -S Target -b
#XJ ./mkGardener.py -p Apr2017_summer16 -s MCWeights -i lepSel -S Target -b
#XJ ./mkGardener.py -p Apr2017_summer16 -s bSFLpTEffMulti -i lepSel__MCWeights -S Target -b
#XJ ./mkGardener.py -p Apr2017_summer16 -s cleanTauMC -i lepSel__MCWeights__bSFLpTEffMulti -S Target -b
#XJ 
#XJ 
#XJ #TMP # Fake: >= 1 loose lepton
#XJ./mkGardener.py -p Apr2017_summer16 -s fakeSelMC -i lepSel__MCWeights__bSFLpTEffMulti__cleanTauMC -S Target -b
#XJ./mkGardener.py -p Apr2017_summer16 -s hadd -i lepSel__MCWeights__bSFLpTEffMulti__cleanTauMC__fakeSelMC -S Target -b
#XJ #TMP 
#XJ # l2loose: >= 2 loose leptons
./mkGardener.py -p Apr2017_summer16 -s l2loose -i lepSel__MCWeights__bSFLpTEffMulti__cleanTauMC -S Target -b
./mkGardener.py -p Apr2017_summer16 -s hadd -i lepSel__MCWeights__bSFLpTEffMulti__cleanTauMC__l2loose -S Target -b
#XJ 
#XJ # l2 tight >= 2 tight leptons (any WP)
#XJ ./mkGardener.py -p Apr2017_summer16 -s  l2tightOR -i lepSel__MCWeights__bSFLpTEffMulti__cleanTauMC__l2loose__hadd -S Target -b
#XJ ./mkGardener.py -p Apr2017_summer16 -s  LepTrgFix  -i lepSel__MCWeights__bSFLpTEffMulti__cleanTauMC__l2loose__hadd__l2tightOR -S Target -b
#XJ ./mkGardener.py -p Apr2017_summer16 -s  dorochester -i lepSel__MCWeights__bSFLpTEffMulti__cleanTauMC__l2loose__hadd__l2tightOR__LepTrgFix -S Target -b
#XJ ./mkGardener.py -p Apr2017_summer16 -s  formulasMC  -i lepSel__MCWeights__bSFLpTEffMulti__cleanTauMC__l2loose__hadd__l2tightOR__LepTrgFix__dorochester -S Target -b
#XJ 
# Skims
#XJ for iSkim in wwSel topSel vh3lSel sfSel vbsSel ssSel dymvaSel_2j dymvaSel sfmvaSel ; do
#XJ    ./mkGardener.py -p Apr2017_summer16 -s  ${iSkim} -i lepSel__MCWeights__bSFLpTEffMulti__cleanTauMC__l2loose__hadd__l2tightOR__LepTrgFix__dorochester__formulasMC -S Target -b
#XJ  done

#XJ./mkGardener.py -p Apr2017_summer16 -s vbsLooseSel -i lepSel__MCWeights__bSFLpTEffMulti__cleanTauMC__l2loose__hadd__l2tightOR__LepTrgFix__dorochester__formulasMC -S Target -b
# Systematics

for iSyst in JESup JESdo METup METdo LepElepTup LepElepTdo LepMupTup LepMupTdo;  do
   ./mkGardener.py -p Apr2017_summer16 -s ${iSyst} -i lepSel__MCWeights__bSFLpTEffMulti__cleanTauMC__l2loose__hadd__l2tightOR__LepTrgFix__dorochester__formulasMC -S Target -b
   for iSkim in wwSel topSel vh3lSel sfSel vbsSel ssSel sfmvaSel ; do
#XJ   for iSkim in vbsLooseSel ; do
      ./mkGardener.py -p Apr2017_summer16 -s  ${iSkim} -i lepSel__MCWeights__bSFLpTEffMulti__cleanTauMC__l2loose__hadd__l2tightOR__LepTrgFix__dorochester__formulasMC__${iSyst} -S Target -b
   done
done

#XJ 
#XJ # Charge Flip
#XJ ./mkGardener.py -p Apr2017_summer16 -s chargeFlipWeightVBS -i lepSel__MCWeights__bSFLpTEffMulti__cleanTauMC__l2loose__hadd__l2tightOR__LepTrgFix__dorochester__formulasMC -S Target -b
#XJ ./mkGardener.py -p Apr2017_summer16 -s vbsLooseSel -i lepSel__MCWeights__bSFLpTEffMulti__cleanTauMC__l2loose__hadd__l2tightOR__LepTrgFix__dorochester__formulasMC__chargeFlipWeightVBS -S Target -b
#XJ for iSyst in JESup JESdo METup METdo LepElepTup LepElepTdo LepMupTup LepMupTdo;  do
#XJ   ./mkGardener.py -p Apr2017_summer16 -s chargeFlipWeightVBS -i lepSel__MCWeights__bSFLpTEffMulti__cleanTauMC__l2loose__hadd__l2tightOR__LepTrgFix__dorochester__formulasMC__${iSyst} -S Target -b
#XJ   ./mkGardener.py -p Apr2017_summer16 -s vbsLooseSel -i lepSel__MCWeights__bSFLpTEffMulti__cleanTauMC__l2loose__hadd__l2tightOR__LepTrgFix__dorochester__formulasMC__${iSyst}__chargeFlipWeightVBS -S Target -b
#XJ done
#XJ 
#XJ 
#XJ 
#XJ # UEPS systematic
#XJ #./mkGardener.py -p Apr2017_summer16 -s UEPS -i lepSel__MCWeights__bSFLpTEffMulti__cleanTauMC__l2loose__hadd__l2tightOR__LepTrgFix__dorochester__formulasMC -S Target 
#XJ #for iSkim in wwSel topSel vh3lSel sfSel vbsSel ssSel sfmvaSel ; do
#XJ #  ./mkGardener.py -p Apr2017_summer16 -s ${iSkim} -i lepSel__MCWeights__bSFLpTEffMulti__cleanTauMC__l2loose__hadd__l2tightOR__LepTrgFix__dorochester__formulasMC__UEup -S Target -b
#XJ #  ./mkGardener.py -p Apr2017_summer16 -s ${iSkim} -i lepSel__MCWeights__bSFLpTEffMulti__cleanTauMC__l2loose__hadd__l2tightOR__LepTrgFix__dorochester__formulasMC__UEdo -S Target -b
#XJ #  ./mkGardener.py -p Apr2017_summer16 -s ${iSkim} -i lepSel__MCWeights__bSFLpTEffMulti__cleanTauMC__l2loose__hadd__l2tightOR__LepTrgFix__dorochester__formulasMC__PS   -S Target -b
#XJ #done
