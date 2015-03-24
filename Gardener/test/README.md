Example
====

In this example we add a new variable in the latino trees. It works only on the latino final trees, produced with the 'cmssw2latino.py' script.

    scram b -j 10    

    gardener.py adder \
                -v 'test1/F=ch1*ch2' \
                input.root output.root
