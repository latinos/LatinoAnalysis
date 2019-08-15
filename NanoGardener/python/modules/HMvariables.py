import ROOT
import math
ROOT.PyConfig.IgnoreCommandLineOptions = True
import re
import os

from PhysicsTools.NanoAODTools.postprocessing.framework.datamodel import Collection 
from PhysicsTools.NanoAODTools.postprocessing.framework.eventloop import Module

class HighMassVariables(Module):
    def __init__(self):
        pass

    def beginJob(self):
        pass

    def endJob(self):
        pass

    def beginFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        self.out = wrappedOutputTree
        self.out.branch("mjjGen", "F")
        self.out.branch("back2back", "F")
        #self.out.branch("mjj_hm", "F")
        #self.out.branch("detajj_hm", "F")
        #self.out.branch("mjjj_hm", "F")
        #self.out.branch("detajjj_hm", "F")

    def endFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        pass

    def analyze(self, event):
        """process event, return True (go to next module) or False (fail, go to next event)"""

        njets = getattr(event, "nCleanJet")
        jets = Collection(event, "CleanJet")
        norigjets = getattr(event, "nJet")
        origjets = Collection(event, "Jet")
        ngenjets = getattr(event, "nGenJet")
        genjets = Collection(event, "GenJet")

        # Getting mjjGen is easier here than it was in HIG-17-033, because we already have a lepton-cleaned jet collection
        usingGenJets = []
        for cjet in jets:
          jetidx = cjet.jetIdx
          if jetidx == -1 or jetidx >= norigjets: continue # Should never happen, but does very rarely
          genjetidx = origjets[jetidx].genJetIdx
          if genjetidx == -1 or genjetidx >= ngenjets: continue
          usingGenJets.append(genjetidx)
          if len(usingGenJets) == 2: break

        mjjgen = 0
        if len(usingGenJets) == 2:
          J1 = ROOT.TLorentzVector()
          J2 = ROOT.TLorentzVector()
          J1.SetPtEtaPhiM(genjets[usingGenJets[0]].pt,genjets[usingGenJets[0]].eta,genjets[usingGenJets[0]].phi,0)
          J2.SetPtEtaPhiM(genjets[usingGenJets[1]].pt,genjets[usingGenJets[1]].eta,genjets[usingGenJets[1]].phi,0)
          mjjgen = (J1+J2).M()

        self.out.fillBranch("mjjGen", mjjgen)

        l1_eta = getattr(event, 'Lepton_eta')[0]
        l2_eta = getattr(event, 'Lepton_eta')[1]
        dphill = getattr(event, 'dphill')
        deta = l1_eta+l2_eta
        dphi = math.pi-dphill
        back2back = math.sqrt((deta*deta)+(dphi*dphi))
        self.out.fillBranch("back2back", back2back)

#        max_mjj = -9999
#        max_detajj = -9999 # detajj of two jets with max mjj; NOT max detajj of any jets
#        if njets >= 2:
#          J1 = ROOT.TLorentzVector()
#          J2 = ROOT.TLorentzVector()
#          for i,jet1 in enumerate(jets):
#            for j,jet2 in enumerate(jets):
#              if j <= i: continue
#              try:
#                J1.SetPtEtaPhiM(jet1.pt, jet1.eta, jet1.phi, origjets[jet1.jetIdx].mass)
#                J2.SetPtEtaPhiM(jet2.pt, jet2.eta, jet2.phi, origjets[jet2.jetIdx].mass)
#
#                this_mjj = (J1+J2).M()
#                if this_mjj > max_mjj:
#                  max_mjj = this_mjj
#                  max_detajj = abs(J1.Eta()-J2.Eta())
#              except IndexError: # If "Jet" has less entries as "CleanJet"??? It happened once (2017 GluGluHToWWTo2L2Nu_M800__part2)
#                max_mjj = getattr(event, 'mjj')
#                max_detajj = getattr(event, 'detajj')
#
#        self.out.fillBranch("mjj_hm", max_mjj)
#        self.out.fillBranch("detajj_hm", max_detajj)
#
#        # What if one jet was actually reconstructed as two jets?
#        max_mjjj = -9999
#        max_detajjj = -9999
#        if njets >= 3:
#          J1 = ROOT.TLorentzVector()
#          J2 = ROOT.TLorentzVector()
#          J3 = ROOT.TLorentzVector()
#          for i,jet1 in enumerate(jets):
#            for j,jet2 in enumerate(jets):
#              if j <= i: continue
#              for k,jet3 in enumerate(jets):
#                if k <= j: continue
#                try:
#                  J1.SetPtEtaPhiM(jet1.pt, jet1.eta, jet1.phi, origjets[jet1.jetIdx].mass)
#                  J2.SetPtEtaPhiM(jet2.pt, jet2.eta, jet2.phi, origjets[jet2.jetIdx].mass)
#                  J3.SetPtEtaPhiM(jet3.pt, jet3.eta, jet3.phi, origjets[jet3.jetIdx].mass)
#
#                  detajj_12 = abs(J1.Eta()-J2.Eta())
#                  detajj_13 = abs(J1.Eta()-J3.Eta())
#                  detajj_23 = abs(J2.Eta()-J3.Eta())
#                  if (detajj_12 < detajj_13) and (detajj_12 < detajj_23):
#                    JNew1 = J1+J2
#                    JNew2 = J3
#                  elif detajj_13 < detajj_23:
#                    JNew1 = J1+J3
#                    JNew2 = J2
#                  else:
#                    JNew1 = J2+J3
#                    JNew2 = J1
#
#                  this_mjjj = (JNew1+JNew2).M()
#                  if this_mjjj > max_mjjj:
#                    max_mjjj = this_mjjj
#                    max_detajjj = abs(JNew1.Eta()-JNew2.Eta())
#                except IndexError: # If "Jet" has less entries as "CleanJet"??? It happened once (2017 GluGluHToWWTo2L2Nu_M800__part2)
#                  max_mjjj = getattr(event, 'mjj')
#                  max_detajjj = getattr(event, 'detajj')
#
#        self.out.fillBranch("mjjj_hm", max_mjjj)
#        self.out.fillBranch("detajjj_hm", max_detajjj)

        return True

