#!/usr/bin/env python
import sys, re, os, os.path
import subprocess
import string
import os.path
from LatinoAnalysis.Tools.userConfig  import *

class batchJobs :
   def __init__ (self,baseName,prodName,stepList,targetList,batchSplit):
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
   
         jName  = baseName+'__'+prodName+'__'+kStep+'__'+kTarget
         self.jobsDic[iStep][iTarget] = jName
         if not jName in self.jobsList: self.jobsList.append(jName)
          
     # Create job and init files (loop on Steps,Targets)
     if not os.path.exists(self.subDir) : os.system('mkdir -p '+self.subDir)
     CMSSW=os.environ["CMSSW_BASE"]
     for jName in self.jobsList:
       jFile = open(self.subDir+'/'+jName+'.sh','w')
       jFile.write('#!/bin/bash\n')
       jFile.write('#$ -N '+jName+'\n')
       jFile.write('#$ -q all.q\n')
       jFile.write('#$ -cwd\n')
       jFile.write('pwd')
       jFile.write('source $VO_CMS_SW_DIR/cmsset_default.sh\n') 
       jFile.write('cd '+CMSSW+'\n')
       jFile.write('eval `scramv1 ru -sh`\n')
       jFile.write('ulimit -c 0\n')
       jFile.close()
       os.system('chmod +x '+self.subDir+'/'+jName+'.sh')


   def Add (self,iStep,iTarget,command):
     jName= self.jobsDic[iStep][iTarget]
     print 'Adding to ',self.subDir+'/'+jName  
     jFile = open(self.subDir+'/'+jName+'.sh','a') 
     jFile.write(command+'\n')
     jFile.close()

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
        #print 'cd '+self.subDir+'/'+jName.split('/')[0]+'; bsub -q '+queue+' -o '+outFile+' -e '+errFile+' '+jName.split('/')[1]+'.sh | grep submitted' 
        jobid=os.system('bsub -q '+queue+' -o '+outFile+' -e '+errFile+' '+jobFile+' > '+jidFile)

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
      for iFile in FileList:
        jidFile=iFile.replace('.sh','.jid')
        iStep=iFile.split('__')[3]
        if not iStep in Done: Done[iStep] = 0
        if not iStep in Pend: Pend[iStep] = 0
        if not iStep in Runn: Runn[iStep] = 0
        if not iStep in Tota: Tota[iStep] = 0
        Tota[iStep]+=1
        if os.path.isfile(jidFile):
          iStat = os.popen('cat '+jidFile+' | awk \'{print $2}\' | awk -F\'<\' \'{print $2}\' | awk -F\'>\' \'{print $1}\' | xargs -n 1 bjobs | grep -v "JOBID" | awk \'{print $3}\'').read()
          if 'PEND' in iStat : Pend[iStep]+=1
          else: Runn[iStep]+=1 
        else:
          Done[iStep]+=1
      print iDir+' : '
      for iStep in Done:
        print '     --> '+iStep+' : PENDING= '+str(Pend[iStep])+' RUNNING= '+str(Runn[iStep])+' DONE= '+str(Done[iStep])+' / TOTAL= '+str(Tota[iStep])

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
          os.system('cd '+jobdir+'; rm '+cleanFile)
      try : 
        os.rmdir(jobDir+'/'+iDir) 
      except :
        print 'Some jobs still ongoing in: '+ iDir

#jobs = batchJobs('Gardening','21Oct_25ns',['MCInit','l2sel'],['WW','Top'],['Step','Target'])
#jobs.Add('MCInit','WW','Hello')
#jobs.Sub('8nm')

#batchStatus()
#batchClean()
