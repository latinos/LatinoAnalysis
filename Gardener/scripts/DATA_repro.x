
./mkGardener.py -p 08Jul2016_Run2016C_PromptReco_repro  -s WgStarsel -S Target -b
./mkGardener.py -p 08Jul2016_Run2016C_PromptReco_repro  -s hadd -i WgStarsel -S Target -b
./mkGardener.py -p 08Jul2016_Run2016C_PromptReco_repro  -s EpTCorr -i WgStarsel__hadd -S Target -b

./mkGardener.py -p 08Jul2016_Run2016C_PromptReco_repro  -s l1loose -S Target -b
./mkGardener.py -p 08Jul2016_Run2016C_PromptReco_repro  -s EpTCorr -i l1loose -S Target -b
./mkGardener.py -p 08Jul2016_Run2016C_PromptReco_repro  -s fakeSel -i l1loose__EpTCorr -S Target -b
./mkGardener.py -p 08Jul2016_Run2016C_PromptReco_repro  -s hadd -i l1loose__EpTCorr__fakeSel -S Target -b
./mkGardener.py -p 08Jul2016_Run2016C_PromptReco_repro  -s 3jetsSel -i l1loose__EpTCorr -S Target -b
./mkGardener.py -p 08Jul2016_Run2016C_PromptReco_repro  -s hadd -i l1loose__EpTCorr__3jetsSel -S Target -b
./mkGardener.py -p 08Jul2016_Run2016C_PromptReco_repro  -s hadd -i l1loose__EpTCorr -S Target -b

./mkGardener.py -p 08Jul2016_Run2016C_PromptReco_repro  -s l2loose -S Target -b
./mkGardener.py -p 08Jul2016_Run2016C_PromptReco_repro  -s hadd -i l2loose -S Target -b
./mkGardener.py -p 08Jul2016_Run2016C_PromptReco_repro  -s EpTCorr,l2tight,wwSel -i l2loose__hadd -S Target -b -C
./mkGardener.py -p 08Jul2016_Run2016C_PromptReco_repro  -s vh3lSel -i l2loose__hadd__EpTCorr__l2tight -S Target -b
./mkGardener.py -p 08Jul2016_Run2016C_PromptReco_repro  -s fakeW -i l2loose__hadd__EpTCorr -S Target -b 

./mkGardener.py -p 08Jul2016_Run2016B_PromptReco_repro  -s WgStarsel -S Target -b
./mkGardener.py -p 08Jul2016_Run2016B_PromptReco_repro  -s hadd -i WgStarsel -S Target -b
./mkGardener.py -p 08Jul2016_Run2016B_PromptReco_repro  -s EpTCorr -i WgStarsel__hadd -S Target -b

./mkGardener.py -p 08Jul2016_Run2016B_PromptReco_repro  -s l1loose -S Target -b
./mkGardener.py -p 08Jul2016_Run2016B_PromptReco_repro  -s EpTCorr -i l1loose -S Target -b
./mkGardener.py -p 08Jul2016_Run2016B_PromptReco_repro  -s fakeSel -i l1loose__EpTCorr -S Target -b
./mkGardener.py -p 08Jul2016_Run2016B_PromptReco_repro  -s hadd -i l1loose__EpTCorr__fakeSel -S Target -b
./mkGardener.py -p 08Jul2016_Run2016B_PromptReco_repro  -s 3jetsSel -i l1loose__EpTCorr -S Target -b
./mkGardener.py -p 08Jul2016_Run2016B_PromptReco_repro  -s hadd -i l1loose__EpTCorr__3jetsSel -S Target -b
./mkGardener.py -p 08Jul2016_Run2016B_PromptReco_repro  -s hadd -i l1loose__EpTCorr -S Target -b

