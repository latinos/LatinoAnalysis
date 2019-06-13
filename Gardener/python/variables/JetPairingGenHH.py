# module_name =    ''' 
#    _____      _  _______                _           _            ______                  
#    |_   _|    / ||_   __ \              (_)         (_)         .' ___  |                 
#      | |.---.`| |-'| |__) |,--.  _ .--. __   .--./) __  _ .--. / .'   \_| .---.  _ .--.   
#  _   | / /__\\| |  |  ___/`'_\ :[ `/'`\|  | / /'`\;[  |[ `.-. || |   ____/ /__\\[ `.-. |  
# | |__' | \__.,| |,_| |_   // | |,| |    | | \ \._// | | | | | |\ `.___]  | \__., | | | |  
# `.____.''.__.'\__/_____|  \'-;__[___]  [___].',__` [___|___||__]`._____.' '.__.'[___||__] 
#                                            ( ( __))                                       
# '''

# #
# # This module extracts the pairs of VBS jets and V-jets looking at parton
# # level and geometrically matching with reco jets. 
# # 

import optparse
import numpy
import ROOT
import os.path
from LatinoAnalysis.Gardener.gardening import TreeCloner
import LatinoAnalysis.Gardener.variables.PairingUtils as utils 

class JetPairingGenHH(TreeCloner):

    def __init__(self):
        pass

    def __del__(self):
        pass

    def help(self):
        return '''Identify pairs of jets for semileptonic analyses'''

    def addOptions(self,parser):
        description = self.help()
        group = optparse.OptionGroup(parser,self.label, description)
        group.add_option('-d', '--debug',  dest='debug',  help='Debug flag',  default="0")
        group.add_option('--radius',  dest='radius',  help='Radius for jet-parton association',  default=1.)
        group.add_option('--ptminjet',  dest='ptmin_jet',  help='Min Pt for jets',  default=20.)
        group.add_option('-m', '--mode',  dest='mode',  help='Pairing mode, 0=nearest W mas, 1=max_pt, 2=mindeltaeta',  default="0")
        parser.add_option_group(group)
        return group


    def checkOptions(self,opts):
        self.debug = (opts.debug == "1")
        self.radius = float(opts.radius)
        self.ptmin_jet = float(opts.ptmin_jet)
        self.mode = int(opts.mode)
        self.bWP = opts.bWP

    def process(self,**kwargs):
        print module_name

        tree  = kwargs['tree']
        input = kwargs['input']
        output = kwargs['output']
        self.connect(tree,input)

        newbranches = ["H_jets", "W_jets", "PartonJetMatchFlag"]

        self.clone(output,newbranches)
        
        H_jets    =   numpy.zeros(2, dtype=numpy.int32)
        W_jets  =   numpy.zeros(2, dtype=numpy.int32)
        PartonJetMatchFlag  =   numpy.zeros(1, dtype=numpy.int32)
        self.otree.Branch('H_jets',  H_jets,  'H_jets[2]_true/I')
        self.otree.Branch('W_jets',  W_jets,  'H_jets[2]_true/I')
        self.otree.Branch('PartonJetMatchFlag', PartonJetMatchFlag, 'PartonJetMatchFlag/I')

        nentries = self.itree.GetEntries()
        print 'Total number of entries: ',nentries 

        # avoid dots to go faster
        itree     = self.itree
        otree     = self.otree
        print "Matching radius:", self.radius

        print '- Starting eventloop'
        step = 5000
        for i in xrange(nentries):
            itree.GetEntry(i)
            if i > 0 and i%step == 0.:
                print i,'events processed :: ', nentries
            hpair = [-1,-1]
            wpair = [-1,-1]

            partons, pids = utils.get_hard_partons(itree, self.debug)

            # first take the two bs 
            hpair = [i for i, p in enumerate(pids) if p in [5,-5]]
            
            
            #find the W jets
            if len(partons) >= 4: # and len(hpair) == 2:
                if self.mode == 0:
                    wpair = utils.nearest_mass_pair_notH(jets, 80.385, hpair)
                elif self.mode == 1:
                    wpair = utils.max_pt_pair_notH(jets, hpair)   
                elif self.mode == 2:
                    wpair = utils.min_deltaeta_pairs_notH(jets, hpair)
             
            # now associate partons and nearest jets
            jets = utils.get_jets(itree, self.debug)
            matchresult, flag = utils.associate_vectors(jets, partons, self.radius)
            PartonJetMatchFlag[0] = flag
                
            if flag == 0:
                # Save the truth association only if every parton is 
                # associated to a different jet
                for ip, iparton in enumerate(hpair):
                    H_jets[ip] = matchresult[0][iparton]
                for jp, jparton in enumerate(wpair):
                    W_jets[jp] = matchresult[0][jparton]
               
            otree.Fill()
  
        self.disconnect()
        print '- Eventloop completed'

