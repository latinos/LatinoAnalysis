import ROOT
import math
import os.path
ROOT.PyConfig.IgnoreCommandLineOptions = True

from PhysicsTools.NanoAODTools.postprocessing.framework.datamodel import Collection 
from PhysicsTools.NanoAODTools.postprocessing.framework.eventloop import Module

class mt2Producer(Module):

    ###
    def __init__(self, analysisRegion = '',  dataType = 'mc', looseEleWP = '', looseMuoWP = ''):

        self.analysisRegion = analysisRegion
        self.dataType = dataType
        self.looseEleWp = looseEleWP
        self.looseMuoWp = looseMuoWP

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

        self.out.branch("ptmiss",          "F")
        self.out.branch("ptmiss_phi",      "F")
        self.out.branch("lep0idx",         "I")
        self.out.branch("lep1idx",         "I")

        if 'Fake' in self.analysisRegion:

            self.out.branch("mt2llfake0",      "F")
            self.out.branch("mt2llfake1",      "F")
            self.out.branch("mt2llfake2",      "F")
            self.out.branch("lep2idx",         "I")

        else:

            self.out.branch("channel",         "I")
            self.out.branch("mll",             "F")
            self.out.branch("mt2ll",           "F")

            if 'WZ' in self.analysisRegion or 'ttZ' in self.analysisRegion:
                
                self.out.branch("deltaMassZ",  "F")

        if self.analysisRegion=='':

            self.out.branch("ptmiss_reco",          "F")
            self.out.branch("ptmiss_reco_phi",      "F")
            self.out.branch("mt2ll_reco",           "F")

            if self.dataType!='data':

                self.out.branch("ptmiss_gen",       "F")
                self.out.branch("ptmiss_gen_phi",   "F")
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

        if math.isnan(event.MET_pt): 
            print 'mt2Producer warning: MET_pt is nan'
            return False

        nLeptons = event.nLepton

        if nLeptons<2 :
            return False

        mll        = -1.
        ptmiss     = -1.
        mt2ll      = -1.
        deltaMassZ = -1.
        
        leptons   = Collection(event, 'Lepton')

        lepLoose  = [ ] 
        lepVect   = ROOT.vector('TLorentzVector')()

        for iLep in range(nLeptons) :

            isLooseLepton = False
            if abs(leptons[iLep].pdgId)==11:
                if looseEleWP=='' or (hasattr(leptons[iLep], 'isTightElectron_'+self.looseEleWP))==1: 
                    isLooseLepton = True
            elif abs(leptons[iLep].pdgId)==13:
                if LooseMuoWP=='' or (hasattr(leptons[iLep], 'isTightMuon_'+self.looseMuoWP))==1:
                    isLooseLepton = True

            if isLooseLepton:

                lepLoose.append(iLep)
                lepton = ROOT.TLorentzVector()
                lepton.SetPtEtaPhiM(leptons[iLep].pt, leptons[iLep].eta, leptons[iLep].phi, self.getLeptonMass(leptons[iLep].pdgId))
                lepVect.push_back(lepton)

        nLooseLeptons = len(lepLoose)
           
        if nLooseLeptons<2: return False
 
        ptmissvec3 = ROOT.TVector3()
        if hasattr(event, 'METFixEE2017_pt_nom'):
            ptmissvec3.SetPtEtaPhi(event.METFixEE2017_pt_nom, 0., event.METFixEE2017_phi_nom) 
        else:
            ptmissvec3.SetPtEtaPhi(event.MET_pt, 0., event.MET_phi)
        
        # Looking for the leptons to turn into neutrinos
        Lost = []
        Skip = []

        if self.analysisRegion=='' or self.analysisRegion=='gen' or self.analysisRegion=='reco':

            if nLooseLeptons>2: return False
            if leptons[lepLoose[0]].pdgId*leptons[lepLoose[1]].pdgId>0 : return False
        
        elif 'SameSign' in self.analysisRegion :

            if nLooseLeptons>2: return False
            if leptons[lepLoose[0]].pdgId*leptons[lepLoose[1]].pdgId<0 : return False

        elif 'Fake' in self.analysisRegion :
    
            if nLooseLeptons!=3: return False

            ptmissvec4 = ROOT.TLorentzVector()  
            ptmissvec4.SetPtEtaPhiM(ptmissvec3.Pt(), 0., ptmissvec3.Phi(), 0.)

            mt2llfakes = [ ] 

            for lref in range(nLooseLeptons) :

                mt2ll_ref = 0.

                for l0 in range(nLooseLeptons) :
                    if l0!=lref and lepVect[l0].Pt()>=25.:
                        for l1 in range (l0+1, nLooseLeptons) :
                            if l1!=lref and lepVect[l1].Pt()>=20.:
                                if (lepVect[l0] + lepVect[l1]).M()>=20.:
                                    if leptons[lepLoose[l0]].pdgId*leptons[lepLoose[l1]].pdgId<0:

                                        mt2ll_ref = self.computeMT2(lepVect[l0], lepVect[l1], ptmissvec4)
                                        
                mt2llfakes.append(mt2ll_ref)

            if sum(mt2llfakes)>0.:

                for lref in range(nLooseLeptons):
                    self.out.fillBranch("mt2llfake"+str(lref), mt2llfakes[lref])

                self.out.fillBranch("ptmiss", ptmissvec3.Pt())
                self.out.fillBranch("ptmiss_phi", ptmissvec3.Phi())
                self.out.fillBranch("lep0idx", lepLoose[0])
                self.out.fillBranch("lep1idx", lepLoose[1])
                self.out.fillBranch("lep2idx", lepLoose[2])

                return True
            
            return False

        elif 'WZ' in self.analysisRegion :
                
            if nLooseLeptons!=3 :
                return False

            minDZM = 15. if ('WZtoWW' in self.analysisRegion) else 999. 

            lost = -1
            
            for l0 in range(nLooseLeptons) :
                for l1 in range (l0+1, nLooseLeptons) :
                    if abs(leptons[lepLoose[l0]].pdgId)==abs(leptons[lepLoose[l1]].pdgId) :
                        if leptons[lepLoose[l0]].pdgId*leptons[lepLoose[l1]].pdgId<0 :
                            if abs((lepVect[l0] + lepVect[l1]).M() - self.Zmass)<minDZM :
                                
                                # There might be a more elegant way ...
                                for l2 in range (nLooseLeptons) :
                                    if l2!=l0 and l2!=l1 :
                                        
                                        if leptons[lepLoose[l2]].pdgId*leptons[lepLoose[l0]].pdgId>0 :
                                            lost = l0
                                        else :
                                            lost = l1
                                                
                                minDZM = abs((lepVect[l0] + lepVect[l1]).M() - self.Zmass)
                              
            if lost==-1 :
                return False

            deltaMassZ = minDZM

            if 'WZtoWW' in self.analysisRegion :
                Lost.append(lost)
            else :
                Skip.append(lost)

        elif 'ZZ' in self.analysisRegion or 'ttZ' in self.analysisRegion :
 
            if nLooseLeptons<4 :
                return False

            cutDZM1, cutDZM2, minDZMT = 15., 30., 999.
            lost0, lost1 = -1, -1

            for l0 in range (nLooseLeptons) :
                for l1 in range (l0+1, nLooseLeptons) :
                    if abs(leptons[lepLoose[l0]].pdgId)==abs(leptons[lepLoose[l1]].pdgId) :
                        if leptons[lepLoose[l0]].pdgId*leptons[lepLoose[l1]].pdgId<0 :

                            DZM1 = abs((lepVect[l0] + lepVect[l1]).M() - self.Zmass)
                            if DZM1<cutDZM1 :
                            
                                for l2 in range (nLooseLeptons) :
                                    if l2!=l0 and l2!=l1 :
                                        for l3 in range (l2+1, nLooseLeptons) :
                                            if l3!=l0 and l3!=l1 :
                                                if leptons[lepLoose[l2]].pdgId*leptons[lepLoose[l3]].pdgId<0 :
                                                    
                                                    if 'ttZ' in self.analysisRegion :

                                                        lost0, lost1 = l0, l1
                                                        cutDZM1 = DZM1

                                                    elif 'ZZ' in self.analysisRegion :

                                                        if abs(leptons[lepLoose[l2]].pdgId)==abs(leptons[lepLoose[l3]].pdgId) :

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
                
            deltaMassZ = cutDZM1
            
            Lost.append(lost0)
            Lost.append(lost1)

        # Computing variables to be added to the tree
        W0, W1 = -1, -1

        for iLep in range(nLooseLeptons) :

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
        ptmiss_phi = ptmissvec.Phi()
        mt2ll = self.computeMT2(lepVect[W0], lepVect[W1], ptmissvec)

        channel = 1
        if abs(leptons[lepLoose[W0]].pdgId)==13 : channel += 1
        if abs(leptons[lepLoose[W1]].pdgId)==13 : channel += 1
        if leptons[lepLoose[W0]].pdgId*leptons[lepLoose[W1]].pdgId<0:
            channel *= -1

        self.out.fillBranch("channel",    channel)
        self.out.fillBranch("mll",        mll)
        self.out.fillBranch("lep0idx",    lepLoose[W0])
        self.out.fillBranch("lep1idx",    lepLoose[W1])

        if 'WZ' in self.analysisRegion or 'ttZ' in self.analysisRegion:
            self.out.fillBranch("deltaMassZ",        deltaMassZ)

        if self.analysisRegion=='' or self.analysisRegion=='gen' or self.analysisRegion=='reco':

            if self.analysisRegion=='':
                self.out.fillBranch("ptmiss_reco",     ptmiss)
                self.out.fillBranch("ptmiss_reco_phi", ptmiss_phi)
                self.out.fillBranch("mt2ll_reco",      mt2ll)

            if self.dataType!='data':

                ptmissgenvec = ROOT.TLorentzVector()
                ptmissgenvec.SetPtEtaPhiM(event.GenMET_pt, 0., event.GenMET_phi, 0.)
            
                ptmiss_gen = ptmissgenvec.Pt()
                ptmiss_gen_phi = ptmissgenvec.Phi()
                mt2ll_gen = self.computeMT2(lepVect[0], lepVect[1], ptmissgenvec)

                if self.analysisRegion=='':
                    self.out.fillBranch("ptmiss_gen",     ptmiss_gen)
                    self.out.fillBranch("ptmiss_gen_phi", ptmiss_gen_phi)
                    self.out.fillBranch("mt2ll_gen",      mt2ll_gen)

                if self.dataType=='fastsim':
           
                    if self.analysisRegion=='':
                        ptmiss = (ptmiss + ptmiss_gen)/2.
                        mt2ll = (mt2ll + mt2ll_gen)/2.
                    elif self.analysisRegion=='gen':
                        ptmiss = ptmiss_gen
                        mt2ll = mt2ll_gen
 

        self.out.fillBranch("ptmiss",     ptmiss)
        self.out.fillBranch("ptmiss_phi", ptmiss_phi)
        self.out.fillBranch("mt2ll",      mt2ll)

        return True
 
