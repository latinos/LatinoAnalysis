from LatinoAnalysis.Gardener.gardening import TreeCloner


import optparse
import os
import sys
import ROOT
import numpy
import array
import re
import warnings
import os.path
from math import *
import math



#
#  __ \ \ \   /                                                     _)         |      |
#  |   | \   /       __ `__ \ \ \   /  _` |     \ \   /  _` |   __|  |   _` |  __ \   |   _ \
#  |   |    |        |   |   | \ \ /  (   |      \ \ /  (   |  |     |  (   |  |   |  |   __/
# ____/    _|       _|  _|  _|  \_/  \__,_|       \_/  \__,_| _|    _| \__,_| _.__/  _| \___|
#
#

class DymvaHiggsFiller(TreeCloner):

    def __init__(self):
        pass


    def createDYMVA(self):
        self.getDYMVAV0j    = ROOT.TMVA.Reader();
        self.getDYMVAV1j    = ROOT.TMVA.Reader();
        self.getDYMVAV2jggH = ROOT.TMVA.Reader();
        self.getDYMVAV2jVBF = ROOT.TMVA.Reader();
       
        #0j:nvtx/F:mth/F:ptll/F:projtkmet/F:projpfmet/F:jetpt1_cut/F:uperp/F:upara/F:mtw1/F:PfMetDivSumMet/F:metPuppi/F:dphillmet/F:recoil/F:dphilljet_cut/F:dphilmet1/F:mpmet/F
        self.getDYMVAV0j.AddVariable("nvtx",           (self.var0j1))   
        self.getDYMVAV0j.AddVariable("ptll",           (self.var0j2))   
        self.getDYMVAV0j.AddVariable("projtkmet",      (self.var0j3))   
        self.getDYMVAV0j.AddVariable("projpfmet",      (self.var0j4))   
        self.getDYMVAV0j.AddVariable("jetpt1_cut",     (self.var0j5))   
        self.getDYMVAV0j.AddVariable("upara",          (self.var0j6))   
        self.getDYMVAV0j.AddVariable("PfMetDivSumMet", (self.var0j7))   
        self.getDYMVAV0j.AddVariable("recoil",         (self.var0j8))   
        self.getDYMVAV0j.AddVariable("dphilljet_cut",  (self.var0j9))   
        self.getDYMVAV0j.AddVariable("mpmet",          (self.var0j10))   
        self.getDYMVAV0j.AddVariable("dphijet1met_cut",(self.var0j11))   
        self.getDYMVAV0j.AddVariable("mtw2",           (self.var0j11))   

        # 1j: ptll/F:mth/F:mpmet/F:projtkmet/F:projpfmet/F:upara/F:jetpt1_cut/F:PfMetDivSumMet/F:dphilljet_cut/F:nvtx/F:metPuppi/F:dphijet1met_cut/F:uperp/F
        self.getDYMVAV1j.AddVariable("mpmet",             (self.var1j1))
        self.getDYMVAV1j.AddVariable("projtkmet",         (self.var1j2))
        self.getDYMVAV1j.AddVariable("projpfmet",         (self.var1j3))
        self.getDYMVAV1j.AddVariable("upara",             (self.var1j4))
        self.getDYMVAV1j.AddVariable("PfMetDivSumMet",    (self.var1j5))
        self.getDYMVAV1j.AddVariable("dphilljet_cut",     (self.var1j6))
        self.getDYMVAV1j.AddVariable("nvtx",              (self.var1j7))
        self.getDYMVAV1j.AddVariable("metPuppi",          (self.var1j8))
        self.getDYMVAV1j.AddVariable("dphijet1met_cut",   (self.var1j9))
        self.getDYMVAV1j.AddVariable("uperp",             (self.var1j10))
 
        # 2jggH: projtkmet/F:projpfmet/F:PfMetDivSumMet/F:nvtx/F:metPuppi/F:dphijet1met_cut/F:mth/F:ptll/F:jetpt2_cut/F:upara/F:dphijet2met_cut/F:dphilljetjet_cut/F
        self.getDYMVAV2jggH.AddVariable("projtkmet",         (self.var2jggH1))
        self.getDYMVAV2jggH.AddVariable("projpfmet",         (self.var2jggH2))
        self.getDYMVAV2jggH.AddVariable("PfMetDivSumMet",    (self.var2jggH3))
        self.getDYMVAV2jggH.AddVariable("nvtx",              (self.var2jggH4))
        self.getDYMVAV2jggH.AddVariable("metPuppi",          (self.var2jggH5))
        self.getDYMVAV2jggH.AddVariable("dphijet1met_cut",   (self.var2jggH6))
        self.getDYMVAV2jggH.AddVariable("mth",               (self.var2jggH7))
        self.getDYMVAV2jggH.AddVariable("ptll",              (self.var2jggH8))
        self.getDYMVAV2jggH.AddVariable("jetpt2_cut",        (self.var2jggH9))
        self.getDYMVAV2jggH.AddVariable("upara",             (self.var2jggH10))
        self.getDYMVAV2jggH.AddVariable("dphijet2met_cut",   (self.var2jggH11))
        self.getDYMVAV2jggH.AddVariable("dphilljetjet_cut",  (self.var2jggH12))

        # 2jVBF:  projtkmet/F:projpfmet/F:PfMetDivSumMet/F:nvtx/F:dphijet1met_cut/F:mth/F:dphilljetjet_cut/F:dphijjmet_cut/F:mpmet/F
        self.getDYMVAV2jVBF.AddVariable("projtkmet",         (self.var2jVBF1))
        self.getDYMVAV2jVBF.AddVariable("projpfmet",         (self.var2jVBF2))
        self.getDYMVAV2jVBF.AddVariable("PfMetDivSumMet",    (self.var2jVBF3))
        self.getDYMVAV2jVBF.AddVariable("nvtx",              (self.var2jVBF4))
        self.getDYMVAV2jVBF.AddVariable("dphijet1met_cut",   (self.var2jVBF5))
        self.getDYMVAV2jVBF.AddVariable("mth",               (self.var2jVBF6))
        self.getDYMVAV2jVBF.AddVariable("dphilljetjet_cut",  (self.var2jVBF7))
        self.getDYMVAV2jVBF.AddVariable("dphijjmet_cut",     (self.var2jVBF8))
        self.getDYMVAV2jVBF.AddVariable("mpmet",             (self.var2jVBF9))


        # dymva trainined xml
        baseCMSSW = os.getenv('CMSSW_BASE')
        #self.getDYMVAV0j.BookMVA("BDT",baseCMSSW+"/src/LatinoAnalysis/Gardener/python/data/dymva/UATmva_DYmva_0j_BDTG_9Var.weights.xml")
        #self.getDYMVAV1j.BookMVA("BDT",baseCMSSW+"/src/LatinoAnalysis/Gardener/python/data/dymva/UATmva_DYmva_1j_BDTG_10Var.weights.xml")

        self.getDYMVAV0j.BookMVA("BDT",baseCMSSW+"/src/LatinoAnalysis/Gardener/python/data/dymva/UATmva_DYmva_0j_BDTG_12Var.weights.xml")
        self.getDYMVAV1j.BookMVA("BDT",baseCMSSW+"/src/LatinoAnalysis/Gardener/python/data/dymva/UATmva_DYmva_1j_BDTG_10Var.weights.xml")
        self.getDYMVAV2jggH.BookMVA("BDT",baseCMSSW+"/src/LatinoAnalysis/Gardener/python/data/dymva/UATmva_DYmva_2j_BDTG_12Var.weights.xml")
        self.getDYMVAV2jVBF.BookMVA("BDT",baseCMSSW+"/src/LatinoAnalysis/Gardener/python/data/dymva/UATmva_DYmva_VBF2j_BDTG_9Var.weights.xml")

    def help(self):
        return '''Add dy mva variables'''


    def addOptions(self,parser):
        #description = self.help()
        #group = optparse.OptionGroup(parser,self.label, description)
        #group.add_option('-b', '--branch',   dest='branch', help='Name of something that is not used ... ', default='boh')
        #parser.add_option_group(group)
        #return group
        pass


    def checkOptions(self,opts):
        pass

    def process(self,**kwargs):

        self.getDYMVAV0j    = None
        self.getDYMVAV1j    = None
        self.getDYMVAV2jggH = None
        self.getDYMVAV2jVBF = None

        self.var0j1 = array.array('f',[0])
        self.var0j2 = array.array('f',[0])
        self.var0j3 = array.array('f',[0])
        self.var0j4 = array.array('f',[0])
        self.var0j5 = array.array('f',[0])
        self.var0j6 = array.array('f',[0])
        self.var0j7 = array.array('f',[0])
        self.var0j8 = array.array('f',[0])
        self.var0j9 = array.array('f',[0])
        self.var0j10 = array.array('f',[0])
        self.var0j11 = array.array('f',[0])
        self.var0j12 = array.array('f',[0])
       
        self.var1j1 = array.array('f',[0])
        self.var1j2 = array.array('f',[0])
        self.var1j3 = array.array('f',[0])
        self.var1j4 = array.array('f',[0])
        self.var1j5 = array.array('f',[0])
        self.var1j6 = array.array('f',[0])
        self.var1j7 = array.array('f',[0])
        self.var1j8 = array.array('f',[0])
        self.var1j9 = array.array('f',[0])
        self.var1j10 = array.array('f',[0])

        self.var2jggH1 = array.array('f',[0])
        self.var2jggH2 = array.array('f',[0])
        self.var2jggH3 = array.array('f',[0])
        self.var2jggH4 = array.array('f',[0])
        self.var2jggH5 = array.array('f',[0])
        self.var2jggH6 = array.array('f',[0])
        self.var2jggH7 = array.array('f',[0])
        self.var2jggH8 = array.array('f',[0])
        self.var2jggH9 = array.array('f',[0])
        self.var2jggH10 = array.array('f',[0])
        self.var2jggH11 = array.array('f',[0])
        self.var2jggH12 = array.array('f',[0])

        self.var2jVBF1 = array.array('f',[0])
        self.var2jVBF2 = array.array('f',[0])
        self.var2jVBF3 = array.array('f',[0])
        self.var2jVBF4 = array.array('f',[0])
        self.var2jVBF5 = array.array('f',[0])
        self.var2jVBF6 = array.array('f',[0])
        self.var2jVBF7 = array.array('f',[0])
        self.var2jVBF8 = array.array('f',[0])
        self.var2jVBF9 = array.array('f',[0])
        self.var2jVBF10 = array.array('f',[0])
        self.var2jVBF11 = array.array('f',[0])
        self.var2jVBF12 = array.array('f',[0])

 
        tree  = kwargs['tree']
        input = kwargs['input']
        output = kwargs['output']

        self.connect(tree,input)
        newbranches = ['dymvaggh','dymvavbf']

        self.clone(output,newbranches)

        dymvaggh      = numpy.ones(1, dtype=numpy.float32)
        dymvavbf      = numpy.ones(1, dtype=numpy.float32)

        self.otree.Branch('dymvaggh',  dymvaggh,  'dymvaggh/F')
        self.otree.Branch('dymvavbf',  dymvavbf,  'dymvavbf/F')

        self.createDYMVA()

        nentries = self.itree.GetEntries()
        print 'Total number of entries: ',nentries 

        # avoid dots to go faster
        itree     = self.itree
        otree     = self.otree


        print '- Starting eventloop'
        step = 5000
        for i in xrange(nentries):
            itree.GetEntry(i)

            ## print event count
            if i > 0 and i%step == 0.:
                print i,'events processed.'

            # at least 2 leptons!
            dymvaggh[0] = -9999.
            dymvavbf[0] = -9999. # and at least 2 jets
           
           # just because it is easier to write later ...
            pt1 = itree.std_vector_lepton_pt[0]
            pt2 = itree.std_vector_lepton_pt[1]
            jetpt1 = itree.std_vector_jet_pt[0]
            jetpt2 = itree.std_vector_jet_pt[1]
            mjj    = itree.mjj
            detajj = itree.detajj
 
            if pt1>0 and pt2>0 : 
              
              if jetpt1< 30.0 and jetpt2< 30.0 :

                    # nvtx/F:mth/F:ptll/F:projtkmet/F:projpfmet/F:jetpt1_cut/F:uperp/F:upara/F:mtw1/F:PfMetDivSumMet/F:metPuppi/F:dphillmet/F:recoil/F:dphilljet_cut/F:dphilmet1/F:mpmet/
                    self.var0j1[0] = itree.nvtx
                    self.var0j2[0] = itree.ptll
                    self.var0j3[0] = itree.projtkmet
                    self.var0j4[0] = itree.projpfmet
                    self.var0j5[0] = itree.jetpt1_cut
                    self.var0j6[0] = itree.upara
                    self.var0j7[0] = itree.PfMetDivSumMet
                    self.var0j8[0] = itree.recoil
                    self.var0j9[0] = itree.dphilljet_cut
                    self.var0j10[0] = itree.mpmet
                    self.var0j11[0] = itree.dphijet1met_cut
                    self.var0j12[0] = itree.mtw2
 
                    dymvaggh[0] = self.getDYMVAV0j.EvaluateMVA("BDT")

              if jetpt1>= 30.0 and jetpt2< 30.0 :

                    # ptll/F:mth/F:mpmet/F:projtkmet/F:projpfmet/F:upara/F:jetpt1_cut/F:PfMetDivSumMet/F:dphilljet_cut/F:nvtx/F:metPuppi/F:dphijet1met_cut/F
                    self.var1j1[0]  = itree.mpmet
                    self.var1j2[0]  = itree.projtkmet
                    self.var1j3[0]  = itree.projpfmet
                    self.var1j4[0]  = itree.upara
                    self.var1j5[0]  = itree.PfMetDivSumMet
                    self.var1j6[0]  = itree.dphilljet_cut
                    self.var1j7[0]  = itree.nvtx
                    self.var1j8[0]  = itree.metPuppi
                    self.var1j9[0]  = itree.dphijet1met_cut
                    self.var1j10[0] = itree.uperp

                    dymvaggh[0] = self.getDYMVAV1j.EvaluateMVA("BDT")

              if jetpt1>= 30.0 and jetpt2>= 30.0 :

                    # projtkmet/F:projpfmet/F:PfMetDivSumMet/F:nvtx/F:metPuppi/F:dphijet1met_cut/F:mth/F:ptll/F:jetpt2_cut/F:upara/F:dphijet2met_cut/F:dphilljetjet_cut/F
                    self.var2jggH1[0]  = itree.projtkmet
                    self.var2jggH2[0]  = itree.projpfmet
                    self.var2jggH3[0]  = itree.PfMetDivSumMet
                    self.var2jggH4[0]  = itree.nvtx
                    self.var2jggH5[0]  = itree.metPuppi
                    self.var2jggH6[0]  = itree.dphijet1met_cut
                    self.var2jggH7[0]  = itree.mth
                    self.var2jggH8[0]  = itree.ptll
                    self.var2jggH9[0]  = itree.jetpt2_cut
                    self.var2jggH10[0] = itree.upara
                    self.var2jggH11[0] = itree.dphijet2met_cut
                    self.var2jggH12[0] = itree.dphilljetjet_cut

                    dymvaggh[0] = self.getDYMVAV2jggH.EvaluateMVA("BDT")

                    # projtkmet/F:projpfmet/F:PfMetDivSumMet/F:nvtx/F:dphijet1met_cut/F:mth/F:dphilljetjet_cut/F:dphijjmet_cut/F:mpmet/F

                    self.var2jVBF1[0]  = itree.projtkmet
                    self.var2jVBF2[0]  = itree.projpfmet
                    self.var2jVBF3[0]  = itree.PfMetDivSumMet
                    self.var2jVBF4[0]  = itree.nvtx
                    self.var2jVBF5[0]  = itree.dphijet1met_cut
                    self.var2jVBF6[0]  = itree.mth
                    self.var2jVBF7[0]  = itree.dphilljetjet_cut
                    self.var2jVBF8[0]  = itree.dphijjmet_cut
                    self.var2jVBF9[0]  = itree.mpmet

                    dymvavbf[0] = self.getDYMVAV2jVBF.EvaluateMVA("BDT")

              
            otree.Fill()
            
        self.disconnect()
        print '- Eventloop completed'
