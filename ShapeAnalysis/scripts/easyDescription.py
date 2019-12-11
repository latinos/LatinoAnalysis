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
    parser.add_option('--inputFileNuisances'    , dest='inputFileNuisances'    , help='input file with nuisances'               , default=None)
    parser.add_option('--outputFileNuisances'   , dest='outputFileNuisances'   , help='output file with nuisances expanded'     , default=None)
    parser.add_option('--inputFileCuts'         , dest='inputFileCuts'         , help='input file with cuts'                    , default=None)
    parser.add_option('--outputFileCuts'        , dest='outputFileCuts'        , help='output file with cuts expanded'          , default=None)
    #parser.add_option('--inputFile'      , dest='inputFile'      , help='input file with samples'                 , default=None)
          
    # read default parsing options as well
    (opt, args) = parser.parse_args()

    sys.argv.append( '-b' )
    ROOT.gROOT.SetBatch()


    print "#   inputFileSamples  =               ", opt.inputFileSamples
    print "#   outputFileSamples =               ", opt.outputFileSamples
    print "#   inputFileNuisances  =             ", opt.inputFileNuisances
    print "#   outputFileNuisances =             ", opt.outputFileNuisances
    print "#   inputFileCuts  =                  ", opt.inputFileCuts
    print "#   outputFileCuts =                  ", opt.outputFileCuts
                    
    #                
    # unfold Samples
    #
    
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
      
      #printSampleDic (samples)
       
        
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
         
          if 'subsamples' in sample :
            fileOutSamples.write("     \'subsamples\'  :   " + str(sample['subsamples']) + " ,\n")



                
          fileOutSamples.write("}  \n") 
          fileOutSamples.write("   \n ") 

          
        fileOutSamples.close() 

        
        
        

                    
    #                
    # unfold Nuisances
    #
    
    if opt.inputFileNuisances != None :
      nuisances = OrderedDict()
      if os.path.exists(opt.inputFileNuisances) :
        handle = open(opt.inputFileNuisances,'r')
        exec(handle)
        handle.close()

       
        
      if opt.outputFileNuisances != None :
        
        fileOutNuisances = open(opt.outputFileNuisances,"w") 

        fileOutNuisances.write("# \n")
        fileOutNuisances.write("# Expanded version of samples.py \n")
        fileOutNuisances.write("# \n")
        
        #print " nuisances = ", nuisances
         
        for nuisanceName, nuisance in nuisances.iteritems():
          
          fileOutNuisances.write("nuisances[\'" + nuisanceName + "\'] = { \n") 

          if 'name' in nuisance :
            fileOutNuisances.write("     \'name\'  :   '" + nuisance['name'] + "' ,\n")

          if 'kind' in nuisance :
            fileOutNuisances.write("     \'kind\'  :   '" + nuisance['kind'] + "' ,\n")

          if 'type' in nuisance :
            fileOutNuisances.write("     \'type\'  :   '" + nuisance['type'] + "' ,\n")

          if 'samples' in nuisance :
            fileOutNuisances.write("     \'samples\'  :  { \n")
            for samples in nuisance['samples'] :
              fileOutNuisances.write("            '" + str(samples) + "',\n")        
            fileOutNuisances.write("     },  \n")

          if 'cuts' in nuisance :
            fileOutNuisances.write("     \'cuts\'  :  [ \n")
            for cuts in nuisance['cuts'] :
              fileOutNuisances.write("            '" + str(cuts) + "',\n")        
            fileOutNuisances.write("     ],  \n")


          if 'folderUp' in nuisance :
            fileOutNuisances.write("     \'folderUp\'    :   '" + nuisance['folderUp'] + "' ,\n")

          if 'folderDown' in nuisance :
            fileOutNuisances.write("     \'folderDown\'  :   '" + nuisance['folderDown'] + "' ,\n")


          fileOutNuisances.write("}  \n") 
          fileOutNuisances.write("   \n ") 

          
        fileOutNuisances.close() 

           

    #                
    # unfold Cuts
    #
    
    if opt.inputFileCuts != None :
      cuts = OrderedDict()
      if os.path.exists(opt.inputFileCuts) :
        handle = open(opt.inputFileCuts,'r')
        exec(handle)
        handle.close()

      if opt.outputFileCuts != None :
        
        fileOutCuts = open(opt.outputFileCuts,"w") 

        fileOutCuts.write("# \n")
        fileOutCuts.write("# Expanded version of cuts.py \n")
        fileOutCuts.write("# \n")
        
        # if supercut
        if 'supercut' in locals():
          fileOutCuts.write("supercut = \' " + str(supercut) + " \' \n\n\n") 
        
        # now the cuts

        for cutName, cut in cuts.iteritems():
          
          fileOutCuts.write("cuts[\'" + cutName + "\'] = ' \\\n") 

          fileOutCuts.write(" " + cut + " \\\n") 
                
          fileOutCuts.write(" ' \n") 
          fileOutCuts.write("   \n ") 

          
        fileOutCuts.close() 

        
        
        
        
        
        
#
# How to use it:
#
# easyDescription.py   --inputFileSamples=../../PlotsConfigurations/Configurations/ggH/Full2016/samples.py   --outputFileSamples=test.py
# easyDescription.py   --inputFileSamples=../../PlotsConfigurations/Configurations/ggH/Full2016/samples.py  --inputFileNuisances=../../PlotsConfigurations/Configurations/ggH/Full2016/nuisances.py   --outputFileNuisances=testNuisances.py
# easyDescription.py   --inputFileCuts=cuts.py   --outputFileCuts=cuts_expanded.py
#
#  NB: the "samples" file has to be defined, because some global variables are defined there (e.g. NLep)
#


