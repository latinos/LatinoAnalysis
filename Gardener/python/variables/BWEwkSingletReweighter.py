
from LatinoAnalysis.Gardener.gardening import TreeCloner
import numpy
import ROOT
import math
import sys
import optparse
import re
import warnings
import os.path
from collections import OrderedDict
from array import array;
import numpy as np
import pickle
from scipy.interpolate import interp1d

class BWEwkSingletReweighter(TreeCloner):
    def __init__(self):
      Hmass = [200, 202, 204, 206, 208, 210, 212, 214, 216, 218, 220, 222, 224, 226, 228, 230, 232, 234, 236, 238, 240, 242, 244, 246, 248, 250, 252, 254, 256, 258, 260, 262, 264, 266, 268, 270, 272, 274, 276, 278, 280, 282, 284, 286, 288, 290, 292, 294, 296, 298, 300, 305, 310, 315, 320, 325, 330, 335, 340, 345, 350, 360, 370, 380, 390, 400, 420, 440, 450, 460, 480, 500, 520, 540, 550, 560, 580, 600, 620, 640, 650, 660, 680, 700, 720, 740, 750, 760, 780, 800, 820, 840, 850, 860, 880, 900, 920, 940, 950, 960, 980, 1000., 1050, 1100, 1150, 1200, 1250, 1300, 1350, 1400, 1450, 1500, 1550, 1600, 1650, 1700, 1750, 1800, 1850, 1900, 1950, 2000, 2050, 2100, 2150, 2200, 2250, 2300, 2350, 2400, 2450, 2500, 2550, 2600, 2650, 2700, 2750, 2800, 2850, 2900, 2950, 3000, 3050, 3100, 3150, 3200, 3250, 3300, 3350, 3400, 3450, 3500, 3550, 3600, 3650, 3700, 3750, 3800, 3850, 3900, 3950, 4000, 4050, 4100, 4150, 4200, 4250, 4300, 4350, 4400, 4450, 4500, 4550, 4600, 4650, 4700, 4750, 4800, 4850, 4900, 4950, 5000]

      HmassCPS = [200.0, 202.0, 204.0, 206.0, 208.0, 210.0, 212.0, 214.0, 216.0, 218.0, 220.0, 222.0, 224.0, 226.0, 228.0, 230.0, 232.0, 234.0, 236.0, 238.0, 240.0, 242.0, 244.0, 246.0, 248.0, 250.0, 252.0, 254.0, 256.0, 258.0, 260.0, 262.0, 264.0, 266.0, 268.0, 270.0, 272.0, 274.0, 276.0, 278.0, 280.0, 282.0, 284.0, 286.0, 288.0, 290.0, 292.0, 294.0, 296.0, 298.0, 300.0, 305.0, 310.0, 315.0, 320.0, 325.0, 330.0, 335.0, 340.0, 345.0, 350.0, 360.0, 370.0, 380.0, 390.0, 400.0, 420.0, 440.0, 450.0, 460.0, 480.0, 500.0, 520.0, 540.0, 550.0, 560.0, 580.0, 600.0, 620.0, 640.0, 650.0, 660.0, 680.0, 700.0, 720.0, 740.0, 750.0, 760.0, 780.0, 800.0, 820.0, 840.0, 850.0, 860.0, 880.0, 900.0, 920.0, 940.0, 950.0, 960.0, 980.0, 1000.0, 1050.0, 1100.0, 1150.0, 1200.0, 1250.0, 1300.0, 1350.0, 1400.0, 1450.0, 1500.0, 1550.0, 1600.0, 1650.0, 1700.0, 1750.0, 1800.0, 1850.0, 1900.0, 1950.0, 2000.0, 2050.0, 2100.0, 2150.0, 2200.0, 2250.0, 2300.0, 2350.0, 2400.0, 2450.0, 2500.0, 2550.0, 2600.0, 2650.0, 2700.0, 2750.0, 2800.0, 2850.0, 2900.0, 2950.0, 3000.0, 3050.0, 3100.0, 3150.0, 3200.0, 3250.0, 3300.0, 3350.0, 3400.0, 3450.0, 3500.0, 3550.0, 3600.0, 3650.0, 3700.0, 3750.0, 3800.0, 3850.0, 3900.0, 3950.0, 4000.0, 4050.0, 4100.0, 4150.0, 4200.0, 4250.0, 4300.0, 4350.0, 4400.0, 4450.0, 4500.0, 4550.0, 4600.0, 4650.0, 4700.0, 4750.0, 4800.0, 4850.0, 4900.0, 4950.0, 5000.0] 

      Hwidth = [1.43, 1.51, 1.59, 1.68, 1.76, 1.85, 1.93, 2.02, 2.12, 2.21, 2.31, 2.40, 2.50, 2.61, 2.71, 2.82, 2.93, 3.04, 3.16, 3.27, 3.40, 3.52, 3.64, 3.77, 3.91, 4.04, 4.18, 4.32, 4.46, 4.61, 4.76, 4.91, 5.07, 5.23, 5.39, 5.55, 5.72, 5.89, 6.07, 6.25, 6.43, 6.61, 6.80, 6.99, 7.19, 7.39, 7.59, 7.79, 8.00, 8.22, 8.43, 8.99, 9.57, 10.20, 10.80, 11.40, 12.10, 12.80, 13.50, 14.20, 15.20, 17.60, 20.20, 23.10, 26.10, 29.20, 35.90, 43.00, 46.80, 50.80, 59.10, 68.00, 77.50, 87.70, 93.00, 98.60, 110.00, 123.00, 136.00, 150.00, 158.00, 165.00, 182.00, 199.00, 217.00, 237.00, 247.00, 258.00, 280.00, 304.00, 330.00, 357.00, 371.00, 386.00, 416.00, 449.00, 484.00, 521.00, 540.00, 560.00, 602.00, 647.00, 525, 550, 575, 600, 625, 650, 675, 700, 725, 750, 775, 800, 825, 850, 875, 900, 925, 950, 975, 1000, 1025, 1050, 1075, 1100, 1125, 1150, 1175, 1200, 1225, 1250, 1275, 1300, 1325, 1350, 1375, 1400, 1425, 1450, 1475, 1500, 1525, 1550, 1575, 1600, 1625, 1650, 1675, 1700, 1725, 1750, 1775, 1800, 1825, 1850, 1875, 1900, 1925, 1950, 1975, 2000, 2025, 2050, 2075, 2100, 2125, 2150, 2175, 2200, 2225, 2250, 2275, 2300, 2325, 2350, 2375, 2400, 2425, 2450, 2475, 2500];

      HwidthCPS = [1.42, 1.5, 1.57, 1.65, 1.73, 1.81, 1.89, 1.97, 2.05, 2.14, 2.23, 2.32, 2.41, 2.5, 2.6, 2.7, 2.8, 2.9, 3.01, 3.12, 3.24, 3.36, 3.48, 3.61, 3.74, 3.87, 4.0, 4.13, 4.27, 4.42, 4.56, 4.71, 4.86, 5.01, 5.17, 5.33, 5.5, 5.66, 5.83, 6.01, 6.18, 6.36, 6.55, 6.73, 6.92, 7.12, 7.31, 7.51, 7.72, 7.93, 8.14, 8.68, 9.25, 9.83, 10.45, 11.08, 11.74, 12.43, 13.14, 13.88, 14.89, 17.08, 19.31, 21.63, 24.06, 26.6, 32.03, 37.94, 41.08, 44.35, 51.27, 58.7, 66.67, 75.16, 79.62, 84.2, 93.79, 103.93, 114.63, 125.88, 131.72, 137.69, 150.06, 162.97, 176.43, 190.43, 197.63, 204.96, 220.01, 235.57, 251.63, 268.17, 276.62, 285.18, 302.65, 320.55, 338.88, 357.62, 367.14, 376.75, 396.26, 416.12, 467.24, 520.26, 574.94, 631.07, 688.46, 746.93, 806.33, 866.54, 927.43, 988.91, 1050.89, 1100.0, 1100.0, 1100.0, 1100.0, 900.0, 1100.0, 1100.0, 1100.0, 1000.0, 1100.0, 1050.0, 1075.0, 1100.0, 1100.0, 1100.0, 1100.0, 1100.0, 1100.0, 1100.0, 1100.0, 1100.0, 1100.0, 1100.0, 1100.0, 1100.0, 1100.0, 1100.0, 1100.0, 1100.0, 1100.0, 1100.0, 1100.0, 1100.0, 1100.0, 1100.0, 1100.0, 1100.0, 1100.0, 1100.0, 1100.0, 1100.0, 1100.0, 1100.0, 1100.0, 1100.0, 1100.0, 1100.0, 1100.0, 1100.0, 1100.0, 1100.0, 1100.0, 1100.0, 1100.0, 1100.0, 1100.0, 1100.0, 1100.0, 1100.0, 1100.0, 1100.0, 1100.0, 1100.0, 1100.0, 1100.0, 1100.0, 1100.0, 1100.0, 1100.0] 
      
      self.g = ROOT.TH1D("g","SM Higgs width",len(Hmass)-1,numpy.array(Hmass));
      self.gCPS = ROOT.TH1D("gCPS","SM Higgs width CPS",len(HmassCPS)-1,numpy.array(HmassCPS));
      for k,v in enumerate(Hwidth):
        self.g.SetBinContent(k+1,v);     

      for k,v in enumerate(HwidthCPS):
        self.gCPS.SetBinContent(k+1,v);

      pass

    def help(self):
        return '''calculate event weights in the electroweak singlet model using parameters c' and BRnew. Ranges and steps of those parameters can be specified '''

    def addOptions(self,parser):
        description = self.help()
        group = optparse.OptionGroup(parser,self.label, description)
        #group.add_option('-m', "--mass",       dest = 'mH',   help="mass point",      default=125., type='float')
        group.add_option('-u', "--undoCPS",       dest = 'undoCPS',   help="Needed in case the original sample was produced withc omplex Pole Mass Scheme",      default=True, action='store_true')
        group.add_option('-i', '--cprimemin' , dest='cprimemin' , help="c' minimum value", default=0.1,  type='float')
        group.add_option('-f', '--cprimemax' , dest='cprimemax' , help="c' maximum value", default=1.,  type='float')
        group.add_option('-s', '--cprimestep', dest='cprimestep', help="c' step",          default=0.1, type='float')
        group.add_option('-l', '--brnewmin' , dest='brnewmin' ,   help="BRnew minimum value", default=0.,  type='float')
        group.add_option('-n', '--brnewmax' , dest='brnewmax' ,   help="BRnew maximum value", default=1.,  type='float')
        group.add_option('-q' , '--brnewstep', dest='brnewstep',   help="BRnew step",          default=0.5, type='float') 
        group.add_option('-w' , '--globalshiftfileGG', dest='shiftfileGG',   help="pickle file containing the global shifts due to reweighting (to preserve integral) for GG.", default="data/BWShifts_ggH.pkl") 
        group.add_option('-k' , '--globalshiftfileVBF', dest='shiftfileVBF',   help="pickle file containing the global shifts due to reweighting (to preserve integral) for VBF.", default="data/BWShifts_VBF.pkl") 
        group.add_option('-d' , '--decayWeightsFile', dest='decayWeightsFile',   help="pickle file containing the JHU derived decay weights for WW", default="data/decayWeightsWW.pkl") 
        group.add_option('-p' , '--fileNameFormat', dest='fileNameFormat',   help="file name format to determine production process and mass", default="latino_(GluGlu|VBF)HToWWTo2L2Nu(_JHUGen698|)_M([0-9]+).*\.root") 
        parser.add_option_group(group)
        return group

    def checkOptions(self,opts):
        cmssw_base = os.getenv('CMSSW_BASE')
        self.cprimemin        = opts.cprimemin
        self.cprimemax        = opts.cprimemax
        self.cprimestep       = opts.cprimestep
        self.brnewmin         = opts.brnewmin
        self.brnewmax         = opts.brnewmax
        self.brnewstep        = opts.brnewstep
        #self.mH               = opts.mH
        #self.gsm              = self.g.GetBinContent(self.g.FindBin(self.mH))
        self.undoCPS          = opts.undoCPS
        if opts.shiftfileGG == "":
          self.shiftfileGG        = opts.shiftfileGG
        else:
          self.shiftfileGG        = cmssw_base+'/src/LatinoAnalysis/Gardener/python/'+opts.shiftfileGG
          
        if opts.shiftfileVBF == "":
          self.shiftfileVBF        = opts.shiftfileVBF
        else:
          self.shiftfileVBF        = cmssw_base+'/src/LatinoAnalysis/Gardener/python/'+opts.shiftfileVBF
 
        self.decayWeightsFile = cmssw_base+'/src/LatinoAnalysis/Gardener/python/'+opts.decayWeightsFile
        self.fileNameFormat    = opts.fileNameFormat
        print "c' start", self.cprimemin
        print "c' stop", self.cprimemax
        print "c' step", self.cprimestep
        print "BRnew start", self.brnewmin
        print "BRnew stop", self.brnewmax
        print "BRnew step", self.brnewstep
        print "global shift for GG from file", self.shiftfileGG
        print "global shift for VBF from file", self.shiftfileVBF
        print "Decay weights from file", self.decayWeightsFile
        if self.undoCPS:
          print "Undoing Complex Pole Scheme before applying the BW weights"
        cmssw_base = os.getenv('CMSSW_BASE')
        cmssw_arch = os.getenv('SCRAM_ARCH')
        complexpoleLib = cmssw_base+'/src/LatinoAnalysis/Gardener/python/variables/libcpHTO.so'
        complexpoleSrc = cmssw_base+'/src/LatinoAnalysis/Gardener/python/variables/pwhg_cpHTO_reweight.f'
        if not os.path.exists(complexpoleLib) or \
          os.stat(complexpoleLib).st_mtime < os.stat(complexpoleSrc).st_mtime:
          os.system('gfortran '+complexpoleSrc+' -fPIC --shared -o '+complexpoleLib)
        ROOT.gSystem.Load(complexpoleLib)
        try:
            ROOT.gROOT.LoadMacro(cmssw_base+'/src/LatinoAnalysis/Gardener/python/variables/pwhg_cpHTO_wrapper.cc+g')
        except RuntimeError:
            ROOT.gROOT.LoadMacro(cmssw_base+'/src/LatinoAnalysis/Gardener/python/variables/pwhg_cpHTO_wrapper.cc++g')

        #MELA reweighting
        ROOT.gSystem.AddIncludePath("-I"+cmssw_base+"/interface/");
        ROOT.gSystem.AddIncludePath("-I"+cmssw_base+"/src/");
        ROOT.gSystem.Load("libZZMatrixElementMELA.so");
        ROOT.gSystem.Load("libMelaAnalyticsCandidateLOCaster.so");
        ROOT.gSystem.Load(cmssw_base+"/src/ZZMatrixElement/MELA/data/"+cmssw_arch+"/libmcfm_705.so");
        try:
            ROOT.gROOT.LoadMacro(cmssw_base+'/src/LatinoAnalysis/Gardener/python/variables/melaReweighterWW.C+g')
        except RuntimeError:
            ROOT.gROOT.LoadMacro(cmssw_base+'/src/LatinoAnalysis/Gardener/python/variables/melaReweighterWW.C++g')
    
    def muprime(self, k, br):
      return k*(1-br)

    def FixedBreightWigner(self, m, mH, G):
      return mH*G/((m**2-mH**2)**2 + (mH*G)**2)
    
    def RunningBreightWigner(self, m, mH, G):
      return (m**2*G/mH)/((m**2-mH**2)**2 + (m**2*G/mH)**2)

    def GprimeOverGsm(self, k,br):
      return k/(1-br)

    def Gprime(self, mh,k,br):
      if self.g == None:
        raise Exception("Internal histogram of higgs widths not initialized")
      return  self.GprimeOverGsm(k, br)*self.g.GetBinContent(self.g.FindBin(mh)) 

    def process(self,**kwargs):
        tree  = kwargs['tree']
        input = kwargs['input']
        output = kwargs['output']

        filename = (input.split("/"))[-1]
        pattern = re.match(self.fileNameFormat, filename)
        if pattern == None:
          print "cannot parse filename",filename, "Expected pattern is", self.fileNameFormat
          return
        if pattern.group(1) == "VBF":
          productionProcess = "VBF"
        elif pattern.group(1) == "GluGlu":
          productionProcess = "GG"
        else:
          print pattern.group(1), "is an unknown production process"
          return
        
        self.isNewJHU = pattern.group(2)
        #print "ciaoooo", self.isNewJHU
        self.mH  = float(pattern.group(3))
        self.gsm = self.g.GetBinContent(self.g.FindBin(self.mH))
        self.gsmCPS = self.gCPS.GetBinContent(self.gCPS.FindBin(self.mH))
        print "Mass", self.mH, " with SM width", self.gsm, " and CPS width ", self.gsmCPS

        # does that work so easily and give new variable itree and otree?
        self.connect(tree,input)

        nentries = self.itree.GetEntries()
        print 'Total number of entries: ',nentries 

        self.namesOldBranchesToBeModifiedSimpleVariable = []
        rangecprime = np.arange(self.cprimemin, self.cprimemax, self.cprimestep).tolist()
        rangeBRnew  = np.arange(self.brnewmin, self.brnewmax, self.brnewstep).tolist()
        if (self.cprimemax) not in rangecprime:
          rangecprime.append(self.cprimemax)
        if (self.brnewmin) not in rangeBRnew:
          rangeBRnew.insert(0, self.brnewmin)
        print "cprimes", rangecprime
        print "BRnews", rangeBRnew

        for cprime in rangecprime:
          for BRnew in rangeBRnew:
            self.namesOldBranchesToBeModifiedSimpleVariable.append('cprime'+str(cprime)+"BRnew"+str(BRnew))
            self.namesOldBranchesToBeModifiedSimpleVariable.append('cprime'+str(cprime)+"BRnew"+str(BRnew)+"_I")
            self.namesOldBranchesToBeModifiedSimpleVariable.append('cprime'+str(cprime)+"BRnew"+str(BRnew)+"_B")
            self.namesOldBranchesToBeModifiedSimpleVariable.append('cprime'+str(cprime)+"BRnew"+str(BRnew)+"_I_Honly")
            self.namesOldBranchesToBeModifiedSimpleVariable.append('cprime'+str(cprime)+"BRnew"+str(BRnew)+"_I_Bonly")
            self.namesOldBranchesToBeModifiedSimpleVariable.append('cprime'+str(cprime)+"BRnew"+str(BRnew)+"_I_HB")
            self.namesOldBranchesToBeModifiedSimpleVariable.append('cprime'+str(cprime)+"BRnew"+str(BRnew)+"_H")

        # clone the tree
        self.clone(output, self.namesOldBranchesToBeModifiedSimpleVariable)

        self.oldBranchesToBeModifiedSimpleVariable = {}
        for bname in self.namesOldBranchesToBeModifiedSimpleVariable:
          bvariable = numpy.ones(1, dtype=numpy.float32)
          self.oldBranchesToBeModifiedSimpleVariable[bname] = bvariable

        # now actually connect the branches
        for bname, bvariable in self.oldBranchesToBeModifiedSimpleVariable.iteritems():
            #print " bname   = ", bname
            #print " bvariable = ", bvariable
            self.otree.Branch(bname,bvariable,bname+'/F')

        # input tree and output tree
        itree     = self.itree
        otree     = self.otree
        
        if productionProcess == "GG":
          shiftfile = self.shiftfileGG
        elif productionProcess == "VBF":
          shiftfile = self.shiftfileVBF
        else:
          print "Unknown process", productionProcess
          return

        # only with the old JHU samples, which did not have proper decay weights for WW, we need to load the decay weights file.
        if "JHUGen698" in self.isNewJHU:
          print "This is new JHU, good for you."
          shiftfile = shiftfile.replace(".pkl", "_JHU698.pkl")
        else:
          print "This is old JHU, good for you."
        print "using the following shiftfile:", shiftfile
        if self.isNewJHU=="":
          with open (self.decayWeightsFile) as decayWeightsFile:
            allparams = pickle.load(decayWeightsFile)
            decayWeightFunction = interp1d(**allparams[str(int(self.mH))]["decayWeight"])
            minmass = min(allparams[str(int(self.mH))]["decayWeight"]['x'])
            maxmass = max(allparams[str(int(self.mH))]["decayWeight"]['x'])
            print "decay weights for mass", str(int(self.mH)), " available between", minmass, " and", maxmass 
        if shiftfile != "":
          with open (shiftfile) as shiftfile_stream:
            shifts = pickle.load(shiftfile_stream)
            #print shifts[str(int(self.mH))]



        # MELA reweighter
        mela = ROOT.MelaReweighterWW(13000, self.mH, self.gsm)
        #GF 1.16637e-5
        #sin2thetaW 0.22264585341299603
        #Wmass  = 80.398
        #ZMass = 91.1876
        mela.resetMCFM_EWKParameters(1.16637e-5, 1./128., 80.398, 91.1876, 0.22264585341299603)

        #----------------------------------------------------------------------------------------------------
        print '- Starting eventloop'
        step = 5000 

        for i in xrange(nentries):
        #for i in xrange(1):

            itree.GetEntry(i)

            if i > 0 and i%step == 0.:
                print i,'events processed :: ', nentries
            
            mass = itree.higgsLHEmass
            #mass = itree.higgsLHEMass
            fourMomenta=[]
            ids=[]
            partons   = ROOT.vector('TLorentzVector')()
            partonIDs = ROOT.vector('int')()

            for ilep in range(2):
              l = ROOT.TLorentzVector()
              l.SetPtEtaPhiM(itree.std_vector_LHElepton_pt[ilep], \
                             itree.std_vector_LHElepton_eta[ilep],
                             itree.std_vector_LHElepton_phi[ilep],
                             0.)
              fourMomenta.append(l)
              ids.append(itree.std_vector_LHElepton_id[ilep])
            for ilep in range(2):  
              n = ROOT.TLorentzVector()
              n.SetPtEtaPhiM(itree.std_vector_LHEneutrino_pt[ilep], \
                             itree.std_vector_LHEneutrino_eta[ilep],
                             itree.std_vector_LHEneutrino_phi[ilep],
                             0.)                
              fourMomenta.append(n)
              ids.append(itree.std_vector_LHEneutrino_id[ilep])

            #these are the incoming partons
            mothers = ROOT.vector('TLorentzVector')()
            motherIDs = ROOT.vector('int')()
            incoming1=ROOT.TLorentzVector()
            incoming1.SetPxPyPzE(0.,0., itree.pdfx1*6500, itree.pdfx1*6500)
            incoming2=ROOT.TLorentzVector()
            incoming2.SetPxPyPzE(0.,0.,-itree.pdfx2*6500, itree.pdfx2*6500)
            mothers.push_back(incoming1)
            mothers.push_back(incoming2)
            motherIDs.push_back(int(itree.pdfid1))
            motherIDs.push_back(int(itree.pdfid2))
           
            #print "incoming:"
            #print incoming1.Px(), incoming1.Py(), incoming1.Pz(), int(itree.pdfid1)
            #print incoming2.Px(), incoming2.Py(), incoming2.Pz(), int(itree.pdfid2)

            #print "outgoing:"
            for ijet in range(5):
              if itree.std_vector_LHEparton_pt[ijet] > 0.:
                parton = ROOT.TLorentzVector()
                parton.SetPtEtaPhiM(itree.std_vector_LHEparton_pt[ijet], \
                                    itree.std_vector_LHEparton_eta[ijet],
                                    itree.std_vector_LHEparton_phi[ijet],
                                    0.)
                partons.push_back(parton)                     
                partonIDs.push_back(int(itree.std_vector_LHEparton_id[ijet]))
                #print parton.Px(), parton.Py(), parton.Pz(), int(itree.std_vector_LHEparton_id[ijet])
      
            CPSweight = 1.
            if self.undoCPS:
              if "JHUGen698" in self.isNewJHU:
                # in this case the sample already has the correct decay weights for WW
                # we just need to undo the pure CPS part and restore the SM width
                CPSweight = self.FixedBreightWigner(mass, self.mH, self.gsmCPS)/self.FixedBreightWigner(mass, self.mH, self.gsm)
              else:
                # in this case the sample was done with BOTH CPS width and average decay weights, so we need to undo both
                # using the corresponding POWHEG-passarino code.
                CPSweight = ROOT.getCPSweight(self.mH, self.gsm, 172.5, mass, 0)
            shift = 1.
            # with the new JHU decay weights are alreay in the samplem, no need to apply them here
            if "JHUGen698" in self.isNewJHU:
              decayWeight = 1.
            # with old JHU samples we need to apply the decay weights  
            else:  
              if mass < minmass:
                decayWeight = decayWeightFunction(minmass)
              elif mass > maxmass:  
                decayWeight = decayWeightFunction(maxmass)
              else:   
                decayWeight = decayWeightFunction(mass)
            #print decayWeight    
            for cprime in rangecprime:
              for BRnew in rangeBRnew:
                name = 'cprime'+str(cprime)+"BRnew"+str(BRnew)
                kprime = cprime**2;
                #overallweight = kprime*(1-BRnew) 
                gprime = self.Gprime(self.mH, kprime, BRnew)
                if shiftfile != "":
                  shift = shifts[str(int(self.mH))]["cprime"+str(cprime)]["brnew"+str(BRnew)]["weight"]
                self.oldBranchesToBeModifiedSimpleVariable[name][0] = (1./shift)*decayWeight*self.FixedBreightWigner(mass, self.mH, gprime)/self.FixedBreightWigner(mass, self.mH, self.gsm)/CPSweight
                # tmp fix without interference calculation for VBF
                #if productionProcess=="VBF":
                #  continue
                mela.setMelaHiggsMassWidth(self.mH, gprime)
                mela.setupDaughters((productionProcess=="VBF"), int(ids[0]), int(ids[1]), int(ids[2]), int(ids[3]),
                                                                 fourMomenta[0], fourMomenta[1], fourMomenta[2], fourMomenta[3],
                                                                 partons, partonIDs,
                                                                 mothers, motherIDs)
                weightInterference = mela.weightStoI()
                weightInterferenceHonly = mela.weightStoI_H()
                weightInterferenceBonly = mela.weightStoI_B()
                weightInterferenceHB = mela.weightStoI_HB()
                weightBackground   = mela.weightStoB()
                weightSignalH   = mela.weightStoH()
                #dirty protection for occasional failures
                if math.isnan(weightInterference) or math.isinf(weightInterference):
                  weightInterference=0.
                if math.isnan(weightInterferenceHonly) or math.isinf(weightInterferenceHonly):
                  weightInterferenceHonly=0.
                if math.isnan(weightInterferenceBonly) or math.isinf(weightInterferenceBonly):
                  weightInterferenceBonly=0.
                if math.isnan(weightInterferenceHB) or math.isinf(weightInterferenceHB):
                  weightInterferenceHB=0.
                if math.isnan(weightBackground) or math.isinf(weightBackground):
                  weightBackground=0.
                if math.isnan(weightSignalH) or math.isinf(weightSignalH):
                  weightSignalH=0.     
                self.oldBranchesToBeModifiedSimpleVariable[name+"_I"][0] = self.oldBranchesToBeModifiedSimpleVariable[name][0]*weightInterference
                self.oldBranchesToBeModifiedSimpleVariable[name+"_I_Honly"][0] = self.oldBranchesToBeModifiedSimpleVariable[name][0]*weightInterferenceHonly
                self.oldBranchesToBeModifiedSimpleVariable[name+"_I_Bonly"][0] = self.oldBranchesToBeModifiedSimpleVariable[name][0]*weightInterferenceBonly
                self.oldBranchesToBeModifiedSimpleVariable[name+"_I_HB"][0] = self.oldBranchesToBeModifiedSimpleVariable[name][0]*weightInterferenceHB
                self.oldBranchesToBeModifiedSimpleVariable[name+"_B"][0] = self.oldBranchesToBeModifiedSimpleVariable[name][0]*weightBackground
                self.oldBranchesToBeModifiedSimpleVariable[name+"_H"][0] = self.oldBranchesToBeModifiedSimpleVariable[name][0]*weightSignalH
                #print weightInterference,weightInterferenceHonly,weightInterferenceBonly,weightInterferenceHB,weightBackground,weightSignalH


              
            otree.Fill()

        self.disconnect()
        print '- Eventloop completed'


