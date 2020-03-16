#!/usr/bin/env python

import optparse
import LatinoAnalysis.Gardener.hwwtools as hwwtools

# functions used in everyday life ...
from LatinoAnalysis.Tools.commonTools import *


if __name__ == '__main__':

    usage = 'usage: %prog [options]'
    parser = optparse.OptionParser(usage)
    
    parser.add_option('--outputDirDatacard' , dest='outputDirDatacard' , help='output directory'                          , default='./')   
    parser.add_option('--combineLocation'   , dest='combineLocation'   , help='Combine CMSSW Directory'                   , default='./')   
    parser.add_option('--fomList'           , dest='fomList'           , help='List of Gigure of Merit'  , default=['SExpPre'] , type='string' , action='callback' , callback=list_maker('fomList',','))
    parser.add_option('--combcfg'           , dest='combcfg'           , help='Combination disctionnary'                  , default='NONE')

 
    # read default parsing options as well
    hwwtools.addOptions(parser)
    hwwtools.loadOptDefaults(parser)
    (opt, args) = parser.parse_args()

    print " configuration file = ", opt.pycfg
    print " lumi =               ", opt.lumi

    print " outputDirDatacard  = ", opt.outputDirDatacard
    print " combineLocation    = ", opt.combineLocation  
    print " Figures of Merit   = ", opt.fomList

    # FOM methods 
    fomDic = {}
    fomDic ['SExpPre'] = '-M Significance --expectSignal=1 -t -1' 
    #fomDic ['BestFit'] = '-M FitDiagnostics  --rMin=-5 --rMax=20 -t -1 --expectSignal=1 --robustFit=1' 
    #fomDic ['BestFit'] = '-M FitDiagnostics  --rMin=-5 --rMax=20 -t -1 --expectSignal=1 --robustFit=1 --cminDefaultMinimizerStrategy 0' 
    fomDic ['BestFit'] = '-M FitDiagnostics  --rMin=-5 --rMax=20 -t -1 --expectSignal=1 --robustFit=1 --cminDefaultMinimizerStrategy 0' 

    # Filter fomList

    # Create Needed dictionnary

    samples = {}
    if os.path.exists(opt.samplesFile) :
      handle = open(opt.samplesFile,'r')
      exec(handle)
      handle.close()

    variables = {}
    cuts = {}
    if os.path.exists(opt.cutsFile) :
      handle = open(opt.cutsFile,'r')
      exec(handle)
      handle.close()

    # And COMBINATION 
    combs = {}
    cutsVal = {} 
    if os.path.exists(opt.combcfg) :
      handle = open(opt.combcfg,'r')
      exec(handle)
      handle.close()
      variables['comb'] = {}
      for iComb in combs : cutsVal[iComb] = {}
       
    # ELSE use default set of cards and cuts 
    else:
      
      if os.path.exists(opt.variablesFile) :
        handle = open(opt.variablesFile,'r')
        exec(handle)
        handle.close()
      for iCut in cuts : cutsVal[iCut] = {}

   
    for iVar in variables :
      for iCut in cutsVal:
          print iVar,iCut
          datacardDir=opt.outputDirDatacard+'/'+iCut+'/'+iVar
          command= 'cd '+opt.combineLocation+' ; eval `scramv1 runtime -sh` ; cd - ;'
          command+='cd '+datacardDir+' ;'
          for iFOM in opt.fomList:
            if iFOM in fomDic:
              command+='combine datacard.txt '+fomDic[iFOM]+' -m 0 -n _'+iVar+'_'+iCut+' > '+iFOM+'_'+iVar+'_'+iCut+';'
          command+='cd - ; eval `scramv1 runtime -sh`'
          os.system(command)
          
 
          
