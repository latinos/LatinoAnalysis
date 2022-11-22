#!/usr/bin/env python

import os, sys

import optparse
import LatinoAnalysis.Gardener.hwwtools as hwwtools
import math
import numpy as np

from ROOT import TCanvas, TPad, TFile, TPaveText, TLegend
from ROOT import TH1D, TH1F, TF1, TGraphErrors, TMultiGraph

# Common tools in HWW framework
from LatinoAnalysis.Tools.commonTools import *


# Supporting functions
def check_main_bkg(binning_dictionary):
    '''Checks if there are main bkg with less than 10 MC events'''

    n_main_bkg_to_fix = 0
    for key, value in binning_dictionary.items():
        if binning_dictionary[key]["isMainBackground"] == 1:
            n_main_bkg_to_fix += 1

    return n_main_bkg_to_fix


def do_significance(binning_dictionary, h_dict, last_bin, f_o_m):
    '''Returns the bin giving the larger significance.

    binning_dictionary: the dictionary with the list of processes, saying if they are
        signal, background, or main background
    h_dict: dictionary of histograms to inspect
    last_bin: the last bin to use for the significance calculation
    f_o_m: the figure of merit to use
    '''

    # Initialize main backgrounds
    for key, value in binning_dictionary.items():
        if binning_dictionary[key]["isMainBackground"] == 2:
            binning_dictionary[key]["isMainBackground"] = 1

    print("--------------------------------------")
    print("Inputs: last_bin = {}".format(last_bin))
    if last_bin < 1:
        return 0, 0

    # Get all signals and background yields
    max_significance = 0.0
    max_bin = 0
    max_sig_in_bin = 0
    max_bkg_in_bin = 0
    for i in range(0, last_bin - 2):
        # print("Iteration {}: integral from bin {} to bin {}".format(i, i, last_bin + 1))
        S = 0
        B = 0
        significance = 0.0
        for key, value in binning_dictionary.items():
            integral = h_dict[key].Integral(i, last_bin + 1)
            # print("Integral for process {}: {}".format(key,integral))
            if binning_dictionary[key]["isSignal"] == 1:
                S = S + integral
            else:
                B = B + integral

        # Calculate the significance
        if (B != 0):
            if f_o_m == "S_B":
                significance = S / B
            elif f_o_m == "S_sqrtB":
                significance = S / np.sqrt(B)
            elif f_o_m == "S_sqrtSB":
                significance = S / np.sqrt(S+B)
            else:
                raise ValueError("I don't know this figure of merit")
        else:
            significance = 0.0

        # print("Signal = {}, Background = {}, Significance = {}, max_significance = {}".format(S, B, significance, max_significance))

        # Compare with previous value
        if significance > max_significance:
            max_significance = significance
            max_bin = i
            max_sig_in_bin = S
            max_bkg_in_bin = B

        # print("max_bin:", max_bin)

    # Check if the main backgrounds have at least 10 MC events in the selected range
    # It is not possible to get the number of MC events in a bin of a histogram
    # We try to approximate it like this:
    # - bin_error              = sqrt(MC_events)
    # - obs_events             = MC_events * weight
    # - obs_error              = bin_error * weight = sqrt(MC_events) * weight
    # - obs_error / obs_events = weight * sqrt(MC_events) / (weight * MC_events)
    #   --> MC_events = obs_events^2 / obs_error^2
    #
    # Second attemp: overall event weight is h.Integral()/h.GetEntries() 
    while (check_main_bkg(binning_dictionary)) > 0:
        print("Main bkg to fix: {}".format(check_main_bkg(binning_dictionary)))
        for key, value in binning_dictionary.items():
            MC_events = 0
            if binning_dictionary[key]["isMainBackground"] == 1:
                for i in range(max_bin, last_bin + 1):
                    # First definition of number of MC events
                    if h_dict[key].GetBinContent(i) > 0:
                        MC_events += h_dict[key].GetBinContent(i)*h_dict[key].GetBinContent(i) / (h_dict[key].GetBinError(i)*h_dict[key].GetBinError(i))
                        # print("Process {}: MC events = {}".format(key, MC_events))
                    # Second definition of number of MC events
                    # weight = h_dict[key].Integral() / h_dict[key].GetEntries() 
                    # MC_events += h_dict[key].GetBinContent(i) / weight
                    if MC_events >= 10:
                        binning_dictionary[key]["isMainBackground"] = 2
                    else: 
                        max_bin = max_bin - 1
                    if max_bin < 10:
                        binning_dictionary[key]["isMainBackground"] = 2


    print("Max_bin after main bkg correction:", max_bin)
    print("Signal yield:                     ", max_sig_in_bin)
    print("Background yield:                 ", max_bkg_in_bin)
    print("Corresponding significance:       ", max_significance)

    return max_bin, max_significance