./mkGardener.py -p 08Jul2016_Run2016B_PromptReco_repro  -s l2loose -S Target -b
./mkGardener.py -p 08Jul2016_Run2016B_PromptReco_repro  -s hadd -i l2loose -S Target -b
./mkGardener.py -p 08Jul2016_Run2016B_PromptReco_repro  -s EpTCorr,l2tight,wwSel -i l2loose__hadd -S Target -b -C
./mkGardener.py -p 08Jul2016_Run2016B_PromptReco_repro  -s vh3lSel -i l2loose__hadd__EpTCorr__l2tight -S Target -b
./mkGardener.py -p 08Jul2016_Run2016B_PromptReco_repro  -s fakeW -i l2loose__hadd__EpTCorr -S Target -b 




./mkGardener.py -p 05Jul2016_Run2016B_PromptReco_repro  -s WgStarsel -S Target -b 
./mkGardener.py -p 05Jul2016_Run2016B_PromptReco_repro  -s hadd -i WgStarsel -S Target -b 
./mkGardener.py -p 05Jul2016_Run2016B_PromptReco_repro  -s EpTCorr -i WgStarsel__hadd -S Target -b 

./mkGardener.py -p 05Jul2016_Run2016B_PromptReco_repro  -s l1loose -S Target -b
./mkGardener.py -p 05Jul2016_Run2016B_PromptReco_repro  -s EpTCorr -i l1loose -S Target -b
./mkGardener.py -p 05Jul2016_Run2016B_PromptReco_repro  -s fakeSel -i l1loose__EpTCorr -S Target -b
./mkGardener.py -p 05Jul2016_Run2016B_PromptReco_repro  -s hadd -i l1loose__EpTCorr__fakeSel -S Target -b
./mkGardener.py -p 05Jul2016_Run2016B_PromptReco_repro  -s 3jetsSel -i l1loose__EpTCorr -S Target -b
./mkGardener.py -p 05Jul2016_Run2016B_PromptReco_repro  -s hadd -i l1loose__EpTCorr__3jetsSel -S Target -b
./mkGardener.py -p 05Jul2016_Run2016B_PromptReco_repro  -s hadd -i l1loose__EpTCorr -S Target -b

./mkGardener.py -p 05Jul2016_Run2016B_PromptReco_repro  -s l2loose -S Target -b 
./mkGardener.py -p 05Jul2016_Run2016B_PromptReco_repro  -s hadd -i l2loose -S Target -b 
./mkGardener.py -p 05Jul2016_Run2016B_PromptReco_repro  -s EpTCorr,l2tight,wwSel -i l2loose__hadd -S Target -b -C
./mkGardener.py -p 05Jul2016_Run2016B_PromptReco_repro  -s vh3lSel -i l2loose__hadd__EpTCorr__l2tight -S Target -b 
./mkGardener.py -p 05Jul2016_Run2016B_PromptReco_repro  -s fakeW -i l2loose__hadd__EpTCorr -S Target -b 



./mkGardener.py -p 21Jun2016_v2_Run2016B_PromptReco_repro  -s WgStarsel -S Target -b        
./mkGardener.py -p 21Jun2016_v2_Run2016B_PromptReco_repro  -s hadd -i WgStarsel -S Target -b
./mkGardener.py -p 21Jun2016_v2_Run2016B_PromptReco_repro  -s EpTCorr -i WgStarsel__hadd -S Target -b
 
./mkGardener.py -p 21Jun2016_v2_Run2016B_PromptReco_repro  -s l1loose -S Target -b
./mkGardener.py -p 21Jun2016_v2_Run2016B_PromptReco_repro  -s EpTCorr -i l1loose -S Target -b
./mkGardener.py -p 21Jun2016_v2_Run2016B_PromptReco_repro  -s fakeSel -i l1loose__EpTCorr -S Target -b
./mkGardener.py -p 21Jun2016_v2_Run2016B_PromptReco_repro  -s hadd -i l1loose__EpTCorr__fakeSel -S Target -b
./mkGardener.py -p 21Jun2016_v2_Run2016B_PromptReco_repro  -s 3jetsSel -i l1loose__EpTCorr -S Target -b
./mkGardener.py -p 21Jun2016_v2_Run2016B_PromptReco_repro  -s hadd -i l1loose__EpTCorr__3jetsSel -S Target -b
./mkGardener.py -p 21Jun2016_v2_Run2016B_PromptReco_repro  -s hadd -i l1loose__EpTCorr -S Target -b

