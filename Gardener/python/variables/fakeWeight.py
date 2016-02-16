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
        group.add_option('-s', '--stat', dest='stat', help='<Nominal|MuUp|MuDo|ElUp|ElDo>', default='Nominal')
        parser.add_option_group(group)
        return group


    def checkOptions(self,opts):
        self.stat = opts.stat
        print " stat =", self.stat


    def _getWeight(self, kindLep, pt, eta, istight):

        # FIXME function to be defined
        
        return 1.0, 0.0, 0.0


    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # _getPFWeight
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def _getPFWeight(self, leptons, muonThreshold, electronThreshold):

        if (len(leptons) < 2) :

            return 0.0, 0.0, 0.0

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

                    if   (self.stat == 'MuUp')   : f = f + fE
                    elif (self.stat == 'MuDown') : f = f - fE

                elif (leptons[i][0] == 'el') :

                    f  = 0.03  # GetFactor     (ElecFR[ele],  lep.pt, lep.eta, electronThreshold);
                    fE = 0.01  # GetFactorError(ElecFR[ele],  lep.pt, lep.eta, electronThreshold);

                    if   (self.stat == 'ElUp')   : f = f + fE
                    elif (self.stat == 'ElDown') : f = f - fE

                if (leptons[i][3] == 1) :

                    ntight += 1
 
                    promptProbability[i] = p * (1 - f)
                    fakeProbability[i]   = f * (1 - p)
             
                else :

                    promptProbability[i] = p * f
                    fakeProbability[i]   = p * f

                promptProbability[i] /= (p - f)
                fakeProbability[i]   /= (p - f)
 
            PF = promptProbability[0] * fakeProbability[1]
            FP = promptProbability[1] * fakeProbability[0]

            result = PF + FP;
    
            if (ntight == 0 or ntight == 2) : result *= -1.

###            if (result > 0) : print ' result:',result
 
            return result, result, result


    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # _getFFWeight
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def _getFFWeight (self, leptons, muonThreshold, electronThreshold): 
      
        # Using the dictionary "Leptons" defined below
        #     Leptons[selectedLepton] = [kindLep, pt, eta, IsTightLepton, weight, weigth_error_up, weigth_error_do]
        #     with selectedLepton = 0 or 1

        # FIXME function to be defined
                
        return 1.0, 0.0, 0.0


    def process(self,**kwargs):
        tree   = kwargs['tree']
        input  = kwargs['input']
        output = kwargs['output']

        self.connect(tree,input)
         
        self.fakeVariables = [ 'fakeW2l', 'fakeW2l0j', 'fakeW2l1j', 'fakeW2l2j' ]
        
        # Clone the tree with new branches added
        self.clone(output, self.fakeVariables)
      
        # Now actually connect the branches
        fakeW2l   = numpy.ones(1, dtype=numpy.float32)
        fakeW2lUp = numpy.ones(1, dtype=numpy.float32)
        fakeW2l0j = numpy.ones(1, dtype=numpy.float32)
        fakeW2l1j = numpy.ones(1, dtype=numpy.float32)
        fakeW2l2j = numpy.ones(1, dtype=numpy.float32)

        self.otree.Branch('fakeW2l',   fakeW2l,   'fakeW2l/F')
        self.otree.Branch('fakeW2lUp', fakeW2lUp, 'fakeW2lUp/F')
        self.otree.Branch('fakeW2l0j', fakeW2l0j, 'fakeW2l0j/F')
        self.otree.Branch('fakeW2l1j', fakeW2l1j, 'fakeW2l1j/F')
        self.otree.Branch('fakeW2l2j', fakeW2l2j, 'fakeW2l2j/F')

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

                   
            #                                     mu  ele
            weightPF = self._getPFWeight(Leptons, 15, 15)
            weightFF = self._getFFWeight(Leptons, 15, 15)

            fakeW2l  [0] = weightPF[0] + weightFF[0]
            fakeW2l0j[0] = 1.23456
            fakeW2l1j[0] = 7.890
            fakeW2l2j[0] = 7.890

            fakeW2lUp[0] = weightPF[1] + weightFF[1]
              
            otree.Fill()
            savedentries += 1

        self.disconnect()
        print ' - Event loop completed'
        print '   Saved entries:', savedentries


