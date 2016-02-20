#
#  _____  _____  ______                             _        _       _         
# |  __ \|  __ \|  ____|                           | |      (_)     | |        
# | |__) | |  | | |__     _   _ _ __   ___ ___ _ __| |_ __ _ _ _ __ | |_ _   _ 
# |  ___/| |  | |  __|   | | | | '_ \ / __/ _ \ '__| __/ _` | | '_ \| __| | | |
# | |    | |__| | |      | |_| | | | | (_|  __/ |  | || (_| | | | | | |_| |_| |
# |_|    |_____/|_|       \__,_|_| |_|\___\___|_|   \__\__,_|_|_| |_|\__|\__, |
#                                                                         __/ |
#                                                                        |___/ 



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

class PdfUncertaintyTreeMaker(TreeCloner) :
    def __init__(self) :
       pass

    def help(self) :
        return '''PDF uncertainty'''

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
        
        # Clone the tree with new branches added
        self.clone(output, self.pdfVariables)
      
        # Now actually connect the branches
        pdfUp = numpy.ones(1, dtype=numpy.float32)
        pdfDn = numpy.ones(1, dtype=numpy.float32)
        pdfMd = numpy.ones(1, dtype=numpy.float32)

        self.otree.Branch('pdfScaleUp',    pdfUp, 'pdfScaleUp/F')
        self.otree.Branch('pdfScaleDn',    pdfDn, 'pdfScaleDn/F')
        self.otree.Branch('pdfScaleMd',    pdfMd, 'pdfScaleMd/F')

        # Input tree  
        itree = self.itree

        # Weights Histo
        weightsHisto = self.itreeMcWeightExplainedOrdered
        histoEntries = weightsHisto.GetEntries()
        loopStart = 0
        countEntries = range (1, int(histoEntries))

        for contHisto in countEntries:
            loopStart = contHisto
            label = ROOT.TString(weightsHisto.GetXaxis().GetBinLabel(loopStart))
            print " label ", contHisto, " = ", label
            if (label.Contains("PDF set")):
                break

        # Labels start from Bin 1, vector starts from bin 0
        loopStart = loopStart - 1

        # pdfHisto
        pdfHisto = ROOT.TH1F("pdfHisto", "pdfHisto", 200, 0., 10.)

        #-----------------------------------------------------------------------
        print ' - Starting event loop'
        step = 5000

        for i in xrange(nentries) :
          itree.GetEntry(i)

          pdfRange = range(loopStart,itree.std_vector_LHE_weight.size())
          for count in pdfRange:
              print " itree.std_vector_LHE_weight[", count, "] = ", itree.std_vector_LHE_weight[count]
              pdfHisto.Fill(itree.std_vector_LHE_weight[count])
              if (itree.std_vector_LHE_weight[count] == 1):
                  print 'posizione = ', count

          scaleMd = pdfHisto.GetMean()
          scaleUp = scaleMd + pdfHisto.GetRMS()
          scaleDn = scaleMd - pdfHisto.GetRMS()

          pdfUp[0] = scaleUp / scaleMd
          pdfDn[0] = scaleDn / scaleMd
          pdfMd[0] = scaleMd

          if (i > 0 and i%step == 0.) :
              print i,'events processed ::', nentries, 'Scale Dn:', pdfDn[0], 'Scale Md:', pdfMd[0], 'Scale Up:', pdfUp[0]
              
          self.otree.Fill()
          savedentries+=1
          
        self.disconnect()
        print ' - Event loop completed'
        print ' - Saved entries:', savedentries
