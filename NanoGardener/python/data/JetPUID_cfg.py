# PUID scale factors are downloaded from
# https://lathomas.web.cern.ch/lathomas/JetMETStuff/PUIDStudies/EffMaps/JetPUID_effcyandSF.root
# following Laurent's talk in
# https://indico.cern.ch/event/840819

_jet_puid_sf = {
    '2016': {'source': 'LatinoAnalysis/NanoGardener/python/data/JetPUID_effcyandSF.root'},
    '2017': {'source': 'LatinoAnalysis/NanoGardener/python/data/JetPUID_effcyandSF.root'},
    '2018': {'source': 'LatinoAnalysis/NanoGardener/python/data/JetPUID_effcyandSF.root'}
}

for jet in ['real', 'pu']:
    for wp, iwp in [('loose', 'L'), ('medium', 'M'), ('tight', 'T')]:
        for year, jcfg in _jet_puid_sf.iteritems():
            jcfg['%s_%s' % (jet, wp)] = 'SF%sjets_%s_%s' % (jet, iwp, year)

jet_puid_sf = {}

for cmssw in ['Full2016', 'Full2016v2_hmumu', 'Full2016v4', 'Full2016v5','Full2016v5_mh', 'Full2016v2']:
    jet_puid_sf[cmssw] = _jet_puid_sf['2016']

for cmssw in ['Full2017v2LP19', 'Study2017', 'Full2017', 'Full2017v2', 'Full2017v5', 'Full2017v4']:
    jet_puid_sf[cmssw] = _jet_puid_sf['2017']

for cmssw in ['Full2018','Full2018v4', 'Full2018v5']:
    jet_puid_sf[cmssw] = _jet_puid_sf['2018']

del _jet_puid_sf
