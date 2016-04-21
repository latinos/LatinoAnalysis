import optparse
import numpy
import ROOT
import os.path

from LatinoAnalysis.Gardener.gardening import TreeCloner

#from HWWAnalysis.ShapeAnalysis.triggerEffCombiner import TriggerEff

#___.    __                __________              _________                          ___________              __                       
#\_ |___/  |______     ____\______   \____   ____ /   _____/ ____ _____ _______   ____\_   _____/____    _____/  |_  ___________  ______
# | __ \   __\__  \   / ___\|     ___/  _ \ / ___\\_____  \_/ ___\\__  \\_  __ \_/ __ \|    __) \__  \ _/ ___\   __\/  _ \_  __ \/  ___/
# | \_\ \  |  / __ \_/ /_/  >    |  (  <_> ) /_/  >        \  \___ / __ \|  | \/\  ___/|     \   / __ \\  \___|  | (  <_> )  | \/\___ \ 
# |___  /__| (____  /\___  /|____|   \____/\___  /_______  /\___  >____  /__|    \___  >___  /  (____  /\___  >__|  \____/|__|  /____  >
#     \/          \//_____/               /_____/        \/     \/     \/            \/    \/        \/     \/                       \/ 
                                                                                                                                       
class allBtagPogScaleFactors(TreeCloner):

    def __init__(self):
        pass

    def __del__(self):
        pass

    def help(self):
        return '''Add a scale factor derived according to POG recommendations, method 1a in https://twiki.cern.ch/twiki/bin/view/CMS/BTagSFMethods#1a_Event_reweighting_using_scale'''

    def addOptions(self,parser):
        pass

    def checkOptions(self,opts):
        pass

    def _readSF (self):
        #ROOT.gSystem.Load('libCondFormatsBTagObjects') 
        cmssw_base = os.getenv('CMSSW_BASE')
        effFile = "data/efficiencyMCFile76X_all.py"

        efficienciesMC_CMVA = {}
        efficienciesMC_CSV = {}

        efffile_path = cmssw_base+'/src/LatinoAnalysis/Gardener/python/'+effFile

        if effFile == None :
          print " Please provide an input file with the MC efficiencies "

        elif os.path.exists(efffile_path) :
          handle = open(efffile_path,'r')
          exec(handle)
          handle.close()
        else:
          print "cannot find file", effFile

        self.efficiencyMC_CMVA = efficienciesMC_CMVA
        self.efficiencyMC_CSV = efficienciesMC_CSV

        self.minpt = 20
        self.maxpt = 290 
        
        self.mineta = 0
        self.maxeta = 2.4
        
        wpl = 0
        wpm = 1
        wpt = 2
        wps = 3

        #compile code to read scale factors

        self.cmvaSfFile = 'cMVAv2.csv'
        self.csvSfFile = 'CSVv2.csv'

        #ROOT.gROOT.ProcessLine(".L "+cmssw_base+'/src/LatinoAnalysis/Gardener/python/variables/BTagCalibrationStandalone.cc+')
        try:
            ROOT.gROOT.LoadMacro(cmssw_base+'/src/LatinoAnalysis/Gardener/python/variables/BTagCalibrationStandalone.cc+g')
        except RuntimeError:
            ROOT.gROOT.LoadMacro(cmssw_base+'/src/LatinoAnalysis/Gardener/python/variables/BTagCalibrationStandalone.cc++g')
        #ROOT.gROOT.ProcessLine('.L BTagCalibrationStandalone.cc+') 
        print "CMVA scale factors from", cmssw_base+'/src/LatinoAnalysis/Gardener/python/data/'+self.cmvaSfFile
        print "CSVv2 scale factors from", cmssw_base+'/src/LatinoAnalysis/Gardener/python/data/'+self.csvSfFile

        ### Readers for cMVAv2
        self.calibCMVA = ROOT.BTagCalibration("cMVAv2", cmssw_base+'/src/LatinoAnalysis/Gardener/python/data/'+self.cmvaSfFile)
        self.readerCentralCMVAL = ROOT.BTagCalibrationReader(self.calibCMVA, wpl, "ttbar", "central")
        self.readerUpCMVAL = ROOT.BTagCalibrationReader(self.calibCMVA, wpl, "ttbar", "up")  
        self.readerDownCMVAL = ROOT.BTagCalibrationReader(self.calibCMVA, wpl, "ttbar", "down")

        self.readerCentralCMVAM = ROOT.BTagCalibrationReader(self.calibCMVA, wpm, "ttbar", "central")
        self.readerUpCMVAM = ROOT.BTagCalibrationReader(self.calibCMVA, wpm, "ttbar", "up")
        self.readerDownCMVAM = ROOT.BTagCalibrationReader(self.calibCMVA, wpm, "ttbar", "down")

        self.readerCentralCMVAT = ROOT.BTagCalibrationReader(self.calibCMVA, wpt, "ttbar", "central")
        self.readerUpCMVAT = ROOT.BTagCalibrationReader(self.calibCMVA, wpt, "ttbar", "up")
        self.readerDownCMVAT = ROOT.BTagCalibrationReader(self.calibCMVA, wpt, "ttbar", "down")

        #it seems that so far light jet scale factors are only available in the incl dataset 
        #(light jets is the only thing available in that dataset)
        self.readerLightCentralCMVAL = ROOT.BTagCalibrationReader(self.calibCMVA, wpl, "incl", "central")  
        self.readerLightUpCMVAL = ROOT.BTagCalibrationReader(self.calibCMVA, wpl, "incl", "up")  
        self.readerLightDownCMVAL = ROOT.BTagCalibrationReader(self.calibCMVA, wpl, "incl", "down") 

        self.readerLightCentralCMVAM = ROOT.BTagCalibrationReader(self.calibCMVA, wpm, "incl", "central")
        self.readerLightUpCMVAM = ROOT.BTagCalibrationReader(self.calibCMVA, wpm, "incl", "up")
        self.readerLightDownCMVAM = ROOT.BTagCalibrationReader(self.calibCMVA, wpm, "incl", "down")

        self.readerLightCentralCMVAT = ROOT.BTagCalibrationReader(self.calibCMVA, wpt, "incl", "central")
        self.readerLightUpCMVAT = ROOT.BTagCalibrationReader(self.calibCMVA, wpt, "incl", "up")
        self.readerLightDownCMVAT = ROOT.BTagCalibrationReader(self.calibCMVA, wpt, "incl", "down")


        ### Readers for cMVAv2 re-shaping (1 nominal + 9 Up variations + 9 Down variations)
        self.readerCentralCMVAshape = ROOT.BTagCalibrationReader(self.calibCMVA, wps, "iterativefit", "central")
        self.readerCentralCMVAshape_up_jes = ROOT.BTagCalibrationReader(self.calibCMVA, wps, "iterativefit", "up_jes")
        self.readerCentralCMVAshape_down_jes = ROOT.BTagCalibrationReader(self.calibCMVA, wps, "iterativefit", "down_jes")
        self.readerCentralCMVAshape_up_lf = ROOT.BTagCalibrationReader(self.calibCMVA, wps, "iterativefit", "up_lf")
        self.readerCentralCMVAshape_down_lf = ROOT.BTagCalibrationReader(self.calibCMVA, wps, "iterativefit", "down_lf")
        self.readerCentralCMVAshape_up_hfstats1 = ROOT.BTagCalibrationReader(self.calibCMVA, wps, "iterativefit", "up_hfstats1")
        self.readerCentralCMVAshape_down_hfstats1 = ROOT.BTagCalibrationReader(self.calibCMVA, wps, "iterativefit", "down_hfstats1")
        self.readerCentralCMVAshape_up_hfstats2 = ROOT.BTagCalibrationReader(self.calibCMVA, wps, "iterativefit", "up_hfstats2")
        self.readerCentralCMVAshape_down_hfstats2 = ROOT.BTagCalibrationReader(self.calibCMVA, wps, "iterativefit", "down_hfstats2")
        self.readerCentralCMVAshape_up_cferr1 = ROOT.BTagCalibrationReader(self.calibCMVA, wps, "iterativefit", "up_cferr1")
        self.readerCentralCMVAshape_down_cferr1 = ROOT.BTagCalibrationReader(self.calibCMVA, wps, "iterativefit", "down_cferr1")
        self.readerCentralCMVAshape_up_cferr2 = ROOT.BTagCalibrationReader(self.calibCMVA, wps, "iterativefit", "up_cferr2")
        self.readerCentralCMVAshape_down_cferr2 = ROOT.BTagCalibrationReader(self.calibCMVA, wps, "iterativefit", "down_cferr2")
        self.readerCentralCMVAshape_up_hf = ROOT.BTagCalibrationReader(self.calibCMVA, wps, "iterativefit", "up_hf")
        self.readerCentralCMVAshape_down_hf = ROOT.BTagCalibrationReader(self.calibCMVA, wps, "iterativefit", "down_hf")
        self.readerCentralCMVAshape_up_lfstats1 = ROOT.BTagCalibrationReader(self.calibCMVA, wps, "iterativefit", "up_lfstats1")
        self.readerCentralCMVAshape_down_lfstats1 = ROOT.BTagCalibrationReader(self.calibCMVA, wps, "iterativefit", "down_lfstats1")
        self.readerCentralCMVAshape_up_lfstats2 = ROOT.BTagCalibrationReader(self.calibCMVA, wps, "iterativefit", "up_lfstats2")
        self.readerCentralCMVAshape_down_lfstats2 = ROOT.BTagCalibrationReader(self.calibCMVA, wps, "iterativefit", "down_lfstats2")




        ### Readers for CSVv2
        self.calibCSV = ROOT.BTagCalibration("CSVv2", cmssw_base+'/src/LatinoAnalysis/Gardener/python/data/'+self.csvSfFile)
        self.readerCentralCSVL = ROOT.BTagCalibrationReader(self.calibCSV, wpl, "mujets", "central")
        self.readerUpCSVL = ROOT.BTagCalibrationReader(self.calibCSV, wpl, "mujets", "up")
        self.readerDownCSVL = ROOT.BTagCalibrationReader(self.calibCSV, wpl, "mujets", "down")

        self.readerCentralCSVM = ROOT.BTagCalibrationReader(self.calibCSV, wpm, "mujets", "central")
        self.readerUpCSVM = ROOT.BTagCalibrationReader(self.calibCSV, wpm, "mujets", "up")
        self.readerDownCSVM = ROOT.BTagCalibrationReader(self.calibCSV, wpm, "mujets", "down")

        self.readerCentralCSVT = ROOT.BTagCalibrationReader(self.calibCSV, wpt, "mujets", "central")
        self.readerUpCSVT = ROOT.BTagCalibrationReader(self.calibCSV, wpt, "mujets", "up")
        self.readerDownCSVT = ROOT.BTagCalibrationReader(self.calibCSV, wpt, "mujets", "down")

        #it seems that so far light jet scale factors are only available in the incl dataset 
        #(light jets is the only thing available in that dataset)
        self.readerLightCentralCSVL = ROOT.BTagCalibrationReader(self.calibCSV, wpl, "incl", "central")
        self.readerLightUpCSVL = ROOT.BTagCalibrationReader(self.calibCSV, wpl, "incl", "up")
        self.readerLightDownCSVL = ROOT.BTagCalibrationReader(self.calibCSV, wpl, "incl", "down")

        self.readerLightCentralCSVM = ROOT.BTagCalibrationReader(self.calibCSV, wpm, "incl", "central")
        self.readerLightUpCSVM = ROOT.BTagCalibrationReader(self.calibCSV, wpm, "incl", "up")
        self.readerLightDownCSVM = ROOT.BTagCalibrationReader(self.calibCSV, wpm, "incl", "down")

        self.readerLightCentralCSVT = ROOT.BTagCalibrationReader(self.calibCSV, wpt, "incl", "central")
        self.readerLightUpCSVT = ROOT.BTagCalibrationReader(self.calibCSV, wpt, "incl", "up")
        self.readerLightDownCSVT = ROOT.BTagCalibrationReader(self.calibCSV, wpt, "incl", "down")

        ### Readers for CSVv2 re-shaping (1 nominal + 9 Up variations + 9 Down variations)
        self.readerCentralCSVshape = ROOT.BTagCalibrationReader(self.calibCSV, wps, "iterativefit", "central")
        self.readerCentralCSVshape_up_jes = ROOT.BTagCalibrationReader(self.calibCSV, wps, "iterativefit", "up_jes")
        self.readerCentralCSVshape_down_jes = ROOT.BTagCalibrationReader(self.calibCSV, wps, "iterativefit", "down_jes")
        self.readerCentralCSVshape_up_lf = ROOT.BTagCalibrationReader(self.calibCSV, wps, "iterativefit", "up_lf")
        self.readerCentralCSVshape_down_lf = ROOT.BTagCalibrationReader(self.calibCSV, wps, "iterativefit", "down_lf")
        self.readerCentralCSVshape_up_hfstats1 = ROOT.BTagCalibrationReader(self.calibCSV, wps, "iterativefit", "up_hfstats1")
        self.readerCentralCSVshape_down_hfstats1 = ROOT.BTagCalibrationReader(self.calibCSV, wps, "iterativefit", "down_hfstats1")
        self.readerCentralCSVshape_up_hfstats2 = ROOT.BTagCalibrationReader(self.calibCSV, wps, "iterativefit", "up_hfstats2")
        self.readerCentralCSVshape_down_hfstats2 = ROOT.BTagCalibrationReader(self.calibCSV, wps, "iterativefit", "down_hfstats2")
        self.readerCentralCSVshape_up_cferr1 = ROOT.BTagCalibrationReader(self.calibCSV, wps, "iterativefit", "up_cferr1")
        self.readerCentralCSVshape_down_cferr1 = ROOT.BTagCalibrationReader(self.calibCSV, wps, "iterativefit", "down_cferr1")
        self.readerCentralCSVshape_up_cferr2 = ROOT.BTagCalibrationReader(self.calibCSV, wps, "iterativefit", "up_cferr2")
        self.readerCentralCSVshape_down_cferr2 = ROOT.BTagCalibrationReader(self.calibCSV, wps, "iterativefit", "down_cferr2")
        self.readerCentralCSVshape_up_hf = ROOT.BTagCalibrationReader(self.calibCSV, wps, "iterativefit", "up_hf")
        self.readerCentralCSVshape_down_hf = ROOT.BTagCalibrationReader(self.calibCSV, wps, "iterativefit", "down_hf")
        self.readerCentralCSVshape_up_lfstats1 = ROOT.BTagCalibrationReader(self.calibCSV, wps, "iterativefit", "up_lfstats1")
        self.readerCentralCSVshape_down_lfstats1 = ROOT.BTagCalibrationReader(self.calibCSV, wps, "iterativefit", "down_lfstats1")
        self.readerCentralCSVshape_up_lfstats2 = ROOT.BTagCalibrationReader(self.calibCSV, wps, "iterativefit", "up_lfstats2")
        self.readerCentralCSVshape_down_lfstats2 = ROOT.BTagCalibrationReader(self.calibCSV, wps, "iterativefit", "down_lfstats2")



    def _getEffMC (self, algo, wp, kindJet, pt, eta):

        # fix underflow and overflow
        if pt < self.minpt:
          pt = self.minpt
        if pt > self.maxpt:
          pt = self.maxpt
        
        if eta < self.mineta:
          eta = self.mineta
        if eta > self.maxeta:
          eta = self.maxeta

        if not (wp=='L' or wp=='M' or wp=='T'):
          print "ERROR: wp ", wp, " do not exist or the format is wrong. Please provide a correct wp." 
          print "Available wps are 'L', 'M' or 'T'."

        if algo == "CMVA":
          if (kindJet,wp) in self.efficiencyMC_CMVA.keys() : 
            # get the efficiency
            for point in self.efficiencyMC_CMVA[(kindJet,wp)] : 
              #   pt           eta          eff 
              # (( 0.0, 10.0), (0.0, 1.5), 0.980 ),
              if ( pt  >= point[0][0] and pt  < point[0][1] and
                   eta >= point[1][0] and eta < point[1][1] ) :
                  return point[2]

            # default ... it should never happen!
            print " default ???", pt, eta, kindJet
            return 1.0

        elif algo == "CSV":
          if (kindJet,wp) in self.efficiencyMC_CSV.keys() :
            # get the efficiency
            for point in self.efficiencyMC_CSV[(kindJet,wp)] :
              #   pt           eta          eff 
              # (( 0.0, 10.0), (0.0, 1.5), 0.980 ),
              if ( pt  >= point[0][0] and pt  < point[0][1] and
                   eta >= point[1][0] and eta < point[1][1] ) :
                  #print "kindJet, wp = ", kindJet, " ", wp
                  #print "pt, eta, SF = ", pt, " ", eta, " ", point[2]
                  return point[2]

            # default ... it should never happen!
            print " default ???", pt, eta, kindJet
            return 1.0
        else: 
          print "ERROR: algo ", algo, " is not available. Please specify a correct algo."  
          print "Available algos are 'CMVA' and 'CSV'."

        # not a lepton ... like some default value
        return 1.0


    def process(self,**kwargs):
        tree  = kwargs['tree']
        input = kwargs['input']
        output = kwargs['output']

        self.connect(tree,input)

        self._readSF()        
  
        self.clone(output,["bPogSF", "bPogSFUp", "bPogSFDown",
			   "bPogSF_CMVAL", "bPogSF_CMVAL_Up", "bPogSF_CMVAL_Down",
                           "bPogSF_CMVAM", "bPogSF_CMVAM_Up", "bPogSF_CMVAM_Down",
                           "bPogSF_CMVAT", "bPogSF_CMVAT_Up", "bPogSF_CMVAT_Down",
                           "bPogSF_CSVL", "bPogSF_CSVL_Up", "bPogSF_CSVL_Down",
                           "bPogSF_CSVM", "bPogSF_CSVM_Up", "bPogSF_CSVM_Down",
                           "bPogSF_CSVT", "bPogSF_CSVT_Up", "bPogSF_CSVT_Down",
                           "bPogSF_CMVAreshape", 
			   "bPogSF_CMVAreshape_up_jes", "bPogSF_CMVAreshape_down_jes",
                           "bPogSF_CMVAreshape_up_lf", "bPogSF_CMVAreshape_down_lf",
                           "bPogSF_CMVAreshape_up_hf", "bPogSF_CMVAreshape_down_hf",
                           "bPogSF_CMVAreshape_up_hfstats1", "bPogSF_CMVAreshape_down_hfstats1",
                           "bPogSF_CMVAreshape_up_hfstats2", "bPogSF_CMVAreshape_down_hfstats2",
                           "bPogSF_CMVAreshape_up_lfstats1", "bPogSF_CMVAreshape_down_lfstats1",
                           "bPogSF_CMVAreshape_up_lfstats2", "bPogSF_CMVAreshape_down_lfstats2",
                           "bPogSF_CMVAreshape_up_cferr1", "bPogSF_CMVAreshape_down_cferr1",
                           "bPogSF_CMVAreshape_up_cferr2", "bPogSF_CMVAreshape_down_cferr2",
                           "bPogSF_CSVreshape",
                           "bPogSF_CSVreshape_up_jes", "bPogSF_CSVreshape_down_jes",
                           "bPogSF_CSVreshape_up_lf", "bPogSF_CSVreshape_down_lf",
                           "bPogSF_CSVreshape_up_hf", "bPogSF_CSVreshape_down_hf",
                           "bPogSF_CSVreshape_up_hfstats1", "bPogSF_CSVreshape_down_hfstats1",
                           "bPogSF_CSVreshape_up_hfstats2", "bPogSF_CSVreshape_down_hfstats2",
                           "bPogSF_CSVreshape_up_lfstats1", "bPogSF_CSVreshape_down_lfstats1",
                           "bPogSF_CSVreshape_up_lfstats2", "bPogSF_CSVreshape_down_lfstats2",
                           "bPogSF_CSVreshape_up_cferr1", "bPogSF_CSVreshape_down_cferr1",
                           "bPogSF_CSVreshape_up_cferr2", "bPogSF_CSVreshape_down_cferr2",

			  ])


        #bPogSF and similar are SF from bPOG

        bPogSF = numpy.ones(1, dtype=numpy.float32)
        self.otree.Branch('bPogSF',bPogSF,'bPogSF/F')
        bPogSFUp = numpy.ones(1, dtype=numpy.float32)
        self.otree.Branch('bPogSFUp',bPogSFUp,'bPogSFUp/F') 
        bPogSFDown = numpy.ones(1, dtype=numpy.float32)
        self.otree.Branch('bPogSFDown',bPogSFDown,'bPogSFDown/F')

        #bPogSF and similar are SF from bPOG

        bPogSF_CMVAL = numpy.ones(1, dtype=numpy.float32)
        self.otree.Branch('bPogSF_CMVAL',bPogSF_CMVAL,'bPogSF_CMVAL/F')
        bPogSF_CMVAL_Up = numpy.ones(1, dtype=numpy.float32)
        self.otree.Branch('bPogSF_CMVAL_Up',bPogSF_CMVAL_Up,'bPogSF_CMVAL_Up/F') 
        bPogSF_CMVAL_Down = numpy.ones(1, dtype=numpy.float32)
        self.otree.Branch('bPogSF_CMVAL_Down',bPogSF_CMVAL_Down,'bPogSF_CMVAL_Down/F')

        #bPogSF and similar are SF from bPOG

        bPogSF_CMVAM = numpy.ones(1, dtype=numpy.float32)
        self.otree.Branch('bPogSF_CMVAM',bPogSF_CMVAM,'bPogSF_CMVAM/F')
        bPogSF_CMVAM_Up = numpy.ones(1, dtype=numpy.float32)
        self.otree.Branch('bPogSF_CMVAM_Up',bPogSF_CMVAM_Up,'bPogSF_CMVAM_Up/F') 
        bPogSF_CMVAM_Down = numpy.ones(1, dtype=numpy.float32)
        self.otree.Branch('bPogSF_CMVAM_Down',bPogSF_CMVAM_Down,'bPogSF_CMVAM_Down/F')

        #bPogSF and similar are SF from bPOG

        bPogSF_CMVAT = numpy.ones(1, dtype=numpy.float32)
        self.otree.Branch('bPogSF_CMVAT',bPogSF_CMVAT,'bPogSF_CMVAT/F')
        bPogSF_CMVAT_Up = numpy.ones(1, dtype=numpy.float32)
        self.otree.Branch('bPogSF_CMVAT_Up',bPogSF_CMVAT_Up,'bPogSF_CMVAT_Up/F') 
        bPogSF_CMVAT_Down = numpy.ones(1, dtype=numpy.float32)
        self.otree.Branch('bPogSF_CMVAT_Down',bPogSF_CMVAT_Down,'bPogSF_CMVAT_Down/F')


        # Re-shaping weights for cMVAv2
      
        bPogSF_CMVAreshape = numpy.ones(1, dtype=numpy.float32)
        self.otree.Branch('bPogSF_CMVAreshape',bPogSF_CMVAreshape,'bPogSF_CMVAreshape/F')
        bPogSF_CMVAreshape_up_jes = numpy.ones(1, dtype=numpy.float32)
        self.otree.Branch('bPogSF_CMVAreshape_up_jes',bPogSF_CMVAreshape_up_jes,'bPogSF_CMVAreshape_up_jes/F')
        bPogSF_CMVAreshape_down_jes = numpy.ones(1, dtype=numpy.float32)
        self.otree.Branch('bPogSF_CMVAreshape_down_jes',bPogSF_CMVAreshape_down_jes,'bPogSF_CMVAreshape_down_jes/F')
        bPogSF_CMVAreshape_up_lf = numpy.ones(1, dtype=numpy.float32)
        self.otree.Branch('bPogSF_CMVAreshape_up_lf',bPogSF_CMVAreshape_up_lf,'bPogSF_CMVAreshape_up_lf/F')
        bPogSF_CMVAreshape_down_lf = numpy.ones(1, dtype=numpy.float32)
        self.otree.Branch('bPogSF_CMVAreshape_down_lf',bPogSF_CMVAreshape_down_lf,'bPogSF_CMVAreshape_down_lf/F')
        bPogSF_CMVAreshape_up_hf = numpy.ones(1, dtype=numpy.float32)
        self.otree.Branch('bPogSF_CMVAreshape_up_hf',bPogSF_CMVAreshape_up_hf,'bPogSF_CMVAreshape_up_hf/F')
        bPogSF_CMVAreshape_down_hf = numpy.ones(1, dtype=numpy.float32)
        self.otree.Branch('bPogSF_CMVAreshape_down_hf',bPogSF_CMVAreshape_down_hf,'bPogSF_CMVAreshape_down_hf/F')
        bPogSF_CMVAreshape_up_hfstats1 = numpy.ones(1, dtype=numpy.float32)
        self.otree.Branch('bPogSF_CMVAreshape_up_hfstats1',bPogSF_CMVAreshape_up_hfstats1,'bPogSF_CMVAreshape_up_hfstats1/F')
        bPogSF_CMVAreshape_down_hfstats1 = numpy.ones(1, dtype=numpy.float32)
        self.otree.Branch('bPogSF_CMVAreshape_down_hfstats1',bPogSF_CMVAreshape_down_hfstats1,'bPogSF_CMVAreshape_down_hfstats1/F')
        bPogSF_CMVAreshape_up_hfstats2 = numpy.ones(1, dtype=numpy.float32)
        self.otree.Branch('bPogSF_CMVAreshape_up_hfstats2',bPogSF_CMVAreshape_up_hfstats2,'bPogSF_CMVAreshape_up_hfstats2/F')
        bPogSF_CMVAreshape_down_hfstats2 = numpy.ones(1, dtype=numpy.float32)
        self.otree.Branch('bPogSF_CMVAreshape_down_hfstats2',bPogSF_CMVAreshape_down_hfstats2,'bPogSF_CMVAreshape_down_hfstats2/F')
        bPogSF_CMVAreshape_up_lfstats1 = numpy.ones(1, dtype=numpy.float32)
        self.otree.Branch('bPogSF_CMVAreshape_up_lfstats1',bPogSF_CMVAreshape_up_lfstats1,'bPogSF_CMVAreshape_up_lfstats1/F')
        bPogSF_CMVAreshape_down_lfstats1 = numpy.ones(1, dtype=numpy.float32)
        self.otree.Branch('bPogSF_CMVAreshape_down_lfstats1',bPogSF_CMVAreshape_down_lfstats1,'bPogSF_CMVAreshape_down_lfstats1/F')
        bPogSF_CMVAreshape_up_lfstats2 = numpy.ones(1, dtype=numpy.float32)
        self.otree.Branch('bPogSF_CMVAreshape_up_lfstats2',bPogSF_CMVAreshape_up_lfstats2,'bPogSF_CMVAreshape_up_lfstats2/F')
        bPogSF_CMVAreshape_down_lfstats2 = numpy.ones(1, dtype=numpy.float32)
        self.otree.Branch('bPogSF_CMVAreshape_down_lfstats2',bPogSF_CMVAreshape_down_lfstats2,'bPogSF_CMVAreshape_down_lfstats2/F')
        bPogSF_CMVAreshape_up_cferr1 = numpy.ones(1, dtype=numpy.float32)
        self.otree.Branch('bPogSF_CMVAreshape_up_cferr1',bPogSF_CMVAreshape_up_cferr1,'bPogSF_CMVAreshape_up_cferr1/F')
        bPogSF_CMVAreshape_down_cferr1 = numpy.ones(1, dtype=numpy.float32)
        self.otree.Branch('bPogSF_CMVAreshape_down_cferr1',bPogSF_CMVAreshape_down_cferr1,'bPogSF_CMVAreshape_down_cferr1/F')
        bPogSF_CMVAreshape_up_cferr2 = numpy.ones(1, dtype=numpy.float32)
        self.otree.Branch('bPogSF_CMVAreshape_up_cferr2',bPogSF_CMVAreshape_up_cferr2,'bPogSF_CMVAreshape_up_cferr2/F')
        bPogSF_CMVAreshape_down_cferr2 = numpy.ones(1, dtype=numpy.float32)
        self.otree.Branch('bPogSF_CMVAreshape_down_cferr2',bPogSF_CMVAreshape_down_cferr2,'bPogSF_CMVAreshape_down_cferr2/F')




        bPogSF_CSVL = numpy.ones(1, dtype=numpy.float32)
        self.otree.Branch('bPogSF_CSVL',bPogSF_CSVL,'bPogSF_CSVL/F')
        bPogSF_CSVL_Up = numpy.ones(1, dtype=numpy.float32)
        self.otree.Branch('bPogSF_CSVL_Up',bPogSF_CSVL_Up,'bPogSF_CSVL_Up/F')
        bPogSF_CSVL_Down = numpy.ones(1, dtype=numpy.float32)
        self.otree.Branch('bPogSF_CSVL_Down',bPogSF_CSVL_Down,'bPogSF_CSVL_Down/F')

        #bPogSF and similar are SF from bPOG

        bPogSF_CSVM = numpy.ones(1, dtype=numpy.float32)
        self.otree.Branch('bPogSF_CSVM',bPogSF_CSVM,'bPogSF_CSVM/F')
        bPogSF_CSVM_Up = numpy.ones(1, dtype=numpy.float32)
        self.otree.Branch('bPogSF_CSVM_Up',bPogSF_CSVM_Up,'bPogSF_CSVM_Up/F')
        bPogSF_CSVM_Down = numpy.ones(1, dtype=numpy.float32)
        self.otree.Branch('bPogSF_CSVM_Down',bPogSF_CSVM_Down,'bPogSF_CSVM_Down/F')

        #bPogSF and similar are SF from bPOG

        bPogSF_CSVT = numpy.ones(1, dtype=numpy.float32)
        self.otree.Branch('bPogSF_CSVT',bPogSF_CSVT,'bPogSF_CSVT/F')
        bPogSF_CSVT_Up = numpy.ones(1, dtype=numpy.float32)
        self.otree.Branch('bPogSF_CSVT_Up',bPogSF_CSVT_Up,'bPogSF_CSVT_Up/F')
        bPogSF_CSVT_Down = numpy.ones(1, dtype=numpy.float32)
        self.otree.Branch('bPogSF_CSVT_Down',bPogSF_CSVT_Down,'bPogSF_CSVT_Down/F')


        # Re-shaping weights for CSVv2

        bPogSF_CSVreshape = numpy.ones(1, dtype=numpy.float32)
        self.otree.Branch('bPogSF_CSVreshape',bPogSF_CSVreshape,'bPogSF_CSVreshape/F')
        bPogSF_CSVreshape_up_jes = numpy.ones(1, dtype=numpy.float32)
        self.otree.Branch('bPogSF_CSVreshape_up_jes',bPogSF_CSVreshape_up_jes,'bPogSF_CSVreshape_up_jes/F')
        bPogSF_CSVreshape_down_jes = numpy.ones(1, dtype=numpy.float32)
        self.otree.Branch('bPogSF_CSVreshape_down_jes',bPogSF_CSVreshape_down_jes,'bPogSF_CSVreshape_down_jes/F')
        bPogSF_CSVreshape_up_lf = numpy.ones(1, dtype=numpy.float32)
        self.otree.Branch('bPogSF_CSVreshape_up_lf',bPogSF_CSVreshape_up_lf,'bPogSF_CSVreshape_up_lf/F')
        bPogSF_CSVreshape_down_lf = numpy.ones(1, dtype=numpy.float32)
        self.otree.Branch('bPogSF_CSVreshape_down_lf',bPogSF_CSVreshape_down_lf,'bPogSF_CSVreshape_down_lf/F')
        bPogSF_CSVreshape_up_hf = numpy.ones(1, dtype=numpy.float32)
        self.otree.Branch('bPogSF_CSVreshape_up_hf',bPogSF_CSVreshape_up_hf,'bPogSF_CSVreshape_up_hf/F')
        bPogSF_CSVreshape_down_hf = numpy.ones(1, dtype=numpy.float32)
        self.otree.Branch('bPogSF_CSVreshape_down_hf',bPogSF_CSVreshape_down_hf,'bPogSF_CSVreshape_down_hf/F')
        bPogSF_CSVreshape_up_hfstats1 = numpy.ones(1, dtype=numpy.float32)
        self.otree.Branch('bPogSF_CSVreshape_up_hfstats1',bPogSF_CSVreshape_up_hfstats1,'bPogSF_CSVreshape_up_hfstats1/F')
        bPogSF_CSVreshape_down_hfstats1 = numpy.ones(1, dtype=numpy.float32)
        self.otree.Branch('bPogSF_CSVreshape_down_hfstats1',bPogSF_CSVreshape_down_hfstats1,'bPogSF_CSVreshape_down_hfstats1/F')
        bPogSF_CSVreshape_up_hfstats2 = numpy.ones(1, dtype=numpy.float32)
        self.otree.Branch('bPogSF_CSVreshape_up_hfstats2',bPogSF_CSVreshape_up_hfstats2,'bPogSF_CSVreshape_up_hfstats2/F')
        bPogSF_CSVreshape_down_hfstats2 = numpy.ones(1, dtype=numpy.float32)
        self.otree.Branch('bPogSF_CSVreshape_down_hfstats2',bPogSF_CSVreshape_down_hfstats2,'bPogSF_CSVreshape_down_hfstats2/F')
        bPogSF_CSVreshape_up_lfstats1 = numpy.ones(1, dtype=numpy.float32)
        self.otree.Branch('bPogSF_CSVreshape_up_lfstats1',bPogSF_CSVreshape_up_lfstats1,'bPogSF_CSVreshape_up_lfstats1/F')
        bPogSF_CSVreshape_down_lfstats1 = numpy.ones(1, dtype=numpy.float32)
        self.otree.Branch('bPogSF_CSVreshape_down_lfstats1',bPogSF_CSVreshape_down_lfstats1,'bPogSF_CSVreshape_down_lfstats1/F')
        bPogSF_CSVreshape_up_lfstats2 = numpy.ones(1, dtype=numpy.float32)
        self.otree.Branch('bPogSF_CSVreshape_up_lfstats2',bPogSF_CSVreshape_up_lfstats2,'bPogSF_CSVreshape_up_lfstats2/F')
        bPogSF_CSVreshape_down_lfstats2 = numpy.ones(1, dtype=numpy.float32)
        self.otree.Branch('bPogSF_CSVreshape_down_lfstats2',bPogSF_CSVreshape_down_lfstats2,'bPogSF_CSVreshape_down_lfstats2/F')
        bPogSF_CSVreshape_up_cferr1 = numpy.ones(1, dtype=numpy.float32)
        self.otree.Branch('bPogSF_CSVreshape_up_cferr1',bPogSF_CSVreshape_up_cferr1,'bPogSF_CSVreshape_up_cferr1/F')
        bPogSF_CSVreshape_down_cferr1 = numpy.ones(1, dtype=numpy.float32)
        self.otree.Branch('bPogSF_CSVreshape_down_cferr1',bPogSF_CSVreshape_down_cferr1,'bPogSF_CSVreshape_down_cferr1/F')
        bPogSF_CSVreshape_up_cferr2 = numpy.ones(1, dtype=numpy.float32)
        self.otree.Branch('bPogSF_CSVreshape_up_cferr2',bPogSF_CSVreshape_up_cferr2,'bPogSF_CSVreshape_up_cferr2/F')
        bPogSF_CSVreshape_down_cferr2 = numpy.ones(1, dtype=numpy.float32)
        self.otree.Branch('bPogSF_CSVreshape_down_cferr2',bPogSF_CSVreshape_down_cferr2,'bPogSF_CSVreshape_down_cferr2/F')



        nentries = self.itree.GetEntries()
        print 'Total number of entries: ',nentries 
                
        # avoid dots to go faster
        itree     = self.itree
        otree     = self.otree

        print '- Starting eventloop'
        step = 5000
        for i in xrange(nentries):
            itree.GetEntry(i)
            ## print event count
            if i > 0 and i%step == 0.:
              print i,'events processed.'


            pData_CMVAL         = 1.
            pDataUp_CMVAL       = 1.
            pDataDown_CMVAL     = 1.

            pMC_CMVAL           = 1.

            pData_CMVAM         = 1.
            pDataUp_CMVAM       = 1.
            pDataDown_CMVAM     = 1.

            pMC_CMVAM           = 1.

            pData_CMVAT         = 1.
            pDataUp_CMVAT       = 1.
            pDataDown_CMVAT     = 1.

            pMC_CMVAT           = 1.



            pData_CSVL         = 1.
            pDataUp_CSVL       = 1.
            pDataDown_CSVL     = 1.

            pMC_CSVL           = 1.

            pData_CSVM         = 1.
            pDataUp_CSVM       = 1.
            pDataDown_CSVM     = 1.

            pMC_CSVM           = 1.

            pData_CSVT         = 1.
            pDataUp_CSVT       = 1.
            pDataDown_CSVT     = 1.

            pMC_CSVT           = 1.

            
            bPogSF_CMVAreshape[0]        = 1.
            bPogSF_CMVAreshape_up_jes[0] = 1.
            bPogSF_CMVAreshape_down_jes[0] = 1.
            bPogSF_CMVAreshape_up_lf[0] = 1.
            bPogSF_CMVAreshape_down_lf[0] = 1.
            bPogSF_CMVAreshape_up_hf[0] = 1.
            bPogSF_CMVAreshape_down_hf[0] = 1.
            bPogSF_CMVAreshape_up_hfstats1[0] = 1.
            bPogSF_CMVAreshape_down_hfstats1[0] = 1.
            bPogSF_CMVAreshape_up_hfstats2[0] = 1.
            bPogSF_CMVAreshape_down_hfstats2[0] = 1.
            bPogSF_CMVAreshape_up_lfstats1[0] = 1.
            bPogSF_CMVAreshape_down_lfstats1[0] = 1.
            bPogSF_CMVAreshape_up_lfstats2[0] = 1.
            bPogSF_CMVAreshape_down_lfstats2[0] = 1.
            bPogSF_CMVAreshape_up_cferr1[0] = 1.
            bPogSF_CMVAreshape_down_cferr1[0] = 1.
            bPogSF_CMVAreshape_up_cferr2[0] = 1.
            bPogSF_CMVAreshape_down_cferr2[0] = 1.

            bPogSF_CSVreshape[0]        = 1.
            bPogSF_CSVreshape_up_jes[0] = 1.
            bPogSF_CSVreshape_down_jes[0] = 1.
            bPogSF_CSVreshape_up_lf[0] = 1.
            bPogSF_CSVreshape_down_lf[0] = 1.
            bPogSF_CSVreshape_up_hf[0] = 1.
            bPogSF_CSVreshape_down_hf[0] = 1.
            bPogSF_CSVreshape_up_hfstats1[0] = 1.
            bPogSF_CSVreshape_down_hfstats1[0] = 1.
            bPogSF_CSVreshape_up_hfstats2[0] = 1.
            bPogSF_CSVreshape_down_hfstats2[0] = 1.
            bPogSF_CSVreshape_up_lfstats1[0] = 1.
            bPogSF_CSVreshape_down_lfstats1[0] = 1.
            bPogSF_CSVreshape_up_lfstats2[0] = 1.
            bPogSF_CSVreshape_down_lfstats2[0] = 1.
            bPogSF_CSVreshape_up_cferr1[0] = 1.
            bPogSF_CSVreshape_down_cferr1[0] = 1.
            bPogSF_CSVreshape_up_cferr2[0] = 1.
            bPogSF_CSVreshape_down_cferr2[0] = 1.



            njet 	  = 0

            for iJet in xrange(len(itree.std_vector_jet_pt)) :
             
              pt      = itree.std_vector_jet_pt [iJet]
              eta     = itree.std_vector_jet_eta [iJet]
              flavour = itree.std_vector_jet_HadronFlavour [iJet]
              cmva    = itree.std_vector_jet_cmvav2 [iJet]
              csv    = itree.std_vector_jet_csvv2ivf [iJet]
              tagged_CMVAL  = itree.std_vector_jet_cmvav2 [iJet] > -0.715
              tagged_CMVAM  = itree.std_vector_jet_cmvav2 [iJet] > 0.185
              tagged_CMVAT  = itree.std_vector_jet_cmvav2 [iJet] > 0.875
              tagged_CSVL  = itree.std_vector_jet_csvv2ivf [iJet] > 0.460
              tagged_CSVM  = itree.std_vector_jet_csvv2ivf [iJet] > 0.800
              tagged_CSVT  = itree.std_vector_jet_csvv2ivf [iJet] > 0.935
              
             
              if pt > self.minpt and abs(eta) < self.maxeta:

                kindJet = 'b' # ele or mu
                idJet = 0
                if abs (flavour) == 4 : 
                  kindJet = 'c'
                  idJet = 1
                elif abs (flavour) == 0 :
                  kindJet = 'l'
                  idJet = 2
                elif flavour == 5:
                  kindJet = 'b'
                  idJet = 0
                else:
                  print "BIG PROBLEM! Hadron Flavor is neither 0, 4 or 5"
                #print "pt, eta, idJet, kindJet", pt, eta, idJet, kindJet 
                #print "~~~~~~~~~~~~~~~~ jet ", njet

                sfCMVAshape = self.readerCentralCMVAshape.evaluate(idJet, eta, pt, cmva)
                bPogSF_CMVAreshape[0] *= sfCMVAshape
                #print "CMVA : idJet = ", idJet, " pt = ", pt, " eta = ", eta, " cmva = ", cmva, " SF = ", sfCMVAshape, " weight = ", bPogSF_CMVAreshape[0]

                sfCMVAshape_up_jes = self.readerCentralCMVAshape_up_jes.evaluate(idJet, eta, pt, cmva)
                bPogSF_CMVAreshape_up_jes[0] *= sfCMVAshape_up_jes
                sfCMVAshape_down_jes = self.readerCentralCMVAshape_down_jes.evaluate(idJet, eta, pt, cmva)
                bPogSF_CMVAreshape_down_jes[0] *= sfCMVAshape_down_jes

                #print "CMVA JES UP: idJet = ", idJet, " pt = ", pt, " eta = ", eta, " cmva = ", cmva, " SF = ", sfCMVAshape_up_jes, " weight = ", bPogSF_CMVAreshape_up_jes[0]

                sfCMVAshape_up_lf = self.readerCentralCMVAshape_up_lf.evaluate(idJet, eta, pt, cmva)
                bPogSF_CMVAreshape_up_lf[0] *= sfCMVAshape_up_lf
                sfCMVAshape_down_lf = self.readerCentralCMVAshape_down_lf.evaluate(idJet, eta, pt, cmva)
                bPogSF_CMVAreshape_down_lf[0] *= sfCMVAshape_down_lf

                sfCMVAshape_up_hf = self.readerCentralCMVAshape_up_hf.evaluate(idJet, eta, pt, cmva)
                bPogSF_CMVAreshape_up_hf[0] *= sfCMVAshape_up_hf
                sfCMVAshape_down_hf = self.readerCentralCMVAshape_down_hf.evaluate(idJet, eta, pt, cmva)
                bPogSF_CMVAreshape_down_hf[0] *= sfCMVAshape_down_hf

                sfCMVAshape_up_hfstats1 = self.readerCentralCMVAshape_up_hfstats1.evaluate(idJet, eta, pt, cmva)
                bPogSF_CMVAreshape_up_hfstats1[0] *= sfCMVAshape_up_hfstats1
                sfCMVAshape_down_hfstats1 = self.readerCentralCMVAshape_down_hfstats1.evaluate(idJet, eta, pt, cmva)
                bPogSF_CMVAreshape_down_hfstats1[0] *= sfCMVAshape_down_hfstats1

                sfCMVAshape_up_hfstats2 = self.readerCentralCMVAshape_up_hfstats2.evaluate(idJet, eta, pt, cmva)
                bPogSF_CMVAreshape_up_hfstats2[0] *= sfCMVAshape_up_hfstats2
                sfCMVAshape_down_hfstats2 = self.readerCentralCMVAshape_down_hfstats2.evaluate(idJet, eta, pt, cmva)
                bPogSF_CMVAreshape_down_hfstats2[0] *= sfCMVAshape_down_hfstats2

                sfCMVAshape_up_lfstats1 = self.readerCentralCMVAshape_up_lfstats1.evaluate(idJet, eta, pt, cmva)
                bPogSF_CMVAreshape_up_lfstats1[0] *= sfCMVAshape_up_lfstats1
                sfCMVAshape_down_lfstats1 = self.readerCentralCMVAshape_down_lfstats1.evaluate(idJet, eta, pt, cmva)
                bPogSF_CMVAreshape_down_lfstats1[0] *= sfCMVAshape_down_lfstats1

                sfCMVAshape_up_lfstats2 = self.readerCentralCMVAshape_up_lfstats2.evaluate(idJet, eta, pt, cmva)
                bPogSF_CMVAreshape_up_lfstats2[0] *= sfCMVAshape_up_lfstats2
                sfCMVAshape_down_lfstats2 = self.readerCentralCMVAshape_down_lfstats2.evaluate(idJet, eta, pt, cmva)
                bPogSF_CMVAreshape_down_lfstats2[0] *= sfCMVAshape_down_lfstats2

                sfCMVAshape_up_cferr1 = self.readerCentralCMVAshape_up_cferr1.evaluate(idJet, eta, pt, cmva)
                bPogSF_CMVAreshape_up_cferr1[0] *= sfCMVAshape_up_cferr1
                sfCMVAshape_down_cferr1 = self.readerCentralCMVAshape_down_cferr1.evaluate(idJet, eta, pt, cmva)
                bPogSF_CMVAreshape_down_cferr1[0] *= sfCMVAshape_down_cferr1

                sfCMVAshape_up_cferr2 = self.readerCentralCMVAshape_up_cferr2.evaluate(idJet, eta, pt, cmva)
                bPogSF_CMVAreshape_up_cferr2[0] *= sfCMVAshape_up_cferr2
                sfCMVAshape_down_cferr2 = self.readerCentralCMVAshape_down_cferr2.evaluate(idJet, eta, pt, cmva)
                bPogSF_CMVAreshape_down_cferr2[0] *= sfCMVAshape_down_cferr2




                sfCSVshape = self.readerCentralCSVshape.evaluate(idJet, eta, pt, csv)
                bPogSF_CSVreshape[0] *= sfCSVshape
                #print "CSV : idJet = ", idJet, " pt = ", pt, " eta = ", eta, " csv = ", csv, " SF = ", sfCSVshape, " weight = ", bPogSF_CSVreshape[0]

                sfCSVshape_up_jes = self.readerCentralCSVshape_up_jes.evaluate(idJet, eta, pt, csv)
                bPogSF_CSVreshape_up_jes[0] *= sfCSVshape_up_jes
                sfCSVshape_down_jes = self.readerCentralCSVshape_down_jes.evaluate(idJet, eta, pt, csv)
                bPogSF_CSVreshape_down_jes[0] *= sfCSVshape_down_jes

                sfCSVshape_up_lf = self.readerCentralCSVshape_up_lf.evaluate(idJet, eta, pt, csv)
                bPogSF_CSVreshape_up_lf[0] *= sfCSVshape_up_lf
                sfCSVshape_down_lf = self.readerCentralCSVshape_down_lf.evaluate(idJet, eta, pt, csv)
                bPogSF_CSVreshape_down_lf[0] *= sfCSVshape_down_lf

                sfCSVshape_up_hf = self.readerCentralCSVshape_up_hf.evaluate(idJet, eta, pt, csv)
                bPogSF_CSVreshape_up_hf[0] *= sfCSVshape_up_hf
                sfCSVshape_down_hf = self.readerCentralCSVshape_down_hf.evaluate(idJet, eta, pt, csv)
                bPogSF_CSVreshape_down_hf[0] *= sfCSVshape_down_hf

                sfCSVshape_up_hfstats1 = self.readerCentralCSVshape_up_hfstats1.evaluate(idJet, eta, pt, csv)
                bPogSF_CSVreshape_up_hfstats1[0] *= sfCSVshape_up_hfstats1
                sfCSVshape_down_hfstats1 = self.readerCentralCSVshape_down_hfstats1.evaluate(idJet, eta, pt, csv)
                bPogSF_CSVreshape_down_hfstats1[0] *= sfCSVshape_down_hfstats1

                sfCSVshape_up_hfstats2 = self.readerCentralCSVshape_up_hfstats2.evaluate(idJet, eta, pt, csv)
                bPogSF_CSVreshape_up_hfstats2[0] *= sfCSVshape_up_hfstats2
                sfCSVshape_down_hfstats2 = self.readerCentralCSVshape_down_hfstats2.evaluate(idJet, eta, pt, csv)
                bPogSF_CSVreshape_down_hfstats2[0] *= sfCSVshape_down_hfstats2

                sfCSVshape_up_lfstats1 = self.readerCentralCSVshape_up_lfstats1.evaluate(idJet, eta, pt, csv)
                bPogSF_CSVreshape_up_lfstats1[0] *= sfCSVshape_up_lfstats1
                sfCSVshape_down_lfstats1 = self.readerCentralCSVshape_down_lfstats1.evaluate(idJet, eta, pt, csv)
                bPogSF_CSVreshape_down_lfstats1[0] *= sfCSVshape_down_lfstats1

                sfCSVshape_up_lfstats2 = self.readerCentralCSVshape_up_lfstats2.evaluate(idJet, eta, pt, csv)
                bPogSF_CSVreshape_up_lfstats2[0] *= sfCSVshape_up_lfstats2
                sfCSVshape_down_lfstats2 = self.readerCentralCSVshape_down_lfstats2.evaluate(idJet, eta, pt, csv)
                bPogSF_CSVreshape_down_lfstats2[0] *= sfCSVshape_down_lfstats2

                sfCSVshape_up_cferr1 = self.readerCentralCSVshape_up_cferr1.evaluate(idJet, eta, pt, csv)
                bPogSF_CSVreshape_up_cferr1[0] *= sfCSVshape_up_cferr1
                sfCSVshape_down_cferr1 = self.readerCentralCSVshape_down_cferr1.evaluate(idJet, eta, pt, csv)
                bPogSF_CSVreshape_down_cferr1[0] *= sfCSVshape_down_cferr1

                sfCSVshape_up_cferr2 = self.readerCentralCSVshape_up_cferr2.evaluate(idJet, eta, pt, csv)
                bPogSF_CSVreshape_up_cferr2[0] *= sfCSVshape_up_cferr2
                sfCSVshape_down_cferr2 = self.readerCentralCSVshape_down_cferr2.evaluate(idJet, eta, pt, csv)
                bPogSF_CSVreshape_down_cferr2[0] *= sfCSVshape_down_cferr2





                if idJet != 2:
                  sfCMVAL      = self.readerCentralCMVAL.evaluate(idJet, eta, pt)
                  sfCMVAM      = self.readerCentralCMVAM.evaluate(idJet, eta, pt)
                  sfCMVAT      = self.readerCentralCMVAT.evaluate(idJet, eta, pt)
                  sfCSVL      = self.readerCentralCSVL.evaluate(idJet, eta, pt)
                  sfCSVM      = self.readerCentralCSVM.evaluate(idJet, eta, pt)
                  sfCSVT      = self.readerCentralCSVT.evaluate(idJet, eta, pt)

		  if pt<30:
                    sfCMVALUp    = 2*( self.readerUpCMVAL.evaluate(idJet, eta, pt) - sfCMVAL ) + sfCMVAL
                    sfCMVALDown  = 2*( self.readerDownCMVAL.evaluate(idJet, eta, pt) -sfCMVAL ) +sfCMVAL
                    sfCMVAMUp    = 2*( self.readerUpCMVAM.evaluate(idJet, eta, pt) - sfCMVAM ) + sfCMVAM
                    sfCMVAMDown  = 2*( self.readerDownCMVAM.evaluate(idJet, eta, pt) -sfCMVAM ) +sfCMVAM
                    sfCMVATUp    = 2*( self.readerUpCMVAT.evaluate(idJet, eta, pt) - sfCMVAT ) + sfCMVAT
                    sfCMVATDown  = 2*( self.readerDownCMVAT.evaluate(idJet, eta, pt) -sfCMVAT ) +sfCMVAT
                    sfCSVLUp    = 2*( self.readerUpCSVL.evaluate(idJet, eta, pt) - sfCSVL ) + sfCSVL
                    sfCSVLDown  = 2*( self.readerDownCSVL.evaluate(idJet, eta, pt) -sfCSVL ) +sfCSVL
                    sfCSVMUp    = 2*( self.readerUpCSVM.evaluate(idJet, eta, pt) - sfCSVM ) + sfCSVM
                    sfCSVMDown  = 2*( self.readerDownCSVM.evaluate(idJet, eta, pt) -sfCSVM ) +sfCSVM
                    sfCSVTUp    = 2*( self.readerUpCSVT.evaluate(idJet, eta, pt) - sfCSVT ) + sfCSVT
                    sfCSVTDown  = 2*( self.readerDownCSVT.evaluate(idJet, eta, pt) -sfCSVT ) +sfCSVT


                  else:
                    sfCMVALUp    = self.readerUpCMVAL.evaluate(idJet, eta, pt)
                    sfCMVALDown  = self.readerDownCMVAL.evaluate(idJet, eta, pt)
                    sfCMVAMUp    = self.readerUpCMVAM.evaluate(idJet, eta, pt)
                    sfCMVAMDown  = self.readerDownCMVAM.evaluate(idJet, eta, pt)
                    sfCMVATUp    = self.readerUpCMVAT.evaluate(idJet, eta, pt)
                    sfCMVATDown  = self.readerDownCMVAT.evaluate(idJet, eta, pt)
                    sfCSVLUp    = self.readerUpCSVL.evaluate(idJet, eta, pt)
                    sfCSVLDown  = self.readerDownCSVL.evaluate(idJet, eta, pt)
                    sfCSVMUp    = self.readerUpCSVM.evaluate(idJet, eta, pt)
                    sfCSVMDown  = self.readerDownCSVM.evaluate(idJet, eta, pt)
                    sfCSVTUp    = self.readerUpCSVT.evaluate(idJet, eta, pt)
                    sfCSVTDown  = self.readerDownCSVT.evaluate(idJet, eta, pt)


                else:
                  sfCMVAL      = self.readerLightCentralCMVAL.evaluate(idJet, eta, pt)
                  sfCMVALUp    = self.readerLightUpCMVAL.evaluate(idJet, eta, pt)
                  sfCMVALDown  = self.readerLightDownCMVAL.evaluate(idJet, eta, pt)
                  sfCMVAM      = self.readerLightCentralCMVAM.evaluate(idJet, eta, pt)
                  sfCMVAMUp    = self.readerLightUpCMVAM.evaluate(idJet, eta, pt)
                  sfCMVAMDown  = self.readerLightDownCMVAM.evaluate(idJet, eta, pt)
                  sfCMVAT      = self.readerLightCentralCMVAT.evaluate(idJet, eta, pt)
                  sfCMVATUp    = self.readerLightUpCMVAT.evaluate(idJet, eta, pt)
                  sfCMVATDown  = self.readerLightDownCMVAT.evaluate(idJet, eta, pt)
                  sfCSVL      = self.readerLightCentralCSVL.evaluate(idJet, eta, pt)
                  sfCSVLUp    = self.readerLightUpCSVL.evaluate(idJet, eta, pt)
                  sfCSVLDown  = self.readerLightDownCSVL.evaluate(idJet, eta, pt)
                  sfCSVM      = self.readerLightCentralCSVM.evaluate(idJet, eta, pt)
                  sfCSVMUp    = self.readerLightUpCSVM.evaluate(idJet, eta, pt)
                  sfCSVMDown  = self.readerLightDownCSVM.evaluate(idJet, eta, pt)
                  sfCSVT      = self.readerLightCentralCSVT.evaluate(idJet, eta, pt)
                  sfCSVTUp    = self.readerLightUpCSVT.evaluate(idJet, eta, pt)
                  sfCSVTDown  = self.readerLightDownCSVT.evaluate(idJet, eta, pt)


                effMC_CMVAL = self._getEffMC('CMVA', 'L', kindJet, pt, abs(eta))
                effMC_CMVAM = self._getEffMC('CMVA', 'M', kindJet, pt, abs(eta))
                effMC_CMVAT = self._getEffMC('CMVA', 'T', kindJet, pt, abs(eta))
                effMC_CSVL = self._getEffMC('CSV', 'L', kindJet, pt, abs(eta))
                effMC_CSVM = self._getEffMC('CSV', 'M', kindJet, pt, abs(eta))
                effMC_CSVT = self._getEffMC('CSV', 'T', kindJet, pt, abs(eta))


                #print "pt, eta, idJet, kindJet", pt, eta, idJet, kindJet, " sf, sfUp, sfDown, sfTP, sfTPUp, sfTPDown",  sf, sfUp, sfDown, sfTP, sfTPUp, sfTPDown, " effMC", effMC

                pMC_CMVAL = pMC_CMVAL*effMC_CMVAL if tagged_CMVAL else pMC_CMVAL*(1.-effMC_CMVAL)
                pMC_CMVAM = pMC_CMVAM*effMC_CMVAM if tagged_CMVAM else pMC_CMVAM*(1.-effMC_CMVAM)
                pMC_CMVAT = pMC_CMVAT*effMC_CMVAT if tagged_CMVAT else pMC_CMVAT*(1.-effMC_CMVAT)
                pMC_CSVL = pMC_CSVL*effMC_CSVL if tagged_CSVL else pMC_CSVL*(1.-effMC_CSVL)
                pMC_CSVM = pMC_CSVM*effMC_CSVM if tagged_CSVM else pMC_CSVM*(1.-effMC_CSVM)
                pMC_CSVT = pMC_CSVT*effMC_CSVT if tagged_CSVT else pMC_CSVT*(1.-effMC_CSVT)


                pData_CMVAL     = pData_CMVAL*effMC_CMVAL*sfCMVAL         if tagged_CMVAL else pData_CMVAL*(1.-effMC_CMVAL*sfCMVAL)
                pDataUp_CMVAL   = pDataUp_CMVAL*effMC_CMVAL*sfCMVALUp     if tagged_CMVAL else pDataUp_CMVAL*(1.-effMC_CMVAL*sfCMVALUp)
                pDataDown_CMVAL = pDataDown_CMVAL*effMC_CMVAL*sfCMVALDown if tagged_CMVAL else pDataDown_CMVAL*(1.-effMC_CMVAL*sfCMVALDown)
                pData_CMVAM     = pData_CMVAM*effMC_CMVAM*sfCMVAM         if tagged_CMVAM else pData_CMVAM*(1.-effMC_CMVAM*sfCMVAM)
                pDataUp_CMVAM   = pDataUp_CMVAM*effMC_CMVAM*sfCMVAMUp     if tagged_CMVAM else pDataUp_CMVAM*(1.-effMC_CMVAM*sfCMVAMUp)
                pDataDown_CMVAM = pDataDown_CMVAM*effMC_CMVAM*sfCMVAMDown if tagged_CMVAM else pDataDown_CMVAM*(1.-effMC_CMVAM*sfCMVAMDown)
                pData_CMVAT     = pData_CMVAT*effMC_CMVAT*sfCMVAT         if tagged_CMVAT else pData_CMVAT*(1.-effMC_CMVAT*sfCMVAT)
                pDataUp_CMVAT   = pDataUp_CMVAT*effMC_CMVAT*sfCMVATUp     if tagged_CMVAT else pDataUp_CMVAT*(1.-effMC_CMVAT*sfCMVATUp)
                pDataDown_CMVAT = pDataDown_CMVAT*effMC_CMVAT*sfCMVATDown if tagged_CMVAT else pDataDown_CMVAT*(1.-effMC_CMVAT*sfCMVATDown)
                pData_CSVL     = pData_CSVL*effMC_CSVL*sfCSVL         if tagged_CSVL else pData_CSVL*(1.-effMC_CSVL*sfCSVL)
                pDataUp_CSVL   = pDataUp_CSVL*effMC_CSVL*sfCSVLUp     if tagged_CSVL else pDataUp_CSVL*(1.-effMC_CSVL*sfCSVLUp)
                pDataDown_CSVL = pDataDown_CSVL*effMC_CSVL*sfCSVLDown if tagged_CSVL else pDataDown_CSVL*(1.-effMC_CSVL*sfCSVLDown)
                pData_CSVM     = pData_CSVM*effMC_CSVM*sfCSVM         if tagged_CSVM else pData_CSVM*(1.-effMC_CSVM*sfCSVM)
                pDataUp_CSVM   = pDataUp_CSVM*effMC_CSVM*sfCSVMUp     if tagged_CSVM else pDataUp_CSVM*(1.-effMC_CSVM*sfCSVMUp)
                pDataDown_CSVM = pDataDown_CSVM*effMC_CSVM*sfCSVMDown if tagged_CSVM else pDataDown_CSVM*(1.-effMC_CSVM*sfCSVMDown)
                pData_CSVT     = pData_CSVT*effMC_CSVT*sfCSVT         if tagged_CSVT else pData_CSVT*(1.-effMC_CSVT*sfCSVT)
                pDataUp_CSVT   = pDataUp_CSVT*effMC_CSVT*sfCSVTUp     if tagged_CSVT else pDataUp_CSVT*(1.-effMC_CSVT*sfCSVTUp)
                pDataDown_CSVT = pDataDown_CSVT*effMC_CSVT*sfCSVTDown if tagged_CSVT else pDataDown_CSVT*(1.-effMC_CSVT*sfCSVTDown)

                njet += 1
                #print "flavour, effMC, sf", flavour, effMC, sf

            #print "pData, pMC", pData, pMC

            #print "bPogSF_CMVAreshape[0] = ", bPogSF_CMVAreshape[0]
            #print "bPogSF_CMVAreshape_up_jes[0] = ", bPogSF_CMVAreshape_up_jes[0]

            bPogSF[0]          = pData_CMVAL/pMC_CMVAL
            bPogSFUp[0]        = pDataUp_CMVAL/pMC_CMVAL
            bPogSFDown[0]      = pDataDown_CMVAL/pMC_CMVAL

            bPogSF_CMVAL[0]          = pData_CMVAL/pMC_CMVAL
            bPogSF_CMVAL_Up[0]        = pDataUp_CMVAL/pMC_CMVAL
            bPogSF_CMVAL_Down[0]      = pDataDown_CMVAL/pMC_CMVAL

            bPogSF_CMVAM[0]          = pData_CMVAM/pMC_CMVAM
            bPogSF_CMVAM_Up[0]        = pDataUp_CMVAM/pMC_CMVAM
            bPogSF_CMVAM_Down[0]      = pDataDown_CMVAM/pMC_CMVAM

            bPogSF_CMVAT[0]          = pData_CMVAT/pMC_CMVAT
            bPogSF_CMVAT_Up[0]        = pDataUp_CMVAT/pMC_CMVAT
            bPogSF_CMVAT_Down[0]      = pDataDown_CMVAT/pMC_CMVAT

            bPogSF_CSVL[0]          = pData_CSVL/pMC_CSVL
            bPogSF_CSVL_Up[0]        = pDataUp_CSVL/pMC_CSVL
            bPogSF_CSVL_Down[0]      = pDataDown_CSVL/pMC_CSVL

            bPogSF_CSVM[0]          = pData_CSVM/pMC_CSVM
            bPogSF_CSVM_Up[0]        = pDataUp_CSVM/pMC_CSVM
            bPogSF_CSVM_Down[0]      = pDataDown_CSVM/pMC_CSVM

            bPogSF_CSVT[0]          = pData_CSVT/pMC_CSVT
            bPogSF_CSVT_Up[0]        = pDataUp_CSVT/pMC_CSVT
            bPogSF_CSVT_Down[0]      = pDataDown_CSVT/pMC_CSVT

            otree.Fill()

        self.disconnect()
        print '- Eventloop completed'

