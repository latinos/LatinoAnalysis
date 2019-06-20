#       _                           _____              _                                   _   
#      | |                         |_   _|            | |                                 | |  
#      | |      ___  _ __    _ __    | |    ___   ___ | |  _   _  _ __    ___   ___  _ __ | |_ 
#      | |     / _ \| '_ \  | '_ \   | |   / __| / __|| | | | | || '_ \  / __| / _ \| '__|| __|
#      | |____|  __/| |_) | | |_) |  | |   \__ \| (__ | | | |_| || | | || (__ |  __/| |   | |_ 
#      \_____/ \___|| .__/  | .__/   \_/   |___/ \___||_|  \__,_||_| |_| \___| \___||_|    \__|
#                   | |     | |                                                                
#                   |_|     |_|                                                                
#      
#      


import ROOT
ROOT.PyConfig.IgnoreCommandLineOptions = True

from PhysicsTools.NanoAODTools.postprocessing.framework.datamodel import Collection
from PhysicsTools.NanoAODTools.postprocessing.framework.datamodel import Object
from PhysicsTools.NanoAODTools.postprocessing.framework.eventloop import Module
from PhysicsTools.NanoAODTools.postprocessing.modules.common.collectionMerger import collectionMerger
from LatinoAnalysis.NanoGardener.data.LeptonMaker_cfg import Lepton_br, Lepton_var 

import os.path
import math

