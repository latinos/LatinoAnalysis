import os
import ROOT

from PhysicsTools.NanoAODTools.postprocessing.framework.eventloop import Module
from PhysicsTools.NanoAODTools.postprocessing.framework.datamodel import Collection 

class JetSFMaker(Module):
    """
    Add branches for Jet ID scale factors and uncertainties.
    """

    def __init__(self, cmssw, puid_sf_config='LatinoAnalysis/NanoGardener/python/data/JetPUID_cfg.py'):
        cmssw_base = os.getenv('CMSSW_BASE')
        with open(cmssw_base + '/src/' + puid_sf_config) as src:
            exec(src)
            
        puid_sf_cfg = jet_puid_sf[cmssw]

        source = ROOT.TFile.Open(cmssw_base + '/src/' + puid_sf_cfg['source'])
        self.sf_maps = {}
        self.sf_uncty_maps = {}
        for jtype in ['real', 'pu']:
            for wp, iwp in [('loose', 'L'), ('medium', 'M'), ('tight', 'T')]:
                key = '%s_%s' % (jtype, wp)
                key_uncty = '%s_%s_uncty' % (jtype, wp)
                self.sf_maps[key] = source.Get(puid_sf_cfg[key])
                self.sf_maps[key].SetDirectory(0)
                self.sf_uncty_maps[key_uncty] = source.Get(puid_sf_cfg[key_uncty])
                self.sf_uncty_maps[key_uncty].SetDirectory(0)

        source.Close()

    def beginFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        self.out = wrappedOutputTree

        for wp in ['loose', 'medium', 'tight']:
            self.out.branch('Jet_PUIDSF_%s' % wp, 'F', lenVar='nJet')
            self.out.branch('Jet_PUIDSF_%s_staterr' % wp, 'F', lenVar='nJet')
            self.out.branch('Jet_PUIDSF_%s_systerr' % wp, 'F', lenVar='nJet')

    def analyze(self, event):
        jets = Collection(event, 'Jet')

        sfs = {'loose': [], 'medium': [], 'tight': []}
        sfstat_errs = {'loose': [], 'medium': [], 'tight': []}
        sfsyst_errs = {'loose': [], 'medium': [], 'tight': []}

        for jet in jets:
            if jet.genJetIdx == -1:
                jtype = 'pu'
            else:
                jtype = 'real'

            for wp in ['loose', 'medium', 'tight']:
                sf, stat_err, syst_err = self.get_sf(jtype, wp, jet)
                sfs[wp].append(sf)
                sfstat_errs[wp].append(stat_err)
                sfsyst_errs[wp].append(syst_err)

        for wp in ['loose', 'medium', 'tight']:
            self.out.fillBranch('Jet_PUIDSF_%s' % wp, sfs[wp])            
            self.out.fillBranch('Jet_PUIDSF_%s_staterr' % wp, sfstat_errs[wp])
            self.out.fillBranch('Jet_PUIDSF_%s_systerr' % wp, sfsyst_errs[wp])
            
        return True

    def get_sf(self, jtype, wp, jet):
        sf_map = self.sf_maps['%s_%s' % (jtype, wp)]
        sf_uncty_map = self.sf_uncty_maps['%s_%s_uncty' % (jtype, wp)]  

        ix = min(max(1, sf_map.GetXaxis().FindFixBin(jet.pt)), sf_map.GetNbinsX())
        iy = min(max(1, sf_map.GetYaxis().FindFixBin(jet.eta)), sf_map.GetNbinsY())

        jx = min(max(1, sf_uncty_map.GetXaxis().FindFixBin(jet.pt)), sf_uncty_map.GetNbinsX())
        jy = min(max(1, sf_uncty_map.GetYaxis().FindFixBin(jet.eta)), sf_uncty_map.GetNbinsY())

        return sf_map.GetBinContent(ix, iy), sf_map.GetBinError(ix, iy), sf_uncty_map.GetBinContent(jx, jy)

