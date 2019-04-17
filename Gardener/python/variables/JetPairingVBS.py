module_name =    ''' 
       _        _    _____              _         _     __      __ ____    _____ 
      | |      | |  |  __ \            (_)       (_)    \ \    / /|  _ \  / ____|
      | |  ___ | |_ | |__) |__ _  _ __  _   __ _  _  _ __\ \  / / | |_) || (___  
  _   | | / _ \| __||  ___// _` || '__|| | / _` || || '_ \\ \/ /  |  _ <  \___ \ 
 | |__| ||  __/| |_ | |   | (_| || |   | || (_| || || | | |\  /   | |_) | ____) |
  \____/  \___| \__||_|    \__,_||_|   |_| \__, ||_||_| |_| \/    |____/ |_____/ 
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
        parser.add_option_group(group)
        return group


    def checkOptions(self,opts):
        self.debug = (opts.debug == "1")

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
        self.otree.Branch('V_jets',         V_jets,         'V_jets/I')
        self.otree.Branch('VBS_jets',       VBS_jets,       'VBS_jets/I')

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

            jets = utils.get_jets(itree, self.debug)
            vpair = [0,0]
            vbspair = [0,0]
            
            if len(jets) >=2:
                vpair = utils.nearest_masses_pair(jets, [80.385, 91.1876])

                if len(jets) >=4:
                    remaining_jets = [j for i,j in enumerate(jets) if i not in vpair]
                    vbspair = utils.max_mjj_pair(remaining_jets)

            for i in range(2):
                V_jets[i] = vpair[i]
                VBS_jets[i] = vbspair[i] 
                
            otree.Fill()
  
        self.disconnect()
        print '- Eventloop completed'

