import ROOT
ROOT.PyConfig.IgnoreCommandLineOptions = True

from PhysicsTools.NanoAODTools.postprocessing.framework.datamodel import Collection 
from PhysicsTools.NanoAODTools.postprocessing.framework.eventloop import Module

class PromptParticlesGenVarsProducer(Module):
    def __init__(self):
        self.sortkey = lambda x: x.pt
        pass
    def beginJob(self):
        pass
    def endJob(self):
        pass
    def beginFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        self.out = wrappedOutputTree
        self.particleTypes = ["leptonGen", "neutrinoGen", "photonGen"]
        intQuantities   = ["MotherPID", "MotherStatus", "pdgId"]
        floatQuantities = ["eta", "phi", "pt"]
        boolQuantities  = ["fromHardProcess", "isDirectHadronDecayProduct", "isDirectPromptTauDecayProduct", "isPrompt", "isTauDecayProduct"]
        self.allQuantities = intQuantities + floatQuantities + boolQuantities

        for particle in self.particleTypes:
          for quantity in intQuantities:
            self.out.branch(particle+"_"+quantity, "I", lenVar="n"+particle)
          for quantity in floatQuantities:
            self.out.branch(particle+"_"+quantity, "F", lenVar="n"+particle) 
          for quantity in boolQuantities:
            self.out.branch(particle+"_"+quantity, "O", lenVar="n"+particle)

    def endFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        pass
    def analyze(self, event):
        """process event, return True (go to next module) or False (fail, go to next event)"""
        genParticles = Collection(event, "GenPart")
        leptons=[]
        neutrinos=[]
        photons=[]
        for particle  in genParticles :
          if ( (abs(particle.pdgId)==11 or abs(particle.pdgId==13)) and particle.status == 1) or \
               (abs(particle.pdgId)==15 and particle.statusFlags >> 1 & 1 and particle.statusFlags >> 13 & 1) : # isDecayed and LastCopy
            leptons.append(particle)
          if particle.pdgId == 22 and particle.status == 1 :
            photons.append(particle)
          if (abs(particle.pdgId)==12 or abs(particle.pdgId)==14 or abs(particle.pdgId)==16) and particle.status == 1 : 
            neutrinos.append(particle) 
        allParticles = leptons + neutrinos + photons
        for particle in allParticles:
          motherid = -9999
          motherstatus = -9999
          if particle.genPartIdxMother > 0:
            motherid = genParticles[particle.genPartIdxMother].pdgId
            motherstatus = genParticles[particle.genPartIdxMother].pdgId
          particle.MotherPID = motherid
          particle.MotherStatus = motherstatus
          particle.fromHardProcess = bool(particle.statusFlags >> 8 & 1)
          particle.isDirectHadronDecayProduct = bool(particle.statusFlags >> 6 & 1)
          particle.isDirectPromptTauDecayProduct = bool(particle.statusFlags >> 5 & 1)
          particle.isPrompt = bool(particle.statusFlags & 1)
          particle.isTauDecayProduct = bool(particle.statusFlags >> 3 & 1)
        leptons.sort(  key=self.sortkey, reverse=True)
        neutrinos.sort(key=self.sortkey, reverse=True)
        photons.sort(  key=self.sortkey, reverse=True)

        for particleType in self.particleTypes:
          if particleType == "leptonGen":
            vector = leptons
          elif particleType == "neutrinoGen":
            vector = neutrinos
          else:
            vector = photons  
          for branch in self.allQuantities:
            out = []
            for obj in vector:
              out.append(getattr(obj, branch))
            self.out.fillBranch(particleType+"_"+branch, out)  
            
        return True


# define modules using the syntax 'name = lambda : constructor' to avoid having them loaded when not needed

promptParticlesGenVarsProducer = lambda : PromptParticlesGenVarsProducer() 
 
