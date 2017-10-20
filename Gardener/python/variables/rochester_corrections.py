import optparse
import numpy
import ROOT
import os.path
import math
import random 

from LatinoAnalysis.Gardener.gardening import TreeCloner
                                                                                                                         
class rochester_corr(TreeCloner):

    def __init__(self):
        pass

    def __del__(self):
        pass

    def help(self):
        return '''Add a scale factor from Rochester corrections'''

    def addOptions(self,parser):
        description = self.help()
        group = optparse.OptionGroup(parser,self.label, description)
        group.add_option('-c', '--cmssw', dest='cmssw', help='cmssw version (naming convention may change)', default='763', type='string')
        group.add_option('-d', '--data', dest='isdata', help='is data or not', default='0')
        parser.add_option_group(group)
        return group

    def checkOptions(self,opts):

        self.cmssw = opts.cmssw
        print " cmssw = ", self.cmssw
        cmssw_base = os.getenv('CMSSW_BASE')
        self.isdata = int(opts.isdata)

        try:
            ROOT.gROOT.LoadMacro(cmssw_base+'/src/LatinoAnalysis/Gardener/python/variables/RoccoR.cc+g')
        except RuntimeError:
            ROOT.gROOT.LoadMacro(cmssw_base+'/src/LatinoAnalysis/Gardener/python/variables/RoccoR.cc++g')
       
        
       

    def process(self,**kwargs):
        
        tree  = kwargs['tree']
        input = kwargs['input']
        output = kwargs['output']
     
        self.connect(tree,input)

        self.namesOldBranchesToBeModifiedVector = ['std_vector_lepton_pt','std_vector_muon_pt']

        #vectorsToChange = ['std_vector_lepton_','std_vector_muon_']
        #for b in self.itree.GetListOfBranches():
        #    branchName = b.GetName()
        #    for subString in vectorsToChange:
        #        if subString in branchName: self.namesOldBranchesToBeModifiedVector.append(branchName)

        # NOW WE CAN CLONE THE TREE
        self.clone(output,self.namesOldBranchesToBeModifiedVector)

        # NOW CONNECT ALL NEW/TO BE MODIFIED BRANCHES 

        # ... Old Branches:
        self.oldBranchesToBeModifiedVector = {}
        for bname in self.namesOldBranchesToBeModifiedVector:
          bvector =  ROOT.std.vector(float) ()
          self.oldBranchesToBeModifiedVector[bname] = bvector
        for bname, bvector in self.oldBranchesToBeModifiedVector.iteritems(): self.otree.Branch(bname,bvector)

        cmssw_base = os.getenv('CMSSW_BASE')
        rochester_path = cmssw_base+'/src/LatinoAnalysis/Gardener/python/data/rcdata.2016.v3'
        print "scale factors from", rochester_path
        rc=ROOT.RoccoR(rochester_path)

        # Loop
        nentries = self.itree.GetEntries()
        print 'Total number of entries: ',nentries
        savedentries = 0

        #----------------------------------------------------------------------------------------------------
        print '- Starting eventloop'
        step = 10000

        # input tree and output tree
        itree     = self.itree
        otree     = self.otree
        s=0
        m=0
        for i in xrange(nentries):

            itree.GetEntry(i)
            if i > 0 and i%step == 0.:
                print i,'events processed :: ', nentries

            # Clear all vectors
            for bname, bvector in self.oldBranchesToBeModifiedVector.iteritems() : bvector.clear()

            for iLep in xrange(len(itree.std_vector_lepton_pt)) :

                pt = itree.std_vector_lepton_pt [iLep]
                genpt = itree.std_vector_leptonGen_pt [iLep]
                flavour = itree.std_vector_lepton_flavour [iLep]
                eta = itree.std_vector_lepton_eta [iLep]
                phi =itree.std_vector_lepton_phi [iLep]
                
                # Muons only
                if  abs(flavour) == 13 :
                    
                    charge = int(flavour/abs(flavour))
                    nl =int(itree.std_vector_muon_NValidHitsInTrk [iLep])
                    u1 =random.random()
                    #print charge, pt, eta, phi, nl, genpt, u1

                   
                    if self.isdata == 1 :
                        #for each data muon in the loop, use this function to get a scale factor for its momentum
                        dataSF = rc.kScaleDT(charge,pt,eta,phi)
                        #dataSF= 1.5
                        newpt= pt*dataSF
                        self.oldBranchesToBeModifiedVector['std_vector_lepton_pt'] .push_back(newpt)
                        self.oldBranchesToBeModifiedVector['std_vector_muon_pt'] .push_back(newpt)
                        #if i%step == 0.:
                        #    print dataSF
                    else :
                        #for MC, if matched gen-level muon (genPt) is available, use this function
                        mcSF = rc.kScaleFromGenMC(charge, pt, eta, phi, nl, genpt, u1)
                        #mcSF= 1.5
                        newpt= pt*mcSF
                        self.oldBranchesToBeModifiedVector['std_vector_lepton_pt'] .push_back(newpt)
                        self.oldBranchesToBeModifiedVector['std_vector_muon_pt'] .push_back(newpt)
                        #if i%step == 0.:
                        #    print mcSF
                       
                else:
                    self.oldBranchesToBeModifiedVector['std_vector_lepton_pt'] .push_back(pt)
                    self.oldBranchesToBeModifiedVector['std_vector_muon_pt'] .push_back(pt)
            otree.Fill()
            savedentries+=1

        self.disconnect()
        print '- Eventloop completed'
        print '   Saved: ', savedentries, ' events'
     
        
        



