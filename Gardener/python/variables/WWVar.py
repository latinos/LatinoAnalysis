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
        newbranches = ['pTWW', 'HT', 'redHT', 'mT2', 'mTi', 'mTe', 'choiMass', 'dphillmet', 'jetpt1_cut', 'dphilljet_cut', 'dphijet1met_cut', 'recoil', 'PfMetDivSumMet', 'PfMetDivSumMet', 'upara', 'uperp', 'm2ljj20', 'm2ljj30', 'ptTOT_cut', 'mTOT_cut', 'OLV1_cut', 'OLV2_cut', 'Ceta_cut']
        self.clone(output,newbranches)

        pTWW    = numpy.ones(1, dtype=numpy.float32)
        HT      = numpy.ones(1, dtype=numpy.float32)
        redHT   = numpy.ones(1, dtype=numpy.float32)
        mT2     = numpy.ones(1, dtype=numpy.float32)
        mTi     = numpy.ones(1, dtype=numpy.float32)
        mTe     = numpy.ones(1, dtype=numpy.float32)
        choiMass = numpy.ones(1, dtype=numpy.float32)
        dphillmet       = numpy.ones(1, dtype=numpy.float32)
        jetpt1_cut      = numpy.ones(1, dtype=numpy.float32)
        dphilljet_cut   = numpy.ones(1, dtype=numpy.float32)
        dphijet1met_cut = numpy.ones(1, dtype=numpy.float32)
        recoil          = numpy.ones(1, dtype=numpy.float32)
        PfMetDivSumMet  = numpy.ones(1, dtype=numpy.float32)
        upara           = numpy.ones(1, dtype=numpy.float32)
        uperp           = numpy.ones(1, dtype=numpy.float32)
        m2ljj20         = numpy.ones(1, dtype=numpy.float32)
        m2ljj30         = numpy.ones(1, dtype=numpy.float32)
        ptTOT_cut       = numpy.ones(1, dtype=numpy.float32)
        mTOT_cut        = numpy.ones(1, dtype=numpy.float32)
        OLV1_cut        = numpy.ones(1, dtype=numpy.float32)
        OLV2_cut        = numpy.ones(1, dtype=numpy.float32)
        Ceta_cut        = numpy.ones(1, dtype=numpy.float32)


        self.otree.Branch('pTWW'  , pTWW  , 'pTWW/F')
        self.otree.Branch('HT'    , HT    , 'HT/F')
        self.otree.Branch('redHT' , redHT , 'redHT/F')
        self.otree.Branch('mT2'   , mT2   , 'mT2/F')
        self.otree.Branch('mTi'   , mTi   , 'mTi/F')
        self.otree.Branch('mTe'   , mTe   , 'mTe/F')
        self.otree.Branch('choiMass'   , choiMass   , 'choiMass/F')
        self.otree.Branch('dphillmet'         , dphillmet      , 'dphillmet/F')
        self.otree.Branch('jetpt1_cut'        , jetpt1_cut     , 'jetpt1_cut/F')
        self.otree.Branch('dphilljet_cut'     , dphilljet_cut  , 'dphilljet_cut/F')
        self.otree.Branch('dphijet1met_cut'   , dphijet1met_cut, 'dphijet1met_cut/F')
        self.otree.Branch('recoil'            , recoil         , 'recoil/F')
        self.otree.Branch('PfMetDivSumMet'    , PfMetDivSumMet , 'PfMetDivSumMet/F')
        self.otree.Branch('upara         '    , upara          , 'upara/F')
        self.otree.Branch('uperp         '    , uperp          , 'uperp/F') 
        self.otree.Branch('m2ljj20       '    , m2ljj20        , 'm2ljj20/F') 
        self.otree.Branch('m2ljj30       '    , m2ljj30        , 'm2ljj30/F') 
        self.otree.Branch('ptTOT_cut     '    , ptTOT_cut      , 'ptTOT_cut/F')
        self.otree.Branch('mTOT_cut      '    , mTOT_cut       , 'mTOT_cut/F')
        self.otree.Branch('OLV1_cut      '    , OLV1_cut       , 'OLV1_cut/F')
        self.otree.Branch('OLV2_cut      '    , OLV2_cut       , 'OLV2_cut/F')
        self.otree.Branch('Ceta_cut      '    , Ceta_cut       , 'Ceta_cut/F')

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
            metsum = itree.metPfType1SumEt

            jetpt1   = itree.std_vector_jet_pt[0]
            jetpt2   = itree.std_vector_jet_pt[1]
            jeteta1  = itree.std_vector_jet_eta[0]
            jeteta2  = itree.std_vector_jet_eta[1]
            jetphi1  = itree.std_vector_jet_phi[0]
            jetphi2  = itree.std_vector_jet_phi[1]
            jetmass1 = itree.std_vector_jet_mass[0]
            jetmass2 = itree.std_vector_jet_mass[1]

            WW = ROOT.WW(pt1, pt2, eta1, eta2, phi1, phi2, met, metphi, metsum, jetpt1, jetpt2, jeteta1, jeteta2, jetphi1, jetphi2, jetmass1, jetmass2)

            
            #ptWW
            pTWW[0]   = WW.pTWW()
            #print "dphill = ", WW.dphill()
            
            
            # mT2
            #WW = ROOT.WW(pt1, pt2, phi1, phi2, met, metphi)
            mT2[0]   = WW.mT2()
            
	    # mTi
            WWi = ROOT.WW(pt1, pt2, eta1, eta2, phi1, phi2, met, metphi)
            mTi[0]   = WWi.mTi()
            mTe[0]   = WWi.mTe()
            choiMass[0] = WWi.choiMass()
            
            # calculate HT with leptons and jets
            HT[0] = 0.0
            redHT[0] = 0.0
            for iLep in range(itree.std_vector_lepton_pt.size()) :
              if itree.std_vector_lepton_pt[iLep] > 0 :
                HT[0] += itree.std_vector_lepton_pt[iLep]
                if iLep >= 2 :   # exclude the first two leptons
                  redHT[0] += itree.std_vector_lepton_pt[iLep]
               
            for iJet in range(itree.std_vector_jet_pt.size()) :
              if itree.std_vector_jet_pt[iJet] > 0 :
                HT[0] += itree.std_vector_jet_pt[iJet]
                redHT[0] += itree.std_vector_jet_pt[iJet]
            
            HT[0] += met
            #redHT[0] --> redHT doesn't use met
            
            
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

            #m2ljj20
            m2ljj20[0]         = WW.m2ljj20()

            #m2ljj30
            m2ljj30[0]         = WW.m2ljj30()

            #ptTOT_cut
            ptTOT_cut[0]       = WW.ptTOT_cut() 

            #mTOT_cut 
            mTOT_cut[0]        = WW.mTOT_cut()

            #OLV1_cut 
            OLV1_cut[0]        = WW.OLV1_cut()

            #OLV2_cut 
            OLV2_cut[0]        = WW.OLV2_cut()

            #Ceta_cut 
            Ceta_cut[0]        = WW.Ceta_cut()


            otree.Fill()

        self.disconnect()
        print '- Eventloop completed'
