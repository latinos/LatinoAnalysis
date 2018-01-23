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



# ----------------------------------------------------- Plow --------------------------------------

class Plow:
    _logger = logging.getLogger('Plow')
 
    # _____________________________________________________________________________
    def __init__(self):

        variables = {}
        self._variables = variables

        
 
    # _____________________________________________________________________________
    def makePostFitTable(self):

        print "========================="
        print "==== makePostFitTable ===="
        print "========================="
        
        print " self.inputFileCombine " , self._inputFileCombine
        
        
        fileIn = ROOT.TFile(self._inputFileCombine, "READ")


        self._outFile = open(self._outputFileName, "w")

        self._outFile.write ("")
                 
        self._outFile.write('\n')
        self._outFile.write('\n')
        self._outFile.write('\n')
        
        self._outFile.write('\\begin{table}[h!]\\begin{center}\n')
        self._outFile.write('  \\begin{tabular}{|')
       
        self._outFile.write('c|') # the column with the names   
        self._outFile.write('c|') # the column with the number   
        self._outFile.write('}\n')
       
        self._outFile.write('\\hline\n')
        self._outFile.write('Sample   &   Yield  \\\\ \n')
        self._outFile.write('\\hline\n')

    

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
       
       

        self._samples_yields = OrderedDict()
        
        template_histogram = 0

        #
        # initialize, to preserve the order of the OrderedDict
        #
        for samples_key,samples_values in self._samples.iteritems():
          self._samples_yields [samples_key] = (0, 0)
          #                                  yield, error
          
        #  
        # get data  
        #
        for samples_key,samples_values in self._samples.iteritems():

           # 
           # propagate signal from pre-fit if triggered
           # NB: this is needed for exclusion analyses, where the fitted signal is 0
           #     or to show the signal in the background only fit 
           #
           if (self._getSignalFromPrefit == 1 and samples_key in self._structure.keys() and self._structure[samples_key]['isSignal'] == 1 ) or samples_key == "DATA" :
             
             #print "self._inputFile = " , self._inputFile
             
             fileInJustForDATA = ROOT.TFile(self._inputFile, "READ")
             histo = fileInJustForDATA.Get(self._cutNameInOriginal + "/" + self._variable + "/histo_" + samples_key)   
             #print " histo = ", self._cutNameInOriginal + "/" + self._variable + "/histo_" + samples_key
             
             errorVal = ROOT.Double(0)
             tempo = histo.IntegralAndError(-1, histo.GetNbinsX(), errorVal)
             self._samples_yields [samples_key] = (histo.Integral(), errorVal)



         
        for samples_key,samples_values in self._samples.iteritems():

           #print " samples_key = ", samples_key
           
           copied_from_original = False
           
           #if samples_key != "DATA" :
           if not ((self._getSignalFromPrefit == 1 and samples_key in self._structure.keys() and self._structure[samples_key]['isSignal'] == 1 ) or samples_key == "DATA"):
             if not (fileIn.Get(folder_fit_name + "/" + self._cut).GetListOfKeys().Contains(samples_key) ):
               #print "Sample ", samples_key, " does not exist in ", fileIn
               #
               # If for some reason this histogram is not available in the combine output
               # get the histogram from the input root file, the output of mkShape
               # and scale that to 0, so that it is propagated to be used by mkPlot
               # but it will have 0 contribution, as expected (but legends and all the rest will be ok and nice)
               #
               # continue
               #
               
               self._samples_yields [samples_key] = (0, 0)
               
               copied_from_original = True

             #
             #
             #
             if not copied_from_original :  
               
               histo = fileIn.Get(folder_fit_name + "/" + self._cut + "/" + samples_key)      
               #print folder_fit_name + "/" + self._cut + "/" + samples_key
               
               histo.SetName  ('histo_' + samples_key)
               histo.SetTitle ('histo_' + samples_key)

               errorVal = ROOT.Double(0)
               tempo = histo.IntegralAndError(-1, histo.GetNbinsX(), errorVal)
               self._samples_yields [samples_key] = (histo.Integral(), errorVal)
               


        #
        # total signal and total background, and total
        #
        
        #
        # total signal
        histo_total_signal = fileIn.Get(folder_fit_name + "/" + self._cut + "/" + "total_signal")      
        
        histo_total_signal.SetName  ('histo_' + 'total_signal')
        histo_total_signal.SetTitle ('histo_' + 'total_signal')

        errorVal_sig = ROOT.Double(0)
        tempo = histo_total_signal.IntegralAndError(-1, histo_total_signal.GetNbinsX(), errorVal_sig)        
        self._samples_yields_total_signal = (histo_total_signal.Integral(), errorVal_sig)
        #print "errorVal_sig = ", errorVal_sig
        
        #
        # total background
        histo_total_background = fileIn.Get(folder_fit_name + "/" + self._cut + "/" + "total_background")      
        
        histo_total_background.SetName  ('histo_' + 'total_background')
        histo_total_background.SetTitle ('histo_' + 'total_background')
        
        errorVal_bkg = ROOT.Double(0) 
        tempo = histo_total_background.IntegralAndError(-1, histo_total_background.GetNbinsX(), errorVal_bkg)        
        self._samples_yields_total_background = (histo_total_background.Integral(), errorVal_bkg)
        #print "errorVal_bkg = ", errorVal_bkg
        
        
        #
        # total
        histo_total = fileIn.Get(folder_fit_name + "/" + self._cut + "/" + "total")      
        
        histo_total.SetName  ('histo_' + 'total')
        histo_total.SetTitle ('histo_' + 'total')
        
        errorVal_tot = ROOT.Double(0) 
        tempo = histo_total.IntegralAndError(-1, histo_total.GetNbinsX(), errorVal_tot)        
        self._samples_yields_total = (histo_total.Integral(), errorVal_tot)
        #print "errorVal_tot = ", errorVal_tot



        #
        # Now write the results into the text file
        #


        for samples_key,samples_values in self._samples_yields.iteritems():
          if samples_key != "DATA" :
            self._outFile.write(' %13s ' % samples_key.replace('_', '-'))
            self._outFile.write(' & %.2f \\\\  \n ' % (samples_values[0]) )
        self._outFile.write('\\hline\n')

        self._outFile.write(' Tot Sig ' )
        self._outFile.write(' & %.2f $\\pm$ %.2f \\\\  \n ' % (self._samples_yields_total_signal[0], self._samples_yields_total_signal[1]) )

        self._outFile.write(' Tot Bkg ' )
        self._outFile.write(' & %.2f $\\pm$ %.2f \\\\  \n ' % (self._samples_yields_total_background[0], self._samples_yields_total_background[1]) )

        self._outFile.write('\\hline\n')
        self._outFile.write(' Tot    ' )
        self._outFile.write(' & %.2f $\\pm$ %.2f \\\\  \n ' % (self._samples_yields_total[0], self._samples_yields_total[1]) )

        self._outFile.write('\\hline\n')
        for samples_key,samples_values in self._samples_yields.iteritems():
          if samples_key == "DATA" :
            self._outFile.write(' %13s ' % samples_key.replace('_', '-'))
            self._outFile.write(' & %.2f $\\pm$ %.2f  \\\\  \n ' % (samples_values[0], math.sqrt(samples_values[0])) )


        self._outFile.write('  \\end{tabular}')
        self._outFile.write(' \n')
        self._outFile.write('  \\caption{\n')
        self._outFile.write('     Summary table:: rates. \n ' )
        self._outFile.write('\\label{tab:yields' )
        self._outFile.write('}\n ' )
        
        self._outFile.write('  }\n')
        self._outFile.write('\\end{center}\n')
        self._outFile.write('\\end{table}\n')
       
        self._outFile.close()





        

