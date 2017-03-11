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

#import os.path



# ----------------------------------------------------- ShapeFactory --------------------------------------

class ShapeFactory:
    _logger = logging.getLogger('ShapeFactory')
 
    # _____________________________________________________________________________
    def __init__(self):

        variables = {}
        self._variables = variables

        cuts = {}
        self._cuts = cuts

        samples = OrderedDict()
        self._samples = samples

        outputDirPlots = {}
        self._outputDirPlots = outputDirPlots
        
        self._showIntegralLegend = 1
        # 0 is no

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
        list_thsSignalSup_grouped     = {}
        list_thsBackground_grouped = {}

        list_tcanvas               = {}
        list_tcanvasRatio          = {}
        list_weight_X_tcanvasRatio = {}
        list_tcanvasSigVsBkg       = {}

        generalCounter = 0

        fileIn = ROOT.TFile(inputFile, "READ")
        #---- save one TCanvas for every cut and every variable
        for cutName in self._cuts :
          print "cut = ", cutName, " :: ", cuts[cutName]
          for variableName, variable in self._variables.iteritems():
            print "variableName = ", variableName
  
            tcanvas            = ROOT.TCanvas( "cc" + cutName + "_" + variableName,      "cc"     , 800, 600 )
            tcanvasRatio       = ROOT.TCanvas( "ccRatio" + cutName + "_" + variableName, "ccRatio", 800, 800 )
            weight_X_tcanvasRatio = ROOT.TCanvas( "weight_X_tcanvasRatio" + cutName + "_" + variableName, "weight_X_tcanvasRatio", 800, 800 )
            if self._plotNormalizedDistributions :
              tcanvasSigVsBkg    = ROOT.TCanvas( "ccSigVsBkg" + cutName + "_" + variableName,      "cc"     , 800, 600 )
 
            list_tcanvas                 [generalCounter] = tcanvas
            list_tcanvasRatio            [generalCounter] = tcanvasRatio
            list_weight_X_tcanvasRatio   [generalCounter] = weight_X_tcanvasRatio
            if self._plotNormalizedDistributions :
              list_tcanvasSigVsBkg         [generalCounter] = tcanvasSigVsBkg



            histos = {}
            histos_grouped = {}
            
            #print "here ..."
           
            canvasNameTemplateRatio = 'ccRatio_' + cutName + "_" + variableName
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

            #print " ... how is this still a thing ..."

            #these vectors are needed for nuisances accounting
            nuisances_vy_up     = {}
            #print " ... one "
            nuisances_vy_do     = {}
            #print " ... two"
            tgrMC_vy            = array('f')
 
            #print 'before thstack ...'
            #print 'really before thstack ...'


            #thsData       = ROOT.THStack ("thsData",      "thsData")
            #thsSignal     = ROOT.THStack ("thsSignal",    "thsSignal")
            #thsBackground = ROOT.THStack ("thsBackground","thsBackground")
    
            #thsSignal_grouped     = ROOT.THStack ("thsSignal_grouped",    "thsSignal_grouped")
            #thsBackground_grouped = ROOT.THStack ("thsBackground_grouped","thsBackground_grouped")
    
 
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
            generalCounter += 1
            
            #print '... after thstack ...'

            sigSupList    = []
            sigSupList_grouped    = []
            # list of additional histograms to be used in the ratio plot
            sigForAdditionalRatioList    = {}

            # enhanced list of nuisances, including bin-by-bin 
            mynuisances = {}

            nexpected = 0

            for sampleName, sample in self._samples.iteritems():
              shapeName = cutName+"/"+variableName+'/histo_' + sampleName
              print '     -> shapeName = ', shapeName,
              histo = fileIn.Get(shapeName)
              print ' --> ', histo
              histos[sampleName] = histo.Clone('new_histo_' + sampleName + '_' + cutName + '_' + variableName)                      
              
              #print "     -> sampleName = ", sampleName, " --> ", histos[sampleName].GetTitle(), " --> ", histos[sampleName].GetName(), " --> ", histos[sampleName].GetNbinsX()
              #for iBinAmassiro in range(1, histos[sampleName].GetNbinsX()+1):
                 #print " i = ", iBinAmassiro, " [" , sampleName, " ==> ", histos[sampleName].GetBinContent(iBinAmassiro)

              # allow arbitrary scaling in MC (and DATA??), if needed
              # for example to "see" a signal
              if 'scale' in plot[sampleName].keys() : 
                histos[sampleName].Scale(plot[sampleName]['scale'])
                #print " >> scale ", sampleName, " to ", plot[sampleName]['scale']

              # apply cut dependent scale factors
              # for example when plotting different phase spaces
              if 'cuts' in plot[sampleName].keys() : 
                if cutName in plot[sampleName]['cuts'] :
                  histos[sampleName].Scale( float( plot[sampleName]['cuts'][cutName] ) )
     

              if plot[sampleName]['isData'] == 1 :  
                thsData.Add(histos[sampleName])


              # data style
              if plot[sampleName]['isData'] == 1 :
                #print ' plot[', sampleName, '][color] = ' , plot[sampleName]['color']
                histos[sampleName].SetMarkerColor(plot[sampleName]['color'])
                histos[sampleName].SetMarkerSize(1)
                histos[sampleName].SetMarkerStyle(20)
                histos[sampleName].SetLineColor(plot[sampleName]['color'])
                
                # blind data
                if 'isBlind' in plot[sampleName].keys() :
                  if plot[sampleName]['isBlind'] == 1 :
                    for iBin in range(1, histos[sampleName].GetNbinsX()+1):
                      histos[sampleName].SetBinContent(iBin, 0)
                      histos[sampleName].SetBinError  (iBin, 0)
                    #but_how_is_it_possible = histos[sampleName].Integral(1,histos[sampleName].GetNbinsX()+1)
                    #print " what is it = ", sampleName
                    #print " but_how_is_it_possible [", sampleName, "] = ", but_how_is_it_possible
                    #but_how_is_it_possible_low_high = histos[sampleName].Integral(-1, -1)
                    #print " but_how_is_it_possible_low_high [", sampleName, "] = ", but_how_is_it_possible_low_high
                    histos[sampleName].Reset()
                    #but_how_is_it_possible_low_high_reset = histos[sampleName].Integral(-1, -1)
                    #print " but_how_is_it_possible_low_high_reset [", sampleName, "] = ", but_how_is_it_possible_low_high_reset
                    
                      
                
                #thsData.Add(histos[sampleName])

                # first time fill vectors X axis
                if len(tgrData_vx) == 0 :
                  dataColor = histos[sampleName].GetMarkerColor()
                  for iBin in range(1, histos[sampleName].GetNbinsX()+1):
                    tgrData_vx.append(  histos[sampleName].GetBinCenter (iBin))
                    tgrData_evx.append( histos[sampleName].GetBinWidth (iBin) / 2.)                  
                    tgrData_vy.append(  histos[sampleName].GetBinContent (iBin))
                    #print " plot[", sampleName, "].keys() = ", plot[sampleName].keys()
                    if ('isSignal' not in plot[sampleName].keys() or plot[sampleName]['isSignal'] != 3) and not ('isBlind' in plot[sampleName].keys() and plot[sampleName]['isBlind'] == 1) :
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
                    if 'isSignal' not in plot[sampleName].keys() or plot[sampleName]['isSignal'] == 3 :
                      tgrData_evy_up[iBin-1] = SumQ ( tgrData_evy_up[iBin-1], self.GetPoissError(histos[sampleName].GetBinContent (iBin) , 0, 1) )
                      tgrData_evy_do[iBin-1] = SumQ ( tgrData_evy_do[iBin-1], self.GetPoissError(histos[sampleName].GetBinContent (iBin) , 1, 0) )
                    
                    

              # MC style
              if plot[sampleName]['isData'] == 0 :
                # only background "filled" histogram
                if plot[sampleName]['isSignal'] == 0:
                  #histos[sampleName].SetFillStyle(1001)
                  #histos[sampleName].SetFillColorAlpha(plot[sampleName]['color'], 0.5)
                  #histos[sampleName].SetFillColor(plot[sampleName]['color'])
                  #histos[sampleName].SetLineColor(plot[sampleName]['color']+1)
                  histos[sampleName].SetFillColor(plot[sampleName]['color'])
                  histos[sampleName].SetFillStyle(3001)
                else :
                  histos[sampleName].SetFillStyle(0)
                  histos[sampleName].SetLineWidth(2)
             
                histos[sampleName].SetLineColor(plot[sampleName]['color'])
                # scale to luminosity if MC
                #histos[sampleName].Scale(self._lumi)  ---> NO! They are already scaled to luminosity in mkShape!
                
                if plot[sampleName]['isSignal'] == 1 :
                  thsSignal.Add(histos[sampleName])
                elif plot[sampleName]['isSignal'] == 2 or plot[sampleName]['isSignal'] == 3 :
                  #print "SigSup histo: ", histos[sampleName]
                  sigSupList.append(histos[sampleName])
                  if plot[sampleName]['isSignal'] == 3 :
                    #print "sigForAdditionalRatio histo: ", histos[sampleName]
                    sigForAdditionalRatioList[sampleName] = histos[sampleName]
                else :
                  thsBackground.Add(histos[sampleName])
                  nexpected += histos[sampleName].Integral(-1,-1)
                  #print " adding to background: ", sampleName

                # handle 'stat' nuisance to create the bin-by-bin list of nuisances
                # "massage" the list of nuisances accordingly
                for nuisanceName, nuisance in nuisances.iteritems():         

                  if ('cuts' not in nuisance) or ( ('cuts' in nuisance) and (cutName in nuisance['cuts']) ) :   # run only if this nuisance will affect the phase space defined in "cut"
                    
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
                 
                # prepare the reference distribution
                #if len(tgrMC_vy) == 0:
                  #for iBin in range(1, histos[sampleName].GetNbinsX()+1):
                    #tgrMC_vy.append(0.)
                # fill the reference distribution, and add each "sample" that is not "signal"
                #if plot[sampleName]['isSignal'] == 0:
                  #for iBin in range(1, histos[sampleName].GetNbinsX()+1):
                    #tgrMC_vy[iBin-1] += histos[sampleName].GetBinContent (iBin)
                 
                for nuisanceName, nuisance in mynuisances.iteritems():
                  # is this nuisance to be considered for this background?
                  is_this_nuisance_to_be_considered = False
                  if 'samples' in nuisance.keys() :
                    for sampleNuisName, configurationNuis in nuisance['samples'].iteritems() :
                      if sampleNuisName == sampleName: # complain only if the nuisance was supposed to show up
                        is_this_nuisance_to_be_considered = True
                  elif 'all' in nuisance.keys() and nuisance ['all'] == 1 : # for all samples
                    is_this_nuisance_to_be_considered = True

                  #print " sampleName = ", sampleName, " nuisanceName = ", nuisanceName, " is_this_nuisance_to_be_considered = ", is_this_nuisance_to_be_considered
                  
                  histoUp = None
                  histoDown = None
 
                  if not ( ('cuts' not in nuisance) or ( ('cuts' in nuisance) and (cutName in nuisance['cuts']) ) ) :   # run only if this nuisance will affect the phase space defined in "cut"
                    is_this_nuisance_to_be_considered = False
 
                  if is_this_nuisance_to_be_considered :
                    shapeNameUp = cutName+"/"+variableName+'/histo_' + sampleName+"_"+nuisanceName+"Up"
                    #print "loading shape variation", shapeNameUp
                    histoUp = fileIn.Get(shapeNameUp)
                    shapeNameDown = cutName+"/"+variableName+'/histo_' + sampleName+"_"+nuisanceName+"Down"
                    #print "loading shape variation", shapeNameDown
                    histoDown = fileIn.Get(shapeNameDown)
                    if histoUp == None:
                      if 'all' in nuisance.keys() and nuisance ['all'] == 1 : # for all samples
                         if nuisance['type'] == 'lnN' :                             
                           # example:
                           #              'samples'  : {
                           #                   'WW' : '1.00',    
                           #                   'ggH': '1.23/0.97'
                           #                },                              
                           down_variation = 0.
                           up_variation = 0.
                           
                           if "/" in nuisance['value'] :
                             #print " nuisance['value'] = ", nuisance['value']
                             twovariations = nuisance['value'].split("/")
                             #print " twovariations = ", twovariations
                             down_variation = float(twovariations[0])
                             up_variation   = float(twovariations[1]) 
                           else :
                             down_variation = 2. - float(nuisance['value'])
                             up_variation   = float(nuisance['value']) 
                           
                           # don't use  histos[sampleName], or the second "scale" will fail!!!
                           histoUp   = histo.Clone(cutName+"_"+variableName+'_histo_' + sampleName+"_"+nuisanceName+"Up")
                           histoUp.Scale(up_variation)
                    
                      elif 'samples' in nuisance.keys():
                        for sampleNuisName, configurationNuis in nuisance['samples'].iteritems() :
                          if sampleNuisName == sampleName: # complain only if the nuisance was supposed to show up
                            if 'type' in nuisance.keys() :
                              if nuisance['type'] == 'lnN' :                             
                                # example:
                                #              'samples'  : {
                                #                   'WW' : '1.00',    
                                #                   'ggH': '1.23/0.97'
                                #                },                              
                                down_variation = 0.
                                up_variation = 0.

                                #print " configurationNuis samples = ", configurationNuis
                                
                                if "/" in configurationNuis :
                                  #print " configurationNuis samples = ", configurationNuis
                                  twovariations = configurationNuis.split("/")
                                  #print " twovariations = ", twovariations
                                  down_variation = float(twovariations[0])
                                  up_variation   = float(twovariations[1]) 
                                else :
                                  down_variation = 2. - float(configurationNuis)
                                  up_variation   = float(configurationNuis) 
                                
                                #print " histos[sampleName].GetBinContent(10) = ", histos[sampleName].GetBinContent(10)
                                # don't use  histos[sampleName], or the second "scale" will fail!!!
                                histoUp   = histo.Clone(cutName+"_"+variableName+'_histo_' + sampleName+"_"+nuisanceName+"Up")
                                histoUp.Scale(up_variation)
                                #print " histos[sampleName].GetBinContent(10) = ", histos[sampleName].GetBinContent(10)
                                
                                
                              #else :
                                #print "Warning! No", nuisanceName, " up variation for", sampleName, ' of kind lnN'
                            
                    if histoDown == None:
                      if 'all' in nuisance.keys() and nuisance ['all'] == 1 : # for all samples
                         if nuisance['type'] == 'lnN' :                             
                           # example:
                           #              'samples'  : {
                           #                   'WW' : '1.00',    
                           #                   'ggH': '1.23/0.97'
                           #                },                              
                           down_variation = 0.
                           up_variation = 0.
                           
                           if "/" in nuisance['value'] :
                             #print " nuisance['value'] down = ", nuisance['value']
                             twovariations = nuisance['value'].split("/")
                             down_variation = float(twovariations[0])
                             up_variation   = float(twovariations[1]) 
                           else :
                             down_variation = 2. - float(nuisance['value'])
                             up_variation   = float(nuisance['value']) 
                           
                           # don't use  histos[sampleName], or the second "scale" will fail!!!
                           histoDown   = histo.Clone(cutName+"_"+variableName+'_histo_' + sampleName+"_"+nuisanceName+"Down")
                           histoDown.Scale(down_variation)
                           
                      elif 'samples' in nuisance.keys():
                        for sampleNuisName, configurationNuis in nuisance['samples'].iteritems() :
                          if sampleNuisName == sampleName: # complain only if the nuisance was supposed to show up
                            if 'type' in nuisance.keys() :
                              if nuisance['type'] == 'lnN' :                             
                                # example:
                                #              'samples'  : {
                                #                   'WW' : '1.00',    
                                #                   'ggH': '1.23/0.97'
                                #                },
                                down_variation = 0.
                                up_variation = 0.
                                
                                if "/" in configurationNuis :
                                  #print " configurationNuis down samples = ", configurationNuis
                                  twovariations = configurationNuis.split("/")
                                  down_variation = float(twovariations[0])
                                  up_variation   = float(twovariations[1]) 
                                else :
                                  down_variation = 2. - float(configurationNuis)
                                  up_variation   = float(configurationNuis) 
                                
                                # don't use  histos[sampleName], or the second "scale" will fail!!!
                                histoDown = histo.Clone(cutName+"_"+variableName+'_histo_' + sampleName+"_"+nuisanceName+"Down")
                                histoDown.Scale(down_variation)
                              #else :
                                #print "Warning! No", nuisanceName, " down variation for", sampleName, ' of kind lnN'
                  
                  
                  if 'scale' in plot[sampleName].keys() : 
                    if histoDown != None:  
                      #print " histoDown integral = ", histoDown.Integral()
                      histoDown.Scale(plot[sampleName]['scale'])
                      #print " ---> plot[", sampleName, "]['scale'] = ", plot[sampleName]['scale']
                      #print " --> histoDown integral = ", histoDown.Integral()
                      
                    if histoUp != None:  
                      histoUp.Scale(plot[sampleName]['scale'])
                                 

                  # apply cut dependent scale factors
                  # for example when plotting different phase spaces
                  if 'cuts' in plot[sampleName].keys() : 
                    if cutName in plot[sampleName]['cuts'] :
                      if histoDown != None:  
                        #print " rescaling: ", sampleName, " - ", cutName, " = ", plot[sampleName]['cuts'][cutName]
                        histoDown.Scale( float(plot[sampleName]['cuts'][cutName]) )
                      if histoUp != None:  
                        histoUp.Scale( float(plot[sampleName]['cuts'][cutName]) )

                  
                  # now, even if not considered this nuisance, I need to add it, 
                  # so that in case is "empty" it will add the nominal value
                  # for this sample that is not affected by the nuisance
                  
                  if nuisanceName not in nuisances_vy_up.keys() or nuisanceName not in nuisances_vy_do.keys():  
                    nuisances_vy_up[nuisanceName] = array('f')
                    nuisances_vy_do[nuisanceName] = array('f')
                  if (len(nuisances_vy_up[nuisanceName]) == 0):
                    for iBin in range(1, histos[sampleName].GetNbinsX()+1):
                      nuisances_vy_up[nuisanceName].append(0.)
                  if (len(nuisances_vy_do[nuisanceName]) == 0):
                    for iBin in range(1, histos[sampleName].GetNbinsX()+1):
                      nuisances_vy_do[nuisanceName].append(0.)
                  # get the background sum
                  if plot[sampleName]['isSignal'] == 0:   # ---> add the signal too????? See ~ 20 lines below
                    #print "plot[", sampleName, "]['isSignal'] == ", plot[sampleName]['isSignal']
                    for iBin in range(1, histos[sampleName].GetNbinsX()+1):
                      if histoUp != None:
                        #print " nuisanceName[", iBin, "] = ", nuisanceName, " sampleName = ", sampleName, " histoUp.GetBinContent (", iBin, ") = ", histoUp.GetBinContent (iBin), \
                              #"while default was: ", histos[sampleName].GetBinContent (iBin)
                        nuisances_vy_up[nuisanceName][iBin-1] += histoUp.GetBinContent (iBin)
                      else:
                        # add the central sample 
                        nuisances_vy_up[nuisanceName][iBin-1] += histos[sampleName].GetBinContent (iBin)  
                      if histoDown != None:  
                        #print " nuisanceName[", iBin, "] = ", nuisanceName, " sampleName = ", sampleName, " histoDown.GetBinContent (", iBin, ") = ", histoDown.GetBinContent (iBin), \
                              #"while default was: ", histos[sampleName].GetBinContent (iBin)
                        nuisances_vy_do[nuisanceName][iBin-1] += histoDown.GetBinContent (iBin)
                      else:
                        # add the central sample 
                        nuisances_vy_do[nuisanceName][iBin-1] += histos[sampleName].GetBinContent (iBin)
            

              # create the group of histograms to plot
              # this has to be done after the scaling of the previous lines
              # andl also after all the rest, so that we inherit the style of the histograms
              for sampleNameGroup, sampleConfiguration in groupPlot.iteritems():
                for samples_to_group in sampleConfiguration['samples'] :
                  if samples_to_group == sampleName :
                    if sampleNameGroup in histos_grouped.keys() :
                      histos_grouped[sampleNameGroup].Add(histos[sampleName])
                    else :
                      histos_grouped[sampleNameGroup] = histos[sampleName].Clone('new_histo_group_' + sampleNameGroup + '_' + cutName + '_' + variableName)


            # set the colors for the groups of samples
            for sampleNameGroup, sampleConfiguration in groupPlot.iteritems():
              if sampleNameGroup in histos_grouped.keys() :
                histos_grouped[sampleNameGroup].SetLineColor(sampleConfiguration['color'])
                if sampleConfiguration['isSignal'] == 0:
                  #histos_grouped[sampleNameGroup].SetFillStyle(1001)
                  #histos_grouped[sampleNameGroup].SetFillColorAlpha(sampleConfiguration['color'], 0.5)
                  #histos_grouped[sampleNameGroup].SetFillColor(sampleConfiguration['color'])
                  #histos_grouped[sampleNameGroup].SetLineColor(sampleConfiguration['color']+1)
                  histos_grouped[sampleNameGroup].SetFillColor(sampleConfiguration['color'])
                  histos_grouped[sampleNameGroup].SetFillStyle(3001)
                else :
                  histos_grouped[sampleNameGroup].SetFillStyle(0)
                  histos_grouped[sampleNameGroup].SetLineWidth(2)
            
            # fill the reference distribution with the background only distribution
            # save the central values of the bkg sum for use for the nuisance band 
            #
            #print " tgrMC_vy = ", tgrMC_vy
            for iBin in range(1,thsBackground.GetStack().Last().GetNbinsX()+1):
              tgrMC_vy.append(thsBackground.GetStack().Last().GetBinContent(iBin))
            
                        
            #
            # and now  let's add the signal on top of the background stack 
            # It is important to do this after setting (without signal) tgrMC_vy
            #
            for sampleName, sample in self._samples.iteritems():
              # MC style
              if plot[sampleName]['isData'] == 0 :
                if plot[sampleName]['isSignal'] == 1 :
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

            nuisances_err_up = array('f')
            nuisances_err_do = array('f')
            for nuisanceName in mynuisances.keys():
              #print " nuisanceName = " , nuisanceName
              if len(nuisances_err_up) == 0 : 
                for iBin in range(len(tgrMC_vy)):
                  nuisances_err_up.append(0.)
                  nuisances_err_do.append(0.)
              # now we need to tell wthether the variation is actually up or down ans sum in quadrature those with the same sign 
              for iBin in range(len(tgrMC_vy)):
                #print "bin", iBin, " nuisances_vy_up[", nuisanceName, "][", iBin, "] = ", nuisances_vy_up[nuisanceName][iBin], " central = ", tgrMC_vy[iBin] , " --> " \
                     #" diff = ", nuisances_vy_up[nuisanceName][iBin] - tgrMC_vy[iBin],  \
                     #" new global error = ", nuisances_err_up[iBin]
                #print "bin", iBin, " nuisances_vy_do[", nuisanceName, "][", iBin, "] = ", nuisances_vy_do[nuisanceName][iBin], " central = ", tgrMC_vy[iBin] , " --> " \
                     #" diff = ", nuisances_vy_do[nuisanceName][iBin] - tgrMC_vy[iBin],  \
                     #" new global error = ", nuisances_err_do[iBin]
                
                if nuisances_vy_up[nuisanceName][iBin] - tgrMC_vy[iBin] > 0:
                  nuisances_err_up[iBin] = self.SumQ (nuisances_err_up[iBin], nuisances_vy_up[nuisanceName][iBin] - tgrMC_vy[iBin])
                  nuisances_err_do[iBin] = self.SumQ (nuisances_err_do[iBin], nuisances_vy_do[nuisanceName][iBin] - tgrMC_vy[iBin])
                else:
                  nuisances_err_up[iBin] = self.SumQ (nuisances_err_up[iBin], nuisances_vy_do[nuisanceName][iBin] - tgrMC_vy[iBin])
                  nuisances_err_do[iBin] = self.SumQ (nuisances_err_do[iBin], nuisances_vy_up[nuisanceName][iBin] - tgrMC_vy[iBin]) 

                #print "nuisances_err_up[", iBin, "] = ", nuisances_err_up[iBin], " --> ", \
                      #"nuisances_err_do[", iBin, "] = ", nuisances_err_do[iBin], " --> " 

              
            
            tgrData       = ROOT.TGraphAsymmErrors()
            for iBin in range(0, len(tgrData_vx)) : 
              tgrData.SetPoint     (iBin, tgrData_vx[iBin], tgrData_vy[iBin])
              tgrData.SetPointError(iBin, tgrData_evx[iBin], tgrData_evx[iBin], tgrData_evy_do[iBin], tgrData_evy_up[iBin])
            
            tgrData.SetMarkerColor(dataColor)
            tgrData.SetLineColor(dataColor)
            
            tgrDataOverMC = tgrData.Clone("tgrDataOverMC")
            for iBin in range(0, len(tgrData_vx)) : 
              tgrDataOverMC.SetPoint     (iBin, tgrData_vx[iBin], self.Ratio(tgrData_vy[iBin] , thsBackground.GetStack().Last().GetBinContent(iBin+1)) )
              tgrDataOverMC.SetPointError(iBin, tgrData_evx[iBin], tgrData_evx[iBin], self.Ratio(tgrData_evy_do[iBin], thsBackground.GetStack().Last().GetBinContent(iBin+1)) , self.Ratio(tgrData_evy_up[iBin], thsBackground.GetStack().Last().GetBinContent(iBin+1)) )
            
            if len(mynuisances.keys()) != 0:
              tgrMC = ROOT.TGraphAsymmErrors()  
              for iBin in range(0, len(tgrData_vx)) :
                tgrMC.SetPoint     (iBin, tgrData_vx[iBin], tgrMC_vy[iBin])
                tgrMC.SetPointError(iBin, tgrData_evx[iBin], tgrData_evx[iBin], nuisances_err_do[iBin], nuisances_err_up[iBin])
              
              tgrMCOverMC = tgrMC.Clone("tgrMCOverMC")  
              for iBin in range(0, len(tgrData_vx)) :
                tgrMCOverMC.SetPoint     (iBin, tgrData_vx[iBin], 1.)
                tgrMCOverMC.SetPointError(iBin, tgrData_evx[iBin], tgrData_evx[iBin], self.Ratio(nuisances_err_do[iBin], tgrMC_vy[iBin]), self.Ratio(nuisances_err_up[iBin], tgrMC_vy[iBin]))     
                
                         
            
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
              


            groupFlag = False
            #---- prepare the grouped histograms
            for sampleNameGroup, sampleConfiguration in groupPlot.iteritems():
              if sampleConfiguration['isSignal'] == 1 :
                  print "############################################################## isSignal 1", sampleNameGroup
                  thsSignal_grouped.Add(histos_grouped[sampleNameGroup])
              elif sampleConfiguration['isSignal'] == 2 :
                  print "############################################################## isSignal 2", sampleNameGroup
                  groupFlag = True
                  sigSupList_grouped.append(histos_grouped[sampleNameGroup])
              # the signal is added on top of the background
              # the signal has to be the last one in the dictionary!
              # make it sure in plot.py
              if groupFlag == False: thsBackground_grouped.Add(histos_grouped[sampleNameGroup])
            
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
            scaleToPlot = 2.5
            
            for sampleName, sample in self._samples.iteritems():
              if plot[sampleName]['isData'] == 1 :
                histos[sampleName].Draw("p")
                minXused = histos[sampleName].GetXaxis().GetBinLowEdge(1)
                maxXused = histos[sampleName].GetXaxis().GetBinUpEdge(histos[sampleName].GetNbinsX())
                maxY = self.GetMaximumIncludingErrors(histos[sampleName])
                histos[sampleName].SetMaximum(scaleToPlot * maxY)
                maxYused = scaleToPlot * maxY
                minYused = self.GetMinimum(histos[sampleName])
            
            if thsBackground.GetNhists() != 0:
              thsBackground.Draw("hist")
              maxY = thsBackground.GetMaximum ()
              minXused = thsBackground.GetXaxis().GetBinLowEdge(1)
              maxXused = thsBackground.GetXaxis().GetBinUpEdge(thsBackground.GetHistogram().GetNbinsX())
              if (scaleToPlot * maxY) > maxYused :
                maxYused = scaleToPlot * maxY
              minY = thsBackground.GetMinimum ()
              if (minY < minYused) :
                minYused = minY 

               
            if thsSignal.GetNhists() != 0:
              thsSignal.Draw("hist")
              maxY = thsSignal.GetMaximum ()
              minXused = thsSignal.GetXaxis().GetBinLowEdge(1)
              maxXused = thsSignal.GetXaxis().GetBinUpEdge(thsSignal.GetHistogram().GetNbinsX())
              if (scaleToPlot * maxY) > maxYused :
                maxYused = scaleToPlot * maxY
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
            else :
              frame.GetXaxis().SetTitle(variableName)
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
              for sampleName, sample in self._samples.iteritems():
                if plot[sampleName]['isData'] == 1 :
                  histos[sampleName].Draw("p same")

            #---- the Legend
            tlegend = ROOT.TLegend(0.2, 0.7, 0.8, 0.9)
            tlegend.SetFillColor(0)
            tlegend.SetLineColor(0)
            tlegend.SetShadowColor(0)
            reversedSamplesItems = self._samples.items()
            reversedSamplesItems.reverse()
            reversedSamples = OrderedDict(reversedSamplesItems)
            
            if len(groupPlot.keys()) == 0:
              for sampleName, sample in reversedSamples.iteritems():
                if plot[sampleName]['isData'] == 0 :
                  if 'nameHR' in plot[sampleName].keys() :
                    if plot[sampleName]['nameHR'] != '' :
                      if self._showIntegralLegend == 0 :
                        tlegend.AddEntry(histos[sampleName], plot[sampleName]['nameHR'], "F")
                      else :
                        nevents = histos[sampleName].Integral(1,histos[sampleName].GetNbinsX()+1)
                        tlegend.AddEntry(histos[sampleName], plot[sampleName]['nameHR'] + " [" +  str(round(nevents,1)) + "]", "F")
                  else :
                    if self._showIntegralLegend == 0 :
                      tlegend.AddEntry(histos[sampleName], sampleName, "F")
                    else :
                      nevents = histos[sampleName].Integral(1,histos[sampleName].GetNbinsX()+1)
                      tlegend.AddEntry(histos[sampleName], sampleName + " [" +  str(round(nevents,1)) + "]", "F")
               
              for sampleName, sample in reversedSamples.iteritems():
                if plot[sampleName]['isData'] == 1 :
                  if 'nameHR' in plot[sampleName].keys() :
                    if self._showIntegralLegend == 0 :
                      tlegend.AddEntry(histos[sampleName], plot[sampleName]['nameHR'], "EPL")
                    else :
                      nevents = histos[sampleName].Integral(1,histos[sampleName].GetNbinsX()+1)
                      tlegend.AddEntry(histos[sampleName], plot[sampleName]['nameHR'] + " [" +  str(round(nevents,1)) + "]", "EPL")
                  else :
                    if self._showIntegralLegend == 0 :
                      tlegend.AddEntry(histos[sampleName], sampleName, "EPL")
                    else :
                      nevents = histos[sampleName].Integral(1,histos[sampleName].GetNbinsX()+1)
                      tlegend.AddEntry(histos[sampleName], sampleName + " [" +  str(round(nevents,1)) + "]", "EPL")
            
            else :
              
              for sampleNameGroup, sampleConfiguration in groupPlot.iteritems():
                if self._showIntegralLegend == 0 :
                  tlegend.AddEntry(histos_grouped[sampleNameGroup], sampleConfiguration['nameHR'], "F")
                else :
                  nevents = histos_grouped[sampleNameGroup].Integral(1,histos_grouped[sampleNameGroup].GetNbinsX()+1)
                  tlegend.AddEntry(histos_grouped[sampleNameGroup], sampleConfiguration['nameHR'] + " [" +  str(round(nevents,1)) + "]" , "F")
               
              for sampleName, sample in reversedSamples.iteritems():
                if plot[sampleName]['isData'] == 1 :
                  if 'nameHR' in plot[sampleName].keys() :
                    if self._showIntegralLegend == 0 :
                      tlegend.AddEntry(histos[sampleName], plot[sampleName]['nameHR'], "EPL")
                    else :
                      nevents = histos[sampleName].Integral(1,histos[sampleName].GetNbinsX()+1)
                      print " nevents [", sampleName, "] = ", nevents
                      tlegend.AddEntry(histos[sampleName], plot[sampleName]['nameHR'] + " [" +  str(round(nevents,1)) + "]", "EPL")
                  else :
                    if self._showIntegralLegend == 0 :
                      tlegend.AddEntry(histos[sampleName], sampleName , "EPL")
                    else :
                      nevents = histos[sampleName].Integral(1,histos[sampleName].GetNbinsX()+1)
                      print " nevents [", sampleName, "] = ", nevents
                      tlegend.AddEntry(histos[sampleName], sampleName + " [" +  str(round(nevents,1)) + "]", "EPL")
              
              
                  
            if len(mynuisances.keys()) != 0:
                if self._showIntegralLegend == 0 :
                    tlegend.AddEntry(tgrMC, "Systematics", "F")
                else :
                    print " nexpected  = ", nexpected
                    tlegend.AddEntry(tgrMC, "Systematics [" + str(round(nexpected,1)) + "]", "F")
             
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
            
            tcanvas.SaveAs(self._outputDirPlots + "/" + canvasNameTemplate + ".png")
            tcanvas.SaveAs(self._outputDirPlots + "/" + canvasNameTemplate + ".root")
            tcanvas.SaveAs(self._outputDirPlots + "/" + canvasNameTemplate + ".C")
            #tcanvas.SaveAs(self._outputDirPlots + "/" + canvasNameTemplate + ".eps")
            #tcanvas.SaveAs(self._outputDirPlots + "/" + canvasNameTemplate + ".pdf")
             
            # log Y axis
            frame.GetYaxis().SetRangeUser( max( self._minLogC, minYused), self._maxLogC * maxYused )
            tcanvas.SetLogy()
            tcanvas.SaveAs(self._outputDirPlots + "/log_" + canvasNameTemplate + ".png")
            #tcanvas.SaveAs(self._outputDirPlots + "/log_" + canvasNameTemplate + ".eps")
            #tcanvas.SaveAs(self._outputDirPlots + "/log_" + canvasNameTemplate + ".pdf")
            tcanvas.SetLogy(0)


            if self._plotNormalizedDistributions :
              # ~~~~~~~~~~~~~~~~~~~~
              # plot signal vs background normalized
              tcanvasSigVsBkg.cd()
  
              frameNorm = ROOT.TH1F
              frameNorm = tcanvasSigVsBkg.DrawFrame(minXused, 0.0, maxXused, 1.0)
  
              frameNorm.GetYaxis().SetRangeUser( 0, 2 )
              # setup axis names
              if 'xaxis' in variable.keys() : 
                frameNorm.GetXaxis().SetTitle(variable['xaxis'])
              tcanvasSigVsBkg.RedrawAxis()
  
  
              for ihisto in range(thsBackground_grouped.GetNhists()) :
                num_bins = (thsBackground_grouped.GetHists().At(ihisto)).GetNbinsX()
                for ibin in range( num_bins ) :
                  (thsBackground_grouped.GetHists().At(ihisto)).SetBinError(ibin+1, 0.000001)
                (thsBackground_grouped.GetHists().At(ihisto)).DrawNormalized("same")
                  
              for ihisto in range(thsSignal_grouped.GetNhists()) :
                num_bins = (thsSignal_grouped.GetHists().At(ihisto)).GetNbinsX()
                for ibin in range( num_bins ) :
                  (thsSignal_grouped.GetHists().At(ihisto)).SetBinError(ibin+1, 0.000001)
                (thsSignal_grouped.GetHists().At(ihisto)).DrawNormalized("same")
  
              tlegend.Draw()
              tcanvasSigVsBkg.SaveAs(self._outputDirPlots + "/" + 'cSigVsBkg_' + cutName + "_" + variableName + ".png")
         

            
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
            else :
              frameDistro.GetXaxis().SetTitle(variableName)
            frameDistro.GetYaxis().SetTitle("Events")
            #frameDistro.GetYaxis().SetRangeUser( 0, maxYused )
            frameDistro.GetYaxis().SetRangeUser( max(0.001, minYused), maxYused )


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
            
            tcanvasRatio.SaveAs(self._outputDirPlots + "/" + canvasRatioNameTemplate + ".png")
            tcanvasRatio.SaveAs(self._outputDirPlots + "/" + canvasRatioNameTemplate + ".root")
            
            
            # log Y axis
            frameDistro.GetYaxis().SetRangeUser( max(self._minLogCratio, maxYused/1000), self._maxLogCratio * maxYused )
            pad1.SetLogy()
            tcanvasRatio.SaveAs(self._outputDirPlots + "/log_" + canvasRatioNameTemplate + ".png")
            pad1.SetLogy(0)


          
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
                          integral_bkg += thsBackground.GetStack().Last().GetBinContent(ibin+1 + sliceX * nbinY)
                        else :
                          integral_bkg += thsBackground_grouped.GetStack().Last().GetBinContent(ibin+1 + sliceX * nbinY)
                      integral_sig = 0.
                      
                      if len(groupPlot.keys()) == 0:          
                        for ibin in range( thsSignal.GetStack().Last().GetNbinsX() ) :
                          integral_sig += thsSignal.GetStack().Last().GetBinContent(ibin+1 + sliceX * nbinY)
                      else :
                        for ibin in range( thsSignal_grouped.GetStack().Last().GetNbinsX() ) :
                          integral_sig += thsSignal_grouped.GetStack().Last().GetBinContent(ibin+1 + sliceX * nbinY)
                      
                      # this is because the signal was added into the background  stack before    
                      integral_bkg = integral_bkg - integral_sig
                      weight = 1
                      if integral_bkg != 0 : 
                        weight = integral_sig / integral_bkg
                      else :
                        weight = 1
                      weight_X_list_weights.append(weight)
                      
                      
                      if len(groupPlot.keys()) == 0:          

                          for ihisto in range(thsBackground.GetNhists()) :
                             histo = ROOT.TH1F('h_weigth_X_' +  cutName + '_' + variableName + '_' + ((thsBackground.GetHists().At(ihisto))).GetName() + '_slice_'+ str(sliceX), '-' , nbinY, 0, nbinY)
                             histo.SetFillColor( ((thsBackground.GetHists().At(ihisto))).GetFillColor())
                             histo.SetFillStyle( ((thsBackground.GetHists().At(ihisto))).GetFillStyle())
                             histo.SetLineColor( ((thsBackground.GetHists().At(ihisto))).GetLineColor())
                             histo.SetLineWidth( ((thsBackground.GetHists().At(ihisto))).GetLineWidth())
                             
                             for ibin in range( nbinY ) :
                               histo.SetBinContent(ibin+1, weight * ( ((thsBackground.GetHists().At(ihisto))).GetBinContent(ibin+1 + sliceX * nbinY) ) )
                             
                             if sliceX != 0:
                               weight_X_list_Background[ihisto].Add(histo)
                             else :
                               weight_X_list_Background.append(histo)
                          
                             # the minus signal is because the signal was added into the background stack before  
                             if ihisto < (thsBackground.GetNhists() - thsSignal.GetNhists()) :
                               totalWeightedIntegralBkg += histo.Integral()
                          
                             
                          for ihisto in range(thsSignal.GetNhists()) :
                             histo = ROOT.TH1F('h_weigth_X_' +  cutName + '_' + variableName + '_' + ((thsSignal.GetHists().At(ihisto))).GetName() + '_slice_'+ str(sliceX), "-", nbinY, 0, nbinY)
                             histo.SetFillColor( ((thsSignal.GetHists().At(ihisto))).GetFillColor())
                             histo.SetFillStyle( ((thsSignal.GetHists().At(ihisto))).GetFillStyle())
                             histo.SetLineColor( ((thsSignal.GetHists().At(ihisto))).GetLineColor())
                             histo.SetLineWidth( ((thsSignal.GetHists().At(ihisto))).GetLineWidth())
                             
                             for ibin in range( nbinY ) :
                               histo.SetBinContent(ibin+1, weight * ( ((thsSignal.GetHists().At(ihisto))).GetBinContent(ibin+1 + sliceX * nbinY) ) )
                          
                             if sliceX != 0:
                               weight_X_list_Signal[ihisto].Add(histo)
                             else :
                               weight_X_list_Signal.append(histo)
                               
                             totalWeightedIntegralSig += histo.Integral()
                          
                          
                          for ihisto in range(thsData.GetNhists()) :
                             histo = ROOT.TH1F('h_weigth_X_' +  cutName + '_' + variableName + '_' + ((thsData.GetHists().At(ihisto))).GetName() + '_slice_'+ str(sliceX), "-", nbinY, 0, nbinY)
                             for ibin in range( nbinY ) :
                               histo.SetBinContent(ibin+1, weight * ( ((thsData.GetHists().At(ihisto))).GetBinContent(ibin+1 + sliceX * nbinY) ) )
                             
                             if sliceX != 0:
                               weight_X_list_Data[ihisto].Add(histo)
                             else :
                               weight_X_list_Data.append(histo)
                             #weight_X_list_Data.append(histo)  ## aaaargh!
                      
                      else :

                          for ihisto in range(thsBackground_grouped.GetNhists()) :
                             histo = ROOT.TH1F('h_weigth_X_' +  cutName + '_' + variableName + '_' + ((thsBackground_grouped.GetHists().At(ihisto))).GetName() + '_slice_'+ str(sliceX), '-' , nbinY, 0, nbinY)
                             histo.SetFillColor( ((thsBackground_grouped.GetHists().At(ihisto))).GetFillColor())
                             histo.SetFillStyle( ((thsBackground_grouped.GetHists().At(ihisto))).GetFillStyle())
                             histo.SetLineColor( ((thsBackground_grouped.GetHists().At(ihisto))).GetLineColor())
                             histo.SetLineWidth( ((thsBackground_grouped.GetHists().At(ihisto))).GetLineWidth())
                             
                             for ibin in range( nbinY ) :
                               histo.SetBinContent(ibin+1, weight * ( ((thsBackground_grouped.GetHists().At(ihisto))).GetBinContent(ibin+1 + sliceX * nbinY) ) )
                             
                             if sliceX != 0:
                               weight_X_list_Background[ihisto].Add(histo)
                             else :
                               weight_X_list_Background.append(histo)
                          
                             # the minus signal is because the signal was added into the background stack before  
                             if ihisto < (thsBackground_grouped.GetNhists() - thsSignal_grouped.GetNhists()) :
                               totalWeightedIntegralBkg += histo.Integral()
                          
                             
                          for ihisto in range(thsSignal_grouped.GetNhists()) :
                             histo = ROOT.TH1F('h_weigth_X_' +  cutName + '_' + variableName + '_' + ((thsSignal_grouped.GetHists().At(ihisto))).GetName() + '_slice_'+ str(sliceX), "-", nbinY, 0, nbinY)
                             histo.SetFillColor( ((thsSignal_grouped.GetHists().At(ihisto))).GetFillColor())
                             histo.SetFillStyle( ((thsSignal_grouped.GetHists().At(ihisto))).GetFillStyle())
                             histo.SetLineColor( ((thsSignal_grouped.GetHists().At(ihisto))).GetLineColor())
                             histo.SetLineWidth( ((thsSignal_grouped.GetHists().At(ihisto))).GetLineWidth())
                             
                             for ibin in range( nbinY ) :
                               histo.SetBinContent(ibin+1, weight * ( ((thsSignal_grouped.GetHists().At(ihisto))).GetBinContent(ibin+1 + sliceX * nbinY) ) )
                          
                             if sliceX != 0:
                               weight_X_list_Signal[ihisto].Add(histo)
                             else :
                               weight_X_list_Signal.append(histo)
                               
                             totalWeightedIntegralSig += histo.Integral()
                          
                          
                          
                          
                          for ihisto in range(thsData.GetNhists()) :
                             histo = ROOT.TH1F('h_weigth_X_' +  cutName + '_' + variableName + '_' + ((thsData.GetHists().At(ihisto))).GetName() + '_slice_'+ str(sliceX), "-", nbinY, 0, nbinY)
                             for ibin in range( nbinY ) :
                               histo.SetBinContent(ibin+1, weight * ( ((thsData.GetHists().At(ihisto))).GetBinContent(ibin+1 + sliceX * nbinY) ) )
                             
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
                        y      = weight_X_list_weights[sliceX] * global_normalization * tgrData_vy[ibin + sliceX * nbinY]
                        exlow  = tgrData_evx[ibin + sliceX * nbinY]
                        exhigh = tgrData_evx[ibin + sliceX * nbinY]
                        eylow  = weight_X_list_weights[sliceX] * global_normalization * tgrData_evy_do[ibin + sliceX * nbinY]
                        eyhigh = weight_X_list_weights[sliceX] * global_normalization * tgrData_evy_up[ibin + sliceX * nbinY]
                        
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
                        y = weight_X_list_weights[sliceX] * global_normalization * tgrMC_vy[ibin + sliceX * nbinY]
                        exlow  = tgrData_evx[ibin + sliceX * nbinY]
                        exhigh = tgrData_evx[ibin + sliceX * nbinY]
                        #print " ibin + sliceX * nbinY = " , ibin , "+", sliceX ,"*", nbinY, " = ", ibin + sliceX * nbinY
                        #print "nuisances_err_do = ", nuisances_err_do
                        eylow = 0
                        eyhigh = 0
                        if len(nuisances_err_do) != 0:
                          eylow  = weight_X_list_weights[sliceX] * global_normalization * nuisances_err_do[ibin + sliceX * nbinY]
                          eyhigh = weight_X_list_weights[sliceX] * global_normalization * nuisances_err_up[ibin + sliceX * nbinY]
                        
                        if sliceX != 0 :
                          y += weight_X_tgrMC.GetY()[ibin]
                          eylow  = self.SumQ ( eylow,  weight_X_tgrMC.GetErrorYlow(ibin) )
                          eyhigh = self.SumQ ( eyhigh, weight_X_tgrMC.GetErrorYhigh(ibin) )
                        
                        #print " eylow = ", eylow, " eyhigh = ", eyhigh, " y = ", y, " x = ", x 

                        weight_X_tgrMC.SetPoint      (ibin, x, y)
                        weight_X_tgrMC.SetPointError (ibin, exlow, exhigh, eylow, eyhigh)
                    
                    
                    # create the weighted data over MC distribution
                    weight_X_tgrDataOverMC = weight_X_tgrData.Clone("tgrDataOverMCweighted")
                    for ibin in range( nbinY ) :
                      x = weight_X_tgrDataOverMC.GetX()[ibin]
                      y = self.Ratio(weight_X_tgrData.GetY()[ibin] , weight_X_thsBackground.GetStack().Last().GetBinContent(ibin+1) )
                      exlow  = tgrData_evx[ibin + sliceX * nbinY]
                      exhigh = tgrData_evx[ibin + sliceX * nbinY]
                      eylow  = self.Ratio(weight_X_tgrData.GetErrorYlow(ibin),  weight_X_thsBackground.GetStack().Last().GetBinContent(ibin+1) )
                      eyhigh = self.Ratio(weight_X_tgrData.GetErrorYhigh(ibin), weight_X_thsBackground.GetStack().Last().GetBinContent(ibin+1) )                    
                      
                      weight_X_tgrDataOverMC.SetPoint      (ibin, x, y)
                      weight_X_tgrDataOverMC.SetPointError (ibin, exlow, exhigh, eylow, eyhigh)

                      #print " Ratio:: ibin,x,y = ", ibin, ", ", x, ", ", y, ", ", eylow, ", ", eyhigh, " <-- ", weight_X_tgrData.GetY()[ibin], " / ",  weight_X_thsBackground.GetStack().Last().GetBinContent(ibin+1) 
            
                    # create the weighted MC over MC distribution
                    weight_X_tgrMCOverMC = weight_X_tgrData.Clone("tgrMCOverMCweighted")
                    for ibin in range( nbinY ) :
                      x = weight_X_tgrMCOverMC.GetX()[ibin]
                      y = 1 
                      exlow  = tgrData_evx[ibin + sliceX * nbinY]
                      exhigh = tgrData_evx[ibin + sliceX * nbinY]
                      eylow  = self.Ratio(weight_X_tgrMC.GetErrorYlow(ibin),  weight_X_thsBackground.GetStack().Last().GetBinContent(ibin+1) )
                      eyhigh = self.Ratio(weight_X_tgrMC.GetErrorYhigh(ibin), weight_X_thsBackground.GetStack().Last().GetBinContent(ibin+1) )                    
                      
                      weight_X_tgrMCOverMC.SetPoint      (ibin, x, y)
                      weight_X_tgrMCOverMC.SetPointError (ibin, exlow, exhigh, eylow, eyhigh)
           
           
                    #
                    # now plot
                    #
                    # - recalculate the maxY
                    maxYused = 1.2 * self.GetMaximumIncludingErrors(weight_X_thsBackground.GetStack().Last())

                    weight_X_canvasRatioNameTemplate = 'cratio_weight_X_' + cutName + '_' + variableName
            
                    weight_X_tcanvasRatio.cd()
                    canvasPad1Name = 'weight_X_pad1_' + cutName + "_" + variableName
                    weight_X_pad1 = ROOT.TPad(canvasPad1Name,canvasPad1Name, 0, 1-0.72, 1, 1)
                    weight_X_pad1.SetTopMargin(0.098)
                    weight_X_pad1.SetBottomMargin(0.000) 
                    weight_X_pad1.Draw()
                    
                    weight_X_pad1.cd()
                    weight_X_canvasFrameDistroName = 'weight_X_frame_distro_' + cutName + "_" + variableName
                    #weight_X_frameDistro = weight_X_pad1.DrawFrame(minXused, 0.0, maxXused, 1.0, weight_X_canvasFrameDistroName)
                    weight_X_frameDistro = weight_X_pad1.DrawFrame(0.0, 0.0, nbinY, 1.0, weight_X_canvasFrameDistroName)
                    
                    # style from https://ghm.web.cern.ch/ghm/plots/MacroExample/myMacro.py
                    xAxisDistro = weight_X_frameDistro.GetXaxis()
                    xAxisDistro.SetNdivisions(6,5,0)
            
                    if 'xaxis' in variable.keys() : 
                      weight_X_frameDistro.GetXaxis().SetTitle(variable['xaxis'])
                    else :
                      weight_X_frameDistro.GetXaxis().SetTitle(variableName)
                    weight_X_frameDistro.GetYaxis().SetTitle("S/B weighted Events")
                    weight_X_frameDistro.GetYaxis().SetRangeUser( max(0.001, minYused), maxYused )
            
                    if weight_X_thsBackground.GetNhists() != 0:
                      weight_X_thsBackground.Draw("hist same")
                       
                    if weight_X_thsSignal.GetNhists() != 0:
                      weight_X_thsSignal.Draw("hist same noclear")
                    
                    if (len(mynuisances.keys())!=0):
                      weight_X_tgrMC.SetLineColor(12)
                      weight_X_tgrMC.SetFillColor(12)
                      weight_X_tgrMC.SetFillStyle(3004)
                      weight_X_tgrMC.Draw("2")
           
                    #     - then the DATA  
                    if weight_X_tgrData.GetN() != 0:
                      weight_X_tgrData.Draw("P0")
               
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
                    weight_X_frameRatio = weight_X_pad2.DrawFrame(minXused, 0.0, nbinY, 2.0, weight_X_canvasFrameRatioName)
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
                    
                    weight_X_tcanvasRatio.SaveAs(self._outputDirPlots + "/" + weight_X_canvasRatioNameTemplate + ".png")
                    weight_X_tcanvasRatio.SaveAs(self._outputDirPlots + "/" + weight_X_canvasRatioNameTemplate + ".root")
                    
                    
                    # save also all the TH1F separately for later combination
                    temp_file = ROOT.TFile (self._outputDirPlots + "/" + weight_X_canvasRatioNameTemplate + ".root", "UPDATE")
                   
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
                    weight_X_frameDistro.GetYaxis().SetRangeUser( max(0.001, maxYused/1000), 10 * maxYused )
                    weight_X_pad1.SetLogy()
                    weight_X_tcanvasRatio.SaveAs(self._outputDirPlots + "/log_" + weight_X_canvasRatioNameTemplate + ".png")
                    weight_X_pad1.SetLogy(0)
 
            

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
            
            print " >> end: ", variableName
            
          print " >> all end"

        print " >> all but really all "
        
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
   # --- poissonian error bayesian 1sigma band
   #                                      1/0   1/0
    def GetPoissError(self, numberEvents, down, up):
       alpha = (1-0.6827)
       L = 0
       if numberEvents!=0 : 
         L = ROOT.Math.gamma_quantile (alpha/2,numberEvents,1.)
       U = 0
       if numberEvents==0 :
         U = ROOT.Math.gamma_quantile_c (alpha,numberEvents+1,1.) 
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

        
   


