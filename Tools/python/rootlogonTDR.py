import sys, os, math, argparse
from ROOT import gROOT, gStyle, TStyle, TColor
from array import array
tdrStyle = TStyle("tdrStyle","Style for P-TDR")

kWhite = 0

tdrStyle.SetCanvasBorderMode(0)
tdrStyle.SetCanvasColor(kWhite)
tdrStyle.SetCanvasDefH(600) 
tdrStyle.SetCanvasDefW(600) 
tdrStyle.SetCanvasDefX(0)   
tdrStyle.SetCanvasDefY(0)

tdrStyle.SetPadBorderMode(0)
tdrStyle.SetPadColor(kWhite)
tdrStyle.SetPadGridX(False)
tdrStyle.SetPadGridY(False)
tdrStyle.SetGridColor(0)
tdrStyle.SetGridStyle(3)
tdrStyle.SetGridWidth(1)

tdrStyle.SetFrameBorderMode(0)
tdrStyle.SetFrameBorderSize(1)
tdrStyle.SetFrameFillColor(0)
tdrStyle.SetFrameFillStyle(0)
tdrStyle.SetFrameLineColor(1)
tdrStyle.SetFrameLineStyle(1)
tdrStyle.SetFrameLineWidth(1)

tdrStyle.SetHistFillColor(63)
tdrStyle.SetHistLineColor(1)
tdrStyle.SetHistLineStyle(0)
tdrStyle.SetHistLineWidth(1)


tdrStyle.SetErrorX(0.)

tdrStyle.SetMarkerStyle(20)

tdrStyle.SetOptFit(1)
tdrStyle.SetFitFormat("5.4g")
tdrStyle.SetFuncColor(2)
tdrStyle.SetFuncStyle(1)
tdrStyle.SetFuncWidth(1)

tdrStyle.SetOptDate(0)

tdrStyle.SetOptFile(0)
#tdrStyle.SetOptStat(0111) 
tdrStyle.SetOptStat(0) 
tdrStyle.SetStatColor(kWhite)
tdrStyle.SetStatFont(42)
tdrStyle.SetStatFontSize(0.025)
tdrStyle.SetStatTextColor(1)
tdrStyle.SetStatFormat("6.4g")
tdrStyle.SetStatBorderSize(1)
tdrStyle.SetStatH(0.1)
tdrStyle.SetStatW(0.15)

tdrStyle.SetPadTopMargin(0.05)
tdrStyle.SetPadBottomMargin(0.13)
tdrStyle.SetPadLeftMargin(0.13)
tdrStyle.SetPadRightMargin(0.05)


tdrStyle.SetTitleFont(42)
tdrStyle.SetTitleColor(1)
tdrStyle.SetTitleTextColor(1)
tdrStyle.SetTitleFillColor(10)
tdrStyle.SetTitleFontSize(0.05)

tdrStyle.SetTitleColor(1, "XYZ")
tdrStyle.SetTitleFont(42, "XYZ")
tdrStyle.SetTitleSize(0.06, "XYZ")
tdrStyle.SetTitleXOffset(0.9)
tdrStyle.SetTitleYOffset(1.05)

tdrStyle.SetLabelColor(1, "XYZ")
tdrStyle.SetLabelFont(42, "XYZ")
tdrStyle.SetLabelOffset(0.007, "XYZ")
tdrStyle.SetLabelSize(0.05, "XYZ")

tdrStyle.SetAxisColor(1, "XYZ")
tdrStyle.SetStripDecimals(1)
tdrStyle.SetTickLength(0.03, "XYZ")
tdrStyle.SetNdivisions(510, "XYZ")
tdrStyle.SetPadTickX(1)
tdrStyle.SetPadTickY(1)

tdrStyle.SetOptLogx(0)
tdrStyle.SetOptLogy(0)
tdrStyle.SetOptLogz(0)
tdrStyle.cd()

palette=''
def set_palette(name=palette, ncontours=999):
    """Set a color palette from a given RGB list
    stops, red, green and blue should all be lists of the same length
    see set_decent_colors for an example"""

    if name == "gray" or name == "grayscale":
        stops = [0.00, 0.34, 0.61, 0.84, 1.00]
        red   = [1.00, 0.84, 0.61, 0.34, 0.00]
        green = [1.00, 0.84, 0.61, 0.34, 0.00]
        blue  = [1.00, 0.84, 0.61, 0.34, 0.00]
    # elif name == "whatever":
        # (define more palettes)
    else:
        # default palette, looks cool
        stops = [0.00, 0.34, 0.61, 0.84, 1.00]
        red   = [0.00, 0.00, 0.87, 1.00, 0.51]
        green = [0.00, 0.81, 1.00, 0.20, 0.00]
        blue  = [0.51, 1.00, 0.12, 0.00, 0.00]

    s = array('d', stops)
    r = array('d', red)
    g = array('d', green)
    b = array('d', blue)

    npoints = len(s)
    TColor.CreateGradientColorTable(npoints, s, r, g, b, ncontours)
    gStyle.SetNumberContours(ncontours)



