#!/usr/bin/env python

import json
import sys
from sys import exit
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
import numpy as np
import root_numpy as rnp


# ----------------------------------------------------- PlotFactory --------------------------------------

class PlotFactory:
    _logger = logging.getLogger('PlotFactory')
 
    # _____________________________________________________________________________
    def __init__(self):

        self._tag = ''

        variables = {}
        self._variables = variables

        cuts = {}
        self._cuts = cuts

        samples = OrderedDict()
        self._samples = samples

        self._plotsToWrite = ['c', 'cratio', 'cdifference']
        self._plotLinear = True
        self._plotLog = True

        outputDirPlots = {}
        self._outputDirPlots = outputDirPlots
        
        self._showIntegralLegend = 1
        # 0 is no

        self._FigNamePF = ''

        self._fileFormats = ['png', 'root']

    # _____________________________________________________________________________
    def makePlot(self, inputFile, outputDirPlots, variables, cuts, samples, plot, nuisances, legend, groupPlot):

        print "=================="
        print "==== makePlot ===="
        print "=================="
        
        self.defineStyle()
        
        self._variables = variables
        self._samples   = samples
        self._cuts      = cuts

        self._outputDirPlots = outputDirPlots
        os.system ("mkdir " + outputDirPlots + "/") 
        
        #
        # prepare plotter.html
        #
        text_file_html = open(self._outputDirPlots + "/" + "plotter.html", "w")

        text_file_html.write("<script type=\"text/javascript\" src=\"https://root.cern.ch/js/latest/scripts/JSRootCore.js?gui\"></script>\n")
        text_file_html.write("<div id=\"simpleGUI\" path=\"./\" files=\"\n")


        #tcanvas            = ROOT.TCanvas( "cc",      "cc"     , 800, 600 )
        #tcanvasRatio       = ROOT.TCanvas( "ccRatio", "ccRatio", 800, 800 )
        ## weight_X_tcanvas      = ROOT.TCanvas( "weight_X_tcanvas",      "weight_X_tcanvas",      800, 800 )
        #weight_X_tcanvasRatio = ROOT.TCanvas( "weight_X_tcanvasRatio", "weight_X_tcanvasRatio", 800, 800 )

        ROOT.TH1.SetDefaultSumw2(True)
        
        dataColor = 1

        #thsData       = ROOT.THStack ("thsData",      "thsData")
        #thsSignal     = ROOT.THStack ("thsSignal",    "thsSignal")
        #thsBackground = ROOT.THStack ("thsBackground","thsBackground")

        #thsSignal_grouped     = ROOT.THStack ("thsSignal_grouped",    "thsSignal_grouped")
        #thsBackground_grouped = ROOT.THStack ("thsBackground_grouped","thsBackground_grouped")

        ROOT.gROOT.cd()

        list_thsData       = {}
        list_thsSignal     = {}
        list_thsBackground = {}

        list_thsSignal_grouped     = {}
        list_thsBackground_grouped = {}
        list_thsSignal_grouped_normalized = {}
        list_thsBackground_grouped_normalized = {}

        list_tcanvas               = {}
        list_tcanvasRatio          = {}
        list_weight_X_tcanvasRatio = {}
        list_tcanvasDifference          = {}
        list_weight_X_tcanvasDifference = {}
        list_tcanvasSigVsBkg       = {}
        list_tcanvasSigVsBkgTHstack = {}

        generalCounter = 0

        if os.path.isdir(inputFile):
          # ONLY COMPATIBLE WITH OUTPUTS MERGED TO SAMPLE LEVEL!!
          fileIn = {}
          allFiles = os.listdir(inputFile)
          for sampleName in self._samples:
            fileIn[sampleName] = ROOT.TFile.Open(inputFile+'/plots_%s_ALL_%s.root' % (self._tag, sampleName))
            if not fileIn[sampleName]:
              raise RuntimeError('Input file for sample ' + sampleName + ' missing')
          if os.path.exists(inputFile+'/plots_total.root'):
            fileIn['total'] = ROOT.TFile.Open(inputFile+'/plots_total.root')
              
        else:
          fileIn = ROOT.TFile(inputFile, "READ")

        #---- save one TCanvas for every cut and every variable
        for cutName in self._cuts :
          print "cut =", cutName
          for variableName, variable in self._variables.iteritems():
            if 'cuts' in variable and cutName not in variable['cuts']:
              continue

            if type(fileIn) is not dict and not fileIn.GetDirectory(cutName+"/"+variableName):
              continue
              
            print "variableName =", variableName

            if not "divideByBinWidth" in variable.keys():
              variable["divideByBinWidth"] = 0
  
            tcanvas            = ROOT.TCanvas( "cc" + cutName + "_" + variableName,      "cc"     , 800, 600 )
            tcanvasRatio       = ROOT.TCanvas( "ccRatio" + cutName + "_" + variableName, "ccRatio", 800, 800 )
            weight_X_tcanvasRatio = ROOT.TCanvas( "weight_X_tcanvasRatio" + cutName + "_" + variableName, "weight_X_tcanvasRatio", 800, 800 )
            tcanvasDifference       = ROOT.TCanvas( "ccDifference" + cutName + "_" + variableName, "ccDifference", 800, 800 )
            weight_X_tcanvasDifference = ROOT.TCanvas( "weight_X_tcanvasDifference" + cutName + "_" + variableName, "weight_X_tcanvasDifference", 800, 800 )
            if self._plotNormalizedDistributions :
              tcanvasSigVsBkg    = ROOT.TCanvas( "ccSigVsBkg" + cutName + "_" + variableName,      "cc"     , 800, 600 )

            if self._plotNormalizedDistributionsTHstack :
              tcanvasSigVsBkgTHstack    = ROOT.TCanvas( "ccTHstackSigVsBkg" + cutName + "_" + variableName,      "cc"     , 800, 600 )
 
            list_tcanvas                 [generalCounter] = tcanvas
            list_tcanvasRatio            [generalCounter] = tcanvasRatio
            list_weight_X_tcanvasRatio   [generalCounter] = weight_X_tcanvasRatio
            list_tcanvasDifference            [generalCounter] = tcanvasDifference
            list_weight_X_tcanvasDifference   [generalCounter] = weight_X_tcanvasDifference
            if self._plotNormalizedDistributions :
              list_tcanvasSigVsBkg         [generalCounter] = tcanvasSigVsBkg
            if self._plotNormalizedDistributionsTHstack :
              list_tcanvasSigVsBkgTHstack         [generalCounter] = tcanvasSigVsBkgTHstack



            histos = {}
            histos_grouped = {}
            
            canvasNameTemplateRatio = 'ccRatio_' + cutName + "_" + variableName
            canvasNameTemplateDifference = 'ccDifference_' + cutName + "_" + variableName
            #tcanvasRatio       = ROOT.TCanvas( canvasNameTemplateRatio, variableName, 800, 800 )

            canvasNameTemplate = 'c_' + cutName + "_" + variableName
            #tcanvas = ROOT.TCanvas( canvasNameTemplate, variableName , 800, 600 )
            tcanvas.cd()
            
            #print " and now this ..."

            tgrData_vx     = array('f')
            tgrData_evx    = array('f')
            tgrData_vy     = array('f')
            tgrData_evy_up = array('f')
            tgrData_evy_do = array('f')

            # at least 1 "MC" should be around ... otherwise what are we plotting? Only data?
            tgrMC_vx       = array('f')
            tgrMC_evx      = array('f')

            #these vectors are needed for nuisances accounting
            nuisances_vy_up     = {}
            nuisances_vy_do     = {}
 
            ROOT.gROOT.cd()
 
            thsData       = ROOT.THStack ("thsData_" + cutName + "_" + variableName,      "thsData_" + cutName + "_" + variableName)
            #print 'really before thstack ... one'
            thsSignal     = ROOT.THStack ("thsSignal_" + cutName + "_" + variableName,    "thsSignal_" + cutName + "_" + variableName)
            #print 'really before thstack ... two'
            thsBackground = ROOT.THStack ("thsBackground_" + cutName + "_" + variableName,"thsBackground_" + cutName + "_" + variableName)
            #print 'really before thstack ... three'

            thsSignal_grouped     = ROOT.THStack ("thsSignal_grouped_" + cutName + "_" + variableName,    "thsSignal_grouped_" + cutName + "_" + variableName)
            #print 'really before thstack ... four'
            thsBackground_grouped = ROOT.THStack ("thsBackground_grouped_" + cutName + "_" + variableName,"thsBackground_grouped_" + cutName + "_" + variableName)

            list_thsData               [generalCounter] = thsData
            list_thsSignal             [generalCounter] = thsSignal
            list_thsBackground         [generalCounter] = thsBackground
            list_thsSignal_grouped     [generalCounter] = thsSignal_grouped
            list_thsBackground_grouped [generalCounter] = thsBackground_grouped

            # for special case of plotting normalized
            thsSignal_grouped_normalized     = ROOT.THStack ("thsSignal_grouped_normalized_" + cutName + "_" + variableName,    "thsSignal_grouped_normalized_" + cutName + "_" + variableName)
            thsBackground_grouped_normalized = ROOT.THStack ("thsBackground_grouped_normalized_" + cutName + "_" + variableName,"thsBackground_grouped_normalized_" + cutName + "_" + variableName)
            list_thsSignal_grouped_normalized     [generalCounter] = thsSignal_grouped_normalized
            list_thsBackground_grouped_normalized [generalCounter] = thsBackground_grouped_normalized


            generalCounter += 1
            
            #print '... after thstack ...'

            sigSupList    = []
            sigSupList_grouped    = []
            # list of additional histograms to be used in the ratio plot
            sigForAdditionalRatioList    = {}
            sigForAdditionalDifferenceList    = {}

            # enhanced list of nuisances, including bin-by-bin 
            mynuisances = {}

            nexpected = 0

            for sampleName, plotdef in plot.iteritems():
              if 'samples' in variable and sampleName not in variable['samples']:
                continue

              shapeName = cutName+"/"+variableName+'/histo_' + sampleName
              print '     -> shapeName = ', shapeName
              if type(fileIn) is dict:
                histo = fileIn[sampleName].Get(shapeName)
              else:
                histo = fileIn.Get(shapeName)
              print ' --> ', histo
              print 'new_histo_' + sampleName + '_' + cutName + '_' + variableName
              histos[sampleName] = histo.Clone('new_histo_' + sampleName + '_' + cutName + '_' + variableName)
              
              #print "     -> sampleName = ", sampleName, " --> ", histos[sampleName].GetTitle(), " --> ", histos[sampleName].GetName(), " --> ", histos[sampleName].GetNbinsX()
              #for iBinAmassiro in range(1, histos[sampleName].GetNbinsX()+1):
                 #print " i = ", iBinAmassiro, " [" , sampleName, " ==> ", histos[sampleName].GetBinContent(iBinAmassiro)

              # allow arbitrary scaling in MC (and DATA??), if needed
              # for example to "see" a signal
              if 'scale' in plotdef.keys() : 
                histos[sampleName].Scale(plotdef['scale'])
                #print " >> scale ", sampleName, " to ", plotdef['scale']

              # apply cut dependent scale factors
              # for example when plotting different phase spaces
              if 'cuts' in plotdef.keys() and cutName in plotdef['cuts']:
                histos[sampleName].Scale( float( plotdef['cuts'][cutName] ) )
     
              # data style
              if plotdef['isData'] == 1 :
                if variable['divideByBinWidth'] == 1:
                  histos[sampleName].Scale(1,"width")

                #print ' plot[', sampleName, '][color] = ' , plotdef['color']
                histos[sampleName].SetMarkerColor(plotdef['color'])

                histos[sampleName].SetMarkerSize(1)
                histos[sampleName].SetMarkerStyle(20)
                histos[sampleName].SetLineColor(self._getColor(plotdef['color']))
                
                # blind data
                if 'isBlind' in plotdef.keys() and plotdef['isBlind'] == 1:
                  histos[sampleName].Reset()

                # Per variable blinding
                if 'blind' in variable:
                  if cutName in variable['blind']:
                    blind_range = variable['blind'][cutName]
                    if blind_range == "full":
                      for iBin in range(1, histos[sampleName].GetNbinsX()+1):
                        histos[sampleName].SetBinContent(iBin, 0)
                        histos[sampleName].SetBinError  (iBin, 0)
                      histos[sampleName].Reset()
                    elif type(blind_range) in [list,tuple] and len(blind_range)==2:
                      b0 = histos[sampleName].FindBin(blind_range[0])
                      b1 = histos[sampleName].FindBin(blind_range[1])
                      for iBin in range(1, histos[sampleName].GetNbinsX()+1):
                        if iBin >= b0 and iBin <= b1:
                          histos[sampleName].SetBinContent(iBin, 0)
                          histos[sampleName].SetBinError  (iBin, 0)

                thsData.Add(histos[sampleName])

                # first time fill vectors X axis
                if len(tgrData_vx) == 0 :
                  dataColor = histos[sampleName].GetMarkerColor()
                  for iBin in range(1, histos[sampleName].GetNbinsX()+1):
                    tgrData_vx.append(  histos[sampleName].GetBinCenter (iBin))
                    tgrData_evx.append( histos[sampleName].GetBinWidth (iBin) / 2.)                  
                    tgrData_vy.append(  histos[sampleName].GetBinContent (iBin))
                    #print " plot[", sampleName, "].keys() = ", plotdef.keys()
                    if ('isSignal' not in plotdef.keys() or plotdef['isSignal'] != 3) and not ('isBlind' in plotdef.keys() and plotdef['isBlind'] == 1) :
                      if variable['divideByBinWidth'] == 1:
                        tgrData_evy_up.append( self.GetPoissError(histos[sampleName].GetBinContent (iBin) * histos[sampleName].GetBinWidth (iBin) , 0, 1) / histos[sampleName].GetBinWidth (iBin) )
                        tgrData_evy_do.append( self.GetPoissError(histos[sampleName].GetBinContent (iBin) * histos[sampleName].GetBinWidth (iBin) , 1, 0) / histos[sampleName].GetBinWidth (iBin) )
                      else:
                        tgrData_evy_up.append( self.GetPoissError(histos[sampleName].GetBinContent (iBin) , 0, 1) )
                        tgrData_evy_do.append( self.GetPoissError(histos[sampleName].GetBinContent (iBin) , 1, 0) )
                    else :
                      tgrData_evy_up.append( 0 )
                      tgrData_evy_do.append( 0 )
                      
                else :
                  for iBin in range(1, histos[sampleName].GetNbinsX()+1):
                    tgrData_vx[iBin-1] = (  histos[sampleName].GetBinCenter (iBin))
                    tgrData_evx.append( histos[sampleName].GetBinWidth (iBin) / 2.)                  
                    tgrData_vy[iBin-1] += histos[sampleName].GetBinContent (iBin)
                    if 'isSignal' not in plotdef.keys() or plotdef['isSignal'] == 3 :
                      if variable['divideByBinWidth'] == 1:
                        tgrData_evy_up[iBin-1] = SumQ ( tgrData_evy_up[iBin-1], self.GetPoissError(histos[sampleName].GetBinContent (iBin) * histos[sampleName].GetBinWidth (iBin) , 0, 1) / histos[sampleName].GetBinWidth (iBin))
                        tgrData_evy_do[iBin-1] = SumQ ( tgrData_evy_do[iBin-1], self.GetPoissError(histos[sampleName].GetBinContent (iBin) * histos[sampleName].GetBinWidth (iBin) , 1, 0) / histos[sampleName].GetBinWidth (iBin))
                      else:
                        tgrData_evy_up[iBin-1] = SumQ ( tgrData_evy_up[iBin-1], self.GetPoissError(histos[sampleName].GetBinContent (iBin) , 0, 1) )
                        tgrData_evy_do[iBin-1] = SumQ ( tgrData_evy_do[iBin-1], self.GetPoissError(histos[sampleName].GetBinContent (iBin) , 1, 0) )
                    
              # if plotdef['isData'] == 1:
              else:
                # MC style
                # only background "filled" histogram
                if plotdef['isSignal'] == 0:
                  #histos[sampleName].SetFillStyle(1001)
                  #histos[sampleName].SetFillColorAlpha(self._getColor(plotdef['color'],) 0.5)
                  #histos[sampleName].SetFillColor(self._getColor(plotdef['color']))
                  #histos[sampleName].SetLineColor(self._getColor(plotdef['color']+)1)
                  histos[sampleName].SetFillColor(self._getColor(plotdef['color']))
                  if 'fill' in plotdef:
                    histos[sampleName].SetFillStype(plotdef['fill'])
                  else:
                    histos[sampleName].SetFillStyle(3001)
                else :
                  histos[sampleName].SetFillStyle(0)
                  histos[sampleName].SetLineWidth(2)
             
                histos[sampleName].SetLineColor(self._getColor(plotdef['color']))
                # scale to luminosity if MC
                #histos[sampleName].Scale(self._lumi)  ---> NO! They are already scaled to luminosity in mkShape!
                
                if plotdef['isSignal'] == 1 :
                  if variable['divideByBinWidth'] == 1:
                    histos[sampleName].Scale(1,"width")

                  thsSignal.Add(histos[sampleName])

                elif plotdef['isSignal'] == 2 or plotdef['isSignal'] == 3 :
                  #print "SigSup histo: ", histos[sampleName]
                  if  variable['divideByBinWidth'] == 1:
                    histos[sampleName].Scale(1,"width")

                  sigSupList.append(histos[sampleName])

                  if plotdef['isSignal'] == 3 :
                    #print "sigForAdditionalRatio histo: ", histos[sampleName]
                    sigForAdditionalRatioList[sampleName] = histos[sampleName]
                    sigForAdditionalDifferenceList[sampleName] = histos[sampleName]
                else :
                  nexpected += histos[sampleName].Integral(1,histos[sampleName].GetNbinsX())   # it was (-1, -1) in the past, correct now
                  if variable['divideByBinWidth'] == 1:
                    histos[sampleName].Scale(1,"width")

                  thsBackground.Add(histos[sampleName])
                  #print " adding to background: ", sampleName

                # handle 'stat' nuisance to create the bin-by-bin list of nuisances
                # "massage" the list of nuisances accordingly
                for nuisanceName, nuisance in nuisances.iteritems():         
                  if 'cuts' in nuisance and cutName not in nuisance['cuts']:
                    continue
                  # run only if this nuisance will affect the phase space defined in "cut"

                  #print " nuisanceName = ", nuisanceName
                  if nuisanceName == 'stat' : # 'stat' has a separate treatment, it's the MC/data statistics
                    #print " nuisance = ", nuisance
                    if 'samples' in nuisance.keys():
                      if sampleName in nuisance['samples'].keys() :
                        #print " stat nuisances for ", sampleName
                        if nuisance['samples'][sampleName]['typeStat'] == 'uni' : # unified approach
                          print 'In principle nothing to be done here ... just wait'
                        if nuisance['samples'][sampleName]['typeStat'] == 'bbb' : # bin-by-bin
                          # add N ad hoc nuisances, one for each bin
                          for iBin in range(1, histos[sampleName].GetNbinsX()+1):
                            if ('ibin_' + str(iBin) + '_stat') not in mynuisances.keys() :   # if new, add the new nuisance
                              #  Name of the histogram:    histo_" + sampleName + "_ibin_" + str(iBin) + "_statUp"
                              #  Then the nuisance is "ibin_" + str(iBin) + "_stat"
                              mynuisances['ibin_' + str(iBin) + '_stat'] = {
                                'samples'  : {   sampleName : '1.00', },
                              }
                            else :  # otherwise just add the new sample in the list of samples to be considered
                              mynuisances['ibin_' + str(iBin) + '_stat']['samples'][sampleName] = '1.00'
                  else :
                    if nuisanceName not in mynuisances.keys() :
                      if 'type' in nuisance.keys() and (nuisance['type'] == 'rateParam' or nuisance['type'] == 'lnU') :
                        pass
                        #print "skip this nuisance since 100 percent uncertainty :: ", nuisanceName
                      else :
                        mynuisances[nuisanceName] = nuisances[nuisanceName]
                 
                nuisanceHistos = ({}, {})
                 
                for nuisanceName, nuisance in mynuisances.iteritems():
                  # is this nuisance to be considered for this background?
                  if 'samples' in nuisance:
                    if sampleName not in nuisance['samples']:
                      continue
                  elif 'all' not in nuisance or nuisance['all'] != 1:
                    continue

                  if 'cuts' in nuisance and cutName not in nuisance['cuts']:
                    continue

                  if 'name' in nuisance:
                    shapeNameVars = tuple(cutName+"/"+variableName+'/histo_' + sampleName+"_"+nuisance['name']+var for var in ['Up', 'Down'])
                  else:
                    shapeNameVars = tuple(cutName+"/"+variableName+'/histo_' + sampleName+"_"+nuisanceName+var for var in ['Up', 'Down'])

                  if 'type' in nuisance and nuisance['type'] == 'lnN':
                    if 'samples' in nuisance:
                      values = nuisance['samples'][sampleName]
                      # example:
                      #              'samples'  : {
                      #                   'WW' : '1.00',    
                      #                   'ggH': '1.23/0.97'
                      #                },                              
                    else: # 'all'
                      values = nuisance['value']

                    if '/' in values:
                      variations = map(float, values.split('/'))
                    else:
                      variations = (float(values), 2. - float(values))
                      
                    # don't use  histos[sampleName], or the second "scale" will fail!!!
                    for ivar, shapeNameVar in enumerate(shapeNameVars):
                      histoVar = histo.Clone(shapeNameVar.replace('/', '__'))
                      histoVar.Scale(variations[ivar])

                      nuisanceHistos[ivar][nuisanceName] = histoVar

                  else:
                    for ivar, shapeNameVar in enumerate(shapeNameVars):
                      if type(fileIn) is dict:
                        histoVar = fileIn[sampleName].Get(shapeNameVar)
                      else:
                        histoVar = fileIn.Get(shapeNameVar)
  
                      nuisanceHistos[ivar][nuisanceName] = histoVar

                for ivar, nuisances_vy in enumerate([nuisances_vy_up, nuisances_vy_do]):
                  for nuisanceName, nuisance in mynuisances.iteritems():
                    try:
                      histoVar = nuisanceHistos[ivar][nuisanceName]
                    except KeyError:
                      # now, even if not considered this nuisance, I need to add it, 
                      # so that in case is "empty" it will add the nominal value
                      # for this sample that is not affected by the nuisance
                      histoVar = histos[sampleName]
                    else:
                      if 'scale' in plotdef:
                        histoVar.Scale(plotdef['scale'])
                                   
                      # apply cut dependent scale factors
                      # for example when plotting different phase spaces
                      if 'cuts' in plotdef and cutName in plotdef['cuts']:
                        histoVar.Scale(float(plotdef['cuts'][cutName]))
    
                      if variable["divideByBinWidth"] == 1:
                        histoVar.Scale(1., "width")
                    
                    try:
                      vy = nuisances_vy[nuisanceName]
                    except KeyError:
                      vy = nuisances_vy[nuisanceName] = np.zeros_like(rnp.hist2array(histo, copy=False))

                    # get the background sum
                    if plotdef['isSignal'] == 0:   # ---> add the signal too????? See ~ 20 lines below
                      vy += rnp.hist2array(histoVar, copy=False)

              # create the group of histograms to plot
              # this has to be done after the scaling of the previous lines
              # andl also after all the rest, so that we inherit the style of the histograms
              for sampleNameGroup, sampleConfiguration in groupPlot.iteritems():
                if sampleName in sampleConfiguration['samples']:
                  if sampleNameGroup in histos_grouped.keys() :
                    histos_grouped[sampleNameGroup].Add(histos[sampleName])
                  else :
                    histos_grouped[sampleNameGroup] = histos[sampleName].Clone('new_histo_group_' + sampleNameGroup + '_' + cutName + '_' + variableName)

            # end sample loop

            # set the colors for the groups of samples
            for sampleNameGroup, sampleConfiguration in groupPlot.iteritems():
              if sampleNameGroup in histos_grouped.keys() :
                histos_grouped[sampleNameGroup].SetLineColor(self._getColor(sampleConfiguration['color']))
                if sampleConfiguration['isSignal'] == 0:
                  #histos_grouped[sampleNameGroup].SetFillStyle(1001)
                  #histos_grouped[sampleNameGroup].SetFillColorAlpha(self._getColor(sampleConfiguration['color'],) 0.5)
                  #histos_grouped[sampleNameGroup].SetFillColor(self._getColor(sampleConfiguration['color']))
                  #histos_grouped[sampleNameGroup].SetLineColor(self._getColor(sampleConfiguration['color']+)1)
                  histos_grouped[sampleNameGroup].SetFillColor(self._getColor(sampleConfiguration['color']))
                  if 'fill' in sampleConfiguration:
                    histos_grouped[sampleNameGroup].SetFillStyle(sampleConfiguration['fill'])
                  else:
                    histos_grouped[sampleNameGroup].SetFillStyle(3001)
                else :
                  histos_grouped[sampleNameGroup].SetFillStyle(0)
                  histos_grouped[sampleNameGroup].SetLineWidth(2)
            
            # fill the reference distribution with the background only distribution
            # save the central values of the bkg sum for use for the nuisance band 

            #
            # How could this be ==0 ?
            # At least one MC sample should be defined ... 
            # but still, let's leave the possibility 
            #            
            if thsBackground.GetNhists() != 0:
              last = thsBackground.GetStack().Last()
              tgrMC_vy = rnp.hist2array(last, copy=True)
              for iBin in range(1,thsBackground.GetStack().Last().GetNbinsX()+1):
                tgrMC_vx .append(thsBackground.GetStack().Last().GetBinCenter(iBin))
                tgrMC_evx.append(thsBackground.GetStack().Last().GetBinWidth(iBin) / 2.)
              nuisances_err2_up = rnp.array(last.GetSumw2())[1:-1]
              nuisances_err2_do = rnp.array(last.GetSumw2())[1:-1]
            else:
              tgrMC_vy = np.zeros((0,))
              nuisances_err2_up = np.zeros((0,))
              nuisances_err2_do = np.zeros((0,))
                        
            #
            # and now  let's add the signal on top of the background stack 
            # It is important to do this after setting (without signal) tgrMC_vy
            #
            for sampleName, plotdef in plot.iteritems():
              if 'samples' in variable and sampleName not in variable['samples']:
                continue

              # MC style
              if plotdef['isData'] == 0 :
                if plotdef['isSignal'] == 1 :
                  thsBackground.Add(histos[sampleName])

            #
            # you need to add the signal as well, since the signal was considered in the nuisances vector
            # otherwise you would introduce an uncertainty as big as the signal itself!!!
            #
            #if thsSignal.GetNhists() != 0:
              #for iBin in range(1,thsSignal.GetStack().Last().GetNbinsX()+1):
                #tgrMC_vy[iBin] += (thsSignal.GetStack().Last().GetBinContent(iBin))
                          
              #print " nominal: ", iBin, " ===> ", thsBackground.GetStack().Last().GetBinContent(iBin)
            #print " tgrMC_vy = ", tgrMC_vy

                #else :
                #  for iBin in range(1, histos[sampleName].GetNbinsX()+1):
                #    tgrBkg_vx[iBin-1] = (  histos[sampleName].GetBinCenter (iBin))
                #    tgrBkg_evx.append( histos[sampleName].GetBinWidth (iBin) / 2.)
                #    tgrBkg_vy[iBin-1] += histos[sampleName].GetBinContent (iBin)
                #    tgrBkg_evy_up[iBin-1] = SumQ ( tgrBkg_evy_up[iBin-1], self.GetPoissError(histos[sampleName].GetBinContent (iBin) , 0, 1) )
                #    tgrBkg_evy_do[iBin-1] = SumQ ( tgrBkg_evy_do[iBin-1], self.GetPoissError(histos[sampleName].GetBinContent (iBin) , 1, 0) ) 

            for nuisanceName in mynuisances.keys():
              # now we need to tell wthether the variation is actually up or down ans sum in quadrature those with the same sign 
              up = nuisances_vy_up[nuisanceName]
              do = nuisances_vy_do[nuisanceName]
              up_is_up = (up > tgrMC_vy)
              dup2 = np.square(up - tgrMC_vy)
              ddo2 = np.square(do - tgrMC_vy)
              nuisances_err2_up += np.where(up_is_up, dup2, ddo2)
              nuisances_err2_do += np.where(up_is_up, ddo2, dup2)

            nuisances_err_up = np.sqrt(nuisances_err2_up)
            nuisances_err_do = np.sqrt(nuisances_err2_do)

            tgrData       = ROOT.TGraphAsymmErrors(thsBackground.GetStack().Last().GetNbinsX())
            for iBin in range(0, len(tgrData_vx)) : 
              tgrData.SetPoint     (iBin, tgrData_vx[iBin], tgrData_vy[iBin])
              tgrData.SetPointError(iBin, tgrData_evx[iBin], tgrData_evx[iBin], tgrData_evy_do[iBin], tgrData_evy_up[iBin])
            
            tgrData.SetMarkerColor(dataColor)
            tgrData.SetLineColor(dataColor)
            
            ## Default: --postFit 0 --> No additional line is drawn
            ## ----------------------------------------------------

            ## --postFit 1 --> line is prefit
            if self._postFit == 'p':
                tgrDataOverPF = tgrData.Clone("tgrDataOverPF")    # use this for ratio with Post-Fit MC             
                histoPF = fileIn.Get(cutName+"/"+variableName+'/histo_total_prefit')
            ## --postFit 2 --> line is (S+B) postfit
            if self._postFit == 's':
                tgrDataOverPF = tgrData.Clone("tgrDataOverPF")    # use this for ratio with Post-Fit MC             
                histoPF = fileIn.Get(cutName+"/"+variableName+'/histo_total_postfit_s')
            ## --postFit 3 --> line is B-only postfit
            if self._postFit == 'b':
                tgrDataOverPF = tgrData.Clone("tgrDataOverPF")    # use this for ratio with Post-Fit MC             
                histoPF = fileIn.Get(cutName+"/"+variableName+'/histo_total_postfit_b')

            last = thsBackground.GetStack().Last()

            tgrDataOverMC = tgrData.Clone("tgrDataOverMC")
            tgrDataMinusMC = tgrData.Clone("tgrDataMinusMC")
            for iBin in range(0, len(tgrData_vx)) :
              tgrDataOverMC.SetPoint     (iBin, tgrData_vx[iBin], self.Ratio(tgrData_vy[iBin] , last.GetBinContent(iBin+1)) )
              tgrDataOverMC.SetPointError(iBin, tgrData_evx[iBin], tgrData_evx[iBin], self.Ratio(tgrData_evy_do[iBin], last.GetBinContent(iBin+1)) , self.Ratio(tgrData_evy_up[iBin], last.GetBinContent(iBin+1)) )
              if self._postFit == 'p' or self._postFit == 's' or  self._postFit == 'b':
                  tgrDataOverPF.SetPoint(iBin, tgrData_vx[iBin], self.Ratio(tgrData_vy[iBin] , histoPF.GetBinContent(iBin+1)) )
                  tgrDataOverPF.SetPointError(iBin, tgrData_evx[iBin], tgrData_evx[iBin], self.Ratio(tgrData_evy_do[iBin], histoPF.GetBinContent(iBin+1)) , self.Ratio(tgrData_evy_up[iBin], last.GetBinContent(iBin+1)) )
                  print "Pre-fit ratio: " + str(self.Ratio(tgrData_vy[iBin] , histoPF.GetBinContent(iBin+1)))
                  print "Post-fit ratio: " + str(self.Ratio(tgrData_vy[iBin] , last.GetBinContent(iBin+1)))
                  print iBin
              #
              # data - MC :
              #    MC could be background only
              #    or it can include the signal.
              #    Default is background+signal (check isSignal = 1,2,3 options).
              #    You can activate the data - "background only" by 
              #    using the flag "showDataMinusBkgOnly".
              #    NB: this will change also the case of "(data - expected) / expected"
              #
              #
              if self._showRelativeRatio :
                if self._showDataMinusBkgOnly :
                  tgrDataMinusMC.SetPoint     (iBin, tgrData_vx[iBin], self.Ratio( self.Difference(tgrData_vy[iBin] ,  tgrMC_vy[iBin]),   tgrMC_vy[iBin] ) )
                  tgrDataMinusMC.SetPointError(iBin, tgrData_evx[iBin], tgrData_evx[iBin], self.Ratio(tgrData_evy_do[iBin], tgrMC_vy[iBin]) , self.Ratio(tgrData_evy_up[iBin], tgrMC_vy[iBin]) )
                else :
                  tgrDataMinusMC.SetPoint     (iBin, tgrData_vx[iBin], self.Ratio( self.Difference(tgrData_vy[iBin] , last.GetBinContent(iBin+1)),   last.GetBinContent(iBin+1)) )
                  tgrDataMinusMC.SetPointError(iBin, tgrData_evx[iBin], tgrData_evx[iBin], self.Ratio(tgrData_evy_do[iBin], last.GetBinContent(iBin+1)) , self.Ratio(tgrData_evy_up[iBin], last.GetBinContent(iBin+1)) )
              else :
                if self._showDataMinusBkgOnly :
                  tgrDataMinusMC.SetPoint     (iBin, tgrData_vx[iBin], self.Difference(tgrData_vy[iBin] , tgrMC_vy[iBin]   ) )
                  tgrDataMinusMC.SetPointError(iBin, tgrData_evx[iBin], tgrData_evx[iBin], tgrData_evy_do[iBin] , tgrData_evy_up[iBin] )
                else :
                  tgrDataMinusMC.SetPoint     (iBin, tgrData_vx[iBin], self.Difference(tgrData_vy[iBin] , last.GetBinContent(iBin+1)) )
                  tgrDataMinusMC.SetPointError(iBin, tgrData_evx[iBin], tgrData_evx[iBin], tgrData_evy_do[iBin] , tgrData_evy_up[iBin] )
            
            
            #
            # if there is an histogram called 'histo_total'
            # it means that post-fit plots are provided, 
            # and we can neglect about the nuisances as "quadrature sum" here
            # and use directly the error bars (so far symmetric
            # see https://hypernews.cern.ch/HyperNews/CMS/get/higgs-combination/995.html )
            # from the histogram itself
            #
            special_shapeName = cutName+"/"+variableName+'/histo_total' 
            if type(fileIn) is dict:
              if 'total' in fileIn:
                histo_total = fileIn['total'].Get(special_shapeName)
              else:
                histo_total = None
            else:
              histo_total = fileIn.Get(special_shapeName)

            if variable['divideByBinWidth'] == 1 and histo_total != None:
              histo_total.Scale(1,"width")
            print ' --> ', histo_total
            
            if len(mynuisances.keys()) != 0:
              tgrMC = ROOT.TGraphAsymmErrors()  
              for iBin in range(0, len(tgrMC_vx)) :
                tgrMC.SetPoint     (iBin, tgrMC_vx[iBin], tgrMC_vy[iBin])
                if histo_total:
                  tgrMC.SetPointError(iBin, tgrMC_evx[iBin], tgrMC_evx[iBin], histo_total.GetBinError(iBin+1), histo_total.GetBinError(iBin+1))
                else :
                  tgrMC.SetPointError(iBin, tgrMC_evx[iBin], tgrMC_evx[iBin], nuisances_err_do[iBin], nuisances_err_up[iBin])
              
              tgrMCOverMC = tgrMC.Clone("tgrMCOverMC")  
              tgrMCMinusMC = tgrMC.Clone("tgrMCMinusMC")  
              for iBin in range(0, len(tgrMC_vx)) :
                tgrMCOverMC.SetPoint     (iBin, tgrMC_vx[iBin], 1.)
                tgrMCMinusMC.SetPoint    (iBin, tgrMC_vx[iBin], 0.)
                if histo_total:
                  tgrMCOverMC.SetPointError(iBin, tgrMC_evx[iBin], tgrMC_evx[iBin], self.Ratio(histo_total.GetBinError(iBin+1), tgrMC_vy[iBin]), self.Ratio(histo_total.GetBinError(iBin+1), tgrMC_vy[iBin]))     
                  if self._showRelativeRatio :
                    tgrMCMinusMC.SetPointError(iBin, tgrMC_evx[iBin], tgrMC_evx[iBin], self.Ratio(histo_total.GetBinError(iBin+1), tgrMC_vy[iBin]), self.Ratio(histo_total.GetBinError(iBin+1), tgrMC_vy[iBin]))     
                  else :
                    tgrMCMinusMC.SetPointError(iBin, tgrMC_evx[iBin], tgrMC_evx[iBin], histo_total.GetBinError(iBin+1), histo_total.GetBinError(iBin+1))     
                else :
                  tgrMCOverMC.SetPointError(iBin, tgrMC_evx[iBin], tgrMC_evx[iBin], self.Ratio(nuisances_err_do[iBin], tgrMC_vy[iBin]), self.Ratio(nuisances_err_up[iBin], tgrMC_vy[iBin]))     
                  if self._showRelativeRatio :
                    tgrMCMinusMC.SetPointError(iBin, tgrMC_evx[iBin], tgrMC_evx[iBin], self.Ratio(nuisances_err_do[iBin], tgrMC_vy[iBin]), self.Ratio(nuisances_err_up[iBin], tgrMC_vy[iBin]))     
                  else :
                    tgrMCMinusMC.SetPointError(iBin, tgrMC_evx[iBin], tgrMC_evx[iBin], nuisances_err_do[iBin], nuisances_err_up[iBin])     
                
                         
            
            tgrRatioList = {}
            for samplesToRatioName, samplesToRatio in sigForAdditionalRatioList.iteritems() :
              tgrDataOverMCTemp = tgrData.Clone("tgrDataOverMC"+samplesToRatioName)
              for iBin in range(0, len(tgrData_vx)) : 
                tgrDataOverMCTemp.SetPoint     (iBin, tgrData_vx[iBin], self.Ratio(tgrData_vy[iBin] , samplesToRatio.GetBinContent(iBin+1)) )
                tgrDataOverMCTemp.SetPointError(iBin, tgrData_evx[iBin], tgrData_evx[iBin], self.Ratio(tgrData_evy_do[iBin], samplesToRatio.GetBinContent(iBin+1)) , self.Ratio(tgrData_evy_up[iBin], samplesToRatio.GetBinContent(iBin+1)) )
                if variableName == 'events' :
                   print ' >> ratio[', cutName, '][', samplesToRatioName, ']  = ', self.Ratio(tgrData_vy[0] , samplesToRatio.GetBinContent(0+1)) 

              tgrDataOverMCTemp.SetLineColor(samplesToRatio.GetLineColor())
              tgrDataOverMCTemp.SetMarkerColor(samplesToRatio.GetLineColor())
              tgrDataOverMCTemp.SetMarkerSize(0.3)
              tgrRatioList[samplesToRatioName] = tgrDataOverMCTemp
              

            tgrDifferenceList = {}
            for samplesToDifferenceName, samplesToDifference in sigForAdditionalDifferenceList.iteritems() :
              tgrDataMinusMCTemp = tgrData.Clone("tgrDataMinusMC"+samplesToDifferenceName)
              for iBin in range(0, len(tgrData_vx)) : 
                tgrDataMinusMCTemp.SetPoint     (iBin, tgrData_vx[iBin], self.Difference(tgrData_vy[iBin] , samplesToDifference.GetBinContent(iBin+1)) )
                tgrDataMinusMCTemp.SetPointError(iBin, tgrData_evx[iBin], tgrData_evx[iBin], tgrData_evy_do[iBin] , tgrData_evy_up[iBin] )
                if variableName == 'events' :
                   print ' >> difference[', cutName, '][', samplesToDifferenceName, ']  = ', self.Difference(tgrData_vy[0] , samplesToDifference.GetBinContent(0+1)) 

              tgrDataMinusMCTemp.SetLineColor(samplesToDifference.GetLineColor())
              tgrDataMinusMCTemp.SetMarkerColor(samplesToDifference.GetLineColor())
              tgrDataMinusMCTemp.SetMarkerSize(0.3)
              tgrDifferenceList[samplesToDifferenceName] = tgrDataMinusMCTemp


            groupFlag = False
            #---- prepare the grouped histograms
            for sampleNameGroup, sampleConfiguration in groupPlot.iteritems():
              if 'samples' in variable and len(set(sampleConfiguration['samples']) & set(variable['samples'])) == 0:
                continue
                  
              if sampleConfiguration['isSignal'] == 1 :
                  print "############################################################## isSignal 1", sampleNameGroup
                  #
                  # if, for some reason, you want to scale only the overlaid signal
                  # for example to show the shape of the signal, without affecting the actual stacked (true) distribution
                  #
                  if 'scaleMultiplicativeOverlaid' in sampleConfiguration.keys() : 
                    # may this clone not mess up too much with "gDirectory", see TH1::Copy
                    temp_overlaid = histos_grouped[sampleNameGroup].Clone()
                    temp_overlaid.Scale(sampleConfiguration['scaleMultiplicativeOverlaid'])
                    thsSignal_grouped.Add(temp_overlaid)
                  else :
                    thsSignal_grouped.Add(histos_grouped[sampleNameGroup])
              elif sampleConfiguration['isSignal'] == 2 :
                  print "############################################################## isSignal 2", sampleNameGroup
                  groupFlag = True
                  sigSupList_grouped.append(histos_grouped[sampleNameGroup])
              # the signal is added on top of the background
              # the signal has to be the last one in the dictionary!
              # make it sure in plot.py
              if groupFlag == False:
                  thsBackground_grouped.Add(histos_grouped[sampleNameGroup])
            
            #---- now plot
            
            if thsBackground.GetNhists() != 0:
              print " MC   = ", thsBackground.GetStack().Last().Integral()
              for ihisto in range(thsBackground.GetNhists()) :
                print "     - ",ihisto, " - ", ((thsBackground.GetHists().At(ihisto))).GetName(), " = ", ((thsBackground.GetHists().At(ihisto))).Integral() 
                  
            if thsData.GetNhists() != 0:
              print " DATA = ", thsData.GetStack().Last().Integral()
               
             
                         
            #  - get axis range
            minXused = 0.
            maxXused = 1.

            minYused = 1.
            maxYused = 1.
            
            for sampleName, plotdef in plot.iteritems():
              if 'samples' in variable and sampleName not in variable['samples']:
                continue

              if plotdef['isData'] == 1 :
                histos[sampleName].Draw("p")
                minXused = histos[sampleName].GetXaxis().GetBinLowEdge(1)
                maxXused = histos[sampleName].GetXaxis().GetBinUpEdge(histos[sampleName].GetNbinsX())
                maxY = self.GetMaximumIncludingErrors(histos[sampleName])
                histos[sampleName].SetMaximum(self._scaleToPlot * maxY)
                maxYused = self._scaleToPlot * maxY
                minYused = self.GetMinimum(histos[sampleName])
            
            if thsBackground.GetNhists() != 0:
              thsBackground.Draw("hist")
              maxY = thsBackground.GetMaximum ()
              minXused = thsBackground.GetXaxis().GetBinLowEdge(1)
              maxXused = thsBackground.GetXaxis().GetBinUpEdge(thsBackground.GetHistogram().GetNbinsX())
              if (self._scaleToPlot * maxY) > maxYused :
                maxYused = self._scaleToPlot * maxY
              minY = thsBackground.GetMinimum ()
              if (minY < minYused) :
                minYused = minY 

               
            if thsSignal.GetNhists() != 0:
              thsSignal.Draw("hist")
              maxY = thsSignal.GetMaximum ()
              minXused = thsSignal.GetXaxis().GetBinLowEdge(1)
              maxXused = thsSignal.GetXaxis().GetBinUpEdge(thsSignal.GetHistogram().GetNbinsX())
              if (self._scaleToPlot * maxY) > maxYused :
                maxYused = self._scaleToPlot * maxY
              minY = thsSignal.GetMinimum ()
              if (minY < minYused) :
                minYused = minY 


            #print " X axis = ", minXused, " - ", maxXused
            frame = ROOT.TH1F
            frame = tcanvas.DrawFrame(minXused, 0.0, maxXused, 1.0)
            # style from https://ghm.web.cern.ch/ghm/plots/MacroExample/myMacro.py
            xAxis = frame.GetXaxis()
            xAxis.SetNdivisions(6,5,0)

            # setup axis names
            if 'xaxis' in variable.keys() : 
              frame.GetXaxis().SetTitle(variable['xaxis'])
              if variable["divideByBinWidth"] == 1:
                if "GeV" in variable['xaxis']: 
                  ### FIXME: it's maybe better to add a "yaxis" field in the variable to let the user choose the y axis name
                  frame.GetYaxis().SetTitle("dN/d"+variable['xaxis'].replace("GeV","GeV^{-1}"))
                else:
                  frame.GetYaxis().SetTitle("dN/d"+variable['xaxis'])
              else:
                if 'yaxis' in variable.keys() : 
                  frame.GetYaxis().SetTitle(variable['yaxis'])
                else :
                  frame.GetYaxis().SetTitle("Events")                  
            else :
              if variable["divideByBinWidth"] == 1:
                frame.GetYaxis().SetTitle("dN/d"+variableName)             
              else:
                if 'yaxis' in variable.keys() : 
                  frame.GetYaxis().SetTitle(variable['yaxis'])
                else :
                  frame.GetYaxis().SetTitle("Events")

            #
            #  - now draw
            #     - first the MC    
            #         before the background+signal, and then only the signal alone
            #
            if len(groupPlot.keys()) == 0:          
              if thsBackground.GetNhists() != 0:
                thsBackground.Draw("hist same")
                 
              if thsSignal.GetNhists() != 0:
                #for ihisto in range(thsSignal.GetNhists()) :
                  #((thsSignal.GetHists().At(ihisto))).SetFillStyle(0)
                  #((thsSignal.GetHists().At(ihisto))).Draw("hist same")
                thsSignal.Draw("hist same noclear")
            else :
              if thsBackground_grouped.GetNhists() != 0:
                thsBackground_grouped.Draw("hist same")
                 
              if thsSignal_grouped.GetNhists() != 0:
                thsSignal_grouped.Draw("hist same noclear")
              
              if len(sigSupList_grouped) != 0:
                for histo in sigSupList_grouped:
                  histo.Draw("hist same")
              
            
            # if there is a systematic band draw it
            if len(mynuisances.keys()) != 0:
              tgrMC.SetLineColor(12)
              tgrMC.SetFillColor(12)
              tgrMC.SetLineWidth(2)
              tgrMC.SetFillStyle(3004)
              tgrMCOverMC.SetLineColor(12)
              tgrMCOverMC.SetFillColor(12)
              tgrMCOverMC.SetLineWidth(2)
              tgrMCOverMC.SetFillStyle(3004)
              tgrMC.Draw("2")


	    #     - then the superimposed MC
            if len(sigSupList) != 0 and groupFlag==False:
              for hist in sigSupList:
                hist.Draw("hist same")
  
            #     - then the DATA  
            if tgrData.GetN() != 0:
              tgrData.Draw("P0")
            else : # never happening if at least one data histogram is provided
              for sampleName, plotdef in plot.iteritems():
                if 'samples' in variable and sampleName not in variable['samples']:
                  continue
                if plotdef['isData'] == 1 :
                  histos[sampleName].Draw("p same")

            #---- the Legend
            tlegend = ROOT.TLegend(0.20, 0.65, 0.80, 0.88)
            tlegend.SetFillColor(0)
            tlegend.SetTextFont(42)
            tlegend.SetTextSize(0.035)
            tlegend.SetLineColor(0)
            tlegend.SetShadowColor(0)
            reversedSampleNames = list(self._samples)
            reversedSampleNames.reverse()
            
            if len(groupPlot.keys()) == 0:
              for sampleName in reversedSampleNames:
                try:
                  plotdef = plot[sampleName]
                except KeyError:
                  continue

                if plotdef['isData'] == 0 :
                  if 'nameHR' in plotdef.keys() :
                    if plotdef['nameHR'] != '' :
                      if self._showIntegralLegend == 0 :
                        tlegend.AddEntry(histos[sampleName], plotdef['nameHR'], "F")
                      else :
                        if variable["divideByBinWidth"] == 1:
                          nevents = histos[sampleName].Integral(1,histos[sampleName].GetNbinsX(),"width") 
                        else:
                          nevents = histos[sampleName].Integral(1,histos[sampleName].GetNbinsX())
                        tlegend.AddEntry(histos[sampleName], plotdef['nameHR'] + " [" +  str(round(nevents,1)) + "]", "F")
                  else :
                    if self._showIntegralLegend == 0 :
                      tlegend.AddEntry(histos[sampleName], sampleName, "F")
                    else :
                      if variable["divideByBinWidth"] == 1:
                        nevents = histos[sampleName].Integral(1,histos[sampleName].GetNbinsX(),"width")
                      else:
                        nevents = histos[sampleName].Integral(1,histos[sampleName].GetNbinsX())
                      tlegend.AddEntry(histos[sampleName], sampleName + " [" +  str(round(nevents,1)) + "]", "F")
               
              for sampleName in reversedSampleNames:
                try:
                  plotdef = plot[sampleName]
                except KeyError:
                  continue

                if plotdef['isData'] == 1 :
                  if 'nameHR' in plotdef.keys() :
                    if self._showIntegralLegend == 0 :
                      tlegend.AddEntry(histos[sampleName], plotdef['nameHR'], "EPL")
                    else :
                      if variable["divideByBinWidth"] == 1:
                        nevents = histos[sampleName].Integral(1,histos[sampleName].GetNbinsX(),"width")
                      else:
                        nevents = histos[sampleName].Integral(1,histos[sampleName].GetNbinsX())
                      tlegend.AddEntry(histos[sampleName], plotdef['nameHR'] + " [" +  str(round(nevents,1)) + "]", "EPL")
                  else :
                    if self._showIntegralLegend == 0 :
                      tlegend.AddEntry(histos[sampleName], sampleName, "EPL")
                    else :
                      if variable["divideByBinWidth"] == 1:
                        nevents = histos[sampleName].Integral(1,histos[sampleName].GetNbinsX(),"width")
                      else:
                        nevents = histos[sampleName].Integral(1,histos[sampleName].GetNbinsX())
                      tlegend.AddEntry(histos[sampleName], sampleName + " [" +  str(round(nevents,1)) + "]", "EPL")
            
            else :
              for sampleNameGroup, sampleConfiguration in groupPlot.iteritems():
                if 'samples' in variable and len(set(sampleConfiguration['samples']) & set(variable['samples'])) == 0:
                  continue
                  
                if self._showIntegralLegend == 0 :
                  tlegend.AddEntry(histos_grouped[sampleNameGroup], sampleConfiguration['nameHR'], "F")
                else :
                  if variable["divideByBinWidth"] == 1:
                    nevents = histos_grouped[sampleNameGroup].Integral(1,histos_grouped[sampleNameGroup].GetNbinsX(),"width")
                  else:
                    nevents = histos_grouped[sampleNameGroup].Integral(1,histos_grouped[sampleNameGroup].GetNbinsX())
                  tlegend.AddEntry(histos_grouped[sampleNameGroup], sampleConfiguration['nameHR'] + " [" +  str(round(nevents,1)) + "]" , "F")
               
              for sampleName in reversedSampleNames:
                if 'samples' in variable and sampleName not in variable['samples']:
                  continue

                try:
                  plotdef = plot[sampleName]
                except KeyError:
                  continue
              
                if plotdef['isData'] == 1 :
                  if 'nameHR' in plotdef.keys() :
                    if self._showIntegralLegend == 0 :
                      tlegend.AddEntry(histos[sampleName], plotdef['nameHR'], "EPL")
                    else :
                      if variable["divideByBinWidth"] == 1:
                        nevents = histos[sampleName].Integral(1,histos[sampleName].GetNbinsX(),"width")
                      else:
                        nevents = histos[sampleName].Integral(1,histos[sampleName].GetNbinsX())
                      print " nevents [", sampleName, "] = ", nevents
                      tlegend.AddEntry(histos[sampleName], plotdef['nameHR'] + " [" +  str(round(nevents,1)) + "]", "EPL")
                  else :
                    if self._showIntegralLegend == 0 :
                      tlegend.AddEntry(histos[sampleName], sampleName , "EPL")
                    else :
                      if variable["divideByBinWidth"] == 1:
                        nevents = histos[sampleName].Integral(1,histos[sampleName].GetNbinsX(),"width")
                      else:
                        nevents = histos[sampleName].Integral(1,histos[sampleName].GetNbinsX())
                      print " nevents [", sampleName, "] = ", nevents
                      tlegend.AddEntry(histos[sampleName], sampleName + " [" +  str(round(nevents,1)) + "]", "EPL")
              
              
            if len(mynuisances.keys()) != 0:
                if self._showIntegralLegend == 0 :
                    tlegend.AddEntry(tgrMC, "All MC", "F")
                else :
                    print " nexpected  = ", nexpected
                    tlegend.AddEntry(tgrMC, "All MC [" + str(round(nexpected,1)) + "]", "F")
             
            tlegend.SetNColumns(2)
            tlegend.Draw()
            
            
            #change the CMS_lumi variables (see CMS_lumi.py)
            import LatinoAnalysis.ShapeAnalysis.CMS_lumi as CMS_lumi
            CMS_lumi.lumi_7TeV = "4.8 fb^{-1}"
            CMS_lumi.lumi_8TeV = "18.3 fb^{-1}"
            CMS_lumi.lumi_13TeV = "100 fb^{-1}"
            CMS_lumi.writeExtraText = 1
            CMS_lumi.extraText = "Preliminary"
            CMS_lumi.relPosX = 0.12
            CMS_lumi.lumi_sqrtS = "13 TeV" # used with iPeriod = 0, e.g. for simulation-only plots (default is an empty string)
            if 'sqrt' in legend.keys() :
              CMS_lumi.lumi_sqrtS = legend['sqrt']
            if 'lumi' in legend.keys() :
              CMS_lumi.lumi_13TeV = legend['lumi']
            else:
              CMS_lumi.lumi_13TeV = 'L = %.1f fb^{-1}' % self._lumi
        
            # Simple example of macro: plot with CMS name and lumi text
            #  (this script does not pretend to work in all configurations)
            # iPeriod = 1*(0/1 7 TeV) + 2*(0/1 8 TeV)  + 4*(0/1 13 TeV) 
            # For instance: 
            #               iPeriod = 3 means: 7 TeV + 8 TeV
            #               iPeriod = 7 means: 7 TeV + 8 TeV + 13 TeV 
            #               iPeriod = 0 means: free form (uses lumi_sqrtS)
            iPeriod = 4
            iPos  = 0
            CMS_lumi.CMS_lumi(tcanvas, iPeriod, iPos)    

    
            print "- draw tlegend"
            #---- the Legend (end)
            tlegend.Draw()


            frame.GetYaxis().SetRangeUser( 0, maxYused )
            # draw back all the axes            
            #frame.Draw("AXIS")
            tcanvas.RedrawAxis()

            if 'c' in self._plotsToWrite:
                if self._plotLinear:
                    self._saveCanvas(tcanvas, self._outputDirPlots + "/" + canvasNameTemplate + self._FigNamePF)

                if self._plotLog:
                    # log Y axis
                    frame.GetYaxis().SetRangeUser( max(self._minLogC, minYused), self._maxLogC * maxYused )  # Jonatan
                    #frame.GetYaxis().SetRangeUser( min(self._minLogC, minYused), self._maxLogC * maxYused )  # Jonatan
                    tcanvas.SetLogy(True)
                    # if plotLinear is true, we have already saved root and C (if in the list of formats)
                    self._saveCanvas(tcanvas, self._outputDirPlots + "/log_" + canvasNameTemplate + self._FigNamePF, imageOnly=self._plotLinear)
                    tcanvas.SetLogy(False)

                if 'root' in self._fileFormats:
                    text_file_html.write(canvasNameTemplate + self._FigNamePF + ".root;\n")


            # ~~~~~~~~~~~~~~~~~~~~
            # plot with ratio plot            
            print "- draw with ratio"
            
            canvasRatioNameTemplate = 'cratio_' + cutName + "_" + variableName

            tcanvasRatio.cd()
            canvasPad1Name = 'pad1_' + cutName + "_" + variableName
            pad1 = ROOT.TPad(canvasPad1Name,canvasPad1Name, 0, 1-0.72, 1, 1)
            pad1.SetTopMargin(0.098)
            pad1.SetBottomMargin(0.000) 
            pad1.Draw()
            #pad1.cd().SetGrid()
            
            pad1.cd()
            #print " pad1 = ", pad1
            canvasFrameDistroName = 'frame_distro_' + cutName + "_" + variableName
            frameDistro = pad1.DrawFrame(minXused, 0.0, maxXused, 1.0, canvasFrameDistroName)
            #print " pad1 = ", pad1
            
            # style from https://ghm.web.cern.ch/ghm/plots/MacroExample/myMacro.py
            xAxisDistro = frameDistro.GetXaxis()
            xAxisDistro.SetNdivisions(6,5,0)

            if 'xaxis' in variable.keys() :
              frameDistro.GetXaxis().SetTitle(variable['xaxis'])
              if variable["divideByBinWidth"] == 1:
                if "GeV" in variable['xaxis']: 
                  ### FIXME: it's maybe better to add a "yaxis" field in the variable to let the user choose the y axis name
                  frameDistro.GetYaxis().SetTitle("dN/d"+variable['xaxis'].replace("GeV","GeV^{-1}"))
                else:
                  frameDistro.GetYaxis().SetTitle("dN/d"+variable['xaxis'])
              else:
                if 'yaxis' in variable.keys() : 
                  frameDistro.GetYaxis().SetTitle(variable['yaxis'])
                else :
                  frameDistro.GetYaxis().SetTitle("Events")
            else :
              frameDistro.GetXaxis().SetTitle(variableName)
              if variable["divideByBinWidth"] == 1:
                frameDistro.GetYaxis().SetTitle("dN/d"+variableName)
              else:
                if 'yaxis' in variable.keys() : 
                  frameDistro.GetYaxis().SetTitle(variable['yaxis'])
                else :
                  frameDistro.GetYaxis().SetTitle("Events")
            #frameDistro.GetYaxis().SetRangeUser( 0, maxYused )
            frameDistro.GetYaxis().SetRangeUser( min(0.001, minYused), maxYused )


            if len(groupPlot.keys()) == 0:          
              if thsBackground.GetNhists() != 0:
                thsBackground.Draw("hist same")
                 
              if thsSignal.GetNhists() != 0:
                #for ihisto in range(thsSignal.GetNhists()) :
                  #((thsSignal.GetHists().At(ihisto))).SetFillStyle(0)
                  #((thsSignal.GetHists().At(ihisto))).Draw("hist same")
                thsSignal.Draw("hist same noclear")
            else :
              if thsBackground_grouped.GetNhists() != 0:
                thsBackground_grouped.Draw("hist same")
                 
              if thsSignal_grouped.GetNhists() != 0:
                thsSignal_grouped.Draw("hist same noclear")

              if len(sigSupList_grouped) != 0:
                for histo in sigSupList_grouped: 
                  histo.Draw("hist same")
           
            if (len(mynuisances.keys())!=0):
              tgrMC.Draw("2")
             
            #     - then the superimposed MC
            if len(sigSupList) != 0 and groupFlag==False:
              for hist in sigSupList:
                hist.Draw("hist same")

            #     - then the DATA  
            if tgrData.GetN() != 0:
              tgrData.Draw("P0")
    
            tlegend.Draw()
            #if 'lumi' in legend.keys() and 'sqrt' not in legend.keys():
              #flag_lumi = ROOT.TLatex (minXused + (maxXused-minXused)*3./4., 0 + (maxYused-0)*3.9/4., legend['lumi'])
              #flag_lumi.Draw()
            #if 'sqrt' in legend.keys() and 'lumi' not in legend.keys():
              #flag_sqrt = ROOT.TLatex (minXused + (maxXused-minXused)*3./4., 0 + (maxYused-0)*3.9/4., legend['sqrt'])
              #flag_sqrt.Draw()
            #if 'sqrt' in legend.keys() and 'lumi' in legend.keys():
              #flag_lumi_sqrt = ROOT.TLatex (minXused + (maxXused-minXused)*2.5/4., 0 + (maxYused-0)*3.9/4., "#splitline{CMS preliminary}{#splitline{" +  legend['lumi'] + "}{" + legend['sqrt'] + "} }")
              #flag_lumi_sqrt.Draw()
    
            CMS_lumi.CMS_lumi(tcanvasRatio, iPeriod, iPos)    

            # draw back all the axes            
            #frameDistro.Draw("AXIS")
            pad1.RedrawAxis()

                
            tcanvasRatio.cd()
            canvasPad2Name = 'pad2_' + cutName + "_" + variableName
            pad2 = ROOT.TPad(canvasPad2Name,canvasPad2Name,0,0,1,1-0.72)
            pad2.SetTopMargin(0.000)
            pad2.SetBottomMargin(0.392)
            pad2.Draw()
            #pad2.cd().SetGrid()
            pad2.cd()
            
            #print " pad1 = ", pad1
            #print " pad2 = ", pad2, " minXused = ", minXused, " maxXused = ", maxXused
            canvasFrameRatioName = 'frame_ratio_' + cutName + "_" + variableName
            #print " canvasFrameRatioName = ", canvasFrameRatioName
            frameRatio = pad2.DrawFrame(minXused, 0.0, maxXused, 2.0, canvasFrameRatioName)
            #print " pad2 = ", pad2
            # style from https://ghm.web.cern.ch/ghm/plots/MacroExample/myMacro.py
            xAxisDistro = frameRatio.GetXaxis()
            xAxisDistro.SetNdivisions(6,5,0)

            if 'xaxis' in variable.keys() : 
              frameRatio.GetXaxis().SetTitle(variable['xaxis'])
            else :
              frameRatio.GetXaxis().SetTitle(variableName)
            frameRatio.GetYaxis().SetTitle("Data/Expected")
            #frameRatio.GetYaxis().SetTitle("Data/MC")
            #frameRatio.GetYaxis().SetRangeUser( 0.0, 2.0 )
            frameRatio.GetYaxis().SetRangeUser( 0.5, 1.5 )
            self.Pad2TAxis(frameRatio)
            if (len(mynuisances.keys())!=0):
              tgrMCOverMC.Draw("2") 
            
            tgrDataOverMC.Draw("P0")
            
            
            if self._postFit == 'p' or self._postFit == 's' or  self._postFit == 'b':
            #---- Ratio Legend
                tlegendRatio = ROOT.TLegend(0.20, 0.40, 0.60, 0.55)
                tlegendRatio.SetFillColor(0)
                tlegendRatio.SetTextFont(42)
                ##tlegendRatio.SetTextSize(0.035)
                tlegendRatio.SetLineColor(0)
                tlegendRatio.SetShadowColor(0)
                
                if self._postFit == 'p':
                    tlegendRatio.AddEntry(tgrDataOverMC, "post-fit", "PL")
                    tlegendRatio.AddEntry(tgrDataOverPF, "pre-fit", "PL")
                if self._postFit == 's' or  self._postFit == 'b':
                    tlegendRatio.AddEntry(tgrDataOverMC, "pre-fit", "PL")
                    tlegendRatio.AddEntry(tgrDataOverPF, "post-fit", "PL")
                
                for sampleName, sample in self._samples.iteritems():
                    ##if sampleName.find('total') == 1: 
                    ## or sampleName == 'total_background_prefit' or sampleName == 'total_background_postfit_s' or sampleName == 'total_background_postfit_b':
                    if 'total' in sampleName:
                        tgrDataOverPF.SetMarkerColor(plot[sampleName]['color'])
                        tgrDataOverPF.SetLineColor(plot[sampleName]['color'])
                        # tgrDataOverPF.SetMarkerColor(2)
                        # tgrDataOverPF.SetLineColor(2)
                tgrDataOverPF.Draw("PE,same")
                tlegendRatio.Draw("same")
            
            
            for samplesToRatioGrName, samplesGrToRatio in tgrRatioList.iteritems() :
              samplesGrToRatio.Draw("P")

            
            oneLine2 = ROOT.TLine(frameRatio.GetXaxis().GetXmin(), 1,  frameRatio.GetXaxis().GetXmax(), 1);
            oneLine2.SetLineStyle(3)
            oneLine2.SetLineWidth(3)
            oneLine2.Draw("same")

            # draw back all the axes            
            #frameRatio.Draw("AXIS")
            pad2.RedrawAxis()
            pad2.SetGrid()

            if 'cratio' in self._plotsToWrite:
                if self._plotLinear:
                    self._saveCanvas(tcanvasRatio, self._outputDirPlots + "/" + canvasRatioNameTemplate + self._FigNamePF)

                if self._plotLog:
                    # log Y axis
                    #frameDistro.GetYaxis().SetRangeUser( max(self._minLogCratio, maxYused/1000), self._maxLogCratio * maxYused )
                    frameDistro.GetYaxis().SetRangeUser( min(self._minLogCratio, maxYused/1000), self._maxLogCratio * maxYused )
                    pad1.SetLogy(True)
                    self._saveCanvas(tcanvasRatio, self._outputDirPlots + "/log_" + canvasRatioNameTemplate + self._FigNamePF, imageOnly=self._plotLinear)
                    pad1.SetLogy(False)


            if 'root' in self._fileFormats:
                text_file_html.write(canvasRatioNameTemplate + ".root;\n")

            













            # ~~~~~~~~~~~~~~~~~~~~
            # plot with difference plot            
            print "- draw with difference"
            
            if self._showRelativeRatio :
              canvasDifferenceNameTemplate = 'cdifference_relative_' + cutName + "_" + variableName
            else :
              canvasDifferenceNameTemplate = 'cdifference_' + cutName + "_" + variableName

            tcanvasDifference.cd()
            canvasPad1differenceName = 'pad1difference_' + cutName + "_" + variableName
            pad1difference = ROOT.TPad(canvasPad1differenceName,canvasPad1differenceName, 0, 1-0.72, 1, 1)
            pad1difference.SetTopMargin(0.098)
            pad1difference.SetBottomMargin(0.000) 
            pad1difference.Draw()
            #pad1difference.cd().SetGrid()
            
            pad1difference.cd()
            #print " pad1difference = ", pad1difference
            canvasFrameDistroName = 'frame_distro_' + cutName + "_" + variableName
            frameDistro = pad1difference.DrawFrame(minXused, 0.0, maxXused, 1.0, canvasFrameDistroName)
            #print " pad1difference = ", pad1difference
            
            # style from https://ghm.web.cern.ch/ghm/plots/MacroExample/myMacro.py
            xAxisDistro = frameDistro.GetXaxis()
            xAxisDistro.SetNdivisions(6,5,0)

            if 'xaxis' in variable.keys() :
              frameDistro.GetXaxis().SetTitle(variable['xaxis'])
              if variable["divideByBinWidth"] == 1:
                if "GeV" in variable['xaxis']: 
                  ### FIXME: it's maybe better to add a "yaxis" field in the variable to let the user choose the y axis name
                  frameDistro.GetYaxis().SetTitle("dN/d"+variable['xaxis'].replace("GeV","GeV^{-1}"))
                else:
                  frameDistro.GetYaxis().SetTitle("dN/d"+variable['xaxis'])
              else:
                if 'yaxis' in variable.keys() : 
                  frameDistro.GetYaxis().SetTitle(variable['yaxis'])
                else :
                  frameDistro.GetYaxis().SetTitle("Events")
            else :
              frameDistro.GetXaxis().SetTitle(variableName)
              if variable["divideByBinWidth"] == 1:
                frameDistro.GetYaxis().SetTitle("dN/d"+variableName)
              else:
                if 'yaxis' in variable.keys() : 
                  frameDistro.GetYaxis().SetTitle(variable['yaxis'])
                else :
                  frameDistro.GetYaxis().SetTitle("Events")
            #frameDistro.GetYaxis().SetRangeUser( 0, maxYused )
            frameDistro.GetYaxis().SetRangeUser( min(0.001, minYused), maxYused )


            if len(groupPlot.keys()) == 0:          
              if thsBackground.GetNhists() != 0:
                thsBackground.Draw("hist same")
                 
              if thsSignal.GetNhists() != 0:
                #for ihisto in range(thsSignal.GetNhists()) :
                  #((thsSignal.GetHists().At(ihisto))).SetFillStyle(0)
                  #((thsSignal.GetHists().At(ihisto))).Draw("hist same")
                thsSignal.Draw("hist same noclear")
            else :
              if thsBackground_grouped.GetNhists() != 0:
                thsBackground_grouped.Draw("hist same")
                 
              if thsSignal_grouped.GetNhists() != 0:
                thsSignal_grouped.Draw("hist same noclear")

              if len(sigSupList_grouped) != 0:
                for histo in sigSupList_grouped: 
                  histo.Draw("hist same")
           
            if (len(mynuisances.keys())!=0):
              tgrMC.Draw("2")
             
            #     - then the superimposed MC
            if len(sigSupList) != 0 and groupFlag==False:
              for hist in sigSupList:
                hist.Draw("hist same")

            #     - then the DATA  
            if tgrData.GetN() != 0:
              tgrData.Draw("P0")
    
            tlegend.Draw()
            #if 'lumi' in legend.keys() and 'sqrt' not in legend.keys():
              #flag_lumi = ROOT.TLatex (minXused + (maxXused-minXused)*3./4., 0 + (maxYused-0)*3.9/4., legend['lumi'])
              #flag_lumi.Draw()
            #if 'sqrt' in legend.keys() and 'lumi' not in legend.keys():
              #flag_sqrt = ROOT.TLatex (minXused + (maxXused-minXused)*3./4., 0 + (maxYused-0)*3.9/4., legend['sqrt'])
              #flag_sqrt.Draw()
            #if 'sqrt' in legend.keys() and 'lumi' in legend.keys():
              #flag_lumi_sqrt = ROOT.TLatex (minXused + (maxXused-minXused)*2.5/4., 0 + (maxYused-0)*3.9/4., "#splitline{CMS preliminary}{#splitline{" +  legend['lumi'] + "}{" + legend['sqrt'] + "} }")
              #flag_lumi_sqrt.Draw()
    
            CMS_lumi.CMS_lumi(tcanvasDifference, iPeriod, iPos)    

            # draw back all the axes            
            #frameDistro.Draw("AXIS")
            pad1difference.RedrawAxis()

                
            tcanvasDifference.cd()
            canvasPad2differenceName = 'pad2difference_' + cutName + "_" + variableName
            pad2difference = ROOT.TPad(canvasPad2differenceName,canvasPad2differenceName,0,0,1,1-0.72)
            pad2difference.SetTopMargin(0.000)
            pad2difference.SetBottomMargin(0.392)
            pad2difference.Draw()
            #pad2difference.cd().SetGrid()
            pad2difference.cd()

            canvasFrameDifferenceName = 'frame_difference_' + cutName + "_" + variableName
            
            if self._showRelativeRatio :
              frameDifference = pad2difference.DrawFrame(minXused, -1.0 , maxXused,  1.0 , canvasFrameDifferenceName)
            else :
              frameDifference = pad2difference.DrawFrame(minXused, int ( ROOT.TMath.MinElement(tgrDataMinusMC.GetN(),tgrDataMinusMC.GetY())  - 2 ), maxXused,  int ( ROOT.TMath.MaxElement(tgrDataMinusMC.GetN(),tgrDataMinusMC.GetY())  + 2 ), canvasFrameDifferenceName)


            # style from https://ghm.web.cern.ch/ghm/plots/MacroExample/myMacro.py
            xAxisDistro = frameDifference.GetXaxis()
            xAxisDistro.SetNdivisions(6,5,0)

            if 'xaxis' in variable.keys() : 
              frameDifference.GetXaxis().SetTitle(variable['xaxis'])
            else :
              frameDifference.GetXaxis().SetTitle(variableName)

            if self._showRelativeRatio :
              frameDifference.GetYaxis().SetTitle("#frac{Data - Expected}{Expected}")
              frameDifference.GetYaxis().SetRangeUser(  -1.0, 1.0  )
            else :
              frameDifference.GetYaxis().SetTitle("Data - Expected")
              frameDifference.GetYaxis().SetRangeUser(  int (ROOT.TMath.MinElement(tgrDataMinusMC.GetN(),tgrDataMinusMC.GetY()) - 2 ),  int (ROOT.TMath.MaxElement(tgrDataMinusMC.GetN(),tgrDataMinusMC.GetY()) + 2 ) )
            self.Pad2TAxis(frameDifference)
            if (len(mynuisances.keys())!=0):
              tgrMCMinusMC.SetLineColor(12)
              tgrMCMinusMC.SetFillColor(12)
              tgrMCMinusMC.SetLineWidth(2)
              tgrMCMinusMC.SetFillStyle(3004)
              tgrMCMinusMC.Draw("2") 
            
            tgrDataMinusMC.Draw("P0")
            
            
            #print " tgrDataMinusMC.GetMinimum()/Max = " , tgrDataMinusMC.GetMinimum(), " / " , tgrDataMinusMC.GetMaximum()
            
            
            
            for samplesToDifferenceGrName, samplesGrToDifference in tgrDifferenceList.iteritems() :
              samplesGrToDifference.Draw("P")

            
            oneLine2 = ROOT.TLine(frameDifference.GetXaxis().GetXmin(), 0,  frameDifference.GetXaxis().GetXmax(), 0);
            oneLine2.SetLineStyle(3)
            oneLine2.SetLineWidth(3)
            oneLine2.Draw("same")

            # draw back all the axes            
            #frameDifference.Draw("AXIS")
            pad2difference.RedrawAxis()
            pad2difference.SetGrid()

            if 'cdifference' in self._plotsToWrite:
                if self._plotLinear:
                    self._saveCanvas(tcanvasDifference, self._outputDirPlots + "/" + canvasDifferenceNameTemplate + self._FigNamePF)

                if self._plotLog:
                    # log Y axis
                    #frameDistro.GetYaxis().SetRangeUser( max(self._minLogCdifference, maxYused/1000), self._maxLogCdifference * maxYused )
                    frameDistro.GetYaxis().SetRangeUser( min(self._minLogCdifference, maxYused/1000), self._maxLogCdifference * maxYused )
                    pad1difference.SetLogy(True)
                    self._saveCanvas(tcanvasDifference, self._outputDirPlots + "/log_" + canvasDifferenceNameTemplate + self._FigNamePF, imageOnly=self._plotLinear)
                    pad1difference.SetLogy(False)

                if 'root' in self._fileFormats:
                    text_file_html.write(canvasDifferenceNameTemplate + ".root;\n")






          
            #
            # draw weighted plot
            #
            
            if 'doWeight' in variable.keys() : 
              if variable['doWeight'] == 1 :
                if 'binX' in variable.keys() and 'binY' in variable.keys() :
                  nbinX = variable['binX']
                  nbinY = variable['binY']
                  
                  #
                  # Add weight 1D
                  #  - sample the 1D histogram in 'nbinX' slices long 'nbinY'.
                  #  - calculate the integral of S and B for each of them
                  #  - add a weight on them S/B, for signal, background and data
                  #  - add the weighted histogram to the final histogram, made of 'nbinY' bins
                  #
      
                  
                  # trick to exchange X <-> Y
                  if self._invertXY :
                    temp_nbinX = nbinX
                    nbinX = nbinY
                    nbinY = temp_nbinX
                    
        
                  #
                  # check if I have to remove the signal on the ackground stack here
                  #  --> ok, it works and it is correct
                  #
                  if thsBackground.GetNhists() != 0 and thsSignal.GetNhists() != 0 :

                    weight_X_thsData       = ROOT.THStack ("weight_X_thsData",      "weight_X_thsData")
                    weight_X_thsSignal     = ROOT.THStack ("weight_X_thsSignal",    "weight_X_thsSignal")
                    weight_X_thsBackground = ROOT.THStack ("weight_X_thsBackground","weight_X_thsBackground")
                  
                    #
                    # the final histogram should be scaled such that the integral
                    # is the expected signal + background yield
                    # --> or only background ?
                    #
                    if len(groupPlot.keys()) == 0:          
                      totalBkg = thsBackground.GetStack().Last().Integral()
                      totalSig = thsSignal.GetStack().Last().Integral()
                    else :
                      totalBkg = thsBackground_grouped.GetStack().Last().Integral()
                      totalSig = thsSignal_grouped.GetStack().Last().Integral()

                      
                    totalBkgSig = totalBkg + totalSig
                    
                    totalWeightedIntegralBkg = 0.
                    totalWeightedIntegralSig = 0.
                    
                    weight_X_list_Data = []
                    weight_X_list_Signal = []
                    weight_X_list_Background = []
                    weight_X_list_weights = []
                    
                    for sliceX in range(nbinX) :
                      integral_bkg = 0.
                      #for ibin in range( thsBackground.GetStack().Last().GetNbinsX() )
                      for ibin in range( nbinY ) :
                        if len(groupPlot.keys()) == 0:          

                          if self._invertXY :
                            integral_bkg += thsBackground.GetStack().Last().GetBinContent(ibin*nbinX +1 + sliceX)
                          else :
                            integral_bkg += thsBackground.GetStack().Last().GetBinContent(ibin+1 + sliceX * nbinY)

                        else :

                          if self._invertXY :
                            integral_bkg += thsBackground_grouped.GetStack().Last().GetBinContent(ibin*nbinX +1 + sliceX)
                          else :
                            integral_bkg += thsBackground_grouped.GetStack().Last().GetBinContent(ibin+1 + sliceX * nbinY)

                      integral_sig = 0.
                      
                      if len(groupPlot.keys()) == 0:          
                        for ibin in range( thsSignal.GetStack().Last().GetNbinsX() ) :

                          if self._invertXY :
                            integral_sig += thsSignal.GetStack().Last().GetBinContent(ibin*nbinX +1 + sliceX)
                          else :
                            integral_sig += thsSignal.GetStack().Last().GetBinContent(ibin+1 + sliceX * nbinY)

                      else :
                        for ibin in range( thsSignal_grouped.GetStack().Last().GetNbinsX() ) :

                          if self._invertXY :
                            integral_sig += thsSignal_grouped.GetStack().Last().GetBinContent(ibin*nbinX +1 + sliceX)
                          else :
                            integral_sig += thsSignal_grouped.GetStack().Last().GetBinContent(ibin+1 + sliceX * nbinY)
                      
                      # this is because the signal was added into the background  stack before    
                      integral_bkg = integral_bkg - integral_sig
                      weight = 1
                      if integral_bkg != 0 : 
                        weight = integral_sig / integral_bkg
                      else :
                        weight = 1

                      #
                      # remove weight: use just 1 for each line,
                      # meaning we are just adding the bins together
                      #
                      if self._removeWeight == True :
                        weight = 1
                        
                      weight_X_list_weights.append(weight)
                      
                      
                      if len(groupPlot.keys()) == 0:          

                          for ihisto in range(thsBackground.GetNhists()):
                             hentry = thsBackground.GetHists().At(ihisto)

                             histo = ROOT.TH1F('h_weigth_X_' +  cutName + '_' + variableName + '_' + hentry.GetName() + '_slice_'+ str(sliceX), '-' , nbinY, 0, nbinY)
                             histo = self.FixBins (histo, tgrData_vx, tgrData_evx)
                                      
                             histo.SetFillColor( hentry.GetFillColor())
                             histo.SetFillStyle( hentry.GetFillStyle())
                             histo.SetLineColor( hentry.GetLineColor())
                             histo.SetLineWidth( hentry.GetLineWidth())
                             
                             for ibin in range( nbinY ) :
                               if self._invertXY :
                                 histo.SetBinContent(ibin+1, weight * ( hentry.GetBinContent(ibin*nbinX +1 + sliceX) ) )
                               else :
                                 histo.SetBinContent(ibin+1, weight * ( hentry.GetBinContent(ibin+1 + sliceX * nbinY) ) )
                             
                             if sliceX != 0:
                               weight_X_list_Background[ihisto].Add(histo)
                             else :
                               weight_X_list_Background.append(histo)
                          
                             # the minus signal is because the signal was added into the background stack before  
                             if ihisto < (thsBackground.GetNhists() - thsSignal.GetNhists()) :
                               totalWeightedIntegralBkg += histo.Integral()
                          
                             
                          for ihisto in range(thsSignal.GetNhists()):
                             hentry = thsSignal.GetHists().At(ihisto)

                             histo = ROOT.TH1F('h_weigth_X_' +  cutName + '_' + variableName + '_' + (()).GetName() + '_slice_'+ str(sliceX), "-", nbinY, 0, nbinY)
                             histo = self.FixBins (histo, tgrData_vx, tgrData_evx)
                             
                             histo.SetFillColor( hentry.GetFillColor())
                             histo.SetFillStyle( hentry.GetFillStyle())
                             histo.SetLineColor( hentry.GetLineColor())
                             histo.SetLineWidth( hentry.GetLineWidth())
                             
                             for ibin in range( nbinY ) :
                               if self._invertXY :
                                 histo.SetBinContent(ibin+1, weight * ( hentry.GetBinContent(ibin*nbinX +1 + sliceX) ) )
                               else :
                                 histo.SetBinContent(ibin+1, weight * ( hentry.GetBinContent(ibin+1 + sliceX * nbinY) ) )
                          
                             if sliceX != 0:
                               weight_X_list_Signal[ihisto].Add(histo)
                             else :
                               weight_X_list_Signal.append(histo)
                               
                             totalWeightedIntegralSig += histo.Integral()
                          
                          
                          for ihisto in range(thsData.GetNhists()) :
                             hentry = thsData.GetHists().At(ihisto)

                             histo = ROOT.TH1F('h_weigth_X_' +  cutName + '_' + variableName + '_' + hentry.GetName() + '_slice_'+ str(sliceX), "-", nbinY, 0, nbinY)
                             histo = self.FixBins (histo, tgrData_vx, tgrData_evx)

                             for ibin in range( nbinY ) :
                               if self._invertXY :
                                 histo.SetBinContent(ibin+1, weight * ( hentry.GetBinContent(ibin*nbinX +1 + sliceX ) ) )
                               else :
                                 histo.SetBinContent(ibin+1, weight * ( hentry.GetBinContent(ibin+1 + sliceX * nbinY) ) )
                             
                             if sliceX != 0:
                               weight_X_list_Data[ihisto].Add(histo)
                             else :
                               weight_X_list_Data.append(histo)
                             #weight_X_list_Data.append(histo)  ## aaaargh!
                      
                      else :

                          for ihisto in range(thsBackground_grouped.GetNhists()):
                             hentry = thsBackground_grouped.GetHists().At(ihisto)

                             histo = ROOT.TH1F('h_weigth_X_' +  cutName + '_' + variableName + '_' + hentry.GetName() + '_slice_'+ str(sliceX), '-' , nbinY, 0, nbinY)
                             histo = self.FixBins (histo, tgrData_vx, tgrData_evx)
                             
                             histo.SetFillColor( hentry.GetFillColor())
                             histo.SetFillStyle( hentry.GetFillStyle())
                             histo.SetLineColor( hentry.GetLineColor())
                             histo.SetLineWidth( hentry.GetLineWidth())
                             
                             for ibin in range( nbinY ) :
                               if self._invertXY :
                                 histo.SetBinContent(ibin+1, weight * ( hentry.GetBinContent(ibin*nbinX +1 + sliceX) ) )
                               else :
                                 histo.SetBinContent(ibin+1, weight * ( hentry.GetBinContent(ibin+1 + sliceX * nbinY) ) )
                             
                             if sliceX != 0:
                               weight_X_list_Background[ihisto].Add(histo)
                             else :
                               weight_X_list_Background.append(histo)
                          
                             # the minus signal is because the signal was added into the background stack before  
                             if ihisto < (thsBackground_grouped.GetNhists() - thsSignal_grouped.GetNhists()) :
                               totalWeightedIntegralBkg += histo.Integral()
                          
                             
                          for ihisto in range(thsSignal_grouped.GetNhists()):
                             hentry = thsSignal_grouped.GetHists().At(ihisto)

                             histo = ROOT.TH1F('h_weigth_X_' +  cutName + '_' + variableName + '_' + hentry.GetName() + '_slice_'+ str(sliceX), "-", nbinY, 0, nbinY)
                             histo = self.FixBins (histo, tgrData_vx, tgrData_evx)

                             histo.SetFillColor( hentry.GetFillColor())
                             histo.SetFillStyle( hentry.GetFillStyle())
                             histo.SetLineColor( hentry.GetLineColor())
                             histo.SetLineWidth( hentry.GetLineWidth())
                             
                             for ibin in range( nbinY ) :
                               if self._invertXY :
                                 histo.SetBinContent(ibin+1, weight * ( hentry.GetBinContent(ibin*nbinX +1 + sliceX) ) )
                               else :
                                 histo.SetBinContent(ibin+1, weight * ( hentry.GetBinContent(ibin+1 + sliceX * nbinY) ) )
                          
                             if sliceX != 0:
                               weight_X_list_Signal[ihisto].Add(histo)
                             else :
                               weight_X_list_Signal.append(histo)
                               
                             totalWeightedIntegralSig += histo.Integral()
                          
                          
                          
                          
                          for ihisto in range(thsData.GetNhists()):
                             hentry = thsData.GetHists().At(ihisto)

                             histo = ROOT.TH1F('h_weigth_X_' +  cutName + '_' + variableName + '_' + hentry.GetName() + '_slice_'+ str(sliceX), "-", nbinY, 0, nbinY)
                             histo = self.FixBins (histo, tgrData_vx, tgrData_evx)

                             for ibin in range( nbinY ) :
                               if self._invertXY :
                                 histo.SetBinContent(ibin+1, weight * ( hentry.GetBinContent(ibin*nbinX +1 + sliceX) ) )
                               else :
                                 histo.SetBinContent(ibin+1, weight * ( hentry.GetBinContent(ibin+1 + sliceX * nbinY) ) )
                             
                             if sliceX != 0:
                               weight_X_list_Data[ihisto].Add(histo)
                             else :
                               weight_X_list_Data.append(histo)
                             #weight_X_list_Data.append(histo)  ## aaaargh!
 




                    # 
                    # gloabal scale factor so that the total number of events is such that
                    # the expected signal events is unchanged
                    #
                    #global_normalization = totalBkg / totalWeightedIntegralBkg
                    global_normalization = totalSig / totalWeightedIntegralSig
                    
                    
                    for histo in weight_X_list_Data:
                       histo.Scale(global_normalization)
                    for histo in weight_X_list_Background:
                       histo.Scale(global_normalization)
                    for histo in weight_X_list_Signal:
                       histo.Scale(global_normalization)
                  
                    for histo in weight_X_list_Data:
                       weight_X_thsData.Add(histo)
                    for histo in weight_X_list_Background:
                       weight_X_thsBackground.Add(histo)
                    for histo in weight_X_list_Signal:
                       weight_X_thsSignal.Add(histo)


                    #print " weight_X_list_weights = ", weight_X_list_weights
     
                    # create the weighted data distribution
                    weight_X_tgrData = ROOT.TGraphAsymmErrors()
                    for sliceX in range( nbinX ) :
                      for ibin in range( nbinY ) :
                        x = tgrData_vx[ibin]
                        #print " sliceX, ibin = ", sliceX, " , ", ibin, " -> ", tgrData_vx[ibin]

                        number_of_bin = ibin + sliceX * nbinY
                        if self._invertXY :
                          number_of_bin = ibin*nbinX + sliceX

                        y      = weight_X_list_weights[sliceX] * global_normalization * tgrData_vy[number_of_bin]
                        exlow  = tgrData_evx[number_of_bin]
                        exhigh = tgrData_evx[number_of_bin]
                        eylow  = weight_X_list_weights[sliceX] * global_normalization * tgrData_evy_do[number_of_bin]
                        eyhigh = weight_X_list_weights[sliceX] * global_normalization * tgrData_evy_up[number_of_bin]
                        
                        if sliceX != 0:
                          y += weight_X_tgrData.GetY()[ibin]
                          eylow  = self.SumQ ( eylow,  weight_X_tgrData.GetErrorYlow(ibin) )
                          eyhigh = self.SumQ ( eyhigh, weight_X_tgrData.GetErrorYhigh(ibin) )
                        
                        #print " eylow = ", eylow, " eyhigh = ", eyhigh, " y = ", y, " x = ", x 
                        
                        weight_X_tgrData.SetPoint      (ibin, x, y)
                        weight_X_tgrData.SetPointError (ibin, exlow, exhigh, eylow, eyhigh)
                     
                        #if sliceX == ( nbinX - 1) :
                          #print " ibin,x,y = ", ibin, ", ", x, ", ", y
                          
                    # create the weighted data distribution
                    weight_X_tgrMC = ROOT.TGraphAsymmErrors()
                    for sliceX in range(nbinX) :
                      for ibin in range( nbinY ) :
                        x = tgrData_vx[ibin]

                        number_of_bin = ibin + sliceX * nbinY
                        if self._invertXY :
                          number_of_bin = ibin*nbinX + sliceX

                        y = weight_X_list_weights[sliceX] * global_normalization * tgrMC_vy[number_of_bin]
                        exlow  = tgrData_evx[number_of_bin]
                        exhigh = tgrData_evx[number_of_bin]
                        eylow = 0
                        eyhigh = 0
                        if len(nuisances_err_do) != 0:
                          if histo_total:
                            eylow  = weight_X_list_weights[sliceX] * global_normalization * histo_total.GetBinError(number_of_bin + 1)
                            eyhigh = weight_X_list_weights[sliceX] * global_normalization * histo_total.GetBinError(number_of_bin + 1)
                          else :                        
                            eylow  = weight_X_list_weights[sliceX] * global_normalization * nuisances_err_do[number_of_bin]
                            eyhigh = weight_X_list_weights[sliceX] * global_normalization * nuisances_err_up[number_of_bin]
                        
                        if sliceX != 0 :
                          y += weight_X_tgrMC.GetY()[ibin]
                          eylow  = self.SumQ ( eylow,  weight_X_tgrMC.GetErrorYlow(ibin) )
                          eyhigh = self.SumQ ( eyhigh, weight_X_tgrMC.GetErrorYhigh(ibin) )
                        
                        #print " eylow = ", eylow, " eyhigh = ", eyhigh, " y = ", y, " x = ", x 

                        weight_X_tgrMC.SetPoint      (ibin, x, y)
                        weight_X_tgrMC.SetPointError (ibin, exlow, exhigh, eylow, eyhigh)
                    
                    #
                    # create the weighted data over MC distribution
                    #
                    weight_X_tgrDataOverMC = weight_X_tgrData.Clone("tgrDataOverMCweighted")
                    last = weight_X_thsBackground.GetStack().Last()
                    for ibin in range( nbinY ) :
                      x = weight_X_tgrDataOverMC.GetX()[ibin]
                      y = self.Ratio(weight_X_tgrData.GetY()[ibin] , last.GetBinContent(ibin+1) )

                      number_of_bin = ibin + sliceX * nbinY
                      if self._invertXY :
                        number_of_bin = ibin*nbinX + sliceX

                      exlow  = tgrData_evx[number_of_bin]
                      exhigh = tgrData_evx[number_of_bin]
                      eylow  = self.Ratio(weight_X_tgrData.GetErrorYlow(ibin),  last.GetBinContent(ibin+1) )
                      eyhigh = self.Ratio(weight_X_tgrData.GetErrorYhigh(ibin), last.GetBinContent(ibin+1) )                    
                      
                      weight_X_tgrDataOverMC.SetPoint      (ibin, x, y)
                      weight_X_tgrDataOverMC.SetPointError (ibin, exlow, exhigh, eylow, eyhigh)

                      #print " Ratio:: ibin,x,y = ", ibin, ", ", x, ", ", y, ", ", eylow, ", ", eyhigh, " <-- ", weight_X_tgrData.GetY()[ibin], " / ",  last.GetBinContent(ibin+1) 


                    #
                    # create the weighted data minus MC distribution
                    #
                    weight_X_tgrDataMinusMC = weight_X_tgrData.Clone("tgrDataMinusMCweighted")
                    last = weight_X_thsBackground.GetStack().Last()
                    for ibin in range( nbinY ) :
                      x = weight_X_tgrDataMinusMC.GetX()[ibin]                      
                      if self._showRelativeRatio :
                        y = self.Ratio ( self.Difference(weight_X_tgrData.GetY()[ibin] , last.GetBinContent(ibin+1) ) , last.GetBinContent(ibin+1) )
                      else : 
                        # if show only "data - bkg", subtract "data - (bkg+sig) + sig "
                        if self._showDataMinusBkgOnly :
                          y =  self.Difference(weight_X_tgrData.GetY()[ibin] , last.GetBinContent(ibin+1) )   + weight_X_thsSignal.GetStack().Last().GetBinContent(ibin+1) 
                        else :
                          y = self.Difference(weight_X_tgrData.GetY()[ibin] , last.GetBinContent(ibin+1) )

                      number_of_bin = ibin + sliceX * nbinY
                      if self._invertXY :
                        number_of_bin = ibin*nbinX + sliceX

                      exlow  = tgrData_evx[number_of_bin]
                      exhigh = tgrData_evx[number_of_bin]

                      if self._showRelativeRatio :
                        eylow  = self.Ratio(weight_X_tgrData.GetErrorYlow(ibin),  last.GetBinContent(ibin+1) )
                        eyhigh = self.Ratio(weight_X_tgrData.GetErrorYhigh(ibin), last.GetBinContent(ibin+1) )                    
                      else :
                        eylow  = weight_X_tgrData.GetErrorYlow(ibin) 
                        eyhigh = weight_X_tgrData.GetErrorYhigh(ibin)                  
                      
                      weight_X_tgrDataMinusMC.SetPoint      (ibin, x, y)
                      weight_X_tgrDataMinusMC.SetPointError (ibin, exlow, exhigh, eylow, eyhigh)


            
                    #
                    # create the weighted MC over MC distribution
                    #
                    weight_X_tgrMCOverMC = weight_X_tgrData.Clone("tgrMCOverMCweighted")
                    last = weight_X_thsBackground.GetStack().Last()
                    for ibin in range( nbinY ) :
                      x = weight_X_tgrMCOverMC.GetX()[ibin]
                      y = 1 

                      number_of_bin = ibin + sliceX * nbinY
                      if self._invertXY :
                        number_of_bin = ibin*nbinX + sliceX

                      exlow  = tgrData_evx[number_of_bin]
                      exhigh = tgrData_evx[number_of_bin]
                      eylow  = self.Ratio(weight_X_tgrMC.GetErrorYlow(ibin),  last.GetBinContent(ibin+1) )
                      eyhigh = self.Ratio(weight_X_tgrMC.GetErrorYhigh(ibin), last.GetBinContent(ibin+1) )                    
                      
                      weight_X_tgrMCOverMC.SetPoint      (ibin, x, y)
                      weight_X_tgrMCOverMC.SetPointError (ibin, exlow, exhigh, eylow, eyhigh)

           
                    #
                    # create the weighted MC over MC distribution
                    #
                    weight_X_tgrMCMinusMC = weight_X_tgrData.Clone("tgrMCMinusMCweighted")
                    last = weight_X_thsBackground.GetStack().Last()
                    for ibin in range( nbinY ) :
                      x = weight_X_tgrMCMinusMC.GetX()[ibin]
                      y = 0

                      number_of_bin = ibin + sliceX * nbinY
                      if self._invertXY :
                        number_of_bin = ibin*nbinX + sliceX

                      exlow  = tgrData_evx[number_of_bin]
                      exhigh = tgrData_evx[number_of_bin]
                      if self._showRelativeRatio :
                        eylow  = self.Ratio(weight_X_tgrMC.GetErrorYlow(ibin),  last.GetBinContent(ibin+1) )
                        eyhigh = self.Ratio(weight_X_tgrMC.GetErrorYhigh(ibin), last.GetBinContent(ibin+1) )                    
                      else :
                        eylow  = weight_X_tgrMC.GetErrorYlow(ibin) 
                        eyhigh = weight_X_tgrMC.GetErrorYhigh(ibin)             
                      
                      #print " DIFF::     eylow = ", eylow, " eyhigh = ", eyhigh, " y = ", y, " x = ", x 

                      weight_X_tgrMCMinusMC.SetPoint      (ibin, x, y)
                      weight_X_tgrMCMinusMC.SetPointError (ibin, exlow, exhigh, eylow, eyhigh)

           
                    #
                    # now plot
                    #
                    # - recalculate the maxY
                    #     _maxLinearScale --> 1.45 in the past
                    maxYused = self._maxLinearScale * self.GetMaximumIncludingErrors(last)

                    # recalculate min-max X due to weighting rolling
                    minXused = weight_X_tgrMCMinusMC.GetX()[0] - tgrData_evx[0]
                    maxXused = weight_X_tgrMCMinusMC.GetX()[nbinY-1] + tgrData_evx[nbinY-1]

                    weight_X_canvasRatioNameTemplate = 'cratio_weight_X_' + cutName + '_' + variableName
            
                    weight_X_tcanvasRatio.cd()
                    canvasPad1Name = 'weight_X_pad1_' + cutName + "_" + variableName
                    weight_X_pad1 = ROOT.TPad(canvasPad1Name,canvasPad1Name, 0, 1-0.72, 1, 1)
                    weight_X_pad1.SetTopMargin(0.098)
                    weight_X_pad1.SetBottomMargin(0.000) 
                    weight_X_pad1.Draw()
                    
                    weight_X_pad1.cd()
                    weight_X_canvasFrameDistroName = 'weight_X_frame_distro_' + cutName + "_" + variableName
                    weight_X_frameDistro = weight_X_pad1.DrawFrame(minXused, 0.0, maxXused, 1.0, weight_X_canvasFrameDistroName)
                    #weight_X_frameDistro = weight_X_pad1.DrawFrame(minXused, 0.0, maxXused, 1.0, weight_X_canvasFrameDistroName)
                    #weight_X_frameDistro = weight_X_pad1.DrawFrame(0.0, 0.0, nbinY, 1.0, weight_X_canvasFrameDistroName)
                    
                    # style from https://ghm.web.cern.ch/ghm/plots/MacroExample/myMacro.py
                    xAxisDistro = weight_X_frameDistro.GetXaxis()
                    xAxisDistro.SetNdivisions(6,5,0)
            
                    if 'xaxis' in variable.keys() : 
                      weight_X_frameDistro.GetXaxis().SetTitle(variable['xaxis'])
                    else :
                      weight_X_frameDistro.GetXaxis().SetTitle(variableName)
                    
                    weight_X_frameDistro.GetYaxis().SetTitle("S/B weighted Events")
                    if self._removeWeight == True :
                      weight_X_frameDistro.GetYaxis().SetTitle("Events")

                    weight_X_frameDistro.GetYaxis().SetRangeUser( min(0.001, minYused), maxYused )
            
                    if weight_X_thsBackground.GetNhists() != 0:
                      weight_X_thsBackground.Draw("hist same")
                       
                    if weight_X_thsSignal.GetNhists() != 0:
                      weight_X_thsSignal.Draw("hist same noclear")
                    
                    if (len(mynuisances.keys())!=0):
                      weight_X_tgrMC.SetLineColor(12)
                      weight_X_tgrMC.SetFillColor(12)
                      weight_X_tgrMC.SetFillStyle(3004)
                      weight_X_tgrMC.Draw("2")
                      #weight_X_tgrMC.Draw("P0")
                      #print "            -------------------------> here "
           
                    #     - then the DATA  
                    if weight_X_tgrData.GetN() != 0:
                      weight_X_tgrData.Draw("P0")
                      #print "            -------------------------> here data "
               
                    tlegend.Draw()
              
                    CMS_lumi.CMS_lumi(weight_X_tcanvasRatio, iPeriod, iPos)    
            
                    # draw back all the axes            
                    #weight_X_frameDistro.Draw("AXIS")
                    weight_X_pad1.RedrawAxis()
            
                        
                    weight_X_tcanvasRatio.cd()
                    canvasPad2Name = 'weight_X_weight_X_pad2_' + cutName + "_" + variableName
                    weight_X_pad2 = ROOT.TPad(canvasPad2Name,canvasPad2Name,0,0,1,1-0.72)
                    weight_X_pad2.SetTopMargin(0.000)
                    weight_X_pad2.SetBottomMargin(0.392)
                    weight_X_pad2.Draw()
                    #weight_X_pad2.cd().SetGrid()
                    weight_X_pad2.cd()
                    
                    weight_X_canvasFrameRatioName = 'weight_X_frame_ratio_' + cutName + "_" + variableName
                    #weight_X_frameRatio = weight_X_pad2.DrawFrame(minXused, 0.0, nbinY, 2.0, weight_X_canvasFrameRatioName)
                    weight_X_frameRatio = weight_X_pad2.DrawFrame(minXused, 0.0, maxXused, 2.0, weight_X_canvasFrameRatioName)
                    
                    #print "                minXused = " , minXused
                    #print "                maxXused = " , maxXused
                    #print "                nbinY = " , nbinY
                    
                    # style from https://ghm.web.cern.ch/ghm/plots/MacroExample/myMacro.py
                    xAxisDistro = weight_X_frameRatio.GetXaxis()
                    xAxisDistro.SetNdivisions(6,5,0)
            
                    if 'xaxis' in variable.keys() : 
                      weight_X_frameRatio.GetXaxis().SetTitle(variable['xaxis'])
                    else :
                      weight_X_frameRatio.GetXaxis().SetTitle(variableName)
                    weight_X_frameRatio.GetYaxis().SetTitle("Data/Expected")
                    weight_X_frameRatio.GetYaxis().SetRangeUser( 0.5, 1.5 )
                    self.Pad2TAxis(weight_X_frameRatio)
                    
                    if (len(mynuisances.keys())!=0):
                      weight_X_tgrMCOverMC.SetLineColor(12)
                      weight_X_tgrMCOverMC.SetFillColor(12)
                      weight_X_tgrMCOverMC.SetFillStyle(3004)
                      weight_X_tgrMCOverMC.Draw("2") 
                        
                    weight_X_tgrDataOverMC.Draw("P0")
 
 
                    oneLine2 = ROOT.TLine(weight_X_frameRatio.GetXaxis().GetXmin(), 1,  weight_X_frameRatio.GetXaxis().GetXmax(), 1);
                    oneLine2.SetLineStyle(3)
                    oneLine2.SetLineWidth(3)
                    oneLine2.Draw("same")
            
                    # draw back all the axes            
                    #weight_X_frameRatio.Draw("AXIS")
                    weight_X_pad2.RedrawAxis()
                    
                    self._saveCanvas(weight_X_tcanvasRatio, self._outputDirPlots + "/" + weight_X_canvasRatioNameTemplate + self._FigNamePF)

                    if 'root' in self._fileFormats:
                        text_file_html.write(weight_X_canvasRatioNameTemplate + ".root;\n")
                    
                    # save also all the TH1F separately for later combination
                    temp_file = ROOT.TFile (self._outputDirPlots + "/" + weight_X_canvasRatioNameTemplate + self._FigNamePF + ".root", "UPDATE")
                   
                    histo_global_normalization = ROOT.TH1F("histo_global_normalization", "", 1, 0, 1)
                    histo_global_normalization.Fill(0.5, global_normalization)
                    histo_global_normalization.Write()
                    
                    weight_X_tgrMCOverMC.Write()
                    weight_X_tgrDataOverMC.Write()
                    if (len(mynuisances.keys())!=0):
                      weight_X_tgrMC.Write("weight_X_tgrMC")
                    if weight_X_tgrData.GetN() != 0:
                      weight_X_tgrData.Write("weight_X_tgrData")
                    if weight_X_thsBackground.GetNhists() != 0:
                      weight_X_thsBackground.Write()
                    if weight_X_thsSignal.GetNhists() != 0:
                      weight_X_thsSignal.Write()
                      
                    for histo in weight_X_list_Data:
                       histo.Write()
                    for histo in weight_X_list_Background:
                       histo.Write()
                    for histo in weight_X_list_Signal:
                       histo.Write()
                    
                    temp_file.Close()
                    
                    
 
 
                    # log Y axis
                    if self._plotLog:
                        weight_X_frameDistro.GetYaxis().SetRangeUser( min(0.001, maxYused/1000), 10 * maxYused )
                        weight_X_pad1.SetLogy(True)
                        self._saveCanvas(weight_X_tcanvasRatio, self._outputDirPlots + "/log_" + weight_X_canvasRatioNameTemplate, imageOnly=True)
                        weight_X_pad1.SetLogy(False)


 
                    #
                    # Now plot difference 
                    #
                    weight_X_pad2.cd()
                    
                    if self._showRelativeRatio :
                      weight_X_frameRatio = weight_X_pad2.DrawFrame(minXused, -1.0, maxXused, 1.0, weight_X_canvasFrameRatioName)
                    else :
                      weight_X_frameRatio = weight_X_pad2.DrawFrame(minXused, int( ROOT.TMath.MinElement(weight_X_tgrDataMinusMC.GetN(),weight_X_tgrDataMinusMC.GetY())  - 2 ), maxXused, int ( ROOT.TMath.MaxElement(weight_X_tgrDataMinusMC.GetN(),weight_X_tgrDataMinusMC.GetY())  + 2 ), weight_X_canvasFrameRatioName)
                      
                    # style from https://ghm.web.cern.ch/ghm/plots/MacroExample/myMacro.py
                    xAxisDistro = weight_X_frameRatio.GetXaxis()
                    xAxisDistro.SetNdivisions(6,5,0)

                    if 'xaxis' in variable.keys() : 
                      weight_X_frameRatio.GetXaxis().SetTitle(variable['xaxis'])
                    else :
                      weight_X_frameRatio.GetXaxis().SetTitle(variableName)

                    if self._showRelativeRatio :
                      weight_X_frameRatio.GetYaxis().SetRangeUser(  -1.0 ,  1.0 )
                      weight_X_frameRatio.GetYaxis().SetTitle("#frac{Data - Expected}{Expected}")
                    else :
                      weight_X_frameRatio.GetYaxis().SetRangeUser(  int( ROOT.TMath.MinElement(weight_X_tgrDataMinusMC.GetN(),weight_X_tgrDataMinusMC.GetY())  - 2 ),  int ( ROOT.TMath.MaxElement(weight_X_tgrDataMinusMC.GetN(),weight_X_tgrDataMinusMC.GetY())  + 2 ) )
                      weight_X_frameRatio.GetYaxis().SetTitle("Data - Expected")


                    self.Pad2TAxis(weight_X_frameRatio)

                    if (len(mynuisances.keys())!=0):
                      weight_X_tgrMCMinusMC.SetLineColor(12)
                      weight_X_tgrMCMinusMC.SetFillColor(12)
                      weight_X_tgrMCMinusMC.SetFillStyle(3004)
                      weight_X_tgrMCMinusMC.Draw("2") 
                        
                    weight_X_tgrDataMinusMC.Draw("P0")
                      
                    #print " BINS = " , weight_X_tgrDataMinusMC.GetN()

                    oneLine2 = ROOT.TLine(weight_X_frameRatio.GetXaxis().GetXmin(), 0,  weight_X_frameRatio.GetXaxis().GetXmax(), 0);
                    oneLine2.SetLineStyle(3)
                    oneLine2.SetLineWidth(3)
                    oneLine2.Draw("same")

                    weight_X_pad2.RedrawAxis()

                    if self._showRelativeRatio :
                      weight_X_canvasDifferenceNameTemplate = 'cdifference_relative_weight_X_' + cutName + '_' + variableName
                    else :
                      weight_X_canvasDifferenceNameTemplate = 'cdifference_weight_X_' + cutName + '_' + variableName

                    self._saveCanvas(weight_X_tcanvasRatio, self._outputDirPlots + "/" + weight_X_canvasDifferenceNameTemplate)

                    if 'root' in self._fileFormats:
                      text_file_html.write(weight_X_canvasDifferenceNameTemplate + ".root;\n")
 

            #
            # This is performed at the end because it will change the "FillStyle" of the histograms
            # and you don't want to change it in the previous plots!
            # All histograms will become "transparent" as far as fill style is concerned
            #

            if self._plotNormalizedDistributions :
              # ~~~~~~~~~~~~~~~~~~~~
              # plot signal vs background normalized
              tcanvasSigVsBkg.cd()
  
              frameNorm = ROOT.TH1F
              frameNorm = tcanvasSigVsBkg.DrawFrame(minXused, 0.0, maxXused, 1.0)
  
              frameNorm.GetYaxis().SetRangeUser( 0, 1.5 )
              # setup axis names
              if 'xaxis' in variable.keys() : 
                frameNorm.GetXaxis().SetTitle(variable['xaxis'])
              tcanvasSigVsBkg.RedrawAxis()
  
              maxY_normalized=0.0

              for hentry in thsBackground_grouped.GetHists():
                num_bins = hentry.GetNbinsX()
                if hentry.Integral() > 0.:
                  y_normalized = hentry.GetBinContent(hentry.GetMaximumBin())/hentry.Integral()
                  if y_normalized > maxY_normalized:
                    maxY_normalized = y_normalized

                for ibin in range( num_bins ) :
                  hentry.SetBinError(ibin+1, 0.000001)

                hentry.SetFillStyle(0)
                hentry.SetLineWidth(3)
                hentry.DrawNormalized("hist,same")
                  
              for hentry in thsSignal_grouped.GetHists():
                num_bins = hentry.GetNbinsX()
                if hentry.Integral() > 0.:
                  y_normalized = hentry.GetBinContent(hentry.GetMaximumBin())/hentry.Integral()
                  if y_normalized > maxY_normalized:
                    maxY_normalized = y_normalized

                for ibin in range( num_bins ) :
                  hentry.SetBinError(ibin+1, 0.000001)

                hentry.SetFillStyle(0)
                hentry.SetLineWidth(3)
                hentry.DrawNormalized("hist,same")

              # ~~~~~~~~~~~~~~~~~~~~
              # include data only if required

              if self._plotNormalizedIncludeData : 
                for sampleName, plotdef in plot.iteritems():
                  if plotdef['isData'] == 1 :
                    histos[sampleName].DrawNormalized("p, same")

              frameNorm.GetYaxis().SetRangeUser(0, 1.8*maxY_normalized)

              tlegend.Draw()
              self._saveCanvas(tcanvasSigVsBkg, self._outputDirPlots + "/" + 'cSigVsBkg_' + cutName + "_" + variableName + self._FigNamePF, imageOnly=True)
         
 
 
            if self._plotNormalizedDistributionsTHstack :
              # ~~~~~~~~~~~~~~~~~~~~
              #
              # Plot signal vs background normalized
              # All the backgrounds or signals will be shown as stacked
              # All contributions will be shown as well as in the normal stack distribution
              # keeping though the integral of background and signal set to 1
              #
              
              tcanvasSigVsBkgTHstack.cd()
  
              frameNormTHstack = ROOT.TH1F
              frameNormTHstack = tcanvasSigVsBkgTHstack.DrawFrame(minXused, 0.0, maxXused, 1.0)
  
              frameNormTHstack.GetYaxis().SetRangeUser( 0, 1.5 )
              # setup axis names
              if 'xaxis' in variable.keys() : 
                frameNormTHstack.GetXaxis().SetTitle(variable['xaxis'])
              tcanvasSigVsBkgTHstack.RedrawAxis()
  
              maxY_normalized=0.0

              h_sum_of_backgrounds = thsBackground_grouped.GetStack().Last() 
              h_sum_of_signals = thsSignal_grouped.GetStack().Last() 
              
              normalization_factor_background = 1. / h_sum_of_backgrounds.Integral()
              normalization_factor_signal = 1. / h_sum_of_signals.Integral()

              if h_sum_of_backgrounds.Integral() > 0.:
                maxY_normalized = h_sum_of_backgrounds.GetBinContent(h_sum_of_backgrounds.GetMaximumBin())/h_sum_of_backgrounds.Integral()
              if h_sum_of_signals.Integral() > 0.:
                temp_maxY_normalized = h_sum_of_signals.GetBinContent(h_sum_of_signals.GetMaximumBin())/h_sum_of_signals.Integral()
                if (temp_maxY_normalized > maxY_normalized) :
                  maxY_normalized = temp_maxY_normalized
                
              for hentry in thsBackground_grouped.GetHists():  
                if hentry not in thsSignal_grouped.GetHists() :   # since signal is part of the "background" for plotting reason
                  num_bins = hentry.GetNbinsX()
                  for ibin in range( num_bins ) :
                    hentry.SetBinError(ibin+1, 0.000001)
                  hentry.SetFillStyle(0)
                  hentry.SetLineWidth(3)
                  hentry.Scale(normalization_factor_background)
                  thsBackground_grouped_normalized.Add(hentry)

              for hentry in thsSignal_grouped.GetHists():               
                num_bins = hentry.GetNbinsX()
                for ibin in range( num_bins ) :
                  hentry.SetBinError(ibin+1, 0.000001)
                hentry.SetFillStyle(0)
                hentry.SetLineWidth(3)
                hentry.Scale(normalization_factor_signal)
                thsSignal_grouped_normalized.Add(hentry)

              thsSignal_grouped_normalized.Draw("hist same noclear")
              thsBackground_grouped_normalized.Draw("hist same noclear")

              frameNormTHstack.GetYaxis().SetRangeUser(0, 1.8*maxY_normalized)

              tlegend.Draw()
              self._saveCanvas(tcanvasSigVsBkgTHstack, self._outputDirPlots + "/" + 'ccTHstackSigVsBkg_' + cutName + "_" + variableName + self._FigNamePF, imageOnly=True)
         

            # some cleaning 
            
            #print " cleaning ..."
            #thsData.Delete()
            #print " cleaning ..."
            #thsSignal.Delete()
            #print " cleaning ..."
            #thsBackground.Delete()
            
            #print " cleaning ..."
            #thsSignal_grouped.Delete()    
            #print " cleaning ..."
            #thsBackground_grouped.Delete()
            
            print " >> end:", variableName
            
          print " >> all end"

        print " >> all but really all "
        
        

        #
        # close plotter.html
        #
        text_file_html.write(" \"></div>                                 \"\n")
        text_file_html.close()
        
        
        #sys.exit(0)
	#quit()
	#raise SystemExit()
        os._exit(0)
	#exit()

        # ... or it will remain hanging forever ...
        


   # _____________________________________________________________________________
   # --- squared sum
    def Pad2TAxis(self, hist):
         xaxis = hist.GetXaxis()
         xaxis.SetLabelFont ( 42)
         xaxis.SetLabelOffset( 0.025)
         xaxis.SetLabelSize ( 0.1)
         xaxis.SetNdivisions ( 505)
         xaxis.SetTitleFont ( 42)
         xaxis.SetTitleOffset( 1.35)   
         xaxis.SetTitleSize ( 0.11)
       
         yaxis = hist.GetYaxis()
         yaxis.CenterTitle ( )
         yaxis.SetLabelFont ( 42)
         yaxis.SetLabelOffset( 0.02)
         yaxis.SetLabelSize ( 0.1)
         yaxis.SetNdivisions ( 505)
         yaxis.SetTitleFont ( 42)
         yaxis.SetTitleOffset( .6)
         yaxis.SetTitleSize ( 0.11)
 
 
 
   # _____________________________________________________________________________
   # --- squared sum
    def SumQ(self, A, B):
       return math.sqrt(A*A + B*B)

   # _____________________________________________________________________________
   # --- Ratio: if denominator is zero, then put 0!
    def Ratio(self, A, B):
       if B == 0:
         #print "divide by 0"
         return 0.
       else :
         return A / B
 
   # _____________________________________________________________________________
   # --- Difference
    def Difference(self, A, B):
       return A - B
 


   # _____________________________________________________________________________
   # --- poissonian error bayesian 1sigma band
   #                                      1/0   1/0
    def GetPoissError(self, numberEvents, down, up):
       alpha = (1-0.6827)
       L = 0
       if numberEvents!=0 : 
         L = ROOT.Math.gamma_quantile (alpha/2,numberEvents,1.)
       U = 0
       if numberEvents==0 :
         #
         # Poisson error agreed in the CMS statistics committee
         # see: https://hypernews.cern.ch/HyperNews/CMS/get/statistics/263.html
         # and https://hypernews.cern.ch/HyperNews/CMS/get/HIG-16-042/32/1/1/1/1/1.html
         # and https://twiki.cern.ch/twiki/bin/viewauth/CMS/PoissonErrorBars
         # to avoid flip-flop.
         # The commented version would have created 1.147 for 0 observed events
         # while now we get 1.84 in the case of 0 observed events
         #
         U = ROOT.Math.gamma_quantile_c (alpha/2,numberEvents+1,1.) 
         #U = ROOT.Math.gamma_quantile_c (alpha,numberEvents+1,1.) 
         #print "u = ", U
       else :
         U = ROOT.Math.gamma_quantile_c (alpha/2,numberEvents+1,1.)
         
       # the error
       L = numberEvents - L
       if numberEvents > 0 :
         U = U - numberEvents
       #else :
         #U = 1.14 # --> bayesian interval Poisson with 0 events observed
         #1.14790758039 from 10 lines above
         
       if up and not down :
         return U
       if down and not up :
         return L
       if up and down :
         return (L,U)
                  
   # _____________________________________________________________________________
    def GetMaximumIncludingErrors(self, histo):
        maxWithErrors = 0.
        for iBin in range(1, histo.GetNbinsX()+1):
          binHeight = histo.GetBinContent (iBin) + histo.GetBinError (iBin)
          if binHeight > maxWithErrors :
            maxWithErrors = binHeight
      
        return maxWithErrors;

   # _____________________________________________________________________________
    def GetMinimum(self, histo):
        minimum = -1.
        for iBin in range(1, histo.GetNbinsX()+1):
          binHeight = histo.GetBinContent (iBin)
          if binHeight < minimum or minimum<0:
            minimum = binHeight
      
        return minimum;
 
 
    # _____________________________________________________________________________
    def defineStyle(self):

        print "=================="
        import LatinoAnalysis.ShapeAnalysis.tdrStyle as tdrStyle
        tdrStyle.setTDRStyle()
        
        ROOT.TGaxis.SetExponentOffset(-0.08, 0.00,"y")

        
   # _____________________________________________________________________________
   # --- fix binning
   #
    def FixBins(self, histo, reference_x, reference_x_err):
        
        
        #
        # variable bin width
        #

        nbins = len (reference_x)
        #print " nbins = ", nbins
        
        binning = [ reference_x[ibin]-reference_x_err[ibin]  for ibin in range (0, nbins) ]  
        #binning = [ reference_histo.GetXaxis().GetBinLowEdge(ibin) for ibin in reference_histo.GetNbinsX()+1 ]      
        binning.append (reference_x[nbins-1]+reference_x_err[nbins-1])
        #print " >>>       histo.GetName() ::", histo.GetName(), " ::> " , binning

        hnew = ROOT.TH1F("new_" + histo.GetName(),"", len(binning)-1, array('d', binning ))
        for ibin in range (0, nbins+1) :
          y = histo.GetBinContent(ibin)
          x = histo.GetXaxis().GetBinCenter(ibin)
          hnew.SetBinContent(ibin,y)
        
        hnew.SetFillColor(histo.GetFillColor())
        hnew.SetLineColor(histo.GetLineColor())
        hnew.SetFillStyle(histo.GetFillStyle())
        
        return hnew
      
    def _saveCanvas(self, tcanvas, nameBase, imageOnly=False):
        if 'png' in self._fileFormats:
            tcanvas.SaveAs(nameBase + ".png")
        if 'pdf' in self._fileFormats:
            tcanvas.SaveAs(nameBase + ".pdf")
        if 'eps' in self._fileFormats:
            tcanvas.SaveAs(nameBase + ".eps")

        if not imageOnly:
            if 'root' in self._fileFormats:
                tcanvas.SaveAs(nameBase + ".root")
            if 'C' in self._fileFormats:
                tcanvas.SaveAs(nameBase + ".C")

    def _getColor(self, color):
      if type(color) == int:
        return color
      elif type(color) == tuple:
        # RGB
        return ROOT.TColor.GetColor(*color)
      elif type(color) == str:
        # hex string
        return ROOT.TColor.GetColor(color)

