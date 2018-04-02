#!/usr/bin/env python
import sys, re, os, os.path
import subprocess
import string
import os.path
import socket

# configuration auto-loaded where the job directory and the working directory is defined
from LatinoAnalysis.Tools.userConfig  import *

class crabTool :
   def __init__ (self,baseName,prodName,stepList,targetList,batchSplit,postFix=''):

     self._cmsswBasedir = os.environ["CMSSW_BASE"]

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

   def AddInputFile(self,File):
     self.inputFiles.append(File)

   def AddCommand(self,iStep,iTarget,Command):
     self.jobsDic[iStep][iTarget]['Commands'].append(Command)

   def AddJobOutputFile(self,iStep,iTarget,File):
     self.jobsDic[iStep][iTarget]['outputFiles'].append(File) 

   def Print(self):
     print self.crabCfg
     print self.crabSh
     print self.jobsDic

   def mkCrabCfg(self):
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
     fCfg.write('config.Data.outLFNDirBase = \'/store/group/phys_higgs/cmshww/amassiro/HWWNanoCrab/\'\n')
     # ... User
     fCfg.write('config.section_(\'User\')\n')  
     # ... Site
     fCfg.write('config.section_(\'Site\')\n')
     fCfg.write('config.Site.blacklist = [\'T3_IT_Bologna\', \'T3_US_UMiss\']\n')
     fCfg.write('config.Site.storageSite = \'T2_CH_CERN\'\n')
     # ... Close 
     fCfg.close()

     # BASH script for crab
     fSh = open(self.crabSh,'w')
     fSh.write('set -x\n')
     fSh.write('set -e\n')
     fSh.write('ulimit -s unlimited\n')
     fSh.write('ulimit -c 0 \n')
     fSh.write('\n')
     for iJob in range(1,len(self.jobsList)+1) :
       fSh.write('if [ $1 -eq '+str(iJob)+' ]; then\n')
       jName = self.jobsList[iJob-1]
       for iCommand in self.getCommands(jName): fSh.write('  '+iCommand+'\n')
       fSh.write('  tar -cf '+self.outputFile)
       for iFile in self.getJobOutputFiles(jName): fSh.write(' '+iFile)
       fSh.write('\n') 
       fSh.write('ls -l\n')
       fSh.write('fi\n')
     fSh.close()
     os.system('chmod +x '+self.crabSh)

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
