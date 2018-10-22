import ROOT
ROOT.PyConfig.IgnoreCommandLineOptions = True
import re
import os

from PhysicsTools.NanoAODTools.postprocessing.framework.datamodel import Collection 
from PhysicsTools.NanoAODTools.postprocessing.framework.eventloop import Module

class PrefCorr(Module):
    def __init__(self):
        cmssw_base = os.getenv('CMSSW_BASE')

        self.photon_file = self.open_root(cmssw_base + "/src/LatinoAnalysis/NanoGardener/python/data/prefire_maps/L1prefiring_photon_2017BtoF.root")# TODO PRELIMINARY MAP
        self.photon_map = self.get_root_obj(self.photon_file, "L1prefiring_photon_2017BtoF")

        self.jet_file = self.open_root(cmssw_base + "/src/LatinoAnalysis/NanoGardener/python/data/prefire_maps/L1prefiring_jet_2017BtoF.root")# TODO PRELIMINARY MAP
        self.jet_map = self.get_root_obj(self.jet_file, "L1prefiring_jet_2017BtoF")

    def open_root(self, path):
        r_file = ROOT.TFile.Open(path)
        if not r_file.__nonzero__() or not r_file.IsOpen(): raise NameError('File ' + path + ' not open')
        return r_file

    def get_root_obj(self, root_file, obj_name):
        r_obj = root_file.Get(obj_name)
        if not r_obj.__nonzero__(): raise NameError('Root Object ' + obj_name + ' not found')
        return r_obj

    def beginJob(self):
        pass

    def endJob(self):
        pass

    def beginFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        self.out = wrappedOutputTree
        self.out.branch("PrefireWeight", "F")

    def endFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        pass

    def analyze(self, event):
        """process event, return True (go to next module) or False (fail, go to next event)"""

        photons = Collection(event,"Photon")
        electrons = Collection(event,"Electron")
        jets = Collection(event,"Jet")
        prefw = 1.0
        JetIsEG = []

        # Options
        UseEMpT = 0 # Set to 1 if the jet map is defined for energy deposited in ECAL (pT_EM vs pT). For jet map only, not photon!

        for pho in photons: # All photons. Should be only isolated photons?
          JetIsEG.append(pho.jetIdx)
          if pho.pt > 20 and abs(pho.eta) < 3.25 and abs(pho.eta) > 2: # <- Values may need to be fixed for new maps
            prefw *= 1-self.photon_map.GetBinContent(self.photon_map.FindBin(pho.eta, min(pho.pt, 500)))

        for ele in electrons:
          if ele.jetIdx in JetIsEG: continue
          JetIsEG.append(ele.jetIdx)
          if ele.pt > 20 and abs(ele.eta) < 3.25 and abs(ele.eta) > 2: # <- Values may need to be fixed for new maps
            prefw *= 1-self.photon_map.GetBinContent(self.photon_map.FindBin(ele.eta, min(ele.pt, 500)))

        for jid,jet in enumerate(jets):
          jetpt = jet.pt
          if UseEMpT: jetpt *= (jet.chEmEF + jet.neEmEF)
          if jetpt > 40 and abs(jet.eta) < 3.25 and abs(jet.eta) > 2 and (jid not in JetIsEG): # <- Values may need to be fixed for new maps
            prefw *= 1-self.jet_map.GetBinContent(self.jet_map.FindBin(jet.eta, min(jetpt, 500)))

        self.out.fillBranch("PrefireWeight", prefw)

        return True

