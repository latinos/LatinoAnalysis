#
#
#
#
#    ____|  |              |                            
#    __|    |   _ \   __|  __|   __|  _ \   __ \    __| 
#    |      |   __/  (     |    |    (   |  |   | \__ \ 
#   _____| _| \___| \___| \__| _|   \___/  _|  _| ____/ 
#                                                     
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

class ElectronsVarFiller(TreeCloner):
    def __init__(self):
       pass

    def help(self):
        return '''Add Electrons variables, e.g. eleId flags'''

    def addOptions(self,parser):
        pass

    def checkOptions(self,opts):
        pass

    def process(self,**kwargs):
        tree  = kwargs['tree']
        input = kwargs['input']
        output = kwargs['output']

        self.newbranches = ['std_vector_electron_isLoose']

        # does that work so easily and give new variable itree and otree?
        self.connect(tree,input)
        
        oldbranches = [ b.GetName() for b in self.itree.GetListOfBranches() ]
        hasMutation = False
        for bname in self.newbranches:
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



        self.clone(output,self.newbranches)
        
        newbranchesVecotor = {}
        for bname in self.newbranches:
          bvector =  ROOT.std.vector(int) ()
          newbranchesVecotor[bname] = bvector


        for bname, bvector in newbranchesVecotor.iteritems():
            print " bname   = ", bname
            print " bvector = ", bvector
            self.otree.Branch(bname,bvector)
            #self.otree.Branch(str(bname),"vector<int>",bvector)
            #self.otree.Branch(bname,"vector<int>",bvector)
            #self.otree.Branch(str(bname),"vector<int>",ROOT.AddressOf(bvector))

        nentries = self.itree.GetEntries()
        print 'Total number of entries: ',nentries 

        #what is self.itree? what is self.otree?
        itree     = self.itree
        otree     = self.otree

        #----------------------------------------------------------------------------------------------------
        print '- Starting eventloop'
        step = 5000

        for i in xrange(nentries):

            itree.GetEntry(i)

            if i > 0 and i%step == 0.:
                print i,'events processed.'

            for bname, bvector in newbranchesVecotor.iteritems():
              bvector.clear()
                
            vectorLength = (getattr(itree, "std_vector_lepton_pt")).size()
            #print " vectorLength = ",vectorLength
            for i in range(0, vectorLength):
              if ((getattr(itree, "std_vector_lepton_eta")).at(i)) < 1.2345 :
              #if ((getattr(itree, "std_vector_electron_deltaEtaIn")).at(i)) < 1.2345 :
                for bname, bvector in newbranchesVecotor.iteritems():
                  bvector.push_back(1)
              else :
                for bname, bvector in newbranchesVecotor.iteritems():
                  bvector.push_back(0)


            otree.Fill()

        self.disconnect()
        print '- Eventloop completed'
