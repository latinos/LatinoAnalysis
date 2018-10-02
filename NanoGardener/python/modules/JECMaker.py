from PhysicsTools.NanoAODTools.postprocessing.modules.jme.jecUncertainties import jecUncertProducer 

class JECMaker(jecUncertProducer, object):
    '''
    Jet Energy Correction Module (running on CleanJet's)
    ''' 
    def __init__(self, globalTag, types=['Total'], jetFlav='AK4PFchs'):
       super(JECMaker, self).__init__(globalTag, uncerts=types, jetFlavour=jetFlav, jetColl="CleanJet") 
       types_str = 'CorrectionTypes = '
       for typ in types:
           types_str += typ
           types_str += ', '
       print('JECMaker: globaTag = ' + globalTag + ', ' + types_str + 'JetFlavour = ' + jetFlav)

    def beginFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        self.out = wrappedOutputTree
        for u,branchname in self.uncerts :
            self.out.branch(branchname, "F", lenVar="n"+self.jetColl)

