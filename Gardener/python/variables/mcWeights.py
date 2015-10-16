#
#
#
#                         \ \        /     _)         |      |         
#     __ `__ \    __|      \ \  \   /  _ \  |   _` |  __ \   __|   __| 
#     |   |   |  (          \ \  \ /   __/  |  (   |  | | |  |   \__ \ 
#    _|  _|  _| \___|        \_/\_/  \___| _| \__, | _| |_| \__| ____/ 
#                                             |___/                    
#
#
#


from LatinoAnalysis.Gardener.gardening import TreeCloner
import numpy
import ROOT
import sys
import optparse
import re
import warnings
import os.path
from array import array;

class mcWeightsFiller(TreeCloner):
    def __init__(self):
       pass

    def help(self):
        return '''Add weight for mc weights'''

    def addOptions(self,parser):
        description = self.help()
        group = optparse.OptionGroup(parser,self.label, description)
        parser.add_option_group(group)

        return group


    def checkOptions(self,opts):
        pass
       
       
    def process(self,**kwargs):

        print " starting ..."

        tree  = kwargs['tree']
        input = kwargs['input']
        output = kwargs['output']

        # does that work so easily and give new variable itree and otree?
        self.connect(tree,input)
        newbranches = ['mcWeight']
        self.clone(output,newbranches)


        mcWeight        = numpy.ones(1, dtype=numpy.float32)

        self.otree.Branch('mcWeight'  , mcWeight  , 'mcWeight/F')

        nentries = self.itree.GetEntries()
        print 'Total number of entries: ',nentries 

        #what is self.itree? what is self.otree?
        itree     = self.itree
        otree     = self.otree


        print '- Read histogram with weights'
        
        myTreeWeight = self._getRootObj(self.ifile,'mcweight')
        
        nentriesWeight = myTreeWeight.GetEntries()

        mcWeight[0] = 0
        
        for i in xrange(nentriesWeight):
          myTreeWeight.GetEntry(i)
          
          if myTreeWeight.weightSM > 0 :
             mcWeight[0] += 1
          if myTreeWeight.weightSM < 0 :
             mcWeight[0] -= 1
             
        print ' weight = ',  mcWeight      
        

        print '- Starting eventloop'
        step = 5000

        for i in xrange(nentries):
        #for i in xrange(100):

            itree.GetEntry(i)

            if i > 0 and i%step == 0.:
                print i,'events processed.'

            otree.Fill()

        self.disconnect()
        print '- Eventloop completed'

