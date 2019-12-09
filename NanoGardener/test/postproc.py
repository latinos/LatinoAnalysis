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
from LatinoAnalysis.NanoGardener.modules.qq2vvEWKcorrectionsWeightProducer import *
from LatinoAnalysis.NanoGardener.modules.qq2VEWKcorrectionsWeightProducer import *


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




#/WZTo3LNu_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIIAutumn18NanoAODv5-Nano1June2019_102X_upgrade2018_realistic_v19-v1/NANOAODSIM
#/store/mc/RunIIAutumn18NanoAODv5/WZTo3LNu_TuneCP5_13TeV-amcatnloFXFX-pythia8/NANOAODSIM/Nano1June2019_102X_upgrade2018_realistic_v19-v1/60000/F575D852-8B1F-1C4A-B788-E049F3892AE3.root

#xrdcp root://cms-xrd-global.cern.ch//store/mc/RunIIAutumn18NanoAODv5/WZTo3LNu_TuneCP5_13TeV-amcatnloFXFX-pythia8/NANOAODSIM/Nano1June2019_102X_upgrade2018_realistic_v19-v1/60000/F575D852-8B1F-1C4A-B788-E049F3892AE3.root .
files=["F575D852-8B1F-1C4A-B788-E049F3892AE3.root"]


#selection = "nElectron>0 && nMuon>0 && Electron_pt[0]>20 && Muon_pt[0]>20 && nJet>1 && Jet_pt[0]>30 && Jet_pt[1]>30"
selection = "nElectron>0 && nMuon>0 && Electron_pt[0]>20 && Muon_pt[0]>20"

p = PostProcessor(".", files,
                       cut=selection,
                       branchsel=None,
                       #maxEntries=1000,
                       maxEntries=10000,
                       modules=[
                         #
                         lepMergerLatino(),
                         #
                         Grafter(["baseW/F=1."]),
                         #GenericFormulaAdder('data/formulasToAdd_MC_2018.py'),
                         #PromptParticlesGenVarsProducer(),
                         #wwNLLcorrectionWeightProducer(),
                         #MetUnclusteredTreeMaker(),
                         #GenLeptonMatchProducer("Lepton"),
                         #
                         #GenVarProducer(),
                         #
                         #l2KinProducer(),
                         #l3KinProducer(),
                         #l4KinProducer()
                         #btagSFProducer(era='2016', algo='cmva'),
                         #BTagEventWeightProducer(),
                         #
                         #vvNLOEWKcorrectionWeightProducer('ww')
                         #vvNLOEWKcorrectionWeightProducer('wz')
                         vvNLOEWKcorrectionWeightProducer('zz')
                         #
                         #vNLOEWKcorrectionWeightProducer('z')
                         #vNLOEWKcorrectionWeightProducer('zvv')
                         #vNLOEWKcorrectionWeightProducer('w')
                         ],
                       provenance=True,
                       fwkJobReport=True
                       )

p.run()

print "DONE"

os.system("ls -lR")




