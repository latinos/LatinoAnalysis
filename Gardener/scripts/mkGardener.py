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

def GetBaseW(inTreeList,iTarget,id_Input,isData,db,baseWInfo,version='74x'):
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

class fileManager:
  def __init__(self, iniStep,prodDir, prodDirExt, iProd, InputBase, OutputBase):
    self.totalfileList = {}
    self.iniStep       = iniStep
    self.prodDir       = prodDir
    self.prodDirExt    = prodDirExt
    self.iProd         = iProd
    self.InputBase     = InputBase
    self.OutputBase    = OutputBase
    if 'eos/cms' in InputBase:
      self.xrootdPathIn = 'root://eoscms.cern.ch/'
    else:
      self.xrootdPathIn = 'root://eosuser.cern.ch/'
  def getInitFileDir(self):
    if self.iniStep == 'Prod' :
      inFileDir = self.InputBase +'/'+self.prodDir+'/'+ self.prodDirExt
    else:
      inFileDir = self.InputBase +'/'+ self.iProd+'/'+self.iniStep
    return inFileDir
  def getProdDir(self):
    return self.InputBase +'/'+self.prodDir+'/'+ self.prodDirExt
  def getOutDir(self, outputStep ):
    if self.iniStep == 'Prod' :
      outFileDir = self.OutputBase + '/' + self.iProd + '/' + outputStep
    else:
      outFileDir = self.OutputBase + '/' + self.iProd + '/' + self.iniStep+'__'+ outputStep

    # site specific head
    if 'iihe' in os.uname()[1]:
      if not 'pnfs/iihe/cms/' in outFileDir:
	outFileDir = 'pnfs/iihe/cms/' + outFileDir
      else: pass
    elif 'knu' in os.uname()[1]:
      if not '/pnfs/knu.ac.kr/data/cms/' in outFileDir:
	outFileDir = '/pnfs/knu.ac.kr/data/cms/' + outFileDir
      else: pass
    else: pass 

    return outFileDir

  def setInputFile(self, inputFile):
    if'iihe' in os.uname()[1]:
      if 'iihe/cms' in self.getInitFileDir():
        return '/pnfs/iihe/cms/'+self.getInitFileDir().split('iihe/cms')[1]+'/'+inputFile
      else:
        return '/pnfs/iihe/cms/'+self.getInitFileDir()+'/'+inputFile
    elif'knu' in os.uname()[1]:
      if 'knu.ac.kr/data/cms' in self.getInitFileDir():
        return '/pnfs/knu.ac.kr/data/cms/'+self.getInitFileDir().split('knu.ac.kr/data/cms')[1]+'/'+inputFile
      else:
        return '/pnfs/knu.ac.kr/data/cms/'+self.getInitFileDir()+'/'+inputFile
    else:
      if self.iniStep == 'Prod':
	if 'eos/cms' in self.getInitFileDir():
	  return 'root://eoscms.cern.ch//eos/cms'+ self.getInitFileDir().split('eos/cms')[1] + '/' + inputFile
	else:
	  return 'root://eoscms.cern.ch//eos/cms'+ self.getInitFileDir()+ '/' + inputFile
      else:
	return  self.xrootdPathIn+self.getInitFileDir+'/'+iFile

  def getCopyCommand(self, iStep, redo,fileName, fileNameBase):
    outDirFile = self.getOutDir(iStep) + '/latino_'+fileNameBase+'.root'
    command = ''
    if 'iihe' in os.uname()[1]:
      if redo: command+='srmrm '+'srm://maite.iihe.ac.be:8443/' + outDirFile + ';'
      command+='lcg-cp '+fileName+' '+'srm://maite.iihe.ac.be:8443/' + outDirFile
    elif 'knu' in os.uname()[1]:
      if redo: command+= 'gfal-rm srm://cluster142.knu.ac.kr:8443/srm/managerv2?SFN=' + outDirFile + ';'
      command+='gfal-copy '+fileName+' '+'srm://cluster142.knu.ac.kr:8443/srm/managerv2?SFN='+outDirFile
    elif '/eos/cms' in self.OutputBase:
      command+='xrdcp -f '+fileName+' '+ 'root://eoscms.cern.ch/' + ' ' + outDirFile
    else:
      command+='xrdcp -f '+fileName+' '+ 'root://eosuser.cern.ch/' + ' ' + outDirFile

    return command





    

