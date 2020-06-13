from itertools import chain
from math import cosh, sqrt, cos
from ROOT import TLorentzVector

VBSjjlnu_branches  = {
        "F": [
            "vbs_0_pt", "vbs_0_eta", "vbs_0_phi", "vbs_0_E",
            "vbs_1_pt", "vbs_1_eta", "vbs_1_phi", "vbs_1_E",
            "vjet_0_pt", "vjet_0_eta", "vjet_0_phi", "vjet_0_E",
            "vjet_1_pt", "vjet_1_eta", "vjet_1_phi", "vjet_1_E",
            "mjj_vbs", "mjj_vjet",
            "deltaeta_vbs",  "deltaphi_vbs", 
            "deltaeta_vjet", "deltaphi_vjet", 
            "deltaR_lep_vbs", "deltaR_lep_vjet",
            "deltaphi_lep_nu", "deltaeta_lep_nu",
            "deltaR_lep_nu", "deltaR_vbs", "deltaR_vjet",
            "Rvjets_0", "Rvjets_1",
            "Zvjets_0", "Zvjets_1", "Zlep",
            "Asym_vbs", "Asym_vjet", "Mw_lep", "Mtw_lep", "w_lep_pt", "w_had_pt",
            "Mww", "R_ww", "R_mw", "A_ww",
            "Centr_vbs", "Centr_ww", "Lep_proj", "Lep_projw",
            "recoMET", "recoMET_pz" ,
            ],
        "I": ["N_jets", "N_jets_forward", "N_jets_central"]
    }

VBSjjlnu_vector_branches = [
    {
        "type": "I",
        "len": "N_jets", 
        "name": "other_jets_index"
    },
    {
        "type": "F", 
        "len": 4, 
        "name": "VBS_Whad_vec"
    },
    {
        "type": "F", 
        "len": 4, 
        "name": "VBS_Wlep_vec"
    }
]


def getDefault():
    output = {}
    for br in VBSjjlnu_branches["F"]:
        output[br] = -999.
    for br in VBSjjlnu_branches["I"]:
        output[br] = -999
    for vec_br in VBSjjlnu_vector_branches:
        if type(vec_br["len"]) == int:
            output[vec_br["name"]] = [-999.]*vec_br["len"]
        else:
            output[vec_br["name"]] = []
    return output


