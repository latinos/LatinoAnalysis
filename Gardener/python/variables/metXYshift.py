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
import os
import optparse
import re
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
        group.add_option('-s', '--sample',  dest='sample',  help='sample to correct', default='Run2016BDouble')
        parser.add_option_group(group)
        return group

    def checkOptions(self,opts) :
        self.cmssw     = opts.cmssw
        self.paraFile  = opts.paraFile
        self.sample  = opts.sample
        self.cmssw_base= os.getenv('CMSSW_BASE')
        print "  cmssw =", self.cmssw
        print "  paraFile =",self.cmssw_base,"/src/LatinoAnalysis/Gardener/python/data/met/", self.paraFile

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

        #cmssw_base = os.getenv('CMSSW_BASE')
	#sys.path.append(cmssw_base+'/src/LatinoAnalysis/Gardener/python/data/met/')
	#locateParaFile= cmssw_base+'/src/LatinoAnalysis/Gardener/python/data/met/'+self.paraFile
	#print locateParaFile
	#exec("paraSet = " +self.sample)
	#print 'para. name:', paraSet.name, paraSet.varType, paraSet.fx, paraSet.paraX[0], paraSet.paraX[1], paraSet.fy, paraSet.paraY[0], paraSet.paraY[1]
	#self.extractPara()
        try:
            ROOT.gROOT.LoadMacro(self.cmssw_base+'/src/LatinoAnalysis/Gardener/python/variables/metXYshift.C+g')
        except RuntimeError:
            ROOT.gROOT.LoadMacro(self.cmssw_base+'/src/LatinoAnalysis/Gardener/python/variables/metXYshift.C++g')
	
	MetXYshift = ROOT.metXYshift(self.cmssw_base+"/src/LatinoAnalysis/Gardener/python/data/met/"+self.paraFile)


	MetXYshift.printPara()


        self.connect(tree,input)

        nentries = self.itree.GetEntries()
	#nentries = 10
        print ' - Input entries:', nentries 
        savedentries = 0

	#print "cmssw_base =", cmssw_base
        # Create branches for otree, the ones that will be modified
        self.metVariables = [ 'corrMetPfType1', 'corrMetPfType1Phi', 'corrMetPfRaw', 'corrMetPfRawPhi' ]
        
        # Clone the tree with new branches added
        self.clone(output, self.metVariables)
      
        # Now actually connect the branches
        corrMetPfType1 = numpy.ones(1, dtype=numpy.float32)
        corrMetPfType1Phi = numpy.ones(1, dtype=numpy.float32)
        corrMetPfRaw = numpy.ones(1, dtype=numpy.float32)
        corrMetPfRawPhi = numpy.ones(1, dtype=numpy.float32)

        self.otree.Branch('corrMetPfType1', corrMetPfType1, 'corrMetPfType1/F')
        self.otree.Branch('corrMetPfType1Phi', corrMetPfType1Phi, 'corrMetPfType1Phi/F')
        self.otree.Branch('corrMetPfRaw', corrMetPfType1, 'corrMetPfRaw/F')
        self.otree.Branch('corrMetPfRawPhi', corrMetPfType1Phi, 'corrMetPfRawPhi/F')

        # Input tree  
        itree = self.itree

        #-----------------------------------------------------------------------
        print ' - Starting event loop'
        step = 50000

	#nentries = 10
        corx = ROOT.Double(0)
        cory = ROOT.Double(0)

        oldMetPfType1 = ROOT.Double(0)
        oldMetPfType1Phi = ROOT.Double(0)
        corrMetPfType1_x = ROOT.Double(0)
        corrMetPfType1_y = ROOT.Double(0)
	corrMetPftype1_2d = TVector2()

        oldMetPfRaw = ROOT.Double(0)
        oldMetPfRawPhi = ROOT.Double(0)
        corrMetPfRaw_x = ROOT.Double(0)
        corrMetPfRaw_y = ROOT.Double(0)
	corrMetPfRaw_2d = TVector2()

        nGoodVtx = ROOT.Double(0)

        for i in xrange(nentries) :
          itree.GetEntry(i)

	  nGoodVtx = itree.nGoodVtx

          # 76x ----------------------------------------------------------------
          if self.cmssw >= 763 :
              oldMetPfType1    = itree.metPfType1
              oldMetPfType1Phi    = itree.metPfType1Phi
	      oldMetPfRaw      = itree.metPfRaw
	      oldMetPfRawPhi   = itree.metPfRawPhi


          # 74x ----------------------------------------------------------------
          else :
              oldMetPfType1 = itree.pfType1Met
              oldMetPfType1Phi = itree.pfType1Metphi
	      oldMetPfRaw      = itree.metPfRaw
	      oldMetPfRawPhi   = itree.metPfRawPhi

