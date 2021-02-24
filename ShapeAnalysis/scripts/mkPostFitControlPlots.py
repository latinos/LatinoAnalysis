#!/usr/bin/env python

import json
import sys
from sys import exit
argv = sys.argv
sys.argv = argv[:1]
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
import numpy
import root_numpy

# ----------------------------------------------------- LawnMower --------------------------------------

class AddMCunc:
    _logger = logging.getLogger('LawnMower')
 
    # _____________________________________________________________________________
    def __init__(self):

        pass
      
 
    # _____________________________________________________________________________
    def FixUncertainties(self):

        print "=================="
        print "==== AddMCunc ===="
        print "=================="
        
        print " self._inputFileHisto "       , self._inputFileHisto
        print " self._outputFileHistoClone " , self._outputFileHistoClone
        print " self._listOfFilesOriginal "  , self._listOfFilesOriginal
 
        # copy the input root file        
        os.system ("cp " + self._inputFileHisto + "   " + self._outputFileHistoClone) 
  
        
        # open the original files and add all the histograms together
        # this will provide for each bin the MC uncertainty
  
          
                
        ROOT.TH1.SetDefaultSumw2(True)
        hStackTotal = ROOT.THStack("total",'')
        
        for fileIn in self._listOfFilesOriginal:
            inputFile = ROOT.TFile.Open(fileIn,  "READ")
            for sampleName, plotdef in self._plot.iteritems():
              if sampleName != 'DATA' :    # 'DATA' should not be added/stacked!
                try:
                  histo = inputFile.Get("histo_" + sampleName)
                  hStackTotal.Add(histo)
                except:
                  print "missing histo: histo_" + sampleName
        
        
        #Final histogram -> get MC errors
        histo_sum = hStackTotal.GetStack().Last()
        err_up = numpy.sqrt(numpy.array(histo_sum.GetSumw2())[1:-1]) # GetSumw2 -> array of sum squares of weights
        err_do = numpy.sqrt(numpy.array(histo_sum.GetSumw2())[1:-1]) # GetSumw2 -> array of sum squares of weights
        
        nominal = root_numpy.hist2array(histo_sum, copy=False)
        print "nominal ", nominal
        
        # err_rel_up = err_up / nom 
        # err_rel_do = err_do / nom 
        # print err_rel_up, err_rel_do
        
        outputFile = ROOT.TFile.Open(self._inputFileHisto, "UPDATE")
        graphFinal = ROOT.TGraphAsymmErrors()
        h_err = histo_sum.Clone("htotal_err")
        h_err.Reset()
        graphFinal.SetName("gr_mcstaterr")
        for i in range(1, histo_sum.GetNbinsX()+1):
            graphFinal.SetPoint(i-1, histo_sum.GetBinCenter(i), nominal[i-1])
            graphFinal.SetPointError(i-1, 0.,0., err_do[i-1], err_up[i-1])
            h_err.SetBinContent(i, nominal[i-1])
            h_err.SetBinError(i, err_up[i-1])
        h_err.Write()
        graphFinal.Write()
        
        histo_total = outputFile.Get(self._cutName + "/" + self._variable + "/" + "histo_total")
        print(histo_total)
        histo_total_old = histo_total.Clone(self._cutName + "/" + self._variable + "/" + "histo_total_old")
        
        gr_total = outputFile.Get(self._cutName + "/" + self._variable + "/" + "gr_total")

        
        # Fixed names to be updated:
        #   histo_total
        #   gr_total
        
        for iBin in range(1, histo_total.GetNbinsX()+1):
            old_err = histo_total.GetBinError(iBin)
            new_err = math.sqrt( histo_total.GetBinError(iBin)*histo_total.GetBinError(iBin) + h_err.GetBinError(iBin)*h_err.GetBinError(iBin) )
            print " ", iBin, ") old err: ", old_err, " new err: ", new_err
            histo_total.SetBinError(iBin, new_err)
            gr_total.SetPointError(iBin, 0, 0, -new_err, new_err)
        
        
        outputFile.cd ( self._cutName + "/" + self._variable )
        histo_total_old.Write()
        histo_total.Write()
        gr_total.Write()
        
        outputFile.Close()
        


