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

class LeptonSF():

    def _openRootFile(self,path, option=''):
        f =  ROOT.TFile.Open(path,option)
        if not f.__nonzero__() or not f.IsOpen():
            raise NameError('File '+path+' not open')
        return f

    def _getRootObj(self,d,name):
        o = d.Get(name)
        if not o.__nonzero__():
            print 'Object '+name+' doesn\'t exist in '+d.GetName(), ' BE CAREFUL!'
        return o

    def __init__ (self,kind,cmssw,WPDic,WPType,WP):
        print  "-------- Lepton SF init() ---------"
        print kind,WPType,WP

        cmssw_base = os.getenv('CMSSW_BASE')

        self.kind   = abs(kind)
        self.WPType = WPType
        self.WP     = WP

        # for rounding issues of TH2F, actually only maxeta_ele=2.5 causes a problem
        self.minpt_mu = 10.0001
        self.maxpt_mu = 199.9999
        self.mineta_mu = -2.3999
        self.maxeta_mu = 2.3999

        self.minpt_ele = 10.0001
        self.maxpt_ele = 199.9999
        self.mineta_ele = -2.4999
        self.maxeta_ele = 2.4999

        # Tracker SF

        self.tkSF     = False
        self.tkFile   = []
        self.tkHisto  = []
        self.tkValues = []
        self.tkMinRun = []
        self.tkMaxRun = []

        if 'tkSF' in WPDic[cmssw][WPType][WP] :
          self.tkSF = True
          iRR=0
          for iRunRange in  WPDic[cmssw][WPType][WP]['tkSF'] : 
            iFirstRun = int(iRunRange.split('-')[0])
            iLastRun  = int(iRunRange.split('-')[1])
            tkSFFile  = cmssw_base+'/src/'+WPDic[cmssw][WPType][WP]['tkSF'][iRunRange]
            self.tkFile   .append(self._openRootFile(tkSFFile))
            if self.kind == int(11) :
              self.tkHisto  .append(self._getRootObj(self.tkFile[iRR], 'EGamma_SF2D'))
            if self.kind == int(13) :
              self.tkHisto  .append(self._getRootObj(self.tkFile[iRR], 'ratio_eff_vtx_dr030e030_corr')) 
              self.tkValues .append(self._convGraph2Vec ( self.tkHisto[iRR] ))
            self.tkMinRun .append(iFirstRun)
            self.tkMaxRun .append(iLastRun) 
            iRR+=1

        self.idIsoScaleFactors = {} 
        # WP global SF (used for electrons)
        if self.kind == int(11) : 
          
          self.wpSF     = False
          self.wpFile   = []
          self.wpMinRun = []
          self.wpMaxRun = []

          if 'wpSF' in WPDic[cmssw][WPType][WP] :
            self.wpSF     = True
            iRR=0
            for iRunRange in  WPDic[cmssw][WPType][WP]['wpSF'] :
              iFirstRun = int(iRunRange.split('-')[0])
              iLastRun  = int(iRunRange.split('-')[1])
              SFFile    = cmssw_base+'/src/'+WPDic[cmssw][WPType][WP]['wpSF'][iRunRange] 
              tag       = 'ele_RR'+str(iRR)
              self.idIsoScaleFactors[tag] = [line.rstrip().split()    for line in open(SFFile)    if '#' not in line]  
              iRR+=1

        # Id and Iso SF (used for muons)
        if self.kind == int(13) : 

          # ID
          self.idSF     = False
          self.idFile   = []
          self.idMinRun = []
          self.idMaxRun = []

          if 'idSF' in WPDic[cmssw][WPType][WP] :
            self.idSF     = True
            iRR=0
            for iRunRange in  WPDic[cmssw][WPType][WP]['idSF'] :
              iFirstRun = int(iRunRange.split('-')[0])
              iLastRun  = int(iRunRange.split('-')[1])
              SFFile_Data    = cmssw_base+'/src/'+WPDic[cmssw][WPType][WP]['idSF'][iRunRange][0]
              SFFile_MC      = cmssw_base+'/src/'+WPDic[cmssw][WPType][WP]['idSF'][iRunRange][1]
              tag       = 'mu_id_RR'+str(iRR)+'_DATA' 
              self.idIsoScaleFactors[tag] = [line.rstrip().split()    for line in open(SFFile_Data)   if '#' not in line]   
              tag       = 'mu_id_RR'+str(iRR)+'_MC' 
              self.idIsoScaleFactors[tag] = [line.rstrip().split()    for line in open(SFFile_MC)     if '#' not in line]   
              iRR+=1

          # Isolation
          self.isoSF     = False
          self.isoFile   = []
          self.isoMinRun = []
          self.isoMaxRun = []

          if 'isoSF' in WPDic[cmssw][WPType][WP] :
            self.isoSF     = True
            iRR=0
            for iRunRange in  WPDic[cmssw][WPType][WP]['isoSF'] :
              iFirstRun = int(iRunRange.split('-')[0])
              iLastRun  = int(iRunRange.split('-')[1])
              SFFile_Data    = cmssw_base+'/src/'+WPDic[cmssw][WPType][WP]['isoSF'][iRunRange][0]
              SFFile_MC      = cmssw_base+'/src/'+WPDic[cmssw][WPType][WP]['isoSF'][iRunRange][1]
              tag       = 'mu_iso_RR'+str(iRR)+'_DATA'
              self.idIsoScaleFactors[tag] = [line.rstrip().split()    for line in open(SFFile_Data)   if '#' not in line]                      
              tag       = 'mu_iso_RR'+str(iRR)+'_MC'  
              self.idIsoScaleFactors[tag] = [line.rstrip().split()    for line in open(SFFile_MC)     if '#' not in line]
              iRR+=1

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

    def _getRecoW(self,kindLep, pt_In, eta_In, nvtx_In, runPeriod):

        # Eta/Pt boundaries
        pt   = pt_In
        eta  = eta_In
        nvtx = nvtx_In

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

        # Get RunRange
        nRun = 0
        for iRun in range(0,len(self.tkMinRun)):
          if runPeriod >= self.tkMinRun[iRun] and runPeriod <= self.tkMaxRun[iRun] : nRun = iRun

        # Get SF 
        tkSC     = 1.0
        tkSC_err = 0.0
 
        if kindLep == 'ele' :
          tkSC, tkSC_err = self._getHistoValueRECO(self.tkHisto[nRun], pt, eta)
 
        if kindLep == 'mu' :
          tkSC , tkSC_up , tkSC_do = self._getValueNvtx(self.tkValues[nRun], nvtx)
          # 1% error to cover eta dependence
          tkSC_err = 0.01

        return tkSC,tkSC_err,tkSC_err    

    def _getIdIsoW(self,kindLep, pt_In, eta_In, runPeriod):

        # Eta/Pt boundaries
        pt   = pt_In
        eta  = eta_In

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

        # Get RunRange
        nRun = 0
        for iRun in range(0,len(self.tkMinRun)):
          if runPeriod >= self.tkMinRun[iRun] and runPeriod <= self.tkMaxRun[iRun] : nRun = iRun

        # default weight
        scaleFactor           =  1.0
        error_scaleFactor_up  =  0.0
        error_scaleFactor_do  =  0.0 
        scaleFactor_syst      =  0.0

        # Electron SF
        if kindLep == 'ele' :
          tag = 'ele_RR'+str(nRun)
          for point in self.idIsoScaleFactors[tag] :
              #            eta       |      pt     | eff_data   stat  |  eff_mc   stat |      other nuisances
               #       -2.500  -2.000  10.000  20.000  0.358   0.009     0.286   0.002       0.094   0.048   0.071   0.127   -1      -1

                #
                # Procedure required by EGamma:
                # - electrons scale factors are provided in absolute eta bins
                #    ---------> only for Moriond2016!!!
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

                    return scaleFactor, error_scaleFactor, error_scaleFactor, error_syst_scaleFactor
 

        # Muon SF   
        if kindLep == 'mu' :
                # Iso
                tag = 'mu_iso_RR'+str(nRun)
                #print eta,pt
                for point in self.idIsoScaleFactors[tag+'_DATA'] :
                  if ( eta >= float(point[0]) and eta <= float(point[1]) and         # the "=" in both directions is only used by the overflow bin
                       pt  >= float(point[2]) and pt  <= float(point[3]) ) :         # in other cases the set is (min, max]
                     dataIso = point
                 #    print  dataIso
                     break
                for point in self.idIsoScaleFactors[tag+'_MC'] :
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

                # ID
                tag = 'mu_id_RR'+str(nRun)
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

                # multiply for isolation scale factor
                #  -> sum in quadrature the relative uncertainties
                error_scaleFactor_up = scaleFactor * iso_scaleFactor * math.sqrt(error_scaleFactor_up*error_scaleFactor_up/scaleFactor/scaleFactor +  iso_error_scaleFactor_up*iso_error_scaleFactor_up/iso_scaleFactor/iso_scaleFactor)
                error_scaleFactor_do = scaleFactor * iso_scaleFactor * math.sqrt(error_scaleFactor_do*error_scaleFactor_do/scaleFactor/scaleFactor +  iso_error_scaleFactor_do*iso_error_scaleFactor_do/iso_scaleFactor/iso_scaleFactor)
                scaleFactor *= iso_scaleFactor

                return scaleFactor, error_scaleFactor_do, error_scaleFactor_up, 0.0


        # Return DEFAULT values (should never happen)
        print 'Id/Iso: why am I here ?' 
        return scaleFactor , error_scaleFactor_up , error_scaleFactor_do , scaleFactor_syst

