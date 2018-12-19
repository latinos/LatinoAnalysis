
author: X. Janssen

The tool submit a crabtask per sample and publish in ohys03. Presently the storage of the nAOD is done on the Higgs EOS

mkNanoProd.py -p <Prod> [-T <listof_samples>] [-E <listof_samples>] [-n]

-T: select only these samples

-E: exclude these samples  

-n: prepare cfg and do not submit

Config file:

 * python/Productions_cfg.py  : list of productions
 * python/samples/[Prod].py   : list of samples in that production with list of customisation to apply per sample
 * python/nanoProdCustomise.py: cutomisation functions to be used on top of standard nanoAOD cfg 

TODO:

 * Write the customisation functions !!!!! Now only dummy ones !!!!
 * Maybe allow storage on local user T2
 * DATA: Add JSON filtering if needed for data


