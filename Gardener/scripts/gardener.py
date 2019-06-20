#!/usr/bin/env python

from LatinoAnalysis.Gardener.gardening         import gardener_cli
from LatinoAnalysis.Gardener.gardening         import ModuleManager,Pruner,Grafter,AliasGrafter,RootWeighter
#from LatinoAnalysis.Gardener.ww                import WWPruner, WWFlagsGrafter
#from LatinoAnalysis.Gardener.efficiencies      import EffLepFiller,EffTrgFiller

# pileup
from LatinoAnalysis.Gardener.variables.pileup  import PUpper

# trigger efficiencies
from LatinoAnalysis.Gardener.variables.efficiencies               import EffTrgFiller
from LatinoAnalysis.Gardener.variables.triggerMaker               import triggerCalculator
from LatinoAnalysis.Gardener.variables.triggerMaker               import triggerMaker

# id/isolation scale factors
from LatinoAnalysis.Gardener.variables.idisoScaleFactors          import IdIsoSFFiller
from LatinoAnalysis.Gardener.variables.multiIdisoScaleFactors     import MultiIdIsoSFFiller
from LatinoAnalysis.Gardener.variables.LeptonEtaPtCorrFactors     import LeptonEtaPtCorrFactors

# selections
from LatinoAnalysis.Gardener.variables.l2Sel                      import L2SelFiller
from LatinoAnalysis.Gardener.variables.l1Sel                      import L1SelFiller
from LatinoAnalysis.Gardener.variables.LeptonSel                  import LeptonSel
from LatinoAnalysis.Gardener.variables.TauCleaning                import TauCleaning 

# kinematic variables
from LatinoAnalysis.Gardener.variables.l2Kin                      import L2KinFiller
from LatinoAnalysis.Gardener.variables.l3Kin                      import L3KinFiller
from LatinoAnalysis.Gardener.variables.l4Kin                      import L4KinFiller

# fake weights adder for W+jet sample
from LatinoAnalysis.Gardener.variables.fakeWeight                 import FakeWeightFiller
from LatinoAnalysis.Gardener.variables.multiFakeWeight            import multiFakeWeightFiller

# Charge Flip VBS
from LatinoAnalysis.Gardener.variables.chargeFlipWeightVBS        import chargeFlipWeightVBS


# lepton pt corrector
from LatinoAnalysis.Gardener.variables.lepScaleCorrector          import LeptonPtCorrector

# qqWW corrections
from LatinoAnalysis.Gardener.variables.wwNLLcorrectionWeight      import wwNLLcorrectionWeightFiller
from LatinoAnalysis.Gardener.variables.qq2vvEWKcorrectionsWeight  import qq2vvEWKcorrectionsWeightFiller

# qqWZ and qqZZ corrections
from LatinoAnalysis.Gardener.variables.qq2wzEWKcorrectionsWeight  import qq2wzEWKcorrectionsWeightFiller
from LatinoAnalysis.Gardener.variables.qq2zzEWKcorrectionsWeight  import qq2zzEWKcorrectionsWeightFiller

# rochester corrections to muon pt
from LatinoAnalysis.Gardener.variables.rochester_corrections       import rochester_corr

# new variables
from LatinoAnalysis.Gardener.variables.WW2jVar                    import WW2jVarFiller
from LatinoAnalysis.Gardener.variables.WWVar                      import WWVarFiller
from LatinoAnalysis.Gardener.variables.ElectronsVar               import ElectronsVarFiller
from LatinoAnalysis.Gardener.variables.DMVar                      import DMVarFiller
from LatinoAnalysis.Gardener.variables.XWWVar                     import XWWVarFiller
from LatinoAnalysis.Gardener.variables.dymvaVar                   import DymvaVarFiller
from LatinoAnalysis.Gardener.variables.dymvaHiggs                 import DymvaHiggsFiller
#from LatinoAnalysis.Gardener.variables.VBF_DNNvar                 import DNNvarFiller
#from LatinoAnalysis.Gardener.variables.VBF_DNNvarv1               import DNNvarFillerv1

from LatinoAnalysis.Gardener.variables.chargeFlipWeight           import chargeFlipWeight
# mucca
from LatinoAnalysis.Gardener.variables.muccaMvaVar                import MuccaMvaVarFiller
from LatinoAnalysis.Gardener.variables.muccaMonoHVar              import MuccaMonoHVarFiller
from LatinoAnalysis.Gardener.variables.muccaMonoHFullVar          import MuccaMonoHFullVarFiller
from LatinoAnalysis.Gardener.variables.muccaMonoHFullVarHigh      import MuccaMonoHFullVarHighFiller

# mrww
from LatinoAnalysis.Gardener.variables.MrWWVar                    import MrWWVarFiller   

