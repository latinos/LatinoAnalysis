#!/usr/bin/env python

from LatinoAnalysis.Gardener.gardening         import gardener_cli
from LatinoAnalysis.Gardener.gardening         import ModuleManager,Pruner,Grafter,AliasGrafter,RootWeighter
#from LatinoAnalysis.Gardener.ww                import WWPruner, WWFlagsGrafter
#from LatinoAnalysis.Gardener.efficiencies      import EffLepFiller,EffTrgFiller

# pileup
from LatinoAnalysis.Gardener.variables.pileup  import PUpper

# trigger efficiencies
from LatinoAnalysis.Gardener.variables.efficiencies               import EffTrgFiller

# id/isolation scale factors
from LatinoAnalysis.Gardener.variables.idisoScaleFactors          import IdIsoSFFiller



# selections
from LatinoAnalysis.Gardener.variables.l2Sel                      import L2SelFiller

# kinematic variables
from LatinoAnalysis.Gardener.variables.l2Kin                      import L2KinFiller

# fake weights adder for W+jet sample
from LatinoAnalysis.Gardener.variables.fakeWeight                 import FakeWeightFiller


# lepton pt corrector
from LatinoAnalysis.Gardener.variables.lepScaleCorrector          import LeptonPtCorrector

# qqWW corrections
from LatinoAnalysis.Gardener.variables.wwNLLcorrectionWeight      import wwNLLcorrectionWeightFiller
from LatinoAnalysis.Gardener.variables.qq2vvEWKcorrectionsWeight  import qq2vvEWKcorrectionsWeightFiller

# new variables
from LatinoAnalysis.Gardener.variables.WW2jVar                    import WW2jVarFiller
from LatinoAnalysis.Gardener.variables.WWVar                      import WWVarFiller
from LatinoAnalysis.Gardener.variables.ElectronsVar               import ElectronsVarFiller
from LatinoAnalysis.Gardener.variables.DMVar                      import DMVarFiller
from LatinoAnalysis.Gardener.variables.XWWVar                     import XWWVarFiller
from LatinoAnalysis.Gardener.variables.dymvaVar                   import DymvaVarFiller
# mucca
from LatinoAnalysis.Gardener.variables.muccaMvaVar                import MuccaMvaVarFiller   
# mrww
from LatinoAnalysis.Gardener.variables.MrWWVar                    import MrWWVarFiller   

# specific variables for MC
from LatinoAnalysis.Gardener.variables.mcWeights                  import mcWeightsFiller
from LatinoAnalysis.Gardener.variables.mcWeightsCount             import mcWeightsCounter

#generic tools
from LatinoAnalysis.Gardener.variables.TLorentzVectorCreator      import TLorentzVectorCreator

# JES uncertainty
from LatinoAnalysis.Gardener.variables.jetScaleUncertainty        import JESTreeMaker

# bpog sfale factors
from LatinoAnalysis.Gardener.variables.btagPogScaleFactors        import btagPogScaleFactors
# lepton pT scale uncertainty and resolution
from LatinoAnalysis.Gardener.variables.lepScaleUncertainty        import LeppTScalerTreeMaker
from LatinoAnalysis.Gardener.variables.lepResolutionUncertainty   import LeptonResolutionTreeMaker
# MET uncertainty
from LatinoAnalysis.Gardener.variables.metUncertainty             import MetUncertaintyTreeMaker
# QCD uncertainty
from LatinoAnalysis.Gardener.variables.qcdUncertainty             import QcdUncertaintyTreeMaker
# PDF uncertainty
from LatinoAnalysis.Gardener.variables.pdfUncertainty             import PdfUncertaintyTreeMaker
# PDF and scale uncertainty
from LatinoAnalysis.Gardener.variables.pdfAndScaleUncertainty     import PdfAndScaleUncertaintyTreeMaker


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

# trigger efficiency
    modules['efftfiller']       = EffTrgFiller()


# id/isolation scale factors
    modules['idisofiller'] = IdIsoSFFiller()

# specific variables for MC

    modules['mcweightscounter'] = mcWeightsCounter()
    modules['mcweightsfiller']  = mcWeightsFiller()


# new variables
    modules['ww2jvarfiller']    = WW2jVarFiller()
    modules['wwvarfiller']      = WWVarFiller()
    modules['electronidfiller'] = ElectronsVarFiller()
    modules['dmvarfiller']      = DMVarFiller()
    modules['xwwvarfiller']     = XWWVarFiller()
    modules['dymvaVarFiller']   = DymvaVarFiller()

# mucca
    modules['muccaMvaVarFiller']   = MuccaMvaVarFiller()

# mrWW
    modules['mrWWvarfiller']   = MrWWVarFiller()



# add nll re-weight for ww
    modules['wwNLLcorrections']      =  wwNLLcorrectionWeightFiller()
    modules['wwEWKcorrections']      =  qq2vvEWKcorrectionsWeightFiller()


# add bpog SF
    modules['btagPogScaleFactors']   = btagPogScaleFactors()

# generic tool
    modules['tlorentzvectorfiller']  = TLorentzVectorCreator()

# apply selections and update variables
    modules['l2selfiller']     = L2SelFiller()


# update kinematic variables
    modules['l2kinfiller']     = L2KinFiller()

# Nuisances
    modules['JESTreeMaker']           = JESTreeMaker()
    modules['LeppTScalerTreeMaker']   = LeppTScalerTreeMaker()
    modules['leptonResolution']       = LeptonResolutionTreeMaker()
    modules['metUncertainty']         = MetUncertaintyTreeMaker()
    modules['pdfUncertainty']         = PdfUncertaintyTreeMaker()
    modules['qcdUncertainty']         = QcdUncertaintyTreeMaker()
    modules['pdfAndScaleUncertainty'] = PdfAndScaleUncertaintyTreeMaker()
    
    
# fake weights
    modules['fakeWeights']      = FakeWeightFiller()

# lepton pt corrector
    modules['letPtCorrector']   = LeptonPtCorrector()




    gardener_cli( modules )


