#!/usr/bin/env python

import json
import sys
import ROOT
import optparse
import LatinoAnalysis.Gardener.hwwtools as hwwtools
import logging
import os.path







# ----------------------------------------------------- DatacardFactory --------------------------------------

class DatacardFactory:
    _logger = logging.getLogger('DatacardFactory')

    # _____________________________________________________________________________
    def __init__(self):
      
        variables = {}
        self._variables = variables

        cuts = {}
        self._cuts = cuts

        samples = {}
        self._samples = samples

        ## list of [processes]  
        self.processes = []
        ## list of [signal processes]
        self.signals = []
        ## list of [background processes]
        self.backgrounds = []
        ## data
        self.data = []        
        ## list of [(name of uncert, type of nuisance, list of samples affected, with value, additional value [in case of gmN])]
        self.systs   = []

    # _____________________________________________________________________________
    # a datacard for each "cut" and each "variable" will be produced, in separate sub-folders, names after "cut/variable"
    # _____________________________________________________________________________
    def makeDatacards( self, inputFile, outputDirDatacard, variables, cuts, samples, structureFile):
    
        print "======================="
        print "==== makeDatacards ===="
        print "======================="
        
        self._variables = variables
        self._samples   = samples
        self._cuts      = cuts

        self._outputDirDatacard = outputDirDatacard

        # divide the list of samples among signal, background and data
        for sampleName, sample in self._samples.iteritems():
          if structureFile[sampleName]['isSignal'] == 1 :
            self.signals.append(sampleName)
          if structureFile[sampleName]['isData'] == 1 :
            self.data.append(sampleName)
          if structureFile[sampleName]['isSignal'] == 0 and structureFile[sampleName]['isData'] == 0:
            self.backgrounds.append(sampleName)
          
        # loop over cuts  
        for cutName in self._cuts :
          print "cut = ", cutName, " :: ", cuts[cutName]
          os.mkdir (self._outputDirDatacard + "/" + cutName)
          # loop over variables
          for variableName, variable in self._variables.iteritems():
            print "  variableName = ", variableName
            
            # prepare yields
            yieldsSig  = {}
            yieldsBkg  = {}
            yieldsData = {}
            for sampleName in self.signals:
              yieldsSig[sampleName] = 1.0
              # ge the integral from histogram
            for sampleName in self.backgrounds:
              yieldsBkg[sampleName] = 1.0
              # ge the integral from histogram
            for sampleName in self.data:
              yieldsData['data'] = 1.0 # data is data!
              # ge the integral from histogram
                          
            os.mkdir (self._outputDirDatacard + "/" + cutName + "/" + variableName) 
            os.mkdir (self._outputDirDatacard + "/" + cutName + "/" + variableName + "/shapes/") # and the folder for the root files 
        
            # start creating the datacard 
            cardPath = self._outputDirDatacard + "/" + cutName + "/" + variableName  + "/datacard.txt"
            print 'Writing to ' + cardPath 
            card = open( cardPath ,"w")
            card.write('## Shape input card\n')
        
            card.write('imax 1 number of channels\n')
            card.write('jmax * number of background\n')
            card.write('kmax * number of nuisance parameters\n') 

            card.write('-'*100+'\n')
            tagNameToAppearInDatacard = "test"
            card.write('bin         %s' % tagNameToAppearInDatacard+'\n')
            if len(self.data) == 0:
              self._log.warning( 'no data, no fun! ')
              raise RuntimeError('No Data found!')

            card.write('observation %.0f\n' % yieldsData['data'])
            
            #card.write('shapes  *           * '+
                       #fileFmt.format(mass=self._mass, bin=self._bin)+
                       #'     histo_$PROCESS histo_$PROCESS_$SYSTEMATIC'+'\n')
            #card.write('shapes  data_obs    * '+
                       #fileFmt.format(mass=self._mass, bin=self._bin)+
                       #'     histo_Data'+'\n')

            card.write('-'*100+'\n')

            card.write('\n')
            card.close()



if __name__ == '__main__':
    print '''
--------------------------------------------------------------------------------------------------

  __ \          |                                 |       \  |         |                
  |   |   _` |  __|   _` |   __|   _` |   __|  _` |      |\/ |   _` |  |  /   _ \   __| 
  |   |  (   |  |    (   |  (     (   |  |    (   |      |   |  (   |    <    __/  |    
 ____/  \__,_| \__| \__,_| \___| \__,_| _|   \__,_|     _|  _| \__,_| _|\_\ \___| _|    
                                                                                
--------------------------------------------------------------------------------------------------
'''    

    usage = 'usage: %prog [options]'
    parser = optparse.OptionParser(usage)

    parser.add_option('--tag'                , dest='tag'               , help='Tag used for the shape file name'           , default=None)
    parser.add_option('--sigset'             , dest='sigset'            , help='Signal samples [SM]'                        , default='SM')
    parser.add_option('--outputDirDatacard'  , dest='outputDirDatacard' , help='output directory'                           , default='./')
    parser.add_option('--inputFile'          , dest='inputFile'         , help='input directory'                            , default='./input.root')
    parser.add_option('--structureFile'      , dest='structureFile'     , help='file with datacard configurations'          , default=None )

          
    # read default parsing options as well
    hwwtools.addOptions(parser)
    hwwtools.loadOptDefaults(parser)
    (opt, args) = parser.parse_args()

    sys.argv.append( '-b' )
    ROOT.gROOT.SetBatch()


    print " configuration file = ", opt.pycfg
    
    print " inputFile =                  ", opt.inputFile
    print " outputDirDatacard =          ", opt.outputDirDatacard
 
 
    if not opt.debug:
        pass
    elif opt.debug == 2:
        print 'Logging level set to DEBUG (%d)' % opt.debug
        logging.basicConfig( level=logging.DEBUG )
    elif opt.debug == 1:
        print 'Logging level set to INFO (%d)' % opt.debug
        logging.basicConfig( level=logging.INFO )

      
    factory = DatacardFactory()
    factory._energy    = opt.energy
    factory._lumi      = opt.lumi
    factory._tag       = opt.tag
    
    
    variables = {}
    if os.path.exists(opt.variablesFile) :
      handle = open(opt.variablesFile,'r')
      exec(handle)
      handle.close()
    
    cuts = {}
    if os.path.exists(opt.cutsFile) :
      handle = open(opt.cutsFile,'r')
      exec(handle)
      handle.close()
    
    samples = {}
    if os.path.exists(opt.samplesFile) :
      handle = open(opt.samplesFile,'r')
      exec(handle)
      handle.close()
    
    
    structure = {}
    if opt.structureFile == None :
       print " Please provide the datacard structure "
       exit ()
       
    if os.path.exists(opt.structureFile) :
      handle = open(opt.structureFile,'r')
      exec(handle)
      handle.close()
    
    factory.makeDatacards( opt.inputFile ,opt.outputDirDatacard, variables, cuts, samples, structure)
    
        
        