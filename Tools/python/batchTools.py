#!/usr/bin/env python
import sys, re, os, os.path
import subprocess
import string
import os.path
import socket

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

     #print stepList 
     #print batchSplit

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
       if 'cern' in os.uname()[1] :
         jFile.write('#$ -N '+jName+'\n')
         jFile.write('#$ -q all.q\n')
         jFile.write('#$ -cwd\n')
         jFile.write('export X509_USER_PROXY=/afs/cern.ch/user/'+os.environ["USER"][:1]+'/'+os.environ["USER"]+'/.proxy\n')
       elif "pi.infn.it" in socket.getfqdn():  
         jFile.write('#$ -N '+jName+'\n')
         jFile.write('export X509_USER_PROXY=/home/users/'+os.environ["USER"]+'/.proxy\n')
       elif 'knu' in os.uname()[1]:
         jFile.write('#$ -N '+jName+'\n')
         jFile.write('export X509_USER_PROXY=/u/user/'+os.environ["USER"]+'/.proxy\n')
       elif 'sdfarm' in os.uname()[1]:
         jFile.write('#$ -N '+jName+'\n')
         jFile.write('export VO_CMS_SW_DIR=/cvmfs/cms.cern.ch\n')
         jFile.write('export X509_USER_PROXY=/cms/ldap_home/'+os.environ["USER"]+'/.proxy\n')
       else:
         jFile.write('export X509_USER_PROXY=/user/'+os.environ["USER"]+'/.proxy\n')
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
         elif 'cern' in os.uname()[1]:
           jFile.write("mkdir /tmp/$USER/$LSB_JOBID \n")
           jFile.write("cd /tmp/$USER/$LSB_JOBID \n")
           jFile.write("pwd \n")
         elif "pi.infn.it" in socket.getfqdn():
           jFile.write("mkdir /tmp/$LSB_JOBID \n")
           jFile.write("cd /tmp/$LSB_JOBID \n")
           jFile.write("pwd \n")
         elif 'ifca' in os.uname()[1]:
           jFile.write("cd /gpfs/projects/cms/"+os.environ["USER"]+"/ \n") 
         elif 'sdfarm' or 'knu' in os.uname()[1]:
           jFile.write('cd '+self.subDir+'\n')
         else:
           jFile.write('cd - \n')
           ### the following makes the .sh script exit if an error is thrown after the "set -e" command
           jFile.write('set -e \n')
       else              : jFile.write('cd '+wDir+' \n')
       jFile.close()
       if usePython : pFile.close()
       os.system('chmod +x '+self.subDir+'/'+jName+'.sh')

     # Create Proxy at IIHE
     if 'cern'  in os.uname()[1]:
       cmd='voms-proxy-info'
       proc=subprocess.Popen(cmd, stderr = subprocess.PIPE,stdout = subprocess.PIPE, shell = True)
       out, err = proc.communicate()
       for line in out.split('\n'):
        if "path" in line:
          proxypath=line.split(':')[1]
       os.system('cp '+proxypath+' /afs/cern.ch/user/'+os.environ["USER"][:1]+'/'+os.environ["USER"]+'/.proxy\n')
     if 'iihe'  in os.uname()[1]:
       #os.system('voms-proxy-init --voms cms:/cms/becms --valid 168:0')
       os.system('cp $X509_USER_PROXY /user/'+os.environ["USER"]+'/.proxy')
     if "pi.infn.it" in socket.getfqdn():  
       os.system('cp $X509_USER_PROXY /home/users/'+os.environ["USER"]+'/.proxy')
     if "knu" in os.uname()[1]: 
       os.system('cp $X509_USER_PROXY /u/user/'+os.environ["USER"]+'/.proxy')
       #os.system('cp /tmp/x509up_u$UID /u/user/'+os.environ["USER"]+'/.proxy')
     if "sdfarm" in os.uname()[1]: 
       os.system('cp $X509_USER_PROXY /cms/ldap_home/'+os.environ["USER"]+'/.proxy')

   def Add (self,iStep,iTarget,command):
     jName= self.jobsDic[iStep][iTarget]
     #print 'Adding to ',self.subDir+'/'+jName  
     jFile = open(self.subDir+'/'+jName+'.sh','a') 
     jFile.write(command+'\n')
     jFile.close()

   def Add2All (self,command):
     for jName in self.jobsList:
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

   def GetPyName (self,iStep,iTarget) :
     jName= self.jobsDic[iStep][iTarget]
     return self.subDir+'/'+jName+'.py' 

   def Sub(self,queue='8nh',IiheWallTime='168:00:00',optTodo=False): 
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
        print 'Submit',jName, ' on ', queue
        if 'iihe' in os.uname()[1] : 
          queue='localgrid@cream02'
          QSOPT='-l walltime='+IiheWallTime
          nTry=0
          while nTry < 3 : 
            nTry+=1
            jobid=os.system('qsub '+QSOPT+' -N '+jName+' -q '+queue+' -o '+outFile+' -e '+errFile+' '+jobFile+' > '+jidFile)
            print 'TRY #:', nTry , '--> Jobid : ' , jobid
            if jobid == 0 : nTry = 999
            else:  os.system('rm '+jidFile)
          if not jobid == 0 and optTodo :
            todoFile = open(self.subDir+'/'+jName+'.todo','w')
            todoFile.write('qsub '+QSOPT+' -N '+jName+' -q '+queue+' -o '+outFile+' -e '+errFile+' '+jobFile+' > '+jidFile)
            todoFile.close()

	elif 'knu' in os.uname()[1]:
          #print 'cd '+self.subDir+'/'+jName.split('/')[0]+'; bsub -q '+queue+' -o '+outFile+' -e '+errFile+' '+jName.split('/')[1]+'.sh | grep submitted' 
          #print 'qsub -q '+queue+' -o '+outFile+' -e '+errFile+' '+jobFile+' > '+jidFile
          jobid=os.system('qsub -q '+queue+' -o '+outFile+' -e '+errFile+' '+jobFile+' > '+jidFile)
          #print 'bsub -q '+queue+' -o '+outFile+' -e '+errFile+' '+jobFile+' > '+jidFile
        elif 'sdfarm' in os.uname()[1]:
          jdsFileName=self.subDir+'/'+jName+'.jds'
          jdsFile = open(jdsFileName,'w')
          #jdsFile = open(self.subDir+'/'+jName+'.jds','w')
          jdsFile.write('executable = '+self.subDir+'/'+jName+'.sh\n')
          jdsFile.write('universe = vanilla\n')
          jdsFile.write('output = '+self.subDir+'/'+jName+'.out\n')
          jdsFile.write('error = '+self.subDir+'/'+jName+'.err\n')
          jdsFile.write('log = '+self.subDir+'/'+jName+'.log\n')
          #jdsFile.write('should_transfer_files = YES\n')
          #jdsFile.write('when_to_transfer_output = ON_EXIT\n')
          #jdsFile.write('transfer_input_files = '+jName+'.sh\n')
          jdsFile.write('queue\n')
          jdsFile.close()
	  #print "jdsFile: ", jdsFileName,"jidFile: ", jidFile 
          jobid=os.system('condor_submit '+jdsFileName+' > ' +jidFile)
        elif 'ifca' in os.uname()[1] :
          jobid=os.system('qsub -P l.gaes -S /bin/bash -cwd -N Latino -o '+outFile+' -e '+errFile+' '+jobFile+' -j y > '+jidFile)
        elif "pi.infn.it" in socket.getfqdn():
          queue="cms"
          jobid=os.system('bsub -q '+queue+' -o '+outFile+' -e '+errFile+' '+jobFile+' > '+jidFile)
        else:
          #print 'cd '+self.subDir+'/'+jName.split('/')[0]+'; bsub -q '+queue+' -o '+outFile+' -e '+errFile+' '+jName.split('/')[1]+'.sh | grep submitted' 
          jobid=os.system('bsub -q '+queue+' -o '+outFile+' -e '+errFile+' '+jobFile+' > '+jidFile)
		  #print 'bsub -q '+queue+' -o '+outFile+' -e '+errFile+' '+jobFile+' > '+jidFile

   def AddCopy (self,iStep,iTarget,inputFile,outputFile):
     "Copy file from local to remote server (outputFile = /store/...)"
     
     jName= self.jobsDic[iStep][iTarget]
     #print 'Adding to ',self.subDir+'/'+jName  
     jFile = open(self.subDir+'/'+jName+'.sh','a') 
     if 'iihe' in os.uname()[1] :
        jFile.write('lcg-cp '+inputFile+' srm://maite.iihe.ac.be:8443/pnfs/iihe/cms'+outputFile+'\n')
     elif 'ifca' in os.uname()[1] :
        jFile.write('mv '+inputFile+' /gpfs/gaes/cms'+outputFile+'\n')
     elif "pi.infn.it" in socket.getfqdn():   
        jFile.write('lcg-cp '+inputFile+' srm://stormfe1.pi.infn.it:8444/srm/managerv2?SFN=/cms'+outputFile+'\n')
     elif 'knu' in os.uname()[1] :
        jFile.write('gfal-copy '+inputFile+' srm://cluster142.knu.ac.kr:8443/srm/managerv2?SFN=/pnfs/knu.ac.kr/data/cms/'+outputFile+'\n')
     elif 'sdfarm' in os.uname()[1] :
        jFile.write('gfal-copy -p '+inputFile+' srm://cms-se.sdfarm.kr:8443/srm/v2/server?SFN=/xrootd/'+outputFile+'\n')
     else :
        jFile.write('cp '+inputFile+ " " + outputFile+'\n')
     jFile.close()

