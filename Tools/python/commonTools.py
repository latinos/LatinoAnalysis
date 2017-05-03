#!/usr/bin/env python
import sys, re, os, os.path, string
import subprocess
from cookielib import CookieJar
from urllib2 import build_opener, HTTPCookieProcessor
import socket

from LatinoAnalysis.Tools.HiggsXSection  import *

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
        #print iSample, self.xsections[iSample]['sample'], self.xsections[iSample]['xs']
        return str(float(self.xsections[iSample]['xs'])*float(self.xsections[iSample]['kfact']))
      else : 
        return ''

    def Print(self) :
      print self.xsections

#db = xsectionDB('1wH73CYA_T4KMkl1Cw-xLTj8YG7OPqayDnP53N-lZwFQ')
#print db.get(20001)


#######

def getSampleFiles(inputDir,Sample,absPath=False):

    

    #### SETUP DISK ACCESS ####

    xrootdPath=''
    # ... IIHE
    if 'iihe' in os.uname()[1] :
      absPath=True
      lsCmd='ls '
      if not '/pnfs/' in inputDir and '/store/' in inpuDir: 
         Dir = '/pnfs/iihe/cms/' + inputDir
      else:                        
         Dir = inputDir
      if '/pnfs/' in inputDir :  xrootdPath='dcap://maite.iihe.ac.be/'

    # ... CERN
    elif 'cern' in os.uname()[1] : 
      if not '/eos/' in  inputDir and '/store/' in inpuDir:
         Dir = '/eos/cms/' + inputDir
      else:                          
         Dir = inputDir
      if   '/eos/cms/' in inputDir:
      #   lsCmd='/afs/cern.ch/project/eos/installation/0.3.84-aquamarine/bin/eos.select ls '
         xrootdPath='root://eoscms.cern.ch/'
      elif '/eos/user/' in inputDir:
      #   lsCmd='/afs/cern.ch/project/eos/installation/0.3.84-aquamarine.user/eos.select ls '
         xrootdPath='root://eosuser.cern.ch/'     
      lsCmd='ls ' 
    
    # ... IFCA   
    elif 'ifca' in os.uname()[1] :
      lsCmd='ls '
      if not '/gpfs/' in inputDir and '/store/' in inpuDir:
        Dir = '/gpfs/gaes/cms/' + inputDir 
      else:
        Dir = inputDir

    # ... PISA         
    elif "pi.infn.it" in socket.getfqdn():
      lsCmd='ls '
      if not '/gpfs/' in inputDir and '/store/' in inpuDir:
        Dir = '/gpfs/ddn/srm/cms/' + inputDir 
      else:
        Dir = inputDir

    # ... KNU
    elif "knu" in os.uname()[1]:
      lsCmd='ls '
      if not '/pnfs/' in inputDir and '/store/' in inpuDir: 
        Dir = '/pnfs/knu.ac.kr/data/cms/' + inputDir
      else:
        Dir = inputDir 

    # ... DEFAULT: local mounted disk
    else :
      lsCmd='ls '
      Dir = inputDir

    #print xrootdPath, Dir , lsCmd , Sample

    ##### Now get the files for Sample
    fileCmd = lsCmd+Dir+'/latino_'+Sample+'.root'
    proc    = subprocess.Popen(fileCmd, stderr = subprocess.PIPE,stdout = subprocess.PIPE, shell = True)
    out,err = proc.communicate()
    Files   = string.split(out)
    if len(Files) == 0 :
      fileCmd = lsCmd+Dir+'/latino_'+Sample+'__part*.root'
      proc    = subprocess.Popen(fileCmd, stderr = subprocess.PIPE,stdout = subprocess.PIPE, shell = True)
      out,err = proc.communicate()
      Files   = string.split(out)
    if len(Files) == 0 :
      print 'ERROR: No files found for smaple ',Sample,' in directory ',Dir
      exit() 
    FileTarget = []
    for iFile in Files:
      if absPath : FileTarget.append('###'+xrootdPath+iFile)
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
      name = sampleDic[key]['name'][iEntry].replace('latino_','').replace('.root','').split('__part')[0]
      if name == Sample: 
        sampleDic[key]['weights'][iEntry] += '*(' + Weight + ')'
      

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
    xsFile=CMSSW+'/src/LatinoTrees/AnalysisStep/python/samplesCrossSections.py'
    xsDB.readPython(xsFile)
    xsDB.readYR('YR4prel','13TeV')
    xs = []
    for iSample in Samples :
      xs.append( xsDB.get(iSample) )
    print xs
    for iEntry in range(len(xs)):
      if not xs[iEntry] == xs[0] : 
        print 'ERROR: getBaseW: Trying to mix samples with different x-section'
        exit()

    ### And now get the baseW
    baseW = float(xs[0])*1000./nEvt
    print 'baseW: xs,N -> W', xs[0], nEvt , baseW , ' nTot= ', nTot
    return str(baseW)

#### Print samples dic:
 
def printSampleDic(sampleDic):

    for iKey in sampleDic:
      print '----> Sample: '+iKey
      print 'globalWeight = '+sampleDic[iKey]['weight'] 
      for iEntry in range(len(sampleDic[iKey]['name'])) :
        print 'file = '+sampleDic[iKey]['name'][iEntry]
        if 'weights' in sampleDic[iKey] :
          print 'weight = '+sampleDic[iKey]['weights'][iEntry]  



 
