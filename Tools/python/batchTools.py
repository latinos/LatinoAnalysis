#!/usr/bin/env python
import sys, re, os, os.path
import subprocess
import string
import os.path

# configuration auto-loaded where the job directory and the working directory is defined
from LatinoAnalysis.Tools.userConfig  import *

class batchJobs :
   def __init__ (self,baseName,prodName,stepList,targetList,batchSplit,postFix='',usePython=False,useBatchDir=True,wDir=''):
     # baseName   = Gardening, Plotting, ....
     # prodName   = 21Oct_25ns , ...
     # stepList   = list of steps (like l2sel or a set of plots to produce)
     # targetList = list of targets (aka tree)
     # batchSplit = How to split jobs ( by Step, Target)
     self.jobsDic={}
     self.jobsList=[]
     self.baseName = baseName
     self.prodName = prodName
     self.subDir   = jobDir+'/'+baseName+'__'+prodName
     if not os.path.exists(jobDir) : os.system('mkdir -p '+jobDir)     

     print stepList 
     print batchSplit

     # Init Steps
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
         self.jobsDic[iStep][iTarget] = jName
         if not jName in self.jobsList: self.jobsList.append(jName)
          
     # Create job and init files (loop on Steps,Targets)
     if not os.path.exists(self.subDir) : os.system('mkdir -p '+self.subDir)
     CMSSW=os.environ["CMSSW_BASE"]
     SCRAMARCH=os.environ["SCRAM_ARCH"]
     for jName in self.jobsList:
       jFile = open(self.subDir+'/'+jName+'.sh','w')
       if usePython : pFile = open(self.subDir+'/'+jName+'.py','w') 
       jFile.write('#!/bin/bash\n')
       if 'cern' in os.uname()[1]:
         jFile.write('#$ -N '+jName+'\n')
         jFile.write('#$ -q all.q\n')
         jFile.write('#$ -cwd\n')
       elif 'knu' in os.uname()[1]:
         jFile.write('#$ -N '+jName+'\n')
         jFile.write('#$ -q all.q\n')
         jFile.write('#$ -cwd\n')
       else:
         jFile.write('export X509_USER_PROXY=/user/xjanssen/.proxy\n')
       jFile.write('export SCRAM_ARCH='+SCRAMARCH+'\n')
       jFile.write('source $VO_CMS_SW_DIR/cmsset_default.sh\n') 
       jFile.write('cd '+CMSSW+'\n')
       jFile.write('eval `scramv1 ru -sh`\n')
       if 'knu' in os.uname()[1]:
	 pass
       else:
	 jFile.write('ulimit -c 0\n')
       if    useBatchDir : 
         if 'iihe' in os.uname()[1]:
           jFile.write('cd $TMPDIR \n')
         else:
           jFile.write('cd - \n')
       else              : jFile.write('cd '+wDir+' \n')
       jFile.close()
       if usePython : pFile.close()
       os.system('chmod +x '+self.subDir+'/'+jName+'.sh')

     # Create Proxy at IIHE
     if 'iihe'  in os.uname()[1]:
       #os.system('voms-proxy-init --voms cms:/cms/becms --valid 168:0')
       os.system('cp $X509_USER_PROXY /user/xjanssen/.proxy')

   def Add (self,iStep,iTarget,command):
     jName= self.jobsDic[iStep][iTarget]
     print 'Adding to ',self.subDir+'/'+jName  
     jFile = open(self.subDir+'/'+jName+'.sh','a') 
     jFile.write(command+'\n')
     jFile.close()

   def InitPy (self,command):

     os.system('cd '+self.subDir)
     for jName in self.jobsList:
       pFile = open(self.subDir+'/'+jName+'.py','a')
       pFile.write(command+'\n')
       pFile.close()

   def AddPy2Sh(self):
     for jName in self.jobsList: 
       jFile = open(self.subDir+'/'+jName+'.sh','a')
       command = 'python '+self.subDir+'/'+jName+'.py'
       jFile.write(command+'\n')
       jFile.close()

   def AddPy (self,iStep,iTarget,command):
     jName= self.jobsDic[iStep][iTarget]
     print 'Adding to ',self.subDir+'/'+jName
     pFile = open(self.subDir+'/'+jName+'.py','a')
     pFile.write(command+'\n')
     pFile.close()


   def Sub(self,queue='8nh'): 
     os.system('cd '+self.subDir)
     for jName in self.jobsList:
        print self.subDir+'/'+jName
        jobFile=self.subDir+'/'+jName+'.sh' 
        errFile=self.subDir+'/'+jName+'.err'
        outFile=self.subDir+'/'+jName+'.out'
        jidFile=self.subDir+'/'+jName+'.jid'
        jFile = open(self.subDir+'/'+jName+'.sh','a')
        jFile.write('mv '+jidFile+' '+jidFile.replace('.jid','.done') )
        jFile.close()
        jidFile=self.subDir+'/'+jName+'.jid'
        print 'Submit',jName
        if 'iihe' in os.uname()[1] : 
          queue='localgrid@cream02'
          QSOPT=''
          nTry=0
          while nTry < 5 : 
            nTry+=1
            jobid=os.system('qsub '+QSOPT+' -N '+jName+' -q '+queue+' -o '+outFile+' -e '+errFile+' '+jobFile+' > '+jidFile)
            print 'TRY #:', nTry , '--> Jobid : ' , jobid
            if jobid == 0 : nTry = 999

	elif 'knu' in os.uname()[1]:
          #print 'cd '+self.subDir+'/'+jName.split('/')[0]+'; bsub -q '+queue+' -o '+outFile+' -e '+errFile+' '+jName.split('/')[1]+'.sh | grep submitted' 
          #print 'qsub -q '+queue+' -o '+outFile+' -e '+errFile+' '+jobFile+' > '+jidFile
          jobid=os.system('qsub -q '+queue+' -o '+outFile+' -e '+errFile+' '+jobFile+' > '+jidFile)
          #print 'bsub -q '+queue+' -o '+outFile+' -e '+errFile+' '+jobFile+' > '+jidFile
        else:
          #print 'cd '+self.subDir+'/'+jName.split('/')[0]+'; bsub -q '+queue+' -o '+outFile+' -e '+errFile+' '+jName.split('/')[1]+'.sh | grep submitted' 
          jobid=os.system('bsub -q '+queue+' -o '+outFile+' -e '+errFile+' '+jobFile+' > '+jidFile)
          #print 'bsub -q '+queue+' -o '+outFile+' -e '+errFile+' '+jobFile+' > '+jidFile