if __name__ == '__main__':
    print '''
--------------------------------------------------------------------------------------------------

   _ \   |         |         \  |         |                
  |   |  |   _ \   __|      |\/ |   _` |  |  /   _ \   __| 
  ___/   |  (   |  |        |   |  (   |    <    __/  |    
 _|     _| \___/  \__|     _|  _| \__,_| _|\_\ \___| _|   
 
--------------------------------------------------------------------------------------------------
'''    
    usage = 'usage: %prog [options]'
    parser = optparse.OptionParser(usage)

    parser.add_option('--minLogC'        , dest='minLogC'        , help='min Y in log plots'                         , default=0.01  ,    type=float   )
    parser.add_option('--maxLogC'        , dest='maxLogC'        , help='max Y in log plots'                         , default=100   ,    type=float   )
    parser.add_option('--minLogCratio'   , dest='minLogCratio'   , help='min Y in log ratio plots'                   , default=0.001 ,    type=float   )
    parser.add_option('--maxLogCratio'   , dest='maxLogCratio'   , help='max Y in log ratio plots'                   , default=10    ,    type=float   )
    parser.add_option('--outputDirPlots' , dest='outputDirPlots' , help='output directory'                           , default='./')
    parser.add_option('--inputFile'      , dest='inputFile'      , help='input file with histograms'                 , default='input.root')
    parser.add_option('--nuisancesFile'  , dest='nuisancesFile'  , help='file with nuisances configurations'         , default=None )
   
    parser.add_option('--plotNormalizedDistributions'  , dest='plotNormalizedDistributions'  , help='plot also normalized distributions for optimization purposes'         , default=None )
    parser.add_option('--showIntegralLegend'           , dest='showIntegralLegend'           , help='show the integral, the yields, in the legend'                         , default=0,    type=float )
          
          
          
          
    # read default parsing options as well
    hwwtools.addOptions(parser)
    hwwtools.loadOptDefaults(parser)
    (opt, args) = parser.parse_args()

    sys.argv.append( '-b' )
    ROOT.gROOT.SetBatch()


    print " configuration file = ", opt.pycfg
    print " lumi =               ", opt.lumi
    
    print " inputFile      =          ", opt.inputFile
    print " outputDirPlots =          ", opt.outputDirPlots
 
    print " plotNormalizedDistributions = ", opt.plotNormalizedDistributions
    print " showIntegralLegend = ", opt.showIntegralLegend
    
    print " minLogC   =          ", opt.minLogC
    print " maxLogC   =          ", opt.maxLogC

    print " minLogCratio   =          ", opt.minLogCratio
    print " maxLogCratio   =          ", opt.maxLogCratio

    opt.minLogC = float(opt.minLogC)
    opt.maxLogC = float(opt.maxLogC)

    opt.minLogCratio = float(opt.minLogCratio)
    opt.maxLogCratio = float(opt.maxLogCratio)

    if not opt.debug:
        pass
    elif opt.debug == 2:
        print 'Logging level set to DEBUG (%d)' % opt.debug
        logging.basicConfig( level=logging.DEBUG )
    elif opt.debug == 1:
        print 'Logging level set to INFO (%d)' % opt.debug
        logging.basicConfig( level=logging.INFO )

      
    factory = ShapeFactory()
    factory._energy    = opt.energy
    factory._lumi      = opt.lumi
    factory._plotNormalizedDistributions = opt.plotNormalizedDistributions
    factory._showIntegralLegend = opt.showIntegralLegend
    
    factory._minLogC = opt.minLogC 
    factory._maxLogC = opt.maxLogC 
    factory._minLogCratio = opt.minLogCratio
    factory._maxLogCratio = opt.maxLogCratio

    
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
    
    #samples = {}
    samples = OrderedDict()
    if os.path.exists(opt.samplesFile) :
      handle = open(opt.samplesFile,'r')
      exec(handle)
      handle.close()
    
    groupPlot = OrderedDict()
    plot = {}
    legend = {}
    if os.path.exists(opt.plotFile) :
      handle = open(opt.plotFile,'r')
      exec(handle)
      handle.close()
   
    nuisances = {}
    if opt.nuisancesFile == None :
      print " Please provide the nuisances structure if you want to add nuisances "
    elif os.path.exists(opt.nuisancesFile) :
      handle = open(opt.nuisancesFile,'r')
      exec(handle)
      handle.close() 
   
    factory.makePlot( opt.inputFile ,opt.outputDirPlots, variables, cuts, samples, plot, nuisances, legend, groupPlot)
    
    print '... and now closing ...'
        
       
