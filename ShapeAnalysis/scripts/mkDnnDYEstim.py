#!/usr/bin/env python

import numpy as np

import sys 
argv = sys.argv
sys.argv = argv[:1]

import ROOT

from ROOT import TCanvas, TPad, TFile, TPaveText, TLegend
from ROOT import gBenchmark, gStyle, gROOT, TStyle
from ROOT import TH1D, TF1, TGraphErrors, TMultiGraph

from math import sqrt

from array import array

import LatinoAnalysis.ShapeAnalysis.tdrStyle as tdrStyle
tdrStyle.setTDRStyle()

import LatinoAnalysis.ShapeAnalysis.CMS_lumi as CMS_lumi

# Introducing parser
import optparse

sys.argv = argv

usage = 'usage: %prog [options]'
parser = optparse.OptionParser(usage)

parser.add_option('--inputFile', dest='inputFile', help='histograms file',        default='rootFile/plots_DYMVA_SYS_2016_v6.root') 
parser.add_option('--jet_bin',   dest='jet_bin',   help='phase space to inspect', default='0j') 

(opt, args) = parser.parse_args()

sys.argv.append( '-b' )
ROOT.gROOT.SetBatch()

print("List of inputs:")
print("Input rootfile: {0}".format(opt.inputFile))
print("Jet bin:        {0}".format(opt.jet_bin))

# Assigning inputs to variables
inputFile = opt.inputFile 
jet_bin   = opt.jet_bin 

#change the CMS_lumi variables (see CMS_lumi.py)
CMS_lumi.lumi_13TeV = '35.9 fb^{-1}'
CMS_lumi.writeExtraText = 1
#CMS_lumi.extraText = 'Preliminary'
CMS_lumi.extraText = ''

iPos = 0

gStyle.SetOptFit(0)

def k_value(Num, Den):
   if Num == 0 or Den == 0:
     return 0
   #print('k = ', sqrt( Num / Den ))
   return sqrt( Num / Den )

def k_error(Num, Den, ENum, EDen):
   if Num == 0 or Den == 0: 
     return 0
   #print('k error = ', 0.5 * sqrt( pow((ENum/Num),2) + pow((EDen/Den),2) ) * k_value(Num, Den))
   return 0.5 * sqrt( pow((ENum/Num),2) + pow((EDen/Den),2) ) * k_value(Num, Den)

def R_value(Num, Den):
   if Num == 0 or Den == 0: 
     return 0
   #print( Num/Den )
   return (Num/Den)

def R_error(Num, Den, ENum, EDen):
   if Num == 0 or Den == 0: 
     return 0
   #print( sqrt( pow((ENum/Num),2) + pow((EDen/Den),2) ) * R_value(Num, Den) )
   return sqrt( pow((ENum/Num),2) + pow((EDen/Den),2) ) * R_value(Num, Den)

def DataFromR(R, k, Zsf, Zdf, VVsf, VVdf):
  #print (R * (Zsf-(0.5*k*(Zdf-VVdf))-VVdf))
  return (R * (Zsf-(0.5*k*(Zdf-VVdf))-VVdf))

def DataFromR(R, k, Zsf, Zdf, VVsf, VVdf):
  #print (R * (Zsf-(0.5*k*(Zdf-VVdf))-VVdf))
  return (R * (Zsf-(0.5*k*(Zdf-VVdf))-VVdf))

def loadcanvas():
  canvas = TCanvas('canvas','canvas',400,20,1400,1000)
  canvas.SetFillColor(0)
  canvas.SetBorderMode(0)
  canvas.SetFrameFillStyle(0)
  canvas.SetFrameBorderMode(0)
  canvas.SetTickx(0)
  canvas.SetTicky(0)
  return canvas

def loadlegend(top, bottom, left, right):
  relPosX    = 0.200
  relPosY    = 0.005
  posX = -1
  posX = 1 - right - relPosX*(1-left-right)
  posY = 1 - top - relPosY*(1-top-bottom)
  legendOffsetX = -0.060
  legendOffsetY = 0.
  textSize   = 0.05
  textFont   = 60
  legendSizeX = 0.5
  legendSizeY = 0.2
  legend = TLegend(posX-legendSizeX+legendOffsetX,posY-legendSizeY+legendOffsetY,posX+legendOffsetX,posY+legendOffsetY)
  legend.SetTextSize(textSize)
  legend.SetLineStyle(0)
  legend.SetBorderSize(0)
  return legend

#inputFile = "rootFile/plots_DYMVA_SYS_2016_v6.root"

thefile = TFile(inputFile)
thelist = thefile.GetListOfKeys()
histos  = {}
values  = {}
errors  = {}
graphs  = {}
dymva   = [0.05,0.2,0.4,0.6,0.75,0.825,0.875,0.9125,0.9375,0.9625,0.9875]
e_dymva = [0.05,0.1,0.1,0.1,0.05,0.025,0.025,0.0125,0.0125,0.0125,0.0125]