./mkGardener.py -p 21Jun2016_v2_Run2016B_PromptReco_repro  -s l2loose -S Target -b 
./mkGardener.py -p 21Jun2016_v2_Run2016B_PromptReco_repro  -s hadd -i l2loose -S Target -b 
./mkGardener.py -p 21Jun2016_v2_Run2016B_PromptReco_repro  -s EpTCorr,l2tight,wwSel -i l2loose__hadd -S Target -b -C
./mkGardener.py -p 21Jun2016_v2_Run2016B_PromptReco_repro  -s vh3lSel -i l2loose__hadd__EpTCorr__l2tight -S Target -b
./mkGardener.py -p 21Jun2016_v2_Run2016B_PromptReco_repro  -s fakeW -i l2loose__hadd__EpTCorr -S Target -b 



./mkGardener.py -p 26Jul2016_Run2016D_PromptReco_repro  -s WgStarsel -S Target -b
./mkGardener.py -p 26Jul2016_Run2016D_PromptReco_repro  -s hadd -i WgStarsel -S Target -b
./mkGardener.py -p 26Jul2016_Run2016D_PromptReco_repro  -s ICHEPjson -i WgStarsel__hadd -S Target -b
./mkGardener.py -p 26Jul2016_Run2016D_PromptReco_repro  -s EpTCorr -i WgStarsel__hadd__ICHEPjson -S Target -b

./mkGardener.py -p 26Jul2016_Run2016D_PromptReco_repro  -s l1loose -S Target -b
./mkGardener.py -p 26Jul2016_Run2016D_PromptReco_repro  -s ICHEPjson -i l1loose -S Target -b
./mkGardener.py -p 26Jul2016_Run2016D_PromptReco_repro  -s EpTCorr -i l1loose__ICHEPjson -S Target -b
./mkGardener.py -p 26Jul2016_Run2016D_PromptReco_repro  -s fakeSel -i l1loose__ICHEPjson__EpTCorr -S Target -b
./mkGardener.py -p 26Jul2016_Run2016D_PromptReco_repro  -s hadd -i l1loose__ICHEPjson__EpTCorr__fakeSel -S Target -b
./mkGardener.py -p 26Jul2016_Run2016D_PromptReco_repro  -s 3jetsSel -i l1loose__ICHEPjson__EpTCorr -S Target -b
./mkGardener.py -p 26Jul2016_Run2016D_PromptReco_repro  -s hadd -i l1loose__ICHEPjson__EpTCorr__3jetsSel -S Target -b
./mkGardener.py -p 26Jul2016_Run2016D_PromptReco_repro  -s hadd -i l1loose__ICHEPjson__EpTCorr -S Target -b

./mkGardener.py -p 26Jul2016_Run2016D_PromptReco_repro  -s l2loose -S Target -b
./mkGardener.py -p 26Jul2016_Run2016D_PromptReco_repro  -s hadd -i l2loose -S Target -b
./mkGardener.py -p 26Jul2016_Run2016D_PromptReco_repro  -s ICHEPjson -i l2loose__hadd -S Target -b
./mkGardener.py -p 26Jul2016_Run2016D_PromptReco_repro  -s EpTCorr,l2tight,wwSel -i l2loose__hadd__ICHEPjson -S Target -b -C
./mkGardener.py -p 26Jul2016_Run2016D_PromptReco_repro  -s vh3lSel -i l2loose__hadd__ICHEPjson__EpTCorr__l2tight -S Target -b