def getVBSkin_resolved(vbsjets, vjets, lepton, met, reco_neutrino, other_jets, other_jets_ind, debug=False):
    output = getDefault()
    # variables extraction
    total_vbs = TLorentzVector(0,0,0,0)
    vbs_etas = []
    vbs_phis = []
    vbs_pts = []
    vbs_Es = []
    for i, j in enumerate(vbsjets):
        total_vbs+= j
        vbs_etas.append(j.Eta())
        vbs_phis.append(j.Phi())
        vbs_pts.append(j.Pt())
        vbs_Es.append(j.E())
    if debug:
        print "VBS pts", vbs_pts
        print "VBS etas", vbs_etas
    deltaeta_vbs = abs(vbs_etas[0]- vbs_etas[1])
    mean_eta_vbs = sum(vbs_etas) / 2 
    output["vbs_0_pt"] = vbs_pts[0]
    output["vbs_1_pt"] = vbs_pts[1]
    output["vbs_0_eta"] = vbs_etas[0]
    output["vbs_1_eta"] = vbs_etas[1]
    output["vbs_0_phi"] = vbs_phis[0]
    output["vbs_1_phi"] = vbs_phis[1]
    output["vbs_0_E"] = vbs_Es[0]
    output["vbs_1_E"] = vbs_Es[1]
    output["mjj_vbs"] = total_vbs.M()
    output["deltaeta_vbs"] = deltaeta_vbs
    output["deltaphi_vbs"] = abs(vbsjets[0].DeltaPhi(vbsjets[1]))
    output["deltaR_vbs"] = vbsjets[0].DrEtaPhi(vbsjets[1])
    
    total_vjet = TLorentzVector(0,0,0,0)
    vjet_etas = []
    vjet_phis = []
    vjet_pts = []
    vjet_Es = []
    for i, j in enumerate(vjets):
        total_vjet += j
        vjet_etas.append(j.Eta())
        vjet_phis.append(j.Phi())
        vjet_pts.append(j.Pt())
        vjet_Es.append(j.E())
    if debug:
        print "Vjet pts", vjet_pts
        print "Vjet etas", vjet_etas
    output["vjet_0_pt"] = vjet_pts[0]
    output["vjet_1_pt"] = vjet_pts[1]
    output["vjet_0_eta"] = vjet_etas[0]
    output["vjet_1_eta"] = vjet_etas[1]
    output["vjet_0_phi"] = vjet_phis[0]
    output["vjet_1_phi"] = vjet_phis[1]
    output["vjet_0_E"] = vjet_Es[0]
    output["vjet_1_E"] = vjet_Es[1]
    output["mjj_vjet"] = total_vjet.M()
    output["deltaphi_vjet"] =  abs(vjets[0].DeltaPhi(vjets[1]))
    output["deltaeta_vjet"] = abs(vjet_etas[0] - vjet_etas[1])
    output["deltaR_vjet"] = vjets[0].DrEtaPhi(vjets[1])
    
    output["recoMET"] = reco_neutrino.Pt()
    output["recoMET_pz"] = reco_neutrino.Pz() 
    output["deltaphi_lep_nu"] = abs(lepton.DeltaPhi(reco_neutrino)) 
    output["deltaeta_lep_nu"] = abs(lepton.Eta() - reco_neutrino.Eta())
    output["deltaR_lep_nu"] = lepton.DrEtaPhi(reco_neutrino)    
    # Look for nearest vbs jet from lepton
    output["deltaR_lep_vbs"] = min( [ lepton.DrEtaPhi(vbsjets[0]), lepton.DrEtaPhi(vbsjets[1])])
    output["deltaR_lep_vjet"] = min( [ lepton.DrEtaPhi(vjets[0]), lepton.DrEtaPhi(vjets[1])])
    # Zeppenfeld variables
    if deltaeta_vbs != 0:
        output["Zvjets_0"] = (vjet_etas[0] - mean_eta_vbs)/ deltaeta_vbs
        output["Zvjets_1"] = (vjet_etas[1] - mean_eta_vbs)/ deltaeta_vbs
        output["Zlep"] = (lepton.Eta() - mean_eta_vbs)/ deltaeta_vbs
    #R variables
    ptvbs01  = vbsjets[0].Pt() * vbsjets[1].Pt() 
    output["Rvjets_0"] = (lepton.Pt() * vjets[0].Pt()) / ptvbs01
    output["Rvjets_1"] = (lepton.Pt() * vjets[1].Pt()) / ptvbs01
    #Asymmetry
    output["Asym_vbs"]  = (vbs_pts[0] - vbs_pts[1]) / sum(vbs_pts)
    output["Asym_vjet"] = (vjet_pts[0] - vjet_pts[1]) / sum(vjet_pts)
    #WW variables
    w_lep = lepton + reco_neutrino
    w_had = vjets[0] + vjets[1]

    # Save four momenta
    output["VBS_Wlep_vec"] = [w_lep.Pt(), w_lep.Eta(), w_lep.Phi(), w_lep.M()]
    output["VBS_Whad_vec"] = [w_had.Pt(), w_had.Eta(), w_had.Phi(), w_had.M()]

    w_lep_t = w_lep.Vect()
    w_lep_t.SetZ(0)
    w_had_t = w_had.Vect()
    w_had_t.SetZ(0)
    ww_vec = w_lep + w_had
    output["w_lep_pt"] = w_lep.Pt()
    output["w_had_pt"] = w_had_t.Pt()

    output["Mw_lep"] = w_lep.M()
    #output["Mtw_lep"] = w_lep_t.M()
    output["Mtw_lep"] = sqrt(2 * lepton.Pt() * met.Pt() * (1 - cos( lepton.DeltaPhi(met))));
    
    output["Mww"] = ww_vec.M()
    output["R_ww"] = (w_lep.Pt() * w_lep.Pt()) / ptvbs01
    output["R_mw"] = ww_vec.M() / ptvbs01
    output["A_ww"] = (w_lep_t + w_had_t).Pt() / (w_lep.Pt() + w_had.Pt())
    #Centrality
    eta_ww = (w_lep.Eta() + w_had.Eta())/2
    if deltaeta_vbs != 0.:
        output["Centr_vbs"] = abs(deltaeta_vbs - eta_ww) / deltaeta_vbs
    deltaeta_plus = max(vbs_etas) - max([w_lep.Eta(), w_had.Eta()])
    deltaeta_minus = min([w_lep.Eta(), w_had.Eta()]) - min(vbs_etas)
    output["Centr_ww"] = min([deltaeta_plus, deltaeta_minus])
    #Lepton projection
    lep_vec_t = lepton.Vect()
    lep_vec_t.SetZ(0)
    output["Lep_proj"] = (w_lep_t * lep_vec_t) / w_lep.Pt()
    output["Lep_projw"] = (w_lep_t * lep_vec_t) / (lepton.Pt() * w_lep.Pt())
    # Ht and number of jets with Pt> 20
    # using uncut jets
    Njets = len(other_jets)
    N_jets_forward = 0
    N_jets_central = 0
    for oj in other_jets:
        j_eta, j_pt = oj.Eta(), oj.Pt()
        # Looking only to jets != vbs & vjets
        if deltaeta_vbs != 0.:
            Z = abs((j_eta - mean_eta_vbs)/ deltaeta_vbs)
            if Z > 0.5:
                N_jets_forward += 1
            else:
                N_jets_central += 1
            
    output["N_jets"] = Njets 
    output["N_jets_central"] = N_jets_central
    output["N_jets_forward"] = N_jets_forward
    output["other_jets_index"] = other_jets_ind
    return output

