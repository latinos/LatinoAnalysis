import ROOT
import math
import os
import subprocess
from array import array
ROOT.PyConfig.IgnoreCommandLineOptions = True

from PhysicsTools.NanoAODTools.postprocessing.framework.datamodel import Collection 
from PhysicsTools.NanoAODTools.postprocessing.framework.eventloop import Module

from LatinoAnalysis.NanoGardener.data.SusyISRCorrections import SUSYISRCorrections

class SusyWeightsProducer(Module):

    ###
    def __init__(self, cmssw, sourcedir):
        self.cmssw = cmssw
        self.sourcedir = sourcedir[:sourcedir.index('susyGen')] + 'susyGen'
        pass

    ###
    def beginJob(self):
        pass

    ###
    def endJob(self):
        pass

    ###
    def beginFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        self.out = wrappedOutputTree
        self.out.branch("baseW",         "F")
        self.out.branch("isrW",          "F")
            
        chain = ROOT.TChain('Events')

        inputFileName = inputFile.GetName()
              
        if '__part' in inputFileName :
            inputFileName = inputFileName[:inputFileName.index('__part')] + '__part*.root'
            nInputTrees = int(subprocess.check_output('ls ' + self.sourcedir + '/' + inputFileName + ' | grep -c root', shell=True).strip('\n'))
            for part in range(nInputTrees):
                partFileName = self.sourcedir + '/' + inputFileName.replace('__part*.root', '__part' + str(part) + '.root')
                if os.path.isfile(partFileName) :
                    chain.Add(partFileName)
                else:
                    raise Exception('SusyWeightsProducer ERROR: input susyGen file', partFileName, 'does not exist')

        else:
            chain.Add(self.sourcedir + '/' + inputFileName)
            nInputTrees = 1

        print 'SusyWeightsProducer: read', nInputTrees, 'input susyGen files with', chain.GetEntries(), 'events'

        self.massPointN = { }

        inputTree.SetEstimate(inputTree.GetEntries())
        inputTree.Draw('susyIDprompt')
        idPromptArray = inputTree.GetV1()
        idPromptList = [ ] 
        for i in range(inputTree.GetSelectedRows()):
            if int(idPromptArray[i]) not in idPromptList:
                idPromptList.append(int(idPromptArray[i]))

        for idPrompt in idPromptList:
                
            self.massPointN[idPrompt] = { }

            self.isrObservable = ''

            for process in SUSYISRCorrections:
                if str(idPrompt) in SUSYISRCorrections[process]['susyPromptParticles']:
                    for isrVer in SUSYISRCorrections[process]['version']:
                        if self.cmssw in SUSYISRCorrections[process]['version'][isrVer]['production']:

                            self.isrObservable = SUSYISRCorrections[process]['version'][isrVer]['observable']
                        
                            self.isrEdge = []
                            self.isrCorrection = []

                            for edge in sorted(SUSYISRCorrections[process]['version'][isrVer]['correction'].keys()) :
                                    
                                self.isrEdge.append( float(edge) )
                                self.isrCorrection.append( float(SUSYISRCorrections[process]['version'][isrVer]['correction'][edge]) )

                            self.isrBins = len(self.isrEdge) - 1

            if self.isrObservable=='' :
                raise Exception('SusyWeightsProducer ERROR: SUSY model not found for', inputFile.GetName())

                
            massScan = ROOT.TH2D("massScan", "", 3000, 0., 3000., 3000, 0., 3000.)
            inputTree.Project(massScan.GetName(), "susyMLSP:susyMprompt", "susyIDprompt=="+str(idPrompt), "")
            
            for xb in range(1, massScan.GetNbinsX()+1) :
                for yb in range(1, massScan.GetNbinsY()+1) :
                    if massScan.GetBinContent(xb, yb)>0. :

                        histoISR = ROOT.TH1D("histoISR", "", self.isrBins, array('d',self.isrEdge))
                        chain.Project(histoISR.GetName(), self.isrObservable, "(susyMprompt=="+str(xb-1)+" && susyMLSP=="+str(yb-1)+" && susyIDprompt=="+str(idPrompt)+")*genWeight", "")

                        reweightedNormalization = 0.
                        for ib in range(self.isrBins+1) :
                            reweightedNormalization += histoISR.GetBinContent(ib+1)*self.isrCorrection[ib]

                        normFactor = histoISR.Integral(0, self.isrBins+1)/reweightedNormalization

                        self.massPointN[idPrompt][str(xb-1)+"-"+str(yb-1)] = {}
                        self.massPointN[idPrompt][str(xb-1)+"-"+str(yb-1)]['events'] = histoISR.GetEntries()
                        self.massPointN[idPrompt][str(xb-1)+"-"+str(yb-1)]['isrW'] = normFactor
                        print 'SusyWeightsProducer: overall ISR normalization factor for mass point (',str(idPrompt),',',str(xb-1),',',str(yb-1),'):', normFactor
                        
    ###    
    def endFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        pass

    ###
    def analyze(self, event):
        """process event, return True (go to next module) or False (fail, go to next event)"""

        Xsec  = event.Xsec
        nevents = self.massPointN[int(event.susyIDprompt)][str(int(event.susyMprompt))+"-"+str(int(event.susyMLSP))]['events']
         
        baseW = 1000.*Xsec/nevents

        isrW = self.massPointN[int(event.susyIDprompt)][str(int(event.susyMprompt))+"-"+str(int(event.susyMLSP))]['isrW']
        for ib in reversed(xrange(self.isrBins+1)) :
            if getattr(event, self.isrObservable) >= self.isrEdge[ib] :
                isrW *= self.isrCorrection[ib]
                break

        self.out.fillBranch("baseW",   baseW)
        self.out.fillBranch("isrW",    isrW)      
            
        return True
 
