
# Doing first common Lepton Selection with nLep > =1 +  pTCorr and trigger bits
./mkGardener.py -p Apr2017_summer16 -s lepSel -S Target -b
./mkGardener.py -p Apr2017_summer16 -s MCWeights -i lepSel -S Target -b
./mkGardener.py -p Apr2017_summer16 -s bSFLpTEffMulti -i lepSel__MCWeights -S Target -b
./mkGardener.py -p Apr2017_summer16 -s cleanTauMC -i lepSel__MCWeights__bSFLpTEffMulti -S Target -b


# Fake: >= 1 loose lepton
./mkGardener.py -p Apr2017_summer16 -s fakeSelMC -i lepSel__MCWeights__bSFLpTEffMulti__cleanTauMC -S Target -b
./mkGardener.py -p Apr2017_summer16 -s hadd -i lepSel__MCWeights__bSFLpTEffMulti__cleanTauMC__fakeSelMC -S Target -b

# l2loose: >= 2 loose leptons
./mkGardener.py -p Apr2017_summer16 -s l2loose -i lepSel__MCWeights__bSFLpTEffMulti__cleanTauMC -S Target -b
./mkGardener.py -p Apr2017_summer16 -s hadd -i lepSel__MCWeights__bSFLpTEffMulti__cleanTauMC__l2loose -S Target -b

# l2 tight >= 2 tight leptons (any WP)
./mkGardener.py -p Apr2017_summer16 -s  l2tightOR -i lepSel__MCWeights__bSFLpTEffMulti__cleanTauMC__l2loose__hadd -S Target -b
./mkGardener.py -p Apr2017_summer16 -s  formulasMC -i lepSel__MCWeights__bSFLpTEffMulti__cleanTauMC__l2loose__hadd__l2tightOR -S Target -b

# Skims
for iSkim in wwSel topSel vh3lSel sfSel vbsSel ssSel dymvaSel_2j dymvaSel sfmvaSel ; do
  ./mkGardener.py -p Apr2017_summer16 -s  ${iSkim} -i lepSel__MCWeights__bSFLpTEffMulti__cleanTauMC__l2loose__hadd__l2tightOR__formulasMC -S Target -b
done


# ggHtoMINLO Fix
./mkGardener.py -p Apr2017_summer16 -s ggHtoMINLO -i lepSel__MCWeights -S Target -b
./mkGardener.py -p Apr2017_summer16 -s ggHtoMINLO -i lepSel__MCWeights__bSFLpTEffMulti -S Target -b
./mkGardener.py -p Apr2017_summer16 -s ggHtoMINLO -i lepSel__MCWeights__bSFLpTEffMulti__cleanTauMC -S Target -b
./mkGardener.py -p Apr2017_summer16 -s ggHtoMINLO -i lepSel__MCWeights__bSFLpTEffMulti__cleanTauMC__l2loose -S Target -b
./mkGardener.py -p Apr2017_summer16 -s ggHtoMINLO -i lepSel__MCWeights__bSFLpTEffMulti__cleanTauMC__l2loose__hadd -S Target -b
./mkGardener.py -p Apr2017_summer16 -s ggHtoMINLO -i lepSel__MCWeights__bSFLpTEffMulti__cleanTauMC__l2loose__hadd__l2tightOR -S Target -b
./mkGardener.py -p Apr2017_summer16 -s ggHtoMINLO -i lepSel__MCWeights__bSFLpTEffMulti__cleanTauMC__l2loose__hadd__l2tightOR__formulasMC -S Target -b
for iSkim in wwSel topSel vh3lSel sfSel vbsSel ssSel dymvaSel_2j dymvaSel sfmvaSel ; do
  ./mkGardener.py -p Apr2017_summer16 -s ggHtoMINLO -i lepSel__MCWeights__bSFLpTEffMulti__cleanTauMC__l2loose__hadd__l2tightOR__formulasMC__${iSkim} -S Target -b
done
for iSyst in JESup JESdo METup METdo LepElepTup LepElepTdo LepMupTup LepMupTdo;  do
  ./mkGardener.py -p Apr2017_summer16 -s ggHtoMINLO -i lepSel__MCWeights__bSFLpTEffMulti__cleanTauMC__l2loose__hadd__l2tightOR__formulasMC__${iSyst} -S Target -b
  for iSkim in wwSel topSel vh3lSel sfSel vbsSel ssSel dymvaSel_2j dymvaSel sfmvaSel ; do
    ./mkGardener.py -p Apr2017_summer16 -s ggHtoMINLO -i lepSel__MCWeights__bSFLpTEffMulti__cleanTauMC__l2loose__hadd__l2tightOR__formulasMC__${iSyst}__${iSkim} -S Target -b
  done
done

# Systematics

for iSyst in JESup JESdo METup METdo LepElepTup LepElepTdo LepMupTup LepMupTdo;  do
  ./mkGardener.py -p Apr2017_summer16 -s ${iSyst} -i lepSel__MCWeights__bSFLpTEffMulti__cleanTauMC__l2loose__hadd__l2tightOR__formulasMC -S Target -b
  for iSkim in wwSel topSel vh3lSel sfSel vbsSel ssSel sfmvaSel ; do
    ./mkGardener.py -p Apr2017_summer16 -s  ${iSkim} -i lepSel__MCWeights__bSFLpTEffMulti__cleanTauMC__l2loose__hadd__l2tightOR__formulasMC__${iSyst} -S Target -b
  done
done

# UEPS systematic
./mkGardener.py -p Apr2017_summer16 -s UEPS -i lepSel__MCWeights__bSFLpTEffMulti__cleanTauMC__l2loose__hadd__l2tightOR__formulasMC -S Target 
for iSkim in wwSel topSel vh3lSel sfSel vbsSel ssSel sfmvaSel ; do
  ./mkGardener.py -p Apr2017_summer16 -s ${iSkim} -i lepSel__MCWeights__bSFLpTEffMulti__cleanTauMC__l2loose__hadd__l2tightOR__formulasMC__UEup -S Target -b
  ./mkGardener.py -p Apr2017_summer16 -s ${iSkim} -i lepSel__MCWeights__bSFLpTEffMulti__cleanTauMC__l2loose__hadd__l2tightOR__formulasMC__UEdo -S Target -b
  ./mkGardener.py -p Apr2017_summer16 -s ${iSkim} -i lepSel__MCWeights__bSFLpTEffMulti__cleanTauMC__l2loose__hadd__l2tightOR__formulasMC__PS   -S Target -b
done
