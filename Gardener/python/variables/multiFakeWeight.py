#
#    ____|       |              \ \        /     _)         |      |         
#    |     _` |  |  /   _ \      \ \  \   /  _ \  |   _` |  __ \   __| 
#    __|  (   |    <    __/       \ \  \ /   __/  |  (   |  | | |  |   
#   _|   \__,_| _|\_\ \___|        \_/\_/  \___| _| \__, | _| |_| \__| 
#                                                   |___/                                                                                                                                #
# author:  Xavier Janssen
# purpose: Allow multiple lepton WP in fake Weight application

import optparse
import numpy
import ROOT
import os.path
import math

from LatinoAnalysis.Gardener.gardening import TreeCloner

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

        # Root Files

        self.fileMuPR = self._openRootFile(cmssw_base+'/src/'+self.muDir+'/MuonPR_Run2016_HWW36fb.root')
        self.fileElPR = self._openRootFile(cmssw_base+'/src/'+self.eleDir+'/ElePR_Run2016_HWW36fb.root')

        self.fileMuFR_jet10 = self._openRootFile(cmssw_base+'/src/'+self.muDir+'/MuonFR_Run2016_HWW36fb_jet10.root')
        self.fileMuFR_jet15 = self._openRootFile(cmssw_base+'/src/'+self.muDir+'/MuonFR_Run2016_HWW36fb_jet15.root')
        self.fileMuFR_jet20 = self._openRootFile(cmssw_base+'/src/'+self.muDir+'/MuonFR_Run2016_HWW36fb_jet20.root')
        self.fileMuFR_jet25 = self._openRootFile(cmssw_base+'/src/'+self.muDir+'/MuonFR_Run2016_HWW36fb_jet25.root')
        self.fileMuFR_jet30 = self._openRootFile(cmssw_base+'/src/'+self.muDir+'/MuonFR_Run2016_HWW36fb_jet30.root')
        self.fileMuFR_jet35 = self._openRootFile(cmssw_base+'/src/'+self.muDir+'/MuonFR_Run2016_HWW36fb_jet35.root')
        self.fileMuFR_jet45 = self._openRootFile(cmssw_base+'/src/'+self.muDir+'/MuonFR_Run2016_HWW36fb_jet45.root')

        self.fileElFR_jet25 = self._openRootFile(cmssw_base+'/src/'+self.eleDir+'/EleFR_Run2016_HWW36fb_jet25.root')
        self.fileElFR_jet35 = self._openRootFile(cmssw_base+'/src/'+self.eleDir+'/EleFR_Run2016_HWW36fb_jet35.root')
        self.fileElFR_jet45 = self._openRootFile(cmssw_base+'/src/'+self.eleDir+'/EleFR_Run2016_HWW36fb_jet45.root')

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


    def _getRate(self, h2, pt, eta, leptonptmax):

        aeta  = abs(eta)
        nbins = h2.GetNbinsX()
        ptmax = leptonptmax
        
        if (ptmax <= 0.) : ptmax = h2.GetXaxis().GetBinCenter(nbins)
        
        rate_value = h2.GetBinContent(h2.FindBin(min(pt, ptmax), aeta))
        rate_error = h2.GetBinError  (h2.FindBin(min(pt, ptmax), aeta))
        
        return rate_value, rate_error


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

