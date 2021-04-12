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
import shutil

import numpy
import root_numpy



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

        folder_fit_name = "prefit"
        if self._kind == 'p' :
          folder_fit_name = "prefit"  
        elif  self._kind == 'P' :
          folder_fit_name = "postfit" 
     
        cuts = []
        folders = []
        
        keys = fileIn.GetListOfKeys()
     
        for key in keys:
          #print (" key = ", key)
          obj = key.ReadObj()
          #print " --> " , obj.IsA().GetName()
          if (obj.IsA().GetName() == "TDirectoryFile") :
            if ("_" + folder_fit_name) in obj.GetName():
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

        #
        # get the different histograms in the proper folders and add them if they have the same name
        # namely, if it is the same process
        #
        histos = {}
        
        for folder in folders:
          keys = folder.GetListOfKeys()
          for key in keys:
            obj = key.ReadObj()
            if (obj.IsA().GetName() != "TProfile"
                 and 
                 obj.InheritsFrom("TH1")
               ) :
              if obj.GetName() != "data_obs" and obj.GetName() != "TotalBkg" and obj.GetName() != "TotalProcs" and obj.GetName() != "TotalSig":
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

        total_MC_gr = ROOT.TGraphAsymmErrors(total_MC.GetNbinsX())
       
        for iBin in range(0, total_MC.GetNbinsX()) : 
          total_MC_gr.SetPoint     (iBin, total_MC.GetBinCenter(iBin+1), total_MC.GetBinContent(iBin+1))
          
          low_variation =  total_MC.GetBinContent(iBin+1) -  (total_MC_Errors.GetBinContent(iBin+1) - total_MC_Errors.GetBinError(iBin+1))
          up_variation  =  (total_MC_Errors.GetBinContent(iBin+1) + total_MC_Errors.GetBinError(iBin+1))  -   total_MC.GetBinContent(iBin+1)          
          #print " " , total_MC.GetBinContent(iBin+1), "   " , total_MC_Errors.GetBinContent(iBin+1) , "   ",  total_MC_Errors.GetBinError(iBin+1)
          total_MC_gr.SetPointError(iBin, 0, 0, low_variation, up_variation)
          
          total_MC.SetBinError(iBin+1, total_MC_Errors.GetBinError(iBin+1))
       

        #
        # If this is not a fitted variable ("self._nonFitVariable == True"), we need to add the MC stat uncertainty 
        # as got from the prefit histograms.
        # We should have given this code the list of root files from the different datacards
        # that have been combined to have the final variable *to plot* (not to fit!), namely "self._listOfFilesOriginal"
        #
        if self._nonFitVariable :
   
          # The variable "self._plotFile" is needed because I need the list of 
          # histograms to be added. E.g. if different signals are included, 
          # only the ones that I would plot I want to hadd, to then propagate the MC stat uncertainty
          
          groupPlot = OrderedDict()
          plot = {}
          legend = {}
          if os.path.exists(self._plotFile) :
            handle = open(self._plotFile,'r')
            exec(handle)
            handle.close()
   
   
          ROOT.TH1.SetDefaultSumw2(True)
          hStackTotal = ROOT.THStack("total",'')
          
          for fileInMkShape in self._listOfFilesOriginal:
              inputFile = ROOT.TFile.Open(fileInMkShape,  "READ")
              for sampleName, plotdef in plot.iteritems():
                if sampleName != 'DATA' :    # 'DATA' should not be added/stacked!
                  try:
                    histo = inputFile.Get("histo_" + sampleName)
                    hStackTotal.Add(histo)
                  except:
                    print "missing histo: histo_" + sampleName
          
          
          #Final histogram -> get MC errors
          histo_sum = hStackTotal.GetStack().Last()
          err_up = numpy.sqrt(numpy.array(histo_sum.GetSumw2())[1:-1]) # GetSumw2 -> array of sum squares of weights
          err_do = numpy.sqrt(numpy.array(histo_sum.GetSumw2())[1:-1]) # GetSumw2 -> array of sum squares of weights
          
          nominal = root_numpy.hist2array(histo_sum, copy=False)
          
          # err_rel_up = err_up / nom 
          # err_rel_do = err_do / nom 
          # print err_rel_up, err_rel_do

          for iBin in range(1, histo_sum.GetNbinsX()+1):
        
              old_err = total_MC.GetBinError(iBin)
              new_err = math.sqrt( old_err*old_err + err_up[iBin-1]*err_up[iBin-1] )
              total_MC.SetBinError(iBin, new_err)              
              total_MC_gr.SetPointError(iBin-1, 0.,0., -new_err, new_err)


 
        #
        # now save
        #

        for histoName, histo in histos.iteritems():
          histo.SetName("histo_" + histo.GetName())
        total_data.SetName ("histo_DATA")
        total_MC_gr.SetName ("gr_total")

        self._outFile.cd ( self._cutName + "/" + self._variable )
        total_MC_gr.Write()
        total_MC.Write()
        total_data.Write()
        for histoName, histo in histos.iteritems():
          histo.Write()
          
        
        
        #
        # Do I really need to define myself a cut for cuts.py with the "combined" ?
        # And the simplified variables.py with only the combined variable?
        # Yes: doing it now (it will easy your life) 
        # 
        
        
        # start creating the variables file 
        path = "variables_combined.py"
        variables_file = open( path ,"w")


        #
        #  e.g.
        #
        #  variables['mll']  = {   'name': 'mll',
        #                          'range' : (20, 12,200),
        #                          'xaxis' : 'm_{ll} [GeV]',
        #                          'fold' : 0
        #                          }

        variables_file.write("variables['%s'] = {  \n" % self._variable)
        variables_file.write("           'name' : '%s'   ,\n" % self._variable)
        variables_file.write("           'range' : (%d, %-.4f, %-.4f)   ,\n" % (total_MC.GetNbinsX(), total_MC.GetBinLowEdge(1), total_MC.GetBinLowEdge(total_MC.GetNbinsX()+1)) )
        variables_file.write("           'xaxis' : '%s'   ,\n" % self._variable)
        variables_file.write("           'fold' : 3    \n")
        variables_file.write("           }             \n")
  
        variables_file.write("\n")
        variables_file.close()


        # ... and now creating the cuts file 
        path = "cuts_combined.py"
        cuts_file = open( path ,"w")

        #
        #  e.g.
        #
        #  supercut = '1'
        #  cuts['ww2l2v_13TeV'] = ' mll > 10 '
        #
        #
        
        cuts_file.write("cuts['%s'] = '1' \n" % self._cutName)
 
        cuts_file.write("\n")
        cuts_file.close()

  
        #
        # Now it creates a combined configuration.py file
        # 
        
        path = "configuration_combined.py"
        configuration_file = open( path ,"w")

        #
        #  e.g.
        #
        #  supercut = '1'
        #  cuts['ww2l2v_13TeV'] = ' mll > 10 '
        #
        #
        
        configuration_file.write("tag = 'combined'  \n")
        configuration_file.write("outputDir = './'  \n")
        configuration_file.write("variablesFile = 'variables_combined.py'  \n")
        configuration_file.write("cutsFile = 'cuts_combined.py'  \n")
        #configuration_file.write("samplesFile = 'samples_combined.py'  \n")
        configuration_file.write("plotFile = 'plot_combined.py'   \n")
        #configuration_file.write("lumi = %-.4f \n"  % self._lumi)
        configuration_file.write("outputDirPlots = 'plot_'+tag   \n")
        configuration_file.write("structureFile = 'structure_combined.py'   \n")
        #configuration_file.write("nuisancesFile = 'nuisances.py'  \n")
        configuration_file.write("\n")
        configuration_file.close()

  
  

  
        #
        # Now copy the structureFile to have it at hand and be able to modify it
        # 
        if self._structureFile != None :
          shutil.copyfile(self._structureFile, 'structure_combined.py')

        #
        # Now copy the structureFile to have it at hand and be able to modify it
        # 
        if self._plotFile != None :
          shutil.copyfile(self._plotFile, 'plot_combined.py')
          #
          # One thing you may want to update, maybe automatically
          # 
          # legend['lumi'] = 'L = 35.9/fb'
          #
 
          plot_file = open(  'plot_combined.py' ,"a+")
          plot_file.write("legend['lumi'] = 'L = %s'  \n" % self._lumiText)
          plot_file.write("\n")
          plot_file.close()

  
  
        
        
    # _____________________________________________________________________________
    def _AddHistos(self, histos, nameHisto): 

        list_histo = [histo for histoName, histo in histos.iteritems()]
        new_histo = list_histo[0].Clone(nameHisto)
        
        for i in range(len(list_histo)-1) :
          new_histo.Add (list_histo[i+1])
               
        return new_histo




