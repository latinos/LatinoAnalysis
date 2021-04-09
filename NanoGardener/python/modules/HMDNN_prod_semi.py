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

class ApplyDNN_Production_Semi(Module):
    def __init__(self, branch_map=''):
        cmssw_base = os.getenv('CMSSW_BASE')
        self.pathtotraining = cmssw_base + "/src/LatinoAnalysis/NanoGardener/python/data/HM_DNN/Prod_Semilep/"
        self._branch_map = branch_map

    def beginJob(self):
        pass

    def endJob(self):
        pass

    def beginFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        self.classifiers = []
        self.preprocessing = []
        for c, p in zip(["best_model_1.hdf5","best_model_0.hdf5"], ["fold0_keras_preprocessing_productionsemi.pickle","fold1_keras_preprocessing_productionsemi.pickle"]):
          self.classifiers.append(load_model(self.pathtotraining+c))
          self.preprocessing.append(pickle.load(open(self.pathtotraining+p, "rb")))

        suffix = "" if self._branch_map=="" else "_"+self._branch_map
        self.out = mappedOutputTree(wrappedOutputTree, suffix=suffix)
        self.out.branch("DNN_isVBF", "F")


    def endFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        pass

    def analyze(self, event):
        """process event, return True (go to next module) or False (fail, go to next event)"""

        event = mappedEvent(event, mapname=self._branch_map)

        values = []
        ev = event.event

        njet30 = 0
        jetidx = [-1, -1, -1, -1]
        for alpha in range(int(self.GetValue(event, "nCleanJet"))):
          if self.GetValue(event, "CleanJet_pt["+str(alpha)+"]") >= 30.0:
            njet30 += 1
          else:
            break

        withindex = "[0]" # There was a case once where the entries in a sample weren't a list, for some reason
        try:
          wpt = self.GetValue(event, "HM_CleanFatJetPassMBoosted_pt"+withindex)
          ValidEntry=True
        except IndexError:
          ValidEntry=False
        except TypeError:
          withindex = ''

        if self.GetValue(event, "HM_nCleanFatJetPassMBoosted") >= 1 and ValidEntry: # Boosted
          wpt = self.GetValue(event, "HM_CleanFatJetPassMBoosted_pt"+withindex)
          weta = self.GetValue(event, "HM_CleanFatJetPassMBoosted_eta"+withindex)
          wphi = self.GetValue(event, "HM_CleanFatJetPassMBoosted_phi"+withindex)
          wmass = self.GetValue(event, "HM_CleanFatJetPassMBoosted_mass"+withindex)
          WWmass = self.GetValue(event, "HM_CleanFatJetPassMBoosted_HlnFat_mass"+withindex)

          wr1pt = 0.0
          wr1eta = 0.0
          wr1phi = 0.0
          wr1mass = 0.0
          wr2pt = 0.0
          wr2eta = 0.0
          wr2phi = 0.0
          wr2mass = 0.0

          for i in range(int(self.GetValue(event, "nCleanJet"))):
            if i==4: break
            jetidx[i] = i

        elif int(self.GetValue(event, "HM_idx_j1")) != -1: # Resolved
          wpt = self.GetValue(event, "HM_Whad_pt")
          weta = self.GetValue(event, "HM_Whad_eta")
          wphi = self.GetValue(event, "HM_Whad_phi")
          wmass = self.GetValue(event, "HM_Whad_mass")
          WWmass = self.GetValue(event, "HM_Hlnjj_mass")
          nojet = [int(self.GetValue(event, "HM_idx_j1")), int(self.GetValue(event, "HM_idx_j2"))]

          wr1pt = self.GetValue(event, "CleanJet_pt["+str(nojet[0])+"]")
          wr1eta = self.GetValue(event, "CleanJet_eta["+str(nojet[0])+"]")
          wr1phi = self.GetValue(event, "CleanJet_phi["+str(nojet[0])+"]")
          wr1mass = self.GetValue(event, "Jet_mass["+str(int(self.GetValue(event, "CleanJet_jetIdx["+str(nojet[0])+"]")))+"]")
          wr2pt = self.GetValue(event, "CleanJet_pt["+str(nojet[1])+"]")
          wr2eta = self.GetValue(event, "CleanJet_eta["+str(nojet[1])+"]")
          wr2phi = self.GetValue(event, "CleanJet_phi["+str(nojet[1])+"]")
          wr2mass = self.GetValue(event, "Jet_mass["+str(int(self.GetValue(event, "CleanJet_jetIdx["+str(nojet[1])+"]")))+"]")

          j = 0
          for i in range(int(self.GetValue(event, "nCleanJet"))):
            if i in nojet: continue
            jetidx[j] = i
            j += 1
            if j==4: break

        else: # Neither boosted nor resolved: Event not selected
          self.out.fillBranch("DNN_isVBF", 0.0)
          return True

        if jetidx[0] != -1:
          jetpt1 = self.GetValue(event, "CleanJet_pt["+str(jetidx[0])+"]")
          jeteta1 = self.GetValue(event, "CleanJet_eta["+str(jetidx[0])+"]")
          jetphi1 = self.GetValue(event, "CleanJet_phi["+str(jetidx[0])+"]")
          jetmass1 = self.GetValue(event, "Jet_mass["+str(int(self.GetValue(event, "CleanJet_jetIdx["+str(jetidx[0])+"]")))+"]")
          LorJ1 = ROOT.TLorentzVector()
          LorJ1.SetPtEtaPhiM(jetpt1, jeteta1, jetphi1, jetmass1)
        else:
          jetpt1 = 0.0
          jeteta1 = 0.0
          jetphi1 = 0.0
          jetmass1 = 0.0
        if jetidx[1] != -1:
          jetpt2 = self.GetValue(event, "CleanJet_pt["+str(jetidx[1])+"]")
          jeteta2 = self.GetValue(event, "CleanJet_eta["+str(jetidx[1])+"]")
          jetphi2 = self.GetValue(event, "CleanJet_phi["+str(jetidx[1])+"]")
          jetmass2 = self.GetValue(event, "Jet_mass["+str(int(self.GetValue(event, "CleanJet_jetIdx["+str(jetidx[1])+"]")))+"]")
          LorJ2 = ROOT.TLorentzVector()
          LorJ2.SetPtEtaPhiM(jetpt2, jeteta2, jetphi2, jetmass2)
          mjj_12 = (LorJ1+LorJ2).M()
          detajj_12 = abs(LorJ1.Eta()-LorJ2.Eta())
        else:
          jetpt2 = 0.0
          jeteta2 = 0.0
          jetphi2 = 0.0
          jetmass2 = 0.0
          mjj_12 = 0.0
          detajj_12 = 0.0
        if jetidx[2] != -1:
          jetpt3 = self.GetValue(event, "CleanJet_pt["+str(jetidx[2])+"]")
          jeteta3 = self.GetValue(event, "CleanJet_eta["+str(jetidx[2])+"]")
          jetphi3 = self.GetValue(event, "CleanJet_phi["+str(jetidx[2])+"]")
          jetmass3 = self.GetValue(event, "Jet_mass["+str(int(self.GetValue(event, "CleanJet_jetIdx["+str(jetidx[2])+"]")))+"]")
          LorJ3 = ROOT.TLorentzVector()
          LorJ3.SetPtEtaPhiM(jetpt3, jeteta3, jetphi3, jetmass3)
          mjj_13 = (LorJ1+LorJ3).M()
          detajj_13 = abs(LorJ1.Eta()-LorJ3.Eta())
          mjj_23 = (LorJ2+LorJ3).M()
          detajj_23 = abs(LorJ2.Eta()-LorJ3.Eta())
        else:
          jetpt3 = 0.0
          jeteta3 = 0.0
          jetphi3 = 0.0
          jetmass3 = 0.0
          mjj_13 = 0.0
          detajj_13 = 0.0
          mjj_23 = 0.0
          detajj_23 = 0.0
        if jetidx[3] != -1:
          jetpt4 = self.GetValue(event, "CleanJet_pt["+str(jetidx[3])+"]")
          jeteta4 = self.GetValue(event, "CleanJet_eta["+str(jetidx[3])+"]")
          jetphi4 = self.GetValue(event, "CleanJet_phi["+str(jetidx[3])+"]")
          jetmass4 = self.GetValue(event, "Jet_mass["+str(int(self.GetValue(event, "CleanJet_jetIdx["+str(jetidx[3])+"]")))+"]")
          LorJ4 = ROOT.TLorentzVector()
          LorJ4.SetPtEtaPhiM(jetpt4, jeteta4, jetphi4, jetmass4)
          mjj_14 = (LorJ1+LorJ4).M()
          detajj_14 = abs(LorJ1.Eta()-LorJ4.Eta())
          mjj_24 = (LorJ2+LorJ4).M()
          detajj_24 = abs(LorJ2.Eta()-LorJ4.Eta())
          mjj_34 = (LorJ3+LorJ4).M()
          detajj_34 = abs(LorJ3.Eta()-LorJ4.Eta())
        else:
          jetpt4 = 0.0
          jeteta4 = 0.0
          jetphi4 = 0.0
          jetmass4 = 0.0
          mjj_14 = 0.0
          detajj_14 = 0.0
          mjj_24 = 0.0
          detajj_24 = 0.0
          mjj_34 = 0.0
          detajj_34 = 0.0

        values.append(self.GetValue(event, "Lepton_pt[0]") * math.cos(self.GetValue(event, "Lepton_phi[0]")))
        values.append(self.GetValue(event, "Lepton_pt[0]") * math.sin(self.GetValue(event, "Lepton_phi[0]")))
        values.append(self.GetValue(event, "Lepton_pt[0]") * math.sinh(self.GetValue(event, "Lepton_eta[0]")))

        values.append(jetpt1 * math.cos(jetphi1))
        values.append(jetpt1 * math.sin(jetphi1))
        values.append(jetpt1 * math.sinh(jeteta1))
        values.append(jetmass1)
        values.append(jetpt2 * math.cos(jetphi2))
        values.append(jetpt2 * math.sin(jetphi2))
        values.append(jetpt2 * math.sinh(jeteta2))
        values.append(jetmass2)
        values.append(jetpt3 * math.cos(jetphi3))
        values.append(jetpt3 * math.sin(jetphi3))
        values.append(jetpt3 * math.sinh(jeteta3))
        values.append(jetmass3)
        values.append(jetpt4 * math.cos(jetphi4))
        values.append(jetpt4 * math.sin(jetphi4))
        values.append(jetpt4 * math.sinh(jeteta4))
        values.append(jetmass4)

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
        values.append(wr1mass)
        values.append(wr2pt * math.cos(wr2phi))
        values.append(wr2pt * math.sin(wr2phi))
        values.append(wr2pt * math.sinh(wr2eta))
        values.append(wr2mass)

        values.append(self.GetValue(event, "PuppiMET_pt") * math.cos(self.GetValue(event, "PuppiMET_phi")))
        values.append(self.GetValue(event, "PuppiMET_pt") * math.sin(self.GetValue(event, "PuppiMET_phi")))
        values.append(self.GetValue(event, "nCleanJet"))
        values.append(njet30)
        values.append(self.GetValue(event, "HM_largest_nonW_mjj"))
        values.append(WWmass)

        values.append(mjj_12)
        values.append(detajj_12)
        values.append(mjj_13)
        values.append(detajj_13)
        values.append(mjj_14)
        values.append(detajj_14)
        values.append(mjj_23)
        values.append(detajj_23)
        values.append(mjj_24)
        values.append(detajj_24)
        values.append(mjj_34)
        values.append(detajj_34)


        values_stacked = np.hstack(values).reshape(1, len(values))
        values_preprocessed = self.preprocessing[ev % 2].transform(values_stacked)
        response = self.classifiers[ev % 2].predict(values_preprocessed)
        response = np.squeeze(response)

        self.out.fillBranch("DNN_isVBF", response[0])

        return True

    def GetValue(self, event, variable):
        return eval("event."+variable)

