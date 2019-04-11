import ROOT
import math, os,re
import numpy as np
ROOT.PyConfig.IgnoreCommandLineOptions = True

from PhysicsTools.NanoAODTools.postprocessing.framework.datamodel import Collection, Object
from PhysicsTools.NanoAODTools.postprocessing.framework.eventloop import Module
from PhysicsTools.NanoAODTools.postprocessing.tools import matchObjectCollection, matchObjectCollectionMultiple
from PhysicsTools.NanoAODTools.postprocessing.modules.jme.JetReCalibrator import JetReCalibrator

class jetRecalib(Module):
    # Module based on https://github.com/cms-nanoAOD/nanoAOD-tools/blob/master/python/postprocessing/modules/jme/jetRecalib.py
    def __init__(self,  globalTag, jetCollections = ["CleanJet"], metCollections = ["MET"], jetType = "AK4PFchs"):

        if "AK4" in jetType : 
            self.jetBranchName = "Jet"
        elif "AK8" in jetType :
            self.jetBranchName = "FatJet"
            self.subJetBranchName = "SubJet"
        else:
            raise ValueError("ERROR: Invalid jet type = '%s'!" % jetType)
        self.otherJetBranches = jetCollections # Any jet collections based on full Jet-collection
        self.metCollections = metCollections
        self.rhoBranchName = "fixedGridRhoFastjetAll"
        # To do : change to real values
        self.jmsVals = [1.00, 0.99, 1.01]
        

        self.jesInputFilePath = os.environ['CMSSW_BASE'] + "/src/PhysicsTools/NanoAODTools/data/jme/"

        self.jetReCalibrator = JetReCalibrator(globalTag, jetType , True, self.jesInputFilePath, calculateSeparateCorrections = False, calculateType1METCorrection  = False)
	
        # load libraries for accessing JES scale factors and uncertainties from txt files
        for library in [ "libCondFormatsJetMETObjects", "libPhysicsToolsNanoAODTools" ]:
            if library not in ROOT.gSystem.GetLibraries():
                print("Load Library '%s'" % library.replace("lib", ""))
                ROOT.gSystem.Load(library)

    def beginJob(self):
	pass

    def endJob(self):
	pass

    def beginFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        self.out = wrappedOutputTree
        self.out.branch("%s_pt" % self.jetBranchName, "F", lenVar="n"+self.jetBranchName)
        self.out.branch("%s_rawFactor" % self.jetBranchName, "F", lenVar="n"+self.jetBranchName)
        for jname in self.otherJetBranches:
            self.out.branch("%s_pt" % jname, "F", lenVar="n"+jname)
        for met in self.metCollections:
            self.out.branch("%s_pt" % met, "F")
            self.out.branch("%s_phi" % met, "F")
            
                        
    def endFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        pass
    
    def analyze(self, event):
        """process event, return True (go to next module) or False (fail, go to next event)"""
        jets = Collection(event, self.jetBranchName )
        mets = []
        met_px = []
        met_py = []
        for mid,met in enumerate(self.metCollections):
            mets.append(Object(event, met))
            met_px.append(mets[mid].pt*math.cos(mets[mid].phi))
            met_py.append(mets[mid].pt*math.sin(mets[mid].phi))

        jets_pt_newlist = []
        rawFactor_newlist = []

        otherjets = []
        otherjets_pt_newlist = []
        for jname in self.otherJetBranches:
            otherjets.append(Collection(event, jname ))
            otherjets_pt_newlist.append([])
        
        rho = getattr(event, self.rhoBranchName)
        
        for jid,jet in enumerate(jets):
            # Apply new correction (this includes undoing previous correction first)
	    newjet_pt = self.jetReCalibrator.correct(jet,rho)
            # Rewrite new correction factor
            rawFactor_newlist.append(1. - ((jet.pt * (1. - jet.rawFactor))/newjet_pt))

            if newjet_pt < 0.0: newjet_pt *= -1.0
            jets_pt_newlist.append(newjet_pt)

            if newjet_pt > 15.:
                jet_cosPhi = math.cos(jet.phi)
                jet_sinPhi = math.sin(jet.phi)
                for mid,met in enumerate(self.metCollections):
                    met_px[mid] = met_px[mid] - (newjet_pt - jet.pt)*jet_cosPhi
                    met_py[mid] = met_py[mid] - (newjet_pt - jet.pt)*jet_sinPhi

            for oj,jname in enumerate(self.otherJetBranches):
                for ojet in otherjets[oj]:
                    if jid == ojet.jetIdx:
                        otherjets_pt_newlist[oj].append(newjet_pt)

        self.out.fillBranch("%s_pt" % self.jetBranchName, jets_pt_newlist)
        self.out.fillBranch("%s_rawFactor" % self.jetBranchName, rawFactor_newlist)
        for oj,jname in enumerate(self.otherJetBranches):
            self.out.fillBranch("%s_pt" % jname, otherjets_pt_newlist[oj])
        for mid,met in enumerate(self.metCollections):
            self.out.fillBranch("%s_pt" % met, math.sqrt(met_px[mid]**2 + met_py[mid]**2))
            self.out.fillBranch("%s_phi" % met, math.atan2(met_py[mid], met_px[mid]))   

        return True


# define modules using the syntax 'name = lambda : constructor' to avoid having them loaded when not needed

jetRecalib2017B = lambda : jetRecalib("Fall17_17Nov2017B_V32_DATA", jetCollections=["CleanJet"], metCollections=["MET"])
jetRecalib2017C = lambda : jetRecalib("Fall17_17Nov2017C_V32_DATA", jetCollections=["CleanJet"], metCollections=["MET"])
jetRecalib2017D = lambda : jetRecalib("Fall17_17Nov2017DE_V32_DATA", jetCollections=["CleanJet"], metCollections=["MET"])
jetRecalib2017E = lambda : jetRecalib("Fall17_17Nov2017DE_V32_DATA", jetCollections=["CleanJet"], metCollections=["MET"])
jetRecalib2017F = lambda : jetRecalib("Fall17_17Nov2017F_V32_DATA", jetCollections=["CleanJet"], metCollections=["MET"])
