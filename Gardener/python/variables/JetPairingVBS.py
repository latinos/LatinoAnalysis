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
        group.add_option('-m', '--mode',  dest='mode',  help='Pairing mode, 0=vjet+vbs, 1=vbs+vjet',  default="0")
        parser.add_option_group(group)
        return group


    def checkOptions(self,opts):
        self.debug = (opts.debug == "1")
        self.ptmin_jet = float(opts.ptmin_jet)
        self.mode = int(opts.mode)

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

            if self.mode == 0:
                
                if len(jets) >=2:
                    vpair = utils.nearest_masses_pair(jets, [80.385, 91.1876])
            
                    if len(jets) >=4:
                        # Save pairs of (index, jet) for the next step
                        remaining_jets = [(i,j) for i,j in enumerate(jets) if i not in vpair]
                        # The result of the next step are indexes in the new collection of jets
                        vbspair_newindexes = utils.max_mjj_pair([rj[1] for rj in remaining_jets])
                        # going back to global index 
                        vbspair = [remaining_jets[i][0] for i in vbspair_newindexes]
                                                                
                    elif self.debug:
                        print "Less than 4 jets available"

            elif self.mode == 1:

                if len(jets) >=2:
                    vbspair = utils.max_mjj_pair(jets)
            
                    if len(jets) >=4:
                        # Save pairs of (index, jet) for the next step
                        remaining_jets = [(i,j) for i,j in enumerate(jets) if i not in vbspair]
                        # The result of the next step are indexes in the new collection of jets
                        vpair_newindexes = utils.nearest_masses_pair([rj[1] for rj in remaining_jets], [80.385, 91.1876])
                        # going back to global index 
                        vpair = [remaining_jets[i][0] for i in vpair_newindexes]
                                                                
                    elif self.debug:
                        print "Less than 4 jets available"


            V_jets[0], V_jets[1] = vpair
            VBS_jets[0], VBS_jets[1] = vbspair

            otree.Fill()
  
        self.disconnect()
        print '- Eventloop completed'

