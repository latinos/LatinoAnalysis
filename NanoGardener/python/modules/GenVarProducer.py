#
#
#
#      ___|                  \ \     /            _)         |      |             
#     |       _ \  __ \       \ \   /  _` |   __|  |   _` |  __ \   |   _ \   __| 
#     |   |   __/  |   |       \ \ /  (   |  |     |  (   |  |   |  |   __/ \__ \ 
#    \____| \___| _|  _|        \_/  \__,_| _|    _| \__,_| _.__/  _| \___| ____/ 
#                                                                                 
#
#
#



import ROOT
ROOT.PyConfig.IgnoreCommandLineOptions = True

from PhysicsTools.NanoAODTools.postprocessing.framework.datamodel import Collection 
from PhysicsTools.NanoAODTools.postprocessing.framework.eventloop import Module


import os.path


class GenVarProducer(Module):
    def __init__(self):

        # change this part into correct path structure... 
        cmssw_base = os.getenv('CMSSW_BASE')
        try:
            ROOT.gROOT.LoadMacro(cmssw_base+'/src/LatinoAnalysis/Gardener/python/variables/GenVar.C+g')
        except RuntimeError:
            ROOT.gROOT.LoadMacro(cmssw_base+'/src/LatinoAnalysis/Gardener/python/variables/GenVar.C++g')


      
    def beginJob(self):
        pass

    def endJob(self):
        pass

    def beginFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        self.out = wrappedOutputTree
        self.newbranches = [
           'gen_ptllmet',
           'gen_ptll',
           'gen_mll',
           'gen_llchannel',
           'gen_mlvlv',
           'lhe_mlvlv',
           'lhe_mWp',
           'lhe_mWm'
          ]
        
        for nameBranches in self.newbranches :
          self.out.branch(nameBranches  ,  "F");

    def endFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        pass

    def analyze(self, event):
        """process event, return True (go to next module) or False (fail, go to next event)"""

        genParticles = Collection(event, "GenPart")
        
        # Gen
        leptonGen_pt      = ROOT.std.vector(float)(0)
        leptonGen_eta     = ROOT.std.vector(float)(0)
        leptonGen_phi     = ROOT.std.vector(float)(0)
        leptonGen_pid     = ROOT.std.vector(float)(0)
        leptonGen_status        = ROOT.std.vector(float)(0)
        leptonGen_isPrompt      = ROOT.std.vector(float)(0)
        leptonGen_MotherPID     = ROOT.std.vector(float)(0)
        leptonGen_MotherStatus  = ROOT.std.vector(float)(0)

        partonGen_pt      = ROOT.std.vector(float)(0)
        partonGen_eta     = ROOT.std.vector(float)(0)
        partonGen_phi     = ROOT.std.vector(float)(0)
        partonGen_pid     = ROOT.std.vector(float)(0)

        # LHE
        leptonLHEGen_pt      = ROOT.std.vector(float)(0)
        leptonLHEGen_eta     = ROOT.std.vector(float)(0)
        leptonLHEGen_phi     = ROOT.std.vector(float)(0)
        leptonLHEGen_pid     = ROOT.std.vector(float)(0)

        neutrinoLHEGen_pt      = ROOT.std.vector(float)(0)
        neutrinoLHEGen_eta     = ROOT.std.vector(float)(0)
        neutrinoLHEGen_phi     = ROOT.std.vector(float)(0)
        neutrinoLHEGen_pid     = ROOT.std.vector(float)(0)
        
        #GenPart_statusFlags     Int_t   gen status flags stored bitwise, bits are: 0 : isPrompt, 1 : isDecayedLeptonHadron, 2 : isTauDecayProduct, 3 : isPromptTauDecayProduct, 4 : isDirectTauDecayProduct, 5 : isDirectPromptTauDecayProduct, 6 : isDirectHadronDecayProduct, 7 : isHardProcess, 8 : fromHardProcess, 9 : isHardProcessTauDecayProduct, 10 : isDirectHardProcessTauDecayProduct, 11 : fromHardProcessBeforeFSR, 12 : isFirstCopy, 13 : isLastCopy, 14 : isLastCopyBeforeFSR,
        
        #
        # GEN 
        #
        noMother = False
        for particle  in genParticles :
          #
          # L1 = e-(11) OR mu-(13) OR tau-(15)
          #
          # from SkimEvent.cc
          #
          #     if( !((type == 11 || type == 13) && genParticles_[gp]->status()==1 ) && !(type == 15 && genParticles_[gp]->isPromptDecayed() ) )
          #
          # ele or mu --> isPrompt (or isDirectPromptTauDecayProduct)
          # tau       --> isPrompt
          #
          #
          #    if (( (abs(particle.pdgId) == 11) or (abs(particle.pdgId) == 13)  or (abs(particle.pdgId) == 15)) and
          #        #( ((abs(particle.pdgId) == 11 or abs(particle.pdgId) == 13) and ( (particle.statusFlags >> 0 & 1) or (particle.statusFlags >> 5 & 1) )) or  # isDirectPromptTauDecayProduct FIXME sure?
          #        ( ((abs(particle.pdgId) == 11 or abs(particle.pdgId) == 13) and ( particle.statusFlags >> 0 & 1 )) or
          #          ((abs(particle.pdgId) == 15)  and ( (particle.statusFlags >> 0 & 1)) ) )   # isPrompt FIXME sure?
          #        ) :    
          #
          #
          # gen leptons only electrons and muons (or ele/mu from prompt tau decay)
          #
          if (( (abs(particle.pdgId) == 11) or (abs(particle.pdgId) == 13) ) and
              ( ( particle.statusFlags >> 0 & 1 )  or  ( particle.statusFlags >> 2 & 1 )   or  ( particle.statusFlags >> 3 & 1 )   or  ( particle.statusFlags >> 4 & 1 ) ) ) :
            leptonGen_pt. push_back(particle.pt)
            leptonGen_eta.push_back(particle.eta)
            leptonGen_phi.push_back(particle.phi)
            leptonGen_pid.push_back(particle.pdgId)
            leptonGen_status.push_back(particle.status)
            leptonGen_isPrompt.push_back( (particle.statusFlags >> 0 & 1) )  
            if particle.genPartIdxMother > -1 :
              leptonGen_MotherPID.push_back( genParticles[particle.genPartIdxMother].pdgId )
              leptonGen_MotherStatus.push_back( genParticles[particle.genPartIdxMother].status )
            else :
              noMother = True

          # parton
          #
          #  if (type < 1) continue;
          #  if (type > 8 && type != 21) continue;
          #  if (!genParticles_[gp]->isHardProcess() && !genParticles_[gp]->statusFlags().isPrompt()) continue;
          #  if (!genParticles_[gp]->isHardProcess() && type == 21) continue;
          #  if (!genParticles_[gp]->isHardProcess() && type  <  5) continue;
          #

          elif ( ( (abs(particle.pdgId) == 21) or (abs(particle.pdgId) <= 8) ) and
                ( (particle.statusFlags >> 7 & 1) or  (particle.statusFlags >> 0 & 1) ) and
                not ( (abs(particle.pdgId) == 21) and not(particle.statusFlags >> 7 & 1) ) and
                not ( (abs(particle.pdgId) < 5)   and not(particle.statusFlags >> 7 & 1) )
                ):    
            partonGen_pt. push_back(particle.pt)
            partonGen_eta.push_back(particle.eta)
            partonGen_phi.push_back(particle.phi)
            partonGen_pid.push_back(particle.pdgId)


        #
        # LHE 
        #
    
        # FIXME missing LHE part
          
          

        GenVar = ROOT.GenVar()
       
        # if no gen information, don't fill the variable
        if not noMother :
          GenVar.setLeptons(leptonGen_pt, leptonGen_eta, leptonGen_phi,
                            leptonGen_pid,
                            leptonGen_status,
                            leptonGen_isPrompt,
                            leptonGen_MotherPID,
                            leptonGen_MotherStatus
                            )
        else : 
          GenVar.setLeptons(leptonGen_pt, leptonGen_eta, leptonGen_phi, leptonGen_pid)
        
          GenVar.setJets   (partonGen_pt, partonGen_eta, partonGen_phi, partonGen_pid)

        # add GenMET information
        GenVar.setMET(event.GenMET_pt, event.GenMET_phi)

        # if LHE information is available
        #if hasattr(itree, 'std_vector_LHElepton_pt') :
          #GenVar.setLHELeptons  (itree.std_vector_LHElepton_pt, itree.std_vector_LHElepton_eta, itree.std_vector_LHElepton_phi, itree.std_vector_LHElepton_id)
          #GenVar.setLHENeutrinos(itree.std_vector_LHEneutrino_pt, itree.std_vector_LHEneutrino_eta, itree.std_vector_LHEneutrino_phi, itree.std_vector_LHEneutrino_id)


        # now fill the variables like "mll", "dphill", ...
            
        for nameBranches in self.newbranches :
          self.out.fillBranch(nameBranches  ,  getattr(GenVar, nameBranches)());


        return True