class MultiIdIsoSFFiller(TreeCloner):

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
        group.add_option('-w', '--wpdic',   dest='WPdic', help='WP Dictionnary', default='LatinoAnalysis/Gardener/python/variables/LeptonSel_cfg.py', type='string')

        parser.add_option_group(group)
        return group

    def checkOptions(self,opts):

        self.cmssw = opts.cmssw
        print " cmssw = ", self.cmssw
        cmssw_base = os.getenv('CMSSW_BASE')
        self.WPdic = cmssw_base+'/src/'+opts.WPdic
        print self.WPdic
        if os.path.exists(self.WPdic) :
          handle = open(self.WPdic,'r')
          exec(handle)
          handle.close()
        else:
          print 'ERROR: No WP'
          exit()

        # Create Elecron SF
        self.FirstElectronWP = 'NONE'
        self.TightObjElectronSFs  = {}
        if self.cmssw in ElectronWP :
          if 'TightObjWP' in ElectronWP[self.cmssw] :
            for iWP in ElectronWP[self.cmssw]['TightObjWP']  :
              if self.FirstElectronWP == 'NONE' : self.FirstElectronWP = iWP
              self.TightObjElectronSFs[iWP]  = LeptonSF(11,self.cmssw,ElectronWP,'TightObjWP',iWP)

        # Create Muon SF
        self.FirstMuonWP = 'NONE'
        self.TightObjMuonSFs  = {}
        if self.cmssw in MuonWP :
          if 'TightObjWP' in MuonWP[self.cmssw] :
            for iWP in MuonWP[self.cmssw]['TightObjWP'] : 
              if self.FirstMuonWP == 'NONE' : self.FirstMuonWP = iWP
              self.TightObjMuonSFs[iWP] = LeptonSF(13,self.cmssw,MuonWP,'TightObjWP',iWP)


    def process(self,**kwargs):


        tree  = kwargs['tree']
        input = kwargs['input']
        output = kwargs['output']

        self.connect(tree,input)

        # (Re)Create target variables
   
        # .... recoW unique for all WP (will take from first WP)
        self.namesOldBranchesToBeModifiedVector = [
           'std_vector_lepton_recoW',
           'std_vector_lepton_recoW_Up',
           'std_vector_lepton_recoW_Down'
        ]

        # .... ID/Iso are per WP
        for iWP in self.TightObjElectronSFs :
           self.namesOldBranchesToBeModifiedVector.append('std_vector_electron_idisoW_'+iWP)          
           self.namesOldBranchesToBeModifiedVector.append('std_vector_electron_idisoW_'+iWP+'_Up')          
           self.namesOldBranchesToBeModifiedVector.append('std_vector_electron_idisoW_'+iWP+'_Down')          
           self.namesOldBranchesToBeModifiedVector.append('std_vector_electron_idisoW_'+iWP+'_Syst')          
        for iWP in self.TightObjMuonSFs :
           self.namesOldBranchesToBeModifiedVector.append('std_vector_muon_idisoW_'+iWP)    
           self.namesOldBranchesToBeModifiedVector.append('std_vector_muon_idisoW_'+iWP+'_Up')         
           self.namesOldBranchesToBeModifiedVector.append('std_vector_muon_idisoW_'+iWP+'_Down')    
           self.namesOldBranchesToBeModifiedVector.append('std_vector_muon_idisoW_'+iWP+'_Syst')

        # NOW WE CAN CLONE THE TREE
        self.clone(output,self.namesOldBranchesToBeModifiedVector)

        # NOW CONNECT ALL NEW/TO BE MODIFIED BRANCEHES
        self.oldBranchesToBeModifiedVector = {}
        for bname in self.namesOldBranchesToBeModifiedVector:
          bvector =  ROOT.std.vector(float) ()
          self.oldBranchesToBeModifiedVector[bname] = bvector
        for bname, bvector in self.oldBranchesToBeModifiedVector.iteritems(): self.otree.Branch(bname,bvector)

        #----------------------------------------------------------------------------------------------------
        # START TREE LOOP
        nentries = self.itree.GetEntries()
        savedentries = 0
        print 'Total number of entries: ',nentries
        print '- Starting eventloop'
        step = 5000

        # avoid dots to go faster
        itree     = self.itree
        otree     = self.otree


        for i in xrange(nentries):

            itree.GetEntry(i)

            if i > 0 and i%step == 0.:
                print i,'events processed :: ', nentries

            # Clear all vectors
            for bname, bvector in self.oldBranchesToBeModifiedVector.iteritems() : bvector.clear()

            # Get Run period
            runPeriod = itree.iRunPeriod

            # Loop on leptons
            for iLep in xrange(len(itree.std_vector_lepton_pt)) :

              pt  = itree.std_vector_lepton_pt [iLep]
              eta = itree.std_vector_lepton_eta [iLep]
              flavour = itree.std_vector_lepton_flavour [iLep]
              if   abs (flavour) == 11 : etaSC = itree.std_vector_electron_scEta [iLep]
              else : etaSC = -9999.0
              nvtx = itree.nvtx             
 
              # Reco Weight (Unique for all WP --> Use first WP
              w          = 1.
              error_w_lo = 0.
              error_w_up = 0.
              if   abs (flavour) == 11 and len(self.TightObjElectronSFs) > 0 :
                 w, error_w_lo, error_w_up = self.TightObjElectronSFs[self.FirstElectronWP]._getRecoW( 'ele' , pt , etaSC , nvtx , runPeriod )
              elif abs (flavour) == 13 and len(self.TightObjMuonSFs) > 0 :
                 w, error_w_lo, error_w_up = self.TightObjMuonSFs[self.FirstMuonWP]._getRecoW( 'mu' ,  pt , eta , nvtx , runPeriod )
              self.oldBranchesToBeModifiedVector['std_vector_lepton_recoW']      .push_back(w)
              self.oldBranchesToBeModifiedVector['std_vector_lepton_recoW_Up']   .push_back(w+error_w_up)    
              self.oldBranchesToBeModifiedVector['std_vector_lepton_recoW_Down'] .push_back(w-error_w_lo)    
 

              # Electron SF
              for iWP in self.TightObjElectronSFs :
                w            = 1.
                error_w_lo   = 0.
                error_w_up   = 0.
                error_w_syst = 0.
                if   abs (flavour) == 11 :
                  w, error_w_lo, error_w_up, error_w_syst = self.TightObjElectronSFs[iWP]._getIdIsoW( 'ele' , pt , etaSC , runPeriod )
                self.oldBranchesToBeModifiedVector['std_vector_electron_idisoW_'+iWP]          .push_back(w)
                self.oldBranchesToBeModifiedVector['std_vector_electron_idisoW_'+iWP+'_Up']    .push_back(w+error_w_up)
                self.oldBranchesToBeModifiedVector['std_vector_electron_idisoW_'+iWP+'_Down']  .push_back(w-error_w_lo)
                self.oldBranchesToBeModifiedVector['std_vector_electron_idisoW_'+iWP+'_Syst']  .push_back(w+error_w_syst)

              # Muon SF
              for iWP in self.TightObjMuonSFs :
                w            = 1.
                error_w_lo   = 0.
                error_w_up   = 0.
                error_w_syst = 0.
                if   abs (flavour) == 13 :
                  w, error_w_lo, error_w_up, error_w_syst = self.TightObjMuonSFs[iWP]._getIdIsoW( 'mu' ,  pt , eta , runPeriod )
                self.oldBranchesToBeModifiedVector['std_vector_muon_idisoW_'+iWP]          .push_back(w)
                self.oldBranchesToBeModifiedVector['std_vector_muon_idisoW_'+iWP+'_Up']    .push_back(w+error_w_up)
                self.oldBranchesToBeModifiedVector['std_vector_muon_idisoW_'+iWP+'_Down']  .push_back(w-error_w_lo)
                self.oldBranchesToBeModifiedVector['std_vector_muon_idisoW_'+iWP+'_Syst']  .push_back(w+error_w_syst)


            otree.Fill()
            savedentries+=1

        self.disconnect()
        print '- Eventloop completed'
        print '   Saved: ', savedentries, ' events'


 
