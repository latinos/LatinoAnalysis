#!/usr/bin/env python
import sys, re, os, os.path, math
import optparse

from collections import OrderedDict

from LatinoAnalysis.Tools.commonTools import *

import ROOT



if __name__ == '__main__':
    print '''
#  --------------------------------------------------------------------------------------------------
#  
#     _ \                                                                 |                          |                       
#    |   |  _` |  __ \   |   |   __|  |   |  __ `__ \      \ \   /  _ \   | \ \   /  _ \  __ \    _` |  |   |  __ `__ \      
#    ___/  (   |  |   |  |   |  |     |   |  |   |   |      \ \ /  (   |  |  \ \ /   __/  |   |  (   |  |   |  |   |   |     
#   _|    \__,_|  .__/  \__, | _|    \__,_| _|  _|  _|       \_/  \___/  _|   \_/  \___| _|  _| \__,_| \__,_| _|  _|  _|     
#                _|     ____/                                                                                                
#  
#  --------------------------------------------------------------------------------------------------
'''    

    usage = 'usage: %prog [options]'
    parser = optparse.OptionParser(usage)

    parser.add_option('--inputFileSamples'      , dest='inputFileSamples'      , help='input file with samples'                 , default=None)
    parser.add_option('--outputFileSamples'     , dest='outputFileSamples'     , help='output file with samples expanded'       , default=None)
    #parser.add_option('--inputFile'      , dest='inputFile'      , help='input file with samples'                 , default=None)
          
    # read default parsing options as well
    (opt, args) = parser.parse_args()

    sys.argv.append( '-b' )
    ROOT.gROOT.SetBatch()


    print "#   inputFileSamples  =               ", opt.inputFileSamples
    print "#   outputFileSamples =               ", opt.outputFileSamples
                                                        
    if opt.inputFileSamples != None :
      samples = OrderedDict()
      if os.path.exists(opt.inputFileSamples) :
        handle = open(opt.inputFileSamples,'r')
        exec(handle)
        handle.close()

      #for sampleName, sample in samples.iteritems():
        #print '        '
        #print '     -> ', sampleName, ' :: '
        #if 'name' in sample :
          #for fileName in sample['name'] :
            #print '         ', fileName
        #if 'weight' in sample :
          #print '    weight =     ', sample['weight']
      
      #
      # samples
      #
      
      printSampleDic (samples)
       
        
      if opt.outputFileSamples != None :
        
        fileOutSamples = open(opt.outputFileSamples,"w") 

        fileOutSamples.write("# \n")
        fileOutSamples.write("# Expanded version of samples.py \n")
        fileOutSamples.write("# \n")
        

        for sampleName, sample in samples.iteritems():
          
          fileOutSamples.write("samples[\'" + sampleName + "\'] = { \n") 

          if 'name' in sample :
            fileOutSamples.write("     \'name\'  :  [ \n")
            for fileName in sample['name'] :
              fileOutSamples.write("            '" + fileName + "',\n")        
            fileOutSamples.write("     ],  \n")


          if 'weights' in sample :
            fileOutSamples.write("     \'weights\'  :  [ \n")
            for weights in sample['weights'] :
              fileOutSamples.write("            '" + str(weights) + "',\n")        
            fileOutSamples.write("     ],  \n")
          
          if 'isData' in sample :
            fileOutSamples.write("     \'isData\'  :  [ \n")
            for isData in sample['isData'] :
              fileOutSamples.write("            '" + str(isData) + "',\n")        
            fileOutSamples.write("     ],  \n")
          
          
          if 'weight' in sample :
            fileOutSamples.write("     \'weight\'  :   '" + sample['weight'] + "' ,\n")

          if 'FilesPerJob' in sample :
            fileOutSamples.write("     \'FilesPerJob\'  :   " + str(sample['FilesPerJob']) + " ,\n")
          
                
          fileOutSamples.write("}  \n") 
          fileOutSamples.write("   \n ") 

          
        fileOutSamples.close() 

        
        
        
        
        
        
        
#
# How to use it:
#
# easyDescription.py   --inputFileSamples=../../PlotsConfigurations/Configurations/ggH/Full2016/samples.py   --outputFileSamples=test.py
#