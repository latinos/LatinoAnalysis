import os
from random import random

from PhysicsTools.NanoAODTools.postprocessing.framework.datamodel import Collection 
from PhysicsTools.NanoAODTools.postprocessing.framework.eventloop import Module
from LatinoAnalysis.NanoGardener.framework.BranchMapping import mappedOutputTree, mappedEvent

#      Fractions = { 
#                      'sample_str' : MVA_fraction
#                  } 

class MVAsplitter(Module):
    '''
    Split samples in fraction for MVA training, and fraction for analysis.
     - Give each event a random variable R between 1 and 0.
     - If R > MVA_fraction => analysis event 
     - If R < MVA_fraction => MVA training event 
    '''
    def __init__(self, sample_name, cfg_path, MVA_name='MVA', keep_randomVar=False):
        self.sample_name = sample_name
      
        cmssw_base = os.getenv('CMSSW_BASE')
        var = {}
        execfile(cmssw_base+'/src/'+cfg_path, var)
        self.training_fraction = 0.
        for sample_str in var['Fractions']:
            if sample_str in sample_name:
                self.training_fraction = var['Fractions'][sample_str]
                break
    
        self.MVAn = MVA_name
        self.keep_r = keep_randomVar

    def beginJob(self):
        pass
    def endJob(self):
        pass
    def beginFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        self.out = wrappedOutputTree 
        self.out.branch(self.MVAn+'_isAnalysisEvent', 'O')
        self.out.branch(self.MVAn+'_isTrainingEvent', 'O')
        self.out.branch(self.MVAn+'_analysisWeight', 'F')
        self.out.branch(self.MVAn+'_trainingWeight', 'F')
        if not self.keep_r: self.out.branch(self.MVAn+'_randomVar', 'F')
    
    def endFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        pass
    
    def analyze(self, event):
        """process event, return True (go to next module) or False (fail, go to next event)"""
        if self.keep_r: R = eval('event.'+self.MVAn+'_randomVar')
        else: R = random()

        if R >= self.training_fraction: 
            is_t = False
            is_a = True
        else: 
            is_t = True
            is_a = False
        
        if is_a:
            a_w = 1./(1. - self.training_fraction)
        else: a_w = 0.
        if is_t:
            t_w = 1./(self.training_fraction)
        else: t_w = 0.

        self.out.fillBranch(self.MVAn+'_isAnalysisEvent', is_a)
        self.out.fillBranch(self.MVAn+'_isTrainingEvent', is_t)
        self.out.fillBranch(self.MVAn+'_analysisWeight', a_w)
        self.out.fillBranch(self.MVAn+'_trainingWeight', t_w)
        if not self.keep_r: self.out.fillBranch(self.MVAn+'_randomVar', R)
        return True

