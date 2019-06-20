#  
#     \  |  ____| __ __|                                      |          _)         |          
#    |\/ |  __|      |        |   |  __ \    __|   _ \   __|  __|   _` |  |  __ \   __|  |   | 
#    |   |  |        |        |   |  |   |  (      __/  |     |    (   |  |  |   |  |    |   | 
#   _|  _| _____|   _|       \__,_| _|  _| \___| \___| _|    \__| \__,_| _| _|  _| \__| \__, | 
#                                                                                       ____/  
#  


import ROOT
ROOT.PyConfig.IgnoreCommandLineOptions = True

from PhysicsTools.NanoAODTools.postprocessing.framework.datamodel import Object
from PhysicsTools.NanoAODTools.postprocessing.framework.eventloop import Module

import os.path
import math

class MetUnclusteredTreeMaker(Module) :
    def __init__(self, kind="Up",metCollections=['MET', 'PuppiMET', 'RawMET', 'ChsMET' , 'CaloMET']) :
        self.metCollections = metCollections
        cmssw_base = os.getenv('CMSSW_BASE')
        self.kind = kind

    def beginJob(self):
        pass

    def endJob(self):
        pass

    def beginFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        self.out = wrappedOutputTree
        for x in self.metCollections:
          self.out.branch(x+'_pt', "F")
          self.out.branch(x+'_phi', "F")

    def endFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        pass

    def FixAngle(self, phi) :
        if phi < -ROOT.TMath.Pi() :
            phi += 2*ROOT.TMath.Pi()
        elif phi > ROOT.TMath.Pi() :
            phi -= 2*ROOT.TMath.Pi()
        return phi

    def analyze(self, event):
        """process event, return True (go to next module) or False (fail, go to next event)"""

        metUnclustX = getattr(event, "MET_MetUnclustEnUpDeltaX")
        metUnclustY = getattr(event, "MET_MetUnclustEnUpDeltaY")

        for metType in self.metCollections:
            try:
                met = Object(event, metType)
            except AttributeError:
                continue

            met_px = met.pt * math.cos(met.phi)
            met_py = met.pt * math.sin(met.phi)
            sumEt  = met.sumEt

            if self.kind == 'Up':
                met_px_UnclEn  = met_px + metUnclustX
                met_py_UnclEn  = met_py + metUnclustY

            elif self.kind == 'Dn' or self.kind == 'Down':
                met_px_UnclEn  = met_px - metUnclustX
                met_py_UnclEn  = met_py - metUnclustY

            met_pt_UnclEn  = math.sqrt(met_px_UnclEn**2 + met_py_UnclEn**2)
            met_phi_UnclEn = self.FixAngle(math.atan2(met_py_UnclEn, met_px_UnclEn))

            self.out.fillBranch(metType+"_pt", met_pt_UnclEn)
            self.out.fillBranch(metType+"_phi", met_phi_UnclEn)

        return True

