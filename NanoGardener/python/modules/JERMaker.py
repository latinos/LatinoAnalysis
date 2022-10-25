import re
import os
import ROOT
from LatinoAnalysis.NanoGardener.data.common_cfg import Type_dict
from PhysicsTools.NanoAODTools.postprocessing.modules.jme.jetSmearer import jetSmearer 
from PhysicsTools.NanoAODTools.postprocessing.tools import matchObjectCollection, matchObjectCollectionMultiple
from PhysicsTools.NanoAODTools.postprocessing.framework.eventloop import Module
from PhysicsTools.NanoAODTools.postprocessing.framework.datamodel import Collection
from PhysicsTools.NanoAODTools.postprocessing.framework.datamodel import Object

class JERMaker(jetSmearer, object):
    ###############################################################################################
    # Jet Energy Resolution (JER) wrapper to apply nominal smearing on CleanJet or FatJet coll.
    # !To be applied AFTER nominal JEC corrections on MC only! 
    # (JEC applied on NanoAOD level for UL MC)
    # JER uncertainties (split or not) are by default created by UltraJetUncertaintiesProducer
    # therefore we switch OFF this functionality for JERMaker but it is possible to produce
    # variation branches.
    # References:
    # JER = jet energy resolution: https://twiki.cern.ch/twiki/bin/viewauth/CMS/JetResolution
    # JMR = jet mass resolution: https://twiki.cern.ch/twiki/bin/view/CMS/JetWtagging
    ###############################################################################################
    def __init__(self, era, cmssw, globalTag,\
                 jetType="AK4PFchs",\
                 jetColl="CleanJet",\
                 jerTag="",\
                 jerUncert=False,\
                 splitJER=False,\
                 doGroomed=False,\
                 applyAtLowPt=True,\
                 jmr_vals=[],\
                 jms_vals=[]\
                ):
       self.era = str(era)
       if cmssw != "":
           if "v9" in cmssw: self.era = "UL"+self.era
           if "v9HIPM" in cmssw and str(era) == "2016": self.era += "_preVFP"
       self.rhoBranchName = "fixedGridRhoFastjetAll"  #averaged jet energy density 
       self.jerUncert = jerUncert
       self.splitJER = splitJER
       self.doGroomed = doGroomed
       self.applyAtLowPt = applyAtLowPt
       self.jmrVals = jmr_vals      
       self.jmsVals = jms_vals
       self.isAK8 = "AK8" in jetType
       self.isAK4 = "AK4" in jetType 
       if self.splitJER: 
           self.splitJERIDs = list(range(6))
       else:
           self.splitJERIDs = [""]   

       if jerTag == "":
           #parse config with JER tags
           cmsswBase = os.getenv('CMSSW_BASE')
           configName = "LatinoAnalysis/NanoGardener/python/data/UltraJECandJER_cfg.py"
           config = {}
           with open(cmsswBase + '/src/' + configName) as src:
               exec(src) #tags now stored under 'config'
           if self.era not in ["2016","2017","2018","UL2016","UL2016_preVFP","UL2017","UL2018"]:
               raise ValueError("[ERROR] Invalid era "+str(self.era))
           else:
               jerTag = config['jerTagsMC'][str(self.era)]
               self.jmrVals = config['jmrVals'][str(self.era)]
               self.jmsVals = config['jmsVals'][str(self.era)]
       self.jerInputFileName = jerTag+"_PtResolution_"+jetType+".txt"
       self.jerUncertaintyInputFileName = jerTag+"_SF_"+jetType+".txt"
               
       if globalTag != "":
           print("[WARNING] Global tag approach (still) not supported for JER smearing!")
               
       if "AK4" in jetType:
           self.jetBranchName = jetColl
           self.lenVar = "n"+jetColl
           self.genJetBranchName = "GenJet"
           if len(self.jmrVals) != 0: print("[WARNING] JMR values ignored. (To be used with fat jets only.)") 
           if len(self.jmsVals) != 0: print("[WARNING] JMS values ignored. (To be used with fat jets only.)")
       elif "AK8" in jetType:
           self.jetBranchName = jetColl
           if "Fat" not in self.jetBranchName:
               print("[WARNING] Are you sure you have selected correct jet collection of AK8 jets? jetColl = "+self.jetBranchName) 
           self.subJetBranchName = "SubJet"
           self.genJetBranchName = "GenJetAK8"
           self.genSubJetBranchName = "SubGenJetAK8"
           self.lenVar = "n"+jetColl
           if len(self.jmrVals) == 0 : 
               raise ValueError("[ERROR]   JER tag was specified but JMR (mass resolution) values found empty.") 
           if len(self.jmsVals) == 0 :
               raise ValueError("[ERROR]   JER tag was specified but JMS (mass scale) values found empty.")
           if self.doGroomed: 
               #Here load PUPPI correction files (for now they do not exist for UL samples)
               print("[WARNING] Warning PUPPI corrections do not exist for UL samples.")
       else:
           raise ValueError("[ERROR] Jet type: "+str(jetType)+" not supported yet.")   

       #initialize jetSmearer and notify 
       super(JERMaker, self).__init__(globalTag, jetType=jetType,\
                                      jerInputFileName=self.jerInputFileName,\
                                      jerUncertaintyInputFileName=self.jerUncertaintyInputFileName,\
                                      jmr_vals=self.jmrVals\
                                     )
       print("JERMaker: \n"+"    JetType = "+jetType+"\n"+"    JetColl = "+jetColl+"\n"+\
             "    JER input = "+self.jerInputFileName+"\n"+"    JER SF input = "+self.jerUncertaintyInputFileName+"\n"+\
             "    JER uncty = "+str(self.jerUncert)+"\n"+"    splitJER = "+str(self.splitJER)+"\n"+\
             "    doGroomed = "+str(self.doGroomed)+"\n"+"    applyAtLowPt = "+str(self.applyAtLowPt))

    def beginFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        #setup output tree
        self.out = wrappedOutputTree
        self.collBr = {}
        oBrList = self.out._tree.GetListOfBranches()

        #(re)create branches
        self.hasMass = False
        self.hasGroomedMass = False
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
                if bname == self.jetBranchName+'_msoftdrop':
                    self.hasGroomedMass = True
        if self.isAK4:
            self.backupColl = "Jet"
        elif self.isAK8:
            self.backupColl = "FatJet" 
        if not self.hasMass:
            print("[WARNING] Original jet collection mass branch will be backed by "+self.backupColl+"_mass")  
            self.out.branch("%s_mass" % self.jetBranchName, "F", lenVar=self.lenVar) 
            if 'F' not in self.collBr: self.collBr['F'] = []
            self.collBr['F'].append(self.jetBranchName+"_mass")
        if not self.hasGroomedMass and self.isAK8 and self.doGroomed:
            print("[WARNING] Original jet collection soft drop mass branch will be backed by "+self.backupColl+"_msoftdrop")
            self.out.branch("%s_msoftdrop" % self.jetBranchName, "F", lenVar=self.lenVar)
            if 'F' not in self.collBr: self.collBr['F'] = []
            self.collBr['F'].append(self.jetBranchName+"_msoftdrop")
        self.out.branch("%s_corr_JER" % self.jetBranchName, "F", lenVar=self.lenVar)
        if self.isAK8:
            self.out.branch("%s_corr_JMS" % self.jetBranchName, "F", lenVar=self.lenVar)
            self.out.branch("%s_corr_JMR" % self.jetBranchName, "F", lenVar=self.lenVar)
            if self.doGroomed:
                self.out.branch("%s_msoftdrop_raw" % self.jetBranchName,"F",lenVar=self.lenVar)
                #add other branches when corrections are ready, msoftdrop branch will be only JER smeared for now and original stored in raw
        self.out.branch("%s_%sIdx_preJER" % (self.jetBranchName, self.jetBranchName[:1].lower() + self.jetBranchName[1:] if self.jetBranchName else ''), "I", lenVar=self.lenVar)
        if self.jerUncert:
            for shift in ['Up','Down']:
                for jerID in self.splitJERIDs:  
                    self.out.branch("%s_pt_JER%s%s" % (self.jetBranchName, jerID, shift), "F", lenVar=self.lenVar)
                    self.out.branch("%s_mass_JER%s%s" % (self.jetBranchName, jerID, shift), "F", lenVar=self.lenVar)
                    if self.isAK8 and self.doGroomed:
                        self.out.branch("%s_msoftdrop_JER%s%s" %(self.jetBranchName, jerID, shift), "F", lenVar=self.lenVar)
                if self.isAK8:
                    self.out.branch("%s_mass_JMR%s" % (self.jetBranchName, shift), "F", lenVar=self.lenVar)
                    self.out.branch("%s_mass_JMS%s" % (self.jetBranchName, shift), "F", lenVar=self.lenVar)

    def endFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        pass

    def getJERsplitID(self, pt, eta):
        if not self.splitJER:
            return ""
        if abs(eta) < 1.93:
            return 0
        elif abs(eta) < 2.5:
            return 1
        elif abs(eta) < 3:
            if pt < 50:
                return 2
            else:
                return 3
        else:
            if pt < 50:
                return 4
            else:
                return 5

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

        pairs = matchObjectCollection(jets, genJets, dRmax=0.2, presel=isResMatching)
        if self.doGroomed:
            subJets = Collection(event, self.subJetBranchName)
            genSubJets = Collection(event, self.genSubJetBranchName)
            genSubJetMatcher = matchObjectCollectionMultiple(genJets,genSubJets,dRmax=0.8)

        #randomize smearer
        self.setSeed(event) 
        
        jets_pt_nom       = []
        jets_mass_nom     = []
        jets_corr_JER     = []
        jets_pt_JERUp     = {}
        jets_pt_JERDown   = {}
        jets_mass_JERUp   = {}
        jets_mass_JERDown = {}
        if self.isAK8:
            jets_corr_JMS = []
            jets_corr_JMR = []
            jets_mass_JMRUp = []
            jets_mass_JMRDown = []
            jets_mass_JMSUp = []
            jets_mass_JMSDown = []
            if self.doGroomed:
                jets_msdcorr_nom = []
                jets_msdcorr_raw = []
                jets_msdcorr_JERUp = {}
                jets_msdcorr_JERDown = {}
        for jerID in self.splitJERIDs:
            jets_pt_JERUp[jerID]     = []
            jets_pt_JERDown[jerID]   = []
            jets_mass_JERUp[jerID]   = []
            jets_mass_JERDown[jerID] = [] 
            if self.isAK8 and self.doGroomed:
                jets_msdcorr_JERUp[jerID] = []
                jets_msdcorr_JERDown[jerID] = []
        for iJet, jet in enumerate(jets):
            genJet = pairs[jet]
            if not self.hasMass: 
                jet.mass = backupJets[jet.jetIdx].mass

            if self.era=="2016" and jet.pt<50 and abs(jet.eta)>2.5:
              # Special treatment in pre-UL 2016: We observed that jet horns arise in MC when applying JER to all jets in 2016 (causing data/MC disagreement)
              # Recipe agreed on with JetMET: Don't apply 2016 JER on low pT jets in the forward region
              ( jet_pt_jerNomVal, jet_pt_jerUpVal, jet_pt_jerDownVal ) = ( 1.0, 1.0, 1.0 )
            else:
              #evaluate JER SF for central and up/down variations
              ( jet_pt_jerNomVal, jet_pt_jerUpVal, jet_pt_jerDownVal ) = self.getSmearValsPt(jet, genJet, rho) #super

            if "UL" in self.era and self.isAK8: 
                #JMS and JMR corrections not evaluated for UL samples yet
                (jmsNomVal, jmsDownVal, jmsUpVal) = ( 1.0, 1.0, 1.0 )
                (jet_mass_jmrNomVal, jet_mass_jmrUpVal, jet_mass_jmrDownVal) = ( 1.0, 1.0, 1.0 )
            elif "UL" not in self.era and self.isAK8:
                #evaluate JMS and JMR scale factors and uncertainties
                (jmsNomVal, jmsDownVal, jmsUpVal) = self.jmsVals #global cfg
                (jet_mass_jmrNomVal, jet_mass_jmrUpVal, jet_mass_jmrDownVal) = self.jetSmearer.getSmearValsM(jet, genJet) #super

            if "UL" in self.era and (not self.applyAtLowPt) and jet.pt<50:
              ( jet_pt_jerNomVal, jet_pt_jerUpVal, jet_pt_jerDownVal ) = ( 1.0, 1.0, 1.0 )

            jet_pt_nom       = jet.pt   * jet_pt_jerNomVal
            jet_pt_JERUp     = jet.pt   * jet_pt_jerUpVal
            jet_pt_JERDown   = jet.pt   * jet_pt_jerDownVal
            if not self.hasMass:
                jet_mass_nom     = backupJets[jet.jetIdx].mass * jet_pt_jerNomVal if not self.isAK8 \
                                   else backupJets[jet.jetIdx].mass * jet_pt_jerNomVal * jet_mass_jmrNomVal * jmsNomVal
                #JMS and JMR correction are nominal for JER up/do variation
                jet_mass_JERUp   = backupJets[jet.jetIdx].mass * jet_pt_jerUpVal if not self.isAK8 \
                                   else backupJets[jet.jetIdx].mass * jet_pt_jerUpVal * jet_mass_jmrNomVal * jmsNomVal
                jet_mass_JERDown = backupJets[jet.jetIdx].mass * jet_pt_jerDownVal if not self.isAK8 \
                                   else backupJets[jet.jetIdx].mass * jet_pt_jerDownVal * jet_mass_jmrNomVal * jmsNomVal
                #And reversed for JMR/JMS variations
                jet_mass_JMRUp   = backupJets[jet.jetIdx].mass if not self.isAK8 \
                                   else backupJets[jet.jetIdx].mass * jet_pt_jerNomVal * jet_mass_jmrUpVal * jmsNomVal
                jet_mass_JMRDown = backupJets[jet.jetIdx].mass if not self.isAK8 \
                                   else backupJets[jet.jetIdx].mass * jet_pt_jerNomVal * jet_mass_jmrDownVal * jmsNomVal
                jet_mass_JMSUp   = backupJets[jet.jetIdx].mass if not self.isAK8 \
                                   else backupJets[jet.jetIdx].mass * jet_pt_jerNomVal * jet_mass_jmrNomVal * jmsUpVal
                jet_mass_JMSDown = backupJets[jet.jetIdx].mass if not self.isAK8 \
                                   else backupJets[jet.jetIdx].mass * jet_pt_jerNomVal * jet_mass_jmrNomVal * jmsDownVal
            else:
                jet_mass_nom     = jet.mass * jet_pt_jerNomVal if not self.isAK8 \
                                   else jet.mass * jet_pt_jerNomVal * jet_mass_jmrNomVal * jmsNomVal
                #JMS and JMR correction are nominal for JER up/do variation
                jet_mass_JERUp   = jet.mass * jet_pt_jerUpVal if not self.isAK8 \
                                   else jet.mass * jet_pt_jerUpVal * jet_mass_jmrNomVal * jmsNomVal
                jet_mass_JERDown = jet.mass * jet_pt_jerDownVal if not self.isAK8 \
                                   else jet.mass * jet_pt_jerDownVal * jet_mass_jmrNomVal * jmsNomVal  
                #And reversed for JMR/JMS variations
                jet_mass_JMRUp   = jet.mass if not self.isAK8 \
                                   else jet.mass * jet_pt_jerNomVal * jet_mass_jmrUpVal * jmsNomVal
                jet_mass_JMRDown = jet.mass if not self.isAK8 \
                                   else jet.mass * jet_pt_jerNomVal * jet_mass_jmrDownVal * jmsNomVal
                jet_mass_JMSUp   = jet.mass if not self.isAK8 \
                                   else jet.mass * jet_pt_jerNomVal * jet_mass_jmrNomVal * jmsUpVal
                jet_mass_JMSDown = jet.mass if not self.isAK8 \
                                   else jet.mass * jet_pt_jerNomVal * jet_mass_jmrNomVal * jmsDownVal

            #do also groomed for AK8
            if self.doGroomed and self.isAK8:
                '''
                genGroomedSubJets = genSubJetMatcher[genJet] if genJet is not None else None
                if genGroomedSubJets is not None and len(genGroomedSubJets) >= 2:
                    genGroomedJet = genGroomedSubJets[0].p4() + genGroomedSubJets[1].p4() 
                else:
                    genGroomedJet = None
                '''
                if jet.subJetIdx1 >= 0 and jet.subJetIdx2 >= 0:
                    groomedP4 = subJets[jet.subJetIdx1].p4() + subJets[jet.subJetIdx2].p4()
                else:
                    groomedP4 = None

                jet_msdcorr_raw = groomedP4.M() if groomedP4 is not None else 0.0
                # Here apply PUPPI SD mass correction https://github.com/cms-jet/PuppiSoftdropMassCorr/
                # Not existing for UL
                puppisd_total = 1.0 #puppisd_genCorr * puppisd_recoCorr
                if groomedP4 is not None:
                    groomedP4.SetPtEtaPhiM(groomedP4.Perp(), groomedP4.Eta(),
                                           groomedP4.Phi(),
                                           groomedP4.M() * puppisd_total)

                # now apply the mass Puppi correction to the raw value
                jet_msdcorr_raw = groomedP4.M() if groomedP4 is not None else 0.0

                # evaluate also JMS and JMR scale factors and uncertainties if exist
                # this would use genGroomedJet         

                # apply all 
                jet_msdcorr_nom = jet_msdcorr_raw * jet_pt_jerNomVal 
                jet_msdcorr_JERUp = jet_msdcorr_raw * jet_pt_jerUpVal
                jet_msdcorr_JERDown = jet_msdcorr_raw * jet_pt_jerDownVal
                #* jet_msdcorr_jmrNomVal * jmsNomVal

            #sanity corrections
            if jet_mass_nom < 0.0:
                jet_mass_nom *= -1.0
            if jet_pt_nom < 0.0:
                jet_pt_nom *= -1.0
            if self.doGroomed and self.isAK8:
                if jet_msdcorr_nom < 0.0:
                    jet_msdcorr_nom *= -1.0

            #store nominals
            jets_pt_nom  .append(jet_pt_nom)
            jets_mass_nom.append(jet_mass_nom)
            jets_corr_JER.append(jet_pt_jerNomVal)
            if self.isAK8:
                jets_corr_JMS.append(jmsNomVal)
                jets_corr_JMR.append(jet_mass_jmrNomVal)
                if self.doGroomed:
                    jets_msdcorr_nom.append(jet_msdcorr_nom)
                    jets_msdcorr_raw.append(jet_msdcorr_raw)

            #store uncties
            if self.jerUncert:
                jet_pt_jerUp = {
                    jerID: jet_pt_nom
                    for jerID in self.splitJERIDs
                }
                jet_pt_jerDown = {
                    jerID: jet_pt_nom
                    for jerID in self.splitJERIDs
                }
                jet_mass_jerUp = {
                    jerID: jet_mass_nom
                    for jerID in self.splitJERIDs
                }
                jet_mass_jerDown = {
                    jerID: jet_mass_nom
                    for jerID in self.splitJERIDs
                }
                if self.isAK8 and self.doGroomed:
                    jet_msdcorr_jerUp = {
                        jerID: jet_msdcorr_nom
                        for jerID in self.splitJERIDs
                    }
                    jet_msdcorr_jerDown = {
                        jerID: jet_msdcorr_nom
                        for jerID in self.splitJERIDs
                    }
                thisJERID = self.getJERsplitID(jet_pt_nom, jet.eta)
                jet_pt_jerUp[thisJERID]     = jet_pt_JERUp
                jet_pt_jerDown[thisJERID]   = jet_pt_JERDown
                jet_mass_jerUp[thisJERID]   = jet_mass_JERUp
                jet_mass_jerDown[thisJERID] = jet_mass_JERDown
                if self.isAK8 and self.doGroomed:
                    jet_msdcorr_jerUp[thisJERID] = jet_msdcorr_JERUp
                    jet_msdcorr_jerDown[thisJERID] = jet_msdcorr_JERDown
 
                for jerID in self.splitJERIDs: 
                    jets_pt_JERUp[jerID]    .append(jet_pt_jerUp[jerID])
                    jets_pt_JERDown[jerID]  .append(jet_pt_jerDown[jerID])
                    jets_mass_JERUp[jerID]  .append(jet_mass_jerUp[jerID])
                    jets_mass_JERDown[jerID].append(jet_mass_jerDown[jerID])
                    if self.isAK8 and self.doGroomed:
                        jets_msdcorr_JERUp[jerID]  .append(jet_msdcorr_jerUp[jerID]) 
                        jets_msdcorr_JERDown[jerID].append(jet_msdcorr_jerDown[jerID])

                if self.isAK8:  
                    jets_mass_JMRUp.append(jet_mass_JMRUp)
                    jets_mass_JMRDown.append(jet_mass_JMRDown)
                    jets_mass_JMSUp.append(jet_mass_JMSUp)
                    jets_mass_JMSDown.append(jet_mass_JMSDown)
      
        # Reorder
        #
        # e.g. if pt is         [ 26, 24, 27 ]
        #      you get: order = [ 2, 0, 1]
        #
        order = sorted(range(len(jets_pt_nom)), key=jets_pt_nom.__getitem__, reverse=True)

        #Save to updated branches to jet collection
        for typ in self.collBr:
            for bname in self.collBr[typ]:
                if '_pt' in bname:
                    temp_v = [jets_pt_nom[idx] for idx in order]
                    self.out.fillBranch(bname, temp_v)
                elif '_mass' in bname:
                    temp_v = [jets_mass_nom[idx] for idx in order]
                    self.out.fillBranch(bname, temp_v)
                elif '_msoftdrop' in bname and self.isAK8 and self.doGroomed:
                    temp_v = [jets_msdcorr_nom[idx] for idx in order]
                    self.out.fillBranch(bname, temp_v)
                else:
                    temp_b = bname.replace(self.jetBranchName+'_', '')
                    temp_v = [jets[idx][temp_b] for idx in order]
                    self.out.fillBranch(bname, temp_v)

        #Save new branches to jet collection
        self.out.fillBranch("%s_corr_JER"   % self.jetBranchName, [jets_corr_JER[idx] for idx in order])
        if self.isAK8:
            self.out.fillBranch("%s_corr_JMS"   % self.jetBranchName, [jets_corr_JMS[idx] for idx in order])
            self.out.fillBranch("%s_corr_JMR"   % self.jetBranchName, [jets_corr_JMR[idx] for idx in order])
        self.out.fillBranch("%s_%sIdx_preJER"   % (self.jetBranchName, self.jetBranchName[:1].lower() + self.jetBranchName[1:] if self.jetBranchName else ''), order) 
        if self.jerUncert:
            for jerID in self.splitJERIDs:
                self.out.fillBranch("%s_pt_JER%sUp"   % (self.jetBranchName, jerID), [jets_pt_JERUp[jerID][idx] for idx in order])
                self.out.fillBranch("%s_pt_JER%sDown" % (self.jetBranchName, jerID), [jets_pt_JERDown[jerID][idx] for idx in order]) 
                self.out.fillBranch("%s_mass_JER%sUp"   % (self.jetBranchName, jerID), [jets_mass_JERUp[jerID][idx] for idx in order])
                self.out.fillBranch("%s_mass_JER%sDown" % (self.jetBranchName, jerID), [jets_mass_JERDown[jerID][idx] for idx in order])
                if self.isAK8 and self.doGroomed:
                    self.out.fillBranch("%s_msoftdrop_JER%sUp"   % (self.jetBranchName, jerID), [jets_msdcorr_JERUp[jerID][idx] for idx in order])
                    self.out.fillBranch("%s_msoftdrop_JER%sDown" % (self.jetBranchName, jerID), [jets_msdcorr_JERDown[jerID][idx] for idx in order]) 
            if self.isAK8:
                self.out.fillBranch("%s_mass_JMRUp" % self.jetBranchName, [jets_mass_JMRUp[idx] for idx in order])
                self.out.fillBranch("%s_mass_JMRDown" % self.jetBranchName, [jets_mass_JMRDown[idx] for idx in order])
                self.out.fillBranch("%s_mass_JMSUp" % self.jetBranchName, [jets_mass_JMSUp[idx] for idx in order])
                self.out.fillBranch("%s_mass_JMSDown" % self.jetBranchName, [jets_mass_JMSDown[idx] for idx in order])

        return True

