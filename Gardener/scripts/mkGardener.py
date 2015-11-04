#!/usr/bin/env python
import sys, re, os, os.path
from optparse import OptionParser

from LatinoAnalysis.Tools.userConfig  import *
from LatinoAnalysis.Tools.commonTools import *
from LatinoAnalysis.Tools.batchTools  import *
from LatinoAnalysis.Gardener.Gardener_cfg import *

# ------------------------------------------------------- MAIN --------------------------------------------

parser = OptionParser(usage="usage: %prog [options]")

parser.add_option("-p","--prods",   dest="prods"   , help="List of production to run on"  ,  default=[]     , type='string' , action='callback' , callback=list_maker('prods',','))
parser.add_option("-s","--steps",   dest="steps"   , help="list of Steps to produce"      ,  default=[]     , type='string' , action='callback' , callback=list_maker('steps',','))
parser.add_option("-i","--iStep",   dest="iStep"   , help="Step to restart from"          ,  default='Prod' , type='string' ) 
parser.add_option("-R","--redo" ,   dest="redo"    , help="Redo all trees"                ,  default=False  , action="store_true")
parser.add_option("-b","--batch",   dest="runBatch", help="Run in batch"                  ,  default=False  , action="store_true")
parser.add_option("-S","--batchSplit", dest="batchSplit", help="Splitting mode for batch jobs" , default=[], type='string' , action='callback' , callback=list_maker('batchSplit',','))
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
    
  # Find existing Input files 
  if not options.iStep in Steps: options.iStep = 'Prod'
  if options.iStep == 'Prod' : 
    fileCmd = '/afs/cern.ch/project/eos/installation/0.3.84-aquamarine/bin/eos.select ls '+prodDir+Productions[iProd]['dirExt']
  else:
    fileCmd = '/afs/cern.ch/project/eos/installation/0.3.84-aquamarine.user/bin/eos.select ls '+eosTargBase+'/'+iProd+'/'+options.iStep
  proc=subprocess.Popen(fileCmd, stderr = subprocess.PIPE,stdout = subprocess.PIPE, shell = True)
  out, err = proc.communicate()
  FileInList=string.split(out)
  print FileInList
 
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
       if iSample == 'HWminusJ_HToTauTau_M120' :
        iTree = 'latino_'+iSample+'.root'
        if iTree in FileInList: 
          if options.redo :
            targetList.append(iSample)
          else:
            if not iTree in FileExistList: targetList.append(iSample)
      print targetList  

      # Create Jobs Dictionary
      list=[]
      list.append(iStep)
      options.batchSplit+=',Steps'
      if options.runBatch: jobs = batchJobs('Gardening',iProd,list,targetList,options.batchSplit)    

      # Create Output Directory on eos
      os.system('/afs/cern.ch/project/eos/installation/0.3.84-aquamarine.user/bin/eos.select mkdir '+eosTargBase+'/'+iProd)
      os.system('/afs/cern.ch/project/eos/installation/0.3.84-aquamarine.user/bin/eos.select mkdir '+eosTargBase+'/'+iProd+'/'+iStep)

      # Do some preliminary actions for some Steps

      # And now do/create to job for each target
      for iTarget in targetList: 
        if Steps[iStep]['isChain']:
          print 'TODO: implement chains'
        else:
          print prodDir
          inTree  ='root://eoscms.cern.ch//eos/cms'+prodDir+Productions[iProd]['dirExt']+'/latino_'+iTarget+'.root'
          print inTree
          outTree ='latino_'+iSample+'__'+iStep+'.root'
          tmpDir  =workDir+'/Gardening__'+iProd+'__'+iStep
          command='cd '+tmpDir+' ; '
          command+=Steps[iStep]['command']+' '+inTree+' '+outTree +' ; '
          command+='xrdcp '+outTree+' root://eosuser.cern.ch/'+eosTargBase+'/'+iProd+'/'+iStep+'/latino_'+iTarget+'.root'
          print command
          if not os.path.exists(tmpDir) : os.system('mkdir -p '+tmpDir) 
          os.system(command) 

