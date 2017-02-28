#!/usr/bin/env python

import json
import sys
import ROOT
import optparse
import LatinoAnalysis.Gardener.hwwtools as hwwtools
import logging
import os.path


# Common Tools & batch
from LatinoAnalysis.Tools.commonTools import *





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
    def makeDatacards( self, inputFile, outputDirDatacard, variables, cuts, samples, structureFile, nuisances):
    
        print "======================="
        print "==== makeDatacards ===="
        print "======================="
        
        self._variables = variables
        self._samples   = samples
        self._cuts      = cuts

        self._outputDirDatacard = outputDirDatacard

        self._fileIn = ROOT.TFile(inputFile, "READ")
        
        # divide the list of samples among signal, background and data
        for sampleName, sample in self._samples.iteritems():
          if structureFile[sampleName]['isSignal'] == 1 :
            self.signals.append(sampleName)
          if structureFile[sampleName]['isData'] == 1 :
            self.data.append(sampleName)
          if structureFile[sampleName]['isSignal'] == 0 and structureFile[sampleName]['isData'] == 0:
            self.backgrounds.append(sampleName)
          
        if not os.path.isdir (self._outputDirDatacard + "/") :
          os.mkdir (self._outputDirDatacard + "/")

        # loop over cuts  
        for cutName in self._cuts :
          print "cut = ", cutName, " :: ", cuts[cutName]
          os.system ("rm -rf " + self._outputDirDatacard + "/" + cutName) 
          os.mkdir (self._outputDirDatacard + "/" + cutName)
          # loop over variables
          for variableName, variable in self._variables.iteritems():
            print "  variableName = ", variableName
            tagNameToAppearInDatacard = cutName
            # e.g.    hww2l2v_13TeV_of0j
            #         to be defined in cuts.py

            os.mkdir (self._outputDirDatacard + "/" + cutName + "/" + variableName) 
            os.mkdir (self._outputDirDatacard + "/" + cutName + "/" + variableName + "/shapes/") # and the folder for the root files 

            self._outFile = ROOT.TFile.Open( self._outputDirDatacard + "/" + cutName + "/" + variableName + "/shapes/histos_" + tagNameToAppearInDatacard + ".root", 'recreate')
            ROOT.TH1.SetDefaultSumw2(True)
        
            # prepare yields
            yieldsSig  = {}
            yieldsBkg  = {}
            yieldsData = {}
            
            
            for sampleName in self.signals:
              shapeName = cutName+"/"+variableName+'/histo_' + sampleName
              histo = self._fileIn.Get(shapeName)
              # get the integral == rate from histogram
              yieldsSig[sampleName] = histo.Integral()
              self._outFile.cd()
              histo.Write()
              
            for sampleName in self.backgrounds:
              shapeName = cutName+"/"+variableName+'/histo_' + sampleName
              histo = self._fileIn.Get(shapeName)
              # get the integral == rate from histogram
              #print " shapeName = ", shapeName
              yieldsBkg[sampleName] = histo.Integral()
              self._outFile.cd()
              histo.Write()
            
            for sampleName in self.data:
              shapeName = cutName+"/"+variableName+'/histo_' + sampleName
              histo = self._fileIn.Get(shapeName)
              # get the integral == rate from histogram
              yieldsData['data'] = histo.Integral() # data is data!
              histo.SetName("histo_Data")
              self._outFile.cd()
              histo.Write()
                                     
        
            # start creating the datacard 
            cardPath = self._outputDirDatacard + "/" + cutName + "/" + variableName  + "/datacard.txt"
            print 'Writing to ' + cardPath 
            card = open( cardPath ,"w")
            card.write('## Shape input card\n')
        
            card.write('imax 1 number of channels\n')
            card.write('jmax * number of background\n')
            card.write('kmax * number of nuisance parameters\n') 

            card.write('-'*100+'\n')
            card.write('bin         %s' % tagNameToAppearInDatacard+'\n')
            if len(self.data) == 0:
              self._logger.warning( 'no data, no fun! ')
              #raise RuntimeError('No Data found!')
              yieldsData['data'] = 0

            card.write('observation %.0f\n' % yieldsData['data'])
            
            card.write('shapes  *           * '+
                       'shapes/histos_' + tagNameToAppearInDatacard + ".root" +
                       '     histo_$PROCESS histo_$PROCESS_$SYSTEMATIC' + '\n')
            
            card.write('shapes  data_obs           * '+
                       'shapes/histos_' + tagNameToAppearInDatacard + ".root" +
                       '     histo_Data' + '\n')
            
            #   shapes  *           * shapes/hww-19.36fb.mH125.of_vh2j_shape_mll.root     histo_$PROCESS histo_$PROCESS_$SYSTEMATIC
            #   shapes  data_obs    * shapes/hww-19.36fb.mH125.of_vh2j_shape_mll.root     histo_Data

            
            totalNumberSamples = len(self.signals) + len(self.backgrounds)
            columndef = 30

            # adapt column length to long bin names            
            if len(tagNameToAppearInDatacard) >= (columndef - 5) :
              columndef = len(tagNameToAppearInDatacard) + 7
            
            #print " columndef = ", columndef
            #print " len(tagNameToAppearInDatacard)  = ", len(tagNameToAppearInDatacard) 
            #print " tagNameToAppearInDatacard  = ", tagNameToAppearInDatacard
            
            
            card.write('bin'.ljust(80) + ''.join( [tagNameToAppearInDatacard.ljust(columndef) * totalNumberSamples])+'\n')
            #card.write('bin'.ljust(80) + ''.join( [tagNameToAppearInDatacard.ljust(columndef) for iterator in range(totalNumberSamples) ])+'\n')
            
            card.write('process'.ljust(80))
            card.write(''.join([name.ljust(columndef) for name in self.signals]))
            card.write(''.join([name.ljust(columndef) for name in self.backgrounds]))
            card.write('\n')

            card.write('process'.ljust(80))
            card.write(''.join([('%d' % -iSample   ).ljust(columndef) for iSample in range(len(self.signals))     ]))
            card.write(''.join([('%d' % (iSample+1)).ljust(columndef) for iSample in range(len(self.backgrounds)) ]))
            card.write('\n')

            card.write('rate'.ljust(80))
            card.write(''.join([('%-.4f' % yieldsSig[name]).ljust(columndef) for name in self.signals    ]))
            card.write(''.join([('%-.4f' % yieldsBkg[name]).ljust(columndef) for name in self.backgrounds]))
            card.write('\n')
            
            #bin                                       of_vh2j      of_vh2j    
            #process                                      ggH         ggWW    
            #process                                        0            1    
            #rate                                      1.1234       2.3456

            card.write('-'*100+'\n')

            # add nuisances
            
            # first the lnN nuisances
            for nuisanceName, nuisance in nuisances.iteritems():
              
              # check if a nuisance can be skipped because not in this particular cut
              use_this_nuisance = False
              if  'cuts' in nuisance.keys() :
                for Cuts_where_to_use_nuisance  in   nuisance['cuts'] :
                  if Cuts_where_to_use_nuisance == cutName :
                    # use this niusance
                    use_this_nuisance = True
              else :
                # default is use the nuisance everywhere
                use_this_nuisance = True 
              
              if use_this_nuisance :
               
                if nuisanceName != 'stat' : # 'stat' has a separate treatment, it's the MC/data statistics
                  
                  if 'type' in nuisance.keys() : # some nuisances may not have "type" ... why?
                    #print "nuisance[type] = ", nuisance ['type']
                    if nuisance ['type'] == 'lnN' or nuisance ['type'] == 'lnU' :
                      card.write((nuisance['name']).ljust(80-20))
                      card.write((nuisance ['type']).ljust(20))
                      if 'all' in nuisance.keys() and nuisance ['all'] == 1 : # for all samples
                        #card.write(''.join([('%-.4f' % nuisance['value']).ljust(columndef) for name in self.signals      ]))
                        #card.write(''.join([('%-.4f' % nuisance['value']).ljust(columndef) for name in self.backgrounds  ]))
                        card.write(''.join([(' %s ' % nuisance['value']).ljust(columndef) for name in self.signals      ]))
                        card.write(''.join([(' %s ' % nuisance['value']).ljust(columndef) for name in self.backgrounds  ]))
                        card.write('\n')
                      else :
                        # apply only to selected samples
                        for sampleName in self.signals:
                          if sampleName in nuisance['samples'].keys() :
                            #card.write(('%-.4f' % nuisance['samples'][sampleName]).ljust(columndef))
                            card.write(('%s' % nuisance['samples'][sampleName]).ljust(columndef))
                          else :
                            card.write(('-').ljust(columndef))
                        for sampleName in self.backgrounds:
                          if sampleName in nuisance['samples'].keys() :
                            #card.write(('%-.4f' % nuisance['samples'][sampleName]).ljust(columndef))
                            card.write(('%s' % nuisance['samples'][sampleName]).ljust(columndef))
                          else :
                            card.write(('-').ljust(columndef))
                             
                    elif nuisance ['type'] == 'shape' :
                      card.write(("CMS_" + (nuisance['name'])).ljust(80-20))
                      card.write((nuisance ['type']).ljust(20))
                      if 'all' in nuisance.keys() and nuisance ['all'] == 1 : # for all samples
                        card.write(''.join([('1.000').ljust(columndef) for name in self.signals      ]))
                        card.write(''.join([('1.000').ljust(columndef) for name in self.backgrounds  ]))
                        card.write('\n')
                      else :
                        # apply only to selected samples
                        for sampleName in self.signals:
                          if sampleName in nuisance['samples'].keys() :
                            card.write(('1.000').ljust(columndef))                          
                            # save the nuisance histograms in the root file
                            self._saveHisto(cutName+"/"+variableName+'/',
                                             'histo_' + sampleName + '_' + (nuisance['name']) + "Up",
                                             'histo_' + sampleName + '_CMS_' + (nuisance['name']) + "Up"
                                             )
                            self._saveHisto(cutName+"/"+variableName+'/',
                                             'histo_' + sampleName + '_' + (nuisance['name']) + "Down",
                                             'histo_' + sampleName + '_CMS_' + (nuisance['name']) + "Down"
                                             )
                          else :
                            card.write(('-').ljust(columndef))
                        for sampleName in self.backgrounds:
                          if sampleName in nuisance['samples'].keys() :
                            card.write(('1.000').ljust(columndef))
                            # save the nuisance histograms in the root file
                            self._saveHisto(cutName+"/"+variableName+'/',
                                             'histo_' + sampleName + '_' + (nuisance['name']) + "Up",
                                             'histo_' + sampleName + '_CMS_' + (nuisance['name']) + "Up"
                                             )
                            self._saveHisto(cutName+"/"+variableName+'/',
                                             'histo_' + sampleName + '_' + (nuisance['name']) + "Down",
                                             'histo_' + sampleName + '_CMS_' + (nuisance['name']) + "Down"
                                             )
                          else :
                            card.write(('-').ljust(columndef))
                    
                  # new line at the end of any nuisance that is *not* stat ... because in that case it's already done on its own
                  card.write('\n')
                 
                  
                # stat nuisances  
                if nuisanceName == 'stat' : # 'stat' has a separate treatment, it's the MC/data statistics
                
                  for sampleName in self.signals:
                    if sampleName in nuisance['samples'].keys() :
                      if nuisance['samples'][sampleName]['typeStat'] == 'uni' : # unified approach
                       
                        card.write(( 'CMS_' + tagNameToAppearInDatacard + "_" + sampleName + "_stat" ).ljust(80-20))
                        card.write((nuisance ['type']).ljust(20))
                
                        # write line in datacard
                        for sampleNameIterator2 in self.signals:
                          if sampleNameIterator2 == sampleName :
                            card.write(('1.000').ljust(columndef))
                          else :
                            card.write(('-').ljust(columndef))
                
                        for sampleNameIterator2 in self.backgrounds:
                          card.write(('-').ljust(columndef))
                
                        card.write('\n')
                
                        # save the nuisance histograms in the root file
                        self._saveHisto(cutName+"/"+variableName+'/',
                                         'histo_' + sampleName + '_stat' + "Up",
                                         'histo_' + sampleName + '_CMS_' + tagNameToAppearInDatacard + "_" + sampleName + "_stat" + "Up"
                                         )
                        self._saveHisto(cutName+"/"+variableName+'/',
                                         'histo_' + sampleName + '_stat' + "Down",
                                         'histo_' + sampleName + '_CMS_' + tagNameToAppearInDatacard + "_" + sampleName + "_stat" + "Down"
                                         )
                
                      if nuisance['samples'][sampleName]['typeStat'] == 'bbb' : # bin-by-bin
                       
                         #print "      sampleName = ", sampleName 
                         histoTemplate = self._fileIn.Get(cutName+'/'+variableName+'/histo_' + sampleName)
                         #print "      type = ", type( histoTemplate )
                
                         for iBin in range(1, histoTemplate.GetNbinsX()+1):
                       
                           card.write(( 'CMS_' + tagNameToAppearInDatacard + "_" + sampleName + "_ibin_" + str(iBin) + "_stat" ).ljust(100-20))
                           card.write((nuisance ['type']).ljust(20))
                
                           # write line in datacard
                           for sampleNameIterator2 in self.signals:
                             if sampleNameIterator2 == sampleName :
                               card.write(('1.000').ljust(columndef))
                             else :
                               card.write(('-').ljust(columndef))
                
                           for sampleNameIterator2 in self.backgrounds:
                             card.write(('-').ljust(columndef))
                
                           card.write('\n')
                
                           # save the nuisance histograms in the root file
                           self._saveHisto(cutName+"/"+variableName+'/',
                                            'histo_' + sampleName + '_ibin_' + str(iBin) + '_statUp',
                                            'histo_' + sampleName + '_CMS_' + tagNameToAppearInDatacard + "_" + sampleName + '_ibin_' + str(iBin) + '_stat' + "Up"
                                            )
                           self._saveHisto(cutName+"/"+variableName+'/',
                                            'histo_' + sampleName + '_ibin_' + str(iBin) + '_statDown',
                                            'histo_' + sampleName + '_CMS_' + tagNameToAppearInDatacard + "_" + sampleName + '_ibin_' + str(iBin) + '_stat' + "Down"
                                            )
                
                  for sampleName in self.backgrounds:
                    if sampleName in nuisance['samples'].keys() :
                      if nuisance['samples'][sampleName]['typeStat'] == 'uni' : # unified approach
                       
                        card.write(( 'CMS_' + tagNameToAppearInDatacard + "_" + sampleName + "_stat" ).ljust(80-20))
                        card.write((nuisance ['type']).ljust(20))
                
                        # write line in datacard
                        for sampleNameIterator2 in self.signals:
                          card.write(('-').ljust(columndef))
                
                        for sampleNameIterator2 in self.backgrounds:
                          if sampleNameIterator2 == sampleName :
                            card.write(('1.000').ljust(columndef))
                          else :
                            card.write(('-').ljust(columndef))
                
                        card.write('\n')
                
                        # save the nuisance histograms in the root file
                        self._saveHisto(cutName+"/"+variableName+'/',
                                         'histo_' + sampleName + '_stat' + "Up",
                                         'histo_' + sampleName + '_CMS_' + tagNameToAppearInDatacard + "_" + sampleName + "_stat" + "Up"
                                         )
                        self._saveHisto(cutName+"/"+variableName+'/',
                                         'histo_' + sampleName + '_stat' + "Down",
                                         'histo_' + sampleName + '_CMS_' + tagNameToAppearInDatacard + "_" + sampleName + "_stat" + "Down"
                                         )
                
                      if nuisance['samples'][sampleName]['typeStat'] == 'bbb' : # bin-by-bin
                
                         histoTemplate = self._fileIn.Get(cutName+'/'+variableName+'/histo_' + sampleName)
                         #print "type = ", type( histoTemplate )
                
                
                         for iBin in range(1, histoTemplate.GetNbinsX()+1):
                       
                           card.write(( 'CMS_' + tagNameToAppearInDatacard + "_" + sampleName + "_ibin_" + str(iBin) + "_stat" ).ljust(80-20))
                           card.write((nuisance ['type']).ljust(20))
                
                           # write line in datacard
                           for sampleNameIterator2 in self.signals:
                             card.write(('-').ljust(columndef))
                
                           for sampleNameIterator2 in self.backgrounds:
                             if sampleNameIterator2 == sampleName :
                               card.write(('1.000').ljust(columndef))
                             else :
                               card.write(('-').ljust(columndef))
                
                           card.write('\n')
                
                           # save the nuisance histograms in the root file
                           self._saveHisto(cutName+"/"+variableName+'/',
                                            'histo_' + sampleName + '_ibin_' + str(iBin) + '_statUp',
                                            'histo_' + sampleName + '_CMS_' + tagNameToAppearInDatacard + "_" + sampleName + '_ibin_' + str(iBin) + '_stat' + "Up"
                                            )
                           self._saveHisto(cutName+"/"+variableName+'/',
                                            'histo_' + sampleName + '_ibin_' + str(iBin) + '_statDown',
                                            'histo_' + sampleName + '_CMS_' + tagNameToAppearInDatacard + "_" + sampleName + '_ibin_' + str(iBin) + '_stat' + "Down"
                                            )
                
                
                # now add the "rateParam" for the normalization
                #  e.g.:            z_norm rateParam  htsearch zll 1 
                # see: https://twiki.cern.ch/twiki/bin/view/CMS/HiggsWG/SWGuideNonStandardCombineUses#Rate_Parameters
                if nuisanceName != 'stat' : # 'stat' has a separate treatment, it's the MC/data statistics
                  if 'type' in nuisance.keys() : # some nuisances may not have "type" ... why?
                    #print "nuisance[type] = ", nuisance ['type']
                    # 'rateParam' has a separate treatment -> it's just a line at the end of the datacard. It defines "free floating" samples
                    # I do it here and not before because I want the freee floating parameters at the end of the datacard
                    if nuisance ['type'] == 'rateParam' :
                      card.write((nuisance['name']).ljust(80-20))
                      card.write((nuisance ['type']).ljust(20))
                      card.write((tagNameToAppearInDatacard).ljust(columndef))   # the bin
                      # apply only to selected samples
                      for sampleName in self.signals:
                          if sampleName in nuisance['samples'].keys() :
                            card.write((sampleName).ljust(20))
                            card.write(('%-.4f' % float(nuisance['samples'][sampleName])).ljust(columndef))
                      for sampleName in self.backgrounds:
                          if sampleName in nuisance['samples'].keys() :
                            card.write((sampleName).ljust(20))
                            card.write(('%-.4f' % float(nuisance['samples'][sampleName])).ljust(columndef))
                      card.write('\n')

               
            # now add other nuisances            
            # Are there other kind of nuisances I forgot?
            
            card.write('-'*100+'\n')

            card.write('\n')
            card.close()






   
    # _____________________________________________________________________________
    def _saveHisto(self, folderName, histoName, histoNameOut):     
       shapeName = folderName + histoName
       histo = self._fileIn.Get(shapeName)
       print " shapeName = ", shapeName
       print " --> ", histoNameOut
       print " --> histo = ", histo
       histo.SetName(histoNameOut)
       self._outFile.cd()
       histo.Write()
       













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
    parser.add_option('--nuisancesFile'      , dest='nuisancesFile'     , help='file with nuisances configurations'         , default=None )
    parser.add_option('--cardList'            , dest="cardList"           , help="List of cuts to produce datacards"          , default=[], type='string' , action='callback' , callback=list_maker('cardList',','))

          
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
    
    # ~~~~
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
    if len(opt.cardList)>0:
      cut2del = []
      for iCut in cuts:
        if not iCut in opt.cardList : cut2del.append(iCut)
      for iCut in cut2del : del cuts[iCut]   
 
    samples = {}
    if os.path.exists(opt.samplesFile) :
      handle = open(opt.samplesFile,'r')
      exec(handle)
      handle.close()
   
    # ~~~~
    structure = {}
    if opt.structureFile == None :
       print " Please provide the datacard structure "
       exit ()
       
    if os.path.exists(opt.structureFile) :
      handle = open(opt.structureFile,'r')
      exec(handle)
      handle.close()


    # ~~~~
    nuisances = {}
    if opt.nuisancesFile == None :
       print " Please provide the nuisances structure if you want to add nuisances "
       
    if os.path.exists(opt.nuisancesFile) :
      handle = open(opt.nuisancesFile,'r')
      exec(handle)
      handle.close()
    
    
    factory.makeDatacards( opt.inputFile ,opt.outputDirDatacard, variables, cuts, samples, structure, nuisances)
    
        
        
