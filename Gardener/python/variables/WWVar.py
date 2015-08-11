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
        newbranches = ['pTWW', 'HT', 'redHT']
        self.clone(output,newbranches)

        pTWW    = numpy.ones(1, dtype=numpy.float32)
        HT      = numpy.ones(1, dtype=numpy.float32)
        redHT   = numpy.ones(1, dtype=numpy.float32)

        self.otree.Branch('pTWW'  , pTWW  , 'pTWW/F')
        self.otree.Branch('HT'    , HT    , 'HT/F')
        self.otree.Branch('redHT' , redHT , 'redHT/F')

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

            pt1 = itree.std_vector_lepton_pt[0]
            pt2 = itree.std_vector_lepton_pt[1]
            phi1 = itree.std_vector_lepton_pt[0]
            phi2 = itree.std_vector_lepton_pt[1]


            met = itree.pfType1Met
            metphi = itree.pfType1Metphi
            #met = itree.pfmet
            #metphi = itree.pfmetphi
            
            if pt2 > 0 :
              WW = ROOT.WW(pt1, pt2, phi1, phi2, met, metphi)
              pTWW[0]   = WW.pTWW()
            else :
              pTWW[0]   = -1
  
            #print "dphill = ", WW.dphill()
            
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
            
            otree.Fill()

        self.disconnect()
        print '- Eventloop completed'
