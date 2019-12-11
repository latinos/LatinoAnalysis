import re
import math
import ROOT
from PhysicsTools.NanoAODTools.postprocessing.framework.eventloop import Module
from PhysicsTools.NanoAODTools.postprocessing.framework.datamodel import Collection
from PhysicsTools.NanoAODTools.postprocessing.framework.datamodel import Object
from LatinoAnalysis.NanoGardener.data.common_cfg import Type_dict
import copy

class PtCorrApplier(Module):
    '''
    Module that applies pt corrections to a given collection
    '''
    def __init__(self, Coll='CleanJet', CorrSrc='jecUncertTotal', kind='Up', doMET=True, METobjects = ['MET','PuppiMET','RawMET','TkMET','ChsMET','CaloMET'], suffix=''):
        self.CollTC = Coll
        self._suffix=suffix
        self.CorrSrc = CorrSrc
        self.kind = kind
        self.isUp = True if kind == 'Up' else False
        self.doMET = doMET
        self.METobj = METobjects
        self.minJetEn = 15
        self.has_mass = False
        self.backup_coll = []
        self.skip_sumEt = False
        prt_str = 'PtCorrApplier: CollectionToCorrect = ' + self.CollTC + ', CorrectionsToAplly = ' + self.CorrSrc + ', CorrectionType = ' + self.kind + ', PropagateToMET = ' + str(self.doMET)
        print(prt_str)

    def beginJob(self):
        pass

    def endJob(self):
        pass

    def FixAngle(self, phi) :
        if phi < -ROOT.TMath.Pi() :
            phi += 2*ROOT.TMath.Pi()
        elif phi > ROOT.TMath.Pi() :
            phi -= 2*ROOT.TMath.Pi()
        return phi

    def beginFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        self.out = wrappedOutputTree
        self.CollBr = {}
        # we clone it otherwise it changes as we add more branches
        oBrList = copy.deepcopy(self.out._tree.GetListOfBranches())
        backup_colls = []
        for br in oBrList:
            bname = br.GetName()
            btype = Type_dict[br.GetListOfLeaves()[0].GetTypeName()]
            # GIULIO: we don't want to pick CleanJet_pt_JESup not CleanJet_jecUncert
            if re.match('\A'+self.CollTC+'_', bname) and len(bname.split("_"))==2 and "jecUncert" not in bname:
                if btype not in self.CollBr: self.CollBr[btype] = []
                self.CollBr[btype].append(bname)
                self.out.branch(bname+self._suffix, btype, lenVar='n'+self.CollTC)
                # Does the collection have a mass or do we need a backup collection?
                if bname == self.CollTC+'_mass': self.has_mass = True
                if bname.endswith('Idx'):
                    split_name = bname.split('_')
                    if len(split_name) == 2: 
                        bcoll = split_name[1][0:-3]
                        #self.backup_coll.append(bcoll.capitalize())
                        backup_colls.append(bcoll)
        for br in oBrList:
            bname = br.GetName()
            for bcoll in backup_colls:
                massb = bcoll.capitalize() + '_mass'
                if bname == massb: self.backup_coll.append(bcoll)
        if self.doMET and not self.has_mass and len(self.backup_coll) < 1: 
            print('Warning PtCorrApplier: no mass found in ' + self.CollTC + ' collection, and no backup mass was found. Skipping sumEt correction')
            self.skip_sumEt = True
        elif self.doMET and not self.has_mass:
            coll_str = self.backup_coll[0].capitalize()
            for coll in self.backup_coll[1:]:
                coll_str += ', ' + coll.capitalize()
            print('PtCorrApplier: no mass found in ' + self.CollTC + ', but backup collections found: ' + coll_str + ' using ' + self.backup_coll[0].capitalize() + '_mass[' + self.CollTC + '_' + self.backup_coll[0] +'Idx] as alternative mass' )
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
            
            for met in self.METobj:
                self.out.branch(met+'_pt'+self._suffix, 'F')
                self.out.branch(met+'_phi'+self._suffix, 'F')
                if self.skip_sumEt: continue
                self.out.branch(met+'_sumEt'+self._suffix, 'F')
 
    def endFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        pass

    def analyze(self, event):
        coll = Collection(event, self.CollTC)
        nColl = len(coll)

        if self.doMET:
            if not self.has_mass and not self.skip_sumEt: bcoll = Collection(event, self.backup_coll[0].capitalize())
            MET = {}
            for met in self.METobj:
                temp_met = Object(event, met)
                MET[met] = {}
                #MET[met]['coll'] = Object(event, met)
                MET[met]['pt'] = temp_met['pt']
                MET[met]['px'] = temp_met['pt']*math.cos(temp_met['phi'])   
                MET[met]['py'] = temp_met['pt']*math.sin(temp_met['phi'])   
                MET[met]['phi']   = temp_met['phi']
                MET[met]['sumEt'] = temp_met['sumEt']
                
        # Create new pt
        new_pt = []
        for iObj in range(nColl):
            if self.isUp: tmp_pt = coll[iObj]['pt'] + coll[iObj][self.CorrSrc]*coll[iObj]['pt']
            else: tmp_pt = coll[iObj]['pt'] - coll[iObj][self.CorrSrc]*coll[iObj]['pt']
            new_pt.append(tmp_pt)

            # MET
            if self.doMET and tmp_pt > self.minJetEn:
                pt_diff = tmp_pt - coll[iObj]['pt']
                for met in self.METobj:
                    MET[met]['px'] -= pt_diff*(math.cos(coll[iObj]['phi'])) 
                    MET[met]['py'] -= pt_diff*(math.sin(coll[iObj]['phi']))
                    # SumEt
                    if self.skip_sumEt: continue
                    if self.has_mass: mass = coll[iObj]['mass']
                    else: mass = bcoll[coll[iObj][self.backup_coll[0]+'Idx']]['mass'] 
                    p4 = ROOT.TLorentzVector()
                    p4.SetPtEtaPhiM(coll[iObj]['pt'], coll[iObj]['eta'], coll[iObj]['phi'], mass)
                    et = p4.Energy()*math.sin(p4.Theta())
                    new_p4 = ROOT.TLorentzVector()
                    new_p4.SetPtEtaPhiM(tmp_pt, coll[iObj]['eta'], coll[iObj]['phi'], mass)
                    new_et = new_p4.Energy()*math.sin(new_p4.Theta())
                    MET[met]['sumEt'] += new_et - et 
        if self.doMET:
            for met in self.METobj:
                MET[met]['new_pt'] = math.sqrt(MET[met]['px']**2 + MET[met]['py']**2)
                MET[met]['new_phi'] = math.atan2(MET[met]['py'], MET[met]['px'])

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
                    self.out.fillBranch(bname+self._suffix, temp_v)
                else:
                    temp_b = bname.replace(self.CollTC+'_', '')
                    temp_v = [coll[idx][temp_b] for idx in order]
                    self.out.fillBranch(bname+self._suffix, temp_v)
        if self.doMET:
            for met in self.METobj:
                self.out.fillBranch(met+'_pt'+self._suffix, MET[met]['new_pt'])
                self.out.fillBranch(met+'_phi'+self._suffix, MET[met]['new_phi'])
                if self.skip_sumEt: continue
                self.out.fillBranch(met+'_sumEt'+self._suffix, MET[met]['sumEt'])
        return True 

