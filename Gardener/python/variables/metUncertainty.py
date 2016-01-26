print """

   \  |  ____| __ __|                                      |          _)         |          
  |\/ |  __|      |        |   |  __ \    __|   _ \   __|  __|   _` |  |  __ \   __|  |   | 
  |   |  |        |        |   |  |   |  (      __/  |     |    (   |  |  |   |  |    |   | 
 _|  _| _____|   _|       \__,_| _|  _| \___| \___| _|    \__| \__,_| _| _|  _| \__| \__, | 
                                                                                     ____/  

"""

from LatinoAnalysis.Gardener.gardening import TreeCloner
import numpy
import ROOT
import math
import sys
import optparse
import re
import warnings
import os.path
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
                
        self.connect(tree,input)

        nentries = self.itree.GetEntries()
        print 'Total number of entries:', nentries 
        savedentries = 0

        # Create branches for otree, the ones that will be modified
        self.metVariables = [ 'metPfType1', 'metPfType1Phi' ]
        
        # Clone the tree with new branches added
        self.clone(output,self.metVariables)
      
        # Now actually connect the branches
        newmet = numpy.ones(1, dtype=numpy.float32)
        newphi = numpy.ones(1, dtype=numpy.float32)
        self.otree.Branch('metPfType1',    newmet, 'metPfType1/F')
        self.otree.Branch('metPfType1Phi', newphi, 'metPfType1Phi/F')

        # Input tree  
        itree = self.itree

        #-----------------------------------------------------------------------
        print '- Starting event loop'
        step = 5000

        for i in xrange(nentries):
          itree.GetEntry(i)

          oldmet = itree.metPfType1
          oldphi = itree.metPfType1Phi

          if self.kind == 'Up' :
              metJetEn  = itree.metPfType1JetEnUp  - oldmet
              metJetRes = itree.metPfType1JetResUp - oldmet
              metMuonEn = itree.metPfType1MuonEnUp - oldmet
              metElecEn = itree.metPfType1ElecEnUp - oldmet
              metUnclEn = itree.metPfType1UnclEnUp - oldmet

              phiJetEn  = itree.metPfRawPhiJetEnUp  - oldphi
              phiJetRes = itree.metPfRawPhiJetResUp - oldphi
              phiMuonEn = itree.metPfRawPhiMuonEnUp - oldphi
              phiElecEn = itree.metPfRawPhiElecEnUp - oldphi
              phiUnclEn = itree.metPfRawPhiUnclEnUp - oldphi
          else :
              metJetEn  = itree.metPfType1JetEnDn  - oldmet
              metJetRes = itree.metPfType1JetResDn - oldmet
              metMuonEn = itree.metPfType1MuonEnDn - oldmet
              metElecEn = itree.metPfType1ElecEnDn - oldmet
              metUnclEn = itree.metPfType1UnclEnDn - oldmet

              phiJetEn  = itree.metPfRawPhiJetEnDn  - oldphi
              phiJetRes = itree.metPfRawPhiJetResDn - oldphi
              phiMuonEn = itree.metPfRawPhiMuonEnDn - oldphi
              phiElecEn = itree.metPfRawPhiElecEnDn - oldphi
              phiUnclEn = itree.metPfRawPhiUnclEnDn - oldphi

          deltaphi = max(abs(phiJetEn), abs(phiJetRes), abs(phiMuonEn), abs(phiElecEn), abs(phiUnclEn))

          if (deltaphi == abs(phiJetEn))  : newphi[0] = phiJetEn  + oldphi
          if (deltaphi == abs(phiJetRes)) : newphi[0] = phiJetRes + oldphi
          if (deltaphi == abs(phiMuonEn)) : newphi[0] = phiMuonEn + oldphi
          if (deltaphi == abs(phiElecEn)) : newphi[0] = phiElecEn + oldphi
          if (deltaphi == abs(phiUnclEn)) : newphi[0] = phiUnclEn + oldphi

          deltamet = ROOT.TMath.Sqrt(metJetEn*metJetEn + metJetRes*metJetRes + metElecEn*metElecEn + metMuonEn*metMuonEn + metUnclEn*metUnclEn)

          if self.kind == 'Up' : newmet[0] = oldmet + deltamet
          if self.kind == 'Dn' : newmet[0] = oldmet - deltamet

          #print 'oldmet:', oldmet, 'newmet:', newmet[0], 'oldphi:', oldphi, 'newphi:', newphi[0]

          if i > 0 and i%step == 0.:
            print i,'events processed :: ', nentries
              
          self.otree.Fill()
          savedentries+=1
          
        self.disconnect()
        print '- Event loop completed'
        print '   Saved:', savedentries, 'events'
