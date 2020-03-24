import ROOT
import math
ROOT.PyConfig.IgnoreCommandLineOptions = True
import re
import os

from PhysicsTools.NanoAODTools.postprocessing.framework.datamodel import Collection 
from PhysicsTools.NanoAODTools.postprocessing.framework.eventloop import Module

class EmbedWeights(Module):
    def __init__(self, workspacefile="hww_scalefactors_XXX.root"):

        self.cmssw_base = os.getenv('CMSSW_BASE')
        self.workspacefilename = workspacefile

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
        filename = str(inputFile)[str(inputFile).find("nanoLatino"):str(inputFile).find(".root")+5]
        filenameFormat = "nanoLatino_DYToTT_MuEle_Embedded_Run(2016|2017|2018)(A|B|C|D|E|F|G|H).*\.root"
        pattern = re.match(filenameFormat, filename)
        if pattern == None:
          raise NameError("Cannot parse filename",filename, "; Expected pattern is", filenameFormat)
        self.year = pattern.group(1)
        self.run = pattern.group(2)

        if 'XXX' in self.workspacefilename: self.workspacefilename = self.workspacefilename.replace('XXX',self.year+'FULL') #+self.run
        self.workspace_file = self.open_root(self.cmssw_base + "/src/LatinoAnalysis/NanoGardener/python/data/embedded_data/" + self.workspacefilename)
        self.workspace = self.get_root_obj(self.workspace_file, 'w')

        if self.year == '2016':
          self.WPs = ['mva16'] #['cutSum16', 'mva16', 'cutSum16_SS', 'mva16_SS']
        else:
          self.WPs = ['WP90V1'] #['CutV1', 'CutV2', 'WP90V1', 'WP90V2', 'CutV1_SS', 'CutV2_SS', 'WP90V1_SS', 'WP90V2_SS']

        self.out = wrappedOutputTree
        self.branchnames = ["embed_norm", "embed_mu_isoSF", "embed_mu_idSF"]
        for wp in self.WPs:
          self.branchnames.append("embed_el_idSF_"+wp)
          self.branchnames.append("embed_el_isoSF_"+wp)
          self.branchnames.append("embed_hltSF_"+wp)
          self.branchnames.append("embed_total_"+wp)
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
        w.var("e_phi").setVal(getattr(event, 'Electron_phi')[ele_id])
        #w.var("e_iso").setVal(getattr(event, 'Electron_pfRelIso03_all')[ele_id])
        w.var("m_pt").setVal(getattr(event, 'Muon_pt')[mu_id])
        w.var("m_eta").setVal(getattr(event, 'Muon_eta')[mu_id])
        #w.var("m_iso").setVal(getattr(event, 'Muon_pfRelIso04_all')[mu_id])

        ### Get Isolation and ID scalefactors
        embed_mu_isoSF = w.function("m_iso_embed_WW_ratio").getValV()
        embed_mu_idSF = w.function("m_id_embed_WW_ratio").getValV()
        self.out.fillBranch("embed_mu_isoSF", embed_mu_isoSF)
        self.out.fillBranch("embed_mu_idSF", embed_mu_idSF)

        embed_el_isoSF = {}
        embed_el_idSF = {}
        for wp in self.WPs:
          embed_el_isoSF[wp] = w.function("e_iso_embed_"+wp+"_WW_ratio").getValV()
          embed_el_idSF[wp] = w.function("e_id_embed_"+wp+"_WW_ratio").getValV()
          self.out.fillBranch("embed_el_isoSF_"+wp, embed_el_isoSF[wp])
          self.out.fillBranch("embed_el_idSF_"+wp, embed_el_idSF[wp])

        ### Determine Trigger scalefactor
        embed_hltSF = {}
        trigger_23_data_Weight_2 = w.function("m_trg23_WW_data").getValV()
        trigger_12_data_Weight_2 = w.function("m_trg12_WW_data").getValV()
        trigger_23_embed_Weight_2 = w.function("m_trg23_WW_embed").getValV()
        trigger_12_embed_Weight_2 = w.function("m_trg12_WW_embed").getValV()
        if (self.year == '2017' and self.run == 'B') or (self.year == '2016' and event.run >= 278273):
          trg_muonelectron_mu23ele12 = getattr(event, 'HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_DZ')
        else:
          trg_muonelectron_mu23ele12 = getattr(event, 'HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL')
        if self.year == '2016' and event.run < 278273:
          trigger_12_data_Weight_2 = w.function("m_trg8_WW_data").getValV()
          trigger_12_embed_Weight_2 = w.function("m_trg8_WW_embed").getValV()
          trg_muonelectron_mu12ele23 = getattr(event, 'HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL')
        else:
          trg_muonelectron_mu12ele23 = getattr(event, 'HLT_Mu12_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ')

        for wp in self.WPs:
          trigger_12_data_Weight_1 = w.function("e_trg12_"+wp+"_WW_data").getValV()
          trigger_23_data_Weight_1 = w.function("e_trg23_"+wp+"_WW_data").getValV()
          trigger_12_embed_Weight_1 = w.function("e_trg12_"+wp+"_WW_embed").getValV()
          trigger_23_embed_Weight_1 = w.function("e_trg23_"+wp+"_WW_embed").getValV()

          numerator = (trigger_23_data_Weight_2*trigger_12_data_Weight_1*(trg_muonelectron_mu23ele12==1)+trigger_23_data_Weight_1*trigger_12_data_Weight_2*(trg_muonelectron_mu12ele23==1) - trigger_23_data_Weight_2*trigger_23_data_Weight_1*((trg_muonelectron_mu12ele23==1)*(trg_muonelectron_mu23ele12==1)))
          denominator = (trigger_23_embed_Weight_2*trigger_12_embed_Weight_1*(trg_muonelectron_mu23ele12==1)+trigger_23_embed_Weight_1*trigger_12_embed_Weight_2*(trg_muonelectron_mu12ele23==1) - trigger_23_embed_Weight_2*trigger_23_embed_Weight_1*((trg_muonelectron_mu12ele23==1)*(trg_muonelectron_mu23ele12==1)))

          if denominator == 0:
            embed_hltSF[wp] = 0
          else:
            embed_hltSF[wp] = numerator/denominator
          if embed_hltSF[wp] == 0 and ((trg_muonelectron_mu12ele23==1) or (trg_muonelectron_mu23ele12==1)):
            print "Weird trigger SF: Numerator",numerator,", Denominator",denominator

          self.out.fillBranch("embed_hltSF_"+wp, embed_hltSF[wp])

        ### Total
        embed_total = {}
        totaltotal=0.0
        for wp in self.WPs:
          embed_total[wp] = embed_norm * embed_mu_isoSF * embed_el_isoSF[wp] * embed_mu_idSF * embed_el_idSF[wp] * embed_hltSF[wp]

          if embed_total[wp]>1000:
            print '=========='
            print "Too large weight!", embed_total[wp]

            if ( trg_muonelectron_mu23ele12 and (getattr(event, 'Electron_pt')[ele_id]<12 or getattr(event, 'Muon_pt')[mu_id]<23) ) or ( trg_muonelectron_mu12ele23 and (getattr(event, 'Electron_pt')[ele_id]<23 or getattr(event, 'Muon_pt')[mu_id]<12) ):
              print "...because of Trigger SF" # The Trigger SF is always the reason for too large weights; occurs from few events where the lepton pT is smaller than Trigger leg requirement -> Should be cut in analysis
              embed_total[wp] = embed_total[wp] / embed_hltSF[wp] # ... but remove the weight anyway, just in case
            elif embed_el_idSF[wp]>100:
              print "...because of Ele ID" # Few bins unfortunately have low statistics in T&P, especially in the problematic phi regions.
              #embed_total[wp] = embed_total[wp] / embed_el_idSF[wp] # ... remove phi dependent part
            else:
              print "Don't know why!" # This doesn't occur, last I checked
              print "Norm  :", embed_norm
              print "El ID :", embed_el_idSF[wp]
              print "El Iso:", embed_el_isoSF[wp]
              print "Mu ID :", embed_mu_idSF
              print "Mu Iso:", embed_mu_isoSF
              print "Triggr:", embed_hltSF[wp]
              if trg_muonelectron_mu23ele12==1:
                print "ME TRIG"
              if trg_muonelectron_mu12ele23==1:
                print "EM TRIG"
              print "e_pT: ",getattr(event, 'Electron_pt')[ele_id]
              print "e_eta:",getattr(event, 'Electron_eta')[ele_id]
              print "e_phi:",getattr(event, 'Electron_phi')[ele_id]
              print "m_pT: ",getattr(event, 'Muon_pt')[mu_id]
              print "m_eta:",getattr(event, 'Muon_eta')[mu_id]



          totaltotal += embed_total[wp]
        if totaltotal == 0.0: return False # Remove event; it's 0 anyway

        for wp in self.WPs:
          self.out.fillBranch("embed_total_"+wp, embed_total[wp])

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
        for i,lep in enumerate(leptons):
          recoleps[i] = {}
          #recoleps[i]["pt"] = lep.pt
          recoleps[i]["eta"] = lep.eta
          recoleps[i]["phi"] = lep.phi
        if len(recoleps) == 0:
          print "There aren't even any leptons? In event",getattr(event, 'event')
          return -1

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
          print "Too large deltaR after manual genmatching:",DeltaR,"; not considering event",getattr(event, 'event')
      return lep_id
