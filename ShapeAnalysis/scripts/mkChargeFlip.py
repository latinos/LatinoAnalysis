#!/usr/bin/env python

# Extracts the Z->ee contribution from Data histograms
# Original macro: https://github.com/NTrevisani/NanoFlipper/blob/master/analysis/utils/mkzfit.py
# For the c-f prob extraction: https://github.com/NTrevisani/NanoFlipper/blob/master/analysis/utils/mkflipsf.py
# Does it fit here, or should I move it to another script?

# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# TO FIX: we use global variable like ptbins, etabins, eta_bin_array, eta_bin.
# We should in any case make all function use input arguments and NOT directly the global variables.
# At the moment, we directly point at the global variables in most cases
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

import sys, os
argv = sys.argv
sys.argv = argv[:1]

import ROOT
import optparse
import LatinoAnalysis.Gardener.hwwtools as hwwtools
#import os.path
#import logging
#import imp

import numpy as np
from   math import sqrt

from ROOT  import TMinuit , TFile , TCanvas , TH2D, gROOT, gStyle, TPad
from array import array as arr
from collections import OrderedDict
from ctypes import c_double, c_int, c_float
import random, csv

#from LatinoAnalysis.Tools.commonTools import *

ROOT.gROOT.SetBatch(ROOT.kTRUE)
ROOT.TH1.SetDefaultSumw2()

zmass = "91.1876"

# Define model global function
def model( i, par ):
     pass

# Electrons
# We hard-code the schema to: 
# ptb ins:  [(0., 20.), (20., 200.)] 
# eta bins: [(0., 1.4), (1.4, 2.5)]
ptbins_ele        = ["high_pt", "low_pt"]
etabins_ele       = ["EBEB", "EBEE", "EEEB", "EEEE"]
eta_bin_array_ele = [0.0, 1.4, 2.5]
eta_bin_ele       = ["EB","EE"]


# Also the flip model is fixed at the moment, in agreement with the schema
# from flipModel import model_2x2 as model
# 2x2 eta bin scheme
# parameters : 2
# eta_bin = [ 0., 1.4 , 2.5 ]
def model_2x2( i , par ):

     if   i == 0:  value = ( par[0] * (1-par[ 0]) + (1-par[ 0]) * par[ 0] ) / ( 1 - ( par[0] * (1-par[ 0]) + (1-par[ 0]) * par[ 0] ) )
     elif i == 1:  value = ( par[0] * (1-par[ 1]) + (1-par[ 0]) * par[ 1] ) / ( 1 - ( par[0] * (1-par[ 1]) + (1-par[ 0]) * par[ 1] ) )

     elif i == 2:  value = ( par[1] * (1-par[ 0]) + (1-par[ 1]) * par[ 0] ) / ( 1 - ( par[1] * (1-par[ 0]) + (1-par[ 1]) * par[ 0] ) )
     elif i == 3:  value = ( par[1] * (1-par[ 1]) + (1-par[ 1]) * par[ 1] ) / ( 1 - ( par[1] * (1-par[ 1]) + (1-par[ 1]) * par[ 1] ) )

     return value


# Muons
# We hard-code the schema to: 
# ptb ins:  [(0., 20.), (20., 200.)] 
# eta bins: [(0., 0.9), (0., 1.2), (1.2, 2.1), (2.1, 2.4)]
ptbins_muon        = ["high_pt", "low_pt"]
etabins_muon       = ["BE", "BB", "BO", "BF",
                      "EE", "EB", "EO", "EF",
                      "OE", "OB", "OO", "OF",
                      "FE", "FB", "FO", "FF"]
eta_bin_array_muon = [0.0, 0.9, 1.2, 2.1, 2.4]
eta_bin_muon       = ["B","E","O","F"]

