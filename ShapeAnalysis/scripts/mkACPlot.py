#!/usr/bin/env python

import optparse
import LatinoAnalysis.Gardener.hwwtools as hwwtools
from collections import OrderedDict

import os
import os.path

# ROOT
import ROOT
from ROOT import *

# functions used in everyday life ...
from LatinoAnalysis.Tools.commonTools import *
import LatinoAnalysis.Tools.rootlogonTDR

# PlotFactory
from LatinoAnalysis.ShapeAnalysis.PlotFactory import PlotFactory

def SaveCanvas(c1,Name):
    c1.SaveAs(opt.outputDirPlots+'/'+Name+'.pdf')
    c1.SaveAs(opt.outputDirPlots+'/'+Name+'.png')
    c1.SaveAs(opt.outputDirPlots+'/'+Name+'.root')
    c1.SaveAs(opt.outputDirPlots+'/'+Name+'.C')

def var_getBinning(bins):

    binning = {}
    if not ( isinstance(bins, tuple) or isinstance(bins,list)):
      raise RuntimeError('bin must be an ntuple or an arrays')

    l = len(bins)        
    # 1D variable binning
    if   l == 1 and isinstance(bins[0],list):
      binning['ndim']  = 1
      binning['xbins'] = bins[0]
      binning['nBinX'] = len(bins[0])-1 
    # 2D variable binning 
    elif l == 2 and  isinstance(bins[0],list) and  isinstance(bins[1],list):
      binning['ndim']  = 2
      binning['xbins'] = bins[0]
      binning['ybins'] = bins[1]
      binning['nBinX'] = len(bins[0])-1 
      binning['nBinY'] = len(bins[1])-1 
    # 1D fix binning
    elif l == 3:
      binning['ndim']  = 1
      xbins = []
      wBin = (bins[2]-bins[1])/bins[0]
      for iBin in range(0,bins[0]+1) : 
        xbins.append(bins[1]+iBin*wBin) 
      binning['xbins'] = xbins  
      binning['nBinX'] = len(xbins)-1
    # 2D fix biining
    elif l == 6:
      binning['ndim']  = 2
      xbins = []
      wBin = (bins[2]-bins[1])/bins[0]
      for iBin in range(0,bins[0]+1) :
        xbins.append(bins[1]+iBin*wBin)
      binning['xbins'] = xbins
      binning['nBinX'] = len(xbins)-1
      ybins = []
      wBin = (bins[5]-bins[4])/bins[3]
      for iBin in range(0,bins[3]+1) :
        ybins.append(bins[4]+iBin*wBin)
      binning['ybins'] = ybins 
      binning['nBinY'] = len(ybins)-1
    else:
            raise RuntimeError('What a mess!!! bin malformed!')

    return binning

