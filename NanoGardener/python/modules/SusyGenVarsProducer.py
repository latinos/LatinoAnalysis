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

        self.out.branch("susyMprompt",   "F")
        self.out.branch("susyMstop",     "F")
        self.out.branch("susyMLSP",      "F")
        self.out.branch("susyMChargino", "F")
        self.out.branch("susyMSlepton",  "F")
        self.out.branch("Xsec",          "F")
        self.out.branch("ptISR",         "F")

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

    def getCrossSection(self, susyProcess, susyMass) :

        isusyMass = int(susyMass)

        if str(isusyMass) in SUSYCrossSections[susyProcess]['masspoints'].keys() :
            
            return float(SUSYCrossSections[susyProcess]['masspoints'][str(isusyMass)]['value'])
        
        elif isusyMass%5!=0 :
                    
            isusyMass1 = 5*(iSusyMass/5)
            isusyMass2 = 5*(iSusyMass/5+1)
                    
            if str(isusyMass1) in SUSYCrossSections[susyProcess]['masspoints'].keys() and str(isusyMass2) in SUSYCrossSections[susyProcess]['masspoints'].keys() :

                susyXsec1 = float(SUSYCrossSections[susyProcess]['masspoints'][str(isusyMass1)]['value'])
                susyXsec2 = float(SUSYCrossSections[susyProcess]['masspoints'][str(isusyMass2)]['value'])

                slope = -math.log(susyXsec2/susyXsec1)/(isusyMass2-isusyMass1)
                
                return isusyMass1*math.exp(-slope*(isusyMass-isusyMass1))

        
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
        ptISR        = -1.

        nSusyParticles = 0
        susyParticle1 = ROOT.TLorentzVector()
        susyParticle2 = ROOT.TLorentzVector()

        genParticles = Collection(event, "GenPart")

        # http://pdg.lbl.gov/2007/reviews/montecarlorpp.pdf
        for particle in genParticles :

            if abs(particle.pdgId)>=1000000 and abs(particle.pdgId)<=2001000 : # It´s SUSY particle

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

        xSection = self.getCrossSection(self.susyProcess, massPrompt)
        
        if nSusyParticles==2 :
            ptISR = (susyParticle1+susyParticle2).Pt()
        else :
            print 'SusyGenVarsProducer WARNING:', nSusyParticles, 'SUSY particles found for pt ISR computation'
 
        self.out.fillBranch("susyMprompt",   massPrompt)
        self.out.fillBranch("susyMstop",     massStop)
        self.out.fillBranch("susyMLSP",      massLSP)
        self.out.fillBranch("susyMChargino", massChargino)
        self.out.fillBranch("susyMSlepton",  massSlepton)
        self.out.fillBranch("Xsec",          xSection)
        self.out.fillBranch("ptISR",         ptISR)
            
        return True
 
