#!/usr/bin/env python

import os, sys
argv = sys.argv
sys.argv = argv[:1]

import optparse
import LatinoAnalysis.Gardener.hwwtools as hwwtools
import math

from ROOT import TCanvas, TPad, TFile, TPaveText, TLegend
from ROOT import TH1D, TH1F, TF1, TGraphErrors, TMultiGraph

from LatinoAnalysis.Tools.commonTools import *


if __name__ == '__main__':

    sys.argv = argv

    usage = 'usage: %prog [options]'
    parser = optparse.OptionParser(usage)
    
    parser.add_option('--os_ss_cutsFile' , dest='os_ss_cutsFile' , help='input file with os-ss cuts dictionary'      , default='DEFAULT')
    parser.add_option('--inputFileSS'    , dest='inputFileSS'    , help='input file with same-sign histograms'       , default='DEFAULT')
    parser.add_option('--inputFileOS'    , dest='inputFileOS'    , help='input file with opposite-sign histograms'   , default='DEFAULT')
    parser.add_option('--outputDir'      , dest='outputDir'      , help='output directory'                           , default='DEFAULT')
    parser.add_option('--outputFile'     , dest='outputFile'     , help='output file with histograms'                , default='DEFAULT')
    parser.add_option('--year'           , dest='year'           , help='data-taking year'                           , default='2016')
    parser.add_option('--non_cf_bkg'     , dest='non_cf_bkg'     , help='backgrounds not affected by charge-flip'    , default='DEFAULT')
    parser.add_option('--run_debug'      , dest='debug'          , help='run on debug mode'                          , default=False)
 
    # read default parsing options as well
    (opt, args) = parser.parse_args()

    sys.argv.append( '-b' )
    ROOT.gROOT.SetBatch()

    print("Dictionary with OS/SS cuts              = {}".format(opt.os_ss_cutsFile))
    print("Same-sign input file                    = {}".format(opt.inputFileSS))
    print("Opposite-sign input file                = {}".format(opt.inputFileOS))
    print("Output directory                        = {}".format(opt.outputDir))
    print("Output file                             = {}".format(opt.outputFile))
    print("Year                                    = {}".format(opt.year))
    print("Backgrounds not affected by charge-flip = {}".format(opt.non_cf_bkg))
    print("Debug                                   = {}".format(opt.debug))

    if opt.debug == "True":
      opt.debug = True

    # Exceptions
    if opt.os_ss_cutsFile == 'DEFAULT' :
        raise ValueError("Please insert input file with os-ss cuts dictionary")

    if opt.inputFileSS == 'DEFAULT' :
        raise ValueError("Please insert input file with same-sign histograms")

    if opt.inputFileOS == 'DEFAULT' :
        raise ValueError("Please insert input file with opposite-sign histograms")

    if opt.inputFileOS == 'DEFAULT' :
        raise ValueError("Please insert output directory")

    if opt.outputFile == 'DEFAULT' :
        raise ValueError("Please insert output file")

    if opt.non_cf_bkg == 'DEFAULT' :
        raise ValueError("Backgrounds not affected by charge-flip")

    # Transform 'non_cf_bkg' in a list
    non_cf_bkg = opt.non_cf_bkg.split(',')

    output_file_name = opt.outputDir + "/" + opt.outputFile
    print("Output file complete path = {}".format(output_file_name))

    print("Copying same-sign histogram file into output file...")
    os.system("cp {} {}".format(opt.inputFileSS, output_file_name))

    # Get dictionary of OS to SS cuts
    dict_os_ss_cuts = {}
    if os.path.exists(opt.os_ss_cutsFile,) :
      handle = open(opt.os_ss_cutsFile,'r')
      exec(handle)
      handle.close()

    keys_list = list(dict_os_ss_cuts.keys())
    print("List of keys = {}".format(keys_list))
    for key, value in dict_os_ss_cuts.items():
        print(key, " --> ", value)

    # Open output file to update it
    output_file = TFile.Open(output_file_name, "UPDATE")

    # Open same-sign input file
    file_ss = TFile.Open(opt.inputFileSS)
    directories_ss = file_ss.GetListOfKeys()
    print("Same-sign cuts:")
    for d in directories_ss:
        print(d)

    # Open opposite-sign input file
    file_os = TFile.Open(opt.inputFileOS)
    directories_os = file_os.GetListOfKeys()
    print("Opposite-sign cuts:")
    for d in directories_os:
        print(d)


    # Copy the SS-input-file structure into the output file

    # First layer: cuts
    for cut in file_ss.GetListOfKeys():
      if cut.IsFolder() == False: continue 
      cut_dir = cut.GetName()
      # output_file.mkdir(cut_dir) 
      if opt.debug == True and cut_dir != "hww2l2v_13TeV_WH_SS_ee_1j_minus_pt2ge20": continue # for debugging, just consider one cut
      print("Current cut: {}".format(cut_dir))

      # Second layer: variables
      file_ss.cd(cut_dir)
      for var in ROOT.gDirectory.GetListOfKeys() :
        if var.IsFolder() == False: continue
        var_dir = var.GetName() 
        # output_file.mkdir(cut_dir + '/' + var_dir)
        if opt.debug == True and var_dir != "mll": continue # for debugging, just consider one variable (mll)
        print("  Current variable: {}".format(var_dir))
        
        # Third layer: histograms
        file_ss.cd(cut_dir + '/' + var_dir)
        h_tmp = 0         # nominal cf histogram
        h_tmp_cf_up = 0   # cf histogram with cf variation up
        h_tmp_cf_down = 0 # cf histogram with cf variation down
        h_non_cf = 0
        for histo in ROOT.gDirectory.GetListOfKeys() :
          h_name = histo.GetName() 
          output_file.cd(cut_dir + '/' + var_dir)
          if 'DATA' in h_name:
            print("DATA histogram name: {}".format(h_name))

          if opt.debug == True and ("Up" in h_name or "Down" in h_name or "Var" in h_name or "DY_OS" in h_name): continue # for debugging, not copying systematic-variation histograms

          # Take Data histograms from the opposite-sign rootfile
          # Then subtracts the contributions from backgrounds
          # not affected by charge-flip
          h_tmp_non_cf = 0

          # Nominal CF histogram
          if h_name == "histo_DATA" and cut_dir in keys_list:
            if opt.debug == True and ("Up" in h_name or "Down" in h_name or "Var" in h_name or "DY_OS" in h_name): continue # for debugging, not copying systematic-variation histograms
            print("    I found a DATA histogram: {}".format(dict_os_ss_cuts[cut_dir] + '/' + var_dir + '/' + h_name))
            h_tmp         = file_os.Get(dict_os_ss_cuts[cut_dir] + '/' + var_dir + '/' + h_name).Clone()
            h_tmp_cf_up   = file_os.Get(dict_os_ss_cuts[cut_dir] + '/' + var_dir + '/histo_DATA_CMS_whss_chargeFlipEff_' + opt.year + 'Up').Clone()
            h_tmp_cf_down = file_os.Get(dict_os_ss_cuts[cut_dir] + '/' + var_dir + '/histo_DATA_CMS_whss_chargeFlipEff_' + opt.year + 'Down').Clone()
            if opt.debug == True: print("    Current histo: {}".format(h_name))
          if opt.debug == True and var_dir != "mll": continue # for debugging, just consider one variable (mll)

          # Check for a match between the name of currently-inspected histogram and the list of non-cf backgrounds
          if any('histo_'+bkg == h_name for bkg in non_cf_bkg) and cut_dir in keys_list:
            if opt.debug == True and ("Up" in h_name or "Down" in h_name or "Var" in h_name or "DY_OS" in h_name): continue # for debugging, not copying systematic-variation histograms
            print("    I found a non-cf-bkg histogram: {}".format(dict_os_ss_cuts[cut_dir] + '/' + var_dir + '/' + h_name))
            h_tmp_non_cf = file_os.Get(dict_os_ss_cuts[cut_dir] + '/' + var_dir + '/' + h_name).Clone()
            if h_non_cf == 0:
              h_non_cf = h_tmp_non_cf.Clone()
            else:
              h_non_cf.Add(h_tmp_non_cf, 1)

        # Write ChargeFlip histogram in same-sign rootfile
        if h_tmp != 0:
          print("h_tmp is a histogram!")
          if h_non_cf != 0:
            print("h_non_cf is a histogram!")
            h_tmp.Add(h_non_cf,-1)

          print("h_tmp exists --> writing it to file")
          h_tmp.SetName("histo_ChargeFlip")
          h_tmp.SetTitle("histo_ChargeFlip")
          
          output_file.cd(cut_dir + '/' + var_dir)
          h_tmp.Write("histo_ChargeFlip")

        # Write ChargeFlipUp histogram in same-sign rootfile
        if h_tmp_cf_up != 0:
          print("h_tmp up is a histogram!")
          if h_non_cf != 0:
            print("h_non_cf is a histogram!")
            h_tmp_cf_up.Add(h_non_cf,-1)

          print("h_tmp up exists --> writing it to file")
          h_tmp_cf_up.SetName("histo_ChargeFlip_CMS_whss_chargeFlipEff_" + opt.year + "Up")
          h_tmp_cf_up.SetTitle("histo_ChargeFlip_CMS_whss_chargeFlipEff_" + opt.year + "Up")
          
          output_file.cd(cut_dir + '/' + var_dir)
          h_tmp_cf_up.Write("histo_ChargeFlip_CMS_whss_chargeFlipEff_" + opt.year + "Up")

        # Write ChargeFlipDown histogram in same-sign rootfile
        if h_tmp_cf_down != 0:
          print("h_tmp down is a histogram!")
          if h_non_cf != 0:
            print("h_non_cf is a histogram!")
            h_tmp_cf_down.Add(h_non_cf,-1)

          print("h_tmp_down exists --> writing it to file")
          h_tmp_cf_down.SetName("histo_ChargeFlip_CMS_whss_chargeFlipEff_" + opt.year + "Down")
          h_tmp_cf_down.SetTitle("histo_ChargeFlip_CMS_whss_chargeFlipEff_" + opt.year + "Down")
          
          output_file.cd(cut_dir + '/' + var_dir)
          h_tmp_cf_down.Write("histo_ChargeFlip_CMS_whss_chargeFlipEff_" + opt.year + "Down")

    # Finally, close output file
    output_file.Close()
