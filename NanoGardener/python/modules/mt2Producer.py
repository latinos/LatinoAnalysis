import ROOT
import math
import os.path
ROOT.PyConfig.IgnoreCommandLineOptions = True

from PhysicsTools.NanoAODTools.postprocessing.framework.datamodel import Collection 
from PhysicsTools.NanoAODTools.postprocessing.framework.eventloop import Module

class mt2Producer(Module):

    ###
    def __init__(self, analysisRegion = '',  dataType = 'mc'):

        self.analysisRegion = analysisRegion
        self.dataType = dataType

        self.Zmass = 91.1876

        cmssw_base = os.getenv('CMSSW_BASE')
        ROOT.gROOT.ProcessLine('.L '+cmssw_base+'/src/LatinoAnalysis/NanoGardener/python/modules/lester_mt2_bisect.h+')
     
        pass

    ###
    def beginJob(self):
        ROOT.asymm_mt2_lester_bisect().disableCopyrightMessage()
        pass

    ###
    def endJob(self):
        pass

    ###
    def beginFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        self.out = wrappedOutputTree

        self.out.branch("mt2ll",           "F")

    ###    
    def endFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        pass

    ###
    def getLeptonMass(self, pdgId) :
    
        if abs(pdgId)==11 :
            return 0.000511
        elif abs(pdgId)==13 :
            return 0.105658
        else :
            print 'mt2llProducer: WARNING: unsupported lepton pdgId'
            return -1
        
    ###
    def computeMT2(self, VisibleA, VisibleB, Invisible, MT2Type = 0, MT2Precision = 0) :

        mVisA = abs(VisibleA.M())  # Mass of visible object on side A. Must be >= 0
        mVisB = abs(VisibleB.M())  # Mass of visible object on side B. Must be >= 0

        chiA = 0.  # Hypothesised mass of invisible on side A. Must be >= 0
        chiB = 0.  # Hypothesised mass of invisible on side B. Must be >= 0
  
        if MT2Type== 1 : # This is for mt2 with b jets

            mVisA =  5.
            mVisB =  5.
            chiA  = 80.
            chiB  = 80.
            
        pxA = VisibleA.Px()  # x momentum of visible object on side A
        pyA = VisibleA.Py()  # y momentum of visible object on side A
        
        pxB = VisibleB.Px()  # x momentum of visible object on side B
        pyB = VisibleB.Py()  # y momentum of visible object on side B
        
        pxMiss = Invisible.Px()  # x component of missing transverse momentum
        pyMiss = Invisible.Py()  # y component of missing transverse momentum
        
        # Must be >= 0
        # If = 0 algorithm aims for machine precision
        # If > 0 MT2 computed to supplied absolute precision
        desiredPrecisionOnMt2 = MT2Precision
        
        mT2 = ROOT.asymm_mt2_lester_bisect().get_mT2(mVisA, pxA, pyA,
                                                     mVisB, pxB, pyB,
                                                     pxMiss, pyMiss,
                                                     chiA, chiB,
                                                     desiredPrecisionOnMt2)

        return mT2
    
    ###
    def analyze(self, event):
        """process event, return True (go to next module) or False (fail, go to next event)"""

        nLeptons = event.nLepton

        if nLeptons<2 :
            return False

        mt2ll     = -1.
        
        leptons   = Collection(event, 'Lepton')

        lepVect   = ROOT.vector('TLorentzVector')()

        for iLep in range(nLeptons) :

            lepton = ROOT.TLorentzVector()
            lepton.SetPtEtaPhiM(leptons[iLep].pt, leptons[iLep].eta, leptons[iLep].phi, self.getLeptonMass(leptons[iLep].pdgId))
            lepVect.push_back(lepton)
        
        # Looking for the leptons to turn into neutrinos
        Lost = []
        Skip = []

        #if nLeptons>2 or nVetoLeptons>2: return False
        if leptons[0].pdgId*leptons[1].pdgId>0 : return False

        # Computing variables to be added to the tree
        W0, W1 = -1, -1
            
        ptmissvec3 = ROOT.TVector3()
        ptmissvec3.SetPtEtaPhi(event.PuppiMET_pt, 0., event.PuppiMET_phi) 
        
        for iLep in range(nLeptons) :

            if iLep in Lost :
                ptmissvec3 += lepVect[iLep].Vect()
            elif iLep not in Skip :
                if W0==-1 : W0 = iLep
                elif W1==-1 : W1 = iLep

        if lepVect[W0].Pt()<25. : return False
        if lepVect[W1].Pt()<20. : return False

        mll = (lepVect[W0] + lepVect[W1]).M()  

        if mll<12. : return False

        ptmissvec = ROOT.TLorentzVector()  
        ptmissvec.SetPtEtaPhiM(ptmissvec3.Pt(), 0., ptmissvec3.Phi(), 0.)
            
        ptmiss = ptmissvec.Pt()
        mt2ll = self.computeMT2(lepVect[W0], lepVect[W1], ptmissvec)
 
        self.out.fillBranch("mt2ll",      mt2ll)

        return True
 