# Also the flip model is fixed at the moment, in agreement with the schema
# from flipModel import model_4x4 as model
# 4x4 eta bin scheme
# parameters : 4
# eta_bin = [ 0.0, 0.9, 1.2, 2.1, 2.4 ]
def model_4x4( i , par ):

     if   i == 0:  value = ( par[0] * (1-par[ 0]) + (1-par[ 0]) * par[ 0] ) / ( 1 - ( par[0] * (1-par[ 0]) + (1-par[ 0]) * par[ 0] ) )
     elif i == 1:  value = ( par[0] * (1-par[ 1]) + (1-par[ 0]) * par[ 1] ) / ( 1 - ( par[0] * (1-par[ 1]) + (1-par[ 0]) * par[ 1] ) )
     elif i == 2:  value = ( par[0] * (1-par[ 2]) + (1-par[ 0]) * par[ 2] ) / ( 1 - ( par[0] * (1-par[ 2]) + (1-par[ 0]) * par[ 2] ) )
     elif i == 3:  value = ( par[0] * (1-par[ 3]) + (1-par[ 0]) * par[ 3] ) / ( 1 - ( par[0] * (1-par[ 3]) + (1-par[ 0]) * par[ 3] ) )

     elif i == 4:  value = ( par[1] * (1-par[ 0]) + (1-par[ 1]) * par[ 0] ) / ( 1 - ( par[1] * (1-par[ 0]) + (1-par[ 1]) * par[ 0] ) )
     elif i == 5:  value = ( par[1] * (1-par[ 1]) + (1-par[ 1]) * par[ 1] ) / ( 1 - ( par[1] * (1-par[ 1]) + (1-par[ 1]) * par[ 1] ) )
     elif i == 6:  value = ( par[1] * (1-par[ 2]) + (1-par[ 1]) * par[ 2] ) / ( 1 - ( par[1] * (1-par[ 2]) + (1-par[ 1]) * par[ 2] ) )
     elif i == 7:  value = ( par[1] * (1-par[ 3]) + (1-par[ 1]) * par[ 3] ) / ( 1 - ( par[1] * (1-par[ 3]) + (1-par[ 1]) * par[ 3] ) )

     elif i == 8: value = ( par[2] * (1-par[ 0]) + (1-par[ 2]) * par[ 0] ) / ( 1 - ( par[2] * (1-par[ 0]) + (1-par[ 2]) * par[ 0] ) )
     elif i == 9: value = ( par[2] * (1-par[ 1]) + (1-par[ 2]) * par[ 1] ) / ( 1 - ( par[2] * (1-par[ 1]) + (1-par[ 2]) * par[ 1] ) )
     elif i == 10: value = ( par[2] * (1-par[ 2]) + (1-par[ 2]) * par[ 2] ) / ( 1 - ( par[2] * (1-par[ 2]) + (1-par[ 2]) * par[ 2] ) )
     elif i == 11: value = ( par[2] * (1-par[ 3]) + (1-par[ 2]) * par[ 3] ) / ( 1 - ( par[2] * (1-par[ 3]) + (1-par[ 2]) * par[ 3] ) )

     elif i == 12: value = ( par[3] * (1-par[ 0]) + (1-par[ 3]) * par[ 0] ) / ( 1 - ( par[3] * (1-par[ 0]) + (1-par[ 3]) * par[ 0] ) )
     elif i == 13: value = ( par[3] * (1-par[ 1]) + (1-par[ 3]) * par[ 1] ) / ( 1 - ( par[3] * (1-par[ 1]) + (1-par[ 3]) * par[ 1] ) )
     elif i == 14: value = ( par[3] * (1-par[ 2]) + (1-par[ 3]) * par[ 2] ) / ( 1 - ( par[3] * (1-par[ 2]) + (1-par[ 3]) * par[ 2] ) )
     elif i == 15: value = ( par[3] * (1-par[ 3]) + (1-par[ 3]) * par[ 3] ) / ( 1 - ( par[3] * (1-par[ 3]) + (1-par[ 3]) * par[ 3] ) )

     return value


########################################################################
# Parametric fit to the SS/OS yields ratios to get the c-f probabilities
########################################################################

# The function to minimize is a Chi2
def fcn( npar , deriv , f , par , iflag):
    ''' Function to minimize to get c-f probabilities.

    We define here a simple Chi2. Meaning of parametrs:
    # npar:  number of parameters
    # deriv: array of derivatives df/dp_i (x), optional
    # f:     value of function to be minimised (typically chi2 or negLogL)
    # par:   the array of parameters
    # iflag: internal flag: 1 at first call, 3 at the last, 4 during minimisation
    '''
    
    if flavor == "ele":
         model = model_2x2
    if flavor == "muon":
         model = model_4x4

    chisq=0.0
    for i in range(0, nBins):
        delta = ( model( i, par ) - val[i] ) / err[i]
        chisq += delta*delta

    f[0] = chisq
    pass


def mk2Dfromcsv(ifile_, pt_bin_, eta_bin, output_dir):

    print("In mk2Dfromcsv:")
    print("ifile_  = {}".format(ifile_))
    print("pt_bin_ = {}".format(pt_bin_))
    print("eta_bin = {}".format(eta_bin))

    ptlist = [0.,20.,200.]
    ptlist = sorted(list(dict.fromkeys(ptlist)))

    # initialize csv
    dcsv = OrderedDict()
    c = 0

    for ibin in pt_bin_:
         with open("{}/chargeFlip_{}_SF.csv".format(output_dir, ibin), 'r') as f:
            for x, line in enumerate(csv.DictReader(f)):
                print(line) 
                dcsv[c] = line
                c += 1

    # Initialize mischarge probability h2d
    sf_hist = OrderedDict()
    for ihist in [ 'data' , 'data_sys' , 'mc' , 'mc_sys' , 'sf' , 'sf_sys' ]:
        sf_hist[ihist] = TH2D(ihist, 'charge flipping rate %s ; eta bin ; pt bin' %ihist, len(eta_bin)-1, arr('f' , eta_bin), len(ptlist)-1, arr('f', ptlist))

    h_dummy = sf_hist['data']
    for ibinX in range(1, h_dummy.GetNbinsX()+1):
        eta = h_dummy.GetXaxis().GetBinCenter(ibinX)
        for ibinY in range(1, h_dummy.GetNbinsY()+1):
            pt =  h_dummy.GetYaxis().GetBinCenter(ibinY)

            # Looking for correct (eta, pt) bin
            for num , ibn in dcsv.items():
                if eta >= float(ibn['etaDown']) and eta < float(ibn['etaUp']) and pt >= float(ibn['ptDown']) and pt < float(ibn['ptUp']):

                    data_flip = float(ibn['DATA']) ; data_flip_sys = float(ibn['DATAerr'])
                    mc_flip   = float(ibn['MC']) ; mc_flip_sys = float(ibn['MCerr'])
                    sf_flip   = float(ibn['SF']) ; sf_flip_sys = float(ibn['SFerr'])

                    sf_hist['data'].SetBinContent(    ibinX, ibinY, data_flip)
                    sf_hist['data'].SetBinError(      ibinX, ibinY, data_flip_sys)
                    sf_hist['data_sys'].SetBinContent(ibinX, ibinY, data_flip_sys)
                    sf_hist['mc'].SetBinContent(      ibinX, ibinY, mc_flip)
                    sf_hist['mc'].SetBinError(        ibinX, ibinY, mc_flip_sys)
                    sf_hist['mc_sys'].SetBinContent(  ibinX, ibinY, mc_flip_sys)
                    sf_hist['sf'].SetBinContent(      ibinX, ibinY, sf_flip)
                    sf_hist['sf'].SetBinError(        ibinX, ibinY, sf_flip_sys)
                    sf_hist['sf_sys'].SetBinContent(  ibinX, ibinY, sf_flip_sys)

    # Print histograms 
    c_data = TCanvas('c_data', 'charge flipping rate data', 800, 800)
    c_data.cd()
    tpad_data = TPad("", "", 0.0, 0.0, 1.0, 1.0)
    tpad_data.Draw()
    tpad_data.cd()
    tpad_data.SetLeftMargin(0.12)
    tpad_data.SetRightMargin(0.18)
    sf_hist['data'].Draw("colz,texte")
    c_data.Print('{}/CF_Data.png'.format(output_dir))
    c_data.Print('{}/CF_Data.pdf'.format(output_dir))

    c_MC = TCanvas('c_MC', 'charge flipping rate MC', 800, 800)
    c_MC.cd()
    tpad_MC = TPad("", "", 0.0, 0.0, 1.0, 1.0)
    tpad_MC.Draw()
    tpad_MC.cd()
    tpad_MC.SetLeftMargin(0.12)
    tpad_MC.SetRightMargin(0.18)
    sf_hist['mc'].Draw("colz,texte")
    c_MC.Print('{}/CF_MC.png'.format(output_dir))
    c_MC.Print('{}/CF_MC.pdf'.format(output_dir))

    c_sf = TCanvas('c_sf', 'charge flipping rate sf', 800, 800)
    c_sf.cd()
    tpad_sf = TPad("", "", 0.0, 0.0, 1.0, 1.0)
    tpad_sf.Draw()
    tpad_sf.cd()
    tpad_sf.SetLeftMargin(0.12)
    tpad_sf.SetRightMargin(0.18)
    sf_hist['sf'].Draw("colz,texte")
    c_sf.Print('{}/SF.png'.format(output_dir))
    c_sf.Print('{}/SF.pdf'.format(output_dir))

    # Save it
    h_fileout = TFile.Open("{}/chargeFlip_SF.root".format(output_dir), "RECREATE")
    map(lambda x: sf_hist[x].Write(), sf_hist)
    h_fileout.Close()
    pass


