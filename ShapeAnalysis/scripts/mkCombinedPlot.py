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

        outputDirPlots = {}
        self._outputDirPlots = outputDirPlots
        

    # _____________________________________________________________________________
    def makeCombinedPlot(self, outputDirPlots, cutsToMerge, plot, legend, groupPlot):


        print "=========================="
        print "==== makeCombinedPlot ===="
        print "=========================="
        
        self.defineStyle()
        
        self._outputDirPlots = outputDirPlots

        os.system ("mkdir " + outputDirPlots + "/") 
        
        ROOT.TH1.SetDefaultSumw2(True)
        
        dataColor = 1


        ROOT.gROOT.cd()

        list_thsData       = {}
        list_thsSignal     = {}
        list_thsBackground = OrderedDict()

        tcanvas            = ROOT.TCanvas( "cc" + "_combined_" + "_" + self._variable,      "cc"     , 800, 600 )
        tcanvasRatio       = ROOT.TCanvas( "ccRatio" + "_combined_" + "_" + self._variable, "ccRatio", 800, 800 )


        list_files = {}
        list_files_weights_sig = {}
        list_files_integral_sig = {}
        list_files_weight_integral_sig = {}
        
        for cutName, cutConfig in cutsToMerge.iteritems(): 
          print " cutName = ", cutName , " ----> " , cutConfig['rootFile']
          temp_file = ROOT.TFile(cutConfig['rootFile'], "READ")
          list_files[cutName] = temp_file
          list_files_weights_sig [cutName] = temp_file.Get("histo_global_normalization").GetBinContent(1) 
          # global_normalization = totalSig / totalWeightedIntegralSig

        # loop over all the cuts (= phase spaces) you want to merge in one
        for sampleNameGroup, sampleConfiguration in groupPlot.iteritems():
          for cutName, cutConfig in cutsToMerge.iteritems():         
            nameToBeUsed = cutName
            if 'cutUsed' in cutConfig.keys() :
              nameToBeUsed = cutConfig['cutUsed']
            
            #name_histogram = 'h_weigth_X_' +  nameToBeUsed + '_' + self._variable + '_new_histo_group_' + sampleNameGroup + '_' + nameToBeUsed + '_' +  self._variable + '_slice_0'
            name_histogram = 'new_h_weigth_X_' +  nameToBeUsed + '_' + self._variable + '_new_histo_group_' + sampleNameGroup + '_' + nameToBeUsed + '_' +  self._variable + '_slice_0'

            if 'isSignal' in sampleConfiguration and sampleConfiguration['isSignal'] != 0 :
              if list_files[cutName].Get(name_histogram) :
                
                if cutName not in list_files_integral_sig :
                  list_files_integral_sig[cutName] =  (list_files[cutName].Get(name_histogram)).Integral() 
                else :
                  list_files_integral_sig[cutName] += (list_files[cutName].Get(name_histogram)).Integral() 
                

        #
        # divide by the signal rate
        # save this value to later scale everything
        #
        
        totalIntegralSig = 0.
        totalWeightIntegralSig = 0.
         
        for cutName, cutConfig in cutsToMerge.iteritems():         
          totalIntegralSig       += list_files_integral_sig[cutName] 
          totalWeightIntegralSig += (list_files_integral_sig[cutName] / list_files_weights_sig [cutName])
          list_files_weight_integral_sig[cutName] = (list_files_integral_sig[cutName] / list_files_weights_sig [cutName])
          
        print " totalIntegralSig =       ", totalIntegralSig
        print " totalWeightIntegralSig = ", totalWeightIntegralSig

          
        # loop over all the cuts (= phase spaces) you want to merge in one
        for sampleNameGroup, sampleConfiguration in groupPlot.iteritems():
          for cutName, cutConfig in cutsToMerge.iteritems():         
            #print " cutName = ", cutName , " ----> " , cutConfig['rootFile']
            #print 'h_weigth_X_' +  cutName + '_' + self._variable + '_new_histo_group_' + sampleNameGroup + '_' + cutName + '_' +  self._variable + '_slice_0'
            
            global_scale_factor = totalIntegralSig / totalWeightIntegralSig * list_files_weight_integral_sig[cutName] / list_files_integral_sig[cutName]


            nameToBeUsed = cutName
            if 'cutUsed' in cutConfig.keys() :
              nameToBeUsed = cutConfig['cutUsed']
            
            #name_histogram = 'h_weigth_X_' +  nameToBeUsed + '_' + self._variable + '_new_histo_group_' + sampleNameGroup + '_' + nameToBeUsed + '_' +  self._variable + '_slice_0'
            name_histogram = 'new_h_weigth_X_' +  nameToBeUsed + '_' + self._variable + '_new_histo_group_' + sampleNameGroup + '_' + nameToBeUsed + '_' +  self._variable + '_slice_0'

            if 'isSignal' in sampleConfiguration and sampleConfiguration['isSignal'] != 0 :
              if list_files[cutName].Get(name_histogram) :
                if sampleNameGroup not in list_thsSignal.keys() :
                  list_thsSignal [sampleNameGroup] = list_files[cutName].Get(name_histogram).Clone(name_histogram + '_' + cutName)
                  list_thsSignal [sampleNameGroup].Scale ( 1. * global_scale_factor )
                  
                  #print 'type = ',  type( list_thsSignal [sampleNameGroup]  )
                else :
                  list_thsSignal [sampleNameGroup].Add( list_files[cutName].Get(name_histogram).Clone(name_histogram + '_' + cutName), 1. * global_scale_factor )
            else :
              if list_files[cutName].Get(name_histogram) :
                if sampleNameGroup not in list_thsBackground.keys() :
                  list_thsBackground [sampleNameGroup] = list_files[cutName].Get(name_histogram).Clone(name_histogram + '_' + cutName)
                  list_thsBackground [sampleNameGroup].Scale ( 1. * global_scale_factor )
                  #print 'type = ', type( list_thsBackground [sampleNameGroup]  )
                else :
                  list_thsBackground [sampleNameGroup].Add( list_files[cutName].Get(name_histogram).Clone(name_histogram + '_' + cutName) , 1. * global_scale_factor )
             
             
        for cutName, cutConfig in cutsToMerge.iteritems():         

          global_scale_factor = totalIntegralSig / totalWeightIntegralSig * list_files_weight_integral_sig[cutName] / list_files_integral_sig[cutName]

          nameToBeUsed = cutName
          if 'cutUsed' in cutConfig.keys() :
            nameToBeUsed = cutConfig['cutUsed']

          #name_histogram = 'h_weigth_X_' +  nameToBeUsed + '_' + self._variable + '_new_histo_' + 'DATA' + '_' + nameToBeUsed + '_' +  self._variable + '_slice_0'
          name_histogram = 'new_h_weigth_X_' +  nameToBeUsed + '_' + self._variable + '_new_histo_' + 'DATA' + '_' + nameToBeUsed + '_' +  self._variable + '_slice_0'

          print " data:: ", name_histogram
          
          if list_files[cutName].Get(name_histogram) :
            if 'DATA' not in list_thsData.keys() :
              list_thsData ['DATA'] = list_files[cutName].Get(name_histogram).Clone(name_histogram + '_' + cutName)
              list_thsData ['DATA'].Scale ( 1. * global_scale_factor )
            else :
              list_thsData ['DATA'].Add( list_files[cutName].Get(name_histogram).Clone(name_histogram + '_' + cutName) , 1. * global_scale_factor )
           
        
         
        #
        # fix x-axis range of histograms
        #
        
        list_thsData ['DATA'] = self.FixBins(list_thsData ['DATA'])
        #print " max = ", (list_thsData ['DATA']).GetXaxis().GetBinCenter(list_thsData['DATA'].GetNbinsX()+1)
        for histoname, histo in list_thsSignal.iteritems():
          list_thsSignal[histoname] = self.FixBins(histo)          
          #print " max = ", histo.GetXaxis().GetBinCenter(histo.GetNbinsX())
        for histoname, histo in list_thsBackground.iteritems():
          list_thsBackground[histoname] = self.FixBins(histo)
          #print " max = ", histo.GetXaxis().GetBinCenter(histo.GetNbinsX())
   
  
        #
        # divide the histograms by the bin width if specified
        #
 
        if self._divideByBinWidth == True:
          list_thsData ['DATA'].Scale(1,"width")
          for histoname, histo in list_thsSignal.iteritems():
            list_thsSignal[histoname].Scale(1,"width")
          for histoname, histo in list_thsBackground.iteritems():
            list_thsBackground[histoname].Scale(1,"width")

        #
        # prepare the signal TGraphAsymmErrors
        #

        tgrSig  = ROOT.TGraphAsymmErrors()
        tgrSig.SetLineColor(ROOT.kRed)
        
        for sampleNameGroup, sampleConfiguration in groupPlot.iteritems():
          if 'isSignal' in sampleConfiguration and sampleConfiguration['isSignal'] != 0 :  
            temp_histo = list_thsSignal[sampleNameGroup]
            if tgrSig.GetN() == 0 :
              for iBin in range(temp_histo.GetNbinsX()) :
                tgrSig.SetPoint      (iBin, temp_histo.GetXaxis().GetBinCenter(iBin+1), temp_histo.GetBinContent(iBin+1) )
                tgrSig.SetPointError (iBin, temp_histo.GetBinWidth(iBin+1) /2., temp_histo.GetBinWidth(iBin+1) /2., 0. , 0. )
            
            else :
              for iBin in range(temp_histo.GetNbinsX()) :
                x_temp = tgrSig.GetX()[iBin]
                y_temp = tgrSig.GetY()[iBin]
                exl_temp = tgrSig.GetErrorXlow(iBin)
                exh_temp = tgrSig.GetErrorXhigh(iBin)
                
                tgrSig.SetPoint      (iBin, x_temp, temp_histo.GetBinContent(iBin+1) + y_temp )
                tgrSig.SetPointError (iBin, exl_temp, exh_temp, 0., 0. )
  
        
        
        # now that all the histograms are merged, let's merge the TGraphs
        tgrData  = ROOT.TGraphAsymmErrors()
        tgrMC    = ROOT.TGraphAsymmErrors()
        tgrMC_noSig  = ROOT.TGraphAsymmErrors()

        for cutName, cutConfig in cutsToMerge.iteritems():    
          temp_graph = list_files[cutName].Get("weight_X_tgrMC")
          
          global_scale_factor = totalIntegralSig / totalWeightIntegralSig * list_files_weight_integral_sig[cutName] / list_files_integral_sig[cutName]
          
          if tgrMC.GetN() == 0 :
            for iBin in range(temp_graph.GetN()) :
              #tgrMC.SetPoint      (iBin, temp_graph.GetX()[iBin], temp_graph.GetY()[iBin] )
              #tgrMC.SetPointError (iBin, temp_graph.GetErrorXlow(iBin), temp_graph.GetErrorXhigh(iBin),  temp_graph.GetErrorYlow(iBin), temp_graph.GetErrorYhigh(iBin) )
              if self._divideByBinWidth == True:
                tgrMC.SetPoint      (iBin, list_thsData ['DATA'].GetXaxis().GetBinCenter(iBin+1), temp_graph.GetY()[iBin]  * global_scale_factor / list_thsData ['DATA'].GetXaxis().GetBinWidth(iBin+1) )
                tgrMC.SetPointError (iBin, list_thsData ['DATA'].GetBinWidth(iBin+1)/2., list_thsData ['DATA'].GetBinWidth(iBin+1)/2., temp_graph.GetErrorYlow(iBin)  * global_scale_factor / list_thsData ['DATA'].GetXaxis().GetBinWidth(iBin+1), temp_graph.GetErrorYhigh(iBin)  * global_scale_factor / list_thsData ['DATA'].GetXaxis().GetBinWidth(iBin+1) )
              else:
                tgrMC.SetPoint      (iBin, list_thsData ['DATA'].GetXaxis().GetBinCenter(iBin+1), temp_graph.GetY()[iBin]  * global_scale_factor )
                tgrMC.SetPointError (iBin, list_thsData ['DATA'].GetBinWidth(iBin+1)/2., list_thsData ['DATA'].GetBinWidth(iBin+1)/2., temp_graph.GetErrorYlow(iBin)  * global_scale_factor, temp_graph.GetErrorYhigh(iBin)  * global_scale_factor )
          
          else :
            for iBin in range(temp_graph.GetN()) :
              x_temp = tgrMC.GetX()[iBin]
              y_temp = tgrMC.GetY()[iBin]
              exl_temp = tgrMC.GetErrorXlow(iBin)
              exh_temp = tgrMC.GetErrorXhigh(iBin)
              eyl_temp = tgrMC.GetErrorYlow(iBin)
              eyh_temp = tgrMC.GetErrorYhigh(iBin)
              
              if self._divideByBinWidth == True:
                tgrMC.SetPoint      (iBin, x_temp, (temp_graph.GetY()[iBin]  * global_scale_factor) / list_thsData ['DATA'].GetXaxis().GetBinWidth(iBin+1)  + y_temp )
                tgrMC.SetPointError (iBin, exl_temp, exh_temp, self.SumQ(temp_graph.GetErrorYlow(iBin)* global_scale_factor / list_thsData ['DATA'].GetXaxis().GetBinWidth(iBin+1), eyl_temp) , self.SumQ(temp_graph.GetErrorYhigh(iBin)* global_scale_factor / list_thsData ['DATA'].GetXaxis().GetBinWidth(iBin+1), eyh_temp) )
              else:
                tgrMC.SetPoint      (iBin, x_temp, temp_graph.GetY()[iBin]  * global_scale_factor  + y_temp )
                tgrMC.SetPointError (iBin, exl_temp, exh_temp, self.SumQ(temp_graph.GetErrorYlow(iBin)* global_scale_factor, eyl_temp) , self.SumQ(temp_graph.GetErrorYhigh(iBin)* global_scale_factor, eyh_temp)  )
 
        for cutName, cutConfig in cutsToMerge.iteritems():    
          temp_graph = list_files[cutName].Get("weight_X_tgrData")
          #print 'type = ', type( temp_graph )

          global_scale_factor = totalIntegralSig / totalWeightIntegralSig * list_files_weight_integral_sig[cutName] / list_files_integral_sig[cutName]

          print " global_scale_factor]", cutName, "] = ", global_scale_factor

          if tgrData.GetN() == 0 :
            for iBin in range(temp_graph.GetN()) :
              #tgrData.SetPoint      (iBin, temp_graph.GetX()[iBin], temp_graph.GetY()[iBin] )
              #tgrData.SetPointError (iBin, temp_graph.GetErrorXlow(iBin), temp_graph.GetErrorXhigh(iBin),  temp_graph.GetErrorYlow(iBin), temp_graph.GetErrorYhigh(iBin) )
              if self._divideByBinWidth == True:
                tgrData.SetPoint      (iBin, list_thsData ['DATA'].GetXaxis().GetBinCenter(iBin+1), temp_graph.GetY()[iBin]    * global_scale_factor / list_thsData ['DATA'].GetXaxis().GetBinWidth(iBin+1)  )
                tgrData.SetPointError (iBin, list_thsData ['DATA'].GetBinWidth(iBin+1)/2., list_thsData ['DATA'].GetBinWidth(iBin+1)/2.,  temp_graph.GetErrorYlow(iBin)    * global_scale_factor / list_thsData ['DATA'].GetXaxis().GetBinWidth(iBin+1) , temp_graph.GetErrorYhigh(iBin)    * global_scale_factor / list_thsData ['DATA'].GetXaxis().GetBinWidth(iBin+1)  )
              else:
                tgrData.SetPoint      (iBin, list_thsData ['DATA'].GetXaxis().GetBinCenter(iBin+1), temp_graph.GetY()[iBin]    * global_scale_factor  )
                tgrData.SetPointError (iBin, list_thsData ['DATA'].GetBinWidth(iBin+1)/2., list_thsData ['DATA'].GetBinWidth(iBin+1)/2.,  temp_graph.GetErrorYlow(iBin)    * global_scale_factor , temp_graph.GetErrorYhigh(iBin)    * global_scale_factor  )
          
          else :
            for iBin in range(temp_graph.GetN()) :
              x_temp = tgrData.GetX()[iBin]
              y_temp = tgrData.GetY()[iBin]
              exl_temp = tgrData.GetErrorXlow(iBin)
              exh_temp = tgrData.GetErrorXhigh(iBin)
              eyl_temp = tgrData.GetErrorYlow(iBin)
              eyh_temp = tgrData.GetErrorYhigh(iBin)

              if self._divideByBinWidth == True:
                tgrData.SetPoint      (iBin, x_temp, (temp_graph.GetY()[iBin]   * global_scale_factor) / list_thsData ['DATA'].GetXaxis().GetBinWidth(iBin+1)   + y_temp  )
                tgrData.SetPointError (iBin, exl_temp, exh_temp, self.SumQ(temp_graph.GetErrorYlow(iBin)* global_scale_factor  / list_thsData ['DATA'].GetXaxis().GetBinWidth(iBin+1), eyl_temp), self.SumQ(temp_graph.GetErrorYhigh(iBin)* global_scale_factor  / list_thsData ['DATA'].GetXaxis().GetBinWidth(iBin+1), eyh_temp) )
              else:              
                tgrData.SetPoint      (iBin, x_temp, temp_graph.GetY()[iBin]   * global_scale_factor   + y_temp )
                tgrData.SetPointError (iBin, exl_temp, exh_temp, self.SumQ(temp_graph.GetErrorYlow(iBin)* global_scale_factor, eyl_temp), self.SumQ(temp_graph.GetErrorYhigh(iBin)* global_scale_factor, eyh_temp) )
  
  
        #
        # merge to create the THStack
        #
        weight_X_thsData       = ROOT.THStack ("weight_X_thsData",      "weight_X_thsData")
        weight_X_thsSignal     = ROOT.THStack ("weight_X_thsSignal",    "weight_X_thsSignal")
        weight_X_thsBackground = ROOT.THStack ("weight_X_thsBackground","weight_X_thsBackground")

        for sampleName, histo in list_thsBackground.iteritems():
          weight_X_thsBackground.Add(histo)
        for sampleName, histo in list_thsSignal.iteritems():
          weight_X_thsSignal.Add(histo)
          # the signal is added on top of the background
          # the signal has to be the last one in the dictionary!
          # make it sure in plot.py
          weight_X_thsBackground.Add(histo)

        #
        # the signal is added on top of the background
        #
        
        tgrMC_noSig = tgrMC.Clone("tgrMC_noSig")
        
        for iBin in range( tgrMC.GetN() ) :
          x_temp = tgrMC.GetX()[iBin]
          y_temp = tgrMC.GetY()[iBin]
          exl_temp = tgrMC.GetErrorXlow(iBin)
          exh_temp = tgrMC.GetErrorXhigh(iBin)
          eyl_temp = tgrMC.GetErrorYlow(iBin)
          eyh_temp = tgrMC.GetErrorYhigh(iBin)

          tgrMC.SetPoint      (iBin, x_temp, tgrSig.GetY()[iBin]  + y_temp )
          tgrMC.SetPointError (iBin, exl_temp, exh_temp, eyl_temp , eyh_temp )
      
          

        #
        # prepare ratio plot
        #
        tgrMCOverMC = tgrMC.Clone("tgrMCOverMC")  
        for iBin in range( tgrMCOverMC.GetN() ) :
          tgrMCOverMC.SetPoint     (iBin, tgrMC.GetX()[iBin], 1.)
          tgrMCOverMC.SetPointError(iBin, tgrMC.GetErrorXlow(iBin), tgrMC.GetErrorXhigh(iBin), self.Ratio(tgrMC.GetErrorYlow(iBin), tgrMC.GetY()[iBin]), self.Ratio(tgrMC.GetErrorYhigh(iBin), tgrMC.GetY()[iBin]))     


        tgrDataOverMC = tgrData.Clone("tgrDataOverMC")
        for iBin in range( tgrDataOverMC.GetN() ) :
          tgrDataOverMC.SetPoint     (iBin, tgrData.GetX()[iBin],   self.Ratio(tgrData.GetY()[iBin] ,tgrMC.GetY()[iBin] ) )
          tgrDataOverMC.SetPointError(iBin,  tgrData.GetErrorXlow(iBin), tgrData.GetErrorXhigh(iBin), self.Ratio(tgrData.GetErrorYlow(iBin), tgrMC.GetY()[iBin]), self.Ratio(tgrData.GetErrorYhigh(iBin), tgrMC.GetY()[iBin]) )
                                      

        #---- the Legend
        tlegend = ROOT.TLegend(0.20, 0.60, 0.80, 0.85)
        tlegend.SetFillColor(0)
        tlegend.SetLineColor(0)
        tlegend.SetShadowColor(0)
         
        for sampleNameGroup, sampleConfiguration in groupPlot.iteritems():
          if 'isSignal' in sampleConfiguration and sampleConfiguration['isSignal'] != 0 :
            tlegend.AddEntry( list_thsSignal [sampleNameGroup] ,     sampleConfiguration['nameHR'], "F")          
          else :
            tlegend.AddEntry( list_thsBackground [sampleNameGroup] , sampleConfiguration['nameHR'], "F")
       
        tlegend.AddEntry( tgrData , 'Data', "EPL")
       
        tlegend.AddEntry(tgrMC, "Systematics", "F")

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

    
        
        #
        # now plot
        #
        
        
        # - recalculate the maxY
        maxYused = 2.0 * self.GetMaximumIncludingErrors(weight_X_thsBackground.GetStack().Last()) #1.1 *
        # FIXME these hardcoded numbers
        minYused = 0.001
        #nbinY = 5
        minXused = (list_thsData ['DATA']).GetXaxis().GetBinLowEdge(1) 
        if self._removeOverflow:
          maxXused = (list_thsData ['DATA']).GetXaxis().GetBinCenter( (list_thsData ['DATA']).GetNbinsX()-1 ) + (list_thsData ['DATA']).GetBinWidth( (list_thsData ['DATA'].GetNbinsX())-1 ) /2.
        else:      
          maxXused = (list_thsData ['DATA']).GetXaxis().GetBinCenter( (list_thsData ['DATA']).GetNbinsX() ) + (list_thsData ['DATA']).GetBinWidth( (list_thsData ['DATA'].GetNbinsX()) ) /2.
       
        
        print " minXused = ", minXused
        print " maxXused = ", maxXused,  " = ", (list_thsData ['DATA']).GetXaxis().GetBinCenter( (list_thsData ['DATA']).GetNbinsX() ) , " + ", (list_thsData ['DATA']).GetBinWidth( (list_thsData ['DATA'].GetNbinsX()) )
        print " maxYused = ", maxYused
        
        weight_X_canvasRatioNameTemplate = 'cratio_weight_X_' + self._variable
        weight_X_tcanvasRatio = ROOT.TCanvas(weight_X_canvasRatioNameTemplate, "weight_X_tcanvasRatio", 800, 800 )


        variableName = self._variable
        weight_X_tcanvasRatio.cd()
        canvasPad1Name = 'weight_X_pad1_' + variableName
        weight_X_pad1 = ROOT.TPad(canvasPad1Name,canvasPad1Name, 0, 1-0.72, 1, 1)
        weight_X_pad1.SetTopMargin(0.098)
        weight_X_pad1.SetBottomMargin(0.000) 
        weight_X_pad1.Draw()
        
        weight_X_pad1.cd()
        weight_X_canvasFrameDistroName = 'weight_X_frame_distro_' + variableName
        #weight_X_frameDistro = weight_X_pad1.DrawFrame(0.0, 0.0, nbinY, 1.0, weight_X_canvasFrameDistroName)
        weight_X_frameDistro = weight_X_pad1.DrawFrame(minXused, 0.0, maxXused, maxYused, weight_X_canvasFrameDistroName)
        
        ## style from https://ghm.web.cern.ch/ghm/plots/MacroExample/myMacro.py
        xAxisDistro = weight_X_frameDistro.GetXaxis()
        xAxisDistro.SetNdivisions(6,5,0)

        #if 'xaxis' in variable.keys() : 
          #weight_X_frameDistro.GetXaxis().SetTitle(variable['xaxis'])
        #else :
          #weight_X_frameDistro.GetXaxis().SetTitle(variableName)
        weight_X_frameDistro.GetXaxis().SetTitle(factory._variableHR)
                
        if self._divideByBinWidth==True:        
          weight_X_frameDistro.GetYaxis().SetTitle("S/B weighted Events/GeV")
        else:
          weight_X_frameDistro.GetYaxis().SetTitle("S/B weighted Events")
        weight_X_frameDistro.GetYaxis().SetRangeUser( max(0.001, minYused), maxYused )

        weight_X_thsBackground.Draw("hist same")
           
        weight_X_thsSignal.Draw("hist same noclear")
        
        tgrMC.SetLineColor(12)
        tgrMC.SetFillColor(12)
        tgrMC.SetFillStyle(3004)
        tgrMC.Draw("2")

        ##     - then the DATA  
        tgrData.Draw("P0")
   
        tlegend.Draw()
  
        CMS_lumi.CMS_lumi(weight_X_tcanvasRatio, iPeriod, iPos)    

        ## draw back all the axes            
        weight_X_pad1.RedrawAxis()

            
        weight_X_tcanvasRatio.cd()
        canvasPad2Name = 'weight_X_weight_X_pad2_' + variableName
        weight_X_pad2 = ROOT.TPad(canvasPad2Name,canvasPad2Name,0,0,1,1-0.72)
        weight_X_pad2.SetTopMargin(0.000)
        weight_X_pad2.SetBottomMargin(0.392)
        weight_X_pad2.Draw()
        #weight_X_pad2.cd().SetGrid()
        weight_X_pad2.cd()
        
        weight_X_canvasFrameRatioName = 'weight_X_frame_ratio_' + variableName
        weight_X_frameRatio = weight_X_pad2.DrawFrame(minXused, 0.0, maxXused, 2.0, weight_X_canvasFrameRatioName)
        ## style from https://ghm.web.cern.ch/ghm/plots/MacroExample/myMacro.py
        xAxisDistro = weight_X_frameRatio.GetXaxis()
        xAxisDistro.SetNdivisions(6,5,0)
          
        weight_X_frameRatio.GetXaxis().SetTitle(factory._variableHR)
        weight_X_frameRatio.GetYaxis().SetTitle("Data/Expected")
        weight_X_frameRatio.GetYaxis().SetRangeUser( 0.5, 1.5 )
        self.Pad2TAxis(weight_X_frameRatio)
        
        #if (len(mynuisances.keys())!=0):
        tgrMCOverMC.SetLineColor(12)
        tgrMCOverMC.SetFillColor(12)
        tgrMCOverMC.SetFillStyle(3004)
        tgrMCOverMC.Draw("2") 
            
        tgrDataOverMC.Draw("P0")

       

        oneLine2 = ROOT.TLine(weight_X_frameRatio.GetXaxis().GetXmin(), 1,  weight_X_frameRatio.GetXaxis().GetXmax(), 1);
        oneLine2.SetLineStyle(3)
        oneLine2.SetLineWidth(3)
        oneLine2.Draw("same")

        ## draw back all the axes            
        weight_X_pad2.RedrawAxis()
        
        weight_X_tcanvasRatio.SaveAs(self._outputDirPlots + "/" + weight_X_canvasRatioNameTemplate + ".png")
        weight_X_tcanvasRatio.SaveAs(self._outputDirPlots + "/" + weight_X_canvasRatioNameTemplate + ".root")
        
        
        ###
        #
        # background subtracted plot
        #
        
        tgrData_bkgSubtracted  = ROOT.TGraphAsymmErrors()
        tgrBkg_bkgSubtracted   = ROOT.TGraphAsymmErrors()
        
        maxYused = 0
        minYused = 100
        
        for iBin in range( tgrMC_noSig.GetN() ) :
          x_temp = tgrMC_noSig.GetX()[iBin]
          y_temp = tgrMC_noSig.GetY()[iBin]
          exl_temp = tgrMC_noSig.GetErrorXlow(iBin)
          exh_temp = tgrMC_noSig.GetErrorXhigh(iBin)
          eyl_temp = tgrMC_noSig.GetErrorYlow(iBin)
          eyh_temp = tgrMC_noSig.GetErrorYhigh(iBin)

          tgrData_bkgSubtracted.SetPoint      (iBin, x_temp, tgrData.GetY()[iBin] - y_temp )
          tgrData_bkgSubtracted.SetPointError (iBin, exl_temp, exh_temp, tgrData.GetErrorYlow(iBin) , tgrData.GetErrorYhigh(iBin) )

          tgrBkg_bkgSubtracted.SetPoint      (iBin, x_temp, 0 )
          tgrBkg_bkgSubtracted.SetPointError (iBin, exl_temp, exh_temp, eyl_temp, eyh_temp)

          if maxYused < (tgrData.GetY()[iBin] - y_temp) :
            maxYused = tgrData.GetY()[iBin] - y_temp
            
          if minYused > (tgrData.GetY()[iBin] - y_temp) :
            minYused = tgrData.GetY()[iBin] - y_temp
        
        maxYused *= 1.9
        if minYused < 0:
          #minYused *= 1.9
          minYused *= 1.9
          minYused -= totalIntegralSig/4.
        
        print " minYused = ", minYused
        
        bkgSub_weight_X_canvasRatioNameTemplate = 'cratio_bkgSub_weight_X_' + self._variable
        bkgSub_weight_X_tcanvasRatio = ROOT.TCanvas(bkgSub_weight_X_canvasRatioNameTemplate, "bkgSub_weight_X_tcanvasRatio", 800, 600 )

        bkgSub_weight_X_tcanvasRatio.cd()
        bkgSub_canvasPad1Name = 'bkgSub_weight_X_pad1_' + variableName
        bkgSub_weight_X_pad1 = ROOT.TPad(bkgSub_canvasPad1Name,bkgSub_canvasPad1Name, 0, 0, 1, 1)
        #bkgSub_weight_X_pad1.SetTopMargin(0.098)
        #bkgSub_weight_X_pad1.SetBottomMargin(0.002) 
        bkgSub_weight_X_pad1.Draw()
        
         
        bkgSub_weight_X_pad1.cd()
        bkgSub_weight_X_canvasFrameDistroName = 'bkgSub_weight_X_frame_distro_' + variableName
        bkgSub_weight_X_frameDistro = bkgSub_weight_X_pad1.DrawFrame(minXused, minYused, maxXused, maxYused, bkgSub_weight_X_canvasFrameDistroName)
        
        ## style from https://ghm.web.cern.ch/ghm/plots/MacroExample/myMacro.py
        bkgSub_xAxisDistro = bkgSub_weight_X_frameDistro.GetXaxis()
        bkgSub_xAxisDistro.SetNdivisions(6,5,0)

        bkgSub_weight_X_frameDistro.GetXaxis().SetTitle(factory._variableHR)
                
        
        bkgSub_weight_X_frameDistro.GetYaxis().SetTitle("S/B weighted Events bkg subtracted")
        bkgSub_weight_X_frameDistro.GetYaxis().SetRangeUser( minYused, maxYused )

        ##     - the background         
        tgrBkg_bkgSubtracted.SetLineColor(12)
        tgrBkg_bkgSubtracted.SetFillColor(12)
        tgrBkg_bkgSubtracted.SetFillStyle(3004)
        tgrBkg_bkgSubtracted.Draw("2")

        ##     - the signal         
        #tgrSig.Draw("histo")
        weight_X_thsSignal.Draw("hist same noclear")
        
        ##     - then the DATA  
        tgrData_bkgSubtracted.Draw("P0")
   


        #---- the Legend
        tlegend_bkgsub = ROOT.TLegend(0.70, 0.70, 0.90, 0.85)
        tlegend_bkgsub.SetFillColor(0)
        tlegend_bkgsub.SetLineColor(0)
        tlegend_bkgsub.SetShadowColor(0)
         
        for sampleNameGroup, sampleConfiguration in groupPlot.iteritems():
          if 'isSignal' in sampleConfiguration and sampleConfiguration['isSignal'] != 0 :
            tlegend_bkgsub.AddEntry( tgrSig ,  sampleConfiguration['nameHR'], "L")          
       
        tlegend_bkgsub.AddEntry( tgrData_bkgSubtracted , 'data - backgrounds', "EPL")
       
        tlegend_bkgsub.AddEntry(tgrBkg_bkgSubtracted, "Bkg uncertainty", "F")

        tlegend_bkgsub.SetNColumns(1)
        tlegend_bkgsub.Draw()



   
        CMS_lumi.CMS_lumi(bkgSub_weight_X_tcanvasRatio, iPeriod, iPos)    

        ## draw back all the axes            
        bkgSub_weight_X_pad1.RedrawAxis()
            
        
        bkgSub_weight_X_tcanvasRatio.SaveAs(self._outputDirPlots + "/" + bkgSub_weight_X_canvasRatioNameTemplate + ".png")
        bkgSub_weight_X_tcanvasRatio.SaveAs(self._outputDirPlots + "/" + bkgSub_weight_X_canvasRatioNameTemplate + ".root")
        

                  
                  
                  
    
    
   # _____________________________________________________________________________
   # --- fix binning
    
    def FixBins(self, histo):
        
        
        if len (self._binning) == 0 :
         
          nbins = histo.GetXaxis().GetNbins()
          alpha = (self._maxvariable - self._minvariable) / ( histo.GetXaxis().GetBinLowEdge(nbins+1) +  histo.GetXaxis().GetBinWidth(nbins+1)/2 - histo.GetXaxis().GetBinLowEdge(1))
          
          #print " alpha = ", alpha
          #print " histo.GetTitle() = ", histo.GetTitle()
          #print " histo.GetName() = ", histo.GetName()
          
          hnew = ROOT.TH1F("new_" + histo.GetName(),"",nbins, self._minvariable , self._maxvariable)
          for ibin in range (0, nbins+1) :
            y = histo.GetBinContent(ibin)
            x = histo.GetXaxis().GetBinCenter(ibin)
            xnew =  alpha*x + self._minvariable
            hnew.Fill(xnew,y)
          
          hnew.SetFillColor(histo.GetFillColor())
          hnew.SetLineColor(histo.GetLineColor())
          hnew.SetFillStyle(histo.GetFillStyle())
          
          return hnew
        
        else : 
          #
          # variable bin width
          #
          
          nbins = histo.GetXaxis().GetNbins()

          hnew = ROOT.TH1F("new_" + histo.GetName(),"", len(self._binning)-1, array('d', self._binning ))
          for ibin in range (0, nbins+1) :
            y = histo.GetBinContent(ibin)
            x = histo.GetXaxis().GetBinCenter(ibin)
            hnew.SetBinContent(ibin,y)
          
          hnew.SetFillColor(histo.GetFillColor())
          hnew.SetLineColor(histo.GetLineColor())
          hnew.SetFillStyle(histo.GetFillStyle())
          
          return hnew
        
   


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
 
   ## _____________________________________________________________________________
   ## --- poissonian error bayesian 1sigma band
   ##                                      1/0   1/0
    #def GetPoissError(self, numberEvents, down, up):
       #alpha = (1-0.6827)
       #L = 0
       #if numberEvents!=0 : 
         #L = ROOT.Math.gamma_quantile (alpha/2,numberEvents,1.)
       #U = 0
       #if numberEvents==0 :
         #U = ROOT.Math.gamma_quantile_c (alpha,numberEvents+1,1.) 
         ##print "u = ", U
       #else :
         #U = ROOT.Math.gamma_quantile_c (alpha/2,numberEvents+1,1.)
         
       ## the error
       #L = numberEvents - L
       #if numberEvents > 0 :
         #U = U - numberEvents
       ##else :
         ##U = 1.14 # --> bayesian interval Poisson with 0 events observed
         ##1.14790758039 from 10 lines above
         
       #if up and not down :
         #return U
       #if down and not up :
         #return L
       #if up and down :
         #return (L,U)
                  
   # _____________________________________________________________________________
    def GetMaximumIncludingErrors(self, histo):
        maxWithErrors = 0.
        lastBin = histo.GetNbinsX() if self._removeOverflow==True else histo.GetNbinsX()+1
        for iBin in range(1, lastBin):
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
    parser.add_option('--inputCutsList'  , dest='inputCutsList'  , help='input cuts list with histograms already weighted', default='input_cuts_merge.py')
    parser.add_option('--variable'       , dest='variable'       , help='input variable', default='myVariable')
    parser.add_option('--variableHR'     , dest='variableHR'     , help='input variable name', default='myVariable')
    parser.add_option('--minvariable'    , dest='minvariable'    , help='input variable min', default=0.   ,    type=float)
    parser.add_option('--maxvariable'    , dest='maxvariable'    , help='input variable max', default=10.  ,    type=float)
    parser.add_option('--getVarFromFile' , dest='getVarFromFile' , help='get variable, binning and range from file. Needed for variable bin width (set to 1 to trigger this)', default=0   ,    type=int)
    parser.add_option('--divideByBinWidth' , dest='divideByBinWidth'   , help='divide the bin content by the bin width'     , action='store_true', default=False)
    parser.add_option('--removeOverflow' , dest='removeOverflow'   , help='remove the overflow bin'     , action='store_true', default=False)
    parser.add_option('--invertXY' ,       dest='invertXY'       , help='invert XY axes to make Y projections'     , action='store_true', default=False)


          
    # read default parsing options as well
    hwwtools.addOptions(parser)
    hwwtools.loadOptDefaults(parser)
    (opt, args) = parser.parse_args()

    sys.argv.append( '-b' )
    ROOT.gROOT.SetBatch()


    print " configuration file = ", opt.pycfg
    print " lumi =               ", opt.lumi
    
    print " variable =           ", opt.variable
    print " variableHR =         ", opt.variableHR
    print " minvariable =        ", opt.minvariable
    print " maxvariable =        ", opt.maxvariable

    print " inputCutsList  =     ", opt.inputCutsList
    print " outputDirPlots =     ", opt.outputDirPlots
    
    print " minLogC   =          ", opt.minLogC
    print " maxLogC   =          ", opt.maxLogC

    print " minLogCratio   =          ", opt.minLogCratio
    print " maxLogCratio   =          ", opt.maxLogCratio

    print " divideByBinWidth =        ", opt.divideByBinWidth

    print " removeOverflow =        ", opt.removeOverflow

    print " invertXY =        ", opt.invertXY



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
    
    factory._minLogC = opt.minLogC 
    factory._maxLogC = opt.maxLogC 
    factory._minLogCratio = opt.minLogCratio
    factory._maxLogCratio = opt.maxLogCratio

    factory._variable = opt.variable
    factory._variableHR = opt.variableHR
    factory._minvariable = 1.* opt.minvariable
    factory._maxvariable = 1.* opt.maxvariable

    factory._divideByBinWidth = opt.divideByBinWidth

    factory._removeOverflow = opt.removeOverflow

    #
    # get variables: needed in case you started from 2D plot
    # and weighted it.
    # NB: In this case minvariable and maxvariable will be overloaded
    #
    
    factory._binning = []
    if opt.getVarFromFile == 1 :
      variables = {}
      if os.path.exists(opt.variablesFile) :
        handle = open(opt.variablesFile,'r')
        exec(handle)
        handle.close()
      if factory._variable in  variables.keys() :
        if 'range' in variables[factory._variable] :
          binning_possibly_in_2d = variables[factory._variable]['range']
          #
          # transform 2D into 1D
          # and beg bin edges if required
          #
          
          now_1d_binning = []
          
          # example A: (10, 0,100)
          if len( binning_possibly_in_2d ) == 3 :
            n_x =   binning_possibly_in_2d[0]
            min_x = binning_possibly_in_2d[1]
            max_x = binning_possibly_in_2d[2]
            now_1d_binning = [1.*i*((max_x-min_x)/n_x + min_x) for i in range(n_x+1)  ]
            # -->   0, 10, 20, ... , 90
          
          # example B: ([60,80,90,110,130,150,200],), 
          elif len( binning_possibly_in_2d ) == 1 :
            now_1d_binning = binning_possibly_in_2d[0]
            
          # example C: ([60,80,90,110,130,150,200],[10,20,30,50,70,90,150],), 
          #   -> NB: the two variables are defined as y:x, then it's the second that we care about
          elif len( binning_possibly_in_2d ) == 2 :
            if opt.invertXY:
              now_1d_binning = binning_possibly_in_2d[0]
            else:
              now_1d_binning = binning_possibly_in_2d[1]
          
          
          factory._binning = now_1d_binning

     
    print " binning = ", factory._binning
    
    
    cutsToMerge = {}
    if os.path.exists(opt.inputCutsList) :
      handle = open(opt.inputCutsList,'r')
      exec(handle)
      handle.close()
    
    groupPlot = OrderedDict()
    plot = {}
    legend = {}
    if os.path.exists(opt.plotFile) :
      handle = open(opt.plotFile,'r')
      exec(handle)
      handle.close()
   
   
    factory.makeCombinedPlot( opt.outputDirPlots, cutsToMerge, plot, legend, groupPlot)
    
    print '... and now closing ...'
        
       
