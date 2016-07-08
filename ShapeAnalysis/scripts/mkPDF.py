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



# ----------------------------------------------------- ShapeFactory --------------------------------------

class ShapeFactory:
    _logger = logging.getLogger('ShapeFactory')
 
    # _____________________________________________________________________________
    def __init__(self):

        cuts = {}
        self._cuts = cuts

        samples = OrderedDict()
        self._samples = samples

        outputDirPDF = {}
        self._outputDirPDF = outputDirPDF

    # _____________________________________________________________________________
    def _connectInputs(self, samples, inputDir, skipMissingFiles):
        inputs = {}
        histoName = 'list_vectors_weights'
        for process,filenames in samples.iteritems():
          histo = self._buildchainHisto(histoName,[ (inputDir + '/' + f) for f in filenames], skipMissingFiles)
          inputs[process] = histo       
        return inputs

    # _____________________________________________________________________________
    def _buildchainHisto(self, histoName, files, skipMissingFiles):
        
        histoSum = ROOT.TH1F
        isFirstOne = True
        for path in files:
            doesFileExist = True
            self._logger.debug('     '+str(os.path.exists(path))+' '+path)
            if "eos.cern.ch" not in path and "eosuser.cern.ch" not in path:
              if not os.path.exists(path):
                print 'File '+path+' doesn\'t exists'
                doesFileExist = False
                if not skipMissingFiles : raise RuntimeError('File '+path+' doesn\'t exists')
            else:
              if not self._testEosFile(path):
                doesFileExist = False
                if not skipMissingFiles : raise RuntimeError('File '+path+' doesn\'t exists')
            if doesFileExist :
              fileIn = ROOT.TFile(path)
              print " path = ", path
              if isFirstOne :
                histoSum = fileIn.Get(histoName)   
                isFirstOne = False
              else :
                histoSumTemp = fileIn.Get(histoName)   
                histoSum.Add(histoSumTemp)
              
        return histoSum


    # _____________________________________________________________________________
    def _testEosFile(self,path): 
      eoususer='/afs/cern.ch/project/eos/installation/0.3.84-aquamarine.user/bin/eos.select'
      if 'eosuser.cern.ch' in path: 
        if os.system(eoususer+' ls '+path.split('/eosuser.cern.ch/')[1]) == 0 : return True
      return False 



    # _____________________________________________________________________________
    def makePDF(self, inputFile, outputDirPDF, cuts, samples, inputDir):

        print "================="
        print "==== makePDF ===="
        print "================="

        # NB: the samples have to be OF THE SAME GENERATOR
        #     you cannot get pdf/qcd uncertainty mixing different samples
        #     like mixing A+B, where A is powheg and B is MG5.
        #     If you want to do this
        #     you "mix" it by hand from the output of this code ;)
        #
        
        self._samples   = samples
        self._cuts      = cuts

        self._outputDirPDF = outputDirPDF
        os.system ("mkdir " + outputDirPDF + "/") 

        fileIn = ROOT.TFile(inputFile, "READ")

        variableName = "list_vectors_weights"
        # get the pre-any-cut histogram
        list_of_trees_to_connect = {}
        for sampleName, sample in self._samples.iteritems():
          list_of_trees_to_connect[sampleName] = sample['name']
              
        #                                                                    skipMissingFiles
        preCutsHistograms = self._connectInputs( list_of_trees_to_connect, inputDir, False)
        
        for cutName in self._cuts :
          print "cut = ", cutName, " :: ", cuts[cutName]
            
          for sampleName, sample in self._samples.iteritems():
          
            # get the after-cut histogram
            
            shapeName = cutName+"/"+variableName+'/histo_' + sampleName
            print '     -> shapeName = ', shapeName,
            histoAfterCuts = fileIn.Get(shapeName)
              
            # and now let's play with the histograms
            # the nominal:         preCutsHistograms[shapeName]
            # and the after cuts:  histoAfterCuts
                           
          
        print " >> all but really all "
        


   # _____________________________________________________________________________
   # --- squared sum
    def SumQ(self, A, B):
       return math.sqrt(A*A + B*B)

   # _____________________________________________________________________________
   # --- Ratio: if denominator is zero, then put 0!
    def Ratio(self, A, B):
       if B == 0:
         #print "divide by 0"
         return 0.
       else :
         return A / B
 
                  
   # _____________________________________________________________________________
    def GetMaximumIncludingErrors(self, histo):
        maxWithErrors = 0.
        for iBin in range(1, histo.GetNbinsX()+1):
          binHeight = histo.GetBinContent (iBin) + histo.GetBinError (iBin)
          if binHeight > maxWithErrors :
            maxWithErrors = binHeight
      
        return maxWithErrors;

   # _____________________________________________________________________________
    def GetMinimum(self, histo):
        minimum = -1.
        for iBin in range(1, histo.GetNbinsX()+1):
          binHeight = histo.GetBinContent (iBin)
          if binHeight < minimum or minimum<0:
            minimum = binHeight
      
        return minimum;
 
 
    # _____________________________________________________________________________
    def defineStyle(self):

        print "=================="
        import LatinoAnalysis.ShapeAnalysis.tdrStyle as tdrStyle
        tdrStyle.setTDRStyle()
        
        ROOT.TGaxis.SetExponentOffset(-0.08, 0.00,"y")

        
   


