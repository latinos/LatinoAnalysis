Tools
====

Creation of histograms. It should be used both for plotting purposes and for datacard creation

    mkShape.py

    mkPlot.py

    mkDatacards.py


To transform the output of combine into the input of mkPlot to have the post-fit histograms

    combine -M MaxLikelihoodFit ddatacard.txt -n mytest --saveShapes --saveNormalizations

    mkPostFitPlot.py
    
then you still need to run mkPlot.py to have the plots.

