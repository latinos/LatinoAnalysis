import ROOT
ROOT.PyConfig.IgnoreCommandLineOptions = True
import re
from math import sqrt

from PhysicsTools.NanoAODTools.postprocessing.framework.datamodel import Collection 
from PhysicsTools.NanoAODTools.postprocessing.framework.eventloop import Module
from LatinoAnalysis.NanoGardener.data.FatJetMaker_cfg import CleanFatJet_br, CleanFatJet_var
from LatinoAnalysis.NanoGardener.data.FatJetMaker_cfg import fatjet_mass_scale_sf as JMS_sf
from LatinoAnalysis.NanoGardener.data.FatJetMaker_cfg import fatjet_mass_resolution_sf as JMR_sf
from LatinoAnalysis.NanoGardener.data.FatJetMaker_cfg import fatjet_mass_resolution_MC as JMR_MC

class FatJetMassScaler(Module):
    '''
    This module is used to vary both the scale and the resolution on the FatJet mass. 
    It can be used both for nominal scale/smear and for variations
    type=scale apply the scale
    type=smear apply the resoluton
    type=scale_smear both apply scale and resolution
    kind=Central/Up/Down
    '''
    def __init__(self,year, type,  kind, collection="CleanFatJet"):
        self.year = year
        self.collection = collection
        self.type = type
        self.kind = kind
         # initialize random number generator
        self.rnd = ROOT.TRandom3(12345)

        if self.year not in JMS_sf or self.year not in JMR_sf:
            print("ERROR! No JMS/JMR sf for year ", year)

    def beginJob(self):
        pass
    def endJob(self):
        pass

    def beginFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        self.out = wrappedOutputTree
        # Smearing factor saved for variations
        self.out.branch(self.collection+'_smearfactor', "F", lenVar="n"+self.collection)
        # Mass
        self.out.branch(self.collection+"_mass", "F", lenVar="n"+self.collection)

    def endFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        pass
    
    def analyze(self, event):
        fatjets = Collection(event, self.collection)
        masses = []
        smearfactors = []

        # if len(fatjets)>0 and self.kind != "Central":  
        #     print "previous smear:  ", [ f.smearfactor for f in fatjets]
        #     print "previous mass: ",[f.mass for f in fatjets]

        for fatjet in fatjets:
            if self.kind == "Central":
                # Nominal scale/smearing
                scaled_mass = self.scaleFatJetMass(fatjet.mass, "Central")
                smeared_mass, smearfactor = self.smearFatJetMass(scaled_mass, 1, "Central")
                masses.append(scaled_mass)
                smearfactors.append(smearfactor)
            else:
                # Variations
                if self.type == "scale":
                    masses.append(self.scaleFatJetMass(fatjet.mass, self.kind))
                elif self.type == "smear":
                    new_mass, smearfactor = self.smearFatJetMass(fatjet.mass, fatjet.smearfactor, self.kind)
                    masses.append(new_mass)
                    smearfactors.append(smearfactor)

        # save output
        self.out.fillBranch(self.collection+"_mass", masses)

        if self.kind == "Central" or self.type == "smear":
            self.out.fillBranch(self.collection+"_smearfactor", smearfactors)

        return True

        

    # Scale and smear fatjet mass nominal
    def scaleFatJetMass(self, mass, kind):
        scale_nominal = JMS_sf[self.year][0]
        if kind == "Central": 
            new_mass = mass * scale_nominal
        else:
            if kind == "Up":
                scale_var = scale_nominal + JMS_sf[self.year][1]
            elif kind == "Down":
                scale_var = scale_nominal - JMS_sf[self.year][1]
            # get back raw mass with nominal scale and rescale it
            new_mass = (mass / scale_nominal) * scale_var
        return new_mass

    def smearFatJetMass(self, mass, current_smear, kind):
        res_MC = JMR_MC[self.year]
        res_SF_central = JMR_sf[self.year][0]

        if kind == "Central":
            if res_SF_central > 1: 
                sigma_MC = self.rnd.Gaus(0, res_MC)
                smearfactor = 1 + (sigma_MC/mass)* sqrt(res_SF_central**2 - 1) 
            else:
                smearfactor = 1
            # the base mass is the current one
            raw_mass = mass
        else:
            if kind == "Up":
                res_SF_var = res_SF_central + JMR_sf[self.year][1]
            elif kind == "Down":
                res_SF_var = res_SF_central - JMR_sf[self.year][1]
            # get the base smearing given by resolution at the beginning
            # This is Gaus(0, res_MC) used for nominal smearing (relative to nominal (scaled) mass)
            raw_mass = mass / current_smear
            sigma_MC_relative = 1

            if res_SF_central!=1: ## if res_SF_central==1, denominator==0
                sigma_MC_relative = (current_smear -1)  / ( sqrt(res_SF_central**2 -1))
            else:
                sigma_MC = self.rnd.Gaus(0, res_MC)
                sigma_MC_relative= (sigma_MC/mass)
            
            if res_SF_var > 1:
                smearfactor = 1 + sigma_MC_relative*sqrt(res_SF_var**2 - 1)
            else:
                smearfactor = 1

        #print "smear factor: ", smearfactor
        new_mass = raw_mass * smearfactor

        return new_mass, smearfactor
