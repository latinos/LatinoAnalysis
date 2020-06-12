import re
import ROOT
from LatinoAnalysis.NanoGardener.data.common_cfg import Type_dict
from PhysicsTools.NanoAODTools.postprocessing.modules.jme.jetSmearer import jetSmearer 
from PhysicsTools.NanoAODTools.postprocessing.tools import matchObjectCollection, matchObjectCollectionMultiple
from PhysicsTools.NanoAODTools.postprocessing.framework.eventloop import Module
from PhysicsTools.NanoAODTools.postprocessing.framework.datamodel import Collection
from PhysicsTools.NanoAODTools.postprocessing.framework.datamodel import Object

class JERMaker(jetSmearer, object):
    ##################################################################################
    # Jet Energy Resolution (JER) and JER scale factors creator
    # @Wrapper on CleanJet collection@
    # !To be applied AFTER nominal JEC corrections on MC only!
    ##################################################################################
    def __init__(self, era, globalTag,\
                 jetType="AK4PFchs",\
                 jetColl="CleanJet",\
                 jerTag="",\
                 jmr_vals=[]\
                ):
       self.era = era
       self.rhoBranchName = "fixedGridRhoFastjetAll"  #averaged jet energy density 
       
       if jerTag != "":
           self.jerInputFileName = jerTag+"_PtResolution_"+jetType+".txt"
           self.jerUncertaintyInputFileName = jerTag+"_SF_"+jetType+".txt"
       else:
           if era == "2016":
               self.jerInputFileName = "Summer16_25nsV1_MC_PtResolution_" + jetType + ".txt"
               self.jerUncertaintyInputFileName = "Summer16_25nsV1_MC_SF_" + jetType + ".txt"
           elif era == "2017" or era == "2018": ## use 2017 JER for 2018 for the time being
               self.jerInputFileName = "Fall17_V3_MC_PtResolution_" + jetType + ".txt"
               self.jerUncertaintyInputFileName = "Fall17_V3_MC_SF_" + jetType + ".txt"
           elif era == "2018" and False: ## jetSmearer not working with 2018 JERs yet
               self.jerInputFileName = "Autumn18_V7_MC_PtResolution_" + jetType + ".txt"
               self.jerUncertaintyInputFileName = "Autumn18_V7_MC_SF_" + jetType + ".txt"
           else:
               raise ValueError("[ERROR] Invalid era "+str(era))
 
       if globalTag != "":
           print("[WARNING] Global tag approach not supported for JER smearing yet!")
               
       if "AK4" in jetType:
           self.jetBranchName = jetColl
           self.lenVar = "n"+jetColl
           self.genJetBranchName = "GenJet"
           if len(jmr_vals) != 0: print("[WARNING] JMR values ignored. (To be used with fat jets only.)")  
       else:
           raise ValueError("[ERROR] Jet type: "+str(jetType)+" not supported yet.")   

       super(JERMaker, self).__init__(globalTag, jetType=jetType,\
                                      jerInputFileName=self.jerInputFileName,\
                                      jerUncertaintyInputFileName=self.jerUncertaintyInputFileName,\
                                      jmr_vals=jmr_vals\
                                     )
       print("JERMaker: \n"+"    JetType = "+jetType+"\n"+"    JetColl = "+jetColl+"\n"+\
             "    JER input = "+self.jerInputFileName+"\n"+"    JER SF input = "+self.jerUncertaintyInputFileName)

    def beginFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        self.out = wrappedOutputTree
        self.collBr = {}
        oBrList = self.out._tree.GetListOfBranches()
        self.hasMass = False
        self.backupColl = ""
        for br in oBrList:
            bname = br.GetName()
            btype = Type_dict[br.GetListOfLeaves()[0].GetTypeName()]
            if re.match('\A'+self.jetBranchName+'_', bname):
                if btype not in self.collBr: self.collBr[btype] = []
                self.collBr[btype].append(bname)
                self.out.branch(bname, btype, lenVar=self.lenVar)
                # Does the jet collection have a mass or do we need a backup collection?
                if bname == self.jetBranchName+'_mass': 
                    self.hasMass = True
        if not self.hasMass:
            self.backupColl = "Jet"
            self.out.branch("%s_mass" % self.jetBranchName, "F", lenVar=self.lenVar) 
            if 'F' not in self.collBr: self.collBr['F'] = []
            self.collBr['F'].append(self.jetBranchName+"_mass")
        self.out.branch("%s_corr_JER" % self.jetBranchName, "F", lenVar=self.lenVar)
        for shift in ['Up','Down']:
            self.out.branch("%s_pt_JER%s" % (self.jetBranchName, shift), "F", lenVar=self.lenVar)
            self.out.branch("%s_mass_JER%s" % (self.jetBranchName, shift), "F", lenVar=self.lenVar)

    def endFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        pass

    def analyze(self, event):
        """process event, return True (go to next module) or False (fail, go to next event)"""
        jets      = Collection(event, self.jetBranchName    )
        genJets   = Collection(event, self.genJetBranchName )
        rho       = getattr(event, self.rhoBranchName       )
        if not self.hasMass:
            backupJets = Collection(event, self.backupColl)

        def isResMatching(jet,genJet):
            params = ROOT.PyJetParametersWrapper()
            params.setJetEta(jet.eta)
            params.setJetPt(jet.pt)
            params.setRho(rho)

            resolution = self.jer.getResolution(params) #super

            return abs(jet.pt - genJet.pt) < 3*resolution*jet.pt

        pairs     = matchObjectCollection(jets, genJets, dRmax=0.2, presel=isResMatching)

        #randomize smearer
        self.setSeed(event) 
        
        jets_pt_nom       = []
        jets_mass_nom     = []
        jets_corr_JER     = []
        jets_pt_JERUp     = []
        jets_pt_JERDown   = []
        jets_mass_JERUp   = []
        jets_mass_JERDown = [] 
        for iJet, jet in enumerate(jets):
            genJet = pairs[jet]
            if not self.hasMass: 
                jet.mass = backupJets[jet.jetIdx].mass

            #evaluate JER SF for central and up/down variations
            ( jet_pt_jerNomVal, jet_pt_jerUpVal, jet_pt_jerDownVal ) = self.getSmearValsPt(jet, genJet, rho) #super
            jet_pt_nom       = jet.pt   * jet_pt_jerNomVal
            jet_pt_JERUp     = jet.pt   * jet_pt_jerUpVal
            jet_pt_JERDown   = jet.pt   * jet_pt_jerDownVal
            if not self.hasMass:
                jet_mass_nom     = backupJets[jet.jetIdx].mass * jet_pt_jerNomVal
                jet_mass_JERUp   = backupJets[jet.jetIdx].mass * jet_pt_jerUpVal
                jet_mass_JERDown = backupJets[jet.jetIdx].mass * jet_pt_jerDownVal
            else:
                jet_mass_nom     = jet.mass * jet_pt_jerNomVal 
                jet_mass_JERUp   = jet.mass * jet_pt_jerUpVal
                jet_mass_JERDown = jet.mass * jet_pt_jerDownVal  
            jets_pt_nom      .append(jet_pt_nom)
            jets_mass_nom    .append(jet_mass_nom)
            jets_corr_JER    .append(jet_pt_jerNomVal)
            jets_pt_JERUp    .append(jet_pt_JERUp)
            jets_pt_JERDown  .append(jet_pt_JERDown)
            jets_mass_JERUp  .append(jet_mass_JERUp)
            jets_mass_JERDown.append(jet_mass_JERDown) 
      
        #Reorder
        order = []
        for idx1, pt1 in enumerate(jets_pt_nom):
            pt_idx = 0
            for idx2, pt2 in enumerate(jets_pt_nom):
                if pt1 < pt2 or (pt1 == pt2 and idx1 > idx2): pt_idx += 1
            order.append(pt_idx)

        #Save to updated branches to jet collection
        for typ in self.collBr:
            for bname in self.collBr[typ]:
                if '_pt' in bname:
                    temp_v = [jets_pt_nom[idx] for idx in order]
                    self.out.fillBranch(bname, temp_v)
                elif '_mass' in bname:
                    temp_v = [jets_mass_nom[idx] for idx in order]
                    self.out.fillBranch(bname, temp_v)
                else:
                    temp_b = bname.replace(self.jetBranchName+'_', '')
                    temp_v = [jets[idx][temp_b] for idx in order]
                    self.out.fillBranch(bname, temp_v)

        #Save new branches to jet collection
        self.out.fillBranch("%s_corr_JER"   % self.jetBranchName, [jets_corr_JER[idx] for idx in order]) 
        self.out.fillBranch("%s_pt_JERUp"   % self.jetBranchName, [jets_pt_JERUp[idx] for idx in order])
        self.out.fillBranch("%s_pt_JERDown" % self.jetBranchName, [jets_pt_JERDown[idx] for idx in order]) 
        self.out.fillBranch("%s_mass_JERUp"   % self.jetBranchName, [jets_mass_JERUp[idx] for idx in order])
        self.out.fillBranch("%s_mass_JERDown" % self.jetBranchName, [jets_mass_JERDown[idx] for idx in order])

        return True

# define modules using the syntax 'name = lambda : constructor' to avoid having them loaded when not needed
JERMakerMC16 = lambda : JERMaker("2016","",jetType="AK4PFchs",jetColl="CleanJet",jerTag="Summer16_25nsV1_MC",jmr_vals=[1.0, 1.2, 0.8])   
JERMakerMC17 = lambda : JERMaker("2017","",jetType="AK4PFchs",jetColl="CleanJet",jerTag="Fall17_V3_MC"      ,jmr_vals=[1.09, 1.14, 1.04])
JERMakerMC18 = lambda : JERMaker("2018","",jetType="AK4PFchs",jetColl="CleanJet",jerTag=""    ,jmr_vals=[1.24, 1.20, 1.28])          

