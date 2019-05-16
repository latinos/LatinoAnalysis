
Sites = {

  'iihe' : { 
              'lsCmd'       : 'ls' ,
              'mkDir'       : False , 
              'xrootdPath'  : 'dcap://maite.iihe.ac.be/' ,
              'srmPrefix'   : 'srm://maite.iihe.ac.be:8443' ,
              'treeBaseDir' : '/pnfs/iihe/cms/store/user/xjanssen/HWWNano/' ,
              'batchQueues' : ['localgrid@cream02']
           } ,

  'cern' : {
              'lsCmd'       : 'ls' ,
              'mkDir'       : True ,
              'xrootdPath'  : 'root://eoscms.cern.ch/' ,
              'treeBaseDir' : '/eos/cms/store/group/phys_higgs/cmshww/amassiro/HWWNano/' ,
              'batchQueues' : ['8nh','1nd','2nd','1nw']
           } ,

  'sdfarm' : {
              'lsCmd'       : 'ls' ,
              'mkDir'       : False ,
              'xrootdPath'  : 'root://cms-xrdr.private.lo:2094/',
              'treeBaseDir' : '/xrd/store/group/phys_higgs/cmshww/jhchoi/Latino/HWWNano/',
             } ,

  'ifca' : {
              'lsCmd'       : 'ls' ,
              'mkDir'       : True ,
              'xrootdPath'  : '' ,
              'srmPrefix'   : 'srm://srm01.ifca.es' ,
              'treeBaseDir' : '/gpfs/projects/tier3data/LatinosSkims/RunII/Nano/' ,
             }

}
