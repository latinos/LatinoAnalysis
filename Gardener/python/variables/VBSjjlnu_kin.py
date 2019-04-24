module_name =    ''' 
'''

import optparse
import numpy
import ROOT
import os.path
from collections import namedtuple
from ROOT import TLorentzVector
from LatinoAnalysis.Gardener.gardening import TreeCloner
import LatinoAnalysis.Gardener.variables.PairingUtils as utils 
import LatinoAnalysis.Gardener.variables.VBS_recoNeutrino as RecoNeutrino

vbs_branches = {
            "D": [ "mjj_vbs", "mjj_vjet",
                "vbs_pt_high", "vbs_pt_low", "vbs_etaprod",
                "vjet_pt_high", "vjet_pt_low", 
                "vbs_eta_high", "vbs_eta_low",
                "vjet_eta_high", "vjet_eta_low",
                "deltaeta_vbs",  "deltaphi_vbs", 
                "deltaeta_vjet", "deltaphi_vjet", 
                "deltaphi_lep_vbs_high", "deltaphi_lep_vbs_low", 
                "deltaeta_lep_vbs_high", "deltaeta_lep_vbs_low", 
                "deltaphi_lep_vjet_high", "deltaphi_lep_vjet_low",
                "deltaeta_lep_vjet_high", "deltaeta_lep_vjet_low",
                "deltaR_lep_vbs", "deltaR_lep_vjet",
                "deltaphi_lep_nu", "deltaeta_lep_nu",
                "deltaR_lep_nu", "deltaR_vbs", "deltaR_vjet",
                "Rvjets_high", "Rvjets_low",
                "Zvjets_high", "Zvjets_low", "Zl",
                "A_vbs", "A_vjet", "Mw_lep", "w_lep_pt", 
                "Mww", "R_ww", "R_mw", "A_ww",
                "C_vbs", "C_ww", "L_p", "L_pw", "Ht"          
                ],
            "I": ["N_jets", "N_jets_forward", "N_jets_central"]
            }


def getVBSkinematics(vbsjets, vjets,lepton, met, ):
    output = {}
    # variables extraction
    total_vbs = TLorentzVector(0,0,0,0)
    vbs_etas = []
    vbs_phis = []
    vbs_pts = []
    for i, j in enumerate(vbsjets):
        total_vbs+= j
        vbs_etas.append(j.Eta())
        vbs_phis.append(j.Phi())
        vbs_pts.append(j.Pt())
    deltaeta_vbs = abs(vbs_etas[0]- vbs_etas[1])
    mean_eta_vbs = sum(vbs_etas) / 2 
    output["vbs_pt_high"] = vbs_pts[0]
    output["vbs_pt_low"] = vbs_pts[1]
    output["mjj_vbs"] = total_vbs.M()
    output["deltaeta_vbs"] = deltaeta_vbs
    output["deltaphi_vbs"] = abs(vbsjets[0].DeltaPhi(vbsjets[1]))
    output["deltaR_vbs"] = vbsjets[0].DrEtaPhi(vbsjets[1])
    output["vbs_etaprod"] = vbs_etas[0]*vbs_etas[1]
    sorted_vbs_etas = sorted(vbs_etas)
    sorted_vjet_etas = sorted(vjet_etas)
    output["eta_vbs_high"] = abs(sorted_vbs_etas[0])
    output["eta_vbs_low"] = abs(sorted_vbs_etas[1])

    total_vjet = TLorentzVector(0,0,0,0)
    vjet_etas = []
    vjet_phis = []
    vjet_pts = []
    for i, j in enumerate(vjets):
        total_vjet += j
        vjet_etas.append(j.Eta())
        vjet_phis.append(j.Phi())
        vjet_pts.append(j.Pt())
    output["vjet_pt_high"] = vjet_pts[0]
    output["vjet_pt_low"] = vjet_pts[1]
    output["mjj_vjet"] = total_vjet.M()
    output["deltaphi_vjet"] =  abs(vjets[0].DeltaPhi(vjets[1]))
    output["deltaeta_vjet"] = abs(vjet_etas[0] - vjet_etas[1])
    output["deltaR_vjet"] = vjets[0].DrEtaPhi(vjets[1])
    output["eta_vjet_high"] = abs(sorted_vjet_etas[0])
    output["eta_vjet_low"] = abs(sorted_vjet_etas[1])

    nu_vec = RecoNeutrino.reconstruct_neutrino(lepton, met)
    output["deltaphi_lep_nu"] = abs(lepton.DeltaPhi(nu_vec)) 
    output["deltaeta_lep_nu"] = abs(lepton.Eta() - nu_vec.Eta())
    output["deltaR_lep_nu"] = lepton.DrEtaPhi(nu_vec)

    # Delta Phi with lepton
    output["deltaphi_lep_vbs_high"] = abs(lepton.DeltaPhi(vbsjets[0]))
    output["deltaphi_lep_vbs_low"] = abs(lepton.DeltaPhi(vbsjets[1]))
    output["deltaphi_lep_vjet_high"] = abs(lepton.DeltaPhi(vjets[0]))
    output["deltaphi_lep_vjet_low"] = abs(lepton.DeltaPhi(vjets[1]))

    # Delta Eta with lepton
    output["deltaeta_lep_vbs_high"] = abs(lepton.Eta() - vbs_etas[0])
    output["deltaeta_lep_vbs_low"]  = abs(lepton.Eta() - vbs_etas[1])
    output["deltaeta_lep_vjet_high"] = abs(lepton.Eta() - vjet_etas[0])
    output["deltaeta_lep_vjet_low"] = abs(lepton.Eta() - vjet_etas[1])
        
    # Look for nearest vbs jet from lepton
    output["deltaR_lep_vbs"] = min( [ lepton.DrEtaPhi(vbsjets[0]), lepton.DrEtaPhi(vbsjets[1])])
    output["deltaR_lep_vjet"] = min( [ lepton.DrEtaPhi(vjets[0]), lepton.DrEtaPhi(vjets[1])])

    # Zeppenfeld variables
    output["Zvjets_high"] = (vjet_etas[0] - mean_eta_vbs)/ deltaeta_vbs
    output["Zvjets_low"] = (vjet_etas[1] - mean_eta_vbs)/ deltaeta_vbs
    output["Zlep"] = (lepton.Eta() - mean_eta_vbs)/ deltaeta_vbs

    #R variables
    ptvbs12  = vbsjets[0].Pt() * vbsjets[1].Pt() 
    output["Rvjets_high"] = (lepton.Pt() * vjets[0].Pt()) / ptvbs12
    output["Rvjets_low"] = (lepton.Pt() * vjets[1].Pt()) / ptvbs12

    #Asymmetry
    output["A_vbs"]  = (vbs_pts[0] - vbs_pts[1]) / sum(vbs_pts)
    output["A_vjet"] = (vjet_pts[0] - vjet_pts[1]) / sum(vjet_pts)

    #WW variables
    w_lep = lepton + nu_vec
    w_had = vjets[0] + vjets[1]
    w_lep_t = w_lep.Vect()
    w_lep_t.SetZ(0)
    w_had_t = w_had.Vect()
    w_had_t.SetZ(0)
    ww_vec = w_lep + w_had
    output["w_lep_pt"] = w_lep.Pt()
    output["Mw_lep"] = w_lep.M()
    output["Mww"] = ww_vec.M()
    output["R_ww"] = (w_lep.Pt() * w_lep.Pt()) / ptvbs12
    output["R_mw"] = ww_vec.M() / ptvbs12
    output["A_ww"] = (w_lep_t + w_had_t).Pt() / (w_lep.Pt() + w_had.Pt())
    
    #Centrality
    eta_ww = (w_lep.Eta() + w_had.Eta())/2
    output["C_vbs"] = abs(vbs_etas[0] - eta_ww - vbs_etas[1]) / deltaeta_vbs
    deltaeta_plus = max(vbs_etas) - max([w_lep.Eta(), w_had.Eta()])
    deltaeta_minus = min([w_lep.Eta(), w_had.Eta()]) - min(vbs_etas)
    output["C_ww"] = min([deltaeta_plus, deltaeta_minus])

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
    for j in event.jets:
        if j not in vbsjets and j not in vjets:
            # Looking only to jets != vbs & vjets
            Z = abs((j.Eta() - mean_eta_vbs)/ deltaeta_vbs)
            Njets += 1
            if Z > 0.5:
                N_jets_forward += 1
            else:
                N_jets_central += 1
        # Ht totale
        Ht += j.Pt()
            
    output["N_jets"] = Njets 
    output["N_jets_central"] = N_jets_central
    output["N_jets_forward"] = N_jets_forward
    output["Ht"] = Ht

    return output



