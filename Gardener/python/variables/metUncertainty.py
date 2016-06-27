#  
#     \  |  ____| __ __|                                      |          _)         |          
#    |\/ |  __|      |        |   |  __ \    __|   _ \   __|  __|   _` |  |  __ \   __|  |   | 
#    |   |  |        |        |   |  |   |  (      __/  |     |    (   |  |  |   |  |    |   | 
#   _|  _| _____|   _|       \__,_| _|  _| \___| \___| _|    \__| \__,_| _| _|  _| \__| \__, | 
#                                                                                       ____/  
#  


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

class MetUncertaintyTreeMaker(TreeCloner) :
    def __init__(self) :
       pass

    def help(self) :
        return '''MET uncertainty'''

    def addOptions(self,parser) :
        description = self.help()
        group = optparse.OptionGroup(parser,self.label, description)
        group.add_option('-c', '--cmssw',  dest='cmssw',  help='cmssw version (naming convention may change)', default='763')
        group.add_option('-k', '--kind',   dest='kind',   help='<Up|Dn> variation', default='Up', type='string')
        group.add_option('-l', '--lepton', dest='lepton', help='Include leptons in the MET uncertainty? <yes|no>', default='yes', type='string')
        group.add_option('--jetresolution', dest='jetresolution', help='Include Jet energy resolution in the MET uncertainty? <yes|no>', default='yes', type='string')
        group.add_option('--unclustered',   dest='unclustered',   help='Include unclustered pf candidates in the MET uncertainty? <yes|no>', default='yes', type='string')
        parser.add_option_group(group)
        return group

    def checkOptions(self,opts) :
        self.cmssw  = opts.cmssw
        self.kind   = opts.kind
        self.lepton = opts.lepton
        self.jetresolution = opts.jetresolution
        self.unclustered = opts.unclustered

        # force unclustered part to 'yes' for ICHEP2016
        if opts.cmssw == 'ICHEP2016' :
          self.unclustered = 'yes'

        print "  cmssw =", self.cmssw
        print "   kind =", self.kind
        print " lepton =", self.lepton
        print " jetresolution =", self.jetresolution
        print " unclustered =", self.unclustered
        

    def deltaphi(self, phi1, phi2) :
        dphi = abs(phi1 - phi2)
        if dphi > ROOT.TMath.Pi() :
            dphi = 2*ROOT.TMath.Pi() - dphi
        return dphi

    def process(self,**kwargs) :
        tree   = kwargs['tree']
        input  = kwargs['input']
        output = kwargs['output']
         
        self.connect(tree,input)

        nentries = self.itree.GetEntries()
        print ' - Input entries:', nentries 
        savedentries = 0

        # Create branches for otree, the ones that will be modified
        if self.cmssw == '74x' :
            self.metVariables = [ 'pfType1Met', 'pfType1Metphi' ]
        else :
            self.metVariables = [ 'metPfType1', 'metPfType1Phi' ]
        
        # Clone the tree with new branches added
        self.clone(output, self.metVariables)
      
        # Now actually connect the branches
        newmet = numpy.ones(1, dtype=numpy.float32)
        newphi = numpy.ones(1, dtype=numpy.float32)

        if self.cmssw == '74x' :
            self.otree.Branch('pfType1Met',    newmet, 'pfType1Met/F')
            self.otree.Branch('pfType1Metphi', newphi, 'pfType1Metphi/F')
        else :
            self.otree.Branch('metPfType1',    newmet, 'metPfType1/F')
            self.otree.Branch('metPfType1Phi', newphi, 'metPfType1Phi/F')

        # Input tree  
        itree = self.itree

        #-----------------------------------------------------------------------
        print ' - Starting event loop'
        step = 5000

        for i in xrange(nentries) :
          itree.GetEntry(i)

          # 74x ----------------------------------------------------------------
          if self.cmssw == '74x' :

              oldmet = itree.pfType1Met
              oldphi = itree.pfType1Metphi

              if self.kind == 'Up' : newmet[0] = itree.pfType1Metup
              if self.kind == 'Dn' : newmet[0] = itree.pfType1Metdn

              newphi[0] = oldphi

          # 76x and more ----------------------------------------------------------------
          else :
              oldmet = itree.metPfType1
              oldphi = itree.metPfType1Phi

              if self.kind == 'Up' :
                  metJetEn  = itree.metPfType1JetEnUp  - oldmet
                  metJetRes = itree.metPfType1JetResUp - oldmet
                  metMuonEn = itree.metPfType1MuonEnUp - oldmet
                  metElecEn = itree.metPfType1ElecEnUp - oldmet
                  metUnclEn = itree.metPfType1UnclEnUp - oldmet

                  phiJetEn  = self.deltaphi(itree.metPfRawPhiJetEnUp,  oldphi)
                  phiJetRes = self.deltaphi(itree.metPfRawPhiJetResUp, oldphi)
                  phiMuonEn = self.deltaphi(itree.metPfRawPhiMuonEnUp, oldphi)
                  phiElecEn = self.deltaphi(itree.metPfRawPhiElecEnUp, oldphi)
                  phiUnclEn = self.deltaphi(itree.metPfRawPhiUnclEnUp, oldphi)
                  
                  if (self.lepton == 'no') :
                      metMuonEn = 0.
                      metElecEn = 0.
                      phiMuonEn = 0.
                      phiElecEn = 0.

                  if (self.jetresolution == 'no') :
                      metJetRes = 0.
                      phiJetRes = 0.

                  if (self.unclustered == 'no') :
                      metUnclEn = 0.
                      phiUnclEn = 0.
                      
  
                  deltaphimax = max(phiJetEn, phiJetRes, phiMuonEn, phiElecEn, phiUnclEn)

                  if (deltaphimax == phiJetEn)  : newphi[0] = itree.metPfRawPhiJetEnUp
                  if (deltaphimax == phiJetRes) : newphi[0] = itree.metPfRawPhiJetResUp
                  if (deltaphimax == phiMuonEn) : newphi[0] = itree.metPfRawPhiMuonEnUp
                  if (deltaphimax == phiElecEn) : newphi[0] = itree.metPfRawPhiElecEnUp
                  if (deltaphimax == phiUnclEn) : newphi[0] = itree.metPfRawPhiUnclEnUp

              else :
                  metJetEn  = itree.metPfType1JetEnDn  - oldmet
                  metJetRes = itree.metPfType1JetResDn - oldmet
                  metMuonEn = itree.metPfType1MuonEnDn - oldmet
                  metElecEn = itree.metPfType1ElecEnDn - oldmet
                  metUnclEn = itree.metPfType1UnclEnDn - oldmet

                  phiJetEn  = self.deltaphi(itree.metPfRawPhiJetEnDn,  oldphi)
                  phiJetRes = self.deltaphi(itree.metPfRawPhiJetResDn, oldphi)
                  phiMuonEn = self.deltaphi(itree.metPfRawPhiMuonEnDn, oldphi)
                  phiElecEn = self.deltaphi(itree.metPfRawPhiElecEnDn, oldphi)
                  phiUnclEn = self.deltaphi(itree.metPfRawPhiUnclEnDn, oldphi)

                  if (self.lepton == 'no') :
                      metMuonEn = 0.
                      metElecEn = 0.
                      phiMuonEn = 0.
                      phiElecEn = 0.

                  if (self.jetresolution == 'no') :
                      metJetRes = 0.
                      phiJetRes = 0.

                  if (self.unclustered == 'no') :
                      metUnclEn = 0.
                      phiUnclEn = 0.

                  deltaphimax = max(phiJetEn, phiJetRes, phiMuonEn, phiElecEn, phiUnclEn)
                      
                  if (deltaphimax == phiJetEn)  : newphi[0] = itree.metPfRawPhiJetEnDn
                  if (deltaphimax == phiJetRes) : newphi[0] = itree.metPfRawPhiJetResDn
                  if (deltaphimax == phiMuonEn) : newphi[0] = itree.metPfRawPhiMuonEnDn
                  if (deltaphimax == phiElecEn) : newphi[0] = itree.metPfRawPhiElecEnDn
                  if (deltaphimax == phiUnclEn) : newphi[0] = itree.metPfRawPhiUnclEnDn

              deltamet = ROOT.TMath.Sqrt(metJetEn*metJetEn + metJetRes*metJetRes + metElecEn*metElecEn + metMuonEn*metMuonEn + metUnclEn*metUnclEn)

              if self.kind == 'Up' : newmet[0] = oldmet + deltamet
              if self.kind == 'Dn' : newmet[0] = oldmet - deltamet


          if (i > 0 and i%step == 0.) :
              print i,'events processed ::', nentries, 'oldmet:', oldmet, 'newmet:', newmet[0], 'oldphi:', oldphi, 'newphi:', newphi[0]
              
          self.otree.Fill()
          savedentries+=1
          
        self.disconnect()
        print ' - Event loop completed'
        print ' - Saved entries:', savedentries
