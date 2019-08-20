#!/usr/bin/env python
import sys, re, os, os.path, math, copy
import string
import subprocess
import numpy

# configuration auto-loaded where the job directory and the working directory is defined
from LatinoAnalysis.Tools.userConfig  import *

# functions used in everyday life ...
from LatinoAnalysis.Tools.commonTools import *
from LatinoAnalysis.Tools.batchTools  import *
from LatinoAnalysis.Tools.crabTools  import *

try:
  # CERN-specific LSF<->HTCondor switch
  # This is temporary - CERN will soon become 100% condor
  CERN_USE_LSF = (batchType == 'lsf')
except NameError:
  # if batchType is not set, default to condor
  CERN_USE_LSF = False

class PostProcMaker():

# ------------- Configuration

   def __init__(self) : 

     self._cmsswBasedir = os.environ["CMSSW_BASE"] 

     #self._aaaXrootd = 'root://cms-xrd-global.cern.ch//'
     self._aaaXrootd = 'root://xrootd-cms.infn.it//'
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

     # BaseW
     self._baseW       = {}

     # We need a Proxy !
     self.checkProxy()



#---- Load x-section DB
   def loadXSDB(self,iProd):

    # Among 'gDoc','Python','YellowR' and order Matter (Overwriting for same samples !)
    xsMethods=['Python','YellowR']
    xsFile=self._cmsswBasedir+'/src/'+self._Productions[iProd]['xsFile']
    self._xsDB = xsectionDB()
    for iMethod in xsMethods :

      #OLD if iMethod == 'gDoc'    : self._xsDB.readGDoc(Productions[iProd]['gDocID'])
      if iMethod == 'Python'  : self._xsDB.readPython(xsFile)
      #if iMethod == 'YellowR' : self._xsDB.readYR('YR4','13TeV')
      if iMethod == 'YellowR' : self._xsDB.readYR(self._Productions[iProd]['YRver'][0],self._Productions[iProd]['YRver'][1])

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

     if self._LocalSite == 'cern' and not CERN_USE_LSF:
       self._Sites[self._LocalSite]['batchQueues'] = ['tomorrow', 'espresso', 'microcentury', 'longlunch', 'workday', 'testmatch', 'nextweek']

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
       print '_batchQueue set to = ',self._batchQueue

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
     if len(FileList) == 0 : return FileDic

     # fileCmd .... Directory
     fileCmd = self._Sites[self._LocalSite]['lsCmd']+' '+self._targetDir
     # fileCmd .... Files
     if self._iniStep == 'Prod' :
       if len(FileList) == 1 : fileCmd += self._treeFilePrefix+iSample+'__part0.root'
       else                  : fileCmd += self._treeFilePrefix+iSample+'__part*.root'
     else:
       if not '__part' in FileList[0] : fileCmd += self._treeFilePrefix+iSample+'.root'
       else                           : fileCmd += self._treeFilePrefix+iSample+'__part*.root'

     # fileCmd .... Exec
     proc=subprocess.Popen(fileCmd, stderr = subprocess.PIPE,stdout = subprocess.PIPE, shell = True)
     out, err = proc.communicate()
     FileExistList=string.split(out)
     # Now Check 
     toSkip=[]
     if not self._redo : 
       if  len(FileExistList) == len(FileList) : return FileDic
       for iFile in FileExistList: 
         if not '__part' in iFile : toSkip.append('0')
         else                     : toSkip.append(iFile.replace('.root','').split('__part')[1])

     if not self._iniStep == 'Prod' :
       for iFile in FileList : 
         if not '__part' in iFile : iPart = 0
         else                     : iPart = iFile.replace('.root','').split('__part')[1]
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
           if 'srmPrefix' in self._Samples[iSample]:
             FileDic = self.getTargetFileDic(iProd,iStep,iSample,self.getFilesFromPath(self._Samples[iSample]['paths'],self._Samples[iSample]['srmPrefix']))
           else:  
             if 'dasInst' in self._Samples[iSample] : dasInst = self._Samples[iSample]['dasInst']
             else:                                    dasInst = 'prod/global' 
             FileDic = self.getTargetFileDic(iProd,iStep,iSample,self.getFilesFromDAS(self._Samples[iSample]['nanoAOD'],dasInst))
         # From previous PostProc step
         else :
           FileDic = self.getTargetFileDic(iProd,iStep,iSample,getSampleFiles(self._sourceDir,iSample,True,self._treeFilePrefix,True))
         if len(FileDic) > 0 : self._targetDic[iSample] = FileDic

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

   def getFilesFromPath(self,paths,srmprefix):
     if 'el7' in os.uname()[2]:
       try:
         # gfal-ls from command line (i.e. subprocess) doesn't work in CC7
         # fortunatley the python binding does, but it's not included in the CMSSW python libraries
         import gfal2
         useGfal2Py = True
       except ImportError:
         if '/usr/lib64/python2.7/site-packages' not in sys.path:
           sys.path.append('/usr/lib64/python2.7/site-packages')
         try:
           import gfal2
         except ImportError:
           useGfal2Py = False
         else:
           useGfal2Py = True
     else:
       useGfal2Py = False

     if 'X509_CERT_DIR' not in os.environ and os.path.isdir('/etc/grid-security/certificates'):
       os.environ['X509_CERT_DIR'] = '/etc/grid-security/certificates'

     FileList = []
     for path in paths:
       if useGfal2Py:
         ctx = gfal2.creat_context()
         dircont = ctx.listdir(srmprefix + path)
         files = [f for f in dircont if f.endswith('.root')]
       else:
         command = 'gfal-ls '+srmprefix+path+ " | grep root"
         proc=subprocess.Popen(command, stderr = subprocess.PIPE,stdout = subprocess.PIPE, shell = True)
         out, err = proc.communicate()
         if not proc.returncode == 0 :
           print out
           print err
           exit()
         files=string.split(out)

       for file in files:
         FileList.append(path+"/"+file)

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
       for iUEPS in self._Steps[iStep]['cpMap'] :
         if self._Sites[self._LocalSite]['mkDir'] : 
           os.system('mkdir -p '+ self._Sites[self._LocalSite]['treeBaseDir']+'/'+iProd+'/'+self._iniStep+'__'+iUEPS)

