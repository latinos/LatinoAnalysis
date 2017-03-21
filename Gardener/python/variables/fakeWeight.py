import optparse
import numpy
import ROOT
import os.path
import math

from LatinoAnalysis.Gardener.gardening import TreeCloner


#
#    ____|       |              \ \        /     _)         |      |         
#    |     _` |  |  /   _ \      \ \  \   /  _ \  |   _` |  __ \   __| 
#    __|  (   |    <    __/       \ \  \ /   __/  |  (   |  | | |  |   
#   _|   \__,_| _|\_\ \___|        \_/\_/  \___| _| \__, | _| |_| \__| 
#                                                   |___/                                                                                                                                         
#

#
# Origin: https://github.com/calderona/WW13TeV/blob/master/addWJet/addWJetsWeights.C
#


class FakeWeightFiller(TreeCloner):

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
        # new feature introduced for Full2016 (Jan 2017)
        group.add_option( '--idEleKind' , dest='idEleKind', help='kind of electron id', default=None) # e.g. "cut_WP_Tight80X"

        parser.add_option_group(group)
        return group


    def checkOptions(self,opts):
	cmssw_base = os.getenv('CMSSW_BASE')
        self.cmssw = opts.cmssw
        print " cmssw = ", self.cmssw
        self.idEleKind = opts.idEleKind
        print " idEleKind = ", self.idEleKind

        if self.cmssw == 'Full2016' and self.idEleKind in ['cut_WP_Tight80X'] :   

          self.fileMuPR = self._openRootFile(cmssw_base+'/src/LatinoAnalysis/Gardener/python/data/fake_prompt_rates/80X/HWW36fb/MuonPR_Run2016_HWW36fb.root')
          self.fileElPR = self._openRootFile(cmssw_base+'/src/LatinoAnalysis/Gardener/python/data/fake_prompt_rates/80X/HWW36fb/ElePR_'+self.idEleKind+'_Run2016_HWW36fb.root')

          self.fileMuFR_jet10 = self._openRootFile(cmssw_base+'/src/LatinoAnalysis/Gardener/python/data/fake_prompt_rates/80X/HWW36fb/MuonFR_Run2016_HWW36fb_jet10.root')
          self.fileMuFR_jet15 = self._openRootFile(cmssw_base+'/src/LatinoAnalysis/Gardener/python/data/fake_prompt_rates/80X/HWW36fb/MuonFR_Run2016_HWW36fb_jet15.root')
          self.fileMuFR_jet20 = self._openRootFile(cmssw_base+'/src/LatinoAnalysis/Gardener/python/data/fake_prompt_rates/80X/HWW36fb/MuonFR_Run2016_HWW36fb_jet20.root')
          self.fileMuFR_jet25 = self._openRootFile(cmssw_base+'/src/LatinoAnalysis/Gardener/python/data/fake_prompt_rates/80X/HWW36fb/MuonFR_Run2016_HWW36fb_jet25.root')
          self.fileMuFR_jet30 = self._openRootFile(cmssw_base+'/src/LatinoAnalysis/Gardener/python/data/fake_prompt_rates/80X/HWW36fb/MuonFR_Run2016_HWW36fb_jet30.root')
          self.fileMuFR_jet35 = self._openRootFile(cmssw_base+'/src/LatinoAnalysis/Gardener/python/data/fake_prompt_rates/80X/HWW36fb/MuonFR_Run2016_HWW36fb_jet35.root')
          self.fileMuFR_jet45 = self._openRootFile(cmssw_base+'/src/LatinoAnalysis/Gardener/python/data/fake_prompt_rates/80X/HWW36fb/MuonFR_Run2016_HWW36fb_jet45.root')

          self.fileElFR_jet25 = self._openRootFile(cmssw_base+'/src/LatinoAnalysis/Gardener/python/data/fake_prompt_rates/80X/HWW36fb/EleFR_'+self.idEleKind+'_Run2016_HWW36fb_jet25.root')
          self.fileElFR_jet35 = self._openRootFile(cmssw_base+'/src/LatinoAnalysis/Gardener/python/data/fake_prompt_rates/80X/HWW36fb/EleFR_'+self.idEleKind+'_Run2016_HWW36fb_jet35.root')
          self.fileElFR_jet45 = self._openRootFile(cmssw_base+'/src/LatinoAnalysis/Gardener/python/data/fake_prompt_rates/80X/HWW36fb/EleFR_'+self.idEleKind+'_Run2016_HWW36fb_jet45.root')

        elif self.cmssw == 'ICHEP2016' : 


          self.fileMuPR = self._openRootFile(cmssw_base+'/src/LatinoAnalysis/Gardener/python/data/fake_prompt_rates/80X/HWW12.9fb_repro/MuonPR_Run2016_HWW12fb.root')
          self.fileElPR = self._openRootFile(cmssw_base+'/src/LatinoAnalysis/Gardener/python/data/fake_prompt_rates/80X/HWW12.9fb_repro/ElePR_Run2016_HWW12fb.root')

          self.fileMuFR_jet10 = self._openRootFile(cmssw_base+'/src/LatinoAnalysis/Gardener/python/data/fake_prompt_rates/80X/HWW12.9fb_repro/MuonFR_Run2016_HWW12fb_jet10.root')
          self.fileMuFR_jet15 = self._openRootFile(cmssw_base+'/src/LatinoAnalysis/Gardener/python/data/fake_prompt_rates/80X/HWW12.9fb_repro/MuonFR_Run2016_HWW12fb_jet15.root')
          self.fileMuFR_jet20 = self._openRootFile(cmssw_base+'/src/LatinoAnalysis/Gardener/python/data/fake_prompt_rates/80X/HWW12.9fb_repro/MuonFR_Run2016_HWW12fb_jet20.root')
          self.fileMuFR_jet25 = self._openRootFile(cmssw_base+'/src/LatinoAnalysis/Gardener/python/data/fake_prompt_rates/80X/HWW12.9fb_repro/MuonFR_Run2016_HWW12fb_jet25.root')
          self.fileMuFR_jet30 = self._openRootFile(cmssw_base+'/src/LatinoAnalysis/Gardener/python/data/fake_prompt_rates/80X/HWW12.9fb_repro/MuonFR_Run2016_HWW12fb_jet30.root')
          self.fileMuFR_jet35 = self._openRootFile(cmssw_base+'/src/LatinoAnalysis/Gardener/python/data/fake_prompt_rates/80X/HWW12.9fb_repro/MuonFR_Run2016_HWW12fb_jet35.root')
          self.fileMuFR_jet45 = self._openRootFile(cmssw_base+'/src/LatinoAnalysis/Gardener/python/data/fake_prompt_rates/80X/HWW12.9fb_repro/MuonFR_Run2016_HWW12fb_jet45.root')
                                                                                                                        
          self.fileElFR_jet25 = self._openRootFile(cmssw_base+'/src/LatinoAnalysis/Gardener/python/data/fake_prompt_rates/80X/HWW12.9fb_repro/EleFR_Run2016_HWW12fb_jet25.root')
          self.fileElFR_jet35 = self._openRootFile(cmssw_base+'/src/LatinoAnalysis/Gardener/python/data/fake_prompt_rates/80X/HWW12.9fb_repro/EleFR_Run2016_HWW12fb_jet35.root')
          self.fileElFR_jet45 = self._openRootFile(cmssw_base+'/src/LatinoAnalysis/Gardener/python/data/fake_prompt_rates/80X/HWW12.9fb_repro/EleFR_Run2016_HWW12fb_jet45.root')


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
    def _get2lWeight(self, leptons, MuFR, ElFR, stat):

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
    def _get3lWeight(self, leptons, MuFR, ElFR, stat):

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
    def _get4lWeight(self, leptons, MuFR, ElFR, stat):

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


    def process(self,**kwargs):
        tree   = kwargs['tree']
        input  = kwargs['input']
        output = kwargs['output']

        self.connect(tree,input)
         
        self.fakeVariables = [ 'fakeW2l0j', 'fakeW2l0jMuUp', 'fakeW2l0jMuDown', 'fakeW2l0jElUp', 'fakeW2l0jElDown', 'fakeW2l0jstatMuUp', 'fakeW2l0jstatMuDown', 'fakeW2l0jstatElUp', 'fakeW2l0jstatElDown',
                               'fakeW2l1j', 'fakeW2l1jMuUp', 'fakeW2l1jMuDown', 'fakeW2l1jElUp', 'fakeW2l1jElDown', 'fakeW2l1jstatMuUp', 'fakeW2l1jstatMuDown', 'fakeW2l1jstatElUp', 'fakeW2l1jstatElDown',
                               'fakeW2l2j', 'fakeW2l2jMuUp', 'fakeW2l2jMuDown', 'fakeW2l2jElUp', 'fakeW2l2jElDown', 'fakeW2l2jstatMuUp', 'fakeW2l2jstatMuDown', 'fakeW2l2jstatElUp', 'fakeW2l2jstatElDown',
                               'fakeW3l',   'fakeW3lMuUp',   'fakeW3lMuDown',   'fakeW3lElUp',   'fakeW3lElDown',   'fakeW3lstatMuUp',   'fakeW3lstatMuDown',   'fakeW3lstatElUp',   'fakeW3lstatElDown',
                               'fakeW4l',   'fakeW4lMuUp',   'fakeW4lMuDown',   'fakeW4lElUp',   'fakeW4lElDown',   'fakeW4lstatMuUp',   'fakeW4lstatMuDown',   'fakeW4lstatElUp',   'fakeW4lstatElDown' ]

        # Clone the tree with new branches added
        self.clone(output, self.fakeVariables)
      
        fakeW2l0j           = numpy.ones(1, dtype=numpy.float32)
        fakeW2l0jMuUp       = numpy.ones(1, dtype=numpy.float32)
        fakeW2l0jMuDown     = numpy.ones(1, dtype=numpy.float32)
        fakeW2l0jElUp       = numpy.ones(1, dtype=numpy.float32)
        fakeW2l0jElDown     = numpy.ones(1, dtype=numpy.float32)
        fakeW2l0jstatMuUp   = numpy.ones(1, dtype=numpy.float32)
        fakeW2l0jstatMuDown = numpy.ones(1, dtype=numpy.float32)
        fakeW2l0jstatElUp   = numpy.ones(1, dtype=numpy.float32)
        fakeW2l0jstatElDown = numpy.ones(1, dtype=numpy.float32)

        fakeW2l1j           = numpy.ones(1, dtype=numpy.float32)
        fakeW2l1jMuUp       = numpy.ones(1, dtype=numpy.float32)
        fakeW2l1jMuDown     = numpy.ones(1, dtype=numpy.float32)
        fakeW2l1jElUp       = numpy.ones(1, dtype=numpy.float32)
        fakeW2l1jElDown     = numpy.ones(1, dtype=numpy.float32)
        fakeW2l1jstatMuUp   = numpy.ones(1, dtype=numpy.float32)
        fakeW2l1jstatMuDown = numpy.ones(1, dtype=numpy.float32)
        fakeW2l1jstatElUp   = numpy.ones(1, dtype=numpy.float32)
        fakeW2l1jstatElDown = numpy.ones(1, dtype=numpy.float32)

        fakeW2l2j           = numpy.ones(1, dtype=numpy.float32)
        fakeW2l2jMuUp       = numpy.ones(1, dtype=numpy.float32)
        fakeW2l2jMuDown     = numpy.ones(1, dtype=numpy.float32)
        fakeW2l2jElUp       = numpy.ones(1, dtype=numpy.float32)
        fakeW2l2jElDown     = numpy.ones(1, dtype=numpy.float32)
        fakeW2l2jstatMuUp   = numpy.ones(1, dtype=numpy.float32)
        fakeW2l2jstatMuDown = numpy.ones(1, dtype=numpy.float32)
        fakeW2l2jstatElUp   = numpy.ones(1, dtype=numpy.float32)
        fakeW2l2jstatElDown = numpy.ones(1, dtype=numpy.float32)

        fakeW3l           = numpy.ones(1, dtype=numpy.float32)
        fakeW3lMuUp       = numpy.ones(1, dtype=numpy.float32)
        fakeW3lMuDown     = numpy.ones(1, dtype=numpy.float32)
        fakeW3lElUp       = numpy.ones(1, dtype=numpy.float32)
        fakeW3lElDown     = numpy.ones(1, dtype=numpy.float32)
        fakeW3lstatMuUp   = numpy.ones(1, dtype=numpy.float32)
        fakeW3lstatMuDown = numpy.ones(1, dtype=numpy.float32)
        fakeW3lstatElUp   = numpy.ones(1, dtype=numpy.float32)
        fakeW3lstatElDown = numpy.ones(1, dtype=numpy.float32)

        fakeW4l           = numpy.ones(1, dtype=numpy.float32)
        fakeW4lMuUp       = numpy.ones(1, dtype=numpy.float32)
        fakeW4lMuDown     = numpy.ones(1, dtype=numpy.float32)
        fakeW4lElUp       = numpy.ones(1, dtype=numpy.float32)
        fakeW4lElDown     = numpy.ones(1, dtype=numpy.float32)
        fakeW4lstatMuUp   = numpy.ones(1, dtype=numpy.float32)
        fakeW4lstatMuDown = numpy.ones(1, dtype=numpy.float32)
        fakeW4lstatElUp   = numpy.ones(1, dtype=numpy.float32)
        fakeW4lstatElDown = numpy.ones(1, dtype=numpy.float32)

        self.otree.Branch('fakeW2l0j',           fakeW2l0j,           'fakeW2l0j/F')
        self.otree.Branch('fakeW2l0jMuUp',       fakeW2l0jMuUp,       'fakeW2l0jMuUp/F')
        self.otree.Branch('fakeW2l0jMuDown',     fakeW2l0jMuDown,     'fakeW2l0jMuDown/F')
        self.otree.Branch('fakeW2l0jElUp',       fakeW2l0jElUp,       'fakeW2l0jElUp/F')
        self.otree.Branch('fakeW2l0jElDown',     fakeW2l0jElDown,     'fakeW2l0jElDown/F')
        self.otree.Branch('fakeW2l0jstatMuUp',   fakeW2l0jstatMuUp,   'fakeW2l0jstatMuUp/F')
        self.otree.Branch('fakeW2l0jstatMuDown', fakeW2l0jstatMuDown, 'fakeW2l0jstatMuDown/F')
        self.otree.Branch('fakeW2l0jstatElUp',   fakeW2l0jstatElUp,   'fakeW2l0jstatElUp/F')
        self.otree.Branch('fakeW2l0jstatElDown', fakeW2l0jstatElDown, 'fakeW2l0jstatElDown/F')

        self.otree.Branch('fakeW2l1j',           fakeW2l1j,           'fakeW2l1j/F')
        self.otree.Branch('fakeW2l1jMuUp',       fakeW2l1jMuUp,       'fakeW2l1jMuUp/F')
        self.otree.Branch('fakeW2l1jMuDown',     fakeW2l1jMuDown,     'fakeW2l1jMuDown/F')
        self.otree.Branch('fakeW2l1jElUp',       fakeW2l1jElUp,       'fakeW2l1jElUp/F')
        self.otree.Branch('fakeW2l1jElDown',     fakeW2l1jElDown,     'fakeW2l1jElDown/F')
        self.otree.Branch('fakeW2l1jstatMuUp',   fakeW2l1jstatMuUp,   'fakeW2l1jstatMuUp/F')
        self.otree.Branch('fakeW2l1jstatMuDown', fakeW2l1jstatMuDown, 'fakeW2l1jstatMuDown/F')
        self.otree.Branch('fakeW2l1jstatElUp',   fakeW2l1jstatElUp,   'fakeW2l1jstatElUp/F')
        self.otree.Branch('fakeW2l1jstatElDown', fakeW2l1jstatElDown, 'fakeW2l1jstatElDown/F')

        self.otree.Branch('fakeW2l2j',           fakeW2l2j,           'fakeW2l2j/F')
        self.otree.Branch('fakeW2l2jMuUp',       fakeW2l2jMuUp,       'fakeW2l2jMuUp/F')
        self.otree.Branch('fakeW2l2jMuDown',     fakeW2l2jMuDown,     'fakeW2l2jMuDown/F')
        self.otree.Branch('fakeW2l2jElUp',       fakeW2l2jElUp,       'fakeW2l2jElUp/F')
        self.otree.Branch('fakeW2l2jElDown',     fakeW2l2jElDown,     'fakeW2l2jElDown/F')
        self.otree.Branch('fakeW2l2jstatMuUp',   fakeW2l2jstatMuUp,   'fakeW2l2jstatMuUp/F')
        self.otree.Branch('fakeW2l2jstatMuDown', fakeW2l2jstatMuDown, 'fakeW2l2jstatMuDown/F')
        self.otree.Branch('fakeW2l2jstatElUp',   fakeW2l2jstatElUp,   'fakeW2l2jstatElUp/F')
        self.otree.Branch('fakeW2l2jstatElDown', fakeW2l2jstatElDown, 'fakeW2l2jstatElDown/F')

        self.otree.Branch('fakeW3l',           fakeW3l,           'fakeW3l/F')
        self.otree.Branch('fakeW3lMuUp',       fakeW3lMuUp,       'fakeW3lMuUp/F')
        self.otree.Branch('fakeW3lMuDown',     fakeW3lMuDown,     'fakeW3lMuDown/F')
        self.otree.Branch('fakeW3lElUp',       fakeW3lElUp,       'fakeW3lElUp/F')
        self.otree.Branch('fakeW3lElDown',     fakeW3lElDown,     'fakeW3lElDown/F')
        self.otree.Branch('fakeW3lstatMuUp',   fakeW3lstatMuUp,   'fakeW3lstatMuUp/F')
        self.otree.Branch('fakeW3lstatMuDown', fakeW3lstatMuDown, 'fakeW3lstatMuDown/F')
        self.otree.Branch('fakeW3lstatElUp',   fakeW3lstatElUp,   'fakeW3lstatElUp/F')
        self.otree.Branch('fakeW3lstatElDown', fakeW3lstatElDown, 'fakeW3lstatElDown/F')

        self.otree.Branch('fakeW4l',           fakeW4l,           'fakeW4l/F')
        self.otree.Branch('fakeW4lMuUp',       fakeW4lMuUp,       'fakeW4lMuUp/F')
        self.otree.Branch('fakeW4lMuDown',     fakeW4lMuDown,     'fakeW4lMuDown/F')
        self.otree.Branch('fakeW4lElUp',       fakeW4lElUp,       'fakeW4lElUp/F')
        self.otree.Branch('fakeW4lElDown',     fakeW4lElDown,     'fakeW4lElDown/F')
        self.otree.Branch('fakeW4lstatMuUp',   fakeW4lstatMuUp,   'fakeW4lstatMuUp/F')
        self.otree.Branch('fakeW4lstatMuDown', fakeW4lstatMuDown, 'fakeW4lstatMuDown/F')
        self.otree.Branch('fakeW4lstatElUp',   fakeW4lstatElUp,   'fakeW4lstatElUp/F')
        self.otree.Branch('fakeW4lstatElDown', fakeW4lstatElDown, 'fakeW4lstatElDown/F')

        nentries = self.itree.GetEntries()
        print ' - Input entries:', nentries
        savedentries = 0
                
        # avoid dots to go faster
        itree = self.itree
        otree = self.otree

        print ' - Starting event loop'
        step = 5000

        for i in xrange(nentries):
            itree.GetEntry(i)

            # print event count
            if (i > 0 and i%step == 0.) : print i,'events processed'

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
                   IsTightLepton = itree.std_vector_lepton_isTightLepton[iLep]
                   
                   Leptons[selectedLepton] = [kindLep, pt, eta, IsTightLepton]

                   selectedLepton += 1


            fakeW2l0j          [0] = self._get2lWeight(Leptons, self.MuFR_jet20, self.ElFR_jet35, 'Nominal')
            fakeW2l0jMuUp      [0] = self._get2lWeight(Leptons, self.MuFR_jet30, self.ElFR_jet35, 'Nominal')
            fakeW2l0jMuDown    [0] = self._get2lWeight(Leptons, self.MuFR_jet10, self.ElFR_jet35, 'Nominal')
            fakeW2l0jElUp      [0] = self._get2lWeight(Leptons, self.MuFR_jet20, self.ElFR_jet45, 'Nominal')
            fakeW2l0jElDown    [0] = self._get2lWeight(Leptons, self.MuFR_jet20, self.ElFR_jet25, 'Nominal')
            fakeW2l0jstatMuUp  [0] = self._get2lWeight(Leptons, self.MuFR_jet20, self.ElFR_jet35, 'MuUp')
            fakeW2l0jstatMuDown[0] = self._get2lWeight(Leptons, self.MuFR_jet20, self.ElFR_jet35, 'MuDown')
            fakeW2l0jstatElUp  [0] = self._get2lWeight(Leptons, self.MuFR_jet20, self.ElFR_jet35, 'ElUp')
            fakeW2l0jstatElDown[0] = self._get2lWeight(Leptons, self.MuFR_jet20, self.ElFR_jet35, 'ElDown')

            fakeW2l1j          [0] = self._get2lWeight(Leptons, self.MuFR_jet25, self.ElFR_jet35, 'Nominal')
            fakeW2l1jMuUp      [0] = self._get2lWeight(Leptons, self.MuFR_jet35, self.ElFR_jet35, 'Nominal')
            fakeW2l1jMuDown    [0] = self._get2lWeight(Leptons, self.MuFR_jet15, self.ElFR_jet35, 'Nominal')
            fakeW2l1jElUp      [0] = self._get2lWeight(Leptons, self.MuFR_jet25, self.ElFR_jet45, 'Nominal')
            fakeW2l1jElDown    [0] = self._get2lWeight(Leptons, self.MuFR_jet25, self.ElFR_jet25, 'Nominal')
            fakeW2l1jstatMuUp  [0] = self._get2lWeight(Leptons, self.MuFR_jet25, self.ElFR_jet35, 'MuUp')
            fakeW2l1jstatMuDown[0] = self._get2lWeight(Leptons, self.MuFR_jet25, self.ElFR_jet35, 'MuDown')
            fakeW2l1jstatElUp  [0] = self._get2lWeight(Leptons, self.MuFR_jet25, self.ElFR_jet35, 'ElUp')
            fakeW2l1jstatElDown[0] = self._get2lWeight(Leptons, self.MuFR_jet25, self.ElFR_jet35, 'ElDown')

            fakeW2l2j          [0] = self._get2lWeight(Leptons, self.MuFR_jet35, self.ElFR_jet35, 'Nominal')
            fakeW2l2jMuUp      [0] = self._get2lWeight(Leptons, self.MuFR_jet45, self.ElFR_jet35, 'Nominal')
            fakeW2l2jMuDown    [0] = self._get2lWeight(Leptons, self.MuFR_jet25, self.ElFR_jet35, 'Nominal')
            fakeW2l2jElUp      [0] = self._get2lWeight(Leptons, self.MuFR_jet35, self.ElFR_jet45, 'Nominal')
            fakeW2l2jElDown    [0] = self._get2lWeight(Leptons, self.MuFR_jet35, self.ElFR_jet25, 'Nominal')
            fakeW2l2jstatMuUp  [0] = self._get2lWeight(Leptons, self.MuFR_jet35, self.ElFR_jet35, 'MuUp')
            fakeW2l2jstatMuDown[0] = self._get2lWeight(Leptons, self.MuFR_jet35, self.ElFR_jet35, 'MuDown')
            fakeW2l2jstatElUp  [0] = self._get2lWeight(Leptons, self.MuFR_jet35, self.ElFR_jet35, 'ElUp')
            fakeW2l2jstatElDown[0] = self._get2lWeight(Leptons, self.MuFR_jet35, self.ElFR_jet35, 'ElDown')

            fakeW3l          [0] = self._get3lWeight(Leptons, self.MuFR_jet35, self.ElFR_jet35, 'Nominal')
            fakeW3lMuUp      [0] = self._get3lWeight(Leptons, self.MuFR_jet45, self.ElFR_jet35, 'Nominal')
            fakeW3lMuDown    [0] = self._get3lWeight(Leptons, self.MuFR_jet25, self.ElFR_jet35, 'Nominal')
            fakeW3lElUp      [0] = self._get3lWeight(Leptons, self.MuFR_jet35, self.ElFR_jet45, 'Nominal')
            fakeW3lElDown    [0] = self._get3lWeight(Leptons, self.MuFR_jet35, self.ElFR_jet25, 'Nominal')
            fakeW3lstatMuUp  [0] = self._get3lWeight(Leptons, self.MuFR_jet35, self.ElFR_jet35, 'MuUp')
            fakeW3lstatMuDown[0] = self._get3lWeight(Leptons, self.MuFR_jet35, self.ElFR_jet35, 'MuDown')
            fakeW3lstatElUp  [0] = self._get3lWeight(Leptons, self.MuFR_jet35, self.ElFR_jet35, 'ElUp')
            fakeW3lstatElDown[0] = self._get3lWeight(Leptons, self.MuFR_jet35, self.ElFR_jet35, 'ElDown')

            fakeW4l          [0] = self._get4lWeight(Leptons, self.MuFR_jet35, self.ElFR_jet35, 'Nominal')
            fakeW4lMuUp      [0] = self._get4lWeight(Leptons, self.MuFR_jet45, self.ElFR_jet35, 'Nominal')
            fakeW4lMuDown    [0] = self._get4lWeight(Leptons, self.MuFR_jet25, self.ElFR_jet35, 'Nominal')
            fakeW4lElUp      [0] = self._get4lWeight(Leptons, self.MuFR_jet35, self.ElFR_jet45, 'Nominal')
            fakeW4lElDown    [0] = self._get4lWeight(Leptons, self.MuFR_jet35, self.ElFR_jet25, 'Nominal')
            fakeW4lstatMuUp  [0] = self._get4lWeight(Leptons, self.MuFR_jet35, self.ElFR_jet35, 'MuUp')
            fakeW4lstatMuDown[0] = self._get4lWeight(Leptons, self.MuFR_jet35, self.ElFR_jet35, 'MuDown')
            fakeW4lstatElUp  [0] = self._get4lWeight(Leptons, self.MuFR_jet35, self.ElFR_jet35, 'ElUp')
            fakeW4lstatElDown[0] = self._get4lWeight(Leptons, self.MuFR_jet35, self.ElFR_jet35, 'ElDown')
              
            otree.Fill()
            savedentries += 1

        self.disconnect()
        print ' - Event loop completed'
        print '   Saved entries:', savedentries