./mkGardener.py -p 15Jul2016_Run2016D_PromptReco_repro  -s WgStarsel -S Target -b
./mkGardener.py -p 15Jul2016_Run2016D_PromptReco_repro  -s hadd -i WgStarsel -S Target -b
./mkGardener.py -p 15Jul2016_Run2016D_PromptReco_repro  -s ICHEPjson -i WgStarsel__hadd -S Target -b
./mkGardener.py -p 15Jul2016_Run2016D_PromptReco_repro  -s EpTCorr -i WgStarsel__hadd__ICHEPjson -S Target -b

./mkGardener.py -p 15Jul2016_Run2016D_PromptReco_repro  -s l1loose -S Target -b
./mkGardener.py -p 15Jul2016_Run2016D_PromptReco_repro  -s ICHEPjson -i l1loose -S Target -b
./mkGardener.py -p 15Jul2016_Run2016D_PromptReco_repro  -s EpTCorr -i l1loose__ICHEPjson -S Target -b
./mkGardener.py -p 15Jul2016_Run2016D_PromptReco_repro  -s fakeSel -i l1loose__ICHEPjson__EpTCorr -S Target -b
./mkGardener.py -p 15Jul2016_Run2016D_PromptReco_repro  -s hadd -i l1loose__ICHEPjson__EpTCorr__fakeSel -S Target -b
./mkGardener.py -p 15Jul2016_Run2016D_PromptReco_repro  -s 3jetsSel -i l1loose__ICHEPjson__EpTCorr -S Target -b
./mkGardener.py -p 15Jul2016_Run2016D_PromptReco_repro  -s hadd -i l1loose__ICHEPjson__EpTCorr__3jetsSel -S Target -b
./mkGardener.py -p 15Jul2016_Run2016D_PromptReco_repro  -s hadd -i l1loose__ICHEPjson__EpTCorr -S Target -b

./mkGardener.py -p 15Jul2016_Run2016D_PromptReco_repro  -s l2loose -S Target -b
./mkGardener.py -p 15Jul2016_Run2016D_PromptReco_repro  -s hadd -i l2loose -S Target -b
./mkGardener.py -p 15Jul2016_Run2016D_PromptReco_repro  -s ICHEPjson -i l2loose__hadd -S Target -b
./mkGardener.py -p 15Jul2016_Run2016D_PromptReco_repro  -s EpTCorr,l2tight,wwSel -i l2loose__hadd__ICHEPjson -S Target -b -C
./mkGardener.py -p 15Jul2016_Run2016D_PromptReco_repro  -s vh3lSel -i l2loose__hadd__ICHEPjson__EpTCorr__l2tight -S Target -b


./mkGardener.py -p 15Jul2016_Run2016C_PromptReco_repro  -s WgStarsel -S Target -b
./mkGardener.py -p 15Jul2016_Run2016C_PromptReco_repro  -s hadd -i WgStarsel -S Target -b
./mkGardener.py -p 15Jul2016_Run2016C_PromptReco_repro  -s ICHEPjson -i WgStarsel__hadd -S Target -b
./mkGardener.py -p 15Jul2016_Run2016C_PromptReco_repro  -s EpTCorr -i WgStarsel__hadd__ICHEPjson -S Target -b

./mkGardener.py -p 15Jul2016_Run2016C_PromptReco_repro  -s l1loose -S Target -b
./mkGardener.py -p 15Jul2016_Run2016C_PromptReco_repro  -s ICHEPjson -i l1loose -S Target -b
./mkGardener.py -p 15Jul2016_Run2016C_PromptReco_repro  -s EpTCorr -i l1loose__ICHEPjson -S Target -b
./mkGardener.py -p 15Jul2016_Run2016C_PromptReco_repro  -s fakeSel -i l1loose__ICHEPjson__EpTCorr -S Target -b
./mkGardener.py -p 15Jul2016_Run2016C_PromptReco_repro  -s hadd -i l1loose__ICHEPjson__EpTCorr__fakeSel -S Target -b
./mkGardener.py -p 15Jul2016_Run2016C_PromptReco_repro  -s 3jetsSel -i l1loose__ICHEPjson__EpTCorr -S Target -b
./mkGardener.py -p 15Jul2016_Run2016C_PromptReco_repro  -s hadd -i l1loose__ICHEPjson__EpTCorr__3jetsSel -S Target -b
./mkGardener.py -p 15Jul2016_Run2016C_PromptReco_repro  -s hadd -i l1loose__ICHEPjson__EpTCorr -S Target -b