def mk2DHisto(bins_in, name, eta_bin, bins_error_in=None, ztitle="charge flip probability" ):

    eta_bin_arr = arr('f', eta_bin)

    h_ratio_create=TH2D(name, '%s ; lepton 1 Eta ; lepton 2 Eta' %name, len(eta_bin)-1, eta_bin_arr, len(eta_bin)-1 , eta_bin_arr )
    counter=0
    for i in range(0, len(eta_bin) - 1):
        for j in range(0, len(eta_bin) - 1):
            h_ratio_create.SetBinContent(i+1, j+1, bins_in[counter])
            if bins_error_in is not None: h_ratio_create.SetBinError(i+1, j+1, bins_error_in[counter])
            counter += 1
    h_ratio_create.GetZaxis().SetTitle(ztitle)
    h_ratio_create.SetMarkerSize(1.5)
    return h_ratio_create


def mkValidation(ifile_, flipPro, h_val, ptbin_, year, output_dir):

     print("In mkValidation:")
     print("ifile_:   {}".format(ifile_))
     print("ptbin_:   {}".format(ptbin_))

     if flavor == "ele":
          model = model_2x2
     if flavor == "muon":
          model = model_4x4

     output = '{}/Step4_validateFlip/{}'.format(output_dir, ptbin_)
     os.system('mkdir -p {}'.format(output))

     c = TCanvas('c', 'ratio_postfit_validation', 1200, 800)
     c.Divide(2,2)

     for ids in ['DATA','MC']:
          dim     = len(h_val[year][ids][0]) # Infer dimension
          print("Dim: {}".format(dim))
          flipper = map(lambda x: x[0], flipPro[year][ids]) # Extract the fitted value (mischarge probability)

          bins_postfit = map( lambda x: model(x,flipper) , list(range(0,dim)) ) # Reproduce the ratio
          print("bins_postfit: {}".format(bins_postfit))

          bins_prefit = h_val[year][ids][0]
          bins_diff = map(lambda x : (abs(bins_prefit[x] - bins_postfit[x])/bins_prefit[x])*100. , list(range(0,dim)) )
          # bins_diff = map(lambda x : (abs(bins_prefit[x] - bins_postfit[x])) , list(range(0,dim)) )

          c.cd(1) ; h_prefit  = mk2DHisto(bins_prefit,  'h_ratio_prefit_%s'  %ids, eta_bin_array); h_prefit.Draw("Colz TEXT45")
          c.cd(2) ; h_postfit = mk2DHisto(bins_postfit, 'h_ratio_postfit_%s' %ids, eta_bin_array); h_postfit.Draw("Colz TEXT45")
          c.cd(3) ; h_diff    = mk2DHisto(bins_diff,    'h_ratio_diff_%s'    %ids, eta_bin_array, None, 'rel. Difference in percent'); h_diff.Draw("Colz TEXT45")

          c.Update()
          c.Print( "{}/val_ratio_postprefit_{}.png".format(output,ids))
     pass


