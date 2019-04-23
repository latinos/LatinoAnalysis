module_name =    ''' 
       _      _   _____      _      _          __      ______   _____ 
      | |    | | |  __ \    (_)    (_)         \ \    / /  _ \ / ____|
      | | ___| |_| |__) |_ _ _ _ __ _ _ __   __ \ \  / /| |_) | (___  
  _   | |/ _ \ __|  ___/ _` | | '__| | '_ \ / _` \ \/ / |  _ < \___ \ 
 | |__| |  __/ |_| |  | (_| | | |  | | | | | (_| |\  /  | |_) |____) |
  \____/ \___|\__|_|   \__,_|_|_|  |_|_| |_|\__, | \/   |____/|_____/ 
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
import os.path
from LatinoAnalysis.Gardener.gardening import TreeCloner
import LatinoAnalysis.Gardener.variables.PairingUtils as utils 

class JetPairingVBS(TreeCloner):

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
        parser.add_option_group(group)
        return group


    def checkOptions(self,opts):
        self.debug = (opts.debug == "1")
        self.ptmin_jet = float(opts.ptmin_jet)

    def process(self,**kwargs):
        print module_name

        tree  = kwargs['tree']
        input = kwargs['input']
        output = kwargs['output']

        self.connect(tree,input)

        newbranches = ["V_jets", "VBS_jets"]

        self.clone(output,newbranches)
        V_jets    =   numpy.zeros(2, dtype=numpy.int32)
        VBS_jets  =   numpy.zeros(2, dtype=numpy.int32)
        self.otree.Branch('V_jets',         V_jets,         'V_jets[2]/I')
        self.otree.Branch('VBS_jets',       VBS_jets,       'VBS_jets[2]/I')

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

            jets = utils.get_jets(itree, self.ptmin_jet, self.debug)
            vpair   = [-1,-1]
            vbspair = [-1,-1]
            
            if len(jets) >=2:
                vpair = utils.nearest_masses_pair(jets, [80.385, 91.1876])

                if len(jets) >=4:
                    remaining_jets = [j for i,j in enumerate(jets) if i not in vpair]
                    vbspair = utils.max_mjj_pair(remaining_jets)
                elif self.debug:
                    print "Less than 4 jets available"

            for i in range(2):
                V_jets[i] = vpair[i]
                VBS_jets[i] = vbspair[i] 
                
            otree.Fill()
  
        self.disconnect()
        print '- Eventloop completed'

