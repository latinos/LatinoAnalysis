#
#
#      __ \    \  | 
#      |   |  |\/ | 
#      |   |  |   | 
#     ____/  _|  _| 
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

class DMVarFiller(TreeCloner):
    def __init__(self):
       pass

    def help(self):
        return '''Add new variables for XXWW'''

    def addOptions(self,parser):
        pass

    def checkOptions(self,opts):
        pass

    def process(self,**kwargs):
        tree  = kwargs['tree']
        input = kwargs['input']
        output = kwargs['output']

        # does that work so easily and give new variable itree and otree?
        self.connect(tree,input)
        newbranches = ['dphillStar', 'mllStar']
        self.clone(output,newbranches)

        dphillStar    = numpy.ones(1, dtype=numpy.float32)
        mllStar       = numpy.ones(1, dtype=numpy.float32)
        
        self.otree.Branch('dphillStar'  , dphillStar  , 'dphillStar/F')
        self.otree.Branch('mllStar'     , mllStar     , 'mllStar/F')

        nentries = self.itree.GetEntries()
        print 'Total number of entries: ',nentries 

        #what is self.itree? what is self.otree?
        itree     = self.itree
        otree     = self.otree

        # change this part into correct path structure... 
        cmssw_base = os.getenv('CMSSW_BASE')
        try:
            ROOT.gROOT.LoadMacro(cmssw_base+'/src/LatinoAnalysis/Gardener/python/variables/DMVar.C+g')
        except RuntimeError:
            ROOT.gROOT.LoadMacro(cmssw_base+'/src/LatinoAnalysis/Gardener/python/variables/DMVar.C++g')
        #----------------------------------------------------------------------------------------------------
        print '- Starting eventloop'
        step = 5000

        for i in xrange(nentries):

            itree.GetEntry(i)

            if i > 0 and i%step == 0.:
                print i,'events processed.'

            pt1 = itree.pt1
            pt2 = itree.pt2
            phi1 = itree.phi1
            phi2 = itree.phi2


            met = itree.pfType1Met
            metphi = itree.pfType1Metphi

            #met = itree.pfmet
            #metphi = itree.pfmetphi

            DM = ROOT.DM(pt1, pt2, phi1, phi2, met, metphi)

            dphillStar[0]   = DM.dphillStar()
            mllStar[0]      = DM.mllStar()
             
            otree.Fill()

        self.disconnect()
        print '- Eventloop completed'
