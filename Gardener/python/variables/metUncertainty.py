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
        self.metVariables = [ 'metPfType1', 'metPfType1Phi' ]
        
        # clone the tree with new branches added
        self.clone(output,self.metVariables)
      
        # now actually connect the branches
        newmet = numpy.ones(1, dtype=numpy.float32)
        newphi = numpy.ones(1, dtype=numpy.float32)
        self.otree.Branch('metPfType1',    newmet, 'metPfType1/F')
        self.otree.Branch('metPfType1Phi', newphi, 'metPfType1Phi/F')

        # input tree  
        itree = self.itree

        #-----------------------------------------------------------------------
        print '- Starting event loop'
        step = 5000

        for i in xrange(nentries):
          itree.GetEntry(i)

          oldmet = itree.metPfType1
          oldphi = itree.metPfType1Phi

          if self.kind == 'Up' :
              metJetEn  = oldmet - itree.metPfType1JetEnUp
              metJetRes = oldmet - itree.metPfType1JetResUp
              metMuonEn = oldmet - itree.metPfType1MuonEnUp
              metElecEn = oldmet - itree.metPfType1ElecEnUp
              metUnclEn = oldmet - itree.metPfType1UnclEnUp
              newmet[0] = oldmet + ROOT.TMath.Sqrt(metJetEn*metJetEn + metJetRes*metJetRes + metElecEn*metElecEn + metMuonEn*metMuonEn + metUnclEn*metUnclEn)

              phiJetEn  = oldphi - itree.metPfRawPhiJetEnUp
              phiJetRes = oldphi - itree.metPfRawPhiJetResUp
              phiMuonEn = oldphi - itree.metPfRawPhiMuonEnUp
              phiElecEn = oldphi - itree.metPfRawPhiElecEnUp
              phiUnclEn = oldphi - itree.metPfRawPhiUnclEnUp
              newphi[0] = oldphi + ROOT.TMath.Sqrt(phiJetEn*phiJetEn + phiJetRes*phiJetRes + phiElecEn*phiElecEn + phiMuonEn*phiMuonEn + phiUnclEn*phiUnclEn)
          else :
              metJetEn  = oldmet - itree.metPfType1JetEnDn
              metJetRes = oldmet - itree.metPfType1JetResDn
              metMuonEn = oldmet - itree.metPfType1MuonEnDn
              metElecEn = oldmet - itree.metPfType1ElecEnDn
              metUnclEn = oldmet - itree.metPfType1UnclEnDn
              newmet[0] = oldmet - ROOT.TMath.Sqrt(metJetEn*metJetEn + metJetRes*metJetRes + metElecEn*metElecEn + metMuonEn*metMuonEn + metUnclEn*metUnclEn)

              phiJetEn  = oldphi - itree.metPfRawPhiJetEnDn
              phiJetRes = oldphi - itree.metPfRawPhiJetResDn
              phiMuonEn = oldphi - itree.metPfRawPhiMuonEnDn
              phiElecEn = oldphi - itree.metPfRawPhiElecEnDn
              phiUnclEn = oldphi - itree.metPfRawPhiUnclEnDn
              newphi[0] = oldphi - ROOT.TMath.Sqrt(phiJetEn*phiJetEn + phiJetRes*phiJetRes + phiElecEn*phiElecEn + phiMuonEn*phiMuonEn + phiUnclEn*phiUnclEn)

#          print 'old met:', oldmet, 'new met:', newmet[0], 'old phi:', oldphi, 'new phi:', newphi[0]

          if i > 0 and i%step == 0.:
            print i,'events processed :: ', nentries
              
          self.otree.Fill()
          savedentries+=1
          
        self.disconnect()
        print '- Event loop completed'
        print '   Saved:', savedentries, 'events'
