#!/usr/bin/env python
import sys, re, os, os.path, string
import subprocess
from cookielib import CookieJar
from urllib2 import build_opener, HTTPCookieProcessor
import socket

from LatinoAnalysis.Tools.HiggsXSection  import *

def query_yes_no(question, default="yes"):
    """Ask a yes/no question via raw_input() and return their answer.

    "question" is a string that is presented to the user.
    "default" is the presumed answer if the user just hits <Enter>.
        It must be "yes" (the default), "no" or None (meaning
        an answer is required of the user).

    The "answer" return value is True for "yes" or False for "no".
    """
    valid = {"yes": True, "y": True, "ye": True,
             "no": False, "n": False}
    if default is None:
        prompt = " [y/n] "
    elif default == "yes":
        prompt = " [Y/n] "
    elif default == "no":
        prompt = " [y/N] "
    else:
        raise ValueError("invalid default answer: '%s'" % default)

    while True:
        sys.stdout.write(question + prompt)
        choice = raw_input().lower()
        if default is not None and choice == '':
            return valid[default]
        elif choice in valid:
            return valid[choice]
        else:
            sys.stdout.write("Please respond with 'yes' or 'no' (or 'y' or 'n').\n")

#---
class list_maker:
    def __init__(self, var, sep=',', type=None ):
        self._type= type
        self._var = var
        self._sep = sep

    def __call__(self,option, opt_str, value, parser):
        if not hasattr(parser.values,self._var):
               setattr(parser.values,self._var,[])

        try:
           array = value.split(self._sep)
           if self._type:
               array = [ self._type(e) for e in array ]
           setattr(parser.values, self._var, array)

        except:
           print 'Malformed option (comma separated list expected):',value

#---
class List_Filter:

    def __init__(self, List , Filter ):
       self.FilteredList = []
       if len(Filter) == 0: self.FilteredList = [X for X in List ]
       else               : self.FilteredList = [X for X in Filter if (X in List)]
      
    def get(self):
       return self.FilteredList 

#--- Get X-section from Google doc (other method may come later ...)

class xsectionDB:

    def __init__(self):

      self.xsections = {} 
      self._useYR     = False
      self._YRVersion = ''
      self._YREnergy  = ''

    def readGDoc(self,gdocKey='1wH73CYA_T4KMkl1Cw-xLTj8YG7OPqayDnP53N-lZwFQ'):

      opener = build_opener(HTTPCookieProcessor(CookieJar()))
      resp = opener.open('https://docs.google.com/spreadsheet/ccc?key='+gdocKey+'&output=csv')
      data = resp.read()
      for line in data.splitlines(): 
        info=line.split(",")
        iID=info[0].replace(' ','')
        if iID.isdigit() :
          iKey = info[1].replace(' ','')
          self.xsections[iKey] = {}
          #self.xsections[iKey]['ID']     = iID
          #self.xsections[iKey]['sample'] = info[1].replace(' ','')
          if len(info) > 4 :
            self.xsections[iKey]['xs']     = info[5].replace(' ','')
            self.xsections[iKey]['kfact']  = '1.0'
            self.xsections[iKey]['src']    = 'gDOC' 
          else: 
            self.xsections[iKey]['xs']     = ''
            self.xsections[iKey]['kfact']  = ''
            self.xsections[iKey]['src']    = ''

      #print self.xsections

    def readPython(self,xsFile):
      handle = open(xsFile)
      for iLine in handle.read().split('\n') :
        if 'samples' in iLine.split('#')[0] :
          #print iLine
          iKey=iLine.split('\'')[1].replace(' ','')
          #print iKey
          #if iKey in self.xsections : print 'Replacing ....',iKey,self.xsections[iKey]
          #else : print 'Adding ....',iKey         
          self.xsections[iKey] = {}
          vec=iLine.split('[')[2].split(']')[0]
          #print vec
          for iVec in vec.split(',') : 
            info=iVec.split('\'')[1]
            iName=info.split('=')[0]
            iVal =info.split('=')[1] 
            if iName == 'xsec'  : self.xsections[iKey]['xs']     = iVal
            if iName == 'kfact' : self.xsections[iKey]['kfact']  = iVal
            if iName == 'ref'   : self.xsections[iKey]['src']    = 'Python,ref='+iVal
      handle.close()

    def readYR(self,YRVersion,YREnergy):

      self._useYR     = True
      self._YRVersion = YRVersion
      self._YREnergy  = YREnergy
      self._HiggsXS   = HiggsXSection() 

    def get(self,iSample):
      if self._useYR :
        Higgs = self._HiggsXS.GetHiggsXS4Sample(self._YRVersion,self._YREnergy,iSample)
        print Higgs
        if not Higgs['xs'] == 0. : return str(Higgs['xs'])

      if iSample in self.xsections : 
        print iSample, self.xsections[iSample]['xs'] , self.xsections[iSample]['kfact']
        return str(float(self.xsections[iSample]['xs'])*float(self.xsections[iSample]['kfact']))
      else : 
        return ''

    def Print(self) :
      print self.xsections

