import optparse
import numpy
import ROOT
import os.path
import math

from LatinoAnalysis.Gardener.gardening import TreeCloner

class chargeFlipWeight(TreeCloner):

    def __init__(self):
        pass

    def __del__(self):
        pass

    def help(self):
        return '''Add lepton ee-0S to ee-SS charge flip probality taken form data.'''

    def addOptions(self,parser):
        description = self.help()
        group = optparse.OptionGroup(parser,self.label, description)
        group.add_option('-j', '--njets',  dest='njets',  help='Minimum number of jets',  default='0')
        parser.add_option_group(group)
        return group


    def checkOptions(self,opts):

	self.njets = opts.njets	
        cmssw_base = os.getenv('CMSSW_BASE')
        if self.njets == 0:
            self.chFlipEeFileName = cmssw_base+'/src/LatinoAnalysis/Gardener/python/data/chFlip/DY_SSoverOS_2Dweight_inclusive.root'
            self.chFlipEeHistName = 'DY_leptoneta2D_weight'
        else:
            self.chFlipEeFileName = cmssw_base+'/src/LatinoAnalysis/Gardener/python/data/chFlip/DY_SSoverOS_2Dweight_2jet_MCsubtr_Feb2017.root'
            self.chFlipEeHistName = 'data_leptonabseta2D_weight' 

        self.chFlipEeFile = self._openRootFile(self.chFlipEeFileName)
        self.chFlipEeHist = self._getRootObj(self.chFlipEeFile,self.chFlipEeHistName) 

        self.minpt_ele = 10
        self.maxpt_ele = 200
        self.mineta_ele = -2.4
        self.maxeta_ele = 2.4

    def _getHistoValue(self, h2, eta1, eta2):
        eta1_V = eta1
        eta2_V = eta2
        if eta1 < self.mineta_ele : eta1_V = -2.399
        if eta2 < self.mineta_ele : eta2_V = -2.399
        if eta1 > self.maxeta_ele : eta1_V =  2.399 
        if eta2 > self.maxeta_ele : eta2_V =  2.399 
        value = h2.GetBinContent(h2.FindBin(eta1_V, eta2_V))
        return value

    def process(self,**kwargs):

        tree  = kwargs['tree']
        input = kwargs['input']
        output = kwargs['output']

        self.connect(tree,input)

        newbranches = ['chFlipProba']
        self.clone(output,newbranches)
        chFlipProba      = numpy.ones(1, dtype=numpy.float32)
        self.otree.Branch('chFlipProba',  chFlipProba,  'chFlipProba/F')

        nentries = self.itree.GetEntries()
        print 'Total number of entries: ',nentries 

        # avoid dots to go faster
        itree     = self.itree
        otree     = self.otree

        print '- Starting eventloop'
        step = 5000
        for i in xrange(nentries):
            itree.GetEntry(i)
            chFlipProba[0] = 1.

            # just because it is easier to write later ...
            pt1   = itree.std_vector_lepton_pt[0]
            pt2   = itree.std_vector_lepton_pt[1]
            eta1  = itree.std_vector_lepton_eta[0]
            eta2  = itree.std_vector_lepton_eta[1]
            flav1 = itree.std_vector_lepton_flavour[0]
            flav2 = itree.std_vector_lepton_flavour[1]
 
            if self.njets > 0:
                eta1 = abs(eta1)
                eta2 = abs(eta2)

            if pt1>0 and pt2>0 and (flav1*flav2) == (-11.*11) : chFlipProba[0] = self._getHistoValue(self.chFlipEeHist,eta1,eta2)
               

            otree.Fill()
  
            
        self.disconnect()
        print '- Eventloop completed'

