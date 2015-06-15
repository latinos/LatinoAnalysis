#!/usr/bin/env python

from LatinoAnalysis.Gardener.gardening         import gardener_cli
from LatinoAnalysis.Gardener.gardening         import ModuleManager,Pruner,Grafter,AliasGrafter,RootWeighter
from LatinoAnalysis.Gardener.pileup            import PUpper
#from LatinoAnalysis.Gardener.ww                import WWPruner, WWFlagsGrafter
#from LatinoAnalysis.Gardener.efficiencies      import EffLepFiller,EffTrgFiller

# new variables
from LatinoAnalysis.Gardener.variables.WW2jVar                    import WW2jVarFiller
from LatinoAnalysis.Gardener.variables.WWVar                      import WWVarFiller
from LatinoAnalysis.Gardener.variables.ElectronsVar               import ElectronsVarFiller
from LatinoAnalysis.Gardener.variables.wwNLLcorrectionWeight      import wwNLLcorrectionWeightFiller

#generic tools
from LatinoAnalysis.Gardener.variables.TLorentzVectorCreator      import TLorentzVectorCreator



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
    #modules['effwfiller']       = EffLepFiller()
    #modules['efftfiller']       = EffTrgFiller()

# new variables
    modules['ww2jvarfiller']    = WW2jVarFiller()
    modules['wwvarfiller']      = WWVarFiller()
    modules['electronidfiller'] = ElectronsVarFiller()

# add nll re-weight for ww
    modules['wwNLLcorrections']      =  wwNLLcorrectionWeightFiller()


# generic tool
    modules['tlorentzvectorfiller']  = TLorentzVectorCreator()



    gardener_cli( modules )