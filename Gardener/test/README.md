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
              
              
    scp amassiro@cmsneu.cern.ch:/media/data/amassiro/LatinoTrees/25ns/21Oct2015/mcwghtcount__MC__l2sel/latino_GluGluHToWWTo2L2Nu_M125.root /tmp/amassiro/          
    scp amassiro@cmsneu.cern.ch:/media/data/amassiro/LatinoTrees/25ns/21Oct2015/mcwghtcount__MC__l2sel/latino_WZTo3LNu.root /tmp/amassiro/          
    
    gardener.py  l2selfiller \
                /tmp/amassiro/latino_GluGluHToWWTo2L2Nu_M125.root  \
                /tmp/amassiro/latino_GluGluHToWWTo2L2Nu_M125_TEST.root

    gardener.py  l2selfiller \
                --kind 2 \
                /tmp/amassiro/latino_WZTo3LNu.root  \
                /tmp/amassiro/latino_WZTo3LNu_TEST.root

                -k 2
                --kind 2 

    gardener.py  l2selfiller \
                --kind 3 \
                /tmp/amassiro/latino_WZTo3LNu.root  \
                /tmp/amassiro/latino_WZTo3LNu_TEST.root

                
    scp amassiro@cmsneu.cern.ch:/media/data/amassiro/LatinoTrees/50ns/17Sep2015/25ns/mc/latino_WWTo2L2Nu.root /tmp/amassiro/
    gardener.py  l2selfiller \
                /tmp/amassiro/latino_WWTo2L2Nu.root  \
                /tmp/amassiro/latino_WW_TEST.root
                     
    gardener.py  l2selfiller \
                --cmssw=763   \
                ../LatinoTrees/AnalysisStep/test/latino_stepB_numEvent100.root  \
                test.root

    gardener.py  l2selfiller \
                --kind 2 \
                --cmssw=763   \
                ../LatinoTrees/AnalysisStep/test/latino_stepB_numEvent100.root  \
                test.2.root

    gardener.py  l2selfiller \
                --kind 3 \
                --cmssw=763   \
                ../LatinoTrees/AnalysisStep/test/latino_stepB_numEvent100.root  \
                test.3.root

    gardener.py  l2selfiller \
                --kind 1 \
                --cmssw=763   \
                ../LatinoTrees/AnalysisStep/test/latino_stepB_numEvent100.root  \
                test.1.root
                
                
    gardener.py  l2selfiller \
                --kind 2 \
                --cmssw=763   \
                --selection=1   \
                ../LatinoTrees/AnalysisStep/test/latino_stepB_numEvent100.root  \
                test.root

                
                
Specific modules example:

    gardener.py mcweightsfiller \
                ../../../LatinoTrees/AnalysisStep/test/latino_stepB_MC_numEvent200.root \
                output.root


    gardener.py dymvaVarFiller \
                ../../../LatinoTrees/AnalysisStep/test/latino_stepB_Data_numEvent100.root \
                output.root

                
    gardener.py wwvarfiller \
                ../../../LatinoTrees/AnalysisStep/test/latino_stepB_MC_numEvent200.root \
                output.root

    gardener.py tlorentzvectorfiller \
                -v 'TLlep=std_variable_vector_ton_pt,std_variable_vector_lepton_eta,std_variable_vector_lepton_phi' \
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

          
          
    gardener.py  muccaMvaVarFiller \
                ../LatinoTrees/AnalysisStep/test/latino_stepB_MC_numEvent200.root  \
                test.root

    gardener.py  muccaMvaVarFiller \
                test.root \
                test2.root

    gardener.py  muccaMvaVarFiller \
                --kind 2 \
                test.root \
                test2.root

    
          
          
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
====

get data pu distribution
    
    pileupCalc.py \
       -i /afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions15/13TeV/Cert_246908-251883_13TeV_PromptReco_Collisions15_JSON_v2.txt \
       --inputLumiJSON=/afs/cern.ch/user/a/amassiro/public/RunII/pujson.txt \
       --calcMode=true --minBiasXsec=70000 \
       --maxPileupBin=80   \
       --numPileupBins=80  \
       testPUDATA.root

       
get MC pu distribution
    
    r99t /media/data/amassiro/LatinoTrees/50ns/05Aug2015/latino_DYJetsToLL_M-50.root
    TH1F pileup("pileup","pileup", 80, 0, 80);
    latino->Draw("trpu >> pileup");
    pileup.SaveAs("MCpu.root");
 
New way to get MC pu from MC directly from supporting trees:

    r99t ../../LatinoTrees/AnalysisStep/test/latino_stepB_MC_numEvent200.root
    TH1F pileup("pileup","pileup", 80, 0, 80);
    pu->Draw("trpu >> pileup");
    pileup.SaveAs("MCpu.root");
 
add pu weight

NB: if you don't give the "mcfile" (--mc) the tree with pu information stored within the root file will be used
This is automatic and better, since it will exploit direclty the distribution used to generate that particular samples.


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
      latino_stepB_MC_numEvent200.root  \
      latino_stepB_MC_numEvent200_test.root \
      --data=testPUDATA.root   \
       --HistName=pileup   \
       --branch=puW  \
       --kind=trpu   
           
           

