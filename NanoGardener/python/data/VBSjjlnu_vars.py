from itertools import chain
from math import cosh, sqrt, cos
from ROOT import TLorentzVector
import LatinoAnalysis.Gardener.variables.VBS_recoNeutrino as RecoNeutrino

VBSjjlnu_branches  = {
        "F": [ "mjj_vbs", "mjj_vjet",
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
            "Zvjets_high", "Zvjets_low", "Zlep",
            "Asym_vbs", "Asym_vjet", "Mw_lep", "Mtw_lep", "w_lep_pt", 
            "Mww", "R_ww", "R_mw", "A_ww",
            "Centr_vbs", "Centr_ww", "Lep_proj", "Lep_projw", "Ht",
            "recoMET", "recoMET_pz" ,"recoMET_nearlep", "recoMET_pz_nearlep" ,
            ],
        "I": ["N_jets", "N_jets_forward", "N_jets_central"]
    }

def getDefault():
    output = {}
    for br in VBSjjlnu_branches["F"]:
        output[br] = -999.
    for br in VBSjjlnu_branches["I"]:
        output[br] = -1
    return output


def getVBSkin_resolved(vbsjets, vjets,lepton, met, other_jets, debug=False):
    output = getDefault()
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
    if debug:
        print "VBS pts", vbs_pts
        print "VBS etas", vbs_etas
    deltaeta_vbs = abs(vbs_etas[0]- vbs_etas[1])
    mean_eta_vbs = sum(vbs_etas) / 2 
    output["vbs_pt_high"] = vbs_pts[0]
    output["vbs_pt_low"] = vbs_pts[1]
    output["mjj_vbs"] = total_vbs.M()
    output["deltaeta_vbs"] = deltaeta_vbs
    output["deltaphi_vbs"] = abs(vbsjets[0].DeltaPhi(vbsjets[1]))
    output["deltaR_vbs"] = vbsjets[0].DrEtaPhi(vbsjets[1])
    output["vbs_etaprod"] = vbs_etas[0]*vbs_etas[1]
    output["vbs_eta_high"] = abs(vbs_etas[0])
    output["vbs_eta_low"] = abs(vbs_etas[1])

    total_vjet = TLorentzVector(0,0,0,0)
    vjet_etas = []
    vjet_phis = []
    vjet_pts = []
    for i, j in enumerate(vjets):
        total_vjet += j
        vjet_etas.append(j.Eta())
        vjet_phis.append(j.Phi())
        vjet_pts.append(j.Pt())
    if debug:
        print "Vjet pts", vjet_pts
        print "Vjet etas", vjet_etas
    output["vjet_pt_high"] = vjet_pts[0]
    output["vjet_pt_low"] = vjet_pts[1]
    output["mjj_vjet"] = total_vjet.M()
    output["deltaphi_vjet"] =  abs(vjets[0].DeltaPhi(vjets[1]))
    output["deltaeta_vjet"] = abs(vjet_etas[0] - vjet_etas[1])
    output["deltaR_vjet"] = vjets[0].DrEtaPhi(vjets[1])
    output["vjet_eta_high"] = abs(vjet_etas[0])
    output["vjet_eta_low"] = abs(vjet_etas[1])

    nu_vec = RecoNeutrino.reconstruct_neutrino(lepton, met,mode="central")
    nu_vec_nearlep = RecoNeutrino.reconstruct_neutrino(lepton, met,mode="pz_lep")
    output["recoMET"] = nu_vec.Pt()
    output["recoMET_pz"] = nu_vec.Pz() 
    output["recoMET_nearlep"] = nu_vec_nearlep.Pt()
    output["recoMET_pz_nearlep"] = nu_vec_nearlep.Pz() 
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
    if deltaeta_vbs != 0:
        output["Zvjets_high"] = (vjet_etas[0] - mean_eta_vbs)/ deltaeta_vbs
        output["Zvjets_low"] = (vjet_etas[1] - mean_eta_vbs)/ deltaeta_vbs
        output["Zlep"] = (lepton.Eta() - mean_eta_vbs)/ deltaeta_vbs
    #R variables
    ptvbs12  = vbsjets[0].Pt() * vbsjets[1].Pt() 
    output["Rvjets_high"] = (lepton.Pt() * vjets[0].Pt()) / ptvbs12
    output["Rvjets_low"] = (lepton.Pt() * vjets[1].Pt()) / ptvbs12
    #Asymmetry
    output["Asym_vbs"]  = (vbs_pts[0] - vbs_pts[1]) / sum(vbs_pts)
    output["Asym_vjet"] = (vjet_pts[0] - vjet_pts[1]) / sum(vjet_pts)
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
    #output["Mtw_lep"] = w_lep_t.M()
    output["Mtw_lep"] = sqrt(2 * lepton.Pt() * met.Pt() * (1 - cos( lepton.DeltaPhi(met))));
    output["Mww"] = ww_vec.M()
    output["R_ww"] = (w_lep.Pt() * w_lep.Pt()) / ptvbs12
    output["R_mw"] = ww_vec.M() / ptvbs12
    output["A_ww"] = (w_lep_t + w_had_t).Pt() / (w_lep.Pt() + w_had.Pt())
    #Centrality
    eta_ww = (w_lep.Eta() + w_had.Eta())/2
    if deltaeta_vbs != 0.:
        output["Centr_vbs"] = abs(vbs_etas[0] - eta_ww - vbs_etas[1]) / deltaeta_vbs
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
    Ht = 0.
    for oj in other_jets:
        j_eta, j_pt = oj.Eta(), oj.Pt()
        # Looking only to jets != vbs & vjets
        if deltaeta_vbs != 0.:
            Z = abs((j_eta - mean_eta_vbs)/ deltaeta_vbs)
            if Z > 0.5:
                N_jets_forward += 1
            else:
                N_jets_central += 1
        # Ht totale
        Ht += j_pt
    # Add vbs and vjet to Ht
    for jet in chain(vbsjets, vjets):
        Ht += jet.Pt()
            
    output["N_jets"] = Njets 
    output["N_jets_central"] = N_jets_central
    output["N_jets_forward"] = N_jets_forward
    output["Ht"] = Ht
    return output

