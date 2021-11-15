import ROOT
ROOT.PyConfig.IgnoreCommandLineOptions = True
import re

from PhysicsTools.NanoAODTools.postprocessing.framework.datamodel import Collection 
from PhysicsTools.NanoAODTools.postprocessing.framework.eventloop import Module
from LatinoAnalysis.NanoGardener.data.common_cfg import Type_dict

class JetSel(Module):
    def __init__(self,jetid=2,pujetid='none',minpt=15.0,maxeta=5.2,jetColl="CleanJet", UL2016fix=False):
        # Jet ID flags bit1 is loose (always false in 2017 and 2018 since it does not exist), bit2 is tight, bit3 is tightLepVeto
        # jetId = userInt('tightId')*2+4*userInt('tightIdLepVeto')
        # >=2 -> at least pass tightId
        # >=6 -> pass tightId+tightIdLepVeto  
        # see https://twiki.cern.ch/twiki/bin/viewauth/CMS/JetID for jetID definition (general)
        # see https://twiki.cern.ch/twiki/bin/view/CMS/JetID13TeVUL for UL information
        self.jetid   = jetid

        # Jet PU ID pre-UL: nanoAOD Jet_puId = miniAOD jet.userInt("pileupJetId:fullId")
        # Jet PU ID UL:     nanoAOD Jet_puId = miniAOD jet.userInt("pileupJetIdUpdated:fullId") 
        # Pre-UltraLegacy encoding and 2017&2018 UltraLegacy encoding:
        # loose:    bool(Jet_puId & (1 << 2)), 
        # medium:   bool(Jet_puId & (1 << 1)), 
        # tight:    bool(Jet_puId & (1 << 0))
        # UltraLegacy 2016 encoding (bug introduced on NanoAODv8/NanoAODv9 level):
        # loose:    bool(Jet_puId & (1 << 0)), 
        # medium:   bool(Jet_puId & (1 << 1)), 
        # tight:    bool(Jet_puId & (1 << 2))
        # PU ID is applied only to JEC-corrected jets with pT<50.
        # see https://twiki.cern.ch/twiki/bin/viewauth/CMS/PileupJetID for definition
        # see https://twiki.cern.ch/twiki/bin/view/CMS/PileupJetIDUL for UL information  
        self.pujetid = pujetid
        self.UL2016fix = UL2016fix
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
          if not self.UL2016fix:
              pu_loose  = bool(puId & (1 << 2)) or pt > 50.
              pu_medium = bool(puId & (1 << 1)) or pt > 50.
              pu_tight  = bool(puId & (1 << 0)) or pt > 50.
          else:
              pu_loose  = bool(puId & (1 << 0)) or pt > 50.
              pu_medium = bool(puId & (1 << 1)) or pt > 50.
              pu_tight  = bool(puId & (1 << 2)) or pt > 50.

          goodJet = True
          if pt         <  self.minpt   : goodJet = False    
          if abs(eta)   >  self.maxeta  : goodJet = False 
          if jetId      <  self.jetid   : goodJet = False
          if self.pujetid == 'loose'  and not pu_loose  : goodJet = False
          if self.pujetid == 'medium' and not pu_medium : goodJet = False
          if self.pujetid == 'tight'  and not pu_tight  : goodJet = False
          if self.pujetid == 'custom' and not pu_loose : goodJet = False #for backwards compatibility

          if goodJet : order.append(iJet)

        for typ in self.CollBr: 
          for bname in self.CollBr[typ]:
            temp_b = bname.replace(self.jetColl+'_', '')
            temp_v = [jet_coll[iJet][temp_b] for iJet in order]
            self.out.fillBranch(bname, temp_v )

        return True

