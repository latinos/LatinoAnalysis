Example
====

Here we add a new variable in a latino tree. It works on the trees produced with the `cmssw2latino.py` script.

    scram b -j 10    

    gardener.py adder \
                -v 'test1/F=ch1*ch2' \
                input.root output.root


Specific modules example:

    gardener.py wwvarfiller \
                ../../../LatinoTrees/AnalysisStep/test/latino_stepB_MC_numEvent200.root \
                output.root

    gardener.py tlorentzvectorfiller \
                -v 'TLlep=std_variable_vector_lepton_pt,std_variable_vector_lepton_eta,std_variable_vector_lepton_phi' \
                ../../../LatinoTrees/AnalysisStep/test/latino_stepB_MC_numEvent200.root \
                output.root

              
    gardener.py electronidfiller \
                ../../../LatinoTrees/AnalysisStep/test/latino_stepB_MC_numEvent200.root \
                output.root
    
    gardener.py wwNLLcorrections \
                -m 'powheg'  \
                ../../../LatinoTrees/AnalysisStep/test/latino_stepB_MC_50ns.root \
                output.root
    
        
    gardener.py dmvarfiller \
                ../../../LatinoTrees/AnalysisStep/test/latino_stepB_MC_50ns.root \
                output.root

    gardener.py xwwvarfiller \
                ../../../LatinoTrees/AnalysisStep/test/latino_stepB_MC_50ns.root \
                output.root
                