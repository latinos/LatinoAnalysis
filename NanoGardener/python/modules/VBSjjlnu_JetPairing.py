import ROOT
ROOT.PyConfig.IgnoreCommandLineOptions = True
import re

from PhysicsTools.NanoAODTools.postprocessing.framework.datamodel import Collection
from PhysicsTools.NanoAODTools.postprocessing.framework.eventloop import Module
from LatinoAnalysis.NanoGardener.modules.PairingUtils import *

nearest_massWZ = lambda jets: nearest_mass_pair(jets,85.7863)
nearest_massWZ.__name__ = "nearest_massWZ"

# The dictionary define the name of the tagging strategy and functions to 
# use. The order of the list defines the order of the tagging of VBS and V jets
pairing_strategies_resolved = {
    "maxmjj_massWZ"      : [("VBS", max_mjj_pair),("V", nearest_massWZ)],
    "maxmjj_maxPt"       : [("VBS", max_mjj_pair),("V", max_pt_pair)],
    "maxPt_massWZ"       : [("VBS", max_pt_pair), ("V", nearest_massWZ)],
    "massWZ_maxmjj"      : [("V", nearest_massWZ), ("VBS", max_mjj_pair)],
    "massWZ_maxPt"       : [("V", nearest_massWZ), ("VBS",max_pt_pair)]
}
pairing_strategies_fatjet = {
    "maxmjj": max_mjj_pair,
    "maxPt" : max_pt_pair
}



