#
#
#
#   \ \        / \ \        /       \  |  |      |
#    \ \  \   /   \ \  \   /         \ |  |      |
#     \ \  \ /     \ \  \ /        |\  |  |      |
#      \_/\_/       \_/\_/        _| \_| _____| _____|
#
#
#
#


import ROOT
ROOT.PyConfig.IgnoreCommandLineOptions = True

from PhysicsTools.NanoAODTools.postprocessing.framework.datamodel import Collection 
from PhysicsTools.NanoAODTools.postprocessing.framework.eventloop import Module

import os.path


class wwNLLcorrectionWeightProducer(Module):
    def __init__(self):
        print ' ------> wwNLLcorrectionWeightProducer Init() ----'
        # change this part into correct path structure... 
        cmssw_base = os.getenv('CMSSW_BASE')
        try:
            ROOT.gROOT.LoadMacro(cmssw_base+'/src/LatinoAnalysis/Gardener/python/variables/wwNLLcorrectionWeight.C+g')
        except RuntimeError:
            ROOT.gROOT.LoadMacro(cmssw_base+'/src/LatinoAnalysis/Gardener/python/variables/wwNLLcorrectionWeight.C++g')

        self.wwNLL = ROOT.wwNLL(
                           cmssw_base+'/src/LatinoAnalysis/Gardener/python/data/wwresum/central.dat',
                           cmssw_base+'/src/LatinoAnalysis/Gardener/python/data/wwresum/resum_up.dat',  
                           cmssw_base+'/src/LatinoAnalysis/Gardener/python/data/wwresum/resum_down.dat',
                           cmssw_base+'/src/LatinoAnalysis/Gardener/python/data/wwresum/scale_up.dat', 
                           cmssw_base+'/src/LatinoAnalysis/Gardener/python/data/wwresum/scale_down.dat'
                           )

      
    def beginJob(self):
        pass

    def endJob(self):
        pass

    def beginFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        self.out = wrappedOutputTree
        newbranches = ['nllnnloW', 'nllW', 'nllW_Rup', 'nllW_Qup', 'nllW_Rdown', 'nllW_Qdown', 'gen_mww', 'gen_ptww']
        for nameBranches in newbranches :
          self.out.branch(nameBranches  ,  "F");

    def endFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        pass

    def analyze(self, event):
        """process event, return True (go to next module) or False (fail, go to next event)"""

        nllnnloW    = -1
        nllW        = -1
        nllW_Rup    = -1
        nllW_Qup    = -1
        nllW_Rdown  = -1
        nllW_Qdown  = -1
        gen_mww     = -1
        gen_ptww    = -1

        genParticles = Collection(event, "GenPart")
        
        ptV1  = -1
        ptV2  = -1
        phiV1 = -1
        phiV2 = -1
        etaV1 = -1
        etaV2 = -1
                
        for particle  in genParticles :
          # 24 = W+/-
          #                                         == 13 : isLastCopy
          if abs(particle.pdgId) == 24 and (particle.statusFlags >> 13 & 1):
 
              if ptV1 == -1 :
                ptV1  = particle.pt
                phiV1 = particle.phi
                etaV1 = particle.eta
              elif ptV2 == -1 :
                ptV2  = particle.pt
                phiV2 = particle.phi
                etaV2 = particle.eta
                

        if ptV1 != -1 and ptV2 != -1 :
          self.wwNLL.SetPTWW(ptV1, phiV1, etaV1, ptV2, phiV2, etaV2)

        
          gen_ptww  = self.wwNLL.GetPTWW()
          gen_mww   = self.wwNLL.GetMWW()
           
          nllnnloW   = self.wwNLL.nllnnloWeight(0) 
          nllW       = self.wwNLL.nllWeight(0) 
          nllW_Rup   = self.wwNLL.nllWeight(1,1) 
          nllW_Qup   = self.wwNLL.nllWeight(1,0) 
          nllW_Rdown = self.wwNLL.nllWeight(-1,1) 
          nllW_Qdown = self.wwNLL.nllWeight(-1,0) 
           
 
        self.out.fillBranch("gen_ptww",   gen_ptww)
        self.out.fillBranch("gen_mww",    gen_mww)

        self.out.fillBranch("nllnnloW",   nllnnloW)
        self.out.fillBranch("nllW",       nllW)
        self.out.fillBranch("nllW_Rup",   nllW_Rup)
        self.out.fillBranch("nllW_Qup",   nllW_Qup)
        self.out.fillBranch("nllW_Rdown", nllW_Rdown)
        self.out.fillBranch("nllW_Qdown", nllW_Qdown)


        return True



