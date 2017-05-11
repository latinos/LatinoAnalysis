  
for Run in B C D E F G H; do 
 
  # L2 loose Cut
  
 ./mkGardener.py -p Apr2017_Run2016${Run}_RemAOD -s lep2SelVBS -S Target -b -W 24:00:00
 ./mkGardener.py -p Apr2017_Run2016${Run}_RemAOD -s hadd -i lep2SelVBS -S Target -b -W 8:00:00
 ./mkGardener.py -p Apr2017_Run2016${Run}_RemAOD -s EpTCorr,TrigMakerData,l2tightVBS -C -i lep2SelVBS__hadd -S Target -b -W 8:00:00
 ./mkGardener.py -p Apr2017_Run2016${Run}_RemAOD -s TrigMakerData -i lep2SelVBS__hadd__EpTCorr -S Target -b -W 8:00:00
 ./mkGardener.py -p Apr2017_Run2016${Run}_RemAOD -s l2tightVBS -i lep2SelVBS__hadd__EpTCorr__TrigMakerData -S Target -b -W 8:00:00
 
  # Skims 

 for iSkim in vh3lSelVBS vbsSel tightVbsSel; do
   ./mkGardener.py -p Apr2017_Run2016${Run}_RemAOD -s ${iSkim} -i lep2SelVBS__hadd__EpTCorr__TrigMakerData__l2tightVBS -S Target -b -W 1:00:00
 done

 for iSkim in vh3lFakeSel vbsSel tightVbsSel; do
   ./mkGardener.py -p Apr2017_Run2016${Run}_RemAOD -s ${iSkim} -i lep2SelVBS__hadd__EpTCorr__TrigMakerData -S Target -b -W 1:00:00
 done
 
  # FakeWeights
   
#  ./mkGardener.py -p Apr2017_Run2016${Run}_RemAOD -s fakeW12fb -i lep2SelVBS__hadd__EpTCorr__TrigMakerData__tightVbsSel -S Target -b --user=xjanssen -W 1:00:00
#  ./mkGardener.py -p Apr2017_Run2016${Run}_RemAOD -s fakeW12fb -i lep2SelVBS__hadd__EpTCorr__TrigMakerData__vh3lFakeSel -S Target -b --user=xjanssen -W 1:00:00
 

done 
