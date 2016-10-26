#
#
#   \ \        / \ \        /    
#    \ \  \   /   \ \  \   /     
#     \ \  \ /     \ \  \ /      
#      \_/\_/       \_/\_/       
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

class WWVarFiller(TreeCloner):
    def __init__(self):
       pass

    def help(self):
        return '''Add new variables for WW'''

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
        newbranches = ['dphillmet', 'recoil']
        self.clone(output,newbranches)

        dphillmet       = numpy.ones(1, dtype=numpy.float32)
        jetpt1_cut      = numpy.ones(1, dtype=numpy.float32)
        dphilljet_cut   = numpy.ones(1, dtype=numpy.float32)
        dphijet1met_cut = numpy.ones(1, dtype=numpy.float32)
        recoil          = numpy.ones(1, dtype=numpy.float32)
        PfMetDivSumMet  = numpy.ones(1, dtype=numpy.float32)
        upara           = numpy.ones(1, dtype=numpy.float32)
        uperp           = numpy.ones(1, dtype=numpy.float32)

        self.otree.Branch('dphillmet'         , dphillmet      , 'dphillmet/F')
        self.otree.Branch('jetpt1_cut'        , jetpt1_cut     , 'jetpt1_cut/F')
        self.otree.Branch('dphilljet_cut'     , dphilljet_cut  , 'dphilljet_cut/F')
        self.otree.Branch('dphijet1met_cut'   , dphijet1met_cut, 'dphijet1met_cut/F')
        self.otree.Branch('recoil'            , recoil         , 'recoil/F')
        self.otree.Branch('PfMetDivSumMet'    , PfMetDivSumMet , 'PfMetDivSumMet/F')
        self.otree.Branch('upara         '    , upara          , 'upara/F')
        self.otree.Branch('uperp         '    , uperp          , 'uperp/F')

        nentries = self.itree.GetEntries()
        print 'Total number of entries: ',nentries 

        #what is self.itree? what is self.otree?
        itree     = self.itree
        otree     = self.otree

        # change this part into correct path structure... 
        cmssw_base = os.getenv('CMSSW_BASE')
        try:
            ROOT.gROOT.LoadMacro(cmssw_base+'/src/LatinoAnalysis/Gardener/python/variables/WWVar.C+g')
        except RuntimeError:
            ROOT.gROOT.LoadMacro(cmssw_base+'/src/LatinoAnalysis/Gardener/python/variables/WWVar.C++g')
        #----------------------------------------------------------------------------------------------------
        print '- Starting eventloop'
        step = 5000

        for i in xrange(nentries):

            itree.GetEntry(i)

            if i > 0 and i%step == 0.:
                print i,'events processed.'

            pt1  = itree.std_vector_lepton_pt[0]
            pt2  = itree.std_vector_lepton_pt[1]
            phi1 = itree.std_vector_lepton_pt[0]
            phi2 = itree.std_vector_lepton_pt[1]
            eta1 = itree.std_vector_lepton_eta[0]
            eta2 = itree.std_vector_lepton_eta[1]

            met    = itree.metPfType1
            metphi = itree.metPfType1Phi
            #metx   = itree.metPfType1 * cos(itree.pfType1Metphi)
            #mety   = itree.pfType1Met * sin(itree.pfType1Metphi)
            metsum = itree.metPfType1SumEt
            #met    = itree.pfmet
            #metphi = itree.pfmetphi
            
            jetpt1   = itree.std_vector_jet_pt[0]
            jetpt2   = itree.std_vector_jet_pt[1]
            jeteta1  = itree.std_vector_jet_eta[0]
            jeteta2  = itree.std_vector_jet_eta[1]
            jetphi1  = itree.std_vector_jet_phi[0]
            jetphi2  = itree.std_vector_jet_phi[1]
            jetmass1 = itree.std_vector_jet_mass[0]
            jetmass2 = itree.std_vector_jet_mass[1]

            WW = ROOT.WW(pt1, pt2, eta1, eta2, phi1, phi2, met, metphi, metsum, jetpt1, jetpt2, jeteta1, jeteta2, jetphi1, jetphi2, jetmass1, jetmass2)
 
            #dphillmet
            dphillmet[0]       = WW.dphillmet()

            #jetpt1_cut
            jetpt1_cut[0]      = WW.jetpt1_cut()

            #dphilljet_cut
            dphilljet_cut[0]   = WW.dphilljet_cut()

            #dphijetmet_cut
            dphijet1met_cut[0] = WW.dphijet1met_cut()
            
            #recoil
            recoil[0]          = WW.recoil()

            #PfMetDivSumMet
            PfMetDivSumMet[0]  = WW.PfMetDivSumMet()
            
            #upara
            upara[0]           = WW.upara()

            #uperp
            uperp[0]           = WW.uperp()

            otree.Fill()

        self.disconnect()
        print '- Eventloop completed'
