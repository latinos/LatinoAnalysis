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

class LeppTScalerTreeMaker(TreeCloner):
    def __init__(self):
       pass

    def help(self):
        return '''Lepton pT scaler'''

    def addOptions(self,parser):
        description = self.help()
        group = optparse.OptionGroup(parser,self.label, description)
        group.add_option('-m',  '--muScl',    dest='kind_mu', help='Kind of variation for mu : -1, +1, +0.5, ...', default=1.0)
        group.add_option('-b', '--eEBScl',   dest='kind_eEB', help='Kind of variation for el in EB: -1, +1, +0.5, ...', default=1.0)
        group.add_option('-e', '--eEEScl',   dest='kind_eEE', help='Kind of variation for el in EE: -1, +1, +0.5, ...', default=1.0)
        parser.add_option_group(group)
        return group

    def checkOptions(self,opts):
        if not (hasattr(opts,'kind_mu')):
          self.kind_mu = 1.0
        else :    
          self.kind_mu   = 1.0 * float(opts.kind_mu)
        if not (hasattr(opts,'kind_eEB')):
          self.kind_eEB = 1.0
        else :    
          self.kind_eEB   = 1.0 * float(opts.kind_eEB)
        if not (hasattr(opts,'kind_eEE')):
          self.kind_eEE = 1.0
        else :    
          self.kind_eEE   = 1.0 * float(opts.kind_eEE)

#        print " kind of variation for muon elinEB elinEE= ", self.kind_mu, self.kind_eEB, self.kind_eEE

    def changeOrder(self, vectorname, vector, leptonOrderList) :
        # vector is already linked to the otree branch
        # vector name is the "name" of that vector to be modified        
        #for i in range( len(getattr(self.otree, vectorname)) ) :
          #pass
          #print " --> before ", vectorname, "[", i, "] = ", getattr(self.otree, vectorname)[i]

        # take vector and clone vector
        # equivalent of: temp_vector = itree."vector"
        temp_vector = getattr(self.itree, vectorname)
        # remix the order of vector picking from the clone
        for i in range( len(leptonOrderList) ) :
          #print " --> [", i, " :: ", len(leptonOrderList) ,"] :::>> ", len(temp_vector), " --> ", leptonOrderList[i]      
          # otree."vectorname"[i] = temp_vector[leptonOrderList[i]] <--- that is the "itree" in the correct position
          # setattr(self.otree, vector + "[" + str(i) + "]", temp_vector[ leptonOrderList[i] ])
          vector.push_back ( temp_vector[ leptonOrderList[i] ] )
          #vector.push_back ( 10000. )
        # set the default value for the remaining
        for i in range( len(temp_vector) - len(leptonOrderList) ) :
          vector.push_back ( -9999. )
          
        #for i in range( len(getattr(self.otree, vectorname)) ) :
          #pass
          #print " --> after[ " , len(leptonOrderList), "] ", vectorname, "[", i, "] = ", getattr(self.otree, vectorname)[i]

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
	vectorsToChange = ['std_vector_lepton_']
        for b in self.itree.GetListOfBranches():
	    branchName = b.GetName()
	    for subString in vectorsToChange:
		if subString in branchName:
		    self.namesOldBranchesToBeModifiedVector.append(branchName)
        
        # and these variables NEED to be defined as functions in WWVar.C
        # e.g. mll, dphill, ...
        self.namesOldBranchesToBeModifiedSimpleVariable = [           
           'mll',
           'dphill',
           'yll',
           #'pt1',
           #'pt2',
           #'mth',
           #'mcoll',
           'channel',
#           'drll',
 #          'dphilljet',
  #         'dphilljetjet',
   #        'dphilmet',
    #       'dphilmet1',
     #      'dphilmet2',
           #'mtW1',
           #'mtW2',
           'ptll'
           ]
        
        # lepton variables with the structure "std_vector_lepton_"NAME to be migrated to "lepton"NAME"+number.
        # e.g. leptonpt1, leptoneta1, leptonpt2, leptoneta2, ...
        self.leptonVariables = [
            'pt',
            'eta',
            'phi',
            'flavour'
            ]
        
        self.leptonVarList = []
        # maximum number of "single lepton" variables to be saved
        maxnleptons = 3 # 7 --> everything is available in form of std::vector -> these will be deprecated
        for leptonVar in self.leptonVariables:
            for i in xrange(maxnleptons):
                self.leptonVarList.append("lepton"+leptonVar+str(i+1)) # setting lepton pt1,eta1,phi1 etc

        # clone the tree with new branches added
        self.clone(output,self.namesOldBranchesToBeModifiedVector + self.namesOldBranchesToBeModifiedSimpleVariable + self.leptonVarList)
      
        self.oldBranchesToBeModifiedVector = {}
        for bname in self.namesOldBranchesToBeModifiedVector:
          bvector =  ROOT.std.vector(float) ()
          self.oldBranchesToBeModifiedVector[bname] = bvector
