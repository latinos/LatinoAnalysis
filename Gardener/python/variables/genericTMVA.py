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
#  __ \ \ \   /                                                     _)         |      |
#  |   | \   /       __ `__ \ \ \   /  _` |     \ \   /  _` |   __|  |   _` |  __ \   |   _ \
#  |   |    |        |   |   | \ \ /  (   |      \ \ /  (   |  |     |  (   |  |   |  |   __/
# ____/    _|       _|  _|  _|  \_/  \__,_|       \_/  \__,_| _|    _| \__,_| _.__/  _| \___|
#
#

class GenericTMVAFiller(TreeCloner):

    def __init__(self):
        pass


    def createMVA(self):
        self.reader = ROOT.TMVA.Reader();
        for i, inputVariable in enumerate(self.inputVariables):
          self.reader.AddVariable(inputVariable, (self.vars[i]))  


        # dymva trainined xml
        baseCMSSW = os.getenv('CMSSW_BASE')
        self.reader.BookMVA(self.method, baseCMSSW+"/src/"+self.weightsPath)


    def deltaPhi(self,l1,l2):
       dphi = fabs(l1.DeltaPhi(l2))
       #    dphi = fabs(ROOT.Math.VectorUtil.DeltaPhi(l1.p4(),l2.p4()))
       return dphi


    def help(self):
        return '''Add dy mva variables'''


    def addOptions(self,parser):
        description = self.help()
        group = optparse.OptionGroup(parser,self.label, description)
        group.add_option('-c', '--config',   dest='config', help='condif file', default='LatinoAnalysis/Gardener/python/data/TMVA_cfg.py')
        parser.add_option_group(group)
        return group


    def checkOptions(self,opts):
        cmssw_base = os.getenv('CMSSW_BASE')
        self.config = cmssw_base+'/src/'+opts.config
        if os.path.exists(self.config) :
          handle = open(self.config,'r')
          exec(handle)
          handle.close()

    def process(self,**kwargs):

        self.vars = []
        for i, inputVariable in enumerate(self.inputVariables):
          self.vars.append(array.array('f',[0]))

        
        tree  = kwargs['tree']
        input = kwargs['input']
        output = kwargs['output']

        self.connect(tree,input)
        newbranches = self.outputBranches

        self.clone(output,newbranches)

        outVars = []
        for b in self.outputBranches:  
          outVars.append(numpy.ones(1, dtype=numpy.float32))
          self.otree.Branch(b,  outVars[-1],  b+'/F')

        self.createMVA()

        nentries = self.itree.GetEntries()
        print 'Total number of entries: ',nentries 

        # avoid dots to go faster
        itree     = self.itree
        otree     = self.otree


        print '- Starting eventloop'
        step = 5000
        for i, event in enumerate(itree):
            itree.GetEntry(i)

            ## print event count
            if i > 0 and i%step == 0.:
                print i,'events processed.'

            for iv in range(len(self.vars)):
              self.vars[iv][0] = eval(self.inputFormulas[iv])
              #print self.inputFormulas[iv], self.vars[iv][0]
            for ic in range(len(self.outputBranches)):
              outVars[ic][0] = self.reader.EvaluateMulticlass(int(ic), self.method)
            otree.Fill()
            
        self.disconnect()
        print '- Eventloop completed'


