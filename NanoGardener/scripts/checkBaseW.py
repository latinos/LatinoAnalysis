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
from LatinoAnalysis.NanoGardener.framework.PostProcMaker import *

# ------------------------------------------------------- MAIN --------------------------------------------

if __name__ == '__main__':

    usage = 'usage: %prog [options]'
    parser = optparse.OptionParser(usage)

    # --- Cfg
    parser.add_option("-d","--datacfg" ,  dest="datacfg" , help="Data Prods Cfg"   , default='LatinoAnalysis/NanoGardener/python/framework/Productions_cfg.py' , type='string')
    parser.add_option("-m","--modcfg"  ,  dest="modcfg"  , help="Module Steps Cfg" , default='LatinoAnalysis/NanoGardener/python/framework/Steps_cfg.py' , type='string')
    parser.add_option("--sitescfg"  ,  dest="sitescfg"  , help="Sites Cfg" , default='LatinoAnalysis/NanoGardener/python/framework/Sites_cfg.py' , type='string')

    # --- What to do: 
    parser.add_option("-p","--prods",   dest="prods"   , help="List of production to run on"              , default=[]     , type='string' , action='callback' , callback=list_maker('prods',','))
    parser.add_option("-i","--iniStep",   dest="iniStep"   , help="Step to restart from"                      , default='Prod' , type='string' )
    parser.add_option("-T", "--selTree",   dest="selTree" , help="Select only some tree (comma separated list)" , default=[]     , type='string' , action='callback' , callback=list_maker('selTree',','))
    parser.add_option("-E", "--excTree",   dest="excTree" , help="Exclude some tree (comma separated list)" , default=[]     , type='string' , action='callback' , callback=list_maker('excTree',','))



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
      stepList = List_Filter(Steps,'baseW').get()
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
    if len(prodList) == 0 :
      print 'ERROR: Please specify valid productions'
      exit(1)

    # Re-use factory ad minima
    factory = PostProcMaker() 
    # Sites
    factory._Sites       = Sites
    factory.configSite()

    # Setup Steps and Productions
    factory._Steps       = Steps
    factory._Productions = Productions 
    factory._stepList    = stepList
    factory._prodList    = prodList
    factory._iniStep     = options.iniStep
    factory._selTree     = options.selTree
    factory._excTree     = options.excTree

    # Loop on production
    factory.checkBaseW()     

 
