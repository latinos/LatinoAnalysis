#!/usr/bin/env python
import sys, re, os, os.path, math
import optparse

import ROOT





if __name__ == '__main__':
    print '''
--------------------------------------------------------------------------------------------------
   ___|                     |           |      __ )          |  | 
  |       __|  |   |   __|  __|   _` |  |      __ \    _` |  |  | 
  |      |     |   | \__ \  |    (   |  |      |   |  (   |  |  | 
 \____| _|    \__, | ____/ \__| \__,_| _|     ____/  \__,_| _| _| 
              ____/                                               
--------------------------------------------------------------------------------------------------
'''    
    usage = 'usage: %prog [options]'
    parser = optparse.OptionParser(usage)

    parser.add_option('--inputFile'      , dest='inputFile'      , help='input file with histograms'                 , default='input.root')
          
    # read default parsing options as well
    (opt, args) = parser.parse_args()

    sys.argv.append( '-b' )
    ROOT.gROOT.SetBatch()


    print " inputFile =               ", opt.inputFile
    
    
