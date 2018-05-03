#!/usr/bin/env python
'''
put this file in LatinoAnalysis/NanoGardener/test/
'''

import os, sys
import ROOT
ROOT.PyConfig.IgnoreCommandLineOptions = True

from PhysicsTools.NanoAODTools.postprocessing.framework.postprocessor import PostProcessor

from PhysicsTools.NanoAODTools.postprocessing.modules.common.puWeightProducer import *
from LatinoAnalysis.NanoGardener.modules.LeptonMaker import *
from LatinoAnalysis.NanoGardener.modules.LeptonSelLazy import *

#files1=['8C03AD47-0613-E811-9781-0242AC1C0500.root']
files1=['NANO_testFile.root']
#files2=['8C03AD47-0613-E811-9781-0242AC1C0500_lepMkr.root']
#files=["/afs/cern.ch/user/l/lenzip/work/ww2018/CMSSW_9_4_4/src/LatinoAnalysis/NanoGardener/test/8C03AD47-0613-E811-9781-0242AC1C0500_Skim.root"]
#this takes care of converting the input files from CRAB
#from PhysicsTools.NanoAODTools.postprocessing.framework.crabhelper import inputFiles,runsAndLumis

#selection = "nElectron + nMuon > 0 && Electron_pt[0]>20 && Muon_pt[0]>20 && nJet>1 && Jet_pt[0]>30 && Jet_pt[1]>30"
selection = "nElectron + nMuon > 0"

p1=PostProcessor(".",files1,cut=selection,branchsel=None,modules=[LeptonMaker(), LeptonSelLazy('Full2016', 'Loose', 1)],postfix='_lepMkrSelLazy',provenance=True,fwkJobReport=True)
p1.run()
#p2=PostProcessor(".",files2,cut=selection,branchsel=None,modules=[lepSel('Full2016', 'Loose', 1)],postfix='_lepSel',provenance=True,fwkJobReport=True)
#p2.run()

print "DONE"
