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
                                                                                                                                       
class allBtagPogScaleFactorsICHEP(TreeCloner):

    def __init__(self):
        pass

    def __del__(self):
        pass

    def help(self):
        return '''Add a scale factor derived according to POG recommendations, method 1a in https://twiki.cern.ch/twiki/bin/view/CMS/BTagSFMethods#1a_Event_reweighting_using_scale'''

    def addOptions(self,parser):
        description = self.help()
        group = optparse.OptionGroup(parser,self.label, description)
        group.add_option('-c','--cmssw',dest='cmssw',help='cmssw version req for met vars',default='763')
        return group

    #def checkOptions(self,opts):
    #    pass
    def checkOptions(self,opts):
    #def _readSF (self):
        #ROOT.gSystem.Load('libCondFormatsBTagObjects') 
        cmssw_base = os.getenv('CMSSW_BASE')
        effFile = "data/efficiencyMCFile76X_all.py"
        if opts.cmssw == "ICHEP2016":
          effFile = "data/efficiencyMCFile80X_all.py"

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
        self.cmssw = opts.cmssw

        self.cmvaSfFile = 'cMVAv2.csv'
        self.csvSfFile = 'CSVv2.csv'
        if self.cmssw == "ICHEP2016":
          self.cmvaSfFile = "cMVAv2_ICHEP2016.csv"
          self.csvSfFile  = "CSVv2_ICHEP2016.csv"

        #ROOT.gROOT.ProcessLine(".L "+cmssw_base+'/src/LatinoAnalysis/Gardener/python/variables/BTagCalibrationStandaloneStandalone.cc+')
        try:
            ROOT.gROOT.LoadMacro(cmssw_base+'/src/LatinoAnalysis/Gardener/python/variables/BTagCalibrationStandalone.cc+g')
        except RuntimeError:
            ROOT.gROOT.LoadMacro(cmssw_base+'/src/LatinoAnalysis/Gardener/python/variables/BTagCalibrationStandalone.cc++g')
        #ROOT.gROOT.ProcessLine('.L BTagCalibrationStandaloneStandalone.cc+') 
        print "CMVA scale factors from", cmssw_base+'/src/LatinoAnalysis/Gardener/python/data/'+self.cmvaSfFile
        print "CSVv2 scale factors from", cmssw_base+'/src/LatinoAnalysis/Gardener/python/data/'+self.csvSfFile
        ### Readers for cMVAv2 re-shaping (1 nominal + 9 Up variations + 9 Down variations)
        self.calibCMVA = ROOT.BTagCalibrationStandalone("cMVAv2", cmssw_base+'/src/LatinoAnalysis/Gardener/python/data/'+self.cmvaSfFile)
        if self.cmssw != "ICHEP2016": 
          self.readerCentralCMVAshape = ROOT.BTagCalibrationStandaloneReader(self.calibCMVA, wps, "iterativefit", "central")
          self.readerCentralCMVAshape_up_jes = ROOT.BTagCalibrationStandaloneReader(self.calibCMVA, wps, "iterativefit", "up_jes")
          self.readerCentralCMVAshape_down_jes = ROOT.BTagCalibrationStandaloneReader(self.calibCMVA, wps, "iterativefit", "down_jes")
          self.readerCentralCMVAshape_up_lf = ROOT.BTagCalibrationStandaloneReader(self.calibCMVA, wps, "iterativefit", "up_lf")
          self.readerCentralCMVAshape_down_lf = ROOT.BTagCalibrationStandaloneReader(self.calibCMVA, wps, "iterativefit", "down_lf")
          self.readerCentralCMVAshape_up_hfstats1 = ROOT.BTagCalibrationStandaloneReader(self.calibCMVA, wps, "iterativefit", "up_hfstats1")
          self.readerCentralCMVAshape_down_hfstats1 = ROOT.BTagCalibrationStandaloneReader(self.calibCMVA, wps, "iterativefit", "down_hfstats1")
          self.readerCentralCMVAshape_up_hfstats2 = ROOT.BTagCalibrationStandaloneReader(self.calibCMVA, wps, "iterativefit", "up_hfstats2")
          self.readerCentralCMVAshape_down_hfstats2 = ROOT.BTagCalibrationStandaloneReader(self.calibCMVA, wps, "iterativefit", "down_hfstats2")
          self.readerCentralCMVAshape_up_cferr1 = ROOT.BTagCalibrationStandaloneReader(self.calibCMVA, wps, "iterativefit", "up_cferr1")
          self.readerCentralCMVAshape_down_cferr1 = ROOT.BTagCalibrationStandaloneReader(self.calibCMVA, wps, "iterativefit", "down_cferr1")
          self.readerCentralCMVAshape_up_cferr2 = ROOT.BTagCalibrationStandaloneReader(self.calibCMVA, wps, "iterativefit", "up_cferr2")
          self.readerCentralCMVAshape_down_cferr2 = ROOT.BTagCalibrationStandaloneReader(self.calibCMVA, wps, "iterativefit", "down_cferr2")
          self.readerCentralCMVAshape_up_hf = ROOT.BTagCalibrationStandaloneReader(self.calibCMVA, wps, "iterativefit", "up_hf")
          self.readerCentralCMVAshape_down_hf = ROOT.BTagCalibrationStandaloneReader(self.calibCMVA, wps, "iterativefit", "down_hf")
          self.readerCentralCMVAshape_up_lfstats1 = ROOT.BTagCalibrationStandaloneReader(self.calibCMVA, wps, "iterativefit", "up_lfstats1")
          self.readerCentralCMVAshape_down_lfstats1 = ROOT.BTagCalibrationStandaloneReader(self.calibCMVA, wps, "iterativefit", "down_lfstats1")
          self.readerCentralCMVAshape_up_lfstats2 = ROOT.BTagCalibrationStandaloneReader(self.calibCMVA, wps, "iterativefit", "up_lfstats2")
          self.readerCentralCMVAshape_down_lfstats2 = ROOT.BTagCalibrationStandaloneReader(self.calibCMVA, wps, "iterativefit", "down_lfstats2")

        ### Readers for CSVv2 re-shaping (1 nominal + 9 Up variations + 9 Down variations)
        self.calibCSV  = ROOT.BTagCalibrationStandalone("CSVv2", cmssw_base+'/src/LatinoAnalysis/Gardener/python/data/'+self.csvSfFile)
        if self.cmssw != "ICHEP2016":  
          self.readerCentralCSVshape = ROOT.BTagCalibrationStandaloneReader(self.calibCSV, wps, "iterativefit", "central")
          self.readerCentralCSVshape_up_jes = ROOT.BTagCalibrationStandaloneReader(self.calibCSV, wps, "iterativefit", "up_jes")
          self.readerCentralCSVshape_down_jes = ROOT.BTagCalibrationStandaloneReader(self.calibCSV, wps, "iterativefit", "down_jes")
          self.readerCentralCSVshape_up_lf = ROOT.BTagCalibrationStandaloneReader(self.calibCSV, wps, "iterativefit", "up_lf")
          self.readerCentralCSVshape_down_lf = ROOT.BTagCalibrationStandaloneReader(self.calibCSV, wps, "iterativefit", "down_lf")
          self.readerCentralCSVshape_up_hfstats1 = ROOT.BTagCalibrationStandaloneReader(self.calibCSV, wps, "iterativefit", "up_hfstats1")
          self.readerCentralCSVshape_down_hfstats1 = ROOT.BTagCalibrationStandaloneReader(self.calibCSV, wps, "iterativefit", "down_hfstats1")
          self.readerCentralCSVshape_up_hfstats2 = ROOT.BTagCalibrationStandaloneReader(self.calibCSV, wps, "iterativefit", "up_hfstats2")
          self.readerCentralCSVshape_down_hfstats2 = ROOT.BTagCalibrationStandaloneReader(self.calibCSV, wps, "iterativefit", "down_hfstats2")
          self.readerCentralCSVshape_up_cferr1 = ROOT.BTagCalibrationStandaloneReader(self.calibCSV, wps, "iterativefit", "up_cferr1")
          self.readerCentralCSVshape_down_cferr1 = ROOT.BTagCalibrationStandaloneReader(self.calibCSV, wps, "iterativefit", "down_cferr1")
          self.readerCentralCSVshape_up_cferr2 = ROOT.BTagCalibrationStandaloneReader(self.calibCSV, wps, "iterativefit", "up_cferr2")
          self.readerCentralCSVshape_down_cferr2 = ROOT.BTagCalibrationStandaloneReader(self.calibCSV, wps, "iterativefit", "down_cferr2")
          self.readerCentralCSVshape_up_hf = ROOT.BTagCalibrationStandaloneReader(self.calibCSV, wps, "iterativefit", "up_hf")
          self.readerCentralCSVshape_down_hf = ROOT.BTagCalibrationStandaloneReader(self.calibCSV, wps, "iterativefit", "down_hf")
          self.readerCentralCSVshape_up_lfstats1 = ROOT.BTagCalibrationStandaloneReader(self.calibCSV, wps, "iterativefit", "up_lfstats1")
          self.readerCentralCSVshape_down_lfstats1 = ROOT.BTagCalibrationStandaloneReader(self.calibCSV, wps, "iterativefit", "down_lfstats1")
          self.readerCentralCSVshape_up_lfstats2 = ROOT.BTagCalibrationStandaloneReader(self.calibCSV, wps, "iterativefit", "up_lfstats2")
          self.readerCentralCSVshape_down_lfstats2 = ROOT.BTagCalibrationStandaloneReader(self.calibCSV, wps, "iterativefit", "down_lfstats2")

        ### Readers for CMVA and CSV working point based 

        self.wps = ["L", "M", "T"]
        self.taggers=["CMVA", "CSV"]
        self.flavors=["udsg", "bc"]  
        self.variations=["central", "up", "down"]
        self.readers = {}
        self.readers["CMVA"]={}
        self.readers["CSV"]={}
        for iwp,wp in enumerate(self.wps):
          self.readers["CMVA"][wp] = {}
          self.readers["CSV"][wp]  = {}
          for flavor in self.flavors:
            self.readers["CMVA"][wp][flavor] = {}
            self.readers["CSV"][wp][flavor] = {}
            if flavor == "bc":
              sampleCMVA = "ttbar"
              sampleCSV  = "mujets"
            else:
              sampleCMVA = "incl"
              sampleCSV  ="incl"
            if self.cmssw == "ICHEP2016":
              sampleCMVA = "hww"
              sampleCSV = "hww"
            for variation in self.variations:
              self.readers["CMVA"][wp][flavor][variation] = ROOT.BTagCalibrationStandaloneReader(self.calibCMVA, iwp, sampleCMVA, variation)
              self.readers["CSV"][wp][flavor][variation]  = ROOT.BTagCalibrationStandaloneReader(self.calibCSV,  iwp, sampleCSV,  variation)
    



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

    def resetCounters(self):
      for tagger in self.taggers:
        for wp in self.wps:
          self.pMC[tagger][wp] = 1.
          for variation in self.variations:
            self.pData[tagger][wp][variation]["undef"]=1.
            if variation != "central":
              for flavor in self.flavors:
                self.pData[tagger][wp][variation][flavor]=1. 
      

    def process(self,**kwargs):
        tree  = kwargs['tree']
        input = kwargs['input']
        output = kwargs['output']

        self.connect(tree,input)

        #self._readSF()        
        branchlist = ["bPogSF", "bPogSFUp", "bPogSFDown",
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

                          ] 
        for tagger in self.taggers:
          for wp in self.wps:            
            for variation in self.variations:
              suffix = "_"+variation
              if variation == "central":
                suffix = ""
              namebranch = 'bPogSF_'+tagger+wp+suffix
              branchlist.append(namebranch)
              if variation != "central":
                for flavor in self.flavors:
                  suffix = "_"+flavor+"_"+variation
                  namebranch = 'bPogSF_'+tagger+wp+suffix
                  branchlist.append(namebranch)
  


        self.clone(output, branchlist)         

        bPogSFAll = {}
        self.pData  = {}
        self.pMC    = {}
        for tagger in self.taggers:
          bPogSFAll[tagger]={}
          self.pData[tagger]={}
          self.pMC[tagger]={} 
          for wp in self.wps:
            bPogSFAll[tagger][wp]={}
            self.pMC[tagger][wp] = 1.
            self.pData[tagger][wp]={}  
            for variation in self.variations:
              bPogSFAll[tagger][wp][variation]={}
              self.pData[tagger][wp][variation]={}
              #undef is for correlated variations independent of flaor
              bPogSFAll[tagger][wp][variation]["undef"] = numpy.ones(1, dtype=numpy.float32)
              self.pData[tagger][wp][variation]["undef"]=1.       
              suffix = "_"+variation
              if variation == "central":
                suffix = ""
              namebranch = 'bPogSF_'+tagger+wp+suffix
              self.otree.Branch(namebranch, bPogSFAll[tagger][wp][variation]["undef"], namebranch+"/F")
              if variation != "central":
                for flavor in self.flavors:
                  bPogSFAll[tagger][wp][variation][flavor] = numpy.ones(1, dtype=numpy.float32)
                  self.pData[tagger][wp][variation][flavor] = 1.
                  suffix = "_"+flavor+"_"+variation
                  namebranch = 'bPogSF_'+tagger+wp+suffix
                  self.otree.Branch(namebranch, bPogSFAll[tagger][wp][variation][flavor], namebranch+"/F")
                 
        bPogSF = numpy.ones(1, dtype=numpy.float32)
        self.otree.Branch('bPogSF',bPogSF,'bPogSF/F')        
        bPogSFUp = numpy.ones(1, dtype=numpy.float32)
        self.otree.Branch('bPogSFUp',bPogSFUp,'bPogSFUp/F') 
        bPogSFDown = numpy.ones(1, dtype=numpy.float32)
        self.otree.Branch('bPogSFDown',bPogSFDown,'bPogSFDown/F')   
        if self.cmssw != "ICHEP2016": 
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
  
            self.resetCounters()
            if self.cmssw != "ICHEP2016":  
              # CMVA reshaper
   
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
              tagged = {}
              tagged["CMVA"]={}
              tagged["CMVA"]["L"] = itree.std_vector_jet_cmvav2 [iJet] > -0.715
              tagged["CMVA"]["M"] = itree.std_vector_jet_cmvav2 [iJet] > 0.185
              tagged["CMVA"]["T"] = itree.std_vector_jet_cmvav2 [iJet] > 0.875
              tagged["CSV"]={}
              tagged["CSV"]["L"] = itree.std_vector_jet_csvv2ivf [iJet] > 0.460
              tagged["CSV"]["M"] = itree.std_vector_jet_csvv2ivf [iJet] > 0.800
              tagged["CSV"]["T"] = itree.std_vector_jet_csvv2ivf [iJet] > 0.935  
             
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
                if self.cmssw != "ICHEP2016": 
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

                effMC = {}
                sf = {}
                if (idJet != 2):
                  thisflavor = "bc"
                else:
                  thisflavor = "udsg"
                
                #get the SF
                for tagger in self.taggers:
                  effMC[tagger]={}
                  sf[tagger]={}
                  for wp in self.wps:
                    effMC[tagger][wp]=self._getEffMC(tagger, wp, kindJet, pt, abs(eta))
                    sf[tagger][wp]={}
                    for variation in self.variations:
                      # b/c
                      if (idJet != 2) :
                        sf[tagger][wp][variation] = self.readers[tagger][wp]["bc"][variation].evaluate(idJet, eta, pt)
                        if (pt < 30) and variation != "central":
                          #double the uncertainty for b/c jets below 30 GeV
                          sf[tagger][wp][variation] = 2*(self.readers[tagger][wp]["bc"][variation].evaluate(idJet, eta, pt) - \
                                                         sf[tagger][wp]["central"]) + \
                                                        sf[tagger][wp]["central"]  
                      # udsg
                      else:
                        sf[tagger][wp][variation] = self.readers[tagger][wp]["udsg"][variation].evaluate(idJet, eta, pt) 

                #use the SF to determine event probabilities
                for tagger in self.taggers:
                  for wp in self.wps:
                    if tagged[tagger][wp]:
                      self.pMC[tagger][wp] = self.pMC[tagger][wp]*effMC[tagger][wp]
                    else:
                      self.pMC[tagger][wp] = self.pMC[tagger][wp]*(1.-effMC[tagger][wp])
                    for variation in self.variations:
                      if tagged[tagger][wp]:  
                        self.pData[tagger][wp][variation]["undef"] = self.pData[tagger][wp][variation]["undef"]*effMC[tagger][wp]*sf[tagger][wp][variation]
                      else:
                        self.pData[tagger][wp][variation]["undef"] = self.pData[tagger][wp][variation]["undef"]*(1.-effMC[tagger][wp]*sf[tagger][wp][variation])
                      if variation != "central":
                        for flavor in self.flavors:
                          #if the flavor of this jet is the same as the flavor for which we are computing
                          #the variation, then we need the varied SF
                          #otherwise we take the central SF  
                          if thisflavor == flavor:
                            flavorsf = sf[tagger][wp][variation]
                          else:
                            flavorsf = sf[tagger][wp]["central"]    
                          if tagged[tagger][wp]:  
                            self.pData[tagger][wp][variation][flavor] = self.pData[tagger][wp][variation][flavor]*effMC[tagger][wp]*flavorsf
                          else:
                            self.pData[tagger][wp][variation][flavor] = self.pData[tagger][wp][variation][flavor]*(1.-effMC[tagger][wp]*flavorsf)

                njet += 1
                #print "flavour, effMC, sf", flavour, effMC, sf

            #print "pData, pMC", pData, pMC

            #print "bPogSF_CMVAreshape[0] = ", bPogSF_CMVAreshape[0]
            #print "bPogSF_CMVAreshape_up_jes[0] = ", bPogSF_CMVAreshape_up_jes[0]
            for tagger in self.taggers:
              for wp in self.wps:
                for variation in self.variations:
                  bPogSFAll[tagger][wp][variation]["undef"][0] = self.pData[tagger][wp][variation]["undef"]/self.pMC[tagger][wp]
                  if variation != "central":
                    for flavor in self.flavors:
                      bPogSFAll[tagger][wp][variation][flavor][0] = self.pData[tagger][wp][variation][flavor]/self.pMC[tagger][wp]

            bPogSF[0]          = bPogSFAll["CMVA"]["L"]["central"]["undef"] 
            bPogSFUp[0]        = bPogSFAll["CMVA"]["L"]["up"]["undef"]
            bPogSFDown[0]      = bPogSFAll["CMVA"]["L"]["down"]["undef"]

            otree.Fill()

        self.disconnect()
        print '- Eventloop completed'


