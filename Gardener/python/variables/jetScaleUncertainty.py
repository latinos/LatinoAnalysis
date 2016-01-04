#
#
#      |     ___ \  
#      |        ) | 
#      |       __/  
#     _____| _____| 
#                                
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

class JESTreeMaker(TreeCloner):
    def __init__(self):
       pass

    def help(self):
        return '''Apply id/iso and filter lepton collection'''

    def addOptions(self,parser):
        description = self.help()
        group = optparse.OptionGroup(parser,self.label, description)
        group.add_option('-k', '--kind',   dest='kind', help='Kind of variation: -1, +1, +0.5, ...', default=1.0)
        parser.add_option_group(group)
        return group

    def checkOptions(self,opts):
        if not (hasattr(opts,'kind')):
          self.kind = 1.0
        else :    
          self.kind   = 1.0 * float(opts.kind)
        print " kind of variation = ", self.kind

    def changeOrder(self, vectorname, vector, jetOrderList) :
        # vector is already linked to the otree branch
        # vector name is the "name" of that vector to be modified
        
        #for i in range( len(getattr(self.otree, vectorname)) ) :
          #pass
          #print " --> before ", vectorname, "[", i, "] = ", getattr(self.otree, vectorname)[i]

        # take vector and clone vector
        # equivalent of: temp_vector = itree."vector"
        temp_vector = getattr(self.itree, vectorname)
        # remix the order of vector picking from the clone
        for i in range( len(jetOrderList) ) :
          #print " --> [", i, " :: ", len(jetOrderList) ,"] :::>> ", len(temp_vector), " --> ", jetOrderList[i]      
          # otree."vectorname"[i] = temp_vector[jetOrderList[i]] <--- that is the "itree" in the correct position
          # setattr(self.otree, vector + "[" + str(i) + "]", temp_vector[ jetOrderList[i] ])
          vector.push_back ( temp_vector[ jetOrderList[i] ] )
          #vector.push_back ( 10000. )
        # set the default value for the remaining
        for i in range( len(temp_vector) - len(jetOrderList) ) :
          vector.push_back ( -9999. )
          
        #for i in range( len(getattr(self.otree, vectorname)) ) :
          #pass
          #print " --> after[ " , len(jetOrderList), "] ", vectorname, "[", i, "] = ", getattr(self.otree, vectorname)[i]

    def process(self,**kwargs):
        tree  = kwargs['tree']
        input = kwargs['input']
        output = kwargs['output']
                
        # Make two output directories
        #outputSplit = os.path.split(output)
        #outputUp = os.path.join( outputSplit[0] + 'Up' , outputSplit[1] )
        #if outputUp and not os.path.exists(outputUp):
           #os.system('mkdir -p '+outputUp)
        #outputDown = os.path.join( outputSplit[0] + 'Down' , outputSplit[1] )
        #if outputDown and not os.path.exists(outputDown):
           #os.system('mkdir -p '+outputDown)
           
        # does that work so easily and give new variable itree and otree?
        self.connect(tree,input)

        nentries = self.itree.GetEntries()
        print 'Total number of entries: ',nentries 

        #
        # create branches for otree, the ones that will be modified!
        # see: https://root.cern.ch/phpBB3/viewtopic.php?t=12507
        # this is the list of variables to be modified
        #
	self.namesOldBranchesToBeModifiedVector = []
	vectorsToChange = ['std_vector_jet_']
        for b in self.itree.GetListOfBranches():
	    branchName = b.GetName()
	    for subString in vectorsToChange:
		if subString in branchName:
		    self.namesOldBranchesToBeModifiedVector.append(branchName)
        
        # and these variables NEED to be defined as functions in WWVar.C
        # e.g. mll, dphill, ...
        self.namesOldBranchesToBeModifiedSimpleVariable = [           
           'mjj',
           'njet'
           ]
        
        # jet variables with the structure "std_vector_jet_"NAME to be migrated to "jet"NAME"+number.
        # e.g. jetpt1, jeteta1, jetpt2, jeteta2, ...
        self.jetVariables = [
            'pt',
            'eta',
            'phi',
            #'mass',
            #'tche'
            ]
        
        self.jetVarList = []
        # maximum number of "single jet" variables to be saved
        maxnjets = 2 # 7 --> everything is available in form of std::vector -> these will be deprecated
        for jetVar in self.jetVariables:
          for i in xrange(maxnjets):
            self.jetVarList.append("jet"+jetVar+str(i+1))

        # clone the tree
        self.clone(output,self.namesOldBranchesToBeModifiedVector + self.namesOldBranchesToBeModifiedSimpleVariable + self.jetVarList)
        #self.clone(outputUp,self.namesOldBranchesToBeModifiedVector + self.namesOldBranchesToBeModifiedSimpleVariable + self.jetVarList)
        #self.upTree = self.otree
        #self.upFile = self.ofile
        
        # "=" in python lets the object! 
        # this is not cloning into "down" and "up" separately.
        #self.clone(outputDown,self.namesOldBranchesToBeModifiedVector + self.namesOldBranchesToBeModifiedSimpleVariable + self.jetVarList)
        #self.downTree = self.otree
        #self.downFile = self.ofile

        self.oldBranchesToBeModifiedVector = {}
        for bname in self.namesOldBranchesToBeModifiedVector:
          bvector =  ROOT.std.vector(float) ()
          self.oldBranchesToBeModifiedVector[bname] = bvector

        # now actually connect the branches
        for bname, bvector in self.oldBranchesToBeModifiedVector.iteritems():
            self.otree.Branch(bname,bvector)
            #self.upTree.Branch(bname,bvector)
            #self.downTree.Branch(bname,bvector)

        self.oldBranchesToBeModifiedSimpleVariable = {}
        for bname in self.namesOldBranchesToBeModifiedSimpleVariable:
          bvariable = numpy.ones(1, dtype=numpy.float32)
          self.oldBranchesToBeModifiedSimpleVariable[bname] = bvariable

        # now actually connect the branches
        for bname, bvariable in self.oldBranchesToBeModifiedSimpleVariable.iteritems():
            self.otree.Branch(bname,bvariable,bname+'/F')
            #self.upTree.Branch(bname,bvariable,bname+'/F')
            #self.downTree.Branch(bname,bvariable,bname+'/F')

        #self.jetVarDic = OrderedDict()
        self.jetVarDic = {}
        for bname in self.jetVarList:
          bvariable = numpy.ones(1, dtype=numpy.float32)
          self.jetVarDic[bname] = bvariable

        # now actually connect the branches
        for bname, bvariable in self.jetVarDic.iteritems():
            #print " bname   = ", bname
            #print " bvariable = ", bvariable
            self.otree.Branch(bname,bvariable,bname+'/F')
            #self.upTree.Branch(bname,bvariable,bname+'/F')
            #self.downTree.Branch(bname,bvariable,bname+'/F')
         
        # input tree  
        itree = self.itree

        # change this part into correct path structure... 
        cmssw_base = os.getenv('CMSSW_BASE')
        try:
            ROOT.gROOT.LoadMacro(cmssw_base+'/src/LatinoAnalysis/Gardener/python/variables/WWVar.C+g')

        except RuntimeError:
            ROOT.gROOT.LoadMacro(cmssw_base+'/src/LatinoAnalysis/Gardener/python/variables/WWVar.C++g')

        # Load jes uncertainty
        jecUnc = ROOT.JetCorrectionUncertainty(os.path.expandvars("${CMSSW_BASE}/src/LatinoAnalysis/Gardener/input/Summer15_25nsV6_MC_Uncertainty_AK4PFchs.txt"))
        #----------------------------------------------------------------------------------------------------
        print '- Starting eventloop'
        step = 5000
        #step = 1

        # to be used later on in the code ...
        new_std_vector_jet_pt = ROOT.std.vector(float) ()
        new_std_vector_jet_eta  = ROOT.std.vector(float) ()
        
        #for i in xrange(10000):
        #for i in xrange(2000):
        for i in xrange(nentries):
            itree.GetEntry(i)

            if i > 0 and i%step == 0.:
              print i,'events processed :: ', nentries
                
            # scale jet pt
            # Scale Up
            jetPtUp = []
            #print " itree.std_vector_jet_pt.size() = ", itree.std_vector_jet_pt.size()
            
            for i in range(itree.std_vector_jet_pt.size()):
                if itree.std_vector_jet_pt[i] > 0:
                    jecUnc.setJetEta(itree.std_vector_jet_eta[i])
                    jecUnc.setJetPt(itree.std_vector_jet_pt[i])
                    jetPtUp.append(itree.std_vector_jet_pt[i]*(1 + (self.kind) * (jecUnc.getUncertainty(True))))
                else:
                    break
                
            jetOrderUp = sorted(range(len(jetPtUp)), key=lambda k: jetPtUp[k], reverse=True)
                           
            for bname, bvector in self.oldBranchesToBeModifiedVector.iteritems():
                bvector.clear()
                if 'jet_pt' in bname:
                    for i in range( len(jetOrderUp) ) :
                        bvector.push_back ( jetPtUp[jetOrderUp[i]] )
                    for i in range( len(getattr(self.itree, bname)) - len(jetOrderUp) ) :
                        bvector.push_back ( -9999. )
                else:
                    self.changeOrder( bname, bvector, jetOrderUp)
            
            #print "    jetOrderUp.size() = ", len(jetOrderUp)
            #print "    jetPtUp.size() = ", len(jetPtUp)
            
            if len(jetPtUp) > 1:
                #print "    jetOrderUp[0] = ", jetOrderUp[0]
                #print "    jetOrderUp[1] = ", jetOrderUp[1]
                jetpt1 = jetPtUp[jetOrderUp[0]]
                jetpt2 = jetPtUp[jetOrderUp[1]]
                jeteta1 = itree.std_vector_jet_eta[jetOrderUp[0]]
                jeteta2 = itree.std_vector_jet_eta[jetOrderUp[1]]
                jetphi1 = itree.std_vector_jet_phi[jetOrderUp[0]]
                jetphi2 = itree.std_vector_jet_phi[jetOrderUp[1]]
                jetmass1 = itree.std_vector_jet_mass[jetOrderUp[0]]
                jetmass2 = itree.std_vector_jet_mass[jetOrderUp[1]]
                WWUp = ROOT.WW(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, jetpt1, jetpt2, jeteta1, jeteta2, jetphi1, jetphi2, jetmass1, jetmass2)
            else:
                WWUp = ROOT.WW(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
 
            #print "    here 1 "

            # set the list of jets into the object "WW"
            new_std_vector_jet_pt.clear()
            new_std_vector_jet_eta.clear()
            for iGoodJet in jetOrderUp :
                new_std_vector_jet_pt.push_back( jetPtUp[ iGoodJet ])
                new_std_vector_jet_eta.push_back(jetPtUp[ iGoodJet ])
            WWUp.setJets(new_std_vector_jet_pt, new_std_vector_jet_eta)

            #print "    here 2 "
        
            # now fill the variables like "mjj", "njets" ...
            for bname, bvariable in self.oldBranchesToBeModifiedSimpleVariable.iteritems():
                #print "       >> bname = ", bname
                bvariable[0] = getattr(WWUp, bname)()   

            #print "    here 3 "
                
            # refill the single jet variables
            counter = 0
            varCounter = 0
            for bname, bvariable in self.jetVarDic.iteritems():
                if counter < len(jetOrderUp):
                    if 'jetpt' in bname:
                        bvariable[0] = jetPtUp[ jetOrderUp[counter] ]
                    else:
                        bvariable[0] = (getattr(self.itree, 'std_vector_jet_'+self.jetVariables[varCounter] ))[ jetOrderUp[counter] ]
                    counter += 1
                else:
                    bvariable[0] = -9999.
                if counter == maxnjets:
                    varCounter += 1
                    counter = 0

            self.otree.Fill()
            #self.upTree.Fill()
            
            
            
            # Scale Down
            #jetPtDown = []
            #for i in range(itree.std_vector_jet_pt.size()):
                #if itree.std_vector_jet_pt[i] > 0:
                    #jecUnc.setJetEta(itree.std_vector_jet_eta[i])
                    #jecUnc.setJetPt(itree.std_vector_jet_pt[i])
                    #jetPtDown.append(itree.std_vector_jet_pt[i]*(1-jecUnc.getUncertainty(False)))
                #else:
                     #break
            #jetOrderDown = sorted(range(len(jetPtDown)), key=lambda k: jetPtDown[k], reverse=True)
                    
            #for bname, bvector in self.oldBranchesToBeModifiedVector.iteritems():
                #bvector.clear()
                #if 'jet_pt' in bname:
                    #for i in range( len(jetOrderDown) ) :
                        #bvector.push_back ( jetPtDown[jetOrderDown[i]] )
                    #for i in range( len(getattr(self.itree, bname)) - len(jetOrderDown) ) :
                        #bvector.push_back ( -9999. )
                #else:
                    #self.changeOrder( bname, bvector, jetOrderDown)
                    
            #if len(jetPtDown) > 1:
                ##print "    jetOrderDown[0] = ", jetOrderDown[0]
                ##print "    jetOrderDown[1] = ", jetOrderDown[1]
                #jetpt1 = jetPtDown[jetOrderDown[0]]
                #jetpt2 = jetPtDown[jetOrderDown[1]]
                #jeteta1 = itree.std_vector_jet_eta[jetOrderDown[0]]
                #jeteta2 = itree.std_vector_jet_eta[jetOrderDown[1]]
                #jetphi1 = itree.std_vector_jet_phi[jetOrderDown[0]]
                #jetphi2 = itree.std_vector_jet_phi[jetOrderDown[1]]
                #jetmass1 = itree.std_vector_jet_mass[jetOrderDown[0]]
                #jetmass2 = itree.std_vector_jet_mass[jetOrderDown[1]]
                #WWDown = ROOT.WW(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, jetpt1, jetpt2, jeteta1, jeteta2, jetphi1, jetphi2, jetmass1, jetmass2)
            #else:
                #WWDown = ROOT.WW(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
            ## set the list of jets into the object "WW"
            #new_std_vector_jet_pt.clear()
            #new_std_vector_jet_eta.clear()
            #for iGoodJet in jetOrderDown :
                #new_std_vector_jet_pt.push_back( jetPtDown[ iGoodJet ])
                #new_std_vector_jet_eta.push_back(jetPtDown[ iGoodJet ])
            #WWDown.setJets(new_std_vector_jet_pt, new_std_vector_jet_eta)
        
            ## now fill the variables like "mjj", "njets" ...
            #for bname, bvariable in self.oldBranchesToBeModifiedSimpleVariable.iteritems():
                #bvariable[0] = getattr(WWDown, bname)()  
                
            ## refill the single jet variables
            #counter = 0
            #varCounter = 0
            #for bname, bvariable in self.jetVarDic.iteritems():
                #if counter < len(jetOrderDown):
                    #if 'jetpt' in bname:
                        #bvariable[0] = jetPtDown[ jetOrderDown[counter] ]
                    #else:
                        #bvariable[0] = (getattr(self.itree, 'std_vector_jet_'+self.jetVariables[varCounter] ))[ jetOrderDown[counter] ]
                    #counter += 1
                #else:
                    #bvariable[0] = -9999.
                #if counter == maxnjets:
                    #varCounter += 1
                    #counter = 0
                        
            #self.downTree.Fill()

        #self.otree = self.upTree
        #self.ofile = self.upFile
        #self.disconnect(True,False)
        
        #self.otree = self.downTree
        #self.ofile = self.downFile
        self.disconnect(True,True)
        
        print '- Eventloop completed'

