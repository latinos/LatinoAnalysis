#!/usr/bin/env python
import sys, re, os, os.path, string
import subprocess
from cookielib import CookieJar
from urllib2 import build_opener, HTTPCookieProcessor
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

    def __init__(self,gdocKey='1wH73CYA_T4KMkl1Cw-xLTj8YG7OPqayDnP53N-lZwFQ'):

      self.xsections = {} 

      opener = build_opener(HTTPCookieProcessor(CookieJar()))
      resp = opener.open('https://docs.google.com/spreadsheet/ccc?key='+gdocKey+'&output=csv')
      data = resp.read()
      for line in data.splitlines(): 
        info=line.split(",")
        iID=info[0].replace(' ','')
        if iID.isdigit() :
          iKey = info[1].replace(' ','')
          self.xsections[iKey] = {}
          self.xsections[iKey]['ID']     = iID
          self.xsections[iKey]['sample'] = info[1].replace(' ','')
          if len(info) > 9 :
            self.xsections[iKey]['xs']     = info[9].replace(' ','')
          else: 
            self.xsections[iKey]['xs']     = ''

      #print self.xsections

    def get(self,iSample):
      if iSample in self.xsections : 
        #print iSample, self.xsections[iSample]['sample'], self.xsections[iSample]['xs']
        return self.xsections[iSample]['xs']
      else : 
        return ''

#db = xsectionDB('1wH73CYA_T4KMkl1Cw-xLTj8YG7OPqayDnP53N-lZwFQ')
#print db.get(20001)