def plot_fits():

    gROOT.SetBatch()
    gStyle.SetOptTitle(0)
    gStyle.SetOptStat(0)
    gStyle.SetOptFit(0)

    fIn = ROOT.TFile.Open(opt.inputFitFile,'READ')

    for iCut in cuts:
      fIn.cd()
      for iVar in variables :
        binning = var_getBinning(variables[iVar]['range'])
        if   binning['ndim'] == 1 : nBins = binning['nBinX']
        elif binning['ndim'] == 2 : nBins = binning['nBinX']*binning['nBinY']
        for iDim in ['1D','2D'] :
          if iDim == '1D' : separator = '_par1_'
          if iDim == '2D' : separator = '_par2_'
          if iDim in acoupling['ScanConfig'] and len(acoupling['ScanConfig'][iDim]) > 0 :
            for iScan in acoupling['ScanConfig'][iDim]:
              fIn.cd(iCut+'/'+iVar+'/'+iScan.replace(":","_"))
              toPlot= {}
              Fits= {}
              keyList = ROOT.gDirectory.GetListOfKeys()
              for key in keyList:
                obj = key.ReadObj()
                if 'TH' in  obj.ClassName() : toPlot[int(obj.GetName().split(separator)[1])] = obj
                if 'TF' in  obj.ClassName() : Fits[int(obj.GetName().split(separator)[1])] = obj

              print toPlot
              for iBin in range(1,nBins+1):
                print iBin
                c1 = TCanvas("c1","c1",700,700)
                c1.cd()
                c1.SetRightMargin(0.05)
                c1.SetLeftMargin(0.20)
                c1.SetTopMargin(0.10)
                c1.SetBottomMargin(0.15)

                if iDim == '1D' : 
                  toPlot[iBin].GetXaxis().SetTitle(acoupling['operatorLatex'][iScan]+' ['+acoupling['operatorUnit'][iScan]+']')
                  toPlot[iBin].GetXaxis().SetLabelFont (   42)
                  toPlot[iBin].GetXaxis().SetTitleFont (   42)
                  toPlot[iBin].GetXaxis().SetTitleOffset( 1.4)
                  toPlot[iBin].GetXaxis().SetTitleSize (0.050)
                  toPlot[iBin].GetXaxis().SetLabelSize (0.045)
                 
                  toPlot[iBin].GetYaxis().SetTitle('#sigma_{TGC}/#sigma_{SM}')
                  toPlot[iBin].GetYaxis().SetLabelFont (   42)
                  toPlot[iBin].GetYaxis().SetTitleFont (   42)
                  toPlot[iBin].GetYaxis().SetTitleOffset( 2.0)
                  toPlot[iBin].GetYaxis().SetTitleSize (0.045)
                  toPlot[iBin].GetYaxis().SetLabelSize (0.040)

                if iDim == '2D' :
                  toPlot[iBin].GetXaxis().SetTitle(acoupling['operatorLatex'][iScan.split(":")[0]]+' ['+acoupling['operatorUnit'][iScan.split(":")[0]]+']')
                  toPlot[iBin].GetXaxis().SetLabelFont (   42)
                  toPlot[iBin].GetXaxis().SetTitleFont (   42)
                  toPlot[iBin].GetXaxis().SetTitleOffset( 1.4)
                  toPlot[iBin].GetXaxis().SetTitleSize (0.045)
                  toPlot[iBin].GetXaxis().SetLabelSize (0.040)
 
                  toPlot[iBin].GetYaxis().SetTitle(acoupling['operatorLatex'][iScan.split(":")[1]]+' ['+acoupling['operatorUnit'][iScan.split(":")[1]]+']')
                  toPlot[iBin].GetYaxis().SetLabelFont (   42)
                  toPlot[iBin].GetYaxis().SetTitleFont (   42)
                  toPlot[iBin].GetYaxis().SetTitleOffset( 1.6)
                  toPlot[iBin].GetYaxis().SetTitleSize (0.045)
                  toPlot[iBin].GetYaxis().SetLabelSize (0.040)

                  toPlot[iBin].GetZaxis().SetTitle('#sigma_{TGC}/#sigma_{SM}')
                  toPlot[iBin].GetZaxis().SetLabelFont (   42)
                  toPlot[iBin].GetZaxis().SetTitleFont (   42)
                  toPlot[iBin].GetZaxis().SetTitleOffset( 2.0)
                  toPlot[iBin].GetZaxis().SetTitleSize (0.045)
                  toPlot[iBin].GetZaxis().SetLabelSize (0.040)
 

                if iDim == '1D' : toPlot[iBin].Draw("hist")
                if iDim == '1D' : Fits[iBin].Draw("same")
                if iDim == '2D' : toPlot[iBin].Draw("lego")

                x1=0.20
                y1=0.90
                x2=0.99
                y2=0.98
                fontSize = 0.033

                cms = TPaveText(x1,y1,x2,y2,"brtlNDC");
                cms.SetTextSize(fontSize*1.3);
                cms.SetFillColor(0)
                cms.SetFillStyle(0)
                cms.SetLineStyle(0)
                cms.SetLineWidth(0)
                cms.SetTextAlign(11)
                cms.SetTextFont(61);
                cms.AddText("CMS");
                cms.SetBorderSize(0);
                cms.Draw("same");

                x1=0.3
                status = TPaveText(x1,y1*1.01,x2,y2,"brtlNDC");
                status.SetTextSize(fontSize);
                status.SetFillColor(0)
                status.SetFillStyle(0)
                status.SetLineStyle(0)
                status.SetLineWidth(0)
                status.SetTextAlign(11)
                status.SetTextFont(52);
                status.AddText("Simulation")
                status.SetBorderSize(0);
                status.Draw("same");
               
                SelText = '' 
                vName = variables[iVar]['xaxis'].split('[')[0]
                #vUnit = variables[iVar]['xaxis'].split('[')[1].replace(']','')
                vUnit = 'GeV'
                if binning['ndim'] == 1 : SelText = str(binning['xbins'][iBin-1]) + ' < ' + vName + ' < ' + str(binning['xbins'][iBin]) + ' ' + vUnit

                lumi = TPaveText(x1,y1*1.01,x2,y2,"brtlNDC");
                lumi.SetTextSize(fontSize);
                lumi.SetFillColor(0)
                lumi.SetFillStyle(0)
                lumi.SetLineStyle(0)
                lumi.SetLineWidth(0)
                lumi.SetTextAlign(31)
                lumi.SetTextFont(42);
                lumi.AddText(SelText);
                lumi.SetBorderSize(0);
                lumi.Draw("same");

                c1.Modified()
                c1.Update()
                SaveCanvas(c1,'ACFit__'+iCut+'__'+iVar+'__'+iScan.replace(":","_")+'__bin'+str(iBin)) 


    fIn.Close()
    return