# ------------------------------------------------------- MAIN --------------------------------------------

parser = OptionParser(usage="usage: %prog [options]")

parser.add_option("-p","--prods",   dest="prods"   , help="List of production to run on"              , default=[]     , type='string' , action='callback' , callback=list_maker('prods',','))
parser.add_option("-s","--steps",   dest="steps"   , help="list of Steps to produce"                  , default=[]     , type='string' , action='callback' , callback=list_maker('steps',','))
parser.add_option("-i","--iniStep",   dest="iniStep"   , help="Step to restart from"                      , default='Prod' , type='string' ) 
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

# define parameters
CMSSW_Base=os.environ["CMSSW_BASE"]
cmssw=options.cmssw
# ProdBase, InputBase, OutputBase is defined by default in Gardener/python/Gardener_cfg.py,
InputBase = '/eos/user/j/jlauwers/HWW2015/'
OutputBase= '/eos/user/j/jlauwers/HWW2015/'
if options.inputTarget != None:
  InputBase=options.inputTarget
if options.outputTarget != None:
  OutputBase=options.outputTarget
prodDir = ''
prodDirExt = ''

# fix bTag for 74x
#if options.cmssw == '74x' :
#  Steps['bPogSF']['command'] = 'gardener.py btagPogScaleFactors '  
#  Steps['bPogSF']['do4MC'] = False
#  print Steps['bPogSF']['command']  

# you can change them with option.
#if options.cmssw == '763' :


print "ProdBase    = ", ProdBase
print "InputBase   = ", InputBase
print "OutputBase  = ", OutputBase



#hack to be able to stat both files under /eos/cms and /eos/user
 
aquamarineLocationProd = '0.3.84-aquamarine'
xrootdPathProd         = 'root://eoscms.cern.ch/'

aquamarineLocationIn   = '0.3.84-aquamarine.user'
xrootdPathIn           = 'root://eosuser.cern.ch/'

aquamarineLocationOut  = '0.3.84-aquamarine.user'

if "/eos/cms" in InputBase:
  aquamarineLocationIn = "0.3.84-aquamarine"
  xrootdPathIn = 'root://eoscms.cern.ch/'
if "/eos/cms" in OutputBase:
  aquamarineLocationOut = "0.3.84-aquamarine"

  
# Compile all root macros before sending jobs
if options.runBatch:
  print "Batch mode"
  pathRootMacro = CMSSW_Base + '/src/LatinoAnalysis/Gardener/python/variables/'
  for fn in os.listdir(pathRootMacro):
    if os.path.isfile(pathRootMacro+fn) and fn.endswith('.C'):
      try:
        ROOT.gROOT.LoadMacro(pathRootMacro+fn+'+g')
      except RuntimeError:
        ROOT.gROOT.LoadMacro(pathRootMacro+fn+'++g')

