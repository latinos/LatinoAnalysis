#       _                           _____              _                                   _   
#      | |                         |_   _|            | |                                 | |  
#      | |      ___  _ __    _ __    | |    ___   ___ | |  _   _  _ __    ___   ___  _ __ | |_ 
#      | |     / _ \| '_ \  | '_ \   | |   / __| / __|| | | | | || '_ \  / __| / _ \| '__|| __|
#      | |____|  __/| |_) | | |_) |  | |   \__ \| (__ | | | |_| || | | || (__ |  __/| |   | |_ 
#      \_____/ \___|| .__/  | .__/   \_/   |___/ \___||_|  \__,_||_| |_| \___| \___||_|    \__|
#                   | |     | |                                                                
#                   |_|     |_|                                                                
#      
#      


import ROOT
ROOT.PyConfig.IgnoreCommandLineOptions = True

from PhysicsTools.NanoAODTools.postprocessing.framework.datamodel import Collection
from PhysicsTools.NanoAODTools.postprocessing.framework.datamodel import Object
from PhysicsTools.NanoAODTools.postprocessing.framework.eventloop import Module
from PhysicsTools.NanoAODTools.postprocessing.modules.common.collectionMerger import collectionMerger
from LatinoAnalysis.NanoGardener.data.LeptonMaker_cfg import Lepton_br, Lepton_var 

import os.path

class LeppTScalerTreeMaker(Module) :
    def __init__(self, kind="Up", lepFlavor="ele") :
        cmssw_base = os.getenv('CMSSW_BASE')
        self.kind = kind # "Up" or "Dn"
        self.lepFlavor = lepFlavor # "ele" or "mu"
        leppTscaler = {}
        # TODO Example file only, for Full2016 analysis:
        ScaleFactorFile = cmssw_base+'/src/LatinoAnalysis/Gardener/python/data/lepton_scale_n_smear/leppTscaler_'+lepFlavor[:2]+'_80_remAOD.py'
        if os.path.exists(ScaleFactorFile):
          handle = open(ScaleFactorFile,'r')
          exec(handle)
          handle.close()
        self.leppTscaler = leppTscaler

    def beginJob(self):
        pass

    def endJob(self):
        pass

    def beginFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        self.out = wrappedOutputTree
        self.metVariables = [ 'metPfType1', 'metPfType1Phi' ]
        for nameBranches in self.metVariables :
            self.out.branch(nameBranches  ,  "F")
        if 'instance' not in Lepton_var: Lepton_var.append('instance')
        for typ in Lepton_br:
            for var in Lepton_br[typ]:
                if 'Lepton_' in var: self.out.branch(var, typ, lenVar='nLepton')

    def endFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        pass

    def FixAngle(self, phi) :
        if phi < -ROOT.TMath.Pi() :
            phi += 2*ROOT.TMath.Pi()
        elif phi > ROOT.TMath.Pi() :
            phi -= 2*ROOT.TMath.Pi()
        return phi

    def getScale (self, kindLep, pt, eta):

        # fix underflow and overflow
        self.minpt = 0.0
        self.maxpt = 200.0
        self.maxeta = 2.5

        if pt < self.minpt: pt = self.minpt
        if pt > self.maxpt: pt = self.maxpt - 0.000001
        if eta < 0: eta = -1 * eta
        if eta > self.maxeta: eta = self.maxeta - 0.000001
        
        if kindLep in self.leppTscaler.keys() : 
            # get the scale values in bins of pT and eta
            for point in self.leppTscaler[kindLep] :
                if (pt >= point[0][0] and pt < point[0][1] and eta >= point[1][0] and eta < point[1][1]) :
                    return point[2]
            # default ... it should never happen!
            print "WARNING: Did not find scale factor for pt =",pt,"and eta =",eta,"; using 1.0 as default"
            return 1.0
           
        else:
            return 1.0

    def analyze(self, event):
        """process event, return True (go to next module) or False (fail, go to next event)"""

        newmetmodule = -1
        newmetphi = -1

        if self.kind == 'Up':
            self.variation = 1.0
        elif self.kind == 'Dn' or self.kind == 'Down':
            self.variation = -1.0

        leptons = Collection(event,"Lepton")
        met = Object(event, "MET")
        nLep = getattr(event, "nLepton")

        lep_dict = {}
        for var in Lepton_var:
            lep_dict[var] = [0]*nLep

        # MET
        if self.lepFlavor == 'ele':
            newmetmodule = met.pt * (1 + (self.variation * self.getScale('ele', met.pt, 0.0) / 100.0))
            #newmetphi = self.FixAngle(met.phi + self.FixAngle( itree.metPfRawPhiElecEnUp - getattr(event, "RawMET_phi") )) # TODO: About finding a way to express the old "itree.metPfRawPhiElecEnUp" with nanoAOD variables: How does applying a factor to met.pt affect RawMET_phi?
            newmetphi = met.phi #temporary
        elif self.lepFlavor == 'mu':
            newmetmodule = met.pt * (1 + (self.variation * self.getScale('mu', met.pt, 0.0) / 100.0))
            #newmetphi = self.FixAngle(met.phi + self.FixAngle( itree.metPfRawPhiMuEnUp - getattr(event, "RawMET_phi") )) # TODO: About finding a way to express the old "itree.metPfRawPhiMuEnUp" with nanoAOD variables: How does applying a factor to met.pt affect RawMET_phi?
            newmetphi = met.phi #temporary

        # Leptons
        for idx,lep in enumerate(leptons):
            if self.lepFlavor == 'ele' and abs(lep.pdgId) == 11:
                lep.pt = lep.pt * (1 + (self.variation * self.getScale('ele', lep.pt, lep.eta) / 100.0))
            elif self.lepFlavor == 'mu' and abs(lep.pdgId) == 13:
                lep.pt = lep.pt * (1 + (self.variation * self.getScale('mu', lep.pt, lep.eta) / 100.0))

        # Re-order lepton collection
        for idx,lep in enumerate(leptons):
            pt_idx = 0
            for idx2,lep2 in enumerate(leptons):
                if idx == idx2: continue
                if lep.pt < lep2.pt: pt_idx += 1
            for var in Lepton_var:
                if 'pt' in var:
                    lep_dict[var][pt_idx] = lep.pt
                elif 'instance' in var and not hasattr(event, 'Lepton_'+var):
                    lep_dict[var][pt_idx] = idx
                else:
                    lep_dict[var][pt_idx] = getattr(event, 'Lepton_'+var)[idx]

        self.out.fillBranch("metPfType1", newmetmodule)
        self.out.fillBranch("metPfType1Phi", newmetphi)
        for var in lep_dict:
            self.out.fillBranch('Lepton_' + var, lep_dict[var])

        return True

