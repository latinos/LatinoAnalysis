#!/usr/bin/env python
import os, sys 
import ROOT
ROOT.PyConfig.IgnoreCommandLineOptions = True
from PhysicsTools.NanoAODTools.postprocessing.framework.postprocessor import PostProcessor
#from LatinoAnalysis.NanoGardener.modules.qq2vv2lnujjEWKcorrectionsWeightProducer import *
#from LatinoAnalysis.NanoGardener.modules.qq2vvEWKcorrectionsWeightProducer2 import *
from LatinoAnalysis.NanoGardener.modules.qq2vvEWKcorrectionsWeightProducer import *

files=[
    #'/eos/cms/store/group/phys_higgs/cmshww/amassiro/HWWNano/Fall2017_102X_nAODv5_Full2017v6/MCl1loose2017v6__MCCorr2017v6__l2loose__l2tightOR2017v6/nanoLatino_WWTo2L2Nu__part2.root'
    #'/eos/cms/store/group/phys_higgs/cmshww/amassiro/HWWNano/Fall2017_102X_nAODv5_Full2017v6/MCl1loose2017v6__MCCorr2017v6__Semilep2017/nanoLatino_VBFHToWWToLNuQQ_M120__part0.root'
    '/eos/cms/store/group/phys_higgs/cmshww/amassiro/HWWNano/Summer16_102X_nAODv5_Full2016v6/MCl1loose2016v6__MCCorr2016v6/nanoLatino_WWToLNuQQ__part3.root'
]
selection = None
p=PostProcessor(
    ".",
    files,
    cut=selection,
    branchsel=None,
    modules=[
       vvNLOEWKcorrectionWeightProducer('ww'), 
       #qq2vv2lnujjEWKcorrectionsWeightProducer("ww")
    ],  
    postfix='_WWnloEWKw',
    provenance=True,
    fwkJobReport=True
)
p.run()
print "DONE" 


