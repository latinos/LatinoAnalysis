The latinos framework is roughly divided in three parts.

# 1. Read miniAOD

The code used to read and analyse miniAOD is documented here,

    https://github.com/latinos/LatinoTrees/tree/master/AnalysisStep/test

We produce simple ROOT trees from the data and MC miniAOD datasets. To limit the size of the trees we require the events to have at least one lepton that passes a very loose ID requirement.

# 2. Latino trees post-processing

As calibrations, efficiencies, NLO weights, etc, are often coming a bit late, we have a second processing step based on the previous trees that allows us to modify the 4-vectors of objects and recompute event kinematics, plugin efficiencies, add any weights. This same post-processing is used to apply systematic uncertainties like scale uncertainties (lepton, MET, jets) that require to modify 4-vectors of objects. Once we have all the outputs of the second step, we can also derive skimmed ROOT trees applying different selections, to reduce the size as deemed for a given analysis. The code used at this level is documented here,

    https://github.com/latinos/LatinoAnalysis/tree/master/Gardener

# 3. Draw / analyse

We have some python code that is used to produce plots, study backgrounds & produce data cards for computing significance et al,

    https://github.com/latinos/PlotsConfigurations

One can try the following configuration,

    https://github.com/latinos/PlotsConfigurations/tree/master/Configurations/ControlRegions/WW/Full2016

    mkShapes.py --pycfg=configuration.py \
                --inputDir=/eos/cms/store/group/phys_higgs/cmshww/amassiro/Full2016/Feb2017_summer16/MCl2looseCut__hadd__bSFL2pTEffCut__l2tight \
                --batchSplit=Cuts,Samples \
                --doBatch=True

Once these jobs have finished,

    mkShapes.py --pycfg=configuration.py \
                --inputDir=/eos/cms/store/group/phys_higgs/cmshww/amassiro/Full2016/Feb2017_summer16/MCl2looseCut__hadd__bSFL2pTEffCut__l2tight \
                --batchSplit=Cuts,Samples \
                --doHadd=True

Finally,

    mkPlot.py --inputFile=rootFile/plots_WW.root \
              --showIntegralLegend=1

# 4. Tutorials

    https://twiki.cern.ch/twiki/bin/view/CMS/LatinosFrameworkTutorials
