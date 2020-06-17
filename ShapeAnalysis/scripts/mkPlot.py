#!/usr/bin/env python

import sys
argv = sys.argv
sys.argv = argv[:1]
import ROOT
import optparse
import LatinoAnalysis.Gardener.hwwtools as hwwtools
import os.path
import logging
from array import array
from collections import OrderedDict

#import os.path


# X. Janssen - 21 March 2018
# PlotFactory splitted from this file and moved to python to be able to use in other scripts (mkACPlot.py) 
#

from LatinoAnalysis.ShapeAnalysis.PlotFactory import PlotFactory   

if __name__ == '__main__':
    sys.argv = argv

    print '''
--------------------------------------------------------------------------------------------------

   _ \   |         |         \  |         |                
  |   |  |   _ \   __|      |\/ |   _` |  |  /   _ \   __| 
  ___/   |  (   |  |        |   |  (   |    <    __/  |    
 _|     _| \___/  \__|     _|  _| \__,_| _|\_\ \___| _|   
 
--------------------------------------------------------------------------------------------------
'''    
    usage = 'usage: %prog [options]'
    parser = optparse.OptionParser(usage)

    parser.add_option('--scaleToPlot'    , dest='scaleToPlot'    , help='scale of maxY to maxHistoY'                 , default=3.0  ,    type=float   )
    parser.add_option('--minLogC'        , dest='minLogC'        , help='min Y in log plots'                         , default=0.01  ,    type=float   )
    parser.add_option('--maxLogC'        , dest='maxLogC'        , help='max Y in log plots'                         , default=100   ,    type=float   )
    parser.add_option('--minLogCratio'   , dest='minLogCratio'   , help='min Y in log ratio plots'                   , default=0.001 ,    type=float   )
    parser.add_option('--maxLogCratio'   , dest='maxLogCratio'   , help='max Y in log ratio plots'                   , default=10    ,    type=float   )
    parser.add_option('--maxLinearScale' , dest='maxLinearScale' , help='scale factor for max Y in linear plots (1.45 magic number as default)'     , default=1.45   ,    type=float   )
    parser.add_option('--outputDirPlots' , dest='outputDirPlots' , help='output directory'                           , default='./')
    parser.add_option('--inputFile'      , dest='inputFile'      , help='input file with histograms'                 , default='input.root')
    parser.add_option('--tag'            , dest='tag'            , help='Tag used for the shape file name. Used if inputFile is a directory', default=None)
    parser.add_option('--nuisancesFile'  , dest='nuisancesFile'  , help='file with nuisances configurations'         , default=None )

    parser.add_option('--onlyVariable'   , dest='onlyVariable'   , help='draw only one variable (may be needed in post-fit plots)'          , default=None)
    parser.add_option('--onlyCut'        , dest='onlyCut'        , help='draw only one cut phase space (may be needed in post-fit plots)'   , default=None)
    parser.add_option('--onlyPlot'       , dest='onlyPlot'       , help='draw only specified plot type (comma-separated c, cratio, and/or cdifference)', default=None)

    parser.add_option('--linearOnly'     , dest='linearOnly'     , help='Make linear plot only.', action='store_true', default=False)
    parser.add_option('--logOnly'        , dest='logOnly'        , help='Make log plot only.', action='store_true', default=False)

    parser.add_option('--fileFormats'    , dest='fileFormats'    , help='Output plot file formats (comma-separated png, pdf, root, C, and/or eps). Default "png,root"', default='png,root')

    parser.add_option('--plotNormalizedIncludeData'    , dest='plotNormalizedIncludeData'    , help='plot also normalized distributions for data, for shape comparison purposes', default=None )
    parser.add_option('--plotNormalizedDistributions'         , dest='plotNormalizedDistributions'         , help='plot also normalized distributions for optimization purposes'    ,    action='store_true'     , default=None )
    parser.add_option('--plotNormalizedDistributionsTHstack'  , dest='plotNormalizedDistributionsTHstack'  , help='plot also normalized distributions for optimization purposes, with stacked sig and bkg'  ,    action='store_true'       , default=None )

    parser.add_option('--showIntegralLegend'           , dest='showIntegralLegend'           , help='show the integral, the yields, in the legend'                         , default=0,    type=float )
          
    parser.add_option('--showRelativeRatio'   , dest='showRelativeRatio'   , help='draw instead of data-expected, (data-expected) / expected' ,    action='store_true', default=False)
    parser.add_option('--showDataMinusBkgOnly', dest='showDataMinusBkgOnly', help='draw instead of data-expected, data-expected background only' , action='store_true', default=False)
         
    parser.add_option('--removeWeight', dest='removeWeight', help='Remove weight S/B for PR plots, just do the sum' , action='store_true', default=False)

    parser.add_option('--invertXY', dest='invertXY', help='Invert the weighting for X <-> Y. Instead of slices along Y, do slices along X' , action='store_true', default=False)

    parser.add_option('--postFit', dest='postFit', help='Plot sum of post-fit backgrounds, and the data/post-fit ratio.' , default='n') 

    # read default parsing options as well
    hwwtools.addOptions(parser)
    hwwtools.loadOptDefaults(parser)
    (opt, args) = parser.parse_args()

    sys.argv.append( '-b' )
    ROOT.gROOT.SetBatch()

    print ""
    print "          configuration file =", opt.pycfg
    print "                        lumi =", opt.lumi
    print "                   inputFile =", opt.inputFile
    print "              outputDirPlots =", opt.outputDirPlots
    print " plotNormalizedDistributions =", opt.plotNormalizedDistributions
    print "   plotNormalizedIncludeData =", opt.plotNormalizedIncludeData  
    print " plotNormalizedDistributionsTHstack =", opt.plotNormalizedDistributionsTHstack
    print "          showIntegralLegend =", opt.showIntegralLegend
    print "                 scaleToPlot =", opt.scaleToPlot
    print "                     minLogC =", opt.minLogC
    print "                     maxLogC =", opt.maxLogC
    print "                minLogCratio =", opt.minLogCratio
    print "                maxLogCratio =", opt.maxLogCratio
    print "           showRelativeRatio =", opt.showRelativeRatio
    print "        showDataMinusBkgOnly =", opt.showDataMinusBkgOnly
    print "                removeWeight =", opt.removeWeight
    print "                    invertXY =", opt.invertXY    
    print "                    postFit  =", opt.postFit
    print ""

    opt.scaleToPlot = float(opt.scaleToPlot)
    opt.minLogC = float(opt.minLogC)
    opt.maxLogC = float(opt.maxLogC)

    opt.minLogCratio = float(opt.minLogCratio)
    opt.maxLogCratio = float(opt.maxLogCratio)

    if not opt.debug:
        pass
    elif opt.debug == 2:
        print 'Logging level set to DEBUG (%d)' % opt.debug
        logging.basicConfig( level=logging.DEBUG )
    elif opt.debug == 1:
        print 'Logging level set to INFO (%d)' % opt.debug
        logging.basicConfig( level=logging.INFO )

      
    factory = PlotFactory()
    factory._tag       = opt.tag
    factory._energy    = opt.energy
    factory._lumi      = opt.lumi
    factory._plotNormalizedDistributions = opt.plotNormalizedDistributions
    factory._plotNormalizedIncludeData = opt.plotNormalizedIncludeData
    factory._plotNormalizedDistributionsTHstack = opt.plotNormalizedDistributionsTHstack
    factory._showIntegralLegend = opt.showIntegralLegend

    if opt.onlyPlot is not None:
        factory._plotsToWrite = opt.onlyPlot.split(',')
    factory._plotLinear = opt.linearOnly or not opt.logOnly
    factory._plotLog = opt.logOnly or not opt.linearOnly

    factory._scaleToPlot = opt.scaleToPlot 
    factory._minLogC = opt.minLogC 
    factory._maxLogC = opt.maxLogC 
    factory._minLogCratio = opt.minLogCratio
    factory._maxLogCratio = opt.maxLogCratio
    factory._maxLinearScale = opt.maxLinearScale

    factory._minLogCdifference = opt.minLogCratio
    factory._maxLogCdifference = opt.maxLogCratio

    factory._showRelativeRatio = opt.showRelativeRatio
    factory._showDataMinusBkgOnly = opt.showDataMinusBkgOnly

    factory._removeWeight = opt.removeWeight

    factory._invertXY = opt.invertXY

    factory._fileFormats = opt.fileFormats.split(',')
    
    factory._postFit = opt.postFit

    
    #samples = {}
    samples = OrderedDict()
    if os.path.exists(opt.samplesFile) :
      handle = open(opt.samplesFile,'r')
      exec(handle)
      handle.close()
   
    cuts = {}
    if os.path.exists(opt.cutsFile) :
      handle = open(opt.cutsFile,'r')
      exec(handle)
      handle.close()

    variables = {}
    if os.path.exists(opt.variablesFile) :
      handle = open(opt.variablesFile,'r')
      exec(handle)
      handle.close()

    nuisances = {}
    if opt.nuisancesFile == None :
      print " Please provide the nuisances structure if you want to add nuisances "
    elif os.path.exists(opt.nuisancesFile) :
      handle = open(opt.nuisancesFile,'r')
      exec(handle)
      handle.close()

    import LatinoAnalysis.ShapeAnalysis.utils as utils

    subsamplesmap = utils.flatten_samples(samples)
    categoriesmap = utils.flatten_cuts(cuts)

    utils.update_variables_with_categories(variables, categoriesmap)
    utils.update_nuisances_with_subsamples(nuisances, subsamplesmap)
    utils.update_nuisances_with_categories(nuisances, categoriesmap)
   
    # check if only one cut or only one variable
    # is requested, and filter th elist of cuts and variables
    # using this piece of information
    
    if opt.onlyVariable != None :
      list_to_remove = []
      for variableName, variable in variables.iteritems():
         if variableName != opt.onlyVariable :
           list_to_remove.append(variableName)
      for toRemove in list_to_remove:
        del variables[toRemove]
           
      print  " variables = ", variables

    if opt.onlyCut != None :
      list_to_remove = []
      for cutName, cutExtended in cuts.iteritems():
         if cutName != opt.onlyCut :
           list_to_remove.append(cutName)
      for toRemove in list_to_remove:
        del cuts[toRemove]

      print  " cuts = ", cuts
       
    groupPlot = OrderedDict()
    plot = {}
    legend = {}
    if os.path.exists(opt.plotFile) :
      handle = open(opt.plotFile,'r')
      exec(handle)
      handle.close()
   
    factory.makePlot( opt.inputFile ,opt.outputDirPlots, variables, cuts, samples, plot, nuisances, legend, groupPlot)
    
    print '... and now closing ...'
