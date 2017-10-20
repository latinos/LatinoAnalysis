#!/usr/bin/env python

###   
###       ___|  |            _)          ___|                                                                                                                  
###      |      __ \    _` |  |  __ \  \___ \    _` | \ \  \   /                                                                                               
###      |      | | |  (   |  |  |   |       |  (   |  \ \  \ /                                                                                                
###     \____| _| |_| \__,_| _| _|  _| _____/  \__,_|   \_/\_/                                                                                                 
###                                     |    |          |     _)                    _|                                _)                                       
###       __|  __ `__ \    _ \    _ \   __|  __ \       __ \   |  __ \    __|      |     _ \    __|      __ \   |   |  |   __|   _` |  __ \    __|   _ \   __| 
###     \__ \  |   |   |  (   |  (   |  |    | | |      |   |  |  |   | \__ \      __|  (   |  |         |   |  |   |  | \__ \  (   |  |   |  (      __/ \__ \ 
###     ____/ _|  _|  _| \___/  \___/  \__| _| |_|     _.__/  _| _|  _| ____/     _|   \___/  _|        _|  _| \__,_| _| ____/ \__,_| _|  _| \___| \___| ____/ 
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


class ChainSawFactory:
    _logger = logging.getLogger('ChainSawFactory')

    # _____________________________________________________________________________
    def __init__(self):
      
        variables = {}
        self._variables = variables

        cuts = {}
        self._cuts = cuts

        samples = {}
        self._samples = samples

    # _____________________________________________________________________________
    # a datacard for each "cut" and each "variable" will be produced, in separate sub-folders, names after "cut/variable"
    # _____________________________________________________________________________

    def mkChainSaw (self, outputDirDatacard, variables, cuts, samples, nuisances, threshold) :

        self._variables = variables
        self._samples   = samples
        self._cuts      = cuts

        self._outputDirDatacard = outputDirDatacard

 
        # loop over cuts  
        for cutName in self._cuts :
          print "cut = ", cutName, " :: ", cuts[cutName]
  
          # loop over variables
          for variableName, variable in self._variables.iteritems():
            print "variable = ", variableName, " :: ", variable

            tagNameToAppearInDatacard = cutName
            
            # copy the default root file for bookkeeping
            old_root_file_name = self._outputDirDatacard + "/" + cutName + "/" + variableName + "/shapes/" + "old_histos_" + tagNameToAppearInDatacard + ".root"
            new_root_file_name = self._outputDirDatacard + "/" + cutName + "/" + variableName + "/shapes/" + "histos_"     + tagNameToAppearInDatacard + ".root"
            print " old_root_file_name = ", old_root_file_name
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

                nameTempUp   = 'histo_' + str(sampleName) + '_CMS_' + (nuisance['name']) + 'Up'
                nameTempDown = 'histo_' + str(sampleName) + '_CMS_' + (nuisance['name']) + 'Down'
                nameTemp     = 'histo_' + str(sampleName)
              
                #print " nameTempUp = ", nameTempUp
                
                if nameTempUp in histograms.keys() and  nameTempDown in histograms.keys() : 
                   
                  histo_nominal = histograms[nameTemp] 
                  histo_up   = histograms[nameTempUp] 
                  histo_down = histograms[nameTempDown] 
                  
                  # maximum change in statistical uncertainty
                  max_change_stat_uncertainty = 0.4
                                  
                  for ibin in range( histo_nominal.GetNbinsX() ) :
                    nominal_uncertainty  = histo_nominal.GetBinError(ibin+1)
                    var_up_uncertainty   = histo_up.GetBinError(ibin+1)
                    var_down_uncertainty = histo_down.GetBinError(ibin+1)
                  
                    if (nominal_uncertainty != 0) and ( abs((var_up_uncertainty / nominal_uncertainty)-1) > max_change_stat_uncertainty ) :
                      #print " correct : ", histo_nominal.GetBinContent(ibin+1), " ---> var_up_uncertainty =", var_up_uncertainty, "  ; nominal_uncertainty = ", nominal_uncertainty, " => ", abs((var_up_uncertainty / nominal_uncertainty)-1),
                      #print "    ---> ", histo_up.GetBinContent(ibin+1),
                      histo_up.SetBinContent (ibin+1, histo_nominal.GetBinContent(ibin+1))
                      #print "    ---> ", histo_up.GetBinContent(ibin+1),
                      #print "    --> ", str(sampleName) , "   ",  (nuisance['name']),
                      #print " ibin = ", ibin
                      
       
                    if (nominal_uncertainty != 0) and ( abs((var_down_uncertainty / nominal_uncertainty)-1) > max_change_stat_uncertainty ) :
                      histo_down.SetBinContent (ibin+1, histo_nominal.GetBinContent(ibin+1))
                  
                  histo_up.Write()
                  histo_down.Write()
                  
              # finally save the nominals
              if sampleName != "DATA" :
                nameTemp     = "histo_" + str(sampleName)
                histo_nominal = histograms[nameTemp] 
                histo_nominal.Write()
              else :
                nameTemp     = "histo_Data"
                histo_nominal = histograms[nameTemp] 
                histo_nominal.Write()
                
                
 
 
    #nuisancesToPrune = {}
    #if os.path.exists(nameFileConfiguration):
      #handle = open(nameFileConfiguration,'r')
      #exec(handle)
      #handle.close()

    #print "nuisancesToPrune = ", nuisancesToPrune

    ## remove duplicates in "sampleName"
    ## used in scaling histograms in case of "matching"
    ## and in case the same sample name is used in several "bin"
    ## NB: the order is not preserved, but who cares!
    #reducedsampleName = list(set(sampleName))

    # modify sample rate in root file!

    #for rootFileBin in rootFiles:
      #print "rootFile[", rootFileBin, "] = ",rootFiles[rootFileBin]
      ## check if root file is present (the name must end with .root)
      #matchfile = re.search(".root", rootFiles[rootFileBin])
      #if not matchfile:
       #continue
      #rootFile = ROOT.TFile.Open(str(thepath)+"/"+str(rootFiles[rootFileBin]))

      ## copy the default root file for bookkeeping
      #old_root_file_name = str(thepath)+"/"+"old_"+str(rootFiles[rootFileBin])
      #new_root_file_name = str(thepath)+"/"+str(rootFiles[rootFileBin])
      #print " old_root_file_name = ", old_root_file_name
      #print " new_root_file_name = ", new_root_file_name
      
      #os.system ("cp " + new_root_file_name + "   " + old_root_file_name ) 
     
      #rootFile    = ROOT.TFile.Open( old_root_file_name, "READ")
      #rootFileNew = ROOT.TFile.Open( new_root_file_name, "RECREATE")
      
      ## get the histograms
      #histograms = {}
      #for k in rootFile.GetListOfKeys():
        #h = k.ReadObj()
        ## only 1d histograms supported
        #histoName = h.GetName()
        #match = re.search("histo_", histoName)
        #if not match:
          #continue
        #histograms[h.GetName()] = h
      ##print " histograms = ", histograms

      #nuisance_to_be_removed = []
      #nuisance_to_be_removed_sample_dependent = {}
      #for nuisance in systematicsName :
        #for  hr_list_nuisances_to_test, nuisance_to_test in nuisancesToPrune.iteritems() :
          ##print " hr_list_nuisances_to_test = ", hr_list_nuisances_to_test, " -> ", nuisance_to_test
          #matchNuisance = fnmatch.fnmatch(str(nuisance), nuisance_to_test)
          #if matchNuisance :
            ##print "matchNuisance[", nuisance_to_test, "] -> ", nuisance
            ## relative variation
            #nuisance_to_be_removed_samples = {}
            
            #for sample in reducedsampleName:
              #nameTempUp   = "histo_"+str(sample)+"_"+str(nuisance)+"Up"
              #nameTempDown = "histo_"+str(sample)+"_"+str(nuisance)+"Down"
              #nameTemp     = "histo_"+str(sample)
              
              #if nameTempUp in histograms.keys() and  nameTempDown in histograms.keys() : 
                 
                #histo_nominal = histograms[nameTemp] 
                #histo_up   = histograms[nameTempUp] 
                #histo_down = histograms[nameTempDown] 
                
                ## maximum change in statistical uncertainty
                #max_change_stat_uncertainty = 0.4
                                
                #for ibin in range( histo_nominal.GetNbinsX() ) :
                  #nominal_uncertainty  = histo_nominal.GetBinError(ibin+1)
                  #var_up_uncertainty   = histo_up.GetBinError(ibin+1)
                  #var_down_uncertainty = histo_down.GetBinError(ibin+1)
                
                  #if (nominal_uncertainty != 0) and ( abs((var_up_uncertainty / nominal_uncertainty)-1) > max_change_stat_uncertainty ) :
                    #histo_up.SetBinContent (ibin+1, histo_nominal.GetBinContent(ibin+1))

                  #if (nominal_uncertainty != 0) and ( abs((var_down_uncertainty / nominal_uncertainty)-1) > max_change_stat_uncertainty ) :
                    #histo_down.SetBinContent (ibin+1, histo_nominal.GetBinContent(ibin+1))
                
                #histo_up.Write()
                #histo_down.Write()
                
          #else :  
            #for sample in reducedsampleName:
              #nameTempUp   = "histo_"+str(sample)+"_"+str(nuisance)+"Up"
              #nameTempDown = "histo_"+str(sample)+"_"+str(nuisance)+"Down"
              
              #if nameTempUp in histograms.keys() and  nameTempDown in histograms.keys() : 
                 
                #histo_up   = histograms[nameTempUp] 
                #histo_down = histograms[nameTempDown] 

                #histo_up.Write()
                #histo_down.Write()

      ## finally save the nominals
      #for sample in reducedsampleName:
        #nameTemp     = "histo_"+str(sample)
        #histo_nominal = histograms[nameTemp] 
        #histo_nominal.Write()