# --------------- Job Jandling

   def submitJobs(self,iProd,iStep):

     bpostFix=''
     if not self._iniStep == 'Prod' : bpostFix='____'+self._iniStep

     # Make job directories
     if JOB_DIR_SPLIT :
       jDir = jobDir+'/NanoGardening__'+iProd+'__'+iStep
       for iSample in self._targetDic :
         if not os.path.exists(jDir+'/'+iSample) : os.system('mkdir -p '+jDir+'/'+iSample)
     else:
       jDir = jobDir+'/NanoGardening__'+iProd
     if not os.path.exists(jDir) : os.system('mkdir -p '+jDir)
     wDir = workDir+'/NanoGardening__'+iProd
     if not os.path.exists(wDir) : os.system('mkdir -p '+wDir)

     # prepare targetList
     targetList = []
     for iSample in self._targetDic :
       for iFile in self._targetDic[iSample] :
         iTarget = os.path.basename(self._targetDic[iSample][iFile]).replace(self._treeFilePrefix,'').replace('.root','')
         if JOB_DIR_SPLIT :
           pidFile=jDir+'/'+iSample+'/NanoGardening__'+iProd+'__'+iStep+'__'+iTarget+bpostFix+'.jid'
         else:
           pidFile=jDir+'/NanoGardening__'+iProd+'__'+iStep+'__'+iTarget+bpostFix+'.jid'
         if os.path.isfile(pidFile) :
           print "pidFile", pidFile
           print '--> Job Running already : '+iTarget
         else: targetList.append(iTarget)

     # Dummy stepList for jobs
     stepList=[]
     stepList.append(iStep)

     #print self._targetDic.keys()
     #exit()

     # Check pre bash command for Steps
     preBash = self.checkPreBashStep(iStep)

     if self._jobMode == 'Interactive' :
       print "INFO: Using Interactive command"
     # batchMode Preparation
     elif self._jobMode == 'Batch':
       print "INFO: Using Local Batch"
       self._jobs = batchJobs('NanoGardening',iProd,[iStep],targetList,'Targets,Steps',bpostFix,JOB_DIR_SPLIT_READY=True)
       self._jobs.Add2All('cp '+self._cmsswBasedir+'/src/'+self._haddnano+' .')
       self._jobs.Add2All(preBash)
       self._jobs.AddPy2Sh()
       self._jobs.Add2All('ls -l')
     # CRAB3 Init
     elif self._jobMode == 'Crab':
       print "INFO: Using CRAB3"
       self._crab = crabTool('NanoGardening',iProd,[iStep],targetList,'Targets,Steps',bpostFix)
       self._crab.setStorage('T2_CH_CERN','/store/group/phys_higgs/cmshww/amassiro/HWWNanoCrab/')
       self._crab.AddInputFile(self._cmsswBasedir+'/src/'+self._haddnano) 
       #self._crab._ScriptHeader = self._cmsswBasedir+'/src/LatinoAnalysis/NanoGardener/test/PostProc_CrabScript_Header.sh'

     for iSample in self._targetDic :
       for iFile in self._targetDic[iSample] :
         iTarget = os.path.basename(self._targetDic[iSample][iFile]).replace(self._treeFilePrefix,'').replace('.root','')
         if iTarget in targetList :
           # Create python
           if JOB_DIR_SPLIT :
             pyFile=jDir+'/'+iSample+'/NanoGardening__'+iProd+'__'+iStep+'__'+iTarget+bpostFix+'.py'
           else:
             pyFile=jDir+'/NanoGardening__'+iProd+'__'+iStep+'__'+iTarget+bpostFix+'.py'
           if os.path.isfile(pyFile) : os.system('rm '+pyFile)
           outFile=self._treeFilePrefix+iTarget+'__'+iStep+'.root'
           jsonFilter = self._Productions[iProd]['jsonFile'] if 'jsonFile' in self._Productions[iProd].keys() else None 
           self.mkPyCfg(iProd,iSample,[self.getStageIn(iFile)],iStep,pyFile,outFile,self._Productions[iProd]['isData'], jsonFilter)
           # Stage Out command + cleaning
           stageOutCmd  = self.mkStageOut(outFile,self._targetDic[iSample][iFile])
           rmGarbageCmd = 'rm '+outFile+' ; rm '+ os.path.basename(iFile).replace('.root','_Skim.root') 
           # Interactive 
           if   self._jobMode == 'Interactive' : 
             command = 'cd '+wDir+' ; cp '+self._cmsswBasedir+'/src/'+self._haddnano+' . ; '+preBash+' python '+pyFile \
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
             # TMP FIX to garbage command because of not working PhysicsTools.NanoAODTools.postprocessing.framework.postprocessor import 
             #rmGarbageCmd = 'rm '+outFile#+' ; rm '+ os.path.basename(iFile).replace('.root','_Skim.root') 
             #self._crab.setUnpackCommands(iStep,iTarget,[outFile],[stageOutCmd],[rmGarbageCmd])
             self._crab.setUnpackCommands(iStep,iTarget,[outFile],[stageOutCmd])
     
     if   self._jobMode == 'Batch' and not self._pretend : self._jobs.Sub(self._batchQueue)
     elif self._jobMode == 'Crab': 
        self._crab.mkCrabCfg()
        if not self._pretend : self._crab.Sub()
        else                 : self._crab.Print()
        

   def getStageIn(self,File):
      # CRAB
      if     self._jobMode == 'Crab'    \
         and not self._aaaXrootd in File : 
         return self._aaaXrootd+'/store/'+File.split('/store/')[1]

      # IIHE
      if     self._LocalSite == 'iihe'                               \
         and not self._Sites[self._LocalSite]['xrootdPath']  in File \
         and     self._Sites[self._LocalSite]['treeBaseDir'] in File :
        return self._Sites[self._LocalSite]['xrootdPath']+File
      elif self._LocalSite == 'sdfarm' :
	return File.replace('/xrootd', self._Sites[self._LocalSite]['xrootdPath']+'//xrd')
      else:  
        return File

   def mkStageOut(self,prodFile,storeFile,cpMode=False):
      command=''
      # IIHE
      if   self._LocalSite == 'iihe' :
        if self._redo : 
          command += 'srmrm '+self._Sites[self._LocalSite]['srmPrefix']+storeFile+' ; '
        if not cpMode:
          command += 'lcg-cp '+prodFile+' '+self._Sites[self._LocalSite]['srmPrefix']+storeFile
        else:
          command += 'lcg-cp '+self._Sites[self._LocalSite]['srmPrefix']+prodFile+' '+self._Sites[self._LocalSite]['srmPrefix']+storeFile
      # CERN
      elif self._LocalSite == 'cern' :
        if not cpMode:
          command = 'xrdcp -f '+prodFile+' '+self._Sites[self._LocalSite]['xrootdPath']+storeFile
        else: 
          command = 'xrdcp -f '+self._Sites[self._LocalSite]['xrootdPath']+prodFile+' '+self._Sites[self._LocalSite]['xrootdPath']+storeFile     
      # IFCA
      elif self._LocalSite == 'ifca' : 
         if self._TargetSite == 'ifca' or self._TargetSite == None :
            if self._redo : 
               command += 'rm '+storeFile+' ; ' 
            if not cpMode:
               command += 'cp '+prodFile+' '+storeFile
            else:
               print 'ERROR: mkStageOut for cpMode not yet implemented for _LocalSite = ',self._LocalSite
               exit()
         else :
            print 'ERROR: mkStageOut to different site not yet implemented for _LocalSite = ',self._LocalSite
            exit()
      #KISTI T3
      elif self._LocalSite == 'sdfarm' :
	storeFile = storeFile.replace('xrootd', 'xrd')
        if not cpMode:
          command = 'xrdcp -f '+prodFile+' '+self._Sites[self._LocalSite]['xrootdPath']+storeFile
        else:
          command = 'xrdcp -f '+self._Sites[self._LocalSite]['xrootdPath']+prodFile+' '+self._Sites[self._LocalSite]['xrootdPath']+storeFile
            
      # MISSING STAGE OUT
      else :
        print 'ERROR: mkStageOut not available for _LocalSite = ',self._LocalSite
        exit()  

      return command

   def mkPyCfg(self,iProd,iSample,inputRootFiles,iStep,fPyName,haddFileName=None,isData=False, jsonFile=None):


     fPy = open(fPyName,'a') 
     
     # Common Header
     fPy.write('#!/usr/bin/env python \n')
     fPy.write('import os, sys \n')
     fPy.write('import subprocess\n')
     fPy.write('import ROOT \n')
     fPy.write('ROOT.PyConfig.IgnoreCommandLineOptions = True \n')
     fPy.write(' \n')
     fPy.write('from PhysicsTools.NanoAODTools.postprocessing.framework.postprocessor import PostProcessor \n')
     fPy.write('from LatinoAnalysis.NanoGardener.modules.Dummy import *\n')
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
           #fPy.write(self._Steps[iSubStep]['declare']+'\n')
           fPy.write(self.customizeDeclare(iSubStep)+'\n')
     else:
       if 'declare' in self._Steps[iStep] :
         #fPy.write(self._Steps[iStep]['declare']+'\n') 
         fPy.write(self.customizeDeclare(iStep)+'\n')
     fPy.write(' \n')

     if self._iniStep == 'Prod':
       for iFile in inputRootFiles:
         fPy.write('subprocess.Popen(["xrdcp", "'+iFile+'", "."]).communicate()\n')

     # Files
     fPy.write('files=[')
     if self._iniStep == 'Prod':
       for iFile in inputRootFiles : fPy.write('"./'+os.path.basename(iFile)+'",')
     else:
       for iFile in inputRootFiles : fPy.write('"'+iFile+'",')
     fPy.write(']\n') 
     fPy.write(' \n')
     
     # Configure modules
     fPy.write('p = PostProcessor(  "."   ,          \n')
     fPy.write('                    files ,          \n')
     if jsonFile != None:
       fPy.write('                    jsonInput='+jsonFile+' ,       \n')   
     if 'selection' in self._Steps[iStep] :
       fPy.write('                    cut='+self._Steps[iStep]['selection']+' ,       \n')
     else: 
       fPy.write('                    cut=None ,       \n')
     if 'branchsel' in self._Steps[iStep] :
       fPy.write('                    branchsel='+self._Steps[iStep]['branchsel']+' ,       \n')
     else:
       fPy.write('                    branchsel=None , \n')
     fPy.write('                    modules=[        \n')
     if self._Steps[iStep]['isChain'] :
       for iSubStep in  self._Steps[iStep]['subTargets'] :
         doSubStep = False
         if        isData and self._Steps[iSubStep]['do4Data'] : doSubStep = True
         elif  not isData and self._Steps[iSubStep]['do4MC']   : doSubStep = True       
         # AND onlySample 
         applyStep = self.selectSample(iProd,iSubStep,iSample)
         if doSubStep and applyStep :  fPy.write('                          '+self.customizeModule(iSample,iSubStep)+',\n')
     else:
       fPy.write('                          '+self.customizeModule(iSample,iStep)+'\n') 
     fPy.write('                            ],      \n') 
     fPy.write('                    provenance=True, \n')
     if self._jobMode == 'Crab':
       fPy.write('                    fwkJobReport=True, \n')
     else: 
       fPy.write('                    fwkJobReport=False, \n')
     if not haddFileName == None :
       fPy.write('                    haddFileName="'+haddFileName+'", \n')
     fPy.write('                 ) \n')
     fPy.write(' \n')

     # Common footer
     fPy.write('p.run() \n')
     fPy.write(' \n')

     # Close file
     fPy.close()

