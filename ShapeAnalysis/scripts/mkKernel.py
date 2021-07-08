#!/usr/bin/env python

import json
import sys
argv = sys.argv
sys.argv = argv[:1]
import ROOT
import optparse
import LatinoAnalysis.Gardener.hwwtools as hwwtools
from  LatinoAnalysis.ShapeAnalysis.ShapeFactoryMulti import ShapeFactory as SF
from  LatinoAnalysis.ShapeAnalysis.KernelFactory import KernelFactory
import logging
import collections
import os.path
import shutil
import array
from sklearn.utils import resample
import tempfile
import root_numpy as rnp
import numpy as np
import math
from numpy import linalg as LA
import itertools
from LatinoAnalysis.Tools.batchTools  import *

# Common Tools & batch
from LatinoAnalysis.Tools.commonTools import *


if __name__ == '__main__':
    sys.argv = argv
    
    print '''
                                                                                                    
                                                                                                    
                                                       ````             ```````                     
                                                 `.----------...   .:/+++/++++++++/:.`              
                                               .--..............--//::---:://+ossss++o+:`           
                                             .:-..----..--------.----``          `-/os++o+.         
                                            -:..-------...........-:-.               `:o++s+        
                                           .:.------.`..............--.                 -++o+       
                                          `:.---:/-.`...........-::--...                 -++y`      
                                       ``----::/o-`...........:osssmy-...                `++y`      
                                ```..-::/+os+:yy/.`..........-+d+/ohmo...`              `/++/       
                         ```.----------:::::-:hd:`..........`-:hNho/++:.`.`           .:/:::        
                  ```..----------:::::-------omm-`............--+yhmho+///::------:://:--..         
           ```..---...----:::-----------::/++smN:`...``...........-shdhyso+++///::::-...`           
        -----..------------------:::-------:-smd:...`````````````...+yysssy:::---..``               
       .-------------------------```..``-:...``/...-.`````````````````.-:+:                         
      o/------------..------..``         `   `-...:...``````````````````..                          
      -//:-----....`...                    `....--......````````````  `.``                          
         `...`` ``                      `...`.--........`````````````.``                            
                                      `...`..-.......:..`.-...``````                                
                                    `.-.`.--....``.--.`   `````                                     
                                  `..`..-.....``...-``                                              
                                `-...--......````                                                   
                              .....--.....```                                                       
                            .....---....``..`                                                       
                         `.-..---.....`.-.`                                                         
                       `--..------....`                                                             
                      `/..-------.``.`                                                              
                      .-::-----..-`                                                                 
                      -s----...```                                                                  
                       :.```..`                                                                     
                                                                                                    
                                                                                       
'''   