def outFormat(ifile_, pt_bin_, fitted_prob_, out_, output_dir, useCsv=True):

    print("In outFormat: ")
    print("pt_bin_:  {}".format(pt_bin_))
    print("ifile_ :  {}".format(ifile_))

    pt_lo = 20.
    pt_hi = 200.
    if pt_bin_ == 'low_pt':
         pt_lo = 0.
         pt_hi = 20.

    outfile = open('{}/chargeFlip_{}_SF.csv'.format(output_dir, pt_bin_), "w")
    if not useCsv:
         outfile = open("{}/chargeFlip_{}_SF.txt".format(output_dir, pt_bin_), "w")

    print("Outfile: {}".format(outfile))

    row_list = []

    for i, ieta in enumerate(eta_bin_array):
        row = ""
        if i == (len(eta_bin_array) - 1): continue
        row =  '{:.1f} , {:.1f} , '.format(ieta, eta_bin_array[i+1])
        row += '{:.1f} , {:.1f} , {:.3e} , {:.3e} , {:.3e} , {:.3e} , {:.3e} , {:.3e}'\
                .format(pt_lo, pt_hi, fitted_prob_['DATA'][i][0], fitted_prob_['DATA'][i][1], fitted_prob_['MC'][i][0], fitted_prob_['MC'][i][1], out_[i][0], out_[i][1])
        row_list.append(row if not useCsv else [row])

    # preprocess
    fout = []
    for i, line in enumerate(row_list):
        header = ['etaDown', 'etaUp', 'ptDown', 'ptUp', 'DATA', 'DATAerr', 'MC', 'MCerr', 'SF', 'SFerr']
        if i==0: 
            fout.append(' , '.join(header) if not useCsv else header)
        fout.append(line if not useCsv else line[0].replace(' ','').split(','))

    with outfile as out_handler:
        if not useCsv:
            print("Writing to txt format")
            for listitem in fout:
                out_handler.write('%s\n' %listitem)
        else:
            print("Wiriting to CSV format")
            writer = csv.writer(out_handler)
            writer.writerows(fout)
    pass


def flatten2D(h2d):
     
    bins=[]; 
    errs=[]
    for i in range(1, h2d.GetNbinsX() + 1):
        for j in range(1, h2d.GetNbinsY() + 1):
            bins.append(h2d.GetBinContent(i, j))
            errs.append(h2d.GetBinError(i, j))
    return [bins, errs]


def fit_SF(p, perr):

     global val, err, nBins
     val = p
     err = perr
     nBins=len(val)

     # Fit parameters: two per pT bin --> [cf(barrel), cf(endcap)]
     name = []
     if flavor == "ele":
          name = ['q0', 'q1']
     if flavor == "muon":
          name = ['q0', 'q1', 'q2', 'q3']

     npar=len(name)
     print("Number of parameters: {}".format(npar))
     # Initial parameters values
     vstart = arr('d', npar*[0.1])
     # Initial step size
     step = arr( 'd' , npar*[0.000001] )

     # Set up MINUIT
     gMinuit = TMinuit(npar)         # initialize TMinuit with maximum of npar parameters
     gMinuit.SetFCN(fcn)             # set function to minimize
     arglist = arr('d', npar*[0.01]) # set error definition
     ierflg = c_int(0)

     arglist[0] = 1. # 1 sigma is Delta chi2 = 1
     gMinuit.mnexcm("SET ERR", arglist, 1, ierflg)

     # Set starting values and step size for parameters
     # Define the parameters for the fit
     for i in range(0,npar): 
          gMinuit.mnparm(i, name[i], vstart[i], step[i], 0.000001, 0.01, ierflg)
          # gMinuit.mnparm(i, name[i], vstart[i], step[i], 0, 0, ierflg) # parameters have no physical limits

     # Now ready for minimization step
     arglist [0] = 500                               # Number of calls for FCN before giving up
     arglist [1] = 1.                                # Tolerance
     gMinuit.mnexcm("MIGRAD" , arglist , 2 , ierflg) # execute the minimisation

     # Check TMinuit status
     amin , edm , errdef = c_double(0.) , c_double(0.) , c_double(0.)
     # amin , edm , errdef = 0.,0.,0.
     nvpar , nparx , icstat = c_int(0) , c_int(0) , c_int(0)
     gMinuit.mnstat (amin , edm , errdef , nvpar , nparx , icstat )
     # gMinuit.mnprin(3,amin) # print-out by Minuit

     # meaning of parameters:
     #   amin:   value of fcn distance at minimum (=chi^2)
     #   edm:    estimated distance to minimum
     #   errdef: delta_fcn used to define 1 sigam errors
     #   nvpar:  total number of parameters
     #   icstat: status of error matrix:
     #           3 = accurate
     #           2 = forced pos. def
     #           1 = approximative
     #           0 = not calculated
     #

     # Get results from MINUIT
     finalPar = []
     finalParErr = []
     p, pe = c_double(0.) , c_double(0.)
     for i in range(0,npar):
          # Get parameters and errors
          gMinuit.GetParameter(i, p, pe)
          finalPar.append(float(p.value))
          finalParErr.append(float(pe.value))

     # Get covariance matrix
     buf = arr('d' , npar*npar*[0.])

     # Get error matrix
     gMinuit.mnemat( buf , npar )
     emat = np.array( buf ).reshape( npar , npar )

     # --> provide formatted output of results
     print("\n")
     print("*==* MINUIT fit completed:")
     print('fcn@minimum = %.3g'%(amin.value ), " error code =" , ierflg.value , " status =" , icstat.value , " (if its 3, mean accurate)")
     print( " Results: \t value error corr. mat." )
     for i in range(0, npar):
          print('%s: \t%10.3e +/- %.1e'%(name[i], finalPar[i], finalParErr[i]))
          for j in range (0,i): 
               print('%+.3g'%(emat[i][j]/np.sqrt(emat[i][i])/np.sqrt(emat[j][j])))
          print("\n")

     return [ [i,j]  for i,j in zip(finalPar , finalParErr) ]


