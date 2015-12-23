mkGardener usage
====

How to use mkGardener, automatic handling of gardener modules over lxbatch

count weights: 
    ./mkGardener.py -p 21Oct_25ns_MC -b -s  mcwghtcount -S Target -Q 2nd

apply weitghts on top:
    ./mkGardener.py -p 21Oct_25ns_MC -b -s MC -i mcwghtcount -S Target -Q 2nd

and apply l2sel on top:
    ./mkGardener.py -p 21Oct_25ns_MC -b -s l2sel -i mcwghtcount__MC -S Target -Q 2nd

and for data:
    ./mkGardener.py -p XXXXXX -b -s l2sel -S Target -Q 2nd
where XXX is defined in python/Gardener_cfg.py

You can also do 
    -T <SampleName>
for a single sample
and 
    -R
to overwrite and redo

Adding a gardener module should be done in python/Gardener_cfg.py
If you remove "-b" then jobs are run interactively


General instructions
====

    ./mkGardener.py

    -p -->   list of production to run on (e.g. 21Oct_25ns_MC, 21Oct_Run2015D_05Oct2015, ..., as defined in python/Gardener_cfg.py)
    -s -->   list of Steps to produce (e.g. MC, as defined in python/Gardener_cfg.py)
    -i -->   step to restart from (e.g. mcwghtcount)
    
    -S -->   splitting mode for batch jobs. batchSplit = How to split jobs (by Step, Target)
    FIXME DEFINITION


    
    
    
    