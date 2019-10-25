import ROOT
ROOT.PyConfig.IgnoreCommandLineOptions = True
import re

from PhysicsTools.NanoAODTools.postprocessing.framework.datamodel import Collection 
from PhysicsTools.NanoAODTools.postprocessing.framework.eventloop import Module
from LatinoAnalysis.NanoGardener.data.common_cfg import Type_dict

class WhadJetSel(Module):
    def __init__(self,jetid=1,pujetid='none',minpt=30.0,maxeta=2.4,jetColl="CleanJet"):
        # Jet ID flags bit1 is loose (always false in 2017 since it does not exist), bit2 is tight, bit3 is tightLepVeto
        # jetId = userInt('tightId')*2+4*userInt('tightIdLepVeto')
        # >=2 -> ask tightId
        # >=4 -> ask tightIdLepVeto
        # >=6 -> ask tightId+tightIdLepVeto  
        # see https://twiki.cern.ch/twiki/bin/viewauth/CMS/JetID for jetID definition
        self.jetid   = jetid
        # Jet PU ID: nanoAOD Jet_puId = miniAOD jet.userInt("pileupJetId:fullId")
        # loose:    bool(j.userInt("pileupJetId:fullId") & (1 << 2)), 
        # medium:   bool(j.userInt("pileupJetId:fullId") & (1 << 1)), 
        # tight:    bool(j.userInt("pileupJetId:fullId") & (1 << 0)) 
        self.pujetid = pujetid
        self.minpt   = minpt
        self.maxeta  = maxeta 
        self.jetColl = jetColl
    def beginJob(self):
        pass
    def endJob(self):
        pass
    def beginFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        
        self.out = wrappedOutputTree
        self.out.branch('Whad_px','F')
        self.out.branch('Whad_py','F')
        self.out.branch('Whad_pz','F')
        self.out.branch('Whad_E','F')
        
        self.out.branch('Whad_pt','F')
        self.out.branch('Whad_eta','F')
        self.out.branch('Whad_phi','F')
        self.out.branch('Whad_mass','F')

        self.out.branch('idx_j1','I')
        self.out.branch('idx_j2','I')


    def endFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        pass
    
    def analyze(self, event):
        """process event, return True (go to next module) or False (fail, go to next event)"""


        jet_coll = Collection(event, self.jetColl )
        nJet     = jet_coll._len
        if 'Clean' in self.jetColl : ori_jet_coll = Collection(event, self.jetColl.replace('Clean',''))
        order = []
        for iJet in range(nJet):
          pt  = jet_coll[iJet]['pt']
          eta = jet_coll[iJet]['eta']
          if 'Clean' in self.jetColl : 
             jetId = ori_jet_coll[jet_coll[iJet]['jetIdx']]['jetId']
             puId  = ori_jet_coll[jet_coll[iJet]['jetIdx']]['puId']
          else                       : 
             jetId = jet_coll[iJet]['jetId']
             puId  = jet_coll[iJet]['puId']
          pu_loose  = bool(puId & (1 << 2))
          pu_medium = bool(puId & (1 << 1))
          pu_tight  = bool(puId & (1 << 0))

          goodJet = True
          if pt         <  self.minpt   : goodJet = False    
          if abs(eta)   >  self.maxeta  : goodJet = False 
          if jetId      <  self.jetid   : goodJet = False
          if self.pujetid == 'loose'  and not pu_loose  : goodJet = False
          if self.pujetid == 'medium' and not pu_medium : goodJet = False
          if self.pujetid == 'tight'  and not pu_tight  : goodJet = False
          if self.pujetid == 'custom' and pt <= 50 :
            if not pu_loose  : goodJet = False
            #if abs(eta) > 2.5 and not pu_medium : goodJet = False

          if goodJet : order.append(iJet)



        ##Select best pair for Whad
        ##if there's no pair , indices will have -1
        #temp_v = [jet_coll[iJet][temp_b] for iJet in order]
        
        idx_j1=-1
        idx_j2=-1
        whad_pt=-1.
        whad_eta=-1.
        whad_phi=-1.
        whad_mass=-1.
        whad_px=-1.
        whad_py=-1.
        whad_pz=-1.
        whad_E=-1.

        wmass=80.4
        dM=9999.
        for iJet in order:
            for jJet in order:
                if jJet <= iJet: continue
                
                v1=ROOT.TLorentzVector()
                v2=ROOT.TLorentzVector()
                if 'Clean' in self.jetColl : 
                    jet_pt1  = ori_jet_coll[jet_coll[iJet]['jetIdx']]['pt']
                    jet_eta1 = ori_jet_coll[jet_coll[iJet]['jetIdx']]['eta']
                    jet_phi1  = ori_jet_coll[jet_coll[iJet]['jetIdx']]['phi']
                    jet_mass1 = ori_jet_coll[jet_coll[iJet]['jetIdx']]['mass']

                    jet_pt2  = ori_jet_coll[jet_coll[jJet]['jetIdx']]['pt']
                    jet_eta2 = ori_jet_coll[jet_coll[jJet]['jetIdx']]['eta']
                    jet_phi2  = ori_jet_coll[jet_coll[jJet]['jetIdx']]['phi']
                    jet_mass2 = ori_jet_coll[jet_coll[jJet]['jetIdx']]['mass']
                    
                else : 
                    jet_pt1  = jet_coll[iJet]['pt']
                    jet_eta1 = jet_coll[iJet]['eta']
                    jet_phi1  = jet_coll[iJet]['phi']
                    jet_mass1 = jet_coll[iJet]['mass']

                    jet_pt2  = jet_coll[jJet]['pt']
                    jet_eta2 = jet_coll[jJet]['eta']
                    jet_phi2  = jet_coll[jJet]['phi']
                    jet_mass2 = jet_coll[jJet]['mass']

                    
                v1.SetPtEtaPhiM(jet_pt1,jet_eta1,jet_phi1,jet_mass1)
                v2.SetPtEtaPhiM(jet_pt2,jet_eta2,jet_phi2,jet_mass2)
                M12=(v1+v2).M()
                this_dM = abs(M12-wmass)
                if this_dM < dM:
                    idx_j1=iJet
                    idx_j2=jJet
                    whad_pt=(v1+v2).Pt()
                    whad_eta=(v1+v2).Eta()
                    whad_phi=(v1+v2).Phi()
                    whad_mass=(v1+v2).M()
                    whad_px=(v1+v2).Px()
                    whad_py=(v1+v2).Py()
                    whad_pz=(v1+v2).Pz()
                    whad_E=(v1+v2).E()
                    dM = this_dM


        #self.out.fillBranch()

        self.out.fillBranch('Whad_px',whad_px)
        self.out.fillBranch('Whad_py',whad_py)
        self.out.fillBranch('Whad_pz',whad_pz)
        self.out.fillBranch('Whad_E',whad_E)

        self.out.fillBranch('Whad_pt',whad_pt)
        self.out.fillBranch('Whad_eta',whad_eta)
        self.out.fillBranch('Whad_phi',whad_phi)
        self.out.fillBranch('Whad_mass',whad_mass)

        self.out.fillBranch('idx_j1',idx_j1)
        self.out.fillBranch('idx_j2',idx_j2)





        return True