if __name__ == '__main__':
    print '''
--------------------------------------------------------------------------------------------------



   _ \   __ \   ____|                                      |          _)         |          
  |   |  |   |  |          |   |  __ \    __|   _ \   __|  __|   _` |  |  __ \   __|  |   | 
  ___/   |   |  __|        |   |  |   |  (      __/  |     |    (   |  |  |   |  |    |   | 
 _|     ____/  _|         \__,_| _|  _| \___| \___| _|    \__| \__,_| _| _|  _| \__| \__, | 
                                                                                     ____/  

 
--------------------------------------------------------------------------------------------------
'''    
    usage = 'usage: %prog [options]'
    parser = optparse.OptionParser(usage)

    parser.add_option('--outputDirPDF'   , dest='outputDirPDF'   , help='output directory for values and plots'           , default='./')
    parser.add_option('--inputFile'      , dest='inputFile'      , help='input file with histograms'                      , default='input.root')
    parser.add_option('--inputDir'       , dest='inputDir'       , help='input directory where to find the default trees' , default='./data/')
          
    # read default parsing options as well
    hwwtools.addOptions(parser)
    hwwtools.loadOptDefaults(parser)
    (opt, args) = parser.parse_args()

    sys.argv.append( '-b' )
    ROOT.gROOT.SetBatch()


    print " configuration file = ", opt.pycfg
    
    print " inputFile          = ", opt.inputFile
    print " outputDirPDF       = ", opt.outputDirPDF
    print " inputDir           = ", opt.inputDir
     
    if not opt.debug:
        pass
    elif opt.debug == 2:
        print 'Logging level set to DEBUG (%d)' % opt.debug
        logging.basicConfig( level=logging.DEBUG )
    elif opt.debug == 1:
        print 'Logging level set to INFO (%d)' % opt.debug
        logging.basicConfig( level=logging.INFO )

      
    factory = ShapeFactory()
    
    cuts = {}
    if os.path.exists(opt.cutsFile) :
      handle = open(opt.cutsFile,'r')
      exec(handle)
      handle.close()
    
    samples = OrderedDict()
    if os.path.exists(opt.samplesFile) :
      handle = open(opt.samplesFile,'r')
      exec(handle)
      handle.close()
    
   
    factory.makePDF( opt.inputFile ,opt.outputDirPDF, cuts, samples, opt.inputDir)
    
    print '... and now closing ...'
        
       
