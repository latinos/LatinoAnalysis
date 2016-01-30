#       _                           _____              _                                   _   
#      | |                         |_   _|            | |                                 | |  
#      | |      ___  _ __    _ __    | |    ___   ___ | |  _   _  _ __    ___   ___  _ __ | |_ 
#      | |     / _ \| '_ \  | '_ \   | |   / __| / __|| | | | | || '_ \  / __| / _ \| '__|| __|
#      | |____|  __/| |_) | | |_) |  | |   \__ \| (__ | | | |_| || | | || (__ |  __/| |   | |_ 
#      \_____/ \___|| .__/  | .__/   \_/   |___/ \___||_|  \__,_||_| |_| \___| \___||_|    \__|
#                   | |     | |                                                                
#                   |_|     |_|                                                                
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

class LeppTScalerTreeMaker(TreeCloner):
    def __init__(self):
       pass

    def help(self):
        return '''Lepton pT scaler acc to values given in leppTscaler.py'''

    def addOptions(self,parser):
        description = self.help()
        group = optparse.OptionGroup(parser,self.label, description)
        group.add_option('-f','--fileIn',dest='Filewithleptscalevalues',help='file with lep pT scale values for uncert calc',default=None)
        group.add_option('-v','--upordown',dest='variation',help='specify the variation type whether pT scaled up(1) or down(-1)',default='up')

        parser.add_option_group(group)
        return group

    def checkOptions(self,opts):

        print " >>  checkOptions "
        
        leppTscaler = {}
        self.variation            = 1.0 * float(opts.variation)
        print " amount of variation = ", self.variation


        cmssw_base = os.getenv('CMSSW_BASE')
        if opts.Filewithleptscalevalues == None :
          opts.Filewithleptscalevalues = cmssw_base+'/src/LatinoAnalysis/Gardener/python/data/leppTscaler.py'

        print " opts.Filewithleptscalevalues = " , opts.Filewithleptscalevalues

        if opts.Filewithleptscalevalues == None :
          print " Using the default one"
           
        elif os.path.exists(opts.Filewithleptscalevalues) :
          print " opts.Filewithleptscalevalues = " , opts.Filewithleptscalevalues
          handle = open(opts.Filewithleptscalevalues,'r')
          exec(handle)
          handle.close()
        else :
          print "nothing ?"

        self.leppTscaler = leppTscaler
        self.minpt = 0
        self.maxpt = 200
        self.mineta = 0
        self.maxeta = 2.5


    def _getScale (self, kindLep, pt, eta):
        # fix underflow and overflow
        if pt < self.minpt:
          pt = self.minpt
        if pt > self.maxpt:
          pt = self.maxpt
        
        if eta < self.mineta:
          eta = self.mineta
        if eta > self.maxeta:
          eta = self.maxeta

#        print " pt = ", pt
 #       print " eta = ", eta
        
        if kindLep in self.leppTscaler.keys() : 
            # get the scale values in bins of pT and eta
            #          print " self.leppTscaler[kindLep] = " , self.leppTscaler[kindLep]
            for point in self.leppTscaler[kindLep] :
                if (pt >= point[0][0] and pt < point[0][1] and eta >= point[1][0] and eta < point[1][1]) :
                    #                 print"wt from fx",point[2][0]
                    return point[2][0]
            # default ... it should never happen!
            # print " default ???"
            return 1.0
           
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
        savedenteris=0
        #
        # create branches for otree, the ones that will be modified!
        # see: https://root.cern.ch/phpBB3/viewtopic.php?t=12507
        # this is the list of variables to be modified
        #
	self.namesOldBranchesToBeModifiedVector = []
	vectorsToChange = ['std_vector_lepton_']
        for b in self.itree.GetListOfBranches():
	    branchName = b.GetName()
	    for subString in vectorsToChange:
		if subString in branchName:
		    self.namesOldBranchesToBeModifiedVector.append(branchName)
        
        # clone the tree with new branches added
        self.clone(output,self.namesOldBranchesToBeModifiedVector)
      
        self.oldBranchesToBeModifiedVector = {}
        for bname in self.namesOldBranchesToBeModifiedVector:
          bvector =  ROOT.std.vector(float) ()
          self.oldBranchesToBeModifiedVector[bname] = bvector
         # print "debug 0 ", bname

        # now actually connect the branches
        for bname, bvector in self.oldBranchesToBeModifiedVector.iteritems():
          self.otree.Branch(bname,bvector)            
         
        # input tree  
        itree = self.itree

        print '- Starting eventloop'
        step = 5000
        #step = 1

        for i in xrange(nentries):
            itree.GetEntry(i)

            if i > 0 and i%step == 0.:
              print i,'events processed :: ', nentries
                
            # scale lepton pt
            # Scale Up
            leptonPtChanged = []
            
            for i in range(itree.std_vector_lepton_pt.size()):
                #print " i = ", i, " -->  itree.std_vector_lepton_flavour[i] = ", itree.std_vector_lepton_flavour[i]
                #print "    -> ", abs(itree.std_vector_lepton_flavour[i])
                kindLep = 'lep' # ele or mu
#                print "pt eta",pt_lep,eta_lep
                if not (itree.std_vector_lepton_pt[i] > 0):
                    continue
                pt_lep=itree.std_vector_lepton_pt[i]
                eta_lep=itree.std_vector_lepton_eta[i]
                if abs(itree.std_vector_lepton_flavour[i]) == 13:
                    kindLep = 'mu'
                    wt = self._getScale(kindLep,pt_lep,abs(eta_lep))
                    leptonPtChanged.append(itree.std_vector_lepton_pt[i]*(1 + (self.variation*wt/100.0)))
                elif abs(itree.std_vector_lepton_flavour[i]) == 11:
                    kindLep = 'ele'
                    wt = self._getScale(kindLep,pt_lep,abs(eta_lep))
                    leptonPtChanged.append(itree.std_vector_lepton_pt[i]*(1 + (self.variation*wt/100.0)))
                else:
                    #print " what? "
                    leptonPtChanged.append(itree.std_vector_lepton_pt[i]*(1 + (0./100)))


            leptonOrder = sorted(range(len(leptonPtChanged)), key=lambda k: leptonPtChanged[k], reverse=True) 
                           
            for bname, bvector in self.oldBranchesToBeModifiedVector.iteritems():
                bvector.clear()
                if 'lepton_pt' in bname:
                    for i in range( len(leptonOrder) ) :
                        bvector.push_back ( leptonPtChanged[leptonOrder[i]] )
                    for i in range( len(getattr(self.itree, bname)) - len(leptonOrder) ) :
                        bvector.push_back ( -9999. )
                else:
                    self.changeOrder( bname, bvector, leptonOrder)
            

            self.otree.Fill()
 #           savedenteries+=1
            
            
        self.disconnect()
        print '- Eventloop completed'
  #      print '- Saved:', savedenteris, 'events'

