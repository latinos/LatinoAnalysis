

mkNanoProd.py -p <Prod> [-T <listof_samples>] [-E <listof_samples>] [-n]

-T: select only these samples

-E: exclude these samples  

-n: prepare cfg and do not submit

Config file:

 * python/Productions_cfg.py  : list of productions
 * python/samples/[Prod].py   : list of samples in that production with list of customisation to apply per sample
 * python/nanoProdCustomise.py: cutomisation functions to be used on top of standard nanoAOD cfg 