def mkSf(ifile_, ptbin_, year, output_dir, var, outcsv_=True ):

     print("In mkSf:")
     print("year   = {}".format(year))
     print("ptbin_ = {}".format(ptbin_))

     fitted_prob = OrderedDict()
     h4val       = OrderedDict()
     out         = OrderedDict()
     h_ratio     = {}
     
     name = "{}_{}".format(ptbin_, var)

     h_data = TFile.Open("{0}/Step3_Chflipfit/{1}/ratio_DATA_{1}.root".format(output_dir, name), "READ")
     h_mc   = TFile.Open("{0}/Step3_Chflipfit/{1}/ratio_DY_{1}.root".  format(output_dir, name), "READ") # MC input is hard-coded to DY for now

     # Fit
     fitted_prob[year] = {}
     h4val[year] = {}
     for ids in ['DATA', 'MC']:
          print(ids)
          h4val[year][ids] = flatten2D(h_data.Get('h2_DATA') if ids=='DATA' else h_mc.Get('h2_DY') )
          fitted_prob[year][ids] = fit_SF(arr('f', h4val[year][ids][0]), arr('f', h4val[year][ids][1]))
     out[year] = map(lambda x, y : [x[0]/y[0], sqrt((x[1]*x[1])/(x[0]*x[0]) + (y[1]*y[1])/(y[0]*y[0]))], fitted_prob[year]['DATA'], fitted_prob[year]['MC'])

     print("Output: {}".format(out["2018"]))

     print("h4val: {}".format(h4val))

     # Save output on a CSV file
     outFormat(ifile_, ptbin_, fitted_prob[year], out[year], output_dir, outcsv_)

     return [fitted_prob, h4val, out]


# Main function
def mkflipsf(variable, year, output_dir, var):

    if not os.path.exists(output_dir):
        print("Error, path folder {} does not exist".format(output_dir))
        sys.exit()

    # if flavor == "ele":
    #      ptbins        = ptbins_ele
    #      etabins       = etabins_ele
    #      eta_bin_array = eta_bin_array_ele
    #      eta_bin       = eta_bin_ele
    #      model         = model_2x2
    # if flavor == "muon":
    #      ptbins        = ptbins_muon
    #      etabins       = etabins_muon
    #      eta_bin_array = eta_bin_array_muon
    #      eta_bin       = eta_bin_muon
    #      model         = model_4x4

    # Fit and validate
    for iptbin in ptbins :
        ifile   = "{}/fit_summary_{}.txt".format(output_dir, iptbin)
        summary = open(ifile, "w")
        fpout   = []
        # Get c-f SFs and save them into a csv file
        fitted    = mkSf(ifile, iptbin, year, output_dir, var, True)
        mischarge = fitted[0]
        histo_val = fitted[1]
        epsilon   = fitted[2]
        
        fpout.append(" ===> scale factor DATA/MC for %s" %year)
        for num, isf in enumerate(epsilon[year]):
             fpout.append('q{} data : {:.3e} +/- {:.3e} ; mc : {:.3e} +/- {:.3e} ; SF : {:.3e} +/- {:.3e} ( rel.error : {:.2f} % )'\
                          .format( num , 
                                   mischarge[year]['DATA'][num][0] , mischarge[year]['DATA'][num][1] , 
                                   mischarge[year]['MC'][num][0]   , mischarge[year]['MC'][num][1]   , 
                                   isf[0] , isf[1] , (isf[1]/isf[0])*100 ) )
             print('q{} data : {:.3e} +/- {:.3e} ; mc : {:.3e} +/- {:.3e} ; SF : {:.3e} +/- {:.3e} ( rel.error : {:.2f} % )'\
                          .format( num , 
                                   mischarge[year]['DATA'][num][0] , mischarge[year]['DATA'][num][1] , 
                                   mischarge[year]['MC'][num][0]   , mischarge[year]['MC'][num][1]   , 
                                   isf[0] , isf[1] , (isf[1]/isf[0])*100 ) )

        # On-the-fly validation
        mkValidation(ifile, mischarge, histo_val, iptbin, year, output_dir)

        # Diagnostics
        with summary as out_handling:
            for listitem in fpout:
                out_handling.write('{}\n'.format(listitem))
        os.system('cat {}/fit_summary_{}.txt'.format(output_dir, iptbin))

    # Make histogram from CSV
    list_file = []
    for iptbin in ptbins:
         list_file.append("{}/fit_summary_{}.txt".format(output_dir, iptbin))
    mk2Dfromcsv(list_file, ptbins, eta_bin_array, output_dir)


##############################################################
# Signal + bkg fit to extract yields in the SS/OS phase spaces
##############################################################