class LeppTScalerTreeMaker(Module) :
    def __init__(self, kind="Up", lepFlavor="ele", version='Full2017v2'  , metCollections = ['MET', 'PuppiMET', 'RawMET', 'TkMET' , 'ChsMET']) :
        cmssw_base = os.getenv('CMSSW_BASE')
        self.metCollections = metCollections
        self.kind = kind # "Up" or "Dn"
        self.lepFlavor = lepFlavor # "ele" or "mu"
        leppTscaler = {}
        ScaleFactorFile = cmssw_base + '/src/LatinoAnalysis/NanoGardener/python/data/lepton_scale_n_smear/'+version+'/leppTscaler_'+lepFlavor[:2]+'.py'
        if os.path.exists(ScaleFactorFile):
          handle = open(ScaleFactorFile,'r')
          exec(handle)
          handle.close()
        self.leppTscaler = leppTscaler
        print self.leppTscaler 

        # fix underflow and overflow
        self.minpt = 0.0
        self.maxpt = 0.0
        self.maxeta = 0.0
        for point in self.leppTscaler[lepFlavor]:
          if point[0][1] > self.maxpt  : self.maxpt  = point[0][1]
          if point[1][1] > self.maxeta : self.maxeta = point[1][1]
        print 'maxpt = ',self.maxpt , ' , maxeta = ', self.maxeta

    def beginJob(self):
        pass

    def endJob(self):
        pass

    def beginFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        self.out = wrappedOutputTree
        for x in self.metCollections:
          self.out.branch(x+'_pt', "F")
          self.out.branch(x+'_phi', "F")

        if 'electronIdx' not in Lepton_var: Lepton_var.append('electronIdx')
        if 'muonIdx' not in Lepton_var: Lepton_var.append('muonIdx')
        for typ in Lepton_br:
            for var in Lepton_br[typ]:
                if 'Lepton_' in var: self.out.branch(var, typ, lenVar='nLepton')

    def endFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        pass

    def getScale (self, kindLep, pt, eta):


        if pt < self.minpt: pt = self.minpt
        if pt > self.maxpt: pt = self.maxpt - 0.000001
        if eta < 0: eta = -1 * eta
        if eta > self.maxeta: eta = self.maxeta - 0.000001
        
        if kindLep in self.leppTscaler.keys() : 
            # get the scale values in bins of pT and eta
            for point in self.leppTscaler[kindLep] :
                if (pt >= point[0][0] and pt < point[0][1] and eta >= point[1][0] and eta < point[1][1]) :
                    return point[2]
            # default ... it should never happen!
            print "WARNING: Did not find scale factor for pt =",pt,"and eta =",eta,"; using 1.0 as default"
            return 1.0
           
        else:
            return 1.0

    def analyze(self, event):
        """process event, return True (go to next module) or False (fail, go to next event)"""

        if self.kind == 'Up':
            self.variation = 1.0
        elif self.kind == 'Dn' or self.kind == 'Down':
            self.variation = -1.0

        leptons = Collection(event,"Lepton")
        met = Object(event, "MET")
        nLep = getattr(event, "nLepton")

        lep_dict = {}
        for var in Lepton_var:
            if 'Idx' in var:
                lep_dict[var] = [-1]*nLep
            else:
                lep_dict[var] = [0]*nLep

        # MET
        for metType in self.metCollections:
            try:
                met = Object(event, metType)
            except AttributeError:
                continue

            metx = met.pt * math.cos(met.phi)
            mety = met.pt * math.sin(met.phi)
            for idx,lep in enumerate(leptons):
                if (self.lepFlavor == 'ele' and abs(lep.pdgId) == 11) or (self.lepFlavor == 'mu' and abs(lep.pdgId) == 13):
                    diff = lep.pt * (self.variation * self.getScale(self.lepFlavor, lep.pt, lep.eta) / 100.0)
                    metx = metx - (diff * math.cos(lep.phi))
                    mety = mety - (diff * math.sin(lep.phi))
            newmetpt = math.sqrt(metx**2 + mety**2)
            newmetphi = math.atan2(mety, metx)
            self.out.fillBranch(metType+"_pt", newmetpt)
            self.out.fillBranch(metType+"_phi", newmetphi)

        # Leptons
        for idx,lep in enumerate(leptons):
            origleppt = lep.pt
            if (self.lepFlavor == 'ele' and abs(lep.pdgId) == 11) or (self.lepFlavor == 'mu' and abs(lep.pdgId) == 13):
                lep.pt = lep.pt * (1 + (self.variation * self.getScale(self.lepFlavor, lep.pt, lep.eta) / 100.0))

                #SumET
                if lep.electronIdx > -1: mass = event.Electron_mass[lep.electronIdx]
                elif lep.muonIdx > -1: mass = event.Muon_mass[lep.muonIdx]
                else: continue

                p4 = ROOT.TLorentzVector()
                p4.SetPtEtaPhiM(origleppt, lep.eta, lep.phi, mass)
                et = p4.Energy()*math.sin(p4.Theta())
                new_p4 = ROOT.TLorentzVector()
                new_p4.SetPtEtaPhiM(lep.pt, lep.eta, lep.phi, mass)
                new_et = new_p4.Energy()*math.sin(new_p4.Theta())

                for metType in self.metCollections:
                    try:
                        met = Object(event, metType)
                    except AttributeError:
                        continue
                    met.sumEt += new_et - et

        # Re-order lepton collection
        for idx,lep in enumerate(leptons):
            pt_idx = 0
            for idx2,lep2 in enumerate(leptons):
                if idx == idx2: continue
                if lep.pt < lep2.pt  or (lep.pt==lep2.pt and idx>idx2): pt_idx += 1
            for var in Lepton_var:
                if 'pt' in var:
                    lep_dict[var][pt_idx] = lep.pt
                elif 'Idx' in var:
                    if ('electronIdx' in var and abs(lep.pdgId) == 11) or ('muonIdx' in var and abs(lep.pdgId) == 13):
                        if not hasattr(event, 'Lepton_'+var):
                            lep_dict[var][pt_idx] = idx
                        else:
                            lep_dict[var][pt_idx] = getattr(event, 'Lepton_'+var)[idx]
                    else:
                        continue
                else:
                    lep_dict[var][pt_idx] = getattr(event, 'Lepton_'+var)[idx]

        for var in lep_dict:
            self.out.fillBranch('Lepton_' + var, lep_dict[var])

        return True

