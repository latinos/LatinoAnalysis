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
# origin: https://github.com/calderona/WW13TeV/blob/master/addWJet/addWJetsWeights.C
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
        parser.add_option_group(group)
        return group


    def checkOptions(self,opts):
        pass


    def _getWeight(self, kindLep, pt, eta, istight):

        # FIXME function to be defined
        
        return 1.0, 0.0, 0.0


    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # _get2lWeight
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def _get2lWeight(self, leptons, muonThreshold, electronThreshold, stat):

        if (len(leptons) < 2) :

            return 0.0

        else :

            promptProbability = numpy.ones(2, dtype=numpy.float32)
            fakeProbability   = numpy.ones(2, dtype=numpy.float32)

            ntight = 0

            for i in leptons :

                if (i > 1) : break
                
                p = 1.0  # lep.pr;

                f  = 0.0
                fE = 0.0

                if (leptons[i][0] == 'mu') :

                    f  = 0.05  # GetFactor     (MuonFR[mu],  lep.pt, lep.eta, muonThreshold);
                    fE = 0.02  # GetFactorError(MuonFR[mu],  lep.pt, lep.eta, muonThreshold);

                    if   (stat == 'MuUp')   : f = f + fE
                    elif (stat == 'MuDown') : f = f - fE

                elif (leptons[i][0] == 'el') :

                    f  = 0.03  # GetFactor     (ElecFR[ele],  lep.pt, lep.eta, electronThreshold);
                    fE = 0.01  # GetFactorError(ElecFR[ele],  lep.pt, lep.eta, electronThreshold);

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


    def process(self,**kwargs):
        tree   = kwargs['tree']
        input  = kwargs['input']
        output = kwargs['output']

        self.connect(tree,input)
         
        self.fakeVariables = [ 'fakeW2l0j', 'fakeW2l0jMuUp', 'fakeW2l0jMuDown', 'fakeW2l0jElUp', 'fakeW2l0jElDown', 'fakeW2l0jstatMuUp', 'fakeW2l0jstatMuDown', 'fakeW2l0jstatElUp', 'fakeW2l0jstatElDown',
                               'fakeW2l1j', 'fakeW2l1jMuUp', 'fakeW2l1jMuDown', 'fakeW2l1jElUp', 'fakeW2l1jElDown', 'fakeW2l1jstatMuUp', 'fakeW2l1jstatMuDown', 'fakeW2l1jstatElUp', 'fakeW2l1jstatElDown',
                               'fakeW2l2j', 'fakeW2l2jMuUp', 'fakeW2l2jMuDown', 'fakeW2l2jElUp', 'fakeW2l2jElDown', 'fakeW2l2jstatMuUp', 'fakeW2l2jstatMuDown', 'fakeW2l2jstatElUp', 'fakeW2l2jstatElDown' ]
        
        # Clone the tree with new branches added
        self.clone(output, self.fakeVariables)
      
        # Nominal values
        fakeW2l0j = numpy.ones(1, dtype=numpy.float32)
        fakeW2l1j = numpy.ones(1, dtype=numpy.float32)
        fakeW2l2j = numpy.ones(1, dtype=numpy.float32)

        # Jet pt up/down
        fakeW2l0jMuUp   = numpy.ones(1, dtype=numpy.float32)
        fakeW2l1jMuUp   = numpy.ones(1, dtype=numpy.float32)
        fakeW2l2jMuUp   = numpy.ones(1, dtype=numpy.float32)
        fakeW2l0jMuDown = numpy.ones(1, dtype=numpy.float32)
        fakeW2l1jMuDown = numpy.ones(1, dtype=numpy.float32)
        fakeW2l2jMuDown = numpy.ones(1, dtype=numpy.float32)
        fakeW2l0jElUp   = numpy.ones(1, dtype=numpy.float32)
        fakeW2l1jElUp   = numpy.ones(1, dtype=numpy.float32)
        fakeW2l2jElUp   = numpy.ones(1, dtype=numpy.float32)
        fakeW2l0jElDown = numpy.ones(1, dtype=numpy.float32)
        fakeW2l1jElDown = numpy.ones(1, dtype=numpy.float32)
        fakeW2l2jElDown = numpy.ones(1, dtype=numpy.float32)

        # Fake rate statistical error up/down
        fakeW2l0jstatMuUp   = numpy.ones(1, dtype=numpy.float32)
        fakeW2l1jstatMuUp   = numpy.ones(1, dtype=numpy.float32)
        fakeW2l2jstatMuUp   = numpy.ones(1, dtype=numpy.float32)
        fakeW2l0jstatMuDown = numpy.ones(1, dtype=numpy.float32)
        fakeW2l1jstatMuDown = numpy.ones(1, dtype=numpy.float32)
        fakeW2l2jstatMuDown = numpy.ones(1, dtype=numpy.float32)
        fakeW2l0jstatElUp   = numpy.ones(1, dtype=numpy.float32)
        fakeW2l1jstatElUp   = numpy.ones(1, dtype=numpy.float32)
        fakeW2l2jstatElUp   = numpy.ones(1, dtype=numpy.float32)
        fakeW2l0jstatElDown = numpy.ones(1, dtype=numpy.float32)
        fakeW2l1jstatElDown = numpy.ones(1, dtype=numpy.float32)
        fakeW2l2jstatElDown = numpy.ones(1, dtype=numpy.float32)

        self.otree.Branch('fakeW2l0j', fakeW2l0j, 'fakeW2l0j/F')
        self.otree.Branch('fakeW2l1j', fakeW2l1j, 'fakeW2l1j/F')
        self.otree.Branch('fakeW2l2j', fakeW2l2j, 'fakeW2l2j/F')

        self.otree.Branch('fakeW2l0jMuUp',   fakeW2l0jMuUp,   'fakeW2l0jMuUp/F')
        self.otree.Branch('fakeW2l1jMuUp',   fakeW2l1jMuUp,   'fakeW2l1jMuUp/F')
        self.otree.Branch('fakeW2l2jMuUp',   fakeW2l2jMuUp,   'fakeW2l2jMuUp/F')
        self.otree.Branch('fakeW2l0jMuDown', fakeW2l0jMuDown, 'fakeW2l0jMuDown/F')
        self.otree.Branch('fakeW2l1jMuDown', fakeW2l1jMuDown, 'fakeW2l1jMuDown/F')
        self.otree.Branch('fakeW2l2jMuDown', fakeW2l2jMuDown, 'fakeW2l2jMuDown/F')
        self.otree.Branch('fakeW2l0jElUp',   fakeW2l0jElUp,   'fakeW2l0jElUp/F')
        self.otree.Branch('fakeW2l1jElUp',   fakeW2l1jElUp,   'fakeW2l1jElUp/F')
        self.otree.Branch('fakeW2l2jElUp',   fakeW2l2jElUp,   'fakeW2l2jElUp/F')
        self.otree.Branch('fakeW2l0jElDown', fakeW2l0jElDown, 'fakeW2l0jElDown/F')
        self.otree.Branch('fakeW2l1jElDown', fakeW2l1jElDown, 'fakeW2l1jElDown/F')
        self.otree.Branch('fakeW2l2jElDown', fakeW2l2jElDown, 'fakeW2l2jElDown/F')

        self.otree.Branch('fakeW2l0jstatMuUp',   fakeW2l0jstatMuUp,   'fakeW2l0jstatMuUp/F')
        self.otree.Branch('fakeW2l1jstatMuUp',   fakeW2l1jstatMuUp,   'fakeW2l1jstatMuUp/F')
        self.otree.Branch('fakeW2l2jstatMuUp',   fakeW2l2jstatMuUp,   'fakeW2l2jstatMuUp/F')
        self.otree.Branch('fakeW2l0jstatMuDown', fakeW2l0jstatMuDown, 'fakeW2l0jstatMuDown/F')
        self.otree.Branch('fakeW2l1jstatMuDown', fakeW2l1jstatMuDown, 'fakeW2l1jstatMuDown/F')
        self.otree.Branch('fakeW2l2jstatMuDown', fakeW2l2jstatMuDown, 'fakeW2l2jstatMuDown/F')
        self.otree.Branch('fakeW2l0jstatElUp',   fakeW2l0jstatElUp,   'fakeW2l0jstatElUp/F')
        self.otree.Branch('fakeW2l1jstatElUp',   fakeW2l1jstatElUp,   'fakeW2l1jstatElUp/F')
        self.otree.Branch('fakeW2l2jstatElUp',   fakeW2l2jstatElUp,   'fakeW2l2jstatElUp/F')
        self.otree.Branch('fakeW2l0jstatElDown', fakeW2l0jstatElDown, 'fakeW2l0jstatElDown/F')
        self.otree.Branch('fakeW2l1jstatElDown', fakeW2l1jstatElDown, 'fakeW2l1jstatElDown/F')
        self.otree.Branch('fakeW2l2jstatElDown', fakeW2l2jstatElDown, 'fakeW2l2jstatElDown/F')

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
                   
                   # get the weight, the error up and the error down
                   # FIXME: possibility to extend to more nuisances, like having the statistical nuisance separate.
                   weight, weigth_error_up, weigth_error_do = self._getWeight(kindLep, pt, eta, IsTightLepton)
                   
                   Leptons[selectedLepton] = [kindLep, pt, eta, IsTightLepton, weight, weigth_error_up, weigth_error_do]

                   selectedLepton += 1

            #                                                   mu  ele
            fakeW2l0j          [0] = self._get2lWeight(Leptons, 20, 35, 'Nominal')
            fakeW2l0jMuUp      [0] = self._get2lWeight(Leptons, 30, 35, 'Nominal')
            fakeW2l0jMuDown    [0] = self._get2lWeight(Leptons, 10, 35, 'Nominal')
            fakeW2l0jElUp      [0] = self._get2lWeight(Leptons, 20, 45, 'Nominal')
            fakeW2l0jElDown    [0] = self._get2lWeight(Leptons, 20, 25, 'Nominal')
            fakeW2l0jstatMuUp  [0] = self._get2lWeight(Leptons, 20, 35, 'MuUp')
            fakeW2l0jstatMuDown[0] = self._get2lWeight(Leptons, 20, 35, 'MuDown')
            fakeW2l0jstatElUp  [0] = self._get2lWeight(Leptons, 20, 35, 'ElUp')
            fakeW2l0jstatElDown[0] = self._get2lWeight(Leptons, 20, 35, 'ElDown')

            fakeW2l1j          [0] = self._get2lWeight(Leptons, 25, 35, 'Nominal')
            fakeW2l1jMuUp      [0] = self._get2lWeight(Leptons, 35, 35, 'Nominal')
            fakeW2l1jMuDown    [0] = self._get2lWeight(Leptons, 15, 35, 'Nominal')
            fakeW2l1jElUp      [0] = self._get2lWeight(Leptons, 25, 45, 'Nominal')
            fakeW2l1jElDown    [0] = self._get2lWeight(Leptons, 25, 25, 'Nominal')
            fakeW2l1jstatMuUp  [0] = self._get2lWeight(Leptons, 25, 35, 'MuUp')
            fakeW2l1jstatMuDown[0] = self._get2lWeight(Leptons, 25, 35, 'MuDown')
            fakeW2l1jstatElUp  [0] = self._get2lWeight(Leptons, 25, 35, 'ElUp')
            fakeW2l1jstatElDown[0] = self._get2lWeight(Leptons, 25, 35, 'ElDown')

            fakeW2l2j          [0] = self._get2lWeight(Leptons, 35, 35, 'Nominal')
            fakeW2l2jMuUp      [0] = self._get2lWeight(Leptons, 45, 35, 'Nominal')
            fakeW2l2jMuDown    [0] = self._get2lWeight(Leptons, 25, 35, 'Nominal')
            fakeW2l2jElUp      [0] = self._get2lWeight(Leptons, 35, 45, 'Nominal')
            fakeW2l2jElDown    [0] = self._get2lWeight(Leptons, 35, 25, 'Nominal')
            fakeW2l2jstatMuUp  [0] = self._get2lWeight(Leptons, 35, 35, 'MuUp')
            fakeW2l2jstatMuDown[0] = self._get2lWeight(Leptons, 35, 35, 'MuDown')
            fakeW2l2jstatElUp  [0] = self._get2lWeight(Leptons, 35, 35, 'ElUp')
            fakeW2l2jstatElDown[0] = self._get2lWeight(Leptons, 35, 35, 'ElDown')
              
            otree.Fill()
            savedentries += 1

        self.disconnect()
        print ' - Event loop completed'
        print '   Saved entries:', savedentries


