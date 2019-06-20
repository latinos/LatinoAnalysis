from LatinoAnalysis.Gardener.gardening import TreeCloner
import numpy
import ROOT
import math
import sys
import optparse
import re
import warnings
import os
from array import array;

from LatinoAnalysis.Gardener.gardening import TreeCloner

class PrefCorr(TreeCloner):
    def __init__(self):
        pass

    def help(self) :
        return '''Prefire Corrections'''

    def addOptions(self,parser) :
        description = self.help()
        group = optparse.OptionGroup(parser,self.label, description)
        group.add_option('--jetroot',  dest='jetroot',  help='File containing the jet map', default="L1prefiring_jetpt_2016BtoH.root")
        group.add_option('--photonroot',  dest='photonroot',  help='File containing the photon map', default="L1prefiring_photonpt_2016BtoH.root")
        group.add_option('--jetmap',  dest='jetmap',  help='Name of the jet map', default="L1prefiring_jetpt_2016BtoH")
        group.add_option('--photonmap',  dest='photonmap',  help='Name of the photon map', default="L1prefiring_photonpt_2016BtoH")
        #group.add_option('--empt',  dest='empt',  help='Set to 1 if the jet map is defined for energy deposited in ECAL (pT_EM vs pT). For jet map only, not photon!', default=0)
        parser.add_option_group(group)
        return group

    def checkOptions(self,opts):
        cmssw_base = os.getenv('CMSSW_BASE')

        self.photon_file = self.open_root(cmssw_base + "/src/LatinoAnalysis/NanoGardener/python/data/prefire_maps/" + opts.photonroot)
        self.photon_map = self.get_root_obj(self.photon_file, opts.photonmap)

        self.jet_file = self.open_root(cmssw_base + "/src/LatinoAnalysis/NanoGardener/python/data/prefire_maps/" + opts.jetroot)
        self.jet_map = self.get_root_obj(self.jet_file, opts.jetmap)

        self.UseEMpT = 0 # I can't find "Charged EM fraction" and "Neutral EM fraction" variables in std_vector_jet, so this can't be used


    def open_root(self, path):
        r_file = ROOT.TFile.Open(path)
        if not r_file.__nonzero__() or not r_file.IsOpen(): raise NameError('File ' + path + ' not open')
        return r_file

    def get_root_obj(self, root_file, obj_name):
        r_obj = root_file.Get(obj_name)
        if not r_obj.__nonzero__(): raise NameError('Root Object ' + obj_name + ' not found')
        return r_obj

    def process(self,**kwargs) :
        tree   = kwargs['tree']
        input  = kwargs['input']
        output = kwargs['output']

        self.connect(tree,input)
        nentries = self.itree.GetEntries()
        print 'Total number of entries: ',nentries 
        savedentries = 0

        self.branchnames = ["PrefireWeight", "PrefireWeight_Up", "PrefireWeight_Down"]
        self.clone(output, self.branchnames)

        pref_nom = numpy.ones(1, dtype=numpy.float32)
        pref_up = numpy.ones(1, dtype=numpy.float32)
        pref_dn = numpy.ones(1, dtype=numpy.float32)

        self.otree.Branch('PrefireWeight', pref_nom, 'PrefireWeight/F')
        self.otree.Branch('PrefireWeight_Up', pref_up, 'PrefireWeight_Up/F')
        self.otree.Branch('PrefireWeight_Down', pref_dn, 'PrefireWeight_Down/F')

        itree = self.itree

        print ' - Starting event loop'
        step = 5000

        for i in xrange(nentries) :
          itree.GetEntry(i)

          if i > 0 and i%step == 0.:
            print i,'events processed :: ', nentries

          # Options
          self.JetMinPt = 30 # Min/Max Values may need to be fixed for new maps
          self.JetMaxPt = 500
          self.JetMinEta = 2.0
          self.JetMaxEta = 3.1
          self.PhotonMinPt = 20
          self.PhotonMaxPt = 500
          self.PhotonMinEta = 2.0
          self.PhotonMaxEta = 3.0

          for i in [0,1,-1]:
            self.variation = i
            prefw = 1.0

            for jid in range(itree.std_vector_jet_pt.size()): # First loop over all jets
              jetpf = 1.0
              PhotonInJet = []

              jetpt = itree.std_vector_jet_pt[jid]
              jeteta = itree.std_vector_jet_eta[jid]
              jetphi = itree.std_vector_jet_phi[jid]
              #if self.UseEMpT: jetpt *= (jet.chEmEF + jet.neEmEF)

              if jetpt >= self.JetMinPt and abs(jeteta) <= self.JetMaxEta and abs(jeteta) >= self.JetMinEta:
                jetpf *= 1-self.GetPrefireProbability(self.jet_map, jeteta, jetpt, self.JetMaxPt)

              phopf = self.EGvalue(jetphi, jeteta)
              prefw *= min(jetpf,phopf) # The higher prefire-probablity between the jet and the lower-pt photon(s)/elecron(s) from the jet is chosen

            prefw *= self.EGvalue(-9, -9) # Then loop over all photons/electrons not associated to jets
            if i == 0: pref_nom[0] = prefw
            if i == 1: pref_up[0] = prefw
            if i == -1: pref_dn[0] = prefw

          self.otree.Fill()
          savedentries+=1

        self.disconnect()
        print '- Eventloop completed'
        print '- Saved:', savedentries, 'events'

    def EGvalue(self, jetphi, jeteta):
      itree = self.itree
      phopf = 1.0
      EleIsPhoton = []

      for pid in range(itree.std_vector_photon_pt.size()):
        phopt = itree.std_vector_photon_pt[pid]
        phoeta = itree.std_vector_photon_eta[pid]
        phophi = itree.std_vector_photon_phi[pid]

        if self.inDeltaR(jetphi, jeteta, phophi, phoeta) or (jetphi==-9 and jeteta==-9):
          if phopt >= self.PhotonMinPt and abs(phoeta) <= self.PhotonMaxEta and abs(phoeta) >= self.PhotonMinEta:
            phopf_temp = 1-self.GetPrefireProbability(self.photon_map, phoeta, phopt, self.PhotonMaxPt)

            elepf_temp = 1.0
            for eid in range(itree.std_vector_lepton_pt.size()):
              if abs(itree.std_vector_lepton_flavour[eid]) != 11: continue
              elept = itree.std_vector_lepton_pt[eid]
              eleeta = itree.std_vector_lepton_eta[eid]
              elephi = itree.std_vector_lepton_phi[eid]
              if self.inDeltaR(phophi, phoeta, elephi, eleeta) and (self.inDeltaR(jetphi, jeteta, elephi, eleeta) or (jetphi==-9 and jeteta==-9)): # What if the electron corresponding to the photon would return a different value?
                if elept >= self.PhotonMinPt and abs(eleeta) <= self.PhotonMaxEta and abs(eleeta) >= self.PhotonMinEta:
                  elepf_temp = 1-self.GetPrefireProbability(self.photon_map, eleeta, elept, self.PhotonMaxPt)
                  EleIsPhoton.append(eid)

            phopf *= min(phopf_temp, elepf_temp) # The higher prefire-probablity between the photon and corresponding electron is chosen

      for eid in range(itree.std_vector_lepton_pt.size()):
        if abs(itree.std_vector_lepton_flavour[eid]) != 11 or eid in EleIsPhoton: continue
        elept = itree.std_vector_lepton_pt[eid]
        eleeta = itree.std_vector_lepton_eta[eid]
        elephi = itree.std_vector_lepton_phi[eid]

        if self.inDeltaR(jetphi, jeteta, elephi, eleeta) or (jetphi==-9 and jeteta==-9):
          if elept >= self.PhotonMinPt and abs(eleeta) <= self.PhotonMaxEta and abs(eleeta) >= self.PhotonMinEta:
            phopf *= 1-self.GetPrefireProbability(self.photon_map, eleeta, elept, self.PhotonMaxPt)

      return phopf

    def GetPrefireProbability(self, Map, eta, pt, maxpt):
      bin = Map.FindBin(eta, min(pt, maxpt-0.01))
      pref_prob = Map.GetBinContent(bin)

      # Choose larger uncertainty between 20% of prefire rate and bin statistical uncertainty
      if self.variation == 1: 
        pref_prob = min(max(pref_prob + Map.GetBinError(bin), (1+0.2) * pref_prob), 1.0)
      if self.variation == -1:
        pref_prob = max(min(pref_prob - Map.GetBinError(bin), (1-0.2) * pref_prob), 0.0)
      return pref_prob

    def inDeltaR(self, phi1, eta1, phi2, eta2, drmax=0.4):
      dphi = phi1 - phi2
      if dphi > ROOT.TMath.Pi(): dphi -= 2*ROOT.TMath.Pi()
      if dphi < -ROOT.TMath.Pi(): dphi += 2*ROOT.TMath.Pi()
      deta = eta1 - eta2
      deltaR = (deta*deta) + (dphi*dphi)
      if deltaR < (drmax*drmax):
        return True
      else:
        return False
