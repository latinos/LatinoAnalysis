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
    def makePlot(self, inputFile, outputDir, variables, cuts, samples, plot):

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
             
            thsSignal     = ROOT.THStack ("thsSignal","thsSignal")
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
            for sampleName, sample in self._samples.iteritems():
              if plot[sampleName]['isData'] == 1 :
                histos[sampleName].Draw("p same")

  

               
            #---- the Legend
            legend = ROOT.TLegend(0.2, 0.7, 0.8, 0.9)
            legend.SetFillColor(0)
            legend.SetLineColor(0)
            legend.SetShadowColor(0)
            for sampleName, sample in self._samples.iteritems():
              if plot[sampleName]['isData'] == 0 :
                legend.AddEntry(histos[sampleName], sampleName, "F")
             
            for sampleName, sample in self._samples.iteritems():
              if plot[sampleName]['isData'] == 1 :
                legend.AddEntry(histos[sampleName], "DATA", "P")
             
            legend.SetNColumns(2)
            legend.Draw()
            #print "- draw legend"
            #---- the Legend (end)
            
            frame.GetYaxis().SetRangeUser( 0, maxYused )
            tcanvas.SaveAs(self._outputDir + "/" + canvasNameTemplate + ".png")
            tcanvas.SaveAs(self._outputDir + "/" + canvasNameTemplate + ".root")
             
            # log Y axis
            frame.GetYaxis().SetRangeUser( max(0.01, maxYused/1000), 10 * maxYused )
            tcanvas.SetLogy()
            tcanvas.SaveAs(self._outputDir + "/log_" + canvasNameTemplate + ".png")
            
            
            
            
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
    if os.path.exists(opt.plotFile) :
      handle = open(opt.plotFile,'r')
      exec(handle)
      handle.close()
    
   
    factory.makePlot( opt.inputFile ,opt.outputDir, variables, cuts, samples, plot)
    
        
       