Lepton pT corrector
====

    gardener.py letPtCorrector  ../LatinoTrees/AnalysisStep/test/latino_stepB_numEvent100.root testCorr.root
    
    gardener.py letPtCorrector --isData=0 \
         ../LatinoTrees/AnalysisStep/test/latino_stepB_numEvent100.root testCorr.root
    
    gardener.py letPtCorrector --isData=1 \
         ../LatinoTrees/AnalysisStep/test/latino_stepB_numEvent100_data.root testCorr.root


Fake weight adder
====

    gardener.py fakeWeights input.root output.root


WW NNLO+NNLL scales and uncertainty
====

    scp amassiro@cmsneu.cern.ch:/media/data/amassiro/LatinoTrees/21Oct_25ns_MC/mcwghtcount__MC__l2selFix__hadd__bSFL2Eff/latino_WWTo2L2Nu.root  /tmp/amassiro/
           
    gardener.py wwEWKcorrections \
       ../LatinoTrees/AnalysisStep/test/latino_stepB_numEvent100.root \
       output.root
    
    gardener.py wwEWKcorrections \
       /tmp/amassiro/latino_WWTo2L2Nu.root \
       output.root

       
     

WW EWK corrections
====

    scp amassiro@cmsneu.cern.ch:/media/data/amassiro/LatinoTrees/21Oct_25ns_MC/mcwghtcount__MC__l2selFix__hadd__bSFL2Eff/latino_WWTo2L2Nu.root  /tmp/amassiro/
           
    gardener.py wwNLLcorrections \
       --cmssw=763   \
       ../LatinoTrees/AnalysisStep/test/latino_stepB_numEvent100.root \
       output.root
    
    gardener.py wwNLLcorrections \
       /tmp/amassiro/latino_WWTo2L2Nu.root \
       output.root

    

    
       
Trigger efficiency
====

Module: efftfiller
     
    gardener.py  efftfiller    input.root output.root

           
Id/isolation scale factors
====

Module: idisofiller
          
    gardener.py  idisofiller    input.root output.root
    
    
    
Kinematic variables
====
    
    gardener.py l2kinfiller --cmssw=763    input.root output.root
    gardener.py l2kinfiller                input.root output.root


Jet Energy Scale
====

Module: JESTreeMaker
          
    gardener.py  JESTreeMaker \
       -k 1 \
       /media/data/amassiro/LatinoTrees/WW/50ns/05Aug2015/latino_WZ.root   \
       test.root \      
       
       
    cp ../CMSSW_7_6_2/src/LatinoTrees/AnalysisStep/test/latino_stepB_numEvent100.root    /tmp/amassiro/latino_WWTo2L2Nu.root
    gardener.py  JESTreeMaker \
                -k -1 \
                /tmp/amassiro/latino_WWTo2L2Nu.root  \
                /tmp/amassiro/latino_WW_TEST.root
                           
    gardener.py  JESTreeMaker \
       -k -1 \
       -r /media/data/amassiro/LatinoTrees/WW/50ns/05Aug2015  \
       /media/data/amassiro/LatinoTrees/WW/50ns/05Aug2015_JES \
          
          
b POG scale factors
====

Module: btagPogScaleFactors 

    gardener.py  btagPogScaleFactors \
       /media/data/amassiro/LatinoTrees/WW/50ns/05Aug2015/latino_WZ.root   \
       test.root \


    gardener.py  btagPogScaleFactors \
       -r /media/data/amassiro/LatinoTrees/WW/50ns/05Aug2015  \
       /media/data/amassiro/LatinoTrees/WW/50ns/05Aug2015_puW \          

this module needs to run after l2sel, because it needs the real jets in the event.
The module adds to the trees two sets of weights, one based on the POG provided SF, one based on our Tag and Probe method.
The POG SF are contained in branch named `bPogSF*`, while the Tag & Probe Scale factors are called `bTPSF*`. 

The `bTPSF*` are currently placeholders and their value is 1.


Lepton pT scale uncertainty
====

    gardener.py LeppTScalerTreeMaker -v 1 -k mu  ../LatinoTrees/AnalysisStep/test/latino_stepB_numEvent100.root testscalar.root
    
    
Lepton pT resolution uncertainty
====
    
    gardener.py leptonResolution ../LatinoTrees/AnalysisStep/test/latino_stepB_numEvent100.root     test.root


PDF uncertainty
====
    
    gardener.py pdfUncertainty ../LatinoTrees/AnalysisStep/test/latino_stepB_numEvent100.root     test.root


QCD uncertainty
====
    
    gardener.py qcdUncertainty ../LatinoTrees/AnalysisStep/test/latino_stepB_numEvent100.root     test.root


MET uncertainty
====

If reading 74x MET naming convention and available uncertainties.
    
    gardener.py metUncertainty --kind='Up' --cmssw='74x' input.root output.root
    gardener.py metUncertainty --kind='Dn' --cmssw='74x' input.root output.root

If reading 763 MET naming convention and full set of uncertainties.

    gardener.py metUncertainty --kind='Up' --cmssw='763' input.root output.root
    gardener.py metUncertainty --kind='Dn' --cmssw='763' input.root output.root

    
    
baseW table
====

Get the baseW table

    ls /media/data/amassiro/LatinoTrees/21Oct_25ns_MC/mcwghtcount__MC__l2selFix__hadd__bSFL2Eff/*.root | grep ".root" | awk '{print "root -l -q drawBasew.cxx\\\(\\\""$1"\\\"\\\)"}' | /bin/sh

    