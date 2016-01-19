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

    -p (prods)         -->   list of production to run on (e.g. 21Oct_25ns_MC, 21Oct_Run2015D_05Oct2015, ..., as defined in python/Gardener_cfg.py)
    -s (steps)         -->   list of Steps to produce (e.g. MC, as defined in python/Gardener_cfg.py)
    -i (iStep)         -->   step to restart from (e.g. mcwghtcount or mcwghtcount__MC__l2sel__hadd). It is used as folder name on eos.
                             if not iStep in Steps: options.iStep = 'Prod', that means it's starting from eos of GRID production
    -O (output-target) -->   alternative location on eos, e.g. /eos/user/a/amassiro/Test/ (note that it is still IT eos)
    
    -S (batchSplit)    -->   splitting mode for batch jobs. batchSplit = How to split jobs (by Step, Target)
    
    FIXME DEFINITION


In LatinoAnalysis/Tools/python/userConfig.py (rename from userConfig_TEMPLATE.py) definition of the jobs and working directory
is set, as well as pile-up reference distribution:

    e.g.:
       jobDir 
       workDir
       puData
    
    
Examples
====

    mkGardener.py -p 21Oct_25ns_MC   -b   -s wwNLL   -i mcwghtcount__MC   -S Target   -Q 2nd
    mkGardener.py -p 21Oct_25ns_MC   -b   -s wwNLL   -i mcwghtcount__MC   -S Target   -Q 2nd    -R
    
    mkGardener.py -p 21Oct_25ns_MC   -b   -s wwNLL   -i mcwghtcount__MC   -S Target   -Q 2nd    -O /eos/user/a/amassiro/Test/
    
    mkGardener.py -p 21Oct_25ns_MC   -b   -s wwNLL   -i mcwghtcount__MC   -S Target   -Q 2nd    -O /eos/user/a/amassiro/Test/
    
    mkGardener.py -p 21Oct_25ns_MC   -b   -s JESup   -i mcwghtcount__MC   -S Target   -Q 2nd    -O /eos/user/a/amassiro/Test/
    mkGardener.py -p 21Oct_25ns_MC   -b   -s JESdo   -i mcwghtcount__MC   -S Target   -Q 2nd    -O /eos/user/a/amassiro/Test/
    
    mkGardener.py -p 21Oct_25ns_MC   -b   -s JESup   -i mcwghtcount__MC__l2sel__hadd   -S Target   -Q 2nd    -O /eos/user/a/amassiro/Test/
    mkGardener.py -p 21Oct_25ns_MC   -b   -s JESdo   -i mcwghtcount__MC__l2sel__hadd   -S Target   -Q 2nd    -O /eos/user/a/amassiro/Test/
    
    mkGardener.py -p 21Oct_25ns_MC   -b   -s l2sel   -i mcwghtcount__MC__l2sel__hadd   -S Target   -Q 2nd    -O /eos/user/a/amassiro/Test/
    
to run on data:

    mkGardener.py -p 21Oct_Run2015D_05Oct2015   -b   -s l2sel      -S Target   -Q 2nd    -O /eos/user/a/amassiro/Test/
    mkGardener.py -p 21Oct_Run2015D_PromptReco  -b   -s l2sel      -S Target   -Q 2nd    -O /eos/user/a/amassiro/Test/


    
get access to eos IT:

    source /afs/cern.ch/project/eos/installation/user/etc/setup.sh

see https://cern.service-now.com/service-portal/article.do?n=KB0001998&s=CERNBox

Check:

    /afs/cern.ch/project/eos/installation/0.3.84-aquamarine.user/bin/eos.select ls  -alrth /eos/user/a/amassiro/Test/21Oct_25ns_MC/mcwghtcount__MC__wwNLL/latino_WWTo2L2Nu.root

    
    
    


    
    
    
    