Tools
====

Creation of histograms. It should be used both for plotting purposes and for datacard creation

    mkShape.py

    mkPlot.py

    mkDatacards.py


To transform the output of combine into the input of mkPlot to have the post-fit histograms

    combine -M MaxLikelihoodFit ddatacard.txt -n mytest --saveShapes --saveNormalizations --saveWithUncertainties

    mkPostFitPlot.py
    
then you still need to run mkPlot.py to have the plots.


Easy descriptor:
expand samples.py into something human readable

    easyDescription.py
    
    
Morphing of the histograms for nuisances (removing unwanted fluctuations)

    mkChainSaw.py --pycfg=configuration.py 
    