def plot_plots():

    # Load the fits
    fInFit = ROOT.TFile.Open(opt.inputFitFile,'READ')
    ACFits={}
    for iCut in cuts:
      fInFit.cd()
      ACFits[iCut] = {}
      for iVar in variables :
        ACFits[iCut][iVar] = {}
        for iDim in ['1D','2D'] :
          if iDim == '1D' : separator = '_par1_'
          if iDim == '2D' : separator = '_par2_'
          if iDim in acoupling['ScanConfig'] and len(acoupling['ScanConfig'][iDim]) > 0 :
            for iScan in acoupling['ScanConfig'][iDim]:
              ACFits[iCut][iVar][iScan.replace(":","_")] = {}
              fInFit.cd(iCut+'/'+iVar+'/'+iScan.replace(":","_"))
              keyList = ROOT.gDirectory.GetListOfKeys()
              for key in keyList:
                obj = key.ReadObj()
                if 'TF' in  obj.ClassName() : ACFits[iCut][iVar][iScan.replace(":","_")][int(obj.GetName().split(separator)[1])] = obj

    # And Read Plots + Create AC Plots
    fInPlot = ROOT.TFile.Open(opt.inputPlotFile,'READ')
    fOut    = ROOT.TFile.Open(opt.inputPlotFile.replace('.root','_ACPlots.root'),'RECREATE')

    # ... Get signal name
    sigName =''
    nSignal=0
    for iSample in structure:
      if structure[iSample]['isSignal'] == 1: 
        sigName = iSample
        nSignal+=1
    if nSignal == 1 : 
      print '---> sigName = ',sigName 
    else:
      print '---> No signal FOUND !!!!'
      exit()

    # ... Clone histograms 
    SigNames = {}
    for iCut in cuts:
      fOut.mkdir(iCut)
      for iVar in variables :
        print '-------------- ',iCut,iVar
        fOut.mkdir(iCut+'/'+iVar)
        fInPlot.cd(iCut+'/'+iVar)
        keyList = ROOT.gDirectory.GetListOfKeys()
        fOut.cd(iCut+'/'+iVar)
        foundSignal = False
        for key in keyList:
          obj = key.ReadObj()
          hclone = obj.Clone()
          hclone.Write()
          if obj.GetName() == 'histo_'+sigName :
            foundSignal = True
            sigObj      = obj
        if foundSignal :
          for iDim in ['1D','2D'] :
            if iDim in acoupling['PlotConfig'] and len(acoupling['PlotConfig'][iDim]) > 0 :
              for iPlot in acoupling['PlotConfig'][iDim]:
                print '---> Creating: ',iPlot,' : ',acoupling['PlotConfig'][iDim][iPlot]
                if iDim == '1D' : 
                   hName  = 'histo_ACSig_'+iPlot+str(acoupling['PlotConfig'][iDim][iPlot][0]).replace('.','p').replace('-','m')
                   Legend = acoupling['operatorLatex'][iPlot]+' = '+str(acoupling['PlotConfig'][iDim][iPlot][0])+' '+acoupling['operatorUnit'][iPlot]  
                   Color  = int(acoupling['PlotConfig'][iDim][iPlot][1]) 
                if iDim == '2D' : 
                   hName = 'histo_ACSig_'+iPlot.split(':')[0]+str(acoupling['PlotConfig'][iDim][iPlot][0]).replace('.','p').replace('-','m')+'_'+iPlot.split(':')[1]+str(acoupling['PlotConfig'][iDim][iPlot][1]).replace('.','p').replace('-','m')
                   Legend = acoupling['operatorLatex'][iPlot.split(':')[0]]+' = '+str(acoupling['PlotConfig'][iDim][iPlot][0])+' '+acoupling['operatorUnit'][iPlot.split(':')[0]]+' , '+ \
                            acoupling['operatorLatex'][iPlot.split(':')[1]]+' = '+str(acoupling['PlotConfig'][iDim][iPlot][1])+' '+acoupling['operatorUnit'][iPlot.split(':')[1]]  
                   Color  = int(acoupling['PlotConfig'][iDim][iPlot][2]) 
                SigNames[hName.replace('histo_','')] = {
                                                         'Legend' : Legend ,
                                                         'Color'  : Color
                                                       }
                hclone = sigObj.Clone(hName)
                hclone.SetName(hName)
                for iBin in range(1,hclone.GetNbinsX()+1):
                  ratio = 1
                  if iDim == '1D' : ratio = ACFits[iCut][iVar][iPlot.replace(":","_")][iBin].Eval(acoupling['PlotConfig'][iDim][iPlot][0])
                  if iDim == '2D' : ratio = ACFits[iCut][iVar][iPlot.replace(":","_")][iBin].Eval(acoupling['PlotConfig'][iDim][iPlot][0],acoupling['PlotConfig'][iDim][iPlot][1])
                  hclone.SetBinContent(iBin,hclone.GetBinContent(iBin)*(ratio-1.))
                  hclone.SetBinError(iBin,hclone.GetBinError(iBin)*(ratio-1.))
                hclone.Print()     
                hclone.Write() 
        fOut.cd()

    # Close All Files
    fInFit.Close()
    fInPlot.Close()
    fOut.Close()

    # (Re-)create dictionnary for plotting

    samples2plot   = {}
    plot2plot      = {}
    groupPlot2plot = OrderedDict()   
    
    for iSample in structure:
      samples2plot[iSample] = {}

    for iSample in plot:
      plot2plot[iSample] = plot[iSample]
      plot2plot[iSample]['isSignal'] = 0

    for iGroup in  groupPlot:
      groupPlot2plot[iGroup] = groupPlot[iGroup]
      groupPlot2plot[iGroup]['isSignal'] = 0

    
