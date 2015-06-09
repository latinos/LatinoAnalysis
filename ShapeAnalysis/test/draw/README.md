Simple scripts for super-fast plots
====

Compare two samples, normalized to 1

    r99t file1.root file2.root DrawCompare.cxx\(\"variable\", nBin, min, max, weightAndCut\)
    
    
Example:

    
    r99t ../../../../LatinoTrees/AnalysisStep/test/latino_stepB_MC_50ns.root \
         ../../../../LatinoTrees/AnalysisStep/test/latino_stepB_MC_25ns.root \
         DrawCompare.cxx\(\"std_vector_lepton_pt[0]\",10,0,100\)
    
    
    
    