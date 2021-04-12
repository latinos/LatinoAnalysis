#!/usr/bin/env python

# This script aims to find an effective correction to enhance the Drell-Yan (DY) MC
# description of the process.
# In particular, we assume that subtracting from Data all processes except Drell-Yan, we would
# get the real Drell-Yan contribution. Dividing this histogram by the DY MC histogram and fitting
# the result with a chosen function, we get the correction.

import sys, os
argv = sys.argv
sys.argv = argv[:1]

import re

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
parser.add_option('--fit_func',   dest='fit_func',   help='fit function (use polX)',     default='pol1') 

(opt, args) = parser.parse_args()

sys.argv.append('-b')
ROOT.gROOT.SetBatch()

print("List of inputs:")
print("Input rootfile:   {0}".format(opt.input_file))
print("Cut:              {0}".format(opt.cut))
print("Variable:         {0}".format(opt.variable))
print("Output directory: {0}".format(opt.output_dir))
print("Fit function:     {0}".format(opt.fit_func))

# Assigning inputs to variables
input_file = opt.input_file 
cut        = opt.cut
variable   = opt.variable
output_dir = opt.output_dir 
fit_func   = opt.fit_func

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

                # Fit
                h_Ratio.Fit(fit_func, "", "", x_min, x_max)

                # Fit result
                fit_result = h_Ratio.FindObject(fit_func)
                
                # Fitting parameters
                fit_parameters = []
                fit_par_errors = []

                # Get polX grade
                grade = map(int, re.findall('\d+', fit_func))
                print(grade[0])

                # Get all fit parameters
                grade_loop = 0
                while grade_loop < grade[0]+1:
                    fit_parameters.append(fit_result.GetParameter(grade_loop))
                    fit_par_errors.append(fit_result.GetParError(grade_loop))
                    print("Par {0}: {1:.3f} +/- {2:.3f}".format(grade_loop, fit_parameters[grade_loop], fit_par_errors[grade_loop]))
                    grade_loop += 1
                print(fit_parameters)
                print(fit_par_errors)

                # Plot Ratio histogram with Fit
                c1 = TCanvas("c1", "c1", 600, 600)
                c1.cd()
                h_Ratio.GetYaxis().SetRangeUser(-1, 4)
                h_Ratio.Draw()

                # Put results in legend
                leg = TLegend(0.20, 0.65, 0.80, 0.88)
                leg.SetFillColor(0)
                leg.SetTextFont(42)
                leg.SetTextSize(0.035)
                leg.SetLineColor(0)
                leg.SetShadowColor(0)
                #leg_string = []
                #leg_string.append("Fit with a {}".format(fit_func))
                leg_string = "Fit with a {}".format(fit_func)
                # for i in range(0, grade[0]+1):
                #     leg_string.append("{0:.3f} x^{1}".format(fit_parameters[i],i))

                print(leg_string)
                # s = ""
                # for string in leg_string:
                #     s += string
                # leg.AddEntry(fit_result, s,'lf')
                leg.AddEntry(fit_result, leg_string, 'lf')
                leg.Draw()

                # Save plot
                output_name = output_dir + "/Fit_" + cut + "_" + variable
                c1.Print(output_name + ".png")

                # Print weight to put in samples.py
                phrase = []
                phrase.append("({}".format(fit_parameters[0]))
                for i in range(1, grade[0]+1):
                    if fit_parameters[i] > 0:
                        phrase.append(" + {}".format(fit_parameters[i]))
                    else:
                        phrase.append(" {}".format(fit_parameters[i]))
                    for j in range(0, i):
                        phrase.append(" * {}".format(variable))
                phrase.append(") *")
                if cut.split('_')[0] == "0j": 
                    phrase.append(" (zeroJet)")
                elif cut.split('_')[0] == "1j": 
                    phrase.append(" (oneJet)")
                elif cut.split('_')[0] == "2j": 
                    phrase.append(" (2jggH)")
                elif cut.split('_')[0] == "VBF": 
                    phrase.append(" (2jVBF)")
                elif cut.split('_')[0] == "VH": 
                    phrase.append(" (2jVH)")
                else: 
                    print("I don't know this cut")

                if "ee" in cut:
                    phrase.append(" * (Lepton_pdgId[0]*Lepton_pdgId[1] == -11*11)")
                elif "mm" in cut:
                    phrase.append(" * (Lepton_pdgId[0]*Lepton_pdgId[1] == -13*13)")
                else: 
                    print("I don't know this cut")

                #print(phrase)

                # Copy this in samples.py as an additional weight
                message = ''.join(str(e) for e in phrase)
                print(message)

                # Output in a txt file
                os.system("echo '{}' > {}.txt".format(message, output_name))
