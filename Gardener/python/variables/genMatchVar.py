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
#          ___|                                     |          |     _)               
#         |       _ \  __ \       __ `__ \    _` |  __|   __|  __ \   |  __ \    _` | 
#         |   |   __/  |   |      |   |   |  (   |  |    (     | | |  |  |   |  (   | 
#        \____| \___| _|  _|     _|  _|  _| \__,_| \__| \___| _| |_| _| _|  _| \__, | 
#                                                                              |___/  
#

class GenMatchVarFiller(TreeCloner):

    def __init__(self):
        pass


    def isAcloseToB(self, a_Eta, a_Phi, b_Eta, b_Phi, drmax) :
        dPhi = ROOT.TMath.Abs(b_Phi - a_Phi)
        if dPhi > ROOT.TMath.Pi() :
          dPhi = 2*ROOT.TMath.Pi() - dPhi
        dR2 = (b_Eta - a_Eta) * (b_Eta - a_Eta) + dPhi * dPhi
        #print ">> dR = ", math.sqrt(dR2), " :: ", dPhi, " (+) ", (b_Eta - a_Eta) 
        if dR2 < (drmax*drmax):
            return True
        else:
            return False


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

        tree  = kwargs['tree']
        input = kwargs['input']
        output = kwargs['output']

        self.connect(tree,input)

        self.namesOldBranchesToBeModifiedVector = ['std_vector_lepton_genmatched']

        # clone the tree
        self.clone(output,self.namesOldBranchesToBeModifiedVector)

        self.oldBranchesToBeModifiedVector = {}
        for bname in self.namesOldBranchesToBeModifiedVector:
          bvector =  ROOT.std.vector(float) ()
          self.oldBranchesToBeModifiedVector[bname] = bvector

        # now actually connect the branches
        for bname, bvector in self.oldBranchesToBeModifiedVector.iteritems():
            self.otree.Branch(bname,bvector)


        nentries = self.itree.GetEntries()
        print 'Total number of entries: ',nentries 

        # avoid dots to go faster
        itree     = self.itree
        otree     = self.otree

        savedentries = 0

        print '- Starting eventloop'
        step = 5000
        #for i in xrange(1000):
        for i in xrange(nentries):
            itree.GetEntry(i)

            ## print event count
            if i > 0 and i%step == 0.:
                print i,'events processed.'

            for bname, bvector in self.oldBranchesToBeModifiedVector.iteritems():
                bvector.clear()
            
            for iLep in xrange(len(itree.std_vector_lepton_pt)) :

              # default is not matched            
              isLeptonMatched = 0

              # check if the lepton is modified              
              if hasattr(itree, 'std_vector_leptonGen_pt') :
                for iGenLep in xrange(len(itree.std_vector_leptonGen_pt)) :
                  # if there is a gen lepton with pt>0 and status 1
                  if self.itree.std_vector_leptonGen_pt[iGenLep] > 0 \
                     and  self.itree.std_vector_leptonGen_status[iGenLep] == 1 \
                     and  (abs(self.itree.std_vector_leptonGen_pid[iGenLep]) == 11 or abs(self.itree.std_vector_leptonGen_pid[iGenLep]) == 13)   : 
                    # and if the reco lepton is close to this gen lepton
                    if self.isAcloseToB(self.itree.std_vector_lepton_eta[iLep],    self.itree.std_vector_lepton_phi[iLep],
                                        self.itree.std_vector_leptonGen_eta[iGenLep], self.itree.std_vector_leptonGen_phi[iGenLep],
                                        0.3) :
                      isLeptonMatched = 1
              
              # now save the variable
              for bname, bvector in self.oldBranchesToBeModifiedVector.iteritems():
                bvector.push_back ( isLeptonMatched )
                #print " itree.std_vector_lepton_pt[", iLep, "] = ", itree.std_vector_lepton_pt[iLep], "  --> ", isLeptonMatched
          
          
              
            otree.Fill()
            savedentries+=1
            
        self.disconnect()
        print '- Eventloop completed'
        print '   Saved: ', savedentries, ' events'
        print '   Total: ', nentries 


