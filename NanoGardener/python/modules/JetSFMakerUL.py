import os
import ROOT

from PhysicsTools.NanoAODTools.postprocessing.framework.eventloop import Module
from PhysicsTools.NanoAODTools.postprocessing.framework.datamodel import Collection 
from correctionlib import _core
import gzip

class JetSFMakerUL(Module):
    # -------------------------------------------------------------------------------------
    # Add branches for Jet PUID scale factors and up/down SF variations (per jet).
    # Also store per event weights calculated as a product of per jet SFs.
    # Pre-requisities:
    #   cms-NanoAOD tool "correctionlib"
    #    --> follow: https://cms-nanoaod.github.io/correctionlib/install.html
    #   cms-NanoAOD librabry "jsonpog-integration/POG/JME/"  
    #    --> git clone ssh://git@gitlab.cern.ch:7999/cms-nanoAOD/jsonpog-integration.git
    # -------------------------------------------------------------------------------------

    def __init__(self, year, cmssw, puid="loose"):
        self.wp = puid.lower()  
        self.era = str(year)
        if cmssw != "":
           if "v9HIPM" in cmssw: self.era += "preVFP_UL"
           elif "v9" in cmssw and self.era == "2016": self.era += "postVFP_UL"
           elif "v9" in cmssw: self.era += "_UL"
           else: self.era += "_EOY"
        else: self.era += "_EOY"
        cmssw_base = os.getenv('CMSSW_BASE')
        if "UL" not in self.era:
            fname = '%s/src/jsonpog-integration/POG/JME/%s/%s_jmar.json.gz' % (cmssw_base,self.era,str(year))
        else:
            fname = '%s/src/jsonpog-integration/POG/JME/%s/jmar.json.gz' % (cmssw_base,self.era) 
        if not os.path.exists(fname):
            raise FileNotFoundError(fname) 
        with gzip.open(fname,'rt') as file:
            data = file.read().strip()
            evaluator = _core.CorrectionSet.from_string(data)
        self.corr = evaluator["PUJetID_eff"]

    def beginFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        self.out = wrappedOutputTree

        self.out.branch('Jet_PUIDSF_%s' % self.wp, 'F', lenVar='nJet')
        self.out.branch('Jet_PUIDSF_%s_up' % self.wp, 'F', lenVar='nJet')
        self.out.branch('Jet_PUIDSF_%s_down' % self.wp, 'F', lenVar='nJet')
        self.out.branch('puidWeight', 'F')
        self.out.branch('puidWeightUp', 'F')
        self.out.branch('puidWeightDown', 'F')

    def analyze(self, event):
        jets = Collection(event, 'Jet')
        leptons = Collection(event, 'Lepton')
        WP = self.wp.upper()[0]

        puidWeight = 1.
        puidWeightUp = 1.
        puidWeightDown = 1.   
        sfs = []
        sfs_up = []
        sfs_down = []
        for jet in jets:
            jtype = {'genMatched' : False, 'cleanMatched' : False, 'passedPUID' : False}
            # Gen matching
            if jet.genJetIdx != -1: # Not matched jet is considered PileUp-jet
                jtype['genMatched'] = True
            # Clean matching
            if self.jetIsClean(jet,leptons): # Clean jets w/o PU ID requirement
                jtype['cleanMatched'] = True    
            # PileUp ID check
            puId = jet.puId 
            if "UL" not in self.era or ("UL" in self.era and "2016" not in self.era):
                pu_loose  = bool(puId & (1 << 2))
                pu_medium = bool(puId & (1 << 1))
                pu_tight  = bool(puId & (1 << 0))
            else:
                pu_loose  = bool(puId & (1 << 0))
                pu_medium = bool(puId & (1 << 1))
                pu_tight  = bool(puId & (1 << 2))      
            if WP == "L": jtype['passedPUID'] = pu_loose
            if WP == "M": jtype['passedPUID'] = pu_medium
            if WP == "T": jtype['passedPUID'] = pu_tight  
            
            # Get ingredients
            if not jtype['cleanMatched']:
                # We do not apply PU ID here 
                sf, sf_up, sf_down, effMC = 1.,1.,1.,0. 
            else:
                sf = self.corr.evaluate(jet.eta, jet.pt, "nom", WP)
                sf_up = self.corr.evaluate(jet.eta, jet.pt, "up", WP)
                sf_down = self.corr.evaluate(jet.eta, jet.pt, "down", WP)
                effMC = self.corr.evaluate(jet.eta, jet.pt, "MCEff", WP)

            # Calculate and store per-jet weights
            puid_jw     = 1.
            puid_upjw   = 1.
            puid_downjw = 1.
            if jtype['cleanMatched'] and jtype['passedPUID']:
                puid_jw = sf
                if jtype['genMatched'] or abs(jet.eta) > 2.5: 
                    up   = sf_up
                    down = sf_down
                else:
                    up   = 1 + abs(sf-1)
                    down = 1 - abs(sf-1)
                puid_upjw   = up
                puid_downjw = down   
            else: 
                puid_jw = (1.-sf*effMC)/(1.-effMC)
                if jtype['genMatched'] or abs(jet.eta) > 2.5:
                    up   = sf_up
                    down = sf_down 
                else:
                    up   = 1 + abs(sf-1)
                    down = 1 - abs(sf-1)
                puid_upjw   = (1.-up*effMC)/(1.-effMC)
                puid_downjw = (1.-down*effMC)/(1.-effMC) 
            sfs.append(puid_jw)
            sfs_up.append(puid_upjw)
            sfs_down.append(puid_downjw)

            # Calculate per-event weights
            puidWeight     *= puid_jw
            puidWeightUp   *= puid_upjw
            puidWeightDown *= puid_downjw    

        # Store  
        self.out.fillBranch('Jet_PUIDSF_%s' % self.wp, sfs)            
        self.out.fillBranch('Jet_PUIDSF_%s_up' % self.wp, sfs_up)
        self.out.fillBranch('Jet_PUIDSF_%s_down' % self.wp, sfs_down)
        self.out.fillBranch('puidWeight', puidWeight)
        self.out.fillBranch('puidWeightUp', puidWeightUp)
        self.out.fillBranch('puidWeightDown', puidWeightDown)  

        return True

    def jetIsClean(self, jet, leptons):
        # ------------------------------------------------------------------
        # Auxiliary function to mimic jet cleaning
        # All conditions as for CleanJet collection are applied but PU ID!
        # Extra requirements:
        #  -> 30. < jet.pt < 50. 
        # ------------------------------------------------------------------
  
        minLepPt = 10.
        maxJetEta = 4.7
        minJetPt = 30.
        maxJetPt = 50.
        jetId = 2

        # First minimize subset of jets
        if jet.pt < minJetPt: return False
        if jet.pt > maxJetPt: return False
        if abs(jet.eta) > maxJetEta: return False 
        if jet.jetId < jetId: return False 

        # Then general cleaning from leptons
        isClean = True
        for lepton in leptons:
            if lepton.pt < minLepPt: continue
            if self.jetIsLepton(jet.eta,jet.phi,lepton.eta,lepton.phi):
                isClean = False
                break
            
        return isClean

    def jetIsLepton(self, jetEta, jetPhi, lepEta, lepPhi) :
        dPhi = ROOT.TMath.Abs(lepPhi - jetPhi)
        if dPhi > ROOT.TMath.Pi() :
          dPhi = 2*ROOT.TMath.Pi() - dPhi
        dR2 = (lepEta - jetEta) * (lepEta - jetEta) + dPhi * dPhi
        if dR2 < 0.3*0.3:
            return True
        else:
            return False

