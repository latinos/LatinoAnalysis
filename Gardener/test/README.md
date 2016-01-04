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
                    
    scp amassiro@cmsneu.cern.ch:/media/data/amassiro/LatinoTrees/50ns/17Sep2015/25ns/mc/latino_WWTo2L2Nu.root /tmp/amassiro/
    gardener.py  l2selfiller \
                /tmp/amassiro/latino_WWTo2L2Nu.root  \
                /tmp/amassiro/latino_WW_TEST.root
                     
    gardener.py  l2selfiller \
                ../LatinoTrees/AnalysisStep/test/latino_stepB_MC_numEvent200.root  \
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
           
           
           

Lepton id/iso scale factors
====

Module: effwfiller
          
    gardener.py  effwfiller \
       /media/data/amassiro/LatinoTrees/WW/50ns/05Aug2015/latino_WZ.root   \
       test.root \
       --isoid=/afs/cern.ch/work/a/amassiro/Latinos/Framework/CMSSW_7_4_7/python/LatinoAnalysis/Gardener/data/isoidScaleFactors.py
       
       
       
       
    gardener.py  effwfiller \
       -r /media/data/amassiro/LatinoTrees/WW/50ns/05Aug2015  \
       /media/data/amassiro/LatinoTrees/WW/50ns/05Aug2015_puW \
       --isoid=data/isoidScaleFactors.py

       
Trigger efficiency
====

Module: efftfiller
          
    gardener.py  efftfiller \
       /media/data/amassiro/LatinoTrees/WW/50ns/05Aug2015/latino_WZ.root   \
       test.root \
       --effTrig=/afs/cern.ch/work/a/amassiro/Latinos/Framework/CMSSW_7_4_7/python/LatinoAnalysis/Gardener/data/triggerEfficiencies.py
       
       
       
       
    gardener.py  efftfiller \
       -r /media/data/amassiro/LatinoTrees/WW/50ns/05Aug2015  \
       /media/data/amassiro/LatinoTrees/WW/50ns/05Aug2015_puW \
       --effTrig=data/triggerEfficiencies.py
          

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

We recommend to use the product of the two weights.

So Far, only weights for jets with pt > 30 GeV are added, in other cases the weight is 1.

There are three different central values for each of the two weights, to be used according to the selection.
They differ in the number of jets for which you apply btagging selection and/or veto.
   * If you area applying a btag selection or veto on **all of the jets in your events** you should use `bPogSF*bTPSF`
   * If you are applying a btag selection/veto **on the leading jet only** you should use `bPogSF1Jet*bTPSF1jet`
   * If you are applying a btag selection/veto **on both the leading and the subleading jet** you should use `bPogSF1Jet*bTPSF1jet`
This does not cover all possibilities, but covers most of teh useful ones.   
Some examples:   
   * If you are **vetoing b jets**, as in the signal region, (i.e. you are applying a b-veto on all jets in the event) you should use `bPogSF*bTPSF`
   * If you are checking a control region requesting **the leading jet only to be btagged (or antib-tagged)** you should use `bPogSF1Jet*bTPSF1jet`
   * If you are checking a control region requesting **at least one ofbetween the leading and the sub-leading jet to be b-tagged (or antib-tagged)** you should use `bPogSF2Jet*bTPSF2jet`
