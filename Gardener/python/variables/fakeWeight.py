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

class FakeWeightFiller(TreeCloner):

    def __init__(self):
        pass

    def __del__(self):
        pass

    def help(self):
        return '''Add '''

    def addOptions(self,parser):
        description = self.help()
        group = optparse.OptionGroup(parser,self.label, description)

        parser.add_option_group(group)
        return group



    def checkOptions(self,opts):
       
        # ~~~~
        pass


    def _getWeight (self, kindLep, pt, eta):

        return 1.0, 0.0, 0.0



   
   
    def process(self,**kwargs):
        tree  = kwargs['tree']
        input = kwargs['input']
        output = kwargs['output']

        self.connect(tree,input)

         
        self.fakeVariables = [ 'fakeW', 'fakeW1' ]
        
        # Clone the tree with new branches added
        self.clone(output, self.fakeVariables)
      
        # Now actually connect the branches
        fakeW  = numpy.ones(1, dtype=numpy.float32)
        fakeW1 = numpy.ones(1, dtype=numpy.float32)

        self.otree.Branch('fakeW',    fakeW,  'fakeW/F')
        self.otree.Branch('fakeW1',   fakeW1, 'fakeW1/F')

        nentries = self.itree.GetEntries()
        print 'Total number of entries: ',nentries 
        savedentries = 0
                
        # avoid dots to go faster
        itree     = self.itree
        otree     = self.otree

        print '- Starting eventloop'
        step = 5000
        for i in xrange(nentries):
            itree.GetEntry(i)

            ## print event count
            if i > 0 and i%step == 0.:
              print i,'events processed.'

            fakeW[0]  = 1.23456
            fakeW1[0] = 7.890
          
            otree.Fill()
            savedentries+=1

        self.disconnect()
        print '- Eventloop completed'
        print '   Saved: ', savedentries, ' events'


