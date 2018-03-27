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
    def __init__(self) :
        cmssw_base = os.getenv('CMSSW_BASE')

    def beginJob(self):
        pass

    def endJob(self):
        pass

    def beginFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        self.out = wrappedOutputTree
        self.metVariables = [ 'metPfType1', 'metPfType1Phi' ]
        for nameBranches in self.metVariables :
          self.out.branch(nameBranches  ,  "F");

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

        met_px_UnclEnUp  = met_px + getattr(event, "MET_MetUnclustEnUpDeltaX")
        met_py_UnclEnUp  = met_py + getattr(event, "MET_MetUnclustEnUpDeltaY")
        met_pt_UnclEnUp  = math.sqrt(met_px_UnclEnUp**2 + met_py_UnclEnUp**2)
        met_phi_UnclEnUp = math.atan2(met_py_UnclEnUp, met_px_UnclEnUp)
        newmet_phi_UnclEnUp = self.FixAngle(met.phi + self.FixAngle( met_phi_UnclEnUp - getattr(event, "RawMET_phi") ))

        met_px_UnclEnDn  = met_px - getattr(event, "MET_MetUnclustEnUpDeltaX")
        met_py_UnclEnDn  = met_py - getattr(event, "MET_MetUnclustEnUpDeltaY")
        met_pt_UnclEnDn  = math.sqrt(met_px_UnclEnDn**2 + met_py_UnclEnDn**2)
        met_phi_UnclEnDn = math.atan2(met_py_UnclEnDn, met_px_UnclEnDn)
        newmet_phi_UnclEnDn = self.FixAngle(met.phi + self.FixAngle( met_phi_UnclEnDn - getattr(event, "RawMET_phi") ))

        #TODO: When/How do you use Up or Down?
        if True: #self.kind == 'Up':
            newmetmodule = met_pt_UnclEnUp
            newmetphi = newmet_phi_UnclEnUp

        else: #elif self.kind == 'Dn':
            newmetmodule = met_pt_UnclEnDn
            newmetphi = newmet_phi_UnclEnDn

        self.out.fillBranch("metPfType1", newmetmodule)
        self.out.fillBranch("metPfType1Phi", newmetphi)

        return True

