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
from ROOT import TVector2
#from ROOT import Cartesian2D
import math
import sys
import optparse
import re
import warnings
import os.path
from array import array;

class MetXYshiftTreeMaker(TreeCloner) :
    def __init__(self) :
       pass

    def help(self) :
        return '''MET XYshift'''

    def addOptions(self,parser) :
        description = self.help()
        group = optparse.OptionGroup(parser,self.label, description)
        group.add_option('-c', '--cmssw',  dest='cmssw',  help='cmssw version (naming convention may change)', default='763')
        group.add_option('-p', '--paraFile',  dest='paraFile',  help='correction parameter sets', default='Spring16_V0_MET_MC_XYshiftMC_PfType1MetLocal.txt')
        parser.add_option_group(group)
        return group

    def checkOptions(self,opts) :
        self.cmssw     = opts.cmssw
        self.paraFile  = opts.paraFile
        self.cmssw_base= os.getenv('CMSSW_BASE')
        print "  cmssw =", self.cmssw
        print "  paraFile =", self.paraFile

    def deltaphi(self, phi1, phi2) :
        dphi = abs(phi1 - phi2)
        if dphi > ROOT.TMath.Pi() :
            dphi = dphi - 2*ROOT.TMath.Pi()
        return dphi

    def phiLessPi(self, phi) :
        if phi > ROOT.TMath.Pi() :
            phi = phi - 2*ROOT.TMath.Pi()
        return phi

    #def extractPara(self) :
    #  f = open(self.cmssw_base+"/src/LatinoAnalysis/Gardener/input/"+self.paraFile, 'r')
    #  for line in f:
#	print(line)

    def process(self,**kwargs) :
        tree   = kwargs['tree']
        input  = kwargs['input']
        output = kwargs['output']

	#self.extractPara()
        try:
            ROOT.gROOT.LoadMacro(self.cmssw_base+'/src/LatinoAnalysis/Gardener/python/variables/metXYshift.C+g')
        except RuntimeError:
            ROOT.gROOT.LoadMacro(self.cmssw_base+'/src/LatinoAnalysis/Gardener/python/variables/metXYshift.C++g')
	
	metXYshift = ROOT.metXYshift(self.cmssw_base+"/src/LatinoAnalysis/Gardener/input/"+self.paraFile)
	#metXYshift.printPara()
         
        self.connect(tree,input)

        nentries = self.itree.GetEntries()
        print ' - Input entries:', nentries 
        savedentries = 0

        #cmssw_base = os.getenv('CMSSW_BASE')
	#print "cmssw_base =", cmssw_base
        # Create branches for otree, the ones that will be modified
        self.metVariables = [ 'corrPfType1Met', 'corrPfType1Phi' ]
        
        # Clone the tree with new branches added
        self.clone(output, self.metVariables)
      
        # Now actually connect the branches
        corrPfType1Met = numpy.ones(1, dtype=numpy.float32)
        corrPfType1Phi = numpy.ones(1, dtype=numpy.float32)

        self.otree.Branch('corrPfType1Met', corrPfType1Met, 'corrPfType1Met/F')
        self.otree.Branch('corrPfType1Phi', corrPfType1Phi, 'corrPfType1Phi/F')

        # Input tree  
        itree = self.itree

        #-----------------------------------------------------------------------
        print ' - Starting event loop'
        step = 5000

	#nentries = 100

        for i in xrange(nentries) :
          itree.GetEntry(i)

          # 76x ----------------------------------------------------------------
          if self.cmssw > 763 :
              oldPfType1Met = itree.metPfType1
              oldPfType1Phi = itree.metPfType1Phi


          # 74x ----------------------------------------------------------------
          else :
              oldPfType1Met = itree.pfType1Met
              oldPfType1Phi = itree.pfType1Metphi

          corx = ROOT.Double(0)
          cory = ROOT.Double(0)
	  metXYshift.CalcXYshiftCorr(
	          itree.hEtaPlus_counts,
	          itree.hEtaMinus_counts,
	          itree.h0Barrel_counts,
	          itree.h0EndcapPlus_counts,
	          itree.h0EndcapMinus_counts,
	          itree.gammaBarrel_counts,
	          itree.gammaEndcapPlus_counts,
	          itree.gammaEndcapMinus_counts,
	          itree.hHFPlus_counts,
	          itree.hHFMinus_counts,
	          itree.egammaHFPlus_counts,
	          itree.egammaHFMinus_counts,
		  corx, cory
	      )
	  #print 'corx: ', corx, ' cory: ', cory
	  corrPfType1Met_x = oldPfType1Met*math.cos(oldPfType1Phi)
	  corrPfType1Met_y = oldPfType1Met*math.sin(oldPfType1Phi)
	  #print '=========================='
	  #print 'old xy ', corrPfType1Met_x, corrPfType1Met_y
	  corrPfType1Met_x += corx
	  corrPfType1Met_y += cory
	  #print 'new xy ', corrPfType1Met_x, corrPfType1Met_y
	  corrPftype1Met_2d = TVector2(corrPfType1Met_x, corrPfType1Met_y)
	  corrPfType1Met[0] = corrPftype1Met_2d.Mod()
	  corrPfType1Phi[0] = corrPftype1Met_2d.Phi()
	  corrPfType1Phi[0] = self.phiLessPi(corrPfType1Phi)

	  #corrPfType1Met = math.sqrt(corrPfType1Met_x * corrPfType1Met_x + corrPfType1Met_y*corrPfType1Met_y)
	  #corrPfType1Phi = math.asin(corrPfType1Met_y / corrPfType1Met )

	  #print 'oldMet, phi: ', oldPfType1Met, oldPfType1Phi
	  #print 'newMet, phi: ', corrPfType1Met, corrPfType1Phi


          if (i > 0 and i%step == 0.) :
              print i,'events processed ::', nentries, 'oldPfType1Met:', oldPfType1Met, 'corrPfType1Met:', corrPfType1Met[0], 'oldPfType1Phi:', oldPfType1Phi, 'corrPfType1Phi:', corrPfType1Phi[0] 
              
          self.otree.Fill()
          savedentries+=1
          
        self.disconnect()
        print ' - Event loop completed'
        print ' - Saved entries:', savedentries

