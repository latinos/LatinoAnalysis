#!/usr/bin/env python
import sys, re, os, os.path, math, copy
from optparse import OptionParser
from collections import OrderedDict
import subprocess
import optparse

# Latino Tools
import LatinoAnalysis.Gardener.hwwtools as hwwtools
from LatinoAnalysis.Tools.commonTools import *

# PostProc Class
from LatinoAnalysis.NanoProducer.NanoProdMaker import *

# ------------------------------------------------------- MAIN --------------------------------------------

if __name__ == '__main__':
    print '''
-----------------------------------------------------------------------------------
  _   _                     _____               _            _   _             
 | \ | |                   |  __ \             | |          | | (_)            
 |  \| | __ _ _ __   ___   | |__) _ __ ___   __| |_   _  ___| |_ _  ___  _ __  
 | . ` |/ _` | '_ \ / _ \  |  ___| '__/ _ \ / _` | | | |/ __| __| |/ _ \| '_ \ 
 | |\  | (_| | | | | (_) | | |   | | | (_) | (_| | |_| | (__| |_| | (_) | | | |
 |_| \_|\__,_|_| |_|\___/  |_|   |_|  \___/ \__,_|\__,_|\___|\__|_|\___/|_| |_|

-----------------------------------------------------------------------------------
'''

    usage = 'usage: %prog [options]'
    parser = optparse.OptionParser(usage)

#   # --- Cfg
#   parser.add_option("--sitescfg"  ,  dest="sitescfg"  , help="Sites Cfg" , default='LatinoAnalysis/NanoGardener/python/framework/Sites_cfg.py' , type='string')
#   parser.add_option("-m","--modcfg"  ,  dest="modcfg"  , help="Module Steps Cfg" , default='LatinoAnalysis/NanoGardener/python/framework/Steps_cfg.py' , type='string')
    parser.add_option("-d","--datacfg" ,  dest="datacfg" , help="Data Prods Cfg"   , default='LatinoAnalysis/NanoProducer/python/Productions_cfg.py' , type='string')

    # --- What to do: 
    parser.add_option("-p","--prods",   dest="prods"   , help="List of production to run on"              , default=[]     , type='string' , action='callback' , callback=list_maker('prods',','))
    parser.add_option("-T", "--selTree",   dest="selTree" , help="Select only some tree (comma separated list)" , default=[]     , type='string' , action='callback' , callback=list_maker('selTree',','))
    parser.add_option("-E", "--excTree",   dest="excTree" , help="Exclude some tree (comma separated list)" , default=[]     , type='string' , action='callback' , callback=list_maker('excTree',','))

#   # --- How to run:
    parser.add_option("-n", "--dry-run",    dest="pretend", help="(use with -v) just list the datacards that will go into this combination", default=False, action="store_true")
#   parser.add_option("-R","--redo" ,   dest="redo"    , help="Redo, don't check if tree already exists"  , default=False  , action="store_true")

# ---------------------------------------- Config
  
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

#   if os.path.exists(CMSSW+'/src/'+options.sitescfg):
#     handle = open(CMSSW+'/src/'+options.sitescfg)
#     exec(handle)
#     handle.close()
#   else:
#     print 'ERROR: Please specify the site config with -S <fileName>'
#     exit(1)


    print " Productions : " , prodList
    if len(prodList) == 0 :
      print 'ERROR: Please specify valid productions (-p <prodList>)'
      exit(1)

# ---------------------------------------- And Here we go:

    factory = NanoProdMaker() 
 
#   # Sites
#   factory._Sites       = Sites  
#   factory.configSite()

    # Setup Productions 
    factory._Productions = Productions

    # What to do
    factory._prodList    = prodList
    factory._selTree     = options.selTree
    factory._excTree     = options.excTree

#   # job mode = Interactive / Batch / Crab / DryRun
#   factory._redo        = options.redo
    factory._pretend     = options.pretend  
  
    factory.process()    

