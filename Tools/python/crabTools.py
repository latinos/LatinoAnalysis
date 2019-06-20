#!/usr/bin/env python
import sys, re, os, os.path
import subprocess
import string
import os.path
import socket
import json

# configuration auto-loaded where the job directory and the working directory is defined
from LatinoAnalysis.Tools.userConfig  import *
from LatinoAnalysis.Tools.commonTools  import *

## ----------- THIS IS THE SUBMISSION PART :

class crabTool :
   def __init__ (self,baseName,prodName,stepList,targetList,batchSplit,postFix=''):

     self._cmsswBasedir = os.environ["CMSSW_BASE"]

     # Send our own code sandBox
     self._SendSrcSandBox = True     

     # Common set of bash commands for every job
     self._ScriptHeader = None

     # CRAB Stage Out Config
     self._storageSite   = 'T2_CH_CERN'
     self._outLFNDirBase = '/store/group/phys_higgs/cmshww/amassiro/HWWNanoCrab/'

     # PostCrab Stage Out Config
     self._UnpackCommands = {}
     for iStep in stepList:
       self._UnpackCommands[iStep] = {}
       for iTarget in targetList : 
         self._UnpackCommands[iStep][iTarget] = {}
         self._UnpackCommands[iStep][iTarget]['Files'] = [] 
         self._UnpackCommands[iStep][iTarget]['cpCmd'] = [] 
         self._UnpackCommands[iStep][iTarget]['rmGarbage'] = [] 

     # White/Black lists (Here we can have a default for blacklist and add later):
     self._blacklist = ['T3_IT_Bologna', 'T3_US_UMiss']
     self._whitelist = []

     # Job dictionary
     self._inputFiles = [] 
     self._jobsDic={}
     self._jobsList=[]
     self._baseName = baseName
     self._prodName = prodName
     self._subDir   = jobDir+'/'+baseName+'__'+prodName
     if not os.path.exists(jobDir) : os.system('mkdir -p '+jobDir)


     # Get the job splitting
     for iStep in stepList:
       self._jobsDic[iStep] = {}
       if not 'Step' in batchSplit and len(stepList)>1 :
         kStep = 'AllSteps'
         for jStep in stepList: kStep+='-'+jStep
       else:
         kStep = iStep

       # Init Targets
       for iTarget in targetList:
         self._jobsDic[iStep][iTarget] = ''
         if not 'Target' in batchSplit and len(targetList)>1 :
           kTarget = 'AllTargets'
         else:
           kTarget = iTarget

         jName  = baseName+'__'+prodName+'__'+kStep+'__'+kTarget+postFix
         self._jobsDic[iStep][iTarget] = {}
         self._jobsDic[iStep][iTarget]['jName']       = jName
         self._jobsDic[iStep][iTarget]['Commands']    = []
         self._jobsDic[iStep][iTarget]['outputFiles'] = []
         if not jName in self._jobsList: self._jobsList.append(jName)
    
     # Need an unique name for the crab cfg (allow more than one pass)
     cmd='ls '+self._subDir+'/'+baseName+'__'+prodName+'__'+kStep+postFix+'__crab3cfg_*.py'
     proc=subprocess.Popen(cmd, stderr = subprocess.PIPE,stdout = subprocess.PIPE, shell = True)
     out, err = proc.communicate()
     CfgExist=string.split(out)
     iCfgMax=-1     
     for iCfg in CfgExist :
       nCfg = int(iCfg.split('__crab3cfg_')[1].replace('.py',''))
       if nCfg > iCfgMax : iCfgMax = nCfg
     self._nCfg        = iCfgMax+1 
     self._requestName = baseName+'__'+prodName+'__'+kStep+postFix+'__crab3cfg_'+str(self._nCfg)
     self._outputFile  = self._requestName+'__output.tar'
     self._crabCfg     = self._subDir+'/'+self._requestName+'.py'
     self._crabSh      = self._subDir+'/'+self._requestName+'.sh'
     self._srcSandbox  = self._subDir+'/'+self._requestName+'__srcSandbox.tgz' 
     self._UnpackFile  = self._subDir+'/'+self._requestName+'.unpack'

   def setStorage(self,storageSite,outLFNDirBase): 
     self._storageSite   = storageSite
     self._outLFNDirBase = outLFNDirBase

   def setSiteBlackList(self,blacklist):
     for iSite in blacklist : self._blacklist.append(iSite)  

   def setSiteWhiteList(self,whitelist):
     for iSite in whitelist : self._whitelist.append(iSite)

   def AddInputFile(self,File):
     self._inputFiles.append(File)

   def AddCommand(self,iStep,iTarget,Command):
     self._jobsDic[iStep][iTarget]['Commands'].append(Command)

   def AddJobOutputFile(self,iStep,iTarget,File):
     self._jobsDic[iStep][iTarget]['outputFiles'].append(File) 

   def setUnpackCommands(self,iStep,iTarget,FileList=[],cpCmd=[],rmGarbage=[]):
     self._UnpackCommands[iStep][iTarget]['Files']     = FileList
     self._UnpackCommands[iStep][iTarget]['cpCmd']     = cpCmd
     self._UnpackCommands[iStep][iTarget]['rmGarbage'] = rmGarbage

   def Print(self):
     print "--> Crab Cfg    = " , self._crabCfg
     print "--> Crab Script = " , self._crabSh
     print "--> Unpack File = " , self._UnpackFile 

   def mkCrabCfg(self):
     if len(self._jobsList) == 0 :
       print 'INFO: No jobs to run'
       return

     # Create SrcSandBox
     if self._SendSrcSandBox : 
        self.createSrcSandBox()
        self.AddInputFile(self._srcSandbox)

     print "Creating CRAB3 config" 
     # Needed dummy FrameworkJobReport files
     self.AddInputFile(self._cmsswBasedir+'/src/LatinoAnalysis/Tools/test/FrameworkJobReport.xml')

     # Crab3 cfg
     fCfg = open(self._crabCfg,'w')
     fCfg.write('from WMCore.Configuration import Configuration\n')
     fCfg.write('config = Configuration()\n')
     # ... General
     fCfg.write('config.section_(\'General\')\n') 
     fCfg.write('config.General.transferLogs = True\n') 
     fCfg.write('config.General.requestName = \''+self._requestName+'\'\n')
     # ... JobType
     fCfg.write('config.section_(\'JobType\')\n')
     fCfg.write('config.JobType.psetName = \''+self._cmsswBasedir+'/src/LatinoAnalysis/Tools/test/do_nothing_cfg.py'+'\'\n') 
     fCfg.write('config.JobType.pluginName = \'PrivateMC\'\n')
     fCfg.write('config.JobType.inputFiles = [')
     for iFile in self._inputFiles: fCfg.write('\''+iFile+'\',')  
     fCfg.write(']\n')
     fCfg.write('config.JobType.outputFiles = [\''+self._outputFile+'\']\n')
     fCfg.write('config.JobType.scriptExe = \''+self._crabSh+'\'\n')
     fCfg.write('config.JobType.sendPythonFolder = True\n')
     # ... Data
     fCfg.write('config.section_(\'Data\')\n')
     fCfg.write('config.Data.outputDatasetTag = \''+self._requestName+'\'\n')
     fCfg.write('config.Data.publication = False\n')
     fCfg.write('config.Data.unitsPerJob = 1\n')
     fCfg.write('config.Data.splitting = \'EventBased\'\n') 
     fCfg.write('config.Data.outputPrimaryDataset = \''+self._baseName+'\'\n')
     fCfg.write('config.Data.totalUnits = '+str(len(self._jobsList))+'\n')
     fCfg.write('config.Data.outLFNDirBase = \''+self._outLFNDirBase+'\'\n')
     # ... User
     fCfg.write('config.section_(\'User\')\n')  
     # ... Site
     fCfg.write('config.section_(\'Site\')\n')
     fCfg.write('config.Site.blacklist = [\'T3_IT_Bologna\', \'T3_US_UMiss\']\n')
     fCfg.write('config.Site.storageSite = \''+self._storageSite+'\'\n')
     # ... Close 
     fCfg.close()

     # BASH script for crab
     # ... Error handler
     os.system('cp '+self._cmsswBasedir+'/src/LatinoAnalysis/Tools/test/crab_script_header.sh '+self._crabSh)
     fSh = open(self._crabSh,'a')
     # Unpack srcSandBox
     if self._srcSandbox:
       fSh.write('tar xzf '+os.path.basename(self._srcSandbox)+' -C $CMSSW_BASE\n')
     # ... Common Header (if provided)
     if not self._ScriptHeader == None :
       with open(self._ScriptHeader) as infile: fSh.write(infile.read())
     # ... Jobs
     for iJob in range(1,len(self._jobsList)+1) :
       fSh.write('if [ $1 -eq '+str(iJob)+' ]; then\n')
       jName = self._jobsList[iJob-1]
       for iCommand in self.getCommands(jName): fSh.write('  '+iCommand+'\n')
       #for iFile in self.getJobOutputFiles(jName): fSh.write('  touch '+iFile+'\n')
       fSh.write('  tar -cf '+self._outputFile)
       for iFile in self.getJobOutputFiles(jName): fSh.write(' '+iFile)
       fSh.write('\n') 
       fSh.write('  ls -l\n')
       for iGarbageCmd in self.getGarbageCmd(jName): fSh.write('  '+iGarbageCmd+'\n') 
       fSh.write('fi\n')
     fSh.close()
     os.system('chmod +x '+self._crabSh)

     # Unpacker json
     self.mkUnpack()

   def getCommands(self,jName):
     Commands = []
     for iStep in self._jobsDic:
       for iTarget in self._jobsDic[iStep]:
         if self._jobsDic[iStep][iTarget]['jName'] == jName:
           for iCommand in self._jobsDic[iStep][iTarget]['Commands'] : Commands.append(iCommand)
     return Commands 

   def getJobOutputFiles(self,jName):
     JobOutputFiles = []
     for iStep in self._jobsDic:
       for iTarget in self._jobsDic[iStep]:
         if self._jobsDic[iStep][iTarget]['jName'] == jName:
           for iFile in self._jobsDic[iStep][iTarget]['outputFiles'] : JobOutputFiles.append(iFile)
     return JobOutputFiles

   def getGarbageCmd(self,jName):
     GarbageCmd = []
     for iStep in self._jobsDic:
       for iTarget in self._jobsDic[iStep]:
         if self._jobsDic[iStep][iTarget]['jName'] == jName:
           for iGarbageCmd in self._UnpackCommands[iStep][iTarget]['rmGarbage'] : GarbageCmd.append(iGarbageCmd)
     return GarbageCmd

   def createSrcSandBox(self):
     toExclude="--exclude='*.pyc' --exclude='*/.git*'  --exclude='*_C.so' --exclude='*_C.d' --exclude='*_C_ACLiC_dict_rdict.pcm'"
     os.system('cd '+self._cmsswBasedir+' ; tar czf '+self._srcSandbox+' '+toExclude+' src/*') 

   def mkUnpack(self):
     self._Unpacker = {}
     self._Unpacker['outputPrimaryDataset']     = self._baseName
     self._Unpacker['storageSite']              = self._storageSite
     self._Unpacker['outLFNDirBase']            = self._outLFNDirBase
     self._Unpacker['unpackMap']                = {} 
     for iJob in range(1,len(self._jobsList)+1) :
       jName   = self._jobsList[iJob-1]
       self._Unpacker['unpackMap'][iJob]          = {} 
       self._Unpacker['unpackMap'][iJob]['Files'] = []
       self._Unpacker['unpackMap'][iJob]['cpCmd'] = []
       for iStep in self._jobsDic:
         for iTarget in self._jobsDic[iStep]:
           if self._jobsDic[iStep][iTarget]['jName'] == jName:
             self._Unpacker['unpackMap'][iJob]['jName'] = jName
             for iFile in self._UnpackCommands[iStep][iTarget]['Files'] : self._Unpacker['unpackMap'][iJob]['Files'].append(iFile)
             for iCmd  in self._UnpackCommands[iStep][iTarget]['cpCmd'] : self._Unpacker['unpackMap'][iJob]['cpCmd'].append(iCmd)
     with open(self._UnpackFile, 'w') as f: json.dump(self._Unpacker, f)

   def Sub(self):
      if len(self._jobsList) == 0 :
        print 'INFO: No jobs to run'
        return
      print "Submitting to CRAB:"
      self.Print()
      # Submit
      os.system('cd '+self._subDir+' ; source /cvmfs/cms.cern.ch/crab3/crab.sh ; crab submit -c '+os.path.basename(self._crabCfg))      
      # Check result
      logFile = self._subDir+'/crab_'+self._requestName+'/crab.log'
      succes=False
      taskName=None
      with open(logFile) as search:
        for line in search:
          line = line.rstrip()
          if 'Success: Your task has been delivered to the CRAB3 server' in line : succes=True
          if 'Task name:' in line:
            taskName=line.split()[5]
      print 'Success = ',succes,' --> TaskName = ',taskName
      # Make .jid files
      if succes:
        # Keep the task ID
        tidFile = self._subDir+'/'+self._requestName+'.tid'
        f = open(tidFile,'w')
        f.write('CRABTask = '+taskName)
        f.close() 
        # Create the job ID to lock
        for iJob in range(1,len(self._jobsList)+1) :
          jName   = self._jobsList[iJob-1]
          jidFile = self._subDir+'/'+jName+'.jid'
          f = open(jidFile,'w')
          f.write('CRABTask = '+taskName)
          f.close()


