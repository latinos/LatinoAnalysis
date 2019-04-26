import ROOT
ROOT.PyConfig.IgnoreCommandLineOptions = True
import re

from PhysicsTools.NanoAODTools.postprocessing.framework.datamodel import Collection 
from PhysicsTools.NanoAODTools.postprocessing.framework.eventloop import Module
from LatinoAnalysis.NanoGardener.data.common_cfg import Type_dict

class FatJetSel(Module):##inherit from Module
    def __init__(self,jetid=1,minpt=200.0, maxeta=2.4, max_tau21=0.4, fatjetColl="FatJet"):
        # bit1 : loose id / bit2 : tight id / bit3 : tightLepVeto
        # if fatjet = loose && tight && tightLepVeto => 111(in binary) => 1+2+4 = 7
        # (is loose id) + 2*(is tight id) + 4*(is tightLepVeto id)
        # Jet ID flags bit1 is loose (always false in 2017 since it does not exist), bit2 is tight, bit3 is tightLepVeto
        
        # >=2 -> ask tightId
        # >=4 -> ask tightIdLepVeto
        # >=6 -> ask tightId+tightIdLepVeto  
        # see https://twiki.cern.ch/twiki/bin/viewauth/CMS/JetWtagging#Working_points_and_data_MC_scale
        
        self.jetid   = jetid
        self.minpt   = minpt
        self.maxeta  = maxeta 
        self.max_tau21 = max_tau21
        self.fatjetColl = fatjetColl
    def beginJob(self):
        pass
    def endJob(self):
        pass
    def beginFile(self, inputFile, outputFile, inputTree, wrappedOutputTree): ##wrappedOutputTree = Events
        self.out = wrappedOutputTree
        self.itree = inputTree

        # Get List of variables in the collection
        self.CollBr = {}
        oBrList = self.out._tree.GetListOfBranches() 
        for br in oBrList:
            bname = br.GetName()
            btype = Type_dict[br.GetListOfLeaves()[0].GetTypeName()] ##varible type
            if re.match('\AFatJet_', bname):
                if btype not in self.CollBr: self.CollBr[btype] = [] ## add branch type if not added yet
                self.CollBr[btype].append(bname)
                self.out.branch(bname, btype, lenVar='nFatJet')    ## initialize output branch ##remove original ones?

    def endFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        pass
    
    def analyze(self, event):
        """process event, return True (go to next module) or False (fail, go to next event)"""
        fatjet_coll = Collection(event, "FatJet" )
        nFatJet     = fatjet_coll._len
        
        order = []

        for iFatJet in range(nFatJet):
          pt  = fatjet_coll[iFatJet]['pt'] ##it will read 'FatJet_pt[iFatJet]'
          eta = fatjet_coll[iFatJet]['eta']
          
          jetId = fatjet_coll[iFatJet]['jetId']
          
          goodFatJet = True
          if pt         <  self.minpt   : goodFatJet = False    
          if abs(eta)   >  self.maxeta  : goodFatJet = False 
          if jetId      <  self.jetid   : goodFatJet = False
          
          if goodFatJet : order.append(iFatJet)##order = index list of good fatjets 

        for typ in self.CollBr: ##each type of branch  
          for bname in self.CollBr[typ]: ## braches of a specific type
            temp_b = bname.replace(self.fatjetColl+'_', '') ## remove string "FatJet"->only variable name
            temp_v = [fatjet_coll[iFatJet][temp_b] for iFatJet in order] ## select a good fatjet
            self.out.fillBranch(bname, temp_v )

        return True