# Signal + bkg fit
def fit(filename, ptbin, output, year, var, flavor):

    print(">>>>>>>>>>>>>>>>>>>> Extracting signal and background yields")
    fin             = ROOT.TFile.Open(filename)

    if flavor == "ele":
         ptbins        = ptbins_ele
         etabins       = etabins_ele
         eta_bin_array = eta_bin_array_ele
         eta_bin       = eta_bin_ele
         model         = model_2x2
    if flavor == "muon":
         ptbins        = ptbins_muon
         etabins       = etabins_muon
         eta_bin_array = eta_bin_array_muon
         eta_bin       = eta_bin_muon
         model         = model_4x4

    # Hard coded, at least for now
    histos_DATA     = []
    histos_DY       = []
    histos_DY_LO    = []
    count_DATA      = {}
    count_DATA_err  = {}
    count_DY        = {}
    count_DY_err    = {}
    count_DY_LO     = {}
    count_DY_LO_err = {}

    print("Input file name = {}".format(filename))
    print("ptbin           = {}".format(ptbin))
    print("Output          = {}".format(output))
    print("Year            = {}".format(year))
    print("Eta_bin         = {}".format(eta_bin))
    print("Eta_bin_array   = {}".format(eta_bin_array))
    print("Variable        = {}".format(var))

    output += "/{}_mll".format(ptbin)
    os.system('mkdir -p {}'.format(output))

    # Store all interesting histograms                                                                                                 
    for tkey in fin.GetListOfKeys():
        key = tkey.GetName()
        print("I found this cut: {}".format(key))
        if ptbin not in key: continue
        # We want to treat differently DATA and MC histograms                                                                          
        # For MC histograms ['DY','DY_LO'] we can just count the events                                                                
        # For DATA, we need to extract the DY events through a fit                                                                     
        histos_DATA.append(key  + "/{}/histo_DATA".format(var))
        histos_DY.append(key    + "/{}/histo_DY".format(var))
        histos_DY_LO.append(key + "/{}/histo_DY_LO".format(var))
        print("---> histogram stored!")

    # Extract DY yields from data using a sig+bkg fit                                                                                  
    for ihis in histos_DATA:
        print("Looking at histogram called: {}".format(ihis))
        if var not in ihis: continue
        print("fit to: {}".format(ihis))
        htmp = fin.Get(ihis)
        for ibin in range(0, htmp.GetNbinsX()):
            if htmp.GetBinContent(ibin+1) < 0:
                htmp.SetBinContent(ibin+1, 0)

        nEvent = htmp.Integral()
        nHalf  = 0.8*nEvent

        # Roofit setup
        w = ROOT.RooWorkspace("w")
        # Signal function definition
        w.factory("BreitWigner:sig_bw(mll[76.2, 106.2], bwmean[91.1876,89,93], bwgamma[2.4952,2.4,2.6])")
        w.factory("Gaussian:sig_gau(mll, gaumean[0,-100,100], gausigma[2.5,0.1,5])")
        w.factory("FCONV:bxc(mll,sig_bw,sig_gau)")
        # Background function definition
        w.factory("Exponential:bkg(mll,exalpha[-1.,-10,1])")
        # Sum everything to build the model
        w.factory("SUM:model(nsig[{},0,{}]*bxc, nbkg[{},0,{}]*bkg)".format(str(nHalf), str(nEvent), str(nEvent-nHalf), str(nEvent)))

        # Plot distributions
        mll = w.var(var)
        pdf = w.pdf('model')
        dh  = ROOT.RooDataHist('d'+ihis, 'd'+ihis, ROOT.RooArgList(mll), htmp)
        getattr(w, 'import')(dh)
        r    = pdf.fitTo(dh, ROOT.RooFit.Save(True), ROOT.RooFit.Minimizer("Minuit2","Migrad"))
        c    = ROOT.TCanvas()
        plot = mll.frame(ROOT.RooFit.Title(ihis))
        dh.plotOn(plot)
        pdf.plotOn(plot)
        pdf.plotOn(plot, ROOT.RooFit.Components("bkg"), ROOT.RooFit.LineStyle(2))
        pdf.plotOn(plot, ROOT.RooFit.Components("bxc"), ROOT.RooFit.LineColor(2), ROOT.RooFit.LineStyle(2))
        pdf.paramOn(plot,ROOT.RooFit.Layout(0.57,0.97,0.85))
        plot.Draw()
        c.GetPrimitive("model_paramBox").SetFillStyle(0)
        c.GetPrimitive("model_paramBox").SetBorderSize(0)

        ihis_out_name = ihis.replace("/", "_")
        c.SaveAs(output + '/c_' + ihis_out_name + '.png')
        mc = ROOT.RooStats.ModelConfig("ModelConfig_" + ihis_out_name, w)
        mc.SetPdf(pdf)
        mc.SetParametersOfInterest(ROOT.RooArgSet(w.var("nsig")))
        mc.SetSnapshot(ROOT.RooArgSet(w.var("nsig")))
        mc.SetObservables(ROOT.RooArgSet(w.var(var)))
        w.defineSet("nuisParams", "nbkg,bwmean,bwgamma,gaumean,gausigma,exalpha")
        nuis = getattr(w, 'set')("nuisParams")
        mc.SetNuisanceParameters(nuis)
        getattr(w, 'import')(mc)
        w.writeToFile(output + '/' + ihis_out_name + "_config.root", True)
        count_DATA[ihis_out_name] = w.var("nsig").getVal()
        count_DATA_err[ihis_out_name] = w.var("nsig").getError()
        print("Count     = {}".format(count_DATA[ihis_out_name]))
        print("Count err = {}".format(count_DATA_err[ihis_out_name]))


    # DY NLO MC yields: just take integral of the histogram                                                                            
    for ihis in histos_DY:
        print("Looking for histogram called: {}".format(ihis))
        if 'mll' not in ihis: continue
        print('fit to: ',ihis)
        htmp=fin.Get(ihis)
        for ibin in range(0,60):
            if htmp.GetBinContent(ibin+1)<0:
                htmp.SetBinContent(ibin+1,0)

        nEvent   = htmp.Integral()
        nEntries = htmp.GetEntries()

        ihis_out_name = ihis.replace("/", "_")

        count_DY[ihis_out_name] = nEvent
        count_DY_err[ihis_out_name] = 1
        if nEntries != 0:
            count_DY_err[ihis_out_name] = nEvent/np.sqrt(nEntries)
        print("Count DY     = {}".format(count_DY[ihis_out_name]))
        print("Count DY err = {}".format(count_DY_err[ihis_out_name]))

    # DY LO MC yields: just take integral of the histogram                                                                             
    for ihis in histos_DY_LO:
        print("Looking for histogram called: {}".format(ihis))
        if 'mll' not in ihis: continue
        print('fit to: ',ihis)
        htmp=fin.Get(ihis)
        for ibin in range(0,60):
            if htmp.GetBinContent(ibin+1)<0:
                htmp.SetBinContent(ibin+1,0)

        nEvent   = htmp.Integral()
        nEntries = htmp.GetEntries()

        ihis_out_name = ihis.replace("/", "_")

        count_DY_LO[ihis_out_name] = nEvent
        count_DY_LO_err[ihis_out_name] = 1
        if nEntries != 0:
            count_DY_LO_err[ihis_out_name] = nEvent/np.sqrt(nEntries)
        print("Count DY LO     = {}".format(count_DY_LO[ihis_out_name]))
        print("Count DY LO err = {}".format(count_DY_LO_err[ihis_out_name]))

    # Prepare output
    fout     = ROOT.TFile(output + '/Count_' + ptbin + ".root", 'recreate')
    h_ss_sub = ROOT.TH2D()
    h_os_sub = ROOT.TH2D()

    samples = {
        'DATA'  : [count_DATA,  count_DATA_err],
        'DY'    : [count_DY,    count_DY_err],
        'DY_LO' : [count_DY_LO, count_DY_LO_err],
    }
    ss_plots = []
    os_plots = []

    # Get parameters from the fit and store them into TH2D
    for isample in samples:
        h_ss = ROOT.TH2D('h_' + ptbin + '_ss_' + isample, 'h_' + ptbin + '_ss_' + isample, len(eta_bin), eta_bin_array[0], eta_bin_array[-1], len(eta_bin), eta_bin_array[0], eta_bin_array[-1])
        h_os = ROOT.TH2D('h_' + ptbin + '_os_' + isample, 'h_' + ptbin + '_os_' + isample, len(eta_bin), eta_bin_array[0], eta_bin_array[-1], len(eta_bin), eta_bin_array[0], eta_bin_array[-1])
        for i in range(0, len(eta_bin)):
            for j in range(0, len(eta_bin)):
                if flavor == "ele": 
                     h_ss.SetBinContent(i+1 , j+1 , samples[isample][0]['DY_ee_cf_ss_' + ptbin + '_' + eta_bin[i] + eta_bin[j] + '_mll_histo_' + isample])
                     h_ss.SetBinError  (i+1 , j+1 , samples[isample][1]['DY_ee_cf_ss_' + ptbin + '_' + eta_bin[i] + eta_bin[j] + '_mll_histo_' + isample])
                     h_os.SetBinContent(i+1 , j+1 , samples[isample][0]['DY_ee_cf_os_' + ptbin + '_' + eta_bin[i] + eta_bin[j] + '_mll_histo_' + isample])
                     h_os.SetBinError  (i+1 , j+1 , samples[isample][1]['DY_ee_cf_os_' + ptbin + '_' + eta_bin[i] + eta_bin[j] + '_mll_histo_' + isample])
                elif flavor == "muon": 
                     h_ss.SetBinContent(i+1 , j+1 , samples[isample][0]['DY_mm_cf_ss_' + ptbin + '_' + eta_bin[i] + eta_bin[j] + '_mll_histo_' + isample])
                     h_ss.SetBinError  (i+1 , j+1 , samples[isample][1]['DY_mm_cf_ss_' + ptbin + '_' + eta_bin[i] + eta_bin[j] + '_mll_histo_' + isample])
                     h_os.SetBinContent(i+1 , j+1 , samples[isample][0]['DY_mm_cf_os_' + ptbin + '_' + eta_bin[i] + eta_bin[j] + '_mll_histo_' + isample])
                     h_os.SetBinError  (i+1 , j+1 , samples[isample][1]['DY_mm_cf_os_' + ptbin + '_' + eta_bin[i] + eta_bin[j] + '_mll_histo_' + isample])
        ss_plots.append(h_ss)
        os_plots.append(h_os)

    # Write output TH2D into rootfile
    map(lambda x: x.Write() , ss_plots+os_plots)
    fout.Close()

    pass


