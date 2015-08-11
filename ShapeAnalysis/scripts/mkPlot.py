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



# ----------------------------------------------------- ShapeFactory --------------------------------------

class ShapeFactory:
    _logger = logging.getLogger('ShapeFactory')
 
    # _____________________________________________________________________________
    def __init__(self):
        self._stdWgt = 'baseW*puW*effW*triggW'
        self._systByWeight = {}
      
        variables = {}
        self._variables = variables

        cuts = {}
        self._cuts = cuts

        samples = {}
        self._samples = samples

        outputDir = {}
        self._outputDir = outputDir

    # _____________________________________________________________________________
    def makePlot(self, inputFile, outputDir, variables, cuts, samples, plot, legend):

        print "=================="
        print "==== makePlot ===="
        print "=================="
        
        self.defineStyle()
        
        self._variables = variables
        self._samples   = samples
        self._cuts      = cuts

        self._outputDir = outputDir

        ROOT.TH1.SetDefaultSumw2(True)
        
        fileIn = ROOT.TFile(inputFile, "READ")
        #---- save one TCanvas for every cut and every variable
        for cutName in self._cuts :
          print "cut = ", cutName, " :: ", cuts[cutName]
          for variableName, variable in self._variables.iteritems():
            histos = {}
            canvasNameTemplate = 'c_' + cutName + "_" + variableName
            
            tcanvas = ROOT.TCanvas( canvasNameTemplate, variableName , 800, 600 )
             
            tgrData_vx     = array('f')
            tgrData_evx    = array('f')
            tgrData_vy     = array('f')
            tgrData_evy_up = array('f')
            tgrData_evy_do = array('f')
            
            thsData       = ROOT.THStack ("thsData",      "thsData")
            thsSignal     = ROOT.THStack ("thsSignal",    "thsSignal")
            thsBackground = ROOT.THStack ("thsBackground","thsBackground")

            for sampleName, sample in self._samples.iteritems():
              shapeName = cutName+"/"+variableName+'/histo_' + sampleName
              histo = fileIn.Get(shapeName)
              histos[sampleName] = histo.Clone('new_histo_' + sampleName)
              #print "     -> sampleName = ", sampleName, " --> ", histos[sampleName].GetTitle(), " --> ", histos[sampleName].GetName()

              # data style
              if plot[sampleName]['isData'] == 1 :
                histos[sampleName].SetMarkerColor(plot[sampleName]['color'])
                histos[sampleName].SetMarkerSize(1)
                histos[sampleName].SetMarkerStyle(20)
                histos[sampleName].SetLineColor(plot[sampleName]['color'])
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
                    

              # MC style
              if plot[sampleName]['isData'] == 0 :
                histos[sampleName].SetFillColor(plot[sampleName]['color'])
                histos[sampleName].SetFillStyle(3001)
                histos[sampleName].SetLineColor(plot[sampleName]['color'])
                # scale to luminosity if MC
                histos[sampleName].Scale(self._lumi)
                
                if plot[sampleName]['isSignal'] == 1 :
                  thsSignal.Add(histos[sampleName])
                else :
                  thsBackground.Add(histos[sampleName])

            tgrData       = ROOT.TGraphAsymmErrors()
            for iBin in range(0, len(tgrData_vx)) : 
              tgrData.SetPoint     (iBin, tgrData_vx[iBin], tgrData_vy[iBin])
              tgrData.SetPointError(iBin, tgrData_evx[iBin], tgrData_evx[iBin], tgrData_evy_do[iBin], tgrData_evy_up[iBin])
            
            tgrDataOverMC = tgrData.Clone("tgrDataOverMC")
            for iBin in range(0, len(tgrData_vx)) : 
              tgrDataOverMC.SetPoint     (iBin, tgrData_vx[iBin], self.Ratio(tgrData_vy[iBin] , thsBackground.GetStack().Last().GetBinContent(iBin+1)) )
              tgrDataOverMC.SetPointError(iBin, tgrData_evx[iBin], tgrData_evx[iBin], self.Ratio(tgrData_evy_do[iBin], thsBackground.GetStack().Last().GetBinContent(iBin+1)) , self.Ratio(tgrData_evy_up[iBin], thsBackground.GetStack().Last().GetBinContent(iBin+1)) )
            
            
            
            #---- now plot
            
            
            #  - get axis range
            minXused = 0.
            maxXused = 1.

            maxYused = 1.
            scaleToPlot = 2.5
            
            for sampleName, sample in self._samples.iteritems():
              if plot[sampleName]['isData'] == 1 :
                histos[sampleName].Draw("p")
                minXused = histos[sampleName].GetXaxis().GetBinLowEdge(1)
                maxXused = histos[sampleName].GetXaxis().GetBinUpEdge(histos[sampleName].GetNbinsX()+1)
                maxY = self.GetMaximumIncludingErrors(histos[sampleName])
                histos[sampleName].SetMaximum(scaleToPlot * maxY)
                maxYused = scaleToPlot * maxY
            
            if thsBackground.GetNhists() != 0:
              thsBackground.Draw("hist")
              maxY = thsBackground.GetMaximum ()
              minXused = thsBackground.GetXaxis().GetBinLowEdge(1)
              maxXused = thsBackground.GetXaxis().GetBinUpEdge(thsBackground.GetHistogram().GetNbinsX()+1)
              if (scaleToPlot * maxY) > maxYused :
                maxYused = scaleToPlot * maxY
               
            if thsSignal.GetNhists() != 0:
              thsSignal.Draw("hist")
              maxY = thsSignal.GetMaximum ()
              minXused = thsSignal.GetXaxis().GetBinLowEdge(1)
              maxXused = thsSignal.GetXaxis().GetBinUpEdge(thsSignal.GetHistogram().GetNbinsX()+1)
              if (scaleToPlot * maxY) > maxYused :
                maxYused = scaleToPlot * maxY


            #print " X axis = ", minXused, " - ", maxXused
            frame = ROOT.TH1F
            frame = tcanvas.DrawFrame(minXused, 0.0, maxXused, 1.0)

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
            for sampleName, sample in self._samples.iteritems():
              if plot[sampleName]['isData'] == 0 :
                tlegend.AddEntry(histos[sampleName], sampleName, "F")
             
            for sampleName, sample in self._samples.iteritems():
              if plot[sampleName]['isData'] == 1 :
                tlegend.AddEntry(histos[sampleName], "DATA", "P")
             
            tlegend.SetNColumns(2)
            tlegend.Draw()
            
            if 'lumi' in legend.keys() and 'sqrt' not in legend.keys():
              flag_lumi = ROOT.TLatex (minXused + (maxXused-minXused)*3./4., 0 + (maxYused-0)*3./4., legend['lumi'])
              flag_lumi.Draw()
            if 'sqrt' in legend.keys() and 'lumi' not in legend.keys():
              flag_sqrt = ROOT.TLatex (minXused + (maxXused-minXused)*3./4., 0 + (maxYused-0)*2.5/4., legend['sqrt'])
              flag_sqrt.Draw()
            if 'sqrt' in legend.keys() and 'lumi' in legend.keys():
              flag_lumi_sqrt = ROOT.TLatex (minXused + (maxXused-minXused)*3./4., 0 + (maxYused-0)*2.5/4., "#splitline{" +  legend['lumi'] + "}{" + legend['sqrt'] + "}")
              flag_lumi_sqrt.Draw()
    
    
            #print "- draw tlegend"
            #---- the Legend (end)
            
            frame.GetYaxis().SetRangeUser( 0, maxYused )
            tcanvas.SaveAs(self._outputDir + "/" + canvasNameTemplate + ".png")
            tcanvas.SaveAs(self._outputDir + "/" + canvasNameTemplate + ".root")
             
            # log Y axis
            frame.GetYaxis().SetRangeUser( max(0.01, maxYused/1000), 10 * maxYused )
            tcanvas.SetLogy()
            tcanvas.SaveAs(self._outputDir + "/log_" + canvasNameTemplate + ".png")
            
            # ~~~~~~~~~~~~~~~~~~~~
            # plot with ratio plot            
            
            canvasRatioNameTemplate = 'cratio_' + cutName + "_" + variableName
            tcanvasRatio = ROOT.TCanvas( canvasRatioNameTemplate, canvasRatioNameTemplate , 800, 800 )

            tcanvasRatio.cd()
            pad1 = ROOT.TPad("pad1","pad1", 0, 1-0.72, 1, 1)
            pad1.SetTopMargin(0.098)
            pad1.SetBottomMargin(0.000) 
            pad1.Draw()
            pad1.cd().SetGrid()
            
            print " pad1 = ", pad1
            frameDistro = pad1.DrawFrame(minXused, 0.0, maxXused, 1.0)
            print " pad1 = ", pad1
            
            if 'xaxis' in variable.keys() : 
              frameDistro.GetXaxis().SetTitle(variable['xaxis'])
            else :
              frameDistro.GetXaxis().SetTitle(variableName)
            frameDistro.GetYaxis().SetTitle("Events")
            frameDistro.GetYaxis().SetRangeUser( 0, maxYused )
            
            if thsBackground.GetNhists() != 0:
              thsBackground.Draw("hist same")
               
            if thsSignal.GetNhists() != 0:
              thsSignal.Draw("hist same")
              
            #     - then the DATA  
            if tgrData.GetN() != 0:
              tgrData.Draw("P0")
    
            tlegend.Draw()
            if 'lumi' in legend.keys() and 'sqrt' not in legend.keys():
              flag_lumi = ROOT.TLatex (minXused + (maxXused-minXused)*3./4., 0 + (maxYused-0)*3./4., legend['lumi'])
              flag_lumi.Draw()
            if 'sqrt' in legend.keys() and 'lumi' not in legend.keys():
              flag_sqrt = ROOT.TLatex (minXused + (maxXused-minXused)*3./4., 0 + (maxYused-0)*2.5/4., legend['sqrt'])
              flag_sqrt.Draw()
            if 'sqrt' in legend.keys() and 'lumi' in legend.keys():
              flag_lumi_sqrt = ROOT.TLatex (minXused + (maxXused-minXused)*3./4., 0 + (maxYused-0)*2.5/4., "#splitline{" +  legend['lumi'] + "}{" + legend['sqrt'] + "}")
              flag_lumi_sqrt.Draw()
            
            tcanvasRatio.cd()
            pad2 = ROOT.TPad("pad2","pad2",0,0,1,1-0.72)
            pad2.SetTopMargin(0.000)
            pad2.SetBottomMargin(0.392)
            pad2.Draw()
            pad2.cd().SetGrid()
           
            print " pad1 = ", pad1
            print " pad2 = ", pad2
            frameRatio = pad2.DrawFrame(minXused, 0.0, maxXused, 2.0)
            print " pad2 = ", pad2
            if 'xaxis' in variable.keys() : 
              frameRatio.GetXaxis().SetTitle(variable['xaxis'])
            else :
              frameRatio.GetXaxis().SetTitle(variableName)
            frameRatio.GetYaxis().SetTitle("Data/MC")
            frameRatio.GetYaxis().SetRangeUser( 0.0, 2.0 )
           
            tgrDataOverMC.Draw("P0")
            
            tcanvasRatio.SaveAs(self._outputDir + "/" + canvasRatioNameTemplate + ".png")
            tcanvasRatio.SaveAs(self._outputDir + "/" + canvasRatioNameTemplate + ".root")
            
            
            # log Y axis
            frameDistro.GetYaxis().SetRangeUser( max(0.01, maxYused/1000), 10 * maxYused )
            pad1.SetLogy()
            tcanvasRatio.SaveAs(self._outputDir + "/log_" + canvasRatioNameTemplate + ".png")
            
          
          
            print " >> end"
            
          print " >> all end"
            
            
   # _____________________________________________________________________________
   # --- squared sum
    def SumQ(self, A, B):
       return sqrt(A*A + B*B)

   # _____________________________________________________________________________
   # --- Ratio: if denominator is zero, then put 0!
    def Ratio(self, A, B):
       if B == 0: 
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
       else :
         U = ROOT.Math.gamma_quantile_c (alpha/2,numberEvents+1,1.)
         
       # the error
       L = numberEvents - L
       if numberEvents > 0 :
         U = U - numberEvents
       else :
         U = 1.14 # --> bayesian interval Poisson with 0 events observed
       
       if up and not down :
         return L
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

    parser.add_option('--outputDir'      , dest='outputDir'      , help='output directory'                           , default='./')
    parser.add_option('--inputFile'      , dest='inputFile'      , help='input file with histograms'                 , default='input.root')
          
    # read default pargin options as well
    hwwtools.addOptions(parser)
    hwwtools.loadOptDefaults(parser)
    (opt, args) = parser.parse_args()

    sys.argv.append( '-b' )
    ROOT.gROOT.SetBatch()


    print " configuration file = ", opt.pycfg
    print " lumi =               ", opt.lumi
    
    print " inputFile =          ", opt.inputFile
    print " outputDir =          ", opt.outputDir
 
    

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
    
    samples = {}
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
    
   
    factory.makePlot( opt.inputFile ,opt.outputDir, variables, cuts, samples, plot, legend)
    
        
       