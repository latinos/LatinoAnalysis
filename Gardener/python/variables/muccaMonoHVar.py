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

class MuccaMonoHVarFiller(TreeCloner):

    def __init__(self):
        pass


    def createMuccaMonoH(self):
        self.getMuccaMonoH = ROOT.TMVA.Reader();
        
        # the order is important for TMVA!
        self.getMuccaMonoH.AddVariable("std_vector_lepton_pt[0]", (self.var1))
        self.getMuccaMonoH.AddVariable("std_vector_lepton_pt[1]", (self.var2))
        self.getMuccaMonoH.AddVariable("mll",                     (self.var3))
        self.getMuccaMonoH.AddVariable("ptll",                    (self.var4))
        self.getMuccaMonoH.AddVariable("mth",                     (self.var5))
        self.getMuccaMonoH.AddVariable("mtw1",                    (self.var6))
        self.getMuccaMonoH.AddVariable("mtw2",                    (self.var7))
        self.getMuccaMonoH.AddVariable("dphill",                  (self.var8))
        self.getMuccaMonoH.AddVariable("drll",                    (self.var9))
        self.getMuccaMonoH.AddVariable("dphilmet1",               (self.var10))
        self.getMuccaMonoH.AddVariable("dphilmet2",               (self.var11))
        self.getMuccaMonoH.AddVariable("dphilmet",                (self.var12))
        self.getMuccaMonoH.AddVariable("mpmet",                   (self.var13))
        self.getMuccaMonoH.AddVariable("metPfType1",              (self.var14))
        self.getMuccaMonoH.AddVariable("metTtrk",                 (self.var15))

        # I need to declare the spectator ... for some strange ROOT reasons ...
        #self.getMuccaMVAV.AddSpectator("std_vector_jet_pt[0]",   (self.var17))
       
        # mva trainined xml
        baseCMSSW = os.getenv('CMSSW_BASE')
        #self.getMuccaMVAV.BookMVA("BDT",baseCMSSW+"/src/LatinoAnalysis/Gardener/python/data/mucca/TMVAClassification_BDTG.weights.bkg" + self.kind + ".xml")
        self.getMuccaMonoH.BookMVA("BDT","/afs/cern.ch/user/n/ntrevisa/work/CMSSW_8_0_5/src/MUCCA/Optimization/Weights-TTbar/TMVAClassification_BDT4.weights.xml")


    def help(self):
        return '''Add mucca mva variables'''


    def addOptions(self,parser):
        description = self.help()
        group = optparse.OptionGroup(parser,self.label, description)
        group.add_option('-k', '--kind',   dest='kind', help='Which background training to be used', default='1')
        parser.add_option_group(group)
        return group
        pass


    def checkOptions(self,opts):
        if not (hasattr(opts,'kind')):
            raise RuntimeError('Missing parameter')
        self.kind   = opts.kind
        print " kind = ", self.kind


    def process(self,**kwargs):

        self.getMuccaMonoH = None

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
        #self.var17 = array.array('f',[0])
        
        tree  = kwargs['tree']
        input = kwargs['input']
        output = kwargs['output']

        self.connect(tree,input)
        newbranches = ['muccamva'+ self.kind]

        self.clone(output,newbranches)

        muccamva   = numpy.ones(1, dtype=numpy.float32)

        self.otree.Branch('muccamva'+ self.kind,  muccamva,  'muccamva' + self.kind + '/F')

        self.createMuccaMonoH()

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

            muccamva[0] = -9999.
            
            # just because it is easier to write later ...
            pt1 = itree.std_vector_lepton_pt[0]
            pt2 = itree.std_vector_lepton_pt[1]
            
            if pt1>0 and pt2>0 : 

              self.var1[0]   =  itree.std_vector_lepton_pt[0]
              self.var2[0]   =  itree.std_vector_lepton_pt[1]
              self.var3[0]   =  itree.mll
              self.var4[0]   =  itree.ptll
              self.var5[0]   =  itree.mth
              self.var6[0]   =  itree.mtw1
              self.var7[0]   =  itree.mtw2
              self.var8[0]   =  itree.dphill
              self.var9[0]   =  itree.drll
              self.var10[0]  =  itree.dphilmet1
              self.var11[0]  =  itree.dphilmet2
              self.var12[0]  =  itree.dphilmet
              self.var13[0]  =  itree.mpmet
              self.var14[0]  =  itree.metPfType1
              self.var15[0]  =  itree.metTtrk
              #self.var17[0]  =  itree.std_vector_jet_pt[0]
              
              muccamva[0] = self.getMuccaMonoH.EvaluateMVA("BDT")
              
            otree.Fill()
            
        self.disconnect()
        print '- Eventloop completed'


