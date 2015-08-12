#!/usr/bin/env python

import json
import sys
import ROOT
import optparse
import LatinoAnalysis.Gardener.hwwtools as hwwtools
import logging
import os.path







# ----------------------------------------------------- DatacardFactory --------------------------------------

class DatacardFactory:
    _logger = logging.getLogger('DatacardFactory')

    # _____________________________________________________________________________
    def __init__(self):
      
        variables = {}
        self._variables = variables

        cuts = {}
        self._cuts = cuts

        samples = {}
        self._samples = samples













if __name__ == '__main__':
    print '''
--------------------------------------------------------------------------------------------------

  __ \          |                                 |       \  |         |                
  |   |   _` |  __|   _` |   __|   _` |   __|  _` |      |\/ |   _` |  |  /   _ \   __| 
  |   |  (   |  |    (   |  (     (   |  |    (   |      |   |  (   |    <    __/  |    
 ____/  \__,_| \__| \__,_| \___| \__,_| _|   \__,_|     _|  _| \__,_| _|\_\ \___| _|    
                                                                                
--------------------------------------------------------------------------------------------------
'''    

    usage = 'usage: %prog [options]'
    parser = optparse.OptionParser(usage)

    parser.add_option('--tag'                , dest='tag'               , help='Tag used for the shape file name'           , default=None)
    parser.add_option('--sigset'             , dest='sigset'            , help='Signal samples [SM]'                        , default='SM')
    parser.add_option('--outputDirDatacard'  , dest='outputDirDatacard' , help='output directory'                           , default='./')
    parser.add_option('--inputFile'          , dest='inputFile'         , help='input directory'                            , default='./input.root')
          
    # read default parsing options as well
    hwwtools.addOptions(parser)
    hwwtools.loadOptDefaults(parser)
    (opt, args) = parser.parse_args()

    sys.argv.append( '-b' )
    ROOT.gROOT.SetBatch()


    print " configuration file = ", opt.pycfg
    
    print " inputFile =                  ", opt.inputFile
    print " outputDirDatacard =          ", opt.outputDirDatacard
 
 
    if not opt.debug:
        pass
    elif opt.debug == 2:
        print 'Logging level set to DEBUG (%d)' % opt.debug
        logging.basicConfig( level=logging.DEBUG )
    elif opt.debug == 1:
        print 'Logging level set to INFO (%d)' % opt.debug
        logging.basicConfig( level=logging.INFO )

      
    factory = DatacardFactory()
    factory._energy    = opt.energy
    factory._lumi      = opt.lumi
    factory._tag       = opt.tag
    
    
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
    
    samples = {}
    if os.path.exists(opt.samplesFile) :
      handle = open(opt.samplesFile,'r')
      exec(handle)
      handle.close()
    
    
    #factory.makeDatacards( opt.inputFile ,opt.outputDirDatacard, variables, cuts, samples)
    
        
        