#          print "debug 0 ", bname

        # now actually connect the branches
        for bname, bvector in self.oldBranchesToBeModifiedVector.iteritems():
          self.otree.Branch(bname,bvector)            

        self.oldBranchesToBeModifiedSimpleVariable = {}
        for bname in self.namesOldBranchesToBeModifiedSimpleVariable:
            bvariable = numpy.ones(1, dtype=numpy.float32)
            self.oldBranchesToBeModifiedSimpleVariable[bname] = bvariable

        # now actually connect the branches (modifying ptll, mll,mll,etc)
        for bname, bvariable in self.oldBranchesToBeModifiedSimpleVariable.iteritems():
            self.otree.Branch(bname,bvariable,bname+'/F')
            
        #self.leptonVarDic = OrderedDict()
        self.leptonVarDic = {}
        for bname in self.leptonVarList:
          bvariable = numpy.ones(1, dtype=numpy.float32)
          self.leptonVarDic[bname] = bvariable
        # now actually connect the branches
        for bname, bvariable in self.leptonVarDic.iteritems():
#            print " bname in tree  = ", bname
 #           print " bvariable in tree= ", bvariable
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

        #----------------------------------------------------------------------------------------------------
        print '- Starting eventloop'
        step = 5000
        #step = 1

        # to be used later on in the code ... 
        new_std_vector_lepton_pt       = ROOT.std.vector(float) ()
        new_std_vector_lepton_eta      = ROOT.std.vector(float) ()
        new_std_vector_lepton_phi      = ROOT.std.vector(float) ()
        new_std_vector_lepton_flavour  = ROOT.std.vector(float) ()

        #for i in xrange(10000):
        #for i in xrange(2000):
        for i in xrange(nentries):
            itree.GetEntry(i)

            if i > 0 and i%step == 0.:
              print i,'events processed :: ', nentries
                
            # scale lepton pt
            # Scale Up
            leptonPtUp = []
#            print " itree.std_vector_lepton_pt.size() = ", itree.std_vector_lepton_pt.size()
            
            for i in range(itree.std_vector_lepton_pt.size()):
                if not (itree.std_vector_lepton_pt[i] > 0):
                    continue
 #               print "org pt ",itree.std_vector_lepton_pt[i]
  #              print "org flav ",itree.std_vector_lepton_flavour[i]
                if abs(itree.std_vector_lepton_flavour[i])==13:
                    leptonPtUp.append(itree.std_vector_lepton_pt[i]*(1 + (self.kind_mu/100)))
                elif abs(itree.std_vector_lepton_flavour[i])==11:
                    if abs(itree.std_vector_lepton_eta[i]) <=1.479:
                        leptonPtUp.append(itree.std_vector_lepton_pt[i]*(1 + (self.kind_eEB/100)))
                    elif (abs(itree.std_vector_lepton_eta[i]) <1.479 or abs (itree.std_vector_lepton_eta[i]) <=2.5 ):
                        leptonPtUp.append(itree.std_vector_lepton_pt[i]*(1 + (self.kind_eEE/100)))          
#                        print "modified pt for EE",itree.std_vector_lepton_pt[i]*(1 + (self.kind_eEE/100))
                    else: 
                        pass
                else:
                    break
                    
            leptonOrderUp = sorted(range(len(leptonPtUp)), key=lambda k: leptonPtUp[k], reverse=True) # sorting in descending order and storing index
                           
            for bname, bvector in self.oldBranchesToBeModifiedVector.iteritems():
                bvector.clear()
                if 'lepton_pt' in bname:
                    for i in range( len(leptonOrderUp) ) :
                        bvector.push_back ( leptonPtUp[leptonOrderUp[i]] )
                    for i in range( len(getattr(self.itree, bname)) - len(leptonOrderUp) ) :
                        bvector.push_back ( -9999. )
                else:
                    self.changeOrder( bname, bvector, leptonOrderUp)
            
