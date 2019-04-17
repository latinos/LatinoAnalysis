#!/usr/bin/env python
from optparse import OptionParser
from LatinoAnalysis.Gardener import Gardener_cfg as cfg


#
#This script prints out the list of gardener step executed given a directory. 
#It simply reads the Gardener_cfg.py script. 
#

parser = OptionParser(usage="usage: %prog [options]")
parser.add_option("-p","--prod",dest="prod", help="Production directory", type='string', default="")
parser.add_option("-t","--type",dest="type", help="MC/DATA", type='string', default="MC")
(options, args) = parser.parse_args()

parts = options.prod.split("__")
print parts

all_steps = []

T = options.type

def printStep(step, substep=0):
    step_conf = cfg.Steps[step]
    if T == "MC" and not step_conf["do4MC"]:
        return 
    elif T == "DATA" and not step_conf["do4Data"]:
        return
    
    if step_conf["isChain"]:
        print "\t"*substep, ">>> Chain: ", step
        for subs in step_conf["subTargets"]:
            printStep(subs, substep+1)
    else:
        if "command" in step_conf:
            print "\t"*substep, "> Step: ", step, " | command: ", step_conf["command"]
        all_steps.append(step)    
    print "\t"*substep, '------------------------------------------------------'


for part in parts:
    printStep(part)

print  "\nAll steps: \n", ",".join(all_steps)