#------------- MODULE CUSTOMIZATION: baseW, CMSSW_Version, ....

   def computewBaseW(self,iSample,DEBUG=False):
     if   '_ext' in iSample : iSampleXS = iSample.split('_ext')[0]
     elif '-ext' in iSample : iSampleXS = iSample.split('-ext')[0]
     else:                    iSampleXS = iSample
     if not iSample in self._baseW :
       useLocal = False
       # Always check #nAOD files !
       if 'srmPrefix' in self._Samples[iSample]:
         useLocal = True
         nAODFileList = self.getFilesFromPath(self._Samples[iSample]['paths'],self._Samples[iSample]['srmPrefix'])
       else:  
         if 'dasInst' in self._Samples[iSample] : dasInst = self._Samples[iSample]['dasInst']
         else:                                    dasInst = 'prod/global'
         nAODFileList = self.getFilesFromDAS(self._Samples[iSample]['nanoAOD'],dasInst)
       # From central (or private) nanoAOD : DAS instance to be declared for ptrivate nAOD
       if self._iniStep == 'Prod' :
         if 'srmPrefix' in self._Samples[iSample]:
           useLocal = True
           FileList = self.getFilesFromPath(self._Samples[iSample]['paths'],self._Samples[iSample]['srmPrefix'])
         else:   
           if 'dasInst' in self._Samples[iSample] : dasInst = self._Samples[iSample]['dasInst']
           else:                                    dasInst = 'prod/global'
           FileList = self.getFilesFromDAS(self._Samples[iSample]['nanoAOD'],dasInst)
         # From previous PostProc step
       else :
         useLocal = True
         FileList = getSampleFiles(self._sourceDir,iSample,True,self._treeFilePrefix,True)

       # Fallback to nAOD in case of missing files (!!! will always fall back in case of hadd !!!)
       if not len(nAODFileList) == len(FileList) : 
         print ' ################## WARNING: Falling back to original nAOD for baseW : ',iSample, len(nAODFileList) , len(FileList)
