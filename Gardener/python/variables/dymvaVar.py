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

class DymvaVarFiller(TreeCloner):

    def __init__(self):
        pass


    def createDYMVA(self):
        self.getDYMVAV0j = ROOT.TMVA.Reader();
        self.getDYMVAV1j = ROOT.TMVA.Reader();
        self.getDYMVAV2j = ROOT.TMVA.Reader();
        
        self.getDYMVAV0j.AddVariable("met",                 (self.var1))
        self.getDYMVAV0j.AddVariable("metsig",              (self.var2))
        self.getDYMVAV0j.AddVariable("uperp",               (self.var3))
        self.getDYMVAV0j.AddVariable("upara",               (self.var4))
        self.getDYMVAV0j.AddVariable("nGoodVertices",       (self.var5))
        self.getDYMVAV0j.AddVariable("dilep_pt",            (self.var6))
        self.getDYMVAV0j.AddVariable("min_mt",              (self.var7))
        self.getDYMVAV0j.AddVariable("max_mt",              (self.var8))
        self.getDYMVAV0j.AddVariable("min_lep_met_dphi",    (self.var9))
        self.getDYMVAV0j.AddVariable("max_lep_met_dphi",    (self.var10))


        # the order is important for TMVA!
        self.getDYMVAV1j.AddVariable("met",                 (self.var1))
        self.getDYMVAV1j.AddVariable("metsig",              (self.var2))
        self.getDYMVAV1j.AddVariable("jet1_met_dphi",       (self.var13))
        self.getDYMVAV1j.AddVariable("upara",               (self.var4))
        self.getDYMVAV1j.AddVariable("uperp",               (self.var3))
        self.getDYMVAV1j.AddVariable("nGoodVertices",       (self.var5))
        self.getDYMVAV1j.AddVariable("dilep_pt",            (self.var6))
        self.getDYMVAV1j.AddVariable("min_mt",              (self.var7))
        self.getDYMVAV1j.AddVariable("max_mt",              (self.var8))
        self.getDYMVAV1j.AddVariable("min_lep_met_dphi",    (self.var9))
        self.getDYMVAV1j.AddVariable("max_lep_met_dphi",    (self.var10))
        
        self.getDYMVAV1j.AddVariable("jet1_pt",              (self.var11))
        self.getDYMVAV1j.AddVariable("dilep_jet1_dphi",      (self.var12))
        
        
        self.getDYMVAV2j.AddVariable("met",                 (self.var1))
        self.getDYMVAV2j.AddVariable("metsig",              (self.var2))
        self.getDYMVAV2j.AddVariable("min_jet_met_dphi",    (self.var11))
        self.getDYMVAV2j.AddVariable("max_jet_met_dphi",    (self.var12))
        self.getDYMVAV2j.AddVariable("upara",               (self.var4))
        self.getDYMVAV2j.AddVariable("uperp",               (self.var3))
        self.getDYMVAV2j.AddVariable("nGoodVertices",       (self.var5))
        self.getDYMVAV2j.AddVariable("dilep_pt",            (self.var6))
        self.getDYMVAV2j.AddVariable("min_mt",              (self.var7))
        self.getDYMVAV2j.AddVariable("max_mt",              (self.var8))
        self.getDYMVAV2j.AddVariable("min_lep_met_dphi",    (self.var9))
        self.getDYMVAV2j.AddVariable("max_lep_met_dphi",    (self.var10))
        
        self.getDYMVAV2j.AddVariable("jet1_pt",             (self.var15))
        self.getDYMVAV2j.AddVariable("jet2_pt",             (self.var16))
        self.getDYMVAV2j.AddVariable("dilep_jet1_dphi",     (self.var13))
        self.getDYMVAV2j.AddVariable("dilep_jet2_dphi",     (self.var14))
        self.getDYMVAV2j.AddVariable("jet1_jet2_dphi",      (self.var17))


        # dymva trainined xml
        baseCMSSW = os.getenv('CMSSW_BASE')
        self.getDYMVAV0j.BookMVA("BDT",baseCMSSW+"/src/LatinoAnalysis/Gardener/python/data/dymva/dymva_0jet_BDT.weights.xml")
        self.getDYMVAV1j.BookMVA("BDT",baseCMSSW+"/src/LatinoAnalysis/Gardener/python/data/dymva/dymva_1jet_BDT.weights.xml")
        self.getDYMVAV2j.BookMVA("BDT",baseCMSSW+"/src/LatinoAnalysis/Gardener/python/data/dymva/dymva_jets_BDT.weights.xml")


    def deltaPhi(self,l1,l2):
       dphi = fabs(l1.DeltaPhi(l2))
       #    dphi = fabs(ROOT.Math.VectorUtil.DeltaPhi(l1.p4(),l2.p4()))
       return dphi


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

        self.getDYMVAV0j = None
        self.getDYMVAV1j = None
        self.getDYMVAV2j = None

        self.var1 = array.array('f',[0])
        self.var2 = array.array('f',[0])
        self.var3 = array.array('f',[0])
        self.var4 = array.array('f',[0])
        self.var5 = array.array('f',[0])
        self.var6 = array.array('f',[0])
        self.var7 = array.array('f',[0])
        self.var8 = array.array('f',[0])
        self.var9 = array.array('f',[0])
        self.var10 = array.array('f',[0])
        self.var11 = array.array('f',[0])
        self.var12 = array.array('f',[0])
        self.var13 = array.array('f',[0])
        self.var14 = array.array('f',[0])
        self.var15 = array.array('f',[0])
        self.var16 = array.array('f',[0])
        self.var17 = array.array('f',[0])
        
        tree  = kwargs['tree']
        input = kwargs['input']
        output = kwargs['output']

        self.connect(tree,input)
        newbranches = ['dymva', 'upara', 'uperp']

        self.clone(output,newbranches)

        dymva      = numpy.ones(1, dtype=numpy.float32)
        upara      = numpy.ones(1, dtype=numpy.float32)
        uperp      = numpy.ones(1, dtype=numpy.float32)

        self.otree.Branch('dymva',  dymva,  'dymva/F')
        self.otree.Branch('upara',  upara,  'upara/F')
        self.otree.Branch('uperp',  uperp,  'uperp/F')

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
            uperp[0] = 0.
            upara[0] = 0.
            dymva[0] = -9999.
            
            if itree.pt1>0 and itree.pt2>0 : 
            
              l1 = ROOT.TLorentzVector()
              l2 = ROOT.TLorentzVector()
              l1.SetPtEtaPhiM(itree.pt1, itree.eta1, itree.phi1, 0)
              l2.SetPtEtaPhiM(itree.pt2, itree.eta2, itree.phi2, 0)
              
              met = ROOT.TLorentzVector()
              met.SetPxPyPzE(itree.pfType1Met * cos (itree.pfType1Metphi), itree.pfType1Met * sin (itree.pfType1Metphi), 0, itree.pfType1Met)
              
              dileptonTransverse = l1+l2
              dileptonTransverse.SetPz(0)
              
              self.var1[0] =  itree.pfType1Met
              self.var2[0] =  itree.pfmetSignificance
              
              
              #utv = -1. * ( met + dileptonTransverse )
              utv = ( - met - dileptonTransverse )
              ut = utv.P()
              phi = utv.DeltaPhi(dileptonTransverse)
              upara[0] = ut * cos(phi)
              uperp[0] = ut * sin(phi);
              
              self.var3[0] =  uperp[0]
              self.var4[0] =  upara[0]
              
              self.var5[0] =  itree.nvtx
              self.var6[0] =  itree.ptll
              
              min_mt = sqrt(2 * itree.pt2 * itree.pfType1Met * (1 - cos(  self.deltaPhi(met, l2) ) ) )
              max_mt = sqrt(2 * itree.pt1 * itree.pfType1Met * (1 - cos(  self.deltaPhi(met, l1) ) ) )
              
              if min_mt >= max_mt :
                 max_mt, min_mt = min_mt, max_mt

              self.var7[0] =  min_mt
              self.var8[0] =  max_mt
              
              min_lep_met_dphi = self.deltaPhi(met, l2)
              max_lep_met_dphi = self.deltaPhi(met, l1)
            
              if min_lep_met_dphi >= max_lep_met_dphi :
                 max_lep_met_dphi, min_lep_met_dphi = min_lep_met_dphi, max_lep_met_dphi
                 
              
              self.var9[0]  =  min_lep_met_dphi
              self.var10[0] =  max_lep_met_dphi
              
              
              if itree.njet >= 1 :
                self.var11[0] =  itree.std_vector_jet_pt[0]
              
                jet1 = ROOT.TLorentzVector()
                jet1.SetPtEtaPhiM(itree.std_vector_jet_pt[0],  itree.std_vector_jet_eta[0],  itree.std_vector_jet_phi[0], 0)
              
                dilep_jet_dphi =  self.deltaPhi(jet1, dileptonTransverse)
                jet_met_dphi =    self.deltaPhi(jet1, met)
              
                self.var12[0] =  dilep_jet_dphi
                self.var13[0] =  jet_met_dphi
              
                if itree.njet >= 2 :
              
                  jet2 = ROOT.TLorentzVector()
                  jet2.SetPtEtaPhiM(itree.std_vector_jet_pt[1],  itree.std_vector_jet_eta[1],  itree.std_vector_jet_phi[1], 0)
              
                  min_jet_met_dphi =  self.deltaPhi(jet2, met)
                  max_jet_met_dphi =  self.deltaPhi(jet1, met)

                  if min_jet_met_dphi >= max_jet_met_dphi :
                     max_jet_met_dphi, min_jet_met_dphi = min_jet_met_dphi, max_jet_met_dphi
              
                  dilep_jet1_dphi =  self.deltaPhi(jet1, dileptonTransverse)
                  dilep_jet2_dphi =  self.deltaPhi(jet2, dileptonTransverse)
              
                  jet1_jet2_dphi =  self.deltaPhi(jet1, jet2)
              
                  self.var11[0] = min_jet_met_dphi
                  self.var12[0] = max_jet_met_dphi
                  self.var13[0] = dilep_jet1_dphi
                  self.var14[0] = dilep_jet2_dphi
                  self.var15[0] = itree.std_vector_jet_pt[0]
                  self.var16[0] = itree.std_vector_jet_pt[1]
                  self.var17[0] = jet1_jet2_dphi 
                   
                  
                  
              if itree.njet == 0:
                    dymva[0] = self.getDYMVAV0j.EvaluateMVA("BDT")
              elif itree.njet == 1:
                    dymva[0] = self.getDYMVAV1j.EvaluateMVA("BDT")
              else :
                    dymva[0] = self.getDYMVAV2j.EvaluateMVA("BDT")
              
            otree.Fill()
            
        self.disconnect()
        print '- Eventloop completed'


