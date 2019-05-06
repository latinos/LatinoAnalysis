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

# import optparse
# import numpy
# import ROOT
# import os.path
# from LatinoAnalysis.Gardener.gardening import TreeCloner
# import LatinoAnalysis.Gardener.variables.PairingUtils as utils 

# class JetPairingGenVBS(TreeCloner):

#     def __init__(self):
#         pass

#     def __del__(self):
#         pass

#     def help(self):
#         return '''Identify pairs of jets for semileptonic analyses'''

#     def addOptions(self,parser):
#         description = self.help()
#         group = optparse.OptionGroup(parser,self.label, description)
#         group.add_option('-d', '--debug',  dest='debug',  help='Debug flag',  default="0")
#         group.add_option('--radius',  dest='radius',  help='Radius for jet-parton association',  default=1.)
#         parser.add_option_group(group)
#         return group


#     def checkOptions(self,opts):
#         self.debug = (opts.debug == "1")
#         self.radius = float(opts.radius)

#     def process(self,**kwargs):
#         print module_name

#         tree  = kwargs['tree']
#         input = kwargs['input']
#         output = kwargs['output']

#         self.connect(tree,input)

#         newbranches = ["V_jets", "H_jets", "PartonJetMatchFlag"]

#         self.clone(output,newbranches)
        
#         V_jets    =   numpy.zeros(2, dtype=numpy.int32)
#         H_jets  =   numpy.zeros(2, dtype=numpy.int32)
#         PartonJetMatchFlag  =   numpy.zeros(1, dtype=numpy.int32)
#         self.otree.Branch('V_jets',         V_jets,         'V_jets/I')
#         self.otree.Branch('H_jets',       H_jets,       'H_jets/I')
#         self.otree.Branch('PartonJetMatchFlag', PartonJetMatchFlag, 'PartonJetMatchFlag/I')

#         nentries = self.itree.GetEntries()
#         print 'Total number of entries: ',nentries 

#         # avoid dots to go faster
#         itree     = self.itree
#         otree     = self.otree

#         print "Matching radius:", self.radius

#         print '- Starting eventloop'
#         step = 5000
#         for i in xrange(nentries):
#             itree.GetEntry(i)
#             if i > 0 and i%step == 0.:
#                 print i,'events processed :: ', nentries

#             partons, pids = utils.get_hard_partons(itree, self.debug)

#             # first take the two bs and the other two partons
#             bpair = [i, for i, p in enumerate(pids) if p in [5,-5]]
#             v_pair = [ip for ip in range(4) if not ip in bs]
            
#             # now associate partons and nearest jets
#             jets = utils.get_jets(itree, self.debug)
#             matchresult, flag = utils.associate_vectors(jets, partons, self.radius)

#             PartonJetMatchFlag[0] = flag
                
#             if flag == 0:
#                 # Save the truth association only if every parton is 
#                 # associated to a different jet
#                 for ip, iparton in enumerate(vpair):
#                     V_jets[ip] = matchresult[0][iparton]
#                 for jp, jparton in enumerate(bpair):
#                     H_jets[jp] = matchresult[0][iparton]
               
#             otree.Fill()
  
#         self.disconnect()
#         print '- Eventloop completed'