# Loop on input productions
for iProd in prodList :
  if 'cmssw' in Productions[iProd] : cmssw = Productions[iProd]['cmssw']
  # Fix for 74x: can not run these modules: 
  if cmssw == '74x' : Steps['bPogSF']['do4MC'] = False
  if cmssw == '74x' : Steps['genVariables']['do4MC'] = False

  print '----------- Running on production: '+iProd

  # Load sample DB
  samples = {}
  prodFile=CMSSW_Base+'/src/'+Productions[iProd]['samples']
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
  handle.close()
  if 'dir' in Productions[iProd] : prodDir=Productions[iProd]['dir']
  if 'dirExt' in Productions[iProd] : prodDirExt=Productions[iProd]['dirExt']

  # define fileManager class
  if 'fileMan' in locals(): del fileMan
  fileMan=fileManager(options.iniStep, prodDir, prodDirExt, iProd, InputBase, OutputBase)

  # Load x-section DB

  if not Productions[iProd]['isData'] :  
    xsMethods=['Python','YellowR'] # Among 'gDoc','Python','YellowR' and order Matter (Overwriting for same samples !)
    if cmssw == '74x' : xsMethods=['gDoc','Python'] 
    xsFile=CMSSW_Base+'/src/LatinoTrees/AnalysisStep/python/samplesCrossSections.py'
    xsDB = xsectionDB()
    for iMethod in xsMethods :

      if iMethod == 'gDoc'    : xsDB.readGDoc(Productions[iProd]['gDocID'])
      if iMethod == 'Python'  : xsDB.readPython(xsFile)
      if iMethod == 'YellowR' : xsDB.readYR('YR4prel','13TeV')

  # Find existing Input files 
  #if not options.iniStep in Steps: options.iniStep = 'Prod'
  print 'Initial file Dir is ', fileMan.getInitFileDir()
  proc=subprocess.Popen(lsListCommand(fileMan.getInitFileDir(), options.iniStep), stderr = subprocess.PIPE,stdout = subprocess.PIPE, shell = True)
  out, err = proc.communicate()
  InitFileNameAll=string.split(out)
  print "Listing input files: ", InitFileNameAll

  # Initialization for steps
  isFirstinChain = True
  replaceStep=''
  previousStep=''
  InputDirFileListKeep={}

  # Loop on Steps
  for iStep in stepList:
    if ( not Productions[iProd]['isData'] and Steps[iStep]['do4MC'] ) or ( Productions[iProd]['isData'] and Steps[iStep]['do4Data'] ) :
      print '---------------- for Step : ',iStep
      InputDirFileList={}
      # Validate targets tree
      print 'OutFileDir', fileMan.getOutDir(iStep)
      print "lsListCommand", 
      proc=subprocess.Popen(lsListCommand(fileMan.getOutDir(iStep),options.iniStep), stderr = subprocess.PIPE,stdout = subprocess.PIPE, shell = True)
      out, err = proc.communicate()
      OutFileExistList=string.split(out)
      print "OutFileExistList: ", OutFileExistList
      #print samples
      #print samples.keys()
      for iSample in samples : 
        # Tree selector
        selectSample=True
        # ... from options
        if len(options.selTree) > 0 :
          #if 'DYJetsToLL_M-50' in iSample : print iSample
          #print  iSample
          #print options.selTree
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
        #print selectSample
        # And Now add trees
        #if not Productions[iProd]['isData'] :
          #iTree = 'latino_'+iSample+'.root'
          #if iTree in InitFileNameAll: 
          #  if options.redo and selectSample:
          #     InputDirFileList[iSample] = 'NOSPLIT'
          #  else:
          #    if not iTree in OutFileExistList and selectSample: InputDirFileList[iSample] = 'NOSPLIT'
        #else: 
        #if 'ttDM' in iSample: print iSample, selectSample 
        for iFile in InitFileNameAll:
            #if 'DYJetsToLL_M-50_00' in iFile and iSample == 'DYJetsToLL_M-50': print iFile , options.redo ,  iFile in OutFileExistList 
            if options.redo or not iFile in OutFileExistList or iStep == 'hadd' :
              #print iSample 
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
                #print aSample , iSample
                if aSample.replace('_25ns','') == iSample.replace('_25ns','') :
		  InputDirFileList[iKey] = fileMan.setInputFile(iFile)

      #print "InputDirFileList: ", InputDirFileList  

      ##############################################################################################
      # Safeguard against partial run on splitted samples -> Re-include all files from that sample
      ##############################################################################################
      #if  iStep in ['mcwghtcount'] and not Productions[iProd]['isData']: 
      if not Productions[iProd]['isData']: 
        InputDirFileListBaseW = copy.deepcopy(InputDirFileList)
	#print "printing InputDirFileListBaseW", InputDirFileListBaseW
        usedInputSample = []
        for iKeyFile in InputDirFileListBaseW.keys(): 
          if   '_000' in iKeyFile :
            aSample = iKeyFile.split('_000')[0]
            if not aSample in usedInputSample : usedInputSample.append(aSample)
          elif '__part' in iKeyFile:
            aSample = iKeyFile.split('__part')[0]
            if not aSample in usedInputSample : usedInputSample.append(aSample)
        print "usedInputSample", usedInputSample  
        for iUsedSample in usedInputSample:
          for iFile in InitFileNameAll:
            iKey = iFile.replace('latino_','').replace('.root','')
            aSample = iKey
            if '_000' in iKey :
              aSample = iKey.split('_000')[0]
            elif '__part' in iKey :
              aSample = iKey.split('__part')[0] 
            #print aSample, iUsedSample
            if aSample == iUsedSample:
              if not iKey in InputDirFileListBaseW.keys():
                print 'Re-Adding split tree: ', iKey, iFile
		InputDirFileListBaseW[iKey] = fileMan.setInputFile(iFile)



      startingStep = options.iniStep
      if options.chain :
        if not isFirstinChain: 
          print "Gone hacking InputDirFileList for chain"
          #print startingStep,replaceStep,previousStep
          InputDirFileList = InputDirFileListKeep
          for i in InputDirFileList :
            if not replaceStep:
              InputDirFileList[i] =  InputDirFileList[i].replace(InputBase,OutputBase).replace(startingStep,previousStep)
            else:
              InputDirFileList[i] =  InputDirFileList[i].replace(InputBase,OutputBase).replace(replaceStep,previousStep)
          startingStep=previousStep

      #if options.chain and isNotFirstinChain: 
      #   isNotFirstinChain = False
      #   InputDirFileList = InputDirFileListChain
      #InputDirFileListChain=InputDirFileList
      #print "InputDirFileList check 1: ", InputDirFileList
      #for i in InputDirFileList : print i
      #quit() 
      # Create Output Directory on eos
      # TODO lxplus case
      if 'iihe' in os.uname()[1]:
        print 'Using LCG ...'
      elif 'knu' in os.uname()[1]:
	print 'Using gfal ...'
        #if iStep == 'UEPS' :
        #  for iUEPS in Steps[iStep]['cpMap'] :
	#    outDir = TargBaseOut+'/'+iProd+'/'+startingStep+'__'+iUEP
        #    os.system('mkdir -p '+outDir)  
        #else:
        #  if startingStep == 'Prod' :
	#    outDir = TargBaseOut+'/'+iProd+'/'+iStep
        #    os.system('mkdir -p '+ outDir)
        #  else:
	#    outDir = TargBaseOut+'/'+iProd+'/'+startingStep+'__'+iStep
        #    os.system('mkdir -p '+ outDir)
      else:
        if iStep == 'UEPS' :
          for iUEPS in Steps[iStep]['cpMap'] :
            os.system('/afs/cern.ch/project/eos/installation/'+aquamarineLocationOut+'/bin/eos.select mkdir -p '+fileMan.getOutDir(iUEPS))
        else:
          os.system('/afs/cern.ch/project/eos/installation/'+aquamarineLocationOut+'/bin/eos.select mkdir -p '+fileMan.getOutDir(iStep))

      # For hadd Step, regroup Files
      if iStep == 'hadd' :
        inputDirFileGroupList ={} # hadd list without sizeMethod
        inputDirFileGroupSize ={} # sizeMethod list
        for iFileBase in InputDirFileList.keys():
          if '_000' in iFileBase :
            iGroup = iFileBase.split('_000')[0]
          elif '__part' in iFileBase :
            iGroup = iFileBase.split('__part')[0]
          elif Productions[iProd]['isData'] :
            for iSample in samples :
              if iSample.replace('_25ns','') in iFileBase : iGroup = iSample
          else:
            iGroup = iFileBase

          #print iGroup , iFileBase , remoteFileSize(InputDirFileList[iFileBase])

          if not Steps['hadd']['SizeMethod'] :
           if options.redo or not 'latino_'+iGroup+'.root' in OutFileExistList :
            if not iGroup in Steps['hadd']['bigSamples'] or options.forceMerge: 
              if not iGroup in inputDirFileGroupList: inputDirFileGroupList[iGroup] = []
              inputDirFileGroupList[iGroup].append(InputDirFileList[iFileBase])             
            else:
              if not os.path.basename(InputDirFileList[iFileBase]) in OutFileExistList :
               inputDirFileGroupList[iFileBase] = []           
               inputDirFileGroupList[iFileBase].append(InputDirFileList[iFileBase])             
          else:
           if not iGroup in inputDirFileGroupSize: inputDirFileGroupSize[iGroup] = {}
           inputDirFileGroupSize[iGroup][iFileBase]=float(remoteFileSize(InputDirFileList[iFileBase])) 

        # default is 5GB per hadd
        if Steps['hadd']['SizeMethod'] :
         for iGroup in inputDirFileGroupSize:
          iPart=0
          tSize=0
          for (iFile, iSize) in sorted(inputDirFileGroupSize[iGroup].items()) :
            tSize+=iSize
            if tSize > Steps['hadd']['SizeMax']:
              iPart += 1
              tSize = iSize
            haddGroup  = iGroup+'__part'+str(iPart) 
            haddFile = 'latino_'+iGroup+'__part'+str(iPart)+'.root'
            if options.redo or not haddFile in OutFileExistList : 
               #print iFile, iSize , haddFile
               if not haddGroup in inputDirFileGroupList: inputDirFileGroupList[haddGroup] = []
               inputDirFileGroupList[haddGroup].append(InputDirFileList[iFile])  
          if iPart == 0 :
            haddFile = 'latino_'+iGroup+'.root'
            if options.redo or not haddFile in OutFileExistList :         
              inputDirFileGroupList[iGroup] = inputDirFileGroupList.pop(haddGroup)
            else:
              #print haddFile, " exist"
              del inputDirFileGroupList[haddGroup]


        InputDirFileList = inputDirFileGroupList 
        #print InputDirFileList
      # Check job in not already running before allowing it ? 
      keysToDel=[] 
      for iKey in InputDirFileList:
          pidFile=jobDir+'Gardening__'+iProd+'/Gardening__'+iProd+'__'+iStep
          if options.chain: pidFile+='_Chain'
          pidFile+='__'+iKey
          if not startingStep == 'Prod' : pidFile+='____'+startingStep
          pidFile+='.jid'
          if os.path.isfile(pidFile) :
	    print "pidFile", pidFile
            print '--> Job Running already : '+iKey
            keysToDel.append(iKey)
      for iKey in keysToDel:
          del InputDirFileList[iKey]
      # For hadd, we need to check that all jobs are done !

      ######################################################################
      # check if the files are ready after any steps comparing files in Prod
      ######################################################################
      if iStep == 'hadd' : 
        #print InputDirFileList
        keysToDel=[]
        for iGroup in InputDirFileList:
          GroupFiles=[]
          #for jFile in InputDirFileList[iGroup] : 
          #  GroupFiles.append(os.path.basename(jFile))
          filePattern = InputDirFileList[iGroup][0].split('.root')[0]
          if    '_000'   in filePattern : filePattern = filePattern.split('_000')[0]+'_000*.root'
          elif  '__part' in filePattern : filePattern = filePattern.split('__part')[0]+'__part*.root'
          proc=subprocess.Popen(lsListCommand(filePattern), stderr = subprocess.PIPE,stdout = subprocess.PIPE, shell = True)
          out, err = proc.communicate()
          GroupFiles=string.split(out)


          if 'iihe' in os.uname()[1]:
            PrevStep='' 
            if '__' in options.iniStep :
              SubSteps=options.iniStep.split('__')
              for i in range(len(SubSteps)-1) : 
                 PrevStep+=SubSteps[i]
                 if len(SubSteps)-1 > 1 and i < len(SubSteps)-2 : PrevStep+='__'