#db = xsectionDB('1wH73CYA_T4KMkl1Cw-xLTj8YG7OPqayDnP53N-lZwFQ')
#print db.get(20001)


#######

def getSampleFiles(inputDir,Sample,absPath=False,rooFilePrefix='latino_',FromPostProc=False):

    

    #### SETUP DISK ACCESS ####
    #if someoune had defined xrootdPath, live with it
    if 'root://' in inputDir:
      xrdserver=inputDir.lstrip("root://").split("/")[0]
      xrootdPath='root://'+xrdserver
      absPath=True
      lsCmd='xrdfs '+xrdserver+' ls '
      Dir = inputDir.lstrip("root://").lstrip(xrdserver)
    else:  
      xrootdPath=''
      # ... IIHE
      if 'iihe' in os.uname()[1] :
        if not FromPostProc : absPath=True
        lsCmd='ls '
        if not '/pnfs/' in inputDir and '/store/' in inputDir: 
           Dir = '/pnfs/iihe/cms/' + inputDir
        else:                        
           Dir = inputDir
        if '/pnfs/' in inputDir :  xrootdPath='dcap://maite.iihe.ac.be/'

      # ... CERN
      elif 'cern' in os.uname()[1] : 
        if not '/eos/' in  inputDir and '/store/' in inputDir:
           Dir = '/eos/cms/' + inputDir
        else:                          
           Dir = inputDir
        if '/eos/cms/' in inputDir:
           absPath=True
           xrootdPath='root://eoscms.cern.ch/'
        # if   '/eos/cms/' in inputDir:
        # #   lsCmd='/afs/cern.ch/project/eos/installation/0.3.84-aquamarine/bin/eos.select ls '
        #    xrootdPath='root://eoscms.cern.ch/'
        # elif '/eos/user/' in inputDir:
        # #   lsCmd='/afs/cern.ch/project/eos/installation/0.3.84-aquamarine.user/eos.select ls '
        #    xrootdPath='root://eosuser.cern.ch/'     
        lsCmd='ls ' 
      
      # ... IFCA   
      elif 'ifca' in os.uname()[1] :
        lsCmd='ls '
        if not '/gpfs/' in inputDir and '/store/' in inputDir:
          Dir = '/gpfs/gaes/cms/' + inputDir 
        else:
          Dir = inputDir

      # ... PISA         
      elif "pi.infn.it" in socket.getfqdn():
        lsCmd='ls '
        if not '/gpfs/' in inputDir and '/store/' in inputDir:
          Dir = '/gpfs/ddn/srm/cms/' + inputDir 
        else:
          Dir = inputDir

      # ... KNU
      elif "knu" in os.uname()[1]:
        absPath=True
        lsCmd='ls '
        if not '/pnfs/' in inputDir and '/store/' in inputDir: 
          Dir = '/pnfs/knu.ac.kr/data/cms/' + inputDir
        else:
          Dir = inputDir 
        if '/pnfs/' in inputDir :  xrootdPath='dcap://cluster142.knu.ac.kr/'
       
      # ... KISTI
      elif "sdfarm" in os.uname()[1]:
        absPath=True
        lsCmd='ls '
        if not '/xrootd/' in inputDir and '/store/' in inputDir:
          Dir = '/xrootd/store/' + inputDir.split('/store/')[1]
        else:
          Dir = inputDir 
        if '/xrootd/' in Dir :
          #xrootdPath='root://cms-xrdr.sdfarm.kr/'
          #xrootdPath='root://cms-xrdr.sdfarm.kr:1094/' # outside of Korean farm
          xrootdPath='root://cms-xrdr.private.lo:2094/' # inside of Korean farm

      # ... DEFAULT: local mounted disk
      else :
        lsCmd='ls '
        Dir = inputDir


    ##### Now get the files for Sample
    fileCmd = lsCmd+Dir+'/'+rooFilePrefix+Sample+'.root'
    if 'root://' in inputDir:
      fileCmd = lsCmd+Dir+'/ | grep '+rooFilePrefix+Sample+'.root' 
    proc    = subprocess.Popen(fileCmd, stderr = subprocess.PIPE,stdout = subprocess.PIPE, shell = True)
    out,err = proc.communicate()
    Files   = string.split(out)
    if len(Files) == 0 :
      fileCmd = lsCmd+Dir+'/'+rooFilePrefix+Sample+'__part*.root'
      if 'root://' in inputDir:
        fileCmd = lsCmd+Dir+'/ | grep '+rooFilePrefix+Sample+'__part | grep root'
      proc    = subprocess.Popen(fileCmd, stderr = subprocess.PIPE,stdout = subprocess.PIPE, shell = True)
      out,err = proc.communicate()
      Files   = string.split(out)
    if len(Files) == 0 and not FromPostProc :
      print 'ERROR: No files found for sample ',Sample,' in directory ',Dir
      exit() 
    FileTarget = []
    for iFile in Files:
      if absPath :
	#if "sdfarm" in os.uname()[1]:
	#  if 'xrootd' in iFile: iFile = '/xrd/'+iFile.split('xrootd')[1]
        if not FromPostProc :
            if "sdfarm" in os.uname()[1]:
                if '/xrootd/' in iFile: iFile = '/xrd/'+iFile.split('xrootd')[1]
            FileTarget.append('###'+xrootdPath+iFile)
        else:
          FileTarget.append(iFile)
      else       : FileTarget.append(os.path.basename(iFile)) 
    return FileTarget

