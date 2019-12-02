import ROOT
import os
import re
import math
import time
import copy
ROOT.PyConfig.IgnoreCommandLineOptions = True

from PhysicsTools.NanoAODTools.postprocessing.framework.eventloop import Module
from LatinoAnalysis.NanoGardener.data.LeptonSel_cfg import LepFilter_dict 
from LatinoAnalysis.NanoGardener.data.LeptonMaker_cfg import Lepton_br, Lepton_var 
from LatinoAnalysis.NanoGardener.data.LeptonMaker_cfg import VetoLepton_br, VetoLepton_var 
from LatinoAnalysis.NanoGardener.data.LeptonMaker_cfg import CleanJet_br, CleanJet_var 
from LatinoAnalysis.NanoGardener.data.common_cfg import Type_dict

from PhysicsTools.NanoAODTools.postprocessing.framework.datamodel import Collection
from LatinoAnalysis.NanoGardener.framework.BranchMapping import mappedOutputTree, mappedEvent


class LeptonSFMaker(Module):
    '''
    Produce branches with recoSF, IDIsoSF, totSF
    ''' 

    def __init__(self, cmssw, WP_path = 'LatinoAnalysis/NanoGardener/python/data/LeptonSel_cfg.py', branch_map=''):
        self.cmssw = cmssw
        self._branch_map = branch_map
        self.minpt_mu = 10.0001
        self.maxpt_mu = 199.9999
        self.mineta_mu = -2.3999
        self.maxeta_mu = 2.3999

        self.minpt_ele = 10.0001
        self.maxpt_ele = 199.9999
        self.mineta_ele = -2.4999
        self.maxeta_ele = 2.4999

        cmssw_base = os.getenv('CMSSW_BASE')
        var = {}
        execfile(cmssw_base+'/src/'+WP_path, var)
        self.ElectronWP = var['ElectronWP']
        self.MuonWP = var['MuonWP']

        print('LeptonSFMaker: making scale factors for analysis of ' + self.cmssw)

    def beginJob(self): 
        pass

    def endJob(self):
        pass

    def beginFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        self.initReaders(inputTree) # initReaders must be called in beginFile
        self.out = mappedOutputTree(wrappedOutputTree, mapname=self._branch_map)
        
        
        # New Branches
        self.out.branch('Lepton_RecoSF', 'F', lenVar='nLepton')
        self.out.branch('Lepton_RecoSF_Up', 'F', lenVar='nLepton')
        self.out.branch('Lepton_RecoSF_Down', 'F', lenVar='nLepton')
       
        self.wp_sf_pf = ['_IdIsoSF', '_IdIsoSF_Up', '_IdIsoSF_Down', '_IdIsoSF_Syst', '_TotSF', '_TotSF_Up', '_TotSF_Down']
        for wp in self.ElectronWP[self.cmssw]['TightObjWP']:
           for postfix in self.wp_sf_pf:
               self.out.branch('Lepton_tightElectron_'+wp + postfix, 'F', lenVar='nLepton')
        for wp in self.MuonWP[self.cmssw]['TightObjWP']:
           for postfix in self.wp_sf_pf:
               self.out.branch('Lepton_tightMuon_'+wp + postfix, 'F', lenVar='nLepton')

    def endFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        pass

    def initReaders(self,tree): # this function gets the pointers to Value and ArrayReaders and sets them in the C++ worker class
        #self._ttreereaderversion = tree._ttreereaderversion # self._ttreereaderversion must be set AFTER all calls to tree.valueReader or tree.arrayReader
        cmssw_base = os.getenv('CMSSW_BASE')
        self.SF_dict = {}

        # electron setup
        self.SF_dict['electron'] = {}
        for wp in self.ElectronWP[self.cmssw]['TightObjWP']:
            self.SF_dict['electron'][wp] = {}
            self.SF_dict['electron'][wp]['tkSF'] = {}
            self.SF_dict['electron'][wp]['wpSF'] = {}
            for SFkey in self.ElectronWP[self.cmssw]['TightObjWP'][wp]:
                if SFkey == 'tkSF':
                    self.SF_dict['electron'][wp]['tkSF']['data'] = []
                    self.SF_dict['electron'][wp]['tkSF']['beginRP'] = []
                    self.SF_dict['electron'][wp]['tkSF']['endRP'] = []
                    for rpr in self.ElectronWP[self.cmssw]['TightObjWP'][wp]['tkSF']:
                        self.SF_dict['electron'][wp]['tkSF']['beginRP'].append(int(rpr.split('-')[0]))
                        self.SF_dict['electron'][wp]['tkSF']['endRP'].append(int(rpr.split('-')[1]))
                        tk_file = self.open_root(cmssw_base + '/src/' + self.ElectronWP[self.cmssw]['TightObjWP'][wp]['tkSF'][rpr])
                        self.SF_dict['electron'][wp]['tkSF']['data'].append(self.get_root_obj(tk_file, 'EGamma_SF2D'))
                        tk_file.Close()
                if SFkey == 'wpSF':
                    self.SF_dict['electron'][wp]['wpSF']['data'] = []
                    self.SF_dict['electron'][wp]['wpSF']['beginRP'] = []
                    self.SF_dict['electron'][wp]['wpSF']['endRP'] = []
                    for rpr in self.ElectronWP[self.cmssw]['TightObjWP'][wp]['wpSF']:
                        self.SF_dict['electron'][wp]['wpSF']['beginRP'].append(int(rpr.split('-')[0]))
                        self.SF_dict['electron'][wp]['wpSF']['endRP'].append(int(rpr.split('-')[1]))
                        wp_file = open(cmssw_base + '/src/' + self.ElectronWP[self.cmssw]['TightObjWP'][wp]['wpSF'][rpr])
                        self.SF_dict['electron'][wp]['wpSF']['data'].append([line.rstrip().split() for line in wp_file if '#' not in line])
                        wp_file.close()

        # muon setup
        self.SF_dict['muon'] = {}
        for wp in self.MuonWP[self.cmssw]['TightObjWP']:
            self.SF_dict['muon'][wp] = {}
            self.SF_dict['muon'][wp]['tkSF'] = {}
            self.SF_dict['muon'][wp]['idSF'] = {}
            self.SF_dict['muon'][wp]['isoSF'] = {}
            self.SF_dict['muon'][wp]['hasSFreco'] = False
            for SFkey in self.MuonWP[self.cmssw]['TightObjWP'][wp]:
                if SFkey == 'tkSF':
                    self.SF_dict['muon'][wp]['hasSFreco'] = True
                    self.SF_dict['muon'][wp]['tkSF']['data'] = []
                    self.SF_dict['muon'][wp]['tkSF']['beginRP'] = []
                    self.SF_dict['muon'][wp]['tkSF']['endRP'] = []
                    self.SF_dict['muon'][wp]['tkSF']['SFerror'] = self.MuonWP[self.cmssw]['TightObjWP'][wp]['tkSFerror']
                    for rpr in self.MuonWP[self.cmssw]['TightObjWP'][wp]['tkSF']:
                        self.SF_dict['muon'][wp]['tkSF']['beginRP'].append(int(rpr.split('-')[0]))
                        self.SF_dict['muon'][wp]['tkSF']['endRP'].append(int(rpr.split('-')[1]))
                        tk_file = self.open_root(cmssw_base + '/src/' + self.MuonWP[self.cmssw]['TightObjWP'][wp]['tkSF'][rpr])
                        self.SF_dict['muon'][wp]['tkSF']['data'].append(self.conv_graph2list(self.get_root_obj(tk_file, 'ratio_eff_vtx_dr030e030_corr')))
                        tk_file.Close()
                if SFkey == 'idSF':
                    self.SF_dict['muon'][wp]['idSF']['data'] = []
                    self.SF_dict['muon'][wp]['idSF']['mc'] = []
                    self.SF_dict['muon'][wp]['idSF']['beginRP'] = []
                    self.SF_dict['muon'][wp]['idSF']['endRP'] = []
                    self.SF_dict['muon'][wp]['idSF']['isRoot'] = []
                    for rpr in self.MuonWP[self.cmssw]['TightObjWP'][wp]['idSF']:
                        split_file = self.MuonWP[self.cmssw]['TightObjWP'][wp]['idSF'][rpr][0].split('.')
                        if split_file[-1] == 'txt':
                            self.SF_dict['muon'][wp]['idSF']['isRoot'].append(False)
                            self.SF_dict['muon'][wp]['idSF']['beginRP'].append(int(rpr.split('-')[0]))
                            self.SF_dict['muon'][wp]['idSF']['endRP'].append(int(rpr.split('-')[1]))
                            id_file_data = open(cmssw_base + '/src/' + self.MuonWP[self.cmssw]['TightObjWP'][wp]['idSF'][rpr][0])
                            id_file_mc = open(cmssw_base + '/src/' + self.MuonWP[self.cmssw]['TightObjWP'][wp]['idSF'][rpr][1])
                            self.SF_dict['muon'][wp]['idSF']['data'].append([line.rstrip().split() for line in id_file_data if '#' not in line])
                            self.SF_dict['muon'][wp]['idSF']['mc'].append([line.rstrip().split() for line in id_file_mc if '#' not in line])
                            id_file_data.close()
                            id_file_mc.close()
                        if split_file[-1] == 'root':
                            self.SF_dict['muon'][wp]['idSF']['isRoot'].append(True)
                            self.SF_dict['muon'][wp]['idSF']['beginRP'].append(int(rpr.split('-')[0]))
                            self.SF_dict['muon'][wp]['idSF']['endRP'].append(int(rpr.split('-')[1]))
                            data_file = self.open_root(cmssw_base + '/src/' + self.MuonWP[self.cmssw]['TightObjWP'][wp]['idSF'][rpr][0])
                            self.SF_dict['muon'][wp]['idSF']['data'].append(self.get_root_obj(data_file, 'Muon_idSF2D'))
                            data_file.Close()

                if SFkey == 'isoSF':
                    self.SF_dict['muon'][wp]['isoSF']['data'] = []
                    self.SF_dict['muon'][wp]['isoSF']['mc'] = []
                    self.SF_dict['muon'][wp]['isoSF']['beginRP'] = []
                    self.SF_dict['muon'][wp]['isoSF']['endRP'] = []
                    self.SF_dict['muon'][wp]['isoSF']['isRoot'] = []
                    for rpr in self.MuonWP[self.cmssw]['TightObjWP'][wp]['isoSF']:
                        split_file = self.MuonWP[self.cmssw]['TightObjWP'][wp]['idSF'][rpr][0].split('.')
                        if split_file[-1] == 'txt':
                            self.SF_dict['muon'][wp]['isoSF']['isRoot'].append(False)
                            self.SF_dict['muon'][wp]['isoSF']['beginRP'].append(int(rpr.split('-')[0]))
                            self.SF_dict['muon'][wp]['isoSF']['endRP'].append(int(rpr.split('-')[1]))
                            id_file_data = open(cmssw_base + '/src/' + self.MuonWP[self.cmssw]['TightObjWP'][wp]['isoSF'][rpr][0])
                            id_file_mc = open(cmssw_base + '/src/' + self.MuonWP[self.cmssw]['TightObjWP'][wp]['isoSF'][rpr][1])
                            self.SF_dict['muon'][wp]['isoSF']['data'].append([line.rstrip().split() for line in id_file_data if '#' not in line])
                            self.SF_dict['muon'][wp]['isoSF']['mc'].append([line.rstrip().split() for line in id_file_mc if '#' not in line])
                            id_file_data.close()
                            id_file_mc.close()
                        if split_file[-1] == 'root':
                            self.SF_dict['muon'][wp]['isoSF']['isRoot'].append(True)
                            self.SF_dict['muon'][wp]['isoSF']['beginRP'].append(int(rpr.split('-')[0]))
                            self.SF_dict['muon'][wp]['isoSF']['endRP'].append(int(rpr.split('-')[1]))
                            data_file = self.open_root(cmssw_base + '/src/' + self.MuonWP[self.cmssw]['TightObjWP'][wp]['isoSF'][rpr][0])
                            self.SF_dict['muon'][wp]['isoSF']['data'].append(self.get_root_obj(data_file, 'Muon_isoSF2D'))
                            data_file.Close()
            if not self.SF_dict['muon'][wp]['hasSFreco']: 
                self.SF_dict['muon'][wp]['tkSF']['beginRP'] = self.SF_dict['muon'][wp]['idSF']['beginRP']                
                self.SF_dict['muon'][wp]['tkSF']['endRP'] = self.SF_dict['muon'][wp]['idSF']['endRP']                

    #_____Help functions
    def open_root(self, path, option=''):
        r_file = ROOT.TFile.Open(path, option)
        if not r_file.__nonzero__() or not r_file.IsOpen(): raise NameError('File ' + path + ' not open')
        return r_file

    def get_root_obj(self, root_file, obj_name):
        r_obj = root_file.Get(obj_name)
        if not r_obj.__nonzero__(): raise NameError('Root Object ' + obj_name + ' not found')
        return copy.deepcopy(r_obj)

    def conv_graph2list(self, graph):
        lis = []
        for iBin in range(graph.GetN()):
            entry = []
            x = graph.GetX()[iBin]
            xmin = x - graph.GetEXlow()[iBin]
            xmax = x + graph.GetEXhigh()[iBin]
            y = graph.GetY()[iBin]
            entry.append(str(xmin))
            entry.append(str(xmax))
            entry.append(str(y))
            entry.append(str(graph.GetEYhigh()[iBin]))
            entry.append(str(graph.GetEYlow()[iBin]))
            lis.append(entry)
        return lis

    def get_hist_VnE(self, hist, x, y):
        '''
        Get the value of the 2D histogram hist in x and y
        '''
        hx = x
        hy = y


        nybins = hist.GetNbinsY()
        ymax = hist.GetYaxis().GetBinCenter(nybins)
        ymin = hist.GetYaxis().GetXmin()

        xmin = hist.GetXaxis().GetXmin()
        xmax = hist.GetXaxis().GetXmax()

        if hx < xmin: hx = xmin
        if hx > xmax: hx = xmax 

        if hy < ymin: hy = ymin
        if hy > ymax: hy = ymax
        #print('ymax = ' + str(ymax) + ' ' + str(hist.GetYaxis().GetBinUpEdge(1)) )
        #print('ymin = ' + str(hist.GetYaxis().GetBinLowEdge(1)))

        value = hist.GetBinContent(hist.FindBin(hx, hy))
        error = hist.GetBinError(hist.FindBin(hx, hy))

        return value, error

    def get_nvtxGraph_VnUnD(self, graph_list, nvtx):
        '''
        return value, up, down
        '''
        n = len(graph_list) - 1
        nvtx_min = float(graph_list[0][0]) 
        nvtx_max = float(graph_list[n][0])
        nvtx_t = nvtx
        if nvtx_t < nvtx_min: nvtx_t = nvtx_min
        if nvtx_t > nvtx_max: nvtx_t = nvtx_max
        for dot in graph_list:
            if nvtx_t >= float(dot[0]) and nvtx_t < float(dot[1]): return float(dot[2]), float(dot[3]), float(dot[4])
        return 0., 1., 1.

    def trunc_kin(self, pdgId, pt, eta):
        pt_t = pt
        eta_t = eta
        if abs(pdgId) == 11:
            if pt < self.minpt_ele: pt_t = self.minpt_ele
            if pt > self.maxpt_ele: pt_t = self.maxpt_ele
            if eta < self.mineta_ele: eta_t = self.mineta_ele
            if eta > self.maxeta_ele: eta_t = self.maxeta_ele
        elif abs(pdgId) == 13:
            if pt < self.minpt_mu: pt_t = self.minpt_mu
            if pt > self.maxpt_mu: pt_t = self.maxpt_mu
            if eta < self.mineta_mu: eta_t = self.mineta_mu
            if eta > self.maxeta_mu: eta_t = self.maxeta_mu
        else: raise ValueError('LeptonSFMaker trunc_kin: non lepton detected in what should be lepton collection')
        return pt_t, eta_t

    def get_reco_SF(self, pdgId, lep_pt, lep_eta, nvtx, wp, run_period):
        pt, eta = self.trunc_kin(pdgId, lep_pt, lep_eta)
        kin_str = 'electron' if (abs(pdgId) == 11) else 'muon'       

        if abs(pdgId) == 13 and not self.SF_dict[kin_str][wp]['hasSFreco']:
            tkSF = 1.
            tkSF_err = 0.
            return tkSF, tkSF_err, tkSF_err

        #select right SF dict index based on runperiod
        run_idx = 0
        #print(kin_str)
        #print(self.SF_dict[kin_str][wp]['tkSF'])
        for idx in range(len(self.SF_dict[kin_str][wp]['tkSF']['beginRP'])):
            if run_period >= self.SF_dict[kin_str][wp]['tkSF']['beginRP'][idx] and run_period <= self.SF_dict[kin_str][wp]['tkSF']['endRP'][idx]:
                run_idx = idx

        tkSF = 0.
        tkSF_err = 1.
        if abs(pdgId) == 11:
            tkSF, tkSF_err = self.get_hist_VnE(self.SF_dict[kin_str][wp]['tkSF']['data'][run_idx], eta, pt)
        if abs(pdgId) == 13:
            tkSF, tkSF_up, tkSF_dwn = self.get_nvtxGraph_VnUnD(self.SF_dict[kin_str][wp]['tkSF']['data'][run_idx], nvtx)
            tkSF_err = self.SF_dict[kin_str][wp]['tkSF']['SFerror']
        
        return tkSF, tkSF_err, tkSF_err

    def get_idIso_SF(self, pdgId, lep_pt, lep_eta, nvtx, wp, run_period):
        pt, eta = self.trunc_kin(pdgId, lep_pt, lep_eta)
        kin_str = 'electron' if (abs(pdgId) == 11) else 'muon'       

        #select right SF dict index based on runperiod
        run_idx = 0
        for idx in range(len(self.SF_dict[kin_str][wp]['tkSF']['beginRP'])):
            if run_period >= self.SF_dict[kin_str][wp]['tkSF']['beginRP'][idx] and run_period <= self.SF_dict[kin_str][wp]['tkSF']['endRP'][idx]:
                run_idx = idx

        tkSF = 0.
        tkSF_up = 1.
        tkSF_dwn = 1.
        tkSF_sys = 1.
        if abs(pdgId) == 11:
            for dot in self.SF_dict[kin_str][wp]['wpSF']['data'][run_idx]:
                if (pt >= float(dot[2]) and pt <= float(dot[3])) and (eta >= float(dot[0]) and eta <= float(dot[1])):
                    data = float(dot[4])
                    mc = float(dot[6])

                    sigma_d = float(dot[5])
                    sigma_m = float(dot[7])
                    
                    tkSF = data/mc
                    tkSF_err = math.sqrt( (sigma_d/mc)**2 + (data/mc/mc*sigma_m)**2)
                    tkSF_sys = math.sqrt( float(dot[8])**2 + float(dot[9])**2 + float(dot[10])**2 + float(dot[11])**2)
                    tkSF_sys /= mc
                    return tkSF, tkSF_err, tkSF_err, tkSF_sys

        if abs(pdgId) == 13:
            if not self.SF_dict['muon'][wp]['isoSF']['isRoot'][run_idx]:
                dot_iso_d = []
                dot_iso_m = []
                dot_id_d = []
                dot_id_m = []
                for dot in self.SF_dict[kin_str][wp]['isoSF']['data'][run_idx]:
                    if (pt >= float(dot[2]) and pt <= float(dot[3])) and (eta >= float(dot[0]) and eta <= float(dot[1])):
                        dot_iso_d = dot
                        break
                for dot in self.SF_dict[kin_str][wp]['isoSF']['mc'][run_idx]:
                    if (pt >= float(dot[2]) and pt <= float(dot[3])) and (eta >= float(dot[0]) and eta <= float(dot[1])):
                        dot_iso_m = dot
                        break
                for dot in self.SF_dict[kin_str][wp]['idSF']['data'][run_idx]:
                    if (pt >= float(dot[2]) and pt <= float(dot[3])) and (eta >= float(dot[0]) and eta <= float(dot[1])):
                        dot_id_d = dot
                        break
                for dot in self.SF_dict[kin_str][wp]['idSF']['mc'][run_idx]:
                    if (pt >= float(dot[2]) and pt <= float(dot[3])) and (eta >= float(dot[0]) and eta <= float(dot[1])):
                        dot_id_m = dot
                        break
                data_iso = float(dot_iso_d[4])
                mc_iso = float(dot_iso_m[4])

                sigma_iso_up_d = float(dot_iso_d[5])
                sigma_iso_up_m = float(dot_iso_m[5])
                    
                sigma_iso_dwn_d = float(dot_iso_d[6])
                sigma_iso_dwn_m = float(dot_iso_m[6])

                tkSF_iso = data_iso/mc_iso
                tkSF_iso_up = (data_iso + sigma_iso_up_d)/(mc_iso - sigma_iso_dwn_m) - tkSF_iso
                tkSF_iso_dwn = tkSF_iso - (data_iso - sigma_iso_dwn_d)/(mc_iso + sigma_iso_up_m)
            
            else:
                tkSF_iso, tkSF_err = self.get_hist_VnE(self.SF_dict[kin_str][wp]['isoSF']['data'][run_idx], eta, pt)
                tkSF_iso_up = tkSF_err
                tkSF_iso_dwn = tkSF_err
            #tkSF_iso_sys = math.sqrt( float(dot[8])**2 + float(dot[9])**2 + float(dot[10])**2 + float(dot[11])**2)
            #tkSF_iso_sys /= mc_iso
            
            if not self.SF_dict['muon'][wp]['idSF']['isRoot'][run_idx]:
                data_id = float(dot_id_d[4])
                mc_id = float(dot_id_m[4])

                sigma_id_up_d = float(dot_id_d[5])
                sigma_id_up_m = float(dot_id_m[5])
                    
                sigma_id_dwn_d = float(dot_id_d[6])
                sigma_id_dwn_m = float(dot_id_m[6])

                tkSF_id = data_id/mc_id
                tkSF_id_up = (data_id + sigma_id_up_d)/(mc_id - sigma_id_dwn_m) - tkSF_id
                tkSF_id_dwn = tkSF_id - (data_id - sigma_id_dwn_d)/(mc_id + sigma_id_up_m)
            
            else:
                tkSF_id, tkSF_err = self.get_hist_VnE(self.SF_dict[kin_str][wp]['idSF']['data'][run_idx], eta, pt)
                tkSF_id_up = tkSF_err
                tkSF_id_dwn = tkSF_err

                #tkSF_id_sys = math.sqrt( float(dot[8])**2 + float(dot[9])**2 + float(dot[10])**2 + float(dot[11])**2)
                #tkSF_id_sys /= mc_id

            tkSF_up = tkSF_id * tkSF_iso * math.sqrt(tkSF_id_up*tkSF_id_up/tkSF_id/tkSF_id +  tkSF_iso_up*tkSF_iso_up/tkSF_iso/tkSF_iso)
            tkSF_dwn = tkSF_id * tkSF_iso * math.sqrt(tkSF_id_dwn*tkSF_id_dwn/tkSF_id/tkSF_id +  tkSF_iso_dwn*tkSF_iso_dwn/tkSF_iso/tkSF_iso)
            tkSF = tkSF_id*tkSF_iso
            return tkSF, tkSF_dwn, tkSF_up, 0.0
        return tkSF, tkSF_err, tkSF_err, tkSF_sys

    #_____Analyze
    def analyze(self, event):
        """process event, return True (go to next module) or False (fail, go to next event)"""

        #if event._tree._ttreereaderversion > self._ttreereaderversion: # do this check at every event, as other modules might have read further branches
        #    self.initReaders(event._tree)
        # do NOT access other branches in python between the check/call to initReaders and the call to C++ worker code
        event = mappedEvent(event, mapname=self._branch_map)
        
        lepton_col   = Collection(event, 'Lepton')
        nLep = len(lepton_col) 
        #try:
        nvtx = event.PV_npvsGood #event.     => find nvtx
        #except:
        #    nvtx = event.PV_npvs
        run_period = event.run_period

        lep_var = {}
        lep_var['RecoSF'] = []
        lep_var['RecoSF_Up'] = []
        lep_var['RecoSF_Down'] = []
        el_wp_var = {} 
        mu_wp_var = {} 
        for wp in self.ElectronWP[self.cmssw]['TightObjWP']:
           for postfix in self.wp_sf_pf:
               el_wp_var[wp + postfix] = []
        for wp in self.MuonWP[self.cmssw]['TightObjWP']:
           for postfix in self.wp_sf_pf:
               mu_wp_var[wp + postfix] = []

        #------ Lepton Loop
        for iLep in range(nLep):
           pdgId = lepton_col[iLep]['pdgId']
           pt = lepton_col[iLep]['pt']
           eta = lepton_col[iLep]['eta']
           did_reco = False
           reco_sf, reco_sf_dwn, reco_sf_up = 0., 0., 0.
           # Lepton id's
           if abs(lepton_col[iLep]['pdgId']) == 11:
              for wp in self.ElectronWP[self.cmssw]['TightObjWP']:
                  if not did_reco:
                      reco_sf, reco_sf_dwn, reco_sf_up = self.get_reco_SF(pdgId, pt, eta, nvtx, wp, run_period)
                      lep_var['RecoSF'].append(reco_sf)
                      lep_var['RecoSF_Up'].append(reco_sf + reco_sf_up)
                      lep_var['RecoSF_Down'].append(reco_sf - reco_sf_dwn)
                      did_reco = True
                  idiso_sf, idiso_sf_dwn, idiso_sf_up, idiso_sf_sys = self.get_idIso_SF(pdgId, pt, eta, nvtx, wp, run_period)
                  el_wp_var[wp + '_IdIsoSF'].append(idiso_sf)
                  el_wp_var[wp + '_IdIsoSF_Up'].append(idiso_sf + idiso_sf_up)
                  el_wp_var[wp + '_IdIsoSF_Down'].append(idiso_sf - idiso_sf_dwn)
                  el_wp_var[wp + '_IdIsoSF_Syst'].append(idiso_sf + idiso_sf_sys)
                  el_wp_var[wp + '_TotSF'].append(idiso_sf*reco_sf)
                  el_wp_var[wp + '_TotSF_Up'].append(idiso_sf*reco_sf + math.sqrt(idiso_sf_up**2 + reco_sf_up**2 + idiso_sf_sys**2))
                  el_wp_var[wp + '_TotSF_Down'].append(idiso_sf*reco_sf - math.sqrt(idiso_sf_dwn**2 + reco_sf_dwn**2 + idiso_sf_sys**2))
              for wp in self.MuonWP[self.cmssw]['TightObjWP']:
                  mu_wp_var[wp + '_IdIsoSF'].append(1.0)
                  mu_wp_var[wp + '_IdIsoSF_Up'].append(0.0)
                  mu_wp_var[wp + '_IdIsoSF_Down'].append(0.0)
                  mu_wp_var[wp + '_IdIsoSF_Syst'].append(0.0)
                  mu_wp_var[wp + '_TotSF'].append(reco_sf)
                  mu_wp_var[wp + '_TotSF_Up'].append(reco_sf + reco_sf_up)
                  mu_wp_var[wp + '_TotSF_Down'].append(reco_sf - reco_sf_dwn)
           elif abs(lepton_col[iLep]['pdgId']) == 13:
              for wp in self.MuonWP[self.cmssw]['TightObjWP']:
                  if not did_reco:
                      reco_sf, reco_sf_dwn, reco_sf_up = self.get_reco_SF(pdgId, pt, eta, nvtx, wp, run_period)
                      lep_var['RecoSF'].append(reco_sf)
                      lep_var['RecoSF_Up'].append(reco_sf + reco_sf_up)
                      lep_var['RecoSF_Down'].append(reco_sf - reco_sf_dwn)
                      did_reco = True
                  idiso_sf, idiso_sf_dwn, idiso_sf_up, idiso_sf_sys = self.get_idIso_SF(pdgId, pt, eta, nvtx, wp, run_period)
                  mu_wp_var[wp + '_IdIsoSF'].append(idiso_sf)
                  mu_wp_var[wp + '_IdIsoSF_Up'].append(idiso_sf + idiso_sf_up)
                  mu_wp_var[wp + '_IdIsoSF_Down'].append(idiso_sf - idiso_sf_dwn)
                  mu_wp_var[wp + '_IdIsoSF_Syst'].append(idiso_sf + idiso_sf_sys)
                  mu_wp_var[wp + '_TotSF'].append(idiso_sf*reco_sf)
                  mu_wp_var[wp + '_TotSF_Up'].append(idiso_sf*reco_sf + math.sqrt(idiso_sf_up**2 + reco_sf_up**2 + idiso_sf_sys**2))
                  mu_wp_var[wp + '_TotSF_Down'].append(idiso_sf*reco_sf - math.sqrt(idiso_sf_dwn**2 + reco_sf_dwn**2 + idiso_sf_sys**2))
              for wp in self.ElectronWP[self.cmssw]['TightObjWP']:
                  el_wp_var[wp + '_IdIsoSF'].append(1.0)
                  el_wp_var[wp + '_IdIsoSF_Up'].append(0.0)
                  el_wp_var[wp + '_IdIsoSF_Down'].append(0.0)
                  el_wp_var[wp + '_IdIsoSF_Syst'].append(0.0)
                  el_wp_var[wp + '_TotSF'].append(reco_sf)
                  el_wp_var[wp + '_TotSF_Up'].append(reco_sf + reco_sf_up)
                  el_wp_var[wp + '_TotSF_Down'].append(reco_sf - reco_sf_dwn)

        # Filling branches
        for key in lep_var:
            self.out.fillBranch('Lepton_' + key, lep_var[key])
        for key in el_wp_var:
            self.out.fillBranch('Lepton_tightElectron_' + key, el_wp_var[key])
        for key in mu_wp_var:
            self.out.fillBranch('Lepton_tightMuon_' + key, mu_wp_var[key])

        return True

# define modules using the syntax 'name = lambda : constructor' to avoid having them loaded when not needed

#lepSel = lambda x,y,z:  LeptonSel(x, y, z)
