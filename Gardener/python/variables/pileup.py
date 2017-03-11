from LatinoAnalysis.Gardener.gardening import TreeCloner

import optparse
import numpy
import math
import os.path

#    ___  __  __                 
#   / _ \/ / / /__  ___  ___ ____
#  / ___/ /_/ / _ \/ _ \/ -_) __/
# /_/   \____/ .__/ .__/\__/_/   
#           /_/  /_/             

class PUpper(TreeCloner):
    # ----
    def __init__(self):
        pass

    # ----
    def __del__(self):
        for f in ['datafile','mcfile']:
            if hasattr(self,f) and getattr(self,f) != None:
                getattr(self,f).Close()

    # ----
    def help(self):
        return '''Add a pileup weight according to data and mc distributions'''

    # ----
    def addOptions(self,parser):
        description = self.help()
        group = optparse.OptionGroup(parser,self.label, description)
 
        group.add_option('-d', '--data'    , dest='datafile', help='Name of the input root file with pu histogram from data',)
        group.add_option('-m', '--mc'      , dest='mcfile'  , help='Name of the input root file with pu histogram from mc',)
        group.add_option('-p', '--run'     , dest='run'     , help='Use run dependent PU weights', default=False  , action="store_true")
        group.add_option('-c', '--cmssw'   , dest='cmssw'   , help='CMSSW version for run dependent PU weights',)
        group.add_option('-H', '--HistName', dest='histname', help='Histogram name', default='pileup')
        group.add_option('-k', '--kind'    , dest='kind'    , help='kind of PU reweighting: trpu (= true pu), itpu (= in time pu, that is observed!)',)
        group.add_option('-b', '--branch'  , dest='branch'  , help='Name of the branch of PU weight', default='puW')
        parser.add_option_group(group)

        return group

    # ----
    def checkOptions(self,opts):
        if not (hasattr(opts,'datafile') and 
                hasattr(opts,'kind') ):
            raise RuntimeError('Missing parameter')

        self.kind     = opts.kind
        self.branch   = opts.branch

        self.run   = opts.run
        self.cmssw = opts.cmssw
        self.datafileRun = [] 
        self.datahistRun = [] 
        self.minRun = [] 
        self.maxRun = [] 
        if opts.run:
          if opts.cmssw == 'Full2016' :
            CMSSW=os.environ["CMSSW_BASE"]
            self.minRun.append(1)
            self.maxRun.append(4)
            self.minRun.append(5)
            self.maxRun.append(6)
            self.datafileRun.append( self._openRootFile(CMSSW + '/src/LatinoAnalysis/Gardener/python/data/puweight/PileupHistogram_Full2016_271036-278808_69p2mb_Rereco.root' ) )
            self.datafileRun.append( self._openRootFile(CMSSW + '/src/LatinoAnalysis/Gardener/python/data/puweight/PileupHistogram_Full2016_278820-284044_69p2mb_Rereco.root' ) )
            self.datahistRun.append( self._getRootObj(self.datafileRun[0],opts.histname) )
            self.datahistRun.append( self._getRootObj(self.datafileRun[1],opts.histname) )
          else:
            print '[ERROR] PU Weight : period unknown = ',opts.cmssw 
            exit() 
        else:
          self.minRun.append(1)
          self.maxRun.append(1)
          self.datafileRun.append( self._openRootFile(opts.datafile) )
          self.datahistRun.append( self._getRootObj(self.datafileRun[0],opts.histname) )

        if hasattr(opts,'mcfile') and opts.mcfile != None:
          self.mcfile     = self._openRootFile(opts.mcfile)
          self.mcdist     = self._getRootObj(self.mcfile, opts.histname)
          self.getMCpuFromTree = False
        else :
          print 'measure pu from MC sample tree'
          self.getMCpuFromTree = True
          

    # ----
    def process(self,**kwargs):
        tree  = kwargs['tree']
        input = kwargs['input']
        output = kwargs['output']

        self.connect(tree,input)
        self.clone(output,[self.branch])

        weight = numpy.ones(1, dtype=numpy.float32)
        self.otree.Branch(self.branch,weight,self.branch+'/F')

        puScaleDATA   = []
        puScaleMC     = []
        for iRun in range(0,len(self.minRun)):
          print iRun

          data_nBin     = self.datahistRun[iRun].GetNbinsX()
          data_minValue = self.datahistRun[iRun].GetXaxis().GetXmin()
          data_maxValue = self.datahistRun[iRun].GetXaxis().GetXmax()
          data_dValue   = (data_maxValue - data_minValue) / data_nBin
  
  
          if self.getMCpuFromTree :
            itreePU = self.itreePU
            self.mcdist  = self.datahistRun[iRun].Clone("mcdist")
            for iBin in range(0, data_nBin):
              self.mcdist.SetBinContent(iBin+1, 0)
            itreePU.Draw("trpu >> mcdist")
            
            
  
          mc_nBin       = self.mcdist.GetNbinsX()
          mc_minValue   = self.mcdist.GetXaxis().GetXmin()
          mc_maxValue   = self.mcdist.GetXaxis().GetXmax()
          mc_dValue     = (mc_maxValue - mc_minValue) / mc_nBin
    
          ratio    = mc_dValue/data_dValue
          nBin     = data_nBin
