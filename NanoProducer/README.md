
author: X. Janssen

The tool submit a crabtask per sample and publish in phys03 DBS. Presently the storage of the nAOD is done on the Higgs EOS

# CMSSW Install:

Please use the following CMSSW release:

CMSSW_9_4_11_cand1 --> 94X  nAOD

CMSSW_10_2_6       --> 102X nAOD

Please check https://twiki.cern.ch/twiki/bin/view/CMSPublic/WorkBookNanoAOD#How_to_check_out_the_code_and_pr for updates of CMSSW version in the future


On top of LAtinoSetup

run the commands below in the src/ directory of CMSSW:

git cms-merge-topic cms-nanoAOD:master-94X resp. cms-nanoAOD:master-102X

create a branch directly on the nanoAOD branch, skipping the unnecessary merge commit from cms-merge-topic:

git checkout -b nanoAOD cms-nanoAOD/master-94X resp. cms-nanoAOD/master-102X

compile it:

scram build

# USAGE:

mkNanoProd.py -p Prod [-T <listof_samples>] [-E <listof_samples>] [-n]

-T: select only these samples

-E: exclude these samples  

-n: prepare cfg and do not submit

# Config file:

 * python/Productions_cfg.py  : list of productions
 * python/samples/[Prod].py   : list of samples in that production with list of customisation to apply per sample
 * python/nanoProdCustomise.py: cutomisation functions to be used on top of standard nanoAOD cfg 

# TODO:

 * Write the customisation functions !!!!! Now only dummy ones !!!!
 * Maybe allow storage on local user T2
 * DATA: Add JSON filtering if needed for data


