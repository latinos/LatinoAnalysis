#!/usr/bin/env python
import sys, re, os, os.path, math, copy
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
        #fileIn = ROOT.TFile.Open("dcap://maite.iihe.ac.be"+inTree, "READ")
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

# ------------------------------------------------------- MAIN --------------------------------------------

parser = OptionParser(usage="usage: %prog [options]")

parser.add_option("-p","--prods",   dest="prods"   , help="List of production to run on"              , default=[]     , type='string' , action='callback' , callback=list_maker('prods',','))
parser.add_option("-s","--steps",   dest="steps"   , help="list of Steps to produce"                  , default=[]     , type='string' , action='callback' , callback=list_maker('steps',','))
parser.add_option("-i","--iniStep",   dest="iniStep"   , help="Step to restart from"                      , default='Prod' , type='string' ) 
parser.add_option("--friendStep",dest="friendStep"   , help="step to use as auxiliary input file (default None)"    , default=None , type='string' ) 
parser.add_option("-R","--redo" ,   dest="redo"    , help="Redo, don't check if tree already exists"  , default=False  , action="store_true")
parser.add_option("-b","--batch",   dest="runBatch", help="Run in batch"                              , default=False  , action="store_true")
parser.add_option("-S","--batchSplit", dest="batchSplit", help="Splitting mode for batch jobs"        , default='Target', type='string' , action='callback' , callback=list_maker('batchSplit',','))
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
parser.add_option("-a" , "--allSamples" , dest="ignoreOnlySamples",  help="ignoreOnlySamples"  , default=False  , action="store_true")
parser.add_option("-M" , "--forceMerge" , dest="forceMerge", help="Force Merge Big Sample in Hadd" , default=False  , action="store_true")
parser.add_option("-u" , "--user" , dest="user", help="Set user directory" , default='xjanssen')
parser.add_option("-W" , "--iihe-wall-time" , dest="IiheWallTime" , help="Requested IIHE queue Wall Time" , default='168:00:00')

# Parse options and Filter
(options, args) = parser.parse_args()
prodList = List_Filter(Productions,options.prods).get()
stepList = List_Filter(Steps,options.steps).get()

CMSSW=os.environ["CMSSW_BASE"]

# fix bTag for 74x
#if options.cmssw == '74x' :
#  Steps['bPogSF']['command'] = 'gardener.py btagPogScaleFactors '  
#  Steps['bPogSF']['do4MC'] = False
#  print Steps['bPogSF']['command']  

#if options.cmssw == '763' :
#eosTargBaseIn = '/eos/user/j/jgarciaf/'
#eosTargBaseOut= '/eos/user/j/jgarciaf/'
# eosTargBaseIn is defined by default in Gardener/python/Gardener_cfg.py
if options.inputTarget != None:
  eosTargBaseIn=options.inputTarget

# eosTargBaseIn is defined by default in Gardener/python/Gardener_cfg.py
if options.outputTarget != None:
  eosTargBaseOut=options.outputTarget


print "eosProdBase    = ", eosProdBase
print "eosTargBaseIn  = ", eosTargBaseIn
print "eosTargBaseOut = ", eosTargBaseOut 

if 'knu' in os.uname()[1] or 'sdfarm' in os.uname()[1]:
  #inDirBase = options.inputTarget
  #outDirBase = options.outputTarget
  Steps['hadd']['SizeMax']= 1e9 

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


# Compile all root macros before sending jobs
if options.runBatch:
  print "Batch mode"
  pathRootMacro = CMSSW + '/src/LatinoAnalysis/Gardener/python/variables/'
  for fn in os.listdir(pathRootMacro):
    if os.path.isfile(pathRootMacro+fn) and ( fn.endswith('.C') or fn.endswith('.cc') ):
      try:
        ROOT.gROOT.LoadMacro(pathRootMacro+fn+'+g')
      except RuntimeError:
        ROOT.gROOT.LoadMacro(pathRootMacro+fn+'++g')
