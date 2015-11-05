#!/usr/bin/env python
import sys, re, os, os.path
from optparse import OptionParser
import ROOT

from LatinoAnalysis.Tools.userConfig  import *
from LatinoAnalysis.Tools.commonTools import *
from LatinoAnalysis.Tools.batchTools  import *
from LatinoAnalysis.Gardener.Gardener_cfg import *

# ------------------------ baseW -------------------------

def GetBaseW(inTree,iTarget,id_iTarget,isData,db):
   if isData : return '1'
   else:
     xs = db.get(id_iTarget) 
     if xs == '' : return '1'
     else:
       #print 'Opening: ',inTree
       fileIn = ROOT.TFile.Open(inTree, "READ")
       fileIn.ls()
       nEvt = fileIn.Get('totalEvents').GetBinContent(1) 
       fileIn.Close()
       baseW = float(xs)*1000./nEvt
       return str(baseW)

# ------------------------------------------------------- MAIN --------------------------------------------

parser = OptionParser(usage="usage: %prog [options]")

parser.add_option("-p","--prods",   dest="prods"   , help="List of production to run on"  ,  default=[]     , type='string' , action='callback' , callback=list_maker('prods',','))
parser.add_option("-s","--steps",   dest="steps"   , help="list of Steps to produce"      ,  default=[]     , type='string' , action='callback' , callback=list_maker('steps',','))
parser.add_option("-i","--iStep",   dest="iStep"   , help="Step to restart from"          ,  default='Prod' , type='string' ) 
parser.add_option("-R","--redo" ,   dest="redo"    , help="Redo all trees"                ,  default=False  , action="store_true")
parser.add_option("-b","--batch",   dest="runBatch", help="Run in batch"                  ,  default=False  , action="store_true")
parser.add_option("-S","--batchSplit", dest="batchSplit", help="Splitting mode for batch jobs" , default=[], type='string' , action='callback' , callback=list_maker('batchSplit',','))
parser.add_option("-q", "--quiet",    dest="quiet",     help="Quiet logs",                default=False, action="store_true")
parser.add_option("-n", "--dry-run",    dest="pretend",     help="(use with -v) just list the datacards that will go into this combination", default=False, action="store_true")
parser.add_option("-T", "--selTree",   dest="selTree" , help="Select only some tree (comma separated list)" , default=[]     , type='string' , action='callback' , callback=list_maker('selTree',','))
parser.add_option("-E", "--excTree",   dest="excTree" , help="Exclude some tree (comma separated list)" , default=[]     , type='string' , action='callback' , callback=list_maker('excTree',','))

# Parse options and Filter
(options, args) = parser.parse_args()
prodList = List_Filter(Productions,options.prods).get()
stepList = List_Filter(Steps,options.steps).get()

CMSSW=os.environ["CMSSW_BASE"]



