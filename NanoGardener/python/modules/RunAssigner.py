import ROOT
import os
ROOT.PyConfig.IgnoreCommandLineOptions = True

from PhysicsTools.NanoAODTools.postprocessing.framework.eventloop import Module
from LatinoAnalysis.NanoGardener.data.TrigMaker_cfg import Trigger

class RunAssigner(Module):
    '''
    Assign run period to MC events based on run luminosity fractions.
    ''' 

    def __init__(self, cmssw = 'Full2016', seed=65539):
        self.TriggerCfg = Trigger[cmssw]

        self.random = ROOT.TRandom3(seed)

    def beginJob(self): 
        pass

    def endJob(self):
        pass

    def beginFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        self.initReaders(inputTree) # initReaders must be called in beginFile
        self.out = wrappedOutputTree

        self.out.branch('run_period', 'I')

    def endFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        pass

    def initReaders(self,tree): # this function gets the pointers to Value and ArrayReaders and sets them in the C++ worker class

        self.RunFrac = []
        lumi = 0.
        for RunCfg in self.TriggerCfg.itervalues():
            lumi += RunCfg['lumi']
            self.RunFrac.append(lumi)

        for i in range(len(self.RunFrac)):
            self.RunFrac[i] /= lumi
       
    def analyze(self, event):
        """process event, return True (go to next module) or False (fail, go to next event)"""

        x = self.random.Rndm()
        run_period = next(i + 1 for i in range(len(self.RunFrac)) if self.RunFrac[i] >= x)

        self.out.fillBranch('run_period', run_period)

        return True
