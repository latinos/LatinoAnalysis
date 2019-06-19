import ROOT
from ROOT import *
ROOT.PyConfig.IgnoreCommandLineOptions = True
import re
import os
import array
from array import array
from collections import OrderedDict
from keras import models
import numpy
from ROOT import *

from PhysicsTools.NanoAODTools.postprocessing.framework.datamodel import Collection 
from PhysicsTools.NanoAODTools.postprocessing.framework.eventloop import Module

#      mvaDic = { 'nameMva' : {
#                                'model'     : 'LatinoAnalysis/NanoGardener/python/data/....'   ,
#                                'inputVars' : { 'var1Name' : 'var1Expression' ,
#                                                'var2Name' : 'var2Expression' ,
#                                              } 
#                             } ,
#               } 

class KERASfiller(Module):
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
          self.mvaDic[iMva]['model'] = models.load_model(cmssw_base+'/src/'+self.mvaDic[iMva]['h5File'])

    def beginJob(self):
        pass
    def endJob(self):
        pass
    def beginFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        self.out = wrappedOutputTree
        self.itree = inputTree
        for iMva in self.mvaDic :
          self.out.branch(iMva, 'F')
    
    def endFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        pass
    
    def analyze(self, event):
        """process event, return True (go to next module) or False (fail, go to next event)"""
        Lep1_pt  = event.Lepton_pt[0]
        Lep1_eta = event.Lepton_eta[0]
        Lep1_phi = event.Lepton_phi[0]
        Lep2_pt  = event.Lepton_pt[1]
        Lep2_eta = event.Lepton_eta[1]
        Lep2_phi = event.Lepton_phi[1]
        jet1_pt  = event.jetpt1_cut
        if event.jetpt1_cut > 20 :
             jet1_eta  = event.CleanJet_eta[0]
             jet1_phi  = event.CleanJet_phi[0]
             jedId = event.CleanJet_jetIdx[0]
             jet1_btag = event.Jet_btagDeepB[jedId]
        else :
             jet1_eta  = -999.
             jet1_phi  = -999.
             jet1_btag = -999.
        jet2_pt  = event.jetpt2_cut
        if event.jetpt2_cut > 20 :
             jet2_eta  = event.CleanJet_eta[1]
             jet2_phi  = event.CleanJet_phi[1]
             jedId     = event.CleanJet_jetIdx[1]
             jet2_btag = event.Jet_btagDeepB[jedId]
        else :
             jet2_eta  = -999.
             jet2_phi  = -999.
             jet2_btag = -999.
        met_pt       = event.MET_pt
        met_phi      = event.MET_phi
        met_sum      = event.PuppiMET_sumEt
        tkmet_pt     = event.TkMET_pt
        tkmet_phi    = event.TkMET_phi
        tkmet_sum    = event.TkMET_sumEt
        puppimet_pt  = event.PuppiMET_pt
        puppimet_phi = event.PuppiMET_phi
        puppimet_sum = event.PuppiMET_sumEt
        for iMva in self.mvaDic :
          #print "====== ",iMva
          x = [ Lep1_pt, Lep1_eta, Lep1_phi, Lep2_pt, Lep2_eta, Lep2_phi, jet1_pt, jet1_eta, jet1_phi, jet1_btag, jet2_pt, jet2_eta, jet2_phi, jet2_btag, met_pt , met_phi, met_sum, tkmet_pt, tkmet_phi, tkmet_sum, puppimet_pt, puppimet_phi, puppimet_sum ]
          #print x
          x = numpy.asarray(x, dtype=float)
          x = x.reshape( (1, len(x)) )
          value = self.mvaDic[iMva]['model'].predict(x)
          #print 'Predict value ', value
          self.out.fillBranch(iMva, value)

        return True
