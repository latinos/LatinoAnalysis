#
#
#     | ___ \   |  / _)        
#     |    ) |  ' /   |  __ \  
#     |   __/   . \   |  |   | 
#    _| _____| _|\_\ _| _|  _| 
#                                                         
#
#


from LatinoAnalysis.Gardener.gardening import TreeCloner
import numpy
import ROOT
import math
import sys
import optparse
import re
import warnings
import os.path
from collections import OrderedDict
from array import array;

class L3KinFiller(TreeCloner):
    def __init__(self):
       pass

    def help(self):
        return '''Calculate kinematic variables, event base and not single object based. They are all simple float variables like mll, dphill, ... '''

    def addOptions(self,parser):
        description = self.help()
        group = optparse.OptionGroup(parser,self.label, description)
        group.add_option('-c', '--cmssw', dest='cmssw', help='cmssw version (naming convention may change)', default='763', type='string')
        parser.add_option_group(group)
        return group

    def checkOptions(self,opts):

        self.cmssw = opts.cmssw
        print " cmssw = ", self.cmssw

                    
    def process(self,**kwargs):
        tree  = kwargs['tree']
        input = kwargs['input']
        output = kwargs['output']

        # does that work so easily and give new variable itree and otree?
        self.connect(tree,input)

        nentries = self.itree.GetEntries()
        print 'Total number of entries: ',nentries 
        savedentries = 0

        #
        # create branches for otree, the ones that will be modified!
        # These variables NEED to be defined as functions in WWWVar.C
        # e.g. mll, dphill, ...
        # if you add a new variable here, be sure it IS defined in WWWVar.C
        #
        self.namesOldBranchesToBeModifiedSimpleVariable = [
           'mllmin3l',
           'zveto_3l',
           'pt1',
           'pt2',
           'pt3',
           'eta1',
           'eta2',
           'eta3',
           'phi1',
           'phi2',
           'phi3',
   #        'channel',
           'drllmin3l',
           'njet_3l',
           'nbjet_3l',
           'chlll',
           'pfmet',
           'mlll',
           'flagOSSF',
	   'mtwww',
	   'mtw1_wh3l',
	   'mtw2_wh3l',
	   'mtw3_wh3l',
	   'minmtw_wh3l',
	   'mindphi_lmet',
	   'dphilllmet',
	   'ptlll',
	   'pTWWW',
           'dphilmet1_wh3l',
           'dphilmet2_wh3l',
           'dphilmet3_wh3l',
           'ptbest',
	   'z4lveto',
	   'dmjjmW',
	   'mtw_notZ',
	   'pdgid_notZ',
	   'dphilmetjj',
	   'dphilmetj',
	   'mTlmetjj',
	   'pTlmetjj',
	   'pTlmetj',
	   'ptz',
	   'checkmZ',
           ]
        
        # clone the tree
        self.clone(output, self.namesOldBranchesToBeModifiedSimpleVariable)

        self.oldBranchesToBeModifiedSimpleVariable = {}
        for bname in self.namesOldBranchesToBeModifiedSimpleVariable:
          bvariable = numpy.ones(1, dtype=numpy.float32)
          self.oldBranchesToBeModifiedSimpleVariable[bname] = bvariable

        # now actually connect the branches
        for bname, bvariable in self.oldBranchesToBeModifiedSimpleVariable.iteritems():
            #print " bname   = ", bname
            #print " bvariable = ", bvariable
            self.otree.Branch(bname,bvariable,bname+'/F')

        # input tree and output tree
        itree     = self.itree
        otree     = self.otree


        # change this part into correct path structure... 
        cmssw_base = os.getenv('CMSSW_BASE')
        try:
            ROOT.gROOT.LoadMacro(cmssw_base+'/src/LatinoAnalysis/Gardener/python/variables/WWWVar.C+g')
        except RuntimeError:
            ROOT.gROOT.LoadMacro(cmssw_base+'/src/LatinoAnalysis/Gardener/python/variables/WWWVar.C++g')


        #----------------------------------------------------------------------------------------------------
        print '- Starting eventloop'
        step = 5000

        #for i in xrange(2000):
        for i in xrange(nentries):

            itree.GetEntry(i)

            if i > 0 and i%step == 0.:
                print i,'events processed :: ', nentries

            WWW = ROOT.WWW()
#            WWW.setLeptons(itree.std_vector_lepton_pt, itree.std_vector_lepton_eta, itree.std_vector_lepton_phi, itree.std_vector_lepton_flavour)
            WWW.setLeptons(itree.std_vector_lepton_pt, itree.std_vector_lepton_eta, itree.std_vector_lepton_phi, itree.std_vector_lepton_ch, itree.std_vector_lepton_flavour)
            WWW.setJets   (itree.std_vector_jet_pt,       itree.std_vector_jet_eta,    itree.std_vector_jet_phi,    itree.std_vector_jet_mass, itree.std_vector_jet_cmvav2)
            
            if self.cmssw == '74x' :

                met = itree.pfType1Met          # formerly pfType1Met
                metphi = itree.pfType1Metphi    # formerly pfType1Metphi
            else : 

                met = itree.metPfType1      
                metphi = itree.metPfType1Phi
                WWW.setTkMET(itree.metTtrk, itree.metTtrkPhi) # before in 74x we were missing this variable  
            WWW.setMET(met, metphi)
 
            WWW.checkIfOk()

 
            # now fill the variables like "mll", "dphill", ...
            for bname, bvariable in self.oldBranchesToBeModifiedSimpleVariable.iteritems():
              bvariable[0] = getattr(WWW, bname)()
              
            otree.Fill()
            savedentries+=1

        self.disconnect()
        print '- Eventloop completed'
        print '   Saved: ', savedentries, ' events'


