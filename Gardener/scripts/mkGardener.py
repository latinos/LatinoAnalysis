#!/usr/bin/env python
import sys, re, os, os.path, math
from optparse import OptionParser
from collections import OrderedDict

import ROOT

from LatinoAnalysis.Tools.userConfig  import *
from LatinoAnalysis.Tools.commonTools import *
from LatinoAnalysis.Tools.batchTools  import *
from LatinoAnalysis.Gardener.Gardener_cfg import *

# ------------------------ baseW -------------------------

def GetBaseW(inTreeList,iTarget,id_iTarget,isData,db):
   if isData : return '1'
   else:
     xs = db.get(iTarget) 
     if xs == '' : return '1'
     else:
       nEvt = 0
       nTot = 0
       for inTree in inTreeList: 
         print 'Opening: ',inTree
         fileIn = ROOT.TFile.Open(inTree, "READ")
#        fileIn.ls()
         h_mcWhgt = fileIn.Get('mcWhgt')
         if h_mcWhgt.__nonzero__() :
           #print 'Using h_mcWhgt'
           nEvt += h_mcWhgt.GetBinContent(1) 
         else:
           nEvt += fileIn.Get('totalEvents').GetBinContent(1) 
         nTot += fileIn.Get('totalEvents').GetBinContent(1)
         fileIn.Close()
       baseW = float(xs)*1000./nEvt
       print 'baseW: xs,N -> W', xs, nEvt , baseW , ' nTot= ', nTot
       return str(baseW)

# --------------------- SPLIT ---------------------------

