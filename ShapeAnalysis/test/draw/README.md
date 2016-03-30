Compare nuisances
====

See the nuisances effect by means of plots.
On top of mkPlot.py code

    r99t DrawNuisances.cxx\(\"/afs/cern.ch/user/a/amassiro/Framework/CMSSW_7_6_3/src/PlotsConfigurations/Configurations/ggHMoriond/datacards/hww2l2v_13TeV_of0j/mllVSmth/shapes/histos_hww2l2v_13TeV_of0j.root\",\"histo_ggH_hww\",\"histo_ggH_hww_CMS_PSUp\",\"histo_ggH_hww_CMS_PSDown\"\)
    r99t DrawNuisances.cxx\(\"/afs/cern.ch/user/a/amassiro/Framework/CMSSW_7_6_3/src/PlotsConfigurations/Configurations/ggHMoriond/datacards/hww2l2v_13TeV_of0j/mllVSmth/shapes/histos_hww2l2v_13TeV_of0j.root\",\"histo_WW\",\"histo_WW_CMS_WWqscale0jUp\",\"histo_WW_CMS_WWqscale0jDown\"\)
    r99t DrawNuisances.cxx\(\"/afs/cern.ch/user/a/amassiro/Framework/CMSSW_7_6_3/src/PlotsConfigurations/Configurations/ggHMoriond/datacards/hww2l2v_13TeV_of0j/mllVSmth/shapes/histos_hww2l2v_13TeV_of0j.root\",\"histo_WW\",\"histo_WW_CMS_WWqscale0jUp\",\"histo_WW_CMS_WWqscale0jDown\"\)


Run on all:

    python DrawNuisancesAll.py
    python DrawNuisancesAll.py \
         --inputFile /afs/cern.ch/user/a/amassiro/Framework/CMSSW_7_6_3/src/PlotsConfigurations/Configurations/ggHMoriond/datacards/hww2l2v_13TeV_of0j/mllVSmth/shapes/histos_hww2l2v_13TeV_of0j.root  \
         --outputDirPlots ggH0j  \
         --nuisancesFile  /afs/cern.ch/user/a/amassiro/Framework/CMSSW_7_6_3/src/PlotsConfigurations/Configurations/ggH/nuisances.py  \
         --samplesFile    /afs/cern.ch/user/a/amassiro/Framework/CMSSW_7_6_3/src/PlotsConfigurations/Configurations/ggH/samples.py \
         --cutName hww2l2v_13TeV_of0j
    
    python DrawNuisancesAll.py \
         --inputFile /afs/cern.ch/user/a/amassiro/Framework/CMSSW_7_6_3/src/PlotsConfigurations/Configurations/ggHMoriond/datacards/hww2l2v_13TeV_of1j/mllVSmth/shapes/histos_hww2l2v_13TeV_of1j.root  \
         --outputDirPlots ggH1j  \
         --nuisancesFile  /afs/cern.ch/user/a/amassiro/Framework/CMSSW_7_6_3/src/PlotsConfigurations/Configurations/ggH/nuisances.py  \
         --samplesFile    /afs/cern.ch/user/a/amassiro/Framework/CMSSW_7_6_3/src/PlotsConfigurations/Configurations/ggH/samples.py \
         --cutName hww2l2v_13TeV_of1j
    
    
    python DrawNuisancesAll.py \
         --inputFile /afs/cern.ch/user/a/amassiro/Framework/CMSSW_7_6_3/src/PlotsConfigurations/Configurations/ggH/datacards/hww2l2v_13TeV_em_mp_0j/mllVSmth/shapes/histos_hww2l2v_13TeV_em_mp_0j.root  \
         --outputDirPlots ggH_em_mp_0j  \
         --nuisancesFile  /afs/cern.ch/user/a/amassiro/Framework/CMSSW_7_6_3/src/PlotsConfigurations/Configurations/ggH/nuisances.py  \
         --samplesFile    /afs/cern.ch/user/a/amassiro/Framework/CMSSW_7_6_3/src/PlotsConfigurations/Configurations/ggH/samples.py \
         --cutName hww2l2v_13TeV_em_mp_0j
    
    python DrawNuisancesAll.py \
         --inputFile /afs/cern.ch/user/a/amassiro/Framework/CMSSW_7_6_3/src/PlotsConfigurations/Configurations/ggH/datacards/hww2l2v_13TeV_em_pm_0j/mllVSmth/shapes/histos_hww2l2v_13TeV_em_pm_0j.root  \
         --outputDirPlots ggH_em_pm_0j  \
         --nuisancesFile  /afs/cern.ch/user/a/amassiro/Framework/CMSSW_7_6_3/src/PlotsConfigurations/Configurations/ggH/nuisances.py  \
         --samplesFile    /afs/cern.ch/user/a/amassiro/Framework/CMSSW_7_6_3/src/PlotsConfigurations/Configurations/ggH/samples.py \
         --cutName hww2l2v_13TeV_em_pm_0j
         
    
    python DrawNuisancesAll.py \
         --inputFile /afs/cern.ch/user/a/amassiro/Framework/CMSSW_7_6_3/src/PlotsConfigurations/Configurations/ggH/datacards/hww2l2v_13TeV_me_mp_0j/mllVSmth/shapes/histos_hww2l2v_13TeV_me_mp_0j.root  \
         --outputDirPlots ggH_me_mp_0j  \
         --nuisancesFile  /afs/cern.ch/user/a/amassiro/Framework/CMSSW_7_6_3/src/PlotsConfigurations/Configurations/ggH/nuisances.py  \
         --samplesFile    /afs/cern.ch/user/a/amassiro/Framework/CMSSW_7_6_3/src/PlotsConfigurations/Configurations/ggH/samples.py \
         --cutName hww2l2v_13TeV_me_mp_0j
    
    python DrawNuisancesAll.py \
         --inputFile /afs/cern.ch/user/a/amassiro/Framework/CMSSW_7_6_3/src/PlotsConfigurations/Configurations/ggH/datacards/hww2l2v_13TeV_me_pm_0j/mllVSmth/shapes/histos_hww2l2v_13TeV_me_pm_0j.root  \
         --outputDirPlots ggH_me_pm_0j  \
         --nuisancesFile  /afs/cern.ch/user/a/amassiro/Framework/CMSSW_7_6_3/src/PlotsConfigurations/Configurations/ggH/nuisances.py  \
         --samplesFile    /afs/cern.ch/user/a/amassiro/Framework/CMSSW_7_6_3/src/PlotsConfigurations/Configurations/ggH/samples.py \
         --cutName hww2l2v_13TeV_me_pm_0j
    
    
    
    
Simple scripts for super-fast plots
====

Compare two samples, normalized to 1:

    r99t file1.root file2.root DrawCompare.cxx\(\"variable\", nBin, min, max, weightAndCut\)

Plot PDF and QCD scale variation distributions:

    r99t file1.root DrawPDF.cxx\(\"variable\", nBin, min, max, weightAndCut\)
    
    
Example:

    r99t /media/data/amassiro/LatinoTrees/Moriond/MCl2loose__hadd__bSFL2pTEff__l2tight/latino_GluGluHToWWTo2L2Nu_M124.root  \
         DrawPDF.cxx\(\"mll\",10,0,100,\"std_vector_lepton_pt[1]\>15\"\)

    PDF variation
    r99t /media/data/amassiro/LatinoTrees/Moriond/MCl2loose__hadd__bSFL2pTEff__l2tight/latino_GluGluHToWWTo2L2Nu_M124.root  \
         DrawPDF.cxx\(\"mll\",20,12,200,\"std_vector_lepton_pt[1]\>15\",90\)

    r99t /media/data/amassiro/LatinoTrees/Moriond/MCl2loose__hadd__bSFL2pTEff__l2tight/latino_GluGluHToWWTo2L2Nu_M124.root  \
         DrawPDF.cxx\(\"mll\",20,12,200,\"mll\>12\&\&std_vector_lepton_pt[0]\>20\&\&std_vector_lepton_pt[1]\>10\&\&std_vector_lepton_pt[2]\<10\&\&metPfType1\>20\&\&ptll\>30\",90\)

    r99t /media/data/amassiro/LatinoTrees/Moriond/MCl2loose__hadd__bSFL2pTEff__l2tight/latino_GluGluHToWWTo2L2Nu_M124.root  \
         DrawPDF.cxx\(\"mth\",20,60,200,\"mll\>12\&\&std_vector_lepton_pt[0]\>20\&\&std_vector_lepton_pt[1]\>10\&\&std_vector_lepton_pt[2]\<10\&\&metPfType1\>20\&\&ptll\>30\",90\)

    r99t /media/data/amassiro/LatinoTrees/Moriond/MCl2loose__hadd__bSFL2pTEff__l2tight/latino_VBFHToWWTo2L2Nu_M125.root  \
         DrawPDF.cxx\(\"mth\",20,60,200,\"mll\>12\&\&std_vector_lepton_pt[0]\>20\&\&std_vector_lepton_pt[1]\>10\&\&std_vector_lepton_pt[2]\<10\&\&metPfType1\>20\&\&ptll\>30\",90\)
    
    r99t /media/data/amassiro/LatinoTrees/Moriond/MCl2loose__hadd__bSFL2pTEff__l2tight/latino_VBFHToWWTo2L2Nu_M125.root  \
         DrawPDF.cxx\(\"mth\",20,60,200,\"mll\>12\&\&std_vector_lepton_pt[0]\>20\&\&std_vector_lepton_pt[1]\>10\&\&std_vector_lepton_pt[2]\<10\&\&metPfType1\>20\&\&ptll\>30\",90,9,0\)
    
    QCD variation
    r99t /media/data/amassiro/LatinoTrees/Moriond/MCl2loose__hadd__bSFL2pTEff__l2tight/latino_GluGluHToWWTo2L2Nu_M124.root  \
         DrawPDF.cxx\(\"mll\",20,12,200,\"std_vector_lepton_pt[1]\>15\",9,1\)
    
    r99t /media/data/amassiro/LatinoTrees/Moriond/MCl2loose__hadd__bSFL2pTEff__l2tight/latino_GluGluHToWWTo2L2Nu_M124.root  \
         DrawPDF.cxx\(\"mll\",20,12,200,\"mll\>12\&\&std_vector_lepton_pt[0]\>20\&\&std_vector_lepton_pt[1]\>10\&\&std_vector_lepton_pt[2]\<10\&\&metPfType1\>20\&\&ptll\>30\",9,1\)
    
    r99t /media/data/amassiro/LatinoTrees/Moriond/MCl2loose__hadd__bSFL2pTEff__l2tight/latino_GluGluHToWWTo2L2Nu_M124.root  \
         DrawPDF.cxx\(\"mll\",20,12,200,\"std_vector_jet_pt[0]\<30\&\&mll\>12\&\&std_vector_lepton_pt[0]\>20\&\&std_vector_lepton_pt[1]\>10\&\&std_vector_lepton_pt[2]\<10\&\&metPfType1\>20\&\&ptll\>30\",9,1\)
    
    r99t /media/data/amassiro/LatinoTrees/Moriond/MCl2loose__hadd__bSFL2pTEff__l2tight/latino_GluGluHToWWTo2L2Nu_M124.root  \
         DrawPDF.cxx\(\"mth\",20,60,200,\"mll\>12\&\&std_vector_lepton_pt[0]\>20\&\&std_vector_lepton_pt[1]\>10\&\&std_vector_lepton_pt[2]\<10\&\&metPfType1\>20\&\&ptll\>30\",9,1\)
    
    r99t /media/data/amassiro/LatinoTrees/Moriond/MCl2loose__hadd__bSFL2pTEff__l2tight/latino_GluGluHToWWTo2L2Nu_M124.root  \
         DrawPDF.cxx\(\"mth\",20,60,200,\"std_vector_jet_pt[0]\<30\&\&mll\>12\&\&std_vector_lepton_pt[0]\>20\&\&std_vector_lepton_pt[1]\>10\&\&std_vector_lepton_pt[2]\<10\&\&metPfType1\>20\&\&ptll\>30\",9,1\)
    
    r99t /media/data/amassiro/LatinoTrees/Moriond/MCl2loose__hadd__bSFL2pTEff__l2tight/latino_VBFHToWWTo2L2Nu_M125.root  \
         DrawPDF.cxx\(\"mth\",20,60,200,\"std_vector_jet_pt[0]\<30\&\&mll\>12\&\&std_vector_lepton_pt[0]\>20\&\&std_vector_lepton_pt[1]\>10\&\&std_vector_lepton_pt[2]\<10\&\&metPfType1\>20\&\&ptll\>30\",9,1\)
    
    r99t ../../../../LatinoTrees/AnalysisStep/test/latino_stepB_MC_50ns.root \
         ../../../../LatinoTrees/AnalysisStep/test/latino_stepB_MC_25ns.root \
         DrawCompare.cxx\(\"std_vector_lepton_pt[0]\",10,0,100\)
    
    
    
    jets
    r99t ../../../../LatinoTrees/AnalysisStep/test/latino_stepB_MC_50ns.root \
         ../../../../LatinoTrees/AnalysisStep/test/latino_stepB_MC_25ns.root \
         DrawCompare.cxx\(\"std_vector_jet_pt[0]\",10,20,100\)
    
    r99t ../../../../LatinoTrees/AnalysisStep/test/latino_stepB_MC_50ns.root \
         ../../../../LatinoTrees/AnalysisStep/test/latino_stepB_MC_25ns.root \
         DrawCompare.cxx\(\"std_vector_jet_eta[0]\",20,-5,5\)
    
    r99t ../../../../LatinoTrees/AnalysisStep/test/latino_stepB_MC_50ns.root \
         ../../../../LatinoTrees/AnalysisStep/test/latino_stepB_MC_25ns.root \
         DrawCompare.cxx\(\"std_vector_jet_phi[0]\",20,-3.15,3.15\)
    
    
    muons
    r99t ../../../../LatinoTrees/AnalysisStep/test/latino_stepB_MC_50ns.root \
         ../../../../LatinoTrees/AnalysisStep/test/latino_stepB_MC_25ns.root \
         DrawCompare.cxx\(\"std_vector_lepton_pt[0]\",10,0,100,\"std_vector_lepton_id[0]==13\|\|std_vector_lepton_id[0]==-13\"\)
    
    r99t ../../../../LatinoTrees/AnalysisStep/test/latino_stepB_MC_50ns.root \
         ../../../../LatinoTrees/AnalysisStep/test/latino_stepB_MC_25ns.root \
         DrawCompare.cxx\(\"std_vector_lepton_eta[0]\",20,-3,3,\"std_vector_lepton_id[0]==13\|\|std_vector_lepton_id[0]==-13\"\)
    
    electrons
    r99t ../../../../LatinoTrees/AnalysisStep/test/latino_stepB_MC_50ns.root \
         ../../../../LatinoTrees/AnalysisStep/test/latino_stepB_MC_25ns.root \
         DrawCompare.cxx\(\"std_vector_lepton_pt[0]\",10,0,100,\"std_vector_lepton_id[0]==11\|\|std_vector_lepton_id[0]==-11\"\)
    
    r99t ../../../../LatinoTrees/AnalysisStep/test/latino_stepB_MC_50ns.root \
         ../../../../LatinoTrees/AnalysisStep/test/latino_stepB_MC_25ns.root \
         DrawCompare.cxx\(\"std_vector_lepton_eta[0]\",20,-3,3,\"std_vector_lepton_id[0]==11\|\|std_vector_lepton_id[0]==-11\"\)
    
    
    r99t ../../../../LatinoTrees/AnalysisStep/test/latino_stepB_MC_50ns.root \
         ../../../../LatinoTrees/AnalysisStep/test/latino_stepB_MC_25ns.root \
         DrawCompare.cxx\(\"std_vector_lepton_id[0]\",100,-30,30,\"std_vector_lepton_id[0]==13\|\|std_vector_lepton_id[0]==-13\"\)
    
    r99t ../../../../LatinoTrees/AnalysisStep/test/latino_stepB_MC_50ns.root \
         ../../../../LatinoTrees/AnalysisStep/test/latino_stepB_MC_25ns.root \
         DrawCompare.cxx\(\"std_vector_lepton_id[0]\",100,-30,30\)
    
    
    
    
    
    r99t /tmp/amassiro/eos/user/r/rebeca/HWW2015/22Jan_25ns_mAODv2_MC/MCl2loose__hadd__bSFL2pTEff__l2tight/latino_DYJetsToLL_M-50_0000__part0.root  \
         /tmp/amassiro/eos/user/r/rebeca/HWW2015/22Jan_25ns_mAODv2_MC/MCl2loose__hadd__bSFL2pTEff__l2tight/latino_DYJetsToLL_M-50-LO__part0.root  \
         DrawCompare.cxx\(\"ptll\",100,0,200,\"std_vector_lepton_pt[1]\>15\"\)
    
    