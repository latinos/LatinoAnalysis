#!/usr/bin/env python
import sys, re, os, os.path
import subprocess
import string
import json
import os.path
import socket

# configuration auto-loaded where the job directory and the working directory is defined
from LatinoAnalysis.Tools.userConfig  import *

try:
   # batchType can be set in userConfig (only relevant when running at CERN)
   CERN_USE_LSF = (batchType == 'lsf')
except NameError:
   # if batchType is not set, default to HTCondor
   CERN_USE_LSF = False

try:
  JOB_DIR_SPLIT = ( jobDirSplit == True ) 
except NameError:
  JOB_DIR_SPLIT = False
#Avoid using this feature for tools that are not ready for it -> change it in the tool after loading the library

try:
   CONDOR_ACCOUNTING_GROUP = condorAccountingGroup
except NameError:
   CONDOR_ACCOUNTING_GROUP = ''

class batchJobs :
   def __init__ (self,baseName,prodName,stepList,targetList,batchSplit,postFix='',usePython=False,useBatchDir=True,wDir='',JOB_DIR_SPLIT_READY=False):
     # baseName   = Gardening, Plotting, ....
     # prodName   = 21Oct_25ns , ...
     # stepList   = list of steps (like l2sel or a set of plots to produce)
     # targetList = list of targets (aka tree)
     # batchSplit = How to split jobs ( by Step, Target)
     self.jobsDic={}
     self.jobsList=[]
     self.baseName = baseName
     self.prodName = prodName
     self.JOB_DIR_SPLIT_READY = JOB_DIR_SPLIT_READY
     if JOB_DIR_SPLIT and self.JOB_DIR_SPLIT_READY:
       if len(stepList) == 1 : StepName = stepList[0]
       else:
         StepName = ''
         for iStep in stepList : StepName+=iStep
       self.subDir   = jobDir+'/'+baseName+'__'+prodName+'__'+StepName
     else:
       self.subDir   = jobDir+'/'+baseName+'__'+prodName
     if not os.path.exists(jobDir) : os.system('mkdir -p '+jobDir)
     self.nThreads = 1

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
         elif type(iTarget) is tuple:
           if len(iTarget) == 2:
              kTarget = '%s.%d' % iTarget
           else:
              kTarget = '%s.%d.%d' % iTarget
         else:
           kTarget = iTarget
   
         jName  = baseName+'__'+prodName+'__'+kStep+'__'+kTarget+postFix
         self.jobsDic[iStep][iTarget] = jName
         if not jName in self.jobsList: self.jobsList.append(jName)

     # Submit host name to identify the environment
     hostName = os.uname()[1]
          
     # Create job and init files (loop on Steps,Targets)
     if not os.path.exists(self.subDir) : os.system('mkdir -p '+self.subDir)
     CMSSW=os.environ["CMSSW_BASE"]
     SCRAMARCH=os.environ["SCRAM_ARCH"]
     for jName in self.jobsList:
       if JOB_DIR_SPLIT and self.JOB_DIR_SPLIT_READY :
         subDirExtra = '/' + jName.split('__')[3] 
         if not os.path.exists(self.subDir+subDirExtra) : os.system('mkdir -p '+self.subDir+subDirExtra)
       else:
         subDirExtra =''
       jFile = open(self.subDir+subDirExtra+'/'+jName+'.sh','w')
       if usePython : pFile = open(self.subDir+subDirExtra+'/'+jName+'.py','w') 
       jFile.write('#!/bin/bash\n')
       if 'cern' in hostName:
         jFile.write('#$ -N '+jName+'\n')
         if CERN_USE_LSF:
           jFile.write('#$ -q all.q\n')
           jFile.write('#$ -cwd\n')

         jFile.write('export X509_USER_PROXY=/afs/cern.ch/user/'+os.environ["USER"][:1]+'/'+os.environ["USER"]+'/.proxy\n')
       elif "pi.infn.it" in socket.getfqdn():  
         jFile.write('#$ -N '+jName+'\n')
         jFile.write('export X509_USER_PROXY=/home/users/'+os.environ["USER"]+'/.proxy\n')
       elif 'knu' in hostName:
         jFile.write('#$ -N '+jName+'\n')
         jFile.write('export X509_USER_PROXY=/u/user/'+os.environ["USER"]+'/.proxy\n')
       elif 'sdfarm' in hostName:
         jFile.write('#$ -N '+jName+'\n')
         jFile.write('export VO_CMS_SW_DIR=/cvmfs/cms.cern.ch\n')
         jFile.write('export X509_USER_PROXY=/cms/ldap_home/'+os.environ["USER"]+'/.proxy\n')
       elif 'hercules' in hostName:
         jFile.write('#$ -N '+jName+'\n')
         jFile.write('export VO_CMS_SW_DIR=/cvmfs/cms.cern.ch\n')
         jFile.write('export X509_USER_PROXY=/gwpool/users/'+os.environ["USER"]+'/.proxy\n')
       else:
         jFile.write('export X509_USER_PROXY=/user/'+os.environ["USER"]+'/.proxy\n')
       if 'CONFIGURATION_DIRECTORY' in os.environ:
         jFile.write('export CONFIGURATION_DIRECTORY='+os.environ['CONFIGURATION_DIRECTORY']+'\n')
       jFile.write('voms-proxy-info\n')
       jFile.write('export SCRAM_ARCH='+SCRAMARCH+'\n')
       jFile.write('export VO_CMS_SW_DIR=/cvmfs/cms.cern.ch\n')
       jFile.write('source $VO_CMS_SW_DIR/cmsset_default.sh\n') 
       jFile.write('cd '+CMSSW+'\n')
       jFile.write('eval `scramv1 ru -sh`\n')
       if 'knu' in hostName or 'hercules' in hostName:
         pass
       else:
         jFile.write('ulimit -c 0\n')
       if    useBatchDir : 
         if 'iihe' in hostName:
           jFile.write('cd $TMPDIR \n')
         elif 'cern' in hostName:
           if not CERN_USE_LSF:
             jFile.write('cd $TMPDIR \n')
           else:
             jFile.write("mkdir /tmp/$USER/$LSB_JOBID \n")
             jFile.write("cd /tmp/$USER/$LSB_JOBID \n")

           jFile.write("pwd \n")

         elif "pi.infn.it" in socket.getfqdn():
           jFile.write("mkdir /tmp/$LSB_JOBID \n")
           jFile.write("cd /tmp/$LSB_JOBID \n")
           jFile.write("pwd \n")
         elif 'ifca' in hostName:
           jFile.write("cd /gpfs/projects/cms/"+os.environ["USER"]+"/ \n") 
         elif 'sdfarm' in hostName or 'knu' in hostName:
           jFile.write('cd '+self.subDir+subDirExtra+'\n')
         elif 'hercules' in hostName:
           tmpdataDir = jobDir + "/tmp/" + baseName +"_"+prodName
           jFile.write("mkdir "+ jobDir + "/tmp\n")
           jFile.write("mkdir "+ tmpdataDir +  "\n")
           jFile.write("cd "+ tmpdataDir + "\n")
           jFile.write("pwd \n")
         else:
           jFile.write('cd - \n')
           ### the following makes the .sh script exit if an error is thrown after the "set -e" command
           jFile.write('set -e \n')
       else              : jFile.write('cd '+wDir+' \n')
       jFile.close()
       if usePython : pFile.close()
       os.system('chmod +x '+self.subDir+subDirExtra+'/'+jName+'.sh')

     # Create Proxy at IIHE
     if 'cern'  in hostName:
       cmd='voms-proxy-info'
       proc=subprocess.Popen(cmd, stderr = subprocess.PIPE,stdout = subprocess.PIPE, shell = True)
       out, err = proc.communicate()
       proxypath = " xxx "
       for line in out.split('\n'):
        if "path" in line:
          proxypath=line.split(':')[1]
       os.system('cp '+proxypath+' /afs/cern.ch/user/'+os.environ["USER"][:1]+'/'+os.environ["USER"]+'/.proxy\n')
     if 'iihe'  in hostName:
       #os.system('voms-proxy-init --voms cms:/cms/becms --valid 168:0')
       os.system('cp $X509_USER_PROXY /user/'+os.environ["USER"]+'/.proxy')
     if "pi.infn.it" in socket.getfqdn():  
       os.system('cp $X509_USER_PROXY /home/users/'+os.environ["USER"]+'/.proxy')
     if "knu" in hostName: 
       os.system('cp $X509_USER_PROXY /u/user/'+os.environ["USER"]+'/.proxy')
       #os.system('cp /tmp/x509up_u$UID /u/user/'+os.environ["USER"]+'/.proxy')
     if "sdfarm" in hostName: 
       os.system('cp $X509_USER_PROXY /cms/ldap_home/'+os.environ["USER"]+'/.proxy')
     if "hercules" in hostName:
       os.system('cp $X509_USER_PROXY /gwpool/users/'+os.environ["USER"]+'/.proxy')

   def Add (self,iStep,iTarget,command):
     jName= self.jobsDic[iStep][iTarget]
     if JOB_DIR_SPLIT and self.JOB_DIR_SPLIT_READY :
       subDirExtra = '/' + jName.split('__')[3] 
     else:
       subDirExtra =''
     #print 'Adding to ',self.subDir+'/'+jName  
     jFile = open(self.subDir+subDirExtra+'/'+jName+'.sh','a') 
     jFile.write(command+'\n')
     jFile.close()

   def Add2All (self,command):
     for jName in self.jobsList:
       if JOB_DIR_SPLIT and self.JOB_DIR_SPLIT_READY :
         subDirExtra = '/' + jName.split('__')[3] 
       else:
         subDirExtra =''
       jFile = open(self.subDir+subDirExtra+'/'+jName+'.sh','a')
       jFile.write(command+'\n')
       jFile.close()

   def InitPy (self,command):

     #os.system('cd '+self.subDir)
     for jName in self.jobsList:
       if JOB_DIR_SPLIT and self.JOB_DIR_SPLIT_READY :
         subDirExtra = '/' + jName.split('__')[3]
       else:
         subDirExtra =''
       pFile = open(self.subDir+subDirExtra+'/'+jName+'.py','a')
       pFile.write(command+'\n')
       pFile.close()

   def AddPy2Sh(self):
     for jName in self.jobsList: 
       if JOB_DIR_SPLIT and self.JOB_DIR_SPLIT_READY :
         subDirExtra = '/' + jName.split('__')[3]
       else:
         subDirExtra =''
       jFile = open(self.subDir+subDirExtra+'/'+jName+'.sh','a')
       command = 'python '+self.subDir+subDirExtra+'/'+jName+'.py'
       jFile.write(command+'\n')
       jFile.close()

   def AddPy (self,iStep,iTarget,command):
     jName= self.jobsDic[iStep][iTarget]
     if JOB_DIR_SPLIT and self.JOB_DIR_SPLIT_READY :
       subDirExtra = '/' + jName.split('__')[3]
     else:
       subDirExtra =''
     print 'Adding to ',self.subDir+subDirExtra+'/'+jName
     pFile = open(self.subDir+subDirExtra+'/'+jName+'.py','a')
     pFile.write(command+'\n')
     pFile.close()

   def GetPyName (self,iStep,iTarget) :
     jName= self.jobsDic[iStep][iTarget]
     if JOB_DIR_SPLIT and self.JOB_DIR_SPLIT_READY :
       subDirExtra = '/' + jName.split('__')[3]
     else:
       subDirExtra =''
     return self.subDir+subDirExtra+'/'+jName+'.py' 

   def Sub(self,queue='longlunch',IiheWallTime='168:00:00',optTodo=False): 
     # Submit host name to identify the environment
     hostName = os.uname()[1]

     scheduler = ''

     if 'cern' in hostName and not CERN_USE_LSF:
       flavours = ['espresso', 'microcentury', 'longlunch', 'workday', 'tomorrow', 'testmatch', 'nextweek']
       runtimes = [20, 60, 120, 60 * 8, 60 * 24, 60 * 24 * 3, 60 * 24 * 7]
       if queue not in flavours:
         print 'Queue', queue, 'is not defined for CERN HTCondor.'
         print 'Allowed values:', flavours
         raise RuntimeError('Undefined queue')

       MaxRunTime = (runtimes[flavours.index(queue)] - 1) * 60

       scheduler = 'condor'
     


     for jName in self.jobsList:
       if JOB_DIR_SPLIT and self.JOB_DIR_SPLIT_READY :
         subDirExtra = '/' + jName.split('__')[3]
       else:
         subDirExtra =''
       os.system('cd '+self.subDir+subDirExtra)
       print self.subDir+subDirExtra+'/'+jName
       jobFile=self.subDir+subDirExtra+'/'+jName+'.sh' 
       errFile=self.subDir+subDirExtra+'/'+jName+'.err'
       outFile=self.subDir+subDirExtra+'/'+jName+'.out'
       jidFile=self.subDir+subDirExtra+'/'+jName+'.jid'
       jFile = open(self.subDir+subDirExtra+'/'+jName+'.sh','a')
       jFile.write('[ $? -eq 0 ] && mv '+jidFile+' '+jidFile.replace('.jid','.done') )
       jFile.close()
       jidFile=self.subDir+subDirExtra+'/'+jName+'.jid'
       print 'Submit',jName, ' on ', queue

       if 'cern' in hostName:
         if CERN_USE_LSF:
           jobid=os.system('bsub -q '+queue+' -o '+outFile+' -e '+errFile+' '+jobFile+' > '+jidFile)
         else:
           jdsFileName=self.subDir+subDirExtra+'/'+jName+'.jds'
           jdsFile = open(jdsFileName,'w')
           jdsFile.write('executable = '+self.subDir+subDirExtra+'/'+jName+'.sh\n')
           jdsFile.write('universe = vanilla\n')
           #jdsFile.write('use_x509userproxy = true\n')
           jdsFile.write('output = '+self.subDir+subDirExtra+'/'+jName+'.out\n')
           jdsFile.write('error = '+self.subDir+subDirExtra+'/'+jName+'.err\n')
           jdsFile.write('log = '+self.subDir+subDirExtra+'/'+jName+'.log\n')
           if CONDOR_ACCOUNTING_GROUP:
             jdsFile.write('+AccountingGroup = '+CONDOR_ACCOUNTING_GROUP+'\n')
             jdsFile.write('accounting_group = '+CONDOR_ACCOUNTING_GROUP+'\n')
           jdsFile.write('request_cpus = '+str(self.nThreads)+'\n')
           jdsFile.write('+JobFlavour = "'+queue+'"\n')
           jdsFile.write('queue\n')
           jdsFile.close()
           # We write the JDS file for documentation / resubmission, but initial submission will be done in one go below
           # jobid=os.system('condor_submit '+jdsFileName+' > ' +jidFile)
       elif 'iihe' in hostName: 
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
           todoFile = open(self.subDir+subDirExtra+'/'+jName+'.todo','w')
           todoFile.write('qsub '+QSOPT+' -N '+jName+' -q '+queue+' -o '+outFile+' -e '+errFile+' '+jobFile+' > '+jidFile)
           todoFile.close()

       elif 'knu' in hostName:
         #print 'cd '+self.subDir+'/'+jName.split('/')[0]+'; bsub -q '+queue+' -o '+outFile+' -e '+errFile+' '+jName.split('/')[1]+'.sh | grep submitted' 
         #print 'qsub -q '+queue+' -o '+outFile+' -e '+errFile+' '+jobFile+' > '+jidFile
         jobid=os.system('qsub -q '+queue+' -o '+outFile+' -e '+errFile+' '+jobFile+' > '+jidFile)
         #print 'bsub -q '+queue+' -o '+outFile+' -e '+errFile+' '+jobFile+' > '+jidFile
       elif 'hercules' in hostName:
         # mib farm
         if queue not in ['shortcms', 'longcms']:
           queue = 'shortcms'
         print " hercules::queue = ", queue
         print " hercules::outFile = ", outFile
         print " hercules::errFile = ", errFile
         print " hercules::jobFile = ", jobFile
         print " hercules::jidFile = ", jidFile
         # queues: "shortcms" (2 days) and "longcms"
         #jobid=os.system('qsub -q '+queue+' -o '+outFile+' -e '+errFile+' '+jobFile+' > '+jidFile)
         print 'qsub  -o '+outFile+' -e '+errFile+' '+jobFile+' -q ' + queue+ ' > '+jidFile
         jobid=os.system('qsub  -o '+outFile+' -e '+errFile+' '+jobFile+' -q ' +queue +' > '+jidFile)
       elif 'sdfarm' in hostName:
         jdsFileName=self.subDir+subDirExtra+'/'+jName+'.jds'
         jdsFile = open(jdsFileName,'w')
         #jdsFile = open(self.subDir+'/'+jName+'.jds','w')
         jdsFile.write('executable = '+self.subDir+subDirExtra+'/'+jName+'.sh\n')
         jdsFile.write('universe = vanilla\n')
         jdsFile.write('output = '+self.subDir+subDirExtra+'/'+jName+'.out\n')
         jdsFile.write('error = '+self.subDir+subDirExtra+'/'+jName+'.err\n')
         jdsFile.write('log = '+self.subDir+subDirExtra+'/'+jName+'.log\n')
         jdsFile.write('request_cpus = '+str(self.nThreads)+'\n')
         jdsFile.write('accounting_group=group_cms\n')
         
         if 'ui10' in hostName:
            jdsFile.write('requirements = ( HasSingularity == true ) \n')
            jdsFile.write('+SingularityImage = "/cvmfs/singularity.opensciencegrid.org/opensciencegrid/osgvo-el6:latest" \n')
            jdsFile.write('+SingularityBind = "/cvmfs, /cms, /share" \n')
            

         #jdsFile.write('should_transfer_files = YES\n')
         #jdsFile.write('when_to_transfer_output = ON_EXIT\n')
         #jdsFile.write('transfer_input_files = '+jName+'.sh\n')
         jdsFile.write('queue\n')
         jdsFile.close()
     
         #print "jdsFile: ", jdsFileName,"jidFile: ", jidFile 
         # We write the JDS file for documentation / resubmission, but initial submission will be done in one go below
         jobid=os.system('condor_submit '+jdsFileName+' > ' +jidFile)
       elif 'ifca' in hostName :
         jobid=os.system('qsub -P l.gaes -S /bin/bash -cwd -N Latino -o '+outFile+' -e '+errFile+' '+jobFile+' -j y > '+jidFile)
       elif "pi.infn.it" in socket.getfqdn():
         queue="cms"
         jobid=os.system('bsub -q '+queue+' -o '+outFile+' -e '+errFile+' '+jobFile+' > '+jidFile)
       else:
         #print 'cd '+self.subDir+'/'+jName.split('/')[0]+'; bsub -q '+queue+' -o '+outFile+' -e '+errFile+' '+jName.split('/')[1]+'.sh | grep submitted' 
         jobid=os.system('bsub -q '+queue+' -o '+outFile+' -e '+errFile+' '+jobFile+' > '+jidFile)
                 #print 'bsub -q '+queue+' -o '+outFile+' -e '+errFile+' '+jobFile+' > '+jidFile

     # If using condor, we can submit all jobs at once and save time
     if scheduler == 'condor' :
