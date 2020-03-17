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

        self.out.branch("susyIDprompt",  "F")
        self.out.branch("susyMprompt",   "F")
        self.out.branch("susyMstop",     "F")
        self.out.branch("susyMLSP",      "F")
        self.out.branch("susyMChargino", "F")
        self.out.branch("susyMSlepton",  "F")
        self.out.branch("Xsec",          "F")
        self.out.branch("XsecUp",        "F")
        self.out.branch("XsecDown",      "F")
        self.out.branch("ptISR",         "F")
        self.out.branch("njetISR",       "F")

        if self.susyModelIsSet==False :

            self.susyProcess = ''
            self.susyModel = ''

            for process in SUSYCrossSections :
                for model in SUSYCrossSections[process]['susyModels'] :
                    if model in inputFile.GetName() :
                        self.susyProcess = process
                        self.susyModel = model

            if self.susyProcess=='' :
                print 'SusyGenVarsProducer WARNING: SUSY process not found for input file', inputFile.GetName()

                for model in SUSYCrossSections[process]['susyModels'] :
                    if model in outputFile.GetName() :
                        self.susyProcess = process
                        self.susyModel = model

                if self.susyProcess=='' :
                    print 'SusyGenVarsProducer WARNING: SUSY process not found for output file', outputFile.GetName()
            
            if self.susyProcess!='' :
                self.susyModelIsSet = True

    ###    
    def endFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        pass

    def getCrossSectionUncertainty(self, susyProcess, isusyMass, variation):
    
        if 'uncertainty'+variation not in SUSYCrossSections[susyProcess]['massPoints'][str(isusyMass)]: variation = ''
        xsUnc = SUSYCrossSections[susyProcess]['massPoints'][str(isusyMass)]['uncertainty'+variation]

        if '%' not in xsUnc: 
            return float(xsUnc)
        else:
            xsUnc = xsUnc.replace('%', '')
            return float(SUSYCrossSections[susyProcess]['massPoints'][str(isusyMass)]['value'])*float(xsUnc)/100.
        
        def getCrossSection(self, susyProcess, susyModel, susyMass):

            convBR = float(SUSYCrossSections[susyProcess]['susyModels'][susyModel])
        
            isusyMass = int(susyMass)
        
            if str(isusyMass) in SUSYCrossSections[susyProcess]['massPoints'].keys() :
        
                susyXsec = float(SUSYCrossSections[susyProcess]['massPoints'][str(isusyMass)]['value'])

                return [ convBR*susyXsec,
                         convBR*(susyXsec+self.getCrossSectionUncertainty(susyProcess, isusyMass, 'Up')),
                         convBR*(susyXsec-self.getCrossSectionUncertainty(susyProcess, isusyMass, 'Down')) ]
        
            else: # Try to extrapolate

                step = 5 # T2tt
            
                if 'Slepton' in susyProcess:
                    if isusyMass<=400:
                        step =  20
                    elif isusyMass<=440:
                        step =  40
                    elif isusyMass<=500:
                        step =  60
                    elif isusyMass<=1000:
                        step = 100
 
                isusyMass1 = step*(isusyMass/step)
                isusyMass2 = step*(isusyMass/step+1)

                if 'Slepton' in susyProcess:
                    if step==60:
                        isusyMass1 =  440
                        isusyMass2 =  500
                    elif isusyMass>1000:
                        isusyMass1 =  900
                        isusyMass2 = 1000

                if str(isusyMass1) in SUSYCrossSections[susyProcess]['massPoints'].keys() and str(isusyMass2) in SUSYCrossSections[susyProcess]['massPoints'].keys() :

                    susyXsec1 = float(SUSYCrossSections[susyProcess]['massPoints'][str(isusyMass1)]['value'])
                    susyXsec2 = float(SUSYCrossSections[susyProcess]['massPoints'][str(isusyMass2)]['value'])
            
                    slope = -math.log(susyXsec2/susyXsec1)/(isusyMass2-isusyMass1)
                    susyXsec = susyXsec1*math.exp(-slope*(isusyMass-isusyMass1))
            
                    susyXsecRelUncUp = (self.getCrossSectionUncertainty(susyProcess, isusyMass1, 'Up')/susyXsec1 + 
                                        self.getCrossSectionUncertainty(susyProcess, isusyMass2, 'Up')/susyXsec2)/2.
            
                    susyXsecRelUncDown = (self.getCrossSectionUncertainty(susyProcess, isusyMass1, 'Down')/susyXsec1 + 
                                          self.getCrossSectionUncertainty(susyProcess, isusyMass2, 'Down')/susyXsec2)/2.
            
                    return [convBR*susyXsec, convBR*susyXsec*(1.+susyXsecRelUncUp), convBR*susyXsec*(1.-susyXsecRelUncDown)]
            
                raise Exception('susyCrossSections ERROR: cross section not available for', self.susyProcess, 'at mass =', susyMass)

    ###
    def analyze(self, event):
        """process event, return True (go to next module) or False (fail, go to next event)"""

        idPrompt     = -1.
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
                        idPrompt = abs(particle.pdgId)
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

        if self.susyModelIsSet==False:
            if massStop>-1:
                self.susyProcess = 'StopSbottom'
                if massChargino>-1:
                    self.susyModel = 'T2bW'
                else:
                    self.susyModel = 'T2tt'
            elif massChargino>-1:
                self.susyProcess = 'WinoC1C1'
                if massSlepton>-1:
                    self.susyModel = 'TChipmSlepSnu'
                else:
                    self.susyModel = 'TChipmWW'
            elif massSlepton>-1:
                if idPrompt>=2000000:
                    self.susyProcess = 'SleptonHR'
                    if idPrompt==2000011:
                        self.susyModel = 'TSelectronSelectronHR'
                    elif idPrompt==2000013:
                        self.susyModel = 'TSmuonSmuonHR'
                else:
                    self.susyProcess = 'SleptonHL'
                    if idPrompt==1000011:
                        self.susyModel = 'TSelectronSelectronHL'
                    elif idPrompt==1000013:
                        self.susyModel = 'TSmuonSmuonHL'
            else:
                raise Exception('SusyGenVarsProducer ERROR: SUSY process not set from gen particle inspection either')
            print 'SusyGenVarsProducer WARNING: SUSY process set to', self.susyProcess, 'from gen particle inspection'
            self.susyModelIsSet = True
                
    
        susyMass = int(25*round(float(massPrompt)/25)) if ((massPrompt%25)>=21 or (massPrompt%25)<=4) else massPrompt
        xSection, xSectionUp, xSectionDown = self.getCrossSection(self.susyProcess, self.susyModel, susyMass)
        
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

        self.out.fillBranch("susyIDprompt",  idPrompt)
        self.out.fillBranch("susyMprompt",   massPrompt)
        self.out.fillBranch("susyMstop",     massStop)
        self.out.fillBranch("susyMLSP",      massLSP)
        self.out.fillBranch("susyMChargino", massChargino)
        self.out.fillBranch("susyMSlepton",  massSlepton)
        self.out.fillBranch("Xsec",          xSection)
        self.out.fillBranch("XsecUp",        xSectionUp)
        self.out.fillBranch("XsecDown",      xSectionDown)
        self.out.fillBranch("ptISR",         ptISR)
        self.out.fillBranch("njetISR",       njetISR)
            
        return True
 
