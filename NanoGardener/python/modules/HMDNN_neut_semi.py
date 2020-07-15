import ROOT
ROOT.PyConfig.IgnoreCommandLineOptions = True
import re
import os
import numpy as np
from keras.models import load_model
import pickle
import math

from PhysicsTools.NanoAODTools.postprocessing.framework.eventloop import Module
from LatinoAnalysis.NanoGardener.framework.BranchMapping import mappedOutputTree, mappedEvent

class ApplyDNN_Neutrino_Semi(Module):
    def __init__(self, branch_map=''):
        cmssw_base = os.getenv('CMSSW_BASE')
        self.pathtotraining = cmssw_base + "/src/LatinoAnalysis/NanoGardener/python/data/HM_DNN/Neutrino_Semilep/"
        self._branch_map = branch_map

    def beginJob(self):
        pass

    def endJob(self):
        pass

    def beginFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        self.classifiers = []
        self.preprocessing = []
        for c, p in zip(["best_model_1.hdf5","best_model_0.hdf5"], ["fold0_keras_preprocessing_neutrinosemi.pickle","fold1_keras_preprocessing_neutrinosemi.pickle"]):
          self.classifiers.append(load_model(self.pathtotraining+c))
          self.preprocessing.append(pickle.load(open(self.pathtotraining+p, "rb")))

        suffix = "" if self._branch_map=="" else "_"+self._branch_map
        self.out = mappedOutputTree(wrappedOutputTree, suffix=suffix)
        self.out.branch("DNN_mth", "F")


    def endFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        pass

    def analyze(self, event):
        """process event, return True (go to next module) or False (fail, go to next event)"""

        event = mappedEvent(event, mapname=self._branch_map)

        try:
          wpt = self.GetValue(event, "HM_CleanFatJetPassMBoosted_pt[0]")
          ValidEntry=True
        except IndexError:
          ValidEntry=False
        if self.GetValue(event, "HM_nCleanFatJetPassMBoosted") >= 1 and ValidEntry:
          weta = self.GetValue(event, "HM_CleanFatJetPassMBoosted_eta[0]")
          wphi = self.GetValue(event, "HM_CleanFatJetPassMBoosted_phi[0]")
          wmass = self.GetValue(event, "HM_CleanFatJetPassMBoosted_mass[0]")
          WWmass = self.GetValue(event, "HM_CleanFatJetPassMBoosted_HlnFat_mass[0]")
          wptmww = self.GetValue(event, "HM_CleanFatJetPassMBoosted_WptOvHfatM[0]")
          tau21 = self.GetValue(event, "HM_CleanFatJetPassMBoosted_tau21[0]")

          wr1pt = 0.0
          wr1eta = 0.0
          wr1phi = 0.0
          wr2pt = 0.0
          wr2eta = 0.0
          wr2phi = 0.0


          jetidx1 = 0
          jetidx2 = 1
        else:
          wpt = self.GetValue(event, "HM_Whad_pt")
          weta = self.GetValue(event, "HM_Whad_eta")
          wphi = self.GetValue(event, "HM_Whad_phi")
          wmass = self.GetValue(event, "HM_Whad_mass")
          WWmass = self.GetValue(event, "HM_Hlnjj_mass")
          wptmww = self.GetValue(event, "HM_WptOvHak4M")
          tau21 = 0.0

          nojet = [int(self.GetValue(event, "HM_idx_j1")), int(self.GetValue(event, "HM_idx_j2"))]
          if -1 in nojet: # Events has less than 2 jets and shouldn't be considered anyway
            self.out.fillBranch("DNN_isVBF", 0.0)
            return True

          wr1pt = self.GetValue(event, "CleanJet_pt["+str(nojet[0])+"]")
          wr1eta = self.GetValue(event, "CleanJet_eta["+str(nojet[0])+"]")
          wr1phi = self.GetValue(event, "CleanJet_phi["+str(nojet[0])+"]")
          wr2pt = self.GetValue(event, "CleanJet_pt["+str(nojet[1])+"]")
          wr2eta = self.GetValue(event, "CleanJet_eta["+str(nojet[1])+"]")
          wr2phi = self.GetValue(event, "CleanJet_phi["+str(nojet[1])+"]")

          goodjet = [alpha for alpha in range(4) if alpha not in nojet]
          jetidx1 = goodjet[0]
          jetidx2 = goodjet[1]

        if self.GetValue(event, "nCleanJet")>=1+jetidx1:
          jetpt1 = self.GetValue(event, "CleanJet_pt["+str(jetidx1)+"]")
          jeteta1 = self.GetValue(event, "CleanJet_eta["+str(jetidx1)+"]")
          jetphi1 = self.GetValue(event, "CleanJet_phi["+str(jetidx1)+"]")
        else:
          jetpt1 = 0.0
          jeteta1 = 0.0
          jetphi1 = 0.0
        if self.GetValue(event, "nCleanJet")>=1+jetidx2:
          jetpt2 = self.GetValue(event, "CleanJet_pt["+str(jetidx2)+"]")
          jeteta2 = self.GetValue(event, "CleanJet_eta["+str(jetidx2)+"]")
          jetphi2 = self.GetValue(event, "CleanJet_phi["+str(jetidx2)+"]")
        else:
          jetpt2 = 0.0
          jeteta2 = 0.0
          jetphi2 = 0.0

        #if jetidx1==0 and jetidx2==1:
        #  mjj = self.GetValue(event, "mjj")
        #  detajj = self.GetValue(event, "detajj")
        if self.GetValue(event, "nCleanJet")>=1+jetidx2:
          J1 = ROOT.TLorentzVector()
          J2 = ROOT.TLorentzVector()
          J1.SetPtEtaPhiM(self.GetValue(event, "CleanJet_pt["+str(jetidx1)+"]"), self.GetValue(event, "CleanJet_eta["+str(jetidx1)+"]"), self.GetValue(event, "CleanJet_phi["+str(jetidx1)+"]"), self.GetValue(event, "Jet_mass[event.CleanJet_jetIdx["+str(jetidx1)+"]]"))
          J2.SetPtEtaPhiM(self.GetValue(event, "CleanJet_pt["+str(jetidx2)+"]"), self.GetValue(event, "CleanJet_eta["+str(jetidx2)+"]"), self.GetValue(event, "CleanJet_phi["+str(jetidx2)+"]"), self.GetValue(event, "Jet_mass[event.CleanJet_jetIdx["+str(jetidx2)+"]]"))
          mjj = (J1+J2).M()
          detajj = abs(J1.Eta()-J2.Eta())
        else:
          mjj = -9999.0
          detajj = -9999.0

        values = []
        ev = event.event

        values.append(self.GetValue(event, "Lepton_pt[0]") * math.cos(self.GetValue(event, "Lepton_phi[0]")))
        values.append(self.GetValue(event, "Lepton_pt[0]") * math.sin(self.GetValue(event, "Lepton_phi[0]")))
        values.append(self.GetValue(event, "Lepton_pt[0]") * math.sinh(self.GetValue(event, "Lepton_eta[0]")))

        values.append(jetpt1 * math.cos(jetphi1))
        values.append(jetpt1 * math.sin(jetphi1))
        values.append(jetpt1 * math.sinh(jeteta1))
        values.append(jetpt2 * math.cos(jetphi2))
        values.append(jetpt2 * math.sin(jetphi2))
        values.append(jetpt2 * math.sinh(jeteta2))

        values.append(wpt * math.cos(wphi))
        values.append(wpt * math.sin(wphi))
        values.append(wpt * math.sinh(weta))
        values.append(wmass)
        values.append(self.GetValue(event, "HM_Wlep_pt_Puppi") * math.cos(self.GetValue(event, "HM_Wlep_phi_Puppi")))
        values.append(self.GetValue(event, "HM_Wlep_pt_Puppi") * math.sin(self.GetValue(event, "HM_Wlep_phi_Puppi")))
        values.append(self.GetValue(event, "HM_Wlep_pt_Puppi") * math.sinh(self.GetValue(event, "HM_Wlep_eta_Puppi")))
        values.append(self.GetValue(event, "HM_Wlep_mass_Puppi"))
        values.append(wr1pt * math.cos(wr1phi))
        values.append(wr1pt * math.sin(wr1phi))
        values.append(wr1pt * math.sinh(wr1eta))
        values.append(wr2pt * math.cos(wr2phi))
        values.append(wr2pt * math.sin(wr2phi))
        values.append(wr2pt * math.sinh(wr2eta))

        values.append(self.GetValue(event, "PuppiMET_pt") * math.cos(self.GetValue(event, "PuppiMET_phi")))
        values.append(self.GetValue(event, "PuppiMET_pt") * math.sin(self.GetValue(event, "PuppiMET_phi")))
        values.append(wptmww)
        values.append(tau21)
        values.append(WWmass)


        values_stacked = np.hstack(values).reshape(1, len(values))
        values_preprocessed = self.preprocessing[ev % 2].transform(values_stacked)
        response = self.classifiers[ev % 2].predict(values_preprocessed)
        response = np.squeeze(response)

        self.out.fillBranch("DNN_mth", response)

        return True

    def GetValue(self, event, variable):
        return eval("event."+variable)

