import os
import ROOT

from PhysicsTools.NanoAODTools.postprocessing.framework.eventloop import Module
from PhysicsTools.NanoAODTools.postprocessing.framework.datamodel import Collection 

class JetSFMaker(Module):
    """
    Add branches for Jet ID scale factors.
    """

    def __init__(self, cmssw, puid_sf_config='LatinoAnalysis/NanoGardener/python/data/JetPUID_cfg.py'):
        cmssw_base = os.getenv('CMSSW_BASE')
        with open(cmssw_base + '/src/' + puid_sf_config) as src:
            exec(src)
            
        puid_sf_cfg = jet_puid_sf[cmssw]

        source = ROOT.TFile.Open(cmssw_base + '/src/' + puid_sf_cfg['source'])
        self.sf_maps = {}
        for jtype in ['real', 'pu']:
            for wp, iwp in [('loose', 'L'), ('medium', 'M'), ('tight', 'T')]:
                key = '%s_%s' % (jtype, wp)
                self.sf_maps[key] = source.Get(puid_sf_cfg[key])
                self.sf_maps[key].SetDirectory(0)

        source.Close()

    def beginFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        self.out = wrappedOutputTree

        for wp in ['loose', 'medium', 'tight']:
            self.out.branch('Jet_PUIDSF_%s' % wp, 'F', lenVar='nJet')
            self.out.branch('Jet_PUIDSF_%s_staterr' % wp, 'F', lenVar='nJet')

    def analyze(self, event):
        jets = Collection(event, 'Jet')

        sfs = {'loose': [], 'medium': [], 'tight': []}
        sferrs = {'loose': [], 'medium': [], 'tight': []}

        for jet in jets:
            if jet.genJetIdx == -1:
                jtype = 'pu'
            else:
                jtype = 'real'

            for wp in ['loose', 'medium', 'tight']:
                sf, err = self.get_sf(jtype, wp, jet)
                sfs[wp].append(sf)
                sferrs[wp].append(err)

        for wp in ['loose', 'medium', 'tight']:
            self.out.fillBranch('Jet_PUIDSF_%s' % wp, sfs[wp])
            self.out.fillBranch('Jet_PUIDSF_%s_staterr' % wp, sferrs[wp])

        return True

    def get_sf(self, jtype, wp, jet):
        sf_map = self.sf_maps['%s_%s' % (jtype, wp)]

        ix = min(max(1, sf_map.GetXaxis().FindFixBin(jet.pt)), sf_map.GetNbinsX())
        iy = min(max(1, sf_map.GetYaxis().FindFixBin(jet.eta)), sf_map.GetNbinsY())

        return sf_map.GetBinContent(ix, iy), sf_map.GetBinError(ix, iy)