## ----------- THIS IS THE POST-SUBMISSION PART : MONITORING / UNPACKING / CLEANING

class crabMon :

   def __init__ (self,taksFilter=[]):

     self._subDir     = jobDir
     self._taskFilter = taksFilter
     self._taskList   = {}

# ------ COMMON

   def getTaskList(self,done=False):

     self._taskList   = {}
     fileCmd = 'ls '+jobDir
     proc=subprocess.Popen(fileCmd, stderr = subprocess.PIPE,stdout = subprocess.PIPE, shell = True)
     out, err = proc.communicate()
     DirList=string.split(out)
     for iDir in DirList:
       if done :
         fileCmd = 'ls '+jobDir+'/'+iDir+'/'+'*crab3cfg*.done'
       else:
         fileCmd = 'ls '+jobDir+'/'+iDir+'/'+'*crab3cfg*.tid'
       proc=subprocess.Popen(fileCmd, stderr = subprocess.PIPE,stdout = subprocess.PIPE, shell = True)
       out, err = proc.communicate()
       FileList=string.split(out)
       for iFile in FileList:
         taskName = (os.popen('cat '+iFile+' | grep CRABTask | awk \'{print $3}\'').read()).rstrip('\r\n')
         selectTask = False
         if len(self._taskFilter) == 0 : selectTask = True
         else:
           if taskName.split(':')[1].split('_', 2)[-1] in self._taskFilter : selectTask = True
         if selectTask:
           self._taskList[taskName] = {}
           self._taskList[taskName]['subDir']      = os.path.dirname(iFile)+'/'
           self._taskList[taskName]['requestTime'] = taskName.split(':')[0]
           self._taskList[taskName]['requestName'] = taskName.split(':')[1].split('_', 2)[-1]
           self._taskList[taskName]['crabDir']     = 'crab_'+self._taskList[taskName]['requestName']
           self._taskList[taskName]['tidFile']     = iFile
           self._taskList[taskName]['pyCfg']       = iFile.replace('.tid','.py').replace('.done','.py') 
           self._taskList[taskName]['storageSite'] = (os.popen('cat '+self._taskList[taskName]['pyCfg']+'| grep storageSite | awk \'{print $3}\'').read()).rstrip('\r\n').replace('\'','')
           self._taskList[taskName]['outLFNDirBase']  = (os.popen('cat '+self._taskList[taskName]['pyCfg']+'| grep outLFNDirBase | awk \'{print $3}\'').read()).rstrip('\r\n').replace('\'','') 