######################################


if __name__ == '__main__':
   print '''
--------------------------------------------------------------------------------------------------

            ___|  |            _)          ___|                            
           |      __ \    _` |  |  __ \  \___ \    _` | \ \  \   /         
           |      | | |  (   |  |  |   |       |  (   |  \ \  \ /          
          \____| _| |_| \__,_| _| _|  _| _____/  \__,_|   \_/\_/           

--------------------------------------------------------------------------------------------------
'''

   usage = 'usage: %prog [options]'
   parser = optparse.OptionParser(usage)

   parser.add_option("-i", "--inputConfiguration",         dest="nameFileConfiguration",        help="name configuration file with nuisances to remove", default='blabla.py')
   parser.add_option("-t", "--threshold",                  dest="threshold",                    help="threshold", default=0.15,  type='float')
   parser.add_option('--outputDirDatacard'  ,              dest='outputDirDatacard' ,           help='output directory'                           , default='./')
   parser.add_option('--nuisancesFile'      ,              dest='nuisancesFile'     ,           help='file with nuisances configurations'         , default=None )
   parser.add_option('--cardList'        ,                 dest="cardList" ,                    help="List of cuts to produce datacards"          , default=[], type='string' , action='callback' , callback=list_maker('cardList',','))

   # read default parsing options as well
   hwwtools.addOptions(parser)
   hwwtools.loadOptDefaults(parser)
   (opt, args) = parser.parse_args()

   print "opt.pycfg               = ", opt.pycfg
   print "opt.threshold           = ", opt.threshold
   print "opt.inputConfiguration  = ", opt.nameFileConfiguration
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
   
   if len(opt.cardList)>0:
     try:
       newCuts = []
       for iCut in opt.cardList:
         for iOptim in optim:
           newCuts.append(iCut+'_'+iOptim)
       opt.cardList = newCuts
       print opt.cardList
     except:
       print "No optim dictionary"
     cut2del = []
     for iCut in cuts:
       if not iCut in opt.cardList : cut2del.append(iCut)
     for iCut in cut2del : del cuts[iCut]   

  
   # ~~~~
   nuisances = {}
   if opt.nuisancesFile == None :
      print " Please provide the nuisances structure if you want to add nuisances "
      
   if os.path.exists(opt.nuisancesFile) :
     handle = open(opt.nuisancesFile,'r')
     exec(handle)
     handle.close()
   
   
   factory.mkChainSaw( opt.outputDirDatacard, variables, cuts, samples, nuisances, opt.threshold)
   
      