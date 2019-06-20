# Documentation:

   * NanoAOD workbook https://twiki.cern.ch/twiki/bin/view/CMSPublic/WorkBookNanoAOD
   * Latino NanoPostprocessing slides https://indico.cern.ch/event/718326/contributions/2955317/attachments/1625920/2589261/NanoGargener_3Apr2018.pdf
   
# Study2017 ntuples
   * Data: /eos/cms/store/group/phys_higgs/cmshww/amassiro/HWWNano/Run2017_nAOD_v1_Study2017/DATAl1loose2017__hadd/ 
   * MC:  /eos/cms/store/group/phys_higgs/cmshww/amassiro/HWWNano/Fall2017_nAOD_v1_Study2017/MCl1loose2017__baseW__hadd/ 
   
# Full 2017 ntuples
   * Data:  /eos/cms/store/group/phys_higgs/cmshww/amassiro/HWWNano/Run2017_nAOD_v1_Full2017
   * MC:    /eos/cms/store/group/phys_higgs/cmshww/amassiro/HWWNano/Fall2017_nAOD_v1_Full2017
   
# General items to know when using nanoAOD

NanoAODs are provided centrally. The current campaign for 2017 data is based on CMSSW_9_4_7.

The 2017 data production goes under the name [31Mar2018](https://cmsweb.cern.ch/das/request?view=list&limit=50&instance=prod%2Fglobal&input=%2F*%2F*31Mar2018*%2FNANOAOD).

The 2017 mc production goes under the name [12Apr2018](https://cmsweb.cern.ch/das/request?view=list&limit=50&instance=prod%2Fglobal&input=%2F*%2F*12Apr2018*%2FNANOAODSIM).

Events are stored in NanoAOD in the "Events" TTree. This is a plain tree, similar to our old "latino" tree. Branches in that tree are auto-documented, to some extent. If you do Events->Print() you will get a short explaination for each branch. Same explanation is also available [here](https://cms-nanoaod-integration.web.cern.ch/integration/master/mc94X_doc.html).

## Naming conventions
Branches in the Events tree can be either single values or vectors. Branches start with a capital letter and often have a prefix whenever more branches with the same length have to be put together to build a physics object. Example: all the muon branches start with the prefix "Muon_", see [here](https://cms-nanoaod-integration.web.cern.ch/integration/master/mc94X_doc.html#Muon). Since you have many muons in an event, an auxiliary branch "nMuon" (in general "n\<prefix\>") is provided holding an integer thai is the number of items in each of the "Muon_*" branches.
  
Branches can be cross referenced, e.g.  Muon_genPartIdx[i] is the index of the particle in the GenPart_* branches corresponding to a i-th muon.



# Guide to latino postprocessing on NanoAOD

## Installation

    export SCRAM_ARCH=slc6_amd64_gcc630
    cmsrel CMSSW_9_4_9
    cd CMSSW_9_4_9/src
    cmsenv
    git clone --branch 13TeV git@github.com:latinos/setup.git LatinosSetup
    source LatinosSetup/SetupShapeOnly.sh
    scram b

### Customization
Copy the file LatinoAnalysis/Tools/python/userConfig_TEMPLATE.py to LatinoAnalysis/Tools/python/userConfig.py and edit it to reflect your local paths. This is needed for batch jobs submission

### Modules
Postprocessing modules for NanoAOD are based on the centrally provided NanoAOD postprocessing framework https://github.com/cms-nanoAOD/nanoAOD-tools. The main features of this framework are:
   * Modules should inherit from the a Module base class and implement methods to be called upon beginning the job, beginning file, end of job and on every event
   * Objects from the input tree can be accesses with the Collection(event, "branch prefix") helper or Object(event, "branch prefix"). These two helper classes return a python list of objects (Collection) or a single object (Object) whose attrbutes are taken from the corresponding branches. E.. nanoAOD provides Electron_pt, Electron_eta etc vectors for all the nElectron electrons in an event. 

    electrons=Collection(event, "Electron")
    
is a list of objects, and one can access the pt of the first electron with something like
    
    electrons[0].pt
    
   * Multiple modules can be run in the same event loop. Each module can return True or False. If it returns False, subsequent moduled will not be run. Modules can access branches produced by prevoious modules in the same event loop.
   * An Example script running the postprocessor is here: https://github.com/latinos/LatinoAnalysis/blob/master/NanoGardener/test/postproc.py
    

### Postprocessing script
The mkPostProc.py script is provided, that automates the submission of a full postprocessing campaing. The basic idea is that this script creates one python executable similar to the example quoted above (https://github.com/latinos/LatinoAnalysis/blob/master/NanoGardener/test/postproc.py), with automated definition of the input and output files and the list of modules to be run.

This script is based on three master configuration files:

   * Sites_cfg.py (https://github.com/latinos/LatinoAnalysis/blob/master/NanoGardener/python/framework/Sites_cfg.py) defines the sites on which one is willing to write the output. By default, if the postprocessing is run from one of these sites, the output will go to that site.
   * Productions_cfg.py (https://github.com/latinos/LatinoAnalysis/blob/master/NanoGardener/python/framework/Productions_cfg.py) Defines the path to the list of samples.
   * Steps_cfg.py (https://github.com/latinos/LatinoAnalysis/blob/master/NanoGardener/python/framework/Steps_cfg.py) defines the different steps and the chains of steps to be run.
   
 Examples:
 
     mkPostProc.py  -p summer16_nAOD_v1 -s MCl1loose2016 -b 
 
 this will submit the MCl1Loose2016 chain on all the samples defined in summer16_nAOD_v1.
 If you simply replace -b with -c, the submission will go trough crab.    
 
 Options:
     
         -b : submit to batch [default is interactive execution] 
         -c : submit via crab  
         -n : dry-run  just produce script in job directory but di not submit  
         -T <sample1>, ... ,< sampleN > : run only on these samples 
         -E <sample1>, ... ,< sampleN > : do not run on these samples 
         -R : redo all jobs even if output file exist 
         -Q < queuename > : specify queue like 8nh [default btw, see  Site_cfg.py ],   
         Not needed by default 
         --sitescfg  <File> : alternative site cfg
         --modcfg <File> : alternative step/module  cfg
         --datacfg <File> : alternative production cfg

### Full2017 postprocessing campaign

We share the postprocessing of data and MC samples. If you run at CERN, with either crab or LSF, the output of your jobs will automatically go in the usual eos space managed by the Higgs group at the following path:

   * LSF output: /eos/cms/store/group/phys_higgs/cmshww/amassiro/HWWNano
   * CRAB output: /eos/cms/store/group/phys_higgs/cmshww/amassiro/HWWNanoCrab
   
If you use crab, the output stored in the above mentioned directory needs to be unpacked and moved to the standard location, which is the one for LSF output. To do so you can use the script mkCrab.py:

    mkCrab.py -s: To check the status of your tasks
    mkCrab.py -u: to unpack a completed task from HWWNanoCrab to HWWNano
    mkCrab.py -c: to clean a task after having unpacked it
    
We currently have two productions, one for data and one for MC, listed below. The Data production is going to be handled in Brussels, while the MC production needs to be shared. We propose a splitting of the samples among people according to the names proposed in the fall17 MC file list. The list of samples to run on can be specified in the commands below with the -T option and a comma separated list of sample short names, as they appear in the https://github.com/latinos/LatinoAnalysis/blob/master/NanoGardener/python/framework/samples/fall17_nAOD_v1.py file

   * Fall2017_nAOD_v1_Full2017 for MC: https://github.com/latinos/LatinoAnalysis/blob/master/NanoGardener/python/framework/Productions_cfg.py#L43-L49
     
      * Steps (example commands given for LSF running, use -c instead of -b for crab): 
          
    1) mkPostProc.py -p Fall2017_nAOD_v1_Full2017 -s MCl1loose2017 -b -T [comma separated list of samples]     
    2) mkPostProc.py -p Fall2017_nAOD_v1_Full2017 -i MCl1loose2017 -s MCformulas -b -T [comma separated list of samples]
    3) mkPostProc.py -p Fall2017_nAOD_v1_Full2017 -i MCl1loose2017__MCformulas -s MCWeights2017 -b -T [comma separated list of samples]
    
  
  
   * Run2017_nAOD_v1_Full2017 https://github.com/latinos/LatinoAnalysis/blob/master/NanoGardener/python/framework/Productions_cfg.py#L36-L41
   

   