# ------- STATUS

   def getStatus(self,iTask):
     status = os.popen('crab status -d '+self._taskList[iTask]['subDir']+self._taskList[iTask]['crabDir']).read()
     self._currentTaskStatus = {}
     self._currentTaskStatus['full']       = status
     self._currentTaskStatus['crabServerStatus'] = None
     self._currentTaskStatus['schedulerStatus']  = None
     self._currentTaskStatus['jobsStatus']       = []
     startJobInfo=False
     for line in status.splitlines():
       if 'Status on the CRAB server:' in line : self._currentTaskStatus['crabServerStatus'] = line.split(':')[1].strip() 
       if 'Status on the scheduler:'   in line : self._currentTaskStatus['schedulerStatus']  = line.split(':')[1].strip() 
       if not line : startJobInfo=False
       if startJobInfo: self._currentTaskStatus['jobsStatus'].append(line.lstrip())
       if 'Jobs status:'               in line :
          startJobInfo=True
          self._currentTaskStatus['jobsStatus'].append(line.split(':')[1].lstrip())
             
   def printStatus(self):
     self.getTaskList()
     for iTask in self._taskList:
       print '------- CRAB Status for: ',self._taskList[iTask]['requestName']
       self.getStatus(iTask)
       print 'CRAB Server Status = ',self._currentTaskStatus['crabServerStatus']
       print 'Scheduler Status   = ',self._currentTaskStatus['schedulerStatus']
       print 'Job(s)    Status   : '
       for iJob in self._currentTaskStatus['jobsStatus'] : print ' --> ',iJob

