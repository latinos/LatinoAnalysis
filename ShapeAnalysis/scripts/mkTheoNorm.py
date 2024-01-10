#!/usr/bin/env python

import sys
argv = sys.argv
sys.argv = argv[:1]

import ROOT
from ROOT import TFile, TH1
import collections
import json
import sys
import re
import os

from collections import OrderedDict

import optparse

if __name__ == '__main__':

    sys.argv = argv

    usage = 'usage: %prog [options]'
    parser = optparse.OptionParser(usage)

    parser.add_option('--input_file',   dest='input_file',   help='input file with histograms',                default='DEFAULT')
    parser.add_option('--variable',     dest='variable',     help='variable to use for intergral measurement', default='DEFAULT')
    parser.add_option('--cut',          dest='cut',          help='cut to inspect',                            default='DEFAULT')
    parser.add_option('--nuisance',     dest='nuisance',     help='nuisance of interest',                      default='DEFAULT')
    parser.add_option('--nuis_name',    dest='nuis_name',    help='nuisance name to write in json file',       default='DEFAULT')
    parser.add_option('--era',          dest='era',          help='era to consider',                           default='DEFAULT')
    parser.add_option('--samples_file', dest='samples_file', help='file with samples names',                   default='DEFAULT')

    # Read default parsing options
    (opt, args) = parser.parse_args()

    sys.argv.append( '-b' )
    ROOT.gROOT.SetBatch()

    print("Input file    = {}".format(opt.input_file))
    print("Variable      = {}".format(opt.variable))
    print("Cut           = {}".format(opt.cut))
    print("Nuisance      = {}".format(opt.nuisance))
    print("Nuisance name = {}".format(opt.nuis_name))
    print("Era           = {}".format(opt.era))
    print("Samples file  = {}".format(opt.samples_file))

    # Exceptions
    if opt.input_file == 'DEFAULT' :
        raise ValueError("Please specify an input file")
    input_file = opt.input_file

    if opt.variable == 'DEFAULT' :
        raise ValueError("Please specify a variable")
    variable = opt.variable

    if opt.cut == 'DEFAULT' :
        raise ValueError("Please insert a valid cut name")
    cut = opt.cut

    if opt.nuisance == 'DEFAULT' :
        raise ValueError("Please specify a nuisance")
    nuisance = opt.nuisance

    if opt.nuis_name == 'DEFAULT' :
        raise ValueError("Please specify a nuisance name")
    nuis_name = opt.nuis_name

    if opt.era == 'DEFAULT' :
        raise ValueError("Please specify an era")
    era = opt.era

    if opt.samples_file == 'DEFAULT' :
        raise ValueError("Please specify a samples file")
    samples_file = opt.samples_file
    samples = OrderedDict()
    if os.path.exists(opt.samples_file) :
        handle = open(opt.samples_file,'r')
        exec(handle)
        handle.close()

    # Check for input file and open it
    if not os.path.isfile(input_file):
        print("Warning: {} does not exist.".format(filename))
        exit()

    f0 = ROOT.TFile(input_file)
    nfdict = collections.OrderedDict()

    nfdict[nuisance] = {}

    # Get nominal and variations integrals
    for sample in samples.keys():
        
        print("Sample = {}".format(sample))

        h_nom  = f0.Get("{}/{}/histo_{}".format(cut,variable,sample))
        h_up   = f0.Get("{}/{}/histo_{}_{}Up".format(cut,variable,sample,nuisance))
        h_down = f0.Get("{}/{}/histo_{}_{}Down".format(cut,variable,sample,nuisance))

        print("Nominal integral = {}".format(h_nom.Integral()))
        print("Up integral      = {}".format(h_up.Integral()))
        print("Down integral    = {}".format(h_down.Integral()))

        norm_up   = 1.0 if h_up.Integral() == 0   else h_nom.Integral()/h_up.Integral()
        norm_down = 1.0 if h_down.Integral() == 0 else h_nom.Integral()/h_down.Integral()
        
        nfdict[nuisance][sample] = ["{}*({}Up/{})".format(norm_up,nuis_name,nuis_name), "{}*({}Down/{})".format(norm_down,nuis_name,nuis_name)]

    # Save on json file
    with open("TheoNorm_{}_{}_{}.json".format(era,variable,nuisance),"w") as outfile:
        json.dump(nfdict, outfile, indent=4)
