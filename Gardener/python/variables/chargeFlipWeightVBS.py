import optparse
import numpy
import ROOT
import os.path
import math

from LatinoAnalysis.Gardener.gardening import TreeCloner

class chargeFlipWeightVBS(TreeCloner):

    def __init__(self):
        pass

    def __del__(self):
        pass

    def help(self):
        return '''Add lepton ee-0S to ee-SS charge flip probality taken form data.'''

    def addOptions(self,parser):
        description = self.help()
        group = optparse.OptionGroup(parser,self.label, description)
        return group

    def checkOptions(self,opts):
        pass

    def _getHistoValue(self,eta):
        eta_V = eta
        if abs(eta_V)>2.5 : eta_V=2.5
        if 0< abs(eta_V)  <= 0.5  : value=3.8*10.**(-5.)/(1.+3.8*10.**(-5.))
        if 0.5< abs(eta_V) <= 1.0 : value=1.0*10.**(-4.)/(1.+1.0*10.**(-4.))
        if 1.0< abs(eta_V) <= 1.5 : value=5.7*10.**(-4.)/(1.+5.7*10.**(-4.))
        if 1.5< abs(eta_V) <= 2.0 : value=2.4*10.**(-3.)/(1.+2.4*10.**(-3.))
        if 2.0< abs(eta_V) <= 2.5 : value=2.4*10.**(-3.)/(1.+2.4*10.**(-3.))
        return value
    

    def process(self,**kwargs):

        tree  = kwargs['tree']
        input = kwargs['input']
        output = kwargs['output']

        self.connect(tree,input)

        newbranches = ['chFlipProbaVBS']
        self.clone(output,newbranches)
        chFlipProbaVBS      = numpy.ones(1, dtype=numpy.float32)
        self.otree.Branch('chFlipProbaVBS',  chFlipProbaVBS,  'chFlipProbaVBS/F')

        nentries = self.itree.GetEntries()
        print 'Total number of entries: ',nentries 

        # avoid dots to go faster
        itree     = self.itree
        otree     = self.otree

        print '- Starting eventloop'
        step = 5000
        for i in xrange(nentries):
            itree.GetEntry(i)
            chFlipProbaVBS[0] = 0.

            # just because it is easier to write later ...
            pt1   = itree.std_vector_lepton_pt[0]
            pt2   = itree.std_vector_lepton_pt[1]
            eta1  = itree.std_vector_lepton_eta[0]
            eta2  = itree.std_vector_lepton_eta[1]
            flav1 = itree.std_vector_lepton_flavour[0]
            flav2 = itree.std_vector_lepton_flavour[1]
 
            if pt1>0 and pt2>0 and (flav1*flav2) == (-11.*11) : chFlipProbaVBS[0] = self._getHistoValue(eta1)*(1-self._getHistoValue(eta2))+self._getHistoValue(eta2)*(1-self._getHistoValue(eta1))

            if pt1>0 and pt2>0 and (flav1*flav2) == (-11.*13) :
                   if   abs(flav1)==11 : chFlipProbaVBS[0] = self._getHistoValue(eta1)
                   elif abs(flav2)==11 : chFlipProbaVBS[0] = self._getHistoValue(eta2)

            if pt1>0 and pt2>0 and (flav1*flav2) > 0 : chFlipProbaVBS[0] = 0
            if pt1>0 and pt2>0 and abs(flav1*flav2) == (13*13) : chFlipProbaVBS[0] = 0
               

            otree.Fill()
  
            
        self.disconnect()
        print '- Eventloop completed'

