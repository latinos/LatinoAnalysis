from LatinoAnalysis.Gardener.gardening import TreeCloner
import numpy
import ROOT
import sys
import optparse
import re
import warnings
import os.path
from array import array;

class qq2vvEWKcorrectionsWeightFiller(TreeCloner):
    def __init__(self):
       pass

    def help(self):
        return '''Add weight to cope with electroweak corrections'''

    def addOptions(self,parser):
        pass

    def checkOptions(self,opts):
        pass

    def process(self,**kwargs):
        tree  = kwargs['tree']
        input = kwargs['input']
        output = kwargs['output']

        self.connect(tree,input)
        newbranches = ['ewkW']
        self.clone(output,newbranches)

        ewkW    = numpy.ones(1, dtype=numpy.float32)
        self.otree.Branch('ewkW'  , ewkW  , 'ewkW/F')

        nentries = self.itree.GetEntries()
        print 'Total number of entries: ',nentries

        itree     = self.itree
        otree     = self.otree

        cmssw_base = os.getenv('CMSSW_BASE')
        try:
            ROOT.gROOT.LoadMacro(cmssw_base+'/src/LatinoAnalysis/Gardener/python/variables/qq2vvEWKcorrectionsWeight.C+g')
        except RuntimeError:
            ROOT.gROOT.LoadMacro(cmssw_base+'/src/LatinoAnalysis/Gardener/python/variables/qq2vvEWKcorrectionsWeight.C++g')
        #----------------------------------------------------------------------------------------------------

        qq2vvEWKcorrections = ROOT.qq2vvEWKcorrections(cmssw_base+'/src/LatinoAnalysis/Gardener/python/data/ewk/out_qqbww_EW_L8_200_forCMS.dat')

        print '- Starting eventloop'
        step = 5000
        for i in xrange(nentries):
            itree.GetEntry(i)

            if i > 0 and i%step == 0.:
                print i,'events processed.'

            ptl1 = itree.std_vector_LHElepton_pt[0]
            ptl2 = itree.std_vector_LHElepton_pt[1]
            etal1 = itree.std_vector_LHElepton_eta[0]
            etal2 = itree.std_vector_LHElepton_eta[1]
            phil1 = itree.std_vector_LHElepton_phi[0]
            phil2 = itree.std_vector_LHElepton_phi[1]
            idl1 = itree.std_vector_LHElepton_id[0]
            idl2 = itree.std_vector_LHElepton_id[1]

            ptv1 = itree.std_vector_LHEneutrino_pt[0]
            ptv2 = itree.std_vector_LHEneutrino_pt[1]
            etav1 = itree.std_vector_LHEneutrino_eta[0]
            etav2 = itree.std_vector_LHEneutrino_eta[1]
            phiv1 = itree.std_vector_LHEneutrino_phi[0]
            phiv2 = itree.std_vector_LHEneutrino_phi[1]
                  
 
            x1 = itree.pdfx1
            x2 = itree.pdfx2

            id1 = itree.pdfid1
            id2 = itree.pdfid2

    #float ptl1 , float etal1 , float phil1 , float idl1 , // lepton from 1st W
    #float ptl2 , float etal2 , float phil2 , float idl2 , // lepton from 2nd W
    #float ptv1 , float etav1 , float phiv1 ,             // neutrino from 1st W
    #float ptv2 , float etav2 , float phiv2 ,             // neutrino from 2nd W
    #float x1   , float x2 ,                              // parton x-Bjorken
    #int   id1  , int   id2 ,                             // parton PDG id's

            ewkW[0] = qq2vvEWKcorrections.getqq2WWEWKCorr(ptl1, etal1, phil1, idl1, ptl2, etal2, phil2, idl2, ptv1, etav1, phiv1, ptv2, etav2, phiv2, x1, x2, id1, id2)

            otree.Fill()

        self.disconnect()
        print '- Eventloop completed'