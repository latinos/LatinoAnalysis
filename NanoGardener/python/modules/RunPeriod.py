import ROOT
import os
import re
import math
ROOT.PyConfig.IgnoreCommandLineOptions = True

from copy import deepcopy
from PhysicsTools.NanoAODTools.postprocessing.framework.eventloop import Module
#from LatinoAnalysis.NanoGardener.data.RunPeriod_cfg import NewVar_MC_dict, NewVar_DATA_dict
#from LatinoAnalysis.NanoGardener.data.RunPeriod_cfg import Trigger

from PhysicsTools.NanoAODTools.postprocessing.framework.datamodel import Collection

#from LatinoAnalysis.NanoGardener.framework.BranchMapping import mappedOutputTree, mappedEvent

class RunPeriod(Module):
    '''
    Trigger Maker module MC,
    ''' 

    def __init__(self, cmssw = 'Full2016' , isData = False , cfg_path = 'LatinoAnalysis/NanoGardener/python/data/TrigMaker_cfg.py'):
        self.cmssw = cmssw
        self.isData = isData
        self.firstEvent = True
        self.cfg_path = cfg_path 

        cmssw_base = os.getenv('CMSSW_BASE')
        var = {}
        execfile(cmssw_base+'/src/'+cfg_path, var)
        self.Trigger = var['Trigger']
        self.NewVar  = { 'F': [ ], 'I': ['run_period'] }

        print('RunPeriod: CMSSW = ' + self.cmssw + ', isData = ' + str(self.isData)) 
        print('RunPeriod: loaded trigger configuration from ' + cfg_path)

 
    def beginJob(self): 
        pass

    def endJob(self):
        pass

    def beginFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        self.initReaders() # initReaders must be called in beginFile
        self.out = wrappedOutputTree
        #self.out = mappedOutputTree(wrappedOutputTree, mapname=self._branch_map)
        
        for typ in self.NewVar:
           for name in self.NewVar[typ]:
              if 'TriggerEmulator' in name: self.out.branch(name, typ, 6)
              else:                         self.out.branch(name, typ)

    def endFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        pass

    def initReaders(self): # this function gets the pointers to Value and ArrayReaders and sets them in the C++ worker class
        # Specific trigger dicts
        cmssw_base = os.getenv('CMSSW_BASE')
        self.TM_runInt  = {}
        for RunP in self.Trigger[self.cmssw]:
           self.TM_runInt[RunP]  = {'b': self.Trigger[self.cmssw][RunP]['begin'], 'e': self.Trigger[self.cmssw][RunP]['end']}

        # Set some run/event specific var
        self.total_lum = 0.
        for RunP in self.Trigger[self.cmssw]:
           self.total_lum += self.Trigger[self.cmssw][RunP]['lumi']
        
        self.RunFrac = [0.]
        for RunP in self.Trigger[self.cmssw]:
           self.RunFrac.append(self.RunFrac[-1] + self.Trigger[self.cmssw][RunP]['lumi']/self.total_lum)
 
        self.event = 'event.event'
        self.run = 'event.run'

    #_____Help functions
    def _run_period(self, run, event_seed=None):
        if self.isData:
           for RunP in self.TM_runInt:
              if run >= self.TM_runInt[RunP]['b'] and run <= self.TM_runInt[RunP]['e']: return RunP
        else: 
         toss_a_coin = get_rndm(event_seed)
         for iPeriod in range(1,len(self.RunFrac)) :
           if toss_a_coin >= self.RunFrac[iPeriod-1] and toss_a_coin < self.RunFrac[iPeriod]:
              return iPeriod
           if toss_a_coin == 1.0:
              return len(self.RunFrac)-1
        print "Run Period undefined"
        return -1 

    #_____Analyze
    def analyze(self, event):
        """process event, return True (go to next module) or False (fail, go to next event)"""

        run_p = self._run_period(eval(self.run))
        for name in self.NewVar['I']: 
          if 'run_period' in name : self.out.fillBranch(name, run_p)  

        return True

def get_rndm(a):
    if a is None: return ROOT.gRandom.Rndm()
    r = ROOT.TRandom3(int(a))
    toss_a_coin = r.Uniform()
    return toss_a_coin


