#  _____             _____ _                  _             
# |_   _|           /  __ \ |                (_)            
#   | | __ _ _   _  | /  \/ | ___  __ _ _ __  _ _ __   __ _ 
#   | |/ _` | | | | | |   | |/ _ \/ _` | '_ \| | '_ \ / _` |
#   | | (_| | |_| | | \__/\ |  __/ (_| | | | | | | | | (_| |
#   \_/\__,_|\__,_|  \____/_|\___|\__,_|_| |_|_|_| |_|\__, |
#                                                      __/ |
#                                                     |___/ 
# Author:  X. Janssen
# Purpose: Apply Tau ID and clean collection against loose leptons --> also apply SF in veto mode
#          The ID/Iso for tau is hardcoded according to the choice we did for VBS WW 2016 data analysis !!!!

from LatinoAnalysis.Gardener.gardening import TreeCloner
import ROOT
import optparse
import os
import numpy
import math
from collections import OrderedDict

class TauClaning(TreeCloner):

    def __init__(self):
       pass

    def help(self):
       return '''Apply id/iso and filter Tau collection'''

    def addOptions(self,parser):
       description = self.help()
       group = optparse.OptionGroup(parser,self.label, description)
       group.add_option('-c', '--cmssw',   dest='cmssw', help='cmssw version (naming convention may change)', default='Full2016', type='string')
       group.add_option('-d', '--isdata' , dest='isData' , help='True for data' default=False  , action="store_true")

    def checkOptions(self,opts): 
       self.cmssw = opts.cmssw
       print " cmssw = ", self.cmssw
       self.isData = opts.isData
       print " isData= ", self.isData

       # cleaning options
       self.tauCleaning_minpTLep = 10.
       self.tauCleaning_absEta   = 2.3
       self.tauCleaning_dRmax    = 0.3
       self.tauCleaning_dR2max   = self.tauCleaning_dRmax * self.tauCleaning_dRmax

    def changeOrder(self, vectorname, vector, goodtaulist) :
        # vector is already linked to the otree branch
        # vector name is the "name" of that vector to be modified

        #for i in range( len(getattr(self.otree, vectorname)) ) :
          #pass
          #print " --> before ", vectorname, "[", i, "] = ", getattr(self.otree, vectorname)[i]

        # take vector and clone vector
        # equivalent of: temp_vector = itree."vector"
        temp_vector = getattr(self.itree, vectorname)
        # remix the order of vector picking from the clone
        for i in range( len(goodtaulist) ) :
          #print " --> [", i, " :: ", len(goodtaulist) ,"] :::>> ", len(temp_vector), " --> ", goodleptonslist[i]      
          # otree."vectorname"[i] = temp_vector[goodtaulist[i]] <--- that is the "itree" in the correct position
          # setattr(self.otree, vector + "[" + str(i) + "]", temp_vector[ goodtaulist[i] ])
          vector.push_back ( temp_vector[ goodtaulist[i] ] )
          #vector.push_back ( 10000. )
        # set the default value for the remaining
        for i in range( len(temp_vector) - len(goodtaulist) ) :
          vector.push_back ( -9999. )

        #for i in range( len(getattr(self.otree, vectorname)) ) :
          #pass
          #print " --> after[ " , len(goodtaulist), "] ", vectorname, "[", i, "] = ", getattr(self.otree, vectorname)[i]

    def tauIsLepton(self, tauEta, tauPhi, lepEta, lepPhi) :
        #dR = ROOT.TMath.Sqrt( ROOT.TMath.Power(lepEta - tauEta, 2) + ROOT.TMath.Power(ROOT.TMath.Abs(ROOT.TMath.Abs(lepPhi - tauPhi)-ROOT.TMath.Pi())-ROOT.TMath.Pi(), 2) )
        dPhi = ROOT.TMath.Abs(lepPhi - tauPhi)
        if dPhi > ROOT.TMath.Pi() :
          dPhi = 2*ROOT.TMath.Pi() - dPhi
        dR2 = (lepEta - tauEta) * (lepEta - tauEta) + dPhi * dPhi
        if dR2 < self.tauCleaning_dR2max :
            return True
        else:
            return False


    def process(self,**kwargs):

        tree  = kwargs['tree']
        input = kwargs['input']
        output = kwargs['output']

        self.connect(tree,input)

        self.namesNewBranchesVector = []
        self.namesNewBranchesVector.append('std_vector_tau_isTight')
        if not self.isData :
          self.namesNewBranchesVector.append('std_vector_tau_SF')
          self.namesNewBranchesVector.append('std_vector_tau_SF_Up')
          self.namesNewBranchesVector.append('std_vector_tau_SF_Down')

        # Get list of jet and lepton std_vector branches from tree
        self.namesOldBranchesToBeModifiedVector = []
        vectorsToChange = ['std_vector_tau_']
        for b in self.itree.GetListOfBranches():
          branchName = b.GetName()
          for subString in vectorsToChange:
            if subString in branchName and not 'std_vector_tau_SF' in branchName: 
               self.namesOldBranchesToBeModifiedVector.append(branchName)

        # NOW WE CAN CLONE THE TREE
        self.clone(output,self.namesNewBranchesVector+self.namesOldBranchesToBeModifiedVector)

        # NOW CONNECT ALL NEW/TO BE MODIFIED BRANCEHES 

        # ... New Branches: tau Tags 
        self.newBranchesVector = {}
        for bname in self.namesNewBranchesVector:
          bvector =  ROOT.std.vector(float) ()
          self.newBranchesVector[bname] = bvector
        for bname, bvector in self.newBranchesVector.iteritems(): self.otree.Branch(bname,bvector)
 
        # ... Old Branches: std_vector_tau_
        self.oldBranchesToBeModifiedVector = {}
        for bname in self.namesOldBranchesToBeModifiedVector:
          bvector =  ROOT.std.vector(float) ()
          self.oldBranchesToBeModifiedVector[bname] = bvector
        for bname, bvector in self.oldBranchesToBeModifiedVector.iteritems(): self.otree.Branch(bname,bvector)

        # input tree and output tree
        itree     = self.itree
        otree     = self.otree

        # Loop
        nentries = self.itree.GetEntries()
        print 'Total number of entries: ',nentries
        savedentries = 0

        #----------------------------------------------------------------------------------------------------
        print '- Starting eventloop'
        step = 5000

        for i in xrange(nentries):

            itree.GetEntry(i)

            if i > 0 and i%step == 0.:
                print i,'events processed :: ', nentries


            # Cleaning against Loose leptons (electron/muon)
            goodTaus = []
            tightTag = []
            for iTau in xrange(len(itree.std_vector_tau_pt)) :
               isLepton = False;
               if abs(itree.std_vector_tau_eta[iJet]) <= self.tauCleaning_absEta :
                 for iLep in xrange(len(itree.std_vector_lepton_pt)) :
                   if itree.std_vector_lepton_pt[iLep] < self.tauCleaning_minpTLep:
                     break;
                   if self.tauIsLepton(itree.std_vector_tau_eta[iTau],itree.std_vector_tau_phi[iTau],itree.std_vector_lepton_eta[iLep],itree.std_vector_lepton_phi[iLep]) :
                     isLepton = True
                 if not isLepton: 
                   goodTaus.append(iTau)
                   if itree.std_vector_tau_looseIso_dbeta[iTau]>0 : tightTag.append(1.)
                   else:                                            tightTag.append(0.)

            for bname, bvector in self.oldBranchesToBeModifiedVector.iteritems():
                self.changeOrder( bname, bvector, goodTaus )

            # Save default tight Tag 
            maxNumTau = 10
            for iTau in range(len(tightTag)) :
              for bname, bvector in self.newBranchesVector.iteritems() :
                if ("std_vector_tau_isTight" == bname) : bvector.push_back(tightTag[iTau])
            for remainingTau in range( maxNumTau - len(otree.std_vector_tau_isTight) ) : 
              for bname, bvector in self.newBranchesVector.iteritems() :
                if ("std_vector_tau_isTight" == bname) : bvector.push_back(0.)

            # Add SF (kill Tau) --> rejection of 5% +- 5% of tau
            if not self.isData :
              for iTau in xrange(len(itree.std_vector_tau_pt)) :
                rnd =  ROOT.gRandom.Rndm()
                for bname, bvector in self.newBranchesVector.iteritems() :
                  if ("std_vector_tau_SF_Up" == bname) : bvector.push_back(1.) 
                  if ("std_vector_tau_SF" == bname) :
                    if rnd > 0.95 : bvector.push_back(0.)
                    else          : bvector.push_back(1.)
                  if ("std_vector_tau_SF_Down" == bname) :
                    if rnd > 0.90 : bvector.push_back(0.)
                    else          : bvector.push_back(1.)

            # Save Events
            savedentries+=1
            otree.Fill()

        self.disconnect()
        print '- Eventloop completed'
        print '   Saved: ', savedentries, ' events'

