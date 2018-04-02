#!/usr/bin/env python
import sys, re, os, os.path
import subprocess
import string
import os.path
import socket
import json

# configuration auto-loaded where the job directory and the working directory is defined
from LatinoAnalysis.Tools.userConfig  import *

## ----------- THIS IS THE SUBMISSION PART :

class crabTool :
   def __init__ (self,baseName,prodName,stepList,targetList,batchSplit,postFix=''):

     self._cmsswBasedir = os.environ["CMSSW_BASE"]

     # CRAB Stage Out Config
     self.storageSite   = 'T2_CH_CERN'
     self.outLFNDirBase = '/store/group/phys_higgs/cmshww/amassiro/HWWNanoCrab/'

     # PostCrab Stage Out Config
     self.UnpackCommands = {}
     for iStep in stepList:
       self.UnpackCommands[iStep] = {}
       for iTarget in targetList : 
         self.UnpackCommands[iStep][iTarget] = {}
         self.UnpackCommands[iStep][iTarget]['Files'] = [] 
         self.UnpackCommands[iStep][iTarget]['cpCmd'] = [] 
         self.UnpackCommands[iStep][iTarget]['rmGarbage'] = [] 

     # White/Black lists (Here we can have a default for blacklist and add later):
     self.blacklist = ['T3_IT_Bologna', 'T3_US_UMiss']
     self.whitelist = []

     # Job dictionary
     self.inputFiles = [] 
     self.jobsDic={}
     self.jobsList=[]
     self.baseName = baseName
     self.prodName = prodName
     self.subDir   = jobDir+'/'+baseName+'__'+prodName
     if not os.path.exists(jobDir) : os.system('mkdir -p '+jobDir)


     # Get the job splitting
     for iStep in stepList:
       self.jobsDic[iStep] = {}
       if not 'Step' in batchSplit and len(stepList)>1 :
         kStep = 'AllSteps'
         for jStep in stepList: kStep+='-'+jStep
       else:
         kStep = iStep

       # Init Targets
       for iTarget in targetList:
         self.jobsDic[iStep][iTarget] = ''
         if not 'Target' in batchSplit and len(targetList)>1 :
           kTarget = 'AllTargets'
         else:
           kTarget = iTarget

         jName  = baseName+'__'+prodName+'__'+kStep+'__'+kTarget+postFix
         self.jobsDic[iStep][iTarget] = {}
         self.jobsDic[iStep][iTarget]['jName']       = jName
         self.jobsDic[iStep][iTarget]['Commands']    = []
         self.jobsDic[iStep][iTarget]['outputFiles'] = []
         if not jName in self.jobsList: self.jobsList.append(jName)
    
     # Need an unique name for the crab cfg (allow more than one pass)
     cmd='ls '+self.subDir+'/'+baseName+'__'+prodName+'__'+kStep+postFix+'__crab3cfg_*.py'
     proc=subprocess.Popen(cmd, stderr = subprocess.PIPE,stdout = subprocess.PIPE, shell = True)
     out, err = proc.communicate()
     CfgExist=string.split(out)
     iCfgMax=-1     
     for iCfg in CfgExist :
       nCfg = int(iCfg.split('__crab3cfg_')[1].replace('.py',''))
       if nCfg > iCfgMax : iCfgMax = nCfg
     self.nCfg        = iCfgMax+1 
     self.requestName = baseName+'__'+prodName+'__'+kStep+postFix+'__crab3cfg_'+str(self.nCfg)
     self.outputFile  = self.requestName+'__output.tar'
     self.crabCfg     = self.subDir+'/'+self.requestName+'.py'
     self.crabSh      = self.subDir+'/'+self.requestName+'.sh'
     self.UnpackFile  = self.subDir+'/'+self.requestName+'.unpack'

   def setStorage(self,storageSite,outLFNDirBase): 
     self.storageSite   = storageSite
     self.outLFNDirBase = outLFNDirBase

   def setSiteBlackList(self,blacklist):
     for iSite in blacklist : self.blacklist.append(iSite)  

   def setSiteWhiteList(self,whitelist):
     for iSite in whitelist : self.whitelist.append(iSite)

   def AddInputFile(self,File):
     self.inputFiles.append(File)

   def AddCommand(self,iStep,iTarget,Command):
     self.jobsDic[iStep][iTarget]['Commands'].append(Command)

   def AddJobOutputFile(self,iStep,iTarget,File):
     self.jobsDic[iStep][iTarget]['outputFiles'].append(File) 

   def setUnpackCommands(self,iStep,iTarget,FileList=[],cpCmd=[],rmGarbage=[]):
     self.UnpackCommands[iStep][iTarget]['Files']     = FileList
     self.UnpackCommands[iStep][iTarget]['cpCmd']     = cpCmd
     self.UnpackCommands[iStep][iTarget]['rmGarbage'] = rmGarbage

   def Print(self):
     print "--> Crab Cfg    = " , self.crabCfg
     print "--> Crab Script = " , self.crabSh
     print "--> Unpack File = " , self.UnpackFile 

   def mkCrabCfg(self):
     if len(self.jobsList) == 0 :
       print 'INFO: No jobs to run'
       return
     print "Creating CRAB3 config" 
     # Needed dummy FrameworkJobReport files
     self.AddInputFile(self._cmsswBasedir+'/src/LatinoAnalysis/Tools/test/FrameworkJobReport.xml')

     # Crab3 cfg
     fCfg = open(self.crabCfg,'w')
     fCfg.write('from WMCore.Configuration import Configuration\n')
     fCfg.write('config = Configuration()\n')
     # ... General
     fCfg.write('config.section_(\'General\')\n') 
     fCfg.write('config.General.transferLogs = True\n') 
     fCfg.write('config.General.requestName = \''+self.requestName+'\'\n')
     # ... JobType
     fCfg.write('config.section_(\'JobType\')\n')
     fCfg.write('config.JobType.psetName = \''+self._cmsswBasedir+'/src/LatinoAnalysis/Tools/test/do_nothing_cfg.py'+'\'\n') 
     fCfg.write('config.JobType.pluginName = \'PrivateMC\'\n')
     fCfg.write('config.JobType.inputFiles = [')
     for iFile in self.inputFiles: fCfg.write('\''+iFile+'\',')  
     fCfg.write(']\n')
     fCfg.write('config.JobType.outputFiles = [\''+self.outputFile+'\']\n')
     fCfg.write('config.JobType.scriptExe = \''+self.crabSh+'\'\n')
     # ... Data
     fCfg.write('config.section_(\'Data\')\n')
     fCfg.write('config.Data.outputDatasetTag = \''+self.requestName+'\'\n')
     fCfg.write('config.Data.publication = False\n')
     fCfg.write('config.Data.unitsPerJob = 1\n')
     fCfg.write('config.Data.splitting = \'EventBased\'\n') 
     fCfg.write('config.Data.outputPrimaryDataset = \''+self.baseName+'\'\n')
     fCfg.write('config.Data.totalUnits = '+str(len(self.jobsList))+'\n')
     fCfg.write('config.Data.outLFNDirBase = \''+self.outLFNDirBase+'\'\n')
     # ... User
     fCfg.write('config.section_(\'User\')\n')  
     # ... Site
     fCfg.write('config.section_(\'Site\')\n')
     fCfg.write('config.Site.blacklist = [\'T3_IT_Bologna\', \'T3_US_UMiss\']\n')
     fCfg.write('config.Site.storageSite = \''+self.storageSite+'\'\n')
     # ... Close 
     fCfg.close()

     # BASH script for crab
     os.system('cp '+self._cmsswBasedir+'/src/LatinoAnalysis/Tools/test/crab_script_header.sh '+self.crabSh)
     fSh = open(self.crabSh,'a')
     for iJob in range(1,len(self.jobsList)+1) :
       fSh.write('if [ $1 -eq '+str(iJob)+' ]; then\n')
       jName = self.jobsList[iJob-1]
       #for iCommand in self.getCommands(jName): fSh.write('  '+iCommand+'\n')
       for iFile in self.getJobOutputFiles(jName): fSh.write('  touch '+iFile+'\n')
       fSh.write('  tar -cf '+self.outputFile)
       for iFile in self.getJobOutputFiles(jName): fSh.write(' '+iFile)
       fSh.write('\n') 
       fSh.write('  ls -l\n')
       for iGarbageCmd in self.getGarbageCmd(jName): fSh.write('  '+iGarbageCmd+'\n') 
       fSh.write('fi\n')
     fSh.close()
     os.system('chmod +x '+self.crabSh)

     # Unpacker json
     self.mkUnpack()

   def getCommands(self,jName):
     Commands = []
     for iStep in self.jobsDic:
       for iTarget in self.jobsDic[iStep]:
         if self.jobsDic[iStep][iTarget]['jName'] == jName:
           for iCommand in self.jobsDic[iStep][iTarget]['Commands'] : Commands.append(iCommand)
     return Commands 

   def getJobOutputFiles(self,jName):
     JobOutputFiles = []
     for iStep in self.jobsDic:
       for iTarget in self.jobsDic[iStep]:
         if self.jobsDic[iStep][iTarget]['jName'] == jName:
           for iFile in self.jobsDic[iStep][iTarget]['outputFiles'] : JobOutputFiles.append(iFile)
     return JobOutputFiles

   def getGarbageCmd(self,jName):
     GarbageCmd = []
     for iStep in self.jobsDic:
       for iTarget in self.jobsDic[iStep]:
         if self.jobsDic[iStep][iTarget]['jName'] == jName:
           for iGarbageCmd in self.UnpackCommands[iStep][iTarget]['rmGarbage'] : GarbageCmd.append(iGarbageCmd)
     return GarbageCmd

   def mkUnpack(self):
     self.Unpacker = {}
     for iJob in range(1,len(self.jobsList)+1) :
       jName   = self.jobsList[iJob-1]
       self.Unpacker[iJob] = {} 
       self.Unpacker[iJob]['Files'] = []
       self.Unpacker[iJob]['cpCmd'] = []
       for iStep in self.jobsDic:
         for iTarget in self.jobsDic[iStep]:
           if self.jobsDic[iStep][iTarget]['jName'] == jName:
             for iFile in self.UnpackCommands[iStep][iTarget]['Files'] : self.Unpacker[iJob]['Files'].append(iFile)
             for iCmd  in self.UnpackCommands[iStep][iTarget]['cpCmd'] : self.Unpacker[iJob]['cpCmd'].append(iCmd)
     with open(self.UnpackFile, 'w') as f: json.dump(self.Unpacker, f)

   def Sub(self):
      if len(self.jobsList) == 0 :
        print 'INFO: No jobs to run'
        return
      print "Submitting to CRAB:"
      self.Print()
      # Submit
      os.system('cd '+self.subDir+' ; source /cvmfs/cms.cern.ch/crab3/crab.sh ; crab submit -c '+os.path.basename(self.crabCfg))      
      # Check result
      logFile = self.subDir+'/crab_'+self.requestName+'/crab.log'
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
        tidFile = self.subDir+'/'+self.requestName+'.tid'
        f = open(tidFile,'w')
        f.write('CRABTask = '+taskName)
        f.close() 
        # Create the job ID to lock
        for iJob in range(1,len(self.jobsList)+1) :
          jName   = self.jobsList[iJob-1]
          jidFile = self.subDir+'/'+jName+'.jid'
          f = open(jidFile,'w')
          f.write('CRABTask = '+taskName)
          f.close()


