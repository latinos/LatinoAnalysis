#!/usr/bin/env python
import sys, re, os, os.path, math, copy
import string
import subprocess

# configuration auto-loaded where the job directory and the working directory is defined
from LatinoAnalysis.Tools.userConfig  import *

# functions used in everyday life ...
from LatinoAnalysis.Tools.commonTools import *
from LatinoAnalysis.Tools.batchTools  import *
from LatinoAnalysis.Tools.crabTools  import *


class PostProcMaker():

# ------------- Configuration

   def __init__(self) : 

     self._cmsswBasedir = os.environ["CMSSW_BASE"] 

     self._aaaXrootd = 'root://cms-xrd-global.cern.ch//'
     self._haddnano  = 'PhysicsTools/NanoAODTools/scripts/haddnano.py'

     # root tree prefix
     self._treeFilePrefix= 'nanoLatino_'

     # site
     self._LocalSite    = None
     self._TargetSite   = None

     # Cfg
     self._Sites        = {}
     self._Steps        = {}
     self._Productions  = {}

     # job mode = Interactive / Batch / Crab / DryRun
     self._pretend      = False 
     self._jobMode      = 'Interactive'
     self._batchQueue   = '8nh'

     # What to do
     self._prodList     = []
     self._stepList     = [] 
     self._iniStep      = None 
     self._selTree      = []
     self._excTree      = []
     self._redo         = False
  
     # Samples
     self._Samples     = {}

     # We need a Proxy !
     self.checkProxy()

   def Reset(self) : 

     # Samples
     self._Samples     = {}

   def checkProxy(self):
     cmd='voms-proxy-info'
     proc=subprocess.Popen(cmd, stderr = subprocess.PIPE,stdout = subprocess.PIPE, shell = True)
     out, err = proc.communicate() 
     # No Proxy at all ?
     if 'Proxy not found' in err : 
       print 'WARNING: No GRID proxy -> Get one first with:' 
       print 'voms-proxy-init -voms cms -rfc --valid 168:0'         
       exit()
     # More than 24h ?
     timeLeft = 0
     for line in out.split("\n"):
       if 'timeleft' in line : timeLeft = int(line.split(':')[1])

     if timeLeft < 24 :
       print 'WARNING: Your proxy is only valid for ',str(timeLeft),' hours -> Renew it with:' 
       print 'voms-proxy-init -voms cms -rfc --valid 168:0'         
       exit()

   def configSite(self,TargetSite=None):
     osName = os.uname()[1]
     for iSite in self._Sites :
       if iSite in osName : self._LocalSite = iSite
     if self._LocalSite == None :
       print 'ERROR: Unknown site : ', osName
       exit()
     print '_LocalSite  = ',self._LocalSite
     print '_TargetSite = ',self._TargetSite

   def configBatch(self,queue):
     if       queue == None                                        \
          and 'batchQueues' in self._Sites[self._LocalSite]        \
          and len(self._Sites[self._LocalSite]['batchQueues']) > 0  :
       self._batchQueue = self._Sites[self._LocalSite]['batchQueues'][0]
       print 'INFO: _batchQueue set to default = ',self._batchQueue
     elif     'batchQueues' in self._Sites[self._LocalSite]         \
          and len(self._Sites[self._LocalSite]['batchQueues']) > 0  :
       if queue in self._Sites[self._LocalSite]['batchQueues'] : self._batchQueue = queue
       else :
         self._batchQueue = self._Sites[self._LocalSite]['batchQueues'][0]
         print 'WARNING: Queue '+queue+' not existing -->  _batchQueue set to default = ',self._batchQueue

   def readSampleFile(self,iProd):
     prodFile=self._cmsswBasedir+'/src/'+self._Productions[iProd]['samples']
     if os.path.exists(prodFile):
       handle = open(prodFile,'r')
       exec(handle)
       self._Samples     = Samples
       handle.close()  
     keys2del = []
     if len(self._selTree) > 0 :
       for iSample in self._Samples :
         if not iSample in self._selTree : keys2del.append(iSample)
     if len(self._excTree) > 0 :
       for iSample in self._Samples :
         if iSample in self._excTree : keys2del.append(iSample)
     for iSample in keys2del : del self._Samples[iSample]