def batchStatus():
    fileCmd = 'ls '+jobDir
    proc=subprocess.Popen(fileCmd, stderr = subprocess.PIPE,stdout = subprocess.PIPE, shell = True)
    out, err = proc.communicate()
    DirList=string.split(out)
    for iDir in DirList:
      fileCmd = 'ls '+jobDir+'/'+iDir+'/'+'*.sh | grep -v crab3cfg' 
      proc=subprocess.Popen(fileCmd, stderr = subprocess.PIPE,stdout = subprocess.PIPE, shell = True)
      out, err = proc.communicate()
      FileList=string.split(out) 
      Done={}
      Pend={}
      Runn={}
      Crab={}
      Tota={}
      FileRuns={}
      for iFile in FileList:
        jidFile=iFile.replace('.sh','.jid')
        iStep=iFile.split('__')[3]
        iSample=iFile.split('__')[4].replace('.sh','')
        if not iStep in Done: Done[iStep] = 0
        if not iStep in Pend: Pend[iStep] = 0
        if not iStep in Runn: Runn[iStep] = 0
        if not iStep in Crab: Crab[iStep] = 0
        if not iStep in Tota: Tota[iStep] = 0
        if not iStep in FileRuns: FileRuns[iStep] = []
        Tota[iStep]+=1
        if os.path.isfile(jidFile):
          # check if not CRAB:
          iCrab = os.popen('cat '+jidFile+' | awk \'{print $1}\' ').read()
          print iCrab
          if 'CRABTask' in iCrab : Crab[iStep]+=1 
          else:
            if 'iihe' in os.uname()[1] :
              iStat = os.popen('cat '+jidFile+' | awk -F\'.\' \'{print $1}\' | xargs -n 1 qstat | grep localgrid | awk \'{print $5}\' ').read()
              if 'Q' in iStat : Pend[iStep]+=1
              else: Runn[iStep]+=1
            elif 'ifca' in os.uname()[1] :	
              iStat = os.popen('qstat | grep \" qw \" |  awk \'{print $1 \" '+jidFile+'\"}\' | xargs -n 2 grep | awk \'{ print $2 }\' ').read()
	      if 'job' in iStat : Pend[iStep]+=1	
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
        print '     --> '+iStep+' : PENDING= '+str(Pend[iStep])+' RUNNING= '+str(Runn[iStep])+' DONE= '+str(Done[iStep])+' CRAB= '+str(Crab[iStep])+' / TOTAL= '+str(Done[iStep]) +'/'+str(Tota[iStep])
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

