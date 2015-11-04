
eosProdBase= '/eos/cms/'
eosTargBase= '/eos/user/x/xjanssen/HWW2015/'

Productions= {

  '21Oct_25ns_MC'   : {
                        'isData'  : False ,
                        'samples' : 'LatinoTrees/AnalysisStep/test/crab/samples/samples_spring15_miniaodv2_25ns.py' , 
                        'dirExt'  : 'LatinoTrees'
                      } ,

}


Steps= {

# ... Chains

  'MCl2sel' :     {
                  'isChain'    : True ,
                  'do4MC'      : True , 
                  'do4Data'    : True ,
                  'subTargets' : ['mcweights','puadder','baseW','wwNLL','l2sel']
                },

# ... Individual Steps

  'mcweights' : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : False ,
                  'command'    : 'gardener.py mcweightsfiller '
                } ,

  'puadder'   : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : False ,
                  'preproc'    : 'PUCalc' ,
                  'command'    : 'gardener.py puadder --data=RPLME --HistName=pileup --branch=puW --kind=trpu '
                } ,

  'baseW'     : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : False ,
                  'preproc'    : 'baseWCalc' ,
                  'command'    : 'gardener.py -v \'baseW/F=RPLME\' '

                } ,

  'wwNLL'     : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : False ,
                  'preproc'    : 'POWHEG_Only' ,
                  'command'    : 'gardener.py wwNLLcorrections -m \'powheg\' '
                },

  'l2sel'    : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : True  ,
                  'command'    : 'gardener.py l2selfiller '
               },
}

