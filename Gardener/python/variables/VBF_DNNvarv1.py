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

#
#     ___ \       \   |     \   |
#     |    |    |\ \  |   |\ \  |                          _)         |      | 
#     |    |    | \ \ |   | \ \ |      \ \   /  _` |   __|  |   _` |  __ \   |   _ \ 
#     |    |    |  \  |   |  \  |       \ \ /  (   |  |     |  (   |  |   |  |   __/
#    _____/    _|   \_|  _|   \_|        \_/  \__,_| _|    _| \__,_| _.__/  _| \___|
#

class DNNvarFillerv1(TreeCloner):

    def __init__(self):
        pass


    def createVBFDNN(self):
        print("Creating VBFDNN")
        ROOT.TMVA.PyMethodBase.PyInitialize()
        self.getVBFDNN  = ROOT.TMVA.Reader();
       
        self.getVBFDNN.AddVariable("mjj",         (self.VBFDNNvar1))
        self.getVBFDNN.AddVariable("mll",         (self.VBFDNNvar2))
        self.getVBFDNN.AddVariable("drll",        (self.VBFDNNvar3))
        self.getVBFDNN.AddVariable("dphill",      (self.VBFDNNvar4))
        self.getVBFDNN.AddVariable("ptTOT_cut",   (self.VBFDNNvar5))
        self.getVBFDNN.AddVariable("mTOT_cut",    (self.VBFDNNvar6))
        self.getVBFDNN.AddVariable("OLV1_cut",    (self.VBFDNNvar7))
        self.getVBFDNN.AddVariable("OLV2_cut",    (self.VBFDNNvar8))

        print("Setting CMSSW_BASE")
        # trainined xml
        baseCMSSW = os.getenv('CMSSW_BASE')
        print("Accessing weights")
        self.getVBFDNN.BookMVA("PyKeras",baseCMSSW+"/src/LatinoAnalysis/Gardener/python/data/vbfdnn/TMVAClassification_PyKeras.weights.xml")

        print("VBFDNN is created...")

    def help(self):
        return '''Add vbf dnn variables'''


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
        print("Beginning")
        self.getVBFDNN = None

        print("Adding arrays")
        self.VBFDNNvar1 = array.array('f',[0])
        self.VBFDNNvar2 = array.array('f',[0])
        self.VBFDNNvar3 = array.array('f',[0])
        self.VBFDNNvar4 = array.array('f',[0])
        self.VBFDNNvar5 = array.array('f',[0])
        self.VBFDNNvar6 = array.array('f',[0])
        self.VBFDNNvar7 = array.array('f',[0])
        self.VBFDNNvar8 = array.array('f',[0])

        print("Setting trees")

        tree  = kwargs['tree']
        input = kwargs['input']
        output = kwargs['output']

        print("Connecting tree and branches")

        self.connect(tree,input)
        newbranches = ['vbfddn']

        self.clone(output,newbranches)

        vbfddn      = numpy.ones(1, dtype=numpy.float32)

        self.otree.Branch('vbfddn',  vbfddn,  'vbfddn/F')

        self.createVBFDNN()

        nentries = self.itree.GetEntries()
        print 'Total number of entries: ',nentries 

        # avoid dots to go faster
        itree     = self.itree
        otree     = self.otree

        print '- Starting eventloop'
        step = 5000
        for i in xrange(nentries):
            itree.GetEntry(i)

            ## print event count
            if i > 0 and i%step == 0.:
                print i,'events processed.'

            # at least 2 leptons!
            vbfddn[0] = -9999.
           
            # just because it is easier to write later ...
            pt1 = itree.std_vector_lepton_pt[0]
            pt2 = itree.std_vector_lepton_pt[1]
            jetpt1 = itree.std_vector_jet_pt[0]
            jetpt2 = itree.std_vector_jet_pt[1]
            mjj    = itree.mjj
            detajj = itree.detajj
 
            if pt1>0 and pt2>0 : 
              
              if jetpt1>= 30.0 and jetpt2>= 30.0 :

                    self.VBFDNNvar1[0]  = itree.mjj
                    self.VBFDNNvar2[0]  = itree.mll
                    self.VBFDNNvar3[0]  = itree.drll
                    self.VBFDNNvar4[0]  = itree.dphill
                    self.VBFDNNvar5[0]  = itree.ptTOT_cut
                    self.VBFDNNvar6[0]  = itree.mTOT_cut
                    self.VBFDNNvar7[0]  = itree.OLV1_cut
                    self.VBFDNNvar8[0]  = itree.OLV2_cut

                    vbfddn[0] = self.getVBFDNN.EvaluateMVA("PyKeras")
              
            otree.Fill()

        self.disconnect()
        print '- Eventloop completed'