# loading DY histograms

# jet bins = ['0j', '1j', '2j', 'VBF', 'VH']
#jet_bin = '0j'

# jet_bin_folders = ['dymva_alt_dnn_0j', 'dymva_alt_dnn_1j', 'dymva_alt_dnn_2j', 'dymva_alt_dnn_VH', 'dymva_alt_dnn_VBF']
jet_bin_folder = 'dymva_alt_dnn_{}'.format(jet_bin)

print("##########################################")

print("Jet Bin:")
print(jet_bin)

print("Jet Bin Folder:")
print(jet_bin_folder)

print("##########################################")


for dirs in thelist :
  histos['DY_'+dirs.GetName()] = thefile.Get(dirs.GetName()+'/' + jet_bin_folder + '/histo_DY') 
  histos['DATA_'+dirs.GetName()] = thefile.Get(dirs.GetName()+'/' + jet_bin_folder + '/histo_DATA')
  histos['DYDATA_'+dirs.GetName()] = TH1D.Clone(histos['DATA_'+dirs.GetName()])
  histos['AMC_'+dirs.GetName()] = TH1D.Clone(histos['DY_'+dirs.GetName()])
  histos['VV_'+dirs.GetName()] = TH1D('VV_'+dirs.GetName(), 'VV_'+dirs.GetName(), histos['DY_'+dirs.GetName()].GetNbinsX(), histos['DY_'+dirs.GetName()].GetXaxis().GetXbins().GetArray())
  
  # CREATING k histograms
  if 'in' in dirs.GetName() and not 'btag' in dirs.GetName() and not 'df' in dirs.GetName() and not dirs.GetName().startswith('H_') and not 'ww_' in dirs.GetName() and jet_bin in dirs.GetName():
  # not '1j' in dirs.GetName() and not '2j' in dirs.GetName() and not 'VBF' in dirs.GetName() and not 'VH' in dirs.GetName():
    #print('Histos for K and R: ', dirs.GetName())
    histos['k_MC_'+dirs.GetName()] = TH1D('k_MC_'+dirs.GetName(), 'k_MC_'+dirs.GetName(), histos['DY_'+dirs.GetName()].GetNbinsX(), histos['DY_'+dirs.GetName()].GetXaxis().GetXbins().GetArray())
    histos['k_DATA_'+dirs.GetName()] = TH1D('k_DATA_'+dirs.GetName(), 'k_DATA_'+dirs.GetName(), histos['DATA_'+dirs.GetName()].GetNbinsX(), histos['DATA_'+dirs.GetName()].GetXaxis().GetXbins().GetArray())
  # CREATING R histograms
  if 'out' in dirs.GetName() and not 'df' in dirs.GetName() and not dirs.GetName().startswith('H_') and not 'ww_' in dirs.GetName():
    #print('R dirs', dirs.GetName())
    histos['R_MC_'+dirs.GetName()] = TH1D('R_MC_'+dirs.GetName(), 'R_MC_'+dirs.GetName(), histos['DY_'+dirs.GetName()].GetNbinsX(), histos['DY_'+dirs.GetName()].GetXaxis().GetXbins().GetArray())
    histos['R_DATA_'+dirs.GetName()] = TH1D('R_DATA_'+dirs.GetName(), 'R_DATA_'+dirs.GetName(), histos['DATA_'+dirs.GetName()].GetNbinsX(), histos['DATA_'+dirs.GetName()].GetXaxis().GetXbins().GetArray())
    histos['DATA_fromR_'+dirs.GetName()] = TH1D('DATA_fromR_'+dirs.GetName(), 'DATA_fromR_'+dirs.GetName(), histos['DATA_'+dirs.GetName()].GetNbinsX(), histos['DATA_'+dirs.GetName()].GetXaxis().GetXbins().GetArray())
    histos['R_fromDATAR_'+dirs.GetName()] = TH1D('R_fromDATAR_'+dirs.GetName(), 'R_fromDATAR_'+dirs.GetName(), histos['DATA_'+dirs.GetName()].GetNbinsX(), histos['DATA_'+dirs.GetName()].GetXaxis().GetXbins().GetArray())