def SplitTree(inTree,wDir,TargeDir,nEvtToSplit):
   fileIn  = ROOT.TFile.Open(inTree, "READ")
   nEvents = fileIn.Get("latino").GetEntries()
   nTSplit = int(math.ceil(float(nEvents)/float(nEvtToSplit)))
   ObjList = list(OrderedDict.fromkeys( [key.GetName() for key in  fileIn.GetListOfKeys()] ))

   print 'Splitting : ', str(nEvents) , str(nTSplit)
   baseName=os.path.basename(inTree) 
   for iSplit in range(0,nTSplit):
    fileTmp = baseName.replace('.root','__split'+str(iSplit)+'_In.root') 
    fileOut = ROOT.TFile.Open(wDir+'/'+fileTmp, "RECREATE")   
    fileOut.cd()
    for iObj in ObjList:
      pObj = fileIn.Get(iObj)
      if iObj == 'latino' :
       print iObj
       iStart = nEvtToSplit * iSplit
       iStop  = nEvtToSplit*(iSplit+1)
       if nEvents < iStop : iStop=nEvents
       nTree = pObj.CloneTree(0)
       for iEvent in range(iStart,iStop) :
         pObj.GetEntry(iEvent)
         nTree.Fill()
         if iEvent%10000 == 0: print iEvent,' events processed.' 
       nTree.Write()
      elif pObj.ClassName() == 'TTree' :
       nTree = pObj.CloneTree(-1,"fast");
       nTree.Write()
      else: pObj.Write()
    fileOut.Close()
    os.system('xrdcp '+wDir+'/'+fileTmp+' '+TargeDir+'/'+fileTmp)
    os.system('rm '+wDir+'/'+fileTmp)

   fileIn.Close()

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
#queue '8nh'
parser.add_option("-Q" , "--queue" ,  dest="queue"    , help="Batch Queue"  , default="8nh" , type='string' ) 


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
    #print iLine
    if 'samples' in iLine : 
      exec(iLine)  
    #print samples.keys()
    if 'config.Data.outLFNDirBase' in iLine : prodDir=iLine.split('=')[1].replace('\'','').replace(' ','')
  handle.close()

  # Load x-section DB

  if not Productions[iProd]['isData'] :  xsDB = xsectionDB(Productions[iProd]['gDocID'])
    
  # Find existing Input files 
  #if not options.iStep in Steps: options.iStep = 'Prod'
  if options.iStep == 'Prod' : 
    fileCmd = '/afs/cern.ch/project/eos/installation/0.3.84-aquamarine/bin/eos.select ls '+prodDir+Productions[iProd]['dirExt'] #+' | grep -v ttDM'
  else:
    fileCmd = '/afs/cern.ch/project/eos/installation/0.3.84-aquamarine.user/bin/eos.select ls '+eosTargBase+'/'+iProd+'/'+options.iStep
  print fileCmd
  proc=subprocess.Popen(fileCmd, stderr = subprocess.PIPE,stdout = subprocess.PIPE, shell = True)
  out, err = proc.communicate()
  FileInList=string.split(out)
  print FileInList
 
  # Loop on Steps:
  for iStep in stepList:
    if ( not Productions[iProd]['isData'] and Steps[iStep]['do4MC'] ) or ( Productions[iProd]['isData'] and Steps[iStep]['do4Data'] ) :
      print '---------------- for Step : ',iStep
      targetList={}
      # Validate targets tree
      if options.iStep == 'Prod' :
        fileCmd = '/afs/cern.ch/project/eos/installation/0.3.84-aquamarine.user/bin/eos.select ls '+eosTargBase+'/'+iProd+'/'+iStep
      else:
        fileCmd = '/afs/cern.ch/project/eos/installation/0.3.84-aquamarine.user/bin/eos.select ls '+eosTargBase+'/'+iProd+'/'+options.iStep+'__'+iStep
      proc=subprocess.Popen(fileCmd, stderr = subprocess.PIPE,stdout = subprocess.PIPE, shell = True)
      out, err = proc.communicate()
      FileExistList=string.split(out)
      print fileCmd
      print FileExistList
      #print samples.keys()
      for iSample in samples : 
        # Tree selector
        selectSample=True
        # ... from options
        if len(options.selTree) > 0 :
          #print  iSample
          #print options.selTree
          if not iSample in options.selTree: selectSample=False
          #print selectSample
        if len(options.excTree) > 0 :
          if iSample in options.excTree : selectSample=False
        # ... From iStep 
        if 'onlySample' in Steps[iStep] :
          if len(Steps[iStep]['onlySample']) > 0 :
            if not iSample in Steps[iStep]['onlySample'] : selectSample=False
        if 'excludeSample' in Steps[iStep] :
          if len(Steps[iStep]['excludeSample']) > 0 :
            if iSample in Steps[iStep]['excludeSample'] : selectSample=False  
        # And check for mcweight !
        if iStep in ['mcweights'] : # ,'mcwghtcount' ]  :
          if not 'doMCweights=True' in samples[iSample][1] : 
             selectSample=False
        # And Now add trees
        #if not Productions[iProd]['isData'] :
          #iTree = 'latino_'+iSample+'.root'
          #if iTree in FileInList: 
          #  if options.redo and selectSample:
          #     targetList[iSample] = 'NOSPLIT'
          #  else:
          #    if not iTree in FileExistList and selectSample: targetList[iSample] = 'NOSPLIT'
        #else: 
        #print iSample, selectSample 
        for iFile in FileInList:
            if options.redo or not iFile in FileExistList :
              if selectSample and iSample.replace('_25ns','') in iFile:
                iKey = iFile.replace('latino_','').replace('.root','')
                #print iKey
                if '_000' in iKey :
                  aSample = iKey.split('_000')[0]
                elif '__part' in iKey :
                  aSample = iKey.split('__part')[0]
                elif Productions[iProd]['isData'] :
                  if iSample.replace('_25ns','') in iKey : aSample = iSample
                  #for iSample in samples :
                  #if iSample.replace('_25ns','') in iTarget : iTargetOri = iSample
                else:
                  aSample = iKey
                #print aSample , iSample
                if aSample.replace('_25ns','') == iSample.replace('_25ns','') :
                  if options.iStep == 'Prod' :
                    targetList[iKey] = 'root://eoscms.cern.ch//eos/cms'+prodDir+Productions[iProd]['dirExt']+'/'+iFile
                  else:
                    targetList[iKey] = 'root://eosuser.cern.ch/'+eosTargBase+'/'+iProd+'/'+options.iStep+'/'+iFile
      #print targetList  

      # Safeguard against partial run on splitted samples -> Re-include all files from that sample
      if not iStep in ['mcwghtcount']: 
        lSample = []
        for iTarget in targetList.keys(): 
          if   '_000' in iTarget :
            aSample = iTarget.split('_000')[0]
            if not aSample in lSample : lSample.append(aSample)
          elif '__part' in iTarget:
            aSample = iTarget.split('__part')[0]
            if not aSample in lSample : lSample.append(aSample)
        #print lSample  
        for iSample in lSample:
          #print iSample
          for iFile in FileInList:
            iKey = iFile.replace('latino_','').replace('.root','')
            aSample = iKey
            if '_000' in iKey :
              aSample = iKey.split('_000')[0]
            elif '__part' in iKey :
              aSample = iKey.split('__part')[0] 
            #print aSample, iSample
            if aSample == iSample:
              if not iKey in targetList.keys():
                print 'Re-Adding split tree: ', iKey, iFile
                if options.iStep == 'Prod' :
                  targetList[iKey] = 'root://eoscms.cern.ch//eos/cms'+prodDir+Productions[iProd]['dirExt']+'/'+iFile
                else:
                  targetList[iKey] = 'root://eosuser.cern.ch/'+eosTargBase+'/'+iProd+'/'+options.iStep+'/'+iFile 

      print targetList
      #quit() 

      # Create Output Directory on eos
      if options.iStep == 'Prod' :
        os.system('/afs/cern.ch/project/eos/installation/0.3.84-aquamarine.user/bin/eos.select mkdir -p '+eosTargBase+'/'+iProd+'/'+iStep)
      else:
        os.system('/afs/cern.ch/project/eos/installation/0.3.84-aquamarine.user/bin/eos.select mkdir -p '+eosTargBase+'/'+iProd+'/'+options.iStep+'__'+iStep)

      # Check and Split big Trees

