import ROOT
import math
ROOT.PyConfig.IgnoreCommandLineOptions = True

from PhysicsTools.NanoAODTools.postprocessing.framework.datamodel import Collection 
from PhysicsTools.NanoAODTools.postprocessing.framework.eventloop import Module

class SusyWeightsProducer(Module):

    ###
    def __init__(self):
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

        if self.massScanIsFilled==False :

            inputFileName = inputFile.GetName()
            
            chain = ROOT.TChain('Events');
            
            #if '__part' in inputFileName :
            #    s = 1
            
            chain.Add(inputFileName)

            self.massScan = ROOT.TH2D("massScan", "", 3000, 0., 3000., 3000, 0., 3000.)
            chain.Project(self.massScan.GetName(), "susyMLSP:susyMprompt", "genWeight", "")
            
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

        self.out.fillBranch("baseW",         baseW)
            
        return True
 