# Loop on input productions
for iProd in prodList :
  cmssw=options.cmssw
  if 'cmssw' in Productions[iProd] : cmssw = Productions[iProd]['cmssw']
  # Fix for 74x: can not run these modules: 
  if cmssw == '74x' : Steps['bPogSF']['do4MC'] = False
  if cmssw == '74x' : Steps['genVariables']['do4MC'] = False

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
    xsMethods=['Python','YellowR'] # Among 'gDoc','Python','YellowR' and order Matter (Overwriting for same samples !)
    if cmssw == '74x' : xsMethods=['gDoc','Python'] 
    xsFile=CMSSW+'/src/LatinoAnalysis/NanoGardener/python/framework/samples/samplesCrossSections2016.py'
    xsDB = xsectionDB()
    for iMethod in xsMethods :

      if iMethod == 'gDoc'    : xsDB.readGDoc(Productions[iProd]['gDocID'])
      if iMethod == 'Python'  : xsDB.readPython(xsFile)
      if iMethod == 'YellowR' : xsDB.readYR('YR4','13TeV')

  # Find existing Input files 
  #if not options.iniStep in Steps: options.iniStep = 'Prod'
  if 'iihe' in os.uname()[1]:
    if options.iniStep == 'Prod' :
      fileCmd = 'ls /pnfs/iihe/cms/store/user/' + options.user + '/HWW2015/RunII/'+prodDir.split('RunII/')[1]+Productions[iProd]['dirExt'] # +' | grep  ttDM0001scalar0010'
    else:
      fileCmd = 'ls /pnfs/iihe/cms/store/user/' + options.user + '/HWW2015/'+iProd+'/'+options.iniStep
  #elif 'knu' in os.uname()[1]:
  #  if options.iniStep == 'Prod' :
  #    fileCmd = 'ls ' + inDirBase + prodDir+Productions[iProd]['dirExt'] # +' | grep  ttDM0001scalar0010'
  #  else:
  #    fileCmd = 'ls ' + inDirBase +iProd+ '/'+options.iniStep
  elif 'sdfarm' in os.uname()[1]:
    if options.iniStep == 'Prod' :
      fileCmd = 'ls ' + eosTargBaseIn + prodDir.split('RunII/')[1]+Productions[iProd]['dirExt'] # +' | grep  ttDM0001scalar0010'
    else:
      fileCmd = 'ls ' + eosTargBaseIn +iProd+ '/'+options.iniStep
  elif 'hercules' in os.uname()[1]:
    if options.iniStep == 'Prod' :
      fileCmd = 'ls ' + eosTargBaseIn + prodDir + "/" + Productions[iProd]['dirExt']
    else:
      fileCmd = 'ls ' + eosTargBaseIn  + iProd+ '/'+ options.iniStep
  else:
    if options.iniStep == 'Prod' : 
      fileCmd = 'ls '+prodDir+Productions[iProd]['dirExt']  # +' | grep  ttDM'
      #fileCmd = 'ls '+eosTargBaseIn
    else:
      fileCmd = 'ls '+eosTargBaseIn+'/'+iProd+'/'+options.iniStep

  print "input file fileCmd is: ", fileCmd
  proc=subprocess.Popen(fileCmd, stderr = subprocess.PIPE,stdout = subprocess.PIPE, shell = True)
  out, err = proc.communicate()
  FileInList=string.split(out)
  print "Listing input files: ", FileInList

  isFirstinChain = True
  replaceStep=''
  previousStep=''
  targetListKeep={}

  # Loop on Steps
  for iStep in stepList:
    if ( not Productions[iProd]['isData'] and Steps[iStep]['do4MC'] ) or ( Productions[iProd]['isData'] and Steps[iStep]['do4Data'] ) :
      print '---------------- for Step : ',iStep
      targetList={}
      # Validate targets tree
      if 'iihe' in os.uname()[1]:
        if options.iniStep == 'Prod' :
          fileCmd = 'ls /pnfs/iihe/cms/store/user/' + options.user + '/HWW2015'+'/'+iProd+'/'+iStep #+' | grep  ttDM'
        else: 
          fileCmd = 'ls /pnfs/iihe/cms/store/user/' + options.user + '/HWW2015'+'/'+iProd+'/'+options.iniStep+'__'+iStep
      elif 'knu' in os.uname()[1]:
        if options.iniStep == 'Prod' :
          fileCmd = 'ls ' + outDirBase + prodDir+'/'+iProd #+' | grep  ttDM'
        else: 
          fileCmd = 'ls ' + outDirBase + iProd+'/'+options.iniStep+'__'+iStep
      elif 'hercules' in os.uname()[1]:
        if options.iniStep == 'Prod' :
          fileCmd = 'ls ' + eosTargBaseOut + iProd+'/'+ iStep
        else: 
          fileCmd = 'ls ' + eosTargBaseOut + iProd+'/'+options.iniStep+'__'+iStep
      else:
        if options.iniStep == 'Prod' :
          fileCmd = 'ls '+eosTargBaseOut+'/'+iProd+'/'+'Prod__'+iStep
        else:
          fileCmd = 'ls '+eosTargBaseOut+'/'+iProd+'/'+options.iniStep+'__'+iStep
      print 'output file fileCmd', fileCmd
      proc=subprocess.Popen(fileCmd, stderr = subprocess.PIPE,stdout = subprocess.PIPE, shell = True)
      out, err = proc.communicate()
      FileExistList=string.split(out)
      #print "FileExistList: ", FileExistList
      #print 'samples',samples
      #print samples.keys()
      for iSample in samples : 
        # Tree selector
        selectSample=True
        # ... from options
        if len(options.selTree) > 0 :
          #if 'DYJetsToLL_M-50' in iSample : print iSample
          #print 'iSample', iSample ,'selTree',options.selTree
          if not iSample in options.selTree: selectSample=False
          #print selectSample
        if len(options.excTree) > 0 :
          if iSample in options.excTree : selectSample=False
        # ... From Production
        if 'onlySample' in  Productions[iProd] and not options.ignoreOnlySamples :
          if len(Productions[iProd]['onlySample']) > 0 :
            if not iSample in Productions[iProd]['onlySample']: selectSample=False
        if 'excludeSample' in Productions[iProd]:
          if len(Productions[iProd]['excludeSample']) > 0 :
            if iSample in Productions[iProd]['excludeSample'] : selectSample=False  
        # ... From iStep 
        if 'onlySample' in Steps[iStep] and not options.ignoreOnlySamples :
          if len(Steps[iStep]['onlySample']) > 0 :
            if not iSample in Steps[iStep]['onlySample'] : selectSample=False
        if 'excludeSample' in Steps[iStep] :
          if len(Steps[iStep]['excludeSample']) > 0 :
            if iSample in Steps[iStep]['excludeSample'] : selectSample=False  
        # And check for mcweight !
        if iStep in ['mcweights'] : # ,'mcwghtcount' ]  :
          if not 'doMCweights=True' in samples[iSample][1] : 
            selectSample=False
        #print 'iSample',iSample,'selectSample',selectSample
        # And Now add trees
        #if not Productions[iProd]['isData'] :
          #iTree = 'latino_'+iSample+'.root'
          #if iTree in FileInList: 
          #  if options.redo and selectSample:
          #     targetList[iSample] = 'NOSPLIT'
          #  else:
          #    if not iTree in FileExistList and selectSample: targetList[iSample] = 'NOSPLIT'
        #else: 
        #if 'ttDM' in iSample: print iSample, selectSample 
        for iFile in FileInList:
            #if 'DYJetsToLL_M-50_00' in iFile and iSample == 'DYJetsToLL_M-50': print iFile , options.redo ,  iFile in FileExistList 
          if options.redo or not iFile in FileExistList or iStep == 'hadd' :
            #print 'iSample', iSample, 'iFile', iFile
            if selectSample and iSample.replace('_25ns','') in iFile :
              #if 'MuonEG' in iFile : print iFile
              iKey = iFile.replace('latino_','').replace('.root','')
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
              #print 'aSample',aSample,'iSample',iSample
              if aSample.replace('_25ns','') == iSample.replace('_25ns','') :
                if 'iihe' in os.uname()[1]:
                  if options.iniStep == 'Prod' :
                    targetList[iKey] = '/pnfs/iihe/cms/store/user/' + options.user + '/HWW2015/RunII/'+prodDir.split('RunII/')[1]+Productions[iProd]['dirExt']+'/'+iFile
                  else:
                    targetList[iKey] = '/pnfs/iihe/cms/store/user/' + options.user + '/HWW2015/'+iProd+'/'+options.iniStep+'/'+iFile
                elif 'knu' in os.uname()[1]:
                  if options.iniStep == 'Prod' :
                    targetList[iKey] = inDirBase + prodDir+Productions[iProd]['dirExt'] + '/' +iFile 
                  else:
                    targetList[iKey] = inDirBase + iProd+'/'+options.iniStep + '/' +iFile
                elif 'sdfarm' in os.uname()[1]:
                  if options.iniStep == 'Prod' :
                    targetList[iKey] = eosTargBaseIn + prodDir.split('RunII/')[1]+Productions[iProd]['dirExt'] + '/'+iFile 
                  else:
                    targetList[iKey] = eosTargBaseIn + iProd+'/'+options.iniStep + '/' +iFile
                elif 'hercules' in os.uname()[1]:
                  if options.iniStep == 'Prod' :
                    targetList[iKey] = eosTargBaseIn + prodDir + Productions[iProd]['dirExt'] + '/'+iFile 
                  else:
                    targetList[iKey] = eosTargBaseIn  + iProd+ '/'+ options.iniStep + '/' +iFile
                else:
                  if options.iniStep == 'Prod' :
                    targetList[iKey] = 'root://eoscms.cern.ch//eos/cms'+prodDir+Productions[iProd]['dirExt']+'/'+iFile
                  else:
                    targetList[iKey] = eosTargBaseIn+'/'+iProd+'/'+options.iniStep+'/'+iFile

      print "targetList: ", targetList  


      # Safeguard against partial run on splitted samples -> Re-include all files from that sample
      #if  iStep in ['mcwghtcount'] and not Productions[iProd]['isData']: 
      if not Productions[iProd]['isData']: 
        targetListBaseW = copy.deepcopy(targetList)
        #print "printing targetListBaseW", targetListBaseW
        lSample = []
        for iTarget in targetListBaseW.keys(): 
          if   '_000' in iTarget :
            aSample = iTarget.split('_000')[0]
            if not aSample in lSample : lSample.append(aSample)
          elif '__part' in iTarget:
            aSample = iTarget.split('__part')[0]
            if not aSample in lSample : lSample.append(aSample)
        #print "lSample", lSample  
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
              if not iKey in targetListBaseW.keys():
                print 'Re-Adding split tree: ', iKey, iFile

                if 'iihe' in os.uname()[1]:
                  if options.iniStep == 'Prod' :
                    targetListBaseW[iKey] = '/pnfs/iihe/cms/store/user/' + options.user + '/HWW2015/RunII/'+prodDir.split('RunII/')[1]+Productions[iProd]['dirExt']+'/'+iFile
                  else:
                    targetListBaseW[iKey] = '/pnfs/iihe/cms/store/user/' + options.user + '/HWW2015/'+iProd+'/'+options.iniStep+'/'+iFile
                elif 'knu' in os.uname()[1]:
                  if options.iniStep == 'Prod' :
                    targetListBaseW[iKey] = inDirBase + prodDir+Productions[iProd]['dirExt']+'/'+iFile 
                  else:
                    targetListBaseW[iKey] = inDirBase + iProd+'/'+options.iniStep+'/'+iFile
                elif 'sdfarm' in os.uname()[1]:
                  if options.iniStep == 'Prod' :
                    targetListBaseW[iKey] = eosTargBaseIn + prodDir.split('RunII/')[1]+Productions[iProd]['dirExt']+'/'+iFile 
                  else:
                    targetListBaseW[iKey] = eosTargBaseIn + iProd+'/'+options.iniStep+'/'+iFile
                elif 'hercules' in os.uname()[1]:
                  if options.iniStep == 'Prod' :
                    targetList[iKey] = eosTargBaseIn + prodDir + Productions[iProd]['dirExt'] + '/'+iFile 
                  else:
                    targetList[iKey] = eosTargBaseIn  + iProd+ '/'+ options.iniStep + '/' +iFile
                else: 
                  if options.iniStep == 'Prod' :
                    targetListBaseW[iKey] = 'root://eoscms.cern.ch//eos/cms'+prodDir+Productions[iProd]['dirExt']+'/'+iFile
                  else:
                    targetListBaseW[iKey] = eosTargBaseIn+'/'+iProd+'/'+options.iniStep+'/'+iFile 



      startingStep = options.iniStep
      if options.chain :
        if not isFirstinChain: 
          print "Gone hacking targetList for chain"
          print startingStep,replaceStep,previousStep
          print 'targetList',targetList
          targetList = targetListKeep
          print 'targetList',targetList
          for i in targetList :
            if not replaceStep:
              if 'sdfarm' in os.uname()[1]:
                if startingStep == 'Prod':
                  delimit = prodDir.split('RunII/')[1]+Productions[iProd]['dirExt']
                  targetList[i] = targetList[i].split(delimit)[0] + '/'+iProd + '/'+previousStep +'/'+ targetList[i].split(delimit)[1]
                  targetList[i] =  targetList[i].replace(eosTargBaseIn,eosTargBaseOut)
                else: targetList[i] =  targetList[i].replace(eosTargBaseIn,eosTargBaseOut).replace(startingStep,previousStep)
              else: targetList[i] =  targetList[i].replace(eosTargBaseIn,eosTargBaseOut).replace(startingStep,previousStep)
            else:
              targetList[i] =  targetList[i].replace(eosTargBaseIn,eosTargBaseOut).replace(replaceStep,previousStep)
          startingStep=previousStep

      #if options.chain and isNotFirstinChain: 
      #   isNotFirstinChain = False
      #   targetList = targetListChain
      #targetListChain=targetList
      print "targetList check 1: ", targetList
      #for i in targetList : print i
      #quit() 
      # Create Output Directory on eos
      if 'iihe' in os.uname()[1]:
        print 'Using LCG ...'
      elif 'knu' in os.uname()[1]:
        if iStep == 'UEPS' :
          for iUEPS in Steps[iStep]['cpMap'] :
            outDir = outDirBase+'/'+iProd+'/'+startingStep+'__'+iUEP
            os.system('mkdir -p '+outDir)  
        else:
          if startingStep == 'Prod' :
            outDir = outDirBase+'/'+iProd+'/'+iStep
            os.system('mkdir -p '+ outDir)
          else:
            outDir = outDirBase+'/'+iProd+'/'+startingStep+'__'+iStep
            os.system('mkdir -p '+ outDir)
      elif 'hercules' in os.uname()[1]:
        if iStep == 'UEPS' :
          for iUEPS in Steps[iStep]['cpMap'] :
            os.system('mkdir -p '+eosTargBaseOut+'/'+iProd+'/'+startingStep+'__'+iUEPS)  
        else:
          if startingStep == 'Prod' :
            os.system('mkdir -p '+eosTargBaseOut+'/'+iProd+'/'+iStep)
          else:
            os.system('mkdir -p '+eosTargBaseOut+'/'+iProd+'/'+startingStep+'__'+iStep)
      else:
        if iStep == 'UEPS' :
          for iUEPS in Steps[iStep]['cpMap'] :
            os.system('mkdir -p '+eosTargBaseOut+'/'+iProd+'/'+startingStep+'__'+iUEPS)  
        else:
          if startingStep == 'Prod' :
            os.system('mkdir -p '+eosTargBaseOut+'/'+iProd+'/'+iStep)
          else:
            os.system('mkdir -p '+eosTargBaseOut+'/'+iProd+'/'+startingStep+'__'+iStep)

      # For hadd Step, regroup Files
      if iStep == 'hadd' :
        targetGroupList ={}
        targetGroupSize ={}
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

          #print iKey , iTarget , remoteFileSize(targetList[iTarget])

          if not Steps['hadd']['SizeMethod'] :
            if options.redo or not 'latino_'+iKey+'.root' in FileExistList :
              if not iKey in Steps['hadd']['bigSamples'] or options.forceMerge: 
                if not iKey in targetGroupList: targetGroupList[iKey] = []
                targetGroupList[iKey].append(targetList[iTarget])             
              else:
                if not os.path.basename(targetList[iTarget]) in FileExistList :
                  targetGroupList[iTarget] = []           
                  targetGroupList[iTarget].append(targetList[iTarget])             
          else:
            if not iKey in targetGroupSize: targetGroupSize[iKey] = {}
            targetGroupSize[iKey][iTarget]=float(remoteFileSize(targetList[iTarget])) 

        # default is 5GB per hadd
        if Steps['hadd']['SizeMethod'] :
          for iKey in targetGroupSize:
            iPart=0
            tSize=0
            for (iTarget, iSize) in sorted(targetGroupSize[iKey].items()) :
              tSize+=iSize
              if tSize > Steps['hadd']['SizeMax']:
                iPart += 1
                tSize = iSize
              jKey  = iKey+'__part'+str(iPart) 
              iFile = 'latino_'+iKey+'__part'+str(iPart)+'.root'
              if options.redo or not iFile in FileExistList : 
                  #print iTarget, iSize , iFile
                if not jKey in targetGroupList: targetGroupList[jKey] = []
                targetGroupList[jKey].append(targetList[iTarget])  
            if iPart == 0 :
              iFile = 'latino_'+iKey+'.root'
              if options.redo or not iFile in FileExistList :         
                targetGroupList[iKey] = targetGroupList.pop(jKey)
              else:
                #print iFile, " exist"
                del targetGroupList[jKey]

        targetList = targetGroupList 
        #print targetList
      # Check job in not already running before allowing it ? 
      keysToDel=[] 
      for iTarget in targetList:
        pidFile=jobDir+'Gardening__'+iProd+'/Gardening__'+iProd+'__'+iStep
        if options.chain: pidFile+='_Chain'
        pidFile+='__'+iTarget
        if not startingStep == 'Prod' : pidFile+='____'+startingStep
        pidFile+='.jid'
        if os.path.isfile(pidFile) :
          print "pidFile", pidFile
          print '--> Job Running already : '+iTarget
          keysToDel.append(iTarget)
      for iTarget in keysToDel:
        del targetList[iTarget]
      # For hadd, we need to check that all jobs are done !
      if iStep == 'hadd' :
        #print targetList
        keysToDel=[]
        for iTarget in targetList:
          FileTarget=[]
          #for jFile in targetList[iTarget] : 
          #  FileTarget.append(os.path.basename(jFile))
          filePattern = targetList[iTarget][0].split('.root')[0]
          if    '_000'   in filePattern : filePattern = filePattern.split('_000')[0]+'_000*.root'
          elif  '__part' in filePattern : filePattern = filePattern.split('__part')[0]+'__part*.root'
          else: filePattern += '.root'
          if 'iihe' or 'knu' in os.uname()[1]:
            fileCmd = 'ls '+ filePattern
          else:
            fileCmd = 'ls ' + filePattern    
          proc=subprocess.Popen(fileCmd, stderr = subprocess.PIPE,stdout = subprocess.PIPE, shell = True)
          out, err = proc.communicate()
          FileTarget=string.split(out)


          if 'iihe' in os.uname()[1]:
            PrevStep='' 
            if '__' in options.iniStep :
              SubSteps=options.iniStep.split('__')
              for i in range(len(SubSteps)-1) : 
                PrevStep+=SubSteps[i]
                if len(SubSteps)-1 > 1 and i < len(SubSteps)-2 : PrevStep+='__'
                                #            if not '__' in  options.iniStep :
            fileCmd = 'ls /pnfs/iihe/cms/store/user/' + options.user + '/HWW2015/RunII/'+prodDir.split('RunII/')[1]+Productions[iProd]['dirExt']