#### samples Weights

def addSampleWeight(sampleDic,key,Sample,Weight):


    ### Add Weights in sampleDic if needed
    if not 'weights' in sampleDic[key] :
      sampleDic[key]['weights'] = []
    if len(sampleDic[key]['weights']) == 0 :
      for iEntry in range(len(sampleDic[key]['name'])) : sampleDic[key]['weights'].append('(1.)')

    ### Now add the actual weight
    for iEntry in range(len(sampleDic[key]['name'])):
      name = sampleDic[key]['name'][iEntry]
      if '/' in name : name = os.path.basename(name)
      name = name.split('_',1)[-1].replace('.root','').split('__part')[0]
      if name == Sample: 
        sampleDic[key]['weights'][iEntry] += '*(' + Weight + ')'
      
#### To add ext samples
def getEventSumw(directory,sample,prefix):
    Files=getSampleFiles(directory,sample,False,prefix)
    genEventSumw  = 0.0
    for iFile in Files:
        f = ROOT.TFile.Open(iFile.replace('###',''), "READ")
        Runs=f.Get("Runs")
        for iRun in Runs:
            trailer = ""
            if hasattr(iRun, "genEventSumw_"): trailer = "_" 
            genEventSumw  += getattr(iRun, "genEventSumw"+trailer)
        f.Close()
    nEvt = genEventSumw
    return nEvt



#### BaseW across sample _ext