# Loop on input productions
for iProd in prodList :
  samples = {}
  prodDir = 'NONE'
  print '----------- Running on production: '+iProd

  # Load sample DB
  prodFile=CMSSW+'/src/'+Productions[iProd]['samples']
  handle = open(prodFile,'r')
  for iLine in handle.read().split('\n') : 
    if 'samples' in iLine : exec(iLine)  
    if 'config.Data.outLFNDirBase' in iLine : prodDir=iLine.split('=')[1].replace('\'','').replace(' ','')
  handle.close()

  # Load x-section DB

  xsDB = xsectionDB(Productions[iProd]['gDocID'])
    
  # Find existing Input files 
  if not options.iStep in Steps: options.iStep = 'Prod'
  if options.iStep == 'Prod' : 
    fileCmd = '/afs/cern.ch/project/eos/installation/0.3.84-aquamarine/bin/eos.select ls '+prodDir+Productions[iProd]['dirExt']
  else:
    fileCmd = '/afs/cern.ch/project/eos/installation/0.3.84-aquamarine.user/bin/eos.select ls '+eosTargBase+'/'+iProd+'/'+options.iStep
  print fileCmd
  proc=subprocess.Popen(fileCmd, stderr = subprocess.PIPE,stdout = subprocess.PIPE, shell = True)
  out, err = proc.communicate()
  FileInList=string.split(out)
  #print FileInList
 
  # Loop on Steps:
  for iStep in stepList:
    if ( not Productions[iProd]['isData'] and Steps[iStep]['do4MC'] ) or ( Productions[iProd]['isData'] and Steps[iStep]['do4Data'] ) :
      print '---------------- for Step : ',iStep
      targetList=[]
      # Validate targets tree
      fileCmd = '/afs/cern.ch/project/eos/installation/0.3.84-aquamarine.user/bin/eos.select ls '+eosTargBase+'/'+iProd+'/'+iStep
      proc=subprocess.Popen(fileCmd, stderr = subprocess.PIPE,stdout = subprocess.PIPE, shell = True)
      out, err = proc.communicate()
      FileExistList=string.split(out)
      #print FileExistList
      for iSample in samples : 
        # Tree selector
        selectSample=True
        # ... from options
        if len(options.selTree) > 0 :
          if not iSample in options.selTree: selectSample=False
        if len(options.excTree) > 0 :
          if iSample in options.excTree : selectSample=False
        # ... From iStep 
        if 'onlySample' in Steps[iStep] :
          if len(Steps[iStep]['onlySample']) > 0 :
            if not iSample in Steps[iStep]['onlySample'] : selectSample=False
        if 'excludeSample' in Steps[iStep] :
          if len(Steps[iStep]['excludeSample']) > 0 :
            if iSample in Steps[iStep]['excludeSample'] : selectSample=False  
        #if not iSample == 'DYJetsToLL_M-10to50' : selectSample=False
        iTree = 'latino_'+iSample+'.root'
        if iTree in FileInList: 
          if options.redo and selectSample:
            targetList.append(iSample)
          else:
            if not iTree in FileExistList and selectSample: targetList.append(iSample)
      #print targetList  

      # Create Jobs Dictionary
      list=[]
      list.append(iStep)
      options.batchSplit+=',Steps'
      if options.runBatch: jobs = batchJobs('Gardening',iProd,list,targetList,options.batchSplit)    

      # Create Output Directory on eos
      if options.iStep == 'Prod' :
        os.system('/afs/cern.ch/project/eos/installation/0.3.84-aquamarine.user/bin/eos.select mkdir -p '+eosTargBase+'/'+iProd+'/'+iStep)
      else:
        os.system('/afs/cern.ch/project/eos/installation/0.3.84-aquamarine.user/bin/eos.select mkdir -p '+eosTargBase+'/'+iProd+'/'+options.iStep+'__'+iStep)

      # Do some preliminary actions for some Steps

 

      # And now do/create to job for each target
      for iTarget in targetList: 
        id_iTarget=samples[iTarget][1][1].replace('id=','')
        print iTarget, id_iTarget
        # Stage in   
        if options.iStep == 'Prod' :
          inTree  ='root://eoscms.cern.ch//eos/cms'+prodDir+Productions[iProd]['dirExt']+'/latino_'+iTarget+'.root'
        else:
          inTree  ='root://eosuser.cern.ch/'+eosTargBase+'/'+iProd+'/'+options.iStep+'/latino_'+iTarget+'.root'
        oriTree = inTree
        wDir  =workDir+'/Gardening__'+iProd+'__'+iStep
        if not os.path.exists(wDir) : os.system('mkdir -p '+wDir) 
        if   options.runBatch: command=''
        else:                  command='cd '+wDir+' ; '

        # Chains of subTargets
        if 'isChain' in Steps[iStep] and Steps[iStep]['isChain']:
          iName=''
          cStep=0

          for iSubStep in  Steps[iStep]['subTargets'] :
            cStep+=1
            
            # Tree selector
            selectSample=True
            # ... From iStep
            if 'onlySample' in Steps[iSubStep] :
              if len(Steps[iSubStep]['onlySample']) > 0 :
                if not iSample in Steps[iSubStep]['onlySample'] : selectSample=False
            if 'excludeSample' in Steps[iSubStep] :
              if len(Steps[iSubStep]['excludeSample']) > 0 :
                if iSample in Steps[iSubStep]['excludeSample'] : selectSample=False

            if cStep == 1 :
              iName=iSubStep
            else:
              iName+='__'+iSubStep
              if selectSample : inTree  = outTree
            if selectSample : 
              outTree ='latino_'+iTarget+'__'+iName+'.root'
              command+=Steps[iSubStep]['command']+' '+inTree+' '+outTree +' ; '  
            
        # single Target
        else:
          outTree ='latino_'+iTarget+'__'+iStep+'.root'
          command+=Steps[iStep]['command']+' '+inTree+' '+outTree +' ; '

        # Fix baseW if needed
        baseW = GetBaseW(oriTree,iTarget,id_iTarget,Productions[iProd]['isData'],xsDB)
        command = command.replace('RPLME_baseW',baseW)

        # Fix PU data 
        puData = '/afs/cern.ch/user/p/piedra/work/pudata.root' 
        command = command.replace('RPLME_puData',puData)  

        # Stage Out
        if options.iStep == 'Prod' :
          command+='xrdcp '+outTree+' root://eosuser.cern.ch/'+eosTargBase+'/'+iProd+'/'+iStep+'/latino_'+iTarget+'.root'
        else:
          command+='xrdcp '+outTree+' root://eosuser.cern.ch/'+eosTargBase+'/'+iProd+'/'+options.iStep+'__'+iStep+'/latino_'+iTarget+'.root'
        command+='; rm '+outTree
        logFile=wDir+'/log__'+iTarget+'.log'
        if options.quiet :
          command += ' 2>&1 > /dev/null \n' 
        else:
          command += ' 2>&1 | tee '+logFile+' \n'  
        if options.pretend : print command
        else :
          if  options.runBatch: jobs.Add(iStep,iTarget,command)
          else:                 os.system(command) 

      if options.runBatch and not options.pretend: jobs.Sub()
