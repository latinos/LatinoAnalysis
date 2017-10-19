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
#    \  |                                                                               _)         |      |       
#   |\/ |  |   |   __|   __|   _` |      __ `__ \ \ \   /  _` |     \ \   /  _` |   __|  |   _` |  __ \   |   _ \ 
#   |   |  |   |  (     (     (   |      |   |   | \ \ /  (   |      \ \ /  (   |  |     |  (   |  |   |  |   __/ 
#  _|  _| \__,_| \___| \___| \__,_|     _|  _|  _|  \_/  \__,_|       \_/  \__,_| _|    _| \__,_| _.__/  _| \___| 
#                                                                                                                
#

class MuccaMonoHFullVarFiller(TreeCloner):

    def __init__(self):
        pass


    def createMuccaMonoHFull(self):
        self.getMuccaMonoHFull = ROOT.TMVA.Reader();
        
        # the order is important for TMVA!
        self.getMuccaMonoHFull.AddVariable("mth",                     (self.var1))
        self.getMuccaMonoHFull.AddVariable("mtw2",                    (self.var2))
        self.getMuccaMonoHFull.AddVariable("metTtrk",                 (self.var3))
        self.getMuccaMonoHFull.AddVariable("drll",                    (self.var4))
        self.getMuccaMonoHFull.AddVariable("ptll",                    (self.var5))
        self.getMuccaMonoHFull.AddVariable("mpmet",                   (self.var6))
        self.getMuccaMonoHFull.AddVariable("mtw1",                    (self.var7))
        self.getMuccaMonoHFull.AddVariable("mll",                     (self.var8))
        self.getMuccaMonoHFull.AddVariable("dphilmet",                (self.var9))
        self.getMuccaMonoHFull.AddVariable("dphilmet1",               (self.var10))
        self.getMuccaMonoHFull.AddVariable("dphilmet2",               (self.var11))
        self.getMuccaMonoHFull.AddVariable("std_vector_lepton_pt[0]", (self.var12))
        self.getMuccaMonoHFull.AddVariable("metPfType1",              (self.var13))
        self.getMuccaMonoHFull.AddVariable("dphill",                  (self.var14))
        self.getMuccaMonoHFull.AddVariable("std_vector_lepton_pt[1]", (self.var15))

        # I need to declare the spectator ... for some strange ROOT reasons ...
        #self.getMuccaMVAV.AddSpectator("std_vector_jet_pt[0]",   (self.var17))
       
        # mva trainined xml
        baseCMSSW = os.getenv('CMSSW_BASE')
        
        # /afs/cern.ch/user/n/ntrevisa/www/figuresLxplus/15Oct2017/monoH/TMVA/plots_TMVA-2HDM_TTbar_0var_em_600_300/Weights-2HDM_TTbar_0var_em_600_300/TMVAClassification_BDT7.weights.xml
        self.getMuccaMonoHFull.BookMVA("BDT","/afs/cern.ch/user/n/ntrevisa/www/figuresLxplus/15Oct2017/monoH/TMVA/plots_TMVA-" + self.model + "_TTbar_0var_em/Weights-" + self.model + "_TTbar_0var_" + self.channel + "/TMVAClassification_" + self.training + ".weights.xml")

    def help(self):
        return '''Add mucca mva variables'''


    def addOptions(self,parser):
        description = self.help()
        group = optparse.OptionGroup(parser,self.label, description)
        group.add_option('-k', '--kind',     dest='kind',     help='Which background training to be used', default='1')
        group.add_option('-s', '--signal',   dest='signal',   help='Variable name',                        default='2HDMadaptTTbar_em')
        group.add_option('-a', '--training', dest='training', help='Training',                             default='BDT7')
        group.add_option('-c', '--channel',  dest='channel',  help='Channel',                              default='em')
        group.add_option('-m', '--model',    dest='model',    help='Signal Model',                         default='2HDM')
        parser.add_option_group(group)
        return group
        pass


    def checkOptions(self,opts):
        if not (hasattr(opts,'kind')):
            raise RuntimeError('Missing parameter')
        self.kind        = opts.kind
        print " kind     = ", self.kind
        self.signal      = opts.signal
        print " signal   = ", self.signal
        self.training    = opts.training
        print " training = ", self.training
        self.channel     = opts.channel
        print " channel  = ", self.channel
        self.model       = opts.model
        print " model  = ", self.model


    def process(self,**kwargs):

        self.getMuccaMonoHFull = None

        self.var1  = array.array('f',[0])
        self.var2  = array.array('f',[0])
        self.var3  = array.array('f',[0])
        self.var4  = array.array('f',[0])
        self.var5  = array.array('f',[0])
        self.var6  = array.array('f',[0])
        self.var7  = array.array('f',[0])
        self.var8  = array.array('f',[0])
        self.var9  = array.array('f',[0])
        self.var10 = array.array('f',[0])
        self.var11 = array.array('f',[0])
        self.var12 = array.array('f',[0])
        self.var13 = array.array('f',[0])
        self.var14 = array.array('f',[0])
        self.var15 = array.array('f',[0])
        
        tree  = kwargs['tree']
        input = kwargs['input']
        output = kwargs['output']

        self.connect(tree,input)
        newbranches = ['muccamva'+ self.signal]

        self.clone(output,newbranches)

        muccamva = numpy.ones(1, dtype=numpy.float32)

        self.otree.Branch('muccamva'+ self.signal,  muccamva,  'muccamva' + self.signal + '/F')

        self.createMuccaMonoHFull()

        nentries = self.itree.GetEntries()
        print 'Total number of entries: ',nentries 

        # avoid dots to go faster
        itree = self.itree
        otree = self.otree


        print '- Starting eventloop'
        step = 5000
        for i in xrange(nentries):
            itree.GetEntry(i)

            ## print event count
            if i > 0 and i%step == 0.:
                print i,'events processed.'

            muccamva[0] = -9999.
            
            # just because it is easier to write later ...
            pt1 = itree.std_vector_lepton_pt[0]
            pt2 = itree.std_vector_lepton_pt[1]
            
            if pt1>0 and pt2>0 : 

              self.var1[0] = itree.mth
              self.var2[0] = itree.mtw2
              self.var3[0] = itree.metTtrk
              self.var4[0] = itree.drll
              self.var5[0] = itree.ptll
              self.var6[0] = itree.mpmet
              self.var7[0] = itree.mtw1
              self.var8[0] = itree.mll
              self.var9[0] = itree.dphilmet
              self.var10[0] = itree.dphilmet1
              self.var11[0] = itree.dphilmet2
              self.var12[0] = itree.std_vector_lepton_pt[0]
              self.var13[0] = itree.metPfType1
              self.var14[0] = itree.dphill
              self.var15[0] = itree.std_vector_lepton_pt[1]

              muccamva[0] = self.getMuccaMonoHFull.EvaluateMVA("BDT")
              
            otree.Fill()
            
        self.disconnect()
        print '- Eventloop completed'