#varType = "multiplicity":0, "ngoodVertices":1, "sumPt":2
	  if MetXYshift.ParVar() == 0 :
	    #print "multiplicity ===================="
	    #MetXYshift.CalcXYshiftCorr(
	    #    self.sample,
	    #    multi,
	    #      #itree.egammaHFPlus_counts,#TODO need to be changed to ele
	    #      #itree.egammaHFMinus_counts,#TODO need to be changed to mu
	    #      corx, cory
	    #)
	    print "MetXYshift sumPt not ready"
	    sys.exit(0)
	  elif MetXYshift.ParVar() == 1 :

	    MetXYshift.CalcXYshiftCorr(
		self.sample,
		nGoodVtx,
		oldMetPfType1,
	          corx, cory
	    )

	  elif MetXYshift.ParVar() == 2 :
	    print "MetXYshift sumPt not ready"
	    sys.exit(0)
	  else :
	    print "no case of parVar; exiting"
	    sys.exit(0)

          #################################
	  # Correction of PfType1
          #################################
	  #print 'corx: ', corx, ' cory: ', cory
	  oldMetPfType1_x = oldMetPfType1*math.cos(oldMetPfType1Phi)
	  oldMetPfType1_y = oldMetPfType1*math.sin(oldMetPfType1Phi)

	  #print '=========================='
	  #print 'old xy ', corrMetPfType1_x, corrMetPfType1_y
	  corrMetPfType1_x = corx + oldMetPfType1_x
	  corrMetPfType1_y = cory + oldMetPfType1_y
	  #print 'new xy ', corrMetPfType1_x, corrMetPfType1_y
	  corrMetPftype1_2d.Set(corrMetPfType1_x, corrMetPfType1_y)
	  #corrPftype1Met_2d = TVector2(corrMetPfType1_x, corrMetPfType1_y)
	  corrMetPfType1[0] = corrMetPftype1_2d.Mod()
	  corrMetPfType1Phi[0] = corrMetPftype1_2d.Phi()
	  corrMetPfType1Phi[0] = self.phiLessPi(corrMetPfType1Phi)

	  #corrMetPfType1 = math.sqrt(corrMetPfType1_x * corrMetPfType1_x + corrMetPfType1_y*corrMetPfType1_y)
	  #corrMetPfType1Phi = math.asin(corrMetPfType1_y / corrMetPfType1 )

	  #print 'oldMet, phi: ', oldMetPfType1, oldMetPfType1Phi
	  #print 'newMet, phi: ', corrMetPfType1[0], corrMetPfType1Phi[0]

          #################################
	  # Correction of PfRaw
          #################################
	  oldMetPfRaw_x = oldMetPfRaw*math.cos(oldMetPfRawPhi)
	  oldMetPfRaw_y = oldMetPfRaw*math.sin(oldMetPfRawPhi)

	  corrMetPfRaw_x = corx + oldMetPfRaw_x
	  corrMetPfRaw_y = cory + oldMetPfRaw_y
	  corrMetPfRaw_2d.Set(corrMetPfRaw_x, corrMetPfRaw_y)
	  corrMetPfRaw[0] = corrMetPfRaw_2d.Mod()
	  corrMetPfRawPhi[0] = corrMetPfRaw_2d.Phi()
	  corrMetPfRawPhi[0] = self.phiLessPi(corrMetPfRawPhi)


          if (i > 0 and i%step == 0.) :
	    print i,'events processed ::', nentries, 'oldMetPfType1:', oldMetPfType1, 'corrMetPfType1:', corrMetPfType1[0], 'oldMetPfType1Phi:', oldMetPfType1Phi, 'corrMetPfType1Phi:', corrMetPfType1Phi[0]
	    print 'oldMetPfRaw:', oldMetPfRaw, 'corrMetPfRaw:', corrMetPfRaw[0], 'oldMetPfRawPhi:', oldMetPfRawPhi, 'corrMetPfRawPhi:', corrMetPfRawPhi[0]
              
          self.otree.Fill()
          savedentries+=1
        self.disconnect()
        print ' - Event loop completed'
        print ' - Saved entries:', savedentries

