# Documentation:

   * NanoAOD workbook https://twiki.cern.ch/twiki/bin/view/CMSPublic/WorkBookNanoAOD
   * Latino NanoPostprocessing slides https://indico.cern.ch/event/718326/contributions/2955317/attachments/1625920/2589261/NanoGargener_3Apr2018.pdf

# Guide to latino postprocessing on NanoAOD

## Installation

     cmsrel CMSSW_9_4_7
     cd CMSSW_9_4_7/src
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
