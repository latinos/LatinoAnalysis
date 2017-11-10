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
    parser.add_option('--combcfg'           , dest='combcfg'           , help='Combination disctionnary'                  , default='comb.py') 
 
    # read default parsing options as well
    hwwtools.addOptions(parser)
    hwwtools.loadOptDefaults(parser)
    (opt, args) = parser.parse_args()

    print " configuration file = ", opt.pycfg
    print " lumi =               ", opt.lumi

    print " outputDirDatacard  = ", opt.outputDirDatacard
    print " combineLocation    = ", opt.combineLocation  
    print " Combination Cfg    = ", opt.combcfg

    # Filter fomList

    # Create Needed dictionnary

    samples = {}
    if os.path.exists(opt.samplesFile) :
      handle = open(opt.samplesFile,'r')
      exec(handle)
      handle.close()


    variables = {}
    if os.path.exists(opt.variablesFile) :
      handle = open(opt.variablesFile,'r')
      exec(handle)
      handle.close()

    cuts = {}
    if os.path.exists(opt.cutsFile) :
      handle = open(opt.cutsFile,'r')
      exec(handle)
      handle.close()

    combs = {}
    if os.path.exists(opt.combcfg) :
      handle = open(opt.combcfg,'r')
      exec(handle)
      handle.close()

    for iComb in combs :
      print iComb
      print combs[iComb]
      combDir  = opt.outputDirDatacard+'/'+iComb
      if not os.path.exists(combDir)                : os.mkdir(combDir)
      if not os.path.exists(combDir+'/comb')        : os.mkdir(combDir+'/comb')
      if not os.path.exists(combDir+'/comb/shapes') : os.mkdir(combDir+'/comb/shapes')
      combFile = combDir+'/comb/datacard.txt'
      command  = 'cd '+opt.combineLocation+' ; eval `scramv1 runtime -sh` ; cd - ;'
      command += 'combineCards.py -S '
      for iChannel in combs[iComb] :
        os.system('cd '+combDir+'/comb/shapes ; ln -s ../../../'+iChannel+'/'+combs[iComb][iChannel]+'/shapes/histos_'+iChannel+'.root ; cd -' )  
        card=opt.outputDirDatacard+'/'+iChannel+'/'+combs[iComb][iChannel]+'/datacard.txt'
        command += ' '+iChannel+'='+card
      command += ' > '+combFile+'.tmp ; '
      command+='eval `scramv1 runtime -sh`'
      print command
      os.system(command)
      os.system('cat '+combFile +'.tmp | sed "s:datacards.*shapes:shapes:" > '+ combFile )
      os.system('rm '+combFile +'.tmp')
 