#            print "    leptonOrderUp.size() = ", len(leptonOrderUp)
 #           print "    leptonPtUp.size() = ", len(leptonPtUp)

            if len(leptonPtUp) > 1:
  #              print "    leptonOrderUp[0] = ", leptonOrderUp[0]
   #             print "    leptonOrderUp[1] = ", leptonOrderUp[1]
                leptonpt1 = leptonPtUp[leptonOrderUp[0]] #using index returned after sorting
                leptonpt2 = leptonPtUp[leptonOrderUp[1]]
                leptoneta1 = itree.std_vector_lepton_eta[leptonOrderUp[0]]
                leptoneta2 = itree.std_vector_lepton_eta[leptonOrderUp[1]]
                leptonphi1 = itree.std_vector_lepton_phi[leptonOrderUp[0]]
                leptonphi2 = itree.std_vector_lepton_phi[leptonOrderUp[1]]
                leptonflavour1 = itree.std_vector_lepton_flavour[leptonOrderUp[0]]
                leptonflavour2 = itree.std_vector_lepton_flavour[leptonOrderUp[1]]
#                print " id1 ",leptonflavour1
 #               print " id2 ",leptonflavour2
#                print "leptonpt1 leptonpt2", leptonpt1, leptonpt2
                WWUp = ROOT.WW(leptonpt1, leptonpt2, leptoneta1, leptoneta2, leptonphi1, leptonphi2,leptonflavour1,leptonflavour2,0,0)
            elif len(leptonPtUp) > 2:
                #              print "    leptonOrderUp[0] = ", leptonOrderUp[0]
                #             print "    leptonOrderUp[1] = ", leptonOrderUp[1]
                leptonpt1 = leptonPtUp[leptonOrderUp[0]] #using index returned after sorting
                leptonpt2 = leptonPtUp[leptonOrderUp[1]]
                leptonpt3 = leptonPtUp[leptonOrderUp[2]]
                leptoneta1 = itree.std_vector_lepton_eta[leptonOrderUp[0]]
                leptoneta2 = itree.std_vector_lepton_eta[leptonOrderUp[1]]
                leptoneta3 = itree.std_vector_lepton_eta[leptonOrderUp[2]]
                leptonphi1 = itree.std_vector_lepton_phi[leptonOrderUp[0]]
                leptonphi2 = itree.std_vector_lepton_phi[leptonOrderUp[1]]
                leptonphi3 = itree.std_vector_lepton_phi[leptonOrderUp[2]]
                leptonflavour1 = itree.std_vector_lepton_flavour[leptonOrderUp[0]]
                leptonflavour2 = itree.std_vector_lepton_flavour[leptonOrderUp[1]]
                leptonflavour3 = itree.std_vector_lepton_flavour[leptonOrderUp[2]]
#                print " flavour1 ",leptonflavour1
 #               print " flavour2 ",leptonflavour2
  #              print " flavour3 ",leptonflavour3
