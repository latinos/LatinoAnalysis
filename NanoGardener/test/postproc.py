#!/usr/bin/env python
import os, sys
import ROOT
ROOT.PyConfig.IgnoreCommandLineOptions = True

from PhysicsTools.NanoAODTools.postprocessing.framework.postprocessor import PostProcessor

from PhysicsTools.NanoAODTools.postprocessing.modules.common.puWeightProducer import *
from LatinoAnalysis.NanoGardener.modules.Grafter import *
from LatinoAnalysis.NanoGardener.modules.GenericFormulaAdder import *
from LatinoAnalysis.NanoGardener.modules.HiggsGenVarsProducer import *
from LatinoAnalysis.NanoGardener.modules.PromptParticlesGenVarsProducer import *
from LatinoAnalysis.NanoGardener.modules.GenLeptonMatchProducer import *
from LatinoAnalysis.NanoGardener.modules.TopGenVarsProducer import *
from LatinoAnalysis.NanoGardener.modules.wwNLLcorrectionWeightProducer import *
from LatinoAnalysis.NanoGardener.modules.MetUnclustered import *

from PhysicsTools.NanoAODTools.postprocessing.modules.common.collectionMerger import collectionMerger
from PhysicsTools.NanoAODTools.postprocessing.modules.btv.btagSFProducer import btagSFProducer

lepMergerLatino = lambda : collectionMerger(
        input  = ["Electron","Muon"],
        output = "Lepton", 
        reverse = True
        )




from LatinoAnalysis.NanoGardener.modules.l2KinProducer import *
from LatinoAnalysis.NanoGardener.modules.l3KinProducer import *
from LatinoAnalysis.NanoGardener.modules.l4KinProducer import *

from LatinoAnalysis.NanoGardener.modules.GenVarProducer import *
from LatinoAnalysis.NanoGardener.modules.BTagEventWeightProducer import *



#files=["root://cms-xrd-global.cern.ch//store/mc/RunIISummer16NanoAOD/GluGluHToWWTo2L2Nu_M125_13TeV_powheg_pythia8/NANOAODSIM/PUMoriond17_05Feb2018_94X_mcRun2_asymptotic_v2-v1/40000/8C03AD47-0613-E811-9781-0242AC1C0500.root"]
#files=["/afs/cern.ch/user/l/lenzip/work/ww2018/CMSSW_9_4_4/src/LatinoAnalysis/NanoGardener/test/8C03AD47-0613-E811-9781-0242AC1C0500_Skim.root"]

#xrdcp root://cms-xrd-global.cern.ch//store/mc/RunIISummer16NanoAOD/GluGluHToWWTo2L2Nu_M125_13TeV_powheg_pythia8/NANOAODSIM/PUMoriond17_05Feb2018_94X_mcRun2_asymptotic_v2-v1/40000/8C03AD47-0613-E811-9781-0242AC1C0500.root .
#files=["8C03AD47-0613-E811-9781-0242AC1C0500.root"]
files=["8C03AD47-0613-E811-9781-0242AC1C0500.root"]


#this takes care of converting the input files from CRAB
#from PhysicsTools.NanoAODTools.postprocessing.framework.crabhelper import inputFiles,runsAndLumis

selection = "nElectron>0 && nMuon>0 && Electron_pt[0]>20 && Muon_pt[0]>20 && nJet>1 && Jet_pt[0]>30 && Jet_pt[1]>30"

#p=PostProcessor(".",files,cut=selection,branchsel=None,modules=[Grafter(["baseW/F=1."]), GenericFormulaAdder('data/formulasToAdd_MC.py')],provenance=True,fwkJobReport=True)

p = PostProcessor(".", files,
                       cut=selection,
                       branchsel=None,
                       modules=[
                         Grafter(["baseW/F=1."]),
                         GenericFormulaAdder('data/formulasToAdd_MC.py'),
                         PromptParticlesGenVarsProducer(),
                         #wwNLLcorrectionWeightProducer(),
                         #MetUnclusteredTreeMaker(),
                         lepMergerLatino(),
                         GenLeptonMatchProducer("Lepton"),
                         #
                         GenVarProducer(),
                         #
                         #l2KinProducer(),
                         #l3KinProducer(),
                         #l4KinProducer()
                         btagSFProducer(era='2016', algo='cmva'),
                         BTagEventWeightProducer()
                         ],
                       provenance=True,
                       fwkJobReport=True
                       )

p.run()

print "DONE"
os.system("ls -lR")