#    if 'btag' not in dirs.GetName():
#      histos['A_ww_MC_'+dirs.GetName()] = TH1D('A_ww_MC_'+dirs.GetName(), 'A_ww_MC_'+dirs.GetName(), histos['DY_'+dirs.GetName()].GetNbinsX(), histos['DY_'+dirs.GetName()].GetXaxis().GetXbins().GetArray())
#      histos['A_ww_DATA_'+dirs.GetName()] = TH1D('A_ww_DATA_'+dirs.GetName(), 'A_ww_DATA_'+dirs.GetName(), histos['DATA_'+dirs.GetName()].GetNbinsX(), histos['DATA_'+dirs.GetName()].GetXaxis().GetXbins().GetArray())
#      histos['A_H_MC_'+dirs.GetName()] = TH1D('A_H_MC_'+dirs.GetName(), 'A_H_MC_'+dirs.GetName(), histos['DY_'+dirs.GetName()].GetNbinsX(), histos['DY_'+dirs.GetName()].GetXaxis().GetXbins().GetArray())
#      histos['A_H_DATA_'+dirs.GetName()] = TH1D('A_H_DATA_'+dirs.GetName(), 'A_H_DATA_'+dirs.GetName(), histos['DATA_'+dirs.GetName()].GetNbinsX(), histos['DATA_'+dirs.GetName()].GetXaxis().GetXbins().GetArray())
  currentdir = dirs.ReadObj()
  for subdir in currentdir.GetListOfKeys(): 
    if subdir.GetName()!= jet_bin_folder: #'dymva_alt_dnn_0j': 
      continue
    currentsubdir = subdir.ReadObj()
    previoussample=''
    for sample in currentsubdir.GetListOfKeys():
      if sample.GetName()==previoussample:
        continue
      previoussample = sample.GetName()
      if 'histo_DATA' in sample.GetName() or 'histo_DY' in sample.GetName():
        continue
      histos[sample.GetName()+dirs.GetName()] = thefile.Get(dirs.GetName()+'/' + jet_bin_folder + '/'+sample.GetName())
      histos['AMC_'+dirs.GetName()].Add(histos[sample.GetName()+dirs.GetName()])
      histos['DYDATA_'+dirs.GetName()].Add(histos[sample.GetName()+dirs.GetName()],-1)
      if 'histo_V' in sample.GetName():
        histos['VV_'+dirs.GetName()].Add(histos[sample.GetName()+dirs.GetName()])
  print('----------------------------', dirs.GetName(), '----------------------------')
  print('Integral of DY is           ', histos['DY_'+dirs.GetName()].Integral())
  print('Integral of DY from DATA is ', histos['DYDATA_'+dirs.GetName()].Integral())
  print('Integral of DATA is   ', histos['DATA_'+dirs.GetName()].Integral())
  print('Integral of all MC is ', histos['AMC_'+dirs.GetName()].Integral())
  print('Integral of VV is ', histos['VV_'+dirs.GetName()].Integral())

# Filling k histos
for dirs in thelist :
  if 'in' in dirs.GetName() and not 'btag' in dirs.GetName() and not 'df' in dirs.GetName() and not dirs.GetName().startswith('H_') and not 'ww_' in dirs.GetName() and jet_bin in dirs.GetName():
  # not '1j' in dirs.GetName() and not '2j' in dirs.GetName() and not 'VBF' in dirs.GetName() and not 'VH' in dirs.GetName(): 
    lastbin = histos['k_MC_'+dirs.GetName()].GetNbinsX() + 1
    for iBin in range(1, lastbin):
      NumMC = histos['DY_'+dirs.GetName()].Integral(iBin,lastbin)
      NumDATA = histos['DYDATA_'+dirs.GetName()].Integral(iBin,lastbin)
      if 'ee' in dirs.GetName():
        Denword = dirs.GetName().replace('ee','mm')
        DenMC  = histos['DY_'+Denword].Integral(iBin,lastbin)
        DenDATA  = histos['DYDATA_'+Denword].Integral(iBin,lastbin)
      elif 'mm' in dirs.GetName():
        Denword = dirs.GetName().replace('mm','ee')
        DenMC  = histos['DY_'+Denword].Integral(iBin,lastbin)
        DenDATA  = histos['DYDATA_'+Denword].Integral(iBin,lastbin)
      #print('DY_'+dirs.GetName(),NumMC,'DY_'+Denword,DenMC)
      #print('DYDATA_'+dirs.GetName(),NumDATA,'DYDATA_'+Denword,DenDATA)
      histos['k_MC_'+dirs.GetName()].SetBinContent(iBin, k_value(NumMC,DenMC))
      if NumMC<0 or DenMC<0 : histos['k_MC_'+dirs.GetName()].SetBinError(iBin, 0)
      else                    : histos['k_MC_'+dirs.GetName()].SetBinError(iBin, k_error(NumMC,DenMC,sqrt(NumMC),sqrt(DenMC)))
      histos['k_DATA_'+dirs.GetName()].SetBinContent(iBin, k_value(NumDATA,DenDATA))
      if NumDATA<0 or DenDATA<0 : histos['k_DATA_'+dirs.GetName()].SetBinError(iBin, 0)
      else                        : histos['k_DATA_'+dirs.GetName()].SetBinError(iBin, k_error(NumDATA,DenDATA,sqrt(NumDATA),sqrt(DenDATA)))

