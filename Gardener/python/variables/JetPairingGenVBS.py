module_name =    ''' 
       _      _   _____      _      _              _____        __      ______   _____ 
      | |    | | |  __ \    (_)    (_)            / ____|       \ \    / /  _ \ / ____|
      | | ___| |_| |__) |_ _ _ _ __ _ _ __   __ _| |  __  ___ _ _\ \  / /| |_) | (___  
  _   | |/ _ \ __|  ___/ _` | | '__| | '_ \ / _` | | |_ |/ _ \ '_ \ \/ / |  _ < \___ \ 
 | |__| |  __/ |_| |  | (_| | | |  | | | | | (_| | |__| |  __/ | | \  /  | |_) |____) |
  \____/ \___|\__|_|   \__,_|_|_|  |_|_| |_|\__, |\_____|\___|_| |_|\/   |____/|_____/ 
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

class JetPairingGenVBS(TreeCloner):

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
        parser.add_option_group(group)
        return group


    def checkOptions(self,opts):
        self.debug = (opts.debug == "1")
        self.radius = float(opts.radius)
        self.ptmin_jet = float(opts.ptmin_jet)

    def process(self,**kwargs):
        print module_name

        tree  = kwargs['tree']
        input = kwargs['input']
        output = kwargs['output']

        self.connect(tree,input)

        newbranches = ["hasTopGen", "V_jets", "VBS_jets", "PartonJetMatchFlag"]

        self.clone(output,newbranches)
        
        hasTopGen =   numpy.zeros(1, dtype=numpy.float32)
        V_jets    =   numpy.zeros(2, dtype=numpy.int32)
        VBS_jets  =   numpy.zeros(2, dtype=numpy.int32)
        PartonJetMatchFlag  =   numpy.zeros(1, dtype=numpy.int32)
        self.otree.Branch('hasTopGen',      hasTopGen,      'hasTopGen/F')
        self.otree.Branch('V_jets_true',    V_jets,         'V_jets_true[2]/I')
        self.otree.Branch('VBS_jets_true',   VBS_jets,       'VBS_jets_true[2]/I')
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

            partons, pids = utils.get_hard_partons(itree, self.debug)

            # Exclude events with top in the partons
            if 6 in pids or -6 in pids:
                hasTopGen[0] = 1.
                PartonJetMatchFlag[0] = -1
            else:
                hasTopGen[0] = 0.
                # If the event doesn't have top we can extract
                # "true" partons from VBS processes

                # get the pair nearest  to W or Z mass
                vpair = utils.nearest_masses_pair(partons, [80.385, 91.1876])
                vbspair = [ip for ip in range(4) if not ip in vpair]

                # now associate partons and nearest jets
                jets = utils.get_jets(itree, self.ptmin_jet, self.debug)
                matchresult, flag = utils.associate_vectors(jets, partons, self.radius)

                PartonJetMatchFlag[0] = flag
                
                if flag == 0:
                    # Save the truth association only if every parton is 
                    # associated to a different jet
                    for ip, iparton in enumerate(vpair):
                        V_jets[ip] = matchresult[0][iparton]
                    for jp, jparton in enumerate(vbspair):
                        VBS_jets[jp] = matchresult[0][jparton]
               
            otree.Fill()
  
        self.disconnect()
        print '- Eventloop completed'

