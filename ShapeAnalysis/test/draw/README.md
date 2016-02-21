Simple scripts for super-fast plots
====

Compare two samples, normalized to 1:

    r99t file1.root file2.root DrawCompare.cxx\(\"variable\", nBin, min, max, weightAndCut\)

Plot PDF and QCD scale variation distributions:

    r99t file1.root DrawPDF.cxx\(\"variable\", nBin, min, max, weightAndCut\)
    
    
Example:

    r99t /media/data/amassiro/LatinoTrees/Moriond/MCl2loose__hadd__bSFL2pTEff__l2tight/latino_GluGluHToWWTo2L2Nu_M124.root  \
         DrawPDF.cxx\(\"mll\",10,0,100,\"std_vector_lepton_pt[1]\>15\"\)

    r99t /media/data/amassiro/LatinoTrees/Moriond/MCl2loose__hadd__bSFL2pTEff__l2tight/latino_GluGluHToWWTo2L2Nu_M124.root  \
         DrawPDF.cxx\(\"mll\",10,0,100,\"std_vector_lepton_pt[1]\>15\",90\)
         
    
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
    
    