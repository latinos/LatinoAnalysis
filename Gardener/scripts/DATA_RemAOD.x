  
for Run in B C D E F G H; do 

#  # Doing first common Lepton Selection with nLep > =1 +  pTCorr and trigger bits
#  ./mkGardener.py -p Apr2017_Run2016${Run}_RemAOD -s lepSel -S Target -b
#  ./mkGardener.py -p Apr2017_Run2016${Run}_RemAOD -s EpTCorr,TrigMakerData,cleanTauData -i lepSel -C -S Target -b

#  # Fake: >= 1 loose lepton
#  ./mkGardener.py -p Apr2017_Run2016${Run}_RemAOD -s hadd    -i lepSel__EpTCorr__TrigMakerData__cleanTauData -S Target -b 
#  ./mkGardener.py -p Apr2017_Run2016${Run}_RemAOD -s fakeSel -i lepSel__EpTCorr__TrigMakerData__cleanTauData -S Target -b
#  ./mkGardener.py -p Apr2017_Run2016${Run}_RemAOD -s hadd    -i lepSel__EpTCorr__TrigMakerData__cleanTauData__fakeSel -S Target -b 

#  # l2loose: >= 2 loose leptons 
#  ./mkGardener.py -p Apr2017_Run2016${Run}_RemAOD -s l2loose -i lepSel__EpTCorr__TrigMakerData__cleanTauData -S Target -b
#  ./mkGardener.py -p Apr2017_Run2016${Run}_RemAOD -s hadd    -i lepSel__EpTCorr__TrigMakerData__cleanTauData__l2loose -S Target -b

# # FakeW
#  ./mkGardener.py -p Apr2017_Run2016${Run}_RemAOD -s multiFakeW -i lepSel__EpTCorr__TrigMakerData__cleanTauData__l2loose -S Target -b
#  ./mkGardener.py -p Apr2017_Run2016${Run}_RemAOD -s dorochester -i lepSel__EpTCorr__TrigMakerData__cleanTauData__l2loose__multiFakeW -S Target -b
#  ./mkGardener.py -p Apr2017_Run2016${Run}_RemAOD -s formulasFAKE -i lepSel__EpTCorr__TrigMakerData__cleanTauData__l2loose__multiFakeW__dorochester -S Target -b
#  ./mkGardener.py -p Apr2017_Run2016${Run}_RemAOD -s hadd -i lepSel__EpTCorr__TrigMakerData__cleanTauData__l2loose__multiFakeW__dorochester__formulasFAKE -S Target -b
#  for iSkim in wwSel topSel vh3lFakeSel sfSel vbsSel ssSel sfmvaSel ; do
   for vbsLooseSel ; do
     ./mkGardener.py -p Apr2017_Run2016${Run}_RemAOD -s ${iSkim} -i lepSel__EpTCorr__TrigMakerData__cleanTauData__l2loose__multiFakeW__dorochester__formulasFAKE__hadd -S Target -b
   done

   # FakeW
#  ./mkGardener.py -p Apr2017_Run2016${Run}_RemAOD -s dorochester  -i lepSel__EpTCorr__TrigMakerData__cleanTauData__l2loose -S Target -b   
#  ./mkGardener.py -p Apr2017_Run2016${Run}_RemAOD -s multiFakeW   -i lepSel__EpTCorr__TrigMakerData__cleanTauData__l2loose__dorochester -S Target -b
#  ./mkGardener.py -p Apr2017_Run2016${Run}_RemAOD -s formulasFAKE -i lepSel__EpTCorr__TrigMakerData__cleanTauData__l2loose__dorochester__multiFakeW -S Target -b
#  ./mkGardener.py -p Apr2017_Run2016${Run}_RemAOD -s hadd         -i lepSel__EpTCorr__TrigMakerData__cleanTauData__l2loose__dorochester__multiFakeW__formulasFAKE -S Target -b
#  for iSkim in wwSel topSel vh3lFakeSel sfSel vbsSel ssSel sfmvaSel ; do
   for vbsLooseSel ; do
     ./mkGardener.py -p Apr2017_Run2016${Run}_RemAOD -s ${iSkim} -i lepSel__EpTCorr__TrigMakerData__cleanTauData__l2loose__dorochester__multiFakeW__formulasFAKE__hadd -S Target -b
   done
   


#  # l2 tight >= 2 tight leptons (any WP) 
#  ./mkGardener.py -p Apr2017_Run2016${Run}_RemAOD -s l2tightOR -i lepSel__EpTCorr__TrigMakerData__cleanTauData__l2loose__hadd -S Target -b
#  ./mkGardener.py -p Apr2017_Run2016${Run}_RemAOD -s formulasDATA -i lepSel__EpTCorr__TrigMakerData__cleanTauData__l2loose__hadd__l2tightOR -S Target -b

#  ./mkGardener.py -p Apr2017_Run2016${Run}_RemAOD -s dorochester -i lepSel__EpTCorr__TrigMakerData__cleanTauData__l2loose__hadd__l2tightOR -S Target -b
#  ./mkGardener.py -p Apr2017_Run2016${Run}_RemAOD -s formulasDATA -i lepSel__EpTCorr__TrigMakerData__cleanTauData__l2loose__hadd__l2tightOR__dorochester -S Target -b

   # Skims
#  for iSkim in wwSel topSel vh3lSel sfSel vbsSel ssSel sfmvaSel ; do
   for vbsLooseSel ; do
     ./mkGardener.py -p Apr2017_Run2016${Run}_RemAOD -s ${iSkim} -i lepSel__EpTCorr__TrigMakerData__cleanTauData__l2loose__hadd__l2tightOR__dorochester__formulasDATA -S Target -b
   done

done