## ----------- THIS IS THE POST-SUBMISSION PART : MONITORING / UNPACKING / CLEANING

class crabMon :

   def __init__ (self,taksFilter=[]):

     self.subDir     = jobDir
     self.taskFilter = taksFilter
     self.taskList   = {}

# ------ COMMON

   def getTaskList(self):

     self.taskList   = {}
     fileCmd = 'ls '+jobDir
     proc=subprocess.Popen(fileCmd, stderr = subprocess.PIPE,stdout = subprocess.PIPE, shell = True)
     out, err = proc.communicate()
     DirList=string.split(out)
     for iDir in DirList:
       fileCmd = 'ls '+jobDir+'/'+iDir+'/'+'*.tid'
       proc=subprocess.Popen(fileCmd, stderr = subprocess.PIPE,stdout = subprocess.PIPE, shell = True)
       out, err = proc.communicate()
       FileList=string.split(out)
       for iFile in FileList:
         taskName = (os.popen('cat '+iFile+' | grep CRABTask | awk \'{print $3}\'').read()).rstrip('\r\n')
         selectTask = False
         if len(self.taskFilter) == 0 : selectTask = True
         else:
           if taskName.split(':')[1].split('_', 2)[-1] in self.taskFilter : selectTask = True
         if selectTask:
           self.taskList[taskName] = {}
           self.taskList[taskName]['subDir']      = os.path.dirname(iFile)+'/'
           self.taskList[taskName]['requestTime'] = taskName.split(':')[0]
           self.taskList[taskName]['requestName'] = taskName.split(':')[1].split('_', 2)[-1]
           self.taskList[taskName]['crabDir']     = 'crab_'+self.taskList[taskName]['requestName']
           self.taskList[taskName]['tidFile']     = iFile
           self.taskList[taskName]['pyCfg']       = iFile.replace('.tid','.py') 
           self.taskList[taskName]['storageSite'] = (os.popen('cat '+self.taskList[taskName]['pyCfg']+'| grep storageSite | awk \'{print $3}\'').read()).rstrip('\r\n').replace('\'','')
           self.taskList[taskName]['outLFNDirBase']  = (os.popen('cat '+self.taskList[taskName]['pyCfg']+'| grep outLFNDirBase | awk \'{print $3}\'').read()).rstrip('\r\n').replace('\'','') 