#      jds = 'executable = '+self.subDir+'/$(JName).sh\n'
#      jds += 'universe = vanilla\n'
#      jds += 'output = '+self.subDir+'/$(JName).out\n'
#      jds += 'error = '+self.subDir+'/$(JName).err\n'
#      jds += 'log = '+self.subDir+'/$(JName).log\n'

       jds = 'executable = $(JName).sh\n'
       jds += 'universe = vanilla\n'
       jds += 'output = $(JName).out\n'
       jds += 'error = $(JName).err\n'
       jds += 'log = $(JName).log\n'
       #jds += 'use_x509userproxy = true\n'
       jds += 'request_cpus = '+str(self.nThreads)+'\n'
       if CONDOR_ACCOUNTING_GROUP:
         jds += '+AccountingGroup = '+CONDOR_ACCOUNTING_GROUP+'\n'
         jds += 'accounting_group = '+CONDOR_ACCOUNTING_GROUP+'\n'
       jds += '+JobFlavour = "'+queue+'"\n'
       jds += 'queue JName in (\n'
       for jName in self.jobsList:
         if JOB_DIR_SPLIT and self.JOB_DIR_SPLIT_READY :
           subDirExtra = '/' + jName.split('__')[3] 
         else:
           subDirExtra = '' 
         jds += self.subDir+subDirExtra+'/'+jName + '\n'
       jds += ')\n'

       proc = subprocess.Popen(['condor_submit'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
       out, err = proc.communicate(jds)
       if proc.returncode != 0:
         sys.stderr.write(err)
         raise RuntimeError('Job submission failed.')

       print out.strip()

       matches = re.match('.*submitted to cluster ([0-9]*)\.', out.split('\n')[-2])
       if not matches:
         sys.stderr.write('Failed to retrieve the job id. Job submission may have failed.\n')
         for jName in self.jobsList:
           jidFile=self.subDir+subDirExtra+'/'+jName+'.jid'
           open(jidFile, 'w').close()
       else:
         clusterId = matches.group(1)
         # now write the jid files
         proc = subprocess.Popen(['condor_q', clusterId, '-l', '-attr', 'ProcId,Cmd', '-json'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
         out, err = proc.communicate()
         try:
           qlist = json.loads(out.strip())
         except:
           sys.stderr.write('Failed to retrieve job info. Job submission may have failed.\n')
           for jName in self.jobsList:
              jidFile=self.subDir+subDirExtra+'/'+jName+'.jid'
              open(jidFile, 'w').close()
         else:
           for qdict in qlist:
             with open(qdict['Cmd'].replace('.sh', '.jid'), 'w') as out:
               out.write('%s.%d\n' % (clusterId, qdict['ProcId']))

   def AddCopy (self,iStep,iTarget,inputFile,outputFile):
     "Copy file from local to remote server (outputFile = /store/...)"

     # Submit host name to identify the environment
     hostName = os.uname()[1]
     
     jName= self.jobsDic[iStep][iTarget]
     if JOB_DIR_SPLIT and self.JOB_DIR_SPLIT_READY :
         subDirExtra = '/' + jName.split('__')[3]
     else:
         subDirExtra =''
     #print 'Adding to ',self.subDir+'/'+jName  
     jFile = open(self.subDir+subDirExtra+'/'+jName+'.sh','a') 
     if 'iihe' in hostName :
        jFile.write('lcg-cp '+inputFile+' srm://maite.iihe.ac.be:8443/pnfs/iihe/cms'+outputFile+'\n')
     elif 'ifca' in hostName :
        jFile.write('mv '+inputFile+' /gpfs/gaes/cms'+outputFile+'\n')
     elif "pi.infn.it" in socket.getfqdn():   
        jFile.write('lcg-cp '+inputFile+' srm://stormfe1.pi.infn.it:8444/srm/managerv2?SFN=/cms'+outputFile+'\n')
     elif 'knu' in hostName :
        jFile.write('gfal-copy '+inputFile+' srm://cluster142.knu.ac.kr:8443/srm/managerv2?SFN=/pnfs/knu.ac.kr/data/cms/'+outputFile+'\n')
     elif 'sdfarm' in hostName :
        jFile.write('gfal-copy -p '+inputFile+' srm://cms-se.sdfarm.kr:8443/srm/v2/server?SFN=/xrootd/'+outputFile+'\n')
     elif 'hercules' in hostName :
        jFile.write('gfal-copy -p file://`pwd`/' + inputFile + ' srm://storm.mib.infn.it:8444/cms/' + outputFile+ '\n')
     else :
        jFile.write('cp '+inputFile+ " " + outputFile+'\n')
     jFile.close()

def batchStatus():
    fileCmd = 'ls '+jobDir
    proc=subprocess.Popen(fileCmd, stderr = subprocess.PIPE,stdout = subprocess.PIPE, shell = True)
    out, err = proc.communicate()

    # Submit host name to identify the environment
    hostName = os.uname()[1]

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
          #print iCrab
          if 'CRABTask' in iCrab : Crab[iStep]+=1 
          else:
            if 'iihe' in hostName :
              iStat = os.popen('cat '+jidFile+' | awk -F\'.\' \'{print $1}\' | xargs -n 1 qstat | grep localgrid | awk \'{print $5}\' ').read()
              if 'Q' in iStat : Pend[iStep]+=1
              else: Runn[iStep]+=1
            elif 'ifca' in os.uname()[1] :	
              iStat = os.popen('qstat | grep \" qw \" |  awk \'{print $1 \" '+jidFile+'\"}\' | xargs -n 2 grep | awk \'{ print $2 }\' ').read()
	      if 'job' in iStat : Pend[iStep]+=1
              else: Runn[iStep]+=1
            elif 'cern' in hostName and not CERN_USE_LSF:
              iStat = os.popen(r'cat '+jidFile+" | xargs -n 1 condor_q | tail -n1").read()
              if '1 idle' in iStat: Pend[iStep]+=1
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

def batchResub(Dir='ALL',queue='longlunch',requestCpus=1,IiheWallTime='168:00:00',optTodo=True):
    # jobDir imported from userConfig

    if Dir == 'ALL' :
      fileCmd = 'ls '+jobDir
      proc=subprocess.Popen(fileCmd, stderr = subprocess.PIPE,stdout = subprocess.PIPE, shell = True)
      out, err = proc.communicate()
      DirList=string.split(out)
    else:
      DirList=[Dir]

    # Submit host name to identify the environment
    hostName = os.uname()[1]
    scheduler = ''

    if 'cern' in hostName and not CERN_USE_LSF:
      flavours = ['espresso', 'microcentury', 'longlunch', 'workday', 'tomorrow', 'testmatch', 'nextweek']
      runtimes = [20, 60, 120, 60 * 8, 60 * 24, 60 * 24 * 3, 60 * 24 * 7]
      if queue not in flavours:
        print 'Queue', queue, 'is not defined for CERN HTCondor.'
        print 'Allowed values:', flavours
        raise RuntimeError('Undefined queue')

      MaxRunTime = (runtimes[flavours.index(queue)] - 1) * 60

      scheduler = 'condor'
    

    for iDir in DirList:
      subDir = jobDir+'/'+iDir

      # This is for big crunch of jobs that were planned ahead
      fileCmd = 'ls '+subDir+'/'+'*.todo'
      proc=subprocess.Popen(fileCmd, stderr = subprocess.PIPE,stdout = subprocess.PIPE, shell = True)
      out, err = proc.communicate()
      FileList=string.split(out)
      for iFile in FileList:
        jidFile=iFile.replace('.todo','.jid')
        if 'iihe' in os.uname()[1]:
          jobid=os.system('bash '+iFile)
          print 'Submitting ' , iFile
          if jobid == 0 : os.system('rm '+iFile)
          else          : os.system('rm '+jidFile)

      # Do some search fo missing jobs ?
      fileCmd = 'ls '+subDir+'/'+'*.sh'
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
      jobsList = []

      fileCmd = 'ls '+subDir+'/'+'*.redo'
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

        jobsList.append(jName)

        if os.path.isfile(jidFile) : 
          os.system('echo rm '+jidFile)

        if 'cern' in hostName and not CERN_USE_LSF:
          jdsFileName=subDir+'/'+jName+'.jds'
          jdsFile = open(subDir+'/'+jName+'.jds','w')
          jdsFile.write('executable = '+subDir+'/'+jName+'.sh\n')
          jdsFile.write('universe = vanilla\n')
          jdsFile.write('output = '+subDir+'/'+jName+'.out\n')
          jdsFile.write('error = '+subDir+'/'+jName+'.err\n')
          jdsFile.write('log = '+subDir+'/'+jName+'.log\n')
          jdsFile.write('request_cpus = '+str(requestCpus)+'\n')
          if CONDOR_ACCOUNTING_GROUP:
            jdsFile.write('+AccountingGroup = '+CONDOR_ACCOUNTING_GROUP+'\n')
            jdsFile.write('accounting_group = '+CONDOR_ACCOUNTING_GROUP+'\n')
          jdsFile.write('+JobFlavour = "'+queue+'"\n')
          jdsFile.write('queue\n')
          jdsFile.close()
          # We write the JDS file for documentation / resubmission, but initial submission will be done in one go below
          #jobid=os.system('condor_submit '+jdsFileName+' > ' +jidFile)
          if jobid == 0 : os.system('rm '+iFile)   
          else: os.system('rm '+jidFile)
        elif 'iihe' in hostName :
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
            todoFile = open(subDir+'/'+jName+'.todo','w')
            todoFile.write('qsub '+QSOPT+' -N '+jName+' -q '+queue+' -o '+outFile+' -e '+errFile+' '+jobFile+' > '+jidFile)
            todoFile.close()
        elif 'knu' in hostName:
          jobid=os.system('qsub -q '+queue+' -o '+outFile+' -e '+errFile+' '+jobFile+' > '+jidFile)
          if jobid == 0 : os.system('rm '+iFile)   
          else: os.system('rm '+jidFile)
        elif 'hercules' in hostName:
          # mib farm
          if queue not in ['shortcms', 'longcms']:
            queue = 'shortcms'
          jobid=os.system('qsub -q '+queue+' -o '+outFile+' -e '+errFile+' '+jobFile+' -q ' + queue +' > '+jidFile)
          if jobid == 0 : os.system('rm '+iFile)   
          else: os.system('rm '+jidFile)
        elif 'sdfarm' in hostName:
          jdsFileName=subDir+'/'+jName+'.jds'
          jdsFile = open(subDir+'/'+jName+'.jds','w')
          jdsFile.write('executable = '+subDir+'/'+jName+'.sh\n')
          jdsFile.write('universe = vanilla\n')
          jdsFile.write('output = '+subDir+'/'+jName+'.out\n')
          jdsFile.write('error = '+subDir+'/'+jName+'.err\n')
          jdsFile.write('log = '+subDir+'/'+jName+'.log\n')
          jdsFile.write('request_cpus = '+str(requestCpus)+'\n')
          #jdsFile.write('should_transfer_files = YES\n')
          #jdsFile.write('when_to_transfer_output = ON_EXIT\n')
          #jdsFile.write('transfer_input_files = '+jName+'.sh\n')
          jdsFile.write('queue\n')
          jdsFile.close()
          # We write the JDS file for documentation / resubmission, but initial submission will be done in one go below
          #jobid=os.system('condor_submit '+jdsFileName+' > ' +jidFile)
          if jobid == 0 : os.system('rm '+iFile)   
          else: os.system('rm '+jidFile)
        elif 'ifca' in hostName:
          jobid=os.system('qsub -P l.gaes -S /bin/bash -cwd -N Latino -o '+outFile+' -e '+errFile+' '+jobFile+' -j y > '+jidFile)
          if jobid == 0 : os.system('rm '+iFile)   
          else: os.system('rm '+jidFile)
        elif "pi.infn.it" in socket.getfqdn():
          queue="cms"
          jobid=os.system('bsub -q '+queue+' -o '+outFile+' -e '+errFile+' '+jobFile+' > '+jidFile)
          if jobid == 0 : os.system('rm '+iFile)   
          else: os.system('rm '+jidFile)
        else:
          #print 'cd '+subDir+'/'+jName.split('/')[0]+'; bsub -q '+queue+' -o '+outFile+' -e '+errFile+' '+jName.split('/')[1]+'.sh | grep submitted' 
          jobid=os.system('bsub -q '+queue+' -o '+outFile+' -e '+errFile+' '+jobFile+' > '+jidFile)
          if jobid == 0 : os.system('rm '+iFile)   
          else: os.system('rm '+jidFile)
                  #print 'bsub -q '+queue+' -o '+outFile+' -e '+errFile+' '+jobFile+' > '+jidFile

      # If using condor, we can submit all jobs at once and save time
      if scheduler == 'condor':
        jds = 'executable = '+subDir+'/$(JName).sh\n'
        jds += 'universe = vanilla\n'
        jds += 'output = '+subDir+'/$(JName).out\n'
        jds += 'error = '+subDir+'/$(JName).err\n'
        jds += 'log = '+subDir+'/$(JName).log\n'
        jds += 'request_cpus = '+str(requestCpus)+'\n'
        jds += '+JobFlavour = "'+queue+'"\n'
        if CONDOR_ACCOUNTING_GROUP:
          jds += '+AccountingGroup = '+CONDOR_ACCOUNTING_GROUP+'\n'
          jds += 'accounting_group = '+CONDOR_ACCOUNTING_GROUP+'\n'
        jds += 'queue JName in (\n'
        for jName in jobsList:
          jds += jName + '\n'
        jds += ')\n'
        proc = subprocess.Popen(['condor_submit'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
        out, err = proc.communicate(jds)
        if proc.returncode != 0:
          sys.stderr.write(err)
          raise RuntimeError('Job submission failed.')
        print out.strip()

        matches = re.match('.*submitted to cluster ([0-9]*)\.', out.split('\n')[-2])
        if not matches:
          sys.stderr.write('Failed to retrieve the job id. Job submission may have failed.\n')
          for jName in jobsList:
            jidFile=subDir+'/'+jName+'.jid'
            open(jidFile, 'w').close()
        else:
          clusterId = matches.group(1)
          # now write the jid files
          proc = subprocess.Popen(['condor_q', clusterId, '-l', '-attr', 'ProcId,Cmd', '-json'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
          out, err = proc.communicate()
          try:
            qlist = json.loads(out.strip())
          except:
            sys.stderr.write('Failed to retrieve job info. Job submission may have failed.\n')
            for jName in jobsList:
               jidFile=subDir+'/'+jName+'.jid'
               open(jidFile, 'w').close()
          else:
            for qdict in qlist:
              with open(qdict['Cmd'].replace('.sh', '.jid'), 'w') as out:
                out.write('%s.%d\n' % (clusterId, qdict['ProcId']))


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