#                print "leptonpt1 leptonpt2 3", leptonpt1, leptonpt2,leptonpt3
                WWUp = ROOT.WW(leptonpt1, leptonpt2, leptoneta1, leptoneta2, leptonphi1, leptonphi2,leptonflavour1,leptonflavour2,0,0)
                
            else:
                WWUp = ROOT.WW(0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
                

            # set the list of leptons into the object "WW"
            new_std_vector_lepton_pt.clear()
            new_std_vector_lepton_eta.clear()
            new_std_vector_lepton_phi.clear()
            new_std_vector_lepton_flavour.clear()
#            print "    here 1 "

            for iGoodLepton in leptonOrderUp :
 #               print "Good lepton section",leptonPtUp[ iGoodLepton ]
                new_std_vector_lepton_pt.push_back(leptonPtUp[ iGoodLepton ])
                new_std_vector_lepton_eta.push_back(leptonPtUp[ iGoodLepton ])
                new_std_vector_lepton_phi.push_back(leptonPtUp[ iGoodLepton ])
                new_std_vector_lepton_flavour.push_back(leptonPtUp[ iGoodLepton ])

 #           print "    here 1.1 "

            WWUp.setLeptons(new_std_vector_lepton_pt, new_std_vector_lepton_eta,new_std_vector_lepton_phi,new_std_vector_lepton_flavour)

  #          print "    here 2 "
        
            # now fill the variables like mll mtW1,2 .....
            for bname, bvariable in self.oldBranchesToBeModifiedSimpleVariable.iteritems():
#                print "       >> bname = ", bname
                bvariable[0] = getattr(WWUp, bname)()   

   #         print "    here 3 "
                
            # refill the lepton variables
            counter = 0
            varCounter = 0
            for bname, bvariable in self.leptonVarDic.iteritems():
                if counter < len(leptonOrderUp):
                    if 'leptonpt' in bname:
  #                      print "bname ins last sec", bname
                        bvariable[0] = leptonPtUp[ leptonOrderUp[counter] ]
                    else:
                        bvariable[0] = (getattr(self.itree, 'std_vector_lepton_'+self.leptonVariables[varCounter] ))[ leptonOrderUp[counter] ]
                    counter += 1
                else:
                    bvariable[0] = -9999.
                if counter == maxnleptons:
                    varCounter += 1
                    counter = 0

            self.otree.Fill()
            
            
            
            
            # Scale Down
            #leptonPtDown = []
            #for i in range(itree.std_vector_lepton_pt.size()):
                #if itree.std_vector_lepton_pt[i] > 0:
                    #jecUnc.setLeptonEta(itree.std_vector_lepton_eta[i])
                    #jecUnc.setLeptonPt(itree.std_vector_lepton_pt[i])
                    #leptonPtDown.append(itree.std_vector_lepton_pt[i]*(1-jecUnc.getUncertainty(False)))
                #else:
                     #break
            #leptonOrderDown = sorted(range(len(leptonPtDown)), key=lambda k: leptonPtDown[k], reverse=True)
                    
            #for bname, bvector in self.oldBranchesToBeModifiedVector.iteritems():
                #bvector.clear()
                #if 'lepton_pt' in bname:
                    #for i in range( len(leptonOrderDown) ) :
                        #bvector.push_back ( leptonPtDown[leptonOrderDown[i]] )
                    #for i in range( len(getattr(self.itree, bname)) - len(leptonOrderDown) ) :
                        #bvector.push_back ( -9999. )
                #else:
                    #self.changeOrder( bname, bvector, leptonOrderDown)
                    
            #if len(leptonPtDown) > 1:
                ##print "    leptonOrderDown[0] = ", leptonOrderDown[0]
                ##print "    leptonOrderDown[1] = ", leptonOrderDown[1]
                #leptonpt1 = leptonPtDown[leptonOrderDown[0]]
                #leptonpt2 = leptonPtDown[leptonOrderDown[1]]
                #leptoneta1 = itree.std_vector_lepton_eta[leptonOrderDown[0]]
                #leptoneta2 = itree.std_vector_lepton_eta[leptonOrderDown[1]]
                #leptonphi1 = itree.std_vector_lepton_phi[leptonOrderDown[0]]
                #leptonphi2 = itree.std_vector_lepton_phi[leptonOrderDown[1]]
                #leptonmass1 = itree.std_vector_lepton_mass[leptonOrderDown[0]]
                #leptonmass2 = itree.std_vector_lepton_mass[leptonOrderDown[1]]
                #WWDown = ROOT.WW(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, leptonpt1, leptonpt2, leptoneta1, leptoneta2, leptonphi1, leptonphi2, leptonmass1, leptonmass2)
            #else:
                #WWDown = ROOT.WW(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
            ## set the list of leptons into the object "WW"
            #new_std_vector_lepton_pt.clear()
            #new_std_vector_lepton_eta.clear()
            #for iGoodLepton in leptonOrderDown :
                #new_std_vector_lepton_pt.push_back( leptonPtDown[ iGoodLepton ])
                #new_std_vector_lepton_eta.push_back(leptonPtDown[ iGoodLepton ])
            #WWDown.setLeptons(new_std_vector_lepton_pt, new_std_vector_lepton_eta)
        
            ## now fill the variables like "mjj", "nleptons" ...
            #for bname, bvariable in self.oldBranchesToBeModifiedSimpleVariable.iteritems():
                #bvariable[0] = getattr(WWDown, bname)()  
                
            ## refill the single lepton variables
            #counter = 0
            #varCounter = 0
            #for bname, bvariable in self.leptonVarDic.iteritems():
                #if counter < len(leptonOrderDown):
                    #if 'leptonpt' in bname:
                        #bvariable[0] = leptonPtDown[ leptonOrderDown[counter] ]
                    #else:
                        #bvariable[0] = (getattr(self.itree, 'std_vector_lepton_'+self.leptonVariables[varCounter] ))[ leptonOrderDown[counter] ]
                    #counter += 1
                #else:
                    #bvariable[0] = -9999.
                #if counter == maxnleptons:
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