# -------------- File Handling

   def selectSample(self,iProd,iStep,iSample):
      # From Production
      if     'onlySample' in  self._Productions[iProd]              \
         and len(self._Productions[iProd]['onlySample']) > 0        \
         and not iSample in self._Productions[iProd]['onlySample']  : return False
      if     'excludeSample' in self._Productions[iProd]            \
         and len(self._Productions[iProd]['excludeSample']) > 0     \
         and iSample in self._Productions[iProd]['excludeSample']   : return False
      # From Step
      if     'onlySample' in  self._Steps[iStep]              \
         and len(self._Steps[iStep]['onlySample']) > 0        \
         and not iSample in self._Steps[iStep]['onlySample']  : return False
      if     'excludeSample' in self._Steps[iStep]            \
         and len(self._Steps[iStep]['excludeSample']) > 0     \
         and iSample in self._Steps[iStep]['excludeSample']   : return False
      # ---
      return True

   def getTargetFileDic(self,iProd,iStep,iSample,FileList):
     FileDic = {}

     # fileCmd .... Directory
     fileCmd = self._Sites[self._LocalSite]['lsCmd']+' '+self._targetDir
     # fileCmd .... Files
     if len(FileList) == 1 : fileCmd += self._treeFilePrefix+iSample+'.root'
     else                  : fileCmd += self._treeFilePrefix+iSample+'__part*.root'

     # fileCmd .... Exec
     proc=subprocess.Popen(fileCmd, stderr = subprocess.PIPE,stdout = subprocess.PIPE, shell = True)
     out, err = proc.communicate()
     FileExistList=string.split(out)
     # Now Check 
     toSkip=[]
     if not self._redo : 
       if  len(FileExistList) == len(FileList) : return FileDic
       for iFile in FileExistList: toSkip.append(iFile.replace('.root','').split('__part')[1])

     if not self._iniStep == 'Prod' :
       for iFile in FileList : 
         iPart = iFile.replace('.root','').split('__part')[1]
         if not iPart in toSkip : 
           FileDic[iFile] = self._targetDir+os.path.basename(iFile)
     else :
       # Here I have to assume/fix the ordering !!!!
       iPart = 0
       for iFile in FileList:
         if not str(iPart) in toSkip :
           PartName=''
           if len(FileList)>0 : PartName='__part'+str(iPart)
           fileTargetName = self._targetDir+self._treeFilePrefix+iSample+PartName+'.root'
           FileDic[self._aaaXrootd+iFile] = fileTargetName
         iPart +=1 

     return FileDic

   def getTargetFiles(self,iProd,iStep):

     self._targetDic = {}

     for iSample in self._Samples :
       if self.selectSample(iProd,iStep,iSample) :
         # From central (or private) nanoAOD : DAS instance to be declared for ptrivate nAOD
         if self._iniStep == 'Prod' : 
           if 'dasInst' in self._Samples[iSample] : dasInst = self._Samples[iSample]['dasInst']
           else:                                    dasInst = 'prod/global' 
           FileDic = self.getTargetFileDic(iProd,iStep,iSample,self.getFilesFromDAS(self._Samples[iSample]['nanoAOD'],dasInst))
         # From previous PostProc step
         else :
           FileDic = self.getTargetFileDic(iProd,iStep,iSample,getSampleFiles(self._sourceDir,iSample,True,'nanoLatino_',True))
         if len(FileDic) : self._targetDic[iSample] = FileDic

   def getFilesFromDAS(self,dataset,dasInstance='prod/global'):
     dasCmd='dasgoclient -query="instance='+dasInstance+' file dataset='+dataset+'"'
     proc=subprocess.Popen(dasCmd, stderr = subprocess.PIPE,stdout = subprocess.PIPE, shell = True)
     out, err = proc.communicate()
     if not proc.returncode == 0 :
       print out
       print err
       exit()
     FileList=string.split(out)
     return FileList

   def mkFileDir(self,iProd,iStep):

     self._targetDir = None
     self._sourceDir = None
     if not self._iniStep == 'Prod' :
       self._sourceDir = self._Sites[self._LocalSite]['treeBaseDir']+'/'+iProd+'/'+self._iniStep+'/'

     
     if not iStep == 'UEPS' : 

       self._targetDir = self._Sites[self._LocalSite]['treeBaseDir']+'/'+iProd+'/'
       if not self._iniStep == 'Prod' : self._targetDir += self._iniStep+'__'+iStep+'/'
       else                           : self._targetDir += iStep+'/'

       if self._Sites[self._LocalSite]['mkDir'] : os.system('mkdir -p '+ self._targetDir )

     # UEPS
     else:
       for iUEPS in Steps[iStep]['cpMap'] :
         os.system('mkdir -p '+ self._Sites[self._LocalSite]['treeBaseDir']+'/'+iProd+'/'+self._iniStep+'__'+iUEPS)
  
  


