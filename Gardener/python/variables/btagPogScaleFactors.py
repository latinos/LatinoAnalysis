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
                                                                                                                                       
class btagPogScaleFactors(TreeCloner):

    def __init__(self):
        pass

    def __del__(self):
        pass

    def help(self):
        return '''Add a scale factor derived according to POG recommendations, method 1a in https://twiki.cern.ch/twiki/bin/view/CMS/BTagSFMethods#1a_Event_reweighting_using_scale'''

    def addOptions(self,parser):
        description = self.help()
        group = optparse.OptionGroup(parser,self.label, description)
        group.add_option('-w', '--working-point', dest='workingPoint', help='CSVv2 working point', default='0')
        group.add_option('-s', '--scalefactor-file', dest='sfFile', help='file with scale factors', default='data/cMVAv2.csv')
        group.add_option('-p', '--scalefactor-file-tp', dest='sfFileTP', help='file with scale factors', default='data/TPScaleFactors.csv')
        group.add_option('-e', '--efficiency-file', dest='efficiencyMCFile', help='file with efficiency tables on MC', default='data/efficiencyMCFile76X.py')

        parser.add_option_group(group)
        return group



    def checkOptions(self,opts):
       
        # ~~~~
        #ROOT.gSystem.Load('libCondFormatsBTagObjects') 
        cmssw_base = os.getenv('CMSSW_BASE')
        efficienciesMC = {}
        efffile_path = cmssw_base+'/src/LatinoAnalysis/Gardener/python/'+opts.efficiencyMCFile
        if opts.efficiencyMCFile == None :
          print " Please provide an input file with the MC efficiencies "
           
        elif os.path.exists(efffile_path) :
          handle = open(efffile_path,'r')
          exec(handle)
          handle.close()
        else:  
          print "cannot find file", opts.efficiencyMCFile

        #print " isoidScaleFactors = ", isoidScaleFactors
        
        self.efficienciesMC = efficienciesMC

        self.minpt = 20
        self.maxpt = 290 
        
        self.mineta = 0
        self.maxeta = 2.4

        #compile code to read scale factors

        #ROOT.gROOT.ProcessLine(".L "+cmssw_base+'/src/LatinoAnalysis/Gardener/python/variables/BTagCalibrationStandalone.cc+')
        try:
            ROOT.gROOT.LoadMacro(cmssw_base+'/src/LatinoAnalysis/Gardener/python/variables/BTagCalibrationStandalone.cc+g')
        except RuntimeError:
            ROOT.gROOT.LoadMacro(cmssw_base+'/src/LatinoAnalysis/Gardener/python/variables/BTagCalibrationStandalone.cc++g')
        #ROOT.gROOT.ProcessLine('.L BTagCalibrationStandalone.cc+') 
        print "scale factors from", cmssw_base+'/src/LatinoAnalysis/Gardener/python/data/'+opts.sfFile

        wp = int(opts.workingPoint)
        self.calib = ROOT.BTagCalibration("cMVAv2", cmssw_base+'/src/LatinoAnalysis/Gardener/python/'+opts.sfFile)
        self.readerCentral = ROOT.BTagCalibrationReader(self.calib, wp, "ttbar", "central")  
        self.readerUp = ROOT.BTagCalibrationReader(self.calib, wp, "ttbar", "up")  
        self.readerDown = ROOT.BTagCalibrationReader(self.calib, wp, "ttbar", "down")  
        
        #it seems that so far light jet scale factors are only available in the incl dataset 
        #(light jets is the only thing available in that dataset)
        self.readerLightCentral = ROOT.BTagCalibrationReader(self.calib, wp, "incl", "central")  
        self.readerLightUp = ROOT.BTagCalibrationReader(self.calib, wp, "incl", "up")  
        self.readerLightDown = ROOT.BTagCalibrationReader(self.calib, wp, "incl", "down")  

        # our T&P scale factors
        self.calibTP = ROOT.BTagCalibration("csvv2", cmssw_base+'/src/LatinoAnalysis/Gardener/python/'+opts.sfFileTP)
        self.readerCentralTP = ROOT.BTagCalibrationReader(self.calibTP, wp, "tp", "central") 
        self.readerUpTP = ROOT.BTagCalibrationReader(self.calibTP, wp, "tp", "up")  
        self.readerDownTP = ROOT.BTagCalibrationReader(self.calibTP, wp, "tp", "down")  

        self.readerLightCentralTP = ROOT.BTagCalibrationReader(self.calibTP, wp, "zcontrol", "central")  
        self.readerLightUpTP = ROOT.BTagCalibrationReader(self.calibTP, wp, "zcontrol", "up")  
        self.readerLightDownTP = ROOT.BTagCalibrationReader(self.calibTP, wp, "zcontrol", "down")  

        
        if wp == 0:
          self.cut = -0.715
        elif wp == 1:
          self.cut =0.185
        elif wp == 2:
          self.cut =0.875
        else:
          print "WP", opts.workingPoint, " is not supported"



    def _getEffMC (self, kindJet, pt, eta):

        # fix underflow and overflow
        if pt < self.minpt:
          pt = self.minpt
        if pt > self.maxpt:
          pt = self.maxpt
        
        if eta < self.mineta:
          eta = self.mineta
        if eta > self.maxeta:
          eta = self.maxeta


        if kindJet in self.efficienciesMC.keys() : 
          # get the efficiency
          for point in self.efficienciesMC[kindJet] : 
            #   pt           eta          eff 
            # (( 0.0, 10.0), (0.0, 1.5), 0.980 ),
            if ( pt  >= point[0][0] and pt  < point[0][1] and
                 eta >= point[1][0] and eta < point[1][1] ) :
                return point[2]

          # default ... it should never happen!
          print " default ???", pt, eta, kindJet
          return 1.0
 
        # not a lepton ... like some default value
        return 1.0
   

    def process(self,**kwargs):
        tree  = kwargs['tree']
        input = kwargs['input']
        output = kwargs['output']

        self.connect(tree,input)

          
        self.clone(output,["bPogSF", "bPogSFUp", "bPogSFDown", 
                           "bTPSF", "bTPSFUp", "bTPSFDown",
			   "bPogSF1Jet", "bPogSF1JetUp", "bPogSF1JetDown",
                           "bTPSF1Jet", "bTPSF1JetUp", "bTPSF1JetDown",
			   "bPogSF2Jet", "bPogSF2JetUp", "bPogSF2JetDown",
                           "bTPSF2Jet", "bTPSF2JetUp", "bTPSF2JetDown",])


        #bPogSF and similar are SF from bPOG

        bPogSF = numpy.ones(1, dtype=numpy.float32)
        self.otree.Branch('bPogSF',bPogSF,'bPogSF/F')
        bPogSFUp = numpy.ones(1, dtype=numpy.float32)
        self.otree.Branch('bPogSFUp',bPogSFUp,'bPogSFUp/F') 
        bPogSFDown = numpy.ones(1, dtype=numpy.float32)
        self.otree.Branch('bPogSFDown',bPogSFDown,'bPogSFDown/F')

        #bTPSF and similar are scale factors from out Tag and Probe studies

        bTPSF = numpy.ones(1, dtype=numpy.float32)
        self.otree.Branch('bTPSF',bTPSF,'bTPSF/F')
        bTPSFUp = numpy.ones(1, dtype=numpy.float32)
        self.otree.Branch('bTPSFUp',bTPSFUp,'bTPSFUp/F')
        bTPSFDown = numpy.ones(1, dtype=numpy.float32)
        self.otree.Branch('bTPSFDown',bTPSFDown,'bTPSFDown/F')





        #bPogSF1Jet and similar are SF from bPOG

        bPogSF1Jet = numpy.ones(1, dtype=numpy.float32)
        self.otree.Branch('bPogSF1Jet',bPogSF1Jet,'bPogSF1Jet/F')
        bPogSF1JetUp = numpy.ones(1, dtype=numpy.float32)
        self.otree.Branch('bPogSF1JetUp',bPogSF1JetUp,'bPogSF1JetUp/F')
        bPogSF1JetDown = numpy.ones(1, dtype=numpy.float32)
        self.otree.Branch('bPogSF1JetDown',bPogSF1JetDown,'bPogSF1JetDown/F')

        #bTPSF1Jet and similar are scale factors from out Tag and Probe studies

        bTPSF1Jet = numpy.ones(1, dtype=numpy.float32)
        self.otree.Branch('bTPSF1Jet',bTPSF1Jet,'bTPSF1Jet/F')
        bTPSF1JetUp = numpy.ones(1, dtype=numpy.float32)
        self.otree.Branch('bTPSF1JetUp',bTPSF1JetUp,'bTPSF1JetUp/F')
        bTPSF1JetDown = numpy.ones(1, dtype=numpy.float32)
        self.otree.Branch('bTPSF1JetDown',bTPSF1JetDown,'bTPSF1JetDown/F')




        #bPogSF2Jet and similar are SF from bPOG

        bPogSF2Jet = numpy.ones(1, dtype=numpy.float32)
        self.otree.Branch('bPogSF2Jet',bPogSF2Jet,'bPogSF2Jet/F')
        bPogSF2JetUp = numpy.ones(1, dtype=numpy.float32)
        self.otree.Branch('bPogSF2JetUp',bPogSF2JetUp,'bPogSF2JetUp/F')
        bPogSF2JetDown = numpy.ones(1, dtype=numpy.float32)
        self.otree.Branch('bPogSF2JetDown',bPogSF2JetDown,'bPogSF2JetDown/F')

        #bTPSF2Jet and similar are scale factors from out Tag and Probe studies

        bTPSF2Jet = numpy.ones(1, dtype=numpy.float32)
        self.otree.Branch('bTPSF2Jet',bTPSF2Jet,'bTPSF2Jet/F')
        bTPSF2JetUp = numpy.ones(1, dtype=numpy.float32)
        self.otree.Branch('bTPSF2JetUp',bTPSF2JetUp,'bTPSF2JetUp/F')
        bTPSF2JetDown = numpy.ones(1, dtype=numpy.float32)
        self.otree.Branch('bTPSF2JetDown',bTPSF2JetDown,'bTPSF2JetDown/F')


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


            pData         = 1.
            pDataUp       = 1.
            pDataDown     = 1.

            pDataTP       = 1.
            pDataTPUp     = 1.
            pDataTPDown   = 1.

            pMC           = 1.

            njet 	  = 0

            for iJet in xrange(len(itree.std_vector_jet_pt)) :
             
              pt      = itree.std_vector_jet_pt [iJet]
              eta     = itree.std_vector_jet_eta [iJet]
              flavour = itree.std_vector_jet_HadronFlavour [iJet]
              tagged  = itree.std_vector_jet_csvv2ivf[iJet] > self.cut
             
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
                if idJet != 2:
                  sf      = self.readerCentral.evaluate(idJet, eta, pt)
                  sfUp    = self.readerUp.evaluate(idJet, eta, pt)
                  sfDown  = self.readerDown.evaluate(idJet, eta, pt)
                  sfTP      = self.readerCentralTP.evaluate(idJet, eta, pt)
                  sfTPUp    = self.readerUpTP.evaluate(idJet, eta, pt)
                  sfTPDown  = self.readerDownTP.evaluate(idJet, eta, pt)

                else:
                  sf      = self.readerLightCentral.evaluate(idJet, eta, pt)
                  sfUp    = self.readerLightUp.evaluate(idJet, eta, pt)
                  sfDown  = self.readerLightDown.evaluate(idJet, eta, pt)
                  sfTP      = self.readerLightCentralTP.evaluate(idJet, eta, pt)
                  sfTPUp    = self.readerLightUpTP.evaluate(idJet, eta, pt)
                  sfTPDown  = self.readerLightDownTP.evaluate(idJet, eta, pt)

                effMC = self._getEffMC(kindJet, pt, abs(eta))
                #print "pt, eta, idJet, kindJet", pt, eta, idJet, kindJet, " sf, sfUp, sfDown, sfTP, sfTPUp, sfTPDown",  sf, sfUp, sfDown, sfTP, sfTPUp, sfTPDown, " effMC", effMC

                pMC = pMC*effMC if tagged else pMC*(1.-effMC)

                pData     = pData*effMC*sf         if tagged else pData*(1.-effMC*sf)
                pDataUp   = pDataUp*effMC*sfUp     if tagged else pDataUp*(1.-effMC*sfUp)
                pDataDown = pDataDown*effMC*sfDown if tagged else pDataDown*(1.-effMC*sfDown)

                #pDataTP     = pDataTP*effMC*sfTP         if tagged else pDataTP*(1.-effMC*sfTP)
                #pDataTPUp   = pDataTPUp*effMC*sfTPUp     if tagged else pDataTPUp*(1.-effMC*sfTPUp)
                #pDataTPDown = pDataTPDown*effMC*sfTPDown if tagged else pDataTPDown*(1.-effMC*sfTPDown)

		if njet < 1:
		  bPogSF1Jet[0]          = pData/pMC
                  bPogSF1JetUp[0]        = pDataUp/pMC
                  bPogSF1JetDown[0]      = pDataDown/pMC

                  #bTPSF1Jet[0]          = pDataTP/pMC
                  #bTPSF1JetUp[0]        = pDataTPUp/pMC
                  #bTPSF1JetDown[0]      = pDataTPDown/pMC

                if njet < 2:
                  bPogSF2Jet[0]          = pData/pMC
                  bPogSF2JetUp[0]        = pDataUp/pMC
                  bPogSF2JetDown[0]      = pDataDown/pMC

                  #bTPSF2Jet[0]          = pDataTP/pMC
                  #bTPSF2JetUp[0]        = pDataTPUp/pMC
                  #bTPSF2JetDown[0]      = pDataTPDown/pMC

                njet += 1
                #print "flavour, effMC, sf", flavour, effMC, sf

            #print "pData, pMC", pData, pMC

            bPogSF[0]          = pData/pMC
            bPogSFUp[0]        = pDataUp/pMC
            bPogSFDown[0]      = pDataDown/pMC

            #bTPSF[0]          = pDataTP/pMC
            #bTPSFUp[0]        = pDataTPUp/pMC
            #bTPSFDown[0]      = pDataTPDown/pMC

            otree.Fill()

        self.disconnect()
        print '- Eventloop completed'

