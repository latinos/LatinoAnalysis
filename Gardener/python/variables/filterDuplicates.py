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
#    ____| _)  |  |                    __ \                 | _)               |               
#    |      |  |  __|   _ \   __|      |   |  |   |  __ \   |  |   __|   _` |  __|   _ \   __| 
#    __|    |  |  |     __/  |         |   |  |   |  |   |  |  |  (     (   |  |     __/ \__ \ 
#   _|     _| _| \__| \___| _|        ____/  \__,_|  .__/  _| _| \___| \__,_| \__| \___| ____/ 
#                                                   _|                                                                                                                                                       
#

class FilterDuplicates(TreeCloner):

    def __init__(self):
        pass


    def help(self):
        return '''Add mucca mva variables'''


    def addOptions(self,parser):
        description = self.help()
        group = optparse.OptionGroup(parser,self.label, description)
        parser.add_option_group(group)
        return group
        pass


    def checkOptions(self,opts):
        pass

    def process(self,**kwargs):

        tree  = kwargs['tree']
        input = kwargs['input']
        output = kwargs['output']

        self.connect(tree,input)
        newbranches = ['isDuplicate']

        self.clone(output,newbranches)
        isDuplicate   = numpy.ones(1, dtype=numpy.float32)
        self.otree.Branch('isDuplicate',  isDuplicate,  'isDuplicate/F')

        nentries = self.itree.GetEntries()
        print 'Total number of entries: ',nentries 
        savedentries = 0

        # avoid dots to go faster
        itree     = self.itree
        otree     = self.otree


        print '- Starting eventloop'
        step = 5000
        
        # duplicate check
        DoubleChecker = {}
         
        for i in xrange(nentries):
            itree.GetEntry(i)

            ## print event count
            if i > 0 and i%step == 0.:
                print i,'events processed.'

            isDuplicate[0] = -9999.
            
            run_lumi = ( itree.run, itree.lumi )
            if  run_lumi in DoubleChecker.keys() :
              if itree.event in DoubleChecker[run_lumi]:
                print " already there! "
                isDuplicate[0] = 0
              else :
                isDuplicate[0] = 1
                DoubleChecker[run_lumi].append(itree.event)
            else :
              isDuplicate[0] = 1
              DoubleChecker[run_lumi] = [itree.event]
            
            
            otree.Fill()
            savedentries+=1
            
        #print " DoubleChecker = ", DoubleChecker  
          
        self.disconnect()
        print '- Eventloop completed'
        print '   Saved: ', savedentries, ' events'