./mkGardener.py -p 15Jul2016_Run2016C_PromptReco_repro  -s l2loose -S Target -b
./mkGardener.py -p 15Jul2016_Run2016C_PromptReco_repro  -s hadd -i l2loose -S Target -b
./mkGardener.py -p 15Jul2016_Run2016C_PromptReco_repro  -s ICHEPjson -i l2loose__hadd -S Target -b
./mkGardener.py -p 15Jul2016_Run2016C_PromptReco_repro  -s EpTCorr,l2tight,wwSel -i l2loose__hadd__ICHEPjson -S Target -b -C
./mkGardener.py -p 15Jul2016_Run2016C_PromptReco_repro  -s vh3lSel -i l2loose__hadd__ICHEPjson__EpTCorr__l2tight -S Target -b



./mkGardener.py -p 11Jul2016_Run2016C_PromptReco_repro  -s WgStarsel -S Target -b
./mkGardener.py -p 11Jul2016_Run2016C_PromptReco_repro  -s hadd -i WgStarsel -S Target -b
./mkGardener.py -p 11Jul2016_Run2016C_PromptReco_repro  -s ICHEPjson -i WgStarsel__hadd -S Target -b
./mkGardener.py -p 11Jul2016_Run2016C_PromptReco_repro  -s EpTCorr -i WgStarsel__hadd__ICHEPjson -S Target -b

./mkGardener.py -p 11Jul2016_Run2016C_PromptReco_repro  -s l1loose -S Target -b
./mkGardener.py -p 11Jul2016_Run2016C_PromptReco_repro  -s ICHEPjson -i l1loose -S Target -b
./mkGardener.py -p 11Jul2016_Run2016C_PromptReco_repro  -s EpTCorr -i l1loose__ICHEPjson -S Target -b
./mkGardener.py -p 11Jul2016_Run2016C_PromptReco_repro  -s fakeSel -i l1loose__ICHEPjson__EpTCorr -S Target -b
./mkGardener.py -p 11Jul2016_Run2016C_PromptReco_repro  -s hadd -i l1loose__ICHEPjson__EpTCorr__fakeSel -S Target -b
./mkGardener.py -p 11Jul2016_Run2016C_PromptReco_repro  -s 3jetsSel -i l1loose__ICHEPjson__EpTCorr -S Target -b
./mkGardener.py -p 11Jul2016_Run2016C_PromptReco_repro  -s hadd -i l1loose__ICHEPjson__EpTCorr__3jetsSel -S Target -b
./mkGardener.py -p 11Jul2016_Run2016C_PromptReco_repro  -s hadd -i l1loose__ICHEPjson__EpTCorr -S Target -b

./mkGardener.py -p 11Jul2016_Run2016C_PromptReco_repro  -s l2loose -S Target -b
./mkGardener.py -p 11Jul2016_Run2016C_PromptReco_repro  -s hadd -i l2loose -S Target -b
./mkGardener.py -p 11Jul2016_Run2016C_PromptReco_repro  -s ICHEPjson -i l2loose__hadd -S Target -b
./mkGardener.py -p 11Jul2016_Run2016C_PromptReco_repro  -s EpTCorr,l2tight,wwSel -i l2loose__hadd__ICHEPjson -S Target -b -C
./mkGardener.py -p 11Jul2016_Run2016C_PromptReco_repro  -s vh3lSel -i l2loose__hadd__ICHEPjson__EpTCorr__l2tight -S Target -b

# Extra Selection:

