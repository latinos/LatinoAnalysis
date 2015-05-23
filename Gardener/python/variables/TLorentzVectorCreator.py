#
#
#    __ __|  |                               |       \ \     /            |                
#       |    |       _ \    __|  _ \  __ \   __| _  / \ \   /  _ \   __|  __|   _ \    __| 
#       |    |      (   |  |     __/  |   |  |     /   \ \ /   __/  (     |    (   |  |    
#      _|   _____| \___/  _|   \___| _|  _| \__| ___|   \_/  \___| \___| \__| \___/  _|    
#                                                                                         
#
#


from LatinoAnalysis.Gardener.gardening import TreeCloner
import numpy
import ROOT
import sys
import optparse
import re
import warnings
import os.path
from array import array;

from ROOT import std

class TLorentzVectorCreator(TreeCloner):


    def __init__(self):
        self.variables = {}
        #self.regex = re.compile("([a-zA-Z0-9]*)/([FID])=(.*)")
        self.regex = re.compile("([a-zA-Z0-9]*)=([a-zA-Z0-9-_]*),([a-zA-Z0-9-_]*),([a-zA-Z0-9-_]*)")

    def help(self):
        return '''Add TLorentz Vectors variables from std::vector float'''

    def addOptions(self,parser):
        description = self.help()
        #print " self.label = ", self.label
        group = optparse.OptionGroup(parser,self.label, description)
        group.add_option('-v','--var',dest='variables',action='append',default=[])
        parser.add_option_group(group)
        #print " >>> ciao"
        return group

    def checkOptions(self,opts):
        if not opts.variables:
            raise ValueError('No variables defined?!?')

        print " opts.variables: ", opts.variables
        for s in opts.variables:
            r = self.regex.match(s)
            if not r:
                raise RuntimeError('Malformed option '+s)
            name = r.group(1)
            print " name = ", name
            pt  = r.group(2)
            print " pt   = ", pt
            eta = r.group(3)
            print " eta  = ", eta
            phi = r.group(4)
            print " phi  = ", phi

            #print "self.regex = ", self.regex
            #print "s = ", s
            #print "r = ", r
            #print "r.groups() = ", r.groups()
            #print "len(r.groups()) = ", len(r.groups())
            if len(r.groups()) == 5 :
              en = r.group(5)
            else :
              en = "DUMMY"
              
            print " en = ", en
            #-v 'TLlep=std_variable_vector_lepton_pt,std_variable_vector_lepton_eta,std_variable_vector_lepton_phi' \

            TL = ROOT.std.vector(ROOT.TLorentzVector) ()
            self.variables[name] = (TL, pt, eta, phi, en)


    def process(self,**kwargs):

        tree  = kwargs['tree']
        input = kwargs['input']
        output = kwargs['output']

        self.connect(tree,input)

        print " begin ... "

        #vars = [ ( value, type, ROOT.TTreeFormula(name,formula, self.itree)) for name, (value, type, formula) in self.variables.iteritems() ]
        vars = [ (name, TL, pt, eta, phi, en) for name, (TL, pt, eta, phi, en) in self.variables.iteritems() ]
        #TL, pt, eta, phi, en
        
        #vector<TLorentzVector> theJets;
        #tcal.Branch("theJets",&theJets);


        print 'Adding/replacing the following branches'
        template=' {0:10} | "{2}" | "{2}" | "{2}" | "{2}" '
        for name  in sorted(self.variables):
            (TL, pt, eta, phi, en) = self.variables[name]
            print template.format(name, pt, eta, phi, en)
            print pt, "-", eta, "-", phi, "-", en
        print



        oldbranches = [ b.GetName() for b in self.itree.GetListOfBranches() ]
        hasMutation = False
        for bname in self.variables:
            # not there, continue
            if bname not in oldbranches: continue
            # found, check for consistency
            branch = self.itree.GetBranch(bname)
            newtitle = bname
            if ( branch.GetTitle() != newtitle ):
                print 'WARNING: Branch mutation detected: from',branch.GetTitle(),'to',newtitle
                hasMutation = True

        if hasMutation:
            confirm('Mutation detected. Do you _really_ want to continue?') or sys.exit(0)

        self.clone(output,self.variables.keys())

        for (name, TL, pt, eta, phi, en) in vars:
            #title = name
            self.otree.Branch(name,TL)
            #self.otree.Branch(str(name),"vector<TLorentzVector>",id(TL))
            #self.otree.Branch(str(name),"vector<TLorentzVector>",ROOT.AddressOf(TL))

        nentries = self.itree.GetEntries()
        print 'Entries:',nentries

        # avoid dots in the loop
        itree = self.itree
        otree = self.otree

        step = 5000
        for i in xrange(0,nentries):
            itree.GetEntry(i)

            if i > 0 and i%step == 0:
                print str(i)+' events processed.'

            with warnings.catch_warnings():
                warnings.simplefilter("ignore")
                for (name, TL, pt, eta, phi, en) in vars:
                    TL.clear()
                    #print " size = ", pt
                    #print " size = ", (getattr(itree, pt)).size()
                    vectorLength = (getattr(itree, pt)).size()
                    for i in range(0, vectorLength):
                       singleTL = ROOT.TLorentzVector()
                       if en != "DUMMY" :
                         print "not dummy??"
                         singleTL.SetPtEtaPhiE((getattr(itree, pt)).at(i), (getattr(itree, eta)).at(i), (getattr(itree, phi)).at(i), (getattr(itree, en)).at(i))
                       else:
                         # massless
                         singleTL.SetPtEtaPhiM((getattr(itree, pt)).at(i), (getattr(itree, eta)).at(i), (getattr(itree, phi)).at(i), 0.0)

                       TL.push_back(singleTL)
                    #print name

            otree.Fill()
        
        self.disconnect()
        print '- Eventloop completed'
        
        
