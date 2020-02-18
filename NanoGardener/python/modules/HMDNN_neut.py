import ROOT
ROOT.PyConfig.IgnoreCommandLineOptions = True
import re
import os
import numpy as np
from keras.models import load_model
import pickle
import math

from PhysicsTools.NanoAODTools.postprocessing.framework.eventloop import Module

class ApplyDNN_Neutrino(Module):
    def __init__(self):
        cmssw_base = os.getenv('CMSSW_BASE')
        self.pathtotraining = cmssw_base + "/src/LatinoAnalysis/NanoGardener/python/data/HM_DNN/Neutrino/"

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

        self.out = wrappedOutputTree
        self.out.branch("DNNneutrino_pt", "F", 2)
        self.out.branch("DNNneutrino_phi", "F", 2)
        self.out.branch("DNNneutrino_eta", "F", 2)
        self.out.branch("DNN_mtw1", "F")
        self.out.branch("DNN_mtw2", "F")
        self.out.branch("DNN_mth", "F")


    def endFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        pass

    def analyze(self, event):
        """process event, return True (go to next module) or False (fail, go to next event)"""

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

        values_stacked = np.hstack(values).reshape(1, len(values))
        values_preprocessed = self.preprocessing[ev % 2].transform(values_stacked)
        response = self.classifiers[ev % 2].predict(values_preprocessed)
        response = np.squeeze(response)

        Npt = []
        Nphi = []
        Neta = []

        Npt.append(math.sqrt(response[0]**2 + response[1]**2))
        costheta = response[2]/math.sqrt(response[0]**2 + response[1]**2 + response[2]**2)
        Neta.append(-0.5* math.log( (1.0-costheta)/(1.0+costheta) ))
        Nphi.append(math.atan2(response[1], response[0]))

        Npt.append(math.sqrt(response[3]**2 + response[4]**2))
        costheta = response[5]/math.sqrt(response[3]**2 + response[4]**2 + response[5]**2)
        Neta.append(-0.5* math.log( (1.0-costheta)/(1.0+costheta) ))
        Nphi.append(math.atan2(response[4], response[3]))

        l1 = ROOT.TLorentzVector()
        l1.SetPtEtaPhiM(self.GetValue(event, "Lepton_pt[0]"),self.GetValue(event, "Lepton_eta[0]"),self.GetValue(event, "Lepton_phi[0]"),0)
        l2 = ROOT.TLorentzVector()
        l2.SetPtEtaPhiM(self.GetValue(event, "Lepton_pt[1]"),self.GetValue(event, "Lepton_eta[1]"),self.GetValue(event, "Lepton_phi[1]"),0)
        np1 = ROOT.TLorentzVector()
        np1.SetXYZM(response[0],response[1],response[2],0)
        np2 = ROOT.TLorentzVector()
        np2.SetXYZM(response[3],response[4],response[5],0)
        mtw1 = (l1+np1).M()
        mtw2 = (l2+np2).M()
        mth = ((l1+np1)+(l2+np2)).M()

        self.out.fillBranch("DNNneutrino_pt", Npt)
        self.out.fillBranch("DNNneutrino_eta", Neta)
        self.out.fillBranch("DNNneutrino_phi", Nphi)
        self.out.fillBranch("DNN_mtw1", mtw1)
        self.out.fillBranch("DNN_mtw2", mtw2)
        self.out.fillBranch("DNN_mth", mth)

        return True

    def GetValue(self, event, variable):
        return eval("event."+variable)

