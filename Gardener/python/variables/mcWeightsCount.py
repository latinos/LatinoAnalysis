#
#
#
#                         \ \        /     _)         |      |         
#     __ `__ \    __|      \ \  \   /  _ \  |   _` |  __ \   __|   __| 
#     |   |   |  (          \ \  \ /   __/  |  (   |  | | |  |   \__ \ 
#    _|  _|  _| \___|        \_/\_/  \___| _| \__, | _| |_| \__| ____/ 
#                                             |___/                    
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


class mcWeightsCounter(TreeCloner):
    def __init__(self):
       pass

    def help(self):
        return '''Add weight for mc weights'''

    def addOptions(self,parser):
        description = self.help()
        group = optparse.OptionGroup(parser,self.label, description)
        parser.add_option_group(group)

        return group


    def checkOptions(self,opts):
        pass
       
       
    def process(self,**kwargs):

        print " starting ..."

        tree  = kwargs['tree']
        input = kwargs['input']
        output = kwargs['output']

        # does that work so easily and give new variable itree and otree?
        # Histos that will be created and should be overwritten if existing
        histos2Create = ['mcWhgt','mcWhgtPos','mcWhgtNeg','mcWhgtLHE','mcEvtCount']
        self.connect(tree,input,histos2Create)
        newbranches = ['mcWeight']
        newbranches = []
        self.clone(output,newbranches)


        mcWeight        = numpy.ones(1, dtype=numpy.float32)
#       self.otree.Branch('mcWeight'  , mcWeight  , 'mcWeight/F')
        mcNegW        = numpy.ones(1, dtype=numpy.float32)
#       self.otree.Branch('mcNegW'  , mcNegW  , 'mcNegW/F')

        bvector =  ROOT.std.vector(float) ()
#       self.otree.Branch("mcWeightSyst",bvector)


        step = 5000
        nentries = 15000
        nentries = self.itree.GetEntries()
        print 'Total number of entries: ',nentries 

        #what is self.itree? what is self.otree?
        itree     = self.itree
        otree     = self.otree


        print '- Read histogram with weights'
        
        myTreeWeight = self._getRootObj(self.ifile,'mcweight')
        if myTreeWeight.__nonzero__() :       

          nentriesWeight = myTreeWeight.GetEntries()
           
          mcWeight[0] = 0
          mcNegW[0] = 0
          positive = 0
          negative = 0
  
          if nentriesWeight > 0 :
            myTreeWeight.GetEntry(0)
            print 'Syst vec size: ',str(myTreeWeight.weightsLHE.size())
            for isyst in xrange(myTreeWeight.weightsLHE.size()) :
              bvector.push_back(0)
          print 'Init done'
  
          for i in xrange(nentriesWeight):
            myTreeWeight.GetEntry(i)
            if i > 0 and i%step == 0.:
                  print i,'events processed. / ',nentriesWeight
            weightSM   = myTreeWeight.weightSM          
            weightsLHE = myTreeWeight.weightsLHE
  
            if weightSM > 0 :
               mcWeight[0] += 1
               positive += 1
               for isyst in xrange(weightsLHE.size()) : bvector[isyst] += weightsLHE.at(isyst) / weightSM
            elif weightSM < 0 :
               mcWeight[0] -= 1
               negative += 1
               for isyst in xrange(weightsLHE.size()) : bvector[isyst] -= weightsLHE.at(isyst) / weightSM
            
            #print list(bvector )
   
          print ' weight = ',  mcWeight, " = ", positive, " - ", negative      
          mcNegW[0] = 1. * (positive - negative) / (positive + negative)
  
          print '- Starting eventloop'
  
          
          for i in xrange(nentries):
          #for i in xrange(100):
  
              itree.GetEntry(i)
  
              if i > 0 and i%step == 0.:
                  print i,'events processed.'
  
              otree.Fill()
  
          print '- Eventloop completed'
  
          self.ofile.cd()
  
          h_mcCount   = ROOT.TH1F("mcEvtCount" ,"mcEvtCount"    ,1,0,1)
          h_mcWhgt    = ROOT.TH1F("mcWhgt"   ,"mcWhgt"   ,1,0,1)
          h_mcWhgtPos = ROOT.TH1F("mcWhgtPos","mcWhgtPos",1,0,1)
          h_mcWhgtNeg = ROOT.TH1F("mcWhgtNeg","mcWhgtNeg",1,0,1)
          h_mcWhgtLHE = ROOT.TH1F("mcWhgtLHE","mcWhgtLHE",len(bvector),0,len(bvector))
  
          h_mcCount.Fill(0.5,nentriesWeight) 
          h_mcWhgt.Fill(0.5,mcWeight[0])
          h_mcWhgtPos.Fill(0.5,positive)
          h_mcWhgtNeg.Fill(0.5,negative)
          for isyst in xrange(weightsLHE.size()) : h_mcWhgtLHE.Fill(isyst+0.5,bvector[isyst])        
 
          h_mcCount.Write() 
          h_mcWhgt.Write()
          h_mcWhgtPos.Write()
          h_mcWhgtNeg.Write()
          h_mcWhgtLHE.Write()

        else:
          # Else we simply copy no to loose the tree .... but hopeffuly you don't call from here
          for i in xrange(nentries):
            itree.GetEntry(i)
            if i > 0 and i%step == 0.:
                  print i,'events processed.'
            otree.Fill() 

        self.disconnect(False)
