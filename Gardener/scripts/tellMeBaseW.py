#!/usr/bin/env python
import sys, re, os, os.path, math
import optparse

from collections import OrderedDict

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

    parser.add_option('--inputFile'      , dest='inputFile'      , help='input file with histograms'                 , default=None)
    parser.add_option('--inputFiles'     , dest='inputFiles'     , help='list of input files with histograms'        , default=None)
    parser.add_option('--folder'         , dest='folder'         , help='folder for input files with histograms'     , default='./')
          
    # read default parsing options as well
    (opt, args) = parser.parse_args()

    sys.argv.append( '-b' )
    ROOT.gROOT.SetBatch()


    print " inputFile =               ", opt.inputFile

    if opt.inputFiles != None :
      samples = OrderedDict()
      if os.path.exists(opt.inputFiles) :
        handle = open(opt.inputFiles,'r')
        exec(handle)
        handle.close()

      for sampleName, sample in samples.iteritems():
        #print '     -> sampleName = ', sampleName
        list_of_trees_to_connect = sample['name']      
        for file_name in list_of_trees_to_connect :
          #print 'file = ', file_name
          nEvt = 0
          nTot = 0
          nPos = 0
          nNeg = 0
          
          if os.path.exists(opt.folder + '/' + file_name) :
            fileIn = ROOT.TFile.Open(opt.folder + '/' + file_name, "READ")
            #fileIn.ls()
            h_mcWeightPos = fileIn.Get('mcWeightPos')
            h_mcWeightNeg = fileIn.Get('mcWeightNeg')
            if h_mcWeightPos.__nonzero__() and h_mcWeightNeg.__nonzero__() :
              nEvt += h_mcWeightPos.GetBinContent(1) - h_mcWeightNeg.GetBinContent(1)
              nPos += h_mcWeightPos.GetBinContent(1)
              nNeg += h_mcWeightNeg.GetBinContent(1) 
              #print 'Pos, Neg = ',h_mcWeightPos.GetBinContent(1),h_mcWeightNeg.GetBinContent(1)
            else:
              totalEvents = fileIn.Get('totalEvents')
              if totalEvents.__nonzero__() :
                nEvt += fileIn.Get('totalEvents').GetBinContent(1)
                nPos += fileIn.Get('totalEvents').GetBinContent(1)
           
            totalEvents = fileIn.Get('totalEvents')
            if totalEvents.__nonzero__() :
              nTot += fileIn.Get('totalEvents').GetBinContent(1)
            fileIn.Close()
        
          xs = 1.
          if nEvt != 0 :
            baseW = float(xs)*1000./nEvt
            print '[', sampleName, ']: file, N, nPos, nNeg -> W', file_name, ', ', nEvt , ', ', nPos , ', ', nNeg , ' , ', baseW , ' nTot= ', nTot
            
            
          
  
    else :
      nEvt = 0
      nTot = 0
      nPos = 0
      nNeg = 0

      print 'Opening: ',opt.inputFile
      if opt.inputFile != None :
        fileIn = ROOT.TFile.Open(opt.inputFile, "READ")
        #fileIn.ls()
        h_mcWeightPos = fileIn.Get('mcWeightPos')
        h_mcWeightNeg = fileIn.Get('mcWeightNeg')
        if h_mcWeightPos.__nonzero__() and h_mcWeightNeg.__nonzero__() :
          nEvt += h_mcWeightPos.GetBinContent(1) - h_mcWeightNeg.GetBinContent(1)
          nPos += h_mcWeightPos.GetBinContent(1)
          nNeg += h_mcWeightNeg.GetBinContent(1) 
          print 'Pos, Neg = ',h_mcWeightPos.GetBinContent(1),h_mcWeightNeg.GetBinContent(1)
        else:
          nEvt += fileIn.Get('totalEvents').GetBinContent(1)
          nPos += fileIn.Get('totalEvents').GetBinContent(1)
        
        nTot += fileIn.Get('totalEvents').GetBinContent(1)
        fileIn.Close()
      
      xs = 1.
      baseW = float(xs)*1000./nEvt
      print 'baseW: xs,N -> W', xs, ' , ', nEvt , ' , ', baseW , ' nTot= ', nTot
    
    
    