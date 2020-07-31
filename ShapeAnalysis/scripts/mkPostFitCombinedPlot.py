#!/usr/bin/env python

import json
import sys
from sys import exit
argv = sys.argv
sys.argv = argv[:1]
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



# ----------------------------------------------------- LawnMower --------------------------------------

class LawnMower:
    _logger = logging.getLogger('EdgeTrimmer')
 
    # _____________________________________________________________________________
    def __init__(self):

        variables = {}
        self._variables = variables

        
 
    # _____________________________________________________________________________
    def makePostFitCombinedPlot(self):

        print "================================="
        print "==== makePostFitCombinedPlot ===="
        print "================================="
 
        print "                                                                                       "
        print "     ____|      |                  __ __|     _)                                       "
        print "     __|     _` |   _` |   _ \        |   __|  |  __ `__ \   __ `__ \    _ \   __|     "
        print "     |      (   |  (   |   __/        |  |     |  |   |   |  |   |   |   __/  |        "
        print "    _____| \__,_| \__, | \___|       _| _|    _| _|  _|  _| _|  _|  _| \___| _|        "
        print "                  |___/                                                                "    
        print "                                                                                       "
        

        #
        # Create a new "bin", phase space, that is the combination of all the phase spaces.
        # This code will create a new cuts.py with its definitio
        # as well as the root file with the histograms 
        # and the TGraphAsymmetricErrors that is given to mkPlot.py
        # to add the correct uncertainty band
        #
        #            
        #        PostFitShapesFromWorkspace  \
        #              -w combined12.root  \
        #              -d combined12.txt \
        #              -o output_histograms.root \
        #              --postfit --sampling \
        #              -f fitDiagnosticsCombined/fitDiagnostics.root:fit_s  \
        #              --total-shapes
        #        
        #  Inputs needed: 
        #
        #    - output_histograms.root
        #          -> histo data (data_obs)
        #          -> histograms for each sample in each phase space ---> need to add them up
        #                    - from the list of histograms, extract the list of samples/names
        #                      excluding the "totalXX" and the data
        #          -> final histogram with uncertainty ---> transform into a TGraphAsymmetricErrors and use the previous histogram as central value
        #    
        #    - output file
        #    - varible name 
        #
        
        print " self.inputFilePostFitShapesFromWorkspace " , self._inputFilePostFitShapesFromWorkspace
        
        
        fileIn = ROOT.TFile(self._inputFilePostFitShapesFromWorkspace, "READ")

        #
        # find list of cuts that have been combined 
        #
     
        cuts = []
        folders = []
        
        keys = fileIn.GetListOfKeys()
     
        for key in keys:
          #print (" key = ", key)
          obj = key.ReadObj()
          #print " --> " , obj.IsA().GetName()
          if (obj.IsA().GetName() == "TDirectoryFile") :
            if "_prefit" in obj.GetName():
              #print "obj.GetName() = " , obj.GetName() 
              cuts.append (obj.GetName()[:-7])   # length of "_prefit" = 7
              folders.append(obj)
              
        print " cuts = ", cuts
        
        #
        # prepare output file
        #
        
        #self._outFile = ROOT.TFile.Open( self._outputFileName, 'update')  # need to append in an existing file if more cuts/variables are wanted
        self._outFile = ROOT.TFile.Open( self._outputFileName, 'recreate')  # need to append in an existing file if more cuts/variables are wanted

        self._outFile.mkdir ( self._cutName )
        self._outFile.mkdir ( self._cutName + "/" + self._variable)

        self._outFile.cd ( self._cutName + "/" + self._variable )

        folder_fit_name = "prefit"
        if self._kind == 'p' :
          folder_fit_name = "prefit"  
        elif  self._kind == 'P' :
          folder_fit_name = "postfit" 
        

        #
        # get the different histograms in the proper folders and add them if they have the same name
        # namely, if it is the same process
        #
        histos = {}
        
        for folder in folders:
          keys = folder.GetListOfKeys()
          for key in keys:
            obj = key.ReadObj()
            print " obj ----> " , obj
            print "           " , obj.IsA().GetName()
            print "           " , obj.InheritsFrom("TH1")
            if (obj.IsA().GetName() != "TProfile"
                 and 
                 obj.InheritsFrom("TH1")
               ) :
              print " it's an histogram "
        
              if obj.GetName() != "data_obs" and obj.GetName() != "TotalBkg" and obj.GetName() != "TotalProcs" and obj.GetName() != "TotalSig":
                print " SOMETHING "
                if (obj.GetName() in histos.keys()) :
                  histos[obj.GetName()].Add(obj)
                else :
                  histos[obj.GetName()] = obj
           
        print " histos selected = ", histos
        
        total_MC = self._AddHistos(histos, "histo_total")
        
        
        
        #
        # Now get the histogram from which I extract the 68% error band
        # And since I am already looping, let's copy also the combined data histogram
        #
        
        keys = fileIn.GetListOfKeys()
        
        for key in keys:
          obj = key.ReadObj()
          if (obj.IsA().GetName() == "TDirectoryFile") :
            if obj.GetName() == folder_fit_name:    # either "prefit" or "postfit"
              keys_histo = obj.GetListOfKeys()
              for key_histo in keys_histo:
                obj_histo = key_histo.ReadObj()
              
                if (obj_histo.IsA().GetName() != "TProfile"
                     and 
                     obj_histo.InheritsFrom("TH1")
                   ) :
                  
                  if obj_histo.GetName() == "TotalProcs":
                    total_MC_Errors = obj_histo
                  if obj_histo.GetName() == "data_obs":
                    total_data = obj_histo

        #
        # And prepare the TGraphAsymmErrors for total predicted distribution
        #

        total_MC_gr = ROOT.TGraphAsymmErrors(total_MC_gr.GetNbinsX())
       
        for iBin in range(0, total_MC_gr.GetNbinsX()) : 
          total_MC_gr.SetPoint     (iBin, total_MC.GetBinCenter(iBin+1), total_MC.GetBinContent(iBin+1))
          
          low_variation =  total_MC.GetBinContent(iBin+1) -  (total_MC_Errors.GetBinContent(iBin+1) - total_MC_Errors.GetBinError(iBin+1))
          up_variation  =  (total_MC_Errors.GetBinContent(iBin+1) + total_MC_Errors.GetBinError(iBin+1))  -   total_MC.GetBinContent(iBin+1)
          
          total_MC_gr.SetPointError(iBin, 0, 0, low_variation, up_variation)
        
       
        #
        # now save
        #
        self._outFile.cd ( self._cutName + "/" + self._variable )
        total_MC_gr.Write()
        total_data.Write()
        for histoName, histo in histos.iteritems():
          histo.Write()
          
        
        
        
        #template_histogram = 0
        
        #for sampleName, structureDef in self._structure.iteritems():
           #if '/' in sampleName:
             #cardName = sampleName.replace('/', '__')
             #binName = sampleName[sampleName.find('/') + 1:]
             #shapeSource = 'binned/' + binName + '/' + self._cutNameInOriginal + "/" + self._variable
             #sampleName = sampleName[:sampleName.find('/')]
           #else:
             #cardName = sampleName
             #shapeSource = self._cutNameInOriginal+"/"+self._variable
           
           #in_samples = False
           #if sampleName in self._samples: in_samples = True
           
           #if not in_samples:
             ## check if it is in subsamples
             #in_subsample = False
             #for _sampleName, _sample in self._samples.items():
               #if "subsamples" not in _sample: continue
               #for _subsam in  _sample["subsamples"].keys():
                 #if _sampleName+"_"+ _subsam == sampleName:
                   #in_subsample = True
                   #break
             #if not in_subsample: continue
           
           #if 'removeFromCuts' in structureDef and self._cutNameInOriginal in structureDef['removeFromCuts']:
             #continue
           
           
           ## 
           ## propagate signal from pre-fit if triggered
           ## NB: this is needed for exclusion analyses, where the fitted signal is 0
           ##     or to show the signal in the background only fit 
           ##
           #if (self._getSignalFromPrefit == 1 and structureDef['isSignal'] == 1 ) or sampleName == "DATA" :
             
             #print "THISFILE:",self._inputFile
             #fileInJustForDATA = ROOT.TFile(self._inputFile, "READ")

             #self._outFile.cd (self._cutNameInOriginal+"/"+self._variable)

             #print shapeSource + "/histo_" + sampleName
             #histo = fileInJustForDATA.Get(shapeSource + "/histo_" + sampleName)
             #print histo
             #print 'histo_' + cardName
             #histo.SetName  ('histo_' + cardName)
             #histo.SetTitle ('histo_' + cardName)
             #histo.Write()              
             
             #template_histogram = histo.Clone ("template")


        ##print " template_histogram = " , template_histogram
         
        #for sampleName, structureDef in self._structure.iteritems():
           #if '/' in sampleName:
             #cardName = sampleName.replace('/', '__')
             #binName = sampleName[sampleName.find('/') + 1:]
             #shapeSource = 'binned/' + binName + '/' + self._cutNameInOriginal + "/" + self._variable
             #sampleName = sampleName[:sampleName.find('/')]
           #else:
             #cardName = sampleName
             #shapeSource = self._cutNameInOriginal+"/"+self._variable

           #in_samples = False
           #if sampleName in self._samples: in_samples = True
         
           #if not in_samples:
            ## check if it is in subsamples
            #in_subsample = False
            #for _sampleName, _sample in self._samples.items():
               #if "subsamples" not in _sample: continue
               #for _subsam in  _sample["subsamples"].keys():
                  #if _sampleName+"_"+ _subsam == sampleName:
                     #in_subsample = True
                     #break
            #if not in_subsample: continue

           #if 'removeFromCuts' in structureDef and self._cutNameInOriginal in structureDef['removeFromCuts']:
             #continue

           #print " sampleName = ", sampleName
           
           #copied_from_original = False
           
           ##if samples_key != "DATA" :
           #if not ((self._getSignalFromPrefit == 1 and structureDef['isSignal'] == 1 ) or sampleName == "DATA"):
             #if not (fileIn.Get(folder_fit_name + "/" + self._cut).GetListOfKeys().Contains(cardName) ):
               #print "Sample ", cardName, " does not exist in ", fileIn
               ##
               ## If for some reason this histogram is not available in the combine output
               ## get the histogram from the input root file, the output of mkShape
               ## and scale that to 0, so that it is propagated to be used by mkPlot
               ## but it will have 0 contribution, as expected (but legends and all the rest will be ok and nice)
               ##
               ## continue
               ##
               #fileInJustForDATA = ROOT.TFile(self._inputFile, "READ")

               #self._outFile.cd(self._cutNameInOriginal+"/"+self._variable)

               #histo = fileInJustForDATA.Get(shapeSource + "/histo_" + sampleName)
               #histo.SetName  ('histo_' + cardName)
               #histo.SetTitle ('histo_' + cardName)
               #histo.Write()  
               
               #copied_from_original = True

             ##
             ##
             ##
             #if not copied_from_original :  
               
               #histo = fileIn.Get(folder_fit_name + "/" + self._cut + "/" + cardName)
               #print folder_fit_name + "/" + self._cut + "/" + cardName
               
               #histo.SetName  ('histo_' + cardName)
               #histo.SetTitle ('histo_' + cardName)
               
               ## fix the binning copying from "DATA" binning, if available
               #if (template_histogram != 0) :
                 #histo = self._ChangeBin(histo, template_histogram)
               
               #histo.Write()              


        ##
        ## total signal and total background, and total
        ##
        
        ##
        ## total signal
        #histo_total_signal = fileIn.Get(folder_fit_name + "/" + self._cut + "/" + "total_signal")      

        #if histo_total_signal:
          #histo_total_signal.SetName  ('histo_' + 'total_signal')
          #histo_total_signal.SetTitle ('histo_' + 'total_signal')
          
          ## fix the binning copying from "DATA" binning, if available
          #if (template_histogram != 0) :
            #histo_total_signal = self._ChangeBin(histo_total_signal, template_histogram)
          
          #histo_total_signal.Write()              

        ##
        ## total background
        #histo_total_background = fileIn.Get(folder_fit_name + "/" + self._cut + "/" + "total_background")      
        #histo_total_background.SetName  ('histo_' + 'total_background')
        #histo_total_background.SetTitle ('histo_' + 'total_background')
        
        #histo_total_background_prefit  = fileIn.Get("shapes_prefit/" + self._cut + "/" + "total_background")      
        #histo_total_background_prefit.SetName  ('histo_total_background_prefit')
        #histo_total_background_prefit.SetTitle ('histo_total_background_prefit')

        #histo_total_background_postfit_s = fileIn.Get("shapes_fit_s/" + self._cut + "/" + "total_background")      
        #histo_total_background_postfit_s.SetName  ('histo_total_background_postfit_s')
        #histo_total_background_postfit_s.SetTitle ('histo_total_background_postfit_s')

        #histo_total_background_postfit_b = fileIn.Get("shapes_fit_s/" + self._cut + "/" + "total_background")      
        #histo_total_background_postfit_b.SetName  ('histo_total_background_postfit_b')
        #histo_total_background_postfit_b.SetTitle ('histo_total_background_postfit_b')

        ## fix the binning copying from "DATA" binning, if available
        #if (template_histogram != 0) :
          #histo_total_background = self._ChangeBin(histo_total_background, template_histogram)
          #histo_total_background_prefit = self._ChangeBin(histo_total_background_prefit, template_histogram)
          #histo_total_background_postfit_s = self._ChangeBin(histo_total_background_postfit_s, template_histogram)
          #histo_total_background_postfit_b = self._ChangeBin(histo_total_background_postfit_b, template_histogram)
        
        #histo_total_background.Write()              
        #histo_total_background_prefit.Write()              
        #histo_total_background_postfit_s.Write()              
        #histo_total_background_postfit_b.Write()              
        
        ##
        ## total
        #histo_total = fileIn.Get(folder_fit_name + "/" + self._cut + "/" + "total")      
        
        #histo_total.SetName  ('histo_' + 'total')
        #histo_total.SetTitle ('histo_' + 'total')
        
        #histo_total_prefit  = fileIn.Get("shapes_prefit/" + self._cut + "/" + "total")      
        #histo_total_prefit.SetName  ('histo_total_prefit')
        #histo_total_prefit.SetTitle ('histo_total_prefit')

        #histo_total_postfit_s = fileIn.Get("shapes_fit_s/" + self._cut + "/" + "total")      
        #histo_total_postfit_s.SetName  ('histo_total_postfit_s')
        #histo_total_postfit_s.SetTitle ('histo_total_postfit_s')

        #histo_total_postfit_b = fileIn.Get("shapes_fit_s/" + self._cut + "/" + "total")      
        #histo_total_postfit_b.SetName  ('histo_total_postfit_b')
        #histo_total_postfit_b.SetTitle ('histo_total_postfit_b')

        ## fix the binning copying from "DATA" binning, if available
        #if (template_histogram != 0) :
          #histo_total = self._ChangeBin(histo_total, template_histogram)
          #histo_total_prefit = self._ChangeBin(histo_total_prefit, template_histogram)
          #histo_total_postfit_s = self._ChangeBin(histo_total_postfit_s, template_histogram)
          #histo_total_postfit_b = self._ChangeBin(histo_total_postfit_b, template_histogram)
        
        #histo_total.Write()              
        #histo_total_prefit.Write()      
        #histo_total_postfit_s.Write()        
        #histo_total_postfit_b.Write()

    ## _____________________________________________________________________________
    #def _ChangeBin(self, myhisto, templatehisto): 

        #nx = templatehisto.GetNbinsX()
        
        #binLowEdge = []

        #for iBin in range(1, nx+1):
          #binLowEdge.append(templatehisto.GetXaxis().GetBinLowEdge(iBin))
        #binLowEdge.append(templatehisto.GetXaxis().GetBinLowEdge(nx+1))
        ##print " binLowEdge = ", binLowEdge

        #new_histo = ROOT.TH1F("temporary","",nx,array('d',binLowEdge))
          
        #for iBin in range(1, nx+1):
          #new_histo.SetBinContent(iBin, myhisto.GetBinContent(iBin))
          #new_histo.SetBinError  (iBin, myhisto.GetBinError(iBin))
          
        #new_histo.SetName  (myhisto.GetName())
        #new_histo.SetTitle (myhisto.GetTitle())
        
        #return new_histo
        
    # _____________________________________________________________________________
    def _AddHistos(self, histos, nameHisto): 

        print "histos = ", histos
        
        iterator = iter(histos.values())
        templatehisto = next(iterator)
        
        nx = templatehisto.GetNbinsX()
        
        binLowEdge = []

        for iBin in range(1, nx+1):
          binLowEdge.append(templatehisto.GetXaxis().GetBinLowEdge(iBin))
        binLowEdge.append(templatehisto.GetXaxis().GetBinLowEdge(nx+1))

        new_histo = ROOT.TH1F(nameHisto,nameHisto,nx,array('d',binLowEdge))

        for histoName, histo in histos.iteritems():
          new_histo.Add (histo)
          
        return new_histo
        




        


