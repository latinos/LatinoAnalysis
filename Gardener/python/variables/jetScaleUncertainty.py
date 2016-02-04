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

class JESTreeMaker(TreeCloner):
    def __init__(self):
       pass

    def help(self):
        return '''Apply id/iso and filter lepton collection'''

    def addOptions(self,parser):
        description = self.help()
        group = optparse.OptionGroup(parser,self.label, description)
        group.add_option('-k', '--kind',   dest='kind', help='Kind of variation: -1, +1, +0.5, ...', default=1.0)
        parser.add_option_group(group)
        return group

    def checkOptions(self,opts):
        if not (hasattr(opts,'kind')):
          self.kind = 1.0
        else :    
          self.kind   = 1.0 * float(opts.kind)
        print " kind of variation = ", self.kind

    def changeOrder(self, vectorname, vector, jetOrderList) :
        # take vector and clone vector
        # equivalent of: temp_vector = itree."vector"
        temp_vector = getattr(self.itree, vectorname)
        # remix the order of vector picking from the clone
        for i in range( len(jetOrderList) ) :
          vector.push_back ( temp_vector[ jetOrderList[i] ] )
        # set the default value for the remaining
        for i in range( len(temp_vector) - len(jetOrderList) ) :
          vector.push_back ( -9999. )
          


    def process(self,**kwargs):
        tree  = kwargs['tree']
        input = kwargs['input']
        output = kwargs['output']

        self.connect(tree,input)

        nentries = self.itree.GetEntries()
        print 'Total number of entries: ',nentries 

        #
        # create branches for otree, the ones that will be modified!
        # see: https://root.cern.ch/phpBB3/viewtopic.php?t=12507
        # this is the list of variables to be modified
        #
	self.namesOldBranchesToBeModifiedVector = []
	vectorsToChange = ['std_vector_jet_']
        for b in self.itree.GetListOfBranches():
	    branchName = b.GetName()
	    for subString in vectorsToChange:
		if subString in branchName:
		    self.namesOldBranchesToBeModifiedVector.append(branchName)

        # clone the tree
        self.clone(output,self.namesOldBranchesToBeModifiedVector)

        self.oldBranchesToBeModifiedVector = {}
        for bname in self.namesOldBranchesToBeModifiedVector:
          bvector =  ROOT.std.vector(float) ()
          self.oldBranchesToBeModifiedVector[bname] = bvector

        # now actually connect the branches
        for bname, bvector in self.oldBranchesToBeModifiedVector.iteritems():
            self.otree.Branch(bname,bvector)
        
        # input tree  
        itree = self.itree

        # change this part into correct path structure... 
        cmssw_base = os.getenv('CMSSW_BASE')
        try:
            ROOT.gROOT.LoadMacro(cmssw_base+'/src/LatinoAnalysis/Gardener/python/variables/WWVar.C+g')

        except RuntimeError:
            ROOT.gROOT.LoadMacro(cmssw_base+'/src/LatinoAnalysis/Gardener/python/variables/WWVar.C++g')

        # Load jes uncertainty
        jecUnc = ROOT.JetCorrectionUncertainty(os.path.expandvars("${CMSSW_BASE}/src/LatinoAnalysis/Gardener/input/Summer15_25nsV6_MC_Uncertainty_AK4PFchs.txt"))
        #----------------------------------------------------------------------------------------------------
        print '- Starting eventloop'
        step = 5000

        for i in xrange(nentries):
            itree.GetEntry(i)

            if i > 0 and i%step == 0.:
              print i,'events processed :: ', nentries
                
            # scale jet pt
            jetPtUp = []
            
            for i in range(itree.std_vector_jet_pt.size()):
                if itree.std_vector_jet_pt[i] > 0:
                    jecUnc.setJetEta(itree.std_vector_jet_eta[i])
                    jecUnc.setJetPt(itree.std_vector_jet_pt[i])
                    jetPtUp.append(itree.std_vector_jet_pt[i]*(1 + (self.kind) * (jecUnc.getUncertainty(True))))
                else:
                    break
                
            jetOrderUp = sorted(range(len(jetPtUp)), key=lambda k: jetPtUp[k], reverse=True)
                           
            for bname, bvector in self.oldBranchesToBeModifiedVector.iteritems():
                bvector.clear()
                if 'jet_pt' in bname:
                    for i in range( len(jetOrderUp) ) :
                        bvector.push_back ( jetPtUp[jetOrderUp[i]] )
                    for i in range( len(getattr(self.itree, bname)) - len(jetOrderUp) ) :
                        bvector.push_back ( -9999. )
                else:
                    self.changeOrder( bname, bvector, jetOrderUp)

            self.otree.Fill()

        self.disconnect(True,True)
        
        print '- Eventloop completed'