#        print ' EXIT !!!!'
#        exit()
         FileList = nAODFileList
         if 'srmPrefix' in self._Samples[iSample]: useLocal = False

       # Now compute #evts
       genEventCount = 0
       genEventSumw  = 0.0
       genEventSumw2 = 0.0
       for iFile in FileList:
         if DEBUG : print iFile 
         if useLocal:
           f = ROOT.TFile.Open(iFile, "READ")
         else:
           f = ROOT.TFile.Open(self._aaaXrootd+iFile, "READ")
         Runs = f.Get("Runs")
         for iRun in Runs : 
           if DEBUG : print '---> genEventSumw = ', iRun.genEventSumw
           genEventCount += iRun.genEventCount
           genEventSumw  += iRun.genEventSumw
           genEventSumw2 += iRun.genEventSumw2
         f.Close()
       # get the X-section and baseW
       nEvt = genEventSumw
       Xsec  = self._xsDB.get(iSampleXS)
       baseW = float(Xsec)*1000./nEvt
       print 'baseW: xs,N -> W', Xsec , nEvt , baseW
       # Store Info
       self._baseW[iSample] = { 'baseW' : baseW , 'Xsec' : Xsec }

   def customizeModule(self,iSample,iStep):

     if not 'module' in self._Steps[iStep] : return 'Dummy()'
     module = self._Steps[iStep]['module']

     # baseW
     if iStep == 'baseW' :
       print "Computing baseW for",iSample  
       self.computewBaseW(iSample)
       print self._baseW[iSample]['baseW']  
       module = module.replace('RPLME_baseW'    , str(self._baseW[iSample]['baseW']))
       module = module.replace('RPLME_XSection' , str(self._baseW[iSample]['Xsec']))

     # "CMSSW" version
     if 'RPLME_CMSSW' in module :
       module = module.replace('RPLME_CMSSW',self._prodVersion)
     
     # GT for JES uncertainties
     if 'RPLME_JESGT' in module :
       module = module.replace('RPLME_JESGT',self._prodJESGT)

     # YEAR
     if 'RPLME_YEAR' in module :
       module = module.replace('RPLME_YEAR',self._prodYear)

     return module


   def customizeDeclare(self,iStep):
     declare = self._Steps[iStep]['declare']

     # "CMSSW" version
     if 'RPLME_CMSSW' in declare :
       declare = declare.replace('RPLME_CMSSW',self._prodVersion)

     # GT for JES uncertainties  
     if 'RPLME_JESGT' in declare :
       declare = declare.replace('RPLME_JESGT',self._prodJESGT)

    # YEAR
     if 'RPLME_YEAR' in declare :
       declare = declare.replace('RPLME_YEAR',self._prodYear)

     return declare


   def checkPreBashStep(self,iStep):
     preBash = ''
     if self._Steps[iStep]['isChain'] :
       for iSubStep in self._Steps[iStep]['subTargets'] :
         if 'prebash' in self._Steps[iSubStep] : 
            for iPreBash in self._Steps[iSubStep]['prebash'] : preBash += iPreBash + ' ; '
     else:
       if 'prebash' in self._Steps[iStep] :
         for iPreBash in self._Steps[iStep]['prebash'] : preBash += iPreBash + ' ; '
     return preBash 

