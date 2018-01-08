Get baseW
====

    tellMeBaseW.py
    
    tellMeBaseW.py --inputFile  /tmp/amassiro/eos/user/r/rebeca/HWW2015/22Jan_25ns_mAODv2_MC/MCl2loose__hadd__bSFL2pTEff__l2tight/latino_Zg.root
    
    tellMeBaseW.py --inputFiles  ../PlotsConfigurations/Configurations/ggH/samples.py  \
                   --folder      /tmp/amassiro/eos/user/r/rebeca/HWW2015/22Jan_25ns_mAODv2_MC/MCl2loose__hadd__bSFL2pTEff__l2tight/
    
    

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
              

    gardener.py l2selfiller --kind 2 --cmssw Full2016 --selection 1 --idEleKind cut_WP_Tight80X   \
              /eos/cms/store/group/phys_higgs/cmshww/amassiro/RunII/2016/Feb2017/MC/LatinoTrees/latino_GluGluWWTo2L2Nu_MCFM__part0.root  \
              /tmp/amassiro/mytest.root
              
              
              
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
                ../LatinoTrees/AnalysisStep/test/latino_stepB_mc_numEvent100.root  \
                test.root

    gardener.py  l2selfiller \
                --kind 2 \
                --cmssw=763   \
                ../LatinoTrees/AnalysisStep/test/latino_stepB_mc_numEvent100.root  \
                test.2.root

    gardener.py  l2selfiller \
                --kind 3 \
                --cmssw=763   \
                ../LatinoTrees/AnalysisStep/test/latino_stepB_mc_numEvent100.root  \
                test.3.root

    gardener.py  l2selfiller \
                --kind 1 \
                --cmssw=763   \
                ../LatinoTrees/AnalysisStep/test/latino_stepB_mc_numEvent100.root  \
                test.1.root
                
    gardener.py  l2selfiller \
                --kind 1 \
                --cmssw=ICHEP2016   \
                ../LatinoTrees/AnalysisStep/test/latino_stepB_mc_numEvent100.root  \
                test.1.root

                
                
    gardener.py  l2selfiller \
                --kind 2 \
                --cmssw=763   \
                --selection=1   \
                ../LatinoTrees/AnalysisStep/test/latino_stepB_mc_numEvent100.root  \
                test.root

    gardener.py  l1selfiller \
                --kind 2 \
                --cmssw=763   \
                ../LatinoTrees/AnalysisStep/test/latino_stepB_numEvent100.root  \
                test.l1sel.root

    gardener.py  l1selfiller \
                --kind 1 \
                --cmssw=ICHEP2016   \
                ../LatinoTrees/AnalysisStep/test/latino_stepB_mc_numEvent100.root  \
                test.l1sel.1.root

                
How to keep only some branches of a tree:

    gardener.py filter -k "njet" latino_stepB_numEvent100.root output.root	

    gardener.py filter -k "njet" -k "std_vector_lepton_pt" latino_stepB_numEvent100.root output.root	
                
                
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
                     

                     
                     
Generator Lepton matching
====

Check if there is a gen lepton close to the reco-lepton.
Used to remove fake-leptons in MC samples, already estimated with data-driven methods.


    gardener.py  genmatchvarfiller \
                test.root  \
                test.genmatch.root

    gardener.py  genmatchvarfiller \
                /tmp/amassiro/eos/user/r/rebeca/HWW2015/22Jan_25ns_mAODv2_MC/MCl2loose__hadd__bSFL2pTEff__l2tight__wwSel/latino_WWTo2L2Nu.root \
                /tmp/amassiro/latino_WWTo2L2Nu_gen.root
                
                
                
                     
                     
                     
Filter duplicates
====

Filter duplicates in data

    gardener.py  filterduplicates \
                ../LatinoTrees/AnalysisStep/test/latino_stepB_data_numEvent100.root  \
                test.root

                
    gardener.py  filterduplicates \
                /tmp/amassiro/eos/user/r/rebeca/HWW2015/03Mar_Run2015D_16Dec2015/l2loose__hadd__EpTCorr__l2tight__wwSel/latino_Run2015D_16Dec2015_SingleMuon.root \
                /tmp/amassiro/test.root
                
                
         
                     
Filter using JSON
====

Filter using JSON in data

    gardener.py  filterjson \
                --json=Cert_271036-273450_13TeV_PromptReco_Collisions16_JSON_NoL1T.txt  \
                data.root  \
                test.root

                
                
         
         
         
         
         

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
         ../LatinoTrees/AnalysisStep/test/latino_stepB_data_numEvent100.root testCorr.root


         
    gardener.py letPtCorrector --isData=0 \
         --cmssw=ICHEP2016    \
         test.root testCorr.root
    
    gardener.py letPtCorrector --isData=1 \
         --cmssw=ICHEP2016    \
         test.root testCorr.root


         
         
Fake weight adder
====

    gardener.py fakeWeights \
                21Jun2016_Run2016B_PromptReco/l2loose__hadd__EpTCorr/latino_Run2016B_PromptReco_DoubleEG.root \
                latino_DD_Run2016B_PromptReco_DoubleEG.root