if __name__ == '__main__':
    sys.argv = argv
    
    print '''
----------------------------------------------------------------------------------------------------------------------------------


   _ \               |        ____| _)  |         _ \   |         |               ___|                    |     _)                   | 
  |   |  _ \    __|  __|      |      |  __|      |   |  |   _ \   __|   __|      |       _ \   __ `__ \   __ \   |  __ \    _ \   _` | 
  ___/  (   | \__ \  |        __|    |  |        ___/   |  (   |  |   \__ \      |      (   |  |   |   |  |   |  |  |   |   __/  (   | 
 _|    \___/  ____/ \__|     _|     _| \__|     _|     _| \___/  \__| ____/     \____| \___/  _|  _|  _| _.__/  _| _|  _| \___| \__,_| 
                                                                                                                                       
                                                                                                                                       
----------------------------------------------------------------------------------------------------------------------------------
'''    
    usage = 'usage: %prog [options]'
    parser = optparse.OptionParser(usage)

    parser.add_option('--inputFilePostFitShapesFromWorkspace'      , dest='inputFilePostFitShapesFromWorkspace'      , help='input file with roofit results, mlfit'                          , default='input.root')
    parser.add_option('--outputFile'            , dest='outputFile'            , help='output file with histograms, same format as mkShape.py output'  , default='output.root')
    parser.add_option('--inputFile'             , dest='inputFile'             , help='input file with histograms (only to get the DATA distribution)' , default='input.root')
    parser.add_option('--kind'                  , dest='kind'                  , help='which kind of pre/post-fit distribution: p = prefit, P = postfit'  , default='P')
    parser.add_option('--cutName'               , dest='cutName'               , help='cut name as will appear in cuts.py'  , default='combined')
    parser.add_option('--variable'              , dest='variable'              , help='variable name'  , default='mll')
    #parser.add_option('--cut'                   , dest='cut'                   , help='cut name'  , default='0j')
    #parser.add_option('--cutNameInOriginal'     , dest='cutNameInOriginal'     , help='cut name as appears in cuts.py'  , default='')
    #parser.add_option('--structureFile'         , dest='structureFile'         , help='file with datacard configurations'          , default=None )
    #parser.add_option('--getSignalFromPrefit'   , dest='getSignalFromPrefit'   , help='get the signal shape and normalization from pre-fit. Needed for exclusion analyses. Set to 1 to trigger this.', default=0   ,    type=int)
          
          
    # read default parsing options as well
    hwwtools.addOptions(parser)
    hwwtools.loadOptDefaults(parser)
    (opt, args) = parser.parse_args()

    sys.argv.append( '-b' )
    ROOT.gROOT.SetBatch()

    print " configuration file    =          ", opt.pycfg
    print " inputFilePostFitShapesFromWorkspace      =          ", opt.inputFilePostFitShapesFromWorkspace
    print " outputFile            =          ", opt.outputFile
    print " variable              =          ", opt.variable
    #print " cut                   =          ", opt.cut
    print " kind                  =          ", opt.kind
    #print " getSignalFromPrefit   =          ", opt.getSignalFromPrefit
    #print " structureFile         =          ", opt.structureFile
    #print " inputFile (for DATA)  =          ", opt.inputFile
    print " cutName               =          ", opt.cutName


    #if opt.cutNameInOriginal == '' :
      #opt.cutNameInOriginal = opt.cut
    #print " cutNameInOriginal     =          ", opt.cutNameInOriginal


    if not opt.debug:
        pass
    elif opt.debug == 2:
        print 'Logging level set to DEBUG (%d)' % opt.debug
        logging.basicConfig( level=logging.DEBUG )
    elif opt.debug == 1:
        print 'Logging level set to INFO (%d)' % opt.debug
        logging.basicConfig( level=logging.INFO )

    factory = LawnMower()
    factory._inputFilePostFitShapesFromWorkspace  = opt.inputFilePostFitShapesFromWorkspace
    factory._outputFileName    = opt.outputFile
    factory._variable          = opt.variable
    #factory._cut               = opt.cut
    #factory._cutNameInOriginal = opt.cutNameInOriginal
    factory._kind              = opt.kind
    
    factory._cutName           = opt.cutName
    
    #factory._getSignalFromPrefit = opt.getSignalFromPrefit
    

    # ~~~~
    #samples = OrderedDict()
    #if os.path.exists(opt.samplesFile) :
      #handle = open(opt.samplesFile,'r')
      #exec(handle)
      #handle.close()

    #factory._samples = samples

    # ~~~~
    #structure = {}
    #if opt.structureFile == None :
       #print " Please provide the datacard structure "
       ##exit ()

    #elif os.path.exists(opt.structureFile) :
      #handle = open(opt.structureFile,'r')
      #exec(handle)
      #handle.close()


    #factory._structure = structure
    
    #factory._inputFile = opt.inputFile
    
    factory.makePostFitCombinedPlot()
    
    print '... and now closing ...'
        
       
       
       