#Fillin R histos
for dirs in thelist :
  if 'out' in dirs.GetName() and not 'df' in dirs.GetName() and not dirs.GetName().startswith('H_') and not 'ww_' in dirs.GetName() and jet_bin in dirs.GetName():
  #not '1j' in dirs.GetName() and not '2j' in dirs.GetName() and not 'VBF' in dirs.GetName() and not 'VH' in dirs.GetName():
    print(dirs.GetName())
    if 'btag' not in dirs.GetName():
      values['A_ww_MC_'+dirs.GetName()]  = []
      values['A_ww_DATA_'+dirs.GetName()]= []
      errors['A_ww_MC_'+dirs.GetName()]  = []
      errors['A_ww_DATA_'+dirs.GetName()]= []
      values['A_H_MC_'+dirs.GetName()]   = []
      values['A_H_DATA_'+dirs.GetName()] = []
      errors['A_H_MC_'+dirs.GetName()]   = []
      errors['A_H_DATA_'+dirs.GetName()] = []
    lastbin = histos['R_MC_'+dirs.GetName()].GetNbinsX() + 1
    for iBin in range(1, lastbin):
      print(iBin)
      NumMC = histos['DY_'+dirs.GetName()].Integral(iBin,lastbin)
      NumDATA = histos['DYDATA_'+dirs.GetName()].Integral(iBin,lastbin)
      Denword = dirs.GetName().replace('out','in')
      DenMC  = histos['DY_'+Denword].Integral(iBin,lastbin)
      DenDATA  = histos['DYDATA_'+Denword].Integral(iBin,lastbin)
      #print('DY_'+dirs.GetName(),NumMC,'DY_'+Denword,DenMC)
      #print('DYDATA_'+dirs.GetName(),NumDATA,'DYDATA_'+Denword,DenDATA)
      if NumMC<0 or DenMC<0   : 
         histos['R_MC_'+dirs.GetName()].SetBinError(iBin, 0)
         histos['R_MC_'+dirs.GetName()].SetBinContent(iBin, 0)
      else                    : 
         histos['R_MC_'+dirs.GetName()].SetBinContent(iBin, R_value(NumMC,DenMC))
         histos['R_MC_'+dirs.GetName()].SetBinError(iBin, R_error(NumMC,DenMC,sqrt(NumMC),sqrt(DenMC)))
      histos['R_DATA_'+dirs.GetName()].SetBinContent(iBin, R_value(NumDATA,DenDATA))
      print(NumDATA,DenDATA)
      if NumDATA<0 or DenDATA<0 : 
        histos['R_DATA_'+dirs.GetName()].SetBinContent(iBin, 0)
        histos['R_DATA_'+dirs.GetName()].SetBinError(iBin, 0)
      else                      : 
        histos['R_DATA_'+dirs.GetName()].SetBinContent(iBin, R_value(NumDATA,DenDATA))
        histos['R_DATA_'+dirs.GetName()].SetBinError(iBin, R_error(NumDATA,DenDATA,sqrt(NumDATA),sqrt(DenDATA)))
      R = histos['R_MC_'+dirs.GetName()].GetBinContent(iBin)
      if 'btag' in  dirs.GetName():
        kword = Denword.replace('btag_','')
        k    = histos['k_MC_'+kword].GetBinContent(iBin)
      else:
        k    = histos['k_MC_'+Denword].GetBinContent(iBin)
      Zsf  = histos['DATA_'+Denword].Integral(iBin,lastbin)
      VVsf = histos['VV_'+Denword].Integral(iBin,lastbin)
      if 'ee' in dirs.GetName():
        Zdfword = Denword.replace('ee','df')
      elif 'mm' in dirs.GetName():
        Zdfword  = Denword.replace('mm','df')
      Zdf   = histos['DATA_'+Zdfword].Integral(iBin,lastbin)
      VVdf  = histos['VV_'+Zdfword].Integral(iBin,lastbin)
      print('R',R,'k',k,'Zsf',Zsf,'Zdf',Zdf,'VVsf',VVsf,'VVdf',VVdf)
      histos['DATA_fromR_'+dirs.GetName()].SetBinContent(iBin, DataFromR(R, k, Zsf, Zdf, VVsf, VVdf))
      NumDATAR  = histos['DATA_fromR_'+dirs.GetName()].Integral(iBin,lastbin)
      histos['R_fromDATAR_'+dirs.GetName()].SetBinContent(iBin, R_value(NumDATAR,Zsf))
      if NumDATAR<0 or Zsf<0 : histos['R_fromDATAR_'+dirs.GetName()].SetBinError(iBin, 0)
      else                     : histos['R_fromDATAR_'+dirs.GetName()].SetBinError(iBin, R_error(NumDATAR,DenDATA,sqrt(NumDATAR),sqrt(Zsf)))
      print('R from DY ESTIM = ', histos['R_fromDATAR_'+dirs.GetName()].GetBinContent(iBin),'Num = ',NumDATAR ,'Den = ', DenDATA)
      print('R_MC           ', histos['R_MC_'+dirs.GetName()].GetBinContent(iBin), ' +/- ', histos['R_MC_'+dirs.GetName()].GetBinError(iBin))
      print('R_DATA         ', histos['R_DATA_'+dirs.GetName()].GetBinContent(iBin), ' +/- ', histos['R_DATA_'+dirs.GetName()].GetBinError(iBin))
      print('R_from DYESTIM ', histos['R_fromDATAR_'+dirs.GetName()].GetBinContent(iBin), ' +/- ', histos['R_fromDATAR_'+dirs.GetName()].GetBinError(iBin))

      if 'btag' not in dirs.GetName():
        print(dirs.GetName())
        AccDen = histos['DY_'+dirs.GetName()].Integral(iBin,lastbin)
        WWNum  = histos['DY_ww_'+dirs.GetName()].Integral(iBin,lastbin)
        HNum   = histos['DY_H_'+dirs.GetName()].Integral(iBin,lastbin)
        AccDenData = histos['DYDATA_'+dirs.GetName()].Integral(iBin,lastbin)
        WWNumData  = histos['DYDATA_ww_'+dirs.GetName()].Integral(iBin,lastbin)
        HNumData   = histos['DYDATA_H_'+dirs.GetName()].Integral(iBin,lastbin)
        if WWNum<0 or AccDen<0 :
          values['A_ww_MC_'+dirs.GetName()].append(0) 
          errors['A_ww_MC_'+dirs.GetName()].append(0)
        else                   : 
          values['A_ww_MC_'+dirs.GetName()].append(R_value(WWNum,AccDen))
          errors['A_ww_MC_'+dirs.GetName()].append(R_error(WWNum,AccDen,sqrt(WWNum),sqrt(AccDen)))
        if WWNumData<0 or AccDenData<0 : 
          values['A_ww_DATA_'+dirs.GetName()].append(0)
          errors['A_ww_DATA_'+dirs.GetName()].append(0)
        else                           : 
          errors['A_ww_DATA_'+dirs.GetName()].append(R_error(WWNumData,AccDenData,sqrt(WWNumData),sqrt(AccDenData)))
          values['A_ww_DATA_'+dirs.GetName()].append(R_value(WWNumData,AccDenData))
        print('Acceptance for DY in WW CR',dirs.GetName(),'(MC)  ', values['A_ww_MC_'+dirs.GetName()][iBin-1], WWNum, AccDen)
        print('Acceptance for DY in WW CR',dirs.GetName(),'(DATA)', values['A_ww_DATA_'+dirs.GetName()][iBin-1], WWNumData, AccDenData)
        if HNum<0 or AccDen<0 : 
          values['A_H_MC_'+dirs.GetName()].append(0)
          errors['A_H_MC_'+dirs.GetName()].append(0)
        else                  : 
          errors['A_H_MC_'+dirs.GetName()].append(R_error(HNum,AccDen,sqrt(HNum),sqrt(AccDen)))
          values['A_H_MC_'+dirs.GetName()].append(R_value(HNum,AccDen))
        if HNumData<0 or AccDenData<0 : 
          values['A_H_DATA_'+dirs.GetName()].append(0)
          errors['A_H_DATA_'+dirs.GetName()].append(0)
        else                          : 
          errors['A_H_DATA_'+dirs.GetName()].append(R_error(HNumData,AccDenData,sqrt(HNumData),sqrt(AccDenData)))
          values['A_H_DATA_'+dirs.GetName()].append(R_value(HNumData,AccDenData))
        print('Acceptance for DY in SR',dirs.GetName(),'(MC)  ', values['A_H_MC_'+dirs.GetName()][iBin-1], HNum, AccDen)
        print('Acceptance for DY in SR',dirs.GetName(),'(DATA)', values['A_H_DATA_'+dirs.GetName()][iBin-1], HNumData, AccDenData)

    print(dirs.GetName())
    print('Integral of DY is           ', histos['DY_'+dirs.GetName()].Integral())
    print('Integral of DY from DATA is ', histos['DYDATA_'+dirs.GetName()].Integral())
    print('Integral of DY from R is    ', histos['DATA_fromR_'+dirs.GetName()].Integral())

    if 'out' in dirs.GetName() and not 'df' in dirs.GetName() and not dirs.GetName().startswith('H_') and not 'ww_' in dirs.GetName() and 'btag' not in dirs.GetName() and jet_bin in dirs.GetName():
    #not '1j' in dirs.GetName() and not '2j' in dirs.GetName() and not 'VBF' in dirs.GetName() and not 'VH' in dirs.GetName():
      print(values['A_ww_MC_'+dirs.GetName()])
      print(errors['A_ww_MC_'+dirs.GetName()])
      print(values['A_ww_DATA_'+dirs.GetName()])
      print(errors['A_ww_DATA_'+dirs.GetName()])
      print(values['A_H_MC_'+dirs.GetName()])
      print(errors['A_H_MC_'+dirs.GetName()])
      print(values['A_H_DATA_'+dirs.GetName()])
      print(errors['A_H_DATA_'+dirs.GetName()])
      graphs['A_ww_MC_'+dirs.GetName()]   = TGraphErrors(len(values['A_ww_MC_'+dirs.GetName()]),   np.array(dymva), np.array(values['A_ww_MC_'+dirs.GetName()]),  np.array(e_dymva), np.array(errors['A_ww_MC_'+dirs.GetName()]));
      graphs['A_ww_DATA_'+dirs.GetName()] = TGraphErrors(len(values['A_ww_DATA_'+dirs.GetName()]), np.array(dymva), np.array(values['A_ww_DATA_'+dirs.GetName()]),np.array(e_dymva), np.array(errors['A_ww_DATA_'+dirs.GetName()]));
      graphs['A_H_MC_'+dirs.GetName()]    = TGraphErrors(len(values['A_H_MC_'+dirs.GetName()]),    np.array(dymva), np.array(values['A_H_MC_'+dirs.GetName()]),   np.array(e_dymva), np.array(errors['A_H_MC_'+dirs.GetName()]));
      graphs['A_H_DATA_'+dirs.GetName()]  = TGraphErrors(len(values['A_H_DATA_'+dirs.GetName()]),  np.array(dymva), np.array(values['A_H_DATA_'+dirs.GetName()]), np.array(e_dymva), np.array(errors['A_H_DATA_'+dirs.GetName()]));

