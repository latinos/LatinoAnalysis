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
    
    nEvt = 0
    nTot = 0
    nPos = 0
    nNeg = 0
    
    print 'Opening: ',opt.inputFile
    fileIn = ROOT.TFile.Open(opt.inputFile, "READ")
    fileIn.ls()
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
    print 'baseW: xs,N -> W', xs, nEvt , baseW , ' nTot= ', nTot
    
    
    