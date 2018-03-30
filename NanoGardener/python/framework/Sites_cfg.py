
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
              'batchQueues' : ['8nh','1nd']
           } ,

  'sdfarm' : {
              'lsCmd'       : 'ls' ,
              'mkDir'       : True ,
              'xrootdPath'  : 'root://eoscms.cern.ch/' ,
              'treeBaseDir' : '/eos/cms/store/group/phys_higgs/cmshww/amassiro/HWWNano/' ,
             }

}
