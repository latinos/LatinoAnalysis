import optparse
import numpy
import ROOT
import os
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
    Add a scale factor from Rochester corrections                                                                                                                                                             
    '''

    def __init__(self,isdata = False , year=2016 , lepColl="Lepton",metColls=['MET','PuppiMET','RawMET','TkMET','ChsMET']):
        cmssw_base = os.getenv('CMSSW_BASE')
        self.isdata = isdata
        print "Loading macros from "+cmssw_base+"/src/LatinoAnalysis/NanoGardener/python/modules/RoccoR_NG.cc"
        try:
            ROOT.gROOT.LoadMacro(cmssw_base+'/src/LatinoAnalysis/NanoGardener/python/modules/RoccoR_NG.cc+g')                                                                    
        except RuntimeError: 
            ROOT.gROOT.LoadMacro(cmssw_base+'/src/LatinoAnalysis/NanoGardener/python/modules/RoccoR_NG.cc++g')      
        print "Loaded"  
     
        if year == 2016 : rochester_path=cmssw_base+"/src/LatinoAnalysis/NanoGardener/python/data/RoccoR2016.txt"
        if year == 2017 : rochester_path=cmssw_base+"/src/LatinoAnalysis/NanoGardener/python/data/RoccoR2017.txt"        
        if year == 2018 : rochester_path=cmssw_base+"/src/LatinoAnalysis/NanoGardener/python/data/RoccoR2018.txt"        
        print "scale factors from", rochester_path
        rc=ROOT.RoccoR_NG(rochester_path)
        self.rc= rc        

        self.lepColl  = lepColl
        self.metColls = metColls

    def beginJob(self): 
        pass

    def endJob(self):
        pass

    def beginFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        self.initReaders(inputTree) # initReaders must be called in beginFile
        self.out = wrappedOutputTree
        
        # Lepton branches to clean
        self.CollBr = {}
        oBrList = self.out._tree.GetListOfBranches()
        for br in oBrList:
            bname = br.GetName()
            btype = Type_dict[br.GetListOfLeaves()[0].GetTypeName()]
            if re.match('\A'+self.lepColl+'_', bname): 
              if not '_rochesterSF' in bname :
                if btype not in self.CollBr: self.CollBr[btype] = []
                self.CollBr[btype].append(bname)
                self.out.branch(bname, btype, lenVar='n'+self.lepColl)   

        # New Lepton Branches (optional)
        self.out.branch(self.lepColl+'_rochesterSF',   'F', lenVar='n'+self.lepColl)
        #self.out.branch(self.lepColl+'_rochesterSFerr',   'F', lenVar='n'+self.lepColl)

        # New/Updated MET
        for iMET in self.metColls:
          self.out.branch(iMET+'_pt','F')
          self.out.branch(iMET+'_phi','F')

    def endFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        pass

    def initReaders(self,tree): # this function gets the pointers to Value and ArrayReaders and sets them in the C++ worker class                                                                              
        self._ttreereaderversion = tree._ttreereaderversion # self._ttreereaderversion must be set AFTER all calls to tree.valueReader or tree.arrayReader                                                       
        pass

    def _corMET (self,metLoc,lpt_orgLoc,lptLoc):
        newmetLoc = metLoc + lpt_orgLoc - lptLoc
        return newmetLoc

    def howCloseIsAToB(self, a_Eta, a_Phi, b_Eta, b_Phi) :
        dPhi = ROOT.TMath.Abs(b_Phi - a_Phi)
        if dPhi > ROOT.TMath.Pi() :
            dPhi = 2*ROOT.TMath.Pi() - dPhi
        dR2 = (b_Eta - a_Eta) * (b_Eta - a_Eta) + dPhi * dPhi
        #print ">> dR = ", math.sqrt(dR2), " :: ", dPhi, " (+) ", (b_Eta - a_Eta)                                                                                                                                 
        return dR2

    def analyze(self, event):
        lepton_col   = Collection(event, self.lepColl)
        muon_col = Collection(event, 'Muon')
        nLep = len(lepton_col)
        if self.isdata == False : # gen level colection for MC
            genlepton_col = Collection(event, 'LeptonGen')
            ngenLep = len(genlepton_col)

        met      = {}
        met_org  = {}
        newmet   = {} 
        for iMET in self.metColls: 
          met[iMET] = Object(event, iMET)
          met_org[iMET] = ROOT.TLorentzVector()
          met_org[iMET].SetPtEtaPhiM(met[iMET]['pt'], 0, met[iMET]['phi'], 0)
          newmet[iMET]  = ROOT.TLorentzVector()
          newmet[iMET].SetPtEtaPhiM(met[iMET]['pt'], 0, met[iMET]['phi'], 0)
        
        l1 = ROOT.TLorentzVector()
        l1_org = ROOT.TLorentzVector()
        newpt_vec=[]
        #optional branches        
        dataSF_vec=[]
        mcSF_vec=[]
        #dataSFerr_vec=[]        
        #mcSFerr_vec=[]        

        for iLep in xrange(nLep) :
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
                        mcSF = self.rc.kSmearMC(charge, pt, eta, phi, nl, u1)                                                                                                                         
                        #mcSFerr = self.rc.kSmearMCerror(charge, pt, eta, phi, nl, u1)
                        # Old functions
                        #u2 =random.random()
                        #mcSF = self.rc.kScaleAndSmearMC(charge, pt, eta, phi, nl, u1, u2)                                                                                                                         
                        #mcSFerr = self.rc.kScaleAndSmearMCerror(charge, pt, eta, phi, nl, u1, u2)                                                                                                                         
                    #for MC, if matched gen-level muon (genPt) is available, use this function                                                                                                                
                    else :
                        mcSF = self.rc.kSpreadMC(charge, pt, eta, phi, matchedgenpt)
                        #mcSFerr = self.rc.kSpreadMCerror(charge, pt, eta, phi, matchedgenpt)
                        # Old functions
                        #mcSF = self.rc.kScaleFromGenMC(charge, pt, eta, phi, nl, matchedgenpt, u1)
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
            for iMET in self.metColls: newmet[iMET] = self._corMET(newmet[iMET],l1_org,l1)
            newpt_vec.append(newpt)

        # Reorder
        order=[]
        for idx1, pt1 in enumerate(newpt_vec):
            pt_idx = 0
            for idx2, pt2 in enumerate(newpt_vec):
                if pt1 < pt2 or (pt1 == pt2 and idx1 > idx2): pt_idx += 1
            order.append(pt_idx)

        # Fill branches
        for typ in self.CollBr: 
          for bname in self.CollBr[typ]:
            temp_b = bname.replace(self.lepColl+'_', '')
            if temp_b == 'pt' :
              temp_v = [newpt_vec[idx] for idx in order]
              self.out.fillBranch(bname, temp_v)
            else:
              temp_v = [lepton_col[idx][temp_b] for idx in order]
              self.out.fillBranch(bname, temp_v)  

        for iMET in self.metColls:
          self.out.fillBranch(iMET+'_pt', newmet[iMET].Pt())
          self.out.fillBranch(iMET+'_phi', newmet[iMET].Phi())
    
        # Optional branches
        for idx in order:
            if self.isdata == True :
                temp_sf = [dataSF_vec[idx] for idx in order]
                self.out.fillBranch('Lepton_rochesterSF', temp_sf)
                #temp_sferr = [dataSFerr_vec[idx] for idx in order]
                #self.out.fillBranch('Lepton_rochesterSFerr', temp_sferr)
            else:
                temp_sf = [mcSF_vec[idx] for idx in order]
                self.out.fillBranch('Lepton_rochesterSF', temp_sf)
                #temp_sferr = [mcSFerr_vec[idx] for idx in order]
                #self.out.fillBranch('Lepton_rochesterSFerr', temp_sferr)

        return True





 


