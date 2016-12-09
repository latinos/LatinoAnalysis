#
#
#
#
#   Quark TOP pT
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
import math

class TopGenPt(TreeCloner):
    def __init__(self):
       pass

    def help(self):
        return ''' Calculate Quark Top-Antipot pT from children at LHE level '''

    def addOptions(self,parser):
        pass

    def checkOptions(self,opts):
        pass

    def process(self,**kwargs):
        tree  = kwargs['tree']
        input = kwargs['input']
        output = kwargs['output']

        self.newbranches = ['LHEquark_top_pt',
                            'LHEquark_antitop_pt',
                            'LHEnumTOP',    
                            'LHEnumANTITOP',    
                            ]

        # does that work so easily and give new variable itree and otree?
        self.connect(tree,input)
 

        self.clone(output,self.newbranches)

                
        newbranchesVecotor = {}
        for bname in self.newbranches:
          #bvector =  ROOT.std.vector(float) ()
          bvariable = numpy.ones(1, dtype=numpy.float32)
          newbranchesVecotor[bname] = bvariable


        for bname, bvariable in newbranchesVecotor.iteritems():
            print " bname   = ", bname
            print " bvariable = ", bvariable
            self.otree.Branch(bname,bvariable,bname+'/F')


  
        nentries = self.itree.GetEntries()
        print 'Total number of entries: ',nentries 

        # input tree and output tree
        itree     = self.itree
        otree     = self.otree
        numTOP=0.
        numAntiTOP=0.
        #----------------------------------------------------------------------------------------------------
        print '- Starting eventloop'
        step = 5000

        #for i in xrange(5000):
        for i in xrange(nentries):

          itree.GetEntry(i)

          if i > 0 and i%step == 0.:
              print i,'events processed.'

          #for bname, bvector in newbranchesVecotor.iteritems():
          #    bvector.clear()
                
          #print "----------------"
          ilTop=-1;
          ilAntiTop=-1;
          inTop = -1;
          inAntiTop = -1;
          ibTop = -1;
          ibAntiTop = -1;
          
           #over Leptons
          for i in xrange(0,3): 
            if ( (getattr(itree, "std_vector_LHElepton_id")).at(i)== 11  or (getattr(itree, "std_vector_LHElepton_id")).at(i)== 13 or (getattr(itree, "std_vector_LHElepton_id")).at(i)== 15):
              ilAntiTop = i;
              #print "std_vector_LHElepton_id-AntiTOP=", i,"  ",  (getattr(itree, "std_vector_LHElepton_id")).at(i)
            if ( (getattr(itree, "std_vector_LHElepton_id")).at(i)== -11  or (getattr(itree, "std_vector_LHElepton_id")).at(i)== -13 or (getattr(itree, "std_vector_LHElepton_id")).at(i)== -15):
              ilTop = i;
              #print "std_vector_LHElepton_id-TOP=", i,"  ",  (getattr(itree, "std_vector_LHElepton_id")).at(i)

            
          #over neutrinos
          for i in xrange(0,3): 
            if ( (getattr(itree, "std_vector_LHEneutrino_id")).at(i)== -12  or (getattr(itree, "std_vector_LHEneutrino_id")).at(i)== -14 or (getattr(itree, "std_vector_LHEneutrino_id")).at(i)== -16):
              inAntiTop = i;
              #print "std_vector_LHEneutrino_id-AntiTOP=", i,"  ",  (getattr(itree, "std_vector_LHEneutrino_id")).at(i)
            if ( (getattr(itree, "std_vector_LHEneutrino_id")).at(i)== 12  or (getattr(itree, "std_vector_LHEneutrino_id")).at(i)== 14 or (getattr(itree, "std_vector_LHEneutrino_id")).at(i)== 16):
              inTop = i;
              #print "std_vector_LHEneutrino_id-TOP=", i,"  ",  (getattr(itree, "std_vector_LHEneutrino_id")).at(i)

         #over Top
          for i in xrange(0,3): 
            if ( (getattr(itree, "std_vector_LHEparton_id")).at(i)== -5):
               ibAntiTop = i;
            if ( (getattr(itree, "std_vector_LHEparton_id")).at(i)== 5):
               ibTop = i;
            
         
          Top = ROOT.TLorentzVector()
          AntiTop = ROOT.TLorentzVector()

          #print ilTop, ilAntiTop,  inTop,  inAntiTop, ibTop,  ibAntiTop
          #if(ilTop!=-1 and ilAntiTop!=-1 and  inTop!=-1 and inAntiTop!= -1 and  ibTop!= -1):
          if (ilTop != -1 and inTop != -1 and ibTop != -1 and ilAntiTop != -1 and inAntiTop != -1  ):
         
           lTop = ROOT.TLorentzVector()
           lTop.SetPtEtaPhiM((getattr(itree, "std_vector_LHElepton_pt")).at(ilTop), (getattr(itree, "std_vector_LHElepton_eta")).at(ilTop), (getattr(itree, "std_vector_LHElepton_phi")).at(ilTop), 0.)

           nTop = ROOT.TLorentzVector()
           nTop.SetPtEtaPhiM((getattr(itree, "std_vector_LHEneutrino_pt")).at(inTop), (getattr(itree, "std_vector_LHEneutrino_eta")).at(inTop), (getattr(itree, "std_vector_LHEneutrino_phi")).at(inTop), 0.)

           massDiffTop=9999.0
           index=11

           for i in xrange(0,3): 
               if ((getattr(itree, "std_vector_LHEparton_id")).at(i) == 5):
                   bTop = ROOT.TLorentzVector()
                   bTop.SetPtEtaPhiM((getattr(itree, "std_vector_LHEparton_pt")).at(i), (getattr(itree, "std_vector_LHEparton_eta")).at(i), (getattr(itree, "std_vector_LHEparton_phi")).at(i), 4.8) #chiedere a giulio
                   tempTop=ROOT.TLorentzVector()
                   tempTop = lTop+nTop+bTop;

                   if (math.fabs(tempTop.M() - 172.5) < massDiffTop):
                       massDiffTop = math.fabs(tempTop.M() - 172.5);
                       Top = tempTop;
                       LHEquark_top_pt=Top.Pt()
                       index=i
                       #print "mass W+=", (lTop+nTop).M()
           #print "pT=", LHEquark_top_pt, "mass=", Top.M(),  "leptonID=", (getattr(itree, "std_vector_LHElepton_id")).at(ilTop), "neutrinoID=", (getattr(itree, "std_vector_LHEneutrino_id")).at(inTop), "partonID=", (getattr(itree, "std_vector_LHEparton_id")).at(ibTop), "Index", index
                       

           #FOR antiTOP

           lAntiTop = ROOT.TLorentzVector()
           lAntiTop.SetPtEtaPhiM((getattr(itree, "std_vector_LHElepton_pt")).at(ilAntiTop), (getattr(itree, "std_vector_LHElepton_eta")).at(ilAntiTop), (getattr(itree, "std_vector_LHElepton_phi")).at(ilAntiTop), 0.)

           nAntiTop = ROOT.TLorentzVector()
           nAntiTop.SetPtEtaPhiM((getattr(itree, "std_vector_LHEneutrino_pt")).at(inAntiTop), (getattr(itree, "std_vector_LHEneutrino_eta")).at(inAntiTop), (getattr(itree, "std_vector_LHEneutrino_phi")).at(inAntiTop), 0.)


           massDiffAntiTop=9999.0

           for i in xrange(0,4): 
               if ((getattr(itree, "std_vector_LHEparton_id")).at(i) == 5 and index!=i):
                   #print i
                   bTop = ROOT.TLorentzVector()
                   bTop.SetPtEtaPhiM((getattr(itree, "std_vector_LHEparton_pt")).at(i), (getattr(itree, "std_vector_LHEparton_eta")).at(i), (getattr(itree, "std_vector_LHEparton_phi")).at(i), 4.8) 
                   tempTop=ROOT.TLorentzVector()
                   tempTop = lAntiTop+ nAntiTop +bTop;

                   if (math.fabs(tempTop.M() - 172.5) <  massDiffAntiTop):
                       massDiffAntiTop = math.fabs(tempTop.M() - 172.5);
                       AntiTop = tempTop;
                       LHEquark_antitop_pt=AntiTop.Pt()
                       #print "mass W-=", (lAntiTop+ nAntiTop).M()         
                       #print "Index b=", i

           #print "pT=", LHEquark_antitop_pt, "mass=", AntiTop.M(),  "leptonID=", (getattr(itree, "std_vector_LHElepton_id")).at(ilAntiTop), "neutrinoID=", (getattr(itree, "std_vector_LHEneutrino_id")).at(inAntiTop), "partonID=", (getattr(itree, "std_vector_LHEparton_id")).at(ibTop)
                       


          #FILL the TTREE
          #for bname, bvector in newbranchesVecotor.iteritems():
          #newbranchesVecotor["LHEquark_top_pt"].push_back(LHEquark_top_pt)   
          #newbranchesVecotor["LHEquark_antitop_pt"].push_back(LHEquark_antitop_pt)             
          #LHEquark_antitop_pt.push_back(LHEquark_antitop_pt)
          #for bname, bvariable in self.newbranchesVecotor.iteritems():
          #    bvariable[0] = getattr(WW, bname)()
           #newbranchesVecotor["LHEquark_antitop_pt"] = LHEquark_antitop_pt  
           #newbranchesVecotor["LHEquark_top_pt"] = LHEquark_top_pt  
 
           
          for bname, bvariable in newbranchesVecotor.iteritems():              

              if(bname == "LHEquark_top_pt"): 
                  bvariable[0] = LHEquark_top_pt  
                  numTOP=numTOP+1                 
                  #print "TOP: bvariable[0]",bvariable[0], LHEquark_top_pt, "numtop=", numTOP 

              elif(bname == "LHEnumTOP"): 
                  #numTOP=numTOP+1  
                  bvariable[0] =numTOP

              if(bname == "LHEquark_antitop_pt"): 
                  bvariable[0] = LHEquark_antitop_pt  
                  numAntiTOP=numAntiTOP+1
                  #print "ANTITOP: bvariable[0]",bvariable[0], LHEquark_antitop_pt 

              if(bname == "LHEnumANTITOP"): 
                  #numTOP=numTOP+1  
                  bvariable[0] =numAntiTOP

          otree.Fill()

        self.disconnect()
        print '- Eventloop completed'




        '''          #over Leptons
          for i in xrange(0,3): 
            if ( (getattr(itree, "std_vector_LHElepton_id")).at(i)== 11  or (getattr(itree, "std_vector_LHElepton_id")).at(i)== 13 or (getattr(itree, "std_vector_LHElepton_id")).at(i)== 15):
              ilTop = i;
            if ( (getattr(itree, "std_vector_LHElepton_id")).at(i)== -11  or (getattr(itree, "std_vector_LHElepton_id")).at(i)== -13 or (getattr(itree, "std_vector_LHElepton_id")).at(i)== -15):
              ilAntiTop = i;
            
          #over neutrinos
          for i in xrange(0,3): 
            if ( (getattr(itree, "std_vector_LHEneutrino_id")).at(i)== -12  or (getattr(itree, "std_vector_LHEneutrino_id")).at(i)== -14 or (getattr(itree, "std_vector_LHEneutrino_id")).at(i)== -16):
              inTop = i;
            if ( (getattr(itree, "std_vector_LHEneutrino_id")).at(i)== 12  or (getattr(itree, "std_vector_LHEneutrino_id")).at(i)== 14 or (getattr(itree, "std_vector_LHEneutrino_id")).at(i)== 16):
              inAntiTop = i;
            
         #over Top
          for i in xrange(0,4): 
            if ( (getattr(itree, "std_vector_LHEparton_id")).at(i)== -5):
               ibAntiTop = i;
            if ( (getattr(itree, "std_vector_LHEparton_id")).at(i)== 5):
               ibTop = i;

          '''
