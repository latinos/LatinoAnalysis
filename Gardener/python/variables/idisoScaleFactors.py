import optparse
import numpy
import ROOT
import os.path
import math

from LatinoAnalysis.Gardener.gardening import TreeCloner

#
#  _ _|      |         /     _ _|                    ___|                |            ____|             |                           
#    |    _` |        /        |    __|   _ \      \___ \    __|   _` |  |   _ \      |     _` |   __|  __|   _ \    __|  __| 
#    |   (   |       /         |  \__ \  (   |           |  (     (   |  |   __/      __|  (   |  (     |    (   |  |   \__ \ 
#  ___| \__,_|     _/        ___| ____/ \___/      _____/  \___| \__,_| _| \___|     _|   \__,_| \___| \__| \___/  _|   ____/ 
#                                                                                                                             
#

class IdIsoSFFiller(TreeCloner):

    def __init__(self):
        pass

    def __del__(self):
        pass

    def help(self):
        return '''Add a new lepton scale factor weight based on id/isolation scale factors data/MC.'''

    def addOptions(self,parser):
        description = self.help()
        group = optparse.OptionGroup(parser,self.label, description)

        group.add_option('-c', '--cmssw', dest='cmssw', help='cmssw version (naming convention may change)', default='763', type='string')

        group.add_option( '--idmu',       dest='idScaleFactorsFileMu' ,       help='file with scale factors for id for muons', default=None)
        group.add_option( '--isoTightmu', dest='isoTightScaleFactorsFileMu' , help='file with scale factors for isolation ,tight definition, for muons', default=None)
        group.add_option( '--isoLoosemu', dest='isoLooseScaleFactorsFileMu' , help='file with scale factors for isolation ,loose definition, for muons', default=None)
        
        group.add_option( '--isoidele'   , dest='idIsoScaleFactorsFileElectron',            help='file with scale factors for isolation and id for electrons',                  default=None)
        group.add_option( '--tkSCele'    , dest='tkSCFileElectron',                         help='file with scale factors for track-SC efficiency for electrons',               default=None)
        group.add_option( '--tkMu'       , dest='tkMuFile',                         help='file with scale factors for track-SC efficiency for electrons',               default=None)
        group.add_option( '--isoideleAlt', dest='idIsoScaleFactorsFileElectronAlternative', help='file with scale factors for isolation and id for electrons, alternative',     default=None)
        group.add_option( '--isoideleAltLumiRatio', dest='idIsoScaleFactorsFileElectronAlternativeLumiRatio', help='Luminosity ratio between first period and the whole', type='float'  ,    default=-1.0)

        # new feature introduced for Full2016 (Jan 2017)
        group.add_option( '--idEleKind'   , dest='idEleKind',            help='kind of electron id. This will allow to pick up the correct electron SF and give the right name',  default=None)   # e.g. "cut_WP_Tight80X"

        parser.add_option_group(group)
        return group



    def checkOptions(self,opts):
       
        # ~~~~
        idIsoScaleFactors = {}

        self.idEleKind = opts.idEleKind

        cmssw_base = os.getenv('CMSSW_BASE')

        # Muon SF
        if opts.idScaleFactorsFileMu == None :
          if opts.cmssw == "ICHEP2016" :  opts.idScaleFactorsFileMu =        cmssw_base+'/src/LatinoAnalysis/Gardener/python/data/idiso/ICHEP2016fullLumi/muons.txt'  
          else :                          opts.idScaleFactorsFileMu =        cmssw_base+'/src/LatinoAnalysis/Gardener/python/data/idiso/muons_Moriond76x.txt'

        if opts.isoTightScaleFactorsFileMu == None :
          if opts.cmssw == "ICHEP2016" :  opts.isoTightScaleFactorsFileMu = cmssw_base+'/src/LatinoAnalysis/Gardener/python/data/idiso/ICHEP2016fullLumi/muons_iso_tight.txt'  
          else :                          opts.isoTightScaleFactorsFileMu = cmssw_base+'/src/LatinoAnalysis/Gardener/python/data/idiso/muons_iso_tight_Moriond76x.txt'
        if opts.isoLooseScaleFactorsFileMu == None :
          if opts.cmssw == "ICHEP2016" :  opts.isoLooseScaleFactorsFileMu = cmssw_base+'/src/LatinoAnalysis/Gardener/python/data/idiso/ICHEP2016fullLumi/muons_iso_loose.txt'  
          else :                          opts.isoLooseScaleFactorsFileMu = cmssw_base+'/src/LatinoAnalysis/Gardener/python/data/idiso/muons_iso_loose_Moriond76x.txt'

        if opts.cmssw == "Full2016" :
          self.IdMuMinRun    = []
          self.IdMuMaxRun    = []
          self.IdMuFileData  = []
          self.IdMuFileMC    = []
          self.IdMuMinRun    .append(1)
          self.IdMuMaxRun    .append(4)
          self.IdMuFileData  .append(cmssw_base+'/src/LatinoAnalysis/Gardener/python/data/idiso/Full2016/Tight_Run2016BCDEF_PTvsETA_HWW.txt')
          self.IdMuFileMC    .append(cmssw_base+'/src/LatinoAnalysis/Gardener/python/data/idiso/Full2016/TightID_DY_madgraphLikeRun2016BCDEF_PTvsETA_HWW.txt')
          self.IdMuMinRun    .append(5)
          self.IdMuMaxRun    .append(6)
          self.IdMuFileData  .append(cmssw_base+'/src/LatinoAnalysis/Gardener/python/data/idiso/Full2016/Tight_Run2016GH_PTvsETA_HWW.txt')
          self.IdMuFileMC    .append(cmssw_base+'/src/LatinoAnalysis/Gardener/python/data/idiso/Full2016/TightID_DY_madgraphLikeRun2016GH_PTvsETA_HWW.txt')

          self.IsoMuMinRun   = []
          self.IsoMuMaxRun   = []
          self.IsoMuFileData = []
          self.IsoMuFileMC   = []
          self.IsoMuMinRun   .append(1)
          self.IsoMuMaxRun   .append(4)
          self.IsoMuFileData .append(cmssw_base+'/src/LatinoAnalysis/Gardener/python/data/idiso/Full2016/ISOTight_Run2016BCDEF_PTvsETA_HWW.txt')
          self.IsoMuFileMC   .append(cmssw_base+'/src/LatinoAnalysis/Gardener/python/data/idiso/Full2016/ISOTight_DY_madgraphLikeRun2016BCDEF_PTvsETA_HWW.txt')
          self.IsoMuMinRun   .append(5)
          self.IsoMuMaxRun   .append(6)
          self.IsoMuFileData .append(cmssw_base+'/src/LatinoAnalysis/Gardener/python/data/idiso/Full2016/ISOTight_Run2016GH_PTvsETA_HWW.txt')
          self.IsoMuFileMC   .append(cmssw_base+'/src/LatinoAnalysis/Gardener/python/data/idiso/Full2016/ISOTight_DY_madgraphLikeRun2016GH_PTvsETA_HWW.txt')       

        # Muon tracking efficiency
        self.tkMuFile = []
        self.tkMuMinRun = []
        self.tkMuMaxRun = []
        if opts.tkMuFile == None:
          if opts.cmssw == "Full2016" :
            self.tkMuMinRun.append(1)
            self.tkMuMaxRun.append(4)
            self.tkMuMinRun.append(5)
            self.tkMuMaxRun.append(6)
            self.tkMuFile.append(cmssw_base+'/src/LatinoAnalysis/Gardener/python/data/idiso/Full2016/trackerSF_Moriond17_MuoPOG_BCDEF.root')
            self.tkMuFile.append(cmssw_base+'/src/LatinoAnalysis/Gardener/python/data/idiso/Full2016/trackerSF_Moriond17_MuoPOG_GH.root')
        else:
          self.tkMuFile.append(opts.tkMuFile)

        # Electron SF
        if opts.idIsoScaleFactorsFileElectron == None :
          if opts.cmssw == "ICHEP2016" :  opts.idIsoScaleFactorsFileElectron = cmssw_base+'/src/LatinoAnalysis/Gardener/python/data/idiso/ICHEP2016fullLumi/electrons.txt'   
          elif opts.cmssw == "Full2016" :
            if self.idEleKind != None :
              opts.idIsoScaleFactorsFileElectron = cmssw_base+'/src/LatinoAnalysis/Gardener/python/data/idiso/Full2016/electrons_' + self.idEleKind + '.txt'  
          else :  
              opts.idIsoScaleFactorsFileElectron = cmssw_base+'/src/LatinoAnalysis/Gardener/python/data/idiso/electrons_Moriond76x.txt' 
        if opts.cmssw == "ICHEP2016" :  opts.idIsoScaleFactorsFileElectronAlternative = cmssw_base+'/src/LatinoAnalysis/Gardener/python/data/idiso/ICHEP2016fullLumi/electrons_firstPart.txt'   
       
        # Electron GSF Efficiency 
        if opts.tkSCFileElectron == None :
          if opts.cmssw == "ICHEP2016" : 
            opts.tkSCFileElectron = cmssw_base+'/src/LatinoAnalysis/Gardener/python/data/idiso/ICHEP2016fullLumi/egammaEffi.txt_SF2D.root'
      #      opts.tkSCFileElectron = cmssw_base+'/src/LatinoAnalysis/Gardener/python/data/idiso/ICHEP2016/egammaEffi_nVtx.txt_SF2D.root'
          else :
            opts.tkSCFileElectron = cmssw_base+'/src/LatinoAnalysis/Gardener/python/data/idiso/eleRECO.txt.egamma_SF2D.root'
 
          if opts.cmssw == "Full2016" :
            opts.tkSCFileElectron = cmssw_base+'/src/LatinoAnalysis/Gardener/python/data/idiso/Full2016/egammaEffi.txt_EGM2D.root'

 
 
           
        print "opts.idScaleFactorsFileMu = ", opts.idScaleFactorsFileMu
        print "opts.isoTightScaleFactorsFileMu = ", opts.isoTightScaleFactorsFileMu
        print "opts.isoLooseScaleFactorsFileMu = ", opts.isoLooseScaleFactorsFileMu
        print "opts.tkSCFileElectron = ", opts.tkSCFileElectron
        print "opts.idIsoScaleFactorsFileElectron = ", opts.idIsoScaleFactorsFileElectron
        print "opts.idIsoScaleFactorsFileElectronAlternative = ", opts.idIsoScaleFactorsFileElectronAlternative
        print "opts.idEleKind = ", opts.idEleKind
        
        file_idScaleFactorsFileMu  = open (opts.idScaleFactorsFileMu)
        file_isoTightScaleFactorsFileMu  = open (opts.isoTightScaleFactorsFileMu)
        file_isoLooseScaleFactorsFileMu  = open (opts.isoLooseScaleFactorsFileMu)

        file_idIsoScaleFactorsFileElectron = open (opts.idIsoScaleFactorsFileElectron)
        if opts.cmssw == "ICHEP2016" :  file_idIsoScaleFactorsFileElectronAlternative = open (opts.idIsoScaleFactorsFileElectronAlternative)


        self.idIsoScaleFactors = {}
        #                                       create the list               from the line                                if there is no "#"
        self.idIsoScaleFactors['ele']    =    [line.rstrip().split()    for line in file_idIsoScaleFactorsFileElectron     if '#' not in line]
        if opts.cmssw == "ICHEP2016" : 
          self.idIsoScaleFactors['eleAlt'] =    [line.rstrip().split()    for line in file_idIsoScaleFactorsFileElectronAlternative     if '#' not in line]
        if opts.cmssw == "Full2016" :
          for iRun in range(0,len(self.IdMuMinRun)) :
            tag = 'mu_Run'+str(iRun)
            print 'ID Run: ',iRun, tag
            print 'DATA: ' , self.IdMuFileData[iRun]
            print 'MC  : ' , self.IdMuFileMC[iRun] 
            self.idIsoScaleFactors[tag+'_DATA'] = [line.rstrip().split()    for line in open(self.IdMuFileData[iRun])   if '#' not in line]
            self.idIsoScaleFactors[tag+'_MC']   = [line.rstrip().split()    for line in open(self.IdMuFileMC[iRun])     if '#' not in line]
            self.idIsoScaleFactors['mu']    = []
        else: 
          self.idIsoScaleFactors['mu']    =    [line.rstrip().split()    for line in file_idScaleFactorsFileMu              if '#' not in line]

        self.isoScaleFactors = {}
        if opts.cmssw == "Full2016":
          for iRun in range(0,len(self.IsoMuMinRun)) :
            tag = 'muTight_Run'+str(iRun)
            print 'Iso Run: ',iRun, tag
            print 'DATA: ' , self.IsoMuFileData[iRun]
            print 'MC  : ' , self.IsoMuFileMC[iRun]
            self.isoScaleFactors[tag+'_DATA'] = [line.rstrip().split()    for line in open(self.IsoMuFileData[iRun])   if '#' not in line]
            self.isoScaleFactors[tag+'_MC']   = [line.rstrip().split()    for line in open(self.IsoMuFileMC[iRun])     if '#' not in line]
        else:
          self.isoScaleFactors['muTight']   =    [line.rstrip().split()    for line in file_isoTightScaleFactorsFileMu        if '#' not in line]
          self.isoScaleFactors['muLoose']   =    [line.rstrip().split()    for line in file_isoLooseScaleFactorsFileMu        if '#' not in line]

        self.tkMuRootFile = []
        self.tkMuGraph    = []
        self.tkMuValues   = []
        if len(self.tkMuFile) > 0 :
          for iRun in range(0,len(self.tkMuFile)):
            self.tkMuRootFile.append(self._openRootFile(self.tkMuFile[iRun]))
            self.tkMuGraph.append(self._getRootObj(self.tkMuRootFile[iRun],'ratio_eff_vtx_dr030e030_corr'))
            self.tkMuValues.append( self._convGraph2Vec ( self.tkMuGraph[iRun] )  )
            print 'tkMu: ',iRun, self.tkMuFile[iRun] , self.tkMuGraph[iRun]
        #print self.tkMuValues

        self.tkSCElectronRootFile = self._openRootFile(opts.tkSCFileElectron)
        self.tkSCElectronHisto = self._getRootObj(self.tkSCElectronRootFile, 'EGamma_SF2D')



        self.cmssw = opts.cmssw
        self.idIsoScaleFactorsFileElectronAlternativeLumiRatio = opts.idIsoScaleFactorsFileElectronAlternativeLumiRatio


        
        self.minpt_mu = 10
        self.maxpt_mu = 200
        self.mineta_mu = -2.4
        self.maxeta_mu = 2.4
        
        self.minpt_ele = 10
        self.maxpt_ele = 200
        self.mineta_ele = -2.5
        self.maxeta_ele = 2.5

    def _convGraph2Vec(self,graph):
        Vec = []
        for iBin in range (0,graph.GetN()) :
          subVec = []
          x = graph.GetX()[iBin]
          xmin = x - graph.GetEXlow()[iBin]
          xmax = x + graph.GetEXhigh()[iBin]
          y = graph.GetY()[iBin]
          subVec.append(str(xmin))
          subVec.append(str(xmax))
          subVec.append(str(y))
          subVec.append(str(graph.GetEYhigh()[iBin]))
          subVec.append(str(graph.GetEYlow()[iBin]))
          Vec.append(subVec)
        return Vec

    def _getValueNvtx(self,Values, nvtxIn):
        N=len(Values)-1
        vmin = float(Values[0][0])
        vmax = float(Values[N][1])
        nvtx = nvtxIn
        if nvtx < vmin : nvtx = vmin
        if nvtx > vmax : nvtx = vmax-0.001
        for point in Values : 
          if nvtx >= float(point[0]) and nvtx < float(point[1]) : return float(point[2]) , float(point[3]) , float(point[4])
        return 1. , 0., 0.

    def _getHistoValue(self, h2, ptIn, etaIn):
        pt    = ptIn
        eta   = etaIn
        nbins = h2.GetNbinsY()
        ptmax = -1
        if (ptmax <= 0.) : 
          ptmax = h2.GetYaxis().GetBinCenter(nbins)
        
        # eta on x-axis, pt on y-axis
        value = h2.GetBinContent(h2.FindBin(eta, min(pt, ptmax)))
        error = h2.GetBinError  (h2.FindBin(eta, min(pt, ptmax)))
        
        #print ' x,y(max),z,err = ', eta, ' - ', min(pt, ptmax), '(', ptmax, ') - ', value, ' - ', error
        return value, error

    def _getHistoValueRECO(self, h2, pt, eta):

        nbins = h2.GetNbinsY()
        ptmax = -1
        if (ptmax <= 0.) :
          ptmax = h2.GetYaxis().GetBinCenter(nbins)

        # eta on x-axis, pt on y-axis
        etamin = h2.GetXaxis().GetXmin()
        if eta < etamin : eta = etamin
        etamax = h2.GetXaxis().GetXmax()
        if eta > etamax : eta = etamax

        ptmin = h2.GetYaxis().GetXmin()
        if (pt < ptmin) : #because reco histo starts from 20 GeV and no dependency on PT.
          pt = ptmin

        value = h2.GetBinContent(h2.FindBin(eta, min(pt, ptmax)))
        error = h2.GetBinError  (h2.FindBin(eta, min(pt, ptmax)))

        #print ' x,y(max),z,err = ', eta, ' - ', min(pt, ptmax), '(', ptmax, ') - ', value, ' - ', error
        return value, error

    def _getHistoValueNVTX(self, h2, nvtx, eta):

        nbins = h2.GetNbinsY()
        nvtxmax = -1
        if (nvtxmax <= 0.) : 
          nvtxmax = h2.GetYaxis().GetBinCenter(nbins)
        
        # eta on x-axis, nvtx on y-axis
        value = h2.GetBinContent(h2.FindBin(eta, min(nvtx, nvtxmax)))
        error = h2.GetBinError  (h2.FindBin(eta, min(nvtx, nvtxmax)))
        
        return value, error



    #                                              wantOnlyRecoEff = 0 ( idiso scale factors only ), 1 (reco scale factors only), 2 ( idiso * reco scale factors )
    def _getWeight (self, kindLep, pt, eta, tight, wantOnlyRecoEff, nvtx, etaSC, runPeriod):

        # fix underflow and overflow

        # print " kindLep = ", kindLep
        
        if kindLep == 'ele' :          
          if pt < self.minpt_ele:
            pt = self.minpt_ele
          if pt > self.maxpt_ele:
            pt = self.maxpt_ele
          
          if eta < self.mineta_ele:
            eta = self.mineta_ele
          if eta > self.maxeta_ele:
            eta = self.maxeta_ele

        if kindLep == 'mu' :          
          if pt < self.minpt_mu:
            pt = self.minpt_mu
          if pt > self.maxpt_mu:
            pt = self.maxpt_mu
          
          if eta < self.mineta_mu:
            eta = self.mineta_mu
          if eta > self.maxeta_mu:
            eta = self.maxeta_mu
 
 
        #print " self.idIsoScaleFactors = ", self.idIsoScaleFactors
        
        # decide if to use the first period of 2016 electron data
        # or the second period
        toss_a_coin = 1.
        if self.cmssw == "ICHEP2016" : 
          toss_a_coin = ROOT.gRandom.Rndm()
          if kindLep == 'ele' :
            if toss_a_coin < self.idIsoScaleFactorsFileElectronAlternativeLumiRatio: 
              kindLep == 'eleAlt'
        
        # idiso * reco scale factors
        if wantOnlyRecoEff == 2 or wantOnlyRecoEff == 0:
          if kindLep in self.idIsoScaleFactors.keys() : 
            #print " self.idIsoScaleFactors = ", self.idIsoScaleFactors
            #print " eta,pt = ",eta, ", ", pt
            # get the efficiency
            if kindLep == 'ele' :
              #print " self.idIsoScaleFactors[", kindLep, "] = ", self.idIsoScaleFactors[kindLep]
              
              
              tkSC, tkSC_err = self._getHistoValueRECO(self.tkSCElectronHisto, pt, etaSC)
              #tkSC, tkSC_err = self._getHistoValueNVTX(self.tkSCElectronHisto, nvtx, eta)
              
              #print ' pt, eta, tkSC, tkSC_err = ', pt, ' ', eta, ' ', tkSC, ' ', tkSC_err
              
              for point in self.idIsoScaleFactors[kindLep] : 
          
               #            eta       |      pt     | eff_data   stat  |  eff_mc   stat |      other nuisances
               #       -2.500  -2.000  10.000  20.000  0.358   0.009     0.286   0.002       0.094   0.048   0.071   0.127   -1      -1
          
                #
                # Procedure required by EGamma:
                # - electrons scale factors are provided in absolute eta bins
                #    ---------> only for Moriond2016!!!
                if not self.cmssw == "ICHEP2016" : 
                  eta = abs(eta)
          
                if ( eta >= float(point[0]) and eta <= float(point[1]) and         # the "=" in both directions is only used by the overflow bin
                     pt  >= float(point[2]) and pt  <= float(point[3]) ) :         # in other cases the set is (min, max]
                    
                    data = float(point[4])
                    mc   = float(point[6])
          
                    sigma_data = float(point[5])
                    sigma_mc   = float(point[7])
                    
                    scaleFactor = data / mc
                    error_scaleFactor = math.sqrt((sigma_data / mc) * (sigma_data / mc) + (data / mc / mc * sigma_mc)*(data / mc / mc * sigma_mc))
                    
                    # systematic uncertainty
                    error_syst_scaleFactor = math.sqrt( float(point[8]) * float(point[8])   + 
                                                        float(point[9]) * float(point[9])   +
                                                        float(point[10]) * float(point[10]) +
                                                        float(point[11]) * float(point[11])  )
                    
                    error_syst_scaleFactor = error_syst_scaleFactor / mc
                    
                    #  idiso * reco scale factors 
                    if tkSC != 0 and wantOnlyRecoEff == 2:
                      # sum in quadrature the relative uncertainty
                      error_scaleFactor = scaleFactor * math.sqrt(error_scaleFactor/scaleFactor*error_scaleFactor/scaleFactor + tkSC_err/tkSC*tkSC_err/tkSC )
                      # now scale by the correction factor
                      scaleFactor *= tkSC
                      error_scaleFactor *= tkSC 
                      error_syst_scaleFactor *= tkSC 
          
                    return scaleFactor, error_scaleFactor, error_scaleFactor, error_syst_scaleFactor
          
              # default ... it should never happen!
              #print " default ele ???"
              return 1.0, 0.0, 0.0, 0.0
          
          
            elif kindLep == 'mu' :
               
              # Tracker Mu Eff
              tkSC     = 1. 
              tkSC_err = 0.
              if len(self.tkMuFile) == 1 :
                tkSC , tkSC_up , tkSC_do = self._getValueNvtx(self.tkMuValues[0], nvtx)
                # 1% error to cover eta dependence
                tkSC_err = 0.01
              elif len(self.tkMuFile)>1:
                nRun = 0
                for iRun in range(0,len(self.tkMuMinRun)):
                  if runPeriod >= self.tkMuMinRun[iRun] and runPeriod <= self.tkMuMaxRun[iRun] : nRun = iRun
                tkSC , tkSC_up , tkSC_do = self._getValueNvtx(self.tkMuValues[nRun], nvtx)
                # 1% error to cover eta dependence
                tkSC_err = 0.01

              # ID/Iso (after Full2016)
              if self.cmssw == "Full2016" : 
                if tight == 0 : return 1. ,  0. , 0. , 0. 
                #... Iso
                nRun = 0
                for iRun in range(0,len(self.IsoMuMinRun)):
                  if runPeriod >= self.IsoMuMinRun[iRun] and runPeriod <= self.IsoMuMaxRun[iRun] : nRun = iRun
                tag = 'muTight_Run'+str(nRun)
                for point in self.isoScaleFactors[tag+'_DATA'] : 
                  if ( eta >= float(point[0]) and eta <= float(point[1]) and         # the "=" in both directions is only used by the overflow bin
                       pt  >= float(point[2]) and pt  <= float(point[3]) ) :         # in other cases the set is (min, max]
                     dataIso = point
                     break
                for point in self.isoScaleFactors[tag+'_MC'] :
                  if ( eta >= float(point[0]) and eta <= float(point[1]) and         # the "=" in both directions is only used by the overflow bin
                       pt  >= float(point[2]) and pt  <= float(point[3]) ) :         # in other cases the set is (min, max]
                     MCIso = point
                     break

                data = float(dataIso[4])
                mc   = float(MCIso[4])
                sigma_up_data = float(dataIso[5])
                sigma_up_mc   = float(MCIso[5])

                sigma_do_data = float(dataIso[6])
                sigma_do_mc   = float(MCIso[6])              

                iso_scaleFactor = data / mc
                iso_error_scaleFactor_up = (data + sigma_up_data) / (mc - sigma_do_mc)  - iso_scaleFactor
                iso_error_scaleFactor_do = iso_scaleFactor -   (data - sigma_do_data) / (mc + sigma_up_mc)

                #... ID 
                nRun = 0
                for iRun in range(0,len(self.IdMuMinRun)):
                  if runPeriod >= self.IdMuMinRun[iRun] and runPeriod <= self.IdMuMaxRun[iRun] : nRun = iRun
                tag = 'mu_Run'+str(nRun)
                for point in self.idIsoScaleFactors[tag+'_DATA'] :
                  if ( eta >= float(point[0]) and eta <= float(point[1]) and         # the "=" in both directions is only used by the overflow bin
                       pt  >= float(point[2]) and pt  <= float(point[3]) ) :         # in other cases the set is (min, max]
                     dataId = point
                     break
                for point in self.idIsoScaleFactors[tag+'_MC'] :
                  if ( eta >= float(point[0]) and eta <= float(point[1]) and         # the "=" in both directions is only used by the overflow bin
                       pt  >= float(point[2]) and pt  <= float(point[3]) ) :         # in other cases the set is (min, max]
                     MCId = point
                     break

                data = float(dataId[4])
                mc   = float(MCId[4])
                sigma_up_data = float(dataId[5])
                sigma_up_mc   = float(MCId[5])

                sigma_do_data = float(dataId[6])
                sigma_do_mc   = float(MCId[6])

                scaleFactor = data / mc
                error_scaleFactor_up = (data + sigma_up_data) / (mc - sigma_do_mc)  - scaleFactor
                error_scaleFactor_do = scaleFactor -   (data - sigma_do_data) / (mc + sigma_up_mc)

                #print nRun,pt,eta,scaleFactor,iso_scaleFactor
                # multiply for isolation scale factor
                #  -> sum in quadrature the relative uncertainties
                error_scaleFactor_up = scaleFactor * iso_scaleFactor * math.sqrt(error_scaleFactor_up*error_scaleFactor_up/scaleFactor/scaleFactor +  iso_error_scaleFactor_up*iso_error_scaleFactor_up/iso_scaleFactor/iso_scaleFactor)
                error_scaleFactor_do = scaleFactor * iso_scaleFactor * math.sqrt(error_scaleFactor_do*error_scaleFactor_do/scaleFactor/scaleFactor +  iso_error_scaleFactor_do*iso_error_scaleFactor_do/iso_scaleFactor/iso_scaleFactor)
                scaleFactor *= iso_scaleFactor
                      
                #                                                             no systematic uncertainty for the time being
                #print  scaleFactor, error_scaleFactor_do, error_scaleFactor_up, 0.0

                #  idiso * reco scale factors
                if tkSC != 0 and wantOnlyRecoEff == 2:
                      # sum in quadrature the relative uncertainty
                      error_scaleFactor = scaleFactor * math.sqrt(error_scaleFactor/scaleFactor*error_scaleFactor/scaleFactor + tkSC_err/tkSC*tkSC_err/tkSC )
                      # now scale by the correction factor
                      scaleFactor *= tkSC
                      error_scaleFactor *= tkSC
                      error_syst_scaleFactor *= tkSC

                return scaleFactor, error_scaleFactor_do, error_scaleFactor_up, 0.0
          
              # default ... it should never happen!

              # ID/Iso (before Full2016)
              else:
                kindTight = ""
                if tight == 1 :
                  kindTight = "muTight"
                else :
                  kindTight = "muLoose"
                for point in self.isoScaleFactors[kindTight] : 
                  iso_scaleFactor = 1
                  iso_error_scaleFactor_up = 0
                  iso_error_scaleFactor_do = 0
                  
                  if ( eta >= float(point[0]) and eta <= float(point[1]) and         # the "=" in both directions is only used by the overflow bin
                       pt  >= float(point[2]) and pt  <= float(point[3]) ) :         # in other cases the set is (min, max]
                      data = float(point[4])
                      mc   = float(point[7])
            
                      sigma_up_data = float(point[5])
                      sigma_up_mc   = float(point[8])
            
                      sigma_do_data = float(point[6])
                      sigma_do_mc   = float(point[9])
                      
                      iso_scaleFactor = data / mc
                      iso_error_scaleFactor_up = (data + sigma_up_data) / (mc - sigma_do_mc)  - iso_scaleFactor
                      iso_error_scaleFactor_do = iso_scaleFactor -   (data - sigma_do_data) / (mc + sigma_up_mc)  
               
                      break
                
               
                for point in self.idIsoScaleFactors[kindLep] : 
                 #            eta       |      pt     | eff_data   stat up   stat down |  eff_mc   stat up   stat down  |      other nuisances
                 #       -2.500  -2.000  10.000  20.000  0.358   0.009        0.009       0.286   0.002       0.009          0.094   0.048   0.071   0.127   -1      -1
            
                  if ( eta >= float(point[0]) and eta <= float(point[1]) and         # the "=" in both directions is only used by the overflow bin
                       pt  >= float(point[2]) and pt  <= float(point[3]) ) :         # in other cases the set is (min, max]
                      data = float(point[4])
                      mc   = float(point[7])
            
                      sigma_up_data = float(point[5])
                      sigma_up_mc   = float(point[8])
            
                      sigma_do_data = float(point[6])
                      sigma_do_mc   = float(point[9])
                      
                      scaleFactor = data / mc
                      error_scaleFactor_up = (data + sigma_up_data) / (mc - sigma_do_mc)  - scaleFactor
                      error_scaleFactor_do = scaleFactor -   (data - sigma_do_data) / (mc + sigma_up_mc)  
                      
                      # multiply for isolation scale factor
                      #  -> sum in quadrature the relative uncertainties
                      error_scaleFactor_up = scaleFactor * iso_scaleFactor * math.sqrt(error_scaleFactor_up*error_scaleFactor_up/scaleFactor/scaleFactor +  iso_error_scaleFactor_up*iso_error_scaleFactor_up/iso_scaleFactor/iso_scaleFactor)
                      error_scaleFactor_do = scaleFactor * iso_scaleFactor * math.sqrt(error_scaleFactor_do*error_scaleFactor_do/scaleFactor/scaleFactor +  iso_error_scaleFactor_do*iso_error_scaleFactor_do/iso_scaleFactor/iso_scaleFactor)
                      scaleFactor *= iso_scaleFactor
                      
                      #                                                             no systematic uncertainty for the time being
                      return scaleFactor, error_scaleFactor_do, error_scaleFactor_up, 0.0
          
              # default ... it should never happen!
              #print " default mu ???"
              return 1.0, 0.0, 0.0, 0.0
          
          
            # not a lepton ... like some default value: and what can it be if not a lepton? ah ah 
            # --> it happens for default values -9999.
            return 1.0, 0.0, 0.0, 0.0
          
          # not a lepton ... like some default value: and what can it be if not a lepton? ah ah 
          # --> it happens for default values -9999.
          return 1.0, 0.0, 0.0, 0.0
        
        # reco scale factors only
        elif wantOnlyRecoEff == 1:
         
          scaleFactor = 1 
          error_scaleFactor = 0. 
          if kindLep == 'ele' :
            tkSC, tkSC_err = self._getHistoValueRECO(self.tkSCElectronHisto, pt, etaSC)
            scaleFactor *= tkSC
            error_scaleFactor = tkSC_err 
         
          # Tracker Mu Eff
          elif kindLep == 'mu' :
            tkSC     = 1.
            tkSC_err = 0.
            if len(self.tkMuFile) == 1 :
              tkSC , tkSC_up , tkSC_do = self._getValueNvtx(self.tkMuValues[0], nvtx)
              # 1% error to cover eta dependence
              tkSC_err = 0.01
            elif len(self.tkMuFile)>1:
              nRun = 0
              for iRun in range(0,len(self.tkMuMinRun)):
                if runPeriod >= self.tkMuMinRun[iRun] and runPeriod <= self.tkMuMaxRun[iRun] : nRun = iRun
              tkSC , tkSC_up , tkSC_do = self._getValueNvtx(self.tkMuValues[nRun], nvtx)
              # 1% error to cover eta dependence
              tkSC_err = 0.01
            scaleFactor *= tkSC
            error_scaleFactor = tkSC_err 
            
          return scaleFactor, error_scaleFactor, error_scaleFactor, 0
             


   
   
    def process(self,**kwargs):
        tree  = kwargs['tree']
        input = kwargs['input']
        output = kwargs['output']

        self.connect(tree,input)

        self.namesOldBranchesToBeModifiedVector = [
           'std_vector_lepton_recoW',
           'std_vector_lepton_recoW_Up',
           'std_vector_lepton_recoW_Down',                              
           'std_vector_lepton_idisoW',
           'std_vector_lepton_idisoW_Up',
           'std_vector_lepton_idisoW_Down',                              
           'std_vector_lepton_idisoW_Syst',                               
           'std_vector_lepton_idisoLooseW',
           'std_vector_lepton_idisoLooseW_Up',
           'std_vector_lepton_idisoLooseW_Down',                              
           'std_vector_lepton_idisoLooseW_Syst'                              
           ]
        

        
        if self.idEleKind != None :
          self.namesOldBranchesToBeModifiedVector.append(  'std_vector_lepton_idisoW' + self.idEleKind )
          self.namesOldBranchesToBeModifiedVector.append(  'std_vector_lepton_idisoW' + self.idEleKind + '_Up')
          self.namesOldBranchesToBeModifiedVector.append(  'std_vector_lepton_idisoW' + self.idEleKind + '_Down' )

        
        self.clone(output,self.namesOldBranchesToBeModifiedVector)


        bvector_reco =  ROOT.std.vector(float) ()
        self.otree.Branch('std_vector_lepton_recoW',bvector_reco)
        bvector_reco_Up =  ROOT.std.vector(float) ()
        self.otree.Branch('std_vector_lepton_recoW_Up',bvector_reco_Up)
        bvector_reco_Down =  ROOT.std.vector(float) ()
        self.otree.Branch('std_vector_lepton_recoW_Down',bvector_reco_Down)
            
        bvector_idisoLoose =  ROOT.std.vector(float) ()
        self.otree.Branch('std_vector_lepton_idisoLooseW',bvector_idisoLoose)
        bvector_idisoLoose_Up =  ROOT.std.vector(float) ()
        self.otree.Branch('std_vector_lepton_idisoLooseW_Up',bvector_idisoLoose_Up)
        bvector_idisoLoose_Down =  ROOT.std.vector(float) ()
        self.otree.Branch('std_vector_lepton_idisoLooseW_Down',bvector_idisoLoose_Down)
        bvector_idisoLoose_Syst =  ROOT.std.vector(float) ()
        self.otree.Branch('std_vector_lepton_idisoLooseW_Syst',bvector_idisoLoose_Syst)
            

        if self.idEleKind != None :
          bvector_idiso_eleUserDefined =  ROOT.std.vector(float) ()
          self.otree.Branch('std_vector_lepton_idisoW' + self.idEleKind, bvector_idiso_eleUserDefined)
          bvector_idiso_eleUserDefined_Up =  ROOT.std.vector(float) ()
          self.otree.Branch('std_vector_lepton_idisoW' + self.idEleKind + '_Up', bvector_idiso_eleUserDefined_Up)
          bvector_idiso_eleUserDefined_Down =  ROOT.std.vector(float) ()
          self.otree.Branch('std_vector_lepton_idisoW' + self.idEleKind + '_Down', bvector_idiso_eleUserDefined_Down)
          bvector_idiso_eleUserDefined_Syst =  ROOT.std.vector(float) ()
          self.otree.Branch('std_vector_lepton_idisoW' + self.idEleKind + '_Syst', bvector_idiso_eleUserDefined_Syst)

        else :
          bvector_idiso =  ROOT.std.vector(float) ()
          self.otree.Branch('std_vector_lepton_idisoW',bvector_idiso)
          bvector_idiso_Up =  ROOT.std.vector(float) ()
          self.otree.Branch('std_vector_lepton_idisoW_Up',bvector_idiso_Up)
          bvector_idiso_Down =  ROOT.std.vector(float) ()
          self.otree.Branch('std_vector_lepton_idisoW_Down',bvector_idiso_Down)
          bvector_idiso_Syst =  ROOT.std.vector(float) ()
          self.otree.Branch('std_vector_lepton_idisoW_Syst',bvector_idiso_Syst)
            
            
        nentries = self.itree.GetEntries()
        print 'Total number of entries: ',nentries 
        savedentries = 0
                
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

            bvector_reco.clear()
            bvector_reco_Up.clear()
            bvector_reco_Down.clear()

            bvector_idisoLoose.clear()
            bvector_idisoLoose_Up.clear()
            bvector_idisoLoose_Down.clear()
            bvector_idisoLoose_Syst.clear()
            
            if self.idEleKind != None :
              bvector_idiso_eleUserDefined.clear()
              bvector_idiso_eleUserDefined_Up.clear()
              bvector_idiso_eleUserDefined_Down.clear()
              bvector_idiso_eleUserDefined_Syst.clear()
            
            else :
              bvector_idiso.clear()
              bvector_idiso_Up.clear()
              bvector_idiso_Down.clear()
              bvector_idiso_Syst.clear()
  
            runPeriod = -1
            if len(self.tkMuFile)>=2  :
              runPeriod = itree.iRunPeriod 

            for iLep in xrange(len(itree.std_vector_lepton_pt)) :
             
              pt = itree.std_vector_lepton_pt [iLep]
              eta = itree.std_vector_lepton_eta [iLep]
              flavour = itree.std_vector_lepton_flavour [iLep]
              
              kindLep = 'nonlep' # ele or mu
              if abs (flavour) == 11 : 
                kindLep = 'ele'
                etaSC = itree.std_vector_electron_scEta [iLep]
              elif abs (flavour) == 13 :
                kindLep = 'mu'
                etaSC = eta
 
 
              # use the user defined names for id/iso
              if self.idEleKind != None :
                ##                                                              is tight lepton? 1=tight, 0=loose 
                w, error_w_lo, error_w_up, error_w_syst = self._getWeight (kindLep, pt, eta, 1,                   0,     itree.nvtx, etaSC, runPeriod)
               
                #if kindLep == 'ele' : print " kindLep, pt, eta, w, ", kindLep, "  ", pt, "  ", eta, "  ", w
                
                bvector_idiso_eleUserDefined.push_back(w)
                bvector_idiso_eleUserDefined_Up.push_back(w+error_w_up)
                bvector_idiso_eleUserDefined_Down.push_back(w-error_w_lo)             
                bvector_idiso_eleUserDefined_Syst.push_back(w+error_w_syst)             

              else :
               
                #                                                              is tight lepton? 1=tight, 0=loose
                w, error_w_lo, error_w_up, error_w_syst = self._getWeight (kindLep, pt, eta, 1,                   0,     itree.nvtx, etaSC, runPeriod)
               
                #if kindLep == 'ele' : print " kindLep, pt, eta, w, ", kindLep, "  ", pt, "  ", eta, "  ", w
                
                bvector_idiso.push_back(w)
                bvector_idiso_Up.push_back(w+error_w_up)
                bvector_idiso_Down.push_back(w-error_w_lo)             
                bvector_idiso_Syst.push_back(w+error_w_syst)             
  
  
              # the reco and loose (mu) ones are always defined 
              # even if the userDefined electron id is set
              # FIXME: possible improvements: 
              #             - split electrons and muons? -> but then needed to be handled properly in mkShape
              #             - create a matrix of all combinations: different muons id : different electron id -> tihs will absorb the "loose" ad hoc implementation
  
              w, error_w_lo, error_w_up, error_w_syst = self._getWeight (kindLep, pt, eta, 1,                   1,     itree.nvtx, etaSC, runPeriod)
             
              bvector_reco.push_back(w)
              bvector_reco_Up.push_back(w+error_w_up)
              bvector_reco_Down.push_back(w-error_w_lo)             
  
  
  
              loose_w, error_loose_w_lo, error_loose_w_up, error_loose_w_syst = self._getWeight (kindLep, pt, eta, 0,       0,     itree.nvtx, etaSC, runPeriod)
              
              bvector_idisoLoose.push_back(loose_w)
              bvector_idisoLoose_Up.push_back(loose_w+error_loose_w_up)
              bvector_idisoLoose_Down.push_back(loose_w-error_loose_w_lo)             
              bvector_idisoLoose_Syst.push_back(loose_w+error_loose_w_syst)             
  
                

            otree.Fill()
            savedentries+=1

        self.disconnect()
        print '- Eventloop completed'
        print '   Saved: ', savedentries, ' events'


