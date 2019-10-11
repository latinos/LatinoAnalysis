import ROOT
import os
import re
import numpy
import math
import time
import copy
ROOT.PyConfig.IgnoreCommandLineOptions = True

from PhysicsTools.NanoAODTools.postprocessing.framework.eventloop import Module
from LatinoAnalysis.NanoGardener.data.LeptonMaker_cfg import Lepton_br, Lepton_var
from LatinoAnalysis.NanoGardener.data.LeptonMaker_cfg import VetoLepton_br, VetoLepton_var
from LatinoAnalysis.NanoGardener.data.LeptonMaker_cfg import CleanJet_br, CleanJet_var
from LatinoAnalysis.NanoGardener.data.common_cfg import Type_dict

from PhysicsTools.NanoAODTools.postprocessing.framework.datamodel import Collection


class FakeWeight():

    def _openRootFile(self,path, option=''):
        f =  ROOT.TFile.Open(path,option)
        if not f.__nonzero__() or not f.IsOpen():
            raise NameError('File '+path+' not open')
        return f

    def _getRootObj(self,d,name):
        o = d.Get(name)
        if not o.__nonzero__():
            print 'Object '+name+' doesn\'t exist in '+d.GetName(), ' BE CAREFUL!'
        return o

    def __init__ (self,cmssw,eleWPDic,muWPDic,WPType,eleWP,muWP):
        print  "-------- Fake Weight init() ---------"
        print eleWP,muWP

        cmssw_base = os.getenv('CMSSW_BASE')

        self.eleDir = eleWPDic[cmssw][WPType][eleWP]['fakeW']
        self.muDir  = muWPDic[cmssw][WPType][muWP]['fakeW']
        print self.eleDir , self.muDir

        # Root Files

        self.fileMuPR = self._openRootFile(cmssw_base+'/src/'+self.muDir+'/MuonPR.root')
        self.fileElPR = self._openRootFile(cmssw_base+'/src/'+self.eleDir+'/ElePR.root')

        self.fileMuFR_jet10 = self._openRootFile(cmssw_base+'/src/'+self.muDir+'/MuonFR_jet10.root')
        self.fileMuFR_jet15 = self._openRootFile(cmssw_base+'/src/'+self.muDir+'/MuonFR_jet15.root')
        self.fileMuFR_jet20 = self._openRootFile(cmssw_base+'/src/'+self.muDir+'/MuonFR_jet20.root')
        self.fileMuFR_jet25 = self._openRootFile(cmssw_base+'/src/'+self.muDir+'/MuonFR_jet25.root')
        self.fileMuFR_jet30 = self._openRootFile(cmssw_base+'/src/'+self.muDir+'/MuonFR_jet30.root')
        self.fileMuFR_jet35 = self._openRootFile(cmssw_base+'/src/'+self.muDir+'/MuonFR_jet35.root')
        self.fileMuFR_jet45 = self._openRootFile(cmssw_base+'/src/'+self.muDir+'/MuonFR_jet45.root')

        self.fileElFR_jet25 = self._openRootFile(cmssw_base+'/src/'+self.eleDir+'/EleFR_jet25.root')
        self.fileElFR_jet35 = self._openRootFile(cmssw_base+'/src/'+self.eleDir+'/EleFR_jet35.root')
        self.fileElFR_jet45 = self._openRootFile(cmssw_base+'/src/'+self.eleDir+'/EleFR_jet45.root')

        # Root Histos

        self.MuPR = self._getRootObj(self.fileMuPR, 'h_Muon_signal_pt_eta_bin')
        self.ElPR = self._getRootObj(self.fileElPR, 'h_Ele_signal_pt_eta_bin')

        self.MuFR_jet10 = self._getRootObj(self.fileMuFR_jet10, 'FR_pT_eta_EWKcorr')
        self.MuFR_jet15 = self._getRootObj(self.fileMuFR_jet15, 'FR_pT_eta_EWKcorr')
        self.MuFR_jet20 = self._getRootObj(self.fileMuFR_jet20, 'FR_pT_eta_EWKcorr')
        self.MuFR_jet25 = self._getRootObj(self.fileMuFR_jet25, 'FR_pT_eta_EWKcorr')
        self.MuFR_jet30 = self._getRootObj(self.fileMuFR_jet30, 'FR_pT_eta_EWKcorr')
        self.MuFR_jet35 = self._getRootObj(self.fileMuFR_jet35, 'FR_pT_eta_EWKcorr')
        self.MuFR_jet45 = self._getRootObj(self.fileMuFR_jet45, 'FR_pT_eta_EWKcorr')

        self.ElFR_jet25 = self._getRootObj(self.fileElFR_jet25, 'FR_pT_eta_EWKcorr')
        self.ElFR_jet35 = self._getRootObj(self.fileElFR_jet35, 'FR_pT_eta_EWKcorr')
        self.ElFR_jet45 = self._getRootObj(self.fileElFR_jet45, 'FR_pT_eta_EWKcorr')

        #self.MuFR_jet10 = self._getRootObj(self.fileMuFR_jet10, 'FR_pt_eta_EWKcorr')
        #self.MuFR_jet15 = self._getRootObj(self.fileMuFR_jet15, 'FR_pt_eta_EWKcorr')
        #self.MuFR_jet20 = self._getRootObj(self.fileMuFR_jet20, 'FR_pt_eta_EWKcorr')
        #self.MuFR_jet25 = self._getRootObj(self.fileMuFR_jet25, 'FR_pt_eta_EWKcorr')
        #self.MuFR_jet30 = self._getRootObj(self.fileMuFR_jet30, 'FR_pt_eta_EWKcorr')
        #self.MuFR_jet35 = self._getRootObj(self.fileMuFR_jet35, 'FR_pt_eta_EWKcorr')
        #self.MuFR_jet45 = self._getRootObj(self.fileMuFR_jet45, 'FR_pt_eta_EWKcorr')

        #self.ElFR_jet25 = self._getRootObj(self.fileElFR_jet25, 'FR_pt_eta_EWKcorr')
        #self.ElFR_jet35 = self._getRootObj(self.fileElFR_jet35, 'FR_pt_eta_EWKcorr')
        #self.ElFR_jet45 = self._getRootObj(self.fileElFR_jet45, 'FR_pt_eta_EWKcorr')

    def _getRate(self, h2, pt, eta, leptonptmax):

        aeta  = abs(eta)
        nbins = h2.GetNbinsX()
        ptmax = leptonptmax
        
        if (ptmax <= 0.) : ptmax = h2.GetXaxis().GetBinCenter(nbins)
        
        rate_value = h2.GetBinContent(h2.FindBin(min(pt, ptmax), aeta))
        rate_error = h2.GetBinError  (h2.FindBin(min(pt, ptmax), aeta))
        
        return rate_value, rate_error


    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # _get1lWeight
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def _get1lWeight(self, leptons, MuFRName, ElFRName, stat):

        # Get FR
        exec ('ElFR = self.'+ElFRName )
        exec ('MuFR = self.'+MuFRName )

        # avoid dots to go faster
        MuPR = self.MuPR
        ElPR = self.ElPR

        #only the first lepton 
        lepton = leptons[0]

        promptProbability = numpy.ones(1, dtype=numpy.float32)
        fakeProbability   = numpy.ones(1, dtype=numpy.float32)
        
        p  = 1.  # prompt rate
        f  = 0.  # fake   rate
        pE = 0.  # prompt rate statistical error
        fE = 0.  # fake   rate statistical error

        if (lepton[0] == 'mu') :

            p, pE = self._getRate(MuPR, lepton[1], lepton[2], -999.)
            f, fE = self._getRate(MuFR, lepton[1], lepton[2],   35.)

            if   (stat == 'MuUp')   : f = f + fE
            elif (stat == 'MuDown') : f = f - fE

        elif (lepton[0] == 'ele') :

            p, pE = self._getRate(ElPR, lepton[1], lepton[2], -999.)
            f, fE = self._getRate(ElFR, lepton[1], lepton[2],   35.)

            if   (stat == 'ElUp')   : f = f + fE
            elif (stat == 'ElDown') : f = f - fE

        if (lepton[3] == 1) :
            # Tight lepton
            fakeProbability   = (-1) * f * (1 - p)
        
        else :
            fakeProbability   = p * f

        fakeProbability   /= (p - f)

        return fakeProbability

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # _get2lWeight
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def _get2lWeight(self, leptons, MuFRName, ElFRName, stat):

        # Get FR
        exec ('ElFR = self.'+ElFRName )
        exec ('MuFR = self.'+MuFRName )

        # avoid dots to go faster
        MuPR = self.MuPR
        ElPR = self.ElPR

        if (len(leptons) < 2) :

            return 0.0

        else :

            promptProbability = numpy.ones(2, dtype=numpy.float32)
            fakeProbability   = numpy.ones(2, dtype=numpy.float32)

            ntight = 0

            for i in leptons :

                if (i > 1) : break
                
                p  = 1.  # prompt rate
                f  = 0.  # fake   rate
                pE = 0.  # prompt rate statistical error
                fE = 0.  # fake   rate statistical error

                if (leptons[i][0] == 'mu') :

                    p, pE = self._getRate(MuPR, leptons[i][1], leptons[i][2], -999.)
                    f, fE = self._getRate(MuFR, leptons[i][1], leptons[i][2],   35.)

                    if   (stat == 'MuUp')   : f = f + fE
                    elif (stat == 'MuDown') : f = f - fE

                elif (leptons[i][0] == 'ele') :

                    p, pE = self._getRate(ElPR, leptons[i][1], leptons[i][2], -999.)
                    f, fE = self._getRate(ElFR, leptons[i][1], leptons[i][2],   35.)

                    if   (stat == 'ElUp')   : f = f + fE
                    elif (stat == 'ElDown') : f = f - fE

                if (leptons[i][3] == 1) :

                    ntight += 1
 
                    promptProbability[i] = p * (1 - f)
                    fakeProbability[i]   = f * (1 - p)
             
                else :

                    promptProbability[i] = p * f
                    fakeProbability[i]   = p * f

                promptProbability[i] /= (p - f)
                fakeProbability[i]   /= (p - f)
 
            PF = promptProbability[0] * fakeProbability  [1]
            FP = fakeProbability  [0] * promptProbability[1]
            FF = fakeProbability  [0] * fakeProbability  [1]

            if (ntight == 1) :
                FF *= -1.
            else :
                PF *= -1.
                FP *= -1.

            result = PF + FP + FF
    
            return result


    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # _get3lWeight
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def _get3lWeight(self, leptons, MuFRName, ElFRName, stat):

        # Get FR
        exec ('ElFR = self.'+ElFRName )
        exec ('MuFR = self.'+MuFRName )


        # avoid dots to go faster
        MuPR = self.MuPR
        ElPR = self.ElPR

        if (len(leptons) < 3) :

            return 0.0

        else :

            promptProbability = numpy.ones(3, dtype=numpy.float32)
            fakeProbability   = numpy.ones(3, dtype=numpy.float32)

            ntight = 0

            for i in leptons :

                if (i > 2) : break
                
                p  = 1.  # prompt rate
                f  = 0.  # fake   rate
                pE = 0.  # prompt rate statistical error
                fE = 0.  # fake   rate statistical error

                if (leptons[i][0] == 'mu') :

                    p, pE = self._getRate(MuPR, leptons[i][1], leptons[i][2], -999.)
                    f, fE = self._getRate(MuFR, leptons[i][1], leptons[i][2],   35.)

                    if   (stat == 'MuUp')   : f = f + fE
                    elif (stat == 'MuDown') : f = f - fE

                elif (leptons[i][0] == 'ele') :

                    p, pE = self._getRate(ElPR, leptons[i][1], leptons[i][2], -999.)
                    f, fE = self._getRate(ElFR, leptons[i][1], leptons[i][2],   35.)

                    if   (stat == 'ElUp')   : f = f + fE
                    elif (stat == 'ElDown') : f = f - fE

                if (leptons[i][3] == 1) :

                    ntight += 1
 
                    promptProbability[i] = p * (1 - f)
                    fakeProbability[i]   = f * (1 - p)
             
                else :

                    promptProbability[i] = p * f
                    fakeProbability[i]   = p * f

                promptProbability[i] /= (p - f)
                fakeProbability[i]   /= (p - f)
 
            PPF = promptProbability[0] * promptProbability[1] * fakeProbability  [2];
            PFP = promptProbability[0] * fakeProbability  [1] * promptProbability[2];
            FPP = fakeProbability  [0] * promptProbability[1] * promptProbability[2];

            PFF = promptProbability[0] * fakeProbability  [1] * fakeProbability  [2];
            FPF = fakeProbability  [0] * promptProbability[1] * fakeProbability  [2];
            FFP = fakeProbability  [0] * fakeProbability  [1] * promptProbability[2];

            FFF = fakeProbability[0] * fakeProbability[1] * fakeProbability[2];

            if (ntight == 1 or ntight == 3) :
                PPF *= -1.
                PFP *= -1.
                FPP *= -1.
                FFF *= -1.
            else :
                PFF *= -1.
                FPF *= -1.
                FFP *= -1.

            result = PPF+PFP+FPP + PFF+FPF+FFP + FFF
    
            return result


    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # _get4lWeight
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def _get4lWeight(self, leptons, MuFRName, ElFRName, stat):

        # Get FR
        exec ('ElFR = self.'+ElFRName )
        exec ('MuFR = self.'+MuFRName )

        # avoid dots to go faster
        MuPR = self.MuPR
        ElPR = self.ElPR

        if (len(leptons) < 4) :

            return 0.0

        else :

            promptProbability = numpy.ones(4, dtype=numpy.float32)
            fakeProbability   = numpy.ones(4, dtype=numpy.float32)

            ntight = 0

            for i in leptons :

                if (i > 3) : break
                
                p  = 1.  # prompt rate
                f  = 0.  # fake   rate
                pE = 0.  # prompt rate statistical error
                fE = 0.  # fake   rate statistical error

                if (leptons[i][0] == 'mu') :

                    p, pE = self._getRate(MuPR, leptons[i][1], leptons[i][2], -999.)
                    f, fE = self._getRate(MuFR, leptons[i][1], leptons[i][2],   35.)

                    if   (stat == 'MuUp')   : f = f + fE
                    elif (stat == 'MuDown') : f = f - fE

                elif (leptons[i][0] == 'ele') :

                    p, pE = self._getRate(ElPR, leptons[i][1], leptons[i][2], -999.)
                    f, fE = self._getRate(ElFR, leptons[i][1], leptons[i][2],   35.)

                    if   (stat == 'ElUp')   : f = f + fE
                    elif (stat == 'ElDown') : f = f - fE

                if (leptons[i][3] == 1) :

                    ntight += 1
 
                    promptProbability[i] = p * (1 - f)
                    fakeProbability[i]   = f * (1 - p)
             
                else :

                    promptProbability[i] = p * f
                    fakeProbability[i]   = p * f

                promptProbability[i] /= (p - f)
                fakeProbability[i]   /= (p - f)
 
            PPPF = promptProbability[0] * promptProbability[1] * promptProbability[2] * fakeProbability  [3];
            PPFP = promptProbability[0] * promptProbability[1] * fakeProbability  [2] * promptProbability[3];
            PFPP = promptProbability[0] * fakeProbability  [1] * promptProbability[2] * promptProbability[3];
            FPPP = fakeProbability  [0] * promptProbability[1] * promptProbability[2] * promptProbability[3];

            FFPP = fakeProbability  [0] * fakeProbability  [1] * promptProbability[2] * promptProbability[3];
            PPFF = promptProbability[0] * promptProbability[1] * fakeProbability  [2] * fakeProbability  [3];
            PFPF = promptProbability[0] * fakeProbability  [1] * promptProbability[2] * fakeProbability  [3];
            FPFP = fakeProbability  [0] * promptProbability[1] * fakeProbability  [2] * promptProbability[3];
            FPPF = fakeProbability  [0] * promptProbability[1] * promptProbability[2] * fakeProbability  [3];
            PFFP = promptProbability[0] * fakeProbability  [1] * fakeProbability  [2] * promptProbability[3];

            FFFP = fakeProbability  [0] * fakeProbability  [1] * fakeProbability  [2] * promptProbability[3];
            FFPF = fakeProbability  [0] * fakeProbability  [1] * promptProbability[2] * fakeProbability  [3];
            FPFF = fakeProbability  [0] * promptProbability[1] * fakeProbability  [2] * fakeProbability  [3];
            PFFF = promptProbability[0] * fakeProbability  [1] * fakeProbability  [2] * fakeProbability  [3];

            FFFF = fakeProbability[0] * fakeProbability[1] * fakeProbability[2] * fakeProbability[3];

            if (ntight == 1 or ntight == 3) :
                FFPP *= -1.
                PPFF *= -1.
                PFPF *= -1.
                FPFP *= -1.
                FPPF *= -1.
                PFFP *= -1.
                #
                FFFF *= -1.
            else :
                PPPF *= -1.
                PPFP *= -1.
                PFPP *= -1.
                FPPP *= -1.
                #
                FFFP *= -1.
                FFPF *= -1.
                FPFF *= -1.
                PFFF *= -1.

            result = PPPF+PPFP+PFPP+FPPP + FFPP+PPFF+PFPF+FPFP+FPPF+PFFP + FFFP+FFPF+FPFF+FPFF+PFFF + FFFF

            return result

