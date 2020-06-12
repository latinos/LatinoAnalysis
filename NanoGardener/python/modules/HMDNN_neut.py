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

class ApplyDNN_Neutrino(Module):
    def __init__(self, branch_map=''):
        cmssw_base = os.getenv('CMSSW_BASE')
        self.pathtotraining = cmssw_base + "/src/LatinoAnalysis/NanoGardener/python/data/HM_DNN/Neutrino/"
        self._branch_map = branch_map

    def beginJob(self):
        pass

    def endJob(self):
        pass

    def beginFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        self.classifiers = []
        self.preprocessing = []
        for c, p in zip(["best_model_1.hdf5","best_model_0.hdf5"], ["fold0_keras_preprocessing_neutrino.pickle","fold1_keras_preprocessing_neutrino.pickle"]):
          self.classifiers.append(load_model(self.pathtotraining+c, custom_objects={'customLoss': self.customLoss}))
          self.preprocessing.append(pickle.load(open(self.pathtotraining+p, "rb")))

        self.out = mappedOutputTree(wrappedOutputTree, suffix= "_"+self._suffix)
        self.out.branch("DNN_mth", "F")


    def endFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        pass

    def analyze(self, event):
        """process event, return True (go to next module) or False (fail, go to next event)"""

        event = mappedEvent(event, mapname=self._branch_map)

        values = []
        ev = event.event

        values.append(self.GetValue(event, "Lepton_pt[0]") * math.cos(self.GetValue(event, "Lepton_phi[0]")))
        values.append(self.GetValue(event, "Lepton_pt[0]") * math.sin(self.GetValue(event, "Lepton_phi[0]")))
        values.append(self.GetValue(event, "Lepton_pt[0]") * math.sinh(self.GetValue(event, "Lepton_eta[0]")))
        values.append(self.GetValue(event, "Lepton_pt[1]") * math.cos(self.GetValue(event, "Lepton_phi[1]")))
        values.append(self.GetValue(event, "Lepton_pt[1]") * math.sin(self.GetValue(event, "Lepton_phi[1]")))
        values.append(self.GetValue(event, "Lepton_pt[1]") * math.sinh(self.GetValue(event, "Lepton_eta[1]")))

        if self.GetValue(event, "nCleanJet")>=1:
          values.append(self.GetValue(event, "CleanJet_pt[0]") * math.cos(self.GetValue(event, "CleanJet_phi[0]")))
          values.append(self.GetValue(event, "CleanJet_pt[0]") * math.sin(self.GetValue(event, "CleanJet_phi[0]")))
          values.append(self.GetValue(event, "CleanJet_pt[0]") * math.sinh(self.GetValue(event, "CleanJet_eta[0]")))
        else:
          values.append(0.0)
          values.append(0.0)
          values.append(0.0)
        if self.GetValue(event, "nCleanJet")>=2:
          values.append(self.GetValue(event, "CleanJet_pt[1]") * math.cos(self.GetValue(event, "CleanJet_phi[1]")))
          values.append(self.GetValue(event, "CleanJet_pt[1]") * math.sin(self.GetValue(event, "CleanJet_phi[1]")))
          values.append(self.GetValue(event, "CleanJet_pt[1]") * math.sinh(self.GetValue(event, "CleanJet_eta[1]")))
        else:
          values.append(0.0)
          values.append(0.0)
          values.append(0.0)

        values.append(self.GetValue(event, "PuppiMET_pt") * math.cos(self.GetValue(event, "PuppiMET_phi")))
        values.append(self.GetValue(event, "PuppiMET_pt") * math.sin(self.GetValue(event, "PuppiMET_phi")))
        values.append(self.GetValue(event, "dphilmet"))
        values.append(self.GetValue(event, "dphilmet1"))
        values.append(self.GetValue(event, "dphilmet2"))
        values.append(self.GetValue(event, "mll"))
        values.append(self.GetValue(event, "mTi"))
        values.append(self.GetValue(event, "mth"))
        values.append(self.GetValue(event, "mtw1"))
        values.append(self.GetValue(event, "mtw2"))
        values.append(self.GetValue(event, "ht"))


        values_stacked = np.hstack(values).reshape(1, len(values))
        values_preprocessed = self.preprocessing[ev % 2].transform(values_stacked)
        response = self.classifiers[ev % 2].predict(values_preprocessed)
        response = np.squeeze(response)

        self.out.fillBranch("DNN_mth", response)

        return True

    def GetValue(self, event, variable):
        return eval("event."+variable)