WW NNLO+NNLL scales and uncertainty
====

    scp amassiro@cmsneu.cern.ch:/media/data/amassiro/LatinoTrees/21Oct_25ns_MC/mcwghtcount__MC__l2selFix__hadd__bSFL2Eff/latino_WWTo2L2Nu.root  /tmp/amassiro/
           
    gardener.py wwNLLcorrections \
       --cmssw=763   \
       ../LatinoTrees/AnalysisStep/test/latino_stepB_numEvent100.root \
       output.root
    
    gardener.py wwNLLcorrections \
       /tmp/amassiro/latino_WWTo2L2Nu.root \
       output.root

    
    
WW EWK corrections
====

    scp amassiro@cmsneu.cern.ch:/media/data/amassiro/LatinoTrees/21Oct_25ns_MC/mcwghtcount__MC__l2selFix__hadd__bSFL2Eff/latino_WWTo2L2Nu.root  /tmp/amassiro/
           
    gardener.py wwEWKcorrections \
       ../LatinoTrees/AnalysisStep/test/latino_stepB_numEvent100.root \
       output.root
    
    gardener.py wwEWKcorrections \
       /tmp/amassiro/latino_WWTo2L2Nu.root \
       output.root

       
    cp /tmp/amassiro/eos/cms//store/group/phys_higgs/cmshww/amassiro/HWW12fb_repro/07Jun2016_spring16_mAODv2_12pXfbm1_repro/MCl2loose__hadd__bSFL2pTEff__l2tight__wwSel/latino_WWTo2L2Nu.root   /tmp/amassiro/

    gardener.py wwEWKcorrections \
       /tmp/amassiro/latino_WWTo2L2Nu.root \
       /tmp/amassiro/latino_WWTo2L2Nu_test.root        
    
    

WZ and ZZ EWK corrections
====

    eosmount eos
    cp /tmp/amassiro/eos/cms//store/group/phys_higgs/cmshww/amassiro/HWW12fb_repro/07Jun2016_spring16_mAODv2_12pXfbm1_repro/MCl2loose__hadd__bSFL2pTEff__l2tight__wwSel/latino_WZTo3LNu.root   /tmp/amassiro/
           
    gardener.py wzEWKcorrections \
       /tmp/amassiro/latino_WZTo3LNu.root \
       /tmp/amassiro/latino_WZTo3LNu_test.root


    cp /tmp/amassiro/eos/cms//store/group/phys_higgs/cmshww/amassiro/HWW12fb_repro/07Jun2016_spring16_mAODv2_12pXfbm1_repro/MCl2loose__hadd__bSFL2pTEff__l2tight__wwSel/latino_WZTo2L2Q__part0.root   /tmp/amassiro/
       
    gardener.py wzEWKcorrections \
       /tmp/amassiro/latino_WZTo2L2Q__part0.root \
       /tmp/amassiro/latino_WZTo2L2Q__part0_test.root

       
    cp /tmp/amassiro/eos/cms//store/group/phys_higgs/cmshww/amassiro/HWW12fb_repro/07Jun2016_spring16_mAODv2_12pXfbm1_repro/MCl2loose__hadd__bSFL2pTEff__l2tight__wwSel/latino_ZZTo2L2Nu.root   /tmp/amassiro/
    cp /tmp/amassiro/eos/cms//store/group/phys_higgs/cmshww/amassiro/HWW12fb_repro/07Jun2016_spring16_mAODv2_12pXfbm1_repro/MCl2loose__hadd__bSFL2pTEff__l2tight__wwSel/latino_ZZTo2L2Q__part0.root   /tmp/amassiro/
    cp /eos/cms//store/group/phys_higgs/cmshww/amassiro/HWW12fb_repro/07Jun2016_spring16_mAODv2_12pXfbm1_repro/MCl2loose__hadd__bSFL2pTEff__l2tight__wwSel/latino_ZZTo2L2Nu.root   /tmp/amassiro/
    cp /eos/cms/store/group/phys_higgs/cmshww/amassiro/Full2016/Feb2017_summer16/MCl2looseCut__hadd__bSFL2pTEffCut__l2tight/latino_ZZTo2L2Nu.root   /tmp/amassiro/
    
    gardener.py zzEWKcorrections \
       /tmp/amassiro/latino_ZZTo2L2Nu.root \
       /tmp/amassiro/latino_ZZTo2L2Nu_test.root

    gardener.py zzEWKcorrections \
       /tmp/amassiro/latino_ZZTo2L2Q__part0.root \
       /tmp/amassiro/latino_ZZTo2L2Q__part0_test.root


    
       
Trigger efficiency
====

