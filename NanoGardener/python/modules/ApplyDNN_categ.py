import ROOT
ROOT.PyConfig.IgnoreCommandLineOptions = True
import re
import os
import numpy as np
from keras.models import load_model
import pickle
import math

from PhysicsTools.NanoAODTools.postprocessing.framework.eventloop import Module

class ApplyDNN_Category(Module):
    def __init__(self):
        cmssw_base = os.getenv('CMSSW_BASE')
        self.pathtotraining = cmssw_base + "/src/LatinoAnalysis/NanoGardener/python/data/HM_DNN/Categ/"

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

        self.out = wrappedOutputTree
        self.classes = ["WW", "ggH125", "ggH130", "ggH140", "ggH150", "ggH160", "ggH170", "ggH180", "ggH190", "ggH200", "ggH210", "ggH230", "ggH250", "ggH270", "ggH300", "ggH350", "ggH400", "ggH450", "ggH500", "ggH550", "ggH600", "ggH650", "ggH700", "ggH750", "ggH800", "ggH900", "ggH1000", "ggH1500", "ggH2000", "ggH2500", "ggH3000", "ggH4000", "ggH5000", "VBF125", "VBF130", "VBF140", "VBF150", "VBF160", "VBF170", "VBF180", "VBF190", "VBF200", "VBF210", "VBF230", "VBF250", "VBF270", "VBF300", "VBF350", "VBF400", "VBF450", "VBF500", "VBF550", "VBF600", "VBF650", "VBF700", "VBF750", "VBF800", "VBF900", "VBF1000", "VBF1500", "VBF2000", "VBF2500", "VBF3000", "VBF4000", "VBF5000", "other"]
        for cla in self.classes:
          self.out.branch("DNN_"+cla, "F")
        self.out.branch("DNN_categ", "I")
        self.out.branch("DNN_categ_maxscore", "I")
        self.out.branch("DNN_categ_difftosecond", "I")


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
        values.append(self.GetValue(event, "vht_pt")) # values.append(self.GetValue(event, "vht_pt") * math.cos(self.GetValue(event, "vht_phi")))
        values.append(self.GetValue(event, "vht_phi")) # values.append(self.GetValue(event, "vht_pt") * math.sin(self.GetValue(event, "vht_phi")))


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
        self.out.fillBranch("DNN_cat_maxscore", maxscore)
        self.out.fillBranch("DNN_cat_difftosecond", maxscore-secondmax)

        return True

    def GetValue(self, event, variable):
        return eval("event."+variable)

