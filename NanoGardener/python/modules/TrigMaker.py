import ROOT
import os
import re
import math
ROOT.PyConfig.IgnoreCommandLineOptions = True

from copy import deepcopy
from PhysicsTools.NanoAODTools.postprocessing.framework.eventloop import Module
from LatinoAnalysis.NanoGardener.data.TrigMaker_cfg import NewVar_MC_dict, NewVar_DATA_dict
from LatinoAnalysis.NanoGardener.data.TrigMaker_cfg import Trigger

from PhysicsTools.NanoAODTools.postprocessing.framework.datamodel import Collection

from LatinoAnalysis.NanoGardener.framework.BranchMapping import mappedOutputTree, mappedEvent

class TrigMaker(Module):
    '''
    Trigger Maker module MC,
    ''' 

    def __init__(self, cmssw = 'Full2016', isData = False, keepRunP = False, cfg_path = 'LatinoAnalysis/NanoGardener/python/data/TrigMaker_cfg.py', seeded = False, branch_map=''):
        self.cmssw = cmssw
        self.isData = isData
        self.keepRunP = keepRunP
        self.seeded = seeded
        self.firstEvent = True
 
        self.mu_maxPt = 200
        self.mu_minPt = 10
        self.mu_maxEta = 2.4
        self.mu_minEta = -2.4

        self.el_maxPt = 100
        self.el_minPt = 10
        self.el_maxEta = 2.5
        self.el_minEta = -2.5
        self.cfg_path = cfg_path 

        cmssw_base = os.getenv('CMSSW_BASE')
        var = {}
        execfile(cmssw_base+'/src/'+cfg_path, var)
        if self.isData:
           self.typeStr = 'DATA'
           self.NewVar = var['NewVar_DATA_dict']
        else:
           self.NewVar = var['NewVar_MC_dict']
           self.typeStr = 'MC'

        self.Trigger = var['Trigger']

        print('TrigMaker: CMSSW = ' + self.cmssw + ', isData = ' + str(self.isData) + ', keepRunPeriod = ' + str(self.keepRunP))
        if cfg_path != 'LatinoAnalysis/NanoGardener/python/data/TrigMaker_cfg.py':
            print('TrigMaker: loaded trigger configuration from ' + cfg_path)

        self._branch_map = branch_map
 
    def beginJob(self): 
        pass

    def endJob(self):
        pass

    def beginFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        self.initReaders() # initReaders must be called in beginFile
        self.out = mappedOutputTree(wrappedOutputTree, mapname=self._branch_map)
        
        if self.keepRunP:
           # Check if input tree indeed contains run_period
           #isThere = False
           #for br in wrappedOutputTree.GetListOfBranches():
           #   if br.GetName() == 'run_period': isThere = True
           #if not isThere: print("TrigMaker WARNING: Input tree does not contain the 'run_period' branch, while 'keepRunP' is True.")
           #else: 
           try: self.NewVar['I'].remove('run_period')
           except: pass
 
        for typ in self.NewVar:
           for name in self.NewVar[typ]:
              if 'TriggerEmulator' in name: self.out.branch(name, typ, 6)
              else:                         self.out.branch(name, typ)

    def endFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        pass

    def initReaders(self): # this function gets the pointers to Value and ArrayReaders and sets them in the C++ worker class
        # Specific trigger dicts
        cmssw_base = os.getenv('CMSSW_BASE')
        self.TM_trig    = {}
        self.TM_LegEffData  = {}
        self.TM_LegEffMC  = {}
        self.TM_DZEff   = {}
        self.TM_GlEff = {}
        #self.TM_trkSFMu = {}
        self.TM_runInt  = {}
        for RunP in self.Trigger[self.cmssw]:
           #self.TM_trkSFMu[RunP] = deepcopy(self.Trigger[self.cmssw][RunP]['trkSFMu'])
           self.TM_trig[RunP]    = {}
           self.TM_LegEffData[RunP]  = {}
           self.TM_LegEffMC[RunP]  = {}
           self.TM_DZEff[RunP]   = {}
           self.TM_GlEff[RunP] = {}
           self.TM_runInt[RunP]  = {'b': self.Trigger[self.cmssw][RunP]['begin'], 'e': self.Trigger[self.cmssw][RunP]['end']}
           for Tname in self.Trigger[self.cmssw][RunP][self.typeStr]:
              self.TM_trig[RunP][Tname] = []
              for HLT in self.Trigger[self.cmssw][RunP][self.typeStr][Tname]:
                 if HLT is not None: self.TM_trig[RunP][Tname].append('event.'+HLT)
                 else: self.TM_trig[RunP][Tname].append('False')

           for Tname in self.Trigger[self.cmssw][RunP]['LegEffData']:
              if self.Trigger[self.cmssw][RunP]['LegEffData'][Tname] is not None:
                  temp_file = open(cmssw_base + '/src/LatinoAnalysis/NanoGardener/python/data/trigger/' + self.Trigger[self.cmssw][RunP]['LegEffData'][Tname], 'r')
              else:
                  temp_file = open(cmssw_base + '/src/LatinoAnalysis/NanoGardener/python/data/trigger/dummy_trigger_efficiency.txt', 'r')
              self.TM_LegEffData[RunP][Tname] = [line.rstrip().split() for line in temp_file if '#' not in line]
              temp_file.close()

           for Tname in self.Trigger[self.cmssw][RunP]['LegEffMC']:
              if self.Trigger[self.cmssw][RunP]['LegEffMC'][Tname] is not None:
                  temp_file = open(cmssw_base + '/src/LatinoAnalysis/NanoGardener/python/data/trigger/' + self.Trigger[self.cmssw][RunP]['LegEffMC'][Tname], 'r')
              else:
                  temp_file = open(cmssw_base + '/src/LatinoAnalysis/NanoGardener/python/data/trigger/dummy_trigger_efficiency.txt', 'r')
              self.TM_LegEffMC[RunP][Tname] = [line.rstrip().split() for line in temp_file if '#' not in line]
              temp_file.close()

           for Tname in self.Trigger[self.cmssw][RunP]['DZEff']:
              Key = list(self.Trigger[self.cmssw][RunP]['DZEff'][Tname].keys())[0]
              self.TM_DZEff[RunP][Tname] = {}
              self.TM_DZEff[RunP][Tname]['type'] = Key  
              if Key == 'value' :
                  self.TM_DZEff[RunP][Tname]['vals'] = self.Trigger[self.cmssw][RunP]['DZEff'][Tname]['value']
              else: 
                  temp_file = open(cmssw_base + '/src/LatinoAnalysis/NanoGardener/python/data/trigger/' + self.Trigger[self.cmssw][RunP]['DZEff'][Tname][Key],'r')
                  self.TM_DZEff[RunP][Tname]['vals'] = [line.rstrip().split() for line in temp_file if '#' not in line]
                  temp_file.close()

           for Tname in self.Trigger[self.cmssw][RunP]['GlEff']:
              self.TM_GlEff[RunP][Tname] = [] 
              self.TM_GlEff[RunP][Tname].append(self.Trigger[self.cmssw][RunP]['GlEff'][Tname][0])
              self.TM_GlEff[RunP][Tname].append(self.Trigger[self.cmssw][RunP]['GlEff'][Tname][0]-self.Trigger[self.cmssw][RunP]['GlEff'][Tname][1])
              self.TM_GlEff[RunP][Tname].append(min(1.,self.Trigger[self.cmssw][RunP]['GlEff'][Tname][0]+self.Trigger[self.cmssw][RunP]['GlEff'][Tname][1]))
              # In the following we append the same content of the previous 2 lines, it is just a trick to handle stat and syst components later on
              self.TM_GlEff[RunP][Tname].append(self.Trigger[self.cmssw][RunP]['GlEff'][Tname][0]-self.Trigger[self.cmssw][RunP]['GlEff'][Tname][1])
              self.TM_GlEff[RunP][Tname].append(min(1.,self.Trigger[self.cmssw][RunP]['GlEff'][Tname][0]+self.Trigger[self.cmssw][RunP]['GlEff'][Tname][1]))
              self.TM_GlEff[RunP][Tname].append(self.Trigger[self.cmssw][RunP]['GlEff'][Tname][0]-self.Trigger[self.cmssw][RunP]['GlEff'][Tname][1])
              self.TM_GlEff[RunP][Tname].append(min(1.,self.Trigger[self.cmssw][RunP]['GlEff'][Tname][0]+self.Trigger[self.cmssw][RunP]['GlEff'][Tname][1]))



        # Set some run/event specific var
        self.total_lum = 0.
        self.EMTFbug = {}
        for RunP in self.Trigger[self.cmssw]:
           self.total_lum += self.Trigger[self.cmssw][RunP]['lumi']
           self.EMTFbug[RunP] = self.Trigger[self.cmssw][RunP]['EMTFBug']
        
        self.RunFrac = [0.]
        for RunP in self.Trigger[self.cmssw]:
           self.RunFrac.append(self.RunFrac[-1] + self.Trigger[self.cmssw][RunP]['lumi']/self.total_lum)
       
        if self.keepRunP: self.run_p = 'event.run_period'
 
        self.event = 'event.event'
        self.run = 'event.run'

    #_____Help functions
    def _run_period(self, run, event_seed=None):
        if self.isData:
           for RunP in self.TM_runInt:
              if run >= self.TM_runInt[RunP]['b'] and run <= self.TM_runInt[RunP]['e']: return RunP
        else: 
         toss_a_coin = get_rndm(event_seed)
         for iPeriod in range(1,len(self.RunFrac)) :
           if toss_a_coin >= self.RunFrac[iPeriod-1] and toss_a_coin < self.RunFrac[iPeriod]:
              return iPeriod
           if toss_a_coin == 1.0:
              return len(self.RunFrac)-1
        print "Run Period undefined"
        return -1 

    def _get_LegEff(self, pt, eta, run_p, trig_name, isdata):
        legEffs = self.TM_LegEffData[run_p][trig_name] if isdata else self.TM_LegEffMC[run_p][trig_name]
        for eff_l in legEffs:
           if len(eff_l) > 5:
              if (eta >= float(eff_l[0]) and eta <= float(eff_l[1]) and         # the "=" in both directions is only used by the overflow bin
                  pt  >= float(eff_l[2]) and pt  <= float(eff_l[3]) ) :         # in other cases the set is (min, max]
                 
                 eff = float(eff_l[4])
                 eff_stat_u = min(1.0, float(eff_l[4]) + float(eff_l[6]))
                 eff_stat_d = max(0.0, float(eff_l[4]) - float(eff_l[5]))
                 eff_syst_u = min(1.0, float(eff_l[4]) + float(eff_l[8]))
                 eff_syst_d = max(0.0, float(eff_l[4]) - float(eff_l[7]))

                 eff_d = math.sqrt(eff_stat_d**2 + eff_syst_d**2)
                 eff_u = math.sqrt(eff_stat_u**2 + eff_syst_u**2)

                 return [eff, eff_d, eff_u, eff_stat_d, eff_stat_u, eff_syst_d, eff_syst_u]
           elif len(eff_l) > 2:
              raise IOError('Unexpected info in /LatinoAnalysis/NanoGardener/python/data/trigger/' + self.Trigger[self.cmssw][run_p]['LegEff'][trig_name] +\
                            ': ' + eff_l + ' not enough inputs?') 
        return [0. , 0., 0.]
        
    def _over_under(self, pdgId, pt, eta):
        if abs(pdgId) == 11:
           return max(self.el_minPt, min(self.el_maxPt, pt)), max(self.el_minEta, min(self.el_maxEta, eta))
        elif abs(pdgId) == 13:
           return max(self.mu_minPt, min(self.mu_maxPt, pt)), max(self.mu_minEta, min(self.mu_maxEta, eta))
        else:
           raise ValueError('_over_under can only operate on leptons, pdgI = ' + str(pdgId) + ', pt = ' + str(pt) + ', eta = ' + str(eta))

    def _get_SF(self, eff_data, eff_mc):
        return eff_data / eff_mc if eff_mc!=0. else 0.

    def _get_SFUnc(self, eff_data, eff_mc):

        eff_data_nom = eff_data[0]
        # stat up and down should be the same, but let's propgate them as they are in the input files
        eff_data_stat_d = eff_data[3]
        eff_data_stat_u = eff_data[4]
        eff_data_syst_d = eff_data[5]
        eff_data_syst_u = eff_data[6]

        eff_mc_nom = eff_mc[0]
        # stat up and down should be the same, but let's propgate them as they are in the input files
        eff_mc_stat_d = eff_mc[3]
        eff_mc_stat_u = eff_mc[4]
        eff_mc_syst_d = eff_mc[5]
        eff_mc_syst_u = eff_mc[6]

        if eff_mc_nom==0. or eff_data_nom==0.: return (0,0)
 
        SF_stat_d = math.sqrt( (abs(eff_data_stat_d-eff_data_nom)/eff_data_nom)**2 + (abs(eff_mc_stat_d-eff_mc_nom)/eff_mc_nom)**2 )*eff_data_nom/eff_mc_nom
        SF_stat_u = math.sqrt( (abs(eff_data_stat_u-eff_data_nom)/eff_data_nom)**2 + (abs(eff_mc_stat_u-eff_mc_nom)/eff_mc_nom)**2 )*eff_data_nom/eff_mc_nom

        SF_syst_d = eff_data_syst_d/eff_mc_syst_d if eff_mc_syst_d!=0 else 0
        SF_syst_u = eff_data_syst_u/eff_mc_syst_u if eff_mc_syst_u!=0 else 0

        # return (down, up) uncertainties
        return ( math.sqrt( SF_stat_d**2 + SF_syst_d**2 ),
                 math.sqrt( SF_stat_u**2 + SF_syst_u**2 ) 
                )
    

    def _get_DZEff(self,run_p,trigName,nvtxIn,pt1In,pt2In):
      DZeff = 1. 
      nvtx = nvtxIn
      pt1 = pt1In
      pt2 = pt2In
      if    self.TM_DZEff[run_p][trigName]['type'] == 'value' : 
         DZeff      = self.TM_DZEff[run_p][trigName]['vals'][0]
         DZeff_err  = self.TM_DZEff[run_p][trigName]['vals'][1]
      elif  self.TM_DZEff[run_p][trigName]['type'] == 'nvtx'  :
        if nvtx >= 70 : nvtx = 69
        for eff_dz in self.TM_DZEff[run_p][trigName]['vals'] :
          if nvtx >= float(eff_dz[0]) and nvtx < float(eff_dz[1]) : 
            DZeff     = float(eff_dz[2])
            DZeff_err = float(eff_dz[3])
      elif  self.TM_DZEff[run_p][trigName]['type'] == 'pt1:pt2' :
        if pt1 >= 100. : pt1 = 99.9
        if pt2 >= 100. : pt2 = 99.9
        for eff_dz in self.TM_DZEff[run_p][trigName]['vals'] :
          if pt1 >= float(eff_dz[0]) and pt1 < float(eff_dz[1]) and pt2 >= float(eff_dz[2]) and pt2 < float(eff_dz[3]) : 
            DZeff     = float(eff_dz[4])    
            DZeff_err = float(eff_dz[5])    

      #print run_p,trigName,nvtx,pt1,pt2,DZeff,DZeff_err,DZeff-DZeff_err,min(1.,DZeff+DZeff_err)
      return DZeff,DZeff-DZeff_err,min(1.,DZeff+DZeff_err)

    def _pair_eff(self, pdgId1, pt1, eta1, pdgId2, pt2, eta2, nvtx, run_p):
        '''
        Look op leg efficiencies and apply 5% sys for Electron and tracker SF for Muon
        '''
        
        eff_dz_nom = 1.
        eff_dz_do = 1.
        eff_dz_up = 1.
        eff_gl = []
        # Leg_map = ['singA', 'singB', 'leadA', 'leadB', 'trailA', 'trailB'] 
        # With A the lepton with the higer pt, B the one with the lower pt
        # Lead is the tracked lepton and trail is the trailing 
        Leg_names = []
        if abs(pdgId1) == 11 and abs(pdgId2) == 11:
           Leg_names = ['SingleEle', 'SingleEle', 'DoubleEleLegHigPt', 'DoubleEleLegHigPt', 'DoubleEleLegLowPt', 'DoubleEleLegLowPt']
           eff_dz_nom,eff_dz_do,eff_dz_up = self._get_DZEff(run_p,'DoubleEle',nvtx,pt1,pt2)
           eff_gl.append( self.TM_GlEff[run_p]['SingleEle'] )
           eff_gl.append( self.TM_GlEff[run_p]['SingleEle'] )
           eff_gl.append( self.TM_GlEff[run_p]['DoubleEle'] )
        elif abs(pdgId1) == 13 and abs(pdgId2) == 13:
           Leg_names = ['SingleMu', 'SingleMu', 'DoubleMuLegHigPt', 'DoubleMuLegHigPt', 'DoubleMuLegLowPt', 'DoubleMuLegLowPt']
           eff_dz_nom,eff_dz_do,eff_dz_up = self._get_DZEff(run_p,'DoubleMu',nvtx,pt1,pt2)
           eff_gl.append( self.TM_GlEff[run_p]['SingleMu'] )
           eff_gl.append( self.TM_GlEff[run_p]['SingleMu'] )
           eff_gl.append( self.TM_GlEff[run_p]['DoubleMu'] )
        elif abs(pdgId1) == 11 and abs(pdgId2) == 13:
           Leg_names = ['SingleEle', 'SingleMu', 'EleMuLegHigPt', 'MuEleLegHigPt', 'MuEleLegLowPt', 'EleMuLegLowPt']
           eff_dz_nom,eff_dz_do,eff_dz_up = self._get_DZEff(run_p,'EleMu',nvtx,pt1,pt2)
           eff_gl.append( self.TM_GlEff[run_p]['SingleEle'] )
           eff_gl.append( self.TM_GlEff[run_p]['SingleMu'] )
           eff_gl.append( self.TM_GlEff[run_p]['EleMu'] )
        else:
           Leg_names = ['SingleMu', 'SingleEle', 'MuEleLegHigPt', 'EleMuLegHigPt', 'EleMuLegLowPt', 'MuEleLegLowPt']
           eff_dz_nom,eff_dz_do,eff_dz_up = self._get_DZEff(run_p,'MuEle',nvtx,pt1,pt2)
           eff_gl.append( self.TM_GlEff[run_p]['SingleMu'] )
           eff_gl.append( self.TM_GlEff[run_p]['SingleEle'] )
           eff_gl.append( self.TM_GlEff[run_p]['MuEle'] )

        eff_dz = []
        eff_dz.append(eff_dz_nom)       
        eff_dz.append(eff_dz_do)       
        eff_dz.append(eff_dz_up)       
        # In the following we append the same content of the previous 2 lines, it is just a trick to handle stat and syst components later on
        eff_dz.append(eff_dz_do)
        eff_dz.append(eff_dz_up)
        eff_dz.append(eff_dz_do)
        eff_dz.append(eff_dz_up)
 
        # eff_map = ['singA', 'singB', 'leadA', 'leadB', 'trailA', 'trailB']
        effData = []
        effMC = []
        for iLeg in range(len(Leg_names)):
           isdata=True
           effData.append(self._get_LegEff(eval('pt'+str(iLeg%2 + 1)), eval('eta'+str(iLeg%2 + 1)), run_p, Leg_names[iLeg], isdata))
           isdata=False
           effMC.append(self._get_LegEff(eval('pt'+str(iLeg%2 + 1)), eval('eta'+str(iLeg%2 + 1)), run_p, Leg_names[iLeg], isdata))
         
           # Muon tracker SF
           #if abs(pdgId1) == 13 and not iLeg%2:
           #   eff[iLeg] = [a*b for a,b in zip(eff[iLeg], self.TM_trkSFMu[run_p])] 
           #if abs(pdgId2) == 13 and iLeg%2:
           #   eff[iLeg] = [a*b for a,b in zip(eff[iLeg], self.TM_trkSFMu[run_p])] 
                
        return effData, effMC, eff_dz , eff_gl

    def _get_w(self, pdgId1, pt1, eta1, pdgId2, pt2, eta2, nvtx, run_p, event_seed=None):
         
        pt1, eta1 = self._over_under(pdgId1, pt1, eta1)
        pt2, eta2 = self._over_under(pdgId2, pt2, eta2)
      
        effData, effMC, eff_dz , eff_gl = self._pair_eff(pdgId1, pt1, eta1, pdgId2, pt2, eta2, nvtx, run_p)
        #eff_map = ['SingleEle', 'SingleMu', 'EleMuLegHigPt', 'MuEleLegHigPt', 'MuEleLegLowPt', 'EleMuLegLowPt']

        # nom, tot_d, tot_u, stat_d, stat_u, syst_d, syst_u
        effData_dbl = [0., 0., 0., 0., 0., 0., 0.]
        effData_sgl = [0., 0., 0., 0., 0., 0., 0.]
        effData_evt = [0., 0., 0., 0., 0., 0., 0.]
        effMC_dbl = [0., 0., 0., 0., 0., 0., 0.]
        effMC_sgl = [0., 0., 0., 0., 0., 0., 0.]
        effMC_evt = [0., 0., 0., 0., 0., 0., 0.]
        # SFnom, SF_d, SF_u
        SF_evt = [0., 0., 0.]

        for i in range(7): 
           effData_dbl[i] = max( (effData[4][i]*effData[3][i] + effData[2][i]*effData[5][i] - effData[3][i]*effData[2][i])*eff_gl[2][i]*eff_dz[i], 0.0001 )
           effData_sgl[i] =  effData[0][i]*eff_gl[0][i]+effData[1][i]*eff_gl[1][i]-effData[0][i]*effData[1][i]*eff_gl[0][i]*eff_gl[1][i]
           effData_evt[i] = effData_dbl[i] + effData_sgl[i] - effData[5][i]*eff_gl[2][i]*effData[0][i]*eff_gl[0][i] - effData[4][i]*eff_gl[2][i]*effData[1][i]*eff_gl[1][i]*( 1 - effData[5][i]*eff_gl[2][i]*effData[0][i]*eff_gl[0][i]/effData_dbl[i] )

           effMC_dbl[i] = max( (effMC[4][i]*effMC[3][i] + effMC[2][i]*effMC[5][i] - effMC[3][i]*effMC[2][i])*eff_gl[2][i]*eff_dz[i], 0.0001 )
           effMC_sgl[i] =  effMC[0][i]*eff_gl[0][i]+effMC[1][i]*eff_gl[1][i]-effMC[0][i]*effMC[1][i]*eff_gl[0][i]*eff_gl[1][i]
           effMC_evt[i] = effMC_dbl[i] + effMC_sgl[i] - effMC[5][i]*eff_gl[2][i]*effMC[0][i]*eff_gl[0][i] - effMC[4][i]*eff_gl[2][i]*effMC[1][i]*eff_gl[1][i]*( 1 - effMC[5][i]*eff_gl[2][i]*effMC[0][i]*eff_gl[0][i]/effMC_dbl[i] )

        SF_evt[0] = self._get_SF(effData_evt[0] , effMC_evt[0])
        SF_evt[1] = self._get_SFUnc(effData_evt, effMC_evt)[0]
        SF_evt[2] = self._get_SFUnc(effData_evt, effMC_evt)[1]


        # More specific event efficiencies (stored in a vector hence _v)
        # eff_evt_v_map = ['sinEl', 'sinMu', 'doubleEl', 'doubleMu', 'ElMu']
        effData_evt_v = [0., 0., 0., 0., 0.]
        effMC_evt_v = [0., 0., 0., 0., 0.]
        SF_evt_v = [0., 0., 0., 0., 0.]
        SF_evt_v_d = [0., 0., 0., 0., 0.]
        SF_evt_v_u = [0., 0., 0., 0., 0.]
        effs_data = [0., 0., 0., 0., 0., 0., 0.]
        effs_mc = [0., 0., 0., 0., 0., 0., 0.]

        if abs(pdgId1) == 11 and abs(pdgId2) == 11:
           effData_evt_v[0] = effData[0][0]*eff_gl[0][0] + (1 - effData[0][0]*eff_gl[0][0])*effData[1][0]*eff_gl[1][0]
           effMC_evt_v[0] = effMC[0][0]*eff_gl[0][0] + (1 - effMC[0][0]*eff_gl[0][0])*effMC[1][0]*eff_gl[1][0]
           SF_evt_v[0] = self._get_SF(effData_evt_v[0] , effMC_evt_v[0])
           effs_data[0] = effData_evt_v[0]
           effs_mc[0] = effMC_evt_v[0]
           for i in range(1,7):
             effs_data[i] = effData[0][i]*eff_gl[0][i] + (1 - effData[0][i]*eff_gl[0][i])*effData[1][i]*eff_gl[1][i]
             effs_mc[i] = effMC[0][i]*eff_gl[0][i] + (1 - effMC[0][i]*eff_gl[0][i])*effMC[1][i]*eff_gl[1][i]

           SF_evt_v_d[0] = self._get_SFUnc(effs_data, effs_mc)[0]
           SF_evt_v_u[0] = self._get_SFUnc(effs_data, effs_mc)[1]

           effData_evt_v[2] = (effData[4][0]*effData[3][0] + effData[2][0]*effData[5][0] - effData[3][0]*effData[2][0])*eff_gl[2][0]*eff_dz[0]
           effMC_evt_v[2] = (effMC[4][0]*effMC[3][0] + effMC[2][0]*effMC[5][0] - effMC[3][0]*effMC[2][0])*eff_gl[2][0]*eff_dz[0]
           SF_evt_v[2] = self._get_SF(effData_evt_v[2] , effMC_evt_v[2])
           effs_data[0] = effData_evt_v[2]
           effs_mc[0] = effMC_evt_v[2]
           for i in range(1,7):
             effs_data[i] = (effData[4][i]*effData[3][i] + effData[2][i]*effData[5][i] - effData[3][i]*effData[2][i])*eff_gl[2][i]*eff_dz[i] 
             effs_mc[i] = (effMC[4][i]*effMC[3][i] + effMC[2][i]*effMC[5][i] - effMC[3][i]*effMC[2][i])*eff_gl[2][i]*eff_dz[i] 

           SF_evt_v_d[2] = self._get_SFUnc(effs_data, effs_mc)[0]
           SF_evt_v_u[2] = self._get_SFUnc(effs_data, effs_mc)[1]

 

        elif abs(pdgId1) == 13 and abs(pdgId2) == 13:
           effData_evt_v[1] = effData[0][0]*eff_gl[0][0] + (1 - effData[0][0]*eff_gl[0][0])*effData[1][0]*eff_gl[1][0]
           effMC_evt_v[1] = effMC[0][0]*eff_gl[0][0] + (1 - effMC[0][0]*eff_gl[0][0])*effMC[1][0]*eff_gl[1][0]
           SF_evt_v[1] = self._get_SF(effData_evt_v[1] , effMC_evt_v[1])
           effs_data[0] = effData_evt_v[1]
           effs_mc[0] = effMC_evt_v[1]
           for i in range(1,7):
               effs_data[i] = effData[0][i]*eff_gl[0][i] + (1 - effData[0][0]*eff_gl[0][i])*effData[1][i]*eff_gl[1][i]
               effs_mc[i] = effMC[0][i]*eff_gl[0][i] + (1 - effMC[0][i]*eff_gl[0][i])*effMC[1][i]*eff_gl[1][i]

           SF_evt_v_d[1] = self._get_SFUnc(effs_data, effs_mc)[0]
           SF_evt_v_u[1] = self._get_SFUnc(effs_data, effs_mc)[1] 


           effData_evt_v[3] = (effData[4][0]*effData[3][0] + effData[2][0]*effData[5][0] - effData[3][0]*effData[2][0])*eff_gl[2][0]*eff_dz[0]
           effMC_evt_v[3] = (effMC[4][0]*effMC[3][0] + effMC[2][0]*effMC[5][0] - effMC[3][0]*effMC[2][0])*eff_gl[2][0]*eff_dz[0]
           SF_evt_v[3] = self._get_SF(effData_evt_v[3] , effMC_evt_v[3])
           effs_data[0] = effData_evt_v[3]
           effs_mc[0] = effMC_evt_v[3]
           for i in range(1,7):
               effs_data[i] = (effData[4][i]*effData[3][i] + effData[2][i]*effData[5][i] - effData[3][i]*effData[2][i])*eff_gl[2][i]*eff_dz[i]
               effs_mc[i] = (effMC[4][i]*effMC[3][i] + effMC[2][i]*effMC[5][i] - effMC[3][i]*effMC[2][i])*eff_gl[2][i]*eff_dz[i]

           SF_evt_v_d[3] = self._get_SFUnc(effs_data, effs_mc)[0]
           SF_evt_v_u[3] = self._get_SFUnc(effs_data, effs_mc)[1]


        elif abs(pdgId1) == 11 and abs(pdgId2) == 13:
           effData_evt_v[0] = effData[0][0]*eff_gl[0][0]
           effMC_evt_v[0] = effMC[0][0]*eff_gl[0][0]
           SF_evt_v[0] = self._get_SF(effData_evt_v[0] , effMC_evt_v[0])
           effs_data[0] = effData_evt_v[0]
           effs_mc[0] = effMC_evt_v[0]
           for i in range(1,7):
               effs_data[i] = effData[0][i]*eff_gl[0][i]
               effs_mc[i] = effMC[0][i]*eff_gl[0][i]

           SF_evt_v_d[0] = self._get_SFUnc(effs_data, effs_mc)[0]
           SF_evt_v_u[0] = self._get_SFUnc(effs_data, effs_mc)[1]

           effData_evt_v[1] = effData[1][0]*eff_gl[1][0]
           effMC_evt_v[1] = effMC[1][0]*eff_gl[1][0]
           SF_evt_v[1] = self._get_SF(effData_evt_v[1] , effMC_evt_v[1])
           effs_data[0] = effData_evt_v[1]
           effs_mc[0] = effMC_evt_v[1]
           for i in range(1,7):
               effs_data[i] = effData[1][i]*eff_gl[1][i]
               effs_mc[i] = effMC[1][i]*eff_gl[1][i]

           SF_evt_v_d[1] = self._get_SFUnc(effs_data, effs_mc)[0]
           SF_evt_v_u[1] = self._get_SFUnc(effs_data, effs_mc)[1]

           effData_evt_v[4]  = (effData[4][0]*effData[3][0] + effData[2][0]*effData[5][0] - effData[3][0]*effData[2][0])*eff_gl[2][0]*eff_dz[0]
           effMC_evt_v[4]  = (effMC[4][0]*effMC[3][0] + effMC[2][0]*effMC[5][0] - effMC[3][0]*effMC[2][0])*eff_gl[2][0]*eff_dz[0]
           SF_evt_v[4] = self._get_SF(effData_evt_v[4] , effMC_evt_v[4])
           effs_data[0] = effData_evt_v[4]
           effs_mc[0] = effMC_evt_v[4]
           for i in range(1,7):
               effs_data[i] = (effData[4][i]*effData[3][i] + effData[2][i]*effData[5][i] - effData[3][i]*effData[2][i])*eff_gl[2][i]*eff_dz[i]
               effs_data[i] = (effMC[4][i]*effMC[3][i] + effMC[2][i]*effMC[5][i] - effMC[3][i]*effMC[2][i])*eff_gl[2][i]*eff_dz[i]

           SF_evt_v_d[4] = self._get_SFUnc(effs_data, effs_mc)[0]
           SF_evt_v_u[4] = self._get_SFUnc(effs_data, effs_mc)[1]

        else:
           effData_evt_v[0] = effData[1][0]*eff_gl[0][0]
           effMC_evt_v[0] = effMC[1][0]*eff_gl[0][0]
           SF_evt_v[0] = self._get_SF(effData_evt_v[0] , effMC_evt_v[0])
           effs_data[0] = effData_evt_v[0]
           effs_mc[0] = effMC_evt_v[0]
           for i in range(1,7):
               effs_data[i] = effData[1][i]*eff_gl[0][i]
               effs_mc[i] = effMC[1][i]*eff_gl[0][i]

           SF_evt_v_d[0] = self._get_SFUnc(effs_data, effs_mc)[0]
           SF_evt_v_u[0] = self._get_SFUnc(effs_data, effs_mc)[1]


           effData_evt_v[1] = effData[0][0]*eff_gl[1][0]
           effMC_evt_v[1] = effMC[0][0]*eff_gl[1][0]
           SF_evt_v[1] = self._get_SF(effData_evt_v[1] , effMC_evt_v[1])
           effs_data[0] = effData_evt_v[0]
           effs_mc[0] = effMC_evt_v[0]
           for i in range(1,7):
               effs_data[i] = effData[0][i]*eff_gl[1][i]
               effs_mc[i] = effMC[0][i]*eff_gl[1][i]

           SF_evt_v_d[1] = self._get_SFUnc(effs_data, effs_mc)[0]
           SF_evt_v_u[1] = self._get_SFUnc(effs_data, effs_mc)[1]


           effData_evt_v[4]  = (effData[4][0]*effData[3][0] + effData[2][0]*effData[5][0] - effData[3][0]*effData[2][0])*eff_gl[2][0]*eff_dz[0]
           effMC_evt_v[4]  = (effMC[4][0]*effMC[3][0] + effMC[2][0]*effMC[5][0] - effMC[3][0]*effMC[2][0])*eff_gl[2][0]*eff_dz[0]
           SF_evt_v[4] = self._get_SF(effData_evt_v[4] , effMC_evt_v[4])
           effs_data[0] = effData_evt_v[4]
           effs_mc[0] = effMC_evt_v[4]
           for i in range(1,7):
               effs_data[i] = (effData[4][i]*effData[3][i] + effData[2][i]*effData[5][i] - effData[3][i]*effData[2][i])*eff_gl[2][i]*eff_dz[i]
               effs_mc[i] = (effMC[4][i]*effMC[3][i] + effMC[2][i]*effMC[5][i] - effMC[3][i]*effMC[2][i])*eff_gl[2][i]*eff_dz[i]

           SF_evt_v_d[4] = self._get_SFUnc(effs_data, effs_mc)[0]
           SF_evt_v_u[4] = self._get_SFUnc(effs_data, effs_mc)[1]

        # Trigger emulator
        Trig_em = [False, False, False, False, False, False]  
        Trndm = []
        for a in range(8):
           if event_seed is not None:
              if a == 0: Trndm.append(get_rndm(event_seed*event_seed))
              else: Trndm.append(get_rndm(10000*Trndm[a-1]))
           else: Trndm.append(get_rndm(event_seed))

        sApass   = effData[0][0]*eff_gl[0][0] > Trndm[0]
        sBpass   = effData[1][0]*eff_gl[1][0] > Trndm[1]
        lApass   = effData[2][0] > Trndm[2]
        lBpass   = effData[3][0] > Trndm[3]
        tApass   = effData[4][0] > Trndm[4]
        tBpass   = effData[5][0] > Trndm[5]
        DZpass   =    eff_dz[0] > Trndm[6]
        dblglpass=    eff_gl[2][0] > Trndm[7]

        if abs(pdgId1) == 11 and abs(pdgId2) == 11:
           Trig_em[1] = sApass or sBpass
           Trig_em[3] = (lApass and tBpass and  DZpass and dblglpass) or (lBpass and tApass and  DZpass and dblglpass)        
        elif abs(pdgId1) == 13 and abs(pdgId2) == 13:
           Trig_em[2] = sApass or sBpass
           Trig_em[4] = (lApass and tBpass and  DZpass and dblglpass) or (lBpass and tApass and  DZpass and dblglpass)        
        elif abs(pdgId1) == 11 and abs(pdgId2) == 13:
           Trig_em[1] = sApass
           Trig_em[2] = sBpass
           Trig_em[5] = (lApass and tBpass and  DZpass and dblglpass) or (lBpass and tApass and  DZpass and dblglpass)
        else:
           Trig_em[1] = sBpass
           Trig_em[2] = sApass
           Trig_em[5] = (lApass and tBpass and  DZpass and dblglpass) or (lBpass and tApass and  DZpass and dblglpass)

        Trig_em[0] = Trig_em[1] or Trig_em[2] or Trig_em[3] or Trig_em[4] or Trig_em[5]

        return effData_evt, effData_evt_v, SF_evt, SF_evt_v, SF_evt_v_d, SF_evt_v_u, Trig_em 


    def _get_w1l(self, pdgId1, pt1, eta1, run_p, event_seed=None):
         
        pt1, eta1 = self._over_under(pdgId1, pt1, eta1)

        if abs(pdgId1) == 11 :
           singleLeg  = "SingleEle"                              
        if abs(pdgId1) == 13:
           singleLeg  = "SingleMu"

         # Get Leg Efficiencies
        eff_sgl, low_eff_sgl, high_eff_sgl, low_eff_sgl_stat, high_eff_sgl_stat, low_eff_sgl_syst, high_eff_sgl_syst = self._get_LegEff (pt1, eta1, run_p, singleLeg, isdata=True)
        eff_gl = self.TM_GlEff[run_p][singleLeg]

        eff_v=[]
        eff_v.append(eff_sgl*eff_gl[0])
        eff_v.append(low_eff_sgl*eff_gl[1]) 
        eff_v.append(high_eff_sgl*eff_gl[2])

        # Trigger emulator
        Trig_em = [False, False, False, False, False, False]  
        Trndm = []
        for a in range(8):
           if event_seed is not None:
              if a == 0: Trndm.append(get_rndm(event_seed*event_seed))
              else: Trndm.append(get_rndm(10000*Trndm[a-1]))
           else: Trndm.append(get_rndm(event_seed))

         # eff_evt_v_map = ['sinEl', 'sinMu', 'doubleEl', 'doubleMu', 'ElMu']
        eff_evt_v = [0.,0.,0.,0.,0.]
        if abs(pdgId1) == 11 :
           eff_evt_v[0] = eff_sgl
           Trig_em[0] = eff_sgl > Trndm[0]

        if abs(pdgId1) == 13 :
           eff_evt_v[1] = eff_sgl
           Trig_em[1] = eff_sgl > Trndm[1]
         
        Trig_em[0] = Trig_em[1] or Trig_em[2] or Trig_em[3] or Trig_em[4] or Trig_em[5]

        return eff_v, eff_evt_v, Trig_em 

    def _get_3lw(self, pdgId1, pt1, eta1, pdgId2, pt2, eta2, pdgId3, pt3, eta3, nvtx, run_p):
        
        pt1, eta1 = self._over_under(pdgId1, pt1, eta1)
        pt2, eta2 = self._over_under(pdgId2, pt2, eta2)
        pt3, eta3 = self._over_under(pdgId3, pt3, eta3)

        eff12Data, eff12MC, eff_dz12 , eff_gl12 = self._pair_eff(pdgId1, pt1, eta1, pdgId2, pt2, eta2, nvtx, run_p)
        eff13Data, eff13MC, eff_dz13 , eff_gl13 = self._pair_eff(pdgId1, pt1, eta1, pdgId3, pt3, eta3, nvtx, run_p)
        eff23Data, eff23MC, eff_dz23 , eff_gl23 = self._pair_eff(pdgId2, pt2, eta2, pdgId3, pt3, eta3, nvtx, run_p)

        eff_evt = [0., 0., 0.]
        for i in range(3):
           s1 = eff13Data[0][i]*eff_gl13[0][i]
           s2 = eff23Data[0][i]*eff_gl12[1][i]
           s3 = eff13Data[1][i]*eff_gl13[1][i]
           eff_sng = s1 + (1-s1)*s2 + (1 - s1 - (1 - s1*s2))*s3
           e12 = (eff12Data[2][i]*eff12Data[5][i] + (1 - eff12Data[2][i]*eff12Data[5][i])*eff12Data[3][i]*eff12Data[4][i])*eff_dz12[i]*eff_gl12[2][i]
           e13 = (eff13Data[2][i]*eff13Data[5][i] + (1 - eff13Data[2][i]*eff13Data[5][i])*eff13Data[3][i]*eff13Data[4][i])*eff_dz13[i]*eff_gl13[2][i]
           e23 = (eff23Data[2][i]*eff23Data[5][i] + (1 - eff23Data[2][i]*eff23Data[5][i])*eff23Data[3][i]*eff23Data[4][i])*eff_dz23[i]*eff_gl23[2][i]
           eff_dbl = e12 + (1 - e12)*e13 + (1 - e12)*(1 - e13)*e23
           #eff_dbl = e12 + (1 - e12)*e13 + (1 - e12 - (1 - e12)*e13)*e23
           eff_evt[i] = eff_dbl + (1 - eff_dbl)*eff_sng 

        return eff_evt 

    def _get_nlw(self, pdgId_v, pt_v, eta_v, nvtx, run_p):
        if not (len(pdgId_v) == len(pt_v) and len(pt_v) == len(eta_v)):
           raise ValueError('Incorrect input format: requires vectors of equal length.')
        nLep = len(pt_v)
        if nLep < 2:
           raise ValueError('At least 2 leptons required.')
        
        for h in range(nLep):
           pt_v[h], eta_v[h] = self._over_under(pdgId_v[h], pt_v[h], eta_v[h])

        eff_dict = {}
        eff_dbl_inv = [1., 1., 1.]
        eff_sng_inv = [1., 1., 1.]
        #eff_dbl_inv = [0., 0., 0.]
        #eff_sng_inv = [0., 0., 0.]
        eff_evt = [0., 0., 0.]
        for i in range(nLep):
           for j in range(i+1, nLep):
              key_name = str(i+1) + '_' + str(j+1)
              eff_dict[key_name] = {}

              temp_effData, temp_effMC, temp_eff_dz , temp_eff_gl = self._pair_eff(pdgId_v[i], pt_v[i], eta_v[i], pdgId_v[j], pt_v[j], eta_v[j], nvtx, run_p)
              eff_dict[key_name]['eff']     = temp_effData
              eff_dict[key_name]['eff_dz']  = temp_eff_dz
              eff_dict[key_name]['eff_gl']  = temp_eff_gl
               
              for k in range(3):
                 temp_var = (temp_effData[2][k]*temp_effData[5][k] + (1 - temp_effData[2][k]*temp_effData[5][k])*temp_effData[3][k]*temp_effData[4][k])*temp_eff_dz[k]*temp_eff_gl[2][k]
                 eff_dbl_inv[k] *= (1 - temp_var)
                 #eff_dbl_inv[k] += (1 - eff_dbl_inv[k])*temp_var
           for l in range(3):
              if i == nLep-1:
                 eff_sng_inv[l] *= (1 - eff_dict['1_'+str(nLep)]['eff'][1][l]*eff_dict['1_'+str(nLep)]['eff_gl'][1][l])
                 #eff_sng_inv[l] += (1 - eff_sng_inv[l])*eff_dict['1_'+str(nLep)]['eff'][1][l]
              else:
                 eff_sng_inv[l] *= (1 - eff_dict[str(i + 1)+'_'+str(nLep)]['eff'][0][l]*eff_dict[str(i + 1)+'_'+str(nLep)]['eff_gl'][0][l])
                 #eff_sng_inv[l] += (1 - eff_sng_inv[l])*eff_dict[str(i + 1)+'_'+str(nLep)]['eff'][0][l]

        for m in range(3):
           eff_evt[m] = 1. - eff_dbl_inv[m]*eff_sng_inv[m]
           #eff_evt[m] = eff_dbl_inv[m] + (1 - eff_dbl_inv[m])*eff_sng_inv[m]

        return eff_evt


    def _get_trigDec(self, run_p, event):
        dec = {}
        for Tname in self.TM_trig[run_p]:
           temp_dec = 0
           for bit in self.TM_trig[run_p][Tname]:
              if eval(bit) == 1: temp_dec = 1
           dec[Tname] = temp_dec
        return dec

    def _dPhi(self,phi1,phi2):
        '''Copied from Gardener/python/varialbe/triggerMaker.py '''
        PI=3.14159265359
        dphi=abs(phi1-phi2)*180./PI
        if dphi>180 : dphi=360-dphi
        return dphi

    def _phiCSC(self,pt,eta,phi,charge):
        '''Copied from Gardener/python/varialbe/triggerMaker.py '''
        theta = 2. * math.atan ( math.exp(-1.*eta) )
        phiCSC = phi + charge * (1./pt) * ( 10.48 - 5.1412 * theta + 0.02308 * theta * theta ) 
        return phiCSC

    def _get_EMTFbug_veto(self, pdgId_v, pt_v, eta_v, phi_v, run_p):
        if self.EMTFbug[run_p]:
           temp_phi = []
           temp_eta = []
           for i in range(len(pt_v)):
              if abs(pdgId_v[i]) == 13 and pt_v[i] >= 10. and abs(eta_v[i]) >= 1.24:
                 temp_eta.append(eta_v[i])
                 temp_phi.append(phi_v[i])
           if len(temp_eta) > 1:
              for i in range(len(temp_eta)):
                 for j in range(len(temp_eta)):
                    if i == j and temp_eta[i]*temp_eta[j] > 0: continue 
                    if self._dPhi(temp_phi[i], temp_phi[j]) < 80.: return 0
        return 1

    #_____Analyze
    def analyze(self, event):
        """process event, return True (go to next module) or False (fail, go to next event)"""
        event = mappedEvent(event, mapname=self._branch_map)
        
        if self.firstEvent:
            self.firstEvent = False
            if self.keepRunP and not hasattr(event, 'run_period'): raise ValueError('TrigMaker: event does not contain the \'run_period\' branch, while \'keepRunP\' is True.')

        # Make your life easier
        if self.seeded: evt = eval(self.event)
        else: evt = None

        if not self.keepRunP: run_p = self._run_period(eval(self.run), evt) 
        else: run_p = eval(self.run_p)

        nvtx = event.PV_npvsGood

        lep_col = Collection(event, 'Lepton')
        nLep  = len(lep_col)

        pdgId = [] 
        pt    = []
        eta   = []
        phi   = []

        for iLep in range(nLep):
           pdgId.append(lep_col[iLep]['pdgId'])
           pt.append(lep_col[iLep]['pt'])
           eta.append(lep_col[iLep]['eta'])
           phi.append(lep_col[iLep]['phi'])

        EMTF  = self._get_EMTFbug_veto(pdgId, pt, eta, phi, run_p)
        trig_dec = self._get_trigDec(run_p, event)        
 
        # Fill DATA branches
        for name in self.NewVar['I']: 
            if 'Trigger_sngEl' in name: self.out.fillBranch(name, trig_dec['SingleEle']) 
            elif 'Trigger_sngMu' in name: self.out.fillBranch(name,  trig_dec['SingleMu']) 
            elif 'Trigger_dblEl' in name: self.out.fillBranch(name, trig_dec['DoubleEle']) 
            elif 'Trigger_dblMu' in name: self.out.fillBranch(name,  trig_dec['DoubleMu']) 
            elif 'Trigger_ElMu' in name: self.out.fillBranch(name,      trig_dec['EleMu']) 
            elif 'run_period' in name and not self.keepRunP: self.out.fillBranch(name, run_p) 
            elif 'EMTFbug_veto' in name : self.out.fillBranch(name, EMTF)

        #self.out.fillBranch('Trigger_sngMu',  trig_dec['SingleMu']) 
        #self.out.fillBranch('Trigger_dblEl', trig_dec['DoubleEle']) 
        #self.out.fillBranch('Trigger_dblMu',  trig_dec['DoubleMu']) 
        #self.out.fillBranch('Trigger_ElMu' ,     trig_dec['EleMu']) 
        #if not self.keepRunP: self.out.fillBranch('run_period', run_p) 
        #self.out.fillBranch('EMTFbug_veto', EMTF)
 
        # Stop here if not MC 
        if self.isData: return True

        # Trigger efficiencies 
        eff_dict = {}
        sf_dict = {}
        for name in self.NewVar['F']:
           if 'EffWeight' in name: eff_dict[name] = 0.
           if 'SFWeight' in name: sf_dict[name] = 0.
        Trig_em = [False]*6     

        if nLep > 0 :
           temp_evt, temp_evt_v, Trig_em = self._get_w1l(pdgId[0], pt[0], eta[0], run_p, evt)
           for name in self.NewVar['F']:
               if 'TriggerEffWeight' in name:
                   if '_1l' in name:
                       if '_1l_d' in name: eff_dict[name] = temp_evt[1]
                       elif '_1l_u' in name: eff_dict[name] = temp_evt[2]
                       else: eff_dict[name] = temp_evt[0]
                   elif '_sngEl' in name: eff_dict[name] = temp_evt_v[0]
                   elif '_sngMu' in name: eff_dict[name] = temp_evt_v[1]
                   elif '_dblEl' in name: eff_dict[name] = temp_evt_v[2]
                   elif '_dblMu' in name: eff_dict[name] = temp_evt_v[3]
                   elif '_ElMu' in name: eff_dict[name]  = temp_evt_v[4]
 
           #eff_dict['TriggerEffWeight_1l']   = temp_evt[0]
           #eff_dict['TriggerEffWeight_1l_d'] = temp_evt[1]
           #eff_dict['TriggerEffWeight_1l_u'] = temp_evt[2]
           #eff_dict['TriggerEffWeight_sngEl'] = temp_evt_v[0]
           #eff_dict['TriggerEffWeight_sngMu'] = temp_evt_v[1]
           #eff_dict['TriggerEffWeight_dblEl'] = temp_evt_v[2]
           #eff_dict['TriggerEffWeight_dblMu'] = temp_evt_v[3]
           #eff_dict['TriggerEffWeight_ElMu']  = temp_evt_v[4]
 
        if nLep > 1:
           tempData_evt, tempData_evt_v, tempSF_evt, tempSF_evt_v, tempSF_evt_v_d, tempSF_evt_v_u, Trig_em = self._get_w(pdgId[0], pt[0], eta[0], pdgId[1], pt[1], eta[1], nvtx, run_p, evt)
           for name in self.NewVar['F']:
               if 'TriggerEffWeight' in name:
                   if '_2l' in name:
                       if '_2l_d' in name: eff_dict[name] = tempData_evt[1]
                       elif '_2l_u' in name: eff_dict[name] = tempData_evt[2]
                       else: eff_dict[name] = tempData_evt[0]
                   elif '_sngEl' in name: eff_dict[name] = tempData_evt_v[0]
                   elif '_sngMu' in name: eff_dict[name] = tempData_evt_v[1]
                   elif '_dblEl' in name: eff_dict[name] = tempData_evt_v[2]
                   elif '_dblMu' in name: eff_dict[name] = tempData_evt_v[3]
                   elif '_ElMu' in name: eff_dict[name]  = tempData_evt_v[4]

               elif 'TriggerSFWeight' in name:
                   if '_2l' in name:
                       if '_2l_d' in name: sf_dict[name] = tempSF_evt[1]
                       elif '_2l_u' in name: sf_dict[name] = tempSF_evt[2]
                       else: sf_dict[name] = tempSF_evt[0]
                   elif '_sngEl' in name: 
                       if '_sngEl_d' in name: sf_dict[name] = tempSF_evt_v_d[0] 
                       elif '_sngEl_u' in name: sf_dict[name] = tempSF_evt_v_u[0]                       
                       else: sf_dict[name] = tempSF_evt_v[0]
                   elif '_sngMu' in name: 
                       if '_sngMu_d' in name: sf_dict[name] = tempSF_evt_v_d[1]
                       elif '_sngMu_u' in name: sf_dict[name] = tempSF_evt_v_u[1]
                       else: sf_dict[name] = tempSF_evt_v[1]
                   elif '_dblEl' in name:
                       if '_dblEl_d' in name: sf_dict[name] = tempSF_evt_v_d[2]
                       elif '_dblEl_u' in name: sf_dict[name] = tempSF_evt_v_u[2]
                       else: sf_dict[name] = tempSF_evt_v[2]
                   elif '_dblMu' in name:
                       if '_dblMu_d' in name: sf_dict[name] = tempSF_evt_v_d[3]
                       elif '_dblMu_u' in name: sf_dict[name] = tempSF_evt_v_u[3]
                       else: sf_dict[name] = tempSF_evt_v[3]
                   elif '_ElMu' in name:
                       if '_ElMu_d' in name: sf_dict[name] = tempSF_evt_v_d[4]
                       elif '_ElMu_u' in name: sf_dict[name] = tempSF_evt_v_u[4]
                       else: sf_dict[name] = tempSF_evt_v[4]

           #eff_dict['TriggerEffWeight_2l']   = temp_evt[0]
           #eff_dict['TriggerEffWeight_2l_d'] = temp_evt[1]
           #eff_dict['TriggerEffWeight_2l_u'] = temp_evt[2]
           #eff_dict['TriggerEffWeight_sngEl'] = temp_evt_v[0]
           #eff_dict['TriggerEffWeight_sngMu'] = temp_evt_v[1]
           #eff_dict['TriggerEffWeight_dblEl'] = temp_evt_v[2]
           #eff_dict['TriggerEffWeight_dblMu'] = temp_evt_v[3]
           #eff_dict['TriggerEffWeight_ElMu']  = temp_evt_v[4]

        if nLep > 2:
           temp_evt = self._get_3lw(pdgId[0], pt[0], eta[0], pdgId[1], pt[1], eta[1], pdgId[2], pt[2], eta[2], nvtx, run_p)
           for name in self.NewVar['F']:
               if 'TriggerEffWeight' in name:
                   if '_3l' in name:
                       if '_3l_d' in name: eff_dict[name] = temp_evt[1]
                       elif '_3l_u' in name: eff_dict[name] = temp_evt[2]
                       else: eff_dict[name] = temp_evt[0]

           #eff_dict['TriggerEffWeight_3l']   = temp_evt[0]
           #eff_dict['TriggerEffWeight_3l_d'] = temp_evt[1]
           #eff_dict['TriggerEffWeight_3l_u'] = temp_evt[2]
           
        if nLep > 3:
           temp_evt = self._get_nlw(pdgId[:4], pt[:4], eta[:4], nvtx, run_p)
           for name in self.NewVar['F']:
               if 'TriggerEffWeight' in name:
                   if '_4l' in name:
                       if '_4l_d' in name: eff_dict[name] = temp_evt[1]
                       elif '_4l_u' in name: eff_dict[name] = temp_evt[2]
                       else: eff_dict[name] = temp_evt[0]

           #eff_dict['TriggerEffWeight_4l']   = temp_evt[0]
           #eff_dict['TriggerEffWeight_4l_d'] = temp_evt[1]
           #eff_dict['TriggerEffWeight_4l_u'] = temp_evt[2]

        # Fill branches
        if 'TriggerEmulator' in self.NewVar['I']:
            self.out.fillBranch('TriggerEmulator', Trig_em)
        for name in eff_dict:
            self.out.fillBranch(name, eff_dict[name])
        for name in sf_dict:
            self.out.fillBranch(name, sf_dict[name])
        return True

def get_rndm(a):
    if a is None: return ROOT.gRandom.Rndm()
    r = ROOT.TRandom3(int(a))
    toss_a_coin = r.Uniform()
    return toss_a_coin

# define modules using the syntax 'name = lambda : constructor' to avoid having them loaded when not needed

trigMkr_MC       = lambda x:  TrigMaker(x)
trigMkr_MC_rerun = lambda x:  TrigMaker(x, keepRunP=True)
seededTrigMkr_MC = lambda x:  TrigMaker(x, seeded=True)

trigMkr_DATA       = lambda x:  TrigMaker(x, isData=True)
trigMkr_DATA_rerun = lambda x:  TrigMaker(x, isData=True, keepRunP=True)
seededTrigMkr_DATA = lambda x:  TrigMaker(x, isData=True, seeded=True)
