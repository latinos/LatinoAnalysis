#!/usr/bin/env python
import sys, re, os, os.path, math, copy
from optparse import OptionParser
from collections import OrderedDict

import subprocess

import optparse
import LatinoAnalysis.Gardener.hwwtools as hwwtools
from LatinoAnalysis.Tools.commonTools import *


# ------------------------------------------------------- MAIN --------------------------------------------

if __name__ == '__main__':
    print '''
--------------------------------------------------------------------------------------------
   _  __                 ___           __    ___                           _          
  / |/ /__ ____  ___    / _ \___  ___ / /_  / _ \_______  _______ ___ ___ (_)__  ___ _
 /    / _ `/ _ \/ _ \  / ___/ _ \(_-</ __/ / ___/ __/ _ \/ __/ -_|_-<(_-</ / _ \/ _ `/
/_/|_/\_,_/_//_/\___/ /_/   \___/___/\__/ /_/  /_/  \___/\__/\__/___/___/_/_//_/\_, / 
                                                                               /___/  
--------------------------------------------------------------------------------------------
'''

    usage = 'usage: %prog [options]'
    parser = optparse.OptionParser(usage)

    # --- Cfg
    parser.add_option("-m","--modcfg"  ,  dest="modcfg"  , help="Module Steps Cfg" , default='LatinoAnalysis/NanoGardener/python/framework/StepsProd_cfg.py' , type='string')
    parser.add_option("-d","--datacfg" ,  dest="datacfg" , help="Data Prods Cfg"   , default='LatinoAnalysis/NanoGardener/python/framework/DataProd_cfg.py' , type='string')

    # --- What to do: 
    parser.add_option("-p","--prods",   dest="prods"   , help="List of production to run on"              , default=[]     , type='string' , action='callback' , callback=list_maker('prods',','))
    parser.add_option("-s","--steps",   dest="steps"   , help="list of Steps to produce"                  , default=[]     , type='string' , action='callback' , callback=list_maker('steps',','))
    parser.add_option("-i","--iniStep",   dest="iniStep"   , help="Step to restart from"                      , default='Prod' , type='string' )
    parser.add_option("-T", "--selTree",   dest="selTree" , help="Select only some tree (comma separated list)" , default=[]     , type='string' , action='callback' , callback=list_maker('selTree',','))
    parser.add_option("-E", "--excTree",   dest="excTree" , help="Exclude some tree (comma separated list)" , default=[]     , type='string' , action='callback' , callback=list_maker('excTree',','))

    # --- How to run:
    parser.add_option("-n", "--dry-run",    dest="pretend", help="(use with -v) just list the datacards that will go into this combination", default=False, action="store_true")
    parser.add_option("-R","--redo" ,   dest="redo"    , help="Redo, don't check if tree already exists"  , default=False  , action="store_true")
    parser.add_option("-b","--batch",   dest="runBatch", help="Run in batch"                              , default=False  , action="store_true")
    parser.add_option("-Q" , "--queue" ,  dest="queue"    , help="Batch Queue"  , default="8nh" , type='string' )
    # TODO: parser.add_option("-g","--grid",    dest="runGrid", help="Run in Grid"                              , default=False  , action="store_true")

# ---------------------------------------- Config

    # --- Job splitting:
    parser.add_option("-S","--batchSplit", dest="batchSplit", help="Splitting mode for batch jobs"        , default='Target', type='string' , action='callback' , callback=list_maker('batchSplit',','))

  
    # Parse options 
    (options, args) = parser.parse_args()
    CMSSW=os.environ["CMSSW_BASE"]

    # Load Cfg + Filter
    if os.path.exists(CMSSW+'/src/'+options.datacfg):
       handle = open(CMSSW+'/src/'+options.datacfg)
       exec(handle)
       handle.close()
       prodList = List_Filter(Productions,options.prods).get()

    if os.path.exists(CMSSW+'/src/'+options.modcfg):
       handle = open(CMSSW+'/src/'+options.modcfg)
       exec(handle)
       handle.close()
       stepList = List_Filter(Steps,options.steps).get()

    print " Productions : " , prodList
    print " Steps       : " , stepList

    # Compile all root macros before sending jobs
#   pathRootMacro = CMSSW + '/src/LatinoAnalysis/Gardener/python/variables/'
#   for fn in os.listdir(pathRootMacro):
#     if os.path.isfile(pathRootMacro+fn) and ( fn.endswith('.C') or fn.endswith('.cc') ):
#       try:
#         ROOT.gROOT.LoadMacro(pathRootMacro+fn+'+g')
#       except RuntimeError:
#         ROOT.gROOT.LoadMacro(pathRootMacro+fn+'++g')