# Main function
if __name__ == '__main__':

    usage = 'usage: %prog [options]'
    parser = optparse.OptionParser(usage)
    
    parser.add_option('--pyCfg',     dest='pyCfg',     help='definition of signal, backgrounds, and main backgrounds', default='DEFAULT')
    parser.add_option('--inputFile', dest='inputFile', help='input rootfile with histograms',                          default='DEFAULT')
    parser.add_option('--cut',       dest='cut',       help='cut to inspect',                                          default='DEFAULT')
    parser.add_option('--variable',  dest='variable',  help='variable to inspect',                                     default='DEFAULT')
    parser.add_option('--figure',    dest='figure',    help='choose figure of merit: S_B, S_sqrtB, S_sqrtSB',          default='S_B')

 
    # read default parsing options as well
    hwwtools.addOptions(parser)
    hwwtools.loadOptDefaults(parser)
    (opt, args) = parser.parse_args()

    print " configuration file = ", opt.pyCfg
    print " input  = ",             opt.inputFile
    print " cut  = ",               opt.cut
    print " variable  = ",          opt.variable
    print " figure of merit  = ",   opt.figure


    # Value Errors in case input parameters are missing
    if opt.pyCfg == 'DEFAULT' :
        raise ValueError("Please specify configuration file")
    pyCfg = opt.pyCfg

    if opt.inputFile == 'DEFAULT' :
        raise ValueError("Please specify input rootfile")
    input_file = opt.inputFile

    if opt.cut == 'DEFAULT' :
        raise ValueError("Please specify the cut to inspect")
    cut = opt.cut

    if opt.variable == 'DEFAULT' :
        raise ValueError("Please specify the variable to inspect")
    variable = opt.variable

    figure = opt.figure


    # Create Needed dictionary
    binning = collections.OrderedDict()
    if os.path.exists(opt.pyCfg) :
      handle = open(opt.pyCfg,'r')
      exec(handle)
      handle.close()
      
    # Just printing the dictionary for testing
    # print(binning)

    
    # Open input rootfile: f
    f = TFile(input_file)

    # Prepare subfolder in the rootfile
    folder = cut + "/" + variable + "/histo_"

    # Get the histograms
    histograms = {}
    n_bins = 0
    for key, value in binning.items():
        # print("Reading histogram: {}".format(folder + key))
        histograms[key] = f.Get(folder + key)
        # print(histograms[key].Integral())
    # At the end of the loop, get the number of bins in the histograms and the bin width
    else:
        n_bins         = histograms[key].GetNbinsX()
        bin_width      = histograms[key].GetBinWidth(1)
        first_bin_edge = histograms[key].GetBinLowEdge(1)
        print("The histograms have {} bins, with width {}. The x-axis starts at {}".format(n_bins, bin_width, first_bin_edge))
        

    # Calculate figures of merit
    max_bin = n_bins + 1
    my_bins = []
    my_significances = []
    stop = 0
    my_bins.append(max_bin)
    # my_significances.append(0.0)
    print("Max bin = ", max_bin)
    while (stop == 0):
        new_max_bin, new_max_significance = do_significance(binning, histograms, max_bin, figure)
        print(new_max_bin)
        if new_max_bin == max_bin or max_bin <= 1:
            my_bins.append(0)
            stop = 1
            break
        max_bin = new_max_bin
        if new_max_bin < 0: continue
        my_bins.append(new_max_bin)
        my_significances.append(new_max_significance)

    print(my_bins)

    # Translate bin number into bin edges
    bin_edges = []
    for my_bin in my_bins:
        bin_edges.append(first_bin_edge + bin_width*my_bin)
    for b in bin_edges:
        print(round(b,2))

    # 'range' : ([60.,120.,130.,140.,150.,160.,170.,180.,190.,200.,250.,300.],),
    output_string = "'range': ([" # + reversed(bin_edges) + ",),"
    for i in reversed(bin_edges):
        output_string += str(i) + ","
    output_string += "],),"
    print(output_string)

    output_significance = "'sign.': (["
    for i in reversed(my_significances):
        output_significance += str(round(i,4)) + ","
    output_significance += "],),"
    print(output_significance)

    output_file_name = "Binning_" + cut.replace("hww2l2v_13TeV_WH_SS_","") + "_" + figure + ".txt"
    with open(output_file_name, "w") as f:
        f.write("variables['BDTG6_" + cut.replace("hww2l2v_13TeV_WH_SS_","") + "_" + figure+ "'] = {\n") # currently, variable is hard-coded
        f.write("    'name'  : 'BDT_SS_v7',\n")        
        f.write("    " + output_string)
        f.write("\n")
        f.write("    'xaxis' : 'BDT discriminant',\n")
        f.write("    'fold'  : 3\n")
        f.write("}\n")
        f.write("# " + output_significance)
        f.write("\n")
    f.close()    

    # print(my_significances)