def getBaseW(directory,Samples = [] ):

    ### Count #evt

    nEvt = 0
    nTot = 0
    nPos = 0
    nNeg = 0

    for iSample in Samples : 
      Files = getSampleFiles(directory,iSample,True)
      for iFile in Files :
        #print 'Opening: ', iFile.replace('###','')
        fileIn = ROOT.TFile.Open(iFile.replace('###',''), "READ")
        h_mcWeightPos = fileIn.Get('mcWeightPos')
        h_mcWeightNeg = fileIn.Get('mcWeightNeg')
        if h_mcWeightPos.__nonzero__() and h_mcWeightNeg.__nonzero__() :
             nEvt += h_mcWeightPos.GetBinContent(1) - h_mcWeightNeg.GetBinContent(1)
             nPos += h_mcWeightPos.GetBinContent(1)
             nNeg += h_mcWeightNeg.GetBinContent(1)
             #print 'Pos, Neg = ',h_mcWeightPos.GetBinContent(1),h_mcWeightNeg.GetBinContent(1)
        else:
             nEvt += fileIn.Get('totalEvents').GetBinContent(1)
             nPos += fileIn.Get('totalEvents').GetBinContent(1)
        nTot += fileIn.Get('totalEvents').GetBinContent(1)
        fileIn.Close()
 
    ### Get XS
    xsDB = xsectionDB()
    CMSSW=os.environ["CMSSW_BASE"]
    #xsFile=CMSSW+'/src/LatinoTrees/AnalysisStep/python/samplesCrossSections.py'
    xsFile=CMSSW+'/src/LatinoAnalysis/NanoGardener/python/framework/samples/samplesCrossSections2016.py'
    print "I'm reading XS in latinoAnalysis"
    xsDB.readPython(xsFile)
    xsDB.readYR('YR4','13TeV')
    xs = []
    for iSample in Samples :
      xs.append( xsDB.get(iSample) )
    #print xs
    for iEntry in range(len(xs)):
      if not xs[iEntry] == xs[0] : 
        print 'ERROR: getBaseW: Trying to mix samples with different x-section'
        exit()

    ### And now get the baseW
    baseW = float(xs[0])*1000./nEvt
    #print 'baseW: xs,N -> W', xs[0], nEvt , baseW , ' nTot= ', nTot
    return str(baseW)

#### Print samples dic:

def getBaseWnAOD(directory,iProd,Samples = [] , prodCfg='LatinoAnalysis/NanoGardener/python/framework/Productions_cfg.py' ):

    # Compute #evts
    genEventCount = 0
    genEventSumw  = 0.0
    genEventSumw2 = 0.0

    for iSample in Samples :
      FileList = getSampleFiles(directory,iSample,True,'nanoLatino_')
      for iFile in FileList:
        f = ROOT.TFile.Open(iFile.replace('###',''),'READ')
        Runs = f.Get("Runs")
        for iRun in Runs :
          trailer = ""
          if hasattr(iRun, "genEventSumw_"): trailer = "_" 
          genEventCount += getattr(iRun, "genEventCount"+trailer)
          genEventSumw  += getattr(iRun, "genEventSumw" +trailer)
          genEventSumw2 += getattr(iRun, "genEventSumw2"+trailer)
        f.Close()
    
    ### Get XS

    # Load Producton Cfg + check
    CMSSW=os.environ["CMSSW_BASE"]
    if os.path.exists(CMSSW+'/src/'+prodCfg) :
      handle = open(CMSSW+'/src/'+prodCfg)
      exec(handle)
      handle.close()
      prodList =  Productions.keys()   
    else:
      print 'ERROR: Please specify the input data config'
      exit(1)
    if not iProd in prodList:
      print 'ERROR: iProd not in prodList: ',prodList 

    # Load X-section
    xsDB = xsectionDB()
    xsDB.readPython(CMSSW+'/src/'+Productions[iProd]['xsFile'])
    xsDB.readYR(Productions[iProd]['YRver'][0],Productions[iProd]['YRver'][1])

    # Get x-sections + checks
    xs = []
    for iSample in Samples : 
      if   '_ext' in iSample : iSampleXS = iSample.split('_ext')[0]
      elif '-ext' in iSample : iSampleXS = iSample.split('-ext')[0]
      else:                    iSampleXS = iSample
      xs.append( xsDB.get(iSampleXS) )
    for iEntry in range(len(xs)):
      if not xs[iEntry] == xs[0] :
        print 'ERROR: getBaseW: Trying to mix samples with different x-section'
        exit()

    ### AND NOW: Compute new baseW
    nEvt = genEventSumw
    Xsec  = xsDB.get(iSampleXS)
    baseW = float(Xsec)*1000./nEvt

    return str(baseW)
 
