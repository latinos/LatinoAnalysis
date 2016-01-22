from LatinoAnalysis.Gardener.gardening import TreeCloner
import numpy
import ROOT
import math
import sys
import optparse
import re
import warnings
import os.path
from collections import OrderedDict
from array import array;

class MetUncertaintyTreeMaker(TreeCloner):
    def __init__(self):
       pass

    def help(self):
        return '''MET uncertainty'''

    def addOptions(self,parser):
        description = self.help()
        group = optparse.OptionGroup(parser,self.label, description)
        group.add_option('-c', '--cmssw', dest='cmssw', help='cmssw version (naming convention may change)', default='763')
        group.add_option('-k',  '--kind', dest='kind',  help='<Up|Dn> variation', default='Up')
        parser.add_option_group(group)
        return group

    def checkOptions(self,opts):
        self.cmssw = opts.cmssw
        self.kind  = opts.kind

    def process(self,**kwargs):
        tree   = kwargs['tree']
        input  = kwargs['input']
        output = kwargs['output']
                
        # does that work so easily and give new variable itree and otree?
        self.connect(tree,input)

        nentries = self.itree.GetEntries()
        print 'Total number of entries:', nentries 
        savedentries = 0

        # create branches for otree, the ones that will be modified
        self.metVariables = ['metPfType1']
        
        # clone the tree with new branches added
        self.clone(output,self.metVariables)
      
        self.oldMetBranches = {}
        for bname in self.metVariables:
          bvariable = numpy.ones(1, dtype=numpy.float32)
          self.oldMetBranches[bname] = bvariable

        # now actually connect the branches
        for bname, bvariable in self.oldMetBranches.iteritems():
            self.otree.Branch(bname,bvariable,bname+'/F')

        # input tree  
        itree = self.itree

        #-----------------------------------------------------------------------
        print '- Starting event loop'
        step = 5000

        for i in xrange(nentries):
          itree.GetEntry(i)

          oldmet = itree.metPfType1

          if self.kind == 'Up' :
              jetEn  = oldmet - itree.metPfType1JetEnUp
              jetRes = oldmet - itree.metPfType1JetResUp
              muonEn = oldmet - itree.metPfType1MuonEnUp
              elecEn = oldmet - itree.metPfType1ElecEnUp
              unclEn = oldmet - itree.metPfType1UnclEnUp
              newmet = oldmet + ROOT.TMath.Sqrt(jetEn*jetEn + jetRes*jetRes + muonEn*muonEn + unclEn*unclEn)
          else :
              jetEn  = oldmet - itree.metPfType1JetEnDn
              jetRes = oldmet - itree.metPfType1JetResDn
              muonEn = oldmet - itree.metPfType1MuonEnDn
              elecEn = oldmet - itree.metPfType1ElecEnDn
              unclEn = oldmet - itree.metPfType1UnclEnDn
              newmet = oldmet - ROOT.TMath.Sqrt(jetEn*jetEn + jetRes*jetRes + muonEn*muonEn + unclEn*unclEn)

          print 'old met:', oldmet, 'new met:', newmet

          if i > 0 and i%step == 0.:
            print i,'events processed :: ', nentries
              
          # now fill the variables
#          for bname, bvariable in self.oldMetBranches.iteritems():
#              bvariable[0] = getattr(WW, bname)()

          self.otree.Fill()
          savedentries+=1
          
        self.disconnect()
        print '- Event loop completed'
        print '   Saved:', savedentries, 'events'
