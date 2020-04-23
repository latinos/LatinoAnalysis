import ROOT
ROOT.PyConfig.IgnoreCommandLineOptions = True
import re
import os

from PhysicsTools.NanoAODTools.postprocessing.framework.datamodel import Collection 
from PhysicsTools.NanoAODTools.postprocessing.framework.eventloop import Module

class runDependentPuW(Module):
    def __init__(self , cmssw, PUWeight_cfg = 'LatinoAnalysis/NanoGardener/python/data/PUWeight_cfg.py' ):
        self.cmssw = cmssw
        cmssw_base = os.getenv('CMSSW_BASE')
        var = {}
        execfile(cmssw_base+'/src/'+PUWeight_cfg, var)
        self.PUWeightCfg = var['PUCfg'][self.cmssw]

        self.targeth = {}
        self.targeth['beginRP']    = []
        self.targeth['endRP']      = []
        self.targeth['hist']       = []
        self.targeth['name']       = []
        if self.PUWeightCfg['doSysVar']:
            self.targeth['hist_plus']  = [] 
            self.targeth['hist_minus'] = [] 
        for rpr in self.PUWeightCfg['targetfiles'] : 
          self.targeth['beginRP'] .append(int(rpr.split('-')[0]))
          self.targeth['endRP']   .append(int(rpr.split('-')[1])) 
          self.targeth['hist']    .append(self.loadHisto(cmssw_base+'/src/'+self.PUWeightCfg['targetfiles'][rpr],self.PUWeightCfg['targethist']))
          self.targeth['name']    .append(self.PUWeightCfg['targetfiles'][rpr].split('/')[-1].split('.')[0].replace('_PU',''))  
          if self.PUWeightCfg['doSysVar']:
            self.targeth['hist_plus']  .append(self.loadHisto(cmssw_base+'/src/'+self.PUWeightCfg['targetfiles'][rpr],self.PUWeightCfg['targethist']+"_plus"))
            self.targeth['hist_minus'] .append(self.loadHisto(cmssw_base+'/src/'+self.PUWeightCfg['targetfiles'][rpr],self.PUWeightCfg['targethist']+"_minus"))

        self.fixLargeWeights = True
        if self.PUWeightCfg['srcfile'] != "auto" :
            self.autoPU=False
            self.myh = self.loadHisto(self.PUWeightCfg['srcfile'],self.PUWeightCfg['srchist'])
        else :
            self.fixLargeWeights = False #AR: it seems to crash with it, to be deugged
            self.autoPU=True
            ROOT.gROOT.cd()
            self.myh=self.targeth['hist'][0].Clone("autoPU")
            self.myh.Reset()
        self.name = self.PUWeightCfg['name']
        self.norm = self.PUWeightCfg['norm']
        self.verbose = self.PUWeightCfg['verbose']
        self.nvtxVar = self.PUWeightCfg['nvtx_var']
        self.doSysVar = self.PUWeightCfg['doSysVar']
        self.doSplitPU = True

        #Try to load module via python dictionaries
        try:
            ROOT.gSystem.Load("libPhysicsToolsNanoAODTools")
            dummy = ROOT.WeightCalculatorFromHistogram
        #Load it via ROOT ACLIC. NB: this creates the object file in the CMSSW directory,
        #causing problems if many jobs are working from the same CMSSW directory
        except Exception as e:
            print "Could not load module via python, trying via ROOT", e
            if "/WeightCalculatorFromHistogram_cc.so" not in ROOT.gSystem.GetLibraries():
                print "Load C++ Worker"
                ROOT.gROOT.ProcessLine(".L %s/src/PhysicsTools/NanoAODTools/src/WeightCalculatorFromHistogram.cc++" % os.environ['CMSSW_BASE'])
            dummy = ROOT.WeightCalculatorFromHistogram

    def loadHisto(self,filename,hname):
        tf = ROOT.TFile.Open(filename)
        hist = tf.Get(hname)
        hist.SetDirectory(None)
        tf.Close()
        return hist

    def beginJob(self):
        pass
    def endJob(self):
        pass
    def beginFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        self.out = wrappedOutputTree
        if self.autoPU :
           self.myh.Reset()
           print "Computing PU profile for this file"
           ROOT.gROOT.cd()
           inputFile.Get("Events").Project("autoPU",self.nvtxVar)#doitfrom inputFile
           if outputFile : 
             outputFile.cd()
             self.myh.Write()    
        # ---- Workers
        self._worker = []
        for i in range(len(self.targeth['hist'])):
          self._worker .append ( ROOT.WeightCalculatorFromHistogram(self.myh,self.targeth['hist'][i],self.norm,self.fixLargeWeights,self.verbose)  )
          if self.doSplitPU : self.out.branch(self.name+'_'+self.targeth['name'][i],"F")
        self.out.branch(self.name, "F")
        if self.doSysVar:
          self._worker_plus  = []
          for i in range(len(self.targeth['hist_plus'])):
            self._worker_plus .append ( ROOT.WeightCalculatorFromHistogram(self.myh,self.targeth['hist_plus'][i],self.norm,self.fixLargeWeights,self.verbose) )
            if self.doSplitPU : self.out.branch(self.name+'_'+self.targeth['name'][i]+"Up","F")
          self.out.branch(self.name+"Up","F")
          self._worker_minus = []
          for i in range(len(self.targeth['hist_minus'])):
            self._worker_minus .append ( ROOT.WeightCalculatorFromHistogram(self.myh,self.targeth['hist_minus'][i],self.norm,self.fixLargeWeights,self.verbose) )
            if self.doSplitPU : self.out.branch(self.name+'_'+self.targeth['name'][i]+"Down","F")
          self.out.branch(self.name+"Down","F")
        
        pass 
    def endFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        pass
    def analyze(self, event):
        """process event, return True (go to next module) or False (fail, go to next event)"""
        #select right index based on runperiod
        run_period = event.run_period
        run_idx = 0
        for idx in range(len(self.targeth['beginRP'])):
            if run_period >= self.targeth['beginRP'][idx] and run_period <= self.targeth['endRP'][idx]:
                run_idx = idx
        # Compute weight now 
        if hasattr(event,self.nvtxVar):
            nvtx = int(getattr(event,self.nvtxVar))
            weight = self._worker[run_idx].getWeight(nvtx) if nvtx < self.myh.GetNbinsX() else 1
            if self.doSysVar:
                weight_plus = self._worker_plus[run_idx].getWeight(nvtx) if nvtx < self.myh.GetNbinsX() else 1
                weight_minus = self._worker_minus[run_idx].getWeight(nvtx) if nvtx < self.myh.GetNbinsX() else 1
        else: weight = 1
        self.out.fillBranch(self.name,weight)
        if self.doSysVar:
            self.out.fillBranch(self.name+"Up",weight_plus)
            self.out.fillBranch(self.name+"Down",weight_minus)
        # Store PU for subperiod as a whole
        if self.doSplitPU :
          for idx in range(len(self.targeth['name'])):
            weight = self._worker[idx].getWeight(nvtx) if nvtx < self.myh.GetNbinsX() else 1
            self.out.fillBranch(self.name+'_'+self.targeth['name'][idx],weight)
            if self.doSysVar:
              weight_plus = self._worker_plus[idx].getWeight(nvtx) if nvtx < self.myh.GetNbinsX() else 1
              weight_minus = self._worker_minus[idx].getWeight(nvtx) if nvtx < self.myh.GetNbinsX() else 1
              self.out.fillBranch(self.name+'_'+self.targeth['name'][idx]+"Up",weight_plus)
              self.out.fillBranch(self.name+'_'+self.targeth['name'][idx]+"Down",weight_minus) 
        return True