#            if not '__' in  options.iniStep :
            fileToLook = fileMan.getProdDir()
#            else:
#              fileToLook = 'ls /pnfs/iihe/cms/store/user/' + options.user + '/HWW2015/'+iProd+'/'+PrevStep
          else:
#            if not '__' in  options.iniStep :
            fileToLook = fileMan.getProdDir()
#            else:
#              fileToLook = '/afs/cern.ch/project/eos/installation/'+aquamarineLocationIn+'/bin/eos.select ls '+InputBase+'/'+iProd+'/'+PrevStep

          fileToLook += '/' + os.path.basename(InputDirFileList[iGroup][0]).split('_000')[0].split('__part')[0]
          if   '_000'   in InputDirFileList[iGroup][0] : fileToLook += '_000*.root'
          elif '__part' in InputDirFileList[iGroup][0] : fileToLook += '__part*.root'
          else : fileToLook += '.root'
          #print fileToLook 
          proc=subprocess.Popen(lsListCommand(fileToLook, 'Prod'), stderr = subprocess.PIPE,stdout = subprocess.PIPE, shell = True)
          out, err = proc.communicate()
          ProdGroupFileList=string.split(out)
          haddTest=True
          GroupFilesStrip=[]
          for jFile in GroupFiles : GroupFilesStrip.append(os.path.basename(jFile))  
          for jFile in ProdGroupFileList:
            if not (os.path.basename(jFile)) in GroupFilesStrip : 
                print jFile , os.path.basename(jFile) , iGroup
                haddTest=False
          if not haddTest : keysToDel.append(iGroup)
        for iGroup in keysToDel:
          iKey = iGroup.split('_000')[0].split('__part')[0]
          if not iKey in Steps['hadd']['bigSamples'] or Steps['hadd']['SizeMethod']:
            print '--> HADD: Some jobs stil running/not done : '+iGroup 
            del InputDirFileList[iGroup]

      # Create Jobs Dictionary
      list=[]
      list.append(iStep)
      options.batchSplit.append('Steps')
      #options.batchSplit+=',Steps'
      print 'batchSplit:', options.batchSplit
      bpostFix=''
      if not startingStep == 'Prod' : bpostFix='____'+startingStep
      if options.runBatch: 
        if options.chain: 
          if isFirstinChain:
            list=[iStep+'_Chain']
            stepBatch=iStep+'_Chain'
            print "crating jobs :",'Gardening',iProd,list,InputDirFileList.keys(),options.batchSplit,bpostFix
            jobs = batchJobs('Gardening',iProd,list,InputDirFileList.keys(),options.batchSplit,bpostFix)

        else:
          stepBatch=iStep
          jobs = batchJobs('Gardening',iProd,list,InputDirFileList.keys(),options.batchSplit,bpostFix)
      # Do some preliminary actions for some Steps

      # And now do/create to job for each target
      for inputKey in InputDirFileList.keys(): 
        print "DOING : ",inputKey
        GarbageCollector=[]
        if '_000' in inputKey :
          inputKeyBase = inputKey.split('_000')[0]
        elif '__part' in inputKey :
          inputKeyBase = inputKey.split('__part')[0]
        elif Productions[iProd]['isData'] :
          for iSample in samples :  
            if iSample.replace('_25ns','') in inputKey : inputKeyBase = iSample
        else:
          inputKeyBase = inputKey
        #print inputKeyBase
        if Productions[iProd]['isData'] :
          id_Input='0'
        else:
          id_Input=samples[inputKeyBase][1][1].replace('id=','')
        #print inputKey , inputKeyBase , id_Input
        # Stage in   
        #print InputDirFileList[inputKey] 
        inputKeyDirFile = InputDirFileList[inputKey]  # Pointing to File in case of Split
	wDir  =workDir+'/Gardening__'+iProd+'__'+iStep
        if not os.path.exists(wDir) : os.system('mkdir -p '+wDir) 
        if   options.runBatch : command=''
        else:  
          if 'iihe' or 'knu' in os.uname()[1]:
            command='cd '+wDir+' ; '
          else:       
            command='cd /tmp/'+os.getlogin()+' ; '

        ###############################
        # Command depending on Step
        ###############################
        if iStep == 'hadd' :