./mkGardener.py -p 08Jul2016_Run2016C_PromptReco_repro  -s topSel -i l2loose__hadd__EpTCorr__l2tight -S Target -b
./mkGardener.py -p 08Jul2016_Run2016B_PromptReco_repro  -s topSel -i l2loose__hadd__EpTCorr__l2tight -S Target -b
./mkGardener.py -p 05Jul2016_Run2016B_PromptReco_repro  -s topSel -i l2loose__hadd__EpTCorr__l2tight -S Target -b 
./mkGardener.py -p 21Jun2016_Run2016B_PromptReco_repro  -s topSel -i l2loose__hadd__EpTCorr__l2tight -S Target -b
./mkGardener.py -p 21Jun2016_v2_Run2016B_PromptReco_repro  -s topSel -i l2loose__hadd__EpTCorr__l2tight -S Target -b
./mkGardener.py -p 26Jul2016_Run2016D_PromptReco_repro  -s topSel -i l2loose__hadd__ICHEPjson__EpTCorr__l2tight -S Target -b
./mkGardener.py -p 15Jul2016_Run2016D_PromptReco_repro  -s topSel -i l2loose__hadd__ICHEPjson__EpTCorr__l2tight -S Target -b
./mkGardener.py -p 15Jul2016_Run2016C_PromptReco_repro  -s topSel -i l2loose__hadd__ICHEPjson__EpTCorr__l2tight -S Target -b
./mkGardener.py -p 11Jul2016_Run2016C_PromptReco_repro  -s topSel -i l2loose__hadd__ICHEPjson__EpTCorr__l2tight -S Target -b

./mkGardener.py -p 08Jul2016_Run2016C_PromptReco_repro  -s sfSel -i l2loose__hadd__EpTCorr__l2tight -S Target -b
./mkGardener.py -p 08Jul2016_Run2016B_PromptReco_repro  -s sfSel -i l2loose__hadd__EpTCorr__l2tight -S Target -b
./mkGardener.py -p 05Jul2016_Run2016B_PromptReco_repro  -s sfSel -i l2loose__hadd__EpTCorr__l2tight -S Target -b
./mkGardener.py -p 21Jun2016_Run2016B_PromptReco_repro  -s sfSel -i l2loose__hadd__EpTCorr__l2tight -S Target -b
./mkGardener.py -p 21Jun2016_v2_Run2016B_PromptReco_repro  -s sfSel -i l2loose__hadd__EpTCorr__l2tight -S Target -b
./mkGardener.py -p 26Jul2016_Run2016D_PromptReco_repro  -s sfSel -i l2loose__hadd__ICHEPjson__EpTCorr__l2tight -S Target -b
./mkGardener.py -p 15Jul2016_Run2016D_PromptReco_repro  -s sfSel -i l2loose__hadd__ICHEPjson__EpTCorr__l2tight -S Target -b
./mkGardener.py -p 15Jul2016_Run2016C_PromptReco_repro  -s sfSel -i l2loose__hadd__ICHEPjson__EpTCorr__l2tight -S Target -b
./mkGardener.py -p 11Jul2016_Run2016C_PromptReco_repro  -s sfSel -i l2loose__hadd__ICHEPjson__EpTCorr__l2tight -S Target -b

./mkGardener.py -p 08Jul2016_Run2016C_PromptReco_repro  -s wh2lss1jSel -i l2loose__hadd__EpTCorr__l2tight -S Target -b
./mkGardener.py -p 08Jul2016_Run2016B_PromptReco_repro  -s wh2lss1jSel -i l2loose__hadd__EpTCorr__l2tight -S Target -b
./mkGardener.py -p 05Jul2016_Run2016B_PromptReco_repro  -s wh2lss1jSel -i l2loose__hadd__EpTCorr__l2tight -S Target -b
./mkGardener.py -p 21Jun2016_v2_Run2016B_PromptReco_repro  -s wh2lss1jSel -i l2loose__hadd__EpTCorr__l2tight -S Target -b
./mkGardener.py -p 26Jul2016_Run2016D_PromptReco_repro  -s wh2lss1jSel -i l2loose__hadd__ICHEPjson__EpTCorr__l2tight -S Target -b
./mkGardener.py -p 15Jul2016_Run2016D_PromptReco_repro  -s wh2lss1jSel -i l2loose__hadd__ICHEPjson__EpTCorr__l2tight -S Target -b
./mkGardener.py -p 15Jul2016_Run2016C_PromptReco_repro  -s wh2lss1jSel -i l2loose__hadd__ICHEPjson__EpTCorr__l2tight -S Target -b
./mkGardener.py -p 11Jul2016_Run2016C_PromptReco_repro  -s wh2lss1jSel -i l2loose__hadd__ICHEPjson__EpTCorr__l2tight -S Target -b

