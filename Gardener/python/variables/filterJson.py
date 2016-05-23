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
import json


#
#     ____| _)  |  |                        |   ___|    _ \    \  | 
#     |      |  |  __|   _ \   __|          | \___ \   |   |    \ | 
#     __|    |  |  |     __/  |         \   |       |  |   |  |\  | 
#    _|     _| _| \__| \___| _|        \___/  _____/  \___/  _| \_| 
#                                                                                                                                                                                 
#

class FilterJSON(TreeCloner):

    def __init__(self):
        pass


    def help(self):
        return '''Tag events using Json file: adding a variable 0/1 about it'''


    def addOptions(self,parser):
        description = self.help()
        group = optparse.OptionGroup(parser,self.label, description)
        group.add_option( '--json',       dest='jsonFile' ,       help='Json file with list of good run/lumi', default=None)
        parser.add_option_group(group)
        return group
        pass


    def checkOptions(self,opts):

        if opts.jsonFile != None :
          self.run_lumi_json = json.loads( (open(opts.jsonFile)).read() )
        else :
          self.run_lumi_json = {}
          
        print "---------------------------------------"
        print " self.run_lumi_json =", self.run_lumi_json
        
          
    def process(self,**kwargs):

        tree  = kwargs['tree']
        input = kwargs['input']
        output = kwargs['output']

        self.connect(tree,input)
        newbranches = ['isJsonOk']

        self.clone(output,newbranches)
        isJsonOk   = numpy.ones(1, dtype=numpy.float32)
        self.otree.Branch('isJsonOk',  isJsonOk,  'isJsonOk/F')

        nentries = self.itree.GetEntries()
        print 'Total number of entries: ',nentries 
        savedentries = 0

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

            isJsonOk[0] = 0
            
            #print " self.run_lumi_json = ", self.run_lumi_json
            #print "run, lumi = ", itree.run, " , ", itree.lumi
            if str(itree.run) in self.run_lumi_json.keys() :
              lumi_blocks = self.run_lumi_json[str(itree.run)]     # example:   "273158": [[1, 1279]]
              #print " lumi_blocks = ", lumi_blocks
              for ilumi_block in lumi_blocks :
                if itree.lumi >= ilumi_block[0] :
                  if len(ilumi_block) > 1 :
                    if itree.lumi <= ilumi_block[1]:
                      isJsonOk[0] = 1
                      savedentries+=1
                  else :
                    isJsonOk[0] = 1
                    savedentries+=1
                      
            
            otree.Fill()
            
        #print " DoubleChecker = ", DoubleChecker  
          
        self.disconnect()
        print '- Eventloop completed'
        print '   Passing tag: ', savedentries, ' events out of', nentries