#------------- Hadd step

   def getHaddFiles(self,iProd,iStep):

     self._HaddDic = {}

     for iSample in self._Samples :
       if self.selectSample(iProd,iStep,iSample) :
         HaddDic = {}
         # Get File List in input directory
         # ... From central (or private) nanoAOD : DAS instance to be declared for ptrivate nAOD
         if self._iniStep == 'Prod' :
           if 'srmPrefix' in self._Samples[iSample]:
             FileInList = self.getFilesFromPath(self._Samples[iSample]['paths'],self._Samples[iSample]['srmPrefix'])
           else:  
             if 'dasInst' in self._Samples[iSample] : dasInst = self._Samples[iSample]['dasInst']
             else:                                    dasInst = 'prod/global'
             FileInList = self.getFilesFromDAS(self._Samples[iSample]['nanoAOD'],dasInst)
         # ... From previous PostProc step
         else :
           FileInList = getSampleFiles(self._sourceDir,iSample,True,self._treeFilePrefix,True)

         if len(FileInList) == 0 : continue

         # Check size(FileInList) == size(Initial Step File List), i.e. do not Hadd in case previous step is not done
         # ... Only needed if from previous PostProc step
         if not self._iniStep == 'Prod' :
           #... if no hadd before -> Prod:
           if not 'hadd' in self._sourceDir :
             if 'srmPrefix' in self._Samples[iSample]:
               FileOriList = self.getFilesFromPath(self._Samples[iSample]['paths'],self._Samples[iSample]['srmPrefix'])
             else:   
               if 'dasInst' in self._Samples[iSample] : dasInst = self._Samples[iSample]['dasInst']
               else:                                    dasInst = 'prod/global'
               FileOriList = self.getFilesFromDAS(self._Samples[iSample]['nanoAOD'],dasInst) 
             if not len(FileInList) == len (FileOriList) :
               print 'WARNING: HADD not possible, missing files in _sourceDir for iSample ',iSample,' --> SKIPPING IT !!!'
               continue
           else:
             print 'ERROR: HADD CASE not implemented: hadd on top of hadd !'
             exit()

         # Now Build the HADD dictionnary according to target size
         sortDic={} 
         if '__part' in FileInList[0]:
           for iFile in FileInList :
             sortDic[int(iFile.split('__part')[1].replace('.root',''))] = iFile
         else:
           iPart=0
           for iFile in FileInList :
             sortDic[iPart] = iFile
             iPart+=1 

         iPart=0
         tSize=0
         for iKey in sortDic : 
           iFile = sortDic[iKey] 
           targetFileName = (self._targetDir+self._treeFilePrefix+iSample+'__part'+str(iPart)+'.root').replace('//','/')
           if not targetFileName in HaddDic : HaddDic[targetFileName] = [] 
           HaddDic[targetFileName].append(iFile)
           iSize = float(remoteFileSize(iFile))
           tSize+=iSize
           if tSize > self._Steps['hadd']['SizeMax']: 
             iPart+=1
             tSize=0

         # Remove '__part0' if only 1 target file
         if len(HaddDic) == 1 : 
           oldKey=''
           for iKey in HaddDic: oldKey = iKey
           newKey = iKey.replace('__part0','')
           HaddDic[newKey] = HaddDic.pop(iKey)          

         # Check if Taget files are existing
         if not self._redo :
           FileOutList=getSampleFiles(self._targetDir,iSample,True,self._treeFilePrefix,True)
           for iFile in FileOutList : 
             if iFile.replace('//','/') in HaddDic : del HaddDic[iFile.replace('//','/')]

         if len(HaddDic) > 0 : self._HaddDic[iSample] = HaddDic

   def mkHadd(self,iProd,iStep):

     bpostFix=''
     if not self._iniStep == 'Prod' : bpostFix='____'+self._iniStep

     # Make job directories
     jDir = jobDir+'/NanoGardening__'+iProd
     if not os.path.exists(jDir) : os.system('mkdir -p '+jDir)
     wDir = workDir+'/NanoGardening__'+iProd
     if not os.path.exists(wDir) : os.system('mkdir -p '+wDir)

     # prepare targetList
     targetList = []
     for iSample in self._HaddDic:
       for iFile in self._HaddDic[iSample] :
         iTarget = os.path.basename(iFile).replace(self._treeFilePrefix,'').replace('.root','')
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
     # CRAB3 Init
     elif self._jobMode == 'Crab':
       print "INFO: Using CRAB3"
       self._crab = crabTool('NanoGardening',iProd,[iStep],targetList,'Targets,Steps',bpostFix)
       self._crab.setStorage('T2_CH_CERN','/store/group/phys_higgs/cmshww/amassiro/HWWNanoCrab/')

     for iSample in self._HaddDic:
       for iFile in self._HaddDic[iSample] :
         iTarget = os.path.basename(iFile).replace(self._treeFilePrefix,'').replace('.root','')
         if iTarget in targetList :
           outFile=self._treeFilePrefix+iTarget+'__'+iStep+'.root'
           # Stage Out command + cleaning
           stageOutCmd  = self.mkStageOut(outFile,iFile)
           rmGarbageCmd = 'rm '+outFile
           # Final command
           if   self._jobMode == 'Interactive' : command  = 'cd '+wDir+' ; '+self._cmsswBasedir+'/src/'+self._haddnano+' '+outFile+' '
           else:                                 command  = '$CMSSW_BASE/src/'+self._haddnano+' '+outFile+' '     
           for sFile in self._HaddDic[iSample][iFile] : command += self.getStageIn(sFile)+' '
           command += ' ; ls -l ; '
           if not self._jobMode == 'Crab':  command += stageOutCmd+' ; '+rmGarbageCmd
           # Interactive
           if   self._jobMode == 'Interactive' :
             if not self._pretend : os.system(command)
             else                 : print command                
           # Batch
           elif self._jobMode == 'Batch' :
             self._jobs.Add(iStep,iTarget,command)
           elif self._jobMode == 'Crab':
             self._crab.AddCommand(iStep,iTarget,command)
             self._crab.AddJobOutputFile(iStep,iTarget,outFile)
             self._crab.setUnpackCommands(iStep,iTarget,[outFile],[stageOutCmd])      
               
     if   self._jobMode == 'Batch' and not self._pretend : self._jobs.Sub()
     elif self._jobMode == 'Crab':
        self._crab.mkCrabCfg()
        if not self._pretend : self._crab.Sub()
        else                 : self._crab.Print()

