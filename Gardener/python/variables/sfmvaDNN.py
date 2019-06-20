from LatinoAnalysis.Gardener.gardening import TreeCloner

import optparse
import os
import sys
import ROOT
import numpy
import array
import re
import warnings
import os.path
from math import *
import math
from keras import models 

#
#     ___ \       \   |     \   |
#     |    |    |\ \  |   |\ \  |                          _)         |      | 
#     |    |    | \ \ |   | \ \ |      \ \   /  _` |   __|  |   _` |  __ \   |   _ \ 
#     |    |    |  \  |   |  \  |       \ \ /  (   |  |     |  (   |  |   |  |   __/
#    _____/    _|   \_|  _|   \_|        \_/  \__,_| _|    _| \__,_| _.__/  _| \___|
#

class kerasModel(TreeCloner):

    def __init__(self):
        pass


    def createSFMVA(self):
        print("Setting CMSSW_BASE")
        # trainined xml
        baseCMSSW = os.getenv('CMSSW_BASE')
        print("Accessing model")
        self.model = models.load_model(baseCMSSW+"/src/LatinoAnalysis/Gardener/python/data/dymva/2017/model_2hiddenLayers_512unitsPerLayer_relu_Adam_relativeLearningRate1_relativeLearningRateDecay0p95.h5")
        print("SFDNN is loaded...")

    def help(self):
        return '''Add dymva variables'''


    def addOptions(self,parser):
        #description = self.help()
        #group = optparse.OptionGroup(parser,self.label, description)
        #group.add_option('-b', '--branch',   dest='branch', help='Name of something that is not used ... ', default='boh')
        #parser.add_option_group(group)
        #return group
        pass


    def checkOptions(self,opts):
        pass

    def process(self,**kwargs):
        print("Setting trees")

        tree  = kwargs['tree']
        input = kwargs['input']
        output = kwargs['output']

        print("Connecting tree and branches")

        self.connect(tree,input)
        newbranches = ['sfdnn']

        self.clone(output,newbranches)

        sfdnn = numpy.ones(1, dtype=numpy.float32)
        branch_list = numpy.array(1, dtype=float32)

        self.otree.Branch('sfdnn',  sfdnn,  'sfdnn/F')

        self.createSFMVA()

        nentries = self.itree.GetEntries()
        print 'Total number of entries: ',nentries 

        # avoid dots to go faster
        itree     = self.itree
        otree     = self.otree

        print '- Starting eventloop'
        step = 10000
        for i in xrange(nentries):
            itree.GetEntry(i)

            ## print event count
            if i > 0 and i%step == 0.:
                print i,'events processed.'

            # at least 2 leptons!
            sfdnn[0] = -9999.
           
            # just because it is easier to write later ...
            Lep1_pt  = itree.Lepton_pt[0]
            Lep1_eta = itree.Lepton_eta[0]
            Lep1_phi = itree.Lepton_phi[0]
            Lep2_pt  = itree.Lepton_pt[1]
            Lep2_eta = itree.Lepton_eta[1]
            Lep2_phi = itree.Lepton_phi[1]
            jet1_pt  = itree.jetpt1_cut
            if itree.jetpt1_cut > 20 :
              jet1_eta  = itree.CleanJet_eta[0]
              jet1_phi  = itree.CleanJet_phi[0]
              jet1_btag = itree.Jet_btagDeepB[itree.CleanJet_jetIdx[0]]
            else :
              jet1_eta  = -999.
              jet1_phi  = -999.
              jet1_btag = -999.
            jet2_pt  = itree.jetpt2_cut
            if itree.jetpt2_cut > 20 :
              jet2_eta  = itree.CleanJet_eta[1]
              jet2_phi  = itree.CleanJet_phi[1]
              jet2_btag = itree.Jet_btagDeepB[itree.CleanJet_jetIdx[1]]
            else :
              jet2_eta  = -999.
              jet2_phi  = -999.
              jet2_btag = -999.
            met_pt    = itree.PuppiMET_pt
            met_phi   = itree.PuppiMET_phi
            met_sum   = itree.PuppiMET_sumEt
            tkmet_pt  = itree.TkMET_pt
            tkmet_phi = itree.TkMET_phi
            tkmet_sum = itree.TkMET_sumEt

            if Lep1_pt>0 and Lep2_pt>0 : 
              
              branch_list = [
                'Lep1_pt' , 'Lep1_eta' , 'Lep1_phi' ,
                'Lep2_pt' , 'Lep2_eta' , 'Lep2_phi' ,
                'jet1_pt' , 'jet1_eta' , 'jet1_phi' , 'jet1_btag',
                'jet2_pt' , 'jet2_eta' , 'jet2_phi' , 'jet2_btag',
                'met_pt'  , 'met_phi'  , 'met_sum'  ,
                'tkmet_pt', 'tkmet_phi', 'tkmet_sum'
              ]

              sfdnn = float( self.model.predict(branch_list) )

            otree.Fill()

        self.disconnect()
        print '- Event loop completed'
