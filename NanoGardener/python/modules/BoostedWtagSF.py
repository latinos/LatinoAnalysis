import ROOT
from math import sqrt
ROOT.PyConfig.IgnoreCommandLineOptions = True


from PhysicsTools.NanoAODTools.postprocessing.framework.datamodel import Collection
from PhysicsTools.NanoAODTools.postprocessing.framework.eventloop import Module
from LatinoAnalysis.NanoGardener.framework.BranchMapping import mappedOutputTree, mappedEvent

# High purity category SF and uncertainty
SF_hp = {
    "2016": (1.  ,  0.06 ),
    "2017": (0.97,  0.06 ),
    "2018": (0.980, 0.027)
}
# Low purity category SF and uncertainty
SF_lp = {
    "2016": (0.96, 0.11 ),
    "2017": (1.14, 0.29 ),
    "2018": (1.20, 0.275)
}

class BoostedWtagSF(Module):
    
    def __init__(self, year, input_branch_suffix="", output_branch_map="",
                    jetid=0, minpt=200.0, maxeta=2.4, max_tau21=0.45, mass_range=[65, 105], 
                    over_lepR =0.8, debug = False):
        '''
        
        The input_branch_prefix is used to load the correct branches from the CorrFatJet module. 
        The output_branch_map is used to save the variations with the correct suffix. 

        '''
        self.year = year
        self.jetid = jetid
        self.minpt = minpt
        self.maxeta = maxeta 
        self.max_tau21 = max_tau21
        self.mass_range = mass_range 
        self.over_lepR = over_lepR
        self.debug = debug
        self._output_branch_map = output_branch_map
        if input_branch_suffix != '':
            self._input_branch_prefix = "_"+ input_branch_suffix
        else:
            # nominal vars from NanoAODtools
            self._input_branch_prefix = "_nom"


    def beginJob(self):
        pass
    def endJob(self):
        pass

    def beginFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        self.out = mappedOutputTree(wrappedOutputTree, mapname=self._output_branch_map)
        # New Branches
        self.out.branch("BoostedWtagSF_nominal", "F")
        self.out.branch("BoostedWtagSF_up",    "F")
        self.out.branch("BoostedWtagSF_down", "F")


    def endFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        pass


    def analyze(self, event):
        # Let's map the event with the branch mapping we are using in the chain
        event = mappedEvent(event, mapname=self._output_branch_map)
        # output SF: nominal, up, down
        output_SF = [1., 1., 1.,]
        
        
        #  We need to get a list of FatJet passing kinematical cuts and lepton cleaning 
        # and then check the tau21 selection to assign the correct SF

        leptons_coll = Collection(event, "Lepton")
        fatjets_coll = Collection(event, "FatJet")

        goodfatjet_tau21s = []
        for ifj, fj in enumerate(fatjets_coll):
            # removing attribute fetching for performance
            fj_id            = fj.jetId
            fj_eta           = fj.eta
            fj_phi           = fj.phi
            fj_tau1          = fj.tau1
            fj_tau2          = fj.tau2
            # Get branches with prefixes for Jes,jmr,jer
            fj_softdrop_mass = getattr(fj, "msoftdrop" + self._input_branch_prefix)
            if "jes" in self._input_branch_prefix or "jer" in self._input_branch_prefix :
                fj_pt = getattr(fj, "pt" + self._input_branch_prefix) # for systematic variations
            else:
                fj_pt  = fj.pt  
            
            # If the FatJet has only 1 particle remove it (rare corner case)
            if fj_tau1 == 0:  continue
            fj_tau21 = fj_tau2 / fj_tau1
            
            goodFatJet = True
            if fj_id      <  self.jetid     : goodFatJet = False
            if fj_pt < self.minpt:              goodFatJet = False
            if abs(fj_eta) > self.maxeta :      goodFatJet = False
            if fj_softdrop_mass < self.mass_range[0] or fj_softdrop_mass> self.mass_range[1]: goodFatJet = False
            
            # Do not perform tau21 cut

            # Check overlap with leptons if the ID kinematics cuts are passed
            if goodFatJet:
                # Loop on leptons and exclude FatJet if there's a lepton with DeltaR < 1
                for il,lep in enumerate(leptons_coll):
                    dRLep = self.getDeltaR(fj_phi, fj_eta, lep.phi, lep.eta)
                    if dRLep < self.over_lepR:
                        goodFatJet = False

            # Now save the tau21 of the Fatjet passing kinematical cuts
            if goodFatJet:
                goodfatjet_tau21s.append(fj_tau21)
    

        # Apply the tau21 cut on all the fatjets passing the kinematical cuts
        tau21cut = list(map(lambda t: t<=self.max_tau21, goodfatjet_tau21s))

        if any(tau21cut):
            #  we have found at least one fatjet passing kin cuts and also tau21 ID --> high purity SF region
            hpsf, hpsf_unc = SF_hp[self.year]
            output_SF = [ hpsf,            #nomimal
                            hpsf + hpsf_unc, #up
                            hpsf - hpsf_unc  #down
                        ]

        elif len(tau21cut)>0:
            # If there is not fatjet passing tau cut but there are good fatjet passing kinematical cuts  --> low purity SF region 
            lpsf, lpsf_unc = SF_lp[self.year]
            # The up/down variations are opposite than the high purity category
            output_SF = [ lpsf,            #nomimal
                            lpsf - lpsf_unc, #up
                            lpsf + lpsf_unc  #down
                        ]
        # If there are not good fatjet the SF remains 1.   
                   
        # Write out 
        self.out.fillBranch("BoostedWtagSF_nominal", output_SF[0])
        self.out.fillBranch("BoostedWtagSF_up",      output_SF[1])  
        self.out.fillBranch("BoostedWtagSF_down",    output_SF[2])
        
        return True
               
            
    def getDeltaR(self, phi1, eta1, phi2, eta2):
        dphi = phi1 - phi2
        if dphi > ROOT.TMath.Pi(): dphi -= 2*ROOT.TMath.Pi()
        if dphi < -ROOT.TMath.Pi(): dphi += 2*ROOT.TMath.Pi()
        deta = eta1 - eta2
        deltaR = sqrt((deta*deta) + (dphi*dphi))
        return deltaR
