
Productions = { 
   
   'Fall2017_nAOD_v2_94X':  {
                         'isData'       : False ,
                         'samples'      : 'LatinoAnalysis/NanoProducer/python/samples/fall17_mAOD_v1.py' ,
                         'GlobalTag'    : '94X_mc2017_realistic_v14' ,
                         'EraModifiers' : 'Run2_2017,run2_nanoAOD_94XMiniAODv2' ,
                   },     


  # ---- Relaxed loose ID / misHit / ...

   'Run2017_nAOD_v2_94X':  {
                         'isData'  : True ,
                         'jsonFile'     : '"%s/src/LatinoAnalysis/NanoGardener/python/data/certification/Cert_294927-306462_13TeV_EOY2017ReReco_Collisions17_JSON.txt"  % os.environ["CMSSW_BASE"]',
                         'samples'      : 'LatinoAnalysis/NanoProducer/python/samples/Run2017_mAOD_v1.py' ,
                         'GlobalTag'    : '94X_mc2017_realistic_v14' ,
                         'EraModifiers' : 'Run2_2017,run2_nanoAOD_94XMiniAODv2' ,
                   },

   'Summer16_102X_nAODv4_Full2016v4': {
                         'isData'       : False ,
                         'samples'      : 'LatinoAnalysis/NanoProducer/python/samples/Summer16_102X_mAODv3.py' ,
                         'GlobalTag'    : '102X_mcRun2_asymptotic_v6' ,
                         'EraModifiers' : 'Run2_2016,run2_nanoAOD_94X2016' ,
   },
   'Fall17_102X_nAODv4_Full2017v4': {
                         'isData'       : False ,
                         'samples'      : 'LatinoAnalysis/NanoProducer/python/samples/Fall17_102X_mAODv3.py' ,
                         'GlobalTag'    : '102X_mc2017_realistic_v6' ,
                         'EraModifiers' : 'Run2_2017,run2_nanoAOD_94XMiniAODv2' ,
   },
   'Autumn18_102X_nAODv4_GTv16_Full2018v4': {
                         'isData'       : False ,
                         'samples'      : 'LatinoAnalysis/NanoProducer/python/samples/Autumn18_102X_mAODv3.py' ,
                         'GlobalTag'    : '102X_upgrade2018_realistic_v16' ,
                         'EraModifiers' : 'Run2_2018,run2_nanoAOD_102Xv1' ,
   },
}