# ------ UNPACKING

   def unpackAll(self):
     self.getTaskList()
     for iTask in self._taskList:
       print '------- UNPACKING TASK: ',self._taskList[iTask]['requestName']
       self.unpackTask(iTask)

   def unpackTask(self,iTask):
     self.getStatus(iTask)
     print 'Scheduler Status   = ',self._currentTaskStatus['schedulerStatus']
     if not ( self._currentTaskStatus['schedulerStatus'] == 'COMPLETED' or self._currentTaskStatus['crabServerStatus'] == 'KILLED' ) :
       print 'WARNING Task not FINISHED -> SKIPPING : STATUS = ',self._currentTaskStatus['schedulerStatus'] 
       return
     # Retrieving Info + Unpacking map
     self._requestName          = self._taskList[iTask]['requestName']
     self._requestTime          = self._taskList[iTask]['requestTime']
     self._subDir               = self._taskList[iTask]['subDir']
     self._crabDir              = self._taskList[iTask]['crabDir']
     self._storageSite          = self._taskList[iTask]['storageSite']
     self._outLFNDirBase        = self._taskList[iTask]['outLFNDirBase']
     self._tidFile              = self._taskList[iTask]['tidFile']
     self._Unpacker             = json.load(open(self._subDir+self._requestName+'.unpack'))          
     self._outputPrimaryDataset = self._Unpacker['outputPrimaryDataset']
     self._storeDir             = self._outLFNDirBase+'/'+self._outputPrimaryDataset+'/'+self._requestName+'/'+self._requestTime+'/'     
 
     # Loop on jobs 
     for iJob in self._Unpacker['unpackMap']:
        jidFile = self._subDir+self._Unpacker['unpackMap'][iJob]['jName']+'.jid'
        if os.path.isfile(jidFile) :
          iDir = "%04d" % int((int(iJob)/1000)*1000)
          storeFile = self._storeDir+'/'+str(iDir)+'/'+self._requestName+'__output_'+iJob+'.tar'
          # check if exist
          lsCmd = lsListCommand(storeFile)
          proc=subprocess.Popen(lsCmd, stderr = subprocess.PIPE,stdout = subprocess.PIPE, shell = True)
          out, err = proc.communicate()
          if storeFile in out : 
            # cp to local directory 
            tmpDir = getTmpDir()
            storeFileLocal = tmpDir+os.path.basename(storeFile)
            srmcp2local(storeFile,storeFileLocal)
            # check for expected content
            FileCheck = True
            proc=subprocess.Popen('tar tf '+storeFileLocal, stderr = subprocess.PIPE,stdout = subprocess.PIPE, shell = True)
            out, err = proc.communicate()
            FileList=string.split(out)
            for iFile in self._Unpacker['unpackMap'][iJob]['Files'] :
              if not iFile in FileList : 
                print 'WARNING: missing output = ',iFile
                print '         --> Going to remove the jidFile anyway to be able to resubmit: ',jidFile
                FileCheck = False
            # STAGE OUT
            if FileCheck:
              command = 'cd '+tmpDir+ ' ; tar xf '+os.path.basename(storeFile)+' ; '
              for cpCmd in self._Unpacker['unpackMap'][iJob]['cpCmd'] : command += cpCmd+' ; '
              for iFile in self._Unpacker['unpackMap'][iJob]['Files'] : command += 'rm '+iFile+' ; '
              command += 'rm '+os.path.basename(storeFile)
              os.system(command)
          else:
            print 'WARNING: storeFile not found = ',storeFile
            print '         --> Going to remove the jidFile anyway to be able to resubmit: ',jidFile
          # Move jidFile to DONE
          os.system('mv '+jidFile+' '+jidFile.replace('.jid','.done'))       
     # Move tidFile to DONE
     os.system('mv '+self._tidFile+' '+self._tidFile.replace('.tid','.done'))       