Module: efftfiller
     
    gardener.py  efftfiller    input.root output.root

    gardener.py  efftfiller   --cmssw=ICHEP2016  /tmp/amassiro/latino_GluGluHToWWTo2L2NuPowheg_M125_idiso.root  \
         /tmp/amassiro/latino_GluGluHToWWTo2L2NuPowheg_M125_idiso_trigg.root
    
    gardener.py  efftfiller   --cmssw=ICHEP2016  /tmp/amassiro/latino_DYJetsToLL_M-50_0001__part2_idiso.root  \
         /tmp/amassiro/latino_DYJetsToLL_M-50_0001__part2_idiso_trigg.root
    
    gardener.py  efftfiller   --cmssw=ICHEP2016  /tmp/amassiro/latino_DYJetsToLL_M-50_0000__part2.root  \
         /tmp/amassiro/latino_DYJetsToLL_M-50_0000__part2_trigg.root
    /tmp/amassiro/eos/cms/store/group/phys_higgs/cmshww/amassiro/TESTAUGUST/latino_DYJetsToLL_M-50_0000__part2.root
    
           
Id/isolation scale factors
====

Module: idisofiller
          
    gardener.py  idisofiller    input.root output.root
    
    gardener.py  idisofiller    -r     eos/user/a/amassiro/HWW2015/22Jan_25ns_mAODv2_MC/MCl2loose__hadd__bSFL2pTEff__l2tight__wwSel__TrigEff/   \
         /tmp/amassiro/test/
    
    gardener.py  idisofiller   --cmssw=ICHEP2016  /tmp/amassiro/latino_GluGluHToWWTo2L2NuPowheg_M125.root  \
         /tmp/amassiro/latino_GluGluHToWWTo2L2NuPowheg_M125_idiso.root
    
    
    gardener.py  idisofiller   --cmssw=ICHEP2016  /tmp/amassiro/latino_DYJetsToLL_M-50_0001__part2.root  \
         /tmp/amassiro/latino_DYJetsToLL_M-50_0001__part2_idiso.root
    
    
    gardener.py  idisofiller   --cmssw=ICHEP2016 --isoideleAltLumiRatio=0.079  /tmp/amassiro/latino_DYJetsToLL_M-50_0001__part2_idiso_trigg.root  \
         /tmp/amassiro/latino_DYJetsToLL_M-50_0001__part2_idiso_trigg_again_2.root
    
    
    gardener.py  idisofiller   --cmssw=ICHEP2016 --isoideleAltLumiRatio=0.079  /tmp/amassiro/latino_DYJetsToLL_M-50_0000__part0.root  \
         /tmp/amassiro/latino_DYJetsToLL_M-50_0000__part0_newidiso.root
    
    gardener.py  idisofiller   --cmssw=ICHEP2016 --isoideleAltLumiRatio=0.079  /tmp/amassiro/latino_DYJetsToLL_M-50_0000__part0.root  \
         /tmp/amassiro/latino_DYJetsToLL_M-50_0000__part0_newidiso.root
    

    
    cp /tmp/amassiro/eos/cms//store/group/phys_higgs/cmshww/amassiro/HWW12fb_repro/07Jun2016_spring16_mAODv2_12pXfbm1_repro/MCl2loose__hadd__bSFL2pTEff__l2tight__wwSel/latino_WWTo2L2Nu.root   /tmp/amassiro/

    gardener.py  idisofiller   --cmssw=Full2016     \
                               --idEleKind=cut_WP_Tight80X    \
                               /tmp/amassiro/latino_WWTo2L2Nu.root  \
                               /tmp/amassiro/latino_WWTo2L2Nu.idisotest.root
    

    
    
    
Kinematic variables
====
    
    gardener.py l2kinfiller --cmssw=763    input.root output.root
    gardener.py l2kinfiller                input.root output.root

    gardener.py l2kinfiller --cmssw=763    eos/user/a/amassiro/HWW2015/ICHEP/07Jun2016_spring16_mAODv2_12pXfbm1/MCl2loose__hadd__bSFL2pTEff__l2tight__wwSel/latino_GluGluHToWWTo2L2NuPowheg_M125.root    output.root

    gardener.py  l2kinfiller --cmssw=ICHEP2016  test.root      test.l2kin.root
    
    
    
    
Jet Energy Scale
====

Module: JESTreeMaker
          
    gardener.py JESTreeMaker 	           input.root output.root
    gardener.py JESTreeMaker            -r inputDir/ outputDir/

    options:
	-k/--kind  : factor (usually 1 or -1)
	-c/--cmssw : cmssw version (f.e. ICHEP2016)
	-m/--maxUncertainty : Maximum of Fall15_25nsV2 and Summer15_25nsV6 uncertainties

          
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

Module options:
    
    '-w', '--working-point' (default 0): 0 (loose), 1 (medium), 2 (tight)
    '-s', '--scalefactor-file' (default: data/cMVAv2.csv): csv file with the scale factors
    '-p', '--scalefactor-file-tp' (CURRENTLY NOT USED): csv file with the T&P scale factors
    '-e', '--efficiency-file' (default: data/efficiencyMCFile76X.py): root file with MC efficiencies for b, c and light jets in bins of eta and pT


The `bTPSF*` are currently placeholders and their value is 1.

NB: currently only the scale factors provided by BTV are used, even for jets with pT between 20 and 30 GeV (doubling the uncertainty).


Module: allBtagPogScaleFactors 

    gardener.py  allBtagPogScaleFactors \
       /media/data/amassiro/LatinoTrees/WW/50ns/05Aug2015/latino_WZ.root   \
       test.root \


    gardener.py  allBtagPogScaleFactors --cmssw=ICHEP2016  \
       /tmp/amassiro/latino_TTTo2L2Nu_ext1__part0.root   \
       /tmp/amassiro/latino_TTTo2L2Nu_ext1__part0_btag.root            

       
