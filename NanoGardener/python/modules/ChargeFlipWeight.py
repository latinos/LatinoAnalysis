import os
import ROOT
import math
ROOT.PyConfig.IgnoreCommandLineOptions = True

from PhysicsTools.NanoAODTools.postprocessing.framework.datamodel import Collection 
from PhysicsTools.NanoAODTools.postprocessing.framework.eventloop import Module

class ChargeFlipWeight(Module):
    def __init__(self, cmssw, MCType ='DY', useData = True , CF_cfg = 'LatinoAnalysis/NanoGardener/python/data/ChargeFlip_cfg.py' , collection="Lepton"):
        self.cmssw = cmssw
        self.MCType = MCType
        self.useData = useData
        cmssw_base = os.getenv('CMSSW_BASE') 
        ScaleFactorFile = cmssw_base + '/src/' + CF_cfg
        if os.path.exists(ScaleFactorFile):
          handle = open(ScaleFactorFile,'r')
          exec(handle)
          handle.close()
        self.SFDic = ChargeFlip[cmssw]
        self.collection = collection
        self.etaMax = 0.  
        self.ptMin  = 9999999.
        self.ptMax  = 0.
        for iLine in self.SFDic['FlipProba'] :  
           if iLine[1] > self.etaMax: self.etaMax = iLine[1] 
           if iLine[2] < self.ptMin : self.ptMin  = iLine[2]
           if iLine[3] > self.ptMax : self.ptMax  = iLine[3]
        self.ptMax  *= 0.9999
        self.etaMax *= 0.9999

    def beginJob(self):
        pass
    def endJob(self):
        pass

    def beginFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        self.out = wrappedOutputTree

        self.out.branch("ChargeFlipSF", "F")
        self.out.branch("ChargeFlipSF_up", "F")
        self.out.branch("ChargeFlipSF_do", "F")

        self.out.branch("ChargeFlipW", "F")
        self.out.branch("ChargeFlipW_0j", "F")
        self.out.branch("ChargeFlipW_1j", "F")
        self.out.branch("ChargeFlipW_2j", "F")
        self.out.branch("ChargeFlipW_vbs", "F")

        self.out.branch("ChargeFlipW_up", "F")
        self.out.branch("ChargeFlipW_0j_up", "F")
        self.out.branch("ChargeFlipW_1j_up", "F")
        self.out.branch("ChargeFlipW_2j_up", "F")
        self.out.branch("ChargeFlipW_vbs_up", "F")

        self.out.branch("ChargeFlipW_do", "F")
        self.out.branch("ChargeFlipW_0j_do", "F")
        self.out.branch("ChargeFlipW_1j_do", "F")
        self.out.branch("ChargeFlipW_2j_do", "F")
        self.out.branch("ChargeFlipW_vbs_do", "F")
    
    def endFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        pass

    def getFlipProba (self,pt_in,eta_in,data=True): 
        if    pt_in < self.ptMin : pt = self.ptMin
        elif  pt_in > self.ptMax : pt = self.ptMax
        else                     : pt = pt_in
        if    eta_in > self.etaMax : eta = self.etaMax
        else                       : eta = eta_in
        for iLine in self.SFDic['FlipProba'] :
          if      pt  >= iLine[2] and  pt  <  iLine[3] and  eta >= iLine[0] and  eta <  iLine[1] :
             if data : 
               val = iLine[4]
               up  = min( 1. , iLine[4] + math.sqrt(iLine[5]**2+iLine[7]**2) )
               do  = max( 0. , iLine[4] - math.sqrt(iLine[5]**2+iLine[6]**2) )
             else:
               val = iLine[8]
               up  = min( 1. , iLine[8] + iLine[9] )
               do  = max( 0. , iLine[8] - iLine[9] )
        return val, up , do

    def getScaleFactor(self,pt_in,eta_in):
        if    pt_in < self.ptMin : pt = self.ptMin
        elif  pt_in > self.ptMax : pt = self.ptMax
        else                     : pt = pt_in
        if    eta_in > self.etaMax : eta = self.etaMax
        else                       : eta = eta_in
        for iLine in self.SFDic['FlipProba'] :
          if      pt  >= iLine[2] and  pt  <  iLine[3] and  eta >= iLine[0] and  eta <  iLine[1] :
             val = iLine[10]
             up  = iLine[10] + math.sqrt(iLine[11]**2+iLine[13]**2)
             do  = max( 0. , iLine[10] - math.sqrt(iLine[11]**2+iLine[12]**2) )
        return val, up , do

    def analyze(self, event):
        """process event, return True (go to next module) or False (fail, go to next event)"""
        leptons = Collection(event, self.collection)
        nLep = len(leptons)
        genLeptons = Collection(event, "LeptonGen" )
        nGenLep = len(genLeptons)  

        CommomW    = 0.
        CommomW_up = 0.
        CommomW_do = 0.

        ChargeFlipW_0j  = 0.
        ChargeFlipW_1j  = 0.
        ChargeFlipW_2j  = 0.
        ChargeFlipW_vbs = 0.

        ChargeFlipW_0j_up  = 0.
        ChargeFlipW_1j_up  = 0.
        ChargeFlipW_2j_up  = 0.
        ChargeFlipW_vbs_up = 0.

        ChargeFlipW_0j_do  = 0.
        ChargeFlipW_1j_do  = 0.
        ChargeFlipW_2j_do  = 0.
        ChargeFlipW_vbs_do = 0.

        ChargeFlipSF     = 1.
        ChargeFlipSF_up  = 1.
        ChargeFlipSF_do  = 1.  

        if nLep >= 2 :
          Epsilon     = []
          Epsilon_Up  = []
          Epsilon_Do  = []
          #print leptons[0].pdgId , leptons[0].pt , leptons[0].eta 
          #print leptons[1].pdgId , leptons[1].pt , leptons[1].eta 
          if abs(leptons[0].pdgId) == 11:
            val , up , do = self.getFlipProba(leptons[0].pt,abs(leptons[0].eta),self.useData) 
            Epsilon     .append(val)
            Epsilon_Up  .append(up)
            Epsilon_Do  .append(do)
          else:
            Epsilon     .append(0.)
            Epsilon_Up  .append(0.)
            Epsilon_Do  .append(0.)
          if abs(leptons[1].pdgId) == 11:
            val , up , do = self.getFlipProba(leptons[1].pt,abs(leptons[1].eta),self.useData)
            Epsilon     .append(val)
            Epsilon_Up  .append(up)
            Epsilon_Do  .append(do)
          else:
            Epsilon     .append(0.)
            Epsilon_Up  .append(0.)
            Epsilon_Do  .append(0.)
          #print Epsilon 
          #print Epsilon_Up 
          #print Epsilon_Do 

          if leptons[0].pdgId*leptons[1].pdgId == -11*11 :
            CommomW    = Epsilon[0] * ( 1.-Epsilon[1] ) + Epsilon[1] * ( 1.-Epsilon[0] ) 
            CommomW_up = Epsilon_Up[0] * ( 1.-Epsilon_Up[1] ) + Epsilon_Up[1] * ( 1.-Epsilon_Up[0] ) 
            CommomW_do = Epsilon_Do[0] * ( 1.-Epsilon_Do[1] ) + Epsilon_Do[1] * ( 1.-Epsilon_Do[0] ) 

            ChargeFlipW_0j  = CommomW / ( 1.-self.SFDic['SSOSMC'][self.MCType]['0j'][0] )
            ChargeFlipW_1j  = CommomW / ( 1.-self.SFDic['SSOSMC'][self.MCType]['1j'][0] )
            ChargeFlipW_2j  = CommomW / ( 1.-self.SFDic['SSOSMC'][self.MCType]['2j'][0] )
            ChargeFlipW_vbs = CommomW / ( 1.-self.SFDic['SSOSMC'][self.MCType]['vbs'][0] )

            ChargeFlipW_0j_up  = CommomW_up / ( 1.-self.SFDic['SSOSMC'][self.MCType]['0j'][0] )
            ChargeFlipW_1j_up  = CommomW_up / ( 1.-self.SFDic['SSOSMC'][self.MCType]['1j'][0] )
            ChargeFlipW_2j_up  = CommomW_up / ( 1.-self.SFDic['SSOSMC'][self.MCType]['2j'][0] )
            ChargeFlipW_vbs_up = CommomW_up / ( 1.-self.SFDic['SSOSMC'][self.MCType]['vbs'][0] )

            ChargeFlipW_0j_do  = CommomW_do / ( 1.-self.SFDic['SSOSMC'][self.MCType]['0j'][0] )
            ChargeFlipW_1j_do  = CommomW_do / ( 1.-self.SFDic['SSOSMC'][self.MCType]['1j'][0] )
            ChargeFlipW_2j_do  = CommomW_do / ( 1.-self.SFDic['SSOSMC'][self.MCType]['2j'][0] )
            ChargeFlipW_vbs_do = CommomW_do / ( 1.-self.SFDic['SSOSMC'][self.MCType]['vbs'][0] )

          elif leptons[0].pdgId*leptons[1].pdgId == -11*13 :
            CommomW    = Epsilon[0]    + Epsilon[1]
            CommomW_up = Epsilon_Up[0] + Epsilon_Up[1]
            CommomW_do = Epsilon_Do[0] + Epsilon_Do[1]

          elif leptons[0].pdgId*leptons[1].pdgId == 11*11 or leptons[0].pdgId*leptons[1].pdgId == 11*13 :
            for genLepton in genLeptons:
              if abs(genLepton.pdgId) == 11 and genLepton.pt > 5 :
                genp4 = ROOT.TLorentzVector()
                genp4.SetPtEtaPhiM(genLepton.pt, genLepton.eta, genLepton.phi, 0)
                for iLep in range(2) :
                  if abs(leptons[iLep].pdgId) == 11: 
                    lepp4 = ROOT.TLorentzVector()
                    lepp4.SetPtEtaPhiM(leptons[iLep].pt, leptons[iLep].eta, leptons[iLep].phi, 0)
                    if genp4.DeltaR(lepp4) < 0.3 and leptons[iLep].pdgId*genLepton.pdgId == -11*11 :             
                      ChargeFlipSF , ChargeFlipSF_up , ChargeFlipSF_do = self.getScaleFactor(leptons[iLep].pt,abs(leptons[iLep].eta))

        #leptonleptonprint CommomW , CommomW_up , CommomW_do 
        #print ChargeFlipW_0j , ChargeFlipW_0j_up , ChargeFlipW_0j_do
        #print ChargeFlipW_1j , ChargeFlipW_1j_up , ChargeFlipW_1j_do
        #print ChargeFlipW_2j , ChargeFlipW_2j_up , ChargeFlipW_2j_do
        #print ChargeFlipW_vbs , ChargeFlipW_vbs_up , ChargeFlipW_vbs_do

        self.out.fillBranch("ChargeFlipSF" , ChargeFlipSF )
        self.out.fillBranch("ChargeFlipSF_up" , ChargeFlipSF_up )
        self.out.fillBranch("ChargeFlipSF_do" , ChargeFlipSF_do )
          
        self.out.fillBranch("ChargeFlipW" , CommomW )
        self.out.fillBranch("ChargeFlipW_up" , CommomW_up )
        self.out.fillBranch("ChargeFlipW_do" , CommomW_do )

        self.out.fillBranch("ChargeFlipW_0j"  , ChargeFlipW_0j )
        self.out.fillBranch("ChargeFlipW_1j"  , ChargeFlipW_1j )
        self.out.fillBranch("ChargeFlipW_2j"  , ChargeFlipW_2j )
        self.out.fillBranch("ChargeFlipW_vbs" , ChargeFlipW_vbs )

        self.out.fillBranch("ChargeFlipW_0j_up"  , ChargeFlipW_0j_up )
        self.out.fillBranch("ChargeFlipW_1j_up"  , ChargeFlipW_1j_up )
        self.out.fillBranch("ChargeFlipW_2j_up"  , ChargeFlipW_2j_up  )
        self.out.fillBranch("ChargeFlipW_vbs_up" , ChargeFlipW_vbs_up )

        self.out.fillBranch("ChargeFlipW_0j_do"  , ChargeFlipW_0j_do )
        self.out.fillBranch("ChargeFlipW_1j_do"  , ChargeFlipW_1j_do )
        self.out.fillBranch("ChargeFlipW_2j_do"  , ChargeFlipW_2j_do )
        self.out.fillBranch("ChargeFlipW_vbs_do" , ChargeFlipW_vbs_do )

#       genLeptons = Collection(event, "LeptonGen")
#       for lepton  in leptons:
#         lepp4 = ROOT.TLorentzVector()
#         lepp4.SetPtEtaPhiM(lepton.pt, lepton.eta, lepton.phi, 0)
#         lepton.isMatched = False
#         lepton.isPromptMatched = False
#         for genLepton in genLeptons:
#           if ( abs(genLepton.pdgId) == 11 or abs(genLepton.pdgId) == 13 ) and \
#                genLepton.status == 1 and \
#                genLepton.p4().DeltaR(lepp4) < 0.3 :
#             lepton.isMatched = True
#             if genLepton.isPrompt or genLepton.isDirectPromptTauDecayProduct:
#               lepton.isPromptMatched = True
#               
#       outGenMatched = []
#       outPromptGenMatched = []
#       for lepton in leptons:
#         outGenMatched.append(lepton.isMatched)    
#         outPromptGenMatched.append(lepton.isPromptMatched)
#       self.out.fillBranch("Lepton_genmatched", outGenMatched)
#       self.out.fillBranch("Lepton_promptgenmatched", outPromptGenMatched)
        return True

