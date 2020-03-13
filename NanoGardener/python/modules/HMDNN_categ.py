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

class ApplyDNN_Category(Module):
    def __init__(self, branch_map=''):
        cmssw_base = os.getenv('CMSSW_BASE')
        self.pathtotraining = cmssw_base + "/src/LatinoAnalysis/NanoGardener/python/data/HM_DNN/Categ/"
        self._branch_map = branch_map

    def beginJob(self):
        pass

    def endJob(self):
        pass

    def beginFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        self.classifiers = []
        self.preprocessing = []
        for c, p in zip(["best_model_1.hdf5","best_model_0.hdf5"], ["fold0_keras_preprocessing_category.pickle","fold1_keras_preprocessing_category.pickle"]):
          self.classifiers.append(load_model(self.pathtotraining+c))
          self.preprocessing.append(pickle.load(open(self.pathtotraining+p, "rb")))

        self.out = mappedOutputTree(wrappedOutputTree, suffix= "_"+self._suffix)
        self.classes = ["WW", "ggH115_190", "ggH200_450", "ggH500_5000", "VBF115_190", "VBF200_450", "VBF500_5000", "other"]
        for cla in self.classes:
          self.out.branch("DNN_"+cla, "F")
        self.out.branch("DNN_categ", "I")
        self.out.branch("DNN_categ_maxscore", "I")
        self.out.branch("DNN_categ_difftosecond", "I")


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
        values.append(self.GetValue(event, "nCleanJet"))
        values.append(self.GetValue(event, "detajj"))
        values.append(self.GetValue(event, "dphill"))
        values.append(self.GetValue(event, "drll"))
        values.append(self.GetValue(event, "dphilmet"))
        values.append(self.GetValue(event, "dphilmet1"))
        values.append(self.GetValue(event, "dphilmet2"))
        values.append(self.GetValue(event, "mjj"))
        values.append(self.GetValue(event, "mll"))
        values.append(self.GetValue(event, "mTi"))
        values.append(self.GetValue(event, "mth"))
        values.append(self.GetValue(event, "ht"))
        values.append(self.GetValue(event, "mtw1"))
        values.append(self.GetValue(event, "mtw2"))
        values.append(self.GetValue(event, "ptll"))
        values.append(self.GetValue(event, "mcoll"))
        values.append(self.GetValue(event, "mcollWW"))
        values.append(self.GetValue(event, "vht_pt") * math.cos(self.GetValue(event, "vht_phi")))
        values.append(self.GetValue(event, "vht_pt") * math.sin(self.GetValue(event, "vht_phi")))


        if ev%64 < 32:
          intothisfold=0
        else:
          intothisfold=1
        values_stacked = np.hstack(values).reshape(1, len(values))
        values_preprocessed = self.preprocessing[intothisfold].transform(values_stacked)
        response = self.classifiers[intothisfold].predict(values_preprocessed)
        response = np.squeeze(response)

        maxscore = 0
        secondmax = 0
        for i, r in enumerate(response):
          self.out.fillBranch("DNN_"+self.classes[i], r)
          if r > maxscore:
            secondmax = maxscore
            maxscore = r
            maxindex = i
          elif r > secondmax:
            secondmax = r

        self.out.fillBranch("DNN_categ", maxindex)
        self.out.fillBranch("DNN_categ_maxscore", maxscore)
        self.out.fillBranch("DNN_categ_difftosecond", maxscore-secondmax)

        return True

    def GetValue(self, event, variable):
        return eval("event."+variable)

