#!/usr/bin/env python
import os, sys
import ROOT
ROOT.PyConfig.IgnoreCommandLineOptions = True

from PhysicsTools.NanoAODTools.postprocessing.framework.postprocessor import PostProcessor

from PhysicsTools.NanoAODTools.postprocessing.modules.common.puWeightProducer import *
from LatinoAnalysis.NanoGardener.modules.TrigMaker import *

files=['NANO_testFile_lepMkrSel.root']
#files=["/afs/cern.ch/user/l/lenzip/work/ww2018/CMSSW_9_4_4/src/LatinoAnalysis/NanoGardener/test/8C03AD47-0613-E811-9781-0242AC1C0500_Skim.root"]
#this takes care of converting the input files from CRAB
#from PhysicsTools.NanoAODTools.postprocessing.framework.crabhelper import inputFiles,runsAndLumis

selection = None

p=PostProcessor(".",files,cut=selection,branchsel=None,modules=[trigMkr_MC('Full2016')],postfix='_trigMkr',provenance=True,fwkJobReport=True)
p.run()

print "DONE"
