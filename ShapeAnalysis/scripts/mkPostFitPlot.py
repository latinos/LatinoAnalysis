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
        
        
        fileIn = ROOT.TFile(self._inputFileCombine, "READ")


        self._outFile = ROOT.TFile.Open( self._outputFileName, 'update')  # need to append in an existing file if more cuts/variables are wanted

        self._outFile.mkdir ( self._cutNameInOriginal )
        self._outFile.mkdir ( self._cutNameInOriginal + "/" + self._variable)

        self._outFile.cd ( self._cutNameInOriginal + "/" + self._variable )

        
        #post_RooArgSet = ROOT.RooArgSet()
        post_RooArgSet = fileIn.Get("norm_fit_s")      
        normalization = post_RooArgSet
        
        
        if self._kind == 's' :
          folder_fit_name = "shapes_fit_s"   # signal + background
        elif  self._kind == 'b' :
          folder_fit_name = "shapes_fit_b"   # background only fit
        elif  self._kind == 'p' :
          folder_fit_name = "shapes_prefit"   # prefit
        else :
          print " Seriously? What do you want from me? "
          return 
       
       
        template_histogram = 0
        
        for samples_key,samples_values in self._samples.iteritems():
           if samples_key == "DATA" :
             fileInJustForDATA = ROOT.TFile(self._inputFile, "READ")

             self._outFile.cd ( self._cutNameInOriginal + "/" + self._variable )

             histo = fileInJustForDATA.Get(self._cutNameInOriginal + "/" + self._variable + "/histo_" + samples_key)      
             histo.SetName  ('histo_' + samples_key)
             histo.SetTitle ('histo_' + samples_key)
             histo.Write()              
             
             template_histogram = histo.Clone ("template")


        #print " template_histogram = " , template_histogram
         
        for samples_key,samples_values in self._samples.iteritems():

           print " samples_key = ", samples_key
           
           if samples_key != "DATA" :
             histo = fileIn.Get(folder_fit_name + "/" + self._cut + "/" + samples_key)      
             print folder_fit_name + "/" + self._cut + "/" + samples_key
             
             histo.SetName  ('histo_' + samples_key)
             histo.SetTitle ('histo_' + samples_key)
             
             # fix the binning copying from "DATA" binning, if available
             if (template_histogram != 0) :
               histo = self._ChangeBin(histo, template_histogram)
             
             histo.Write()              

        #
        # total signal and total background, and total
        #
        
        #
        # total signal
        histo_total_signal = fileIn.Get(folder_fit_name + "/" + self._cut + "/" + "total_signal")      
        
        histo_total_signal.SetName  ('histo_' + 'total_signal')
        histo_total_signal.SetTitle ('histo_' + 'total_signal')
        
        # fix the binning copying from "DATA" binning, if available
        if (template_histogram != 0) :
          histo_total_signal = self._ChangeBin(histo_total_signal, template_histogram)
        
        histo_total_signal.Write()              

        #
        # total background
        histo_total_background = fileIn.Get(folder_fit_name + "/" + self._cut + "/" + "total_background")      
        
        histo_total_background.SetName  ('histo_' + 'total_background')
        histo_total_background.SetTitle ('histo_' + 'total_background')
        
        # fix the binning copying from "DATA" binning, if available
        if (template_histogram != 0) :
          histo_total_background = self._ChangeBin(histo_total_background, template_histogram)
        
        histo_total_background.Write()              
        
        #
        # total
        histo_total = fileIn.Get(folder_fit_name + "/" + self._cut + "/" + "total")      
        
        histo_total.SetName  ('histo_' + 'total')
        histo_total.SetTitle ('histo_' + 'total')
        
        # fix the binning copying from "DATA" binning, if available
        if (template_histogram != 0) :
          histo_total = self._ChangeBin(histo_total, template_histogram)
        
        histo_total.Write()              
        
        
        
        
             
     
        
    # _____________________________________________________________________________
    def _ChangeBin(self, myhisto, templatehisto): 

        nx = templatehisto.GetNbinsX()
        
        binLowEdge = []

        for iBin in range(1, nx+1):
          binLowEdge.append(templatehisto.GetXaxis().GetBinLowEdge(iBin))
        binLowEdge.append(templatehisto.GetXaxis().GetBinLowEdge(nx+1))
        #print " binLowEdge = ", binLowEdge

        new_histo = ROOT.TH1F("temporary","",nx,array('d',binLowEdge))
          
        for iBin in range(1, nx+1):
          new_histo.SetBinContent(iBin, myhisto.GetBinContent(iBin))
          new_histo.SetBinError  (iBin, myhisto.GetBinError(iBin))
          
        new_histo.SetName  (myhisto.GetName())
        new_histo.SetTitle (myhisto.GetTitle())
        
        return new_histo
        

        


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

    parser.add_option('--inputFileCombine'      , dest='inputFileCombine'      , help='input file with roofit results, mlfit'                          , default='input.root')
    parser.add_option('--outputFile'            , dest='outputFile'            , help='output file with histograms, same format as mkShape.py output'  , default='output.root')
    parser.add_option('--variable'              , dest='variable'              , help='variable name'  , default='mll')
    parser.add_option('--cut'                   , dest='cut'                   , help='cut name'  , default='0j')
    parser.add_option('--cutNameInOriginal'     , dest='cutNameInOriginal'     , help='cut name as appears in cuts.py'  , default='')
    parser.add_option('--inputFile'             , dest='inputFile'             , help='input file with histograms (only to get the DATA distribution)' , default='input.root')
    parser.add_option('--kind'                  , dest='kind'                  , help='which kind of post-fit distribution: s = signal + background, b = background only, p = prefit'  , default='s')
          
          
    # read default parsing options as well
    hwwtools.addOptions(parser)
    hwwtools.loadOptDefaults(parser)
    (opt, args) = parser.parse_args()

    sys.argv.append( '-b' )
    ROOT.gROOT.SetBatch()

    print " configuration file    =          ", opt.pycfg
    print " inputFileCombine      =          ", opt.inputFileCombine
    print " inputFile (for DATA)  =          ", opt.inputFile
    print " outputFile            =          ", opt.outputFile
    print " variable              =          ", opt.variable
    print " cut                   =          ", opt.cut
    print " kind                  =          ", opt.kind

    if opt.cutNameInOriginal == '' :
      opt.cutNameInOriginal = opt.cut
    print " cutNameInOriginal     =          ", opt.cutNameInOriginal


    if not opt.debug:
        pass
    elif opt.debug == 2:
        print 'Logging level set to DEBUG (%d)' % opt.debug
        logging.basicConfig( level=logging.DEBUG )
    elif opt.debug == 1:
        print 'Logging level set to INFO (%d)' % opt.debug
        logging.basicConfig( level=logging.INFO )

    factory = LawnMower()
    factory._inputFileCombine  = opt.inputFileCombine
    factory._outputFileName    = opt.outputFile
    factory._variable          = opt.variable
    factory._cut               = opt.cut
    factory._cutNameInOriginal = opt.cutNameInOriginal
    factory._kind             = opt.kind


    samples = OrderedDict()
    if os.path.exists(opt.samplesFile) :
      handle = open(opt.samplesFile,'r')
      exec(handle)
      handle.close()

    factory._samples = samples
    
    factory._inputFile = opt.inputFile
    
    factory.makePostFitPlot()
    
    print '... and now closing ...'
        
       
       
       
