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


