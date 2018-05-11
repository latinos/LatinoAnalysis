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

class TrigMaker(Module):
    '''
    Trigger Maker module MC,
    ''' 

    def __init__(self, cmssw = 'Full2016', isData = False, keepRunP = False, seeded = False):
        self.cmssw = cmssw
        self.isData = isData
        self.keepRunP = keepRunP
        self.seeded = seeded

        self.mu_maxPt = 200
        self.mu_minPt = 10
        self.mu_maxEta = 2.4
        self.mu_minEta = -2.4

        self.el_maxPt = 100
        self.el_minPt = 10
        self.el_maxEta = 2.5
        self.el_minEta = -2.5

        if self.isData:
           self.typeStr = 'DATA'
           self.NewVar = NewVar_DATA_dict
        else:
           self.NewVar = NewVar_MC_dict
           self.typeStr = 'MC'

        print('TrigMaker: CMSSW = ' + self.cmssw + ', isData = ' + str(self.isData) + ', keepRunPeriod = ' + str(self.keepRunP))

    def beginJob(self): 
        pass

    def endJob(self):
        pass

    def beginFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        self.initReaders(inputTree) # initReaders must be called in beginFile
        self.out = wrappedOutputTree
        
        if self.keepRunP:
           # Check if input tree indeed contains run_period
           isThere = False
           for br in inputTree.GetListOfBranches():
              if br.GetName() == 'run_period': isThere = True
           if not isThere: raise IOError("Input tree does not contain the 'run_period' branch. Set 'keepRunP' to False.")
           else: self.NewVar['I'].remove('run_period')
 
        for typ in self.NewVar:
           for name in self.NewVar[typ]:
              if name == 'TriggerEmulator': self.out.branch(name, typ, 6)
              else:                         self.out.branch(name, typ)

    def endFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        pass

    def initReaders(self,tree): # this function gets the pointers to Value and ArrayReaders and sets them in the C++ worker class
        # Specific trigger dicts
        cmssw_base = os.getenv('CMSSW_BASE')
        self.TM_trig    = {}
        self.TM_LegEff  = {}
        self.TM_DZEff   = {}
        #self.TM_trkSFMu = {}
        self.TM_runInt  = {}
        for RunP in Trigger[self.cmssw]:
           #self.TM_trkSFMu[RunP] = deepcopy(Trigger[self.cmssw][RunP]['trkSFMu'])
           self.TM_trig[RunP]    = {}
           self.TM_LegEff[RunP]  = {}
           self.TM_DZEff[RunP]   = {}
           self.TM_runInt[RunP]  = {'b': Trigger[self.cmssw][RunP]['begin'], 'e': Trigger[self.cmssw][RunP]['end']}
           for Tname in Trigger[self.cmssw][RunP][self.typeStr]:
              self.TM_trig[RunP][Tname] = []
              for HLT in Trigger[self.cmssw][RunP][self.typeStr][Tname]:
                 self.TM_trig[RunP][Tname].append('event.'+HLT)

           for Tname in Trigger[self.cmssw][RunP]['LegEff']:
              temp_file = open(cmssw_base + '/src/LatinoAnalysis/NanoGardener/python/data/trigger/' + Trigger[self.cmssw][RunP]['LegEff'][Tname], 'r')
              self.TM_LegEff[RunP][Tname] = [line.rstrip().split() for line in temp_file if '#' not in line]
              temp_file.close()

           for Tname in Trigger[self.cmssw][RunP]['DZEff']:
              self.TM_DZEff[RunP][Tname] = Trigger[self.cmssw][RunP]['DZEff'][Tname]

        # Set some run/event specific var
        self.total_lum = 0.
        self.EMTFbug = {}
        for RunP in Trigger[self.cmssw]:
           self.total_lum += Trigger[self.cmssw][RunP]['lumi']
           self.EMTFbug[RunP] = Trigger[self.cmssw][RunP]['EMTFBug']
        
        self.RunFrac = [0.]
        for RunP in Trigger[self.cmssw]:
           self.RunFrac.append(self.RunFrac[-1] + Trigger[self.cmssw][RunP]['lumi']/self.total_lum)
       
        if self.keepRunP: self.run_p = 'event.run_period'
 
        self.event = 'event.event'
        self.run = 'event.run'

    #_____Help functions
    def _run_period(self, run, event_seed=None):
        if self.isData:
           for RunP in self.TM_runInt:
              if run > self.TM_runInt[RunP]['b'] and run < self.TM_runInt[RunP]['e']: return RunP
        toss_a_coin = get_rndm(event_seed)
        for iPeriod in range(1,len(self.RunFrac)) :
           if toss_a_coin >= self.RunFrac[iPeriod-1] and toss_a_coin < self.RunFrac[iPeriod]:
              return iPeriod
           if toss_a_coin == 1.0:
              return len(self.RunFrac)-1
        print('strange', toss_a_coin)
        return -1 

    def _get_LegEff(self, pt, eta, run_p, trig_name):
        for eff_l in self.TM_LegEff[run_p][trig_name]:
           if len(eff_l) > 5:
              if (eta >= float(eff_l[0]) and eta <= float(eff_l[1]) and         # the "=" in both directions is only used by the overflow bin
                  pt  >= float(eff_l[2]) and pt  <= float(eff_l[3]) ) :         # in other cases the set is (min, max]
                 
                 eff = float(eff_l[4])
                 eff_u = min(1.0, float(eff_l[4]) + float(eff_l[5]))
                 if len(eff_l) > 6:
                    eff_d = max(0.0, float(eff_l[4]) - float(eff_l[6]))
                 else:
                    eff_d = max(0.0, float(eff_l[4]) - float(eff_l[5]))

                 return [eff, eff_d, eff_u]
           elif len(eff_l) > 2:
              raise IOError('Unexpected info in /LatinoAnalysis/NanoGardener/python/data/trigger/' + Trigger[self.cmssw][run_p]['LegEff'][trig_name] +\
                            ': ' + eff_l + ' not enough inputs?') 
        return [0. , 0., 0.]
        
    def _over_under(self, pdgId, pt, eta):
        if abs(pdgId) == 11:
           return max(self.el_minPt, min(self.el_maxPt, pt)), max(self.el_minEta, min(self.el_maxEta, eta))
        elif abs(pdgId) == 13:
           return max(self.mu_minPt, min(self.mu_maxPt, pt)), max(self.mu_minEta, min(self.mu_maxEta, eta))
        else:
           raise ValueError('_over_under can only operate on leptons, pdgI = ' + str(pdgId) + ', pt = ' + str(pt) + ', eta = ' + str(eta))

    def _pair_eff(self, pdgId1, pt1, eta1, pdgId2, pt2, eta2, run_p):
        '''
        Look op leg efficiencies and apply 5% sys for Electron and tracker SF for Muon
        '''
        eff_dz = 1.
        # Leg_map = ['singA', 'singB', 'leadA', 'leadB', 'trailA', 'trailB'] 
        # With A the lepton with the higer pt, B the one with the lower pt
        # Lead is the tracked lepton and trail is the trailing 
        Leg_names = []
        if abs(pdgId1) == 11 and abs(pdgId2) == 11:
           Leg_names = ['SingleEle', 'SingleEle', 'DoubleEleLegHigPt', 'DoubleEleLegHigPt', 'DoubleEleLegLowPt', 'DoubleEleLegLowPt']
           eff_dz = self.TM_DZEff[run_p]['DoubleEle']
        elif abs(pdgId1) == 13 and abs(pdgId2) == 13:
           Leg_names = ['SingleMu', 'SingleMu', 'DoubleMuLegHigPt', 'DoubleMuLegHigPt', 'DoubleMuLegLowPt', 'DoubleMuLegLowPt']
           eff_dz = self.TM_DZEff[run_p]['DoubleMu']
        elif abs(pdgId1) == 11 and abs(pdgId2) == 13:
           Leg_names = ['SingleEle', 'SingleMu', 'EleMuLegHigPt', 'MuEleLegHigPt', 'MuEleLegLowPt', 'EleMuLegLowPt']
           eff_dz = self.TM_DZEff[run_p]['EleMu']
        else:
           Leg_names = ['SingleMu', 'SingleEle', 'MuEleLegHigPt', 'EleMuLegHigPt', 'EleMuLegLowPt', 'MuEleLegLowPt']
           eff_dz = self.TM_DZEff[run_p]['MuEle']
        
        # eff_map = ['singA', 'singB', 'leadA', 'leadB', 'trailA', 'trailB']
        eff = []
        for iLeg in range(len(Leg_names)):
           eff.append(self._get_LegEff(eval('pt'+str(iLeg%2 + 1)), eval('eta'+str(iLeg%2 + 1)), run_p, Leg_names[iLeg]))
           # add 5% sys to single ele
           if Leg_names[iLeg] == 'SingleEle':
              sys_u = (eff[iLeg][2] - eff[iLeg][0])**2
              sys_d = (eff[iLeg][0] - eff[iLeg][1])**2
              sys_u += 0.05**2
              sys_d += 0.05**2
              eff[iLeg][2] = min(1.0, eff[iLeg][0] + math.sqrt(sys_u))
              eff[iLeg][1] = max(0.0, eff[iLeg][0] - math.sqrt(sys_d))
           # Muon tracker SF
           #if abs(pdgId1) == 13 and not iLeg%2:
           #   eff[iLeg] = [a*b for a,b in zip(eff[iLeg], self.TM_trkSFMu[run_p])] 
           #if abs(pdgId2) == 13 and iLeg%2:
           #   eff[iLeg] = [a*b for a,b in zip(eff[iLeg], self.TM_trkSFMu[run_p])] 
                
        return eff, eff_dz

    def _get_w(self, pdgId1, pt1, eta1, pdgId2, pt2, eta2, run_p, event_seed=None):
        
        pt1, eta1 = self._over_under(pdgId1, pt1, eta1)
        pt2, eta2 = self._over_under(pdgId2, pt2, eta2)
      
        eff, eff_dz = self._pair_eff(pdgId1, pt1, eta1, pdgId2, pt2, eta2, run_p)
       
        eff_dbl = [0., 0., 0.]
        eff_evt = [0., 0., 0.]
        for i in range(3): 
           eff_dbl[i] = (eff[4][i]*eff[3][i] + eff[2][i]*eff[5][i] - eff[3][i]*eff[2][i])
           eff_evt[i] = (eff_dbl[i] + eff[0][i]*(1. - eff[5][i]) + eff[1][i]*(1. - eff[4][i]))*eff_dz       
        
        eff_tl = eff[2][0]*eff[5][0]*eff_dz #eff_dz
        eff_lt = eff[3][0]*eff[4][0]*eff_dz #eff_dz

        # eff_evt_v (whatever it is)
        # eff_evt_v_map = ['sinEl', 'sinMu', 'doubleEl', 'doubleMu', 'ElMu']
        eff_evt_v = [0., 0., 0., 0., 0.]
        if abs(pdgId1) == 11 and abs(pdgId2) == 11:
           eff_evt_v[0] = eff[0][0] + (1 - eff[0][0])*eff[1][0]
           eff_evt_v[2] = eff[4][0]*eff[3][0] + eff[2][0]*eff[5][0] - eff[3][0]*eff[2][0]
        elif abs(pdgId1) == 13 and abs(pdgId2) == 13:
           eff_evt_v[1] = eff[0][0] + (1 - eff[0][0])*eff[1][0]
           eff_evt_v[3] = eff[4][0]*eff[3][0] + eff[2][0]*eff[5][0] - eff[3][0]*eff[2][0]
        elif abs(pdgId1) == 11 and abs(pdgId2) == 13:
           eff_evt_v[0] = eff[0][0]
           eff_evt_v[1] = eff[1][0]
           eff_evt_v[4]  = eff_tl + (1 - eff_tl)*eff_lt
        else:
           eff_evt_v[0] = eff[1][0]
           eff_evt_v[1] = eff[0][0]
           eff_evt_v[4]  = eff_tl + (1 - eff_tl)*eff_lt

        # Trigger emulator
        Trig_em = [False, False, False, False, False, False]  
        Trndm = []
        for a in range(8):
           if event_seed is not None:
              if a == 0: Trndm.append(get_rndm(event_seed*event_seed))
              else: Trndm.append(get_rndm(10000*Trndm[a-1]))
           else: Trndm.append(get_rndm(event_seed))

        sApass   = eff[0][0] > Trndm[0]
        sBpass   = eff[1][0] > Trndm[1]
        lApass   = eff[2][0] > Trndm[2]
        lBpass   = eff[3][0] > Trndm[3]
        tApass   = eff[4][0] > Trndm[4]
        tBpass   = eff[5][0] > Trndm[5]
        tlDZpass =    eff_dz > Trndm[6]
        ltDZpass =    eff_dz > Trndm[7]

        if abs(pdgId1) == 11 and abs(pdgId2) == 11:
           Trig_em[1] = sApass or sBpass
           Trig_em[3] = (lApass and tBpass and tlDZpass) or (lBpass and tApass and ltDZpass)        
        elif abs(pdgId1) == 13 and abs(pdgId2) == 13:
           Trig_em[2] = sApass or sBpass
           Trig_em[4] = (lApass and tBpass and tlDZpass) or (lBpass and tApass and ltDZpass)        
        elif abs(pdgId1) == 11 and abs(pdgId2) == 13:
           Trig_em[1] = sApass
           Trig_em[2] = sBpass
           Trig_em[5] = (lApass and tBpass and tlDZpass) or (lBpass and tApass and ltDZpass)
        else:
           Trig_em[1] = sBpass
           Trig_em[2] = sApass
           Trig_em[5] = (lApass and tBpass and tlDZpass) or (lBpass and tApass and ltDZpass)

        Trig_em[0] = Trig_em[1] or Trig_em[2] or Trig_em[3] or Trig_em[4] or Trig_em[5]

        return eff_evt, eff_evt_v, Trig_em 

    def _get_3lw(self, pdgId1, pt1, eta1, pdgId2, pt2, eta2, pdgId3, pt3, eta3, run_p):
        
        pt1, eta1 = self._over_under(pdgId1, pt1, eta1)
        pt2, eta2 = self._over_under(pdgId2, pt2, eta2)
        pt3, eta3 = self._over_under(pdgId3, pt3, eta3)

        eff12, eff_dz12 = self._pair_eff(pdgId1, pt1, eta1, pdgId2, pt2, eta2, run_p)
        eff13, eff_dz13 = self._pair_eff(pdgId1, pt1, eta1, pdgId3, pt3, eta3, run_p)
        eff23, eff_dz23 = self._pair_eff(pdgId2, pt2, eta2, pdgId3, pt3, eta3, run_p)

        eff_evt = [0., 0., 0.]
        for i in range(3):
           eff_sng = eff13[0][i] + (1 - eff13[0][i])*eff23[0][i] + (1 - eff13[0][i] - (1 - eff13[0][i])*eff23[0][i])*eff13[1][i]
           e12 = (eff12[2][i]*eff12[5][i] + (1 - eff12[2][i]*eff12[5][i])*eff12[3][i]*eff12[4][i])*eff_dz12
           e13 = (eff13[2][i]*eff13[5][i] + (1 - eff13[2][i]*eff13[5][i])*eff13[3][i]*eff13[4][i])*eff_dz13
           e23 = (eff23[2][i]*eff23[5][i] + (1 - eff23[2][i]*eff23[5][i])*eff23[3][i]*eff23[4][i])*eff_dz23
           #eff_dbl = e12 + (1 - e12)*e13 + (1 - e12)*(1 - e13)*e23
           eff_dbl = e12 + (1 - e12)*e13 + (1 - e12 - (1 - e12)*e13)*e23
           eff_evt[i] = eff_dbl + (1 - eff_dbl)*eff_sng 

        return eff_evt # return format: eff, error up, error down

    def _get_nlw(self, pdgId_v, pt_v, eta_v, run_p):
        if not (len(pdgId_v) == len(pt_v) and len(pt_v) == len(eta_v)):
           raise ValueError('Incorrect input format: requires vectors of equal length.')
        nLep = len(pt_v)
        if nLep < 2:
           raise ValueError('At leat 2 leptons required.')
        
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
              eff_dict[key_name] = {}

              temp_eff, temp_eff_dz = self._pair_eff(pdgId_v[i], pt_v[i], eta_v[i], pdgId_v[j], pt_v[j], eta_v[j], run_p)
              eff_dict[key_name]['eff']     = temp_eff
              eff_dict[key_name]['eff_dz']  = temp_eff_dz
              for k in range(3):
                 temp_var = (temp_eff[2][k]*temp_eff[5][k] + (1 - temp_eff[2][k]*temp_eff[5][k])*temp_eff[3][k]*temp_eff[4][k])*temp_eff_dz
                 eff_dbl_inv[k] *= (1 - temp_var)
                 #eff_dbl_inv[k] += (1 - eff_dbl_inv[k])*temp_var
           for l in range(3):
              if i == nLep-1:
                 eff_sng_inv[l] *= (1 - eff_dict['1_'+str(nLep)]['eff'][1][l])
                 #eff_sng_inv[l] += (1 - eff_sng_inv[l])*eff_dict['1_'+str(nLep)]['eff'][1][l]
              else:
                 eff_sng_inv[l] *= (1 - eff_dict[str(i + 1)+'_'+str(nLep)]['eff'][0][l])
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

        #if event._tree._ttreereaderversion > self._ttreereaderversion: # do this check at every event, as other modules might have read further branches
        #    self.initReaders(event._tree)
        # do NOT access other branches in python between the check/call to initReaders and the call to C++ worker code
 
        # Make your life easier
        if self.seeded: evt = eval(self.event)
        else: evt = None

        if not self.keepRunP: run_p = self._run_period(eval(self.run), evt) 
        else: run_p = eval(self.run_p)

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


        # MET filter
        #metF_pass = 1
        #for bit in self.SPtrigger:
        #   if self.SPtrigger[bit] == 0: 
        #      metF_pass = 0
        #      break

        trig_dec = self._get_trigDec(run_p, event)        
 
        # Fill DATA branches
        self.out.fillBranch('Trigger_sngEl', trig_dec['SingleEle']) 
        self.out.fillBranch('Trigger_sngMu',  trig_dec['SingleMu']) 
        self.out.fillBranch('Trigger_dblEl', trig_dec['DoubleEle']) 
        self.out.fillBranch('Trigger_dblMu',  trig_dec['DoubleMu']) 
        self.out.fillBranch('Trigger_ElMu' ,     trig_dec['EleMu']) 
        if not self.keepRunP: self.out.fillBranch('run_period', run_p) 
        self.out.fillBranch('EMTFbug_veto', EMTF)
        #self.out.fillBranch('metFilter', metF_pass)
 
        # Stop here if not MC 
        if self.isData: return True

        # Trigger efficiencies 
        eff_dict = {}
        for name in self.NewVar['F']:
           if 'EffWeight' in name: eff_dict[name] = 0.
        Trig_em = [False]*6       
 
        if nLep > 1:
           temp_evt, temp_evt_v, Trig_em = self._get_w(pdgId[0], pt[0], eta[0], pdgId[1], pt[1], eta[1], run_p, evt)
           eff_dict['TriggerEffWeight_2l']   = temp_evt[0]
           eff_dict['TriggerEffWeight_2l_d'] = temp_evt[1]
           eff_dict['TriggerEffWeight_2l_u'] = temp_evt[2]
           eff_dict['TriggerEffWeight_sngEl'] = temp_evt_v[0]
           eff_dict['TriggerEffWeight_sngMu'] = temp_evt_v[1]
           eff_dict['TriggerEffWeight_dblEl'] = temp_evt_v[2]
           eff_dict['TriggerEffWeight_dblMu'] = temp_evt_v[3]
           eff_dict['TriggerEffWeight_ElMu']  = temp_evt_v[4]

           #temp_evt2 = self._get_nlw(pdgId[:2], pt[:2], eta[:2], run_p)
           #print('________vvvvvvv________')
           #print('2lw: ', temp_evt)
           #print('nlw: ', temp_evt2)
           #print('_______________________')

        if nLep > 2:
           temp_evt = self._get_3lw(pdgId[0], pt[0], eta[0], pdgId[1], pt[1], eta[1], pdgId[2], pt[2], eta[2], run_p)
           eff_dict['TriggerEffWeight_3l']   = temp_evt[0]
           eff_dict['TriggerEffWeight_3l_d'] = temp_evt[1]
           eff_dict['TriggerEffWeight_3l_u'] = temp_evt[2]
           
           #temp_evt2 = self._get_nlw(pdgId[:3], pt[:3], eta[:3], run_p)
           #print('________vvvvvvv________')
           #print('3lw    : ', temp_evt)
           #print('nlw    : ', temp_evt2)
           #print('_______________________')
           
        if nLep > 3:
           temp_evt = self._get_nlw(pdgId[:4], pt[:4], eta[:4], run_p)
           eff_dict['TriggerEffWeight_4l']   = temp_evt[0]
           eff_dict['TriggerEffWeight_4l_d'] = temp_evt[1]
           eff_dict['TriggerEffWeight_4l_u'] = temp_evt[2]

        # Fill branches
        self.out.fillBranch('TriggerEmulator', Trig_em)
        #if not self.keepRunP: self.out.fillBranch('run_period', run_p) 
        #self.out.fillBranch('metFilter', metF_pass)
        for name in eff_dict:
           self.out.fillBranch(name, eff_dict[name])

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
