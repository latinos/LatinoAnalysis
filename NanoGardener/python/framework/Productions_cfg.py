
Productions = { 
   
   'summer16_nAOD_v1' : {
                          'isData'  : False ,
                          'samples' : 'LatinoAnalysis/NanoGardener/python/framework/samples/summer16_nAOD_v1.py' ,
                          'cmssw'   : 'Full2016' ,  
                          'xsFile'  : 'LatinoAnalysis/NanoGardener/python/framework/samples/samplesCrossSections2016.py' ,
                          'YRver'   : ['YR4','13TeV'] ,
                        },

   'summer16_nAOD_v1_test' : {
                          'isData'  : False ,
                          'samples' : 'LatinoAnalysis/NanoGardener/python/framework/samples/summer16_nAOD_v1_test.py' ,
                          'cmssw'   : 'Full2016' ,
                          'xsFile'  : 'LatinoAnalysis/NanoGardener/python/framework/samples/samplesCrossSections2016.py' ,
                          'YRver'   : ['YR4','13TeV'] ,
                        },                    

   'Run2017_nAOD_v1_Study2017':  {
                         'isData'  : True ,
                         'jsonFile'   : '"%s/src/LatinoAnalysis/NanoGardener/python/data/certification/Cert_294927-306462_13TeV_EOY2017ReReco_Collisions17_JSON.txt"  % os.environ["CMSSW_BASE"]',
                         'samples' : 'LatinoAnalysis/NanoGardener/python/framework/samples/Run2017_nAOD_v1.py' ,
                         'cmssw'   : 'Study2017' ,
                         'xsFile'  : 'LatinoAnalysis/NanoGardener/python/framework/samples/samplesCrossSections2017.py' ,
                         'YRver'   : ['YR4','13TeV'] ,
                   },

   'Fall2017_nAOD_v1_Study2017':  {
                         'isData'  : False ,
                         'samples' : 'LatinoAnalysis/NanoGardener/python/framework/samples/fall17_nAOD_v1.py' ,
                         'cmssw'   : 'Study2017' ,
                   },               

   # ---- BAD electron ID: 

   'Run2017_nAOD_v1_Full2017':  {
                         'isData'  : True ,
                         'jsonFile'   : '"%s/src/LatinoAnalysis/NanoGardener/python/data/certification/Cert_294927-306462_13TeV_EOY2017ReReco_Collisions17_JSON.txt"  % os.environ["CMSSW_BASE"]',
                         'samples' : 'LatinoAnalysis/NanoGardener/python/framework/samples/Run2017_nAOD_v1.py' ,
                         'cmssw'   : 'Full2017' ,
                   },

   'Fall2017_nAOD_v1_Full2017':  {
                         'isData'  : False ,
                         'samples' : 'LatinoAnalysis/NanoGardener/python/framework/samples/fall17_nAOD_v1.py' ,
                         'cmssw'   : 'Full2017' ,
                         'xsFile'  : 'LatinoAnalysis/NanoGardener/python/framework/samples/samplesCrossSections2017.py' ,
                         'YRver'   : ['YR4','13TeV'] ,
                   },     


  # ---- Relaxed loose ID / misHit / ...

   'Run2017_nAOD_v1_Full2017v2':  {
                         'isData'  : True ,
                         'jsonFile'   : '"%s/src/LatinoAnalysis/NanoGardener/python/data/certification/Cert_294927-306462_13TeV_EOY2017ReReco_Collisions17_JSON.txt"  % os.environ["CMSSW_BASE"]',
                         'samples' : 'LatinoAnalysis/NanoGardener/python/framework/samples/Run2017_nAOD_v1.py' ,
                         'cmssw'   : 'Full2017v2' ,
                   },

   'Fall2017_nAOD_v1_Full2017v2':  {
                         'isData'  : False ,
                         'samples' : 'LatinoAnalysis/NanoGardener/python/framework/samples/fall17_nAOD_v1.py' ,
                         'cmssw'   : 'Full2017v2' ,
                         'JESGT'   : 'Fall17_17Nov2017_V6_MC' , 
                         'xsFile'  : 'LatinoAnalysis/NanoGardener/python/framework/samples/samplesCrossSections2017.py' ,
                         'YRver'   : ['YR4','13TeV'] ,
                   },           

################################### 102X nAODv3 ######################################

 # -------- 2016 DATA 102X nAODv3
 'Run2016_102X_nAODv3_Full2016v3': {
                       'isData'  : True ,
                       'jsonFile'   : '"%s/src/LatinoAnalysis/NanoGardener/python/data/certification/Cert_271036-284044_13TeV_23Sep2016ReReco_Collisions16_JSON.txt"  % os.environ["CMSSW_BASE"]',
                       'samples' : 'LatinoAnalysis/NanoGardener/python/framework/samples/Run2016_102X_nAODv3.py' ,
                       'cmssw'   : 'Full2016v3',
                   }, 

 # -------- 2017 DATA 102X nAODv3 (TODO: samples/Run2017_102X_nAODv3.py)
 'Run2017_102X_nAODv3_Full2017v3': {
                       'isData'  : True ,
                       'jsonFile'   : '"%s/src/LatinoAnalysis/NanoGardener/python/data/certification/Cert_294927-306462_13TeV_EOY2017ReReco_Collisions17_JSON.txt"  % os.environ["CMSSW_BASE"]',
                       'samples' : 'LatinoAnalysis/NanoGardener/python/framework/samples/Run2017_102X_nAODv3.py' ,
                       'cmssw'   : 'Full2017v3',
                   },



}
