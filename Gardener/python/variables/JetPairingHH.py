module_name =    ''' 
       _      _   _____      _      _             _    _ _    _ 
      | |    | | |  __ \    (_)    (_)           | |  | | |  | |
      | | ___| |_| |__) |_ _ _ _ __ _ _ __   __ _| |__| | |__| |
  _   | |/ _ \ __|  ___/ _` | | '__| | '_ \ / _` |  __  |  __  |
 | |__| |  __/ |_| |  | (_| | | |  | | | | | (_| | |  | | |  | |
  \____/ \___|\__|_|   \__,_|_|_|  |_|_| |_|\__, |_|  |_|_|  |_|
                                             __/ |              
                                            |___/               
'''

#
# This module extracts the pairs of VBS jets and V-jets looking at parton
# level and geometrically matching with reco jets. 
# 

import optparse
import numpy
import ROOT
from operator import itemgetter
import os.path
from LatinoAnalysis.Gardener.gardening import TreeCloner
import LatinoAnalysis.Gardener.variables.PairingUtils as utils 
from LatinoAnalysis.Gardener.data.btagging import tagger as bTaggingWPs

class JetPairingHH(TreeCloner):

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
        group.add_option('--ptminjet',  dest='ptmin_jet',  help='Min Pt for jets',  default=20.)
        group.add_option('-m', '--mode',  dest='mode',  help='Pairing mode, 0=nearest W mas, 1=max_pt, 2=mindeltaeta',  default="0")
        group.add_option('-b', '--bWP',  dest='bWP',  help='btagging WP: L,M,T',  default="L")
        parser.add_option_group(group)
        return group


    def checkOptions(self,opts):
        self.debug = (opts.debug == "1")
        self.ptmin_jet = float(opts.ptmin_jet)
        self.mode = int(opts.mode)
        self.bWP = opts.bWP

    def process(self,**kwargs):
        print module_name

        tree  = kwargs['tree']
        input = kwargs['input']
        output = kwargs['output']

        self.connect(tree,input)

        newbranches = ["H_jets", "W_jets"]

        self.clone(output,newbranches)
        H_jets  = numpy.zeros(2, dtype=numpy.int32)
        W_jets  = numpy.zeros(2, dtype=numpy.int32)
        self.otree.Branch('H_jets',  H_jets,  'H_jets[2]/I')
        self.otree.Branch('W_jets',  W_jets,  'W_jets[2]/I')

        nentries = self.itree.GetEntries()
        print 'Total number of entries: ',nentries 

        # avoid dots to go faster
        itree     = self.itree
        otree     = self.otree

        print '- Starting eventloop'
        step = 5000
        for i in xrange(nentries):
            itree.GetEntry(i)
            if i > 0 and i%step == 0.:
                print i,'events processed :: ', nentries

            hpair = [-1,-1]
            wpair = [-1,-1]

            jets, b_scores = utils.get_jets_and_bscore(itree, self.ptmin_jet, self.debug)

            bjets = [(i, bscore) for i, bscore in enumerate(b_scores)
                    if bscore >= bTaggingWPs['deepCSV'][self.bWP]]

            print bjets

            if len(bjets) >= 2:
                # Take the indexes of the two jets with bigger bscore
                hpair = [j[0] for j in list(sorted(bjets, key=itemgetter(1), reverse=True))[:2]]
                print hpair
                
                if len(jets) >=4:
                    if self.mode == 0:
                        wpair = utils.nearest_mass_pair_notH(jets, 80.385, hpair)
                    elif self.mode == 1:
                        wpair = utils.max_pt_pair_notH(jets, hpair)   
                    elif self.mode == 2:
                        wpair = utils.min_deltaeta_pairs_notH(jets, hpair)

            H_jets[0], H_jets[1] = hpair 
            W_jets[0], W_jets[1] = wpair            
            otree.Fill()
  
        self.disconnect()
        print '- Eventloop completed'


