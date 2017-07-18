#!/usr/bin/env python

import json
import sys
from sys import exit
import ROOT
import optparse
import LatinoAnalysis.Gardener.hwwtools as hwwtools
import os.path
import string
import logging
import LatinoAnalysis.Gardener.odict as odict
import traceback
from array import array
from collections import OrderedDict
import math

#import os.path



# ----------------------------------------------------- LawnMower --------------------------------------

class LawnMower:
    _logger = logging.getLogger('LawnMower')
 
    # _____________________________________________________________________________
    def __init__(self):

        variables = {}
        self._variables = variables

 
    # _____________________________________________________________________________
    def makePostFitPlot(self):

        print "========================="
        print "==== makePostFitPlot ===="
        print "========================="
        
        print " self.inputFileCombine " , self._inputFileCombine
        
        
        process = "ggH_hww"
        cut = "hww2l2v_13TeV_em_pm_0j"
        
        fileIn = ROOT.TFile(self._inputFileCombine, "READ")

        
        #post_RooArgSet = ROOT.RooArgSet()
        post_RooArgSet = fileIn.Get("norm_fit_s") 
        
        name = cut + "/" + process
        normalization = post_RooArgSet
        
        print " name = ", name 
        
        if (post_RooArgSet.find(name)) :
          print "found "
          
          norm_post =  post_RooArgSet.find(name)

          print " integral = ", norm_post.getVal()
          

        
        


if __name__ == '__main__':
    print '''
----------------------------------------------------------------------------------------------------------------------------------


    _ \                                            _ \               |         ____| _)  |               |         |         
  |   |   __|  _ \  __ \    _` |   __|  _ \      |   |  _ \    __|  __|       |      |  __|      __ \   |   _ \   __|   __| 
  ___/   |     __/  |   |  (   |  |     __/      ___/  (   | \__ \  | _____|  __|    |  |        |   |  |  (   |  |   \__ \ 
 _|     _|   \___|  .__/  \__,_| _|   \___|     _|    \___/  ____/ \__|      _|     _| \__|      .__/  _| \___/  \__| ____/ 
                   _|                                                                           _|                          
 

----------------------------------------------------------------------------------------------------------------------------------
'''    
    usage = 'usage: %prog [options]'
    parser = optparse.OptionParser(usage)

    parser.add_option('--inputFileCombine'      , dest='inputFileCombine'      , help='input file with roofit results, mlfit'                 , default='input.root')
          
    # read default parsing options as well
    hwwtools.addOptions(parser)
    hwwtools.loadOptDefaults(parser)
    (opt, args) = parser.parse_args()

    sys.argv.append( '-b' )
    ROOT.gROOT.SetBatch()

    print " inputFileCombine      =          ", opt.inputFileCombine

    if not opt.debug:
        pass
    elif opt.debug == 2:
        print 'Logging level set to DEBUG (%d)' % opt.debug
        logging.basicConfig( level=logging.DEBUG )
    elif opt.debug == 1:
        print 'Logging level set to INFO (%d)' % opt.debug
        logging.basicConfig( level=logging.INFO )

    factory = LawnMower()
    factory._inputFileCombine = opt.inputFileCombine
    
    factory.makePostFitPlot()
    
    print '... and now closing ...'
        
       
