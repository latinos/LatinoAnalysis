import ROOT
ROOT.PyConfig.IgnoreCommandLineOptions = True
import re
import os

from PhysicsTools.NanoAODTools.postprocessing.framework.datamodel import Collection 
from PhysicsTools.NanoAODTools.postprocessing.framework.eventloop import Module

#      mvaDic = { 'nameMva' : {
#                                'type'      : 'BDT' ,  
#                                'xmlFile'   : 'LatinoAnalysis/NanoGardener/python/data/....'   ,
#                                'inputVars' : { 'var1Name' : 'var1Expression' ,
#                                                'var2Name' : 'var2Expression' ,
#                                              } 
#                             } ,
#               } 

class TMVAfiller(Module):
    def __init__(self,mvaCfgFile):

       cmssw_base = os.getenv('CMSSW_BASE')
       mvaFile = cmssw_base+'/src/LatinoAnalysis/NanoGardener/python/'+mvaCfgFile
       if os.path.exists(mvaFile):
         handle = open(mvaFile,'r')
         exec(handle)
         self.mvaDic = mvaDic
         handle.close()
        print self.mvaDic

        self.mvaDic = mvaDic
        cmssw_base = os.getenv('CMSSW_BASE') 
        for iMva in self.mvaDic :
          self.mvaDic[iMva]['reader'] = ROOT.TMVA.Reader()
          self.mvaDic[iMva]['inputs'] = []
          jVar=0
          for iVar in self.mvaDic[iMva]['inputVars'] :
            self.mvaDic[iMva]['inputs'].push_back(array.array('f',[0]))
            self.mvaDic[iMva]['reader'].AddVariable(iVar,self.mvaDic[iMva]['inputs'][jVar])
            jVar+=1
          self.mvaDic[iMva]['reader'].BookMVA(self.mvaDic[iMva]['type'],cmssw_base+'/src/'+self.mvaDic[iMva]['xmlFile'])      

    def beginJob(self):
        pass
    def endJob(self):
        pass
    def beginFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        self.out = wrappedOutputTree
        self.itree = inputTree
        for iMva in self.mvaDic :
          self.out.branch(iMva,  'F')
        #for key in self.formulas.keys():
        #  self.formulas[key] = eval('lambda event:'+self.formulas[key])
        #  self.out.branch(key,  'F');
    
    def endFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        pass
    
    def analyze(self, event):
        """process event, return True (go to next module) or False (fail, go to next event)"""
        for iMva in self.mvaDic :
          jVar=0
          for iVar in self.mvaDic[iMva]['inputVars'] :  
            self.mvaDic[iMva]['inputs'][jVar] = eval(self.mvaDic[iMva]['inputVars'][iVar])
            jVar+=1
          self.out.fillBranch(iMva, self.mvaDic[iMva]['reader'].EvaluateMVA(self.mvaDic[iMva]['type'])) 

        return True

