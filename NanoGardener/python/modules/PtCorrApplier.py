from PhysicsTools.NanoAODTools.postprocessing.framework.eventloop import Module
from PhysicsTools.NanoAODTools.postprocessing.framework.datamodel import Collection
from LatinoAnalysis.NanoGardener.data.LeptonMaker_cfg import CleanJet_br

class PtCorrApplier(Module):
    '''
    Module that applies pt corrections to a given collection
    '''
    def __init__(self, Coll='CleanJet', CorrSrc='jecUncertTotal', kind='Up' ):
        self.CollTC = Coll
        self.CorrSrc = CorrSrc
        self.kind = kind
        self.isUp = True if kind == 'Up' else False
        if self.CollTC == 'CleanJet':
            self.CollBr = CleanJet_br
        else: raise ValueError('Unknown Collection: PtCorrApplier not (yet) implemented for collection ' + self.CollTC) 
        print('PtCorrApplier: CollectionToCorrect = ' + self.CollTC + ', CorrectionsToAplly = ' + self.CorrSrc + ', CorrectionType = ' + self.kind)

    def beginJob(self):
        pass

    def endJob(self):
        pass

    def beginFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        self.out = wrappedOutputTree
        for typ in self.CollBr:
            for bname in self.CollBr[typ]:
                self.out.branch(bname, typ, lenVar='n'+self.CollTC)
 
    def endFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        pass

    def analyze(self, event):
        coll = Collection(event, self.CollTC)
        nColl = len(coll)

        # Create new pt
        new_pt = []
        for iObj in range(nColl):
            if self.isUp: new_pt.append(coll[iObj]['pt'] + coll[iObj][self.CorrSrc]*coll[iObj]['pt'])
            else: new_pt.append(coll[iObj]['pt'] - coll[iObj][self.CorrSrc]*coll[iObj]['pt'])

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
        return True 

