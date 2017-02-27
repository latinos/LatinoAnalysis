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
        group.add_option('-m', '--maxUncertainty',   dest='maxUncertainty', help='Use maximum of JES uncertainties', default=False, action="store_true")
        group.add_option('-c', '--cmssw', dest='cmssw', help='cmssw version (naming convention may change)', default='763', type='string')
        parser.add_option_group(group)
        return group

    def checkOptions(self,opts):
        if not (hasattr(opts,'kind')):
            self.kind = 1.0
        else :    
            self.kind   = 1.0 * float(opts.kind)
        print " kind of variation = ", self.kind

        self.maxUncertainty = opts.maxUncertainty
        print " Using maximum of JES uncertainties = ", self.maxUncertainty

        self.cmssw = opts.cmssw
        print " cmssw = ", self.cmssw

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
        if self.cmssw == 'Full2016':
            jecUnc = ROOT.JetCorrectionUncertainty(os.path.expandvars("${CMSSW_BASE}/src/LatinoAnalysis/Gardener/input/Summer16_23Sep2016V4_MC_Uncertainty_AK4PFchs.txt"))
        if self.cmssw == 'ICHEP2016':
            jecUncSpring16V1 = ROOT.JetCorrectionUncertainty(os.path.expandvars("${CMSSW_BASE}/src/LatinoAnalysis/Gardener/input/Spring16_25nsV1_MC_Uncertainty_AK4PFchs.txt"))
            jecUncSpring16V6 = ROOT.JetCorrectionUncertainty(os.path.expandvars("${CMSSW_BASE}/src/LatinoAnalysis/Gardener/input/Spring16_25nsV6_MC_Uncertainty_AK4PFchs.txt"))
        else:
            jecUncFall15 = ROOT.JetCorrectionUncertainty(os.path.expandvars("${CMSSW_BASE}/src/LatinoAnalysis/Gardener/input/Fall15_25nsV2_MC_Uncertainty_AK4PFchs.txt"))
            jecUncSummer15 = ROOT.JetCorrectionUncertainty(os.path.expandvars("${CMSSW_BASE}/src/LatinoAnalysis/Gardener/input/Summer15_25nsV6_MC_Uncertainty_AK4PFchs.txt"))

        #----------------------------------------------------------------------------------------------------
        print '- Starting eventloop'
        step = 5000

        for i in xrange(nentries):
            itree.GetEntry(i)

            if i > 0 and i%step == 0.:
                print i,'events processed :: ', nentries
                
            # scale jet 4-vector
            jetPtUp = []
            jetMassUp = []
            
            for i in range(itree.std_vector_jet_pt.size()):
                if itree.std_vector_jet_pt[i] > 0:
                    if self.cmssw == 'Full2016':
                        jecUnc.setJetEta(itree.std_vector_jet_eta[i])
                        jecUnc.setJetPt(itree.std_vector_jet_pt[i])
                        unc = jecUnc.getUncertainty(True)
                    if self.cmssw == 'ICHEP2016':
                        jecUncSpring16V1.setJetEta(itree.std_vector_jet_eta[i])
                        jecUncSpring16V1.setJetPt(itree.std_vector_jet_pt[i])
                        unc = jecUncSpring16V1.getUncertainty(True)

                        if self.maxUncertainty:
                            jecUncSpring16V6.setJetEta(itree.std_vector_jet_eta[i])
                            jecUncSpring16V6.setJetPt(itree.std_vector_jet_pt[i])
                            unc = max(unc,jecUncSpring16V6.getUncertainty(True))

                            if abs(itree.std_vector_jet_eta[i]) > 2.5:
                                if itree.std_vector_jet_pt[i] > 150:
                                    unc *= 2
                                elif itree.std_vector_jet_pt[i] > 50:
                                    unc *= 1 + (itree.std_vector_jet_pt[i] - 50 ) / 100.
                    else:
                        jecUncSummer15.setJetEta(itree.std_vector_jet_eta[i])
                        jecUncSummer15.setJetPt(itree.std_vector_jet_pt[i])
                        unc = jecUncSummer15.getUncertainty(True)

                        if self.maxUncertainty:
                            jecUncFall15.setJetEta(itree.std_vector_jet_eta[i])
                            jecUncFall15.setJetPt(itree.std_vector_jet_pt[i])
                            unc = max(unc,jecUncFall15.getUncertainty(True))

                    jetPtUp.append(itree.std_vector_jet_pt[i]*(1 + (self.kind) * unc))
                    jetMassUp.append(itree.std_vector_jet_mass[i]*(1 + (self.kind) * unc))
                else:
                    break
                
            jetOrderUp = sorted(range(len(jetPtUp)), key=lambda k: jetPtUp[k], reverse=True)
                        
            for bname, bvector in self.oldBranchesToBeModifiedVector.iteritems():
                bvector.clear()
                if bname == 'std_vector_jet_pt' :
                    for i in range( len(jetOrderUp) ) :
                        bvector.push_back ( jetPtUp[jetOrderUp[i]] )
                    for i in range( len(getattr(self.itree, bname)) - len(jetOrderUp) ) :
                        bvector.push_back ( -9999. )
                elif bname == 'std_vector_jet_mass' :
                    for i in range( len(jetOrderUp) ) :
                        bvector.push_back ( jetMassUp[jetOrderUp[i]] )
                    for i in range( len(getattr(self.itree, bname)) - len(jetOrderUp) ) :
                        bvector.push_back ( -9999. )
                else:
                    self.changeOrder( bname, bvector, jetOrderUp)

            self.otree.Fill()

        self.disconnect(True,True)
        
        print '- Eventloop completed'