def printSampleDic(sampleDic):

    for iKey in sampleDic:
      print '----> Sample: '+iKey
      print 'globalWeight = '+sampleDic[iKey]['weight'] 
      for iEntry in range(len(sampleDic[iKey]['name'])) :
        print 'file = '+sampleDic[iKey]['name'][iEntry]
        if 'weights' in sampleDic[iKey] :
          print 'weight = '+sampleDic[iKey]['weights'][iEntry]  

#### SITE COMMANDS:

def getTmpDir():
    if   'iihe' in os.uname()[1] : return '/scratch/'
    elif 'cern' in os.uname()[1] : return '/tmp/$USER/'
    elif 'ifca' in os.uname()[1] : return '/gpfs/projects/cms/'+os.environ["USER"]+'/'
    else : return '/tmp'

def delDirSE(Dir):
    inDir = Dir
    if 'iihe' in os.uname()[1] :
      if not '/pnfs/iihe/cms' in inDir : inDir = '/pnfs/iihe/cms' + inDir
      os.system('echo ssh m10 rm -rf '+inDir)
    elif 'cern' in os.uname()[1] :
      if not '/eos/cms' in inDir : inDir = '/eos/cms' + inDir
      os.system('rm -rf '+inDir)
    elif 'ifca' in os.uname()[1] : 
      if not '/gpfs/gaes/cms' in inDir : inDir = '/gpfs/gaes/cms' + inDir
      os.system('rm -rf '+inDir) 
    else:
      print 'ERROR: Unknown SITE for srmcp2local ->exit()'
      exit()

def srmcp2local(inFile,outFile):
    srcFile = inFile
    if 'iihe' in os.uname()[1] :
      if not '/pnfs/iihe/cms' in srcFile : srcFile = '/pnfs/iihe/cms' + srcFile
      os.system('lcg-cp srm://maite.iihe.ac.be:8443'+srcFile+' file://'+outFile)
    elif 'cern' in os.uname()[1] :
      if not '/eos/cms' in srcFile : srcFile = '/eos/cms' + srcFile
      os.system('cp '+srcFile+' '+outFile)
    elif  'ifca' in os.uname()[1] : 
      if not '/gpfs/gaes/cms' in srcFile : srcFile = '/gpfs/gaes/cms' + srcFile
      os.system('cp '+srcFile+' '+outFile)
    else:
      print 'ERROR: Unknown SITE for srmcp2local ->exit()'
      exit()

def lsListCommand(inputDir, iniStep = 'Prod'):
    "Returns ls command on remote server directory (/store/...) in list format ( \n between every output )"
    if 'iihe' in os.uname()[1] :
      if '/pnfs/iihe/cms' in inputDir:
        usedDir = inputDir.split('/pnfs/iihe/cms')[1]
      else:
        usedDir = inputDir
      return "ls -1 /pnfs/iihe/cms" + usedDir
    elif 'cern' in os.uname()[1] :
      if '/eos/cms' in inputDir:
        usedDir = inputDir.split('/eos/cms')[1]
      else:
        usedDir = inputDir
      return 'ls /eos/cms' + usedDir
    elif 'ifca' in os.uname()[1] :
      if '/gpfs/gaes/cms/' in inputDir:
        usedDir = inputDir.split('/gpfs/gaes/cms/')[1]
      else:
        usedDir = inputDir
      return "ls /gpfs/gaes/cms/" + usedDir
    elif "pi.infn.it" in socket.getfqdn():
      if '/gpfs/ddn/srm/cms/' in inputDir:
        usedDir = inputDir.split('/gpfs/ddn/srm/cms/')[1]
      else:
        usedDir = inputDir
      return "ls /gpfs/ddn/srm/cms/" + usedDir
    elif "knu" in os.uname()[1]:
      if '/pnfs/knu.ac.kr/data/cms/' in inputDir:
        usedDir = inputDir.split('/pnfs/knu.ac.kr/data/cms/')[1]
      else:
        usedDir = inputDir
      return "ls /pnfs/knu.ac.kr/data/cms/" + usedDir
    elif "sdfarm" in os.uname()[1]:
      if '/xrootd/' in inputDir:
        usedDir = inputDir.split('/xrootd/')[1]
      else:
        usedDir = inputDir
      return "ls /xrootd/" + usedDir
    elif "hercules" in os.uname()[1]:   # cluster MiB
      if "/store/group" in inputDir:
        return "ls /gwteras/cms/" +inputDir
      else:
        return "ls "+ inputDir
    else :
      if iniStep == 'Prod' :
        return " ls " + inputDir
      else:
        return " ls " + inputDir
    
