import ROOT
import math
ROOT.PyConfig.IgnoreCommandLineOptions = True

from PhysicsTools.NanoAODTools.postprocessing.framework.datamodel import Collection 
from PhysicsTools.NanoAODTools.postprocessing.framework.eventloop import Module

from LatinoAnalysis.NanoGardener.framework.samples.susyCrossSections import SUSYCrossSections

class SusyGenVarsProducer(Module):

    ###
    def __init__(self):
        pass

    ###
    def beginJob(self):
        self.susyModelIsSet = False
        pass

    ###
    def endJob(self):
        pass

    ###
    def beginFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        self.out = wrappedOutputTree

        self.out.branch("susyMprompt",     "F")
        self.out.branch("susyMstop",       "F")
        self.out.branch("susyMLSP",        "F")
        self.out.branch("susyMChargino",   "F")
        self.out.branch("susyMSlepton",    "F")
        self.out.branch("Xsec",            "F")
        self.out.branch("XsecUncertainty", "F")
        self.out.branch("ptISR",           "F")
        self.out.branch("njetISR",         "F")

        if self.susyModelIsSet==False :

            self.susyProcess = ''

            for process in SUSYCrossSections :
                for susyModel in SUSYCrossSections[process]['susyModels'] :
                    if susyModel in inputFile.GetName() :
                        self.susyProcess = process

            if self.susyProcess=='' :
                raise Exception('SusyGenVarsProducer ERROR: SUSY process not found for', inputFile.GetName())
            
            self.susyModelIsSet = True

    ###    
    def endFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        pass

    def getCrossSectionUncertainty(self, susyProcess, isusyMass):
        
        xsUnc = SUSYCrossSections[susyProcess]['massPoints'][str(isusyMass)]['uncertainty']
        if '%' not in xsUnc: 
            return float(xsUnc)
        else:
            xsUnc = xsUnc.replace('%', '')
            return float(SUSYCrossSections[susyProcess]['massPoints'][str(isusyMass)]['value'])*float(xsUnc)/100.

    def getCrossSection(self, susyProcess, susyMass):

        isusyMass = int(susyMass)

        if str(isusyMass) in SUSYCrossSections[susyProcess]['massPoints'].keys() :
            
            return [float(SUSYCrossSections[susyProcess]['massPoints'][str(isusyMass)]['value']),
                    self.getCrossSectionUncertainty(susyProcess, isusyMass)]
        
        elif isusyMass%5!=0 :
                    
            isusyMass1 = 5*(isusyMass/5)
            isusyMass2 = 5*(isusyMass/5+1)
                    
            if str(isusyMass1) in SUSYCrossSections[susyProcess]['massPoints'].keys() and str(isusyMass2) in SUSYCrossSections[susyProcess]['massPoints'].keys() :

                susyXsec1 = float(SUSYCrossSections[susyProcess]['massPoints'][str(isusyMass1)]['value'])
                susyXsec2 = float(SUSYCrossSections[susyProcess]['massPoints'][str(isusyMass2)]['value'])

                slope = -math.log(susyXsec2/susyXsec1)/(isusyMass2-isusyMass1)
                susyXsec = susyXsec1*math.exp(-slope*(isusyMass-isusyMass1))

                susyXsecRelUnc = (self.getCrossSectionUncertainty(susyProcess, isusyMass1)/susyXsec1 + 
                                  self.getCrossSectionUncertainty(susyProcess, isusyMass2)/susyXsec2)/2.
                
                return [susyXsec, susyXsec*susyXsecRelUnc]

        raise Exception('SusyGenVarsProducer ERROR: cross section not available for', self.susyProcess, 'at mass =', susyMass)

    ###
    def analyze(self, event):
        """process event, return True (go to next module) or False (fail, go to next event)"""

        massPrompt   = -1.
        massStop     = -1.
        massLSP      = -1.
        massChargino = -1.
        massSlepton  = -1.
        xSection     = -1.
        xSecUncert   = -1.
        ptISR        = -1.
        njetISR      =  0.

        nSusyParticles = 0
        susyParticle1 = ROOT.TLorentzVector()
        susyParticle2 = ROOT.TLorentzVector()

        genParticles = Collection(event, "GenPart")

        # http://pdg.lbl.gov/2007/reviews/montecarlorpp.pdf
        for particle in genParticles :

            if abs(particle.pdgId)>=1000000 and abs(particle.pdgId)<=2001000 : # It is SUSY particle

                if abs(genParticles[particle.genPartIdxMother].pdgId)<1000000 : # Its mother is not SUSY

                    if nSusyParticles==0 :
                        massPrompt = particle.mass
                        susyParticle1.SetPtEtaPhiM(particle.pt, particle.eta, particle.phi, particle.mass)
                    elif nSusyParticles==1 :
                        susyParticle2.SetPtEtaPhiM(particle.pt, particle.eta, particle.phi, particle.mass)
                    nSusyParticles += 1

                if abs(particle.pdgId)==1000006 : # Stop1
                    massStop = particle.mass
                
                if abs(particle.pdgId)==1000022 : # Chi^0_1
                    massLSP = particle.mass
                    
                if abs(particle.pdgId)==1000024 : # Chi^{\pm}_1
                    massChargino = particle.mass
                        
                if ((abs(particle.pdgId)>=1000011 and abs(particle.pdgId)<=1000016) or # LH sleptons
                    (abs(particle.pdgId)==2000011 or abs(particle.pdgId)==2000013 or abs(particle.pdgId)==2000015)) : # RH sleptons
                    massSlepton = particle.mass

        xSec = self.getCrossSection(self.susyProcess, massPrompt)
        xSection = xSec[0]
        xSecUncert = xSec[1]
        
        if nSusyParticles==2 :
            ptISR = (susyParticle1+susyParticle2).Pt()
        else :
            print 'SusyGenVarsProducer WARNING:', nSusyParticles, 'SUSY particles found for pt ISR computation'

        # Adapted from (check for updates for nanoAOD):
        # https://github.com/manuelfs/babymaker/blob/0136340602ee28caab14e3f6b064d1db81544a0a/bmaker/plugins/bmaker_full.cc#L1268-L1295
        jetColl = Collection(event, "Jet")

        for jet in jetColl :
            # https://github.com/manuelfs/babymaker/blob/0136340602ee28caab14e3f6b064d1db81544a0a/bmaker/plugins/bmaker_full.cc#L372-L395
            if jet.jetId & 1 : # is loose 
                # https://github.com/manuelfs/babymaker/blob/11e7a6f26ed6c1efcd0027c8b4219eb69a997bae/bmaker/interface/jet_met_tools.hh
                if jet.pt>30 and abs(jet.eta)<2.4 :
                    
                    matched = False

                    jetV = ROOT.TLorentzVector()
                    jetV.SetPtEtaPhiM(jet.pt, jet.eta, jet.phi, jet.mass)
                    
                    for particle in genParticles :

                        if particle.genPartIdxMother>-1 :

                            matchThis = False

                            motherId = abs(genParticles[particle.genPartIdxMother].pdgId) 

                            if abs(particle.pdgId)==11 or abs(particle.pdgId)==13 :
                                if motherId==15 or motherId==23 or motherId==24 or motherId==25 or motherId>1e6 :
                                    matchThis = True
                        
                            if motherId<=5 : # Why not gluons?
                                if genParticles[particle.genPartIdxMother].genPartIdxMother>-1 :
                                    grandmotherId = abs(genParticles[genParticles[particle.genPartIdxMother].genPartIdxMother].pdgId) 
                                    if grandmotherId==6 or grandmotherId==23 or grandmotherId==24 or grandmotherId==25 or grandmotherId>1e6 : 
                                        matchThis = True

                            if matchThis==True :

                                parV = ROOT.TLorentzVector()
                                parV.SetPtEtaPhiM(particle.pt, particle.eta, particle.phi, particle.mass)

                                if jetV.DeltaR(parV)<0.3 :
                                    matched = True
                                    break

                    if matched==False:
                        njetISR += 1

        self.out.fillBranch("susyMprompt",     massPrompt)
        self.out.fillBranch("susyMstop",       massStop)
        self.out.fillBranch("susyMLSP",        massLSP)
        self.out.fillBranch("susyMChargino",   massChargino)
        self.out.fillBranch("susyMSlepton",    massSlepton)
        self.out.fillBranch("Xsec",            xSection)
        self.out.fillBranch("XsecUncertainty", xSecUncert)
        self.out.fillBranch("ptISR",           ptISR)
        self.out.fillBranch("njetISR",         njetISR)
            
        return True
 
