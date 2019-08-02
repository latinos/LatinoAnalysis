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
    SwitchDict = {
        '<desired_branchname>': {
            'threshold': [
                'event.<desired_cut>',
            ]
        },
    }
    '''
    def __init__(self, cfg_path = 'LatinoAnalysis/NanoGardener/python/data/Switch_cfg.py'):
        cmssw_base = os.getenv('CMSSW_BASE')
        var = {}
        execfile(cmssw_base+'/src/'+cfg_path, var)
        self.switch_dict = var['SwitchDict']
        

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
            self.th_dict[bname] = self.switch_dict[name]['threshold'] 

    def endFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        pass

    # Help functions
    def decide(self, th_list, event):
        for th in th_list:
            #th_str = 'event.' + th
            happy = False
            try: happy = eval(th)
            except: raise ValueError('Switch decide: Could not evaluate ' + th)
            if not happy: return False
        return True

    def analyze(self, event):
        """process event, return True (go to next module) or False (fail, go to next event)"""
        for name in self.th_dict:
            dec = self.decide(self.th_dict[name], event)
            self.out.fillBranch(name, dec)
        return True

