#!/usr/bin/env python
import sys, re, os, os.path, math
from optparse import OptionParser
from collections import OrderedDict

import subprocess

import ROOT


# configuration auto-loaded where the job directory and the working directory is defined
from LatinoAnalysis.Tools.userConfig  import *

# functions used in everyday life ...
from LatinoAnalysis.Tools.commonTools import *
from LatinoAnalysis.Tools.batchTools  import *

# list of different productions and chains
from LatinoAnalysis.Gardener.Gardener_cfg import *


# ------------------------ baseW -------------------------

def GetBaseW(inTreeList,iTarget,id_iTarget,isData,db,baseWInfo,version='74x'):
   if isData : return '1'
   else:
     xs = db.get(iTarget) 
     if xs == '' : 
       print 'WARNING: X-section not found for sample: ',iTarget,' !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!'
       baseWInfo['xs']     = ''
       baseWInfo['baseW']  = '-1'
       baseWInfo['nEvt']   = ''
       baseWInfo['nPos']   = ''
       baseWInfo['nNeg']   = ''
       return '-1'
     else:
       nEvt = 0
       nTot = 0
       nPos = 0
       nNeg = 0
       for inTree in inTreeList: 
         print 'Opening: ',inTree
         fileIn = ROOT.TFile.Open(inTree, "READ")
#        fileIn.ls()
         if version == '74x' : 
           h_mcWhgt = fileIn.Get('mcWhgt')
           if h_mcWhgt.__nonzero__() :
             #print 'Using h_mcWhgt'
             nEvt += h_mcWhgt.GetBinContent(1) 
           else:
             nEvt += fileIn.Get('totalEvents').GetBinContent(1) 
             nPos += fileIn.Get('totalEvents').GetBinContent(1)
         else:
           h_mcWeightPos = fileIn.Get('mcWeightPos')
           h_mcWeightNeg = fileIn.Get('mcWeightNeg')
           if h_mcWeightPos.__nonzero__() and h_mcWeightNeg.__nonzero__() :
             nEvt += h_mcWeightPos.GetBinContent(1) - h_mcWeightNeg.GetBinContent(1)
             nPos += h_mcWeightPos.GetBinContent(1)
             nNeg += h_mcWeightNeg.GetBinContent(1) 
             print 'Pos, Neg = ',h_mcWeightPos.GetBinContent(1),h_mcWeightNeg.GetBinContent(1)
           else:
             nEvt += fileIn.Get('totalEvents').GetBinContent(1)
             nPos += fileIn.Get('totalEvents').GetBinContent(1)
         nTot += fileIn.Get('totalEvents').GetBinContent(1)
         fileIn.Close()
       baseW = float(xs)*1000./nEvt
       print 'baseW: xs,N -> W', xs, nEvt , baseW , ' nTot= ', nTot
       baseWInfo['xs']     = str(xs)
       baseWInfo['baseW']  = str(baseW) 
       baseWInfo['nEvt']   = str(nEvt)
       baseWInfo['nPos']   = str(nPos)
       baseWInfo['nNeg']   = str(nNeg)
       baseWInfo['nTot']   = str(nTot)
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

parser.add_option("-p","--prods",   dest="prods"   , help="List of production to run on"              , default=[]     , type='string' , action='callback' , callback=list_maker('prods',','))
parser.add_option("-s","--steps",   dest="steps"   , help="list of Steps to produce"                  , default=[]     , type='string' , action='callback' , callback=list_maker('steps',','))
parser.add_option("-i","--iStep",   dest="iStep"   , help="Step to restart from"                      , default='Prod' , type='string' ) 
parser.add_option("-R","--redo" ,   dest="redo"    , help="Redo, don't check if tree already exists"  , default=False  , action="store_true")
parser.add_option("-b","--batch",   dest="runBatch", help="Run in batch"                              , default=False  , action="store_true")
parser.add_option("-S","--batchSplit", dest="batchSplit", help="Splitting mode for batch jobs"        , default=[], type='string' , action='callback' , callback=list_maker('batchSplit',','))
parser.add_option("-q", "--quiet",    dest="quiet",     help="Quiet logs"                             , default=False, action="store_true")
parser.add_option("-n", "--dry-run",    dest="pretend", help="(use with -v) just list the datacards that will go into this combination", default=False, action="store_true")
parser.add_option("-T", "--selTree",   dest="selTree" , help="Select only some tree (comma separated list)" , default=[]     , type='string' , action='callback' , callback=list_maker('selTree',','))
parser.add_option("-I", "--input-target",   dest="inputTarget" , help="Input Target directory"        , default=None     , type='string' , action='store' )
parser.add_option("-O", "--output-target",   dest="outputTarget" , help="output Target directory"     , default=None     , type='string' , action='store' )
parser.add_option("-E", "--excTree",   dest="excTree" , help="Exclude some tree (comma separated list)" , default=[]     , type='string' , action='callback' , callback=list_maker('excTree',','))
parser.add_option("-Q" , "--queue" ,  dest="queue"    , help="Batch Queue"  , default="8nh" , type='string' ) 
#parser.add_option("-A",  "--aquamarine-location", dest="aquamarineLocation", help="the acuamarine location (i.e. the eos interface) to use ", action='store', default="0.3.84-aquamarine.user")
parser.add_option("-c" , "--cmssw" , dest="cmssw"     , help="CMSSW version" , default='763' , type='string' )
parser.add_option("-C" , "--chain" , dest="chain"     , help="Chain several steps" , default=False, action="store_true")

