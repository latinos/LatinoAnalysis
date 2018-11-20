import optparse
import numpy
import ROOT
import os.path
import math
import random
import re
from PhysicsTools.NanoAODTools.postprocessing.framework.eventloop import Module
from PhysicsTools.NanoAODTools.postprocessing.framework.datamodel import Collection
from PhysicsTools.NanoAODTools.postprocessing.framework.datamodel import Object
from LatinoAnalysis.NanoGardener.data.common_cfg import Type_dict

class rochester_corr(Module):

    '''                                                                                                                                                                                                            
    Add a scale factor from 2017 Rochester corrections                                                                                                                                                             
    '''

    def __init__(self,isdata = False):
        self.isdata = isdata
        print "Loading macros from /afs/cern.ch/work/a/alvareza/public/CMSSW_9_4_9/src/LatinoAnalysis/NanoGardener/python/modules/RoccoR.cc"
        try:
            ROOT.gROOT.LoadMacro('/afs/cern.ch/work/a/alvareza/public/CMSSW_9_4_9/src/LatinoAnalysis/NanoGardener/python/modules/RoccoR.cc+g')                                                                    
        except RuntimeError: 
            ROOT.gROOT.LoadMacro('/afs/cern.ch/work/a/alvareza/public/CMSSW_9_4_9/src/LatinoAnalysis/NanoGardener/python/modules/RoccoR.cc++g')      
        print "Loaded"  

        rochester_path="/afs/cern.ch/work/a/alvareza/public/CMSSW_9_4_9/src/LatinoAnalysis/NanoGardener/python/data/RoccoR2017v0.txt"        
        print "scale factors from", rochester_path
        rc=ROOT.RoccoR(rochester_path)
        self.rc= rc        
        pass

    def beginJob(self): 
        pass

    def endJob(self):
        pass

    def beginFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        self.initReaders(inputTree) # initReaders must be called in beginFile
        self.out = wrappedOutputTree

        # New Branches (optional)
        self.out.branch('Lepton_rochesterMCSF',   'F', lenVar='nLepton')
        self.out.branch('Lepton_rochesterDataSF', 'F', lenVar='nLepton')
        #self.out.branch('Lepton_rochesterMCSFerr',   'F', lenVar='nLepton')
        #self.out.branch('Lepton_rochesterDataSFerr', 'F', lenVar='nLepton')
        
        # Old branches to clean
        self.br_list_F=['Lepton_pt','Lepton_eta','Lepton_phi','Lepton_eCorr']
        self.br_list_I=['Lepton_pdgId','Lepton_electronIdx','Lepton_muonIdx','Lepton_isLoose','Lepton_isVeto','Lepton_isWgs',
                   'Lepton_isTightMuon_cut_Tight_HWWW','Lepton_isTightElectron_mvaFall17Iso_WP90','Lepton_isTightElectron_mvaFall17Iso_WP90_SS']
        for bname in self.br_list_F:
            self.out.branch(bname, 'F', lenVar='nLepton')
        for bname in self.br_list_I:
            self.out.branch(bname, 'I', lenVar='nLepton')
        self.out.branch('MET_pt','F')
        self.out.branch('MET_phi','F')

    def endFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        pass

    def initReaders(self,tree): # this function gets the pointers to Value and ArrayReaders and sets them in the C++ worker class                                                                              
        self._ttreereaderversion = tree._ttreereaderversion # self._ttreereaderversion must be set AFTER all calls to tree.valueReader or tree.arrayReader                                                       
        pass

    def _corMET (self,met,lpt_org,lpt):
        newmet = met + lpt_org - lpt
        return newmet

    def howCloseIsAToB(self, a_Eta, a_Phi, b_Eta, b_Phi) :
        dPhi = ROOT.TMath.Abs(b_Phi - a_Phi)
        if dPhi > ROOT.TMath.Pi() :
            dPhi = 2*ROOT.TMath.Pi() - dPhi
        dR2 = (b_Eta - a_Eta) * (b_Eta - a_Eta) + dPhi * dPhi
        #print ">> dR = ", math.sqrt(dR2), " :: ", dPhi, " (+) ", (b_Eta - a_Eta)                                                                                                                                 
        return dR2

    def analyze(self, event):
        lepton_col   = Collection(event, 'Lepton')
        muon_col = Collection(event, 'Muon')
        nLep = len(lepton_col)
        if self.isdata == False : # gen level colection for MC
            genlepton_col = Collection(event, 'LeptonGen')
            ngenLep = len(genlepton_col)

        met = Object(event, 'MET')
        met_org = ROOT.TLorentzVector()
        met_org.SetPtEtaPhiM(met['pt'], 0, met['phi'], 0)
        newmet = ROOT.TLorentzVector()
        newmet = met_org
        
        l1 = ROOT.TLorentzVector()
        l1_org = ROOT.TLorentzVector()
        newpt_vec=[]
        #optional branches        
        dataSF_vec=[]
        mcSF_vec=[]
        #dataSFerr_vec=[]        
        #mcSFerr_vec=[]        

        for iLep in xrange(nLep) :
            if not (lepton_col[iLep].pt > 0): continue
            pt = lepton_col[iLep].pt
            flavour = lepton_col[iLep].pdgId
            eta = lepton_col[iLep].eta
            phi = lepton_col[iLep].phi
            newpt = pt
            # Muons only                                                                                                                                                                                      
            if  abs(flavour) == 13 :
                charge = int(flavour/abs(flavour))
                #print charge, pt, eta, phi, nl, genpt, u1, u2                                                                                                                                                

                if self.isdata == True :
                    #for each data muon in the loop, use this function to get a scale factor for its momentum                                                                                                 
                    dataSF = self.rc.kScaleDT(charge,pt,eta,phi)
                    #dataSFerr= self.rc.kScaleDTerror(charge,pt,eta,phi)
                    if dataSF < 0.5 or dataSF > 1.5 or math.isnan(dataSF) == 1 :
                        dataSF = 1
                    newpt= pt*dataSF
                    dataSF_vec.append(dataSF)
                    #dataSFerr_vec.append(dataSFerr)
                else :
                    # Look for the Gen lepton that best matches                                                                                                                                               
                    minimumdR2 = 10
                    matchedgenpt = -1
                    nl =int(muon_col[lepton_col[iLep].muonIdx].nTrackerLayers)
                    u1 =random.random()
                    for iGenLep in xrange(ngenLep) :
                        if genlepton_col[iGenLep].pt > 0 \
                                and  genlepton_col[iGenLep].status == 1 \
                                and  (abs(genlepton_col[iGenLep].pdgId) == 13)   :
                            # and if the reco lepton is close to this gen lepton                                                                                                                              
                            dR2 = self.howCloseIsAToB(lepton_col[iLep].eta, lepton_col[iLep].phi, genlepton_col[iGenLep].eta, genlepton_col[iGenLep].phi)
                            if dR2 < minimumdR2 :
                                matchedgenpt = genlepton_col[iGenLep].pt
                                minimumdR2 = dR2
                    if matchedgenpt == -1 :
                        u2 =random.random()
                        mcSF = self.rc.kScaleAndSmearMC(charge, pt, eta, phi, nl, u1, u2)                                                                                                                         
                        #mcSFerr = self.rc.kScaleAndSmearMCerror(charge, pt, eta, phi, nl, u1, u2)                                                                                                                         
                    #for MC, if matched gen-level muon (genPt) is available, use this function                                                                                                                
                    else :
                        mcSF = self.rc.kScaleFromGenMC(charge, pt, eta, phi, nl, matchedgenpt, u1)
                        #mcSFerr = self.rc.kScaleFromGenMCerror(charge, pt, eta, phi, nl, matchedgenpt, u1)
                    if mcSF < 0.5 or mcSF > 1.5 or math.isnan(mcSF) == 1 :
                        mcSF = 1
                    newpt= pt*mcSF
                    mcSF_vec.append(mcSF)
                    #mcSFerr_vec.append(mcSFerr)
                    
            else :
                if self.isdata == True :
                    dataSF_vec.append(1)
                    #dataSFerr_vec.append(0)
                else :
                    mcSF_vec.append(1)
                    #mcSFerr_vec.append(0)

            # correct MET and save newpt         
            l1_org.SetPtEtaPhiM(pt,eta,phi,0)
            l1.SetPtEtaPhiM (newpt,eta,phi,0)
            newmet = self._corMET(newmet,l1_org,l1)
            newpt_vec.append(newpt)

        # Reorder
        order=[]
        for idx1, pt1 in enumerate(newpt_vec):
            pt_idx = 0
            for idx2, pt2 in enumerate(newpt_vec):
                if pt1 < pt2 or (pt1 == pt2 and idx1 > idx2): pt_idx += 1
            order.append(pt_idx)

        # Fill branches
        for bname in self.br_list_F:
            if '_pt' in bname:
                temp_v = [newpt_vec[idx] for idx in order]
                self.out.fillBranch(bname, temp_v)
            else:
                temp_b = bname.replace('Lepton_', '')
                temp_v = [lepton_col[idx][temp_b] for idx in order]
                self.out.fillBranch(bname, temp_v)
        for bname in self.br_list_I:
            temp_b = bname.replace('Lepton_', '')
            temp_v = [lepton_col[idx][temp_b] for idx in order]
            self.out.fillBranch(bname, temp_v)

        self.out.fillBranch('MET_pt', newmet.Pt())
        self.out.fillBranch('MET_phi', newmet.Phi())
    
        # Optional branches
        for idx in order:
            if self.isdata == True :
                temp_sf = [dataSF_vec[idx] for idx in order]
                self.out.fillBranch('Lepton_rochesterDataSF', temp_sf)
                #temp_sferr = [dataSFerr_vec[idx] for idx in order]
                #self.out.fillBranch('Lepton_rochesterDataSFerr', temp_sferr)
            else:
                temp_sf = [mcSF_vec[idx] for idx in order]
                self.out.fillBranch('Lepton_rochesterMCSF', temp_sf)
                #temp_sferr = [mcSFerr_vec[idx] for idx in order]
                #self.out.fillBranch('Lepton_rochesterMCSFerr', temp_sferr)

        return True





 


