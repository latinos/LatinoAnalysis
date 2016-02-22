
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
import numpy as np


class BWEwkSingletReweighter(TreeCloner):
    def __init__(self):
      Hmass = [200, 202, 204, 206, 208, 210, 212, 214, 216, 218, 220, 222, 224, 226, 228, 230, 232, 234, 236, 238, 240, 242, 244, 246, 248, 250, 252, 254, 256, 258, 260, 262, 264, 266, 268, 270, 272, 274, 276, 278, 280, 282, 284, 286, 288, 290, 292, 294, 296, 298, 300, 305, 310, 315, 320, 325, 330, 335, 340, 345, 350, 360, 370, 380, 390, 400, 420, 440, 450, 460, 480, 500, 520, 540, 550, 560, 580, 600, 620, 640, 650, 660, 680, 700, 720, 740, 750, 760, 780, 800, 820, 840, 850, 860, 880, 900, 920, 940, 950, 960, 980, 1000.]

      Hwidth = [1.43, 1.51, 1.59, 1.68, 1.76, 1.85, 1.93, 2.02, 2.12, 2.21, 2.31, 2.40, 2.50, 2.61, 2.71, 2.82, 2.93, 3.04, 3.16, 3.27, 3.40, 3.52, 3.64, 3.77, 3.91, 4.04, 4.18, 4.32, 4.46, 4.61, 4.76, 4.91, 5.07, 5.23, 5.39, 5.55, 5.72, 5.89, 6.07, 6.25, 6.43, 6.61, 6.80, 6.99, 7.19, 7.39, 7.59, 7.79, 8.00, 8.22, 8.43, 8.99, 9.57, 10.20, 10.80, 11.40, 12.10, 12.80, 13.50, 14.20, 15.20, 17.60, 20.20, 23.10, 26.10, 29.20, 35.90, 43.00, 46.80, 50.80, 59.10, 68.00, 77.50, 87.70, 93.00, 98.60, 110.00, 123.00, 136.00, 150.00, 158.00, 165.00, 182.00, 199.00, 217.00, 237.00, 247.00, 258.00, 280.00, 304.00, 330.00, 357.00, 371.00, 386.00, 416.00, 449.00, 484.00, 521.00, 540.00, 560.00, 602.00, 647.00];

      self.g = ROOT.TH1D("g","SM Higgs width",len(Hmass)-1,numpy.array(Hmass));
      for k,v in enumerate(Hwidth):
        self.g.SetBinContent(k+1,v);     
      pass

    def help(self):
        return '''calculate event weights in the electroweak singlet model using parameters c' and BRnew. Ranges and steps of those parameters can be specified '''

    def addOptions(self,parser):
        description = self.help()
        group = optparse.OptionGroup(parser,self.label, description)
        group.add_option('-m',    "--mass",       dest = 'mH',   help="mass point",      default=125., type='float')
        group.add_option('-i', '--cprimemin' , dest='cprimemin' , help="c' minimum value", default=0.,  type='float')
        group.add_option('-f', '--cprimemax' , dest='cprimemax' , help="c' maximum value", default=1.,  type='float')
        group.add_option('-s' , '--cprimestep', dest='cprimestep', help="c' step",          default=0.1, type='float')
        group.add_option('-l', '--brnewmin' , dest='brnewmin' ,   help="BRnew minimum value", default=0.,  type='float')
        group.add_option('-n', '--brnewmax' , dest='brnewmax' ,   help="BRnew maximum value", default=1.,  type='float')
        group.add_option('-q' , '--brnewstep', dest='brnewstep',   help="BRnew step",          default=0.1, type='float') 

        parser.add_option_group(group)
        return group

    def checkOptions(self,opts):
        self.cprimemin = opts.cprimemin
        self.cprimemax = opts.cprimemax
        self.cprimestep = opts.cprimestep
        self.brnewmin  = opts.brnewmin
        self.brnewmax  = opts.brnewmax
        self.brnewstep = opts.brnewstep
        self.mH        = opts.mH
        self.gsm       = self.g.GetBinContent(self.g.FindBin(self.mH))
        print "c' start", self.cprimemin
        print "c' stop", self.cprimemax
        print "c' step", self.cprimestep
        print "BRnew start", self.brnewmin
        print "BRnew stop", self.brnewmax
        print "BRnew step", self.brnewstep
        print "Mass", self.mH, " with SM width", self.gsm
    
    def muprime(self, k, br):
      return k*(1-br)

    def RelBreightWigner(self, m, mH, G):
      gamma = ROOT.TMath.Sqrt(mH*mH*(mH*mH+G*G))
      N = mH*G*gamma/ROOT.TMath.Sqrt(mH*mH+gamma)
      return N/((m*m-mH*mH)*(m*m-mH*mH)+mH*mH*G*G)

    def GprimeOverGsm(self, k,br):
      return k/(1-br)

    def Gprime(self, mh,k,br):
      if self.g == None:
        raise Exception("Internal histogram of higgs widths not initialized")
      return  self.GprimeOverGsm(k, br)*self.g.GetBinContent(self.g.FindBin(mh)) 

                
    def process(self,**kwargs):
        tree  = kwargs['tree']
        input = kwargs['input']
        output = kwargs['output']

        # does that work so easily and give new variable itree and otree?
        self.connect(tree,input)

        nentries = self.itree.GetEntries()
        print 'Total number of entries: ',nentries 

        self.namesOldBranchesToBeModifiedSimpleVariable = []
        rangecprime = np.arange(self.cprimemin, self.cprimemax, self.cprimestep).tolist()
        rangeBRnew  = np.arange(self.brnewmin, self.brnewmax, self.brnewstep).tolist()
        print "cprimes", rangecprime
        print "BRnews", rangeBRnew
        if (self.cprimemax) not in rangecprime:
          rangecprime.append(self.cprimemax)
        if (self.brnewmin) not in rangeBRnew:
          rangeBRnew.insert(0, self.brnewmin)
        for cprime in rangecprime:
          for BRnew in rangeBRnew:
            self.namesOldBranchesToBeModifiedSimpleVariable.append('cprime'+str(cprime)+"BRnew"+str(BRnew))
        
        # clone the tree
        self.clone(output, self.namesOldBranchesToBeModifiedSimpleVariable)

        self.oldBranchesToBeModifiedSimpleVariable = {}
        for bname in self.namesOldBranchesToBeModifiedSimpleVariable:
          bvariable = numpy.ones(1, dtype=numpy.float32)
          self.oldBranchesToBeModifiedSimpleVariable[bname] = bvariable

        # now actually connect the branches
        for bname, bvariable in self.oldBranchesToBeModifiedSimpleVariable.iteritems():
            #print " bname   = ", bname
            #print " bvariable = ", bvariable
            self.otree.Branch(bname,bvariable,bname+'/F')

        # input tree and output tree
        itree     = self.itree
        otree     = self.otree


        #----------------------------------------------------------------------------------------------------
        print '- Starting eventloop'
        step = 5000

        #for i in xrange(2000):
        for i in xrange(nentries):

            itree.GetEntry(i)

            if i > 0 and i%step == 0.:
                print i,'events processed :: ', nentries
            
            mass = itree.higgsGenmass
            for cprime in rangecprime:
              for BRnew in rangeBRnew:
                name = 'cprime'+str(cprime)+"BRnew"+str(BRnew)
                kprime = cprime**2;
                overallweight = kprime*(1-BRnew) 
                gprime = self.Gprime(self.mH, kprime, BRnew);
                self.oldBranchesToBeModifiedSimpleVariable[name][0] = self.RelBreightWigner(mass, self.mH, gprime)/self.RelBreightWigner(mass, self.mH, self.gsm)*overallweight
                #print self.oldBranchesToBeModifiedSimpleVariable[name]  
              
            otree.Fill()

        self.disconnect()
        print '- Eventloop completed'