#      for iTarget in targetList.keys():
#        if  'bigSamples' in Productions[iProd] and iTarget in Productions[iProd]['bigSamples'] :
#          if options.iStep == 'Prod' :
#            os.system('/afs/cern.ch/project/eos/installation/0.3.84-aquamarine.user/bin/eos.select mkdir -p '+eosTargBase+'/'+iProd+'/'+iStep+'/Split')      
#            fileCmd = '/afs/cern.ch/project/eos/installation/0.3.84-aquamarine.user/bin/eos.select ls '+eosTargBase+'/'+iProd+'/'+iStep+'/Split/latino_'+iTarget+'__part*_In.root'
#          else:
#            os.system('/afs/cern.ch/project/eos/installation/0.3.84-aquamarine.user/bin/eos.select mkdir -p '+eosTargBase+'/'+iProd+'/'+options.iStep+'__'+iStep+'/Split')
#            #fileCmd = '/afs/cern.ch/project/eos/installation/0.3.84-aquamarine.user/bin/eos.select ls '+eosTargBase+'/'+iProd+'/'+options.iStep+'__'+iStep+'/Split/latino_'+iTarget+'_part*_In.root'
#            # Well I can use __partX_Out of prevous step and no split again 
#            fileCmd = '/afs/cern.ch/project/eos/installation/0.3.84-aquamarine.user/bin/eos.select ls '+eosTargBase+'/'+iProd+'/'+options.iStep+'/Split/latino_'+iTarget+'__part*_Out.root'
#            
#          proc=subprocess.Popen(fileCmd, stderr = subprocess.PIPE,stdout = subprocess.PIPE, shell = True)
#          out, err = proc.communicate()
#          SplitFileList=string.split(out)
#          if len(SplitFileList) == 0 :
#            print 'Need to Split'
#            if options.iStep == 'Prod' :
#              inTree     = 'root://eoscms.cern.ch//eos/cms'+prodDir+Productions[iProd]['dirExt']+'/latino_'+iTarget+'.root'
#              targetDir  = 'root://eosuser.cern.ch/'+eosTargBase+'/'+iProd+'/'+iStep+'/Split'
#            else:
#              inTree     = 'root://eosuser.cern.ch/'+eosTargBase+'/'+iProd+'/'+options.iStep+'/latino_'+iTarget+'.root'
#              targetDir  = 'root://eosuser.cern.ch/'+eosTargBase+'/'+iProd+'/'+options.iStep+'__'+iStep+'/Split'
#            wDir  ='/tmp/xjanssen'+'/Gardening__'+iProd+'__'+iStep
#            if not os.path.exists(wDir) : os.system('mkdir -p '+wDir)
#            SplitTree(inTree,wDir,targetDir,1000000)
#            proc=subprocess.Popen(fileCmd, stderr = subprocess.PIPE,stdout = subprocess.PIPE, shell = True)
#            out, err = proc.communicate()
#            SplitFileList=string.split(out) 
#          else:
#            print 'Found Split tree !'
#          print SplitFileList
#          del targetList[Target]
#          for iSplit in SplitFileList : 
#            iKey = iSplit.replace('latino_','').replace('.root','')  
#            if options.iStep == 'Prod' :
#              File = 'root://eosuser.cern.ch/'+eosTargBase+'/'+iProd+'/'+iStep+'/Split/'+iSplit            
#            else:
#              File = 'root://eosuser.cern.ch/'+eosTargBase+'/'+iProd+'/'+options.iStep+'/Split/'+iSplit
#            targetList[iKey] = File

      # Create Jobs Dictionary
      list=[]
      list.append(iStep)
      options.batchSplit+=',Steps'
      if options.runBatch: jobs = batchJobs('Gardening',iProd,list,targetList.keys(),options.batchSplit)

      # Do some preliminary actions for some Steps

      # And now do/create to job for each target
      for iTarget in targetList.keys(): 
        if '_000' in iTarget :
          iTargetOri = iTarget.split('_000')[0]
        elif '__part' in iTarget :
          iTargetOri = iTarget.split('__part')[0]
        elif Productions[iProd]['isData'] :
          for iSample in samples :  
            if iSample.replace('_25ns','') in iTarget : iTargetOri = iSample
        else:
          iTargetOri = iTarget
        #print iTargetOri
        if Productions[iProd]['isData'] :
          id_iTarget='0'
        else:
          id_iTarget=samples[iTargetOri][1][1].replace('id=','')
        #print iTarget , iTargetOri , id_iTarget
        # Stage in   
        #print targetList[iTarget] 
        if targetList[iTarget] == 'NOSPLIT':
          if options.iStep == 'Prod' :
            inTree  ='root://eoscms.cern.ch//eos/cms'+prodDir+Productions[iProd]['dirExt']+'/latino_'+iTarget+'.root'
          else:
            inTree  ='root://eosuser.cern.ch/'+eosTargBase+'/'+iProd+'/'+options.iStep+'/latino_'+iTarget+'.root'
        else:
          inTree = targetList[iTarget]  # Pointing to File in case of Split
        oriTree = inTree
        wDir  =workDir+'/Gardening__'+iProd+'__'+iStep
        if not os.path.exists(wDir) : os.system('mkdir -p '+wDir) 
        if   options.runBatch: command=''
        else:                  command='cd '+wDir+' ; '

        # Chains of subTargets
        if 'isChain' in Steps[iStep] and Steps[iStep]['isChain']:
          iName=''
          cStep=0
          finalTree=inTree

          for iSubStep in  Steps[iStep]['subTargets'] :
            cStep+=1
            
            # Tree selector
            selectSample=True
            # ... From iStep
            if 'onlySample' in Steps[iSubStep] :
              if len(Steps[iSubStep]['onlySample']) > 0 :
                #print Steps[iSubStep]['onlySample'] , iSample , iTargetOri
                if not iTargetOri in Steps[iSubStep]['onlySample'] : selectSample=False
            if 'excludeSample' in Steps[iSubStep] :
              if len(Steps[iSubStep]['excludeSample']) > 0 :
                if iTargetOri in Steps[iSubStep]['excludeSample'] : selectSample=False
            if iSubStep in ['mcweights']: # ,'mcwghtcount' ]  :
              if not 'doMCweights=True' in samples[iTargetOri][1] : selectSample=False

            #print iSubStep , selectSample

            if cStep == 1 :
              iName=iSubStep
            else:
              iName+='__'+iSubStep

            if selectSample : 
              inTree=finalTree              
              outTree ='latino_'+iTarget+'__'+iName+'.root'
              command+=Steps[iSubStep]['command']+' '+inTree+' '+outTree +' ; '  
              finalTree=outTree

          # Tree to be kept:
          outTree = finalTree  

        # single Target
        else:
          outTree ='latino_'+iTarget+'__'+iStep+'.root'
          command+=Steps[iStep]['command']+' '+inTree+' '+outTree +' ; '

        # Fix baseW if needed
        if Productions[iProd]['isData'] : baseW = '1.'
        elif iStep == 'baseW' or ( 'isChain' in Steps[iStep] and Steps[iStep]['isChain'] and 'baseW' in Steps[iStep]['subTargets'] ): 
          oriTreeList = []
          for kTarget in targetList.keys():
            kTargetOri = kTarget
            if '_000' in kTarget :
              kTargetOri = kTarget.split('_000')[0]
            elif '__part' in kTarget :
              kTargetOri = kTarget.split('__part')[0]
            if iTargetOri == kTargetOri : 
               oriTreeList.append(os.path.dirname(oriTree)+'/latino_'+kTarget+'.root')
          #print oriTreeList
          baseW = GetBaseW(oriTreeList,iTargetOri,id_iTarget,Productions[iProd]['isData'],xsDB)
        else: baseW = '1.'
        command = command.replace('RPLME_baseW',baseW)

        # Fix PU data 
        #puData = '/afs/cern.ch/user/p/piedra/work/pudata.root' 
        puData = '/afs/cern.ch/user/x/xjanssen/public/MyDataPileupHistogram.root'
        command = command.replace('RPLME_puData',puData)  

        # Stage Out
        #if '__part' in iTarget:
        # iPart = iTarget.split('__part')[1].split('_')[0]
        # if options.iStep == 'Prod' :
        #   command+='xrdcp '+outTree+' root://eosuser.cern.ch/'+eosTargBase+'/'+iProd+'/'+iStep+'/Split/latino_'+iTarget+'__part'+iPart+'_Out.root'
        # else:
        #   command+='xrdcp '+outTree+' root://eosuser.cern.ch/'+eosTargBase+'/'+iProd+'/'+options.iStep+'__'+iStep+'/Split/latino_'+iTarget+'__part'+iPart+'_Out.root'
        #lse:
        if options.iStep == 'Prod' :
          command+='xrdcp -f '+outTree+' root://eosuser.cern.ch/'+eosTargBase+'/'+iProd+'/'+iStep+'/latino_'+iTarget+'.root'
        else:
          command+='xrdcp -f '+outTree+' root://eosuser.cern.ch/'+eosTargBase+'/'+iProd+'/'+options.iStep+'__'+iStep+'/latino_'+iTarget+'.root'

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

      if options.runBatch and not options.pretend: jobs.Sub(options.queue)