#   for iSig in SigNames:
#     print iSig , ' ' , SigNames[iSig] 
#     samples2plot[iSig] = {}
#     plot2plot[iSig] = { 
#                        'color'    : SigNames[iSig]['Color'],
#                        'isSignal' : 2,
#                        'isData'   : 0,
#                        'scale'    : 1. 
#                       }
#     groupPlot2plot[iSig] = {
#                             'nameHR' : SigNames[iSig]['Legend'],
#                             'isSignal' : 2,
#                             'color': SigNames[iSig]['Color'],  #  kGreen+2
#                             'samples'  : [iSig]
#                            }

    print samples2plot
    print plot2plot
    print groupPlot2plot

    # Create the PlotFactory and execute it

    ROOT.gROOT.SetBatch()

    for iSig in SigNames:
      print iSig , ' ' , SigNames[iSig]
      samples2plot[iSig] = {}
      plot2plot[iSig] = {
                         'color'    : SigNames[iSig]['Color'],
                         'isSignal' : 2,
                         'isData'   : 0,
                         'scale'    : 1.
                        }
      groupPlot2plot[iSig] = {
                              'nameHR' : SigNames[iSig]['Legend'],
                              'isSignal' : 1,
                              'color': SigNames[iSig]['Color'],  #  kGreen+2
                              'samples'  : [iSig]
                             }

      factory = PlotFactory()
      factory._energy    = opt.energy
      factory._lumi      = opt.lumi
      factory._plotNormalizedDistributions = opt.plotNormalizedDistributions
      factory._showIntegralLegend = opt.showIntegralLegend

      factory._scaleToPlot = opt.scaleToPlot
      factory._minLogC = opt.minLogC
      factory._maxLogC = opt.maxLogC
      factory._minLogCratio = opt.minLogCratio
      factory._maxLogCratio = opt.maxLogCratio
      factory._maxLinearScale = opt.maxLinearScale

      factory._minLogCdifference = opt.minLogCratio
      factory._maxLogCdifference = opt.maxLogCratio

      factory._showRelativeRatio = opt.showRelativeRatio
      factory._showDataMinusBkgOnly = opt.showDataMinusBkgOnly

      factory._removeWeight = opt.removeWeight

      factory._invertXY = opt.invertXY

      factory._FigNamePF = '_'+iSig

      factory.makePlot( opt.inputPlotFile.replace('.root','_ACPlots.root') ,opt.outputDirPlots+'_ACPlots', variables, cuts, samples2plot, plot2plot, nuisances, legend, groupPlot2plot)

      del samples2plot[iSig]
      del plot2plot[iSig]
      del groupPlot2plot[iSig]
      del factory