# specific variables for MC
from LatinoAnalysis.Gardener.variables.mcWeights                  import mcWeightsFiller
from LatinoAnalysis.Gardener.variables.mcWeightsCount             import mcWeightsCounter
from LatinoAnalysis.Gardener.variables.GenVar                     import genVariablesFiller
# gen lepton matching
from LatinoAnalysis.Gardener.variables.genMatchVar                import GenMatchVarFiller

#generic tools
from LatinoAnalysis.Gardener.variables.TLorentzVectorCreator      import TLorentzVectorCreator

# filter duplicates in data
from LatinoAnalysis.Gardener.variables.filterDuplicates           import FilterDuplicates

# filter using a JSON in data
from LatinoAnalysis.Gardener.variables.filterJson                 import FilterJSON


# JES uncertainty
from LatinoAnalysis.Gardener.variables.jetScaleUncertainty        import JESTreeMaker

# bpog sfale factors
from LatinoAnalysis.Gardener.variables.btagPogScaleFactors        import btagPogScaleFactors
from LatinoAnalysis.Gardener.variables.allBtagPogScaleFactors     import allBtagPogScaleFactors
from LatinoAnalysis.Gardener.variables.allBtagPogScaleFactorsICHEP     import allBtagPogScaleFactorsICHEP
# lepton pT scale uncertainty and resolution
from LatinoAnalysis.Gardener.variables.lepScaleUncertainty        import LeppTScalerTreeMaker
from LatinoAnalysis.Gardener.variables.lepResolutionUncertainty   import LeptonResolutionTreeMaker
# MET uncertainty
from LatinoAnalysis.Gardener.variables.metUncertainty             import MetUncertaintyTreeMaker
from LatinoAnalysis.Gardener.variables.metUnclustered             import MetUnclusteredTreeMaker
from LatinoAnalysis.Gardener.variables.metXYshift                 import MetXYshiftTreeMaker
# QCD uncertainty
#from LatinoAnalysis.Gardener.variables.qcdUncertainty             import QcdUncertaintyTreeMaker
# PDF uncertainty
#from LatinoAnalysis.Gardener.variables.pdfUncertainty             import PdfUncertaintyTreeMaker
# EWK singlet reweighter
from LatinoAnalysis.Gardener.variables.BWEwkSingletReweighter     import BWEwkSingletReweighter
# PDF and scale uncertainty
#from LatinoAnalysis.Gardener.variables.pdfAndScaleUncertainty     import PdfAndScaleUncertaintyTreeMaker
# GenPT for the top
from LatinoAnalysis.Gardener.variables.TopGenPt                   import TopGenPt

# ggH uncertainty LHCXSWG
from LatinoAnalysis.Gardener.variables.ggHUncertainty             import ggHUncertaintyMaker
# ggH reweighting to MINLO
from LatinoAnalysis.Gardener.variables.ggHToMINLO                 import ggHtoMINLOMaker

# VH reweighting for anomalous HHH coupling
from LatinoAnalysis.Gardener.variables.reweightHHH                import genReweightHHHMaker



# generic formula adder
from LatinoAnalysis.Gardener.variables.genericFormulaAdder        import genericFormulaAdder

# generic TMVA
from LatinoAnalysis.Gardener.variables.genericTMVA        import GenericTMVAFiller

# Prefiring
from LatinoAnalysis.Gardener.variables.PrefireCorr_gardener          import PrefCorr

# jet pairs identification
from LatinoAnalysis.Gardener.variables.JetPairingGenVBS             import JetPairingGenVBS
from LatinoAnalysis.Gardener.variables.JetPairingVBS                import JetPairingVBS
from LatinoAnalysis.Gardener.variables.JetPairingHH                import JetPairingHH
from LatinoAnalysis.Gardener.variables.JetPairingGenHH             import JetPairingGenHH
from LatinoAnalysis.Gardener.variables.VBSjjlnu_kin                  import VBSjjlnu_kin

if __name__ == '__main__':

    print "gardener"
    
    modules = ModuleManager()
    modules['filter']           = Pruner()
    modules['adder']            = Grafter()
    modules['alias']            = AliasGrafter()
    modules['rootweighter']     = RootWeighter()
    #modules['wwfilter']         = WWPruner()
    #modules['wwflagger']        = WWFlagsGrafter()
    modules['puadder']          = PUpper()


# filter duplicates
    modules['filterduplicates']          = FilterDuplicates()

# filter using a json file
    modules['filterjson']          = FilterJSON()


# trigger efficiency
    modules['efftfiller']       = EffTrgFiller()
    modules['trigMaker']        = triggerMaker()

# id/isolation scale factors
    modules['idisofiller'] = IdIsoSFFiller()
    modules['multiidiso']  = MultiIdIsoSFFiller()
    modules['etaptlepsf']  = LeptonEtaPtCorrFactors()

# specific variables for MC

    modules['mcweightscounter'] = mcWeightsCounter()
    modules['mcweightsfiller']  = mcWeightsFiller()

# generator level variables
    modules['genvariablesfiller']  = genVariablesFiller()
