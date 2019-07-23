import ROOT
ROOT.PyConfig.IgnoreCommandLineOptions = True
import re

from PhysicsTools.NanoAODTools.postprocessing.framework.datamodel import Collection 
from PhysicsTools.NanoAODTools.postprocessing.framework.eventloop import Module
from LatinoAnalysis.NanoGardener.data.FatJetMaker_cfg import CleanFatJet_br, CleanFatJet_var

class FatJetMaker(Module):
    '''
    This module cleans FatJet collection 
    1) kinematics cuts:  minpt, maxeta, max_tau21, mass_range
    2) for each FatJet passing the cuts the overlapping with leptons is checked
       with a configurable radius, (default 1.0)
    3) The CleanJet collection is checked to save a vector with the ids of the jets
        not overlapping with the CleanFatJet. (default radius 0.8)

    The output of this module is a CleanFatJet collection with pt,eta,phi. Also a jetIdx reference 
    to FatJet original collection is saved.
    The list of CleanJet ids not overlapping with FatJets is saved in  CleanJetNotFat_jetIdx collection 
    and relative size nCleanJetNotFat. 


    Reference for FatJet ID:
    https://twiki.cern.ch/twiki/bin/viewauth/CMS/JetWtagging
    https://indico.cern.ch/event/779704/contributions/3245276/attachments/1768349/2874166/WtagSF_tau21.pdf

    '''
    def __init__(self, minpt=200.0, maxeta=2.4, max_tau21=0.4,mass_range=[100, 200], 
                    over_lepR =1.0, over_jetR = 1.2):
        self.minpt = minpt
        self.maxeta = maxeta 
        self.max_tau21 = max_tau21
        self.mass_range = mass_range 
        self.over_lepR = over_lepR
        self.over_jetR = over_jetR

    def beginJob(self):
        pass
    def endJob(self):
        pass

    def beginFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        self.initReaders(inputTree)
        self.out = wrappedOutputTree

        # New Branches
        for typ in CleanFatJet_br:
            for var in CleanFatJet_br[typ]:
                self.out.branch(var, typ, lenVar='nCleanFatJet')
        #vector of CleanJet idx not overlapping with Fatjets
        self.out.branch('CleanJetNotFat_jetIdx', "I", lenVar="nCleanJetNotFat") 

    def endFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        pass


    def initReaders(self,tree): # this function gets the pointers to Value and ArrayReaders and sets them in the C++ worker class
        self.lepton_var = {}
        self.jet_var = {}
        self.fatjet_var = {}
        for br in tree.GetListOfBranches():
           bname = br.GetName()
           if re.match('\ALepton_', bname):  self.lepton_var[bname] =  tree.arrayReader(bname)
           if re.match('\ACleanJet_', bname): self.jet_var[bname] =    tree.arrayReader(bname)
           if re.match('\AFatJet_', bname):   self.fatjet_var[bname] = tree.arrayReader(bname)

        self.nLepton = tree.valueReader('nLepton')
        self.nJet = tree.valueReader('nCleanJet')
        self.nFatJet = tree.valueReader('nFatJet')
        self._ttreereaderversion = tree._ttreereaderversion
        
    
    def analyze(self, event):
        # do this check at every event, as other modules might have read further branches
        if event._tree._ttreereaderversion > self._ttreereaderversion: 
            self.initReaders(event._tree)

        nFatJet = int(self.nFatJet)
        nLep = int(self.nLepton)
        nJet = int(self.nJet)

        overlapping_jets = []
        output_vars  = {}
        for typ in CleanFatJet_br:
            for var in CleanFatJet_br[typ]:
                output_vars[var] = []

        for ifj in range(nFatJet):
            fj_pt = self.fatjet_var["FatJet_pt"][ifj]
            fj_eta = self.fatjet_var["FatJet_eta"][ifj]
            fj_phi = self.fatjet_var["FatJet_phi"][ifj]
            fj_softdrop_mass = self.fatjet_var["FatJet_msoftdrop"][ifj]
            fj_tau1 = self.fatjet_var["FatJet_tau1"][ifj]
            fj_tau2 = self.fatjet_var["FatJet_tau2"][ifj]
            # If the FatJet has only 1 particle remove it (rare corner case)
            if fj_tau1 == 0:  continue
            fj_tau21 = fj_tau2 / fj_tau1
            
            goodFatJet = True

            if fj_pt < self.minpt:              goodFatJet = False
            if abs(fj_eta) > self.maxeta :      goodFatJet = False
            if fj_softdrop_mass < self.mass_range[0] or fj_softdrop_mass> self.mass_range[1]: goodFatJet = False
            if fj_tau21 > self.max_tau21:       goodFatJet = False

            # Check leptons if the ID kinematics cuts are passed
            if goodFatJet:
                # Loop on leptons and exclude FatJet if there's a lepton with DeltaR < 1
                for il in range(nLep):
                    lep_phi = self.lepton_var["Lepton_phi"][il]
                    lep_eta = self.lepton_var["Lepton_eta"][il]
                    if self.inDeltaR(fj_phi, fj_eta, lep_phi, lep_eta, drmax=self.over_lepR): 
                        goodFatJet = False
                       #print("Found lepton matched to FatJet")

            if goodFatJet:
                # save the CleanFatJet info
                output_vars["CleanFatJet_pt"].append(fj_pt)
                output_vars["CleanFatJet_eta"].append(fj_eta)
                output_vars["CleanFatJet_phi"].append(fj_phi)
                output_vars["CleanFatJet_mass"].append(fj_softdrop_mass)
                output_vars["CleanFatJet_tau21"].append(fj_tau21)
                output_vars["CleanFatJet_jetIdx"].append(ifj)

                # Get the jet overlapping with this CleanFatJet  DeltaR<0.8
                for ij in range(nJet):
                    if self.inDeltaR(fj_phi, fj_eta, 
                                    self.jet_var["CleanJet_phi"][ij], self.jet_var["CleanJet_eta"][ij], 
                                    drmax = self.over_jetR):
                        overlapping_jets.append(ij)
                        #print("Found overlapping jet")
        
        # Fill all branches
        for var in output_vars:
            self.out.fillBranch(var, output_vars[var])
        # Now let's save a vector of CleanJet NOT overlapping with CleanFatJet
        cleanjet_notoverlap = [ij for ij in range(nJet) if ij not in overlapping_jets]
        self.out.fillBranch("CleanJetNotFat_jetIdx", cleanjet_notoverlap)

        """return True (go to next module) or False (fail, go to next event)"""
        return True



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
