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

class NanoProdMaker():

# ------------- Configuration

   def __init__(self) :

     self.checkProxy()

     # CRAB Stage Out Config
     self._storageSite   = 'T2_CH_CERN'
     self._outLFNDirBase = '/store/group/phys_higgs/cmshww/amassiro/NanoProd/'

     # CMS Stuff
     self._cmsswBasedir = os.environ["CMSSW_BASE"]
     self._cmsDriverMC   = 'cmsDriver.py myNanoProdMc   -s NANO --mc   --eventcontent NANOAODSIM --datatier NANOAODSIM --no_exec'
     self._cmsDriverDATA = 'cmsDriver.py myNanoProdData -s NANO --data --eventcontent NANOAOD    --datatier NANOAOD    --no_exec'
     self._customiseFile = 'LatinoAnalysis/NanoProducer/nanoProdCustomise'
     self._customiseFunc = 'nanoProdCustomise_'

     # Cfg
     # self._Sites        = {}
     self._Productions  = {}

     # What to do
     self._prodList     = []
     self._selTree      = []
     self._excTree      = []
     self._redo         = False
     self._pretend      = False 

     # Samples
     self._Samples     = {}

   def Reset(self) :

     # Samples
     self._Samples     = {}

# ------------- checkProxy

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

#------------- Samples

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

# --------------- Job Jandling

   def submitJobs(self,iProd):

      # Prepare Base cmsDriver command     
      if   self._Productions[iProd]['isData'] : cmsDrvBase = self._cmsDriverDATA
      else                                 : cmsDrvBase = self._cmsDriverMC
      cmsDrvBase += ' --conditions ' + self._Productions[iProd]['GlobalTag']
      cmsDrvBase += ' --era '        + self._Productions[iProd]['EraModifiers']
      
      # 
      for iSample in self._Samples :

        # Prepare Directory and check if task was already done
        self._jDir = jobDir+'/NanoProd__'+iProd+'/'+iSample
        if not os.path.exists(self._jDir) : os.system('mkdir -p '+self._jDir)
        self._taskName='nanoAOD__'+iProd+'__'+iSample
        tidFile = self._jDir+'/'+self._taskName+'.tid'
        if os.path.isfile(tidFile) :
           print '--> CRAB Task Running already : ',tidFile
           print '--> Clean if you want ot resubmit'
           continue

        # prepare cmsDriver python
        print '---------------------- Sample = ',iSample
        cmsDrvCmd = cmsDrvBase 
        self._PyCfg=self._jDir+'/'+self._taskName+'.py'
        cmsDrvCmd += ' --python_filename='+self._PyCfg
        self._fileOut=self._taskName+'.root'
        cmsDrvCmd += ' --fileout='+self._fileOut
        if 'customise' in self._Samples[iSample] :
          cmsDrvCmd += ' --customise='
          for iCustom in range(len(self._Samples[iSample]['customise'])) :
            cmsDrvCmd +=self._customiseFile+'.'+self._customiseFunc+self._Samples[iSample]['customise'][iCustom] 
            if len(self._Samples[iSample]['customise'])>1 and iCustom < len(self._Samples[iSample]['customise'])-1: cmsDrvCmd +=','
        os.system(cmsDrvCmd)    

        # prepare the crab Cfg
        self._crabCfg=self._jDir+'/'+self._taskName+'_cfg.py'
        fCfg = open(self._crabCfg,'w')
        fCfg.write('from WMCore.Configuration import Configuration\n')
        fCfg.write('config = Configuration()\n')
        # ... General
        fCfg.write('config.section_(\'General\')\n')
        fCfg.write('config.General.transferLogs = True\n')
        fCfg.write('config.General.requestName = \''+self._taskName+'\'\n') 
        # ... JobType
        fCfg.write('config.section_(\'JobType\')\n')
        fCfg.write('config.JobType.psetName = \''+self._PyCfg+'\'\n')
        fCfg.write('config.JobType.pluginName = \'Analysis\'\n')
        fCfg.write('config.JobType.outputFiles = [\''+self._fileOut+'\']\n')
        # ... Data
        fCfg.write('config.section_(\'Data\')\n')
        # ...... Input Data
        fCfg.write('config.Data.inputDataset = \''+self._Samples[iSample]['miniAOD']+'\'\n') 
        fCfg.write('config.Data.inputDBS = \'global\'\n')
        fCfg.write('config.Data.splitting = \'Automatic\'\n')
        #fCfg.write('config.Data.unitsPerJob = 1\n')
        # ...... Output data
        fCfg.write('config.Data.publication = True\n')
        fCfg.write('config.Data.publishDBS = \'phys03\'\n')
        fCfg.write('config.Data.outputDatasetTag = \''+self._taskName+'\'\n')
        fCfg.write('config.Data.outLFNDirBase = \''+self._outLFNDirBase+'\'\n')

        # ... User
        fCfg.write('config.section_(\'User\')\n')
        # ... Site
        fCfg.write('config.section_(\'Site\')\n')
        fCfg.write('config.Site.blacklist = [\'T3_IT_Bologna\', \'T3_US_UMiss\']\n')
        fCfg.write('config.Site.storageSite = \''+self._storageSite+'\'\n')

        # ... Close
        fCfg.close() 

        print self._crabCfg

        # Submit
        if self._pretend :
          print "Not Submitting, dry run : " + self._taskName
        else:
          print "Submitting to CRAB : " + self._taskName
          os.system('cd '+self._jDir+' ; source /cvmfs/cms.cern.ch/crab3/crab.sh ; crab submit -c '+os.path.basename(self._crabCfg))
          # Check result
          logFile = self._jDir+'/crab_'+self._taskName+'/crab.log'
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
           f = open(self._tidFile,'w')
           f.write('CRABTask = '+taskName)
           f.close()


#------------- Main

   def process(self):

     for iProd in self._prodList:
       print '----------- Running on production: '+iProd
       self.readSampleFile(iProd)
       self.submitJobs(iProd) 
       self.Reset()

