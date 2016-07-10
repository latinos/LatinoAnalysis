./mkGardener.py -p 05Jul2016_Run2016B_PromptReco  -s WgStarsel -S Target -b 
./mkGardener.py -p 05Jul2016_Run2016B_PromptReco  -s hadd -i WgStarsel -S Target -b 
./mkGardener.py -p 05Jul2016_Run2016B_PromptReco  -s EpTCorr -i WgStarsel__hadd -S Target -b 

./mkGardener.py -p 05Jul2016_Run2016B_PromptReco  -s l1loose -S Target -b
./mkGardener.py -p 05Jul2016_Run2016B_PromptReco  -s EpTCorr -i l1loose -S Target -b
./mkGardener.py -p 05Jul2016_Run2016B_PromptReco  -s hadd -i l1loose__EpTCorr -S Target -b

./mkGardener.py -p 05Jul2016_Run2016B_PromptReco  -s l2loose -S Target -b 
./mkGardener.py -p 05Jul2016_Run2016B_PromptReco  -s hadd -i l2loose -S Target -b 
./mkGardener.py -p 05Jul2016_Run2016B_PromptReco  -s EpTCorr,l2tight,wwSel -i l2loose__hadd -S Target -b -C
./mkGardener.py -p 05Jul2016_Run2016B_PromptReco  -s vh3lSel -i l2loose__hadd__EpTCorr__l2tight -S Target -b 



./mkGardener.py -p 21Jun2016_Run2016B_PromptReco  -s WgStarsel -S Target -b        
./mkGardener.py -p 21Jun2016_Run2016B_PromptReco  -s hadd -i WgStarsel -S Target -b
./mkGardener.py -p 21Jun2016_Run2016B_PromptReco  -s EpTCorr -i WgStarsel__hadd -S Target -b
 
./mkGardener.py -p 21Jun2016_Run2016B_PromptReco  -s l1loose -S Target -b
./mkGardener.py -p 21Jun2016_Run2016B_PromptReco  -s EpTCorr -i l1loose -S Target -b
./mkGardener.py -p 21Jun2016_Run2016B_PromptReco  -s hadd -i l1loose__EpTCorr -S Target -b

./mkGardener.py -p 21Jun2016_Run2016B_PromptReco  -s l2loose -S Target -b 
./mkGardener.py -p 21Jun2016_Run2016B_PromptReco  -s hadd -i l2loose -S Target -b 
./mkGardener.py -p 21Jun2016_Run2016B_PromptReco  -s EpTCorr,l2tight,wwSel -i l2loose__hadd -S Target -b -C
./mkGardener.py -p 21Jun2016_Run2016B_PromptReco  -s vh3lSel -i l2loose__hadd__EpTCorr__l2tight -S Target -b



