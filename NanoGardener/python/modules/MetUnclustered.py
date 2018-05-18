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
    def __init__(self, kind="Up") :
        cmssw_base = os.getenv('CMSSW_BASE')
        self.kind = kind

    def beginJob(self):
        pass

    def endJob(self):
        pass

    def beginFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        self.out = wrappedOutputTree
        self.metVariables = [ 'MET_pt', 'MET_phi' ]
        for nameBranches in self.metVariables :
          self.out.branch(nameBranches  ,  "F")

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

        newmetmodule = -1
        newmetphi = -1

        met = Object(event, "MET")

        met_px = met.pt * math.cos(met.phi)
        met_py = met.pt * math.sin(met.phi)

        if self.kind == 'Up':
            met_px_UnclEnUp  = met_px + getattr(event, "MET_MetUnclustEnUpDeltaX")
            met_py_UnclEnUp  = met_py + getattr(event, "MET_MetUnclustEnUpDeltaY")
            met_pt_UnclEnUp  = math.sqrt(met_px_UnclEnUp**2 + met_py_UnclEnUp**2)
            met_phi_UnclEnUp = math.atan2(met_py_UnclEnUp, met_px_UnclEnUp)
            newmet_phi_UnclEnUp = self.FixAngle(met.phi + self.FixAngle( met_phi_UnclEnUp - getattr(event, "RawMET_phi") ))

            newmetmodule = met_pt_UnclEnUp
            newmetphi = newmet_phi_UnclEnUp

        elif self.kind == 'Dn' or self.kind == 'Down':
            met_px_UnclEnDn  = met_px - getattr(event, "MET_MetUnclustEnUpDeltaX")
            met_py_UnclEnDn  = met_py - getattr(event, "MET_MetUnclustEnUpDeltaY")
            met_pt_UnclEnDn  = math.sqrt(met_px_UnclEnDn**2 + met_py_UnclEnDn**2)
            met_phi_UnclEnDn = math.atan2(met_py_UnclEnDn, met_px_UnclEnDn)
            newmet_phi_UnclEnDn = self.FixAngle(met.phi + self.FixAngle( met_phi_UnclEnDn - getattr(event, "RawMET_phi") ))

            newmetmodule = met_pt_UnclEnDn
            newmetphi = newmet_phi_UnclEnDn

        self.out.fillBranch("MET_pt", newmetmodule)
        self.out.fillBranch("MET_phi", newmetphi)

        return True

