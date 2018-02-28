#!/usr/bin/env python

import optparse
import LatinoAnalysis.Gardener.hwwtools as hwwtools

# functions used in everyday life ...
from LatinoAnalysis.Tools.commonTools import *
from LatinoAnalysis.Tools.batchTools  import *

def lim_compute():
    nGridPoints = {}
    nGridPoints['1D'] = '100'
    nGridPoints['2D'] = '10000'    

    commands={}
    scanList=[]
    for iComb in cutsVal:
      for iVar in variables :
        for iDim in ['1D','2D'] :
          if iDim in acoupling['ScanConfig'] and len(acoupling['ScanConfig'][iDim]) > 0 :
            for iScan in acoupling['ScanConfig'][iDim]:
               scanList.append(iScan.replace(":","_")+'_'+iComb+'_'+iVar)
               datacard_dir_ac = os.getcwd()+'/'+opt.outputDirDatacard+'/'+iComb+'/'+iVar+'_'+iScan.replace(":","_")
               # Expected Limits
               command='cd '+datacard_dir_ac+' ; '
               command+='combine aC_'+iComb+'.root -M MultiDimFit -n Exp -m 125 --floatOtherPOIs=0 --algo=grid --points='+nGridPoints[iDim]+' --minimizerStrategy=2 -t -1 --expectSignal=1 '
               for iPOI in iScan.split(":") : command+='-P '+iPOI+' '
               command+=' &> LogExp.txt ; cd - '
               commands['Exp,'+iScan.replace(":","_")+'_'+iComb+'_'+iVar]= command 
               # Observed Limits
               command='cd '+datacard_dir_ac+' ; '
               command+='combine aC_'+iComb+'.root -M MultiDimFit -n Obs -m 125 --floatOtherPOIs=0 --algo=grid --points='+nGridPoints[iDim]+' --minimizerStrategy=2 '
               for iPOI in iScan.split(":") : command+='-P '+iPOI+' '
               command+=' &> LogObs.txt ; cd - '
               if opt.unblind: commands['Obs,'+iScan.replace(":","_")+'_'+iComb+'_'+iVar] = command

    if opt.batch: 
      if opt.unblind : targetList = ['Exp','Obs']
      else           : targetList = ['Exp']
      jobs = batchJobs('mkACLim',opt.tag,scanList,targetList,'Steps,Targets','',False)
      for iJob in commands : jobs.Add(iJob.split(",")[1],iJob.split(",")[0],commands[iJob]) 
      jobs.Sub()
    else:
      for iCommand in commands : os.system(iCommand)

def lim_harvest():
    print "Hello"

def lim_plot():
    print "Hello"

if __name__ == '__main__':

    usage = 'usage: %prog [options]'
    parser = optparse.OptionParser(usage)

    parser.add_option('--tag'            , dest='tag'            , help='Tag used for the shape file name'           , default=None)
    parser.add_option('--outputDirDatacard' , dest='outputDirDatacard' , help='output directory'                          , default='./')
    parser.add_option('--combineLocation'   , dest='combineLocation'   , help='Combine CMSSW Directory'                   , default='./')
    parser.add_option('--accfg'          , dest='accfg'          , help='AC coupling dictionary' , default='acoupling.py' , type='string' )
    parser.add_option('--combcfg'           , dest='combcfg'           , help='Combination disctionnary'                  , default='NONE')
    parser.add_option('--step'              , dest='step'              , help='Step=compute/harvest/plot'                 , default='NONE')
    parser.add_option('--unblind'           , dest='unblind'           , help='Unblind'              , action='store_true', default=False)
    parser.add_option('--batch'             , dest='batch'             , help='Batch job(s)'         , action='store_true', default=False)
    parser.add_option('--cutList'        , dest='cutList'        , help='cut list to process' , default=[], type='string' , action='callback' , callback=list_maker('cutList',','))
    parser.add_option('--varList'        , dest='varList'        , help='var list to process' , default=[], type='string' , action='callback' , callback=list_maker('varList',','))
    parser.add_option('--scanList'       , dest='scanList'        , help='scan list to process' , default=[], type='string' , action='callback' , callback=list_maker('scanList',','))


    # read default parsing options as well
    hwwtools.addOptions(parser)
    hwwtools.loadOptDefaults(parser)
    (opt, args) = parser.parse_args()

    print " outputDirDatacard  = ", opt.outputDirDatacard
    print " configuration file = ", opt.pycfg
    print " AC config          = ", opt.accfg
    print " Combination Cfg    = ", opt.combcfg
    print " UNBLIND ?          = ", opt.unblind



    variables = {}
    cuts = {}
    if os.path.exists(opt.cutsFile) :
      handle = open(opt.cutsFile,'r')
      exec(handle)
      handle.close()

    # And COMBINATION 
    combs = {}
    cutsVal = {}
    if os.path.exists(opt.combcfg) :
      handle = open(opt.combcfg,'r')
      exec(handle)
      handle.close()
      variables['comb'] = {}
      for iComb in combs : cutsVal[iComb] = {}

    # ELSE use default set of cards and cuts 
    else:

      if os.path.exists(opt.variablesFile) :
        handle = open(opt.variablesFile,'r')
        exec(handle)
        handle.close()
      for iCut in cuts : cutsVal[iCut] = {}
    


    # acoupling = {}     
    h=open(opt.accfg,'r')
    exec(h)

    # Cuts Preselection
    if len(opt.cutList)>0:
      cut2del=[]
      for iCut in cutsVal:
        if not iCut in opt.cutList : cut2del.append(iCut)
      for iCut in cut2del : del cutsVal[iCut]

    # Variable Preselection
    if len(opt.varList)>0:
      var2del=[]
      for iVar in variables:
        if not iVar in opt.varList : var2del.append(iVar)
      for iVar in var2del : del variables[iVar]

    # Scans Preselection
    if len(opt.scanList)>0:
      dim2del=[]
      for iDim in ['1D','2D','3D'] :
        if iDim in acoupling['ScanConfig'] :
          scan2keep=[]
          for iScan in acoupling['ScanConfig'][iDim] :
            if iScan in opt.scanList : scan2keep.append(iScan)
          acoupling['ScanConfig'][iDim] = scan2keep
          if len(acoupling['ScanConfig'][iDim]) == 0 : dim2del.append(iDim)
      for iDim in dim2del : del acoupling['ScanConfig'][iDim] 

    print " Cuts               = " , cutsVal.keys()
    print " Variables          = " , variables.keys()
    for iDim in ['1D','2D'] :
      if iDim in acoupling['ScanConfig'] : print ' ', iDim , ' Scans  : '  , acoupling['ScanConfig'][iDim]

    print " "
    print " ----------------------- step = " , opt.step , " ----------------------------"
    print " "
    # compute/harvest/plot

    if   opt.step == "compute" : lim_compute()
    elif opt.step == "harvest" : lim_harvest()
    elif opt.step == "plot"    : lim_plot()
    else:
      print "STEP UNKNOWN !!!!!"
    




