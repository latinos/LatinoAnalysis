#!/usr/bin/env python
import sys, re, os, os.path, math, copy
argv = sys.argv
sys.argv = argv[:1]
from optparse import OptionParser
from collections import OrderedDict
import subprocess
import optparse

# Latino Tools
import LatinoAnalysis.Gardener.hwwtools as hwwtools
from LatinoAnalysis.Tools.commonTools import *

# PostProc Class
from LatinoAnalysis.NanoGardener.framework.PostProcMaker import *

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

    sys.argv = argv

    usage = 'usage: %prog [options]'
    parser = optparse.OptionParser(usage)

    # --- Cfg
    parser.add_option("--sitescfg"  ,  dest="sitescfg"  , help="Sites Cfg" , default='LatinoAnalysis/NanoGardener/python/framework/Sites_cfg.py' , type='string')
    parser.add_option("-m","--modcfg"  ,  dest="modcfg"  , help="Module Steps Cfg" , default='LatinoAnalysis/NanoGardener/python/framework/Steps_cfg.py' , type='string')
    parser.add_option("-d","--datacfg" ,  dest="datacfg" , help="Data Prods Cfg"   , default='LatinoAnalysis/NanoGardener/python/framework/Productions_cfg.py' , type='string')

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
    parser.add_option("-c","--crab",   dest="runCrab", help="Run in batch"                              , default=False  , action="store_true")
    parser.add_option("-Q" , "--queue" ,  dest="queue"    , help="Batch Queue"  , default=None , type='string' )
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
    else:
      print 'ERROR: Please specify the input data config with -d <fileName>'
      exit(1)  

    if os.path.exists(CMSSW+'/src/'+options.modcfg):
      handle = open(CMSSW+'/src/'+options.modcfg)
      exec(handle)
      handle.close()
      stepList = List_Filter(Steps,options.steps).get()
    else:
      print 'ERROR: Please specify the input module config with -m <fileName>' 
      exit(1)

    if os.path.exists(CMSSW+'/src/'+options.sitescfg):
      handle = open(CMSSW+'/src/'+options.sitescfg)
      exec(handle)
      handle.close()
    else:
      print 'ERROR: Please specify the site config with -S <fileName>'
      exit(1)


    print " Productions : " , prodList
    print " Steps       : " , stepList
    if len(prodList) == 0 or len(stepList) == 0 :
      print 'ERROR: Please specify valid productions (-p <prodList>) and/or steps (-s <stepList>)'
      exit(1)
 


# ---------------------------------------- Compile all root macros before sending jobs

    if options.runBatch :
      #pathLib = CMSSW + '/lib/'+os.listdir(CMSSW + '/lib/')[0]+'/'
      #for fn in ["libZZMatrixElementMELA.so", "libMelaAnalyticsCandidateLOCaster.so"]: # Needed to compile MELA macros
      #  if os.path.isfile(pathLib+fn):
      #    ROOT.gSystem.Load(fn)
      pathRootMacro = CMSSW + '/src/LatinoAnalysis/Gardener/python/variables/'
      for fn in os.listdir(pathRootMacro):
        if os.path.isfile(pathRootMacro+fn) and ( fn.endswith('.C') or fn.endswith('.cc') ):
          try:
            ROOT.gROOT.LoadMacro(pathRootMacro+fn+'+g')
          except RuntimeError:
            ROOT.gROOT.LoadMacro(pathRootMacro+fn+'++g')
      pathRootMacro = CMSSW + '/src/LatinoAnalysis/NanoGardener/python/modules/'
      for fn in os.listdir(pathRootMacro):
        if os.path.isfile(pathRootMacro+fn) and ( fn.endswith('.C') or fn.endswith('.cc') ):
          try:
            ROOT.gROOT.LoadMacro(pathRootMacro+fn+'+g')
          except RuntimeError:
            ROOT.gROOT.LoadMacro(pathRootMacro+fn+'++g')

# ---------------------------------------- And Here we go:

    factory = PostProcMaker() 
 
    # Sites
    factory._Sites       = Sites  
    factory.configSite()

    # Setup Steps and Productions 
    factory._Steps       = Steps
    factory._Productions = Productions

    # What to do
    factory._stepList    = stepList
    factory._prodList    = prodList
    factory._iniStep     = options.iniStep
    factory._selTree     = options.selTree
    factory._excTree     = options.excTree

    # job mode = Interactive / Batch / Crab / DryRun
    factory._redo        = options.redo
    factory._pretend     = options.pretend  
    if options.runBatch  : 
                             factory._jobMode = 'Batch'
                             factory.configBatch(options.queue)
    elif options.runCrab   : factory._jobMode = 'Crab'
    else                   : factory._jobMode = 'Interactive'
   
    factory.process()    