Same skeleton as the previous module but this time add 3 weights (nominal, up and down) for each working point (loose, medium and tight) of the CMVA and the CSVv2 taggers.
In addition the module also adds the weights for the b tagging discriminator reshaping, both for CMVA and CSVv2.
To each one of the two reshaping weight are associated 18 additional weights representing the systematic variations of several quantities (such as JES variations), to be treated as nuisance parameters.



Lepton pT scale uncertainty
====

    gardener.py LeppTScalerTreeMaker -v 1 -k mu  ../LatinoTrees/AnalysisStep/test/latino_stepB_numEvent100.root testscalar.root

or 
    
    --lepFlavourToChange ele  

    
    gardener.py LeppTScalerTreeMaker -v 1 -k mu  --cmssw='ICHEP2016'   test.trigger.2.root   testscalar.root   

    
Lepton pT resolution uncertainty
====
    
    gardener.py leptonResolution ../LatinoTrees/AnalysisStep/test/latino_stepB_numEvent100.root     test.root


PDF uncertainty
====
    
    gardener.py pdfUncertainty ../LatinoTrees/AnalysisStep/test/latino_stepB_numEvent100.root     test.root


QCD uncertainty
====
    
    gardener.py qcdUncertainty ../LatinoTrees/AnalysisStep/test/latino_stepB_numEvent100.root     test.root

    
PDF and scale uncertainty
====
    
    gardener.py pdfAndScaleUncertainty ../LatinoTrees/AnalysisStep/test/latino_stepB_numEvent100.root     test.root


    
MET uncertainty
====

If reading 74x MET naming convention and available uncertainties.
    
    gardener.py metUncertainty --kind='Up' --cmssw='74x' input.root output.root
    gardener.py metUncertainty --kind='Dn' --cmssw='74x' input.root output.root

If reading 763 MET naming convention and full set of uncertainties.

    gardener.py metUncertainty --kind='Up' --cmssw='763' input.root output.root
    gardener.py metUncertainty --kind='Dn' --cmssw='763' input.root output.root

If reading 763 MET naming convention but not using lepton (electron and muon) uncertainties

    gardener.py metUncertainty --kind='Up' --cmssw='763' --lepton='no' input.root output.root
    gardener.py metUncertainty --kind='Dn' --cmssw='763' --lepton='no' input.root output.root

    
80X MET for ICHEP

    gardener.py metUncertainty --kind='Up' --cmssw='ICHEP2016'  --unclustered='no' test.root test.met.root
    gardener.py metUncertainty --kind='Do' --cmssw='ICHEP2016'  --unclustered='no' test.root test.met.root


MET uncertainty
====

This will add the xy-shift corrected MET and phi in the latino trees: corrPfType1Met and corrPfType1Phi

    gardener.py metXYshift -c 809 -p Spring16_V0_MET_MC_XYshiftMC_PfType1MetLocal.txt input.root output.root


baseW table
====