def rootReadPath(inputFile):
    "Returns path to read a root file (/store/.../*.root) on the remote server"
    if 'iihe' in os.uname()[1] :
        return "dcap://maite.iihe.ac.be/pnfs/iihe/cms" + inputFile
    elif "pi.infn.it" in socket.getfqdn():
      return "/gpfs/ddn/srm/cms/" + inputFile
    elif 'ifca' in os.uname()[1] :
      return "/gpfs/gaes/cms/" + inputFile
    elif 'knu' in os.uname()[1] :
      return "dcap://cluster142.knu.ac.kr//pnfs/knu.ac.kr/data/cms" + inputFile
    elif 'sdfarm' in os.uname()[1] :
      return "root://cms-xrdr.sdfarm.kr:1094//xrd" + inputFile
    elif 'hercules' in os.uname()[1]:
      return "/gwteras/cms" + inputFile
    else :
       return "/eos/cms" + inputFile
       # return  inputFile
    
def remoteFileSize(inputFile):
    "Returns file size in byte for file on remote server (/store/.../*.root)"
    if 'iihe' in os.uname()[1] :
      if "/pnfs" in inputFile:
        return subprocess.check_output("ls -l " + inputFile + " | cut -d ' ' -f 5", shell=True)
      else:
        return subprocess.check_output("ls -l /pnfs/iihe/cms" + inputFile + " | cut -d ' ' -f 5", shell=True)
    elif 'cern' in os.uname()[1] :
      if '/eos/cms/' in inputFile:
        return subprocess.check_output("ls -l " +inputFile + " | cut -d ' ' -f 5", shell=True)
      else:
        return subprocess.check_output("ls -l /eos/cms/" + inputFile + " | cut -d ' ' -f 5", shell=True)
    elif 'ifca' in os.uname()[1] :
        return subprocess.check_output("ls -l /gpfs/gaes/cms/" + inputFile + " | cut -d ' ' -f 5", shell=True)
    elif "pi.infn.it" in socket.getfqdn():
        return subprocess.check_output("ls -l /gpfs/ddn/srm/cms/" + inputFile + " | cut -d ' ' -f 5", shell=True)
    elif "knu" in os.uname()[1]:
      if '/pnfs' in inputFile:
        return subprocess.check_output("ls -l " + inputFile + " | cut -d ' ' -f 5", shell=True)
      else:
        return subprocess.check_output("ls -l /pnfs/knu.ac.kr/data/cms/" + inputFile + " | cut -d ' ' -f 5", shell=True)
    elif "sdfarm" in os.uname()[1]:
      if '/xrootd' in inputFile:
        return subprocess.check_output("ls -l " + inputFile + " | cut -d ' ' -f 5", shell=True)
      else:
        return subprocess.check_output("ls -l /xrootd/" + inputFile + " | cut -d ' ' -f 5", shell=True)
    elif "hercules" in os.uname()[1]:
      if "/store/group" in inputFile:
        return subprocess.check_output("ls -l /gwteras/cms" + inputFile +" | cut -d ' ' -f 5", shell=True)
      else:
        return subprocess.check_output("ls -l "+ inputFile +" | cut -d ' ' -f 5", shell=True)
    else :
       return subprocess.check_output("ls -l /eos/cms/" + inputFile + " | cut -d ' ' -f 5", shell=True)
       # return subprocess.check_output("ls -l " + inputFile + " | cut -d ' ' -f 5", shell=True)


 