class LeptonFakeWMaker(Module):
    '''
    Produce branches with lepton fake weights
    '''

    def __init__(self, cmssw, WPdic='LatinoAnalysis/NanoGardener/python/data/LeptonSel_cfg.py', min_nlep=2):
        self.min_nlep = min_nlep 
        self.cmssw = cmssw     
        cmssw_base = os.getenv('CMSSW_BASE')
        self.WPdic = cmssw_base+'/src/'+WPdic
        print " cmssw = ", self.cmssw
        print " WPDic = ", self.WPdic   
        if os.path.exists(self.WPdic) :
          handle = open(self.WPdic,'r')
          exec(handle)
          handle.close()
        else:
          print 'ERROR: No WP'
          exit()

        # Create Elecron and muon fakeW
        self.FakeWeights = {}
        if self.cmssw in ElectronWP and self.cmssw in MuonWP :
          if 'TightObjWP' in ElectronWP[self.cmssw] and 'TightObjWP' in MuonWP[self.cmssw] :
            for eleWP in ElectronWP[self.cmssw]['TightObjWP']  :
              for muWP in MuonWP[self.cmssw]['TightObjWP'] :
                Tag = 'ele_'+eleWP+'_mu_'+muWP
                self.FakeWeights[Tag] = {}
                self.FakeWeights[Tag]['eleWP'] = eleWP
                self.FakeWeights[Tag]['muWP']  = muWP
                self.FakeWeights[Tag]['fakeW'] = FakeWeight(self.cmssw,ElectronWP,MuonWP,'TightObjWP',eleWP,muWP)
          else:
            print 'ERROR: no TightObjWP in Ele/Mu WPDic'
            exit()
        else:
          print 'ERROR: no CMSSW version ('+self.cmssw+') in Ele/Mu WPDic'
          exit()

    def beginJob(self):
        pass

    def endJob(self):
        pass

    def beginFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        self.out = wrappedOutputTree

        # New Branches
        fakeVarExt =  [ 
                        '_2l0j', '_2l0jMuUp', '_2l0jMuDown', '_2l0jElUp', '_2l0jElDown', '_2l0jstatMuUp', '_2l0jstatMuDown', '_2l0jstatElUp', '_2l0jstatElDown',
                        '_2l1j', '_2l1jMuUp', '_2l1jMuDown', '_2l1jElUp', '_2l1jElDown', '_2l1jstatMuUp', '_2l1jstatMuDown', '_2l1jstatElUp', '_2l1jstatElDown',
                        '_2l2j', '_2l2jMuUp', '_2l2jMuDown', '_2l2jElUp', '_2l2jElDown', '_2l2jstatMuUp', '_2l2jstatMuDown', '_2l2jstatElUp', '_2l2jstatElDown',
                        '_3l',   '_3lMuUp',   '_3lMuDown',   '_3lElUp',   '_3lElDown',   '_3lstatMuUp',   '_3lstatMuDown',   '_3lstatElUp',   '_3lstatElDown',
                        '_4l',   '_4lMuUp',   '_4lMuDown',   '_4lElUp',   '_4lElDown',   '_4lstatMuUp',   '_4lstatMuDown',   '_4lstatElUp',   '_4lstatElDown' ]

        if self.min_nlep == 1:
            fakeVarExt = [ ]
            for mupt in [10,15,20,25,30,35,45]:
                for elept in [25,35,45]:
                    fakeVarExt.append("_mu{}_ele{}".format(mupt,elept))
            

        for iTag in self.FakeWeights:
          for iVarExt in fakeVarExt : 
            print 'Creating  : ','fakeW_'+iTag+iVarExt
            self.out.branch('fakeW_'+iTag+iVarExt,'F')            

    def endFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        pass

    #_____Analyze
    def analyze(self, event):
        """process event, return True (go to next module) or False (fail, go to next event)"""

        # Prepare leptons 
        lepton_col   = Collection(event, 'Lepton')
        nLep = len(lepton_col)

        Leptons = {}
        for iTag in self.FakeWeights: Leptons[iTag] = {}
        selectedLepton = 0
        for iLep in xrange(nLep) :

                # get kinematic
                pt      = lepton_col[iLep]['pt']
                eta     = lepton_col[iLep]['eta']
                flavour = lepton_col[iLep]['pdgId']

                # use strings ... I just like strings, not real reason
                kindLep = 'nonlep' # ele or mu
                if abs (flavour) == 11 :
                  kindLep = 'ele'
                elif abs (flavour) == 13 :
                  kindLep = 'mu'


                # consider only leptons with pt>10 GeV
                if pt > 10 \
                   and (   (kindLep == 'ele' and abs(eta) < 2.5)  \
                        or (kindLep == 'mu'  and abs(eta) < 2.4)  \
                       ) :

                   # save information about "lepton is tight or not"
                   # *all* leptons should be already loose after l2sel step!
                   #IsTightLepton = itree.std_vector_lepton_isTightLepton[iLep]

                   for iTag in self.FakeWeights:
                     eleWP = self.FakeWeights[iTag]['eleWP']
                     muWP  = self.FakeWeights[iTag]['muWP']
                     if   abs (flavour) == 11 : IsTightLepton = lepton_col[iLep]['isTightElectron_'+eleWP]
                     elif abs (flavour) == 13 : IsTightLepton = lepton_col[iLep]['isTightMuon_'+muWP]
                     Leptons[iTag][selectedLepton] = [kindLep, pt, eta, IsTightLepton]

                   selectedLepton += 1

        # Now compute the fakes 
        for iTag in self.FakeWeights:
            if self.min_nlep == 1 and selectedLepton == 1:
               for mupt in [10,15,20,25,30,35,45]:
                  for elept in [25,35,45]:
                     self.out.fillBranch('fakeW_{}_mu{}_ele{}'.format(iTag, mupt, elept) , self.FakeWeights[iTag]['fakeW']._get1lWeight(Leptons[iTag], 'MuFR_jet{}'.format(mupt), 'ElFR_jet{}'.format(elept), 'Nominal'))
            else:   
               self.out.fillBranch('fakeW_'+iTag+'_2l0j'          , self.FakeWeights[iTag]['fakeW']._get2lWeight(Leptons[iTag], 'MuFR_jet20', 'ElFR_jet35', 'Nominal') )
               self.out.fillBranch('fakeW_'+iTag+'_2l0jMuUp'      , self.FakeWeights[iTag]['fakeW']._get2lWeight(Leptons[iTag], 'MuFR_jet30', 'ElFR_jet35', 'Nominal') )
               self.out.fillBranch('fakeW_'+iTag+'_2l0jMuDown'    , self.FakeWeights[iTag]['fakeW']._get2lWeight(Leptons[iTag], 'MuFR_jet10', 'ElFR_jet35', 'Nominal') )
               self.out.fillBranch('fakeW_'+iTag+'_2l0jElUp'      , self.FakeWeights[iTag]['fakeW']._get2lWeight(Leptons[iTag], 'MuFR_jet20', 'ElFR_jet45', 'Nominal') )
               self.out.fillBranch('fakeW_'+iTag+'_2l0jElDown'    , self.FakeWeights[iTag]['fakeW']._get2lWeight(Leptons[iTag], 'MuFR_jet20', 'ElFR_jet25', 'Nominal') )
               self.out.fillBranch('fakeW_'+iTag+'_2l0jstatMuUp'  , self.FakeWeights[iTag]['fakeW']._get2lWeight(Leptons[iTag], 'MuFR_jet20', 'ElFR_jet35', 'MuUp')    )
               self.out.fillBranch('fakeW_'+iTag+'_2l0jstatMuDown', self.FakeWeights[iTag]['fakeW']._get2lWeight(Leptons[iTag], 'MuFR_jet20', 'ElFR_jet35', 'MuDown')  )
               self.out.fillBranch('fakeW_'+iTag+'_2l0jstatElUp'  , self.FakeWeights[iTag]['fakeW']._get2lWeight(Leptons[iTag], 'MuFR_jet20', 'ElFR_jet35', 'ElUp')    )
               self.out.fillBranch('fakeW_'+iTag+'_2l0jstatElDown', self.FakeWeights[iTag]['fakeW']._get2lWeight(Leptons[iTag], 'MuFR_jet20', 'ElFR_jet35', 'ElDown')  )

               self.out.fillBranch('fakeW_'+iTag+'_2l1j'          , self.FakeWeights[iTag]['fakeW']._get2lWeight(Leptons[iTag], 'MuFR_jet25', 'ElFR_jet35', 'Nominal') )
               self.out.fillBranch('fakeW_'+iTag+'_2l1jMuUp'      , self.FakeWeights[iTag]['fakeW']._get2lWeight(Leptons[iTag], 'MuFR_jet35', 'ElFR_jet35', 'Nominal') )
               self.out.fillBranch('fakeW_'+iTag+'_2l1jMuDown'    , self.FakeWeights[iTag]['fakeW']._get2lWeight(Leptons[iTag], 'MuFR_jet15', 'ElFR_jet35', 'Nominal') )
               self.out.fillBranch('fakeW_'+iTag+'_2l1jElUp'      , self.FakeWeights[iTag]['fakeW']._get2lWeight(Leptons[iTag], 'MuFR_jet25', 'ElFR_jet45', 'Nominal') )
               self.out.fillBranch('fakeW_'+iTag+'_2l1jElDown'    , self.FakeWeights[iTag]['fakeW']._get2lWeight(Leptons[iTag], 'MuFR_jet25', 'ElFR_jet25', 'Nominal') )
               self.out.fillBranch('fakeW_'+iTag+'_2l1jstatMuUp'  , self.FakeWeights[iTag]['fakeW']._get2lWeight(Leptons[iTag], 'MuFR_jet25', 'ElFR_jet35', 'MuUp')    )
               self.out.fillBranch('fakeW_'+iTag+'_2l1jstatMuDown', self.FakeWeights[iTag]['fakeW']._get2lWeight(Leptons[iTag], 'MuFR_jet25', 'ElFR_jet35', 'MuDown')  )
               self.out.fillBranch('fakeW_'+iTag+'_2l1jstatElUp'  , self.FakeWeights[iTag]['fakeW']._get2lWeight(Leptons[iTag], 'MuFR_jet25', 'ElFR_jet35', 'ElUp')    )
               self.out.fillBranch('fakeW_'+iTag+'_2l1jstatElDown', self.FakeWeights[iTag]['fakeW']._get2lWeight(Leptons[iTag], 'MuFR_jet25', 'ElFR_jet35', 'ElDown')  )

               self.out.fillBranch('fakeW_'+iTag+'_2l2j'          , self.FakeWeights[iTag]['fakeW']._get2lWeight(Leptons[iTag], 'MuFR_jet35', 'ElFR_jet35', 'Nominal') )
               self.out.fillBranch('fakeW_'+iTag+'_2l2jMuUp'      , self.FakeWeights[iTag]['fakeW']._get2lWeight(Leptons[iTag], 'MuFR_jet45', 'ElFR_jet35', 'Nominal') )
               self.out.fillBranch('fakeW_'+iTag+'_2l2jMuDown'    , self.FakeWeights[iTag]['fakeW']._get2lWeight(Leptons[iTag], 'MuFR_jet25', 'ElFR_jet35', 'Nominal') )
               self.out.fillBranch('fakeW_'+iTag+'_2l2jElUp'      , self.FakeWeights[iTag]['fakeW']._get2lWeight(Leptons[iTag], 'MuFR_jet35', 'ElFR_jet45', 'Nominal') )
               self.out.fillBranch('fakeW_'+iTag+'_2l2jElDown'    , self.FakeWeights[iTag]['fakeW']._get2lWeight(Leptons[iTag], 'MuFR_jet35', 'ElFR_jet25', 'Nominal') )
               self.out.fillBranch('fakeW_'+iTag+'_2l2jstatMuUp'  , self.FakeWeights[iTag]['fakeW']._get2lWeight(Leptons[iTag], 'MuFR_jet35', 'ElFR_jet35', 'MuUp')    )
               self.out.fillBranch('fakeW_'+iTag+'_2l2jstatMuDown', self.FakeWeights[iTag]['fakeW']._get2lWeight(Leptons[iTag], 'MuFR_jet35', 'ElFR_jet35', 'MuDown')  )
               self.out.fillBranch('fakeW_'+iTag+'_2l2jstatElUp'  , self.FakeWeights[iTag]['fakeW']._get2lWeight(Leptons[iTag], 'MuFR_jet35', 'ElFR_jet35', 'ElUp')    )
               self.out.fillBranch('fakeW_'+iTag+'_2l2jstatElDown', self.FakeWeights[iTag]['fakeW']._get2lWeight(Leptons[iTag], 'MuFR_jet35', 'ElFR_jet35', 'ElDown')  )

               self.out.fillBranch('fakeW_'+iTag+'_3l'            , self.FakeWeights[iTag]['fakeW']._get3lWeight(Leptons[iTag], 'MuFR_jet35', 'ElFR_jet35', 'Nominal') )
               self.out.fillBranch('fakeW_'+iTag+'_3lMuUp'        , self.FakeWeights[iTag]['fakeW']._get3lWeight(Leptons[iTag], 'MuFR_jet45', 'ElFR_jet35', 'Nominal') )
               self.out.fillBranch('fakeW_'+iTag+'_3lMuDown'      , self.FakeWeights[iTag]['fakeW']._get3lWeight(Leptons[iTag], 'MuFR_jet25', 'ElFR_jet35', 'Nominal') )
               self.out.fillBranch('fakeW_'+iTag+'_3lElUp'        , self.FakeWeights[iTag]['fakeW']._get3lWeight(Leptons[iTag], 'MuFR_jet35', 'ElFR_jet45', 'Nominal') )
               self.out.fillBranch('fakeW_'+iTag+'_3lElDown'      , self.FakeWeights[iTag]['fakeW']._get3lWeight(Leptons[iTag], 'MuFR_jet35', 'ElFR_jet25', 'Nominal') )
               self.out.fillBranch('fakeW_'+iTag+'_3lstatMuUp'    , self.FakeWeights[iTag]['fakeW']._get3lWeight(Leptons[iTag], 'MuFR_jet35', 'ElFR_jet35', 'MuUp')    )
               self.out.fillBranch('fakeW_'+iTag+'_3lstatMuDown'  , self.FakeWeights[iTag]['fakeW']._get3lWeight(Leptons[iTag], 'MuFR_jet35', 'ElFR_jet35', 'MuDown')  )
               self.out.fillBranch('fakeW_'+iTag+'_3lstatElUp'    , self.FakeWeights[iTag]['fakeW']._get3lWeight(Leptons[iTag], 'MuFR_jet35', 'ElFR_jet35', 'ElUp')    )
               self.out.fillBranch('fakeW_'+iTag+'_3lstatElDown'  , self.FakeWeights[iTag]['fakeW']._get3lWeight(Leptons[iTag], 'MuFR_jet35', 'ElFR_jet35', 'ElDown')  )

               self.out.fillBranch('fakeW_'+iTag+'_4l'            , self.FakeWeights[iTag]['fakeW']._get4lWeight(Leptons[iTag], 'MuFR_jet35', 'ElFR_jet35', 'Nominal') )
               self.out.fillBranch('fakeW_'+iTag+'_4lMuUp'        , self.FakeWeights[iTag]['fakeW']._get4lWeight(Leptons[iTag], 'MuFR_jet45', 'ElFR_jet35', 'Nominal') )
               self.out.fillBranch('fakeW_'+iTag+'_4lMuDown'      , self.FakeWeights[iTag]['fakeW']._get4lWeight(Leptons[iTag], 'MuFR_jet25', 'ElFR_jet35', 'Nominal') )
               self.out.fillBranch('fakeW_'+iTag+'_4lElUp'        , self.FakeWeights[iTag]['fakeW']._get4lWeight(Leptons[iTag], 'MuFR_jet35', 'ElFR_jet45', 'Nominal') )
               self.out.fillBranch('fakeW_'+iTag+'_4lElDown'      , self.FakeWeights[iTag]['fakeW']._get4lWeight(Leptons[iTag], 'MuFR_jet35', 'ElFR_jet25', 'Nominal') )
               self.out.fillBranch('fakeW_'+iTag+'_4lstatMuUp'    , self.FakeWeights[iTag]['fakeW']._get4lWeight(Leptons[iTag], 'MuFR_jet35', 'ElFR_jet35', 'MuUp')    )
               self.out.fillBranch('fakeW_'+iTag+'_4lstatMuDown'  , self.FakeWeights[iTag]['fakeW']._get4lWeight(Leptons[iTag], 'MuFR_jet35', 'ElFR_jet35', 'MuDown')  )
               self.out.fillBranch('fakeW_'+iTag+'_4lstatElUp'    , self.FakeWeights[iTag]['fakeW']._get4lWeight(Leptons[iTag], 'MuFR_jet35', 'ElFR_jet35', 'ElUp') )
               self.out.fillBranch('fakeW_'+iTag+'_4lstatElDown'  , self.FakeWeights[iTag]['fakeW']._get4lWeight(Leptons[iTag], 'MuFR_jet35', 'ElFR_jet35', 'ElDown') )

        return True