def foo_callback(option, opt, value, parser):
  setattr(parser.values, option.dest, value.split(','))




if __name__ == '__main__':
    sys.argv = argv
    
    print '''
----------------------------------------------------------------------------------------------------------------------------------


   _ \                                            _ \               |         ____| _)  |         ___|                |                |       _ \   |         |         
  |   |   __|  _ \  __ \    _` |   __|  _ \      |   |  _ \    __|  __|       |      |  __|      |       _ \   __ \   __|   __|  _ \   |      |   |  |   _ \   __|   __| 
  ___/   |     __/  |   |  (   |  |     __/      ___/  (   | \__ \  | _____|  __|    |  |        |      (   |  |   |  |    |    (   |  |      ___/   |  (   |  |   \__ \ 
 _|     _|   \___|  .__/  \__,_| _|   \___|     _|    \___/  ____/ \__|      _|     _| \__|     \____| \___/  _|  _| \__| _|   \___/  _|     _|     _| \___/  \__| ____/ 
                   _|                                                                                                                                                    
                   
                   

Issue: when using combinetool to create post-fit plots, original nuisances are removed
If a nuisance appears in the control plots (e.g. MC statistical uncertainty)
but not in the fit datacard (e.g. it's another variable an MC stat uncertainty cannot be propagated!)
the nuisance should be added in quadrature

----------------------------------------------------------------------------------------------------------------------------------
'''    
    usage = 'usage: %prog [options]'
    parser = optparse.OptionParser(usage)

    parser.add_option('--inputFileHisto'        , dest='inputFileHisto'        , help='input file with historgrams and tgraph to be modified'           , default='input.root')
    parser.add_option('--outputFileHistoClone'  , dest='outputFileHistoClone'  , help='clone of inputFileHisto, since inputFileHisto will be modified'  , default='output.root')
    parser.add_option('--listOfFilesOriginal'   , dest='listOfFilesOriginal'   , help='list of files with the original histograms, from which to extract the MC stat' , default='one.root,two.root', type='string', action='callback', callback=foo_callback)
    #parser.add_option('--plotFile'              , dest='plotFile'              , help='Plot file'  , default='plot_combined.py')
    parser.add_option('--cutName'               , dest='cutName'               , help='cut name as will appear in cuts.py'  , default='combined')
    parser.add_option('--variable'              , dest='variable'              , help='variable name'  , default='mll')
          
    # read default parsing options as well
    hwwtools.addOptions(parser)
    hwwtools.loadOptDefaults(parser)
    (opt, args) = parser.parse_args()

    sys.argv.append( '-b' )
    ROOT.gROOT.SetBatch()

    print " inputFileHisto        =    ", opt.inputFileHisto
    print " outputFileHistoClone  =    ", opt.outputFileHistoClone
    print " listOfFilesOriginal   =    ", opt.listOfFilesOriginal
    

    if not opt.debug:
        pass
    elif opt.debug == 2:
        print 'Logging level set to DEBUG (%d)' % opt.debug
        logging.basicConfig( level=logging.DEBUG )
    elif opt.debug == 1:
        print 'Logging level set to INFO (%d)' % opt.debug
        logging.basicConfig( level=logging.INFO )

    factory = AddMCunc()
    factory._inputFileHisto         = opt.inputFileHisto
    factory._outputFileHistoClone   = opt.outputFileHistoClone
    factory._listOfFilesOriginal    = opt.listOfFilesOriginal
    factory._variable               = opt.variable
    factory._cutName                = opt.cutName


    # list of samples to be added
    groupPlot = {}
    plot = {}
    legend = {}
    if os.path.exists(opt.plotFile) :
      handle = open(opt.plotFile,'r')
      exec(handle)
      handle.close()
  
    factory._plot = plot
    #
    
    factory.FixUncertainties()
    
    print '... and now closing ...'
        
       
       
       
