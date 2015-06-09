Simple scripts for super-fast plots
====

Compare two samples, normalized to 1

    r99t file1.root file2.root DrawCompare.cxx\(\"variable\", nBin, min, max, weightAndCut\)
    
    
Example:

    
    r99t ../../../../LatinoTrees/AnalysisStep/test/latino_stepB_MC_50ns.root \
         ../../../../LatinoTrees/AnalysisStep/test/latino_stepB_MC_25ns.root \
         DrawCompare.cxx\(\"std_vector_lepton_pt[0]\",10,0,100\)
    
    muons
    r99t ../../../../LatinoTrees/AnalysisStep/test/latino_stepB_MC_50ns.root \
         ../../../../LatinoTrees/AnalysisStep/test/latino_stepB_MC_25ns.root \
         DrawCompare.cxx\(\"std_vector_lepton_pt[0]\",10,0,100,\"std_vector_lepton_id[0]==13\|\|std_vector_lepton_id[0]==-13\"\)
    
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
    
    