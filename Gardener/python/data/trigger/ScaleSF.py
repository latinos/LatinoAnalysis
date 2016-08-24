#!/usr/bin/env python

import json
import sys
from sys import exit
import ROOT
import optparse
import os.path
import string
import logging
import traceback
from array import array
from collections import OrderedDict
import math

import os




if __name__ == '__main__':
    print '''
--------------------------------------------------------------------------------------------------

               ___|                |           \ \     /       |                    
             \___ \    __|   _` |  |   _ \      \ \   /  _` |  |  |   |   _ \   __| 
                   |  (     (   |  |   __/       \ \ /  (   |  |  |   |   __/ \__ \ 
             _____/  \___| \__,_| _| \___|        \_/  \__,_| _| \__,_| \___| ____/ 
                                                                                    
--------------------------------------------------------------------------------------------------
'''    

    usage = 'usage: %prog [options]'
    parser = optparse.OptionParser(usage)

    parser.add_option('--outputFile'     , dest='outputFile'     , help='output file with averaged values'           , default='test.txt')
    parser.add_option('--inputFile'      , dest='inputFile'      , help='input file with averaged values'            , default='testIn.txt')
    parser.add_option('--scale'          , dest='scale'          , help='scale value'                                , default=1.0,   type = float)
          
    # read default parsing options as well
    (opt, args) = parser.parse_args()

    sys.argv.append( '-b' )
    ROOT.gROOT.SetBatch()


    print " inputFile        = ", opt.inputFile
    print " outputFile       = ", opt.outputFile

    
    iFile = open (opt.inputFile)
    
    values = [line.rstrip().split() for line in iFile      if '#' not in line]
      


    outFile = open(opt.outputFile, 'w')
    #outFile.write('# etamin  etamax  ptmin   ptmax   eff    err_eff  \n')

    for point in values:
      outFile.write( '  {0:.2f}  {1:.2f}  {2:.2f}  {3:.2f}  {4:.3f}  {5:.3f} \n '.format(float(point[0]), float(point[1]), float(point[2]), float(point[3]), opt.scale * float(point[4]), opt.scale * float(point[5])) )
      
    
    outFile.close()
    
    
    