class multiFakeWeightFiller(TreeCloner):

    def __init__(self):
        pass


    def __del__(self):
        pass


    def help(self):
        return '''Non-prompt event weights'''

    def addOptions(self,parser):
        description = self.help()
        group = optparse.OptionGroup(parser,self.label, description)
        group.add_option('-c', '--cmssw', dest='cmssw', help='cmssw version (naming convention may change)', default='763', type='string')
        group.add_option('-w', '--wpdic',   dest='WPdic', help='WP Dictionnary', default='LatinoAnalysis/Gardener/python/variables/LeptonSel_cfg.py', type='string')

        parser.add_option_group(group)
        return group


    def checkOptions(self,opts):
        cmssw_base = os.getenv('CMSSW_BASE')
        self.cmssw = opts.cmssw
        print " cmssw = ", self.cmssw

        self.WPdic = cmssw_base+'/src/'+opts.WPdic
        print self.WPdic
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

    def process(self,**kwargs):


        tree  = kwargs['tree']
        input = kwargs['input']
        output = kwargs['output']

        self.connect(tree,input)

        # (Re)Create target variables
        fakeVarExt =  [ '_2l0j', '_2l0jMuUp', '_2l0jMuDown', '_2l0jElUp', '_2l0jElDown', '_2l0jstatMuUp', '_2l0jstatMuDown', '_2l0jstatElUp', '_2l0jstatElDown',
                        '_2l1j', '_2l1jMuUp', '_2l1jMuDown', '_2l1jElUp', '_2l1jElDown', '_2l1jstatMuUp', '_2l1jstatMuDown', '_2l1jstatElUp', '_2l1jstatElDown',
                        '_2l2j', '_2l2jMuUp', '_2l2jMuDown', '_2l2jElUp', '_2l2jElDown', '_2l2jstatMuUp', '_2l2jstatMuDown', '_2l2jstatElUp', '_2l2jstatElDown',
                        '_3l',   '_3lMuUp',   '_3lMuDown',   '_3lElUp',   '_3lElDown',   '_3lstatMuUp',   '_3lstatMuDown',   '_3lstatElUp',   '_3lstatElDown',
                        '_4l',   '_4lMuUp',   '_4lMuDown',   '_4lElUp',   '_4lElDown',   '_4lstatMuUp',   '_4lstatMuDown',   '_4lstatElUp',   '_4lstatElDown' ]

        self.fakeVarNames = [ ]
        for iTag in self.FakeWeights:
          for iVarExt in fakeVarExt : self.fakeVarNames.append('fakeW_'+iTag+iVarExt)
        print self.fakeVarNames

        # Clone the tree with new branches added
        self.clone(output, self.fakeVarNames)
 
        # NOW CONNECT ALL NEW/TO BE MODIFIED BRANCEHES
        self.fakeVar = {}
        for bname in self.fakeVarNames:
          bvariable = numpy.ones(1, dtype=numpy.float32)
          self.fakeVar [bname] = bvariable
        for bname, bvariable in self.fakeVar.iteritems() : self.otree.Branch(bname,bvariable,bname+'/F')

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
       
            # Prepare leptons 
            Leptons = {}
            selectedLepton = 0
            for iLep in xrange(len(itree.std_vector_lepton_pt)) :

                # get kinematic
                pt      = itree.std_vector_lepton_pt     [iLep]
                eta     = itree.std_vector_lepton_eta    [iLep]
                flavour = itree.std_vector_lepton_flavour[iLep]

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
                     if abs (flavour) == 11 :
                       exec ('IsTightLepton = itree.std_vector_electron_isTightLepton_'+eleWP+'[iLep]')
                     elif abs (flavour) == 13 :
                       exec ('IsTightLepton = itree.std_vector_muon_isTightLepton_'+muWP+'[iLep]')
                     Leptons[iTag] = {} 
                     Leptons[iTag][selectedLepton] = [kindLep, pt, eta, IsTightLepton]

                   selectedLepton += 1
 
            # Now compute the fakes 
            for iTag in self.FakeWeights:

               self.fakeVar['fakeW_'+iTag+'_2l0j']          [0] = self.FakeWeights[iTag]['fakeW']._get2lWeight(Leptons, 'MuFR_jet20', 'ElFR_jet35', 'Nominal')
               self.fakeVar['fakeW_'+iTag+'_2l0jMuUp']      [0] = self.FakeWeights[iTag]['fakeW']._get2lWeight(Leptons, 'MuFR_jet30', 'ElFR_jet35', 'Nominal')
               self.fakeVar['fakeW_'+iTag+'_2l0jMuDown']    [0] = self.FakeWeights[iTag]['fakeW']._get2lWeight(Leptons, 'MuFR_jet10', 'ElFR_jet35', 'Nominal')
               self.fakeVar['fakeW_'+iTag+'_2l0jElUp']      [0] = self.FakeWeights[iTag]['fakeW']._get2lWeight(Leptons, 'MuFR_jet20', 'ElFR_jet45', 'Nominal')
               self.fakeVar['fakeW_'+iTag+'_2l0jElDown']    [0] = self.FakeWeights[iTag]['fakeW']._get2lWeight(Leptons, 'MuFR_jet20', 'ElFR_jet25', 'Nominal')
               self.fakeVar['fakeW_'+iTag+'_2l0jstatMuUp']  [0] = self.FakeWeights[iTag]['fakeW']._get2lWeight(Leptons, 'MuFR_jet20', 'ElFR_jet35', 'MuUp')
               self.fakeVar['fakeW_'+iTag+'_2l0jstatMuDown'][0] = self.FakeWeights[iTag]['fakeW']._get2lWeight(Leptons, 'MuFR_jet20', 'ElFR_jet35', 'MuDown')
               self.fakeVar['fakeW_'+iTag+'_2l0jstatElUp']  [0] = self.FakeWeights[iTag]['fakeW']._get2lWeight(Leptons, 'MuFR_jet20', 'ElFR_jet35', 'ElUp')
               self.fakeVar['fakeW_'+iTag+'_2l0jstatElDown'][0] = self.FakeWeights[iTag]['fakeW']._get2lWeight(Leptons, 'MuFR_jet20', 'ElFR_jet35', 'ElDown')
     
               self.fakeVar['fakeW_'+iTag+'_2l1j']          [0] = self.FakeWeights[iTag]['fakeW']._get2lWeight(Leptons, 'MuFR_jet25', 'ElFR_jet35', 'Nominal')
               self.fakeVar['fakeW_'+iTag+'_2l1jMuUp']      [0] = self.FakeWeights[iTag]['fakeW']._get2lWeight(Leptons, 'MuFR_jet35', 'ElFR_jet35', 'Nominal')
               self.fakeVar['fakeW_'+iTag+'_2l1jMuDown']    [0] = self.FakeWeights[iTag]['fakeW']._get2lWeight(Leptons, 'MuFR_jet15', 'ElFR_jet35', 'Nominal')
               self.fakeVar['fakeW_'+iTag+'_2l1jElUp']      [0] = self.FakeWeights[iTag]['fakeW']._get2lWeight(Leptons, 'MuFR_jet25', 'ElFR_jet45', 'Nominal')
               self.fakeVar['fakeW_'+iTag+'_2l1jElDown']    [0] = self.FakeWeights[iTag]['fakeW']._get2lWeight(Leptons, 'MuFR_jet25', 'ElFR_jet25', 'Nominal')
               self.fakeVar['fakeW_'+iTag+'_2l1jstatMuUp']  [0] = self.FakeWeights[iTag]['fakeW']._get2lWeight(Leptons, 'MuFR_jet25', 'ElFR_jet35', 'MuUp')
               self.fakeVar['fakeW_'+iTag+'_2l1jstatMuDown'][0] = self.FakeWeights[iTag]['fakeW']._get2lWeight(Leptons, 'MuFR_jet25', 'ElFR_jet35', 'MuDown')
               self.fakeVar['fakeW_'+iTag+'_2l1jstatElUp']  [0] = self.FakeWeights[iTag]['fakeW']._get2lWeight(Leptons, 'MuFR_jet25', 'ElFR_jet35', 'ElUp')
               self.fakeVar['fakeW_'+iTag+'_2l1jstatElDown'][0] = self.FakeWeights[iTag]['fakeW']._get2lWeight(Leptons, 'MuFR_jet25', 'ElFR_jet35', 'ElDown')

               self.fakeVar['fakeW_'+iTag+'_2l2j']          [0] = self.FakeWeights[iTag]['fakeW']._get2lWeight(Leptons, 'MuFR_jet35', 'ElFR_jet35', 'Nominal')
               self.fakeVar['fakeW_'+iTag+'_2l2jMuUp']      [0] = self.FakeWeights[iTag]['fakeW']._get2lWeight(Leptons, 'MuFR_jet45', 'ElFR_jet35', 'Nominal')
               self.fakeVar['fakeW_'+iTag+'_2l2jMuDown']    [0] = self.FakeWeights[iTag]['fakeW']._get2lWeight(Leptons, 'MuFR_jet25', 'ElFR_jet35', 'Nominal')
               self.fakeVar['fakeW_'+iTag+'_2l2jElUp']      [0] = self.FakeWeights[iTag]['fakeW']._get2lWeight(Leptons, 'MuFR_jet35', 'ElFR_jet45', 'Nominal')
               self.fakeVar['fakeW_'+iTag+'_2l2jElDown']    [0] = self.FakeWeights[iTag]['fakeW']._get2lWeight(Leptons, 'MuFR_jet35', 'ElFR_jet25', 'Nominal')
               self.fakeVar['fakeW_'+iTag+'_2l2jstatMuUp']  [0] = self.FakeWeights[iTag]['fakeW']._get2lWeight(Leptons, 'MuFR_jet35', 'ElFR_jet35', 'MuUp')
               self.fakeVar['fakeW_'+iTag+'_2l2jstatMuDown'][0] = self.FakeWeights[iTag]['fakeW']._get2lWeight(Leptons, 'MuFR_jet35', 'ElFR_jet35', 'MuDown')
               self.fakeVar['fakeW_'+iTag+'_2l2jstatElUp']  [0] = self.FakeWeights[iTag]['fakeW']._get2lWeight(Leptons, 'MuFR_jet35', 'ElFR_jet35', 'ElUp')
               self.fakeVar['fakeW_'+iTag+'_2l2jstatElDown'][0] = self.FakeWeights[iTag]['fakeW']._get2lWeight(Leptons, 'MuFR_jet35', 'ElFR_jet35', 'ElDown')

               self.fakeVar['fakeW_'+iTag+'_3l']            [0] = self.FakeWeights[iTag]['fakeW']._get3lWeight(Leptons, 'MuFR_jet35', 'ElFR_jet35', 'Nominal')
               self.fakeVar['fakeW_'+iTag+'_3lMuUp']        [0] = self.FakeWeights[iTag]['fakeW']._get3lWeight(Leptons, 'MuFR_jet45', 'ElFR_jet35', 'Nominal')
               self.fakeVar['fakeW_'+iTag+'_3lMuDown']      [0] = self.FakeWeights[iTag]['fakeW']._get3lWeight(Leptons, 'MuFR_jet25', 'ElFR_jet35', 'Nominal')
               self.fakeVar['fakeW_'+iTag+'_3lElUp']        [0] = self.FakeWeights[iTag]['fakeW']._get3lWeight(Leptons, 'MuFR_jet35', 'ElFR_jet45', 'Nominal')
               self.fakeVar['fakeW_'+iTag+'_3lElDown']      [0] = self.FakeWeights[iTag]['fakeW']._get3lWeight(Leptons, 'MuFR_jet35', 'ElFR_jet25', 'Nominal')
               self.fakeVar['fakeW_'+iTag+'_3lstatMuUp']    [0] = self.FakeWeights[iTag]['fakeW']._get3lWeight(Leptons, 'MuFR_jet35', 'ElFR_jet35', 'MuUp')
               self.fakeVar['fakeW_'+iTag+'_3lstatMuDown']  [0] = self.FakeWeights[iTag]['fakeW']._get3lWeight(Leptons, 'MuFR_jet35', 'ElFR_jet35', 'MuDown')
               self.fakeVar['fakeW_'+iTag+'_3lstatElUp']    [0] = self.FakeWeights[iTag]['fakeW']._get3lWeight(Leptons, 'MuFR_jet35', 'ElFR_jet35', 'ElUp')
               self.fakeVar['fakeW_'+iTag+'_3lstatElDown']  [0] = self.FakeWeights[iTag]['fakeW']._get3lWeight(Leptons, 'MuFR_jet35', 'ElFR_jet35', 'ElDown')

               self.fakeVar['fakeW_'+iTag+'_4l']            [0] = self.FakeWeights[iTag]['fakeW']._get4lWeight(Leptons, 'MuFR_jet35', 'ElFR_jet35', 'Nominal')
               self.fakeVar['fakeW_'+iTag+'_4lMuUp']        [0] = self.FakeWeights[iTag]['fakeW']._get4lWeight(Leptons, 'MuFR_jet45', 'ElFR_jet35', 'Nominal')
               self.fakeVar['fakeW_'+iTag+'_4lMuDown']      [0] = self.FakeWeights[iTag]['fakeW']._get4lWeight(Leptons, 'MuFR_jet25', 'ElFR_jet35', 'Nominal')
               self.fakeVar['fakeW_'+iTag+'_4lElUp']        [0] = self.FakeWeights[iTag]['fakeW']._get4lWeight(Leptons, 'MuFR_jet35', 'ElFR_jet45', 'Nominal')
               self.fakeVar['fakeW_'+iTag+'_4lElDown']      [0] = self.FakeWeights[iTag]['fakeW']._get4lWeight(Leptons, 'MuFR_jet35', 'ElFR_jet25', 'Nominal')
               self.fakeVar['fakeW_'+iTag+'_4lstatMuUp']    [0] = self.FakeWeights[iTag]['fakeW']._get4lWeight(Leptons, 'MuFR_jet35', 'ElFR_jet35', 'MuUp')
               self.fakeVar['fakeW_'+iTag+'_4lstatMuDown']  [0] = self.FakeWeights[iTag]['fakeW']._get4lWeight(Leptons, 'MuFR_jet35', 'ElFR_jet35', 'MuDown')
               self.fakeVar['fakeW_'+iTag+'_4lstatElUp']    [0] = self.FakeWeights[iTag]['fakeW']._get4lWeight(Leptons, 'MuFR_jet35', 'ElFR_jet35', 'ElUp')
               self.fakeVar['fakeW_'+iTag+'_4lstatElDown']  [0] = self.FakeWeights[iTag]['fakeW']._get4lWeight(Leptons, 'MuFR_jet35', 'ElFR_jet35', 'ElDown')


            savedentries+=1
            otree.Fill()

        self.disconnect()
        print '- Eventloop completed'
        print '   Saved: ', savedentries, ' events'