# Parse options and Filter
(options, args) = parser.parse_args()
prodList = List_Filter(Productions,options.prods).get()
stepList = List_Filter(Steps,options.steps).get()

CMSSW=os.environ["CMSSW_BASE"]

if options.cmssw == '763' :
  eosTargBaseIn = '/eos/user/j/jlauwers/HWW2015/'
  eosTargBaseOut= '/eos/user/j/jlauwers/HWW2015/'

# eosTargBaseIn is defined by default in Gardener/python/Gardener_cfg.py
if options.inputTarget != None:
  eosTargBaseIn=options.inputTarget

# eosTargBaseIn is defined by default in Gardener/python/Gardener_cfg.py
if options.outputTarget != None:
  eosTargBaseOut=options.outputTarget

print "eosProdBase    = ", eosProdBase
print "eosTargBaseIn  = ", eosTargBaseIn
print "eosTargBaseOut = ", eosTargBaseOut  

#hack to be able to stat both files under /eos/cms and /eos/user
 
aquamarineLocationProd = '0.3.84-aquamarine'
xrootdPathProd         = 'root://eoscms.cern.ch/'

aquamarineLocationIn   = '0.3.84-aquamarine.user'
xrootdPathIn           = 'root://eosuser.cern.ch/'

aquamarineLocationOut  = '0.3.84-aquamarine.user'
xrootdPathOut          = 'root://eosuser.cern.ch/'

if "/eos/cms" in eosTargBaseIn:
  aquamarineLocationIn = "0.3.84-aquamarine"
  xrootdPathIn = 'root://eoscms.cern.ch/'
