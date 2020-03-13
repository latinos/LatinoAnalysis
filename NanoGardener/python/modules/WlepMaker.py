import ROOT
import os
import re
import math
ROOT.PyConfig.IgnoreCommandLineOptions = True

from PhysicsTools.NanoAODTools.postprocessing.framework.eventloop import Module
from LatinoAnalysis.NanoGardener.data.WlepMaker_cfg import Wlep_br, Wlep_var
from LatinoAnalysis.NanoGardener.data.common_cfg import Type_dict
from LatinoAnalysis.NanoGardener.framework.BranchMapping import mappedOutputTree, mappedEvent

class WlepMaker(Module):
    '''                                                                                                                        
    put this file in LatinoAnalysis/NanoGardener/python/modules/                                                               
    Add extra variables to NANO tree                                                                                           
    '''
    def __init__(self, branch_map=''):
        
        self._branch_map = branch_map
        print('WlepMaker:')
        
    def beginJob(self):
        pass

    def endJob(self):
        pass

    def beginFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        self.initReaders(inputTree) # initReaders must be called in beginFile
        self.out = mappedOutputTree(wrappedOutputTree, mapname=self._branch_map)
        self.metCollections = {"Puppi":"PuppiMET"} # Name for branch and name of MET collection # "PF":"MET", 
        # New branches
        for MET in self.metCollections:
           for typ in Wlep_br:
              for var in Wlep_br[typ]:
                 if 'Wlep_' in var: self.out.branch("HM_"+var+"_"+MET, typ)

        #self.out.branch("IsWlepEvt", "I")
        self.out.branch("HM_Wlep_mt" , "F")

    def endFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        pass

    def initReaders(self,tree): # this function gets the pointers to Value and ArrayReaders and sets them in the C++ worker class                                                                                                                            
       
       self.wlep_var = {}
       self.lep_var = {}
       
       #self.met_var = {}

       self.lep_var['Lepton_pt']  = tree.arrayReader('Lepton_pt')
       self.lep_var['Lepton_eta'] = tree.arrayReader('Lepton_eta')
       self.lep_var['Lepton_phi'] = tree.arrayReader('Lepton_phi')

       
       #self.met_var['MET_pt']      = tree.valueReader('MET_pt')
       #self.met_var['MET_phi']     = tree.valueReader('MET_phi')


       #print "[jhchoi]type of self.lep_var['Lepton_phi'] = "+str(type(self.lep_var['Lepton_phi']))
       #print "[jhchoi]type of self.met_var['MET_phi'] = "+str(type(self.met_var['MET_phi']))
       #for br in tree.GetListOfBranches():
       #    bname = br.GetName()
       #    if re.match('\ALepton_', bname):       self.lep_var[bname] = tree.arrayReader(bname)
       #    if re.match('\AMET_',    bname):       self.met_var[bname] = tree.valueReader(bname)       
       #        #self.met_var[bname] = tree.arrayReader(bname)
       #self.nFatJet = tree.valueReader('nFatJet')
       self._ttreereaderversion = tree._ttreereaderversion # self._ttreereaderversion must be set AFTER all calls to tree.valueReader or tree.arrayReader

    def analyze(self, event):
       """process event, return True (go to next module) or False (fail, go to next event)"""

       event = mappedEvent(event, mapname=self._branch_map)

       if event._tree._ttreereaderversion > self._ttreereaderversion: # do this check at every event, as other modules might have read further branches
           self.initReaders(event._tree)
       # do NOT access other branches in python between the check/call to initReaders and the call to C++ worker code

       #--- Set vars

       ##### lepton selected at the Step stage, so it is 1 for now
       #IsWlepEvt = 1

       wlep_dict = {}
       for MET in self.metCollections:
           for v in Wlep_var:
               wlep_dict[v+"_"+MET] = 0
       
       
       
       lep_pt =self.lep_var['Lepton_pt'][0]
       lep_eta=self.lep_var['Lepton_eta'][0]
       lep_phi=self.lep_var['Lepton_phi'][0]
       lep_pz =lep_pt*math.sinh(lep_eta) ##pz = pt*sinh(eta)
       lep_E  =lep_pt*math.cosh(lep_eta) ## p = pt*cosh(eta)
       Wlep_mt = -9999.0


       for MET,METtype in self.metCollections.items():
           #met_pt=float(self.met_var['MET_pt'])
           #met_phi=float(self.met_var['MET_phi'])
           #met_pt  = event.PuppiMET_pt
           #met_phi = event.PuppiMET_phi
           met_pt  = getattr(event, METtype+'_pt')
           met_phi = getattr(event, METtype+'_phi')

           wlep_mass  = 80.4

           mu = ((wlep_mass)**2)/2 + lep_pt*met_pt*math.cos(met_phi-lep_phi)

           ##met_pz solution = met_pz_1 +-sqrt(met_pz_2)
           met_pz_1=mu*lep_pz/(lep_pt**2) 
           met_pz_2=(  mu*lep_pz/(lep_pt**2)  )**2 - ( (lep_E*met_pt)**2 - mu**2 )/(lep_pt**2)
           met_pz=0
           ##--complex number case
           if met_pz_2 < 0:
               met_pz = met_pz_1
           ##--real solution    
           else:
               sol1 = met_pz_1+math.sqrt(met_pz_2)
               sol2 = met_pz_1-math.sqrt(met_pz_2)
           
               if math.fabs(sol1) < math.fabs(sol2):
                   met_pz = sol1
               else:
                   met_pz = sol2



           wlep_px = lep_pt*math.cos(lep_phi) + met_pt*math.cos(met_phi)
           wlep_py = lep_pt*math.sin(lep_phi) + met_pt*math.sin(met_phi)
           wlep_pz = lep_pz + met_pz
           wlep_E  = lep_E  + math.sqrt(met_pz**2 + met_pt**2)



           v_wlep = ROOT.TLorentzVector()
           v_wlep.SetPxPyPzE(wlep_px, wlep_py, wlep_pz, wlep_E)
           wlep_dict['pt'+"_"+MET]   = v_wlep.Pt()
           wlep_dict['eta'+"_"+MET]  = v_wlep.Eta()
           wlep_dict['phi'+"_"+MET]  = v_wlep.Phi()
           wlep_dict['mass'+"_"+MET] = v_wlep.M()
           #wlep_dict['px'+"_"+MET] = v_wlep.Px()
           #wlep_dict['py'+"_"+MET] = v_wlep.Py()
           #wlep_dict['pz'+"_"+MET] = v_wlep.Pz()
           #wlep_dict['E'+"_"+MET] = v_wlep.E()
           Wlep_mt = math.sqrt( 2. * lep_pt * met_pt * ( 1. - math.cos (lep_phi - met_phi) ))



       #--- Fill branches                                                                                                     
                   
       for var in wlep_dict:
           self.out.fillBranch( 'HM_Wlep_' + var, wlep_dict[var])
           ##fillBranch(name,value)

       #self.out.fillBranch( 'IsWlepEvt', IsWlepEvt)
       self.out.fillBranch( 'HM_Wlep_mt', Wlep_mt)
       return True


# define modules using the syntax 'name = lambda : constructor' to avoid having them loaded when not needed                    

wlepMkr = lambda : WlepMaker()