# --------------- Job Jandling

   def submitJobs(self,iProd,iStep):

     bpostFix=''
     if not self._iniStep == 'Prod' : bpostFix='____'+self._iniStep

     # Make job directories
     jDir = jobDir+'/NanoGardening__'+iProd
     if not os.path.exists(jDir) : os.system('mkdir -p '+jDir)
     wDir = workDir+'/NanoGardening__'+iProd
     if not os.path.exists(wDir) : os.system('mkdir -p '+wDir)
   

     # prepare targetList
     targetList = []
     for iSample in self._targetDic :
       for iFile in self._targetDic[iSample] :
         iTarget = os.path.basename(self._targetDic[iSample][iFile]).replace(self._treeFilePrefix,'').replace('.root','')
         pidFile=jDir+'/NanoGardening__'+iProd+'__'+iStep+'__'+iTarget+bpostFix+'.jid'
         if os.path.isfile(pidFile) :
           print "pidFile", pidFile
           print '--> Job Running already : '+iTarget
         else: targetList.append(iTarget)

     # Dummy stepList for jobs
     stepList=[]
     stepList.append(iStep)

     if self._jobMode == 'Interactive' :
       print "INFO: Using Interactive command"
     # batchMode Preparation
     elif self._jobMode == 'Batch':
       print "INFO: Using Local Batch"
       self._jobs = batchJobs('NanoGardening',iProd,[iStep],targetList,'Targets,Steps',bpostFix)
       self._jobs.Add2All('cp '+self._cmsswBasedir+'/src/'+self._haddnano+' .')
       self._jobs.AddPy2Sh()
       self._jobs.Add2All('ls -l')
     # CRAB3 Init
     elif self._jobMode == 'Crab':
       print "INFO: Using CRAB3"
       self._crab = crabTool('NanoGardening',iProd,[iStep],targetList,'Targets,Steps',bpostFix)
       self._crab.AddInputFile(self._cmsswBasedir+'/src/'+self._haddnano) 

     for iSample in self._targetDic :
       for iFile in self._targetDic[iSample] :
         iTarget = os.path.basename(self._targetDic[iSample][iFile]).replace(self._treeFilePrefix,'').replace('.root','')
         if iTarget in targetList :
           # Create python
           pyFile=jDir+'/NanoGardening__'+iProd+'__'+iStep+'__'+iTarget+bpostFix+'.py'
           if os.path.isfile(pyFile) : os.system('rm '+pyFile)
           outFile=self._treeFilePrefix+iTarget+'__'+iStep+'.root'
           self.mkPyCfg([self.getStageIn(iFile)],iStep,pyFile,outFile,self._Productions[iProd]['isData'])
           # Stage Out command + cleaning
           stageOutCmd  = self.mkStageOut(outFile,self._targetDic[iSample][iFile])
           rmGarbageCmd = 'rm '+outFile+' ; rm '+ os.path.basename(iFile).replace('.root','_Skim.root') 
           # Interactive 
           if   self._jobMode == 'Interactive' : 
             command = 'cd '+wDir+' ; cp '+self._cmsswBasedir+'/src/'+self._haddnano+' . ; python '+pyFile \
                      +' ; ls -l ; '+stageOutCmd+' ; '+rmGarbageCmd
             if not self._pretend : os.system(command)
             else                 : print command
           # Batch
           elif self._jobMode == 'Batch' : 
             self._jobs.Add(iStep,iTarget,stageOutCmd)
             self._jobs.Add(iStep,iTarget,rmGarbageCmd)
           elif self._jobMode == 'Crab':
             self._crab.AddInputFile(pyFile)  
             self._crab.AddCommand(iStep,iTarget,'python '+os.path.basename(pyFile))
             self._crab.AddJobOutputFile(iStep,iTarget,outFile)
     
     if self._jobMode == 'Batch' and not self._pretend : self._jobs.Sub()
     if self._jobMode == 'Crab': 
        self._crab.Print()
        self._crab.mkCrabCfg()

   def getStageIn(self,File):
      # IIHE
      if     self._LocalSite == 'iihe'                               \
         and not self._Sites[self._LocalSite]['xrootdPath']  in File \
         and     self._Sites[self._LocalSite]['treeBaseDir'] in File :
        return self._Sites[self._LocalSite]['xrootdPath']+File
      else:  
        return File

   def mkStageOut(self,prodFile,storeFile):
      command=''
      # IIHE
      if   self._LocalSite == 'iihe' :
        if self._redo : 
          command += 'srmrm '+self._Sites[self._LocalSite]['srmPrefix']+storeFile+' ; '
        command += 'lcg-cp '+prodFile+' '+self._Sites[self._LocalSite]['srmPrefix']+storeFile
      # CERN
      elif self._LocalSite == 'cern' :
        command = 'xrdcp -f '+prodFile+' '+self._Sites[self._LocalSite]['xrootdPath']+storeFile
      
      # MISSING STAGE OUT
      else :
        print 'ERROR: mkStageOut not available for _LocalSite = ',self._LocalSite
        exit()  

      return command

   def mkPyCfg(self,inputRootFiles,iStep,fPyName,haddFileName=None,isData=False):


     fPy = open(fPyName,'a') 
     
     # Common Header
     fPy.write('#!/usr/bin/env python \n')
     fPy.write('import os, sys \n')
     fPy.write('import ROOT \n')
     fPy.write('ROOT.PyConfig.IgnoreCommandLineOptions = True \n')
     fPy.write(' \n')
     fPy.write('from PhysicsTools.NanoAODTools.postprocessing.framework.postprocessor import PostProcessor \n')
     fPy.write(' \n')

     # Import(s) of modules
     if self._Steps[iStep]['isChain'] :
       for iSubStep in  self._Steps[iStep]['subTargets'] :
         if 'import' in self._Steps[iSubStep] :
           fPy.write('from '+self._Steps[iSubStep]['import']+' import *\n')  
     else:
       if 'import' in self._Steps[iStep] :
         fPy.write('from '+self._Steps[iStep]['import']+' import *\n') 
     fPy.write(' \n')

     # Declaration(s) of in-line modules
     if self._Steps[iStep]['isChain'] :
       for iSubStep in  self._Steps[iStep]['subTargets'] :
         if 'declare' in self._Steps[iSubStep] :
           fPy.write(self._Steps[iSubStep]['declare']+'\n')
     else:
       if 'declare' in self._Steps[iStep] :
         fPy.write(self._Steps[iStep]['declare']+'\n') 
     fPy.write(' \n')

     # Files
     fPy.write('files=[')
     for iFile in inputRootFiles : fPy.write('"'+iFile+'",')
     fPy.write(']\n') 
     fPy.write(' \n')
     
     # Configure modules
     fPy.write('p = PostProcessor(  "."   ,          \n')
     fPy.write('                    files ,          \n')
     fPy.write('                    cut=None ,       \n')
     fPy.write('                    branchsel=None , \n')
     fPy.write('                    modules=[        \n')
     if self._Steps[iStep]['isChain'] :
       for iSubStep in  self._Steps[iStep]['subTargets'] :
         doSubStep = False
         if    isData and self._Steps[iSubStep]['do4Data'] : doSubStep = True
         elif             self._Steps[iSubStep]['do4MC']   : doSubStep = True       
         if doSubStep :  fPy.write('                          '+self._Steps[iSubStep]['module']+',\n')
     else:
       fPy.write('                          '+self._Steps[iStep]['module']+'\n') 
     fPy.write('                            ],      \n') 
     fPy.write('                    provenance=True, \n')
     fPy.write('                    fwkJobReport=True, \n')
     if not haddFileName == None :
       fPy.write('                    haddFileName="'+haddFileName+'", \n')
     fPy.write('                 ) \n')
     fPy.write(' \n')

     # Common footer
     fPy.write('p.run() \n')
     fPy.write(' \n')

     # Close file
     fPy.close()

#------------- Main 

   def process(self):

     for iProd in self._prodList:
       print '----------- Running on production: '+iProd
       self.readSampleFile(iProd) 

       for iStep in self._stepList:
         if    ( not self._Productions[iProd]['isData'] and self._Steps[iStep]['do4MC'] ) \
            or (     self._Productions[iProd]['isData'] and self._Steps[iStep]['do4Data'] ) :
           print '---------------- for Step : ',iStep
           self.mkFileDir(iProd,iStep)
           if not iStep == 'hadd' and not iStep == 'UEPS' :
             self.getTargetFiles(iProd,iStep)
             self.submitJobs(iProd,iStep)
 
       self.Reset()
       


