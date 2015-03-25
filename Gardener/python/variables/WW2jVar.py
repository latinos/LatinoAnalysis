#
#
#   \ \        / \ \        /     ___ \  _)
#    \ \  \   /   \ \  \   /         ) |  |
#     \ \  \ /     \ \  \ /         __/   |
#      \_/\_/       \_/\_/        _____|  |
#                                     ___/
#
#


from tree.gardening import TreeCloner
import numpy
import ROOT
import sys
import optparse
import re
import warnings
import os.path
from array import array;

class WW2jVarFiller(TreeCloner):
    def __init__(self):
       pass

    def help(self):
        return '''Add new variables for WW + 2j'''

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
        newbranches = ['Mljcloser', 'Mljfarther', 'Ml1j1', 'Ml1j2', 'Ml2j1', 'Ml2j2']
        self.clone(output,newbranches)

        Mljcloser    = numpy.ones(1, dtype=numpy.float32)
        Mljfarther   = numpy.ones(1, dtype=numpy.float32)
        Ml1j1        = numpy.ones(1, dtype=numpy.float32)
        Ml1j2        = numpy.ones(1, dtype=numpy.float32)
        Ml2j1        = numpy.ones(1, dtype=numpy.float32)
        Ml2j2        = numpy.ones(1, dtype=numpy.float32)

        self.otree.Branch('Mljcloser'  , Mljcloser  , 'Mljcloser/F')
        self.otree.Branch('Mljfarther' , Mljfarther , 'Mljfarther/F')
        self.otree.Branch('Ml1j1' , Ml1j1 , 'Ml1j1/F')
        self.otree.Branch('Ml1j2' , Ml1j2 , 'Ml1j2/F')
        self.otree.Branch('Ml2j1' , Ml2j1 , 'Ml2j1/F')
        self.otree.Branch('Ml2j2' , Ml2j2 , 'Ml2j2/F')

        nentries = self.itree.GetEntries()
        print 'Total number of entries: ',nentries 

        #what is self.itree? what is self.otree?
        itree     = self.itree
        otree     = self.otree

        # change this part into correct path structure... 
        cmssw_base = os.getenv('CMSSW_BASE')
        try:
            ROOT.gROOT.LoadMacro(cmssw_base+'/src/HWWAnalysis/ShapeAnalysis/python/tree/WW2jVar.C+g')
        except RuntimeError:
            ROOT.gROOT.LoadMacro(cmssw_base+'/src/HWWAnalysis/ShapeAnalysis/python/tree/WW2jVar.C++g')
        #----------------------------------------------------------------------------------------------------
        print '- Starting eventloop'
        step = 5000

        for i in xrange(nentries):

            itree.GetEntry(i)

            if i > 0 and i%step == 0.:
                print i,'events processed.'

            pt1 = itree.pt1
            pt2 = itree.pt2
            eta1 = itree.eta1
            eta2 = itree.eta2
            phi1 = itree.phi1
            phi2 = itree.phi2

            jetpt1 = itree.jetpt1
            jetpt2 = itree.jetpt2
            jeteta1 = itree.jeteta1
            jeteta2 = itree.jeteta2
            jetphi1 = itree.jetphi1
            jetphi2 = itree.jetphi2

            WW2j = ROOT.WW2j(pt1, pt2, eta1, eta2, phi1, phi2,    jetpt1, jetpt2, jeteta1, jeteta2, jetphi1, jetphi2)

            Mljcloser[0]   = WW2j.Mljcloser()
            Mljfarther[0]  = WW2j.Mljfarther()
            Ml1j1[0]       = WW2j.Mlj(1,1)
            Ml1j2[0]       = WW2j.Mlj(1,2)
            Ml2j1[0]       = WW2j.Mlj(2,1)
            Ml2j2[0]       = WW2j.Mlj(2,2)

            otree.Fill()

        self.disconnect()
        print '- Eventloop completed'
