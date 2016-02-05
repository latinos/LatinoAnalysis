#!/usr/bin/env python
import sys, re, os, os.path, string
import ROOT
from ROOT import *
from array import array 

class HiggsXSection:

   def file2map(self,x):
        ret = {}; headers = []
        for x in open(x,"r"):
            cols = x.split()
            if len(cols) < 2: continue
            if "mH" in x:
                headers = [i.strip() for i in cols[1:]]
            else:
                fields = [ float(i) for i in cols ]
                ret[fields[0]] = dict(zip(headers,fields[1:]))
        return ret

   def __init__(self):
      self._cmssw=os.environ["CMSSW_BASE"]
      self._basepath=self._cmssw+'/src/LatinoAnalysis/Tools/data/'
      self._YR = {}       
      
      self.readYR('YR2','7TeV')
      self.readYR('YR2','8TeV')

      self.readYR('YR3','7TeV')
      self.readYR('YR3','8TeV')
      
      self.readYR('YR4prel','13TeV')

   def readYR(self,YRversion,energy,model='sm'):
      if not YRversion in ['YR2','YR3','YR4prel'] : return
      if not energy in ['7TeV','8TeV','13TeV' ] : return
      # Create Structure
      if not YRversion in self._YR : self._YR[YRversion] = {}
      if not model  in self._YR[YRversion] : self._YR[YRversion][model] = {}
      if not 'xs' in self._YR[YRversion][model] : self._YR[YRversion][model]['xs'] = {}
      if not 'br' in self._YR[YRversion][model] : self._YR[YRversion][model]['br'] = {}
      
      # Add x-sections
      if YRversion in  ['YR2','YR3'] :
        if not energy in ['7TeV','8TeV'] : return  
        if not energy in self._YR[YRversion][model]['xs'] : self._YR[YRversion][model]['xs'][energy] = {}
        self._YR[YRversion][model]['xs'][energy]['ggH'] = self.file2map(self._basepath+'lhc-hxswg-'+YRversion+'/sm/xs/'+energy+'/'+energy+'-ggH.txt') 
        self._YR[YRversion][model]['xs'][energy]['vbfH'] = self.file2map(self._basepath+'lhc-hxswg-'+YRversion+'/sm/xs/'+energy+'/'+energy+'-vbfH.txt') 
        self._YR[YRversion][model]['xs'][energy]['WH'] = self.file2map(self._basepath+'lhc-hxswg-'+YRversion+'/sm/xs/'+energy+'/'+energy+'-WH.txt') 
        self._YR[YRversion][model]['xs'][energy]['ZH'] = self.file2map(self._basepath+'lhc-hxswg-'+YRversion+'/sm/xs/'+energy+'/'+energy+'-ZH.txt') 
        self._YR[YRversion][model]['xs'][energy]['ttH'] = self.file2map(self._basepath+'lhc-hxswg-'+YRversion+'/sm/xs/'+energy+'/'+energy+'-ttH.txt') 
  
      if YRversion in  ['YR4prel'] :
        if not energy in ['13TeV'] : return  
        if not energy in self._YR[YRversion][model]['xs'] : self._YR[YRversion][model]['xs'][energy] = {}
        self._YR[YRversion][model]['xs'][energy]['ggH'] = self.file2map(self._basepath+'lhc-hxswg-'+YRversion+'/sm/xs/'+energy+'/'+energy+'-ggH.txt') 
        self._YR[YRversion][model]['xs'][energy]['vbfH'] = self.file2map(self._basepath+'lhc-hxswg-'+YRversion+'/sm/xs/'+energy+'/'+energy+'-vbfH.txt') 
        self._YR[YRversion][model]['xs'][energy]['ttH'] = self.file2map(self._basepath+'lhc-hxswg-'+YRversion+'/sm/xs/'+energy+'/'+energy+'-ttH.txt') 

      # BR
      if YRversion in  ['YR2'] : 
        self._YR[YRversion][model]['br']['VV'] = self.file2map(self._basepath+'lhc-hxswg-'+YRversion+'/sm/br/BR.txt')
        self._YR[YRversion][model]['br']['ff'] = self.file2map(self._basepath+'lhc-hxswg-'+YRversion+'/sm/br/BR1.txt')
      if YRversion in  ['YR3'] : 
        self._YR[YRversion][model]['br']['VV'] = self.file2map(self._basepath+'lhc-hxswg-'+YRversion+'/sm/br/BR2bosons.txt')
        self._YR[YRversion][model]['br']['ff'] = self.file2map(self._basepath+'lhc-hxswg-'+YRversion+'/sm/br/BR2fermions.txt')
      if YRversion in  ['YR4prel'] :  
        print self._basepath+'lhc-hxswg-'+YRversion+'/sm/br/BR4.txt'
        self._YR[YRversion][model]['br']['VV'] = self.file2map(self._basepath+'lhc-hxswg-'+YRversion+'/sm/br/BR4.txt')
        self._YR[YRversion][model]['br']['ff'] = self.file2map(self._basepath+'lhc-hxswg-'+YRversion+'/sm/br/BR4.txt')

   def printYR(self):
      print self._YR

   def GetYRVal(self,YRDic,mh,Key):
     iMass=float(mh)
     if iMass in YRDic :
       if not Key in YRDic[iMass] : return 0.
       return YRDic[iMass][Key]
     else:
       n=len(YRDic.keys())
       x=[]
       y=[]
       for jMass in sorted(YRDic.keys()):
         if  Key in YRDic[jMass] :
           x.append(jMass)
           y.append(YRDic[jMass][Key])
       if iMass < x[0] or iMass > x[n-1] : return 0
       gr = TGraph(n,array('f',x),array('f',y));
       sp = TSpline3("YR",gr);
       return sp.Eval(iMass)
     return 0

   def GetHiggsProdXS(self,YRversion,energy,proc,mh,model='sm'):
     if not YRversion in self._YR                                 : return 0
     if not model     in self._YR[YRversion]                      : return 0
     if not 'xs'      in self._YR[YRversion][model]               : return 0
     if not energy    in self._YR[YRversion][model]['xs']         : return 0
     if not proc      in self._YR[YRversion][model]['xs'][energy] : return 0 
     return self.GetYRVal(self._YR[YRversion][model]['xs'][energy][proc],mh,'XS_pb')

   def YR4dec(self,YRversion,decay):
     if not YRversion in ['YR4prel' ] : return decay
     if decay == 'H_bb'       : return 'hbb'
     if decay == 'H_tautau'   : return 'htt'
     if decay == 'H_mumu'     : return 'hmm'
     if decay == 'H_ssbar'    : return 'hss'
     if decay == 'H_ccbar'    : return 'hcc'
     if decay == 'H_ttbar'    : return 'htoptop'
     if decay == 'H_gg'       : return 'hgluglu'
     if decay == 'H_gamgam'   : return 'hgg'
     if decay == 'H_Zgam'     : return 'hzg'
     if decay == 'H_WW'       : return 'hww'
     if decay == 'H_ZZ'       : return 'hzz'
     return decay

   def GetHiggsBR(self,YRversion,decay,mh,model='sm'):
     if not YRversion in self._YR                                 : return 0
     if not model     in self._YR[YRversion]                      : return 0
     if not 'br'      in self._YR[YRversion][model]               : return 0
     if   decay in [ 'H_bb', 'H_tautau' , 'H_mumu' , 'H_ssbar'  , 'H_ccbar'  , 'H_ttbar' ] : 
       return self.GetYRVal(self._YR[YRversion][model]['br']['ff'],mh,self.YR4dec(YRversion,decay))
     elif decay in [ 'H_gg', 'H_gamgam', 'H_Zgam', 'H_WW' , 'H_ZZ', 'Total_Width_GeV' ] : 
       return self.GetYRVal(self._YR[YRversion][model]['br']['VV'],mh,self.YR4dec(YRversion,decay))
     return 0



HiggsXS = HiggsXSection() 
#HiggsXS.printYR()
print HiggsXS.GetHiggsProdXS('YR2','8TeV','ggH','125.0')
print HiggsXS.GetHiggsProdXS('YR3','8TeV','ggH','125.0')
print HiggsXS.GetHiggsProdXS('YR4prel','13TeV','ggH','125.0')

print HiggsXS.GetHiggsBR('YR2','H_WW','125.0')
print HiggsXS.GetHiggsBR('YR3','H_WW','125.0')
print HiggsXS.GetHiggsBR('YR4prel','H_WW','125.0')