if __name__ == '__main__':

    usage = 'usage: %prog [options]'
    parser = optparse.OptionParser(usage)

    parser.add_option('--type'           , dest='type'           , help='Plot type = fits/plots'                     , default='fits' )
    parser.add_option('--tag'            , dest='tag'            , help='Tag used for the shape file name'           , default=None) 
    parser.add_option('--outputDir'      , dest='outputDir'      , help='output directory'                           , default='./')
    parser.add_option('--outputDirPlots' , dest='outputDirPlots' , help='output directory'                           , default='./')
    parser.add_option('--inputPlotFile'  , dest='inputPlotFile'  , help='input file with histograms'                 , default='DEFAULT')
    parser.add_option('--inputFitFile'   , dest='inputFitFile'   , help='input file with histograms'                 , default='DEFAULT')
    parser.add_option('--structureFile'      , dest='structureFile'     , help='file with datacard configurations'          , default=None )
    parser.add_option('--nuisancesFile'      , dest='nuisancesFile'     , help='file with nuisances configurations'         , default=None )
    parser.add_option('--cutList'        , dest='cutList'        , help='cut list to process' , default=[], type='string' , action='callback' , callback=list_maker('cutList',','))
    parser.add_option('--varList'        , dest='varList'        , help='var list to process' , default=[], type='string' , action='callback' , callback=list_maker('varList',','))
    parser.add_option('--scanList'       , dest='scanList'        , help='scan list to process' , default=[], type='string' , action='callback' , callback=list_maker('scanList',','))

    # Some options for the PlotFactory:
    parser.add_option('--scaleToPlot'    , dest='scaleToPlot'    , help='scale of maxY to maxHistoY'                 , default=3.0  ,    type=float   )
    parser.add_option('--minLogC'        , dest='minLogC'        , help='min Y in log plots'                         , default=0.01  ,    type=float   )
    parser.add_option('--maxLogC'        , dest='maxLogC'        , help='max Y in log plots'                         , default=100   ,    type=float   )
    parser.add_option('--minLogCratio'   , dest='minLogCratio'   , help='min Y in log ratio plots'                   , default=0.001 ,    type=float   )
    parser.add_option('--maxLogCratio'   , dest='maxLogCratio'   , help='max Y in log ratio plots'                   , default=10    ,    type=float   )
    parser.add_option('--maxLinearScale' , dest='maxLinearScale' , help='scale factor for max Y in linear plots (1.45 magic number as default)'     , default=1.45   ,    type=float   )
    parser.add_option('--plotNormalizedDistributions'  , dest='plotNormalizedDistributions'  , help='plot also normalized distributions for optimization purposes'         , default=None )
    parser.add_option('--showIntegralLegend'           , dest='showIntegralLegend'           , help='show the integral, the yields, in the legend'                         , default=0,    type=float )

    parser.add_option('--showRelativeRatio'   , dest='showRelativeRatio'   , help='draw instead of data-expected, (data-expected) / expected' ,    action='store_true', default=False)
    parser.add_option('--showDataMinusBkgOnly', dest='showDataMinusBkgOnly', help='draw instead of data-expected, data-expected background only' , action='store_true', default=False)

    parser.add_option('--removeWeight', dest='removeWeight', help='Remove weight S/B for PR plots, just do the sum' , action='store_true', default=False)

    parser.add_option('--invertXY', dest='invertXY', help='Invert the weighting for X <-> Y. Instead of slices along Y, do slices along X' , action='store_true', default=False)


    # read default parsing options as well
    hwwtools.addOptions(parser)
    hwwtools.loadOptDefaults(parser)
    (opt, args) = parser.parse_args()

    # Set Input fileis
    if opt.inputPlotFile == 'DEFAULT' and opt.type == 'plots' :
      opt.inputPlotFile = opt.outputDir+'/plots_'+opt.tag+'.root'
    if opt.type == 'plots' :
      print " inputPlotFile      =          ", opt.inputPlotFile

    if opt.inputFitFile == 'DEFAULT' and opt.type == 'fits' :
      opt.inputFitFile = opt.outputDir+'/plots_'+opt.tag+'_ACCoupling.root'
    if opt.inputFitFile == 'DEFAULT' : 
       print 'Please specify --inputFitFile <FileName>'
       exit()
    print " inputFitFile      =          ", opt.inputFitFile

    # Create Needed dictionnary


    variables = {}
    if os.path.exists(opt.variablesFile) :
      handle = open(opt.variablesFile,'r')
      exec(handle)
      handle.close()
    if len(opt.varList)>0:
      var2del=[]
      for iVar in variables:
        if not iVar in opt.varList : var2del.append(iVar)
      for iVar in var2del : del variables[iVar]

    cuts = {}
    if os.path.exists(opt.cutsFile) :
      handle = open(opt.cutsFile,'r')
      exec(handle)
      handle.close()
    if len(opt.cutList)>0:
      cut2del=[]
      for iCut in cuts:
        if not iCut in opt.cutList : cut2del.append(iCut)
      for iCut in cut2del : del cuts[iCut]

    samples = {}
    if os.path.exists(opt.samplesFile) :
      handle = open(opt.samplesFile,'r')
      exec(handle)
      handle.close()

