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
        description = self.help()
        group = optparse.OptionGroup(parser,self.label, description)
        group.add_option('-k', '--kind',  dest='kind',  help='Kind of lepton identification to be applied',  default='1')
        group.add_option('-c', '--cmssw', dest='cmssw', help='cmssw version (naming convention may change)', default='764')
        parser.add_option_group(group)
        return group

    def checkOptions(self,opts):
        if not (hasattr(opts,'kind')):
          self.kind = 1
        else :    
          self.kind   = 1.0 * float(opts.kind)
        print " kind of electron id = ", self.kind

        self.cmssw = opts.cmssw
        print " cmssw = ", self.cmssw

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
        #dR = ROOT.TMath.Sqrt( ROOT.TMath.Power(lepEta - jetEta, 2) + ROOT.TMath.Power(ROOT.TMath.Abs(ROOT.TMath.Abs(lepPhi - jetPhi)-ROOT.TMath.Pi())-ROOT.TMath.Pi(), 2) )
        dPhi = ROOT.TMath.Abs(lepPhi - jetPhi)
        if dPhi > ROOT.TMath.Pi() :
          dPhi = 2*ROOT.TMath.Pi() - dPhi
        dR2 = (lepEta - jetEta) * (lepEta - jetEta) + dPhi * dPhi
        if dR2 < (0.3*0.3):
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
        savedentries = 0

        #
        # create branches for otree, the ones that will be modified!
        # see: https://root.cern.ch/phpBB3/viewtopic.php?t=12507
        # this is the list of variables to be modified
        # either because leptons are filtered by id/iso, 
        # or because jets are filtered because they are actually leptons
        #
        self.namesOldBranchesToBeModifiedVector = []
	vectorsToChange = ['std_vector_lepton_','std_vector_electron_','std_vector_muon_','std_vector_jet_','std_vector_puppijet_']
        for b in self.itree.GetListOfBranches():
	    branchName = b.GetName()
	    for subString in vectorsToChange:
		if subString in branchName:
		    self.namesOldBranchesToBeModifiedVector.append(branchName)
        
        # and these variables NEED to be defined as functions in WWVar.C
        # e.g. mll, dphill, ...
        self.namesOldBranchesToBeModifiedSimpleVariable = [
           'mll',
           'dphill',
           'yll',
           'ptll',
           'pt1',
           'pt2',
           'mth',
           'mcoll',
           'channel',
           #'pfmet',
           'projpfmet',

           'drll',
           'dphilljet',
           'dphilljetjet',
           'dphilmet',
           'dphilmet1',
           'dphilmet2',
           'mtw1',
           'mtw2',
           
           'mjj',
           'detajj',
           'njet',
           
           'mllThird'
           
           ]
        
        # jet variables with the structure "std_vector_jet_"NAME to be migrated to "jet"NAME"+number.
        # e.g. jetpt1, jeteta1, jetpt2, jeteta2, ...
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
        # maximum number of "single jet" variables to be saved
        maxnjets = 2 # 7 --> everything is available in form of std::vector -> these will be deprecated
        for jetVar in self.jetVariables:
          for i in xrange(maxnjets):
            self.jetVarList.append("jet"+jetVar+str(i+1))

        # clone the tree
        self.clone(output,self.namesOldBranchesToBeModifiedVector + self.namesOldBranchesToBeModifiedSimpleVariable + self.jetVarList)

        self.oldBranchesToBeModifiedVector = {}
        for bname in self.namesOldBranchesToBeModifiedVector:
          bvector =  ROOT.std.vector(float) ()
          self.oldBranchesToBeModifiedVector[bname] = bvector

        # now actually connect the branches
        for bname, bvector in self.oldBranchesToBeModifiedVector.iteritems():
            #print " bname   = ", bname
            #print " bvector = ", bvector
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

	# keep loose leptons: copy in toto the list of leptons and variables
	#                     and change the name adding "loose" in it
	self.looseLeptonVector = {}
	looseLeptonCollections = ['std_vector_lepton_pt','std_vector_lepton_eta','std_vector_lepton_phi','std_vector_lepton_flavour']
	for bname in looseLeptonCollections:
	  if bname in self.itree.GetListOfBranches():
	    bvector =  ROOT.std.vector(float) ()
            self.looseLeptonVector[bname] = bvector
            self.otree.Branch(bname.replace('lepton','looseLepton'), bvector)

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

        # to be used later on in the code ...
        new_std_vector_jet_pt  = ROOT.std.vector(float) ()
        new_std_vector_jet_eta = ROOT.std.vector(float) ()

        new_std_vector_lepton_pt      = ROOT.std.vector(float) ()
        new_std_vector_lepton_eta     = ROOT.std.vector(float) ()
        new_std_vector_lepton_phi     = ROOT.std.vector(float) ()
        new_std_vector_lepton_flavour = ROOT.std.vector(float) ()

        #for i in xrange(2000):
        for i in xrange(nentries):

            itree.GetEntry(i)

            if i > 0 and i%step == 0.:
                print i,'events processed :: ', nentries

            # apply lepton id and isolation
            # and filter out unwanted leptons
            # putting pt of those leptons to -9999 GeV
            # and all other variables too set to the default -9999

            goodLeps = []
            goodLep1 = -1
            goodLep2 = -1
                        
            for iLep in xrange(len(itree.std_vector_lepton_pt)) :
              isGoodLepton = False
              
              #
              # analysis lepton definition
              #
              if self.kind == 1 :
               
                ###########
                # electron
                
                # id definition
                if ( itree.std_vector_lepton_eleIdTight[iLep] == 1
                     and abs(itree.std_vector_lepton_flavour[iLep]) == 11 
                    ) :
                  isGoodLepton = True
               
                ###########
                # muon
                dxy = float(0.01)
                if (itree.std_vector_lepton_pt[iLep] > 20):
                    dxy = float(0.02)
               
                muonIso = float(0.0)
               
                if ( (itree.std_vector_lepton_photonIso[iLep] +
                     itree.std_vector_lepton_neutralHadronIso[iLep] -
                     0.5 * itree.std_vector_lepton_sumPUPt[iLep]) > 0
                     ) :
                    muonIso = (itree.std_vector_lepton_photonIso[iLep] +
                               itree.std_vector_lepton_neutralHadronIso[iLep] -
                               0.5 * itree.std_vector_lepton_sumPUPt[iLep])
                else:
                    muonIso = 0
               
                if self.cmssw == '763' :
                  if ( itree.std_vector_lepton_isMediumMuon[iLep] == 1 
                     and (itree.std_vector_lepton_chargedHadronIso[iLep] + muonIso) / itree.std_vector_lepton_pt[iLep] < 0.15
                     and abs(itree.std_vector_lepton_flavour[iLep]) == 13
                     and abs(itree.std_vector_lepton_d0[iLep]) < dxy          # formerly std_vector_lepton_BestTrackdxy
                     and abs(itree.std_vector_lepton_dz[iLep]) < 0.1          # formerly std_vector_lepton_BestTrackdz
                     ) :
                    isGoodLepton = True
                else :
                  if ( itree.std_vector_lepton_isMediumMuon[iLep] == 1 
                     and (itree.std_vector_lepton_chargedHadronIso[iLep] + muonIso) / itree.std_vector_lepton_pt[iLep] < 0.15
                     and abs(itree.std_vector_lepton_flavour[iLep]) == 13
                     and abs(itree.std_vector_lepton_BestTrackdxy[iLep]) < dxy    
                     and abs(itree.std_vector_lepton_BestTrackdz[iLep]) < 0.1     
                     ) :
                    isGoodLepton = True

                   
  #and (itree.std_vector_lepton_chargedHadronIso[iLep] + 
                   #     itree.std_vector_lepton_neutralHadronIso[iLep] + 
                   #     itree.std_vector_lepton_photonIso[iLep]
                   #     ) / itree.std_vector_lepton_pt[iLep] < 0.20 
                   #and abs(itree.std_vector_lepton_flavour[iLep]) == 13 
                  #) :
                #isGoodLepton = True

              ##########################################
              # denominator of fakes definition
              if self.kind == 2 :
               
                #print " fakes " 
                ###########
                # electron
                
                # id definition
                if self.cmssw == '763' :               

                  if (
                     abs(itree.std_vector_lepton_flavour[iLep]) == 11 
                     and 
                      ((
                      (abs(itree.std_vector_lepton_eta[iLep]) <= 1.479) 
                      and    (abs(itree.std_vector_electron_dEtaIn[iLep]) < 0.01               and
                              abs(itree.std_vector_electron_dPhiIn[iLep]) < 0.04               and
                              itree.std_vector_electron_full5x5_sigmaIetaIeta[iLep]    < 0.011              and
                              itree.std_vector_electron_hOverE[iLep]              < 0.08               and
                              itree.std_vector_electron_ooEmooP[iLep] < 0.01               and 
                              itree.std_vector_electron_expectedMissingInnerHits[iLep]<=2  and
                              itree.std_vector_lepton_d0[iLep]      < 0.1                and
                              abs(itree.std_vector_lepton_dz[iLep])< 0.373              and
                              itree.std_vector_electron_passConversionVeto[iLep] )
                      )
                      or 
                      (
                      (abs(itree.std_vector_lepton_eta[iLep]) > 1.479 and abs(itree.std_vector_lepton_eta[iLep]) < 2.5)
                      and    (abs(itree.std_vector_electron_dEtaIn[iLep]) < 0.01               and
                              abs(itree.std_vector_electron_dPhiIn[iLep]) < 0.08               and
                              itree.std_vector_electron_full5x5_sigmaIetaIeta[iLep]    < 0.031              and
                              itree.std_vector_electron_hOverE[iLep]              < 0.08               and
                              itree.std_vector_electron_ooEmooP[iLep] < 0.01               and
                              itree.std_vector_electron_expectedMissingInnerHits[iLep]<=1  and
                              itree.std_vector_lepton_d0[iLep]      < 0.2                and
                              abs(itree.std_vector_lepton_dz[iLep])< 0.602              and
                              itree.std_vector_electron_passConversionVeto[iLep] )
                      ))
                     ) : 
                       isGoodLepton = True; 

                else : # 74X cmssw release
                  if (
                     abs(itree.std_vector_lepton_flavour[iLep]) == 11 
                     and 
                      ((
                      (abs(itree.std_vector_lepton_eta[iLep]) <= 1.479) 
                      and    (abs(itree.std_vector_electron_dEtaIn[iLep]) < 0.01               and
                              abs(itree.std_vector_electron_dPhiIn[iLep]) < 0.04               and
                              itree.std_vector_electron_full5x5_sigmaIetaIeta[iLep]    < 0.011              and
                              itree.std_vector_electron_hOverE[iLep]              < 0.08               and
                              itree.std_vector_electron_ooEmooP[iLep] < 0.01               and 
                              itree.std_vector_electron_expectedMissingInnerHits[iLep]<=2  and
                              itree.std_vector_electron_d0[iLep]      < 0.1                and
                              abs(itree.std_vector_electron_dz[iLep])< 0.373              and
                              itree.std_vector_electron_passConversionVeto[iLep] )
                      )
                      or 
                      (
                      (abs(itree.std_vector_lepton_eta[iLep]) > 1.479 and abs(itree.std_vector_lepton_eta[iLep]) < 2.5)
                      and    (abs(itree.std_vector_electron_dEtaIn[iLep]) < 0.01               and
                              abs(itree.std_vector_electron_dPhiIn[iLep]) < 0.08               and
                              itree.std_vector_electron_full5x5_sigmaIetaIeta[iLep]    < 0.031              and
                              itree.std_vector_electron_hOverE[iLep]              < 0.08               and
                              itree.std_vector_electron_ooEmooP[iLep] < 0.01               and
                              itree.std_vector_electron_expectedMissingInnerHits[iLep]<=1  and
                              itree.std_vector_electron_d0[iLep]      < 0.2                and
                              abs(itree.std_vector_electron_dz[iLep])< 0.602              and
                              itree.std_vector_electron_passConversionVeto[iLep] )
                      ))
                     ) : 
                       isGoodLepton = True; 







                ###########
                # muon
                dxy = float(0.01)
                if (itree.std_vector_lepton_pt[iLep] > 20):
                    dxy = float(0.02)
               
                muonIso = float(0.0)
               
                if ( (itree.std_vector_lepton_photonIso[iLep] +
                     itree.std_vector_lepton_neutralHadronIso[iLep] -
                     0.5 * itree.std_vector_lepton_sumPUPt[iLep]) > 0
                     ) :
                    muonIso = (itree.std_vector_lepton_photonIso[iLep] +
                               itree.std_vector_lepton_neutralHadronIso[iLep] -
                               0.5 * itree.std_vector_lepton_sumPUPt[iLep])
                else:
                    muonIso = 0

                if self.cmssw == '763' :               
                  if ( itree.std_vector_lepton_isMediumMuon[iLep] == 1 
                       and (itree.std_vector_lepton_chargedHadronIso[iLep] + muonIso) / itree.std_vector_lepton_pt[iLep] < 0.4
                       and abs(itree.std_vector_lepton_flavour[iLep]) == 13
                       and abs(itree.std_vector_lepton_d0[iLep]) < dxy          # formerly std_vector_lepton_BestTrackdxy
                       and abs(itree.std_vector_lepton_dz[iLep]) < 0.1          # formerly std_vector_lepton_BestTrackdz
                       ) :
                    isGoodLepton = True
                else : 
                  if ( itree.std_vector_lepton_isMediumMuon[iLep] == 1 
                       and (itree.std_vector_lepton_chargedHadronIso[iLep] + muonIso) / itree.std_vector_lepton_pt[iLep] < 0.4
                       and abs(itree.std_vector_lepton_flavour[iLep]) == 13
                       and abs(itree.std_vector_lepton_BestTrackdxy[iLep]) < dxy
                       and abs(itree.std_vector_lepton_BestTrackdz[iLep]) < 0.1 
                       ) :
                    isGoodLepton = True


              # denominator of fakes definition (end)
              ##########################################
 
 
              # now check if we found 2 leptons        
                             
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
              for bname, bvector in self.oldBranchesToBeModifiedVector.iteritems():
                bvector.clear()
             
              # prepare the new vectors removing unwanted positions
              for bname, bvector in self.oldBranchesToBeModifiedVector.iteritems():
                 if ("vector_lepton" in bname) or ("vector_electron" in bname) or ("vector_muon" in bname):
                     self.changeOrder( bname, bvector, goodLeps)            
              
              # now the jets:  
              # - clean jets
              #   for leptons with pt > minLeptonPt (default 10 GeV)
	      minLeptonPt = 10.
	      
              goodJets = []
              for iJet in xrange(len(itree.std_vector_jet_pt)) :
                isLepton = False;
                for iLep in goodLeps :
		  if itree.std_vector_lepton_pt[iLep] < minLeptonPt:
		    break;
                  if self.jetIsLepton(itree.std_vector_jet_eta[iJet],itree.std_vector_jet_phi[iJet],itree.std_vector_lepton_eta[iLep],itree.std_vector_lepton_phi[iLep]) :
                    isLepton = True;
                if not isLepton:
                  goodJets.append(iJet)
              
              goodPuppiJets = []
              for iJet in xrange(len(itree.std_vector_puppijet_pt)) :
                  isLepton = False;
                  for iLep in goodLeps :
	 	      if itree.std_vector_lepton_pt[iLep] < minLeptonPt:
		          break;
                      if self.jetIsLepton(itree.std_vector_puppijet_eta[iJet],itree.std_vector_puppijet_phi[iJet],itree.std_vector_lepton_eta[iLep],itree.std_vector_lepton_phi[iLep]) :
                          isLepton = True;
                  if not isLepton:
                      goodPuppiJets.append(iJet)
                          
              for bname, bvector in self.oldBranchesToBeModifiedVector.iteritems():
                   if (("vector_jet" in bname) or (("vector_puppijet") in bname)) and not (("vector_lepton" in bname) or ("vector_electron" in bname) or ("vector_muon" in bname)):
                       if "vector_puppijet" in bname:
                           self.changeOrder( bname, bvector, goodPuppiJets)
                       else:
                           self.changeOrder( bname, bvector, goodJets)
                           
              for bname, bvector in self.looseLeptonVector.iteritems():
		   bvector.clear() 
                   self.changeOrder( bname, bvector, xrange(len(getattr(self.itree, bname))) )

              #print "goodJets: ", goodJets
              #print "goodPuppiJets: ", goodPuppiJets

              pt1 = itree.std_vector_lepton_pt[goodLep1]
              pt2 = itree.std_vector_lepton_pt[goodLep2]
              eta1 = itree.std_vector_lepton_eta[goodLep1]
              eta2 = itree.std_vector_lepton_eta[goodLep2]             
              phi1 = itree.std_vector_lepton_phi[goodLep1]
              phi2 = itree.std_vector_lepton_phi[goodLep2]
              pid1 = itree.std_vector_lepton_flavour[goodLep1]
              pid2 = itree.std_vector_lepton_flavour[goodLep2]
              if self.cmssw == '763' :
                met = itree.metPfType1      
                metphi = itree.metPfType1Phi
              else : 
                met = itree.pfType1Met          # formerly pfType1Met
                metphi = itree.pfType1Metphi    # formerly pfType1Metphi

              if len(goodJets) >=  2:
                jetpt1 = itree.std_vector_jet_pt[goodJets[0]]
                jetpt2 = itree.std_vector_jet_pt[goodJets[1]]
                jeteta1 = itree.std_vector_jet_eta[goodJets[0]]
                jeteta2 = itree.std_vector_jet_eta[goodJets[1]]
                jetphi1 = itree.std_vector_jet_phi[goodJets[0]]
                jetphi2 = itree.std_vector_jet_phi[goodJets[1]]
                jetmass1 = itree.std_vector_jet_mass[goodJets[0]]
                jetmass2 = itree.std_vector_jet_mass[goodJets[1]]
                WW = ROOT.WW(pt1, pt2, eta1, eta2, phi1, phi2, pid1, pid2, met, metphi, jetpt1, jetpt2, jeteta1, jeteta2, jetphi1, jetphi2, jetmass1, jetmass2)
              else:
                WW = ROOT.WW(pt1, pt2, eta1, eta2, phi1, phi2, pid1, pid2, met, metphi )
              
              
              # set the list of leptons into the object "WW"
              new_std_vector_lepton_pt.clear()
              new_std_vector_lepton_eta.clear()
              new_std_vector_lepton_phi.clear()
              new_std_vector_lepton_flavour.clear()

              for iGoodLep in goodLeps :
                new_std_vector_lepton_pt.push_back(itree.std_vector_lepton_pt[ iGoodLep ])
                new_std_vector_lepton_eta.push_back(itree.std_vector_lepton_eta[ iGoodLep ])
                new_std_vector_lepton_phi.push_back(itree.std_vector_lepton_phi[ iGoodLep ])
                new_std_vector_lepton_flavour.push_back(itree.std_vector_lepton_flavour[ iGoodLep ])
              
              WW.setLeptons(new_std_vector_lepton_pt, new_std_vector_lepton_eta, new_std_vector_lepton_phi, new_std_vector_lepton_flavour)

              # set the list of jets into the object "WW"
              new_std_vector_jet_pt.clear()
              new_std_vector_jet_eta.clear()
              for iGoodJet in goodJets :
                new_std_vector_jet_pt.push_back(itree.std_vector_jet_pt[ iGoodJet ])
                new_std_vector_jet_eta.push_back(itree.std_vector_jet_eta[ iGoodJet ])
              WW.setJets(new_std_vector_jet_pt, new_std_vector_jet_eta)
          
              # now fill the variables like "mll", "dphill", ...
              for bname, bvariable in self.oldBranchesToBeModifiedSimpleVariable.iteritems():
                bvariable[0] = getattr(WW, bname)()
                
              # refill the single jet variables
	      counter = 0
              varCounter = 0
              for bname, bvariable in self.jetVarDic.iteritems():
                  bvariable[0] = (getattr(self.otree, 'std_vector_jet_'+self.jetVariables[varCounter]))[counter]
                  counter += 1
                  if counter == maxnjets:
                      varCounter += 1
                      counter = 0                    

              otree.Fill()
              savedentries+=1

        self.disconnect()
        print '- Eventloop completed'
        print '   Saved: ', savedentries, ' events'