def foo_callback(option, opt, value, parser):
  setattr(parser.values, option.dest, value.split(','))
       


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
    parser.add_option('--kind'                  , dest='kind'                  , help='which kind of pre/post-fit distribution: p = prefit, P = postfit'  , default='P')
    parser.add_option('--cutName'               , dest='cutName'               , help='cut name as will appear in cuts.py'  , default='combined')
    parser.add_option('--variable'              , dest='variable'              , help='variable name'  , default='mll')
    parser.add_option('--structureFile'         , dest='structureFile'         , help='file with datacard configurations'          , default=None )
    parser.add_option('--lumiText'              , dest='lumiText'              , help='text for luminosity to be shown in legend'  , default="100/fb")
    parser.add_option('--nonFitVariable'        , dest='nonFitVariable'        , help='Is this a variable not used in the fit? (default False = it is the variable fitted)', action='store_true', default=False)
    parser.add_option('--listOfFilesOriginal'   , dest='listOfFilesOriginal'   , help='list of files with the original histograms, from which to extract the MC stat' , default='one.root,two.root', type='string', action='callback', callback=foo_callback) # these are the histograms as defined in the root files of the single datacards
       
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
    print " kind                  =          ", opt.kind
    print " cutName               =          ", opt.cutName
    print " structureFile         =          ", opt.structureFile
    print " plotFile              =          ", opt.plotFile
    print " lumiText              =          ", opt.lumiText
    print " nonFitVariable        =          ", opt.nonFitVariable
    if opt.nonFitVariable :
      print " listOfFilesOriginal   =    ", opt.listOfFilesOriginal
  



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
    factory._outputFileName      = opt.outputFile
    factory._variable            = opt.variable
    factory._kind                = opt.kind    
    factory._cutName             = opt.cutName
    factory._structureFile       = opt.structureFile
    factory._plotFile            = opt.plotFile
    factory._lumiText            = opt.lumiText
    factory._nonFitVariable      = opt.nonFitVariable
    factory._listOfFilesOriginal = opt.listOfFilesOriginal
 
 
    factory.makePostFitCombinedPlot()
    
    print '... and now closing ...'
        
       
       
       
