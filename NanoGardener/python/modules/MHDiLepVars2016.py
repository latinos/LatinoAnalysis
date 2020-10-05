import ROOT

from PhysicsTools.NanoAODTools.postprocessing.framework.datamodel import Collection 
from PhysicsTools.NanoAODTools.postprocessing.framework.eventloop import Module

class MHDiLepVars2016(Module):
    def __init__(self):

        self.bVetoCut = 0.2217
        self.metpt = 'event.MET_pt'
        self.metsig = 'event.MET_significance'
        self.lep1pt = 'event.Lepton_pt[0]'
        self.lep2pt = 'event.Lepton_pt[1]'

    def beginJob(self):
        pass
    def endJob(self):
        pass
    def beginFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        
        self.inputFile = inputFile

        self.out = wrappedOutputTree                
        self.out.branch('nbtaggedJets','I')
        self.out.branch('metpt','F')
        self.out.branch('metsig','F')
        self.out.branch('lep1pt','F')
        self.out.branch('lep2pt','F')
        self.out.branch('specialMCWeigths','F')

    def endFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        pass
    
    def analyze(self, event):
        """process event, return True (go to next module) or False (fail, go to next event)"""
        
        Jets = Collection(event, 'Jet')
        CleanJets = Collection(event, 'CleanJet')
        nCleanJets = CleanJets._len
        nbtagged = 0

        for iJet in range(nCleanJets):
            if (CleanJets[iJet].pt > 20. and ROOT.TMath.Abs(CleanJets[iJet].eta) < 2.5 and Jets[CleanJets[iJet].jetIdx].btagDeepB > self.bVetoCut):
                nbtagged += 1
            else:
                continue
                
        if 'TTTo2L2Nu' in str(self.inputFile):
            MCweight = (event.topGenPt * event.antitopGenPt > 0.) * (ROOT.TMath.Sqrt(ROOT.TMath.Exp(-0.158631 + 2.00214e-04*event.topGenPt - 3.09496e-07*event.topGenPt*event.topGenPt + 34.93/(event.topGenPt+135.633)) * ROOT.TMath.Exp(-0.158631 + 2.00214e-04*event.antitopGenPt - 3.09496e-07*event.antitopGenPt*event.antitopGenPt + 34.93/(event.antitopGenPt+135.633)))) + (event.topGenPt * event.antitopGenPt <= 0.)
        elif '_WWTo2L2Nu_' in str(self.inputFile):
            MCweight = event.nllW
        elif '_M-50' in str(self.inputFile): #DY high mass
            MCweight = (0.876979+event.gen_ptll*(4.11598e-03)-(2.35520e-05)*event.gen_ptll*event.gen_ptll)*(1.10211 * (0.958512 - 0.131835*ROOT.TMath.Erf((event.gen_ptll-14.1972)/10.1525)))*(event.gen_ptll<140)+0.891188*(event.gen_ptll>=140)
        elif '_M-10to50' in str(self.inputFile): #DY low mass
            MCweight = (8.61313e-01+event.gen_ptll*4.46807e-03-1.52324e-05*event.gen_ptll*event.gen_ptll)*(1.08683 * (0.95 - 0.0657370*ROOT.TMath.Erf((event.gen_ptll-11.)/5.51582)))*(event.gen_ptll<140)+1.141996*(event.gen_ptll>=140)
        elif '50_HT' in str(self.inputFile): #DY low mass
            MCweight = (8.61313e-01+event.gen_ptll*4.46807e-03-1.52324e-05*event.gen_ptll*event.gen_ptll)*(1.08683 * (0.95 - 0.0657370*ROOT.TMath.Erf((event.gen_ptll-11.)/5.51582)))*(event.gen_ptll<140)+1.141996*(event.gen_ptll>=140)
        elif (('GluGluWWTo2' in str(self.inputFile)) or ('GluGluToWW' in str(self.inputFile))):
            MCweight = 1.53/1.4
        elif (('ZZTo2L2Nu' in str(self.inputFile)) or ('ZZTo2L2Q' in str(self.inputFile)) or ('ZZTo4L' in str(self.inputFile)) or ('WZTo2L2Q' in str(self.inputFile))):
            MCweight = 1.11
        else:
            MCweight = 1.0

        self.out.fillBranch('nbtaggedJets',nbtagged)
        self.out.fillBranch('metpt',eval(self.metpt))
        self.out.fillBranch('metsig',eval(self.metsig))
        self.out.fillBranch('lep1pt',eval(self.lep1pt))
        self.out.fillBranch('lep2pt',eval(self.lep2pt))
        self.out.fillBranch('specialMCWeigths',MCweight)

        return True


