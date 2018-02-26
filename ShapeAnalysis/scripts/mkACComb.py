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
    parser.add_option('--accfg'          , dest='accfg'          , help='AC coupling dictionary' , default='acoupling.py' , type='string' )
    parser.add_option('--nuisancesFile'      , dest='nuisancesFile'     , help='file with nuisances configurations'         , default=None )

    # read default parsing options as well
    hwwtools.addOptions(parser)
    hwwtools.loadOptDefaults(parser)
    (opt, args) = parser.parse_args()

    print " outputDirDatacard  = ", opt.outputDirDatacard
    print " configuration file = ", opt.pycfg
    print " AC config          = ", opt.accfg
    print " Nuissances         = ", opt.nuisancesFile
    print " Combination Cfg    = ", opt.combcfg

#   samples = {}
#   if os.path.exists(opt.samplesFile) :
#     handle = open(opt.samplesFile,'r')
#     exec(handle)
#     handle.close()

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

#   nuisances = {}
#   if opt.nuisancesFile == None :
#      print " Please provide the nuisances structure if you want to add nuisances "

#   if os.path.exists(opt.nuisancesFile) :
#     handle = open(opt.nuisancesFile,'r')
#     exec(handle)
#     handle.close()

    # acoupling = {}     
    h=open(opt.accfg,'r')
    exec(h)

    for iComb in combs :
      print iComb
      print combs[iComb]
      combDir  = opt.outputDirDatacard+'/'+iComb
      if not os.path.exists(combDir) : os.mkdir(combDir)
      for iDim in ['1D','2D','3D'] :
        if iDim in acoupling['ScanConfig'] and len(acoupling['ScanConfig'][iDim]) > 0 :
          for iScan in  acoupling['ScanConfig'][iDim]:
            print iScan
            combSubDir=opt.outputDirDatacard+'/'+iComb+'/comb_'+iScan.replace(":","_")
            if not os.path.exists(combSubDir) : os.mkdir(combSubDir)

            # Combine datacards
            combFile = combSubDir + '/' + 'aC_'+iComb+'.txt'
            command='combineCards.py -S '
            for iChannel in combs[iComb] :
              card=opt.outputDirDatacard+'/'+iChannel+'/'+combs[iComb][iChannel]+'_'+iScan.replace(":","_")+'/aC_'+iChannel+'.txt'
              command+=' '+iChannel+'='+card
              cpcmd='cp '+opt.outputDirDatacard+'/'+iChannel+'/'+combs[iComb][iChannel]+'_'+iScan.replace(":","_")+'/'+iChannel+'_ws.root '+combSubDir+'/.'
              os.system(cpcmd)
              cpcmd='cp '+opt.outputDirDatacard+'/'+iChannel+'/'+combs[iComb][iChannel]+'_'+iScan.replace(":","_")+'/'+iChannel+'.root '+combSubDir+'/.'
              os.system(cpcmd)
              cpcmd='cp '+opt.outputDirDatacard+'/'+iChannel+'/'+combs[iComb][iChannel]+'_'+iScan.replace(":","_")+'/signal_proc_'+iChannel+'.root '+combSubDir+'/.'
              os.system(cpcmd)
            command+=' > '+combFile+'.tmp '
            os.system(command)
            os.system('cat '+combFile +'.tmp | sed "s:datacards_em/.*_'+iScan.replace(":","_")+'/::" > '+ combFile) 

            # Add back rateParam


            # Create final Worspace
            if iDim == '1D' : model = 'par1_TF1_Model'
            if iDim == '2D' : model = 'par1par2_TF2_Model'
            if iDim == '3D' : model = 'par1par2par3_TF3_Model' 
            command='cd '+combSubDir+' ; '
            command+='text2workspace.py -m 125 aC_'+iComb+'.txt -P CombinedEWKAnalysis.CommonTools.ACModel:'+model+' \
                     --PO poi='+iScan.replace(":",",")+' --PO basepath=. --PO channels='
            nChan=0
            for iChannel in combs[iComb]:
              command+=iChannel
              nChan+=1 
              if nChan < len(combs[iComb]) : command+=','
              else                         : command+=' '
            for iOp in iScan.split(":") :
              command+=' --PO range_'+iOp+'='+str(acoupling['operatorRange'][iOp][0])+','+str(acoupling['operatorRange'][iOp][1])
            os.system(command)
            print command 
            