#          if 'iihe' or 'knu' in os.uname()[1]:
#            command='cd '+wDir+' ; '
#          else:
#            command+='cd /tmp/'+os.getlogin()+' ; '
            
          outTree ='latino_'+inputKey+'__'+iStep+'.root'
          if len(InputDirFileList[inputKey]) == 1 :
            if not  'iihe' in os.uname()[1]:
              command += 'xrdcp '+InputDirFileList[inputKey][0]+' '+outTree+' ; ' 
            else:
              outTree = 'srm://maite.iihe.ac.be:8443'+InputDirFileList[inputKey][0]
          else:
            command += 'hadd -f '+outTree+' ' 
            for iFile in InputDirFileList[inputKey] : command += iFile+' '
            command += ' ; ' 
            GarbageCollector.append(outTree)
            command += 'hadd_return=$?; ' 

        elif iStep == 'UEPS' :
          for iUEPS in Steps[iStep]['cpMap'] :
            if inputKey in Steps[iStep]['cpMap'][iUEPS] :
              for i in range(len(Steps[iStep]['cpMap'][iUEPS][inputKey])):
                print iUEPS, inputKey , '--->' , Steps[iStep]['cpMap'][iUEPS][inputKey][i]
                outTree = os.path.dirname(inputKeyDirFile)+'__'+iUEPS+'/'+'latino_'+Steps[iStep]['cpMap'][iUEPS][inputKey][i]+'.root'
                print inputKeyDirFile , '--->', outTree 
                command +='lcg-cp srm://maite.iihe.ac.be:8443'+inputKeyDirFile+' srm://maite.iihe.ac.be:8443'+outTree+' '
                if i <  len(Steps[iStep]['cpMap'][iUEPS][inputKey])-1 : command += ' ; '

        # Chains of subTargets
        elif 'isChain' in Steps[iStep] and Steps[iStep]['isChain']:
          iName=''
          cStep=0
          outTree=inputKeyDirFile
          for iSubStep in  Steps[iStep]['subTargets'] :
            cStep+=1
            
            # Tree selector
            selectSample=True
            # ... From iStep
            if 'onlySample' in Steps[iSubStep] : # and not options.ignoreOnlySamples :
              if len(Steps[iSubStep]['onlySample']) > 0 :
                #print Steps[iSubStep]['onlySample'] , iSample , inputKeyBase
                if not inputKeyBase in Steps[iSubStep]['onlySample'] : selectSample=False
            if 'excludeSample' in Steps[iSubStep] :
              if len(Steps[iSubStep]['excludeSample']) > 0 :
                if inputKeyBase in Steps[iSubStep]['excludeSample'] : selectSample=False
            if iSubStep in ['mcweights']: # ,'mcwghtcount' ]  :
              if not 'doMCweights=True' in samples[inputKeyBase][1] : selectSample=False

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
              inTree=outTree              
              outTree ='latino_'+inputKey+'__'+iName+'.root'
	      if '/pnfs/knu.ac.kr/data/cms' in inTree :
		command+=Steps[iSubStep]['command']+' '+rootReadPath(inTree.split('/data/cms')[1])+' '+outTree +' ; '
	      else:
		command+=Steps[iSubStep]['command']+' '+inTree+' '+outTree +' ; '
              GarbageCollector.append(outTree)

        # single Target
        else:
          outTree ='latino_'+inputKey+'__'+iStep+'.root'
          command+=Steps[iStep]['command']+' '+inputKeyDirFile+' '+outTree +' ; '
          GarbageCollector.append(outTree)

        # Fix CMSSW flag;
        command = command.replace('RPLME_CMSSW',cmssw)
        # Fix baseW if needed
        if Productions[iProd]['isData'] : baseW = '1.'
        elif iStep == 'baseW' or ( 'isChain' in Steps[iStep] and Steps[iStep]['isChain'] and 'baseW' in Steps[iStep]['subTargets'] ): 
          DirFile4aSampleList = []
          for iKey in InputDirFileListBaseW.keys():
            iKeyPrun = iKey
            if '_000' in iKey :
              iKeyPrun = iKey.split('_000')[0]
            elif '__part' in iKey :
              iKeyPrun = iKey.split('__part')[0]
            if inputKeyBase == iKeyPrun : 
               DirFile4aSampleList.append(os.path.dirname(inputKeyDirFile)+'/latino_'+iKey+'.root')
          #print DirFile4aSampleList
          baseWInfo = {}
          baseW = GetBaseW(DirFile4aSampleList,inputKeyBase,id_Input,Productions[iProd]['isData'],xsDB,baseWInfo,cmssw)
          if baseW == '-1' : 
             #xsDB.Print()
             exit()
          print baseWInfo
          f = open(wDir+'/baseWInfo.txt', 'a')
          f.write(iProd+' '+inputKeyBase+' : ')
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
        print 'PU Data : ', puData
        command = command.replace('RPLME_puData',puData)  

        # Stage Out
        #if '__part' in inputKey:
        # iPart = inutKey.split('__part')[1].split('_')[0]
        # if startingStep == 'Prod' :
        #   command+='xrdcp '+outTree+' root://eosuser.cern.ch/'+eosTargBase+'/'+iProd+'/'+iStep+'/Split/latino_'+inputKey+'__part'+iPart+'_Out.root'
        # else:
        #   command+='xrdcp '+outTree+' root://eosuser.cern.ch/'+eosTargBase+'/'+iProd+'/'+startingStep+'__'+iStep+'/Split/latino_'+inputKey+'__part'+iPart+'_Out.root'
        #lse:
        # add hadd return code check

        if iStep == 'hadd':
            command+='if (( hadd_return == 0 )); then '

        if not 'UEPS' == iStep :
	  command+= fileMan.getCopyCommand(iStep, options.redo, outTree, inputKey)
	#print 'command', command

        #for iGarbage in GarbageCollector: 
	  #command+='; rm '+iGarbage
        logFile=wDir+'/log__'+inputKey+'.log'
        if options.quiet :
          command += ' 2>&1 > /dev/null \n' 
        else:
          command += ' 2>&1 | tee '+logFile+' \n'  
          
        # add hadd return code check
        if iStep == 'hadd':
            command+='fi'

        print '--------------------------------', options.pretend
	if options.pretend : print "The command is : ", command
        else :
          if  options.runBatch: jobs.Add(stepBatch,inputKey,command)
          else:
	    os.system(command) 

      if options.chain :
        isFirstinChain = False
        replaceStep=previousStep
        previousStep=startingStep+'__'+iStep
        InputDirFileListKeep=InputDirFileList
      else:
        print "Gone batching ..."
        if options.runBatch and not options.pretend: jobs.Sub(options.queue,options.IiheWallTime)

  if options.chain :
    print "Gone batching for Chain ..."
    if options.runBatch and not options.pretend: jobs.Sub(options.queue,options.IiheWallTime)
