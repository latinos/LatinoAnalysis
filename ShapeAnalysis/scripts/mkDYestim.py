#!/usr/bin/env python

import optparse
import LatinoAnalysis.Gardener.hwwtools as hwwtools

# functions used in everyday life ...
from LatinoAnalysis.Tools.commonTools import *


if __name__ == '__main__':

    usage = 'usage: %prog [options]'
    parser = optparse.OptionParser(usage)
    
    parser.add_option('--dycfg'           , dest='dycfg'           , help='DY estimation dictionary'                  , default='dyestim.py') 
 
    # read default parsing options as well
    hwwtools.addOptions(parser)
    hwwtools.loadOptDefaults(parser)
    (opt, args) = parser.parse_args()

    print " configuration file = ", opt.pycfg
    print " DY estimation Cfg  = ", opt.dycfg

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

