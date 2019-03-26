import optparse
import numpy
import ROOT
import os.path
import math
from operator import attrgetter, itemgetter
from itertools import combinations

from LatinoAnalysis.Gardener.gardening import TreeCloner


def max_deltaeta_pair(jets):
    l = []
    for i ,k  in combinations(range(len(jets)),2):
        l.append( ([i,k], abs(jets[i].Eta() - jets[k].Eta())))
    l = sorted(l, key=itemgetter(1), reverse=True)
    return l[0][0]

def max_mjj_pair(jets):
    l = []
    for i ,k  in combinations(range(len(jets)),2):
        l.append( ([i,k], (jets[i]+ jets[k]).M() ))
    l = sorted(l, key=itemgetter(1), reverse=True)
    return l[0][0]

def max_pt_pair(jets):
    ''' Returns the pair with highest Pt'''
    l = []
    for i ,k  in combinations(range(len(jets)),2):
        l.append(( [i,k], (jets[i]+ jets[k]).Pt() ))
    l = sorted(l, key=itemgetter(1), reverse=True)
    return l[0][0]

def nearest_mass_pair(jets, mass):
    ''' Returns the pair of jets with invariant mass nearest to 
    the given mass '''
    l = []
    for i ,k  in combinations(range(len(jets)),2):
        l.append(([i,k], abs(mass - (jets[i]+ jets[k]).M() )))  
    l = sorted(l, key=itemgetter(1))
    return l[0][0]
    

class jetPairing(TreeCloner):

    def __init__(self):
        pass

    def __del__(self):
        pass

    def help(self):
        return '''Identify pairs of jets for semileptonic analyses'''

    def addOptions(self,parser):
        description = self.help()
        group = optparse.OptionGroup(parser,self.label, description)
        #group.add_option('-j', '--njets',  dest='njets',  help='Minimum number of jets',  default='0')
        parser.add_option_group(group)
        return group


    def checkOptions(self,opts):
        pass


    def process(self,**kwargs):

        tree  = kwargs['tree']
        input = kwargs['input']
        output = kwargs['output']

        self.connect(tree,input)

        newbranches = ["jets_from_H", 
                       "jets_from_W"]

        self.clone(output,newbranches)
        
        jets_from_H = numpy.zeros(2, dtype=numpy.int32)
        jets_from_W = numpy.zeros(2, dtype=numpy.int32)
        self.otree.Branch('jets_from_H',  jets_from_H,  'jets_from_H/F')
        self.otree.Branch('jets_from_W',  jets_from_W,  'jets_from_W/F')

        nentries = self.itree.GetEntries()
        print 'Total number of entries: ',nentries 

        # avoid dots to go faster
        itree     = self.itree
        otree     = self.otree

        print '- Starting eventloop'
        step = 5000
        for i in xrange(nentries):
            itree.GetEntry(i)
            


            
            otree.Fill()
  
            
        self.disconnect()
        print '- Eventloop completed'

