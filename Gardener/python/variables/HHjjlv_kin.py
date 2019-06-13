import optparse
import numpy
import ROOT
import os.path
from collections import namedtuple
from itertools import chain
from math import cosh
from ROOT import TLorentzVector
from LatinoAnalysis.Gardener.gardening import TreeCloner
import LatinoAnalysis.Gardener.variables.PairingUtils as utils 


hh_branches = {
            "F": [ "mjj_b", "mjj_wjet",
                "b_pt_high", "b_pt_low", "b_etaprod",
                "wjet_pt_high", "wjet_pt_low", 
                "b_eta_high", "b_eta_low",
                "wjet_eta_high", "wjet_eta_low",
                "deltaeta_b",  "deltaphi_b", 
                "deltaeta_wjet", "deltaphi_wjet", 
                "deltaphi_lep_b_high", "deltaphi_lep_b_low", 
                "deltaeta_lep_b_high", "deltaeta_lep_b_low", 
                "deltaphi_lep_wjet_high", "deltaphi_lep_wjet_low",
                "deltaeta_lep_wjet_high", "deltaeta_lep_wjet_low",
                "deltaR_lep_b", "deltaR_lep_wjet",
                "deltaphi_lep_nu", "deltaeta_lep_nu",
                "deltaR_lep_nu", "deltaR_b", "deltaR_wjet",
                "Rwjets_high", "Rwjets_low",
                "Zwjets_high", "Zwjets_low", "Zlep",
                "A_b", "A_wjet", "Mw_lep", "w_lep_pt", 
                "Mww", "R_ww", "R_mw", "A_ww",
                "C_b", "C_ww", "L_p", "L_pw", "Ht",
                "recoMET", "recoMET_pz"          
                ],
            "I": ["N_jets", "N_jets_forward", "N_jets_central"]
            }


def getHHkinematics(bjets, wjets,lepton, met, other_jets_eta, other_jets_pts, debug=False):
    output = {}
    # variables extraction for b-jets
    total_b = TLorentzVector(0,0,0,0)
    b_etas = []
    b_phis = []
    b_pts = []
    for i, j in enumerate(bjets):
        total_h+= j
        b_etas.append(j.Eta())
        b_phis.append(j.Phi())
        b_pts.append(j.Pt())
    if debug:
        print "b-jets pts", b_pts
        print "b-jets etas", b_etas
    deltaeta_b = abs(b_etas[0]- b_etas[1])
    mean_eta_b = sum(b_etas) / 2 
    output["b_pt_high"] = b_pts[0]
    output["b_pt_low"] = b_pts[1]
    output["mjj_b"] = total_b.M()
    output["deltaeta_b"] = deltaeta_b
    output["deltaphi_b"] = abs(bjets[0].DeltaPhi(bjets[1]))
    output["deltaR_b"] = bjets[0].DrEtaPhi(bjets[1])
    output["b_etaprod"] = b_etas[0]*b_etas[1]
    output["b_eta_high"] = abs(b_etas[0])
    output["b_eta_low"] = abs(b_etas[1])

    # variables extraction for w-jets
    total_wjet = TLorentzVector(0,0,0,0)
    wjet_etas = []
    wjet_phis = []
    wjet_pts = []
    for i, j in enumerate(wjets):
        total_wjet += j
        wjet_etas.append(j.Eta())
        wjet_phis.append(j.Phi())
        wjet_pts.append(j.Pt())
    if debug:
        print "Wjet pts", wjet_pts
        print "Wjet etas", wjet_etas
    output["Wjet_pt_high"] = wjet_pts[0]
    output["Wjet_pt_low"] = wjet_pts[1]
    output["mjj_Wjet"] = total_wjet.M()
    output["deltaphi_wjet"] =  abs(wjets[0].DeltaPhi(wjets[1]))
    output["deltaeta_wjet"] = abs(wjet_etas[0] - wjet_etas[1])
    output["deltaR_wjet"] = wjets[0].DrEtaPhi(wjets[1])
    output["wjet_eta_high"] = abs(wjet_etas[0])
    output["wjet_eta_low"] = abs(wjet_etas[1])


    # Delta Phi with lepton
    output["deltaphi_lep_b_high"] = abs(lepton.DeltaPhi(bjets[0]))
    output["deltaphi_lep_b_low"] = abs(lepton.DeltaPhi(bjets[1]))
    output["deltaphi_lep_wjet_high"] = abs(lepton.DeltaPhi(wjets[0]))
    output["deltaphi_lep_wjet_low"] = abs(lepton.DeltaPhi(wjets[1]))

    # Delta Eta with lepton
    output["deltaeta_lep_b_high"] = abs(lepton.Eta() - b_etas[0])
    output["deltaeta_lep_b_low"]  = abs(lepton.Eta() - b_etas[1])
    output["deltaeta_lep_wjet_high"] = abs(lepton.Eta() - wjet_etas[0])
    output["deltaeta_lep_wjet_low"] = abs(lepton.Eta() - wjet_etas[1])
       
    #Delta Phi with MET
    output["deltaphi_met_b_high"] = abs(met.DeltaPhi(bjets[0]))
    output["deltaphi_met_b_low"] = abs(met.DeltaPhi(bjets[1]))
    output["deltaphi__wjet_high"] = abs(met.DeltaPhi(wjets[0]))
    output["deltaphi_met_wjet_low"] = abs(met.DeltaPhi(wjets[1]))
 
    # Delta Eta with MET
    output["deltaeta_met_b_high"] = abs(met.Eta() - b_etas[0])
    output["deltaeta_met_b_low"]  = abs(met.Eta() - b_etas[1])
    output["deltaeta_met_wjet_high"] = abs(met.Eta() - wjet_etas[0])
    output["deltaeta_met_wjet_low"] = abs(met.Eta() - wjet_etas[1])

    # Look for nearest  jet from lepton
    output["deltaR_lep_b"] = min( [ lepton.DrEtaPhi(bjets[0]), lepton.DrEtaPhi(bjets[1])])
    output["deltaR_lep_wjet"] = min( [ lepton.DrEtaPhi(wjets[0]), lepton.DrEtaPhi(wjets[1])])

    #R variables
    pt_b_12  = bjets[0].Pt() * bjets[1].Pt() 
    output["Rwjets_high"] = (lepton.Pt() * wjets[0].Pt()) / pt_b_12
    output["Rvjets_low"] = (lepton.Pt() * wjets[1].Pt()) / pt_b_12

    #Asymmetry
    output["A_b"]  = (b_pts[0] - b_pts[1]) / sum(b_pts)
    output["A_wjet"] = (wjet_pts[0] - wjet_pts[1]) / sum(wjet_pts)

    #Lepton projection
    lep_vec_t = lepton.Vect()
    lep_vec_t.SetZ(0)
    output["L_p"] = (w_lep_t * lep_vec_t) / w_lep.Pt()
    output["L_pw"] = (w_lep_t * lep_vec_t) / (lepton.Pt() * w_lep.Pt())

    # Ht and number of jets with Pt> 20
    # using uncut jets
    Njets = 0
    N_jets_forward = 0
    N_jets_central = 0
    Ht = 0.
    for j_eta, j_pt in zip(other_jets_eta, other_jets_pts):
        # Looking only to jets != b-jets & wjets
        Z = abs((j_eta - mean_eta_b)/ deltaeta_b)
        Njets += 1
        if Z > 0.5:
            N_jets_forward += 1
        else:
            N_jets_central += 1
        # Ht totale
        Ht += j_pt
    # Add b-jets and w-jet to Ht
    for jet in chain(bjets, wjets):
        Ht += jet.Pt()
            
    output["N_jets"] = Njets 
    output["N_jets_central"] = N_jets_central
    output["N_jets_forward"] = N_jets_forward
    output["Ht"] = Ht

    return output