def batchStatus():
    fileCmd = 'ls '+jobDir
    proc=subprocess.Popen(fileCmd, stderr = subprocess.PIPE,stdout = subprocess.PIPE, shell = True)
    out, err = proc.communicate()
    DirList=string.split(out)
    for iDir in DirList:
      fileCmd = 'ls '+jobDir+'/'+iDir+'/'+'*.sh' 
      proc=subprocess.Popen(fileCmd, stderr = subprocess.PIPE,stdout = subprocess.PIPE, shell = True)
      out, err = proc.communicate()
      FileList=string.split(out)
      Done={}
      Pend={}
      Runn={}
      Tota={}
      FileRuns={}
      for iFile in FileList:
        jidFile=iFile.replace('.sh','.jid')
        iStep=iFile.split('__')[3]
        iSample=iFile.split('__')[4].replace('.sh','')
        if not iStep in Done: Done[iStep] = 0
        if not iStep in Pend: Pend[iStep] = 0
        if not iStep in Runn: Runn[iStep] = 0
        if not iStep in Tota: Tota[iStep] = 0
        if not iStep in FileRuns: FileRuns[iStep] = []
        Tota[iStep]+=1
        if os.path.isfile(jidFile):
#         print jidFile
          if 'iihe' in os.uname()[1] :
            iStat = os.popen('cat '+jidFile+' | awk -F\'.\' \'{print $1}\' | xargs -n 1 qstat | grep localgrid  | awk \'{print $5}\' ').read()
            if 'Q' in iStat : Pend[iStep]+=1
            else: Runn[iStep]+=1
          else:
            iStat = os.popen('cat '+jidFile+' | awk \'{print $2}\' | awk -F\'<\' \'{print $2}\' | awk -F\'>\' \'{print $1}\' | xargs -n 1 bjobs | grep -v "JOBID" | awk \'{print $3}\'').read()
            if 'PEND' in iStat : Pend[iStep]+=1
            else: Runn[iStep]+=1 
          FileRuns[iStep].append(iSample)
        else:
          Done[iStep]+=1
      print '----------------------------'
      print iDir+' : '
      print '----------------------------'
      for iStep in Done:
        print '     --> '+iStep+' : PENDING= '+str(Pend[iStep])+' RUNNING= '+str(Runn[iStep])+' DONE= '+str(Done[iStep])+' / TOTAL= '+str(Done[iStep]) +'/'+str(Tota[iStep])
      print '   Samples not done:'
      for iStep in Done:
        print '     --> '+iStep+' : ',FileRuns[iStep]

def batchClean():
    fileCmd = 'ls '+jobDir
    proc=subprocess.Popen(fileCmd, stderr = subprocess.PIPE,stdout = subprocess.PIPE, shell = True)
    out, err = proc.communicate()
    DirList=string.split(out)
    for iDir in DirList:
      fileCmd = 'ls '+jobDir+'/'+iDir+'/'+'*.sh'
      proc=subprocess.Popen(fileCmd, stderr = subprocess.PIPE,stdout = subprocess.PIPE, shell = True)
      out, err = proc.communicate()
      FileList=string.split(out)
      for iFile in FileList:
        doneFile=iFile.replace('.sh','.done')
        if os.path.isfile(doneFile):
          cleanFile=iFile.replace('.sh','.*')
          print 'Clean',cleanFile
          os.system('cd '+jobDir+'; rm '+cleanFile)
      try : 
        os.rmdir(jobDir+'/'+iDir) 
      except :
        print 'Some jobs still ongoing in: '+ iDir

#jobs = batchJobs('Gardening','21Oct_25ns',['MCInit','l2sel'],['WW','Top'],['Step','Target'])
#jobs.Add('MCInit','WW','Hello')
#jobs.Sub('8nm')

#batchStatus()
#batchClean()
