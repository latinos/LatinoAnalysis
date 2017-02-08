import optparse
import numpy
import ROOT
import os.path

from LatinoAnalysis.Gardener.gardening import TreeCloner

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
        description = self.help()
        group = optparse.OptionGroup(parser,self.label, description)
        group.add_option('-c','--cmssw',dest='cmssw',help='cmssw version req for met vars',default='763')
        return group

    def checkOptions(self,opts):
        cmssw_base = os.getenv('CMSSW_BASE')
        effFile = "data/efficiencyMCFile76X_all.py"
        if opts.cmssw == "ICHEP2016":
          effFile = "data/efficiencyMCFile80X_all.py"
        if opts.cmssw == "Full2016":
          effFile = "data/efficiencyMCFileFull2016.py"

        efficienciesMC_CMVA = {}
        efficienciesMC_CSV = {}
        efficienciesMC_DeepCSV = {}

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
        self.efficiencyMC_DeepCSV = efficienciesMC_DeepCSV

        self.minpt = 20
        self.maxpt = 290 
        
        self.mineta = 0
        self.maxeta = 2.4
        
        #compile code to read scale factors
        self.cmssw = opts.cmssw

        self.cmvaSfFile = 'cMVAv2.csv'
        self.csvSfFile = 'CSVv2.csv'
        self.deepCSVSfFile = 'deepCSV.csv'
        if self.cmssw == "ICHEP2016":
          self.cmvaSfFile = "cMVAv2_ICHEP2016.csv"
          self.csvSfFile  = "CSVv2_ICHEP2016.csv"
        if self.cmssw == "Full2016":
          self.cmvaSfFile = 'cMVAv2_Moriond17_B_H.csv'
          self.csvSfFile = 'CSVv2_Moriond17_B_H.csv'
          self.deepCSVSfFile = 'DeepCSV_Moriond17_B_H.csv'

        print "CMVA scale factors from", cmssw_base+'/src/LatinoAnalysis/Gardener/python/data/'+self.cmvaSfFile
        print "CSVv2 scale factors from", cmssw_base+'/src/LatinoAnalysis/Gardener/python/data/'+self.csvSfFile
        print "DeepCSV scale factors from", cmssw_base+'/src/LatinoAnalysis/Gardener/python/data/'+self.deepCSVSfFile

        ROOT.gSystem.Load('libCondFormatsBTauObjects')
        ROOT.gSystem.Load('libCondToolsBTau')

        self.wpreshape = 3 
        self.wps = ["L", "M", "T"]
        self.loadflavors=[0,1,2] # 0 is for b flavour, 1: FLAV_C, 2: FLAV_UDSG
        self.flavors=["udsg","bc"]
        self.variations=["central", "up", "down"]
        self.reshape_variations = ["central","up_jes","up_lf","up_hfstats1","up_hfstats2","up_cferr1","up_cferr2","up_hf","up_lfstats1","up_lfstats2","down_jes","down_lf","down_hfstats1","down_hfstats2","down_cferr1","down_cferr2","down_hf","down_lfstats1","down_lfstats2"]

        if self.cmssw == "Full2016":
          self.taggers=["CMVA", "CSV", "deepCSV"]
        else:
          self.taggers=["CMVA", "CSV"]

        self.calibs = {}
        for tagger in self.taggers:
          if tagger == "CMVA":
            self.calibs[tagger] = ROOT.BTagCalibration("cMVAv2", cmssw_base+'/src/LatinoAnalysis/Gardener/python/data/'+self.cmvaSfFile)
          elif tagger == "CSV":
            self.calibs[tagger] = ROOT.BTagCalibration("CSVv2", cmssw_base+'/src/LatinoAnalysis/Gardener/python/data/'+self.csvSfFile)
          elif tagger == "deepCSV":
            self.calibs[tagger] = ROOT.BTagCalibration("DeepCSV", cmssw_base+'/src/LatinoAnalysis/Gardener/python/data/'+self.deepCSVSfFile)
          else:
            print "Error: tagger not found!"
            break

        self.reshape_sys = getattr(ROOT, 'vector<string>')()
        for var in self.reshape_variations:
          if var == "central": continue
          self.reshape_sys.push_back(var)

        self.reshape_readers = {}
        for tagger in self.taggers:
          if tagger == "deepCSV": continue
          self.reshape_readers[tagger] = ROOT.BTagCalibrationReader(self.wpreshape, "central", self.reshape_sys)
          for flavor in self.loadflavors:
            self.reshape_readers[tagger].load(self.calibs[tagger],flavor,"iterativefit")

        self.v_sys = getattr(ROOT, 'vector<string>')()
        self.v_sys.push_back("up")
        self.v_sys.push_back("down")
        self.readers = {}
        for tagger in self.taggers:
          self.readers[tagger] = {}
          for iwp,wp in enumerate(self.wps):
            self.readers[tagger][wp] = ROOT.BTagCalibrationReader(iwp, "central", self.v_sys)
            for flavor in self.loadflavors:
              if flavor == 0 or flavor == 1: # b or c
                sampleCMVA = "ttbar"
                sampleCSV  = "mujets"
                sampleDeepCSV = "mujets"
              else:
                sampleCMVA = "incl"
                sampleCSV  = "incl"
                sampleDeepCSV = "incl"
              if tagger == "CMVA":
                self.readers[tagger][wp].load(self.calibs[tagger],flavor,sampleCMVA) 
              if tagger == "CSV":
                self.readers[tagger][wp].load(self.calibs[tagger],flavor,sampleCSV)
              if tagger == "deepCSV":
                self.readers[tagger][wp].load(self.calibs[tagger],flavor,sampleDeepCSV)

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

        elif algo == "deepCSV":
          if (kindJet,wp) in self.efficiencyMC_DeepCSV.keys() :
            # get the efficiency
            for point in self.efficiencyMC_DeepCSV[(kindJet,wp)] :
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
        branchlist = ["bPogSF", "bPogSFUp", "bPogSFDown"]

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
 
        for tagger in self.taggers:
          if tagger == "deepCSV": continue
          for rvariation in self.reshape_variations:
            if rvariation == "central":
              namebranch = "bPogSF_"+tagger+"reshape"
            else:
              namebranch = "bPogSF_"+tagger+"reshape_"+rvariation
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

        # Re-shaping weights
        bPogSF_reshape = {}
        for tagger in self.taggers:
          if tagger == "deepCSV": continue
          bPogSF_reshape[tagger] = {}
          for rvariation in self.reshape_variations:
            bPogSF_reshape[tagger][rvariation] = numpy.ones(1, dtype=numpy.float32)
            if rvariation == "central":
              namebranch = "bPogSF_"+tagger+"reshape"
            else:
              namebranch = "bPogSF_"+tagger+"reshape_"+rvariation
            self.otree.Branch(namebranch,bPogSF_reshape[tagger][rvariation],namebranch+'/F')

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
  
            for tagger in self.taggers:
              if tagger == "deepCSV": continue
              for rvariation in self.reshape_variations: 
                bPogSF_reshape[tagger][rvariation][0] = 1.

            njet 	  = 0

            for iJet in xrange(len(itree.std_vector_jet_pt)) :
             
              pt      = itree.std_vector_jet_pt [iJet]
              eta     = itree.std_vector_jet_eta [iJet]
              flavour = itree.std_vector_jet_HadronFlavour [iJet]
              cmva    = itree.std_vector_jet_cmvav2 [iJet]
              csv    = itree.std_vector_jet_csvv2ivf [iJet]
              tagged = {}
              tagged["CMVA"]={}
              tagged["CSV"]={}
              tagged["deepCSV"]={}
              if self.cmssw == "Full2016":
                tagged["CMVA"]["L"] = itree.std_vector_jet_cmvav2 [iJet] > -0.5884 
                tagged["CMVA"]["M"] = itree.std_vector_jet_cmvav2 [iJet] > 0.4432 
                tagged["CMVA"]["T"] = itree.std_vector_jet_cmvav2 [iJet] > 0.9432 

                tagged["CSV"]["L"] = itree.std_vector_jet_csvv2ivf [iJet] > 0.5426 
                tagged["CSV"]["M"] = itree.std_vector_jet_csvv2ivf [iJet] > 0.8484 
                tagged["CSV"]["T"] = itree.std_vector_jet_csvv2ivf [iJet] > 0.9535

                tagged["deepCSV"]["L"] = itree.std_vector_jet_DeepCSVB [iJet] > 0.2219
                tagged["deepCSV"]["M"] = itree.std_vector_jet_DeepCSVB [iJet] > 0.6324
                tagged["deepCSV"]["T"] = itree.std_vector_jet_DeepCSVB [iJet] > 0.8958
              else:
                tagged["CMVA"]["L"] = itree.std_vector_jet_cmvav2 [iJet] > -0.715
                tagged["CMVA"]["M"] = itree.std_vector_jet_cmvav2 [iJet] > 0.185
                tagged["CMVA"]["T"] = itree.std_vector_jet_cmvav2 [iJet] > 0.875

                tagged["CSV"]["L"] = itree.std_vector_jet_csvv2ivf [iJet] > 0.460
                tagged["CSV"]["M"] = itree.std_vector_jet_csvv2ivf [iJet] > 0.800
                tagged["CSV"]["T"] = itree.std_vector_jet_csvv2ivf [iJet] > 0.935 
             
              if pt < self.minpt or abs(eta) > self.maxeta: continue

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

              reshapeSF = {}
              for tagger in self.taggers:
                if tagger == "deepCSV": continue
                reshapeSF[tagger] = {}
                for rvariation in self.reshape_variations:
                  if tagger == "CMVA":
                    reshapeSF[tagger][rvariation] = self.reshape_readers[tagger].eval_auto_bounds(rvariation,idJet,eta,pt,cmva)
                  if tagger == "CSV":
                    reshapeSF[tagger][rvariation] = self.reshape_readers[tagger].eval_auto_bounds(rvariation,idJet,eta,pt,csv)
                  bPogSF_reshape[tagger][rvariation][0] *=reshapeSF[tagger][rvariation]

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
                    sf[tagger][wp][variation] = self.readers[tagger][wp].eval_auto_bounds(variation,idJet,eta,pt)
                    #print "~~ tagger : ", tagger, " wp = ", wp, " variation = ", variation, " sf = ", sf[tagger][wp][variation]

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