def getVBSkin_boosted(vbsjets, fatjet, lepton, met, reco_neutrino, other_jets, other_jets_ind, debug=False):
    output = getDefault()
    # variables extraction
    total_vbs = TLorentzVector(0,0,0,0)
    vbs_etas = []
    vbs_phis = []
    vbs_pts = []
    vbs_Es = []
    for i, j in enumerate(vbsjets):
        total_vbs+= j
        vbs_etas.append(j.Eta())
        vbs_phis.append(j.Phi())
        vbs_pts.append(j.Pt())
        vbs_Es.append(j.E())
    if debug:
        print "VBS pts", vbs_pts
        print "VBS etas", vbs_etas
    deltaeta_vbs = abs(vbs_etas[0]- vbs_etas[1])
    mean_eta_vbs = sum(vbs_etas) / 2 
    output["vbs_0_pt"] = vbs_pts[0]
    output["vbs_1_pt"] = vbs_pts[1]
    output["vbs_0_eta"] = vbs_etas[0]
    output["vbs_1_eta"] = vbs_etas[1]
    output["vbs_0_phi"] = vbs_phis[0]
    output["vbs_1_phi"] = vbs_phis[1]
    output["vbs_0_E"] = vbs_Es[0]
    output["vbs_1_E"] = vbs_Es[1]
    output["mjj_vbs"] = total_vbs.M()
    output["deltaeta_vbs"] = deltaeta_vbs
    output["deltaphi_vbs"] = abs(vbsjets[0].DeltaPhi(vbsjets[1]))
    output["deltaR_vbs"] = vbsjets[0].DrEtaPhi(vbsjets[1])

    total_vjet = fatjet
    vjet_eta = fatjet.Eta()
    vjet_pt = fatjet.Pt()
    if debug:
        print "Vjet pt", vjet_pt
        print "Vjet eta", vjet_eta
    output["vjet_0_pt"] = vjet_pt
    output["vjet_0_eta"] = vjet_eta
    output["vjet_0_phi"] = fatjet.Phi()
    output["vjet_0_E"] = fatjet.E()
    output["mjj_vjet"] = total_vjet.M()

    output["recoMET"] = reco_neutrino.Pt()
    output["recoMET_pz"] = reco_neutrino.Pz() 
    output["deltaphi_lep_nu"] = abs(lepton.DeltaPhi(reco_neutrino)) 
    output["deltaeta_lep_nu"] = abs(lepton.Eta() - reco_neutrino.Eta())
    output["deltaR_lep_nu"] = lepton.DrEtaPhi(reco_neutrino)

    # Look for nearest vbs jet from lepton
    output["deltaR_lep_vbs"] = min( [ lepton.DrEtaPhi(vbsjets[0]), lepton.DrEtaPhi(vbsjets[1])])
    output["deltaR_lep_vjet"] = lepton.DrEtaPhi(fatjet)
    # Zeppenfeld variables
    if deltaeta_vbs != 0.:
        output["Zvjets_0"] = (vjet_eta - mean_eta_vbs)/ deltaeta_vbs
        output["Zlep"] = (lepton.Eta() - mean_eta_vbs)/ deltaeta_vbs
    #R variables
    ptvbs01  = vbsjets[0].Pt() * vbsjets[1].Pt() 
    output["Rvjets_0"] = (lepton.Pt() * vjet_pt) / ptvbs01
    #Asymmetry
    output["Asym_vbs"]  = (vbs_pts[0] - vbs_pts[1]) / sum(vbs_pts)
    #WW variables
    w_lep = lepton + reco_neutrino
    w_had = fatjet

     # Save four momenta
    output["VBS_Wlep_vec"] = [w_lep.Pt(), w_lep.Eta(), w_lep.Phi(), w_lep.M()]
    output["VBS_Whad_vec"] = [w_had.Pt(), w_had.Eta(), w_had.Phi(), w_had.M()]

    w_lep_t = w_lep.Vect()
    w_lep_t.SetZ(0)
    w_had_t = w_had.Vect()
    w_had_t.SetZ(0)
    ww_vec = w_lep + w_had
    output["w_lep_pt"] = w_lep.Pt()
    output["w_had_pt"] = w_had_t.Pt()

    output["Mw_lep"] = w_lep.M()
    #output["Mtw_lep"] = w_lep_t.M()
    output["Mtw_lep"] = sqrt(2 * lepton.Pt() * met.Pt() * (1 - cos( lepton.DeltaPhi(met))));
    
    output["Mww"] = ww_vec.M()
    output["R_ww"] = (w_lep.Pt() * w_lep.Pt()) / ptvbs01
    output["R_mw"] = ww_vec.M() / ptvbs01
    output["A_ww"] = (w_lep_t + w_had_t).Pt() / (w_lep.Pt() + w_had.Pt())
    #Centrality
    eta_ww = (w_lep.Eta() + w_had.Eta())/2
    if deltaeta_vbs != 0.:
        output["Centr_vbs"] = abs(deltaeta_vbs - eta_ww) / deltaeta_vbs
    deltaeta_plus = max(vbs_etas) - max([w_lep.Eta(), w_had.Eta()])
    deltaeta_minus = min([w_lep.Eta(), w_had.Eta()]) - min(vbs_etas)
    output["Centr_ww"] = min([deltaeta_plus, deltaeta_minus])
    #Lepton projection
    lep_vec_t = lepton.Vect()
    lep_vec_t.SetZ(0)
    output["Lep_proj"] = (w_lep_t * lep_vec_t) / w_lep.Pt()
    output["Lep_projw"] = (w_lep_t * lep_vec_t) / (lepton.Pt() * w_lep.Pt())
    # Ht and number of jets with Pt> 20
    # using uncut jets
    Njets = len(other_jets)
    N_jets_forward = 0
    N_jets_central = 0
    for oj in other_jets:
        j_eta, j_pt = oj.Eta(), oj.Pt()
        # Looking only to jets != vbs & vjets
        if deltaeta_vbs != 0.:
            Z = abs((j_eta - mean_eta_vbs)/ deltaeta_vbs)
            if Z > 0.5:
                N_jets_forward += 1
            else:
                N_jets_central += 1
            
    output["N_jets"] = Njets 
    output["N_jets_central"] = N_jets_central
    output["N_jets_forward"] = N_jets_forward
    output["other_jets_index"] = other_jets_ind
    return output