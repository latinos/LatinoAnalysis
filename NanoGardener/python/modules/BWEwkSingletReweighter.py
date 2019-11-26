import ROOT
ROOT.PyConfig.IgnoreCommandLineOptions = True
import re
import os
import math
import numpy
import pickle
#import psutil
from scipy.interpolate import interp1d

from PhysicsTools.NanoAODTools.postprocessing.framework.datamodel import Collection 
from PhysicsTools.NanoAODTools.postprocessing.framework.eventloop import Module

# Needs variables from "HiggsGenVars" module to work
class BWEwkSingletReweighter(Module):
    def __init__(self, year="2017", cprime= [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0], brnew=[0.0, 0.5], relw=[0.00, 0.05, 0.10, 0.15, 0.20, 0.25, 0.30], mssm=True, decayWeightsFile="decayWeights.pkl"):

        self.cmssw_base = os.getenv('CMSSW_BASE')

        self.year = str(year)

        self.cprime_list = cprime
        self.brnew_list = brnew
        self.relw_list = relw
        self.mssm = mssm

        self.undoCPS = True
        self.isNewJHU = True
        self.decayWeightsFile = decayWeightsFile

        # Non-CPS values from https://twiki.cern.ch/twiki/bin/view/LHCPhysics/CERNYellowReportPageBR2014 for up to 1000 GeV
        Hmass = [80.0, 81.0, 82.0, 83.0, 84.0, 85.0, 86.0, 87.0, 88.0, 89.0,
                 90.0, 91.0, 92.0, 93.0, 94.0, 95.0, 96.0, 97.0, 98.0, 99.0,
                 100.0, 101.0, 102.0, 103.0, 104.0, 105.0, 106.0, 107.0, 108.0, 109.0,
                 110.0, 110.5, 111.0, 111.5, 112.0, 112.5, 113.0, 113.5, 114.0, 114.5,
                 115.0, 115.5, 116.0, 116.5, 117.0, 117.5, 118.0, 118.5, 119.0, 119.5,

                 120.0, 120.1, 120.2, 120.3, 120.4, 120.5, 120.6, 120.7, 120.8, 120.9,
                 121.0, 121.1, 121.2, 121.3, 121.4, 121.5, 121.6, 121.7, 121.8, 121.9,
                 122.0, 122.1, 122.2, 122.3, 122.4, 122.5, 122.6, 122.7, 122.8, 122.9,
                 123.0, 123.1, 123.2, 123.3, 123.4, 123.5, 123.6, 123.7, 123.8, 123.9,
                 124.0, 124.1, 124.2, 124.3, 124.4, 124.5, 124.6, 124.7, 124.8, 124.9,

                 125.0, 125.1, 125.2, 125.3, 125.4, 125.5, 125.6, 125.7, 125.8, 125.9,
                 126.0, 126.1, 126.2, 126.3, 126.4, 126.5, 126.6, 126.7, 126.8, 126.9,
                 127.0, 127.1, 127.2, 127.3, 127.4, 127.5, 127.6, 127.7, 127.8, 127.9,
                 128.0, 128.1, 128.2, 128.3, 128.4, 128.5, 128.6, 128.7, 128.8, 128.9,
                 129.0, 129.1, 129.2, 129.3, 129.4, 129.5, 129.6, 129.7, 129.8, 129.9,

                 130.0, 130.5, 131.0, 131.5, 132.0, 132.5, 133.0, 133.5, 134.0, 134.5,
                 135.0, 135.5, 136.0, 136.5, 137.0, 137.5, 138.0, 138.5, 139.0, 139.5,
                 140.0, 140.5, 141.0, 141.5, 142.0, 142.5, 143.0, 143.5, 144.0, 144.5,
                 145.0, 145.5, 146.0, 146.5, 147.0, 147.5, 148.0, 148.5, 149.0, 149.5,
                 150.0, 152.0, 154.0, 156.0, 158.0, 160.0, 162.0, 164.0, 165.0, 166.0,

                 168.0, 170.0, 172.0, 174.0, 175.0, 176.0, 178.0, 180.0, 182.0, 184.0,
                 185.0, 186.0, 188.0, 190.0, 192.0, 194.0, 195.0, 196.0, 198.0, 200.0,
                 202.0, 204.0, 206.0, 208.0, 210.0, 212.0, 214.0, 216.0, 218.0, 220.0,
                 222.0, 224.0, 226.0, 228.0, 230.0, 232.0, 234.0, 236.0, 238.0, 240.0,
                 242.0, 244.0, 246.0, 248.0, 250.0, 252.0, 254.0, 256.0, 258.0, 260.0,

                 262.0, 264.0, 266.0, 268.0, 270.0, 272.0, 274.0, 276.0, 278.0, 280.0,
                 282.0, 284.0, 286.0, 288.0, 290.0, 292.0, 294.0, 296.0, 298.0, 300.0,
                 305.0, 310.0, 315.0, 320.0, 325.0, 330.0, 335.0, 340.0, 345.0, 350.0,
                 360.0, 370.0, 380.0, 390.0, 400.0, 420.0, 440.0, 450.0, 460.0, 480.0,
                 500.0, 520.0, 540.0, 550.0, 560.0, 580.0, 600.0, 620.0, 640.0, 650.0,

                 660.0, 680.0, 700.0, 720.0, 740.0, 750.0, 760.0, 780.0, 800.0, 820.0,
                 840.0, 850.0, 860.0, 880.0, 900.0, 920.0, 940.0, 950.0, 960.0, 980.0,
                 1000.0, 1050.0, 1100.0, 1150.0, 1200.0, 1250.0, 1300.0, 1350.0, 1400.0, 1450.0,
                 1500.0, 1550.0, 1600.0, 1650.0, 1700.0, 1750.0, 1800.0, 1850.0, 1900.0, 1950.0,
                 2000.0, 2050.0, 2100.0, 2150.0, 2200.0, 2250.0, 2300.0, 2350.0, 2400.0, 2450.0,

                 2500.0, 2550.0, 2600.0, 2650.0, 2700.0, 2750.0, 2800.0, 2850.0, 2900.0, 2950.0,
                 3000.0, 3050.0, 3100.0, 3150.0, 3200.0, 3250.0, 3300.0, 3350.0, 3400.0, 3450.0,
                 3500.0, 3550.0, 3600.0, 3650.0, 3700.0, 3750.0, 3800.0, 3850.0, 3900.0, 3950.0,
                 4000.0, 4050.0, 4100.0, 4150.0, 4200.0, 4250.0, 4300.0, 4350.0, 4400.0, 4450.0,
                 4500.0, 4550.0, 4600.0, 4650.0, 4700.0, 4750.0, 4800.0, 4850.0, 4900.0, 4950.0, 5000.0]

        Hwidth = [0.00199, 0.00201, 0.00204, 0.00206, 0.00208, 0.00211, 0.00213, 0.00215, 0.00218, 0.0022,
                  0.00222, 0.00225, 0.00227, 0.0023, 0.00232, 0.00235, 0.00237, 0.0024, 0.00243, 0.00246,
                  0.00248, 0.00251, 0.00254, 0.00258, 0.00261, 0.00264, 0.00268, 0.00272, 0.00276, 0.0028,
                  0.00285, 0.00287, 0.00289, 0.00292, 0.00295, 0.00297, 0.003, 0.00303, 0.00306, 0.00309,
                  0.00312, 0.00315, 0.00319, 0.00322, 0.00326, 0.0033, 0.00333, 0.00338, 0.00342, 0.00346,

                  0.00351, 0.00352, 0.00352, 0.00353, 0.00354, 0.00355, 0.00356, 0.00357, 0.00358, 0.00359,
                  0.0036, 0.00361, 0.00362, 0.00363, 0.00364, 0.00365, 0.00366, 0.00367, 0.00368, 0.00369,
                  0.00371, 0.00372, 0.00373, 0.00374, 0.00375, 0.00376, 0.00377, 0.00378, 0.00379, 0.00381,
                  0.00382, 0.00383, 0.00384, 0.00385, 0.00386, 0.00388, 0.00389, 0.0039, 0.00391, 0.00393,
                  0.00394, 0.00395, 0.00396, 0.00398, 0.00399, 0.004, 0.00402, 0.00403, 0.00404, 0.00406,

                  0.00407, 0.00408, 0.0041, 0.00411, 0.00412, 0.00414, 0.00415, 0.00417, 0.00418, 0.0042,
                  0.00421, 0.00423, 0.00424, 0.00426, 0.00427, 0.00429, 0.0043, 0.00432, 0.00433, 0.00435,
                  0.00436, 0.00438, 0.0044, 0.00441, 0.00443, 0.00445, 0.00446, 0.00448, 0.0045, 0.00451,
                  0.00453, 0.00455, 0.00457, 0.00458, 0.0046, 0.00462, 0.00464, 0.00465, 0.00467, 0.00469,
                  0.00471, 0.00473, 0.00475, 0.00477, 0.00479, 0.00481, 0.00483, 0.00485, 0.00487, 0.00489,

                  0.00491, 0.00501, 0.00512, 0.00523, 0.00535, 0.00548, 0.0056, 0.00574, 0.00588, 0.00603,
                  0.00618, 0.00634, 0.00651, 0.00669, 0.00687, 0.00706, 0.00726, 0.00747, 0.0077, 0.00793,
                  0.00817, 0.00843, 0.0087, 0.00898, 0.00928, 0.00959, 0.00992, 0.0103, 0.0106, 0.011,
                  0.0114, 0.0119, 0.0123, 0.0128, 0.0133, 0.0139, 0.0145, 0.0151, 0.0158, 0.0165,
                  0.0173, 0.0211, 0.0266, 0.0351, 0.0502, 0.0831, 0.147, 0.215, 0.246, 0.276,

                  0.33, 0.38, 0.429, 0.477, 0.501, 0.525, 0.575, 0.631, 0.7, 0.788,
                  0.832, 0.876, 0.96, 1.04, 1.12, 1.2, 1.24, 1.28, 1.35, 1.43,
                  1.51, 1.59, 1.68, 1.76, 1.85, 1.93, 2.02, 2.12, 2.21, 2.31,
                  2.40, 2.50, 2.61, 2.71, 2.82, 2.93, 3.04, 3.16, 3.27, 3.40,
                  3.52, 3.64, 3.77, 3.91, 4.04, 4.18, 4.32, 4.46, 4.61, 4.76,

                  4.91, 5.07, 5.23, 5.39, 5.55, 5.72, 5.89, 6.07, 6.25, 6.43,
                  6.61, 6.80, 6.99, 7.19, 7.39, 7.59, 7.79, 8.00, 8.22, 8.43,
                  8.99, 9.57, 10.20, 10.80, 11.40, 12.10, 12.80, 13.50, 14.20, 15.20,
                  17.60, 20.20, 23.10, 26.10, 29.20, 35.90, 43.00, 46.80, 50.80, 59.10,
                  68.00, 77.50, 87.70, 93.00, 98.60, 110.00, 123.00, 136.00, 150.00, 158.00,

                  165.00, 182.00, 199.00, 217.00, 237.00, 247.00, 258.00, 280.00, 304.00, 330.00,
                  357.00, 371.00, 386.00, 416.00, 449.00, 484.00, 521.00, 540.00, 560.00, 602.00,
                  647.00, 525, 550, 575, 600, 625, 650, 675, 700, 725,
                  750, 775, 800, 825, 850, 875, 900, 925, 950, 975,
                  1000, 1025, 1050, 1075, 1100, 1125, 1150, 1175, 1200, 1225,

                  1250, 1275, 1300, 1325, 1350, 1375, 1400, 1425, 1450, 1475,
                  1500, 1525, 1550, 1575, 1600, 1625, 1650, 1675, 1700, 1725,
                  1750, 1775, 1800, 1825, 1850, 1875, 1900, 1925, 1950, 1975,
                  2000, 2025, 2050, 2075, 2100, 2125, 2150, 2175, 2200, 2225,
                  2250, 2275, 2300, 2325, 2350, 2375, 2400, 2425, 2450, 2475, 2500]

        # CPS values from https://github.com/latinos/LatinoAnalysis/blob/master/Gardener/python/variables/pwhg_cpHTO_reweight.f
        HmassCPS = [80.0, 82.0, 84.0, 86.0, 88.0, 90.0, 92.0, 94.0, 96.0, 98.0,
                    100.0, 102.0, 104.0, 106.0, 108.0, 110.0, 112.0, 114.0, 116.0, 118.0,
                    120.0, 122.0, 124.0, 125.0, 126.0, 128.0, 130.0, 132.0, 134.0, 136.0,
                    138.0, 140.0, 142.0, 144.0, 146.0, 148.0, 150.0, 152.0, 154.0, 156.0,
                    158.0, 160.0, 162.0, 164.0, 166.0, 168.0, 170.0, 172.0, 174.0, 176.0,

                    178.0, 180.0, 182.0, 184.0, 186.0, 188.0, 190.0, 192.0, 194.0, 196.0,
                    198.0, 200.0, 202.0, 204.0, 206.0, 208.0, 210.0, 212.0, 214.0, 216.0,
                    218.0, 220.0, 222.0, 224.0, 226.0, 228.0, 230.0, 232.0, 234.0, 236.0,
                    238.0, 240.0, 242.0, 244.0, 246.0, 248.0, 250.0, 252.0, 254.0, 256.0,
                    258.0, 260.0, 262.0, 264.0, 266.0, 268.0, 270.0, 272.0, 274.0, 276.0,

                    278.0, 280.0, 282.0, 284.0, 286.0, 288.0, 290.0, 292.0, 294.0, 296.0,
                    298.0, 300.0, 305.0, 310.0, 315.0, 320.0, 325.0, 330.0, 335.0, 340.0,
                    345.0, 350.0, 360.0, 370.0, 380.0, 390.0, 400.0, 420.0, 440.0, 450.0,
                    460.0, 480.0, 500.0, 520.0, 540.0, 550.0, 560.0, 580.0, 600.0, 620.0,
                    640.0, 650.0, 660.0, 680.0, 700.0, 720.0, 740.0, 750.0, 760.0, 780.0,

                    800.0, 820.0, 840.0, 850.0, 860.0, 880.0, 900.0, 920.0, 940.0, 950.0,
                    960.0, 980.0, 1000.0, 1050.0, 1100.0, 1150.0, 1200.0, 1250.0, 1300.0, 1350.0,
                    1400.0, 1450.0, 1500.0, 1550.0, 1600.0, 1650.0, 1700.0, 1750.0, 1800.0, 1850.0,
                    1900.0, 1950.0, 2000.0, 2050.0, 2100.0, 2150.0, 2200.0, 2250.0, 2300.0, 2350.0,
                    2400.0, 2450.0, 2500.0, 2550.0, 2600.0, 2650.0, 2700.0, 2750.0, 2800.0, 2850.0,

                    2900.0, 2950.0, 3000.0, 3050.0, 3100.0, 3150.0, 3200.0, 3250.0, 3300.0, 3350.0,
                    3400.0, 3450.0, 3500.0, 3550.0, 3600.0, 3650.0, 3700.0, 3750.0, 3800.0, 3850.0,
                    3900.0, 3950.0, 4000.0, 4050.0, 4100.0, 4150.0, 4200.0, 4250.0, 4300.0, 4350.0,
                    4400.0, 4450.0, 4500.0, 4550.0, 4600.0, 4650.0, 4700.0, 4750.0, 4800.0, 4850.0, 4900.0, 4950.0, 5000.0]

        HwidthCPS = [0.00202, 0.00205, 0.00208, 0.00212, 0.00216, 0.00220, 0.00225, 0.00229, 0.00235, 0.00240,
                     0.00246, 0.00252, 0.00259, 0.00266, 0.00273, 0.00282, 0.00292, 0.00303, 0.00316, 0.00330,
                     0.00347, 0.00367, 0.00390, 0.00403, 0.00417, 0.00449, 0.00487, 0.00532, 0.00584, 0.00646,
                     0.00721, 0.00812, 0.00924, 0.0106, 0.0123, 0.0144, 0.0173, 0.0214, 0.0268, 0.0342,
                     0.0493, 0.0828, 0.141, 0.211, 0.276, 0.330, 0.379, 0.427, 0.475, 0.521,

                     0.570, 0.629, 0.702, 0.786, 0.870, 0.953, 1.03, 1.12, 1.19, 1.27,
                     1.35, 1.42, 1.5, 1.57, 1.65, 1.73, 1.81, 1.89, 1.97, 2.05,
                     2.14, 2.23, 2.32, 2.41, 2.5, 2.6, 2.7, 2.8, 2.9, 3.01,
                     3.12, 3.24, 3.36, 3.48, 3.61, 3.74, 3.87, 4.0, 4.13, 4.27,
                     4.42, 4.56, 4.71, 4.86, 5.01, 5.17, 5.33, 5.5, 5.66, 5.83,

                     6.01, 6.18, 6.36, 6.55, 6.73, 6.92, 7.12, 7.31, 7.51, 7.72,
                     7.93, 8.14, 8.68, 9.25, 9.83, 10.45, 11.08, 11.74, 12.43, 13.14,
                     13.88, 14.89, 17.08, 19.31, 21.63, 24.06, 26.6, 32.03, 37.94, 41.08,
                     44.35, 51.27, 58.7, 66.67, 75.16, 79.62, 84.2, 93.79, 103.93, 114.63,
                     125.88, 131.72, 137.69, 150.06, 162.97, 176.43, 190.43, 197.63, 204.96, 220.01,

                     235.57, 251.63, 268.17, 276.62, 285.18, 302.65, 320.55, 338.88, 357.62, 367.14,
                     376.75, 396.26, 416.12, 467.24, 520.26, 574.94, 631.07, 688.46, 746.93, 806.33,
                     866.54, 927.43, 988.91, 1050.9, 1113.3, 1176.1, 1239.2, 1302.5, 1366.1, 1429.9,
                     1493.9, 1558.0, 1622.2, 1686.6, 1751.0, 1815.5, 1880.2, 1944.8, 2009.6, 2074.4,
                     2139.2, 2204.1, 2269.1, 2334.0, 2399.1, 2464.1, 2529.2, 2594.4, 2659.6, 2724.8,

                     2790.1, 2855.4, 2920.7, 2986.1, 3051.7, 3117.4, 3183.1, 3248.9, 3314.7, 3380.5,
                     3446.4, 3512.3, 3578.3, 3644.4, 3710.5, 3776.6, 3831.6, 3883.5, 3935.3, 3987.2,
                     4039.0, 4090.8, 4142.6, 4194.3, 4246.1, 4297.9, 4349.7, 4401.5, 4453.3, 4505.0,
                     4547.8, 4599.5, 4651.2, 4702.8, 4754.5, 4806.2, 4857.9, 4909.6, 4961.2, 5012.9, 5064.6, 5116.3, 5168.0]

        g_graph = ROOT.TGraph(len(Hmass), numpy.array(Hmass), numpy.array(Hwidth))
        gCPS_graph = ROOT.TGraph(len(HmassCPS), numpy.array(HmassCPS), numpy.array(HwidthCPS))

        self.g = ROOT.TH1D("g","SM Higgs width",len(Hmass)-1,numpy.array(Hmass))
        self.gCPS = ROOT.TH1D("gCPS","SM Higgs width CPS",len(HmassCPS)-1,numpy.array(HmassCPS))
        for k,v in enumerate(Hwidth):
          self.g.SetBinContent(k+1,v)

        for k,v in enumerate(HwidthCPS):
          self.gCPS.SetBinContent(k+1,v)

        cmssw_arch = os.getenv('SCRAM_ARCH')
        complexpoleLib = self.cmssw_base+'/src/LatinoAnalysis/Gardener/python/variables/libcpHTO.so'
        complexpoleSrc = self.cmssw_base+'/src/LatinoAnalysis/Gardener/python/variables/pwhg_cpHTO_reweight.f'
        if not os.path.exists(complexpoleLib) or \
          os.stat(complexpoleLib).st_mtime < os.stat(complexpoleSrc).st_mtime:
          os.system('gfortran '+complexpoleSrc+' -fPIC --shared -o '+complexpoleLib)
        ROOT.gSystem.Load(complexpoleLib)
        try:
            ROOT.gROOT.LoadMacro(self.cmssw_base+'/src/LatinoAnalysis/Gardener/python/variables/pwhg_cpHTO_wrapper.cc+g')
        except RuntimeError:
            ROOT.gROOT.LoadMacro(self.cmssw_base+'/src/LatinoAnalysis/Gardener/python/variables/pwhg_cpHTO_wrapper.cc++g')

        #MELA reweighting
        # Stuff needed:
        # Directory ZZMatrixElement: https://github.com/cms-analysis/HiggsAnalysis-ZZMatrixElement.git / https://twiki.cern.ch/twiki/bin/view/CMS/MELAProject
        # Directory MelaAnalytics: https://github.com/usarica/MelaAnalytics.git
        ROOT.gSystem.AddIncludePath("-I"+self.cmssw_base+"/interface/")
        ROOT.gSystem.AddIncludePath("-I"+self.cmssw_base+"/src/")
        ROOT.gSystem.Load("libZZMatrixElementMELA.so")
        ROOT.gSystem.Load("libMelaAnalyticsCandidateLOCaster.so")
        ROOT.gSystem.Load(self.cmssw_base+"/src/ZZMatrixElement/MELA/data/"+cmssw_arch+"/libmcfm_706.so")
        try:
            ROOT.gROOT.LoadMacro(self.cmssw_base+'/src/LatinoAnalysis/Gardener/python/variables/melaReweighterWW.C+g')
        except RuntimeError:
            ROOT.gROOT.LoadMacro(self.cmssw_base+'/src/LatinoAnalysis/Gardener/python/variables/melaReweighterWW.C++g')

    def beginJob(self):
        pass

    def endJob(self):
        pass

    def beginFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):

        filename = str(inputFile)[str(inputFile).find("nanoLatino"):str(inputFile).find(".root")+5]
        filenameFormat = "nanoLatino_(GluGlu|VBF)HToWWTo(2L2Nu|LNuQQ)(_JHUGen698|_JHUGen714|)_M([0-9]+).*\.root"
        pattern = re.match(filenameFormat, filename)
        if pattern == None:
          raise NameError("Cannot parse filename",filename, "; Expected pattern is", filenameFormat)
        if pattern.group(1) == "VBF":
          self.productionProcess = "VBF"
        elif pattern.group(1) == "GluGlu":
          self.productionProcess = "ggH"
        else:
          raise NameError(pattern.group(1), "is an unknown production process")
        if pattern.group(2) == "2L2Nu":
          self.finalState = "2L2Nu"
        elif pattern.group(2) == "LNuQQ":
          self.finalState = "LNuQQ"
        else:
          raise NameError(pattern.group(2), "is an unknown final state")

        try:
          with open(self.cmssw_base+'/src/LatinoAnalysis/NanoGardener/python/data/BWShifts/BWShifts_'+self.productionProcess+'_'+self.finalState+'_'+self.year+'.txt') as shiftfile_stream:
             self.shifts = [line.rstrip().split() for line in shiftfile_stream if '#' not in line]
        except IOError:
          print "Shiftfile not loaded! Result will not be normalized!"
          self.shifts = 0

        self.mH  = float(pattern.group(4))

        # Looks like 714 needs the same treatment as 698. I assume the same goes for 710.
        # So only JHUgen628 from 2016 needs the special treatment
        if self.year == "2016" and pattern.group(3) == "" and self.finalState == "2L2Nu": self.isNewJHU = False
        if self.year == "2016" and self.finalState == "LNuQQ" and ((self.mH == 125.0) or (self.productionProcess == "VBF" and ((self.mH == 210.0) or (self.mH == 250.0)))): self.isNewJHU = False # Cherry picking v628 semileptonic samples

        self.gsm = self.g.GetBinContent(self.g.FindBin(self.mH))
        self.gsmCPS = self.gCPS.GetBinContent(self.gCPS.FindBin(self.mH))

        # only with the old JHU samples, which did not have proper decay weights for WW, we need to load the decay weights file.
        if not self.isNewJHU:
          with open (self.cmssw_base+'/src/LatinoAnalysis/NanoGardener/python/data/'+self.decayWeightsFile) as decayWeightsFile_stream:
            allparams = pickle.load(decayWeightsFile_stream)
          self.decayWeightFunction = interp1d(**allparams[str(int(self.mH))]["decayWeight"])
          self.minmass = min(allparams[str(int(self.mH))]["decayWeight"]['x'])
          self.maxmass = max(allparams[str(int(self.mH))]["decayWeight"]['x'])
          print "decay weights for mass", str(int(self.mH)), "available between", self.minmass, "and", self.maxmass 

        self.out = wrappedOutputTree
        self.branchnames = []

        # SM width model
        for cprime in self.cprime_list:
          for brnew in self.brnew_list:
            for appendix in ["", "_I", "_B", "_I_Honly", "_I_Bonly", "_I_HB", "_H"]:
              self.branchnames.append('cprime'+str(cprime)+"BRnew"+str(brnew)+appendix)
            for bname in self.branchnames:
              self.out.branch(bname, "F")

        # Relative width model
        for relw in self.relw_list:
          for appendix in ["", "_I", "_B", "_I_Honly", "_I_Bonly", "_I_HB", "_H"]:
            self.branchnames.append('RelW'+str(relw)+appendix)
          for bname in self.branchnames:
            self.out.branch(bname, "F")

        # MSSM
        if self.mssm:
          for appendix in ["", "_I", "_B", "_I_Honly", "_I_Bonly", "_I_HB", "_H"]:
            self.branchnames.append('MSSModel'+appendix)
          for bname in self.branchnames:
            self.out.branch(bname, "F")

        self.mela = ROOT.MelaReweighterWW(13, self.mH, self.gsm)
        #GF 1.16637e-5
        #sin2thetaW 0.22264585341299603
        #Wmass  = 80.398
        #ZMass = 91.1876
        self.mela.resetMCFM_EWKParameters(1.16637e-5, 1./128., 80.398, 91.1876, 0.22264585341299603)
        #self.count = 0
        #self.NANlist = []

    def endFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        pass

    def analyze(self, event):
        """process event, return True (go to next module) or False (fail, go to next event)"""

        #self.count += 1
        #if self.count%2000==0:
        #  process = psutil.Process(os.getpid())
        #  print self.count," : ",float(process.memory_info().rss)/(1024.0*1024.0)

        self.LHE = Collection(event,"LHEPart")
        Gen = Collection(event,"GenPart")
        #LHElepId = []
        #LHEneuId = []
        LHEjetId = []
        mass = getattr(event, 'higgsGenMass')

        for idx,part in enumerate(self.LHE):
          #  if abs(part.pdgId) in [11,13,15]:
          #    LHElepId.append(idx)
          #  elif abs(part.pdgId) in [12,14,16]:
          #    LHEneuId.append(idx)
          if abs(part.pdgId) in [1,2,3,4,5,21]:
            LHEjetId.append(idx)

        #LHElepId = self.pTorder(event, LHElepId)
        #LHEneuId = self.pTorder(event, LHEneuId)
        LHEjetId = self.pTorder(event, LHEjetId)

        fourMomenta=[]
        ids=[]

        FinalStatePartIDs = []
        for gid,gen in enumerate(Gen):
          if abs(gen.pdgId) >= 21: continue # Straight up ignore W bosons, photons or gluons from scattering
          if event.GenPart_genPartIdxMother[gid] == -1: continue # Protection for next line
          if abs(event.GenPart_pdgId[event.GenPart_genPartIdxMother[gid]]) != 24: continue # Somehow the check in the next line isn't sufficient for all cases
          plist = self.FromWandH(event, gid)
          if plist == False: continue
          ignore = 0
          for AlreadyIn in FinalStatePartIDs:
            if AlreadyIn in plist: ignore = 1
          if ignore == 1: continue
          FinalStatePartIDs.append(gid)

        if len(FinalStatePartIDs) != 4: # Remove W -> gamma W -> e+ e- W
          removethis = []
          for pi1,p1 in enumerate(FinalStatePartIDs):
            for pi2,p2 in enumerate(FinalStatePartIDs):
              if pi1>=pi2: continue
              if event.GenPart_genPartIdxMother[p1] != event.GenPart_genPartIdxMother[p2]: continue
              if event.GenPart_pdgId[p1] + event.GenPart_pdgId[p2] == 0:
                if p1 not in removethis: removethis.append(p1)
                if p2 not in removethis: removethis.append(p2)
                #print "Removing this: Part",p1,"with id",event.GenPart_pdgId[p1],"with mom",event.GenPart_genPartIdxMother[p1]
                #print "       ...and: Part",p2,"with id",event.GenPart_pdgId[p2],"with mom",event.GenPart_genPartIdxMother[p2]
            #if event.GenPart_pdgId[p1] == 21: removethis.append(p1)# Remove additional gluons
          for rem in removethis:
            FinalStatePartIDs.remove(rem)

        if len(FinalStatePartIDs) != 4: # Remove rare additonal hadrons
          removethis = []
          for pi1,p1 in enumerate(FinalStatePartIDs):
            mom_id = event.GenPart_genPartIdxMother[p1]
            NumWithThisID = 0
            for pi2,p2 in enumerate(FinalStatePartIDs):
              if event.GenPart_genPartIdxMother[p2] == mom_id: NumWithThisID += 1
            if NumWithThisID != 2:
              for pi2,p2 in enumerate(FinalStatePartIDs):
                if (event.GenPart_genPartIdxMother[p2] == mom_id) and (p2 not in removethis):
                  removethis.append(p2)
                  #print "Removing this: Part with id",event.GenPart_pdgId[p2],"from mom",event.GenPart_genPartIdxMother[p2],"with id",event.GenPart_pdgId[event.GenPart_genPartIdxMother[p2]]
          for rem in removethis:
            FinalStatePartIDs.remove(rem)

        # Numerous checks for failures. None should be triggered anymore.
        nlep = 0
        nneu = 0
        njet = 0
        for idx in FinalStatePartIDs:
          if abs(event.GenPart_pdgId[idx]) in [11,13,15]:
            nlep +=1
          elif abs(event.GenPart_pdgId[idx]) in [12,14,16]:
            nneu +=1
          elif abs(event.GenPart_pdgId[idx]) in [1,2,3,4,5,21]:
            njet +=1

        if len(FinalStatePartIDs) != 4:
          print "Not exactly 4 particles!"
          print "Event no.:",event.event

          if self.finalState == "2L2Nu" and njet !=0:
            print "Fixing..."
            removethis = []
            for idx in FinalStatePartIDs:
              if abs(event.GenPart_pdgId[idx]) in [1,2,3,4,5,21]: removethis.append(idx)
            for rem in removethis:
              FinalStatePartIDs.remove(rem)

          print FinalStatePartIDs
          for p in FinalStatePartIDs:
            print p,": id",event.GenPart_pdgId[p],", mom:",event.GenPart_genPartIdxMother[p],", momid:",event.GenPart_pdgId[event.GenPart_genPartIdxMother[p]]#,", mom-mom:",event.GenPart_genPartIdxMother[event.GenPart_genPartIdxMother[p]],", mom-momid:",event.GenPart_pdgId[event.GenPart_genPartIdxMother[event.GenPart_genPartIdxMother[p]]]

        if not ((nlep == 2 and nneu == 2 and self.finalState == "2L2Nu") or (nlep == 1 and nneu == 1 and njet == 2 and self.finalState == "LNuQQ")):
          print "Didn't get expected particles!"
          print "Event no.:",event.event
          print FinalStatePartIDs
          print "nlep:",nlep,", nneu:",nneu,", njet:",njet

        LHEFinalStateIDs = self.getLHE(event, FinalStatePartIDs)

        if len(LHEFinalStateIDs)!=4:
          print "SOMETHING WENT WRONG!"
          print "Event no.:",event.event
          print LHEFinalStateIDs
          print FinalStatePartIDs

        for ipart in LHEFinalStateIDs:
          l = ROOT.TLorentzVector()
          l.SetPtEtaPhiM(LHEFinalStateIDs[ipart][0], LHEFinalStateIDs[ipart][1], LHEFinalStateIDs[ipart][2], 0.)
          fourMomenta.append(l)
          ids.append(LHEFinalStateIDs[ipart][3])

        #if self.finalState == "2L2Nu":
        #  for ilep in range(2):
        #    l = ROOT.TLorentzVector()
        #    l.SetPtEtaPhiM(event.LHEPart_pt[LHElepId[ilep]], event.LHEPart_eta[LHElepId[ilep]], event.LHEPart_phi[LHElepId[ilep]], 0.)
        #    fourMomenta.append(l)
        #    ids.append(event.LHEPart_pdgId[LHElepId[ilep]])
        #  for ineu in range(2):  
        #    n = ROOT.TLorentzVector()
        #    n.SetPtEtaPhiM(event.LHEPart_pt[LHEneuId[ineu]], event.LHEPart_eta[LHEneuId[ineu]], event.LHEPart_phi[LHEneuId[ineu]], 0.)
        #    fourMomenta.append(n)
        #    ids.append(event.LHEPart_pdgId[LHEneuId[ineu]])
        #else:
        #  l = ROOT.TLorentzVector()
        #  l.SetPtEtaPhiM(event.LHEPart_pt[LHElepId[0]], event.LHEPart_eta[LHElepId[0]], event.LHEPart_phi[LHElepId[0]], 0.)
        #  fourMomenta.append(l)
        #  ids.append(event.LHEPart_pdgId[LHElepId[0]])
        #  n = ROOT.TLorentzVector()
        #  n.SetPtEtaPhiM(event.LHEPart_pt[LHEneuId[0]], event.LHEPart_eta[LHEneuId[0]], event.LHEPart_phi[LHEneuId[0]], 0.)
        #  fourMomenta.append(n)
        #  ids.append(event.LHEPart_pdgId[LHEneuId[0]])
        #  for ijet in range(2):
        #    j = ROOT.TLorentzVector()
        #    j.SetPtEtaPhiM(event.LHEPart_pt[LHEjetId[ijet]], event.LHEPart_eta[LHEjetId[ijet]], event.LHEPart_phi[LHEjetId[ijet]], 0.)
        #    fourMomenta.append(j)
        #    ids.append(event.LHEPart_pdgId[LHEjetId[ijet]])


        #these are the incoming partons
        mothers = ROOT.vector('TLorentzVector')()
        motherIDs = ROOT.vector('int')()
        incoming1=ROOT.TLorentzVector()
        incoming1.SetPxPyPzE(0.,0., event.Generator_x1*6500, event.Generator_x1*6500)
        incoming2=ROOT.TLorentzVector()
        incoming2.SetPxPyPzE(0.,0.,-1*event.Generator_x2*6500, event.Generator_x2*6500)
        mothers.push_back(incoming1)
        mothers.push_back(incoming2)
        genid1 = int(event.Generator_id1)
        genid2 = int(event.Generator_id2)

        #print "incoming:", [genid1, genid2]
        #print incoming1.Px(), incoming1.Py(), incoming1.Pz(), genid1, event.Generator_x1
        #print incoming2.Px(), incoming2.Py(), incoming2.Pz(), genid2, event.Generator_x2

        partons   = ROOT.vector('TLorentzVector')()
        partonIDs = ROOT.vector('int')()
        parton_ids = []
        #print "outgoing:",
        for ijet in LHEjetId:
          if ijet in LHEFinalStateIDs: continue
          parton = ROOT.TLorentzVector()
          parton.SetPtEtaPhiM(event.LHEPart_pt[ijet], event.LHEPart_eta[ijet], event.LHEPart_phi[ijet], 0.)
          partons.push_back(parton)                     
          partonIDs.push_back(int(event.LHEPart_pdgId[ijet]))
          parton_ids.append(int(event.LHEPart_pdgId[ijet]))
          #print parton.Px(), parton.Py(), parton.Pz(), int(event.LHEPart_pdgId[ijet])
          #print int(event.LHEPart_pdgId[ijet]),

        # Generator id seems to be wrong in few VBF events... -> Replace pdgId 21 by whatever is in LHE collection
        if self.productionProcess == "VBF" and (genid1==21 or genid2==21) and (21 in parton_ids):
          options = [o for o in parton_ids if o != 21] # Should usually contain 2 entries; There are _always_ 3 LHE jets because VBF samples are NLO
          if genid1==21 and genid2!=21:
            genid1 = options[0] + options[1] - genid2 # USUALLY Sum pdgIds incoming = Sum pdgIds outgoing (exception is 2.gen <-> 1.gen quark)
            print "INFO: Replaced incoming particle ID1 to", genid1, "in event", event.event
          elif genid1!=21 and genid2==21:
            genid2 = options[0] + options[1] - genid1
            print "INFO: Replaced incoming particle ID2 to", genid2, "in event", event.event
          elif genid1==21 and genid2==21: # Assuming qq -> ZZ -> H
            genid1 = options[0]
            genid2 = options[1]
            print "INFO: Replaced incoming particle ID1 to", genid1, "_AND_ ID2 to", genid2, " in event", event.event
          print "incoming:", [genid1, genid2]
          print "outgoing:", parton_ids
          #if self.finalState == "2L2Nu" and self.mH == 800.0 and event.event == 180366: genid1 = 2   # An example
        motherIDs.push_back(genid1)
        motherIDs.push_back(genid2)



        # with the new JHU decay weights are already in the sample, no need to apply them here
        if self.isNewJHU:
          decayWeight = 1.
        # with old JHU samples we need to apply the decay weights  
        else:  
          if mass < self.minmass:
            decayWeight = self.decayWeightFunction(self.minmass)
          elif mass > self.maxmass:  
            decayWeight = self.decayWeightFunction(self.maxmass)
          else:   
            decayWeight = self.decayWeightFunction(mass)


        ########## For SM width model
        CPSweight = 1.
        if self.undoCPS:
          if self.isNewJHU:
            # in this case the sample already has the correct decay weights for WW
            # we just need to undo the pure CPS part and restore the SM width
            CPSweight = self.FixedBreightWigner(mass, self.mH, self.gsmCPS)/self.FixedBreightWigner(mass, self.mH, self.gsm)
          else:
            # in this case the sample was done with BOTH CPS width and average decay weights, so we need to undo both
            # using the corresponding POWHEG-passarino code.
            CPSweight = ROOT.getCPSweight(self.mH, self.gsm, 172.5, mass, 0)

        for cprime in self.cprime_list:
          for brnew in self.brnew_list:
            weights = {}
            name = 'cprime'+str(cprime)+"BRnew"+str(brnew)
            kprime = cprime**2
            #overallweight = kprime*(1-brnew) 
            gprime = self.Gprime(self.mH, kprime, brnew)
            shift = 1.
            if self.shifts:
              for line in self.shifts:
                if float(line[0])==self.mH and float(line[1])==cprime and float(line[2])==brnew:
                  shift = float(line[3])
                  break
            weights[name] = (1./shift)*decayWeight*self.FixedBreightWigner(mass, self.mH, gprime)/self.FixedBreightWigner(mass, self.mH, self.gsm)/CPSweight
            self.mela.setMelaHiggsMassWidth(self.mH, gprime)
            self.mela.setupDaughters((self.productionProcess=="VBF"), int(ids[0]), int(ids[1]), int(ids[2]), int(ids[3]),
                                                         fourMomenta[0], fourMomenta[1], fourMomenta[2], fourMomenta[3],
                                                         partons, partonIDs,
                                                         mothers, motherIDs)
            addweight = {}
            addweight["_I"] = self.mela.weightStoI()
            addweight["_I_Honly"] = self.mela.weightStoI_H()
            addweight["_I_Bonly"] = self.mela.weightStoI_B()
            addweight["_I_HB"] = self.mela.weightStoI_HB()
            addweight["_B"] = self.mela.weightStoB()
            addweight["_H"] = self.mela.weightStoH()

            for appendix in ["_I", "_B", "_I_Honly", "_I_Bonly", "_I_HB", "_H"]:
              if math.isnan(addweight[appendix]) or math.isinf(addweight[appendix]): #dirty protection for occasional failures
                self.NANinfo
                addweight[appendix]=0.
              weights[name+appendix] = weights[name]*addweight[appendix]

            for appendix in ["", "_I", "_B", "_I_Honly", "_I_Bonly", "_I_HB", "_H"]:
              self.out.fillBranch(name+appendix, weights[name+appendix])


        ########## For Relative Width model
        for relw in self.relw_list:
          self.gsm = relw * self.mH
          if self.gsm == 0: self.gsm = 0.001 * self.mH
          if self.undoCPS:
            # Invert CPSweight here w.r.t. previously because it could be 0
            if self.isNewJHU:
              CPSweight = self.FixedBreightWigner(mass, self.mH, self.gsm)/self.FixedBreightWigner(mass, self.mH, self.gsmCPS)
            else:
              thisCPSweight = ROOT.getCPSweight(self.mH, self.gsm, 172.5, mass, 0)
              CPSweight = 0 if (thisCPSweight==0) else 1/thisCPSweight

          weights = {}
          name = 'RelW'+str(relw)
          shift = 1.
          if self.shifts:
            for line in self.shifts:
              if float(line[0])==self.mH and float(line[1])==relw and float(line[2])==-1:
                shift = float(line[3])
                break
          weights[name] = (1./shift)*decayWeight*CPSweight
          self.mela.setMelaHiggsMassWidth(self.mH, self.gsm)
          self.mela.setupDaughters((self.productionProcess=="VBF"), int(ids[0]), int(ids[1]), int(ids[2]), int(ids[3]),
                                                       fourMomenta[0], fourMomenta[1], fourMomenta[2], fourMomenta[3],
                                                       partons, partonIDs,
                                                       mothers, motherIDs)
          addweight = {}
          addweight["_I"] = self.mela.weightStoI()
          addweight["_I_Honly"] = self.mela.weightStoI_H()
          addweight["_I_Bonly"] = self.mela.weightStoI_B()
          addweight["_I_HB"] = self.mela.weightStoI_HB()
          addweight["_B"] = self.mela.weightStoB()
          addweight["_H"] = self.mela.weightStoH()

          for appendix in ["_I", "_B", "_I_Honly", "_I_Bonly", "_I_HB", "_H"]:
            if math.isnan(addweight[appendix]) or math.isinf(addweight[appendix]): #dirty protection for occasional failures
              self.NANinfo
              addweight[appendix]=0.
            weights[name+appendix] = weights[name]*addweight[appendix]

          for appendix in ["", "_I", "_B", "_I_Honly", "_I_Bonly", "_I_HB", "_H"]:
            self.out.fillBranch(name+appendix, weights[name+appendix])


        ########## For MSSM -> No EWK singlet interpretation -> No width reweighting; calculate interference based on original CPS width
        if self.mssm:
          weights = {}
          name = 'MSSModel'

          shift = 1.
          if self.shifts:
            for line in self.shifts:
              if float(line[0])==self.mH and float(line[1])==-1 and float(line[2])==-1:
                shift = float(line[3])
                break
          weights[name] = (1./shift)*decayWeight
          self.mela.setMelaHiggsMassWidth(self.mH, self.gsmCPS)
          self.mela.setupDaughters((self.productionProcess=="VBF"), int(ids[0]), int(ids[1]), int(ids[2]), int(ids[3]),
                                                           fourMomenta[0], fourMomenta[1], fourMomenta[2], fourMomenta[3],
                                                           partons, partonIDs,
                                                           mothers, motherIDs)
          addweight = {}
          addweight["_I"] = self.mela.weightStoI()
          addweight["_I_Honly"] = self.mela.weightStoI_H()
          addweight["_I_Bonly"] = self.mela.weightStoI_B()
          addweight["_I_HB"] = self.mela.weightStoI_HB()
          addweight["_B"] = self.mela.weightStoB()
          addweight["_H"] = self.mela.weightStoH()

          for appendix in ["_I", "_B", "_I_Honly", "_I_Bonly", "_I_HB", "_H"]:
            if math.isnan(addweight[appendix]) or math.isinf(addweight[appendix]): #dirty protection for occasional failures
              self.NANinfo
              addweight[appendix]=0.
            weights[name+appendix] = weights[name]*addweight[appendix]

          for appendix in ["", "_I", "_B", "_I_Honly", "_I_Bonly", "_I_HB", "_H"]:
            self.out.fillBranch(name+appendix, weights[name+appendix])

        return True


    def muprime(self, k, br):
      return k*(1-br)

    def FixedBreightWigner(self, m, mH, G):
      if G == 0.0: return 0.0
      return mH*G/((m**2-mH**2)**2 + (mH*G)**2)
    
    def RunningBreightWigner(self, m, mH, G):
      return (m**2*G/mH)/((m**2-mH**2)**2 + (m**2*G/mH)**2)

    def Gprime(self, mh,k,br):
      if self.g == None:
        raise Exception("Internal histogram of higgs widths not initialized")
      return  self.GprimeOverGsm(k, br)*self.g.GetBinContent(self.g.FindBin(mh))

    def GprimeOverGsm(self, k,br):
      return k/(1-br)

    def pTorder(self, event, oldlist):
      order = []
      for i in oldlist:
        order.append(0)
      for i,pone in enumerate(oldlist):
        for j,ptwo in enumerate(oldlist):
          if pone==ptwo: continue
          if event.LHEPart_pt[pone] > event.LHEPart_pt[ptwo]: order[i] += 1
          if (event.LHEPart_pt[pone] == event.LHEPart_pt[ptwo]) and (i<j):
            order[j] += 1
      newlist = [oldlist[i] for i in order]
      return newlist

    def FromWandH(self, event, pid):
      fromH = 0
      fromW = 0
      plist = []
      while event.GenPart_genPartIdxMother[pid] != -1:
        pid = event.GenPart_genPartIdxMother[pid]
        plist.append(pid)
        if abs(event.GenPart_pdgId[pid]) == 24: fromW = 1
        if event.GenPart_pdgId[pid] == 25: fromH = 1
        if fromH and fromW: return plist
      return False
      

    def getLHE(self, event, genlist): # Particles in LHE collection have higher precision -> Find LHE particles with closest match to GenParticles
      LHElist = {}
      for gid in genlist:
        pt = event.GenPart_pt[gid]
        eta = event.GenPart_eta[gid]
        phi = event.GenPart_phi[gid]
        pdgid = event.GenPart_pdgId[gid]
        deltaR = 9999
        LHEid = -1
        #print "====="
        #print gid,pdgid,eta,phi
        for lid,lhe in enumerate(self.LHE):
          #print lhe.pdgId,lhe.eta,lhe.phi
          if lhe.pdgId != pdgid: continue
          dphi = phi-lhe.phi
          if dphi > math.pi: dphi -= 2*math.pi
          if dphi < -math.pi: dphi += 2*math.pi
          deta = eta-lhe.eta
          dR = math.sqrt((deta)*(deta)+(dphi)*(dphi))
          if deltaR > dR:
            deltaR = dR
            LHEid = lid
            LHEpt = lhe.pt
            LHEeta = lhe.eta
            LHEphi = lhe.phi
            LHEpdg = lhe.pdgId
        #print "DeltaR:",deltaR
        if LHEid==-1: # VERY rare, use placeholder key value
          LHElist[pdgid+100*(len(LHElist)+1)]=[pt, eta, phi, pdgid]
        elif deltaR > 0.2: # Use GenPart information if direction is too different
          #print "Eta:",eta,"vs.",LHEeta
          #print "Phi:",phi,"vs.",LHEphi
          LHElist[LHEid]=[pt, eta, phi, pdgid]
        else:
          LHElist[LHEid]=[LHEpt, LHEeta, LHEphi, pdgid]
        
      return LHElist

    def NANinfo(self, eventnr):
      if eventnr not in self.NANlist:
        self.NANlist.append(eventnr)
        print "Got NAN! Event no.:",eventnr,"; current NAN percentage:", float(len(self.NANlist))/float(self.count)