# gen lepton matching
    modules['genmatchvarfiller']  = GenMatchVarFiller()




# new variables
    modules['ww2jvarfiller']    = WW2jVarFiller()
    modules['wwvarfiller']      = WWVarFiller()
    modules['electronidfiller'] = ElectronsVarFiller()
    modules['dmvarfiller']      = DMVarFiller()
    modules['xwwvarfiller']     = XWWVarFiller()
    modules['dymvaVarFiller']   = DymvaVarFiller()
    modules['dymvaHiggsFiller'] = DymvaHiggsFiller()
  #  modules['vbfdnnvarFiller']  = DNNvarFiller()
 #   modules['vbfdnnvarFillerv1']= DNNvarFillerv1()

# Charge Flip
    modules['chFlipProba']      = chargeFlipWeight()

# mucca
    modules['muccaMvaVarFiller']       = MuccaMvaVarFiller()
    modules['muccaMonoHVarFiller']     = MuccaMonoHVarFiller()
    modules['muccaMonoHFullVarFiller'] = MuccaMonoHFullVarFiller()
    modules['muccaMonoHFullVarHighFiller'] = MuccaMonoHFullVarHighFiller()

# mrWW
    modules['mrWWvarfiller']   = MrWWVarFiller()



# add nll re-weight for ww
    modules['wwNLLcorrections']      =  wwNLLcorrectionWeightFiller()
# add ewk re-weight for ww
    modules['wwEWKcorrections']      =  qq2vvEWKcorrectionsWeightFiller()

# add ewk re-weight for wz and zz
    modules['wzEWKcorrections']      =  qq2wzEWKcorrectionsWeightFiller()
    modules['zzEWKcorrections']      =  qq2zzEWKcorrectionsWeightFiller()

#add rochester weight for muon pt 
    modules['rochester'] = rochester_corr()
    
# add bpog SF
    modules['btagPogScaleFactors']   = btagPogScaleFactors()
    modules['allBtagPogScaleFactors'] = allBtagPogScaleFactors()
    modules['allBtagPogScaleFactorsICHEP'] = allBtagPogScaleFactorsICHEP()

# generic tool
    modules['tlorentzvectorfiller']  = TLorentzVectorCreator()

# apply selections and update variables
    modules['l2selfiller']     = L2SelFiller()
    modules['l1selfiller']     = L1SelFiller()
    modules['lepSel']          = LeptonSel()
    modules['cleanTau']        = TauCleaning()

# update kinematic variables
    modules['l2kinfiller']     = L2KinFiller()
    modules['l3kinfiller']     = L3KinFiller()
    modules['l4kinfiller']     = L4KinFiller()

# jet pairing
    modules['JetPairingGenVBS']   = JetPairingGenVBS()
    modules['JetPairingVBS']      = JetPairingVBS()
    modules['JetPairingGenHH']    = JetPairingGenHH()
    modules['JetPairingHH']       = JetPairingHH()
    modules['VBSjjlnu_kin']       = VBSjjlnu_kin()

# Nuisances
    modules['JESTreeMaker']           = JESTreeMaker()
    modules['LeppTScalerTreeMaker']   = LeppTScalerTreeMaker()
    modules['leptonResolution']       = LeptonResolutionTreeMaker()
    modules['metUncertainty']         = MetUncertaintyTreeMaker()
    modules['metUnclustered']         = MetUnclusteredTreeMaker()
    #modules['pdfUncertainty']         = PdfUncertaintyTreeMaker()
    #modules['qcdUncertainty']         = QcdUncertaintyTreeMaker()
    #modules['pdfAndScaleUncertainty'] = PdfAndScaleUncertaintyTreeMaker()
    
    
# fake weights
    modules['fakeWeights']      = FakeWeightFiller()
    modules['multiFakeWeights']      = multiFakeWeightFiller()
    modules['chargeFlipWeightVBS']      = chargeFlipWeightVBS()

# lepton pt corrector
    modules['letPtCorrector']   = LeptonPtCorrector()
# MET corrector
    modules['metXYshift']     = MetXYshiftTreeMaker()

# EWK bw weights
    modules['BWEwkSingletReweighter'] = BWEwkSingletReweighter()

# Top gen pt for reweighting
    modules['TopGenPt'] = TopGenPt()
    
# ggH uncertainty LHCXSWG
    modules['ggHUncertainty'] = ggHUncertaintyMaker()

# ggH reweighting to MINLO
    modules['ggHtoMINLO'] = ggHtoMINLOMaker()

# VH reweighting for anomalous HHH coupling
    modules['reweightHHH'] = genReweightHHHMaker()


# generic formula adder
    modules['genericFormulaAdder'] = genericFormulaAdder()

# generic TMVA
    modules['genericTMVA'] = GenericTMVAFiller()

# Prefiring
    modules['prefcorrMiniAOD']   = PrefCorr()

    gardener_cli( modules )