class HHjjlnu_kin(TreeCloner):

    def __init__(self):
        pass

    def __del__(self):
        pass

    def help(self):
        return '''Identify pairs of jets for semileptonic analyses'''

    def addOptions(self,parser):
        description = self.help()
        group = optparse.OptionGroup(parser,self.label, description)
        group.add_option('-d', '--debug',  dest='debug',  help='Debug flag',  default="0")
        group.add_option('--ptminjet',  dest='ptmin_jet',  help='Min Pt for jets',  default=20.)
        parser.add_option_group(group)
        return group


    def checkOptions(self,opts):
        self.debug = (opts.debug == "1")
        self.ptmin_jet = float(opts.ptmin_jet)

    def process(self,**kwargs):
        print module_name

        tree  = kwargs['tree']
        input = kwargs['input']
        output = kwargs['output']

        self.connect(tree,input)

        variables = {}
        self.clone(output,  hh_branches["F"]+hh_branches["I"])

        for br in hh_branches["F"]:
            variables[br] = numpy.zeros(1, dtype=numpy.float32)
            self.otree.Branch(br, variables[br], "{}/F".format(br))
        for br in hh_branches["I"]:
            variables[br] = numpy.zeros(1, dtype=numpy.int32)
            self.otree.Branch(br, variables[br], "{}/I".format(br))
       

        nentries = self.itree.GetEntries()
        print 'Total number of entries: ',nentries 

        # avoid dots to go faster
        itree     = self.itree
        otree     = self.otree

        print '- Starting eventloop'
        step = 5000
        for i in xrange(nentries):
            itree.GetEntry(i)
            if i > 0 and i%step == 0.:
                print i,'events processed :: ', nentries

            # Check if we have at least 4 jets with pt > ptmin
            # and VBSjets and Vjets are all associated
            if (not itree.std_vector_jet_pt[3] >= self.ptmin_jet) or  \
                -1 in itree.H_jets or -1 in itree.W_jets:
                for var in variables:
                    variables[var][0] = -9999
            else:
                if self.debug:
                    print "Hjets", [i for i in itree.H_jets]
                    print "Wjets", [j for j in itree.W_jets]

                bjets = utils.get_jets_byindex(itree, itree.H_jets, self.ptmin_jet, self.debug)
                wjets = utils.get_jets_byindex(itree, itree.W_jets, self.ptmin_jet, self.debug)
                
                lepton = TLorentzVector()
                plep = itree.std_vector_lepton_pt[0] * cosh(itree.std_vector_lepton_eta[0])
                lepton.SetPtEtaPhiE(itree.std_vector_lepton_pt[0], itree.std_vector_lepton_eta[0],
                                    itree.std_vector_lepton_phi[0], plep)
                
                met = TLorentzVector()
                met.SetPtEtaPhiE(itree.metPfType1, 0., itree.metPfType1Phi, itree.metPfType1)

                other_jets_eta = []
                other_jets_pts = []
                for i, ( eta, pt) in enumerate(zip(itree.std_vector_jet_eta, itree.std_vector_jet_pt)):
                    if i not in itree.H_jets and i not in itree.W_jets and pt >= self.ptmin_jet and abs(eta)<10:
                        other_jets_eta.append(eta)
                        other_jets_pts.append(pt)
    
                output =  getVBSkinematics(bjets, wjets, lepton, met, 
                                            other_jets_eta, other_jets_pts, self.debug)

                if self.debug:
                    print output

                for vk, vvalue in variables.items():
                    vvalue[0] = output[vk]
                
            otree.Fill()
  
        self.disconnect()
        print '- Eventloop completed'
