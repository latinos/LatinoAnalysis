import re
import math
from PhysicsTools.NanoAODTools.postprocessing.framework.eventloop import Module
from PhysicsTools.NanoAODTools.postprocessing.framework.datamodel import Collection
from PhysicsTools.NanoAODTools.postprocessing.framework.datamodel import Object
from LatinoAnalysis.NanoGardener.data.common_cfg import Type_dict

class PtCorrApplier(Module):
    '''
    Module that applies pt corrections to a given collection
    '''
    def __init__(self, Coll='CleanJet', CorrSrc='jecUncertTotal', kind='Up', doMET=True, METobject = 'MET'):
        self.CollTC = Coll
        self.CorrSrc = CorrSrc
        self.kind = kind
        self.isUp = True if kind == 'Up' else False
        self.doMET = doMET
        self.METobj = METobject
        self.minJetEn = 15
        prt_str = 'PtCorrApplier: CollectionToCorrect = ' + self.CollTC + ', CorrectionsToAplly = ' + self.CorrSrc + ', CorrectionType = ' + self.kind + ', PropagateToMET = ' + str(self.doMET)
        print(prt_str)

    def beginJob(self):
        pass

    def endJob(self):
        pass

    def beginFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        self.out = wrappedOutputTree
        self.CollBr = {}
        oBrList = self.out._tree.GetListOfBranches()
        for br in oBrList:
            bname = br.GetName()
            btype = Type_dict[br.GetListOfLeaves()[0].GetTypeName()]
            if re.match('\A'+self.CollTC+'_', bname):
                if btype not in self.CollBr: self.CollBr[btype] = []
                self.CollBr[btype].append(bname)
                self.out.branch(bname, btype, lenVar='n'+self.CollTC)
        #iBrList = inputTree.GetListOfBranches()
        #for br in iBrList:
        #    bname = br.GetName()
        #    btype = Type_dict[br.GetListOfLeaves()[0].GetTypeName()]
        #    if re.match('\A'+self.CollTC+'_', bname):
        #        if btype not in self.CollBr: self.CollBr[btype] = []
        #        if bname in self.CollBr[btype]: continue
        #        self.CollBr[btype].append(bname)
        #        self.out.branch(bname, btype, lenVar='n'+self.CollTC)
        if len(self.CollBr) < 1: raise IOError('PtCorrApplier: no branches with ' + self.CollTC+'_' +  ' found in inputTree or outputTree.')
        if self.doMET:
            self.out.branch(self.METobj+'_pt', 'F')
            self.out.branch(self.METobj+'_phi', 'F')
 
    def endFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        pass

    def analyze(self, event):
        coll = Collection(event, self.CollTC)
        nColl = len(coll)

        if self.doMET:
            met = Object(event, self.METobj)
            met_px = met['pt']*math.cos(met['phi'])   
            met_py = met['pt']*math.sin(met['phi'])   

        # Create new pt
        new_pt = []
        for iObj in range(nColl):
            if self.isUp: tmp_pt = coll[iObj]['pt'] + coll[iObj][self.CorrSrc]*coll[iObj]['pt']
            else: tmp_pt = coll[iObj]['pt'] - coll[iObj][self.CorrSrc]*coll[iObj]['pt']
            new_pt.append(tmp_pt)

            # MET
            if self.doMET and tmp_pt > self.minJetEn:
                pt_diff = tmp_pt - coll[iObj]['pt']
                met_px -= pt_diff*(math.cos(coll[iObj]['pt'])) 
                met_py -= pt_diff*(math.sin(coll[iObj]['pt'])) 
        if self.doMET:
            new_MET_pt = math.sqrt(met_px**2 + met_py**2)
            new_MET_phi = math.atan2(met_px, met_py)

        # Reorder
        order = []
        for idx1, pt1 in enumerate(new_pt):
            pt_idx = 0
            for idx2, pt2 in enumerate(new_pt):
                if pt1 < pt2 or (pt1 == pt2 and idx1 > idx2): pt_idx += 1
            order.append(pt_idx)
 
        # Fill branches
        for typ in self.CollBr:
            for bname in self.CollBr[typ]:
                if '_pt' in bname: 
                    temp_v = [new_pt[idx] for idx in order]
                    self.out.fillBranch(bname, temp_v)
                else:
                    temp_b = bname.replace(self.CollTC+'_', '')
                    temp_v = [coll[idx][temp_b] for idx in order]
                    self.out.fillBranch(bname, temp_v)
        if self.doMET:
            self.out.fillBranch(self.METobj+'_pt', new_MET_pt)
            self.out.fillBranch(self.METobj+'_phi', new_MET_phi)
        return True 

