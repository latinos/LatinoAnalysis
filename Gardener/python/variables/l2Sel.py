#
#
#      |     ___ \  
#      |        ) | 
#      |       __/  
#     _____| _____| 
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

class L2SelFiller(TreeCloner):
    def __init__(self):
       pass

    def help(self):
        return '''Apply id/iso and filter lepton collection'''

    def addOptions(self,parser):
        pass

    def checkOptions(self,opts):
        pass

    def changeOrder(self, vectorname, vector, goodleptonslist) :
        # vector is already linked to the otree branch
        # vector name is the "name" of that vector to be modified
        
        #for i in range( len(getattr(self.otree, vectorname)) ) :
          #pass
          #print " --> before ", vectorname, "[", i, "] = ", getattr(self.otree, vectorname)[i]

        # take vector and clone vector
        # equivalent of: temp_vector = itree."vector"
        temp_vector = getattr(self.itree, vectorname)
        # remix the order of vector picking from the clone
        for i in range( len(goodleptonslist) ) :
          #print " --> [", i, " :: ", len(goodleptonslist) ,"] :::>> ", len(temp_vector), " --> ", goodleptonslist[i]      
          # otree."vectorname"[i] = temp_vector[goodleptonslist[i]] <--- that is the "itree" in the correct position
          # setattr(self.otree, vector + "[" + str(i) + "]", temp_vector[ goodleptonslist[i] ])
          vector.push_back ( temp_vector[ goodleptonslist[i] ] )
          #vector.push_back ( 10000. )
        # set the default value for the remaining
        for i in range( len(temp_vector) - len(goodleptonslist) ) :
          vector.push_back ( -9999. )
          
        #for i in range( len(getattr(self.otree, vectorname)) ) :
          #pass
          #print " --> after[ " , len(goodleptonslist), "] ", vectorname, "[", i, "] = ", getattr(self.otree, vectorname)[i]
        
    def jetIsLepton(self, jetEta, jetPhi, lepEta, lepPhi) :
        dR = ROOT.TMath.Sqrt( ROOT.TMath.Power(lepEta - jetEta, 2) + ROOT.TMath.Power(ROOT.TMath.Abs(ROOT.TMath.Abs(lepPhi - jetPhi)-ROOT.TMath.Pi())-ROOT.TMath.Pi(), 2) )
        if dR < 0.3:
            return True
        else:
            return False
                    
    def process(self,**kwargs):
        tree  = kwargs['tree']
        input = kwargs['input']
        output = kwargs['output']

        # does that work so easily and give new variable itree and otree?
        self.connect(tree,input)

        nentries = self.itree.GetEntries()
        print 'Total number of entries: ',nentries 


        # create branches for otree, the ones that will be modified!
        # see: https://root.cern.ch/phpBB3/viewtopic.php?t=12507
        
        self.namesOldBranchesToBeModifiedVector = [
            'std_vector_lepton_BestTrackdxy',
            'std_vector_lepton_BestTrackdz',
            'std_vector_lepton_Chi2LocalPos',
            'std_vector_lepton_NTkLayers',
            'std_vector_lepton_NValidFractInTrk',
            'std_vector_lepton_NValidHitsInTrk',
            'std_vector_lepton_NValidHitsSATrk',
            'std_vector_lepton_NValidPixelHitsInTrk',
            'std_vector_lepton_NormChi2GTrk',
            'std_vector_lepton_NumOfMatchedStations',
            'std_vector_lepton_SegCompatibilty',
            'std_vector_lepton_TrkKink',
            'std_vector_lepton_chargedHadronIso',
            'std_vector_lepton_chargedParticleIso',
            'std_vector_lepton_closejet_PartonFlavour',
            'std_vector_lepton_closejet_drlj',
            'std_vector_lepton_closejet_eta',
            'std_vector_lepton_closejet_phi',
            'std_vector_lepton_closejet_pt',
            'std_vector_lepton_eleIdLoose',
            'std_vector_lepton_eleIdMedium',
            'std_vector_lepton_eleIdTight',
            'std_vector_lepton_eleIdVeto',
            'std_vector_lepton_neutralHadronIso',
            'std_vector_lepton_photonIso',
            'std_vector_lepton_sumPUPt',
            'std_vector_lepton_pt',
            'std_vector_lepton_ch',
            'std_vector_lepton_flavour',
            'std_vector_lepton_eta',
            'std_vector_lepton_isMediumMuon',
            'std_vector_lepton_elSIP3D',
            'std_vector_lepton_isTightMuon',
            'std_vector_lepton_muSIP3D',
            'std_vector_lepton_phi',
            
            'std_vector_jet_NumberSoftMu',
            'std_vector_jet_bjpb',
            'std_vector_jet_cmva',
            'std_vector_jet_csvv2ivf',
            'std_vector_jet_mass',
            'std_vector_jet_pfcsv',
            'std_vector_jet_softMuEta',
            'std_vector_jet_softMuIso',
            'std_vector_jet_softMuPhi',
            'std_vector_jet_softMuPt',
            'std_vector_jet_ssvhb',
            'std_vector_jet_ssvhe',
            'std_vector_jet_tche',
            'std_vector_jet_tchp',
            'std_vector_jet_eta',
            'std_vector_jet_QGRmax',
            'std_vector_jet_puid',
            'std_vector_jet_pt',
            'std_vector_jet_phi',
            'std_vector_jet_QGlikelihood',            
            'std_vector_jet_QGaxis2',
            #'std_vector_jet_HadronFlavour',            
            'std_vector_jet_QGaxis1',
            'std_vector_jet_QGRMScand',
            #'std_vector_jet_PartonFlavour',
            
            'std_vector_puppijet_eta',
            'std_vector_puppijet_phi',
            'std_vector_puppijet_pt'
           ]
        
        self.namesOldBranchesToBeModifiedSimpleVariable = [
           'mll',
           'dphill',
           'yll',
           'ptll',
           'pt1',
           'pt2',
           'mth',
           
           'mjj',
           'detajj'
           ]
        
        self.jetVariables = [
            'pt',
            'eta',
            'phi',
            'mass',
            #'mva',
            #'id',
            'tche'       
            # NChgQC, ChgptCut1, NHM, NNeutralptCut, PhM, bjpb, ... ?
            # jetRho ?
            ]
        
        self.jetVarList = []
        self.jetVarBranch = []
        njets = 7
        for jetVar in self.jetVariables:
            self.jetVarBranch.append("std_vector_jet_"+jetVar)
            for i in xrange(njets):
                self.jetVarList.append("jet"+jetVar+str(i+1))

        self.clone(output,self.namesOldBranchesToBeModifiedVector + self.namesOldBranchesToBeModifiedSimpleVariable + self.jetVarList)

        self.oldBranchesToBeModifiedVector = {}
        for bname in self.namesOldBranchesToBeModifiedVector:
          bvector =  ROOT.std.vector(float) ()
          self.oldBranchesToBeModifiedVector[bname] = bvector

        # now actually connect the branches
        for bname, bvector in self.oldBranchesToBeModifiedVector.iteritems():
            print " bname   = ", bname
            print " bvector = ", bvector
            self.otree.Branch(bname,bvector)


        self.oldBranchesToBeModifiedSimpleVariable = {}
        for bname in self.namesOldBranchesToBeModifiedSimpleVariable:
          bvariable = numpy.ones(1, dtype=numpy.float32)
          self.oldBranchesToBeModifiedSimpleVariable[bname] = bvariable

        # now actually connect the branches
        for bname, bvariable in self.oldBranchesToBeModifiedSimpleVariable.iteritems():
            #print " bname   = ", bname
            #print " bvariable = ", bvariable
            self.otree.Branch(bname,bvariable,bname+'/F')

        self.jetVarDic = OrderedDict()
        for bname in self.jetVarList:
          bvariable = numpy.ones(1, dtype=numpy.float32)
          self.jetVarDic[bname] = bvariable

        # now actually connect the branches
        for bname, bvariable in self.jetVarDic.iteritems():
            #print " bname   = ", bname
            #print " bvariable = ", bvariable
            self.otree.Branch(bname,bvariable,bname+'/F')

        # input tree and output tree
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


        #for i in xrange(10000):
        for i in xrange(nentries):

            itree.GetEntry(i)

            if i > 0 and i%step == 0.:
                print i,'events processed :: ', nentries

            # apply lepton id and isolation
            # and filter out unwanted leptons
            # putting pt of those leptons to -10 GeV

            goodLeps = []
            goodLep1 = -1
            goodLep2 = -1
            
            for iLep in xrange(len(itree.std_vector_lepton_pt)) :
              isGoodLepton = False
              # id definition
              if ( itree.std_vector_lepton_eleIdMedium[iLep] == 1
                   and abs(itree.std_vector_lepton_flavour[iLep]) == 11 
                  ) :
                isGoodLepton = True

              if ( itree.std_vector_lepton_isMediumMuon[iLep] == 1 
                   and (itree.std_vector_lepton_chargedHadronIso[iLep] + 
                        itree.std_vector_lepton_neutralHadronIso[iLep] + 
                        itree.std_vector_lepton_photonIso[iLep]
                        ) / itree.std_vector_lepton_pt[iLep] < 0.20 
                   and abs(itree.std_vector_lepton_flavour[iLep]) == 13 
                  ) :
                isGoodLepton = True
              
              if isGoodLepton :
                if goodLep1 < 0: 
                  goodLep1 = iLep
                elif goodLep2 < 0 :
                  goodLep2 = iLep
                goodLeps.append(iLep)
            
            
            #print " goodLep1 = ", goodLep1, 
            #print " goodLep2 = ", goodLep2
            
            # require at least 2 good leptons
            if goodLep1 >= 0 and goodLep2 >= 0 :
            
              # now filter the leptons list
              # [ x, - , - , x , x , x , - , - ]
              # [ x  x   x   x   -   -   -   - ]
              for bname, bvector in self.oldBranchesToBeModifiedVector.iteritems():  # really necessary?
                bvector.clear()
             
              for bname, bvector in self.oldBranchesToBeModifiedVector.iteritems():
                 if "lepton" in bname:
                     self.changeOrder( bname, bvector, goodLeps)
                
              # clean jets
              goodJets = []
              for iJet in xrange(len(itree.std_vector_jet_pt)) :
                  isLepton = False;
                  for iLep in xrange(len(goodLeps)) :
                      if self.jetIsLepton(itree.std_vector_jet_eta[iJet],itree.std_vector_jet_phi[iJet],itree.std_vector_lepton_eta[iLep],itree.std_vector_lepton_phi[iLep]) :
                          isLepton = True;
                  if not isLepton:
                      goodJets.append(iJet)
              
              goodPuppiJets = []
              for iJet in xrange(len(itree.std_vector_puppijet_pt)) :
                  isLepton = False;
                  for iLep in xrange(len(goodLeps)) :
                      if self.jetIsLepton(itree.std_vector_puppijet_eta[iJet],itree.std_vector_puppijet_phi[iJet],itree.std_vector_lepton_eta[iLep],itree.std_vector_lepton_phi[iLep]) :
                          isLepton = True;
                  if not isLepton:
                      goodPuppiJets.append(iJet)
                          
              for bname, bvector in self.oldBranchesToBeModifiedVector.iteritems():
                   if "jet" in bname and not "lepton" in bname:
                       if "puppi" in bname:
                           self.changeOrder( bname, bvector, goodPuppiJets)
                       else:
                           self.changeOrder( bname, bvector, goodJets)
                           
              #print "goodJets: ", goodJets
              #print "goodPuppiJets: ", goodPuppiJets

              pt1 = itree.std_vector_lepton_pt[goodLep1]
              pt2 = itree.std_vector_lepton_pt[goodLep2]
              eta1 = itree.std_vector_lepton_eta[goodLep1]
              eta2 = itree.std_vector_lepton_eta[goodLep2]             
              phi1 = itree.std_vector_lepton_phi[goodLep1]
              phi2 = itree.std_vector_lepton_phi[goodLep2]
              met = itree.pfType1Met
              metphi = itree.pfType1Metphi
              jetpt1 = itree.std_vector_jet_pt[goodJets[0]]
              jetpt2 = itree.std_vector_jet_pt[goodJets[1]]
              jeteta1 = itree.std_vector_jet_eta[goodJets[0]]
              jeteta2 = itree.std_vector_jet_eta[goodJets[1]]
              jetphi1 = itree.std_vector_jet_phi[goodJets[0]]
              jetphi2 = itree.std_vector_jet_phi[goodJets[1]]
              jetmass1 = itree.std_vector_jet_mass[goodJets[0]]
              jetmass2 = itree.std_vector_jet_mass[goodJets[1]]
             
              #WW = ROOT.WW(pt1, pt2, eta1, eta2, phi1, phi2, met, metphi)
              WW = ROOT.WW(pt1, pt2, eta1, eta2, phi1, phi2, met, metphi, jetpt1, jetpt2, jeteta1, jeteta2, jetphi1, jetphi2, jetmass1, jetmass2)
                          
              for bname, bvariable in self.oldBranchesToBeModifiedSimpleVariable.iteritems():
                bvariable[0] = getattr(WW, bname)()
                
              # refill jet variables
              counter = 0
              varCounter = 0
              for bname, bvariable in self.jetVarDic.iteritems():
                  bvariable[0] = (getattr(self.otree, self.jetVarBranch[varCounter]))[counter]
                  counter += 1
                  if counter == 8:
                      varCounter += 1
                      counter = 0
                 

              otree.Fill()

        self.disconnect()
        print '- Eventloop completed'