# ------ CLEANING

   def cleanAll(self):
     self.getTaskList(True)
     for iTask in self._taskList:
       self.cleanTask(iTask)

   def cleanTask(self,iTask):
     print '------- CLEANING TASK: ',self._taskList[iTask]['requestName']
     self.getStatus(iTask)
     print 'Scheduler Status   = ',self._currentTaskStatus['schedulerStatus']
     if not ( self._currentTaskStatus['schedulerStatus'] == 'COMPLETED' or self._currentTaskStatus['crabServerStatus'] == 'KILLED' ):
       print 'WARNING Task not FINISHED -> SKIPPING : STATUS = ',self._currentTaskStatus['schedulerStatus']
       return
     # Retrieving Info + Unpacking map
     self._requestName          = self._taskList[iTask]['requestName']
     self._requestTime          = self._taskList[iTask]['requestTime']
     self._subDir               = self._taskList[iTask]['subDir']
     self._crabDir              = self._taskList[iTask]['crabDir']
     self._storageSite          = self._taskList[iTask]['storageSite']
     self._outLFNDirBase        = self._taskList[iTask]['outLFNDirBase']
     self._tidFile              = self._taskList[iTask]['tidFile']
     self._Unpacker             = json.load(open(self._subDir+self._requestName+'.unpack'))          
     self._outputPrimaryDataset = self._Unpacker['outputPrimaryDataset']
     self._storeDir             = self._outLFNDirBase+'/'+self._outputPrimaryDataset+'/'+self._requestName+'/'+self._requestTime+'/'
     self._motherDir            = self._outLFNDirBase+'/'+self._outputPrimaryDataset+'/'+self._requestName
     if not '.done' in self._tidFile : 
       print 'WARNING Task not UNPACKED -> SKIPPING : tidFile = ',self._tidFile 
       return
     
     print ' ----------------------------------------------->'
     if query_yes_no('DELETE '+self._storeDir+' ??? ') : 
       delDirSE(self._storeDir)
       lsCmd = lsListCommand(self._motherDir)
       proc=subprocess.Popen(lsCmd, stderr = subprocess.PIPE,stdout = subprocess.PIPE, shell = True)
       out, err = proc.communicate()
       List=string.split(out)
       if len(List) == 0 : delDirSE(self._motherDir)
     if query_yes_no('DELETE '+self._requestName+' CONFIG ???') : 
       ext2del=['.done','.sh','.py','__srcSandbox.tgz','.pyc','.unpack']
       for iExt in ext2del: os.system('rm '+self._subDir+self._requestName+iExt)
       for iJob in self._Unpacker['unpackMap']:
         ext2del=['.done','.py']
         for iExt in ext2del: os.system('rm '+self._subDir+self._Unpacker['unpackMap'][iJob]['jName']+iExt)
