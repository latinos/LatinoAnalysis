  
for Run in B C D E F G H; do 

  # Doing first common Lepton Selection with nLep > =1 +  pTCorr and trigger bits
# ./mkGardener.py -p Apr2017_Run2016${Run}_RemAOD -s lepSel -S Target -b
# ./mkGardener.py -p Apr2017_Run2016${Run}_RemAOD -s EpTCorr,TrigMakerData -i lepSel -C -S Target -b

  ./mkGardener.py -p Apr2017_Run2016${Run}_RemAOD -s TrigMakerData -i lepSel__EpTCorr -S Target -b
  ./mkGardener.py -p Apr2017_Run2016${Run}_RemAOD -s cleanTauData  -i lepSel__EpTCorr__TrigMakerData -S Target -b

  # Fake: >= 1 loose lepton
  ./mkGardener.py -p Apr2017_Run2016${Run}_RemAOD -s hadd    -i lepSel__EpTCorr__TrigMakerData__cleanTauData -S Target -b 
  ./mkGardener.py -p Apr2017_Run2016${Run}_RemAOD -s fakeSel -i lepSel__EpTCorr__TrigMakerData__cleanTauData -S Target -b
  ./mkGardener.py -p Apr2017_Run2016${Run}_RemAOD -s hadd    -i lepSel__EpTCorr__TrigMakerData__cleanTauData__fakeSel -S Target -b 

  # l2loose: >= 2 loose leptons 
  ./mkGardener.py -p Apr2017_Run2016${Run}_RemAOD -s l2loose -i lepSel__EpTCorr__TrigMakerData__cleanTauData -S Target -b
  ./mkGardener.py -p Apr2017_Run2016${Run}_RemAOD -s hadd    -i lepSel__EpTCorr__TrigMakerData__cleanTauData__l2loose -S Target -b

  # FakeW
  ./mkGardener.py -p Apr2017_Run2016${Run}_RemAOD -s multiFakeW -i lepSel__EpTCorr__TrigMakerData__cleanTauData__l2loose__hadd -S Target -b

  # l2 tight >= 2 tight leptons (any WP) 
  ./mkGardener.py -p Apr2017_Run2016${Run}_RemAOD -s l2tightOR -i lepSel__EpTCorr__TrigMakerData__cleanTauData__l2loose__hadd -S Target -b
# ./mkGardener.py -p Apr2017_Run2016${Run}_RemAOD -s formulasDATA -i lepSel__EpTCorr__TrigMakerData__cleanTauData__l2loose__hadd__l2tightOR -S Target -b

  # Skims
# for iSkim in wwSel for iSkim in wwSel  ; do
#   ./mkGardener.py -p Apr2017_Run2016${Run}_RemAOD -s ${iSkim} -i lepSel__EpTCorr__TrigMakerData__cleanTauData__l2loose__hadd__l2tightOR__formulasDATA -S Target -b
# done

######## OLD BELOW ########
 
  # L2 loose Cut
  
# ./mkGardener.py -p Apr2017_Run2016${Run}_RemAOD -s l2looseCut -S Target -b
# ./mkGardener.py -p Apr2017_Run2016${Run}_RemAOD -s hadd -i l2looseCut -S Target -b
# ./mkGardener.py -p Apr2017_Run2016${Run}_RemAOD -s EpTCorr,TrigMakerData,l2tight -C -i l2looseCut__hadd -S Target -b
 
# for iSkim in wwSel topSel vh3lSel sfSel vbsSel ; do
#   ./mkGardener.py -p Apr2017_Run2016${Run}_RemAOD -s ${iSkim} -i l2looseCut__hadd__EpTCorr__TrigMakerData__l2tight -S Target -b
# done
 
   # FakeWCut
   
#  ./mkGardener.py -p Apr2017_Run2016${Run}_RemAOD -s fakeWCut -i l2looseCut__hadd__EpTCorr__TrigMakerData -S Target -b
#  for iSkim in wwSel topSel vh3lFakeSel sfSel vbsSel ; do
#    ./mkGardener.py -p Apr2017_Run2016${Run}_RemAOD -s ${iSkim} -i l2looseCut__hadd__EpTCorr__TrigMakerData__fakeWCut -S Target -b
#  done
 
  # L2 vloose Cut
  
# ./mkGardener.py -p Apr2017_Run2016${Run}_RemAOD -s l2vlooseCut -S Target -b
# ./mkGardener.py -p Apr2017_Run2016${Run}_RemAOD -s hadd -i l2vlooseCut -S Target -b 
# ./mkGardener.py -p Apr2017_Run2016${Run}_RemAOD -s EpTCorr,TrigMakerData,l2tight,vbsSel -C -i l2vlooseCut__hadd -S Target -b
# ./mkGardener.py -p Apr2017_Run2016${Run}_RemAOD -s vbsSel -i l2vlooseCut__hadd__EpTCorr__TrigMakerData -S Target -b
 
  # L1 loose Cut
  
# ./mkGardener.py -p Apr2017_Run2016${Run}_RemAOD -s l1looseCut -S Target -b
# ./mkGardener.py -p Apr2017_Run2016${Run}_RemAOD -s EpTCorr,fakeSel -C -i l1looseCut -S Target -b
# ./mkGardener.py -p Apr2017_Run2016${Run}_RemAOD -s hadd -i l1looseCut__EpTCorr -S Target -b
# ./mkGardener.py -p Apr2017_Run2016${Run}_RemAOD -s hadd -i l1looseCut__EpTCorr__fakeSel -S Target -b
  
  # L1 vloose Cut
  
# ./mkGardener.py -p Apr2017_Run2016${Run}_RemAOD -s l1vlooseCut -S Target -b
# ./mkGardener.py -p Apr2017_Run2016${Run}_RemAOD -s EpTCorr,fakeSel -C -i l1vlooseCut -S Target -b
# ./mkGardener.py -p Apr2017_Run2016${Run}_RemAOD -s hadd -i l1vlooseCut__EpTCorr__fakeSel -S Target -b
 
done 
