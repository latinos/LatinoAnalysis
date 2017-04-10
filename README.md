The latinos framework is roughly divided in three parts.

# 1. Read miniAOD

The code used to read and analyse miniAOD is documented here,

    https://github.com/latinos/LatinoTrees/tree/master/AnalysisStep/test

We produce simple ROOT trees from the data and MC miniAOD datasets. To limit the size of the trees we require the events to have at least one lepton that passes a very loose ID requirement.

# 2. Latino trees post-processing

As calibrations, efficiencies, NLO weights, etc, are often coming a bit late, we have a second processing step based on the previous trees, that allows us to modify the 4-vectors of objects (like leptons and jets) and recompute event kinematics, plugin efficiencies, add weights. This same post-processing is used to apply systematics like scale uncertainties (leptons, MET, jets) that require to modify the 4-vectors of objects. Once we have all the outputs of the second step we derive skimmed ROOT trees applying different selections, to reduce the size as deemed for a given analysis. The code used at this level is documented here,

    https://github.com/latinos/LatinoAnalysis/tree/master/Gardener

# 3. Analysis

The following python code is used to produce plots, study backgrounds and produce data cards for computing significance and limits,

    https://github.com/latinos/PlotsConfigurations

As a starting point one can try this WW configuration,

    https://github.com/latinos/PlotsConfigurations/tree/master/Configurations/ControlRegions/WW/Full2016

The first step reads the post-processed latino trees and produces histograms for several variables and phase spaces,

    mkShapes.py --pycfg=configuration.py \
                --inputDir=/eos/cms/store/group/phys_higgs/cmshww/amassiro/Full2016/Feb2017_summer16/MCl2looseCut__hadd__bSFL2pTEffCut__l2tight \
                --batchSplit=Cuts,Samples \
                --doBatch=True \
                --batchQueue=8nh
                
    mkBatch.py --status

Once the previous jobs have finished we hadd the outputs,

    mkShapes.py --pycfg=configuration.py \
                --inputDir=/eos/cms/store/group/phys_higgs/cmshww/amassiro/Full2016/Feb2017_summer16/MCl2looseCut__hadd__bSFL2pTEffCut__l2tight \
                --batchSplit=Cuts,Samples \
                --doHadd=True

Now we are ready to make data/MC comparison plots,

    mkPlot.py --inputFile=rootFile/plots_WW.root \
              --showIntegralLegend=1
              
To move or copy the plots to the web,

    mkdir $HOME/www/latino
    pushd $HOME/www/latino
    wget https://raw.githubusercontent.com/latinos/PlotsConfigurations/master/index.php
    popd
    cp plotWW/*png $HOME/www/latino/.
    
Time to check and share the results.

    https://piedra.web.cern.ch/piedra/latino/

# 4. Tutorials

In the twiki below we have documented the tutorials that have been written for different pieces of the latino framework.

    https://twiki.cern.ch/twiki/bin/view/CMS/LatinosFrameworkTutorials