#            else:
#              fileCmd = 'ls /pnfs/iihe/cms/store/user/' + options.user + '/HWW2015/'+iProd+'/'+PrevStep
          else:
            #            if not '__' in  options.iniStep :
            fileCmd = 'ls '+prodDir+Productions[iProd]['dirExt']  # +' | grep  ttDM'
#            else:
#              fileCmd = '/afs/cern.ch/project/eos/installation/'+aquamarineLocationIn+'/bin/eos.select ls '+eosTargBaseIn+'/'+iProd+'/'+PrevStep

          fileCmd += '/' + os.path.basename(targetList[iTarget][0]).split('_000')[0].split('__part')[0]
          if   '_000'   in targetList[iTarget][0] : fileCmd += '_000*.root'
          elif '__part' in targetList[iTarget][0] : fileCmd += '__part*.root'
          else : fileCmd += '.root'
          #print fileCmd 
          proc=subprocess.Popen(fileCmd, stderr = subprocess.PIPE,stdout = subprocess.PIPE, shell = True)
          out, err = proc.communicate()
          FileOriList=string.split(out)
          haddTest=True
          FileTargetStrip=[]
          for jFile in FileTarget : FileTargetStrip.append(os.path.basename(jFile))  
          for jFile in FileOriList:
            if not (os.path.basename(jFile)) in FileTargetStrip : 
              print jFile , os.path.basename(jFile) , iTarget
              haddTest=False
          if not haddTest : keysToDel.append(iTarget)
        for iTarget in keysToDel:
          iKey = iTarget.split('_000')[0].split('__part')[0]
          if not iKey in Steps['hadd']['bigSamples'] or Steps['hadd']['SizeMethod']:
            print '--> HADD: Some jobs stil running/not done : '+iTarget 
            del targetList[iTarget]

      print "targetList check 2: ", targetList
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
        print "DOING : ",iTarget
        GarbageCollector=[]
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
        inTree = targetList[iTarget]  # Pointing to File in case of Split
        oriTree = inTree
        wDir  =workDir+'/Gardening__'+iProd+'__'+iStep
        if not os.path.exists(wDir) : os.system('mkdir -p '+wDir) 
        if   options.runBatch : command=''
        else:  
          if 'iihe' or 'knu' or 'sdfarm' in os.uname()[1]:
            command='cd '+wDir+' ; '
          else:       
            command='cd /tmp/'+os.getlogin()+' ; '

        # Special hadd command
        if iStep == 'hadd' :
          #          if 'iihe' or 'knu' in os.uname()[1]:
          #            command='cd '+wDir+' ; '
          #          else:
          #            command+='cd /tmp/'+os.getlogin()+' ; '

          outTree ='latino_'+iTarget+'__'+iStep+'.root'
          if len(targetList[iTarget]) == 1 :
            if 'iihe' in os.uname()[1]:
              outTree = 'srm://maite.iihe.ac.be:8443'+targetList[iTarget][0]
            elif 'knu' in os.uname()[1]:
              if options.runBatch :
                command += 'gfal-copy '+rootReadPath(targetList[iTarget][0].split('/data/cms')[1]) + ' '+outTree+' ; '
              else: command += 'cp '+targetList[iTarget][0]+' '+outTree+' ; ' 
            elif 'sdfarm' in os.uname()[1]:
              if options.runBatch :
                command += 'xrdcp -f '+rootReadPath(targetList[iTarget][0].split('xrootd')[1]) + ' '+outTree+' ; '
              else: command += 'cp '+targetList[iTarget][0]+' '+outTree+' ; ' 
            else:
              command += 'xrdcp '+targetList[iTarget][0]+' '+outTree+' ; ' 
          else:
            command += 'hadd -f '+outTree+' ' 
            for iFile in targetList[iTarget] :
              if '/pnfs/knu.ac.kr/data/cms' in iFile :
                if options.runBatch :
                  command += rootReadPath(iFile.split('/data/cms')[1])+' '
                else: command += iFile+' '
              if 'sdfarm' in os.uname()[1] :
                if options.runBatch :
                  command += rootReadPath(iFile.split('xrootd')[1])+' '
                else: command += iFile+' '
              else: command += iFile+' '
            command += ' ; ' 
            GarbageCollector.append(outTree)
            command += 'hadd_return=$?; ' 

        # Special UEPS directories
        elif iStep == 'UEPS' :
          for iUEPS in Steps[iStep]['cpMap'] :
            if iTarget in Steps[iStep]['cpMap'][iUEPS] :
              for i in range(len(Steps[iStep]['cpMap'][iUEPS][iTarget])):
                print iUEPS, iTarget , '--->' , Steps[iStep]['cpMap'][iUEPS][iTarget][i]
                outTree = os.path.dirname(inTree)+'__'+iUEPS+'/'+'latino_'+Steps[iStep]['cpMap'][iUEPS][iTarget][i]+'.root'
                print inTree , '--->', outTree 
                command +='lcg-cp srm://maite.iihe.ac.be:8443'+inTree+' srm://maite.iihe.ac.be:8443'+outTree+' '
                if i <  len(Steps[iStep]['cpMap'][iUEPS][iTarget])-1 : command += ' ; '

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
            if 'onlySample' in Steps[iSubStep] : # and not options.ignoreOnlySamples :
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



            if cStep == 1 :
              iName=iSubStep
            else:
              iName+='__'+iSubStep

            if selectSample : 
              inTree=finalTree
              outTree ='latino_'+iTarget+'__'+iName+'.root'
              if 'pnfs/knu.ac.kr/data/cms' in inTree:
                command+=Steps[iSubStep]['command']+' '+rootReadPath(inTree.split('/data/cms')[1])+' '+outTree +' ; '
              elif 'xrootd' in inTree:
                command+=Steps[iSubStep]['command']+' '+rootReadPath(inTree.split('xrootd')[1])+' '+outTree +' ; '
              else: command+=Steps[iSubStep]['command']+' '+inTree+' '+outTree +' ; '  
              #print 'isChain-------------------------------------------'
              #print 'inTree', inTree
              #print 'outTree',outTree
              #print 'command',command
              finalTree=outTree
              GarbageCollector.append(outTree)

          # Tree to be kept:
          outTree = finalTree  

        # single Target
        else:
          outTree ='latino_'+iTarget+'__'+iStep+'.root'
          if 'knu' in os.uname()[1]:
            command+=Steps[iStep]['command']+' '+rootReadPath(inTree.split('/data/cms')[1])+' '+outTree +' ; '
          elif 'sdfarm' in os.uname()[1]:
            command+=Steps[iStep]['command']+' '+rootReadPath(inTree.split('xrootd')[1])+' '+outTree +' ; '
          else: command+=Steps[iStep]['command']+' '+inTree+' '+outTree +' ; '
          #print 'single Target-------------------------------------------'
          #print 'inTree', inTree
          #print 'outTree',outTree
          #print 'command',command

          GarbageCollector.append(outTree)

        # Fix CMSSW flag
        command = command.replace('RPLME_CMSSW',cmssw)
        if options.friendStep != None:
          command = command.replace('RPLME_AUX',targetList[iTarget].replace(options.iniStep, options.friendStep))
        # Fix baseW if needed
        if Productions[iProd]['isData'] : baseW = '1.'
        elif iStep == 'baseW' or ( 'isChain' in Steps[iStep] and Steps[iStep]['isChain'] and 'baseW' in Steps[iStep]['subTargets'] ): 
          oriTreeList = []
          for kTarget in targetListBaseW.keys():
            kTargetOri = kTarget
            if '_000' in kTarget :
              kTargetOri = kTarget.split('_000')[0]
            elif '__part' in kTarget :
              kTargetOri = kTarget.split('__part')[0]
            if iTargetOri == kTargetOri : 
              oriTreeList.append(os.path.dirname(oriTree)+'/latino_'+kTarget+'.root')
          #print oriTreeList
          baseWInfo = {}
          baseW = GetBaseW(oriTreeList,iTargetOri,id_iTarget,Productions[iProd]['isData'],xsDB,baseWInfo,cmssw)
          if baseW == '-1' : 
            #xsDB.Print()
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
        if 'iihe' in os.uname()[1]:
          puData=puData.replace('/afs/cern.ch/user/x/xjanssen/public','/user/xjanssen/HWW2015/pudata')
        if 'knu' in os.uname()[1]:
          puData='/u/user/salee/Latino/PUdata/PileupHistogram_Full2016_271036-284044_69p2mb_31Jan17.root'
        if 'sdfarm' in os.uname()[1]:
          puData=puData.replace('/afs/cern.ch/user/x/xjanssen/public','/cms/ldap_home/salee/Latino/PUdata')
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
        # add hadd return code check

        if iStep == 'hadd':
          command+='if (( hadd_return == 0 )); then '

        if not 'UEPS' == iStep :
          if 'iihe' in os.uname()[1]:
            if startingStep == 'Prod' :
              if options.redo: command+='srmrm '+'srm://maite.iihe.ac.be:8443/pnfs/iihe/cms/store/user/' + options.user + '/HWW2015/'+iProd+'/'+iStep+'/latino_'+iTarget+'.root;'
              command+='lcg-cp '+outTree+' '+'srm://maite.iihe.ac.be:8443/pnfs/iihe/cms/store/user/' + options.user + '/HWW2015/'+iProd+'/'+iStep+'/latino_'+iTarget+'.root'
              #command+='pwd;ls -l;srmcp file:///`pwd`/'+outTree+' '+'srm://maite.iihe.ac.be:8443/pnfs/iihe/cms/store/user/' + options.user + '/HWW2015/'+iProd+'/'+iStep+'/latino_'+iTarget+'.root'
            else: 
              if options.redo: command+='srmrm '+'srm://maite.iihe.ac.be:8443/pnfs/iihe/cms/store/user/' + options.user + '/HWW2015/'+iProd+'/'+startingStep+'__'+iStep+'/latino_'+iTarget+'.root;'
              command+='lcg-cp '+outTree+' '+'srm://maite.iihe.ac.be:8443/pnfs/iihe/cms/store/user/' + options.user + '/HWW2015/'+iProd+'/'+startingStep+'__'+iStep+'/latino_'+iTarget+'.root'
          elif 'knu' in os.uname()[1]:
            if startingStep == 'Prod' :
              if options.redo: command+='gfal-rm '+'srm://cluster142.knu.ac.kr:8443/srm/managerv2?SFN=' + outDirBase+'/'+iProd+'/'+iStep+'/latino_'+iTarget+'.root;'
              command+='gfal-copy '+outTree+' '+'srm://cluster142.knu.ac.kr:8443/srm/managerv2?SFN=' + outDirBase + iProd+'/'+iStep+'/latino_'+iTarget+'.root'
            else: 
              if options.redo: command+='gfal-rm '+'srm://cluster142.knu.ac.kr:8443/srm/managerv2?SFN=' + outDirBase + iProd+'/'+startingStep+'__'+iStep+'/latino_'+iTarget+'.root;'
              command+='gfal-copy '+outTree+' '+'srm://cluster142.knu.ac.kr:8443/srm/managerv2?SFN=' + outDirBase+iProd+'/'+startingStep+'__'+iStep+'/latino_'+iTarget+'.root'

          elif 'sdfarm' in os.uname()[1]:
            if startingStep == 'Prod' :
              command+='xrdcp -f '+outTree+' '+ rootReadPath(eosTargBaseOut.split('xrootd')[1])+'/'+iProd+'/'+'Prod__'+iStep+'/latino_'+iTarget+'.root'
            else:
              command+='xrdcp -f '+outTree+' '+ rootReadPath(eosTargBaseOut.split('xrootd')[1])+'/'+iProd+'/'+startingStep+'__'+iStep+'/latino_'+iTarget+'.root'
          else:
            if startingStep == 'Prod' :
              command+='xrdcp -f '+outTree+' '+ eosTargBaseOut+'/'+iProd+'/'+iStep+'/latino_'+iTarget+'.root'
            else:
              command+='xrdcp -f '+outTree+' '+ eosTargBaseOut+'/'+iProd+'/'+startingStep+'__'+iStep+'/latino_'+iTarget+'.root'

        # GarbageCollector 
        if 'sdfarm' in os.uname()[1] or 'hercules' in os.uname()[1]:
          for iGarbage in GarbageCollector: 
            command+='; rm -f '+iGarbage

        logFile=wDir+'/log__'+iTarget+'.log'
        if options.quiet :
          command += ' 2>&1 > /dev/null \n' 
        else:
          command += ' 2>&1 | tee '+logFile+' \n'  

        # add hadd return code check
        if iStep == 'hadd':
          command+='fi'

        # Fix dcap for IIHE
        command = command.replace(' /pnfs/iihe',' dcap://maite.iihe.ac.be/pnfs/iihe')        

        if options.pretend : print "The command is : ", command
        else :
          if  options.runBatch: jobs.Add(stepBatch,iTarget,command)
          else:
            os.system(command) 

      if options.chain :
        isFirstinChain = False
        replaceStep=previousStep
        previousStep=startingStep+'__'+iStep
        targetListKeep=targetList
      else:
        print "Gone batching ..."
        if options.runBatch and not options.pretend: jobs.Sub(options.queue,options.IiheWallTime)

  if options.chain :
    print "Gone batching for Chain ..."
    if options.runBatch and not options.pretend: jobs.Sub(options.queue,options.IiheWallTime)
