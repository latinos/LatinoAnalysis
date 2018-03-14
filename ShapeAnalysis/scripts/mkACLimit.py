#!/usr/bin/env python

import optparse
import LatinoAnalysis.Gardener.hwwtools as hwwtools

# functions used in everyday life ...
from LatinoAnalysis.Tools.commonTools import *
from LatinoAnalysis.Tools.batchTools  import *
from LatinoAnalysis.Tools.combPlots   import *

# Job Splitting
nGridPoints = {}
nGridPoints['1D'] = 100
nGridPoints['2D'] = 10000
nGridSplit = {}
nGridSplit['1D'] = 1
nGridSplit['2D'] = 20



def lim_compute():

    commands={}
    scanList=[]
    for iComb in cutsVal:
      for iVar in variables :
        for iDim in ['1D','2D'] :
          if iDim in acoupling['ScanConfig'] and len(acoupling['ScanConfig'][iDim]) > 0 :
            for iScan in acoupling['ScanConfig'][iDim]:
               datacard_dir_ac = os.getcwd()+'/'+opt.outputDirDatacard+'/'+iComb+'/'+iVar+'_'+iScan.replace(":","_")
               if opt.batch:
                 nJobs=nGridSplit[iDim]
                 nPointsJob=nGridPoints[iDim]/nGridSplit[iDim]
               else:
                 nJobs=1
                 nPointsJob=nGridPoints[iDim]
               for iJob in xrange(1,nGridSplit[iDim]+1):
                 namePF=''
                 pointPF=''
                 if not nGridSplit[iDim] == 1:
                   namePF='_'+str(iJob)
                   FPoint=(iJob-1)*nPointsJob
                   LPoint=(iJob)*nPointsJob-1
                   pointPF=' --firstPoint '+str(FPoint)+' --lastPoint '+str(LPoint)+' '
                 scanList.append(iScan.replace(":","_")+'_'+iComb+'_'+iVar+namePF)
                 # Expected Limits
                 command='cd '+datacard_dir_ac+' ; '
                 command+='combine aC_'+iComb+'.root -M MultiDimFit -n Exp_'+iScan.replace(":","_")+'_'+iComb+'_'+iVar+namePF+' -m 125 --floatOtherPOIs=0 --algo=grid --points='+str(nGridPoints[iDim])+pointPF+' --minimizerStrategy=2 -t -1 --expectSignal=1 '
                 for iPOI in iScan.split(":") : command+='-P '+iPOI+' '
                 command+=' &> LogExp.txt ; cd - '
                 commands['Exp,'+iScan.replace(":","_")+'_'+iComb+'_'+iVar+namePF]= command 
                 # Observed Limits
                 command='cd '+datacard_dir_ac+' ; '
                 command+='combine aC_'+iComb+'.root -M MultiDimFit -n Obs_'+iScan.replace(":","_")+'_'+iComb+'_'+iVar+namePF+' -m 125 --floatOtherPOIs=0 --algo=grid --points='+str(nGridPoints[iDim])+pointPF+' --minimizerStrategy=2 '
                 for iPOI in iScan.split(":") : command+='-P '+iPOI+' '
                 command+=' &> LogObs.txt ; cd - '
                 if opt.unblind: commands['Obs,'+iScan.replace(":","_")+'_'+iComb+'_'+iVar+namePF] = command

    if opt.batch: 
      if opt.unblind : targetList = ['Exp','Obs']
      else           : targetList = ['Exp']
      jobs = batchJobs('mkACLim',opt.tag,scanList,targetList,'Steps,Targets','',False)
      for iJob in commands : jobs.Add(iJob.split(",")[1],iJob.split(",")[0],commands[iJob]) 
      jobs.Sub()
    else:
      for iJob in commands : os.system(commands[iJob])

