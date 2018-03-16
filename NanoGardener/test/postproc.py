#!/usr/bin/env python
import os, sys
import ROOT
ROOT.PyConfig.IgnoreCommandLineOptions = True

from PhysicsTools.NanoAODTools.postprocessing.framework.postprocessor import PostProcessor

from PhysicsTools.NanoAODTools.postprocessing.modules.common.puWeightProducer import *
from LatinoAnalysis.NanoGardener.modules.Grafter import *

files=["/afs/cern.ch/user/l/lenzip/work/ww2018/CMSSW_9_4_4/src/8C03AD47-0613-E811-9781-0242AC1C0500.root"]
#this takes care of converting the input files from CRAB
#from PhysicsTools.NanoAODTools.postprocessing.framework.crabhelper import inputFiles,runsAndLumis

selection = "nElectron>0 && nMuon>0 && Electron_pt[0]>20 && Muon_pt[0]>20 && nJet>1 && Jet_pt[0]>30 && Jet_pt[1]>30"

p=PostProcessor(".",files,cut=selection,branchsel=None,modules=[Grafter(["baseW/F=51.*32."])],provenance=True,fwkJobReport=True)
p.run()

print "DONE"
os.system("ls -lR")
