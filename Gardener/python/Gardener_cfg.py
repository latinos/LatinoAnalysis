
eosProdBase= '/eos/cms/'
eosTargBase= '/eos/user/x/xjanssen/HWW2015/'

Productions= {

  '21Oct_25ns_MC'   : {
                        'isData'  : False ,
                        'samples' : 'LatinoTrees/AnalysisStep/test/crab/samples/samples_spring15_miniaodv2_25ns.py' , 
                        'dirExt'  : 'LatinoTrees' ,
                        'dirExt'  : 'split' ,
                        'gDocID'  : '1wH73CYA_T4KMkl1Cw-xLTj8YG7OPqayDnP53N-lZwFQ' ,
                        #'bigSamples': ['DYJetsToLL_M-10to50'] ,
                      } ,

  '21Oct_Run2015D_05Oct2015' : {
                        'isData'  : True ,
                        'samples' : 'LatinoTrees/AnalysisStep/test/crab/samples/samples_dataD_05Oct2015_25ns.py' ,
                        #'dirExt'  : 'Run2015D_05Oct2015' ,
                        'dirExt'  : 'split' ,
                      } ,

  '21Oct_Run2015D_PromptReco' : {
                        'isData'  : True ,
                        'samples' : 'LatinoTrees/AnalysisStep/test/crab/samples/samples_dataD_PromptReco_25ns.py' ,
                        #'dirExt'  : 'Run2015D_PromptReco' ,
                        'dirExt'  : 'split' ,
                      } ,

}


Steps= {

# ... Chains

  'MC' :       {
                  'isChain'    : True ,
                  'do4MC'      : True , 
                  'do4Data'    : False,
                  'subTargets' : ['puadder','baseW','wwNLL']
                },

  'MCl2sel' :       {
                  'isChain'    : True ,
                  'do4MC'      : True ,
                  'do4Data'    : False,
                  'subTargets' : ['puadder','baseW','wwNLL','l2sel']
                },

# ... Individual Steps

  'mcwghtcount':{ 
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : False ,
                  'command'    : 'gardener.py mcweightscounter '
                },

# 'mcweights' : {
#                 'isChain'    : False ,
#                 'do4MC'      : True  ,
#                 'do4Data'    : False ,
#                 'command'    : 'gardener.py mcweightsfiller '
#               } ,

  'puadder'   : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : False ,
                  'command'    : 'gardener.py puadder --data=RPLME_puData --HistName=pileup --branch=puW --kind=trpu '
                } ,

  'puadderFix'   : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : False ,
                  'command'    : 'gardener.py puadder --data=RPLME_puData --HistName=pileup --branch=puW --kind=trpu '
                } ,

  'baseW'     : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : False ,
                  'command'    : 'gardener.py adder -v \'baseW/F=RPLME_baseW\' '

                } ,

  'wwNLL'     : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : False ,
                  'onlySample' : ['WWTo2L2Nu'] ,
                  'command'    : 'gardener.py wwNLLcorrections -m \'powheg\' '
                },

  'l2sel'    : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : True  ,
                  'command'    : 'gardener.py l2selfiller '
               },

  'hadd'     : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : True  ,
               },
}

