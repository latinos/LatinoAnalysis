# PUID scale factors and uncertainties (PRELIMINARY based on 2016 training only) are downloaded from
# https://lathomas.web.cern.ch/lathomas/JetMETStuff/PUIDStudies/Oct2019/
# and from
# /afs/cern.ch/work/l/lathomas/public/PileUpIDScaleFactor_PreliminaryRun2/
# see twiki https://twiki.cern.ch/twiki/bin/viewauth/CMS/PileupJetID
# following Laurent's updated talk in
# https://indico.cern.ch/event/860457/ 

_jet_puid_sf = {
    '2016': {'source': 'LatinoAnalysis/NanoGardener/python/data/PUID_80XTraining_EffSFandUncties.root'},
    '2017': {'source': 'LatinoAnalysis/NanoGardener/python/data/PUID_80XTraining_EffSFandUncties.root'},
    '2018': {'source': 'LatinoAnalysis/NanoGardener/python/data/PUID_80XTraining_EffSFandUncties.root'}
}

for jet, jetTag in [('real','eff'), ('pu','mistag')]:
    for wp, iwp in [('loose', 'L'), ('medium', 'M'), ('tight', 'T')]:
        for year, jcfg in _jet_puid_sf.iteritems():
            jcfg['%s_%s' % (jet, wp)] = 'h2_%s_sf%s_%s' % (jetTag, year, iwp)
            jcfg['%s_mc_%s' % (jet, wp)] = 'h2_%s_mc%s_%s' % (jetTag, year, iwp)
            jcfg['%s_%s_uncty' % (jet, wp)] = 'h2_%s_sf%s_%s_Systuncty' % (jetTag, year, iwp)
             
jet_puid_sf = {}

for cmssw in ['Full2016', 'Full2016v2_hmumu', 'Full2016v4', 'Full2016v5','Full2016v5_mh', 'Full2016v2','Full2016v6','Full2016v7']:
    jet_puid_sf[cmssw] = _jet_puid_sf['2016']

for cmssw in ['Full2017v2LP19', 'Study2017', 'Full2017', 'Full2017v2', 'Full2017v5', 'Full2017v4','Full2017v6','Full2017v7']:
    jet_puid_sf[cmssw] = _jet_puid_sf['2017']

for cmssw in ['Full2018','Full2018v4', 'Full2018v5','Full2018v6', 'Full2018v7']:
    jet_puid_sf[cmssw] = _jet_puid_sf['2018']

del _jet_puid_sf
