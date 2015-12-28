#!/usr/bin/env python

import json
import sys
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

import os.path



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

    # _____________________________________________________________________________
    def makePlot(self, inputFile, outputDirPlots, variables, cuts, samples, plot, nuisances, legend):

        print "=================="
        print "==== makePlot ===="
        print "=================="
        
        self.defineStyle()
        
        self._variables = variables
        self._samples   = samples
        self._cuts      = cuts

        self._outputDirPlots = outputDirPlots
        os.system ("mkdir " + outputDirPlots + "/") 
        

        tcanvas      = ROOT.TCanvas( "cc",      "cc"     , 800, 600 )
        tcanvasRatio = ROOT.TCanvas( "ccRatio", "ccRatio", 800, 800 )

        ROOT.TH1.SetDefaultSumw2(True)
        
        fileIn = ROOT.TFile(inputFile, "READ")
        #---- save one TCanvas for every cut and every variable
        for cutName in self._cuts :
          print "cut = ", cutName, " :: ", cuts[cutName]
          for variableName, variable in self._variables.iteritems():
            histos = {}
            canvasNameTemplate = 'c_' + cutName + "_" + variableName
            
            #tcanvas = ROOT.TCanvas( canvasNameTemplate, variableName , 800, 600 )
            tcanvas.cd()
            
            tgrData_vx     = array('f')
            tgrData_evx    = array('f')
            tgrData_vy     = array('f')
            tgrData_evy_up = array('f')
            tgrData_evy_do = array('f')

            #these vectors are needed for nuisances accounting
            nuisances_vy_up     = {}
            nuisances_vy_do     = {}
            tgrMC_vy         = array('f')
 
            
            thsData       = ROOT.THStack ("thsData",      "thsData")
            thsSignal     = ROOT.THStack ("thsSignal",    "thsSignal")
            thsBackground = ROOT.THStack ("thsBackground","thsBackground")

            for sampleName, sample in self._samples.iteritems():
              shapeName = cutName+"/"+variableName+'/histo_' + sampleName
              histo = fileIn.Get(shapeName)
              histos[sampleName] = histo.Clone('new_histo_' + sampleName)
              #print "     -> sampleName = ", sampleName, " --> ", histos[sampleName].GetTitle(), " --> ", histos[sampleName].GetName(), " --> ", histos[sampleName].GetNbinsX()

              # data style
              if plot[sampleName]['isData'] == 1 :
                histos[sampleName].SetMarkerColor(plot[sampleName]['color'])
                histos[sampleName].SetMarkerSize(1)
                histos[sampleName].SetMarkerStyle(20)
                histos[sampleName].SetLineColor(plot[sampleName]['color'])
                
                # blind data
                if 'isBlind' in plot[sampleName].keys() :
                  if plot[sampleName]['isBlind'] == 1 :
                    for iBin in range(1, histos[sampleName].GetNbinsX()+1):
                      histos[sampleName].SetBinContent(iBin, 0)
                
                
                thsData.Add(histos[sampleName])

                # first time fill vectors X axis
                if len(tgrData_vx) == 0 :
                  for iBin in range(1, histos[sampleName].GetNbinsX()+1):
                    tgrData_vx.append(  histos[sampleName].GetBinCenter (iBin))
                    tgrData_evx.append( histos[sampleName].GetBinWidth (iBin) / 2.)                  
                    tgrData_vy.append(  histos[sampleName].GetBinContent (iBin))
                    tgrData_evy_up.append( self.GetPoissError(histos[sampleName].GetBinContent (iBin) , 0, 1) )
                    tgrData_evy_do.append( self.GetPoissError(histos[sampleName].GetBinContent (iBin) , 1, 0) )
                else :
                  for iBin in range(1, histos[sampleName].GetNbinsX()+1):
                    tgrData_vx[iBin-1] = (  histos[sampleName].GetBinCenter (iBin))
                    tgrData_evx.append( histos[sampleName].GetBinWidth (iBin) / 2.)                  
                    tgrData_vy[iBin-1] += histos[sampleName].GetBinContent (iBin)
                    tgrData_evy_up[iBin-1] = SumQ ( tgrData_evy_up[iBin-1], self.GetPoissError(histos[sampleName].GetBinContent (iBin) , 0, 1) )
                    tgrData_evy_do[iBin-1] = SumQ ( tgrData_evy_do[iBin-1], self.GetPoissError(histos[sampleName].GetBinContent (iBin) , 1, 0) )
                    
                    
              # allow arbitrary scaling in MC (and DATA??), if needed
              # for example to "see" a signal
              if 'scale' in plot[sampleName].keys() : 
                histos[sampleName].Scale(plot[sampleName]['scale'])
                print " >> scale ", sampleName, " to ", plot[sampleName]['scale']

              # MC style
              if plot[sampleName]['isData'] == 0 :
                # only background "filled" histogram
                if plot[sampleName]['isSignal'] == 0 : 
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
                else :
                  thsBackground.Add(histos[sampleName])
                    
                for nuisance in nuisances.keys():
                  shapeNameUp = cutName+"/"+variableName+'/histo_' + sampleName+"_"+nuisance+"Up"
                  print "loading shape variation", shapeNameUp
                  histoUp = fileIn.Get(shapeNameUp)
                  shapeNameDown = cutName+"/"+variableName+'/histo_' + sampleName+"_"+nuisance+"Down"
                  print "loading shape variation", shapeNameDown
                  histoDown = fileIn.Get(shapeNameDown)
                  if histoUp == None:
                    print "Warning! No", nuisance, " up variation for", sampleName
                  if histoDown == None:
                    print "Warning! No", nuisance, " down variation for", sampleName
                  if nuisance not in nuisances_vy_up.keys() or nuisance not in nuisances_vy_do.keys():  
                    nuisances_vy_up[nuisance] = array('f')
                    nuisances_vy_do[nuisance] = array('f')
                  if len(tgrMC_vy) == 0:
                    for iBin in range(1, histos[sampleName].GetNbinsX()+1):
                      tgrMC_vy.append(0.)
                  if (len(nuisances_vy_up[nuisance]) == 0):
                    for iBin in range(1, histos[sampleName].GetNbinsX()+1):
                      nuisances_vy_up[nuisance].append(0.)
                  if (len(nuisances_vy_do[nuisance]) == 0):
                    for iBin in range(1, histos[sampleName].GetNbinsX()+1):
                      nuisances_vy_do[nuisance].append(0.)
                  for iBin in range(1, histos[sampleName].GetNbinsX()+1):
                    tgrMC_vy[iBin-1] += histos[sampleName].GetBinContent (iBin)
                    if histoUp != None:
                      nuisances_vy_up[nuisance][iBin-1] += histoUp.GetBinContent (iBin)
                    else:
                      #add the central sample 
                      nuisances_vy_up[nuisance][iBin-1] += histos[sampleName].GetBinContent (iBin)  
                    if histoDown != None:  
                      nuisances_vy_do[nuisance][iBin-1] += histoDown.GetBinContent (iBin)
                    else:
                      #add the central sample 
                      nuisances_vy_do[nuisance][iBin-1] += histos[sampleName].GetBinContent (iBin)
                                            

                #else :
                #  for iBin in range(1, histos[sampleName].GetNbinsX()+1):
                #    tgrBkg_vx[iBin-1] = (  histos[sampleName].GetBinCenter (iBin))
                #    tgrBkg_evx.append( histos[sampleName].GetBinWidth (iBin) / 2.)
                #    tgrBkg_vy[iBin-1] += histos[sampleName].GetBinContent (iBin)
                #    tgrBkg_evy_up[iBin-1] = SumQ ( tgrBkg_evy_up[iBin-1], self.GetPoissError(histos[sampleName].GetBinContent (iBin) , 0, 1) )
                #    tgrBkg_evy_do[iBin-1] = SumQ ( tgrBkg_evy_do[iBin-1], self.GetPoissError(histos[sampleName].GetBinContent (iBin) , 1, 0) ) 

            nuisances_err_up = array('f')
            nuisances_err_do = array('f')
            for nuisance in nuisances.keys():
              if len(nuisances_err_up) == 0 : 
                for iBin in range(len(tgrMC_vy)):
                  nuisances_err_up.append(0.)
                  nuisances_err_do.append(0.)
              # now we need to tell wthether the variation is actually up or down ans sum in quadrature those with the same sign 
              for iBin in range(len(tgrMC_vy)):
                #print "bin", iBin, " nuisances_vy_up[nuisance][iBin]", nuisances_vy_up[nuisance][iBin], " central", tgrMC_vy[iBin] 
                if nuisances_vy_up[nuisance][iBin] - tgrMC_vy[iBin] > 0:
                  nuisances_err_up[iBin] = self.SumQ (nuisances_err_up[iBin], nuisances_vy_up[nuisance][iBin] - tgrMC_vy[iBin])
                  nuisances_err_do[iBin] = self.SumQ (nuisances_err_do[iBin], nuisances_vy_do[nuisance][iBin] - tgrMC_vy[iBin])
                else:
                  nuisances_err_up[iBin] = self.SumQ (nuisances_err_up[iBin], nuisances_vy_do[nuisance][iBin] - tgrMC_vy[iBin])
                  nuisances_err_do[iBin] = self.SumQ (nuisances_err_do[iBin], nuisances_vy_up[nuisance][iBin] - tgrMC_vy[iBin]) 

              
            
            tgrData       = ROOT.TGraphAsymmErrors()
            for iBin in range(0, len(tgrData_vx)) : 
              tgrData.SetPoint     (iBin, tgrData_vx[iBin], tgrData_vy[iBin])
              tgrData.SetPointError(iBin, tgrData_evx[iBin], tgrData_evx[iBin], tgrData_evy_do[iBin], tgrData_evy_up[iBin])
            
            tgrDataOverMC = tgrData.Clone("tgrDataOverMC")
            for iBin in range(0, len(tgrData_vx)) : 
              tgrDataOverMC.SetPoint     (iBin, tgrData_vx[iBin], self.Ratio(tgrData_vy[iBin] , thsBackground.GetStack().Last().GetBinContent(iBin+1)) )
              tgrDataOverMC.SetPointError(iBin, tgrData_evx[iBin], tgrData_evx[iBin], self.Ratio(tgrData_evy_do[iBin], thsBackground.GetStack().Last().GetBinContent(iBin+1)) , self.Ratio(tgrData_evy_up[iBin], thsBackground.GetStack().Last().GetBinContent(iBin+1)) )
            
            if len(nuisances.keys()) != 0:
              tgrMC = ROOT.TGraphAsymmErrors()  
              for iBin in range(0, len(tgrData_vx)) :
                tgrMC.SetPoint     (iBin, tgrData_vx[iBin], tgrMC_vy[iBin])
                tgrMC.SetPointError(iBin, tgrData_evx[iBin], tgrData_evx[iBin], nuisances_err_do[iBin], nuisances_err_up[iBin])
              
              tgrMCOverMC = tgrMC.Clone("tgrMCOverMC")  
              for iBin in range(0, len(tgrData_vx)) :
                tgrMCOverMC.SetPoint     (iBin, tgrData_vx[iBin], 1.)
                tgrMCOverMC.SetPointError(iBin, tgrData_evx[iBin], tgrData_evx[iBin], self.Ratio(nuisances_err_do[iBin], tgrMC_vy[iBin]), self.Ratio(nuisances_err_up[iBin], tgrMC_vy[iBin]))     
                
                         
            
            #---- now plot
            
            
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

            #  - now draw
            #     - first the MC                        
            if thsBackground.GetNhists() != 0:
              thsBackground.Draw("hist same")
               
            if thsSignal.GetNhists() != 0:
              thsSignal.Draw("hist same")
            
            # if there is a systematic band draw it
            if len(nuisances.keys()) != 0:
              tgrMC.SetLineColor(12)
              tgrMC.SetFillColor(12)
              tgrMC.SetFillStyle(3004)
              tgrMCOverMC.SetLineColor(12)
              tgrMCOverMC.SetFillColor(12)
              tgrMCOverMC.SetFillStyle(3004)
              tgrMC.Draw("2")

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
            
            for sampleName, sample in reversedSamples.iteritems():
              if plot[sampleName]['isData'] == 0 :
                if 'nameHR' in plot[sampleName].keys() :
                  tlegend.AddEntry(histos[sampleName], plot[sampleName]['nameHR'], "F")
                else :
                  tlegend.AddEntry(histos[sampleName], sampleName, "F")
             
            for sampleName, sample in reversedSamples.iteritems():
              if plot[sampleName]['isData'] == 1 :
                if 'nameHR' in plot[sampleName].keys() :
                  tlegend.AddEntry(histos[sampleName], plot[sampleName]['nameHR'], "EPL")
                else :
                  tlegend.AddEntry(histos[sampleName], sampleName, "EPL")
            if len(nuisances.keys()) != 0:
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

    
            print "- draw tlegend"
            #---- the Legend (end)
            tlegend.Draw()


            frame.GetYaxis().SetRangeUser( 0, maxYused )
            # draw back all the axes            
            #frame.Draw("AXIS")
            tcanvas.RedrawAxis()
            
            tcanvas.SaveAs(self._outputDirPlots + "/" + canvasNameTemplate + ".png")
            tcanvas.SaveAs(self._outputDirPlots + "/" + canvasNameTemplate + ".root")
             
            # log Y axis
            frame.GetYaxis().SetRangeUser( max(0.01, minYused), 100 * maxYused )
            tcanvas.SetLogy()
            tcanvas.SaveAs(self._outputDirPlots + "/log_" + canvasNameTemplate + ".png")
            tcanvas.SetLogy(0)


            
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
            print " pad1 = ", pad1
            canvasFrameDistroName = 'frame_distro_' + cutName + "_" + variableName
            frameDistro = pad1.DrawFrame(minXused, 0.0, maxXused, 1.0, canvasFrameDistroName)
            print " pad1 = ", pad1
            
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

            if thsBackground.GetNhists() != 0:
              thsBackground.Draw("hist same")
               
            if thsSignal.GetNhists() != 0:
              thsSignal.Draw("hist same")
           
            if (len(nuisances.keys())!=0):
              tgrMC.Draw("2")

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
            
            print " pad1 = ", pad1
            print " pad2 = ", pad2, " minXused = ", minXused, " maxXused = ", maxXused
            canvasFrameRatioName = 'frame_ratio_' + cutName + "_" + variableName
            print " canvasFrameRatioName = ", canvasFrameRatioName
            frameRatio = pad2.DrawFrame(minXused, 0.0, maxXused, 2.0, canvasFrameRatioName)
            print " pad2 = ", pad2
            # style from https://ghm.web.cern.ch/ghm/plots/MacroExample/myMacro.py
            xAxisDistro = frameRatio.GetXaxis()
            xAxisDistro.SetNdivisions(6,5,0)

            if 'xaxis' in variable.keys() : 
              frameRatio.GetXaxis().SetTitle(variable['xaxis'])
            else :
              frameRatio.GetXaxis().SetTitle(variableName)
            frameRatio.GetYaxis().SetTitle("Data/Expected")
            #frameRatio.GetYaxis().SetTitle("Data/MC")
            frameRatio.GetYaxis().SetRangeUser( 0.0, 2.0 )
            self.Pad2TAxis(frameRatio)
            if (len(nuisances.keys())!=0):
              tgrMCOverMC.Draw("2") 
            
            tgrDataOverMC.Draw("P0")
            
            oneLine2 = ROOT.TLine(frameRatio.GetXaxis().GetXmin(), 1,  frameRatio.GetXaxis().GetXmax(), 1);
            oneLine2.SetLineStyle(3)
            oneLine2.SetLineWidth(3)
            oneLine2.Draw("same")

            # draw back all the axes            
            #frameRatio.Draw("AXIS")
            pad2.RedrawAxis()
            
            tcanvasRatio.SaveAs(self._outputDirPlots + "/" + canvasRatioNameTemplate + ".png")
            tcanvasRatio.SaveAs(self._outputDirPlots + "/" + canvasRatioNameTemplate + ".root")
            
            
            # log Y axis
            frameDistro.GetYaxis().SetRangeUser( max(0.001, maxYused/1000), 10 * maxYused )
            pad1.SetLogy()
            tcanvasRatio.SaveAs(self._outputDirPlots + "/log_" + canvasRatioNameTemplate + ".png")
            pad1.SetLogy(0)


          
          
            print " >> end"
            
          print " >> all end"



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

    parser.add_option('--outputDirPlots' , dest='outputDirPlots' , help='output directory'                           , default='./')
    parser.add_option('--inputFile'      , dest='inputFile'      , help='input file with histograms'                 , default='input.root')
    parser.add_option('--nuisancesFile'  , dest='nuisancesFile'  , help='file with nuisances configurations'         , default=None )
          
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
   
    factory.makePlot( opt.inputFile ,opt.outputDirPlots, variables, cuts, samples, plot, nuisances, legend)
    
        
       
