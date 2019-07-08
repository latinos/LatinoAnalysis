import ROOT
import math
from array import array
ROOT.PyConfig.IgnoreCommandLineOptions = True

from PhysicsTools.NanoAODTools.postprocessing.framework.datamodel import Collection 
from PhysicsTools.NanoAODTools.postprocessing.framework.eventloop import Module

from LatinoAnalysis.NanoGardener.data.SusyISRCorrections import SUSYISRCorrections

class SusyWeightsProducer(Module):

    ###
    def __init__(self, cmssw):
        self.cmssw = cmssw
        pass

    ###
    def beginJob(self):
        self.massScanIsFilled = False
        pass

    ###
    def endJob(self):
        pass

    ###
    def beginFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        self.out = wrappedOutputTree
        self.out.branch("baseW",         "F")
        self.out.branch("isrW",          "F")

        if self.massScanIsFilled==False :

            inputFileName = inputFile.GetName()
            
            chain = ROOT.TChain('Events');
            
            if '__part' in inputFileName :
                inputFileName = inputFileName[:inputFileName.index('__part')] + '__part*.root'

            chain.Add(inputFileName)

            self.massScan = ROOT.TH2D("massScan", "", 3000, 0., 3000., 3000, 0., 3000.)
            chain.Project(self.massScan.GetName(), "susyMLSP:susyMprompt", "genWeight", "")

            self.isrObservable = ''

            for isrObs in SUSYISRCorrections:
                for susyModel in SUSYISRCorrections[isrObs]['susyModels'] :
                    if susyModel in inputFileName :
                        for isrVer in SUSYISRCorrections[isrObs]['version']:
                            if self.cmssw in SUSYISRCorrections[isrObs]['version'][isrVer]['production'].keys():

                                self.isrObservable = isrObs
                        
                                self.isrEdge = []
                                self.isrCorrection = []

                                for edge in sorted(SUSYISRCorrections[isrObs]['version'][isrVer]['correction'].keys()) :
                                    
                                    self.isrEdge.append( float(edge) )
                                    self.isrCorrection.append( float(SUSYISRCorrections[isrObs]['version'][isrVer]['correction'][edge]) )

                                    self.isrBins = len(self.isrEdge) - 1

            if self.isrObservable=='' :
                raise Exception('SusyWeightsProducer ERROR: SUSY model not found for', inputFile.GetName())

            self.isrN = {}
            
            for xb in range(1, self.massScan.GetNbinsX()+1) :
                for yb in range(1, self.massScan.GetNbinsY()+1) :
                    if self.massScan.GetBinContent(xb, yb)>0. :

                        histoISR = ROOT.TH1D("histoISR", "", self.isrBins, array('d',self.isrEdge))
                        chain.Project(histoISR.GetName(), self.isrObservable, "(susyMprompt=="+str(xb-1)+" && susyMLSP=="+str(yb-1)+")*genWeight", "")

                        reweightedNormalization = 0.
                        for ib in range(self.isrBins+1) :
                            reweightedNormalization += histoISR.GetBinContent(ib+1)*self.isrCorrection[ib]

                        normFactor = histoISR.Integral(0, self.isrBins+1)/reweightedNormalization

                        self.isrN.update({str(xb-1)+"-"+str(yb-1):normFactor})
                        print 'SusyWeightsProducer: overall ISR normalization factor for mass point (',str(xb-1),',',str(yb-1),'):', normFactor

            self.massScanIsFilled = True

    ###    
    def endFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        pass

    ###
    def analyze(self, event):
        """process event, return True (go to next module) or False (fail, go to next event)"""

        Xsec  = event.Xsec
        massScanBin = self.massScan.FindBin(event.susyMprompt, event.susyMLSP)
        nevents = self.massScan.GetBinContent(massScanBin)
        
        baseW = 1000.*Xsec/nevents

        isrW = self.isrN[str(int(event.susyMprompt))+'-'+str(int(event.susyMLSP))]
        for ib in reversed(xrange(self.isrBins+1)) :
            if getattr(event, self.isrObservable) >= self.isrEdge[ib] :
                isrW *= self.isrCorrection[ib]
                break

        self.out.fillBranch("baseW",   baseW)
        self.out.fillBranch("isrW",    isrW)      
            
        return True
 
