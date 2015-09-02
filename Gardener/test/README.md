Example
====

Here we add a new variable in a latino tree. It works on the trees produced with the `cmssw2latino.py` script.

    scram b -j 10    

    gardener.py adder \
                -v 'test1/F=ch1*ch2' \
                input.root output.root


How to filter events:

    gardener.py  filter \
                -f "njet>=2"
                -r   /media/data/amassiro/LatinoTrees/25ns/05Aug2015/  \
                     /media/data/amassiro/LatinoTrees/WW/

                     
How to filter events and update some collections:

    gardener.py  l2selfiller \
                -r   /media/data/amassiro/LatinoTrees/25ns/05Aug2015/  \
                     /media/data/amassiro/LatinoTrees/WW/
                    
    gardener.py  l2selfiller \
                /media/data/amassiro/LatinoTrees/50ns/05Aug2015/latino_WWTo2L2Nu.root  \
                /media/data/amassiro/LatinoTrees/WW/50ns/latino_WW_TEST.root
                     

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
    gardener.py xwwvarfiller  \
          -r  /home/amassiro/Latinos/data  \
          ./TEST/

          
          
          
          
          
    gardener.py  l2selfiller \
                -r   /media/data/amassiro/LatinoTrees/25ns/05Aug2015/  \
                     /media/data/amassiro/LatinoTrees/WW/25ns/05Aug2015/ 
         
    gardener.py  l2selfiller \
                -r   /media/data/amassiro/LatinoTrees/50ns/05Aug2015/  \
                     /media/data/amassiro/LatinoTrees/WW/50ns/05Aug2015/ 

    gardener.py  l2selfiller \
                -r   /media/data/amassiro/LatinoTrees/data/  \
                     /media/data/amassiro/LatinoTrees/WW/data/ 
                     
          
puW

    # get data pu distribution
    
    pileupCalc.py \
       -i /afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions15/13TeV/Cert_246908-251883_13TeV_PromptReco_Collisions15_JSON_v2.txt \
       --inputLumiJSON=/afs/cern.ch/user/a/amassiro/public/RunII/pujson.txt \
       --calcMode=true --minBiasXsec=70000 \
       --maxPileupBin=80   \
       --numPileupBins=80  \
       testPUDATA.root

       
    # get MC pu distribution
    
    r99t /media/data/amassiro/LatinoTrees/50ns/05Aug2015/latino_DYJetsToLL_M-50.root
    TH1F pileup("pileup","pileup", 80, 0, 80);
    latino->Draw("trpu >> pileup");
    pileup.SaveAs("MCpu.root");
       
    # add pu weight
    gardener.py  puadder \
       /media/data/amassiro/LatinoTrees/WW/25ns/05Aug2015/latino_WZ.root \
       test.root \
       --mc=MCpu.root    \
       --data=testPUDATA.root   \
       --HistName=pileup   \
       --branch=puW  \
       --kind=trpu   
           
    gardener.py  puadder \
       -r /media/data/amassiro/LatinoTrees/WW/25ns/05Aug2015  \
       /media/data/amassiro/LatinoTrees/WW/25ns/05Aug2015_puW \
       --mc=MCpu.root    \
       --data=testPUDATA.root   \
       --HistName=pileup   \
       --branch=puW  \
       --kind=trpu   
           
    gardener.py  puadder \
       -r /media/data/amassiro/LatinoTrees/WW/50ns/05Aug2015  \
       /media/data/amassiro/LatinoTrees/WW/50ns/05Aug2015_puW \
       --mc=MCpu.root    \
       --data=testPUDATA.root   \
       --HistName=pileup   \
       --branch=puW  \
       --kind=trpu   
           


Trigger efficiency

           effwfiller
          
    gardener.py  effwfiller \
       /media/data/amassiro/LatinoTrees/WW/50ns/05Aug2015/latino_WZ.root   \
       test.root \
       --isoid=data/isoidScaleFactors.py
       
       
       
       
    gardener.py  effwfiller \
       -r /media/data/amassiro/LatinoTrees/WW/50ns/05Aug2015  \
       /media/data/amassiro/LatinoTrees/WW/50ns/05Aug2015_puW \
       --isoid=data/isoidScaleFactors.py
          
          
          
          
          
          
          
          
          