class VBSjjlnu_kin(TreeCloner):

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
        parser.add_option_group(group)
        return group


    def checkOptions(self,opts):
        self.debug = (opts.debug == "1")

    def process(self,**kwargs):
        print module_name

        tree  = kwargs['tree']
        input = kwargs['input']
        output = kwargs['output']

        self.connect(tree,input)

        variables = {}
        self.clone(output,  vbs_branches["F"]+vbs_branches["I"])

        for br in vbs_branches["F"]:
            variables[b] = numpy.zeros(1, dtype=numpy.float32)
            self.otree.Branch(b, variables[b], "{}/F".format(b))
        for br in vbs_branches["I"]:
            variables[b] = numpy.zeros(1, dtype=numpy.int32)
            self.otree.Branch(b, variables[b], "{}/I".format(b))
       

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

            # Check if VBSjets and Vjets are all associated
            if -1 in itree.V_jets or -1 in itree.VBS_jets:
                for var in variables:
                    variables[var][0] = -9999
            
            # Get 4 vectors
            vbsjets = []
            vjets = []

            for vbs_index in itree.VBS_jets:
                vec = TLorentzVector()
                vec.SetPtEtaPhiE(itree.std_vector_jet_pt[vbs_index], 
                                itree.std_vector_jet_eta[vbs_index], 
                                itree.std_vector_jet_phi[vbs_index], 
                                itree.std_vector_jet_mass[vbs_index])
                vbsjets.append(vec)

            for vjet_index in itree.V_jets:
                vec = TLorentzVector()
                vec.SetPtEtaPhiE(itree.std_vector_jet_pt[vjet_index], 
                                itree.std_vector_jet_eta[vjet_index], 
                                itree.std_vector_jet_phi[vjet_index], 
                                itree.std_vector_jet_mass[vjet_index])
                vbsjets.append(vec)
            
            lepton = TLorentzVector()
            lepton.SetPtEtaPhiE(itree.std_vector_lepton_pt[0],
                                itree.std_vector_lepton_eta[0],
                                itree.std_vector_lepton_phi[0],
                                itree.std_vector_lepton_pt[0])
            

            met = TLorentzVector()
            met.SetPt(itree.metPfType1)
            met.SetPhi(itree.metPfType1Phi)

            output =  getVBSkinematics(vbsjets, vjets, lepton, met)
            
            
            for vk, vvalue in variables.items():
                vvalue[0] = output[vk]
                
            otree.Fill()
  
        self.disconnect()
        print '- Eventloop completed'

