#!/usr/bin/env python

import os, sys
argv = sys.argv
sys.argv = argv[:1]

import optparse
import LatinoAnalysis.Gardener.hwwtools as hwwtools
import math

#import ROOT
#from ROOT import gBenchmark, gStyle, gROOT, TStyle
from ROOT import TCanvas, TPad, TFile, TPaveText, TLegend
from ROOT import TH1D, TH1F, TF1, TGraphErrors, TMultiGraph

# functions used in everyday life ...
from LatinoAnalysis.Tools.commonTools import *


if __name__ == '__main__':

    sys.argv = argv

    usage = 'usage: %prog [options]'
    parser = optparse.OptionParser(usage)
    
    parser.add_option('--file_with_sf', dest='file_with_sf', help='input file with btag SFs aaplied',    default='DEFAULT')
    parser.add_option('--file_no_sf',   dest='file_no_sf',   help='input file with no btag SFs applied', default='DEFAULT')
    parser.add_option('--variable',     dest='variable',     help='variable to consider',                default='DEFAULT')

    # Read default parsing options
    (opt, args) = parser.parse_args()

    sys.argv.append( '-b' )
    ROOT.gROOT.SetBatch()

    # Printout the inputs
    print("File with scale factors    = {}".format(opt.file_with_sf))
    print("File without scale factors = {}".format(opt.file_no_sf))
    print("Variable                   = {}".format(opt.variable))

    # Exceptions
    if opt.file_with_sf == 'DEFAULT' :
        raise ValueError("Please insert input file with btag SFs applied")

    if opt.file_no_sf == 'DEFAULT' :
        raise ValueError("Please insert input file without btag SFs applied")

    if opt.variable == 'DEFAULT' :
        raise ValueError("Please insert the variable to consider")

    # Assign inputs to variables
    file_with_sf = opt.file_with_sf
    file_no_sf   = opt.file_no_sf
    variable     = opt.variable

    # Open output file
    output_file_name = "b_tag_norm.txt"
    output_file = open(output_file_name,"w")

    # Open input files
    input_file_with_sf = TFile.Open(file_with_sf)
    input_file_no_sf   = TFile.Open(file_no_sf)

    # Input files structure: hww2l2v_13TeV_samesign_1j/events/histo_WW
    #                        cut / variable / histogram

    # Loop on the cuts:
    for cut in input_file_with_sf.GetListOfKeys() :
        if cut.IsFolder() == False: continue
        cut_dir = cut.GetName() 
        
        print("Cut = {}\n".format(cut_dir))
        output_file.write("Cut = {}\n".format(cut_dir))

        input_file_with_sf.cd(cut_dir)
        input_file_no_sf.cd(cut_dir)

        # Loop on the variables
        for var in ROOT.gDirectory.GetListOfKeys() :
            var_dir = var.GetName() 

            if var_dir == variable: break

        else:
            raise ValueError("I cannot find the variable to inspect")

        print("I found the variable!")
        input_file_with_sf.cd(cut_dir + '/' + var_dir)
        input_file_no_sf.cd(cut_dir + '/' + var_dir)

        # Loop on the histograms
        for histo in ROOT.gDirectory.GetListOfKeys() :
            h_name = histo.GetName() 
            
            # Read the histograms and extract the integral
            h_with_sf = input_file_with_sf.Get(cut_dir + '/' + var_dir + '/' + h_name)
            h_no_sf   =   input_file_no_sf.Get(cut_dir + '/' + var_dir + '/' + h_name)

            h_ratio = h_no_sf.Clone()
            h_ratio.Divide(h_with_sf)
            h_ratio.SetTitle("Ratio (without SF)/(with SF)")

            os.system("mkdir -p ratio_plots")
            os.system("cp /afs/cern.ch/user/n/ntrevisa/public/utils/index.php ratio_plots/")

            c1 = ROOT.TCanvas("c1","c1",600,600)
            c1.cd()
            h_ratio.Draw()
            c1_name = "ratio_plots/ratio_{}_{}_{}.png".format(cut_dir,h_name,var_dir)
            c1.Print(c1_name)

            integral_with_sf = h_with_sf.Integral()
            integral_no_sf   = h_no_sf.Integral()

            if integral_with_sf == 0:
                integral_with_sf = 1
            
            output_string = 'scale_{} = {}/{} = {}\n'.format(h_name,str(integral_no_sf),str(integral_with_sf),str(integral_no_sf/integral_with_sf))

            print(output_string)
            output_file.write(output_string)
            
