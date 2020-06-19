#
#
#
#    \ \     / \ \     /      ____| \ \        /  |  /       \  |  |       _ \  
#     \ \   /   \ \   /       __|    \ \  \   /   ' /         \ |  |      |   | 
#      \ \ /     \ \ /        |       \ \  \ /    . \       |\  |  |      |   | 
#       \_/       \_/        _____|    \_/\_/    _|\_\     _| \_| _____| \___/  
#                                                                               
#
#
#
#
# NLO Electroweak corrections for VV samples
# Currently only WW
#
# Based on qq2vvEWKcorrectionsWeight.py
# Uses GenPart to identify the W daughters
# Then loops LEHPart and matches based on pdgId and pT
# LHEPart info is used to avoid PS alterations

import os
import math
import copy
import ROOT
ROOT.PyConfig.IgnoreCommandLineOptions = True

from PhysicsTools.NanoAODTools.postprocessing.framework.datamodel import Collection 
from PhysicsTools.NanoAODTools.postprocessing.framework.eventloop import Module

import os.path


class qq2vv2lnujjEWKcorrectionsWeightProducer(Module):
    def __init__(self, sample_type='ww'):
        self.sample_type = sample_type
        #self.type_mass = {
        #    'ww': = [80.385, 80.385]
        #}
        print " sample_type = " , sample_type
        self.mass_dict = {
            #pdgId: mass[GeV],
            1: 0.0047,
            2: 0.0022,
            3: 0.095,
            4: 1.28,
            5: 4.18,
            6: 173.,
            11: 0.000511,
            12: 0.,
            13: 0.106,
            14: 0.,
            15: 1.78,
            16: 0.,
        }
        cmssw_base = os.getenv('CMSSW_BASE')
        self.corr_file = cmssw_base+'/src/LatinoAnalysis/Gardener/python/data/ewk/out_qqbww_EW_L8_200_forCMS.dat'

      
    def beginJob(self):
        pass

    def endJob(self):
        pass

    def beginFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        self.out = wrappedOutputTree
        self.out.branch('WWlnujjEwkNloW',  'F');
        self.load_dat_file(self.corr_file)

    def endFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        pass

    def get_sign(self, pdgId):
        #print('Input pdgId: '+str(pdgId))
        sign = 0
        if abs(pdgId) > 10 and abs(pdgId) < 17:
            sign = -1
            if not abs(pdgId)%2: sign = 0
            if pdgId < 0: sign *= -1
        elif abs(pdgId) > 0 and abs(pdgId) < 9:
            sign = -1
            if not abs(pdgId)%2: sign = 1
            if pdgId < 0: sign *= -1
        elif abs(pdgId) == 24:
            sign = 1
            if pdgId < 0: sign *= -1
        #print('Output sign: '+str(sign))
        return sign

    def load_dat_file(self, file_name):
        o_file = open(file_name, 'r')
        lines = o_file.readlines()
        o_file.close()

        self.corr_list = []
        for line in lines:
            line_list = line.replace('\n', '').split(' ')
            info = []
            for bit in line_list:
                if bit == '': continue
                info.append(bit)
            #line_list.remove('') 
            floats = []
            for num in info:
                floats.append(float(num))
            self.corr_list.append(floats)

    def get_w(self, s, t, q_type):
        if q_type < 0: return 1.
        s_sqrt = math.sqrt(s)
        mins_idx = -1
        min_ds = 9999.
        for idx,point in enumerate(self.corr_list):
            ds = abs(point[0] - s_sqrt)
            if ds < min_ds:
                min_ds = ds
                mins_idx = idx
        
        min_idx = -1
        min_dt = 9999.
        for idx,point in enumerate(self.corr_list):
            if not point[0] == self.corr_list[mins_idx][0]: continue
            dt = abs(point[1] - t)
            if dt < min_dt:
                min_dt = dt
                min_idx = idx
        w = 1. + self.corr_list[min_idx][2+q_type]
        return w 

    def calc_s_and_t(self, W1, W2, WW, x1, x2):
        p1 = ROOT.TLorentzVector()        
        p2 = ROOT.TLorentzVector()
        E_scale = 6500. #13TeV/2
        p1.SetPxPyPzE(0., 0., E_scale*x1, E_scale*x1)        
        p2.SetPxPyPzE(0., 0., -E_scale*x2, E_scale*x2)

        s_hat = WW.E()**2 - (WW.Px()**2 + WW.Py()**2 + WW.Pz()**2)        

        M_12   = 80.385
        M_22   = 80.385
 
        la1 = abs(s_hat) 
        la2 = math.sqrt(s_hat**2 + M_12**2 + M_22**2 - 2*(s_hat*M_12 + s_hat*M_22 + M_12*M_22))
 
        W1b = W1 
        W2b = W2  
        p1b = p1
        p2b = p2

        W1b.Boost(-WW.BoostVector()) 
        W2b.Boost(-WW.BoostVector()) 
        p1b.Boost(-WW.BoostVector()) 
        p2b.Boost(-WW.BoostVector()) 

        # Uni vectors
        ee1 = p1b*(1./math.sqrt(p1b.X()**2 + p1b.Y()**2 + p1b.Z()**2)) 
        ee2 = p2b*(1./math.sqrt(p2b.X()**2 + p2b.Y()**2 + p2b.Z()**2)) 
        z1 = W1b*(1./math.sqrt(W1b.X()**2 + W1b.Y()**2 + W1b.Z()**2)) 
        z2 = W2b*(1./math.sqrt(W2b.X()**2 + W2b.Y()**2 + W2b.Z()**2)) 

        ee_n = math.sqrt((ee1.X() - ee2.X())**2 + (ee1.Y() - ee2.Y())**2 + (ee1.Z() - ee2.Z())**2)
        ee = (ee1 - ee2)*(1./ee_n)

        costh = ee.X()*z1.X()+ee.Y()*z1.Y()+ee.Z()*z1.Z()
        t_hat = M_12 - (1./2.)*(s_hat+M_12-M_22) + (1./(2.*s_hat))*la1*la2*costh

        return s_hat, t_hat 

    def analyze(self, event):
        """process event, return True (go to next module) or False (fail, go to next event)"""
        #print('-----New-Event------')

        ewknloW             = -1
        ewknloWuncertainty  = -1

        LHEPart = Collection(event, "LHEPart")
        GenPart = Collection(event, 'GenPart')

        # Look up W daughter id's
        daughter_pdgId = []
        gen_W = {}
        for idx, part in enumerate(GenPart):
            if abs(part.pdgId) > 16: continue
            mom_idx = part.genPartIdxMother
            if mom_idx < 0: continue
            if abs(GenPart[mom_idx].pdgId) == 24:
                if not mom_idx in gen_W: gen_W[mom_idx] = []
                gen_W[mom_idx].append(idx)
                daughter_pdgId.append(part.pdgId)


        # Match gen W daughters to LHEPart based on pdgId
        # If pdgId of daughter appear multiple times in LHEPart, pick one with lowest delta pt
        lhe_W = {}
        for idx, part in enumerate(LHEPart):
            if not part.pdgId in daughter_pdgId: continue
            for w_gen_idx in gen_W:
                if not w_gen_idx in lhe_W: 
                    lhe_W[w_gen_idx] = {}
                    lhe_W[w_gen_idx]['dpt'] = [9999.]*len(gen_W[w_gen_idx])
                    lhe_W[w_gen_idx]['idx'] = [-1]*len(gen_W[w_gen_idx])
                for d_idx, d_gen_idx in enumerate(gen_W[w_gen_idx]):
                    if GenPart[d_gen_idx].pdgId == part.pdgId:
                        dpt = abs(GenPart[d_gen_idx].pt - part.pt)
                        if dpt < lhe_W[w_gen_idx]['dpt'][d_idx]:
                            lhe_W[w_gen_idx]['dpt'][d_idx] = dpt
                            lhe_W[w_gen_idx]['idx'][d_idx] = idx

        # If there are more then 2 Vbosons filter out worst LHE Gen pt matches 
        if len(lhe_W.keys()) != 2: 
            prt = True 
            while len(lhe_W.keys()) > 2: 
                worst_dpt_key = -1
                worst_dpt_sum = 0
                for w in lhe_W:
                    dpt_sum = sum(lhe_W[w]['dpt'])
                    if dpt_sum > worst_dpt_sum: 
                        worst_dpt_key = w
                        worst_dpt_sum = dpt_sum
                del lhe_W[worst_dpt_key]

        # Assemble V LorentzVectors
        V_vec = []
        V_sgn = []
        for w in lhe_W:
            if len(lhe_W[w]['idx']) != 2: print('Warning: V has '+len(lhe_W[w]['idx'])+' daughters!')
            V = ROOT.TLorentzVector()
            for d in lhe_W[w]['idx']:
                if d < 0: 
                    #print('Dropped unmatched V')
                    continue
                D = ROOT.TLorentzVector()
                D.SetPtEtaPhiM(LHEPart[d].pt, LHEPart[d].eta, LHEPart[d].phi, self.mass_dict[abs(LHEPart[d].pdgId)])
                V += D
            V_vec.append(copy.deepcopy(V))
            V_sgn.append(self.get_sign(GenPart[w].pdgId))

        x1 = event.Generator_x1
        x2 = event.Generator_x2

        id1 = event.Generator_id1
        id2 = event.Generator_id2

        # Match Charge sign of W to p to have right t definition
        if V_sgn[0] == self.get_sign(id1):                
            V1 = V_vec[0] 
            V2 = V_vec[1] 
        else:
            V2 = V_vec[0] 
            V1 = V_vec[1] 
        VV = V_vec[0] + V_vec[1] 

        # Calculate s and t and extract weight
        s_hat, t_hat = self.calc_s_and_t(V1, V2, VV, x1, x2)
        q_type = -1.
        if abs(id1)==2 and abs(id2)==2: q_type=0
        elif abs(id1)==1 and abs(id2)==1: q_type=1
        elif abs(id1)==5 and abs(id2)==5: q_type=2
        elif abs(id1)==4 and abs(id2)==4: q_type=0
        elif abs(id1)==3 and abs(id2)==3: q_type=1
        w = self.get_w(s_hat, t_hat, q_type)

        self.out.fillBranch('WWlnujjEwkNloW', w)
        return True

