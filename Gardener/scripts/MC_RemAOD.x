#UEPS 
#UEPS # Doing first common Lepton Selection with nLep > =1 +  pTCorr and trigger bits
#UEPS ./mkGardener.py -p Apr2017_summer16 -s lepSel -S Target -b
#UEPS ./mkGardener.py -p Apr2017_summer16 -s MCWeights -i lepSel -S Target -b
#UEPS ./mkGardener.py -p Apr2017_summer16 -s bSFLpTEffMulti -i lepSel__MCWeights -S Target -b
#UEPS ./mkGardener.py -p Apr2017_summer16 -s cleanTauMC -i lepSel__MCWeights__bSFLpTEffMulti -S Target -b
#UEPS 
#UEPS 
#UEPS # Fake: >= 1 loose lepton
#UEPS ./mkGardener.py -p Apr2017_summer16 -s fakeSelMC -i lepSel__MCWeights__bSFLpTEffMulti__cleanTauMC -S Target -b
#UEPS ./mkGardener.py -p Apr2017_summer16 -s hadd -i lepSel__MCWeights__bSFLpTEffMulti__cleanTauMC__fakeSelMC -S Target -b
#UEPS 
#UEPS # l2loose: >= 2 loose leptons
#UEPS ./mkGardener.py -p Apr2017_summer16 -s l2loose -i lepSel__MCWeights__bSFLpTEffMulti__cleanTauMC -S Target -b
#UEPS ./mkGardener.py -p Apr2017_summer16 -s hadd -i lepSel__MCWeights__bSFLpTEffMulti__cleanTauMC__l2loose -S Target -b
#UEPS 
#UEPS # l2 tight >= 2 tight leptons (any WP)
#UEPS ./mkGardener.py -p Apr2017_summer16 -s  l2tightOR -i lepSel__MCWeights__bSFLpTEffMulti__cleanTauMC__l2loose__hadd -S Target -b
#UEPS ./mkGardener.py -p Apr2017_summer16 -s  formulasMC -i lepSel__MCWeights__bSFLpTEffMulti__cleanTauMC__l2loose__hadd__l2tightOR -S Target -b
#UEPS 
#UEPS # Skims
#UEPS for iSkim in wwSel topSel vh3lSel sfSel vbsSel ssSel dymvaSel_2j dymvaSel sfmvaSel ; do
#UEPS   ./mkGardener.py -p Apr2017_summer16 -s  ${iSkim} -i lepSel__MCWeights__bSFLpTEffMulti__cleanTauMC__l2loose__hadd__l2tightOR__formulasMC -S Target -b
#UEPS done
#UEPS 
#UEPS 
#UEPS # ggHtoMINLO Fix
#UEPS ./mkGardener.py -p Apr2017_summer16 -s ggHtoMINLO -i lepSel__MCWeights -S Target -b
#UEPS ./mkGardener.py -p Apr2017_summer16 -s ggHtoMINLO -i lepSel__MCWeights__bSFLpTEffMulti -S Target -b
#UEPS ./mkGardener.py -p Apr2017_summer16 -s ggHtoMINLO -i lepSel__MCWeights__bSFLpTEffMulti__cleanTauMC -S Target -b
#UEPS ./mkGardener.py -p Apr2017_summer16 -s ggHtoMINLO -i lepSel__MCWeights__bSFLpTEffMulti__cleanTauMC__l2loose -S Target -b
#UEPS ./mkGardener.py -p Apr2017_summer16 -s ggHtoMINLO -i lepSel__MCWeights__bSFLpTEffMulti__cleanTauMC__l2loose__hadd -S Target -b
#UEPS ./mkGardener.py -p Apr2017_summer16 -s ggHtoMINLO -i lepSel__MCWeights__bSFLpTEffMulti__cleanTauMC__l2loose__hadd__l2tightOR -S Target -b
#UEPS ./mkGardener.py -p Apr2017_summer16 -s ggHtoMINLO -i lepSel__MCWeights__bSFLpTEffMulti__cleanTauMC__l2loose__hadd__l2tightOR__formulasMC -S Target -b
#UEPS for iSkim in wwSel topSel vh3lSel sfSel vbsSel ssSel dymvaSel_2j dymvaSel sfmvaSel ; do
#UEPS   ./mkGardener.py -p Apr2017_summer16 -s ggHtoMINLO -i lepSel__MCWeights__bSFLpTEffMulti__cleanTauMC__l2loose__hadd__l2tightOR__formulasMC__${iSkim} -S Target -b
#UEPS done
#UEPS for iSyst in JESup JESdo METup METdo LepElepTup LepElepTdo LepMupTup LepMupTdo;  do
#UEPS   ./mkGardener.py -p Apr2017_summer16 -s ggHtoMINLO -i lepSel__MCWeights__bSFLpTEffMulti__cleanTauMC__l2loose__hadd__l2tightOR__formulasMC__${iSyst} -S Target -b
#UEPS   for iSkim in wwSel topSel vh3lSel sfSel vbsSel ssSel dymvaSel_2j dymvaSel sfmvaSel ; do
#UEPS     ./mkGardener.py -p Apr2017_summer16 -s ggHtoMINLO -i lepSel__MCWeights__bSFLpTEffMulti__cleanTauMC__l2loose__hadd__l2tightOR__formulasMC__${iSyst}__${iSkim} -S Target -b
#UEPS   done
#UEPS done
#UEPS 
#UEPS # Systematics
#UEPS 
#UEPS for iSyst in JESup JESdo METup METdo LepElepTup LepElepTdo LepMupTup LepMupTdo;  do
#UEPS   ./mkGardener.py -p Apr2017_summer16 -s ${iSyst} -i lepSel__MCWeights__bSFLpTEffMulti__cleanTauMC__l2loose__hadd__l2tightOR__formulasMC -S Target -b
#UEPS   for iSkim in wwSel topSel vh3lSel sfSel vbsSel ssSel sfmvaSel ; do
#UEPS     ./mkGardener.py -p Apr2017_summer16 -s  ${iSkim} -i lepSel__MCWeights__bSFLpTEffMulti__cleanTauMC__l2loose__hadd__l2tightOR__formulasMC__${iSyst} -S Target -b
#UEPS   done
#UEPS done

# UEPS systematic
./mkGardener.py -p Apr2017_summer16 -s UEPS -i lepSel__MCWeights__bSFLpTEffMulti__cleanTauMC__l2loose__hadd__l2tightOR__formulasMC -S Target 
for iSkim in wwSel topSel vh3lSel sfSel vbsSel ssSel sfmvaSel ; do
  ./mkGardener.py -p Apr2017_summer16 -s ${iSkim} -i lepSel__MCWeights__bSFLpTEffMulti__cleanTauMC__l2loose__hadd__l2tightOR__formulasMC__UEup -S Target -b
  ./mkGardener.py -p Apr2017_summer16 -s ${iSkim} -i lepSel__MCWeights__bSFLpTEffMulti__cleanTauMC__l2loose__hadd__l2tightOR__formulasMC__UEdo -S Target -b
  ./mkGardener.py -p Apr2017_summer16 -s ${iSkim} -i lepSel__MCWeights__bSFLpTEffMulti__cleanTauMC__l2loose__hadd__l2tightOR__formulasMC__PS   -S Target -b
done
