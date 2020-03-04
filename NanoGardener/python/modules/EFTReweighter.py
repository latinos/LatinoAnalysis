
import ROOT
import math 
import ctypes
ROOT.PyConfig.IgnoreCommandLineOptions = True

from PhysicsTools.NanoAODTools.postprocessing.framework.datamodel import Collection 
from PhysicsTools.NanoAODTools.postprocessing.framework.eventloop import Module
from PhysicsTools.NanoAODTools.postprocessing.modules.common.collectionMerger import collectionMerger

import os.path

class EFTReweighter(Module):
    def __init__(self):
        
        self.cmssw_base = os.getenv('CMSSW_BASE')
        self.cmssw_arch = os.getenv('SCRAM_ARCH')

        ROOT.gSystem.AddIncludePath("-I"+self.cmssw_base+"/interface/")
        ROOT.gSystem.AddIncludePath("-I"+self.cmssw_base+"/src/")
        ROOT.gSystem.Load("libZZMatrixElementMELA.so")
        ROOT.gSystem.Load(self.cmssw_base+"/src/ZZMatrixElement/MELA/data/"+self.cmssw_arch+"/libmcfm_707.so")

        try:
            ROOT.gROOT.LoadMacro(self.cmssw_base+'/src/LatinoAnalysis/Gardener/python/variables/melaHiggsEFT.C+g')
        except RuntimeError:
            ROOT.gROOT.LoadMacro(self.cmssw_base+'/src/LatinoAnalysis/Gardener/python/variables/melaHiggsEFT.C++g')
      
        self.mela = ROOT.Mela(13, 125,  ROOT.TVar.SILENT) 

    def beginJob(self):
        pass

    def endJob(self):
        pass

    def beginFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):

        filename = str(inputFile)[str(inputFile).find("nanoLatino"):str(inputFile).find(".root")+5]

        if "_VBF_H0" in filename :
          self.productionProcess = "VBF"
        elif "_H0" in filename :
          self.productionProcess = "GluGlu"
        else:
          raise NameError(filename, "is an unrecognised simulation")

        print("Running MELA EFT reweighter with " + self.productionProcess + " sample")

        self.out = wrappedOutputTree
        self.newbranches = [
        'gen_me_hsm','gen_me_hm','gen_me_hp','gen_me_hl','gen_me_mixhm','gen_me_mixhp'  
          ]
        
        for nameBranches in self.newbranches :
          self.out.branch(nameBranches  ,  "F");

    def endFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        pass

    def analyze(self, event):
        """process event, return True (go to next module) or False (fail, go to next event)"""

        gen_me_hsm   = -999
        gen_me_hm    = -999
        gen_me_hp    = -999
        gen_me_hl    = -999
        gen_me_mixhm = -999
        gen_me_mixhp = -999 

        self.LHE = Collection(event,"LHEPart")
        Gen = Collection(event,"GenPart")
        LHEjetIdx = []

        for idx,part in enumerate(self.LHE):
          if abs(part.pdgId) in [1,2,3,4,5,21]:
            LHEjetIdx.append(idx)

        LHEjetIdx = self.pTorder(event, LHEjetIdx)

        daughters=[]
        daughterIDs=[]

        FinalStateIdx = []
        for gid,gen in enumerate(Gen):
          if abs(gen.pdgId) >= 21: continue 
          mid = event.GenPart_genPartIdxMother[gid]
          if mid == -1: continue
          if abs(event.GenPart_pdgId[mid]) != 24: continue 
          gmid = event.GenPart_genPartIdxMother[mid]
          if gmid == -1: continue
          if abs(event.GenPart_pdgId[gmid]) != 25: continue 
          if abs(gen.pdgId) in [11,12,13,14,15,16]: FinalStateIdx.append(gid) 

        LHEFinalState = self.getLHE(event, FinalStateIdx) 

        if len(LHEFinalState)!=4:
          print "SOMETHING WENT WRONG!"
          print "Event no.:",event.event
          print LHEFinalState
          print FinalStateIdx

        for ipart in LHEFinalState:
          l = ROOT.TLorentzVector()
          l.SetPtEtaPhiM(LHEFinalState[ipart][0], LHEFinalState[ipart][1], LHEFinalState[ipart][2], 0.)
          daughters.append(l)
          daughterIDs.append(LHEFinalState[ipart][3])                            

        mothers = ROOT.vector('TLorentzVector')()
        motherIDs = ROOT.vector('int')()
        incoming1=ROOT.TLorentzVector()
        incoming1.SetPxPyPzE(0.,0., event.Generator_x1*6500, event.Generator_x1*6500)
        incoming2=ROOT.TLorentzVector()
        incoming2.SetPxPyPzE(0.,0.,-1*event.Generator_x2*6500, event.Generator_x2*6500)
        mothers.push_back(incoming1)
        mothers.push_back(incoming2)
        genid1 = int(event.Generator_id1)
        genid2 = int(event.Generator_id2)

        partons   = ROOT.vector('TLorentzVector')()
        partonIDs = ROOT.vector('int')()
        parton_ids = []

        for ijet in LHEjetIdx:
          parton = ROOT.TLorentzVector()
          parton.SetPtEtaPhiM(event.LHEPart_pt[ijet], event.LHEPart_eta[ijet], event.LHEPart_phi[ijet], 0.)
          partons.push_back(parton)
          partonIDs.push_back(int(event.LHEPart_pdgId[ijet]))
          parton_ids.append(int(event.LHEPart_pdgId[ijet]))

        if self.productionProcess == "VBF" and len(partons) !=2 :
         print "Number of partons does not equal 2! Setup is not appropiate for this simulation"
         print len(partons)

        # Generator id seems to be wrong in few VBF events... -> Replace pdgId 21 by whatever is in LHE collection
        if self.productionProcess == "VBF" and (genid1==21 or genid2==21) and (21 in parton_ids):
          print "Gluons from incoming partons?!"
          options = [o for o in parton_ids if o != 21] # Should usually contain 2 entries; There are _always_ 3 LHE jets because VBF samples are NLO
          if genid1==21 and genid2!=21:
            genid1 = options[0] + options[1] - genid2 # USUALLY Sum pdgIds incoming = Sum pdgIds outgoing (exception is 2.gen <-> 1.gen quark)
            print "INFO: Replaced incoming particle ID1 to", genid1, "in event", event.event
          elif genid1!=21 and genid2==21:
            genid2 = options[0] + options[1] - genid1
            print "INFO: Replaced incoming particle ID2 to", genid2, "in event", event.event
          elif genid1==21 and genid2==21: # Assuming qq -> ZZ -> H
            genid1 = options[0]
            genid2 = options[1]
            print "INFO: Replaced incoming particle ID1 to", genid1, "_AND_ ID2 to", genid2, " in event", event.event
          print "incoming:", [genid1, genid2]
          print "outgoing:", parton_ids

        motherIDs.push_back(genid1)
        motherIDs.push_back(genid2)        

        daughter_coll = ROOT.SimpleParticleCollection_t() 
        associated_coll = ROOT.SimpleParticleCollection_t()        
        mother_coll = ROOT.SimpleParticleCollection_t()

        for idx, dau in enumerate(daughters):
         daughter_coll.push_back(ROOT.SimpleParticle_t(daughterIDs[idx], dau)) 
        
        for idx, par in enumerate(partons):
         associated_coll.push_back(ROOT.SimpleParticle_t(partonIDs[idx], par))
        
        for idx, mot in enumerate(mothers):
         mother_coll.push_back(ROOT.SimpleParticle_t(motherIDs[idx], mot))
                                 
        self.mela.setCandidateDecayMode(ROOT.TVar.CandidateDecay_WW)   
        self.mela.setInputEvent(daughter_coll, associated_coll, mother_coll, 1)
        self.mela.setCurrentCandidateFromIndex(0)
        
        ME1 = [1, 1, 1, 1, 1, 1]
        ME2 = [1, 1, 1, 1, 1, 1]

        if self.productionProcess == "VBF" :

         ME1 = ROOT.melaHiggsEFT(self.mela, ROOT.TVar.JHUGen, ROOT.TVar.ZZINDEPENDENT, 0, 0) 
         ME2 = ROOT.melaHiggsEFT(self.mela, ROOT.TVar.JHUGen, ROOT.TVar.JJVBF, 0, 0) 
  
        elif self.productionProcess == "GluGlu" :

         ME1 = ROOT.melaHiggsEFT(self.mela, ROOT.TVar.JHUGen, ROOT.TVar.ZZINDEPENDENT, 1, 0) 

        gen_me_hsm   = ME1[0]*ME2[0]
        gen_me_hm    = ME1[1]*ME2[1]
        gen_me_hp    = ME1[2]*ME2[2]
        gen_me_hl    = ME1[3]*ME2[3]
        gen_me_mixhm = ME1[4]*ME2[4]
        gen_me_mixhp = ME1[5]*ME2[5] 

        self.mela.resetInputEvent()

        self.out.fillBranch( 'gen_me_hsm',  gen_me_hsm )
        self.out.fillBranch( 'gen_me_hm',   gen_me_hm )
        self.out.fillBranch( 'gen_me_hp',   gen_me_hp )
        self.out.fillBranch( 'gen_me_hl',   gen_me_hl )
        self.out.fillBranch( 'gen_me_mixhm',  gen_me_mixhm )
        self.out.fillBranch( 'gen_me_mixhp',  gen_me_mixhp )

        return True   

    def pTorder(self, event, oldlist):
      order = []
      for i in oldlist:
        order.append(0)
      for i,pone in enumerate(oldlist):
        for j,ptwo in enumerate(oldlist):
          if pone==ptwo: continue
          if event.LHEPart_pt[pone] > event.LHEPart_pt[ptwo]: order[i] += 1
          if (event.LHEPart_pt[pone] == event.LHEPart_pt[ptwo]) and (i<j):
            order[j] += 1
      newlist = [oldlist[i] for i in order]
      return newlist

    def getLHE(self, event, genlist): # Particles in LHE collection have higher precision -> Find LHE particles with closest match to GenParticles
      LHElist = {}
      for gid in genlist:
        pt = event.GenPart_pt[gid]
        eta = event.GenPart_eta[gid]
        phi = event.GenPart_phi[gid]
        pdgid = event.GenPart_pdgId[gid]
        deltaR = 9999
        LHEid = -1
        for lid,lhe in enumerate(self.LHE):
          if lhe.pdgId != pdgid: continue
          dphi = phi-lhe.phi
          if dphi > math.pi: dphi -= 2*math.pi
          if dphi < -math.pi: dphi += 2*math.pi
          deta = eta-lhe.eta
          dR = math.sqrt((deta)*(deta)+(dphi)*(dphi))
          if deltaR > dR:
            deltaR = dR
            LHEid = lid
            LHEpt = lhe.pt
            LHEeta = lhe.eta
            LHEphi = lhe.phi
            LHEpdg = lhe.pdgId
        if LHEid==-1: # VERY rare, use placeholder key value
          LHElist[pdgid+100*(len(LHElist)+1)]=[pt, eta, phi, pdgid]
        elif deltaR > 0.2: # Use GenPart information if direction is too different
          LHElist[LHEid]=[pt, eta, phi, pdgid]
        else:
          LHElist[LHEid]=[LHEpt, LHEeta, LHEphi, pdgid]
        
      return LHElist
    

      