./mkGardener.py -p 08Jul2016_Run2016C_PromptReco_repro  -s vbsSel -i l2loose__hadd__EpTCorr__l2tight -S Target -b
./mkGardener.py -p 08Jul2016_Run2016B_PromptReco_repro  -s vbsSel -i l2loose__hadd__EpTCorr__l2tight -S Target -b
./mkGardener.py -p 05Jul2016_Run2016B_PromptReco_repro  -s vbsSel -i l2loose__hadd__EpTCorr__l2tight -S Target -b
./mkGardener.py -p 21Jun2016_Run2016B_PromptReco_repro  -s vbsSel -i l2loose__hadd__EpTCorr__l2tight -S Target -b
./mkGardener.py -p 21Jun2016_v2_Run2016B_PromptReco_repro  -s vbsSel -i l2loose__hadd__EpTCorr__l2tight -S Target -b
./mkGardener.py -p 26Jul2016_Run2016D_PromptReco_repro  -s vbsSel -i l2loose__hadd__ICHEPjson__EpTCorr__l2tight -S Target -b
./mkGardener.py -p 15Jul2016_Run2016D_PromptReco_repro  -s vbsSel -i l2loose__hadd__ICHEPjson__EpTCorr__l2tight -S Target -b
./mkGardener.py -p 15Jul2016_Run2016C_PromptReco_repro  -s vbsSel -i l2loose__hadd__ICHEPjson__EpTCorr__l2tight -S Target -b
./mkGardener.py -p 11Jul2016_Run2016C_PromptReco_repro  -s vbsSel -i l2loose__hadd__ICHEPjson__EpTCorr__l2tight -S Target -b

./mkGardener.py -p 08Jul2016_Run2016C_PromptReco_repro  -s dymvaGGH -i l2loose__hadd__EpTCorr__l2tight -S Target -b
./mkGardener.py -p 08Jul2016_Run2016B_PromptReco_repro  -s dymvaGGH -i l2loose__hadd__EpTCorr__l2tight -S Target -b
./mkGardener.py -p 05Jul2016_Run2016B_PromptReco_repro  -s dymvaGGH -i l2loose__hadd__EpTCorr__l2tight -S Target -b
./mkGardener.py -p 21Jun2016_Run2016B_PromptReco_repro  -s dymvaGGH -i l2loose__hadd__EpTCorr__l2tight -S Target -b
./mkGardener.py -p 21Jun2016_v2_Run2016B_PromptReco_repro  -s dymvaGGH -i l2loose__hadd__EpTCorr__l2tight -S Target -b
./mkGardener.py -p 26Jul2016_Run2016D_PromptReco_repro  -s dymvaGGH -i l2loose__hadd__ICHEPjson__EpTCorr__l2tight -S Target -b
./mkGardener.py -p 15Jul2016_Run2016D_PromptReco_repro  -s dymvaGGH -i l2loose__hadd__ICHEPjson__EpTCorr__l2tight -S Target -b
./mkGardener.py -p 15Jul2016_Run2016C_PromptReco_repro  -s dymvaGGH -i l2loose__hadd__ICHEPjson__EpTCorr__l2tight -S Target -b
./mkGardener.py -p 11Jul2016_Run2016C_PromptReco_repro  -s dymvaGGH -i l2loose__hadd__ICHEPjson__EpTCorr__l2tight -S Target -b

