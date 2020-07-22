import ROOT
ROOT.PyConfig.IgnoreCommandLineOptions = True
import os
import math

from PhysicsTools.NanoAODTools.postprocessing.framework.datamodel import Object
from PhysicsTools.NanoAODTools.postprocessing.framework.datamodel import Collection 
from PhysicsTools.NanoAODTools.postprocessing.framework.eventloop import Module

class RecoilCorr(Module):
    def __init__(self, year, metCollections=['MET','PuppiMET'], moreVars=False):
        self.cmssw_base = os.getenv('CMSSW_BASE')
        self.year = year
        self.metCollections = metCollections
        self.moreVars = moreVars
        #self.branch_map = branch_map
        try:
            ROOT.gROOT.LoadMacro(self.cmssw_base+'/src/LatinoAnalysis/NanoGardener/python/modules/RecoilCorrector.cc+g')
        except RuntimeError: 
            ROOT.gROOT.LoadMacro(self.cmssw_base+'/src/LatinoAnalysis/NanoGardener/python/modules/RecoilCorrector.cc++g')

        self.Corrector = {}
        self.neglectMET = []
        for metType in self.metCollections:
          if metType=='PuppiMET': correctionFilename = "Type1_PuppiMET_"+str(self.year)+".root"
          elif metType=='MET':    correctionFilename = "Type1_PFMET_"+str(self.year)+".root"
          else:
            print 'No correction files for MET type "'+metType+'"!'
            self.neglectMET.append(metType)
            continue
          self.Corrector[metType] = ROOT.RecoilCorrector('LatinoAnalysis/NanoGardener/python/data/METrecoil/' + correctionFilename)

    def beginJob(self):
        pass

    def endJob(self):
        pass

    def beginFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        self.out = wrappedOutputTree
        for metType in self.metCollections:
          if metType in self.neglectMET: continue
          self.out.branch(metType+'_pt','F')
          self.out.branch(metType+'_phi','F')
          if self.moreVars:
            self.out.branch(metType+'_recoilCorrDiff_pt', 'F')
            self.out.branch(metType+'_recoilCorrDiff_phi', 'F')

    def endFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        pass

    def analyze(self, event):
        """process event, return True (go to next module) or False (fail, go to next event)"""

        Gen = Collection(event,"GenPart")
        Jet = Collection(event,"CleanJet")

        IdxGen = []
        IdxVis = []
        genPx = 0.0
        genPy = 0.0
        visPx = 0.0 # "Visible" refers to generator level information from visible particles (not including neutrinos)
        visPy = 0.0
        for gid,gen in enumerate(Gen):
          pdgId = abs(gen.pdgId)
          sFlag = gen.statusFlags
          if (pdgId>=11 and pdgId <=16 and (sFlag >> 8 & 1)) or (sFlag >> 9 & 1):
            IdxGen.append(gid)
            genPx += (gen.pt * math.cos(gen.phi))
            genPy += (gen.pt * math.sin(gen.phi))
            if pdgId in [11, 13, 15]:
              IdxVis.append(gid)
              visPx += (gen.pt * math.cos(gen.phi))
              visPy += (gen.pt * math.sin(gen.phi))
        nJet30 = 0
        for jid,jet in enumerate(Jet):
          if jet.pt >= 30:
            nJet30 += 1
          else:
            break

        noFix = True if (len(IdxGen)<2 or len(IdxVis)<2) else False

        for metType in self.metCollections:
          if metType in self.neglectMET: continue

          met = Object(event, metType)
          old_met_pt = met.pt
          old_met_phi = met.phi
          old_met_px = old_met_pt * math.cos(old_met_phi)
          old_met_py = old_met_pt * math.sin(old_met_phi)

          if noFix:
            new_met_pt = old_met_pt
            new_met_phi = old_met_phi
          else:
            # Three algorithms exist:
            # CorrectByMeanResolution -> Weights by shifting MC mean of uPara/uPerp to data and adjusting width of distribution
            # Correct -> Does the above by using quantile mapping: Using gaussian functions fitted to the recoil distributions
            # CorrectWithHist -> Uses quantile mapping with histograms instead of fits (overcomes the problem of poorly described tails of the hadronic recoil distributions)
            new_met_pt = self.Corrector[metType].CorrectWithHist_getPt(old_met_px, old_met_py, genPx, genPy, visPx, visPy, nJet30)
            new_met_phi = self.Corrector[metType].CorrectWithHist_getPhi(old_met_px, old_met_py, genPx, genPy, visPx, visPy, nJet30)

          self.out.fillBranch(metType+'_pt', new_met_pt)
          self.out.fillBranch(metType+'_phi', new_met_phi)
          if self.moreVars:
            self.out.fillBranch(metType+'_recoilCorrDiff_pt', new_met_pt - old_met_pt)
            self.out.fillBranch(metType+'_recoilCorrDiff_phi', new_met_phi - old_met_phi)

        return True


