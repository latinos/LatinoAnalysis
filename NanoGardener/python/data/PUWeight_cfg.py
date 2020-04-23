####################### PU Weight CFG ##################################

PUCfg = {

 'Full2016v2' : {
                   'srcfile'     : "auto" ,
                   'targetfiles' : { '1-5' : 'LatinoAnalysis/NanoGardener/python/data/PUweights/2016/2016BCDEF_PU.root' ,
                                     '6-7' : 'LatinoAnalysis/NanoGardener/python/data/PUweights/2016/2016GH_PU.root' ,
                                   } ,
                   'srchist'     : "pileup"   ,
                   'targethist'  : "pileup"   ,
                   'name'        : "puWeight" ,
                   'norm'        : True       ,
                   'verbose'     : False      ,
                   'nvtx_var'    : "Pileup_nTrueInt" ,
                   'doSysVar'    : True ,
                } ,

 'Full2017v2' : {
                   'srcfile'     : "auto" ,
                   'targetfiles' : { '1-1' : 'LatinoAnalysis/NanoGardener/python/data/PUweights/2017/2017B_PU.root' ,
                                     '2-2' : 'LatinoAnalysis/NanoGardener/python/data/PUweights/2017/2017C_PU.root' ,
                                     '3-3' : 'LatinoAnalysis/NanoGardener/python/data/PUweights/2017/2017D_PU.root' ,
                                     '4-4' : 'LatinoAnalysis/NanoGardener/python/data/PUweights/2017/2017E_PU.root' ,
                                     '5-5' : 'LatinoAnalysis/NanoGardener/python/data/PUweights/2017/2017F_PU.root' ,
                                   } ,
                   'srchist'     : "pileup"   ,
                   'targethist'  : "pileup"   ,
                   'name'        : "puWeight" ,
                   'norm'        : True       ,
                   'verbose'     : False      ,
                   'nvtx_var'    : "Pileup_nTrueInt" , 
                   'doSysVar'    : True , 
                } ,

 'Full2018v4' : {
                   'srcfile'     : "auto" ,
                   'targetfiles' : { '1-1' : 'LatinoAnalysis/NanoGardener/python/data/PUweights/2018/2018_PU.root' } ,
                   'srchist'     : "pileup"   ,
                   'targethist'  : "pileup"   ,
                   'name'        : "puWeight" ,
                   'norm'        : True       ,
                   'verbose'     : False      ,
                   'nvtx_var'    : "Pileup_nTrueInt" ,
                   'doSysVar'    : True ,
                } ,

}

PUCfg['Full2016v4'] = PUCfg['Full2016v2']
PUCfg['Full2016v5'] = PUCfg['Full2016v2']
PUCfg['Full2016v5_mh'] = PUCfg['Full2016v2']
PUCfg['Full2017v4'] = PUCfg['Full2017v2']
PUCfg['Full2017v5'] = PUCfg['Full2017v2']
PUCfg['Full2017v2LP19'] = PUCfg['Full2017v2']
PUCfg['Full2018v5'] = PUCfg['Full2018v4']

PUCfg['Full2016v6'] = PUCfg['Full2016v5']
PUCfg['Full2017v6'] = PUCfg['Full2017v5']
PUCfg['Full2018v6'] = PUCfg['Full2018v5']
PUCfg['Full2016v7'] = PUCfg['Full2016v5']
PUCfg['Full2017v7'] = PUCfg['Full2017v5']
PUCfg['Full2018v7'] = PUCfg['Full2018v5']