# Takes as input the rootfile produced by fit()
# and calculates the N_SS/N_OS ratio
def ratio(filename, data, ptbin, output):

    fin  = ROOT.TFile.Open(filename)
    print("h_ss in ratio function: h_{}_ss_{}".format(ptbin, data))
    print("h_os in ratio function: h_{}_os_{}".format(ptbin, data))

    # Reading input and preparing output
    h_ss    = fin.Get('h_{}_ss_{}'.format(ptbin, data))
    h_os    = fin.Get('h_{}_os_{}'.format(ptbin, data))
    h_ratio = h_ss.Clone()
    h_ratio.Divide(h_os)

    # Getting rid of low stats figure, unreliable
    # Changed to: if SS histo has 0 entries, ratio bin content is set to 0.01, with error 0.001
    # This aspect may be tuned better
    for i in range(0, h_ratio.GetNbinsX()):
        for j in range(0, h_ratio.GetNbinsY()):
            # if h_ss.GetBinContent(i+1, j+1) < 10:                                
            if h_ss.GetBinContent(i+1, j+1) == 0:
                h_ratio.SetBinContent(i+1, j+1, 0.001)
                h_ratio.SetBinError(  i+1, j+1, 0.0002)
    h_ratio.SetName('h2_{}'.format(data))
    h_ratio.SetTitle('N_{SS}/N_{OS}')

    # Create output rootfile
    os.system('mkdir -p {}'.format(output))
    fout = ROOT.TFile('{}/ratio_{}_{}_mll.root'.format(output, data, ptbin), 'recreate')
    h_ratio.Write()
    fout.Write()
    fout.Close()

    c = ROOT.TCanvas()
    ROOT.gStyle.SetOptStat(0)
    h_ss.Draw("colz texte")

    c.SaveAs('{}/h_ss_{}_{}_mll.png'.format(output,data,ptbin))
    c.Clear()
    h_os.Draw("colz texte")
    c.SaveAs('{}/h_os_{}_{}_mll.png'.format(output,data,ptbin))
    c.Clear()
    h_ratio.Draw("colz texte")
    c.SaveAs('{}/h_ratio_{}_{}_mll.png'.format(output,data,ptbin))

    pass


