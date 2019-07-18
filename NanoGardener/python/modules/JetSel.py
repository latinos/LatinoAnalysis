import ROOT
ROOT.PyConfig.IgnoreCommandLineOptions = True
import re

from PhysicsTools.NanoAODTools.postprocessing.framework.datamodel import Collection 
from PhysicsTools.NanoAODTools.postprocessing.framework.eventloop import Module
from LatinoAnalysis.NanoGardener.data.common_cfg import Type_dict

class JetSel(Module):
    def __init__(self,jetid=2,pujetid='none',minpt=15.0,maxeta=5.2,jetColl="CleanJet"):
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
        self.itree = inputTree

        # Get List of variables in the collection
        self.CollBr = {}
        oBrList = self.out._tree.GetListOfBranches() 
        for br in oBrList:
            bname = br.GetName()
            btype = Type_dict[br.GetListOfLeaves()[0].GetTypeName()]
            if re.match('\A'+self.jetColl+'_', bname):
                if btype not in self.CollBr: self.CollBr[btype] = []
                self.CollBr[btype].append(bname)
                self.out.branch(bname, btype, lenVar='n'+self.jetColl)    

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

        for typ in self.CollBr: 
          for bname in self.CollBr[typ]:
            temp_b = bname.replace(self.jetColl+'_', '')
            temp_v = [jet_coll[iJet][temp_b] for iJet in order]
            self.out.fillBranch(bname, temp_v )

        return True

