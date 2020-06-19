import os
import ROOT

from PhysicsTools.NanoAODTools.postprocessing.framework.eventloop import Module
from PhysicsTools.NanoAODTools.postprocessing.framework.datamodel import Collection 

class JetSFMaker(Module):
    #----------------------------------------------------------------------------
    #Add branches for Jet PUID scale factors and up/down SF variations (per jet).
    #Per event SF should be calculated as a product of per jet SFs and applied as
    #weight. Same for up/down variations (weights).
    #----------------------------------------------------------------------------

    def __init__(self, cmssw, puid_sf_config='LatinoAnalysis/NanoGardener/python/data/JetPUID_cfg.py'):
        cmssw_base = os.getenv('CMSSW_BASE')
        with open(cmssw_base + '/src/' + puid_sf_config) as src:
            exec(src)
            
        puid_sf_cfg = jet_puid_sf[cmssw]

        source = ROOT.TFile.Open(cmssw_base + '/src/' + puid_sf_cfg['source'])
        self.sf_maps = {}
        self.sf_uncty_maps = {}
        self.eff_maps = {}
        for jtype in ['real', 'pu']:
            for wp, iwp in [('loose', 'L'), ('medium', 'M'), ('tight', 'T')]:
                key = '%s_%s' % (jtype, wp)
                key_uncty = '%s_%s_uncty' % (jtype, wp)
                key_eff = '%s_mc_%s' % (jtype, wp)
                self.sf_maps[key] = source.Get(puid_sf_cfg[key])
                self.sf_maps[key].SetDirectory(0)
                self.sf_uncty_maps[key_uncty] = source.Get(puid_sf_cfg[key_uncty])
                self.sf_uncty_maps[key_uncty].SetDirectory(0)
                self.eff_maps[key_eff] = source.Get(puid_sf_cfg[key_eff])
                self.eff_maps[key_eff].SetDirectory(0)

        source.Close()

    def beginFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        self.out = wrappedOutputTree

        for wp in ['loose', 'medium', 'tight']:
            self.out.branch('Jet_PUIDSF_%s' % wp, 'F', lenVar='nJet')
            self.out.branch('Jet_PUIDSF_%s_up' % wp, 'F', lenVar='nJet')
            self.out.branch('Jet_PUIDSF_%s_down' % wp, 'F', lenVar='nJet')

    def analyze(self, event):
        jets = Collection(event, 'Jet')

        sfs = {'loose': [], 'medium': [], 'tight': []}
        sfs_up = {'loose': [], 'medium': [], 'tight': []}
        sfs_down = {'loose': [], 'medium': [], 'tight': []}

        for jet in jets:
            if jet.genJetIdx == -1:
                jtype = 'pu'
            else:
                jtype = 'real'

            for iwp,wp in [(2,'loose'), (1,'medium'), (0,'tight')]:
                #get ingredients for calculating per jet weights
                sf, stat_err, syst_err, eff = self.get_sf_and_eff(jtype, wp, jet)
                passed_puid  = bool(jet.puId & (1 << iwp))

                #calculate per jet weight + up/down per jet weight variations
                puid_jw     = 1.
                puid_upjw   = 1.
                puid_downjw = 1.
                if passed_puid:
                    puid_jw = sf
                    if (jtype == 'real') or (jtype == 'pu' and abs(jet.eta)>=2.5):
                        up   = sf + syst_err + stat_err
                        down = sf - syst_err - stat_err
                    else:
                        up   = 1 + abs(sf-1)
                        down = 1 - abs(sf-1)
                    puid_upjw   = up
                    puid_downjw = down  
                else:
                    puid_jw = (1.-sf*eff)/(1.-eff)
                    if (jtype == 'real') or (jtype == 'pu' and abs(jet.eta)>=2.5):
                        up   = sf + syst_err + stat_err
                        down = sf - syst_err - stat_err
                    else:
                        up   = 1 + abs(sf-1)
                        down = 1 - abs(sf-1)
                    puid_upjw   = (1.-up*eff)/(1.-eff)
                    puid_downjw = (1.-down*eff)/(1.-eff) 

                #store per jet weights and variations
                sfs[wp].append(puid_jw)
                sfs_up[wp].append(puid_upjw)
                sfs_down[wp].append(puid_downjw)

        for wp in ['loose', 'medium', 'tight']:
            self.out.fillBranch('Jet_PUIDSF_%s' % wp, sfs[wp])            
            self.out.fillBranch('Jet_PUIDSF_%s_up' % wp, sfs_up[wp])
            self.out.fillBranch('Jet_PUIDSF_%s_down' % wp, sfs_down[wp])

        return True

    def get_sf_and_eff(self, jtype, wp, jet):
        sf_map = self.sf_maps['%s_%s' % (jtype, wp)]
        sf_uncty_map = self.sf_uncty_maps['%s_%s_uncty' % (jtype, wp)] 
        eff_map = self.eff_maps['%s_mc_%s' % (jtype, wp)]

        if jet.pt < 30. or jet.pt > 50. or abs(jet.eta) > 4.7: 
            #do not apply SF outside CleanJet region and where PUID was not applied 
            return 1.,0.,0.,0. 

        ix = min(max(1, sf_map.GetXaxis().FindFixBin(jet.pt)), sf_map.GetNbinsX())
        iy = min(max(1, sf_map.GetYaxis().FindFixBin(jet.eta)), sf_map.GetNbinsY())

        jx = min(max(1, sf_uncty_map.GetXaxis().FindFixBin(jet.pt)), sf_uncty_map.GetNbinsX())
        jy = min(max(1, sf_uncty_map.GetYaxis().FindFixBin(jet.eta)), sf_uncty_map.GetNbinsY())

        kx = min(max(1, eff_map.GetXaxis().FindFixBin(jet.pt)), eff_map.GetNbinsX())
        ky = min(max(1, eff_map.GetYaxis().FindFixBin(jet.eta)), eff_map.GetNbinsY())

        return sf_map.GetBinContent(ix, iy), sf_map.GetBinError(ix, iy), sf_uncty_map.GetBinContent(jx, jy), eff_map.GetBinContent(kx, ky)

