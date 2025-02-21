#!/usr/bin/env python

### 
### 
###       ____|       |  |        |    |                                                                                                                                                                                                                       
###       |     _ \   |  |   _ \  __|  __|   _ \                                                                                                                                                                                                               
###       __|  (   |  |  |   __/  |    |    (   |                                                                                                                                                                                                              
###      _|   \___/  _| _| \___| \__| \__| \___/   
### 
### 
###        |                           |                                                            |    |     _)                           _|                                           |     _)                   |                                      |    
###        __ \    _ \ \ \  \   /      __|   _ \        __|  _ \  __ `__ \    _ \ \ \   /  _ \      __|  __ \   |  __ \    _` |   __|      |     _ \    __|       __|   _ \   __ `__ \   __ \   |  __ \    _ \      __|   _ \      \ \  \   /  _ \    __|  |  / 
###        | | |  (   | \ \  \ /       |    (   |      |     __/  |   |   |  (   | \ \ /   __/      |    | | |  |  |   |  (   | \__ \      __|  (   |  |         (     (   |  |   |   |  |   |  |  |   |   __/      |    (   |      \ \  \ /  (   |  |       <  
###       _| |_| \___/   \_/\_/       \__| \___/      _|   \___| _|  _|  _| \___/   \_/  \___|     \__| _| |_| _| _|  _| \__, | ____/     _|   \___/  _|        \___| \___/  _|  _|  _| _.__/  _| _|  _| \___|     \__| \___/        \_/\_/  \___/  _|    _|\_\ 
###                                                                                                                      |___/                                                                                                                                  
###      
###                                                                                                                                                            
###    
###    
###   


import json
import sys
import ROOT
import optparse
import LatinoAnalysis.Gardener.hwwtools as hwwtools
import logging
import os.path


# Common Tools & batch
from LatinoAnalysis.Tools.commonTools import *



# ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ----


class FollettoFactory:
    _logger = logging.getLogger('FollettoFactory')

    # _____________________________________________________________________________
    def __init__(self):
      
        nuisances = {}
        self._nuisances = nuisances

        variables = {}
        self._variables = variables

        variables = {}
        self._variables = variables

        cuts = {}
        self._cuts = cuts

        samples = {}
        self._samples = samples

    def mkFolletto (self, outputDirDatacard, variables, cuts, samples, nuisances) :

        self._nuisances = nuisances
        self._variables = variables
        self._samples   = samples
        self._cuts      = cuts

        self._outputDirDatacard = outputDirDatacard

 
        # loop over cuts  
        for cutName in self._cuts :
          print "cut = ", cutName #, " :: ", cuts[cutName]
  
          # loop over variables
          for variableName, variable in self._variables.iteritems():
            print "variable = ", variableName  #, " :: ", variable

            tagNameToAppearInDatacard = cutName
            
            # copy the default root file for bookkeeping
            old_root_file_name = self._outputDirDatacard + "/" + cutName + "/" + variableName + "/shapes/" + "old_unpruned_histos_" + tagNameToAppearInDatacard + ".root"
            new_root_file_name = self._outputDirDatacard + "/" + cutName + "/" + variableName + "/shapes/" + "histos_"     + tagNameToAppearInDatacard + ".root"
            print " old_unpruned_root_file_name = ", old_root_file_name
            print " new_root_file_name = ", new_root_file_name
            
            os.system ("cp " + new_root_file_name + "   " + old_root_file_name ) 
           
            rootFile    = ROOT.TFile.Open( old_root_file_name, "READ")
            rootFileNew = ROOT.TFile.Open( new_root_file_name, "RECREATE")

            # get the histograms
            histograms = {}
            for k in rootFile.GetListOfKeys():
              h = k.ReadObj()
              # only 1d histograms supported
              histoName = h.GetName()
              match = re.search("histo_", histoName)
              if not match:
                continue
              histograms[h.GetName()] = h
      
                    
            # loop over samples
            for sampleName, sample in self._samples.iteritems():
 
              # loop over nuisances
              for nuisanceName, nuisance in nuisances.iteritems():

                if 'name' in nuisance.keys() :
                  nameTempUp   = 'histo_' + str(sampleName) + '_CMS_' + (nuisance['name']) + 'Up'
                  nameTempDown = 'histo_' + str(sampleName) + '_CMS_' + (nuisance['name']) + 'Down'
                  nameTemp     = 'histo_' + str(sampleName)
                
                  #print " nameTempUp = ", nameTempUp
                  
                  if nameTempUp in histograms.keys() and  nameTempDown in histograms.keys() : 
                    
                    
                    histo_nominal = histograms[nameTemp] 
                    histo_up   = histograms[nameTempUp] 
                    histo_down = histograms[nameTempDown] 
                    
                    if 'AsLnN' in nuisance and float(nuisance['AsLnN']) >= 1.:
                      print ">>>>>", nuisance['name'], " was derived as a shape uncertainty but is being treated as a lnN, thus root file to be renamed not to be used"
                      histo_up.  SetName('backup_nameTempUp'  + nameTempUp)
                      histo_down.SetName('backup_nameTempDown'+ nameTempDown)

                    histo_up.Write()
                    histo_down.Write()
                
              # save all the histograms with different structure,
              # as the bbb histograms and the stats
              
              for histoName, histo in histograms.iteritems() :
                match = re.search("_stat", histoName)
                if match:
                  h.Write()
              
              # finally save the nominals
              if sampleName != "DATA" :
                nameTemp     = "histo_" + str(sampleName)
                histo_nominal = histograms[nameTemp] 
                histo_nominal.Write()
              else :
                nameTemp     = "histo_Data"
                histo_nominal = histograms[nameTemp] 
                histo_nominal.Write()
                
                
 


######################################


if __name__ == '__main__':
   print '''
--------------------------------------------------------------------------------------------------

       ____|       |  |        |    |                                                                                                                                                                                                                       
       |     _ \   |  |   _ \  __|  __|   _ \                                                                                                                                                                                                               
       __|  (   |  |  |   __/  |    |    (   |                                                                                                                                                                                                              
      _|   \___/  _| _| \___| \__| \__| \___/   

--------------------------------------------------------------------------------------------------
'''

   usage = 'usage: %prog [options]'
   parser = optparse.OptionParser(usage)

   parser.add_option('--outputDirDatacard'  ,              dest='outputDirDatacard' ,           help='output directory'                           , default='./')
   parser.add_option('--nuisancesFile'      ,              dest='nuisancesFile'     ,           help='file with nuisances configurations'         , default=None )

   # read default parsing options as well
   hwwtools.addOptions(parser)
   hwwtools.loadOptDefaults(parser)
   (opt, args) = parser.parse_args()

   print "opt.pycfg               = ", opt.pycfg
   print "opt.outputDirDatacard   = ", opt.outputDirDatacard
   print "opt.nuisancesFile       = ", opt.nuisancesFile
   print "opt.cardList            = ", opt.cardList



   factory = ChainSawFactory()
 
   # ~~~~
   samples = {}
   if os.path.exists(opt.samplesFile) :
     handle = open(opt.samplesFile,'r')
     exec(handle)
     handle.close()

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
     
   nuisances = {}
   if opt.nuisancesFile == None :
      print " Please provide the nuisances structure if you want to add nuisances "
      
   if os.path.exists(opt.nuisancesFile) :
     handle = open(opt.nuisancesFile,'r')
     exec(handle)
     handle.close()
     
   
   factory.mkFolletto( opt.outputDirDatacard, variables, cuts, samples, nuisances)

