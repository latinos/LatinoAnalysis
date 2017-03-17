#!/usr/bin/env python
import sys, re, os, os.path, string
import subprocess
from cookielib import CookieJar
from urllib2 import build_opener, HTTPCookieProcessor

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

def getSampleFiles(inputDir,Sample):

    print Dir,Sample
    




    if 'iihe' in os.uname()[1] :
        lsCmd='ls '
        if not '/pnfs' in inputDir : Dir = '/pnfs/iihe/cms/' + inputDir
        else:                        Dir = inputDir
        
    elif 'ifca' in os.uname()[1] :
        return "ls /gpfs/gaes/cms/" + inputDir
        else:                        Dir = inputDir  
#   elif "pi.infn.it" in socket.getfqdn():
#       return "ls /gpfs/ddn/srm/cms/" + inputDir
#   elif "knu" in os.uname()[1]:
#       return "ls /pnfs/knu.ac.kr/data/cms/" + inputDir
#   else :
#       return "/afs/cern.ch/project/eos/installation/0.3.84-aquamarine/bin/eos.select ls " + inputDir

