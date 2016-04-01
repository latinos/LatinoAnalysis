#!/usr/bin/env python
import sys, re, os, os.path, string
import ROOT
from ROOT import *
from array import array 

def file2map(x):
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


Cha=['hbb','htt','hmm','hcc','hss','htoptop','hgluglu','hgg','hzg','hww','hzz']

Width=file2map('Width.txt')
#print Width
f = open('BR4.txt', 'w')
f.write('mH_GeV  ')
for iCha in Cha:
  f.write(iCha+'            ')
f.write('Total_Width_GeV')
f.write('\n') 

for iMass in sorted(Width.keys()):
  f.write(str(iMass)+'  ')  
  #print iMass
  TotWidth=0
  for iCha in Cha: 
    TotWidth+=Width[iMass][iCha]
    #print iCha , Width[iMass][iCha]
  #print 'tot' , TotWidth 
  br={}
  for iCha in Cha:
    br[iCha]=Width[iMass][iCha]/TotWidth
    #print iCha , br[iCha] 
    f.write('%.2e        '% br[iCha])
  f.write('%.2e' % TotWidth)
  f.write('\n')  

f.close()
