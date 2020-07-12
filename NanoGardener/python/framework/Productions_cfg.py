
Productions = { 
   
   'summer16_nAOD_v1' : {
                          'isData'  : False ,
                          'samples' : 'LatinoAnalysis/NanoGardener/python/framework/samples/summer16_nAOD_v1.py' ,
                          'cmssw'   : 'Full2016' ,  
                          'year'    : '2016' , 
                          'xsFile'  : 'LatinoAnalysis/NanoGardener/python/framework/samples/samplesCrossSections2016.py' ,
                          'YRver'   : ['YR4','13TeV'] ,
                        },

   'summer16_nAOD_v1_test' : {
                          'isData'  : False ,
                          'samples' : 'LatinoAnalysis/NanoGardener/python/framework/samples/summer16_nAOD_v1_test.py' ,
                          'cmssw'   : 'Full2016' ,
                          'year'    : '2016' , 
                          'xsFile'  : 'LatinoAnalysis/NanoGardener/python/framework/samples/samplesCrossSections2016.py' ,
                          'YRver'   : ['YR4','13TeV'] ,
                        },                    

   'Run2017_nAOD_v1_Study2017':  {
                         'isData'  : True ,
                         'jsonFile'   : '"%s/src/LatinoAnalysis/NanoGardener/python/data/certification/Cert_294927-306462_13TeV_EOY2017ReReco_Collisions17_JSON.txt"  % os.environ["CMSSW_BASE"]',
                         'samples' : 'LatinoAnalysis/NanoGardener/python/framework/samples/Run2017_nAOD_v1.py' ,
                         'cmssw'   : 'Study2017' ,
                         'year'    : '2017' , 
                         'xsFile'  : 'LatinoAnalysis/NanoGardener/python/framework/samples/samplesCrossSections2017.py' ,
                         'YRver'   : ['YR4','13TeV'] ,
                   },

   'Fall2017_nAOD_v1_Study2017':  {
                         'isData'  : False ,
                         'samples' : 'LatinoAnalysis/NanoGardener/python/framework/samples/fall17_nAOD_v1.py' ,
                         'cmssw'   : 'Study2017' ,
                         'year'    : '2017' , 
                         'xsFile'  : 'LatinoAnalysis/NanoGardener/python/framework/samples/samplesCrossSections2017.py' ,
                         'YRver'   : ['YR4','13TeV'] ,
                   },               

   'Run2018_nAOD_v1_Study2018':  {
                         'isData'  : True ,
                         'jsonFile'   : '"%s/src/LatinoAnalysis/NanoGardener/python/data/certification/Cert_314472-325175_13TeV_PromptReco_Collisions18_JSON.txt"  % os.environ["CMSSW_BASE"]',
                         'samples' : 'LatinoAnalysis/NanoGardener/python/framework/samples/Run2018_nAOD_v1.py' ,
                         'cmssw'   : 'Full2018' ,
                         'year'    : '2018' ,
                         'xsFile'  : 'LatinoAnalysis/NanoGardener/python/framework/samples/samplesCrossSections2018.py' , ## for the moment just copy 'samplesCrossSections2017.py'
                         'YRver'   : ['YR4','13TeV'] ,
                   },


   # ---- BAD electron ID: 

   'Run2017_nAOD_v1_Full2017':  {
                         'isData'  : True ,
                         'jsonFile'   : '"%s/src/LatinoAnalysis/NanoGardener/python/data/certification/Cert_294927-306462_13TeV_EOY2017ReReco_Collisions17_JSON.txt"  % os.environ["CMSSW_BASE"]',
                         'samples' : 'LatinoAnalysis/NanoGardener/python/framework/samples/Run2017_nAOD_v1.py' ,
                         'cmssw'   : 'Full2017' ,
                         'year'    : '2017' , 
                   },

   'Fall2017_nAOD_v1_Full2017':  {
                         'isData'  : False ,
                         'samples' : 'LatinoAnalysis/NanoGardener/python/framework/samples/fall17_nAOD_v1.py' ,
                         'cmssw'   : 'Full2017' ,
                         'year'    : '2017' , 
                         'xsFile'  : 'LatinoAnalysis/NanoGardener/python/framework/samples/samplesCrossSections2017.py' ,
                         'YRver'   : ['YR4','13TeV'] ,
                   },     

################################### nAODv2 : 2017v2 ######################################

 # -------- 2016 DATA 94X nAODv2
 'Run2016_94X_nAODv2_Full2016v2': {
                       'isData'  : True ,
                       'jsonFile'   : '"%s/src/LatinoAnalysis/NanoGardener/python/data/certification/Cert_271036-284044_13TeV_23Sep2016ReReco_Collisions16_JSON.txt"  %os.environ["CMSSW_BASE"]',
                       'samples' : 'LatinoAnalysis/NanoGardener/python/framework/samples/Run2016_94X_nAODv2.py' ,
                       'cmssw'   : 'Full2016v2',
                       'year'    : '2016' ,
                   },

 # -------- 2016 DATA 94X nAODv2
 'Run2016_94X_nAODv2_TESTFW': {
                       'isData'  : True ,
                       'jsonFile'   : '"%s/src/LatinoAnalysis/NanoGardener/python/data/certification/Cert_TESTFW_13TeV_23Sep2016ReReco_Collisions16_JSON.txt"  %os.environ["CMSSW_BASE"]',
                       'samples' : 'LatinoAnalysis/NanoGardener/python/framework/samples/Run2016_94X_nAODv2.py' ,
                       'cmssw'   : 'Full2016v2',
                       'year'    : '2016' ,
                   },

 # -------- 2016 DATA 94X nAODv2
 'Run2016_94X_nAODv2_TESTFW142': {
                       'isData'  : True ,
                       'jsonFile'   : '"%s/src/LatinoAnalysis/NanoGardener/python/data/certification/Cert_TESTFW142_13TeV_23Sep2016ReReco_Collisions16_JSON.txt"  %os.environ["CMSSW_BASE"]',
                       'samples' : 'LatinoAnalysis/NanoGardener/python/framework/samples/Run2016_94X_nAODv2.py' ,
                       'cmssw'   : 'Full2016v2',
                       'year'    : '2016' ,
                   },

  # ---- Embedding 2017 ...

   'Embedding2017_nAOD_v1_Full2017v2':  {
                         'isData'  : True ,
                         'jsonFile'   : '"%s/src/LatinoAnalysis/NanoGardener/python/data/certification/Cert_294927-306462_13TeV_EOY2017ReReco_Collisions17_JSON.txt"  % os.environ["CMSSW_BASE"]',
                         'samples' : 'LatinoAnalysis/NanoGardener/python/framework/samples/Embed2017_nAODv2.py' ,
                         'cmssw'   : 'Full2017v2' ,
                         'year'    : '2017' , 
                   },

  # ---- Relaxed loose ID / misHit / ...

   'Run2017_nAOD_v1_Full2017v2':  {
                         'isData'  : True ,
                         'jsonFile'   : '"%s/src/LatinoAnalysis/NanoGardener/python/data/certification/Cert_294927-306462_13TeV_EOY2017ReReco_Collisions17_JSON.txt"  % os.environ["CMSSW_BASE"]',
                         'samples' : 'LatinoAnalysis/NanoGardener/python/framework/samples/Run2017_nAOD_v1.py' ,
                         'cmssw'   : 'Full2017v2' ,
                         'year'    : '2017' , 
                   },

   'Fall2017_nAOD_v1_Full2017v2':  {
                         'isData'  : False ,
                         'samples' : 'LatinoAnalysis/NanoGardener/python/framework/samples/fall17_nAOD_v1.py' ,
                         'cmssw'   : 'Full2017v2' ,
                         'year'    : '2017' , 
                         'JESGT'   : 'Fall17_17Nov2017_V6_MC' , 
                         'xsFile'  : 'LatinoAnalysis/NanoGardener/python/framework/samples/samplesCrossSections2017.py' ,
                         'YRver'   : ['YR4','13TeV'] ,
                   },           

# ---- Full2017v2LP19 

   'Run2017_nAOD_v1_Full2017v2LP19':  {
                         'isData'  : True ,
                         'jsonFile'   : '"%s/src/LatinoAnalysis/NanoGardener/python/data/certification/Cert_294927-306462_13TeV_EOY2017ReReco_Collisions17_JSON.txt"  % os.environ["CMSSW_BASE"]',
                         'samples' : 'LatinoAnalysis/NanoGardener/python/framework/samples/Run2017_nAOD_v1.py' ,
                         'cmssw'   : 'Full2017v2LP19' ,
                         'year'    : '2017' ,
                   },

   'Fall2017_nAOD_v1_Full2017v2LP19':  {
                         'isData'  : False ,
                         'samples' : 'LatinoAnalysis/NanoGardener/python/framework/samples/fall17_nAOD_v1.py' ,
                         'cmssw'   : 'Full2017v2LP19' ,
                         'year'    : '2017' ,
                         'JESGT'   : 'Fall17_17Nov2017_V6_MC' ,
                         'xsFile'  : 'LatinoAnalysis/NanoGardener/python/framework/samples/samplesCrossSections2017.py' ,
                         'YRver'   : ['YR4','13TeV'] ,
                   },


################################### nAODv3 ######################################

 # -------- 2016 DATA 94X nAODv3
 'Run2016_94X_nAODv3_Full2016v2': {
                       'isData'  : True ,
                       'jsonFile'   : '"%s/src/LatinoAnalysis/NanoGardener/python/data/certification/Cert_271036-284044_13TeV_23Sep2016ReReco_Collisions16_JSON.txt"  %os.environ["CMSSW_BASE"]',
                       'samples' : 'LatinoAnalysis/NanoGardener/python/framework/samples/Run2016_94X_nAODv3.py' ,
                       'cmssw'   : 'Full2016v2',
                       'year'    : '2016' , 
                   },

 # -------- 2016 DATA 94X nAODv3
 'Run2016_94X_nAODv3_TESTFW': {
                       'isData'  : True ,
                       'jsonFile'   : '"%s/src/LatinoAnalysis/NanoGardener/python/data/certification/Cert_TESTFW_13TeV_23Sep2016ReReco_Collisions16_JSON.txt"  %os.environ["CMSSW_BASE"]',
                       'samples' : 'LatinoAnalysis/NanoGardener/python/framework/samples/Run2016_94X_nAODv3.py' ,
                       'cmssw'   : 'Full2016v2',
                       'year'    : '2016' ,
                   },

 # -------- 2016 MC 94X nAODv3
 'Summer16_94X_nAODv3_Full2016v2': {
                       'isData'  : False ,
                       'samples' : 'LatinoAnalysis/NanoGardener/python/framework/samples/Summer16_94X_nAODv3.py' ,
                       'cmssw'   : 'Full2016v2' ,
                       'year'    : '2016' , 
                       'JESGT'   : 'Summer16_23Sep2016V4_MC' ,
                       'xsFile'  : 'LatinoAnalysis/NanoGardener/python/framework/samples/samplesCrossSections2016.py' ,
                       'YRver'   : ['YR4','13TeV'] ,
                   },

################################### nAODv4 ######################################

 # -------- 2016 DATA 102X nAODv4
 'Run2016_102X_nAODv4_Full2016v4': {
                       'isData'  : True ,
                       'jsonFile'   : '"%s/src/LatinoAnalysis/NanoGardener/python/data/certification/Cert_271036-284044_13TeV_23Sep2016ReReco_Collisions16_JSON.txt"  % os.environ["CMSSW_BASE"]',
                       'samples' : 'LatinoAnalysis/NanoGardener/python/framework/samples/Run2016_102X_nAODv4.py' ,
                       'cmssw'   : 'Full2016v4',
                       'year'    : '2016' , 
                   }, 

 # -------- 2016 DATA 102X nAODv4
 'Run2016_102X_nAODv4_Full2016v5': {
                       'isData'  : True ,
                       'jsonFile'   : '"%s/src/LatinoAnalysis/NanoGardener/python/data/certification/Cert_271036-284044_13TeV_23Sep2016ReReco_Collisions16_JSON.txt"  % os.environ["CMSSW_BASE"]',
                       'samples' : 'LatinoAnalysis/NanoGardener/python/framework/samples/Run2016_102X_nAODv4.py' ,
                       'cmssw'   : 'Full2016v5',
                       'year'    : '2016' ,
                   },

 # -------- 2016 DATA 102X nAODv4 + monoH
 'Run2016_102X_nAODv4_Full2016v5_mh': {
                       'isData'  : True ,
                       'jsonFile'   : '"%s/src/LatinoAnalysis/NanoGardener/python/data/certification/Cert_271036-284044_13TeV_23Sep2016ReReco_Collisions16_JSON.txt"  % os.environ["CMSSW_BASE"]',
                       'samples' : 'LatinoAnalysis/NanoGardener/python/framework/samples/Run2016_102X_nAODv4.py' ,
                       'cmssw'   : 'Full2016v5_mh',
                       'year'    : '2016' ,
                   },



 # -------- 2016 MC 102X nAODv4
 'Summer16_102X_nAODv4_Full2016v4': {
                       'isData'  : False ,
                       'samples' : 'LatinoAnalysis/NanoGardener/python/framework/samples/Summer16_102X_nAODv4.py' ,
                       'cmssw'   : 'Full2016v4' ,
                       'year'    : '2016' ,
                       'JESGT'   : 'Summer16_07Aug2017_V11_MC' ,
                       'xsFile'  : 'LatinoAnalysis/NanoGardener/python/framework/samples/samplesCrossSections2016.py' ,
                       'YRver'   : ['YR4','13TeV'] ,
                   },  

 # -------- 2016 MC 102X nAODv4
 'Summer16_102X_nAODv4_Full2016v5': {
                       'isData'  : False ,
                       'samples' : 'LatinoAnalysis/NanoGardener/python/framework/samples/Summer16_102X_nAODv4.py' ,
                       'cmssw'   : 'Full2016v5' ,
                       'year'    : '2016' ,
                       'JESGT'   : 'Summer16_07Aug2017_V11_MC' ,
                       'xsFile'  : 'LatinoAnalysis/NanoGardener/python/framework/samples/samplesCrossSections2016.py' ,
                       'YRver'   : ['YR4','13TeV'] ,
                   },

 # -------- 2016 MC 102X nAODv4 + monoH
 'Summer16_102X_nAODv4_Full2016v5_mh': {
                       'isData'  : False ,
                       'samples' : 'LatinoAnalysis/NanoGardener/python/framework/samples/Summer16_102X_nAODv4.py' ,
                       'cmssw'   : 'Full2016v5_mh' ,
                       'year'    : '2016' ,
                       'JESGT'   : 'Summer16_07Aug2017_V11_MC' ,
                       'xsFile'  : 'LatinoAnalysis/NanoGardener/python/framework/samples/samplesCrossSections2016.py' ,
                       'YRver'   : ['YR4','13TeV'] ,
                   },



 # -------- 2016 MC 102X nAODv4 Hmumu
 'Summer16_102X_nAODv4_Full2016v4_Hmumu': {
                       'isData'  : False ,
                       'samples' : 'LatinoAnalysis/NanoGardener/python/framework/samples/Summer16_Hmumu_102X_nAODv4.py' ,
                       'cmssw'   : 'Full2016v2_hmumu' ,
                       'year'    : '2016' ,
                       'JESGT'   : 'Summer16_07Aug2017_V11_MC' ,
                       'xsFile'  : 'LatinoAnalysis/NanoGardener/python/framework/samples/samplesCrossSections2016.py' ,
                       'YRver'   : ['YR4','13TeV'] ,
                   },  

 # -------- 2016 Susy 102X nAODv4
 'Summer16FS_102X_nAODv4_Full2016v4': {
                       'isData'  : False ,
                       'samples' : 'LatinoAnalysis/NanoGardener/python/framework/samples/Summer16FS_102X_nAODv4.py' ,
                       'cmssw'   : 'Full2016v4' ,
                       'year'    : '2016' ,
                       'xsFile'  : 'LatinoAnalysis/NanoGardener/python/framework/samples/samplesCrossSections2016.py' ,
                       'YRver'   : ['YR4','13TeV'] ,
                   },

 # -------- 2016 Embedding 102X nAODv4
 'Embedding2016_102X_nAODv4_Full2016v4': {
                       'isData'  : True ,
                       'jsonFile'   : '"%s/src/LatinoAnalysis/NanoGardener/python/data/certification/Cert_271036-284044_13TeV_23Sep2016ReReco_Collisions16_JSON.txt"  % os.environ["CMSSW_BASE"]',
                       'samples' : 'LatinoAnalysis/NanoGardener/python/framework/samples/Embed2016_nAODv4.py' ,
                       'cmssw'   : 'Full2016v4',
                       'year'    : '2016' , 
                   }, 

 # -------- 2017 DATA 102X nAODv4 (TODO: samples/Run2017_102X_nAODv4.py)
 'Run2017_102X_nAODv4_Full2017v4': {
                       'isData'  : True ,
                       'jsonFile'   : '"%s/src/LatinoAnalysis/NanoGardener/python/data/certification/Cert_294927-306462_13TeV_EOY2017ReReco_Collisions17_JSON.txt"  % os.environ["CMSSW_BASE"]',
                       'samples' : 'LatinoAnalysis/NanoGardener/python/framework/samples/Run2017_102X_nAODv4.py' ,
                       'cmssw'   : 'Full2017v4',
                       'year'    : '2017' , 
                   },

 # -------- 2017 MC 102X nAODv4
 'Fall2017_102X_nAODv4_Full2017v4' : {
                       'isData'  : False ,
                       'samples' : 'LatinoAnalysis/NanoGardener/python/framework/samples/fall17_102X_nAODv4.py' ,
                       'cmssw'   : 'Full2017v4',
                       'year'    : '2017' ,
                       'JESGT'   : 'Fall17_17Nov2017_V32_MC' ,
                       'xsFile'  : 'LatinoAnalysis/NanoGardener/python/framework/samples/samplesCrossSections2017.py' ,
                       'YRver'   : ['YR4','13TeV'] ,
                   }, 

 # -------- 2017 Embedding 102X nAODv4
 'Embedding2017_102X_nAODv4_Full2017v4': {
                       'isData'  : True ,
                       'jsonFile'   : '"%s/src/LatinoAnalysis/NanoGardener/python/data/certification/Cert_294927-306462_13TeV_EOY2017ReReco_Collisions17_JSON.txt"  % os.environ["CMSSW_BASE"]',
                       'samples' : 'LatinoAnalysis/NanoGardener/python/framework/samples/Embed2017_nAODv4.py' ,
                       'cmssw'   : 'Full2017v4',
                       'year'    : '2017' , 
                   },

 # -------- 2017 DATA 102X nAODv4: Full2017v5 -> Tight Isolation 
 'Run2017_102X_nAODv4_Full2017v5': {
                       'isData'  : True ,
                       'jsonFile'   : '"%s/src/LatinoAnalysis/NanoGardener/python/data/certification/Cert_294927-306462_13TeV_EOY2017ReReco_Collisions17_JSON.txt"  % os.environ["CMSSW_BASE"]',
                       'samples' : 'LatinoAnalysis/NanoGardener/python/framework/samples/Run2017_102X_nAODv4.py' ,
                       'cmssw'   : 'Full2017v5',
                       'year'    : '2017' ,
                   },

 # -------- 2017 MC 102X nAODv4 : Full2017v5 -> Tight Isolation
 'Fall2017_102X_nAODv4_Full2017v5' : {
                       'isData'  : False ,
                       'samples' : 'LatinoAnalysis/NanoGardener/python/framework/samples/fall17_102X_nAODv4.py' ,
                       'cmssw'   : 'Full2017v5',
                       'year'    : '2017' ,
                       'JESGT'   : 'Fall17_17Nov2017_V32_MC' ,
                       'xsFile'  : 'LatinoAnalysis/NanoGardener/python/framework/samples/samplesCrossSections2017.py' ,
                       'YRver'   : ['YR4','13TeV'] ,
                   },


 # -------- 2018 DATA 102X nAODv4 - 14Sep2018 production
 'Run2018_102X_nAODv4_14Sep_Full2018' : {
                       'isData'  : True ,
                       'jsonFile'   : '"%s/src/LatinoAnalysis/NanoGardener/python/data/certification/Cert_314472-325175_13TeV_PromptReco_Collisions18_JSON.txt"  % os.environ["CMSSW_BASE"]',
                       'samples' : 'LatinoAnalysis/NanoGardener/python/framework/samples/Run2018_102X_nAODv4_14Sep2018.py' ,
                       'cmssw'   : 'Full2018',
                       'year'    : '2018' ,
                   },

 # -------- 2018 DATA 102X nAODv4 - 14Dec2018 production
 'Run2018_102X_nAODv4_14Dec_Full2018v4' : {
                       'isData'  : True ,
                       'jsonFile'   : '"%s/src/LatinoAnalysis/NanoGardener/python/data/certification/Cert_314472-325175_13TeV_17SeptEarlyReReco2018ABC_PromptEraD_Collisions18_JSON.txt"  % os.environ["CMSSW_BASE"]',
                       'samples' : 'LatinoAnalysis/NanoGardener/python/framework/samples/Run2018_102X_nAODv4_14Dec2018.py' ,
                       'cmssw'   : 'Full2018v4',
                       'year'    : '2018' ,
                   },

 # -------- 2018 MC 102X nAODv4
 'Autumn18_102X_nAODv4_Full2018': {
                       'isData'  : False ,
                       'samples' : 'LatinoAnalysis/NanoGardener/python/framework/samples/Autumn18_102X_nAODv4.py' ,
                       'cmssw'   : 'Full2018' ,
                       'year'    : '2018' ,
                       'JESGT'   : 'Autumn18_V8_MC' ,
                       'xsFile'  : 'LatinoAnalysis/NanoGardener/python/framework/samples/samplesCrossSections2018.py' ,
                       'YRver'   : ['YR4','13TeV'] ,
                   },

 # -------- 2018 MC 102X nAODv4 
 'Autumn18_102X_nAODv4_GTv16_Full2018v4': {
                       'isData'  : False ,
                       'samples' : 'LatinoAnalysis/NanoGardener/python/framework/samples/Autumn18_102X_nAODv4_v16.py' ,
                       'cmssw'   : 'Full2018v4' ,
                       'year'    : '2018' ,
                       'JESGT'   : 'Autumn18_V8_MC' ,
                       'xsFile'  : 'LatinoAnalysis/NanoGardener/python/framework/samples/samplesCrossSections2018.py' ,
                       'YRver'   : ['YR4','13TeV'] ,
                   },


#################################### nAODv5 DATA ##############################################

 # -------- 2016 DATA 102X nAODv5 : Full2016v6
 'Run2016_102X_nAODv5_Full2016v6': {
                       'isData'  : True ,
                       'jsonFile'   : '"%s/src/LatinoAnalysis/NanoGardener/python/data/certification/Cert_271036-284044_13TeV_23Sep2016ReReco_Collisions16_JSON.txt"  % os.environ["CMSSW_BASE"]',
                       'samples' : 'LatinoAnalysis/NanoGardener/python/framework/samples/Run2016_102X_nAODv5.py' ,
                       'cmssw'   : 'Full2016v6',
                       'year'    : '2016' ,
                   },



 # -------- 2017 DATA 102X nAODv5: Full2017v6 
 'Run2017_102X_nAODv5_Full2017v6': {
                       'isData'  : True ,
                       'jsonFile'   : '"%s/src/LatinoAnalysis/NanoGardener/python/data/certification/Cert_294927-306462_13TeV_EOY2017ReReco_Collisions17_JSON.txt"  % os.environ["CMSSW_BASE"]',
                       'samples' : 'LatinoAnalysis/NanoGardener/python/framework/samples/Run2017_102X_nAODv5.py' ,
                       'cmssw'   : 'Full2017v6',
                       'year'    : '2017' ,
                   },


 # -------- 2018 DATA 102X nAODv5: Full2018v5
'Run2018_102X_nAODv5_Full2018v5' : {
                       'isData'  : True ,
                       'jsonFile'   : '"%s/src/LatinoAnalysis/NanoGardener/python/data/certification/Cert_314472-325175_13TeV_17SeptEarlyReReco2018ABC_PromptEraD_Collisions18_JSON.txt"  % os.environ["CMSSW_BASE"]',
                       'samples' : 'LatinoAnalysis/NanoGardener/python/framework/samples/Run2018_102X_nAODv5.py' ,
                       'cmssw'   : 'Full2018v5',
                       'year'    : '2018' ,
                   },

 # -------- 2018 DATA 102X nAODv5: Full2017v6
'Run2018_102X_nAODv5_Full2018v6' : {
                       'isData'  : True ,
                       'jsonFile'   : '"%s/src/LatinoAnalysis/NanoGardener/python/data/certification/Cert_314472-325175_13TeV_17SeptEarlyReReco2018ABC_PromptEraD_Collisions18_JSON.txt"  % os.environ["CMSSW_BASE"]',
                       'samples' : 'LatinoAnalysis/NanoGardener/python/framework/samples/Run2018_102X_nAODv5.py' ,
                       'cmssw'   : 'Full2018v6',
                       'year'    : '2018' ,
                   },



#################################### nAODv5 MC ##############################################

 # -------- 2016 MC 102X nAODv4
 'Summer16_102X_nAODv5_SigOnly_Full2016v5': {
                       'isData'  : False ,
                       'samples' : 'LatinoAnalysis/NanoGardener/python/framework/samples/Summer16_102X_nAODv5_SigOnly.py' ,
                       'cmssw'   : 'Full2016v5' ,
                       'year'    : '2016' ,
                       'JESGT'   : 'Summer16_07Aug2017_V11_MC' ,
                       'xsFile'  : 'LatinoAnalysis/NanoGardener/python/framework/samples/samplesCrossSections2016.py' ,
                       'YRver'   : ['YR4','13TeV'] ,
                   },

 # -------- 2016 MC 102X nAODv4
 'Summer16_102X_nAODv5_SigOnly_Full2016v5_mh': {
                       'isData'  : False ,
                       'samples' : 'LatinoAnalysis/NanoGardener/python/framework/samples/Summer16_102X_nAODv5_SigOnly.py' ,
                       'cmssw'   : 'Full2016v5_mh' ,
                       'year'    : '2016' ,
                       'JESGT'   : 'Summer16_07Aug2017_V11_MC' ,
                       'xsFile'  : 'LatinoAnalysis/NanoGardener/python/framework/samples/samplesCrossSections2016.py' ,
                       'YRver'   : ['YR4','13TeV'] ,
                   },


 # -------- 2016 MC 102X nAODv5 + Full2016v6
 'Summer16_102X_nAODv5_Full2016v6': {
                       'isData'  : False ,
                       'samples' : 'LatinoAnalysis/NanoGardener/python/framework/samples/Summer16_102X_nAODv5.py' ,
                       'cmssw'   : 'Full2016v6' ,
                       'year'    : '2016' ,
                       'JESGT'   : 'Summer16_07Aug2017_V11_MC' ,
                       'xsFile'  : 'LatinoAnalysis/NanoGardener/python/framework/samples/samplesCrossSections2016.py' ,
                       'YRver'   : ['YR4','13TeV'] ,
                   },


 # -------- 2017 MC 102X nAODv5 : Full2017v5 -> Tight Isolation
 'Fall2017_102X_nAODv5_SigOnly_Full2017v5' : {
                       'isData'  : False ,
                       'samples' : 'LatinoAnalysis/NanoGardener/python/framework/samples/fall17_102X_nAODv5_SigOnly.py' ,
                       'cmssw'   : 'Full2017v5',
                       'year'    : '2017' ,
                       'JESGT'   : 'Fall17_17Nov2017_V32_MC' ,
                       'xsFile'  : 'LatinoAnalysis/NanoGardener/python/framework/samples/samplesCrossSections2017.py' ,
                       'YRver'   : ['YR4','13TeV'] ,
                   },

 # -------- 2017 MC 102X nAODv5 : Full2017v6 
 'Fall2017_102X_nAODv5_Full2017v6' : {
                       'isData'  : False ,
                       'samples' : 'LatinoAnalysis/NanoGardener/python/framework/samples/fall17_102X_nAODv5.py' ,
                       'cmssw'   : 'Full2017v6',
                       'year'    : '2017' ,
                       'JESGT'   : 'Fall17_17Nov2017_V32_MC' ,
                       'xsFile'  : 'LatinoAnalysis/NanoGardener/python/framework/samples/samplesCrossSections2017.py' ,
                       'YRver'   : ['YR4','13TeV'] ,
                   },


 # -------- 2018 MC 102X nAODv5
 'Autumn18_102X_nAODv5_Full2018v5':{
                       'isData'  : False ,
                       'samples' : 'LatinoAnalysis/NanoGardener/python/framework/samples/Autumn18_102X_nAODv5.py' ,
                       'cmssw'   : 'Full2018v5' ,
                       'year'    : '2018' ,
                       'JESGT'   : 'Autumn18_V8_MC',
                       'xsFile'  : 'LatinoAnalysis/NanoGardener/python/framework/samples/samplesCrossSections2018.py' ,
                       'YRver'   : ['YR4','13TeV'] ,
                   },

 # -------- 2018 MC 102X nAODv5
 'Autumn18_102X_nAODv5_Full2018v6':{
                       'isData'  : False ,
                       'samples' : 'LatinoAnalysis/NanoGardener/python/framework/samples/Autumn18_102X_nAODv5.py' ,
                       'cmssw'   : 'Full2018v6' ,
                       'year'    : '2018' ,
                       'JESGT'   : 'Autumn18_V8_MC',
                       'xsFile'  : 'LatinoAnalysis/NanoGardener/python/framework/samples/samplesCrossSections2018.py' ,
                       'YRver'   : ['YR4','13TeV'] ,
                   },


 # -------- 2018 DATA 102X nAODv5 
 'Run2018_102X_nAODv5_Full2018v4' : {
                       'isData'  : True ,
                       'jsonFile'   : '"%s/src/LatinoAnalysis/NanoGardener/python/data/certification/Cert_314472-325175_13TeV_17SeptEarlyReReco2018ABC_PromptEraD_Collisions18_JSON.txt"  % os.environ["CMSSW_BASE"]',
                       'samples' : 'LatinoAnalysis/NanoGardener/python/framework/samples/Run2018_102X_nAODv5.py' ,
                       'cmssw'   : 'Full2018v4',
                       'year'    : '2018' ,
                   },


#################################### nAODv5 EMBEDDING ##############################################

 # -------- 2016 DATA 102X nAODv5 : Full2016v6
 'Embedding2016_102X_nAODv5_Full2016v6': {
                       'isData'  : True ,
                       'jsonFile'   : '"%s/src/LatinoAnalysis/NanoGardener/python/data/certification/Cert_271036-284044_13TeV_23Sep2016ReReco_Collisions16_JSON.txt"  % os.environ["CMSSW_BASE"]',
                       'samples' : 'LatinoAnalysis/NanoGardener/python/framework/samples/Embed2016_nAODv5.py' ,
                       'cmssw'   : 'Full2016v6',
                       'year'    : '2016' ,
                   },

 # -------- 2017 DATA 102X nAODv5: Full2017v6 
 'Embedding2017_102X_nAODv5_Full2017v6': {
                       'isData'  : True ,
                       'jsonFile'   : '"%s/src/LatinoAnalysis/NanoGardener/python/data/certification/Cert_294927-306462_13TeV_EOY2017ReReco_Collisions17_JSON.txt"  % os.environ["CMSSW_BASE"]',
                       'samples' : 'LatinoAnalysis/NanoGardener/python/framework/samples/Embed2017_nAODv5.py' ,
                       'cmssw'   : 'Full2017v6',
                       'year'    : '2017' ,
                   },

 # -------- 2018 Embedding 102X nAODv5
 'Embedding2018_102X_nAODv5_Full2018v5': {
                       'isData'  : True ,
                       'jsonFile'   : '"%s/src/LatinoAnalysis/NanoGardener/python/data/certification/Cert_314472-325175_13TeV_17SeptEarlyReReco2018ABC_PromptEraD_Collisions18_JSON.txt"  % os.environ["CMSSW_BASE"]',
                       'samples' : 'LatinoAnalysis/NanoGardener/python/framework/samples/Embed2018_nAODv5.py' ,
                       'cmssw'   : 'Full2018v5',
                       'year'    : '2018' ,
                   }, 


#################################### nAODv6 DATA  ##############################################

 # -------- 2016 DATA 102X nAODv7: Full2016v7
 'Run2016_102X_nAODv7_Full2016v7': {
                       'isData'  : True ,
                       'jsonFile'   : '"%s/src/LatinoAnalysis/NanoGardener/python/data/certification/Cert_271036-284044_13TeV_23Sep2016ReReco_Collisions16_JSON.txt"  % os.environ["CMSSW_BASE"]',
                       'samples' : 'LatinoAnalysis/NanoGardener/python/framework/samples/Run2016_102X_nAODv7.py' ,
                       'cmssw'   : 'Full2016v7',
                       'year'    : '2016' ,
                   },

 # -------- 2017 DATA 102X nAODv7: Full2017v7
 'Run2017_102X_nAODv7_Full2017v7': {
                       'isData'  : True ,
                       'jsonFile'   : '"%s/src/LatinoAnalysis/NanoGardener/python/data/certification/Cert_294927-306462_13TeV_EOY2017ReReco_Collisions17_JSON.txt"  % os.environ["CMSSW_BASE"]',
                       'samples' : 'LatinoAnalysis/NanoGardener/python/framework/samples/Run2017_102X_nAODv7.py' ,
                       'cmssw'   : 'Full2017v7',
                       'year'    : '2017' ,
                   },

 # -------- 2018 DATA 102X nAODv7: Full2018v7
 'Run2018_102X_nAODv7_Full2018v7': {
                       'isData'  : True ,
                       'jsonFile'   : '"%s/src/LatinoAnalysis/NanoGardener/python/data/certification/Cert_314472-325175_13TeV_17SeptEarlyReReco2018ABC_PromptEraD_Collisions18_JSON.txt"  % os.environ["CMSSW_BASE"]',
                       'samples' : 'LatinoAnalysis/NanoGardener/python/framework/samples/Run2018_102X_nAODv7.py' ,
                       'cmssw'   : 'Full2018v7',
                       'year'    : '2018' ,
                   },

 # -------- 2018 DATA 102X nAODv6: Full2018v6
'Run2018_102X_nAODv6_Full2018v6' : {
                       'isData'  : True ,
                       'jsonFile'   : '"%s/src/LatinoAnalysis/NanoGardener/python/data/certification/Cert_314472-325175_13TeV_17SeptEarlyReReco2018ABC_PromptEraD_Collisions18_JSON.txt"  % os.environ["CMSSW_BASE"]',
                       'samples' : 'LatinoAnalysis/NanoGardener/python/framework/samples/Run2018_102X_nAODv6.py' ,
                       'cmssw'   : 'Full2018v6',
                       'year'    : '2018' ,
                   },

#################################### nAODv6 MC ##############################################

 # -------- 2016 MC 102X nAODv7: Full2016v7
 'Summer16_102X_nAODv7_Full2016v7': {
                       'isData'  : False ,
                       'samples' : 'LatinoAnalysis/NanoGardener/python/framework/samples/Summer16_102X_nAODv7.py' ,
                       'cmssw'   : 'Full2016v7' ,
                       'year'    : '2016' ,
                       'JESGT'   : 'Summer16_07Aug2017_V11_MC' ,
                       'xsFile'  : 'LatinoAnalysis/NanoGardener/python/framework/samples/samplesCrossSections2016.py' ,
                       'YRver'   : ['YR4','13TeV'] ,
                   },

 # -------- 2017 MC 102X nAODv7 : Full2017v7 
 'Fall2017_102X_nAODv7_Full2017v7' : {
                       'isData'  : False ,
                       'samples' : 'LatinoAnalysis/NanoGardener/python/framework/samples/fall17_102X_nAODv7.py' ,
                       'cmssw'   : 'Full2017v7',
                       'year'    : '2017' ,
                       'JESGT'   : 'Fall17_17Nov2017_V32_MC' ,
                       'xsFile'  : 'LatinoAnalysis/NanoGardener/python/framework/samples/samplesCrossSections2017.py' ,
                       'YRver'   : ['YR4','13TeV'] ,
                   },

 # -------- 2018 MC 102X nAODv7
 'Autumn18_102X_nAODv7_Full2018v7':{
                       'isData'  : False ,
                       'samples' : 'LatinoAnalysis/NanoGardener/python/framework/samples/Autumn18_102X_nAODv7.py' ,
                       'cmssw'   : 'Full2018v7' ,
                       'year'    : '2018' ,
                       'JESGT'   : 'Autumn18_V19_MC',
                       'xsFile'  : 'LatinoAnalysis/NanoGardener/python/framework/samples/samplesCrossSections2018.py' ,
                       'YRver'   : ['YR4','13TeV'] ,
                   },

 # -------- 2018 MC 102X nAODv6
 'Autumn18_102X_nAODv6_Full2018v6':{
                       'isData'  : False ,
                       'samples' : 'LatinoAnalysis/NanoGardener/python/framework/samples/Autumn18_102X_nAODv6.py' ,
                       'cmssw'   : 'Full2018v6' ,
                       'year'    : '2018' ,
                       'JESGT'   : 'Autumn18_V19_MC',
                       'xsFile'  : 'LatinoAnalysis/NanoGardener/python/framework/samples/samplesCrossSections2018.py' ,
                       'YRver'   : ['YR4','13TeV'] ,
                   },
  
   # -------- 2016 MC 102X nAODv6
 'Summer16_102X_nAODv6_Full2016v6': {
                       'isData'  : False ,
                       'samples' : 'LatinoAnalysis/NanoGardener/python/framework/samples/Summer16_102X_nAODv6.py' ,
                       'cmssw'   : 'Full2016v6' ,
                       'year'    : '2016' ,
                       'JESGT'   : 'Summer16_07Aug2017_V11_MC' ,
                       'xsFile'  : 'LatinoAnalysis/NanoGardener/python/framework/samples/samplesCrossSections2016.py' ,
                       'YRver'   : ['YR4','13TeV'] ,
                   },

#################################### nAODv6 EMBEDDING ##############################################

 'Embedding2016_102X_nAODv6_Full2016v7' : {
                       'isData'  : True ,
                       'jsonFile'   : '"%s/src/LatinoAnalysis/NanoGardener/python/data/certification/Cert_271036-284044_13TeV_23Sep2016ReReco_Collisions16_JSON.txt"  % os.environ["CMSSW_BASE"]',
                       'samples' : 'LatinoAnalysis/NanoGardener/python/framework/samples/Embed2016_nAODv6.py' ,
                       'cmssw'   : 'Full2016v6',
                       'year'    : '2016' ,
                      },

 'Embedding2017_102X_nAODv6_Full2017v7' : {
                       'isData'  : True ,
                       'jsonFile'   : '"%s/src/LatinoAnalysis/NanoGardener/python/data/certification/Cert_294927-306462_13TeV_EOY2017ReReco_Collisions17_JSON.txt"  % os.environ["CMSSW_BASE"]',
                       'samples' : 'LatinoAnalysis/NanoGardener/python/framework/samples/Embed2017_nAODv6.py' ,
                       'cmssw'   : 'Full2017v6',
                       'year'    : '2017' ,
                      },

 'Embedding2018_102X_nAODv6_Full2018v6' : {
                       'isData'  : True ,
                       'jsonFile'   : '"%s/src/LatinoAnalysis/NanoGardener/python/data/certification/Cert_314472-325175_13TeV_17SeptEarlyReReco2018ABC_PromptEraD_Collisions18_JSON.txt"  % os.environ["CMSSW_BASE"]',
                       'samples' : 'LatinoAnalysis/NanoGardener/python/framework/samples/Embed2018_nAODv6.py' ,
                       'cmssw'   : 'Full2018v6',
                       'year'    : '2018' ,
                      },

 'Embedding2018_102X_nAODv6_Full2018v7' : {
                       'isData'  : True ,
                       'jsonFile'   : '"%s/src/LatinoAnalysis/NanoGardener/python/data/certification/Cert_314472-325175_13TeV_17SeptEarlyReReco2018ABC_PromptEraD_Collisions18_JSON.txt"  % os.environ["CMSSW_BASE"]',
                       'samples' : 'LatinoAnalysis/NanoGardener/python/framework/samples/Embed2018_nAODv6.py' ,
                       'cmssw'   : 'Full2018v7',
                       'year'    : '2018' ,
                      },

}

