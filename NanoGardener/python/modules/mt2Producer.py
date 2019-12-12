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

        self.out.branch("channel",         "I")
        self.out.branch("mll",             "F")

        self.out.branch("ptmiss",          "F")
        self.out.branch("mt2ll",           "F")

        if self.analysisRegion=='':

            self.out.branch("ptmiss_reco",          "F")
            self.out.branch("mt2ll_reco",           "F")

            if self.dataType!='data':

                self.out.branch("ptmiss_gen",       "F")
                self.out.branch("mt2ll_gen",        "F")

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

        mll       = -1.
        ptmiss    = -1.
        mt2ll     = -1.

        nVetoLeptons = event.nVetoLepton
        
        leptons   = Collection(event, 'Lepton')

        lepVect   = ROOT.vector('TLorentzVector')()

        for iLep in range(nLeptons) :

            lepton = ROOT.TLorentzVector()
            lepton.SetPtEtaPhiM(leptons[iLep].pt, leptons[iLep].eta, leptons[iLep].phi, self.getLeptonMass(leptons[iLep].pdgId))
            lepVect.push_back(lepton)
        
        # Looking for the leptons to turn into neutrinos
        Lost = []
        Skip = []

        if self.analysisRegion=='' or self.analysisRegion=='gen' or self.analysisRegion=='reco':

            if nLeptons>2 or nVetoLeptons>2: return False
            if leptons[0].pdgId*leptons[1].pdgId>0 : return False
        
        elif 'SameSign' in self.analysisRegion :

            if nLeptons>2 or nVetoLeptons>2: return False
            if leptons[0].pdgId*leptons[1].pdgId<0 : return False

        elif 'WZ' in self.analysisRegion :
                
            if nLeptons!=3 or nVetoLeptons>=4:
                return False

            minDZM = 10.
            lost = -1
            
            for l0 in range (nLeptons) :
                for l1 in range (l0+1, nLeptons) :
                    if abs(leptons[l0].pdgId)==abs(leptons[l1].pdgId) :
                        if leptons[l0].pdgId*leptons[l1].pdgId<0 :
                            if abs((lepVect[l0] + lepVect[l1]).M() - self.Zmass)<minDZM :
                                
                                # There might be a more elegant way ...
                                for l2 in range (nLeptons) :
                                    if l2!=l0 and l2!=l1 :
                                        
                                        if leptons[l2].pdgId*leptons[l0].pdgId>0 :
                                            lost = l0
                                        else :
                                            lost = l1
                                                
                                minDZM = abs((lepVect[l0] + lepVect[l1]).M() - self.Zmass)
                              
            if lost==-1 :
                return False

            if 'WZtoWW' in self.analysisRegion :
                Lost.append(lost)
            else :
                Skip.append(lost)

        elif 'ZZ' in self.analysisRegion or 'ttZ' in self.analysisRegion :
 
            if nLeptons<4 :
                return False

            cutDZM1, cutDZM2, minDZMT = 15., 30., 999.
            lost0, lost1 = -1, -1

            for l0 in range (nLeptons) :
                for l1 in range (l0+1, nLeptons) :
                    if abs(leptons[l0].pdgId)==abs(leptons[l1].pdgId) :
                        if leptons[l0].pdgId*leptons[l1].pdgId<0 :

                            DZM1 = abs((lepVect[l0] + lepVect[l1]).M() - self.Zmass)
                            if DZM1<cutDZM1 :
                            
                                for l2 in range (nLeptons) :
                                    if l2!=l0 and l2!=l1 :
                                        for l3 in range (l2+1, nLeptons) :
                                            if l3!=l0 and l3!=l1 :
                                                if leptons[l2].pdgId*leptons[l3].pdgId<0 :
                                                    
                                                    if 'ttZ' in self.analysisRegion :

                                                        lost0, lost1 = l0, l1
                                                        cutDZM1 = DZM1
                    
                                                    elif 'ZZ' in self.analysisRegion :

                                                        if abs(leptons[l2].pdgId)==abs(leptons[l3].pdgId) :

                                                            DZM2 = abs((lepVect[l2] + lepVect[l3]).M() - self.Zmass)
                                                            if DZM2<cutDZM2 :
                                                                
                                                                DZMT = math.sqrt(DZM1*DZM1 + DZM2*DZM2)
                                                                if DZMT<minDZMT :

                                                                    if DZM1<DZM2 :
                                                                        lost0, lost1 = l0, l1
                                                                    else :
                                                                        lost0, lost1 = l2, l3
                                                                    minDZMT = DZMT
                                                                    
            if lost0==-1 or lost1==-1 :
                return False
            
            Lost.append(lost0)
            Lost.append(lost1)

        # Computing variables to be added to the tree
        W0, W1 = -1, -1
            
        ptmissvec3 = ROOT.TVector3()
        ptmissvec3.SetPtEtaPhi(event.MET_pt, 0., event.MET_phi) 
        
        for iLep in range(nLeptons) :

            if iLep in Lost :
                ptmissvec3 += lepVect[iLep].Vect()
            elif iLep not in Skip :
                if W0==-1 : W0 = iLep
                elif W1==-1 : W1 = iLep

        if lepVect[W0].Pt()<25. : return False
        if lepVect[W1].Pt()<20. : return False

        mll = (lepVect[W0] + lepVect[W1]).M()  

        if mll<20. : return False

        ptmissvec = ROOT.TLorentzVector()  
        ptmissvec.SetPtEtaPhiM(ptmissvec3.Pt(), 0., ptmissvec3.Phi(), 0.)
            
        ptmiss = ptmissvec.Pt()
        mt2ll = self.computeMT2(lepVect[W0], lepVect[W1], ptmissvec)

        channel = 0
        if abs(leptons[W0].pdgId)==13 : channel += 1
        if abs(leptons[W1].pdgId)==13 : channel += 1

        self.out.fillBranch("channel",    channel)
        self.out.fillBranch("mll",        mll)

        if self.analysisRegion=='' or self.analysisRegion=='gen' or self.analysisRegion=='reco':

            if self.analysisRegion=='':
                self.out.fillBranch("ptmiss_reco",   ptmiss)
                self.out.fillBranch("mt2ll_reco",    mt2ll)

            if self.dataType!='data':

                ptmissgenvec = ROOT.TLorentzVector()
                ptmissgenvec.SetPtEtaPhiM(event.GenMET_pt, 0., event.GenMET_phi, 0.)
            
                ptmiss_gen = ptmissgenvec.Pt()
                mt2ll_gen = self.computeMT2(lepVect[0], lepVect[1], ptmissgenvec)

                if self.analysisRegion=='':
                    self.out.fillBranch("ptmiss_gen",   ptmiss_gen)
                    self.out.fillBranch("mt2ll_gen",    mt2ll_gen)

                if self.dataType=='fastsim':
           
                    if self.analysisRegion=='':
                        ptmiss = (ptmiss + ptmiss_gen)/2.
                        mt2ll = (mt2ll + mt2ll_gen)/2.
                    elif self.analysisRegion=='gen':
                        ptmiss = ptmiss_gen
                        mt2ll = mt2ll_gen
 

        self.out.fillBranch("ptmiss",     ptmiss)
        self.out.fillBranch("mt2ll",      mt2ll)

        return True
 
