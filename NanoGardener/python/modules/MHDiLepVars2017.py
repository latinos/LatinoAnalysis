import ROOT

from PhysicsTools.NanoAODTools.postprocessing.framework.datamodel import Collection 
from PhysicsTools.NanoAODTools.postprocessing.framework.eventloop import Module

class MHDiLepVars2017(Module):
    def __init__(self):

        self.bVetoCut = 0.1522
        self.metpt = 'event.METFixEE2017_pt'
        self.metsig = 'event.METFixEE2017_significance'
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
            MCweight = (event.topGenPt * event.antitopGenPt > 0.) * (ROOT.TMath.Sqrt(ROOT.TMath.Exp(-1.43717e-02 - 1.18358e-04*event.topGenPt - 1.70651e-07*event.topGenPt*event.topGenPt + 4.47969/(event.topGenPt+28.7)) * ROOT.TMath.Exp(-1.43717e-02 - 1.18358e-04*event.antitopGenPt - 1.70651e-07*event.antitopGenPt*event.antitopGenPt + 4.47969/(event.antitopGenPt+28.7)))) + (event.topGenPt * event.antitopGenPt <= 0.)
        elif '_WWTo2L2Nu_' in str(self.inputFile):
            MCweight = event.nllW
        elif 'DYJetsToLL_M-50' in str(self.inputFile):
            MCweight = (((0.623108 + 0.0722934*event.gen_ptll - 0.00364918*event.gen_ptll*event.gen_ptll + 6.97227e-05*event.gen_ptll*event.gen_ptll*event.gen_ptll - 4.52903e-07*event.gen_ptll*event.gen_ptll*event.gen_ptll*event.gen_ptll)*(event.gen_ptll<45)*(event.gen_ptll>0) + 1*(event.gen_ptll>=45))*(ROOT.TMath.Abs(event.gen_mll-90)<3) + (ROOT.TMath.Abs(event.gen_mll-90)>3))
        elif 'DYJetsToLL_M-10to50-LO' in str(self.inputFile):
            MCweight = ((0.632927+0.0456956*event.gen_ptll-0.00154485*event.gen_ptll*event.gen_ptll+2.64397e-05*event.gen_ptll*event.gen_ptll*event.gen_ptll-2.19374e-07*event.gen_ptll*event.gen_ptll*event.gen_ptll*event.gen_ptll+6.99751e-10*event.gen_ptll*event.gen_ptll*event.gen_ptll*event.gen_ptll*event.gen_ptll)*(event.gen_ptll>0)*(event.gen_ptll<100)+(1.41713-0.00165342*event.gen_ptll)*(event.gen_ptll>=100)*(event.gen_ptll<300)+1*(event.gen_ptll>=300))
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


