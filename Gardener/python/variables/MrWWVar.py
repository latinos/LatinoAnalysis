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
#      \  |   _ \      \ \        / \ \        / 
#     |\/ |  |   |      \ \  \   /   \ \  \   /  
#     |   |  __ <        \ \  \ /     \ \  \ /   
#    _|  _| _| \_\        \_/\_/       \_/\_/    
#                                                                                                                                                             
#

class MrWWVarFiller(TreeCloner):

    def __init__(self):
        pass


    def createMrWW(self):
        self.getMrWW = ROOT.TMVA.Reader();
        
        # the order is important for TMVA!
        self.getMrWW.AddVariable("std_vector_lepton_pt[0]",    (self.var1))
        self.getMrWW.AddVariable("std_vector_lepton_pt[1]",    (self.var2))
        self.getMrWW.AddVariable("mll",               (self.var3))
        self.getMrWW.AddVariable("dphill*mll",            (self.var4))
        self.getMrWW.AddVariable("mth",               (self.var5))
        self.getMrWW.AddVariable("mtw1",              (self.var6))
        self.getMrWW.AddVariable("mtw2",              (self.var7))
        self.getMrWW.AddVariable("dphilmet1*mll",         (self.var8))
        self.getMrWW.AddVariable("dphilmet2*mll",         (self.var9))
        self.getMrWW.AddVariable("drll",              (self.var10))
        self.getMrWW.AddVariable("mcoll",             (self.var11))

       
        # mva trainined xml
        baseCMSSW = os.getenv('CMSSW_BASE')
        self.getMrWW.BookMVA("BDT",baseCMSSW+"/src/LatinoAnalysis/Gardener/python/data/mrww/TMVARegression_BDT.weights.xml")


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

        self.getMrWW = None

        self.var1 = array.array('f',[0])
        self.var2 = array.array('f',[0])
        self.var3 = array.array('f',[0])
        self.var4 = array.array('f',[0])
        self.var5 = array.array('f',[0])
        self.var6 = array.array('f',[0])
        self.var7 = array.array('f',[0])
        self.var8 = array.array('f',[0])
        self.var9 = array.array('f',[0])
        self.var10 = array.array('f',[0])
        self.var11 = array.array('f',[0])
        self.var12 = array.array('f',[0])
        self.var13 = array.array('f',[0])
        self.var14 = array.array('f',[0])
        
        tree  = kwargs['tree']
        input = kwargs['input']
        output = kwargs['output']

        self.connect(tree,input)
        newbranches = ['mrww'+ self.kind]

        self.clone(output,newbranches)

        mrww   = numpy.ones(1, dtype=numpy.float32)

        self.otree.Branch('mrww'+ self.kind,  mrww,  'mrww' + self.kind + '/F')

        self.createMrWW()

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

            mrww[0] = -9999.
            
            # just because it is easier to write later ...
            pt1 = itree.std_vector_lepton_pt[0]
            pt2 = itree.std_vector_lepton_pt[1]
            
            if pt1>0 and pt2>0 : 
            
              self.var1[0]   =  itree.std_vector_lepton_pt[0]
              self.var2[0]   =  itree.std_vector_lepton_pt[1]
              self.var3[0]   =  itree.mll
              self.var4[0]   =  itree.dphill * itree.mll
              self.var5[0]   =  itree.mth
              self.var6[0]  =  itree.mtw1
              self.var7[0]  =  itree.mtw2
              self.var8[0]  =  itree.dphilmet1 * itree.mll
              self.var9[0]  =  itree.dphilmet2 * itree.mll
              self.var10[0]  =  itree.drll 
              self.var10[0]  =  itree.mcoll
              
              mrww[0] = self.getMrWW.EvaluateRegression(0,"BDT")
              
            otree.Fill()
            
        self.disconnect()
        print '- Eventloop completed'

 
