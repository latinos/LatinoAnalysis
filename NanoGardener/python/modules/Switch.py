import ROOT
ROOT.PyConfig.IgnoreCommandLineOptions = True
import re
import os

from PhysicsTools.NanoAODTools.postprocessing.framework.datamodel import Collection 
from PhysicsTools.NanoAODTools.postprocessing.framework.eventloop import Module

class Switch(Module):
    '''
    
    Create branch <desired_branchname> with boolean

    In cfg_path:
    SwitchDict[era] = {
        '<desired_branchname>': {               
            '<or_case>': [                      or_case (for example cut on run_period region) all or_case need to be complementary
                'event.<desired_cut>',          actual turn on statement
            ]
        },
    }
    '''
    def __init__(self, cmssw = 'Full2016v2', cfg_path = 'LatinoAnalysis/NanoGardener/python/data/switch/MH_triggerSwitch_cfg.py'):
        cmssw_base = os.getenv('CMSSW_BASE')
        var = {}
        execfile(cmssw_base+'/src/'+cfg_path, var)
        self.switch_dict = var['SwitchDict'][cmssw]
        

    def beginJob(self):
        pass

    def endJob(self):
        pass

    def beginFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        self.out = wrappedOutputTree
        self.th_dict = {}
        for name in self.switch_dict:
            bname = 'Switch_'+name
            self.out.branch(bname, 'O')
            self.th_dict[bname] = []
            self.th_dict[bname] = self.switch_dict[name] 

    def endFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        pass

    # Help functions
    def decide(self, th_list, event):
        current_case = None
        for case in th_list:
            this_case = False
            try:  this_case = eval(case)
            except: raise ValueError('Switch decide: Could not evaluate case: ' + case)
            if this_case:
                current_case = case
                break
        if current_case is None: ValueError('Switch decide: no case found, cases need to be complementary')
            
        for th in th_list[current_case]:
            #th_str = 'event.' + th
            happy = False
            try: happy = eval(th)
            except: raise ValueError('Switch decide: Could not evaluate threshold: ' + th)
            if not happy: return False
        return True

    def analyze(self, event):
        """process event, return True (go to next module) or False (fail, go to next event)"""
        for name in self.th_dict:
            dec = self.decide(self.th_dict[name], event)
            self.out.fillBranch(name, dec)
        return True

