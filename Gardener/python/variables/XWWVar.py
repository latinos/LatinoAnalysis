#
#    \ \  / \ \        / \ \        / 
#     \  /   \ \  \   /   \ \  \   /  
#        \    \ \  \ /     \ \  \ /   
#     _/\_\    \_/\_/       \_/\_/    
#   
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

class XWWVarFiller(TreeCloner):
    def __init__(self):
       pass

    def help(self):
        return '''Add new variables for XWW'''

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
        newbranches = ['m2l']
        self.clone(output,newbranches)

        m2l    = numpy.ones(1, dtype=numpy.float32)

        self.otree.Branch('m2l'  , m2l  , 'm2l/F')

        nentries = self.itree.GetEntries()
        print 'Total number of entries: ',nentries 

        #what is self.itree? what is self.otree?
        itree     = self.itree
        otree     = self.otree

        # change this part into correct path structure... 
        cmssw_base = os.getenv('CMSSW_BASE')
        try:
            ROOT.gROOT.LoadMacro(cmssw_base+'/src/LatinoAnalysis/Gardener/python/variables/XWWVar.C+g')
        except RuntimeError:
            ROOT.gROOT.LoadMacro(cmssw_base+'/src/LatinoAnalysis/Gardener/python/variables/XWWVar.C++g')
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
            eta1 = itree.eta1
            eta2 = itree.eta2


            met = itree.pfType1Met
            metphi = itree.pfType1Metphi

            #met = itree.pfmet
            #metphi = itree.pfmetphi

            XWW = ROOT.XWW(pt1, pt2, phi1, phi2, eta1, eta2, met, metphi)

            m2l[0]   = XWW.M2l()
             
            otree.Fill()

        self.disconnect()
        print '- Eventloop completed'