# Main function
def mkzfit(input_file, output_dir, era, var, flavor):

    output_1 = "{}/Step2_Zmassfit".format(output_dir)
    output_2 = "{}/Step3_Chflipfit".format(output_dir)

    if not os.path.exists(output_1): os.system('mkdir -p {}'.format(output_1))
    if not os.path.exists(output_2): os.system('mkdir -p {}'.format(output_2))

    if flavor == "ele":
         ptbins        = ptbins_ele
         etabins       = etabins_ele
         eta_bin_array = eta_bin_array_ele
         eta_bin       = eta_bin_ele
         model         = model_2x2
    if flavor == "muon":
         ptbins        = ptbins_muon
         etabins       = etabins_muon
         eta_bin_array = eta_bin_array_muon
         eta_bin       = eta_bin_muon
         model         = model_4x4

    for iptbin in ptbins :
        name = "{}_{}".format(iptbin, var)
        print("Name: {}".format(name))
        # Signal + bkg fit to data distributions.
        # MC yields are also extracted here, just counting the expected events
        fit(input_file, iptbin, output_1, era, var, flavor)

        # Compute SS/OS ratio
        for idata in ['DATA', 'DY', 'DY_LO']:
            print("Ratio input file: {}/{}/Count_{}.root".format(output_1, name, iptbin))
            ratio("{}/{}/Count_{}.root".format(output_1, name, iptbin), idata, iptbin, '{}/{}'.format(output_2, name))

##############################################################
# What we actually execute when we run the script
##############################################################

if __name__ == '__main__':

    sys.argv = argv

    usage = 'usage: %prog [options]'
    parser = optparse.OptionParser(usage)
    
    parser.add_option('--input_file', dest='input_file', help='input file with histograms',                              default='DEFAULT')
    parser.add_option('--output_dir', dest='output_dir', help='output directory',                                        default='test')
    parser.add_option('--era'       , dest='era'       , help='Run 2 data taking period',                                default='2018')
    parser.add_option('--var'       , dest='var'       , help='Name of the variable to fit. Must be the invariant mass', default='mll')
    parser.add_option('--steps'     , dest='steps'     , help='Steps to perform: z_fit, cf_fit, both',                   default='both')
    parser.add_option('--flavor'    , dest='flavor'    , help='Particle flavor: ele, muon',                              default='ele')
 
    # Read default parsing options as well
    #hwwtools.addOptions(parser)
    #hwwtools.loadOptDefaults(parser)
    (opt, args) = parser.parse_args()

    sys.argv.append( '-b' )
    ROOT.gROOT.SetBatch()

    if opt.input_file == 'DEFAULT' :
        raise ValueError("Please specify input rootfile")

    if opt.steps != 'z_fit' and opt.steps != 'cf_fit' and opt.steps != 'both':
        raise ValueError("Please introduce a valid step: z_fit, cf_fit, or both")

    input_file    = opt.input_file
    output_dir    = opt.output_dir
    era           = opt.era
    var           = opt.var
    steps         = opt.steps
    global flavor 
    flavor        = opt.flavor

    # Global variables definitions
    global ptbins
    global etabins
    global eta_bin_array
    global eta_bin

    if flavor == "ele":
         ptbins        = ptbins_ele
         etabins       = etabins_ele
         eta_bin_array = eta_bin_array_ele
         eta_bin       = eta_bin_ele

    if flavor == "muon":
         ptbins        = ptbins_muon
         etabins       = etabins_muon
         eta_bin_array = eta_bin_array_muon
         eta_bin       = eta_bin_muon

    # Move input parameters to variables
    print("Input file       = {}".format(input_file))
    print("Output directory = {}".format(output_dir))
    print("Era              = {}".format(era))
    print("Variable         = {}".format(var))
    print("Steps            = {}".format(steps))
    print("Flavor           = {}".format(flavor))

    # Execute sig+bkg fit to get N_SS and N_OS yields,
    # then prepare the ratios N_SS/N_OS
    if steps == 'both' or steps == 'z_fit':
        mkzfit(input_file, output_dir, era, var, flavor)
    
    # Extract the charge-flip probabilities and scale factors
    if steps == 'both' or steps == 'cf_fit':
        mkflipsf(var, era, output_dir, var)
