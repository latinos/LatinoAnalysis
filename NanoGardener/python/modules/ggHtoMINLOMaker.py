#    See https://twiki.cern.ch/twiki/bin/viewauth/CMS/HiggsWG/SignalModelingTools

import os
import ROOT
ROOT.PyConfig.IgnoreCommandLineOptions = True

from PhysicsTools.NanoAODTools.postprocessing.framework.datamodel import Collection 
from PhysicsTools.NanoAODTools.postprocessing.framework.eventloop import Module

class ggHtoMINLOMaker(Module):

    def _openRootFile(self,path, option=''):
        f =  ROOT.TFile.Open(path,option)
        if not f.__nonzero__() or not f.IsOpen():
            raise NameError('File '+path+' not open')
        return f

    def _getRootObj(self,d,name):
        o = d.Get(name)
        if not o.__nonzero__():
            print 'Object '+name+' doesn\'t exist in '+d.GetName(), ' BE CAREFUL!'
        return o

    def __init__(self, generator):
        self.generator = generator

        cmssw_base = os.getenv('CMSSW_BASE')
        
        nameFileWithWeights = cmssw_base+'/src/LatinoAnalysis/Gardener/python/data/powheg2minlo/NNLOPS_reweight.root'
        self.fileWithWeights = self._openRootFile(nameFileWithWeights)  

        if self.generator == 'powheg':
            self.graph_weights_0jet = self._getRootObj(self.fileWithWeights, 'gr_NNLOPSratio_pt_powheg_0jet')
            self.graph_weights_1jet = self._getRootObj(self.fileWithWeights, 'gr_NNLOPSratio_pt_powheg_1jet')
            self.graph_weights_2jet = self._getRootObj(self.fileWithWeights, 'gr_NNLOPSratio_pt_powheg_2jet')
            self.graph_weights_3jet = self._getRootObj(self.fileWithWeights, 'gr_NNLOPSratio_pt_powheg_3jet')
        elif self.generator == 'mcatnlo':
            self.graph_weights_0jet = self._getRootObj(self.fileWithWeights, 'gr_NNLOPSratio_pt_mcatnlo_0jet')
            self.graph_weights_1jet = self._getRootObj(self.fileWithWeights, 'gr_NNLOPSratio_pt_mcatnlo_1jet')
            self.graph_weights_2jet = self._getRootObj(self.fileWithWeights, 'gr_NNLOPSratio_pt_mcatnlo_2jet')
            self.graph_weights_3jet = self._getRootObj(self.fileWithWeights, 'gr_NNLOPSratio_pt_mcatnlo_3jet')
        else :
            print "Please enter a valid generator name: powheg or mcatnlo"

    def beginJob(self):
        pass
    def endJob(self):
        pass

    def beginFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        self.out = wrappedOutputTree
        self.out.branch("weight2MINLO", "F")

    def endFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        pass

    def analyze(self, event):
        """ggH reweight to MINLO"""

        HTXS_Higgs_pt = getattr(event, "HTXS_Higgs_pt")
        HTXS_njets30  = getattr(event, "HTXS_njets30")

        graph_weights_0jet = self.graph_weights_0jet
        graph_weights_1jet = self.graph_weights_1jet
        graph_weights_2jet = self.graph_weights_2jet
        graph_weights_3jet = self.graph_weights_3jet

        weight2MINLO = 1.
          
        Njets30_HTXS = HTXS_njets30
          
        if (Njets30_HTXS==0):
            weight2MINLO = graph_weights_0jet.Eval( min(HTXS_Higgs_pt,125.0) )
        elif (Njets30_HTXS==1):
            weight2MINLO = graph_weights_1jet.Eval( min(HTXS_Higgs_pt,625.0) )
        elif (Njets30_HTXS==2):
            weight2MINLO = graph_weights_2jet.Eval( min(HTXS_Higgs_pt,800.0) )
        elif (Njets30_HTXS>=3):
            weight2MINLO = graph_weights_3jet.Eval( min(HTXS_Higgs_pt,925.0) )
        else:
            weight2MINLO = 1.0

        #print " Njets30_HTXS = " , Njets30_HTXS , " --> weight2MINLO = ", weight2MINLO
       
        self.out.fillBranch("weight2MINLO", weight2MINLO)
        return True