#
#     This code is run between mkShape and mkDatacard/mkPlot
#     The idea is to massage the input histograms to deal with empty bins for selected samples
#

    usage = 'usage: %prog [options]'
    parser = optparse.OptionParser(usage)

    parser.add_option('--inputFile'          , dest='inputFile'           , help='input file '                                , default='./input.root')
    parser.add_option('--inputFileTree'          , dest='inputFileTree'           , help='input file with the tree holding the branches to make the RooKeysPdf' , default='./input.root')
    parser.add_option('--treeNameForKernel'          , dest='treeNameForKernel'           , help='name of the tree in inputTreeFile' , default='tree')
    parser.add_option('--outputFile'         , dest='outputFile'          , help='output file. Copy of the input file with modified histograms'    , default='./output.root')
    parser.add_option('--structureFile'      , dest='structureFile'       , help='file with datacard configurations'          , default=None )
    parser.add_option('--doBatch'        , dest='doBatch'        , help='Run on batch'                               , default=False)
    parser.add_option('--batchQueue'     , dest='batchQueue'     , help='Queue on batch'                             , default='workday')
    parser.add_option('--nuisancesFile'      , dest='nuisancesFile'       , help='file with nuisances configurations'         , default=None )
    parser.add_option('--sample'      , dest='samplesToTreat'       , help='sample to tun on (can repeat multiple times)'         , default=[], action='append' )
    parser.add_option('--cut', dest='cuts_to_run', help='list of cuts to run on (can repear multiple times)', default=[], action='append')
    parser.add_option("-W" , "--iihe-wall-time" , dest="IiheWallTime" , help="Requested IIHE queue Wall Time" , default='168:00:00')
    parser.add_option("-n", "--dry-run"  , dest="dryRun"         , help="do not make shapes"                         , default=False, action="store_true")
   
    cmssw_base = os.getenv('CMSSW_BASE')
    try:
      ROOT.gROOT.LoadMacro(cmssw_base+'/src/LatinoAnalysis/ShapeAnalysis/scripts/RooNDKeysPdfAnalytical.cxx+g')
    except RuntimeError:
      ROOT.gROOT.LoadMacro(cmssw_base+'/src/LatinoAnalysis/ShapeAnalysis/scripts/RooNDKeysPdfAnalytical.cxx++g')

    # read default parsing options as well
    hwwtools.addOptions(parser)
    hwwtools.loadOptDefaults(parser)
    (opt, args) = parser.parse_args()

    sys.argv.append( '-b' )
    ROOT.gROOT.SetBatch()

    print " configuration file = ", opt.pycfg
    
    print " inputFile  =          ", opt.inputFile
    print " outputFile =          ", opt.outputFile
    
    if not opt.debug:
      pass
    elif opt.debug == 2:
      print 'Logging level set to DEBUG (%d)' % opt.debug
      logging.basicConfig( level=logging.DEBUG )
    elif opt.debug == 1:
      print 'Logging level set to INFO (%d)' % opt.debug
      logging.basicConfig( level=logging.INFO )

    if opt.nuisancesFile == None :
      print " Please provide the nuisances structure if you want to add nuisances "

    if opt.structureFile == None :
      print " Please provide the datacard structure "
      exit ()

    ROOT.TH1.SetDefaultSumw2(True)
      
    factory = KernelFactory()
   
    if os.path.exists(opt.pycfg) :
      handle = open(opt.pycfg,'r')
      exec(handle)
      handle.close()
      

    ## load the samples
    samples = {}
    if os.path.exists(opt.samplesFile) :
      handle = open(opt.samplesFile,'r')
      exec(handle)
      handle.close()

    ## load the cuts
    cuts = {}
    if os.path.exists(opt.cutsFile) :
      handle = open(opt.cutsFile,'r')
      exec(handle)
      handle.close()

    ## load the variables
    variables = {}
    if os.path.exists(opt.variablesFile) :
      handle = open(opt.variablesFile,'r')
      exec(handle)
      handle.close()

    ## load the nuisances
    nuisances = collections.OrderedDict()
    if os.path.exists(opt.nuisancesFile) :
      handle = open(opt.nuisancesFile,'r')
      exec(handle)
      handle.close()
    for n in nuisances:
      nuisances[n].pop('cutspost', None)
    import LatinoAnalysis.ShapeAnalysis.utils as utils

    subsamplesmap = utils.flatten_samples(samples)
    categoriesmap = utils.flatten_cuts(cuts)

    utils.update_variables_with_categories(variables, categoriesmap)
    utils.update_nuisances_with_subsamples(nuisances, subsamplesmap)
    utils.update_nuisances_with_categories(nuisances, categoriesmap)

    ## load the structure file (use flattened sample and cut names)
    structure = collections.OrderedDict()
    if os.path.exists(opt.structureFile) :
      handle = open(opt.structureFile,'r')
      exec(handle)
      handle.close()

    ## command-line cuts restriction
    cutstorun = cuts if len(opt.cuts_to_run) == 0 else opt.cuts_to_run
    samplestorun = samples.keys() if len(opt.samplesToTreat) == 0 else opt.samplesToTreat

    if not opt.doBatch:
      factory.mkKernel( opt.inputFile, opt.outputFile, opt.inputFileTree, opt.treeNameForKernel, variables, cutstorun, samples.keys(), structure, nuisances, samplestorun)
    else:  
      if 'slc7' in os.environ['SCRAM_ARCH'] and 'iihe' in os.uname()[1] : use_singularity = True
      else : use_singularity = False
      bpostFix=''
      targetList = list(itertools.product(cutstorun, range(len(samplestorun))))
      jobs = batchJobs('mkKernel',tag,['all'],targetList,'Target',bpostFix,JOB_DIR_SPLIT_READY=True,USE_SINGULARITY=use_singularity)

      jobs.AddPy2Sh()
      jobs.InitPy('import os')
      jobs.InitPy('import ROOT')
      jobs.InitPy('from collections import OrderedDict')
      jobs.InitPy("from LatinoAnalysis.ShapeAnalysis.KernelFactory import KernelFactory\n")
      jobs.InitPy("factory = KernelFactory()")
      jobs.InitPy("\n")

      #outputDir=os.getcwd()+'/'+opt.outputDir

      for iTarget in targetList:
          tname = '%s.%d' % iTarget

          outfile = opt.outputFile.replace('.root', "_"+tname+".root")  
          instructions_for_configuration_file  = ""
          instructions_for_configuration_file += "os.system(\"cp "+os.getcwd()+'/'+opt.inputFile+" .\") \n"
          instructions_for_configuration_file += "os.system(\"cp "+os.getcwd()+'/'+opt.inputFileTree+" .\") \n"
          instructions_for_configuration_file += "try:\n"
          instructions_for_configuration_file += "  ROOT.gROOT.LoadMacro('"+cmssw_base+"/src/LatinoAnalysis/ShapeAnalysis/scripts/RooNDKeysPdfAnalytical.cxx+g')\n"
          instructions_for_configuration_file += "except RuntimeError:\n"
          instructions_for_configuration_file += "  ROOT.gROOT.LoadMacro('"+cmssw_base+"/src/LatinoAnalysis/ShapeAnalysis/scripts/RooNDKeysPdfAnalytical.cxx++g')\n"

          instructions_for_configuration_file += "factory.mkKernel(   \n"
          instructions_for_configuration_file += "     '" + opt.inputFile.split('/')[-1] +"',    \n"
          instructions_for_configuration_file += "     '" + outfile + "',     \n"
          instructions_for_configuration_file += "     '" + opt.inputFileTree.split('/')[-1] + "',     \n"
          instructions_for_configuration_file += "     '" + opt.treeNameForKernel + "', \n"
          instructions_for_configuration_file += "      " + str(variables) + ",      \n"
          instructions_for_configuration_file += "      ['" + str(iTarget[0]) + "'],      \n"
          instructions_for_configuration_file += "      " + str(samples.keys()) + ",      \n"
          instructions_for_configuration_file += "      " + str(structure) + ",      \n"
          instructions_for_configuration_file += "      " + str(nuisances) + ",      \n"
          instructions_for_configuration_file += "      ['" + str(samplestorun[iTarget[1]]) + "'])      \n"
          instructions_for_configuration_file += "os.system(\"cp "+outfile+" "+os.getcwd()+"\") \n"

          jobs.AddPy ('all', iTarget, instructions_for_configuration_file)

      if not opt.dryRun:
        jobs.Sub(opt.batchQueue,opt.IiheWallTime,True)