filetosave = TFile('DYestim.root','recreate')
filetosave.cd()
for histo in histos:
  if histo.startswith('R_') or histo.startswith('k_') or histo.startswith('A_') :
    histos[histo].Write()
  #Saving R histos
  if 'R_MC' in histo and 'btag' not in histo and jet_bin in histo:
  #not '1j' in histo and not '2j' in histo and not 'VBF' in histo and not 'VH' in histo:
    print(histo)
    canvas = loadcanvas()
    canvas.cd()
    legend = loadlegend(canvas.GetTopMargin(), canvas.GetBottomMargin(), canvas.GetLeftMargin(), canvas.GetRightMargin())
    histos[histo].SetLineColor(2)
    histos[histo].SetLineWidth(2)
    histos[histo].GetYaxis().SetRangeUser(0,1)
    #if '0j' in histo  :  histos[histo].SetXTitle("DYMVA_{DNN}^{0j}")
    histo_x_title = "DYMVA_{DNN}^{" + jet_bin + "}"
    print(histo_x_title)
    histos[histo].SetXTitle(histo_x_title)
    if 'ee' in histo   : histos[histo].SetYTitle("R^{ee}")
    elif 'mm' in histo : histos[histo].SetYTitle("R^{#mu#mu}")
    histos[histo].Draw()
    histos[histo].Fit("pol0","","",0.9,0.95)
    fitMC = histos[histo].FindObject("pol0")
    p0MC = fitMC.GetParameter(0)
    e0MC = fitMC.GetParError(0)
    fitMC = histos[histo].FindObject("pol0")
    fitMC.SetLineColor(2)
    fitMC.Draw('same')
    dataword=histo.replace('R_MC','R_DATA')
    #dataword=histo.replace('R_MC','R_fromDATAR')
    histos[dataword].SetLineColor(4)
    histos[dataword].SetLineWidth(2)
    histos[dataword].Draw('same')
    histos[dataword].Fit("pol0","","",0.9,0.95)
    fitDATA = histos[dataword].FindObject("pol0")
    p0DATA = fitDATA.GetParameter(0)
    #e0DATA = fitDATA.GetParError(0)
    e0DATA = abs(histos[dataword].GetBinContent(10) - histos[dataword].GetBinContent(8))
    fitDATA = histos[dataword].FindObject("pol0")
    fitDATA.SetLineColor(4)
    fitDATA.Draw('same')

    legend.AddEntry(histos[histo], 'DY MC','lf')
    legend.AddEntry(fitMC, "{0:.3f}".format(p0MC)+'#pm'+"{0:.3f}".format(e0MC) , 'lf')
    legend.AddEntry(histos[dataword], 'DY DATA','lf')
    legend.AddEntry(fitDATA, "{0:.3f}".format(p0DATA)+'#pm'+"{0:.3f}".format(e0DATA) , 'lf')
    CMS_lumi.CMS_lumi(canvas, 4, iPos)
    canvas.Update()
    legend.Draw()
    canvas.SaveAs(histo+'.png')
    #canvas.SaveAs(histo+'.root')

  '''
  if 'R_MC' in histo and 'btag' in histo  and not '1j' in histo and not '2j' in histo and not 'VBF' in histo and not 'VH' in histo:
    print(histo)
    canvas = loadcanvas()
    canvas.cd()
    legend = loadlegend(canvas.GetTopMargin(), canvas.GetBottomMargin(), canvas.GetLeftMargin(), canvas.GetRightMargin())
    histos[histo].SetLineColor(2)
    histos[histo].SetLineWidth(2)
    histos[histo].GetYaxis().SetRangeUser(0,1)
    if '0j' in histo  :  histos[histo].SetXTitle("DYMVA_{DNN}^{0j}")
    if 'ee' in histo   : histos[histo].SetYTitle("R^{ee}")
    elif 'mm' in histo : histos[histo].SetYTitle("R^{#mu#mu}")
    histos[histo].Draw()
    histos[histo].Fit("pol0","","",0.975,1)
    fitMC = histos[histo].FindObject("pol0")
    p0MC = fitMC.GetParameter(0)
    e0MC = fitMC.GetParError(0)
    fitMC = histos[histo].FindObject("pol0")
    fitMC.SetLineColor(2)
    fitMC.Draw('same')
    #bvetoword=histo.replace('R_MC','R_DATA')
    bvetoword=histo.replace('R_MC','R_fromDATAR')
    histos[bvetoword].SetLineColor(4)
    histos[bvetoword].SetLineWidth(2)
    histos[bvetoword].Draw('same')
    histos[bvetoword].Fit("pol0","","",0.975,1)
    fitbveto = histos[bvetoword].FindObject("pol0")
    p0bveto = fitbveto.GetParameter(0)
    e0bveto = fitbveto.GetParError(0)
    fitbveto = histos[bvetoword].FindObject("pol0")
    fitbveto.SetLineColor(4)
    fitbveto.Draw('same')

    legend.AddEntry(histos[histo], 'DY MC (btag)','lf')
    #legend.AddEntry(fitMC, "{0:.3f}".format(p0MC)+'#pm'+"{0:.3f}".format(e0MC) , 'lf')
    legend.AddEntry(histos[bvetoword],'DY DATA (btag)','lf')
    #legend.AddEntry(fitbveto, "{0:.3f}".format(p0bveto)+'#pm'+"{0:.3f}".format(e0bveto) , 'lf')
    CMS_lumi.CMS_lumi(canvas, 4, iPos)
    canvas.Update()
    legend.Draw()
    #canvas.SaveAs(histo+'.png')
    #canvas.SaveAs(histo+'.root')
  '''

  
  #Saving k histos
  if 'k_MC' in histo and 'btag' not in histo and jet_bin in histo:
  #not '1j' in histo and not '2j' in histo and not 'VBF' in histo and not 'VH' in histo:
    print(histo)
    canvas = loadcanvas()
    canvas.cd()
    legend = loadlegend(canvas.GetTopMargin(), canvas.GetBottomMargin(), canvas.GetLeftMargin(), canvas.GetRightMargin())
    histos[histo].SetLineColor(2)
    histos[histo].SetLineWidth(2)
    #if '0j' in histo  :  histos[histo].SetXTitle("DYMVA_{DNN}^{0j}")
    histo_x_title = "DYMVA_{DNN}^{" + jet_bin + "}"
    histos[histo].SetXTitle(histo_x_title)
    if 'ee' in histo   : 
      histos[histo].SetYTitle("k^{ee}")
      histos[histo].GetYaxis().SetRangeUser(0.5,1)
    elif 'mm' in histo : 
      histos[histo].SetYTitle("k^{#mu#mu}")
      histos[histo].GetYaxis().SetRangeUser(1,2)
    histos[histo].Draw()
    histos[histo].Fit("pol0","","",0.8,0.9)
    fitMC = histos[histo].FindObject("pol0")
    p0MC = fitMC.GetParameter(0)
    e0MC = fitMC.GetParError(0)
    fitMC = histos[histo].FindObject("pol0")
    fitMC.SetLineColor(2)
    fitMC.Draw('same')
    dataword=histo.replace('k_MC','k_DATA')
    histos[dataword].SetLineColor(4)
    histos[dataword].SetLineWidth(2)
    histos[dataword].Draw('same')
    histos[dataword].Fit("pol0","","",0.8,0.9)
    fitDATA = histos[dataword].FindObject("pol0")
    p0DATA = fitDATA.GetParameter(0)
    e0DATA = fitDATA.GetParError(0)
    fitDATA = histos[dataword].FindObject("pol0")
    fitDATA.SetLineColor(4)
    fitDATA.Draw('same')

    legend.AddEntry(histos[histo], 'DY MC','lf')
    legend.AddEntry(fitMC, "{0:.3f}".format(p0MC)+'#pm'+"{0:.3f}".format(e0MC) , 'lf')
    legend.AddEntry(histos[dataword], 'DY DATA','lf')
    legend.AddEntry(fitDATA, "{0:.3f}".format(p0DATA)+'#pm'+"{0:.3f}".format(e0DATA) , 'lf')
    CMS_lumi.CMS_lumi(canvas, 4, iPos)
    canvas.Update()
    legend.Draw()
    canvas.SaveAs(histo+'.png')
    #canvas.SaveAs(histo+'.root')

  #Saving Acceptance histos
