#
#
#      |                   |                       _ \                      |         |   _)               
#      |       _ \  __ \   __|   _ \   __ \       |   |   _ \   __|   _ \   |  |   |  __|  |   _ \   __ \  
#      |       __/  |   |  |    (   |  |   |      __ <    __/ \__ \  (   |  |  |   |  |    |  (   |  |   | 
#     _____| \___|  .__/  \__| \___/  _|  _|     _| \_\ \___| ____/ \___/  _| \__,_| \__| _| \___/  _|  _| 
#                  _|                                                                                                                  
#
#


from LatinoAnalysis.Gardener.gardening import TreeCloner
import numpy
import ROOT
import math
import sys
import optparse
import re
import warnings
import os.path
from collections import OrderedDict
from array import array;

class LeptonResolutionTreeMaker(TreeCloner):
    def __init__(self):
       pass

    def help(self):
        return '''Lepton pT resolution'''

    def addOptions(self,parser):
        description = self.help()
        group = optparse.OptionGroup(parser,self.label, description)
        group.add_option('-f',  '--file',    dest='resolutionFile', help='Resolution file with numbers', default=None)
        group.add_option('-k',  '--kind',    dest='kind', help='Kind of variation: -1, +1, +0.5, ..., meaning 100%, 50% of the values from the file', default=1.0)
        parser.add_option_group(group)
        return group

    def checkOptions(self,opts):
        print " >>  checkOptions "
        leppTresolution = {}
        self.kind            = 1.0 * float(opts.kind)
        print " amount of variation = ", self.kind

        cmssw_base = os.getenv('CMSSW_BASE')
        if opts.resolutionFile == None :
          opts.resolutionFile = cmssw_base+'/src/LatinoAnalysis/Gardener/python/data/leppTresolution.py'

        print " opts.resolutionFile = " , opts.resolutionFile

        if opts.resolutionFile == None :
          print " Using the default one"

        elif os.path.exists(opts.resolutionFile) :
          print " opts.resolutionFile = " , opts.resolutionFile
          handle = open(opts.resolutionFile,'r')
          exec(handle)
          handle.close()
        else :
          print "nothing ?"

        self.leppTresolution = leppTresolution
        self.minpt = 0
        self.maxpt = 200
        self.mineta = 0
        self.maxeta = 2.5


    def _getSmear (self, kindLep, pt, eta):
        # fix underflow and overflow                                                                                                    
        if pt < self.minpt:
          pt = self.minpt
        if pt > self.maxpt:
          pt = self.maxpt

        if eta < self.mineta:
          eta = self.mineta
        if eta > self.maxeta:
          eta = self.maxeta
        
        if kindLep in self.leppTresolution.keys() :
            for point in self.leppTresolution[kindLep] :
                if (pt >= point[0][0] and pt < point[0][1] and eta >= point[1][0] and eta < point[1][1]) :
                    print"wt from fx",point[2]
                    sigma=point[2]
                        
            smeared_pt = -1
            while smeared_pt < 0 :
                smeared_pt=ROOT.gRandom.Gaus(pt, sigma*pt)
                print" orignal and smeared pT",pt,smeared_pt
                return smeared_pt
        else:
              return 1.0

    def changeOrder(self, vectorname, vector, leptonOrderList) :
        # vector is already linked to the otree branch
        # vector name is the "name" of that vector to be modified        

        # take vector and clone vector
        # equivalent of: temp_vector = itree."vector"
        temp_vector = getattr(self.itree, vectorname)
        # remix the order of vector picking from the clone
        for i in range( len(leptonOrderList) ) :
          vector.push_back ( temp_vector[ leptonOrderList[i] ] )
        # set the default value for the remaining
        for i in range( len(temp_vector) - len(leptonOrderList) ) :
          vector.push_back ( -9999. )



    def process(self,**kwargs):
        tree  = kwargs['tree']
        input = kwargs['input']
        output = kwargs['output']
                
        # does that work so easily and give new variable itree and otree?
        self.connect(tree,input)

        nentries = self.itree.GetEntries()
        print 'Total number of entries: ',nentries 
        savedentries = 0

        #
        # create branches for otree, the ones that will be modified!
        # see: https://root.cern.ch/phpBB3/viewtopic.php?t=12507
        # this is the list of variables to be modified
        #
        # all the vectors that start with "std_vector_lepton_" are to be changed
        self.namesOldBranchesToBeModifiedVector = []
        vectorsToChange = ['std_vector_lepton_']
        for b in self.itree.GetListOfBranches():
            branchName = b.GetName()
            for subString in vectorsToChange:
                if subString in branchName:
                    self.namesOldBranchesToBeModifiedVector.append(branchName)
        
        # all "event based" variables will be changed in a "l2sel" step afterwards
        # like mll, dphill, ...
        

        # clone the tree with new branches added
        self.clone(output,self.namesOldBranchesToBeModifiedVector)
      
        self.oldBranchesToBeModifiedVector = {}
        for bname in self.namesOldBranchesToBeModifiedVector:
          bvector =  ROOT.std.vector(float) ()
          self.oldBranchesToBeModifiedVector[bname] = bvector

        # now actually connect the branches
        for bname, bvector in self.oldBranchesToBeModifiedVector.iteritems():
          self.otree.Branch(bname,bvector)            

        # input tree  
        itree = self.itree

        #----------------------------------------------------------------------------------------------------
        print '- Starting eventloop'
        step = 5000
        #step = 1


        #for i in xrange(2000):
        for i in xrange(nentries):
          itree.GetEntry(i)

          if i > 0 and i%step == 0.:
            print i,'events processed :: ', nentries
              
          # smear lepton pt, the core of this module
          leptonPtChanged = []            
          for i in range(itree.std_vector_lepton_pt.size()):
            # don't do anything if pt < 0, meaning it's the default value -9999.
            if not (itree.std_vector_lepton_pt[i] > 0):
              continue                 
            pt_lep=itree.std_vector_lepton_pt[i]
            eta_lep=itree.std_vector_lepton_eta[i]
            print pt_lep,eta_lep
            if abs(itree.std_vector_lepton_flavour[i]) == 13: # muon
                kindLep = 'mu'
                print kindLep
                pt_smeared = self._getSmear(kindLep,pt_lep,abs(eta_lep))
                print "smeared value",pt_smeared                
                leptonPtChanged.append(pt_smeared)
            elif abs(itree.std_vector_lepton_flavour[i]) == 11:
                kindLep = 'ele'
                print kindLep
                pt_smeared = self._getSmear(kindLep,pt_lep,abs(eta_lep))
                print "smeared value",pt_smeared                
                leptonPtChanged.append(pt_smeared)
            else: 
                leptonPtChanged.append(itree.std_vector_lepton_pt[i]) # how could it be nor endcap nor barrel? Sneaky electron!     

 
          # sorting in descending order and storing index
          leptonOrder = sorted(range(len(leptonPtChanged)), key = lambda k: leptonPtChanged[k], reverse=True)
          # leptonOrder is the list of indexes "pt" ordered
          
          # now save into the tree the new pt "std_vector_lepton_pt" variable
          # and reorder all th eother variables, to keep the correct order of leptons
          for bname, bvector in self.oldBranchesToBeModifiedVector.iteritems():
              bvector.clear()
              if 'std_vector_lepton_pt' in bname:
                  print bname
                  for i in range( len(leptonOrder) ) :
                      print"fishy thing",leptonPtChanged[leptonOrder[i]]
                      bvector.push_back (leptonPtChanged[leptonOrder[i]] )
                      # and if for any reason the list of leptonPtChanged (that is leptonOrder) is smaller than
                      # the original std_vector one, add the default values atthe end
                      for i in range( len(getattr(self.itree, bname)) - len(leptonOrder) ) :
                          bvector.push_back ( -9999. )
              else:
                  # for all the std_vector variables that are not "pt", just re-order them
                  self.changeOrder( bname, bvector, leptonOrder)
                          
                          
          self.otree.Fill()
          #savedentries+=1
          
          
        self.disconnect()
        print '- Eventloop completed'
        #print '   Saved: ', savedentries, ' events'
            