#   treeBaseDir =''

    # Scans Preselection
    if len(opt.scanList)>0:
      dim2del=[]
      for iDim in ['1D','2D','3D'] :
        if iDim in acoupling['ScanConfig'] :
          scan2keep=[]
          for iScan in acoupling['ScanConfig'][iDim] :
            if iScan in opt.scanList : scan2keep.append(iScan)
          acoupling['ScanConfig'][iDim] = scan2keep
          if len(acoupling['ScanConfig'][iDim]) == 0 : dim2del.append(iDim)
      for iDim in dim2del : del acoupling['ScanConfig'][iDim]

    print " Cuts               = " , cuts.keys()
    print " Variables          = " , variables.keys()
    for iDim in ['1D','2D'] :
      if iDim in acoupling['ScanConfig'] : print ' ', iDim , ' Scans  : '  , acoupling['ScanConfig'][iDim]

    # Need more dictionaries for plots
    if opt.type == 'plots'  : 

      print ""
      print " plotNormalizedDistributions =", opt.plotNormalizedDistributions
      print "          showIntegralLegend =", opt.showIntegralLegend
      print "                 scaleToPlot =", opt.scaleToPlot
      print "                     minLogC =", opt.minLogC
      print "                     maxLogC =", opt.maxLogC
      print "                minLogCratio =", opt.minLogCratio
      print "                maxLogCratio =", opt.maxLogCratio
      print "           showRelativeRatio =", opt.showRelativeRatio
      print "        showDataMinusBkgOnly =", opt.showDataMinusBkgOnly
      print "                removeWeight =", opt.removeWeight
      print "                    invertXY =", opt.invertXY
      print ""

      # ~~~~
      groupPlot = OrderedDict()
      plot = {}
      legend = {}
      if os.path.exists(opt.plotFile) :
        handle = open(opt.plotFile,'r')
        exec(handle)
        handle.close()

      # ~~~~
      structure = {}
      if opt.structureFile == None :
         print " Please provide the datacard structure "
         exit ()

      if os.path.exists(opt.structureFile) :
        handle = open(opt.structureFile,'r')
        exec(handle)
        handle.close()

      # ~~~~
      nuisances = {}
      if opt.nuisancesFile == None :
         print " Please provide the nuisances structure if you want to add nuisances "
      else:
        if os.path.exists(opt.nuisancesFile) :
          handle = open(opt.nuisancesFile,'r')
          exec(handle)
          handle.close()

    if opt.type == 'fits'   :
      opt.outputDirPlots+="_ACFits"
      if not os.path.exists(opt.outputDirPlots) : os.mkdir(opt.outputDirPlots)

    print " "
    print " ----------------------- Plot Type = " , opt.type , " ----------------------------"
    print " "

    if   opt.type == 'fits'   :  plot_fits()
    elif opt.type == 'plots'  :  plot_plots()
    else:
      print "STEP UNKNOWN !!!!!"
  
           
