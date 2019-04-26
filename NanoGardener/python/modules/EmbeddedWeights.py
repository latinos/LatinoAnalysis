import ROOT
import math
ROOT.PyConfig.IgnoreCommandLineOptions = True
import re
import os

from PhysicsTools.NanoAODTools.postprocessing.framework.datamodel import Collection 
from PhysicsTools.NanoAODTools.postprocessing.framework.eventloop import Module

class EmbedWeights(Module):
    def __init__(self, workspacefile="htt_scalefactors_2017_v1.root"):

        cmssw_base = os.getenv('CMSSW_BASE')

        self.workspace_file = self.open_root(cmssw_base + "/src/LatinoAnalysis/NanoGardener/python/data/embedded_data/" + workspacefile)
        self.workspace = self.get_root_obj(self.workspace_file, 'w')

    def open_root(self, path):
        r_file = ROOT.TFile(path, 'r')
        if not r_file.__nonzero__() or not r_file.IsOpen(): raise NameError('File ' + path + ' not open')
        return r_file

    def get_root_obj(self, root_file, obj_name):
        r_obj = root_file.Get(obj_name)
        if not r_obj.__nonzero__(): raise NameError('Root Object ' + obj_name + ' not found')
        return r_obj

    def beginJob(self):
        pass

    def endJob(self):
        pass

    def beginFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        filename = str(inputFile)[str(inputFile).find("/nanoLatino")+1:str(inputFile).find(".root")+5]
        filenameFormat = "nanoLatino_DYToTT_MuEle_Embedded_Run(2016|2017)(B|C|D|E|F|G|H).*\.root"
        pattern = re.match(filenameFormat, filename)
        if pattern == None:
          raise NameError("Cannot parse filename",filename, "; Expected pattern is", filenameFormat)
        self.year = pattern.group(1)
        self.run = pattern.group(2)

        self.out = wrappedOutputTree
        self.branchnames = ["embed_norm", "embed_mu_isoSF", "embed_mu_idSF", "embed_el_isoSF", "embed_el_idSF", "embed_hltSF", "embed_stitching", "embed_total"]
        for bname in self.branchnames:
          self.out.branch(bname, "F")

    def endFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        pass

    def analyze(self, event):
        """process event, return True (go to next module) or False (fail, go to next event)"""

        w = self.workspace
        self.genparts = Collection(event,"GenPart")

        ### Global normalization derived from data using scale factors
        # Input: generator-level pt and eta of both taus (arbitrary order)
        # Exactly 9 GenParts saved in each embedded event: Z(0) -> tau(1)+tau(2) -> nutau(3)e(4)nue(5) + nutau(6)mu(7)numu(8)
        # Any 2 GenParts that are taus are those we're looking for

        ntau = 0
        embed_norm = 1.0
        for gen in self.genparts:
          if abs(gen.pdgId)==15:
            ntau += 1
            w.var("gt"+str(ntau)+"_pt").setVal(gen.pt)
            w.var("gt"+str(ntau)+"_eta").setVal(gen.eta)

            # Additional normalization for each individual GenTau
            w.var("gt_pt").setVal(gen.pt)
            w.var("gt_eta").setVal(gen.eta)
            embed_norm *= w.function("m_sel_idEmb_ratio").getValV()

        embed_norm *= w.function("m_sel_trg_ratio").getValV()
        self.out.fillBranch("embed_norm", embed_norm)

        ### Corrections on the muon and electron ID, Isolation and Trigger efficiencies
        # First find leptons comming from embedded tau:
        ele_id = self.FindTauMatch(event, 11)
        mu_id = self.FindTauMatch(event, 13)

        if ele_id == -1 or mu_id == -1: return False # Lepton not reconstructed / couldn't be matched to Tau decay product: Remove event

        w.var("e_pt").setVal(getattr(event, 'Electron_pt')[ele_id])
        w.var("e_eta").setVal(getattr(event, 'Electron_eta')[ele_id])
        w.var("e_iso").setVal(getattr(event, 'Electron_pfRelIso03_all')[ele_id])
        w.var("m_pt").setVal(getattr(event, 'Muon_pt')[mu_id])
        w.var("m_eta").setVal(getattr(event, 'Muon_eta')[mu_id])
        w.var("m_iso").setVal(getattr(event, 'Muon_pfRelIso04_all')[mu_id])

        ### Get Isolation and ID scalefactors
        if self.year == "2017":
          embed_mu_isoSF = w.function("m_looseiso_binned_embed_ratio").getValV()
          embed_el_isoSF = w.function("e_iso_binned_embed_ratio").getValV()
          embed_mu_idSF = w.function("m_id_embed_ratio").getValV()
          embed_el_idSF = w.function("e_id_embed_ratio").getValV()
        elif self.year == "2016":
          embed_mu_isoSF = w.function("m_iso_ratio").getValV()
          embed_el_isoSF = w.function("e_iso_ratio").getValV()
          embed_mu_idSF = w.function("m_id_ratio").getValV()
          embed_el_idSF = w.function("e_id_ratio").getValV()
        self.out.fillBranch("embed_mu_isoSF", embed_mu_isoSF)
        self.out.fillBranch("embed_el_isoSF", embed_el_isoSF)
        self.out.fillBranch("embed_mu_idSF", embed_mu_idSF)
        self.out.fillBranch("embed_el_idSF", embed_el_idSF)

        ### Determine Trigger scalefactor
        # The actual HLT triggers used here (w/ or w/o "_DZ") don't exactly correspond to what we use in the end,
        # but they're the ones that were used to compute der Trigger scale factors, so they NEED to be used here
        if self.year == "2017":
          trigger_12_data_Weight_1 = w.function("e_trg_binned_12_data").getValV()
          trigger_23_data_Weight_2 = w.function("m_trg_binned_23_data").getValV()
          trigger_23_data_Weight_1 = w.function("e_trg_binned_23_data").getValV()
          trigger_8_data_Weight_2 = w.function("m_trg_binned_8_data").getValV()
          trigger_12_embed_Weight_1 = w.function("e_trg_binned_12_embed").getValV()
          trigger_23_embed_Weight_2 = w.function("m_trg_binned_23_embed").getValV()
          trigger_23_embed_Weight_1 = w.function("e_trg_binned_23_embed").getValV()
          trigger_8_embed_Weight_2 = w.function("m_trg_binned_8_embed").getValV()
          trg_muonelectron_mu23ele12 = getattr(event, 'HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_DZ')
          trg_muonelectron_mu8ele23 = getattr(event, 'HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ')
        elif self.year == "2016":
          trigger_12_data_Weight_1 = w.function("e_trg12_binned_ic_data").getValV()
          trigger_23_data_Weight_2 = w.function("m_trg23_binned_ic_data").getValV()
          trigger_23_data_Weight_1 = w.function("e_trg23_binned_ic_data").getValV()
          trigger_8_data_Weight_2 = w.function("m_trg8_binned_ic_data").getValV()
          trigger_12_embed_Weight_1 = w.function("e_trg12_binned_ic_embed").getValV()
          trigger_23_embed_Weight_2 = w.function("m_trg23_binned_ic_embed").getValV()
          trigger_23_embed_Weight_1 = w.function("e_trg23_binned_ic_embed").getValV()
          trigger_8_embed_Weight_2 = w.function("m_trg8_binned_ic_embed").getValV()
          trg_muonelectron_mu23ele12 = getattr(event, 'HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL')
          trg_muonelectron_mu8ele23 = getattr(event, 'HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL')

        numerator = (trigger_23_data_Weight_2*trigger_12_data_Weight_1*(trg_muonelectron_mu23ele12==1)+trigger_23_data_Weight_1*trigger_8_data_Weight_2*(trg_muonelectron_mu8ele23==1) - trigger_23_data_Weight_2*trigger_23_data_Weight_1*((trg_muonelectron_mu8ele23==1)*(trg_muonelectron_mu23ele12==1)))
        denominator = (trigger_23_embed_Weight_2*trigger_12_embed_Weight_1*(trg_muonelectron_mu23ele12==1)+trigger_23_embed_Weight_1*trigger_8_embed_Weight_2*(trg_muonelectron_mu8ele23==1) - trigger_23_embed_Weight_2*trigger_23_embed_Weight_1*((trg_muonelectron_mu8ele23==1)*(trg_muonelectron_mu23ele12==1)))

        if denominator == 0:
          embed_hltSF = 0
        else:
          embed_hltSF = numerator/denominator

        if embed_hltSF == 0 and ((trg_muonelectron_mu8ele23==1) or (trg_muonelectron_mu23ele12==1)):
          print "Weird trigger SF: Numerator",numerator,", Denominator",denominator

        self.out.fillBranch("embed_hltSF", embed_hltSF)

        ### Stitching for 2016 samples
        embed_stitching = 1.0
        if self.year == "2016":
          if self.run == "B": embed_stitching = 1.0/0.891 # runnr >= 272007 and runnr < 275657
          elif self.run == "C": embed_stitching = 1.0/0.910 # runnr >= 275657 and runnr < 276315
          elif self.run == "D": embed_stitching = 1.0/0.953 # runnr >= 276315 and runnr < 276831
          elif self.run == "E": embed_stitching = 1.0/0.947 # runnr >= 276831 and runnr < 277772
          elif self.run == "F": embed_stitching = 1.0/0.942 # runnr >= 277772 and runnr < 278820
          elif self.run == "G": embed_stitching = 1.0/0.906 # runnr >= 278820 and runnr < 280919
          elif self.run == "H": embed_stitching = 1.0/0.950 # runnr >= 280919 and runnr < 284045
        self.out.fillBranch("embed_stitching", embed_stitching)

        ### Total
        embed_total = embed_norm * embed_mu_isoSF * embed_el_isoSF * embed_mu_idSF * embed_el_idSF * embed_hltSF * embed_stitching
        if embed_total == 0: return False # Remove event; it's 0 anyway
        self.out.fillBranch("embed_total", embed_total)

        return True


    def FindTauMatch(self, event, pdgId):
      lep_id = -1
      if pdgId == 11: leptype = "Electron"
      if pdgId == 13: leptype = "Muon"
      leptons = Collection(event,leptype)

      for i,lep in enumerate(leptons):
        if lep.genPartIdx != -1:
          mother_of_lep = getattr(event, 'GenPart_genPartIdxMother')[lep.genPartIdx]
          if abs(getattr(event, 'GenPart_pdgId')[mother_of_lep]) == 15:
            lep_id = i
            break

      if lep_id == -1: # Manual matching
        for gen in self.genparts:
          if abs(gen.pdgId) == pdgId:
            #gpt = gen.pt
            geta = gen.eta
            gphi = gen.phi
        recoleps = {}
        i=0
        for lep in leptons:
          recoleps[i] = {}
          #recoleps[i]["pt"] = lep.pt
          recoleps[i]["eta"] = lep.eta
          recoleps[i]["phi"] = lep.phi
          i += 1

        DeltaR = 99
        UseThisIndex = -1
        for i in range(len(recoleps)):
          dphi = recoleps[i]["phi"]-gphi
          if dphi > math.pi: dphi -= 2*math.pi
          if dphi < -math.pi: dphi += 2*math.pi
          deta = recoleps[i]["eta"]-geta
          dr = math.sqrt((deta)*(deta)+(dphi)*(dphi))
          if DeltaR > dr:
            DeltaR = dr
            UseThisIndex = i

        if DeltaR < 0.4: 
          lep_id = UseThisIndex
        else:
          print "Too large deltaR after manual genmatching:",DeltaR,"; not considering event"
      return lep_id