def getVBSkin_boosted(vbsjets, fatjet, lepton, met, other_jets, debug=False):
    output = getDefault()
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
    if debug:
        print "VBS pts", vbs_pts
        print "VBS etas", vbs_etas
    deltaeta_vbs = abs(vbs_etas[0]- vbs_etas[1])
    mean_eta_vbs = sum(vbs_etas) / 2 
    output["vbs_pt_high"] = vbs_pts[0]
    output["vbs_pt_low"] = vbs_pts[1]
    output["mjj_vbs"] = total_vbs.M()
    output["deltaeta_vbs"] = deltaeta_vbs
    output["deltaphi_vbs"] = abs(vbsjets[0].DeltaPhi(vbsjets[1]))
    output["deltaR_vbs"] = vbsjets[0].DrEtaPhi(vbsjets[1])
    output["vbs_etaprod"] = vbs_etas[0]*vbs_etas[1]
    output["vbs_eta_high"] = abs(vbs_etas[0])
    output["vbs_eta_low"] = abs(vbs_etas[1])

    total_vjet = fatjet
    vjet_etas = [fatjet.Eta(),  -999.]
    vjet_phis = [fatjet.Phi(), -999.]
    vjet_pts = [fatjet.Pt(),   -999.]
    if debug:
        print "Vjet pts", vjet_pts
        print "Vjet etas", vjet_etas
    output["vjet_pt_high"] = vjet_pts[0]
    output["vjet_pt_low"] =  vjet_pts[1]
    output["mjj_vjet"] = total_vjet.M()
    output["vjet_eta_high"] = abs(vjet_etas[0])

    nu_vec = RecoNeutrino.reconstruct_neutrino(lepton, met,mode="central")
    nu_vec_nearlep = RecoNeutrino.reconstruct_neutrino(lepton, met,mode="pz_lep")
    output["recoMET"] = nu_vec.Pt()
    output["recoMET_pz"] = nu_vec.Pz() 
    output["recoMET_nearlep"] = nu_vec_nearlep.Pt()
    output["recoMET_pz_nearlep"] = nu_vec_nearlep.Pz() 
    output["deltaphi_lep_nu"] = abs(lepton.DeltaPhi(nu_vec)) 
    output["deltaeta_lep_nu"] = abs(lepton.Eta() - nu_vec.Eta())
    output["deltaR_lep_nu"] = lepton.DrEtaPhi(nu_vec)
    # Delta Phi with lepton
    output["deltaphi_lep_vbs_high"] = abs(lepton.DeltaPhi(vbsjets[0]))
    output["deltaphi_lep_vbs_low"] = abs(lepton.DeltaPhi(vbsjets[1]))
    output["deltaphi_lep_vjet_high"] = abs(lepton.DeltaPhi(fatjet))
    # Delta Eta with lepton
    output["deltaeta_lep_vbs_high"] = abs(lepton.Eta() - vbs_etas[0])
    output["deltaeta_lep_vbs_low"]  = abs(lepton.Eta() - vbs_etas[1])
    output["deltaeta_lep_vjet_high"] = abs(lepton.Eta() - vjet_etas[0])
    # Look for nearest vbs jet from lepton
    output["deltaR_lep_vbs"] = min( [ lepton.DrEtaPhi(vbsjets[0]), lepton.DrEtaPhi(vbsjets[1])])
    output["deltaR_lep_vjet"] = lepton.DrEtaPhi(fatjet)
    # Zeppenfeld variables
    if deltaeta_vbs != 0.:
        output["Zvjets_high"] = (vjet_etas[0] - mean_eta_vbs)/ deltaeta_vbs
        output["Zlep"] = (lepton.Eta() - mean_eta_vbs)/ deltaeta_vbs
    #R variables
    ptvbs12  = vbsjets[0].Pt() * vbsjets[1].Pt() 
    output["Rvjets_high"] = (lepton.Pt() * fatjet.Pt()) / ptvbs12
    #Asymmetry
    output["Asym_vbs"]  = (vbs_pts[0] - vbs_pts[1]) / sum(vbs_pts)
    #WW variables
    w_lep = lepton + nu_vec
    w_had = fatjet
    w_lep_t = w_lep.Vect()
    w_lep_t.SetZ(0)
    w_had_t = w_had.Vect()
    w_had_t.SetZ(0)
    ww_vec = w_lep + w_had
    output["w_lep_pt"] = w_lep.Pt()
    output["Mw_lep"] = w_lep.M()
    #output["Mtw_lep"] = w_lep_t.M()
    output["Mtw_lep"] = sqrt(2 * lepton.Pt() * met.Pt() * (1 - cos( lepton.DeltaPhi(met))));
    output["Mww"] = ww_vec.M()
    output["R_ww"] = (w_lep.Pt() * w_lep.Pt()) / ptvbs12
    output["R_mw"] = ww_vec.M() / ptvbs12
    output["A_ww"] = (w_lep_t + w_had_t).Pt() / (w_lep.Pt() + w_had.Pt())
    #Centrality
    eta_ww = (w_lep.Eta() + w_had.Eta())/2
    if deltaeta_vbs != 0.:
        output["Centr_vbs"] = abs(vbs_etas[0] - eta_ww - vbs_etas[1]) / deltaeta_vbs
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
    Ht = 0.
    for oj in other_jets:
        j_eta, j_pt = oj.Eta(), oj.Pt()
        # Looking only to jets != vbs & vjets
        if deltaeta_vbs != 0.:
            Z = abs((j_eta - mean_eta_vbs)/ deltaeta_vbs)
            if Z > 0.5:
                N_jets_forward += 1
            else:
                N_jets_central += 1
        # Ht totale
        Ht += j_pt
    # Add vbs and vjet to Ht
    for jet in chain(vbsjets, [fatjet]):
        Ht += jet.Pt()
            
    output["N_jets"] = Njets 
    output["N_jets_central"] = N_jets_central
    output["N_jets_forward"] = N_jets_forward
    output["Ht"] = Ht
    return output