def batchResub(Dir='ALL',queue='8nh',IiheWallTime='168:00:00',optTodo=True):
    if Dir == 'ALL' :
      fileCmd = 'ls '+jobDir
      proc=subprocess.Popen(fileCmd, stderr = subprocess.PIPE,stdout = subprocess.PIPE, shell = True)
      out, err = proc.communicate()
      DirList=string.split(out)
    else:
      DirList=[Dir]

    for iDir in DirList:

      # This is for big crunch of jobs that were planned ahead
      fileCmd = 'ls '+jobDir+'/'+iDir+'/'+'*.todo'
      proc=subprocess.Popen(fileCmd, stderr = subprocess.PIPE,stdout = subprocess.PIPE, shell = True)
      out, err = proc.communicate()
      FileList=string.split(out)
      for iFile in FileList:
        jidFile=iFile.replace('.todo','.jid')
        if 'iihe' in os.uname()[1] :
          jobid=os.system('bash '+iFile)
          print 'Submitting ' , iFile
          if jobid == 0 : os.system('rm '+iFile)
          else          : os.system('rm '+jidFile)

      # Do some search fo missing jobs ?
      fileCmd = 'ls '+jobDir+'/'+iDir+'/'+'*.sh'
      proc=subprocess.Popen(fileCmd, stderr = subprocess.PIPE,stdout = subprocess.PIPE, shell = True)
      out, err = proc.communicate()
      FileList=string.split(out)
      for iFile in FileList:
        jidFile=iFile.replace('.sh','.jid') 
        doneFile=iFile.replace('.sh','.done') 
        todoFile=iFile.replace('.sh','.todo')
        redoFile=iFile.replace('.sh','.redo')
        if not os.path.isfile(jidFile) and not os.path.isfile(doneFile) and not  os.path.isfile(todoFile) and not os.path.isfile(redoFile) :
          os.system('touch '+redoFile)

      # Here we resub jobs that were manually killed for which we have a .redo file 
      fileCmd = 'ls '+jobDir+'/'+iDir+'/'+'*.redo'
      proc=subprocess.Popen(fileCmd, stderr = subprocess.PIPE,stdout = subprocess.PIPE, shell = True)
      out, err = proc.communicate()
      FileList=string.split(out)
      for iFile in FileList:
        subDir = os.path.dirname(iFile)
        jName  = os.path.basename(iFile).split('.')[0]
        print subDir , ' ---> ', jName
        jobFile=subDir+'/'+jName+'.sh'
        errFile=subDir+'/'+jName+'.err'
        outFile=subDir+'/'+jName+'.out'
        jidFile=subDir+'/'+jName+'.jid'
        print 'Submit',jName, ' on ', queue

        if os.path.isfile(jidFile) : 
          os.system('echo rm '+jidFile)

        if 'iihe' in os.uname()[1] :
          queue='localgrid@cream02'
          QSOPT='-l walltime='+IiheWallTime
          nTry=0
          while nTry < 3 :
            nTry+=1
            jobid=os.system('qsub '+QSOPT+' -N '+jName+' -q '+queue+' -o '+outFile+' -e '+errFile+' '+jobFile+' > '+jidFile)
            print 'TRY #:', nTry , '--> Jobid : ' , jobid
            if jobid == 0 : nTry = 999
            else:  os.system('rm '+jidFile)
          if jobid == 0 : os.system('rm '+iFile)   
          if not jobid == 0 and optTodo :
            todoFile = open(self+'/'+jName+'.todo','w')
            todoFile.write('qsub '+QSOPT+' -N '+jName+' -q '+queue+' -o '+outFile+' -e '+errFile+' '+jobFile+' > '+jidFile)
            todoFile.close()
        elif 'knu' in os.uname()[1]:
          jobid=os.system('qsub -q '+queue+' -o '+outFile+' -e '+errFile+' '+jobFile+' > '+jidFile)
          if jobid == 0 : os.system('rm '+iFile)   
          else: os.system('rm '+jidFile)
        elif 'sdfarm' in os.uname()[1]:
          jdsFileName=self.subDir+'/'+jName+'.jds'
          jdsFile = open(self.subDir+'/'+jName+'.jds','w')
          jdsFile.write('executable = '+self.subDir+'/'+jName+'.sh\n')
          jdsFile.write('universe = vanilla\n')
          jdsFile.write('output = '+self.subDir+'/'+jName+'.out\n')
          jdsFile.write('error = '+self.subDir+'/'+jName+'.err\n')
          jdsFile.write('log = '+self.subDir+'/'+jName+'.log\n')
          #jdsFile.write('should_transfer_files = YES\n')
          #jdsFile.write('when_to_transfer_output = ON_EXIT\n')
          #jdsFile.write('transfer_input_files = '+jName+'.sh\n')
          jdsFile.write('queue\n')
          jdsFile.close()
          jobid=os.system('condor_submit '+jdsFileName+' > ' +jidFile)
          if jobid == 0 : os.system('rm '+iFile)   
          else: os.system('rm '+jidFile)
        elif 'ifca' in os.uname()[1] :
          jobid=os.system('qsub -P l.gaes -S /bin/bash -cwd -N Latino -o '+outFile+' -e '+errFile+' '+jobFile+' -j y > '+jidFile)
          if jobid == 0 : os.system('rm '+iFile)   
          else: os.system('rm '+jidFile)
        elif "pi.infn.it" in socket.getfqdn():
          queue="cms"
          jobid=os.system('bsub -q '+queue+' -o '+outFile+' -e '+errFile+' '+jobFile+' > '+jidFile)
          if jobid == 0 : os.system('rm '+iFile)   
          else: os.system('rm '+jidFile)
        else:
          #print 'cd '+self.subDir+'/'+jName.split('/')[0]+'; bsub -q '+queue+' -o '+outFile+' -e '+errFile+' '+jName.split('/')[1]+'.sh | grep submitted' 
          jobid=os.system('bsub -q '+queue+' -o '+outFile+' -e '+errFile+' '+jobFile+' > '+jidFile)
          if jobid == 0 : os.system('rm '+iFile)   
          else: os.system('rm '+jidFile)
                  #print 'bsub -q '+queue+' -o '+outFile+' -e '+errFile+' '+jobFile+' > '+jidFile



def batchTest():
    jobs = batchJobs('Test','Test',['Test'],['Test'],['Step','Target'])
    jobs.Add('Test','Test','echo Hello World')
    jobs.Add('Test','Test','sleep 120')
    jobs.Sub()

#jobs = batchJobs('Gardening','21Oct_25ns',['MCInit','l2sel'],['WW','Top'],['Step','Target'])
#jobs.Add('MCInit','WW','Hello')
#jobs.Sub('8nm')

#batchStatus()
#batchClean()