def lim_harvest():
    
    for iComb in cutsVal:
      for iVar in variables :
        for iDim in ['1D','2D'] :
          if iDim in acoupling['ScanConfig'] and len(acoupling['ScanConfig'][iDim]) > 0 :
            for iScan in acoupling['ScanConfig'][iDim]:
               datacard_dir_ac = os.getcwd()+'/'+opt.outputDirDatacard+'/'+iComb+'/'+iVar+'_'+iScan.replace(":","_")
               if opt.batch and not nGridSplit[iDim] == 1:
                 nJobs=nGridSplit[iDim]
                 nPointsJob=nGridPoints[iDim]/nGridSplit[iDim]
                 LimTypes=['Exp']
                 if opt.unblind: LimTypes.append('Obs') 
                 for iLim in LimTypes:
                   srcFiles=[]
                   for iJob in xrange(1,nGridSplit[iDim]+1): 
                     allDone=True
                     pidFile = jobDir+'mkACLim__'+opt.tag+'/mkACLim__'+opt.tag+'__'+iScan.replace(":","_")+'_'+iComb+'_'+iVar+'_'+str(iJob)+'__'+iLim+'.jid'
                     if os.path.isfile(pidFile) :
                       print '--> Job Running : ',pidFile
                       allDone=False
                     srcFile = datacard_dir_ac+'/higgsCombine'+iLim+'_'+iScan.replace(":","_")+'_'+iComb+'_'+iVar+'_'+str(iJob)+'.MultiDimFit.mH125.root'
                     srcFiles.append(srcFile)
                     if not os.path.isfile(srcFile) :
                       print '--> Missing root file: '+srcFile 
                       allDone=False
                     if allDone :
                       command = 'cd '+datacard_dir_ac+' ; hadd -f higgsCombine'+iLim+'_'+iScan.replace(":","_")+'_'+iComb+'_'+iVar+'.MultiDimFit.mH125.root '
                       cleanup = ''
                       for iFile in srcFiles:
                         command+=' '+iFile
                         cleanup+='rm '+iFile+' ; '
                       os.system(command) 
                       # os.system(cleanup)

def lim_plot():

    for iComb in cutsVal:
      for iVar in variables :
        for iDim in ['1D','2D'] :
          if iDim in acoupling['ScanConfig'] and len(acoupling['ScanConfig'][iDim]) > 0 :
            for iScan in acoupling['ScanConfig'][iDim]:
               datacard_dir_ac = os.getcwd()+'/'+opt.outputDirDatacard+'/'+iComb+'/'+iVar+'_'+iScan.replace(":","_")
               LimFiles={}
               LimFiles['Exp'] = datacard_dir_ac+'/higgsCombineExp_'+iScan.replace(":","_")+'_'+iComb+'_'+iVar+'.MultiDimFit.mH125.root' 
               if opt.unblind: 
                 LimFiles['Obs'] = datacard_dir_ac+'/higgsCombineObs_'+iScan.replace(":","_")+'_'+iComb+'_'+iVar+'.MultiDimFit.mH125.root'
               print LimFiles
               blind = not opt.unblind
               plot=combPlot(opt.outputDirPlots,blind,False,False,legend['lumiEnrg'])
               plotDic={}
               plotDic['LegTitle'] = acoupling['combsName'][iComb] 
               plotDic['Keys'] = iScan.split(":")
               plotDic['AxisTitle'] = []
               plotDic['Min'] = []
               plotDic['Max'] = []
               plotDic['MinPlt'] = []
               plotDic['MaxPlt'] = []
               for iKey in plotDic['Keys'] : 
                 plotDic['AxisTitle'].append(acoupling['operatorLatex'][iKey]+' ['+acoupling['operatorUnit'][iKey]+']') 
                 plotDic['Min'].append(acoupling['operatorRange'][iKey][0])
                 plotDic['Max'].append(acoupling['operatorRange'][iKey][1]) 
                 plotDic['MinPlt'].append(acoupling['operatorPlot'][iKey][0]) 
                 plotDic['MaxPlt'].append(acoupling['operatorPlot'][iKey][1])
               # 2*NLL Limits:
               plotDic['MinPlt'].append(0.)
               plotDic['MaxPlt'].append(10.)

               plotName = iScan.replace(":","_")+'_'+iComb+'_'+iVar
               if iDim == '1D' : plot.MDF1D(plotName,plotDic,LimFiles)
               if iDim == '2D' : plot.MDF2D(plotName,plotDic,LimFiles)

if __name__ == '__main__':


    usage = 'usage: %prog [options]'
    parser = optparse.OptionParser(usage)

    parser.add_option('--tag'            , dest='tag'            , help='Tag used for the shape file name'           , default=None)
    parser.add_option('--outputDirPlots' , dest='outputDirPlots' , help='output directory'                           , default='./')
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

    opt.outputDirPlots+='_ACLimits'

    groupPlot = OrderedDict()
    plot = {}
    legend = {}
    if os.path.exists(opt.plotFile) :
      handle = open(opt.plotFile,'r')
      exec(handle)
      handle.close()


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
    