if __name__ == '__main__':
    print '''
----------------------------------------------------------------------------------------------------------------------------------

    
       _ \                                            _ \               |         ____| _)  |       __ __|       |      |             
      |   |   __|  _ \  __ \    _` |   __|  _ \      |   |  _ \    __|  __|       |      |  __|        |   _` |  __ \   |   _ \   __| 
      ___/   |     __/  |   |  (   |  |     __/      ___/  (   | \__ \  | _____|  __|    |  |          |  (   |  |   |  |   __/ \__ \ 
     _|     _|   \___|  .__/  \__,_| _|   \___|     _|    \___/  ____/ \__|      _|     _| \__|       _| \__,_| _.__/  _| \___| ____/ 
                       _|                                                                                                             
                       
                       

----------------------------------------------------------------------------------------------------------------------------------
'''    
    usage = 'usage: %prog [options]'
    parser = optparse.OptionParser(usage)

    parser.add_option('--inputFileCombine'      , dest='inputFileCombine'      , help='input file with roofit results, mlfit'                          , default='input.root')
    parser.add_option('--outputFile'            , dest='outputFile'            , help='output file with tables '                                       , default='output.txt')
    parser.add_option('--variable'              , dest='variable'              , help='variable name'  , default='mll')
    parser.add_option('--cut'                   , dest='cut'                   , help='cut name'  , default='0j')
    parser.add_option('--cutNameInOriginal'     , dest='cutNameInOriginal'     , help='cut name as appears in cuts.py'  , default='')
    parser.add_option('--inputFile'             , dest='inputFile'             , help='input file with histograms (only to get the DATA distribution)' , default='input.root')
    parser.add_option('--kind'                  , dest='kind'                  , help='which kind of post-fit distribution: s = signal + background, b = background only, p = prefit'  , default='s')
    parser.add_option('--structureFile'         , dest='structureFile'         , help='file with datacard configurations'          , default=None )
    parser.add_option('--getSignalFromPrefit'   , dest='getSignalFromPrefit'   , help='get the signal shape and normalization from pre-fit. Needed for exclusion analyses. Set to 1 to trigger this.', default=0   ,    type=int)
          
          
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
    print " getSignalFromPrefit   =          ", opt.getSignalFromPrefit
    print " structureFile         =          ", opt.structureFile



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

    factory = Plow()
    factory._inputFileCombine  = opt.inputFileCombine
    factory._outputFileName    = opt.outputFile
    factory._variable          = opt.variable
    factory._cut               = opt.cut
    factory._cutNameInOriginal = opt.cutNameInOriginal
    factory._kind              = opt.kind
    factory._getSignalFromPrefit = opt.getSignalFromPrefit
    

    # ~~~~
    samples = OrderedDict()
    if os.path.exists(opt.samplesFile) :
      handle = open(opt.samplesFile,'r')
      exec(handle)
      handle.close()

    factory._samples = samples

    # ~~~~
    structure = {}
    if opt.structureFile == None :
       print " Please provide the datacard structure "
       #exit ()

    elif os.path.exists(opt.structureFile) :
      handle = open(opt.structureFile,'r')
      exec(handle)
      handle.close()


    factory._structure = structure
    
    factory._inputFile = opt.inputFile
    
    factory.makePostFitTable()
    
    print '... and now closing ...'
        
       
       
       
