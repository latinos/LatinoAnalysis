#!/usr/bin/env python

import optparse
import LatinoAnalysis.Gardener.hwwtools as hwwtools

# functions used in everyday life ...
from LatinoAnalysis.Tools.commonTools import *


if __name__ == '__main__':

    usage = 'usage: %prog [options]'
    parser = optparse.OptionParser(usage)
    
    parser.add_option('--dycfg'           , dest='dycfg'           , help='DY estimation dictionary'                  , default='dyestim.py') 
    parser.add_option('--outputDir'      , dest='outputDir'      , help='output directory'                           , default='./')
    parser.add_option('--tag'            , dest='tag'            , help='Tag used for the shape file name'           , default=None)
    parser.add_option('--DYtag'          , dest='DYtag'          , help='Tag added to the shape file name'           , default='DYEstim')
    parser.add_option('--inputFile'      , dest='inputFile'      , help='input file with histograms'                 , default='DEFAULT')
    parser.add_option('--outputFile'     , dest='outputFile'     , help='output file with histograms'                 , default='DEFAULT')
 
    # read default parsing options as well
    hwwtools.addOptions(parser)
    hwwtools.loadOptDefaults(parser)
    (opt, args) = parser.parse_args()

    print " configuration file = ", opt.pycfg
    print " DY estimation Cfg  = ", opt.dycfg

    # Set Input file
    if opt.inputFile == 'DEFAULT' :
      opt.inputFile = opt.outputDir+'/plots_'+opt.tag+'.root'
    print " inputFile      =          ", opt.inputFile

    # Set Output file
    if opt.outputFile == 'DEFAULT' :
      opt.outputFile = opt.outputDir+'/plots_'+opt.tag+'_'+opt.DYtag+'.root'
    print " ooutputFile    =          ", opt.outputFile

    # Create Needed dictionnary

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

    RAndKff = {}
    DYestim = {}
    if os.path.exists(opt.dycfg) :
      handle = open(opt.dycfg,'r')
      exec(handle)
      handle.close()

    # Compute Rinout and K_ff
    Rinout = {}
    K_ff   = {}

    for iRAndKff in RAndKff :
      Rinout[iRAndKff] = {}
      Rinout[iRAndKff]['0jee'] = 0.
      Rinout[iRAndKff]['0jmm'] = 0.
      Rinout[iRAndKff]['1jee'] = 0.
      Rinout[iRAndKff]['1jmm'] = 0.
      K_ff[iRAndKff] = {}
      K_ff[iRAndKff]['0jee'] = 0.
      K_ff[iRAndKff]['0jmm'] = 0.
      K_ff[iRAndKff]['1jee'] = 0.
      K_ff[iRAndKff]['1jmm'] = 0.

    print ' ----- Rinout -----'
    print Rinout
    print ' ----- K_ff -------'
    print K_ff 

    # Apply Rinout and K_ff

    for iDYestim in DYestim :
      print iDYestim