Get the baseW table

    ls /media/data/amassiro/LatinoTrees/21Oct_25ns_MC/mcwghtcount__MC__l2selFix__hadd__bSFL2Eff/*.root | grep ".root" | awk '{print "root -l -q drawBasew.cxx\\\(\\\""$1"\\\"\\\)"}' | /bin/sh

    

           
generator level variables
====

Module: genvariablesfiller
          
    gardener.py  genvariablesfiller    input.root output.root
    
    gardener.py  genvariablesfiller    test.kin.root  test.mc.root
    gardener.py  genvariablesfiller    /tmp/amassiro/eos/user/j/jlauwers/HWW2015/22Jan_25ns_mAODv2_MC/MCl2loose__hadd__bSFL2pTEff__l2tight/latino_DYJetsToLL_M-50_0000__part0.root   /tmp/amassiro/test.mc.root
    gardener.py  genvariablesfiller    /tmp/amassiro/eos/user/j/jlauwers/HWW2015/22Jan_25ns_mAODv2_MC/MCl2loose__hadd__bSFL2Eff/latino_DYJetsToLL_M-50_0000__part0.root   /tmp/amassiro/test.mc.2.root
    
    
    gardener.py  genvariablesfiller   /tmp/amassiro/latino_DYJetsToLL_M-50_0000__part0.root /tmp/amassiro/latino_DYJetsToLL_M-50_0000__part0_genVar.root
    
    
    
    latino->Draw("gen_ptll / ptll", "gen_ptll / ptll < 3")
    latino->Draw("gen_ptll / ptll", "gen_ptll / ptll < 3 && gen_llchannel == -11*11")
    latino->Draw("gen_ptll / ptll", "gen_ptll / ptll < 3 && gen_llchannel == -13*13")
    latino->Draw("gen_ptll / ptll", "gen_ptll / ptll < 3 && gen_llchannel == -15*15")
    
    
    gardener.py  genvariablesfiller   eos/user/x/xjanssen/HWW2015/22Jan_25ns_mAODv2_MC/MCl2loose__hadd__bSFL2pTEff__l2tight__wwSel/latino_WpWmJJ_EWK_QCD_noTop.root   /tmp/amassiro/latino_WpWmJJ_EWK_QCD_noTop.root
    gardener.py  genvariablesfiller   eos/user/x/xjanssen/HWW2015/22Jan_25ns_mAODv2_MC/MCl2loose__hadd__bSFL2pTEff__l2tight__wwSel/latino_WpWmJJ_QCD_noTop.root   /tmp/amassiro/latino_WpWmJJ_QCD_noTop.root
    
    
    latino->Draw("gen_mll / std_vector_VBoson_mass[0]","GEN_weight_SM/abs(GEN_weight_SM) * (std_vector_VBoson_mass[0]>0)", "same")
    
    
    latino->Draw("mll","GEN_weight_SM/abs(GEN_weight_SM) * (mll<120 && gen_llchannel == -11*11 && std_vector_lepton_pt[1]>15)")
    latino->Draw("mll","GEN_weight_SM/abs(GEN_weight_SM) * (mll<120 && gen_llchannel == -11*11 && std_vector_lepton_pt[1]>15 && gen_mll>80)", "same")
    
    latino->Draw("mll","GEN_weight_SM/abs(GEN_weight_SM) * (std_vector_leptonGen_isPrompt[0] == 1 && std_vector_leptonGen_isPrompt[1] == 1 &&  mll<120 && gen_llchannel == -11*11 && std_vector_lepton_pt[1]>15)")
    latino->Draw("mll","GEN_weight_SM/abs(GEN_weight_SM) * (std_vector_leptonGen_isPrompt[0] == 1 && std_vector_leptonGen_isPrompt[1] == 1 &&  mll<120 && gen_llchannel == -11*11 && std_vector_lepton_pt[1]>15 && std_vector_VBoson_mass[0]>80)", "same")
    
    latino->Draw("mll","GEN_weight_SM/abs(GEN_weight_SM) * (std_vector_VBoson_mass[0]>0) * (std_vector_lepton_isTightLepton[0]<0.5 || std_vector_lepton_isTightLepton[1]<0.5) * (std_vector_leptonGen_isPrompt[0] == 1 && std_vector_leptonGen_isPrompt[1] == 1 &&  mll<120 && gen_llchannel == -11*11 && std_vector_lepton_pt[1]>15)")
    latino->Draw("std_vector_VBoson_mass[0]","GEN_weight_SM/abs(GEN_weight_SM) * (std_vector_VBoson_mass[0]>0) * (std_vector_lepton_isTightLepton[0]<0.5 || std_vector_lepton_isTightLepton[1]<0.5) * (std_vector_leptonGen_isPrompt[0] == 1 && std_vector_leptonGen_isPrompt[1] == 1 &&  mll<120 && gen_llchannel == -11*11 && std_vector_lepton_pt[1]>15)")
    latino->Draw("mll","GEN_weight_SM/abs(GEN_weight_SM) * (std_vector_VBoson_mass[0]>0) * (std_vector_lepton_isTightLepton[0]<0.5 || std_vector_lepton_isTightLepton[1]<0.5) * (std_vector_leptonGen_isPrompt[0] == 1 && std_vector_leptonGen_isPrompt[1] == 1 &&  mll<120 && gen_llchannel == -11*11 && std_vector_lepton_pt[1]>15)", "same")
    
    latino->Draw("std_vector_VBoson_mass[0]","GEN_weight_SM/abs(GEN_weight_SM) * (std_vector_VBoson_mass[0]>0) * (std_vector_lepton_isTightLepton[0]<0.5 || std_vector_lepton_isTightLepton[1]<0.5) * (std_vector_leptonGen_isPrompt[0] == 1 && std_vector_leptonGen_isPrompt[1] == 1 &&  mll<120 && gen_llchannel == -11*11 && std_vector_lepton_pt[1]>10 && std_vector_lepton_pt[1]<20)")
    latino->Draw("mll","GEN_weight_SM/abs(GEN_weight_SM) * (std_vector_VBoson_mass[0]>0) * (std_vector_lepton_isTightLepton[0]<0.5 || std_vector_lepton_isTightLepton[1]<0.5) * (std_vector_leptonGen_isPrompt[0] == 1 && std_vector_leptonGen_isPrompt[1] == 1 &&  mll<120 && gen_llchannel == -11*11 && std_vector_lepton_pt[1]>10 && std_vector_lepton_pt[1]<20)", "same")
    
    latino->Draw("mll","GEN_weight_SM/abs(GEN_weight_SM) * (std_vector_leptonGen_isPrompt[0] == 1 && std_vector_leptonGen_isPrompt[1] == 1 &&  mll<120 && gen_llchannel == -11*11 && std_vector_lepton_pt[1]>15 && std_vector_lepton_pt[1]<20)")
    latino->Draw("mll","GEN_weight_SM/abs(GEN_weight_SM) * (std_vector_leptonGen_isPrompt[0] == 1 && std_vector_leptonGen_isPrompt[1] == 1 &&  mll<120 && gen_llchannel == -11*11 && std_vector_lepton_pt[1]>15 && std_vector_lepton_pt[1]<20 && gen_mll>80)", "same")
    
    latino->Draw("mll","GEN_weight_SM/abs(GEN_weight_SM) * (std_vector_leptonGen_isPrompt[0] == 1 && std_vector_leptonGen_isPrompt[1] == 1 &&  mll<120 && gen_llchannel == -11*11 && std_vector_lepton_pt[1]>15 && std_vector_lepton_pt[1]<20)")
    latino->Draw("mll","GEN_weight_SM/abs(GEN_weight_SM) * (std_vector_leptonGen_isPrompt[0] == 1 && std_vector_leptonGen_isPrompt[1] == 1 &&  mll<120 && gen_llchannel == -11*11 && std_vector_lepton_pt[1]>15 && std_vector_lepton_pt[1]<20 && gen_mll>80)", "same")
    
    
    
    latino->Draw("mll","GEN_weight_SM/abs(GEN_weight_SM) * (std_vector_leptonGen_isPrompt[0] == 1 && std_vector_leptonGen_isPrompt[1] == 1 &&  mll<120 && gen_llchannel == -13*13 && std_vector_lepton_pt[1]>15 && std_vector_lepton_pt[1]<20)")
    latino->Draw("mll","GEN_weight_SM/abs(GEN_weight_SM) * (std_vector_leptonGen_isPrompt[0] == 1 && std_vector_leptonGen_isPrompt[1] == 1 &&  mll<120 && gen_llchannel == -13*13 && std_vector_lepton_pt[1]>15 && std_vector_lepton_pt[1]<20 && gen_mll>80)", "same")
    
    
Higgs Lineshape variations    
====

Module: BWEwkSingletReweighter

  This module reweights the Higgs lineshape according to the EWK singlet c' BRnew parametrization. It does not change the overall normalization. If you want the EWK singlet corresponfing cross section you should multiply your event yield by c'c'(1-BRnew) 

  The module adds to the tree a set of weights names cprime[value]\_BRnew[value].

  Example:

  gardener.py BWEwkSingletReweighter filein.root fileout.root

    options:

    -u, --undoCPS:  assumes the POWHEG sample was produced with CPS lineshape. Default True.

    (-i, --cprimemin), (-f, --cprimemax), (-s, --cprimestep) are used to compute the c' steps, from cprimemin (default 0.1) to cprimemax (default 1.0) in cprimestep (default 0.1) steps
   
    (-l, --brnewmin), (-n, --brnewmax), (-q, --brnewstep), same as above for BRnew. defaults: brnewmin 0.0, brnewmax 1.0, brnewstep 0.1

    -w , --globalshiftfileGG,  pickle file containing the global shifts due to reweighting (to preserve integral) for GG. Default="data/BWShifts_ggH.pkl"
   
    -k , --globalshiftfileVBF, pickle file containing the global shifts due to reweighting (to preserve integral) for VBF. Default="data/BWShifts_VBF.pkl"

    -d , --decayWeightsFile, pickle file containing the JHU derived decay weights for WW, default="data/decayWeightsWW.pkl"
          
    -p , --fileNameFormat, file name format to determine production process and mass, default="latino_(GluGlu|VBF)HToWWTo2L2Nu_M([0-9]+).root")

  Code to produce the pickle files in https://github.com/lenzip/LineshapeTools. Currently these are produced for the default cprime and BRnew intervals and steps only.


Top Gen Pt
====

Module: TopGenPt

  This module adds the gen level quark op and antiquark top pT to the tree, to be used for Pt Reweighting according top the recipe in https://twiki.cern.ch/twiki/bin/viewauth/CMS/TopPtReweighting

                    
                     
Higgs ggH uncertainties
====

Add event weights for nuisances according to the 2017 interim prescription of the LHCXSWG

    gardener.py  ggHUncertainty \
                /tmp/amassiro/latino_GluGluHToWWTo2L2NuPowheg_M125.root   \
                /tmp/amassiro/latino_GluGluHToWWTo2L2NuPowheg_M125.TEST.root  
              
              
 Higgs ggH re-weighter to MINLO
====

Add event weight to scale POWHEG to MINLO to macth kinematic distributions.
Source: https://twiki.cern.ch/twiki/bin/viewauth/CMS/HiggsWG/SignalModelingTools


    gardener.py  ggHtoMINLO \
                /tmp/amassiro/latino_GluGluHToWWTo2L2NuPowheg_M125.root   \
                /tmp/amassiro/latino_GluGluHToWWTo2L2NuPowheg_M125.TEST.root  
              
              

 Higgs VH re-weighter for anomalous HHH coupling
====

Add event weight to allow scaling with anomalous EWK HHH coupling.

    gardener.py  reweightHHH \
                --productionkind=wph  \
                /tmp/amassiro/latino_HWplusJ_HToWW_M125.root   \
                /tmp/amassiro/latino_HWplusJ_HToWW_M125.root.TEST.root  
              
     gardener.py  reweightHHH \
                --productionkind=zh  \
                /tmp/amassiro/latino_HZJ_HToWWTo2L2Nu_M125.root   \
                /tmp/amassiro/latino_HZJ_HToWWTo2L2Nu_M125.root.TEST.root  
              

 3-leptons kinematic
====
         
    gardener.py  l3kinfiller \
                /tmp/amassiro/latino_HWplusJ_HToWW_M125.root  \
                /tmp/amassiro/latino_HWplusJ_HToWW_M125_TEST.root
         
         
              
              
              
Add generic branches as formulas of other branches
====

Module: genericFormulaAdder

This module adds generic expressions of of branches to the tree. The typical use is to precompute common weights.
The new branches to ad are defined in https://github.com/latinos/LatinoAnalysis/blob/master/Gardener/python/data/formulasToAdd.py

    gardener.py  genericFormulaAdder \
                /tmp/amassiro/latino_GluGluHToWWTo2L2NuPowheg_M125.root   \
                /tmp/amassiro/latino_GluGluHToWWTo2L2NuPowheg_M125.TEST.root	
		
		
Slimmed version of systematic trees
====

Since Sept 2017 it is possible to compute a slimmed version of the systematic trees, holding only the varied branches. These trees need to be used together with the nominal tree, from which all non varied branches are taken, using the TTree friend mechanism in ROOT.

All gardener modules have been provided with two new options:

     --saveOnlyModifiedBranches: will output only the branches that are touched by the gardener module
     --auxiliaryFile: this option allows any gardener module to load an auxiliary file holding branches that are not in the main tree, e.g. when the main tree has been produced with the --saveOnlyModifiedBranches
     
Suppose you want to produce the JESup variation of a give file latino_XXX.root. The list of commands to issue would be:

     gardener.py JESTreeMaker -k 1 --saveOnlyModifiedBranches latino_XXX.root latino_XXX_JESup.root
     gardener.py allBtagPogScaleFactors --auxiliaryFile=latino_XXX.root latino_XXX_JESup.root latino_XXX_JESup_bPog.root
     gardener.py l2kinfiller --auxiliaryFile=latino_XXX.root latino_XXX_JESup_bPog.root latino_XXX_JESup_bPog_l2kin.root
     ...
     
The final latino_XXX_JESup_bPog_l2kin.root in this example will hold all the branches modified by the three modules run, and only those ones. All other untouched branches can be taken from the nominal latino_XXX.root.

An usage example in an analysis code would be the following:

     TFile* file_syst = new TFile("latino_XXX_JESup_bPog_l2kin.root");
     TTree* latino_syst = (TTree*) file_syst->Get("latino");
     TFile* file_nominal = new TFile("latino_XXX.root");
     TTree* latino_nominal = (TTree*) file_nominal->Get("latino");
     latino_syst->AddFriend(latino_nominal);
     // now you can draw whatever variable you like, you will get the systematic variation JESup for that variable
     
 If you are using mkShapes.py all of this is done automatically onece the nuisances.py is configured properly, see below.
 
 Skim do not play well with the Friend tree mechanism, because once you filter the tree with modified branches for the systematic variation unders study, you loose the syncronization with the tree holding the unmodified branches. An option has been added to the Pruner gardener module to output only an event list of the selected events. For example, if you want to do a wwSel skim of the JESup variation, following the previous example, you could do something like:
 
     gardener.py filter -f \' mll>12 && std_vector_lepton_pt[0]>20 && std_vector_lepton_pt[1]>10 && std_vector_lepton_pt[2]<10 && metPfType1 > 20 && ptll > 30 && (std_vector_lepton_flavour[0] * std_vector_lepton_flavour[1] == -11*13) \'  --eventListOutput --auxiliaryFile latino_XXX.root latino_XXX_JESup_bPog_l2kin.root latino_XXX_JESup_bPog_l2kin_wwSel.root
     
The --eventListOutput option tells the Pruner module to only output the TEventList of the selected entries for the JESup variation. Indeed latino_XXX_JESup_bPog_l2kin_wwSel.root does not contain any tree, it only contains a TEventList.

So, if you want to get the wwSel skim of the JESup variation of nominal file  latino_XXX.root, you have to do something like the following:

     TFile* file_syst = new TFile("latino_XXX_JESup_bPog_l2kin.root");
     TTree* latino_syst = (TTree*) file_syst->Get("latino");
     TFile* file_nominal = new TFile("latino_XXX.root");
     TTree* latino_nominal = (TTree*) file_nominal->Get("latino");
     latino_syst->AddFriend(latino_nominal);
     
     TFile* file_evlist = new TFile("latino_XXX_JESup_bPog_l2kin_wwSel.root");
     TEventList * evlist = (TEventList*) file_evlist->Get("prunerlist");
     latino_syst->SetEventList(evlist);
     
Again, if you are using mkShapes.py, this is done internally provided nuisances.py is configured properly.     


Example mkGardener commands:
     mkGardener.py -p Apr2017_summer16 -s FJESSubTotalRelativedo -i lepSel__MCWeights__bSFLpTEffMulti__cleanTauMC__l2loose__hadd__l2tightOR__formulasMC --friendStep lepSel__MCWeights__bSFLpTEffMulti__cleanTauMC__l2loose__hadd__l2tightOR__formulasMC --input-target /eos/cms/store/caf/user/lenzip/test/ --output-target=/eos/cms/store/caf/user/lenzip/test/ --queue=1nd  --batch --batchSplit=Target,Steps 
     mkGardener.py -p Apr2017_summer16 -s FwwSel -i lepSel__MCWeights__bSFLpTEffMulti__cleanTauMC__l2loose__hadd__l2tightOR__formulasMC__FJESSubTotalRelativedo --friendStep lepSel__MCWeights__bSFLpTEffMulti__cleanTauMC__l2loose__hadd__l2tightOR__formulasMC --input-target /eos/cms/store/caf/user/lenzip/test/ --output-target=/eos/cms/store/caf/user/lenzip/test/ --queue=1nd  --batch --batchSplit=Target,Steps

Usage of friend trees in mkShapes.py
===


The configuration you would normally use with full trees in nuisances.py is something like:

	nuisances['jes']  = {
                'name'  : 'scale_j',
                'kind'  : 'tree',
                'type'  : 'shape',
                'samples'  : {
                   'ggWW' :['1', '1'],
                   'WW' :  ['1', '1'],
                   'DY' :  ['1', '1'],
                   'top' : ['1', '1'],
                   'VZ' :  ['1', '1'],
                   'VVV' : ['1', '1'],
                   'Vg' : ['1', '1'],
                   'VgS': ['1', '1'],
                   'ggH_hww' : ['1', '1'],
                   'qqH_hww' : ['1', '1'],
                   'WH_hww' :  ['1', '1'],
                   'ZH_hww' :  ['1', '1'],
                   'ggZH_hww':  ['1', '1'],
                   'bbH_hww' : ['1', '1'],
                   'H_htt' : ['1', '1'],
                },
                'folderUp'   : 	xrootdPath+treeBaseDir+'Apr2017_summer16/lepSel__MCWeights__bSFLpTEffMulti__cleanTauMC__l2loose__hadd__l2tightOR__formulasMC__JESup'+skim,
                'folderDown' : xrootdPath+treeBaseDir+'Apr2017_summer16/lepSel__MCWeights__bSFLpTEffMulti__cleanTauMC__l2loose__hadd__l2tightOR__formulasMC__JESdo'+skim,
	}

Suppose you have produced the slimmed version of JES systematic trees, as descrived above, and that you want to run on the wwSel skim. The configuration of nuisances.py changes to:


	nuisances['jes']  = {
                'name'  : 'scale_j',
                'kind'  : 'tree',
                'type'  : 'shape',
                'samples'  : {
                   'ggWW' :['1', '1'],
                   'WW' :  ['1', '1'],
                   'DY' :  ['1', '1'],
                   'top' : ['1', '1'],
                   'VZ' :  ['1', '1'],
                   'VVV' : ['1', '1'],
                   'Vg' : ['1', '1'],
                   'VgS': ['1', '1'],
                   'ggH_hww' : ['1', '1'],
                   'qqH_hww' : ['1', '1'],
                   'WH_hww' :  ['1', '1'],
                   'ZH_hww' :  ['1', '1'],
                   'ggZH_hww':  ['1', '1'],
                   'bbH_hww' : ['1', '1'],
                   'H_htt' : ['1', '1'],
                },
                'unskimmedFolderUp'   : xrootdPath+treeBaseDir+'Apr2017_summer16/lepSel__MCWeights__bSFLpTEffMulti__cleanTauMC__l2loose__hadd__l2tightOR__formulasMC__FJESup',
                'unskimmedFolderDown' : xrootdPath+treeBaseDir+'Apr2017_summer16/lepSel__MCWeights__bSFLpTEffMulti__cleanTauMC__l2loose__hadd__l2tightOR__formulasMC__FJESdo',
                'unskimmedFriendTreeDir' : xrootdPath+treeBaseDir+'Apr2017_summer16/lepSel__MCWeights__bSFLpTEffMulti__cleanTauMC__l2loose__hadd__l2tightOR__formulasMC',
                'skimListFolderUp': xrootdPath+treeBaseDir+'Apr2017_summer16/lepSel__MCWeights__bSFLpTEffMulti__cleanTauMC__l2loose__hadd__l2tightOR__formulasMC__FJESup'+skim,
                'skimListFolderDown': xrootdPath+treeBaseDir+'Apr2017_summer16/lepSel__MCWeights__bSFLpTEffMulti__cleanTauMC__l2loose__hadd__l2tightOR__formulasMC__FJESdo'+skim
	}

where 'unskimmedFolderUp/Down' is the location of the full (i.e. unskimmed) tree for the Up/Down variation (the file latino_XXX_JESup_bPog_l2kin.root in the examples above); 'unskimmedFriendTreeDir' is the location of the nominal unskimmed file to be used for all unmodified branches (the file latino_XXX.root in the examples above); 'skimListFolderUp/Down' is the location of the files containing the TEventList's of events passing the wwSel skim (the file latino_XXX_JESup_bPog_l2kin_wwSel.root in the explicit examples above). 

If you do not want to run on a skim, simply drop 'skimListFolderUp/Down'.

	
                
