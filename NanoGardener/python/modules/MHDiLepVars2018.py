import ROOT

from PhysicsTools.NanoAODTools.postprocessing.framework.datamodel import Collection 
from PhysicsTools.NanoAODTools.postprocessing.framework.eventloop import Module

class MHDiLepVars2018(Module):
    def __init__(self):

        self.bVetoCut = 0.1241
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
        self.out.branch('PrefireWeight','F')

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
            MCweight = (ROOT.TMath.Sqrt(ROOT.TMath.Exp(-1.43717e-02 - 1.18358e-04*event.topGenPt - 1.70651e-07*event.topGenPt*event.topGenPt + 4.47969/(event.topGenPt+28.7)) * ROOT.TMath.Exp(-1.43717e-02 - 1.18358e-04*event.antitopGenPt - 1.70651e-07*event.antitopGenPt*event.antitopGenPt + 4.47969/(event.antitopGenPt+28.7))))
        elif '_WWTo2L2Nu_' in str(self.inputFile):
            MCweight = event.nllW
        elif '_M-50' in str(self.inputFile): #DY high mass
            MCweight = (0.87*(event.gen_ptll<10)+(0.379119+0.099744*event.gen_ptll-0.00487351*event.gen_ptll*event.gen_ptll+9.19509e-05*event.gen_ptll*event.gen_ptll*event.gen_ptll-6.0212e-07*event.gen_ptll*event.gen_ptll*event.gen_ptll*event.gen_ptll)*(event.gen_ptll>=10 and event.gen_ptll<45)+(9.12137e-01+1.11957e-04*event.gen_ptll-3.15325e-06*event.gen_ptll*event.gen_ptll-4.29708e-09*event.gen_ptll*event.gen_ptll*event.gen_ptll+3.35791e-11*event.gen_ptll*event.gen_ptll*event.gen_ptll*event.gen_ptll)*(event.gen_ptll>=45 and event.gen_ptll<200) + 1*(event.gen_ptll>200))
        elif '_M-10to50-LO' in str(self.inputFile): # DY low mass
            MCweight = ((0.632927+0.0456956*event.gen_ptll-0.00154485*event.gen_ptll*event.gen_ptll+2.64397e-05*event.gen_ptll*event.gen_ptll*event.gen_ptll-2.19374e-07*event.gen_ptll*event.gen_ptll*event.gen_ptll*event.gen_ptll+6.99751e-10*event.gen_ptll*event.gen_ptll*event.gen_ptll*event.gen_ptll*event.gen_ptll)*(event.gen_ptll>0)*(event.gen_ptll<100)+(1.41713-0.00165342*event.gen_ptll)*(event.gen_ptll>=100)*(event.gen_ptll<300)+1*(event.gen_ptll>=300))
        elif '50_HT' in str(self.inputFile): # DY HT binned samples
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
        self.out.fillBranch('PrefireWeight',1.0)

        return True