#         minValue = data_minValue
#         maxValue = data_maxValue
          dValue   = data_dValue
   
          print "Data/MC bin Ratio:",ratio
   
          if (ratio - int(ratio)) != 0 :
              raise RuntimeError(" ERROR: incompatible intervals!")
   
          puScaleDATA   .append( numpy.ones(nBin, dtype=numpy.float32) )
          puScaleMC     .append( numpy.ones(nBin, dtype=numpy.float32) )
          puScaleMCtemp = numpy.ones(nBin, dtype=numpy.float32)
  
          for iBin in xrange(0, nBin):
              puScaleDATA[iRun][iBin] = self.datahistRun[iRun].GetBinContent(iBin+1)
              mcbin = int(math.floor(iBin / ratio))
              puScaleMCtemp[iBin] = self.mcdist.GetBinContent(mcbin+1)
  
   
          integralDATA = 0.
          integralMC   = 0.
   
          for iBin in range(0, nBin):
              integralDATA += puScaleDATA[iRun][iBin]
              integralMC   += puScaleMCtemp[iBin]
  
          print "Integrals: data = %.3f, mc = %3f" % (integralDATA,integralMC)
   
          for iBin in xrange(nBin):
              puScaleMC[iRun][iBin] =  puScaleMCtemp[iBin] * integralDATA / integralMC

        # start loop on tree
 
        nentries = self.itree.GetEntries()
        print 'Total number of entries: ',nentries
        
        # this is for speed
        leaf = self.kind 
        itree = self.itree
        otree = self.otree
        
        print '- Starting eventloop'
        step = 5000
        for i in xrange(nentries):
            itree.GetEntry(i)

            ## print event count
            if i > 0 and i%step == 0.:
                print i,'events processed.'

            nRun = 0
            if self.run:
                runPeriod = itree.iRunPeriod
                for iRun in range(0,len(self.minRun)):
                  if runPeriod >= self.minRun[iRun] and runPeriod <= self.maxRun[iRun] : nRun = iRun
            weight[0] = 1.

            ## true pu reweighting 
            ibin = int(getattr(itree,leaf) / dValue)
            if ibin >= len(puScaleDATA[nRun]) : ibin = len(puScaleDATA[nRun])-1

            if puScaleMC[nRun][ibin] != 0 :
                weight[0] = 1. * puScaleDATA[nRun][ibin] / puScaleMC[nRun][ibin]
            else:
                weight[0] = 1.
            
            otree.Fill()

        self.disconnect(False)
        print '- Eventloop completed'


