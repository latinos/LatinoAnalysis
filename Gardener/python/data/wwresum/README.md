NNLO + NNLL resummed calculations
====

Get root file from Rafael, from Hari and Meade.

Convert the root file into a txt file:

    root -l -q HistoToText.cxx
    
Apply the 

    gardener.py wwNLLcorrections \
       --cmssw=74x   \
       /tmp/amassiro/latino_WWTo2L2Nu.root \
       output.root

    gardener.py wwNLLcorrections \
       --cmssw=763   \
       ../LatinoTrees/AnalysisStep/test/latino_stepB_numEvent100.root \
       output.root
           