# ------- STATUS

   def getStatus(self,iTask):
     status = os.popen('crab status -d '+self.taskList[iTask]['subDir']+self.taskList[iTask]['crabDir']).read()
     self.currentTaskStatus = {}
     self.currentTaskStatus['full']       = status
     self.currentTaskStatus['crabServerStatus'] = None
     self.currentTaskStatus['schedulerStatus']  = None
     self.currentTaskStatus['jobsStatus']       = []
     startJobInfo=False
     for line in status.splitlines():
       if 'Status on the CRAB server:' in line : self.currentTaskStatus['crabServerStatus'] = line.split(':')[1].strip() 
       if 'Status on the scheduler:'   in line : self.currentTaskStatus['schedulerStatus']  = line.split(':')[1].strip() 
       if not line : startJobInfo=False
       if startJobInfo: self.currentTaskStatus['jobsStatus'].append(line.lstrip())
       if 'Jobs status:'               in line :
          startJobInfo=True
          self.currentTaskStatus['jobsStatus'].append(line.split(':')[1].lstrip())
             
   def printStatus(self):
     self.getTaskList()
     for iTask in self.taskList:
       print '------- CRAB Status for: ',self.taskList[iTask]['requestName']
       self.getStatus(iTask)
       print 'CRAB Server Status = ',self.currentTaskStatus['crabServerStatus']
       print 'Scheduler Status   = ',self.currentTaskStatus['schedulerStatus']
       print 'Job(s)    Status   : '
       for iJob in self.currentTaskStatus['jobsStatus'] : print ' --> ',iJob

# ------ UNPACKING

   def unpackAll(self):
     self.getTaskList()
     for iTask in self.taskList:
       print '------- UNPACKING TASK: ',self.taskList[iTask]['requestName']
       self.unpackTask(iTask)

   def unpackTask(self,iTask):
     self.getStatus(iTask)
     if not self.currentTaskStatus['schedulerStatus'] == 'COMPLETED':
       print 'WARNING Task not FINISHED -> SKIPPING : STATUS = ',self.currentTaskStatus['schedulerStatus'] 
       return
     print self.taskList[iTask]
     # Getting list of output
     #fileCmd = 'ls '
     #proc=subprocess.Popen(fileCmd, stderr = subprocess.PIPE,stdout = subprocess.PIPE, shell = True)
     #out, err = proc.communicate()
     #DirList=string.split(out)

# ------ CLEANING