if "/eos/cms" in eosTargBaseOut:
  aquamarineLocationOut = "0.3.84-aquamarine"
  xrootdPathOut = 'root://eoscms.cern.ch/'
  

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
      iLineMod=iLine
      if 'reName' in Productions[iProd]:
        for iOldName in Productions[iProd]['reName']: 
          iLineMod=iLineMod.replace(iOldName, Productions[iProd]['reName'][iOldName])
      exec(iLineMod)  
    #print samples.keys()
    if 'config.Data.outLFNDirBase' in iLine : prodDir=iLine.split('=')[1].replace('\'','').replace(' ','')
    if 'dir' in Productions[iProd] : prodDir=Productions[iProd]['dir']
  handle.close()

  # Load x-section DB

  if not Productions[iProd]['isData'] :  
    xsMethods=['gDoc','Python']  # Among 'gDoc','Python','YellowR' and order Matter (Overwriting for same samples !)
    if options.cmssw == '763' : xsMethods=['Python','YellowR']
    xsFile=CMSSW+'/src/LatinoTrees/AnalysisStep/python/samplesCrossSections.py'
    xsDB = xsectionDB()
    for iMethod in xsMethods :

      if iMethod == 'gDoc'    : xsDB.readGDoc(Productions[iProd]['gDocID'])
      if iMethod == 'Python'  : xsDB.readPython(xsFile)
      if iMethod == 'YellowR' : xsDB.readYR('YR4prel','13TeV')

  # Find existing Input files 
  #if not options.iStep in Steps: options.iStep = 'Prod'
  if options.iStep == 'Prod' : 
    fileCmd = '/afs/cern.ch/project/eos/installation/'+aquamarineLocationProd+'/bin/eos.select ls '+prodDir+Productions[iProd]['dirExt'] #+' | grep -v ttDM'
  else:
    fileCmd = '/afs/cern.ch/project/eos/installation/'+aquamarineLocationIn+'/bin/eos.select ls '+eosTargBaseIn+'/'+iProd+'/'+options.iStep
  print fileCmd
  proc=subprocess.Popen(fileCmd, stderr = subprocess.PIPE,stdout = subprocess.PIPE, shell = True)
  out, err = proc.communicate()
  FileInList=string.split(out)
  print FileInList

  isFirstinChain = True
  previousStep=''
  targetListKeep={}

  # Loop on Steps:
  for iStep in stepList:
    if ( not Productions[iProd]['isData'] and Steps[iStep]['do4MC'] ) or ( Productions[iProd]['isData'] and Steps[iStep]['do4Data'] ) :
      print '---------------- for Step : ',iStep
      targetList={}
      # Validate targets tree
      if options.iStep == 'Prod' :
        fileCmd = '/afs/cern.ch/project/eos/installation/'+aquamarineLocationOut+'/bin/eos.select ls '+eosTargBaseOut+'/'+iProd+'/'+iStep
      else:
        fileCmd = '/afs/cern.ch/project/eos/installation/'+aquamarineLocationOut+'/bin/eos.select ls '+eosTargBaseOut+'/'+iProd+'/'+options.iStep+'__'+iStep
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
                    targetList[iKey] = xrootdPathIn+eosTargBaseIn+'/'+iProd+'/'+options.iStep+'/'+iFile
      #print targetList  

      # Safeguard against partial run on splitted samples -> Re-include all files from that sample
      if not iStep in ['mcwghtcount'] and not Productions[iProd]['isData']: 
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
                  targetList[iKey] = xrootdPathIn+eosTargBaseIn+'/'+iProd+'/'+options.iStep+'/'+iFile 
     

      startingStep = options.iStep       
      if options.chain :
        if not isFirstinChain: 
          print "Gone hacking targetList for chain"
          print startingStep,previousStep
          targetList = targetListKeep
          for i in targetList :
            targetList[i] =  targetList[i].replace(eosTargBaseIn,eosTargBaseOut).replace(startingStep,previousStep)
          startingStep=previousStep

      #if options.chain and isNotFirstinChain: 
      #   isNotFirstinChain = False
      #   targetList = targetListChain
      #targetListChain=targetList
      print targetList
      #for i in targetList : print i
      #quit() 

      # Create Output Directory on eos
      if startingStep == 'Prod' :
        os.system('/afs/cern.ch/project/eos/installation/'+aquamarineLocationOut+'/bin/eos.select mkdir -p '+eosTargBaseOut+'/'+iProd+'/'+iStep)
      else:
        os.system('/afs/cern.ch/project/eos/installation/'+aquamarineLocationOut+'/bin/eos.select mkdir -p '+eosTargBaseOut+'/'+iProd+'/'+startingStep+'__'+iStep)


      # For hadd Step, regroup Files
      if iStep == 'hadd' :
        targetGroupList ={}
        for iTarget in targetList.keys():
          if '_000' in iTarget :
            iKey = iTarget.split('_000')[0]
          elif '__part' in iTarget :
            iKey = iTarget.split('__part')[0]
          elif Productions[iProd]['isData'] :
            for iSample in samples :
              if iSample.replace('_25ns','') in iTarget : iKey = iSample
          else:
            iKey = iTarget

          if options.redo or not 'latino_'+iKey+'.root' in FileExistList :
            if not iKey in targetGroupList:
              targetGroupList[iKey] = []
            targetGroupList[iKey].append(targetList[iTarget])             

        targetList = targetGroupList 

      # Create Jobs Dictionary
      list=[]
      list.append(iStep)
      options.batchSplit+=',Steps'
      bpostFix=''
      if not startingStep == 'Prod' : bpostFix='____'+startingStep
      if options.runBatch: 
        if options.chain: 
          if isFirstinChain:
            list=[iStep+'_Chain']
            stepBatch=iStep+'_Chain'
            print "crating jobs :",'Gardening',iProd,list,targetList.keys(),options.batchSplit,bpostFix
            jobs = batchJobs('Gardening',iProd,list,targetList.keys(),options.batchSplit,bpostFix)

        else:
          stepBatch=iStep
          jobs = batchJobs('Gardening',iProd,list,targetList.keys(),options.batchSplit,bpostFix)

      # Do some preliminary actions for some Steps

      # And now do/create to job for each target
      for iTarget in targetList.keys(): 
        print "FOING : ",iTarget
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
          if startingStep == 'Prod' :
            inTree  ='root://eoscms.cern.ch//eos/cms'+prodDir+Productions[iProd]['dirExt']+'/latino_'+iTarget+'.root'
          else:
            inTree  =xrootdPathIn+eosTargBaseIn+'/'+iProd+'/'+startingStep+'/latino_'+iTarget+'.root'
        else:
          inTree = targetList[iTarget]  # Pointing to File in case of Split
        oriTree = inTree
        wDir  =workDir+'/Gardening__'+iProd+'__'+iStep
        if not os.path.exists(wDir) : os.system('mkdir -p '+wDir) 
        if   options.runBatch: command=''
        #else:                  command='cd '+wDir+' ; '
        else:                  command='cd /tmp/'+os.getlogin()+' ; '

        if iStep == 'hadd' :
          command+='cd /tmp/'+os.getlogin()+' ; '
          outTree ='latino_'+iTarget+'__'+iStep+'.root'
          if len(targetList[iTarget]) == 1 :
            command += 'xrdcp '+targetList[iTarget][0]+' '+outTree+' ; ' 
          else:
            command += 'hadd -f '+outTree+' ' 
            for iFile in targetList[iTarget] : command += iFile+' '
            command += ' ; ' 
        # Chains of subTargets
        elif 'isChain' in Steps[iStep] and Steps[iStep]['isChain']:
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

            if Productions[iProd]['isData'] : 
              if not Steps[iSubStep]['do4Data'] : selectSample=False
            else:
              if not Steps[iSubStep]['do4MC'] : selectSample=False


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

        # Fix CMSSW flag
        command = command.replace('RPLME_CMSSW',options.cmssw)

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
          baseWInfo = {}
          baseW = GetBaseW(oriTreeList,iTargetOri,id_iTarget,Productions[iProd]['isData'],xsDB,baseWInfo,options.cmssw)
          if baseW == '-1' : 
             xsDB.Print()
             exit()
          print baseWInfo
          f = open(wDir+'/baseWInfo.txt', 'a')
          f.write(iProd+' '+iTargetOri+' : ')
          f.write(str(baseWInfo))
          f.write('\n')
          f.close()
          command = command.replace('RPLME_baseW',baseW)
          command = command.replace('RPLME_XSection',baseWInfo['xs'])

        # Fix PU data 
        #puData = '/afs/cern.ch/user/p/piedra/work/pudata.root' 
        #puData = '/afs/cern.ch/user/x/xjanssen/public/MyDataPileupHistogram.root'
        puData = '/afs/cern.ch/user/x/xjanssen/public/Cert_246908-260627_13TeV_PromptReco_Collisions15_25ns_JSON_v2_from256630_PileupHistogram.root'
        if 'puData' in Productions[iProd] : puData = Productions[iProd]['puData']
        print 'PU Data : ', puData
        command = command.replace('RPLME_puData',puData)  

        # Stage Out
        #if '__part' in iTarget:
        # iPart = iTarget.split('__part')[1].split('_')[0]
        # if startingStep == 'Prod' :
        #   command+='xrdcp '+outTree+' root://eosuser.cern.ch/'+eosTargBase+'/'+iProd+'/'+iStep+'/Split/latino_'+iTarget+'__part'+iPart+'_Out.root'
        # else:
        #   command+='xrdcp '+outTree+' root://eosuser.cern.ch/'+eosTargBase+'/'+iProd+'/'+startingStep+'__'+iStep+'/Split/latino_'+iTarget+'__part'+iPart+'_Out.root'
        #lse:
        if startingStep == 'Prod' :
          command+='xrdcp -f '+outTree+' '+xrootdPathOut+eosTargBaseOut+'/'+iProd+'/'+iStep+'/latino_'+iTarget+'.root'
        else:
          command+='xrdcp -f '+outTree+' '+xrootdPathOut+eosTargBaseOut+'/'+iProd+'/'+startingStep+'__'+iStep+'/latino_'+iTarget+'.root'

        command+='; rm '+outTree
        logFile=wDir+'/log__'+iTarget+'.log'
        if options.quiet :
          command += ' 2>&1 > /dev/null \n' 
        else:
          command += ' 2>&1 | tee '+logFile+' \n'  
        if options.pretend : print command
        else :
          if  options.runBatch: jobs.Add(stepBatch,iTarget,command)
          else:                 os.system(command) 

      if options.chain :
        isFirstinChain = False
        previousStep=startingStep+'__'+iStep
        targetListKeep=targetList
      else:
        print "Gone batching ..."
        if options.runBatch and not options.pretend: jobs.Sub(options.queue)

  if options.chain :
    print "Gone batching for Chain ..."
    if options.runBatch and not options.pretend: jobs.Sub(options.queue)