for graph in graphs:
  if 'MC' in graph and jet_bin in graph:
  # not '1j' in graph and not '2j' in graph and not 'VBF' in graph and not 'VH' in graph:
    print(graph)
    canvas = loadcanvas()
    canvas.cd()
    legend = loadlegend(canvas.GetTopMargin(), canvas.GetBottomMargin(), canvas.GetLeftMargin(), canvas.GetRightMargin())
    graphs[graph].SetLineColor(2)
    graphs[graph].SetLineWidth(2)
    graphs[graph].GetYaxis().SetRangeUser(0,1)
    graphs[graph].GetXaxis().SetRangeUser(0,1)
    #if '0j' in graph:    graphs[graph].GetXaxis().SetTitle("DYMVA_{DNN}^{0j}")
    graph_x_title = "DYMVA_{DNN}^{" + jet_bin + "}"
    graphs[graph].GetXaxis().SetTitle(graph_x_title)
    if 'A_ww' in graph and 'ee' in graph   : graphs[graph].GetYaxis().SetTitle("A_{WW}^{ee}")
    elif 'A_ww' in graph and 'mm' in graph : graphs[graph].GetYaxis().SetTitle("A_{WW}^{#mu#mu}")
    elif 'A_H' in graph and 'ee' in graph  : graphs[graph].GetYaxis().SetTitle("A_{H}^{ee}")
    elif 'A_H' in graph and 'mm' in graph  : graphs[graph].GetYaxis().SetTitle("A_{H}^{#mu#mu}")
    graphs[graph].Draw('AP')
    graphs[graph].Fit("pol0","","",0.9,0.95)
    fitMC = graphs[graph].FindObject("pol0")
    if fitMC:
      p0MC = fitMC.GetParameter(0)
      e0MC = fitMC.GetParError(0)
      fitMC = graphs[graph].FindObject("pol0")
      fitMC.SetLineColor(2)
    else:
      p0MC = 0
      e0MC = 0.01
    #fitMC.Draw('SAME')
    dataword=graph.replace('_MC_','_DATA_')
    graphs[dataword].SetLineColor(4)
    graphs[dataword].SetLineWidth(2)
    graphs[dataword].Draw('P')
    graphs[dataword].Fit("pol0","","",0.9,0.95)
    fitDATA = graphs[dataword].FindObject("pol0")
    if fitDATA:
      p0DATA = fitDATA.GetParameter(0)
      e0DATA = fitDATA.GetParError(0)
      fitDATA = graphs[dataword].FindObject("pol0")
      fitDATA.SetLineColor(4)
    else:
      p0DATA = 0 
      e0DATA = 0.01 
    #fitDATA.Draw('SAME')

    legend.AddEntry(graphs[graph],    "DY MC   " "{0:.3f}".format(p0MC)+'#pm'+"{0:.3f}".format(e0MC),'lp')
    #legend.AddEntry(fitMC, "DY MC" "{0:.3f}".format(p0MC)+'#pm'+"{0:.3f}".format(e0MC) , 'lf')
    legend.AddEntry(graphs[dataword], "DY DATA " "{0:.3f}".format(p0DATA)+'#pm'+"{0:.3f}".format(e0DATA),'lp')
    #legend.AddEntry(fitDATA, "{0:.3f}".format(p0DATA)+'#pm'+"{0:.3f}".format(e0DATA) , 'lf')
    CMS_lumi.CMS_lumi(canvas, 4, iPos)
    canvas.Update()
    legend.Draw()

    canvas.SaveAs(graph+'.png')
    #canvas.SaveAs(graph+'.root')

filetosave.Close()
