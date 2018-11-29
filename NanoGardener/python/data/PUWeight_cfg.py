####################### PU Weight CFG ##################################

PUCfg = {

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

}
