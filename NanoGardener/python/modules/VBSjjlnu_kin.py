import ROOT
ROOT.PyConfig.IgnoreCommandLineOptions = True
from ROOT import TLorentzVector
from math import cosh, sqrt
from PhysicsTools.NanoAODTools.postprocessing.framework.datamodel import Collection, Object
from PhysicsTools.NanoAODTools.postprocessing.framework.eventloop import Module
import LatinoAnalysis.NanoGardener.data.VBSjjlnu_vars as vbs_vars
import LatinoAnalysis.Gardener.variables.VBS_recoNeutrino as RecoNeutrino


class VBSjjlnu_kin(Module):
    '''
    This module calculates several VBS semileptonic analysis observables. 
    The VBS and Vjets have been already associated by the VBSjjlnu_JetPairing module. 
    The mode selects the tagging algorithm. 

    The mode option is a list. It selects the association algo for each category of 
    VBS_category.  For example mode=[maxmjj, maxmjj_massWZ] selects the maxmjj strategy 
    for Fatjet events and  maxmjj_massWZ for resolved events.

    metType can be PF or Puppi.
    '''
    def __init__(self, mode=[ "maxmjj", "maxmjj_massWZ"], met="Puppi", debug=False):
        self.V_jets_var = { 0: "V_jets_"+ mode[0],  1: "V_jets_"+ mode[1]}
        self.VBS_jets_var = { 0: "VBS_jets_"+mode[0], 1: "VBS_jets_" +mode[1]}
        self.metType = met
        self.debug = debug      

    def beginJob(self):
        pass
    def endJob(self):
        pass

    def beginFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        #self.initReaders(inputTree)
        self.out = wrappedOutputTree

        # New Branches
        for typ, branches in vbs_vars.VBSjjlnu_branches.items():
            for var in branches:
                self.out.branch(var, typ)
        for vec_branch in vbs_vars.VBSjjlnu_vector_branches:
            self.out.branch(vec_branch["name"], vec_branch["type"], lenVar=vec_branch["len"])
        
    def endFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        pass

    
    def analyze(self, event):
        # Read branches that may be created by previous step in the chain
        # It's important to read them like this in case they 
        # are created by the step before in a PostProcessor chain. 
        self.vbs_category = event.VBS_category
        self.rawJet_coll    = Collection(event, 'Jet')
        self.Jet_coll       = Collection(event, 'CleanJet')
        self.JetNotFat_coll = Collection(event, 'CleanJetNotFat')

        lepton_raw = Object(event, "Lepton", index=0)
        if self.metType == "PF":
            met_raw    = Object(event, "MET")
        elif self.metType == "Puppi":
            met_raw = Object(event, "PuppiMET")

        category = int(self.vbs_category)

        lep = TLorentzVector()
        lep.SetPtEtaPhiE(lepton_raw.pt, lepton_raw.eta,lepton_raw.phi, lepton_raw.pt * cosh(lepton_raw.eta))
        met = TLorentzVector()
        met.SetPtEtaPhiE(met_raw.pt, 0., met_raw.phi, met_raw.pt)
        
        # Reconstruct neutrino from lepton and met
        reco_neutrino = RecoNeutrino.reconstruct_neutrino(lep,met,mode="central")

        # Extract the jets four momenta using only JetNotFat but keeping 
        # a reference to the CleanJet index. 
        jets, jets_ids = self.get_jets_vectors()
        vbsjets = []
        vjets = []
        other_jets = []
        other_jets_ind = []
        for jet, jetind in zip(jets, jets_ids):
            if jetind in event[self.VBS_jets_var[category]]:  
                vbsjets.append(jet)
            elif jetind in event[self.V_jets_var[category]]:
                vjets.append(jet)
            else:                      
                other_jets.append(jet)
                other_jets_ind.append(jetind)

        output = None

        if category == 0:
            #####################
            # Boosted category
            fatjet = Object(event, "CleanFatJet", index=0)
            # CleanFatJet collection mass is Softdrop PUPPI mass
            output = vbs_vars.getVBSkin_boosted(vbsjets, fatjet.p4(), lep, met, reco_neutrino,
                                other_jets, other_jets_ind, debug=self.debug )

        elif category == 1:
            #####################
            # Resolved category
            output = vbs_vars.getVBSkin_resolved(vbsjets, vjets, lep, met, reco_neutrino,
                                other_jets, other_jets_ind, debug=self.debug )

        # Fill the branches
        for var, val in output.items():
            self.out.fillBranch(var, val)        

        """return True (go to next module) or False (fail, go to next event)"""
        return True

    def get_jets_vectors(self):
        '''
        Returns a list of 4-momenta for jets looking only at jets
        that are cleaned from FatJets.
        A list of indexes in the collection of CleanJet is returned as a reference. 
        '''
        jets = []
        coll_ids = []
        for ijnf in range(len(self.JetNotFat_coll)):
            jetindex = self.JetNotFat_coll[ijnf].jetIdx
            # index in the original Jet collection
            rawjetid = self.Jet_coll[jetindex].jetIdx
            pt, eta, phi, mass = self.Jet_coll[jetindex].pt, \
                        self.Jet_coll[jetindex].eta,\
                        self.Jet_coll[jetindex].phi, \
                        self.rawJet_coll[rawjetid].mass

            if abs(eta) > 10 : continue
            p = pt * cosh(eta)
            en = sqrt(p**2 + mass**2)
            vec = TLorentzVector()
            vec.SetPtEtaPhiE(pt, eta, phi, en)
            # check if different from the previous one
            if self.debug:
                print "Jet index: ", jetindex, "> pt:", pt ," eta:", eta, " phi:", phi, " mass:", mass
            jets.append(vec)
            coll_ids.append(jetindex)
        return jets, coll_ids