# define modules using the syntax 'name = lambda : constructor' to avoid having them loaded when not needed
JERMakerMC16 = lambda : JERMaker("2016","","",jetType="AK4PFchs",jetColl="CleanJet",jerTag="Summer16_25nsV1_MC",jmr_vals=[1.0, 1.2, 0.8])   
JERMakerMC17 = lambda : JERMaker("2017","","",jetType="AK4PFchs",jetColl="CleanJet",jerTag="Fall17_V3_MC"      ,jmr_vals=[1.09, 1.14, 1.04])
JERMakerMC18 = lambda : JERMaker("2018","","",jetType="AK4PFchs",jetColl="CleanJet",jerTag="Autumn18_V7b_MC"    ,jmr_vals=[1.24, 1.20, 1.28])          
JERMakerMCUL16 = lambda : JERMaker("2016","Full2016v9noHIPM","",jetType="AK4PFchs",jetColl="CleanJet",jerTag="")
JERMakerMCUL16_preVFP = lambda : JERMaker("2016","Full2016v9HIPM","",jetType="AK4PFchs",jetColl="CleanJet",jerTag="")
JERMakerMCUL17 = lambda : JERMaker("2017","Full2017v9","",jetType="AK4PFchs",jetColl="CleanJet",jerTag="")
JERMakerMCUL18 = lambda : JERMaker("2018","Full2018v9","",jetType="AK4PFchs",jetColl="CleanJet",jerTag="")
FatJERMakerMCUL16 = lambda : JERMaker("2016","Full2016v9noHIPM","",jetType="AK8PFPuppi",jetColl="FatJet",jerTag="",doGroomed=True)
FatJERMakerMCUL16_preVFP = lambda : JERMaker("2016","Full2016v9HIPM","",jetType="AK8PFPuppi",jetColl="FatJet",jerTag="",doGroomed=True)
FatJERMakerMCUL17 = lambda : JERMaker("2017","Full2017v9","",jetType="AK8PFPuppi",jetColl="FatJet",jerTag="",doGroomed=True)
FatJERMakerMCUL18 = lambda : JERMaker("2018","Full2018v9","",jetType="AK8PFPuppi",jetColl="FatJet",jerTag="",doGroomed=True)
FatJERMakerMCUL17_highPt = lambda : JERMaker("2017","Full2017v9","",jetType="AK8PFPuppi",jetColl="FatJet",jerTag="",doGroomed=True, applyAtLowPt=False)
FatJERMakerMCUL18_highPt = lambda : JERMaker("2018","Full2018v9","",jetType="AK8PFPuppi",jetColl="FatJet",jerTag="",doGroomed=True, applyAtLowPt=False)
