import ROOT
ROOT.PyConfig.IgnoreCommandLineOptions = True
import re
from ROOT import TLorentzVector
from math import cosh
from PhysicsTools.NanoAODTools.postprocessing.framework.datamodel import Collection, Object
from PhysicsTools.NanoAODTools.postprocessing.framework.eventloop import Module
import LatinoAnalysis.NanoGardener.data.VBSjjlnu_vars as vbs_vars


class VBSjjlnu_kin(Module):
    '''
    
    '''
    def __init__(self, minptjet = 20, debug=False):
        self.minptjet = minptjet 
        self.debug = debug      

    def beginJob(self):
        pass
    def endJob(self):
        pass

    def beginFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        self.initReaders(inputTree)
        self.out = wrappedOutputTree

        # New Branches
        for typ, branches in vbs_vars.VBSjjlnu_branches.items():
            for var in branches:
                self.out.branch(var, typ)
        
    def endFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        pass


    def initReaders(self,tree): # this function gets the pointers to Value and ArrayReaders and sets them in the C++ worker class
        self.jet_var = {}
        for br in tree.GetListOfBranches():
           bname = br.GetName()
           if re.match('\ACleanJet_', bname): self.jet_var[bname] =    tree.arrayReader(bname)
        self.nJet = tree.valueReader('nCleanJet')

        self._ttreereaderversion = tree._ttreereaderversion
        
    
    def analyze(self, event):
        # Read branches that may be created by previous step in the chain
        # It's important to read them like this in case they 
        # are created by the step before in a PostProcessor chain. 
        print(event._tree._extrabranches)
        self.vbs_category = event.VBS_category
        self.vbs_jets = event.VBS_jets
        self.v_jets = event.V_jets
        self.nFatJet = event.nCleanFatJet
        self.JetNotFat_index = event.CleanJetNotFat_jetIdx
        self.nJetNotFat = event.nCleanJetNotFat
        self.rawjet_mass = event.Jet_mass

        # do this check at every event, as other modules might have read further branches
        #if event._tree._ttreereaderversion > self._ttreereaderversion: 
        self.initReaders(event._tree)

        print(self.jet_var["CleanJet_jetIdx"])

        lepton = Object(event, "Lepton", index=0)
        MET    = Object(event, "PuppiMET")
        category = int(self.vbs_category)

        lep = TLorentzVector()
        lep.SetPtEtaPhiE(lepton.pt, lepton.eta,lepton.phi, lepton.pt * cosh(lepton.eta))
        met = TLorentzVector()
        met.SetPtEtaPhiE(MET.pt, 0., MET.phi, MET.pt)

        # Trick for ArrayRead -> list
        vbs_jets_index = [self.vbs_jets[0], self.vbs_jets[1]]
        v_jets_index = [self.v_jets[0], self.v_jets[1]]

        jets, jets_ids = self.get_jets_vectors(event, self.minptjet, self.debug)

        output = None

        if category == 0:
            #####################
            # Boosted category
            fatjet = Object(event, "CleanFatJet", index=0)
            other_jets = []
            vbsjets = []
            # N.B. VBsjets and VJets indexes refers to the original CleanJet collection
            # the jets list is loaded with the NotFatJet mask. We have to compare original ids. 
            for jet, jetind in zip(jets, jets_ids):
                if jetind in vbs_jets_index:  
                    vbsjets.append(jet)
                else:                      
                    other_jets.append(jet)

            output = vbs_vars.getVBSkin_boosted(vbsjets, vjets, lepton, met, other_jets, debug=self.debug )

        
        elif category == 1:
            #####################
            # Resolved category
            other_jets = []
            vbsjets = []
            vjets = []
            for jet, jetind in zip(jets, jets_ids):
                if jetind in vbs_jets_index:  
                    vbsjets.append(jet)
                elif jetind in vjet_jets_index:
                    vjets.append(jet)
                else:                      
                    other_jets.append(jet)

            output = vbs_vars.getVBSkin_resolved(vbsjets, vjets, lepton, met, other_jets, debug=self.debug )
        
        elif category == 2:
            ##############################
            # Missing jet (3-jet) category
            output = vbs_vars.getDefault()

        # Fill the branches
        for var, val in output.items():
            self.out.fillBranch(var, val)        

        """return True (go to next module) or False (fail, go to next event)"""
        return True

    def get_jets_vectors(self, event, ptmin, debug=False):
        '''
        Returns a list of 4-momenta for jets looking only at jets
        that are cleaned from FatJets.
        A list of indexes in the collection of CleanJet is returned as a reference. 
        '''
        jets = []
        coll_ids = []
        for ijnf in range(int(self.nJetNotFat)):
            jetindex = self.JetNotFat_index[ijnf]
            print(jetindex, self.JetNotFat_index)
            # index in the original Jet collection
            rawjetid = self.jet_var["CleanJet_jetIdx"][jetindex]
            pt, eta, phi, mass = self.jet_var["CleanJet_pt"][jetindex], \
                        self.jet_var["CleanJet_eta"][jetindex],\
                        self.jet_var["CleanJet_phi"][jetindex], \
                        self.rawjet_mass[rawjetid]

            if pt < ptmin or pt<0: 
                break
            if abs(eta) > 10 : continue
            p = pt * cosh(eta)
            en = sqrt(p**2 + mass**2)
            vec = TLorentzVector()
            vec.SetPtEtaPhiE(pt, eta, phi, en)
            # check if different from the previous one
            if debug:
                print "Jet index: ", jetindex, "> pt:", pt ," eta:", eta, " phi:", phi, " mass:", mass
            jets.append(vec)
            coll_ids.append(jetindex)
        return jets, coll_ids




