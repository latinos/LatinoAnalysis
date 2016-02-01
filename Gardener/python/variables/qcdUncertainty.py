
#   ____   _____ _____                              _        _       _         
#  / __ \ / ____|  __ \                            | |      (_)     | |        
# | |  | | |    | |  | |  _   _ _ __   ___ ___ _ __| |_ __ _ _ _ __ | |_ _   _ 
# | |  | | |    | |  | | | | | | '_ \ / __/ _ \ '__| __/ _` | | '_ \| __| | | |
# | |__| | |____| |__| | | |_| | | | | (_|  __/ |  | || (_| | | | | | |_| |_| |
#  \___\_\\_____|_____/   \__,_|_| |_|\___\___|_|   \__\__,_|_|_| |_|\__|\__, |
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

class QcdUncertaintyTreeMaker(TreeCloner) :
    def __init__(self) :
       pass

    def help(self) :
        return '''QCD uncertainty'''

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
        self.qcdVariables = [ 'qcdScaleUp', 'qcdScaleDn', 'qcdScaleMd' ]
        
        # Clone the tree with new branches added
        self.clone(output, self.qcdVariables)
      
        # Now actually connect the branches
        qcdUp = numpy.ones(1, dtype=numpy.float32)
        qcdDn = numpy.ones(1, dtype=numpy.float32)
        qcdMd = numpy.ones(1, dtype=numpy.float32)

        self.otree.Branch('qcdScaleUp',    qcdUp, 'qcdScaleUp/F')
        self.otree.Branch('qcdScaleDn',    qcdDn, 'qcdScaleDn/F')
        self.otree.Branch('qcdScaleMd',    qcdMd, 'qcdScaleMd/F')

        # Input tree  
        itree = self.itree

        # Weights Histo
        weightsHisto = self.itreeMcWeightExplainedOrdered
        histoEntries = weightsHisto.GetEntries()
        loopStart = 0
        muRmuFmd  = 0
        muRmuFup  = 0
        muRmuFdn  = 0
        countEntries = range (1, int(histoEntries))

        for contHisto in countEntries:
            label = ROOT.TString(weightsHisto.GetXaxis().GetBinLabel(loopStart))
            if (label.Contains("muR=1 muF=1")):
                muRmuFmd = contHisto
            if (label.Contains("muR=2 muF=2")):
                muRmuFup = contHisto
            if (label.Contains("muR=0.5 muF=0.5")):
                muRmuFdn = contHisto
            if (muRmuFup != 0 and muRmuFdn != 0):
                break

        # Labels start from Bin 1, vector starts from bin 0
        muRmuFmd = muRmuFmd -1
        muRmuFup = muRmuFup -1
        muRmuFdn = muRmuFdn -1

        # pdfHisto
        pdfHisto = ROOT.TH1F("qcdHisto", "qcdHisto", 200, 0., 10.)

        #-----------------------------------------------------------------------
        print ' - Starting event loop'
        step = 5000

        for i in xrange(nentries) :
          itree.GetEntry(i)

          scaleMd = itree.std_vector_LHE_weight[muRmuFmd];
          scaleUp = itree.std_vector_LHE_weight[muRmuFup] / scaleMd;
          scaleDn = itree.std_vector_LHE_weight[muRmuFdn] / scaleMd;

          qcdMd[0] = scaleMd
          qcdUp[0] = scaleUp
          qcdDn[0] = scaleDn

          if (i > 0 and i%step == 0.) :
              print i,'events processed ::', nentries, 'scaleDn:', qcdDn[0], 'scaleMd:', qcdMd[0], 'scaleUp:', qcdUp[0], 
              
          self.otree.Fill()
          savedentries+=1
          
        self.disconnect()
        print ' - Event loop completed'
        print ' - Saved entries:', savedentries
