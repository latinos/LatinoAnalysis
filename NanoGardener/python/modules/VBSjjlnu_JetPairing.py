import ROOT
ROOT.PyConfig.IgnoreCommandLineOptions = True
import re

from PhysicsTools.NanoAODTools.postprocessing.framework.datamodel import Collection 
from PhysicsTools.NanoAODTools.postprocessing.framework.eventloop import Module
from LatinoAnalysis.NanoGardener.modules.PairingUtils import *

class VBSjjlnu_JetPairing(Module):
    
    def __init__(self, minpt=20, mode="vbs:maxmjj-vjet:massWZ", debug = False):
        '''
        This modules performs the Jet pairing for VBS semileptonic analysis. 
        It separates events in three categories: boosted, resolved, missing-jet. 

        In the boosted category, only events with 1 FatJet are saved. Events with more FatJets 
        are vetoed. In the remaining jets the VBS pair is selected using the maximum invariant mass. 

        In the resolved category (>= 4 jets) different algorithms can be used to 
        choose the VBS jets and V jets. 

        Modes (for resolved category):
        - vbs:maxmjj-vjet:massWZ :  first of all VBS jets with maxmjj, then two jets nearest to W,Z mass
        - vbs:maxmjj-vjet:maxPt :   first of all VBS jets with maxmjj, then two jets with biggest Pt
        - vjet:massWZ-vbs:maxmjj:   like the 1st but in reverse order

        '''
        self.minpt = minpt
        self.mode = mode
        self.debug = debug

    def beginJob(self):
        pass
    def endJob(self):
        pass

    def beginFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        self.initReaders(inputTree)
        self.out = wrappedOutputTree

        # New Branches
        self.out.branch("VBS_jets", "I", n=2)
        self.out.branch("V_jets", "I", n=2)
        # 0-boosted, 1-resolved (4jets), 2-missing jet (3 jets)
        self.out.branch("VBS_category", "I")
        

    def endFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        pass


    def initReaders(self,tree): # this function gets the pointers to Value and ArrayReaders and sets them in the C++ worker class
        self.jet_var = {}
        for br in tree.GetListOfBranches():
           bname = br.GetName()
           if re.match('\ACleanJet_', bname): self.jet_var[bname] =    tree.arrayReader(bname)
        self.nJet = tree.valueReader('nCleanJet')
        self.nFatJet = tree.valueReader('nCleanFatJet')
        self.JetNotFat = tree.arrayReader("CleanJetNotFat_jetIdx")
        self.nJetNotFat = tree.valueReader("nCleanJetNotFat")
        self.rawjet_mass = tree.arrayReader("Jet_mass")

        self._ttreereaderversion = tree._ttreereaderversion
        
    
    def analyze(self, event):
        # do this check at every event, as other modules might have read further branches
        if event._tree._ttreereaderversion > self._ttreereaderversion: 
            self.initReaders(event._tree)

        nFatJet = int(self.nFatJet)
        VBS_jets = [-1,-1]
        V_jets = [-1,-1]
        category= -1

        # Take the 4-momenta of the CleanJets.
        # If FatJets are present only the CleanJetNotFat are taken
        good_jets = self.get_jets_vectors(event, self.minpt, self.debug)

        # Veto events with more than 1 FatJet
        if nFatJet >1 : return False

        if nFatJet == 1 and len(good_jets) >= 2 :
            ###################################
            # Boosted category
            ##################################
            category = 0
            # The V jet is the FatJet with largest Pt
            # We save the index of the FatJet, the jet collection will be choosen using the category
            V_jets = [0,0]
            # Vbs jets
            # Let's take the pair with biggest invariant mass
            VBS_jets = max_mjj_pair(good_jets)
            
        elif len(good_jets) >= 4:
            ##############################
            # Resolved category
            ###########################
            category = 1

            if self.mode == "vbs:maxmjj-vjet:massWZ":
                VBS_jets = max_mjj_pair(good_jets)
                # Save pairs of (index, jet) for the next step
                remaining_jets = [(i,j) for i,j in enumerate(good_jets) if i not in VBS_jets]
                # The result of the next step are indexes in the new collection of jets
                vpair_newindexes = nearest_mass_pair([rj[1] for rj in remaining_jets], 85.7863)
                # going back to global index 
                V_jets = [remaining_jets[i][0] for i in vpair_newindexes]

            elif self.mode == "vbs:maxmjj-vjet:maxPt":
                VBS_jets = max_mjj_pair(good_jets)
                # Save pairs of (index, jet) for the next step
                remaining_jets = [(i,j) for i,j in enumerate(good_jets) if i not in VBS_jets]
                # The result of the next step are indexes in the new collection of jets
                vpair_newindexes = max_pt_pair([rj[1] for rj in remaining_jets])
                # going back to global index 
                V_jets = [remaining_jets[i][0] for i in vpair_newindexes]

            elif self.mode == "vjet:massWZ-vbs:maxmjj":
                V_jets = nearest_mass_pair(jets, 85.7863)
                # Save pairs of (index, jet) for the next step
                remaining_jets = [(i,j) for i,j in enumerate(jets) if i not in V_jets]
                # The result of the next step are indexes in the new collection of jets
                vbspair_newindexes = max_mjj_pair([rj[1] for rj in remaining_jets])
                # going back to global index 
                VBS_jets = [remaining_jets[i][0] for i in vbspair_newindexes]
                                                            
        elif len(good_jets) == 3:
            # One jet is missing
            category = 2   
        else:   
            # Cut the event:
            # or it's boosted but with not enough jets, 
            # or it is not boosted and it has less than 3 jets.
            return False    

        
        if self.debug:
            VBS_mass = (good_jets[VBS_jets[0]] + good_jets[VBS_jets[1]]).M()
            VBS_eta = abs(good_jets[VBS_jets[0]].Eta() - good_jets[VBS_jets[1]].Eta())
            if category ==1:
                # Calculate invariant masses and deltaEta
                Vjet_mass = (good_jets[V_jets[0]] + good_jets[V_jets[1]]).M()
                print("Resolved| mjj_vbs:{:.3f}, vbs_deltaeta: {:.3f}, mjj_vjet: {:.3f}".format(
                        VBS_mass, VBS_eta, Vjet_mass))
            elif category == 0:
                print("Boosted| mjj_vbs:{:.3f}, vbs_deltaeta: {:.3f}".format(VBS_mass, VBS_eta))

        # Fill the variables
        self.out.fillBranch("VBS_category", category)
        self.out.fillBranch("VBS_jets", VBS_jets)
        self.out.fillBranch("V_jets", V_jets)       

        """return True (go to next module) or False (fail, go to next event)"""
        return True


    def get_jets_vectors(self, event, ptmin, debug=False):
        '''
        Returns a list of 4-momenta for jets (CleanJetNotFat)
        '''
        jets = []
        for ijnf in range(int(self.nJetNotFat)):
            jetindex = self.JetNotFat[ijnf]
            rawjetid = self.jet_var["CleanJet_jetIdx"][jetindex]
            pt, eta, phi, mass = self.jet_var["CleanJet_pt"][jetindex], \
                        self.jet_var["CleanJet_eta"][jetindex],\
                        self.jet_var["CleanJet_phi"][jetindex], \
                        self.rawjet_mass[rawjetid]

            if pt < ptmin or pt<0: 
                break
            if abs(eta) < 10 :
                p = pt * cosh(eta)
                en = sqrt(p**2 + mass**2)
                vec = TLorentzVector()
                vec.SetPtEtaPhiE(pt, eta, phi, en)
                # check if different from the previous one
                if debug:
                    print "Jet index: ", jetindex, "> pt:", pt ," eta:", eta, " phi:", phi, " mass:", mass
                jets.append(vec)
        return jets

