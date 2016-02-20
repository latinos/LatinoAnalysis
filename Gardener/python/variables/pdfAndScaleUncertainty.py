#
# 
#    _ \   __ \   ____|                        |       ___|                |            |   |                           |          _)         |          
#   |   |  |   |  |           _` |  __ \    _` |     \___ \    __|   _` |  |   _ \      |   |  __ \    __|   _ \   __|  __|   _` |  |  __ \   __|  |   | 
#   ___/   |   |  __|        (   |  |   |  (   |           |  (     (   |  |   __/      |   |  |   |  (      __/  |     |    (   |  |  |   |  |    |   | 
#  _|     ____/  _|         \__,_| _|  _| \__,_|     _____/  \___| \__,_| _| \___|     \___/  _|  _| \___| \___| _|    \__| \__,_| _| _|  _| \__| \__, | 
#                                                                                                                                                 ____/  
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
from array import array;

class PdfAndScaleUncertaintyTreeMaker(TreeCloner) :
    def __init__(self) :
       pass

    def help(self) :
        return '''PDF and scale uncertainty'''

    def addOptions(self,parser) :
        description = self.help()
        group = optparse.OptionGroup(parser,self.label, description)
        group.add_option('-c', '--cmssw', dest='cmssw', help='cmssw version (naming convention may change)', default='763')
        group.add_option('-k',  '--kind', dest='kind',  help='<Up|Dn> variation', default='Up', type='string')
        parser.add_option_group(group)
        return group

    def checkOptions(self,opts) :
        self.cmssw = opts.cmssw
        self.kind  = opts.kind
        print " cmssw =", self.cmssw
        print "  kind =", self.kind

    def process(self,**kwargs) :
        tree   = kwargs['tree']
        input  = kwargs['input']
        output = kwargs['output']

        self.connect(tree,input)

        nentries = self.itree.GetEntries()
        print ' - Input entries:', nentries 
        savedentries = 0

        # Create branches for otree, the ones that will be modified
        self.pdfVariables = [ 'pdfScaleUp', 'pdfScaleDn', 'pdfScaleMd' ]
        self.RFVariables  = [ 'RFUp', 'RFDn', 'RFMd' ]

        # Clone the tree with new branches added
        self.clone(output, self.pdfVariables)
        self.clone(output, self.RFVariables)
      
        # Now actually connect the branches
        pdfUp = numpy.ones(1, dtype=numpy.float32)
        pdfDn = numpy.ones(1, dtype=numpy.float32)
        pdfMd = numpy.ones(1, dtype=numpy.float32)

        RFUp = numpy.ones(1, dtype=numpy.float32)
        RFDn = numpy.ones(1, dtype=numpy.float32)
        RFMd = numpy.ones(1, dtype=numpy.float32)


        self.otree.Branch('pdfScaleUp',    pdfUp, 'pdfScaleUp/F')
        self.otree.Branch('pdfScaleDn',    pdfDn, 'pdfScaleDn/F')
        self.otree.Branch('pdfScaleMd',    pdfMd, 'pdfScaleMd/F')

        self.otree.Branch('RFUp', RFUp, 'RFUp/F')
        self.otree.Branch('RFDn', RFDn, 'RFDn/F')
        self.otree.Branch('RFMd', RFMd, 'RFMd/F')

        # Input tree  
        itree = self.itree

        # Weights Histo
        #weightsHisto = self.itreeMcWeightExplainedOrdered
        #histoEntries = weightsHisto.GetEntries()
        #loopStart = 0
        #countEntries = range (1, int(histoEntries))

        #for contHisto in countEntries:
        #    loopStart = contHisto
        #    label = ROOT.TString(weightsHisto.GetXaxis().GetBinLabel(loopStart))
        #    if (label.Contains("PDF set")):
        #       break

        # Labels start from Bin 1, vector starts from bin 0
        #loopStart = loopStart - 1

        # pdfHisto & QCDhisto
        pdfHisto = ROOT.TH1F("pdfHisto", "pdfHisto", 200, 0., 3.)
        RFHisto  = ROOT.TH1F("RFHisto" , "RFHisto" , 200, 0., 3.)

        #-----------------------------------------------------------------------
        print ' - Starting event loop'
        step = 5000

        for i in xrange(nentries) :
          itree.GetEntry(i)

          default_weight = itree.std_vector_LHE_weight[0]
          print " default_weight = ", default_weight
          
          #pdfRange = range(loopStart,itree.std_vector_LHE_weight.size())
          pdfRange = range(9, 108)
          for count in pdfRange:
              print " itree.std_vector_LHE_weight[", count, "] = ", itree.std_vector_LHE_weight[count]
              pdfHisto.Fill(itree.std_vector_LHE_weight[count] / default_weight)
              #if (itree.std_vector_LHE_weight[count] == 1):
              #    print 'posizione = ', count

          RFRange = range(1, 8)
          for count in RFRange:
              print " itree.std_vector_LHE_weight[", count, "] = ", itree.std_vector_LHE_weight[count]
              RFHisto.Fill(itree.std_vector_LHE_weight[count] / default_weight)

          scaleMd = pdfHisto.GetMean()
          scaleUp = scaleMd + pdfHisto.GetRMS()
          scaleDn = scaleMd - pdfHisto.GetRMS()

          pdfUp[0] = scaleUp / scaleMd
          pdfDn[0] = scaleDn / scaleMd
          pdfMd[0] = scaleMd


          RFmean = RFHisto.GetMean()
          RFup   = RFMd + RFHisto.GetRMS()
          RFdown = RFMd - RFHisto.GetRMS()

          RFUp[0] = RFup   / RFmean
          RFDn[0] = RFdown / RFmean
          RFMd[0] = RFmean

          if (i > 0 and i%step == 0.) :
              print i,'events processed ::', nentries, 'Scale Dn:', pdfDn[0], 'Scale Md:', pdfMd[0], 'Scale Up:', pdfUp[0]

          if (i > 0 and i%step == 1.) :
              print i, 'RF Dn:', RFDn[0], 'RF Md:', RFMd[0], 'RF Up:', RFUp[0]
              
          self.otree.Fill()
          savedentries+=1
          
        self.disconnect()
        print ' - Event loop completed'
        print ' - Saved entries:', savedentries
