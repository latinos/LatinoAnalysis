#!/usr/bin/env python

# This script aims to find an effective correction to enhance the Drell-Yan (DY) MC
# description of the process.
# In particular, we assume that subtracting from Data all processes except Drell-Yan, we would
# get the real Drell-Yan contribution. Dividing this histogram by the DY MC histogram and fitting
# the result with a chosen function, we get the correction.

import sys, os
argv = sys.argv
sys.argv = argv[:1]

import ROOT

from ROOT import TFile, TH1D, TCanvas, TLegend, gStyle

# input_file = "rootFile/plots_ggH_SF_2016_v7_DY_CR.root"
# cut = "0j_ee_in"
# variable = "mth"

# Introducing parser
import optparse

sys.argv = argv

usage = 'usage: %prog [options]'
parser = optparse.OptionParser(usage)

parser.add_option('--input_file', dest='input_file', help='histograms file',             default='rootFile/plots_ggH_SF_2016_v7_DY_CR.root') 
parser.add_option('--cut',        dest='cut',        help='cut to inspect',              default='0j_ee_in') 
parser.add_option('--variable',   dest='variable',   help='variable to use for the fit', default='mth') 
parser.add_option('--output_dir', dest='output_dir', help='output directory',            default='Fit_results') 

(opt, args) = parser.parse_args()

sys.argv.append('-b')
ROOT.gROOT.SetBatch()

print("List of inputs:")
print("Input rootfile:   {0}".format(opt.input_file))
print("Cut:              {0}".format(opt.cut))
print("Variable:         {0}".format(opt.variable))
print("Output directory: {0}".format(opt.output_dir))

# Assigning inputs to variables
input_file = opt.input_file 
cut        = opt.cut
variable   = opt.variable
output_dir = opt.output_dir 

mkdir_command = "mkdir -p {0}".format(output_dir)
os.system(mkdir_command)

gStyle.SetOptFit(0)
gStyle.SetOptStat(0)

# Here starts the actual script
my_file = TFile(input_file)

# Get all directories in file
folders_list = my_file.GetListOfKeys()

for folder in folders_list:
    if folder.GetName() == cut:
        print("Cut: {}".format(folder.GetName()))
        current_folder = folder.ReadObj()
        for var in current_folder.GetListOfKeys():
            if var.GetName() == variable:
                current_var = var.ReadObj()
                print("Variable: {}".format(var.GetName()))

                # Get Data histogram
                h_Data = my_file.Get(cut + "/" + variable + "/histo_DATA")
                print("Data integral: {}".format(h_Data.Integral()))
                for process in current_var.GetListOfKeys():
                    if not "histo_DY" in process.GetName() and not "histo_DATA" in process.GetName():
                        # Subtract from Data non-DY MC
                        print(process.GetName())
                        h_tmp = my_file.Get(cut + "/" + variable + "/" + process.GetName())
                        h_Data.Add(h_tmp, -1)
                print("Data integral after MC subtraction: {}".format(h_Data.Integral()))

                # Get DY MC histogram
                h_DY = my_file.Get(cut + "/" + variable + "/histo_DY")
                print("DY MC integral: {}".format(h_DY.Integral()))
                
                # Prepare Data/MC histogram ratio
                h_Ratio = TH1D.Clone(h_Data)
                h_Ratio.Divide(h_DY)
                print("Ratio integral: {}".format(h_Ratio.Integral()))
                h_Ratio.Draw()
                
                # Define Fit range
                x_min = h_Ratio.GetXaxis().GetXmin()
                x_max = h_Ratio.GetXaxis().GetXmax()

                # Fit (for the moment just with a pol1)
                h_Ratio.Fit("pol1", "", "", x_min, x_max)

                # Fit result = a + bx
                fit_result = h_Ratio.FindObject("pol1")
                a = fit_result.GetParameter(0)
                a_err = fit_result.GetParError(0)
                print("a = {} +- {}".format(a, a_err))
                b = fit_result.GetParameter(1)
                b_err = fit_result.GetParError(1)
                print("b = {} +- {}".format(b, b_err))

                # Plot Ratio histogram with Fit
                c1 = TCanvas("c1", "c1", 600, 600)
                c1.cd()
                h_Ratio.Draw()

                # Put results in legend
                leg = TLegend(0.20, 0.65, 0.80, 0.88)
                leg.SetFillColor(0)
                leg.SetTextFont(42)
                leg.SetTextSize(0.035)
                leg.SetLineColor(0)
                leg.SetShadowColor(0)
                leg.AddEntry(fit_result, "Fit parameters: {0:.3f} + {1:.3f} x".format(a,b),'lf')
                leg.Draw()

                # Save plot
                output_name = output_dir + "/Fit_" + cut + "_" + variable + ".png"
                c1.Print(output_name)