#------------- UEPS step

   def mkUEPS(self,iProd,iStep):

     for iSample in self._Samples :
       if self.selectSample(iProd,iStep,iSample) :
         # Get File List in input directory
         # ... From central (or private) nanoAOD : DAS instance to be declared for ptrivate nAOD
         if self._iniStep == 'Prod' :
           print 'ERROR: Can mot make UEPS Step direcectly from central (or private) nanoAOD !'
           exit() 
         # ... From previous PostProc step
         else :
           FileInList = getSampleFiles(self._sourceDir,iSample,True,self._treeFilePrefix,True)

         if len(FileInList) == 0 : continue

         for iUEPS in self._Steps[iStep]['cpMap'] :
           if iSample in self._Steps[iStep]['cpMap'][iUEPS]:
             self._targetDir = self._Sites[self._LocalSite]['treeBaseDir']+'/'+iProd+'/'+self._iniStep+'__'+iUEPS 
             for tSample in self._Steps[iStep]['cpMap'][iUEPS][iSample] :
               FileOutList = getSampleFiles(self._targetDir,tSample,True,self._treeFilePrefix,True) 
               for iFile in FileInList:
                 tFile = self._targetDir + '/' +  os.path.basename(iFile).replace(iSample,tSample)
                 if not tFile in FileOutList or self._redo : 
                   os.system(self.mkStageOut(iFile,tFile,True))