class VBSjjlnu_JetPairing(Module):
    
    def __init__(self, minpt=20, etacuts=[], mode="ALL", debug = False):
        '''
        This modules performs the Jet pairing for VBS semileptonic analysis. 
        It separates events in three categories: boosted and resolved. 

        In the boosted category, only events with 1 FatJet are saved. Events with more FatJets 
        are vetoed. In the remaining jets the VBS pair is selected using the maximum invariant mass. 

        In the resolved category (>= 4 jets) different algorithms can be used to 
        choose the VBS jets and V jets. 

        An eta interval cut can be specified to avoid using the jets in those regions for tagging

        Modes (for resolved category):
        "maxmjj_massWZ" : before VBS jets with max Mjj, than V-jets with mass nearest to (mW+mZ)/2
        "maxmjj_maxPt" : before VBS jets with max Mjj, then V-jets as the pair with max Pt,
        "maxmjj_maxPtsingle"  : before VBS jets with max Mjj, then V-jets as the two jets with highest Pt
        "maxPt_massWZ"  : before VBS jets as pair with max Pt, then V-jets with mass W,Z
        "maxPtsingle_massWZ" : befor VBS jets as the two jets with highest Pt, then V-jet with mass W,Z

        "massWZ_maxmjj": before V jets with mass nearest to W,Z, then VBS jets with MaxMjj
        "massWZ_maxPt" :before V jets with mass nearest to W,Z, then VBS jets with pair with max Pt
       

        '''
        self.minpt = minpt
        self.mode = mode
        self.etacuts = etacuts
        self.debug = debug

    def beginJob(self):
        pass
    def endJob(self):
        pass

    def beginFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        #self.initReaders(inputTree)
        self.out = wrappedOutputTree

        # New Branches
        for key in pairing_strategies_resolved.keys():
            self.out.branch("VBS_jets_"+key, "I", n=2)
            self.out.branch("V_jets_"+key, "I", n=2)
        for key in pairing_strategies_fatjet.keys():
            self.out.branch("VBS_jets_"+key, "I", n=2)
            self.out.branch("V_jets_"+key, "I", n=2)
        # 0-boosted, 1-resolved (4jets)
        self.out.branch("VBS_category", "I")
        

    def endFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        pass


    def analyze(self, event):
        # Read branches that may be created by previous step in the chain
        # It's important to read them like this in case they 
        # are created by the step before in a PostProcessor chain. 
        self.nFatJet = event.nCleanFatJet
        self.rawJet_coll    = Collection(event, 'Jet')
        self.Jet_coll       = Collection(event, 'CleanJet')
        self.JetNotFat_coll = Collection(event,'CleanJetNotFat')
        
        # do this check at every event, as other modules might have read further branches
        # if event._tree._ttreereaderversion > self._ttreereaderversion: 
        #     self.initReaders(event._tree)

        category= -1

        # Take the 4-momenta of the CleanJets.
        # If FatJets are present only the CleanJetNotFat are taken. A list of indexes
        # referring to the CleanJet collection is keeps to save the final result
        good_jets, good_jets_ids = self.get_jets_vectors(self.minpt, self.etacuts)
         # N.B. The VBS_jets and V_jets index are positions in the list of 
        # good_jets (Jet not overlapping with Fatjet with a minpt). 
        # We want to save a reference to the CleanJet collection.
        
        # Veto events with more than 1 FatJet
        if self.nFatJet >1 : return False

        if self.nFatJet == 1 and len(good_jets) >= 2 :
            ###################################
            # Boosted category
            ##################################
            category = 0
            # Vbs jets with different algo
            for key, algo in pairing_strategies_fatjet.items():
                VBS_jets = [-1,-1]
                V_jets =   [-1,-1]
                # N.B. always get back CleanJet collection ids 
                VBS_jets = [good_jets_ids[ij] for ij in algo(good_jets)]
                self.out.fillBranch("VBS_jets_"+key, VBS_jets)
                self.out.fillBranch("V_jets_"+key, V_jets)

        elif len(good_jets) >= 4:
            ##############################
            # Resolved category
            ###########################
            category = 1

            # Cache of association algos
            # (N.B. indexes by good_jets collections)
            cache = { }  # algo: ( associated_jets, remaining jets)

            if self.mode=="ALL":
                for key, algos in pairing_strategies_resolved.items():
                    self.perform_jet_association(key, good_jets, good_jets_ids, cache)
            else:
                if self.mode in pairing_strategies_resolved:
                    self.perform_jet_association(self.mode, good_jets, good_jets_ids, cache)
                else:
                    print("ERROR! Selected pairing mode not found!!")
                    return False
        else:   
            # Cut the event:
            # or it's boosted but with not enough jets, 
            # or it is not boosted and it has less than 4 jets with minpt
            #print("Event removed")
            return False    


        # Fill the category
        self.out.fillBranch("VBS_category", category)    

        """return True (go to next module) or False (fail, go to next event)"""
        return True
 

    def get_jets_vectors(self, ptmin, etacuts=[]):
        '''
        Returns a list of 4-momenta for jets looking only at jets
        that are cleaned from FatJets.
        A list of indexes in the collection of CleanJet is returned as a reference. 

        Inserted here an eta interval cut to avoid using the jets in a specified region for 
        tagging. 
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

            if pt < ptmin or pt<0: 
                break

            passetacut = True
            for cut in etacuts:
                if abs(eta) > cut[0] and abs(eta) < cut[1]: 
                    passetacut = False
                    if self.debug: 
                        print "Jet index: ", jetindex, " CUT > pt:", pt ," eta:", eta, " phi:", phi, " mass:", mass
            if not passetacut : continue
            
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

    
    def perform_jet_association(self, mode, good_jets, good_jets_ids, cache):
        '''
            This function perform the association of the jets with one of the 
            algorithm in pairing_strategies_resolved map.
        '''
        (tag1, algo1), (tag2, algo2) = pairing_strategies_resolved[mode]
        if self.debug: print "Association: ", tag1, algo1.__name__, tag2, algo2.__name__

        if algo1.__name__ in cache:
            if self.debug: print "using cache for algo: ", algo1.__name__, algo1
            V1, remain_jets = cache[algo1.__name__]
        else:
            # Apply first algo
            V1 = algo1(good_jets)
            # Get a [index, jet] of jets remained to be used
            remain_jets = [(i,j) for i,j in enumerate(good_jets) if i not in V1]
            # save in cache
            cache[algo1.__name__] = (V1, remain_jets)

        #apply algo 2 and get indexes in good_jets collections from remain_jets 
        V2 = [remain_jets[k][0] for k in algo2([rj[1] for rj in remain_jets])]
        # Now going back to CleanJet indexes 
        V1_cleanjets = [good_jets_ids[ij] for ij in V1]
        V2_cleanjets = [good_jets_ids[ij] for ij in V2]

        if self.debug:
            print mode , "> ", tag1, V1_cleanjets, " | ", tag2, V2_cleanjets

        self.out.fillBranch("{}_jets_{}".format(tag1,mode), V1_cleanjets)
        self.out.fillBranch("{}_jets_{}".format(tag2,mode), V2_cleanjets)