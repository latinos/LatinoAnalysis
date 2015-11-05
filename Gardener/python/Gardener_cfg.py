
eosProdBase= '/eos/cms/'
eosTargBase= '/eos/user/x/xjanssen/HWW2015/'

Productions= {

  '21Oct_25ns_MC'   : {
                        'isData'  : False ,
                        'samples' : 'LatinoTrees/AnalysisStep/test/crab/samples/samples_spring15_miniaodv2_25ns.py' , 
                        'dirExt'  : 'LatinoTrees' ,
                        'gDocID'  : '1wH73CYA_T4KMkl1Cw-xLTj8YG7OPqayDnP53N-lZwFQ' ,
                      } ,

}


Steps= {

# ... Chains

  'MC' :       {
                  'isChain'    : True ,
                  'do4MC'      : True , 
                  'do4Data'    : False,
                  'subTargets' : ['mcweights','puadder','baseW','wwNLL']
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
                  'command'    : 'gardener.py puadder --data=RPLME_puData --HistName=pileup --branch=puW --kind=trpu '
                } ,

  'baseW'     : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : False ,
                  'command'    : 'gardener.py -v \'baseW/F=RPLME_baseW\' '

                } ,

  'wwNLL'     : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : False ,
                  #'preproc'    : 'POWHEG_Only' ,
                  'command'    : 'gardener.py wwNLLcorrections -m \'powheg\' '
                },

  'l2sel'    : {
                  'isChain'    : False ,
                  'do4MC'      : True  ,
                  'do4Data'    : True  ,
                  'command'    : 'gardener.py l2selfiller '
               },
}