#------------- Main 

   def process(self):

     for iProd in self._prodList:
       print '----------- Running on production: '+iProd
       self._prodVersion = self._Productions[iProd]['cmssw']
       if 'JESGT' in self._Productions[iProd] : self._prodJESGT = self._Productions[iProd]['JESGT']
       if 'year'  in self._Productions[iProd] : self._prodYear  = self._Productions[iProd]['year']
       self.readSampleFile(iProd) 
       if not self._Productions[iProd]['isData'] : self.loadXSDB(iProd)

       for iStep in self._stepList:
         if    ( not self._Productions[iProd]['isData'] and self._Steps[iStep]['do4MC'] ) \
            or (     self._Productions[iProd]['isData'] and self._Steps[iStep]['do4Data'] ) :
           print '---------------- for Step : ',iStep
           self.mkFileDir(iProd,iStep)
           if   not iStep == 'hadd' and not iStep == 'UEPS' :
             self.getTargetFiles(iProd,iStep)
             self.submitJobs(iProd,iStep)
           elif iStep == 'hadd' :
             self.getHaddFiles(iProd,iStep) 
             self.mkHadd(iProd,iStep)
           elif iStep == 'UEPS' :  
             self.mkUEPS(iProd,iStep)  

       self.Reset()
       

# ------------ check baseW

   def checkBaseW(self):
     for iProd in self._prodList:
       print '----------- Running on production: '+iProd
       self.readSampleFile(iProd)
       if not self._Productions[iProd]['isData'] : self.loadXSDB(iProd)
       else: 
         print '----> This is DATA, skipping !!!!'
         exit()
       print '---------------- for Step : ',self._iniStep
       self.mkFileDir(iProd,'baseW')
       self.getTargetFiles(iProd,'baseW')         
       for iSample in self._targetDic:
         print '------------------- for Sample : ',iSample 
         self.computewBaseW(iSample)
         test = {}
         result = True
         for iFile in self._targetDic[iSample] : 
           f = ROOT.TFile.Open(iFile, "READ")
           Events = f.Get("Events")
           for iEvt in Events:
             baseW = iEvt.baseW
             if not numpy.isclose(baseW , self._baseW[iSample]['baseW']) : result = False
             break
           f.Close()
           test[iFile] = baseW
         print iSample, result
         if not result : print test
