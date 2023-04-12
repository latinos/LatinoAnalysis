#!/bin/env python

from LatinoAnalysis.Tools.commonTools import getSampleFiles

import os
import multiprocessing
import ROOT

def nanoGetSampleFiles(inputDir, sample):
    return getSampleFiles(inputDir, sample, True, 'nanoLatino_')

exec(open(os.getenv("CMSSW_BASE") + "/src/LatinoAnalysis/NanoGardener/python/framework/samples/HMjjlnu_samples.py"))
baseDir = '/eos/cms/store/group/phys_higgs/cmshww/amassiro/HWWNano/'

#productions = ['Summer16_102X_nAODv7_Full2016v7']
#productions = ['Fall2017_102X_nAODv7_Full2017v7']
productions = ['Autumn18_102X_nAODv7_Full2018v7']
directories = ['HMlnjjVarsGen__BWReweight_LNuQQ']

prod_dirs = zip(productions,directories)

variations=[0.00, 0.01, 0.02, 0.05, 0.10, 0.20, 0.30, 10.0, 100.0, "orig"]

NUM_PROC  = 5
for p,d in prod_dirs:
  print p,d
  for sample in LNuQQSamples:
    sampledir=baseDir+"/"+p+"/"+d
    pid = os.fork()
    if pid==0:
      files = nanoGetSampleFiles(sampledir, sample)
      #print files
      chain = ROOT.TChain("Events")
      for infile in files:
        infile = infile[25:]
        #print infile
        chain.Add(infile)
      horig = ROOT.TH1F("horig", "horig", 2, 0, 2)
      chain.Draw("1>>horig", "genWeight", "goff")
      for variation in variations:
        hvar = ROOT.TH1F("hvar", "hvar", 2, 0, 2)
        chain.Draw("1>>hvar", "genWeight*RelW"+str(variation), "goff")
        #print sample, variation, horig.Integral(), hvar.Integral(), horig.Integral()/hvar.Integral()
        print sample, variation, "-1", hvar.Integral()/horig.Integral()
        del hvar
      exit(0)
    else:
      os.waitpid(pid, 0)
    

