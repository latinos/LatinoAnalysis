#!/usr/bin/env python
#import os

import optparse
import LatinoAnalysis.Gardener.hwwtools as hwwtools
import math

#import ROOT
#from ROOT import *
#from ROOT import gBenchmark, gStyle, gROOT, TStyle
from ROOT import TCanvas, TPad, TFile, TPaveText, TLegend
from ROOT import TH1D, TH1F, TF1, TGraphErrors, TMultiGraph

# functions used in everyday life ...
from LatinoAnalysis.Tools.commonTools import *


if __name__ == '__main__':

    usage = 'usage: %prog [options]'
    parser = optparse.OptionParser(usage)
    
    parser.add_option('--dycfg'          , dest='dycfg'          , help='DY estimation dictionary'                   , default='dyestim.py') 
    parser.add_option('--outputDir'      , dest='outputDir'      , help='output directory'                           , default='./')
    parser.add_option('--tag'            , dest='tag'            , help='Tag used for the shape file name'           , default=None)
    parser.add_option('--DYtag'          , dest='DYtag'          , help='Tag added to the shape file name'           , default='DYEstimDATA')
    parser.add_option('--inputFile'      , dest='inputFile'      , help='input file with histograms'                 , default='DEFAULT')
    parser.add_option('--outputFile'     , dest='outputFile'     , help='output file with histograms'                , default='DEFAULT')
 
    # read default parsing options as well
    hwwtools.addOptions(parser)
    hwwtools.loadOptDefaults(parser)
    (opt, args) = parser.parse_args()

    print " configuration file = ", opt.pycfg
    print " DY estimation Cfg  = ", opt.dycfg

    # Set Input file
    if opt.inputFile == 'DEFAULT' :
      opt.inputFile = opt.outputDir+'/plots_'+opt.tag+'.root'
    print " inputFile      =          ", opt.inputFile

    # Set Output file
    if opt.outputFile == 'DEFAULT' :
      opt.outputFile = opt.outputDir+'/plots_'+opt.tag+'_'+opt.DYtag+'.root'
    print " outputFile    =          ", opt.outputFile

    # Create Needed dictionnary
    variables = {}
    if os.path.exists(opt.variablesFile) :
      handle = open(opt.variablesFile,'r')
      exec(handle)
      handle.close()

    samples = {}
    if os.path.exists(opt.samplesFile) :
      handle = open(opt.samplesFile,'r')
      exec(handle)
      handle.close()

    cuts = {}
    if os.path.exists(opt.cutsFile) :
      handle = open(opt.cutsFile,'r')
      exec(handle)
      handle.close()

    RAndKff = {}
    DYestim = {}
    if os.path.exists(opt.dycfg) :
      handle = open(opt.dycfg,'r')
      exec(handle)
      handle.close()

    print RAndKff

    # Load C  
    cmssw_base = os.getenv('CMSSW_BASE')
    try:
      ROOT.gROOT.LoadMacro(cmssw_base+'/src/LatinoAnalysis/ShapeAnalysis/src/DYEST.C+g')
    except RuntimeError:
      ROOT.gROOT.LoadMacro(cmssw_base+'/src/LatinoAnalysis/ShapeAnalysis/src/DYEST.C++g')


    DYCalc = ROOT.DYCalc()

    # Compute Rinout and K_ff
    Rinout          = {}
    K_ff            = {}
    K_ff_data       = {}
    K_ff_data_value = {}
    Rfile           = {}
    Kfile           = {}
    thelist         = {}
    DataR           = {}

    for iRAndKff in RAndKff :
      Rinout[iRAndKff]          = {}
      Rfile[iRAndKff]           = {}
      Kfile[iRAndKff]           = {}
      thelist[iRAndKff]         = {}
      DataR[iRAndKff]           = {}
      K_ff[iRAndKff]            = {}
      K_ff_data[iRAndKff]       = {}
      K_ff_data_value[iRAndKff] = {}

      print iRAndKff

      # Input: dyestim.py file in configuration folder
      for iRegion in RAndKff[iRAndKff]['Regions']: 
        print iRegion

        #       print iRegion ,' k = ' , DYCalc.k_MC(RAndKff[iRAndKff]['KffFile'],RAndKff[iRAndKff]['Regions'][iRegion]['kNum'],RAndKff[iRAndKff]['Regions'][iRegion]['kDen']),' +/- ', DYCalc.Ek_MC(RAndKff[iRAndKff]['KffFile'],RAndKff[iRAndKff]['Regions'][iRegion]['kNum'],RAndKff[iRAndKff]['Regions'][iRegion]['kDen'])
        #       print iRegion ,' R = ' , DYCalc.R_outin_MC(RAndKff[iRAndKff]['RFile'],RAndKff[iRAndKff]['Regions'][iRegion]['RNum'],RAndKff[iRAndKff]['Regions'][iRegion]['RDen']),' +/- ', DYCalc.ER_outin_MC(RAndKff[iRAndKff]['RFile'],RAndKff[iRAndKff]['Regions'][iRegion]['RNum'],RAndKff[iRAndKff]['Regions'][iRegion]['RDen'])

        # Compute K and its uncertainty - using MC
        print("Starting with MC")

        K_ff[iRAndKff][iRegion] = {} 
        RAndKff[iRAndKff]['KffFile'], RAndKff[iRAndKff]['Regions']
        K_ff[iRAndKff][iRegion]['val'] = DYCalc.k_MC(RAndKff[iRAndKff]['KffFile'],
                                                     RAndKff[iRAndKff]['Regions'][iRegion]['kNum'] + "/events/histo_DY",
                                                     RAndKff[iRAndKff]['Regions'][iRegion]['kDen'] + "/events/histo_DY")

        K_ff[iRAndKff][iRegion]['err'] = DYCalc.Ek_MC(RAndKff[iRAndKff]['KffFile'],
                                                      RAndKff[iRAndKff]['Regions'][iRegion]['kNum'] + "/events/histo_DY",
                                                      RAndKff[iRAndKff]['Regions'][iRegion]['kDen'] + "/events/histo_DY")

        print("MC:")
        print("K value from MC: {} +- {}".format(K_ff[iRAndKff][iRegion]['val'], K_ff[iRAndKff][iRegion]['err']))


        # Compute K and its uncertainty - using DATA
        # Open input rootfile
        K_ff_data[iRAndKff][iRegion] = {}
        K_ff_data_value[iRAndKff][iRegion] = {}

        print 'K file = ', RAndKff[iRAndKff]['KffFile']
        Kfile[iRAndKff]   = TFile(RAndKff[iRAndKff]['KffFile'])
        thelist[iRAndKff] = Kfile[iRAndKff].GetListOfKeys()

        # Prepare numerator and denominator for K computation
        for dirs in thelist[iRAndKff] :
          # K numerator
          if RAndKff[iRAndKff]['Regions'][iRegion]['kNum'] in dirs.GetName():
            currentdir = dirs.ReadObj()
            for subdir in currentdir.GetListOfKeys():
              if subdir.GetName()!='events':
                continue
              # Numerator: starting with total data in the actual channel (ee or mm)
              K_ff_data[iRAndKff][iRegion]['NumDATA'] = Kfile[iRAndKff].Get(dirs.GetName()+'/'+subdir.GetName()+'/histo_DATA')
              K_ff_data[iRAndKff][iRegion]['kNum']    = TH1D.Clone(K_ff_data[iRAndKff][iRegion]['NumDATA'])
              print("Total data = {}".format(K_ff_data[iRAndKff][iRegion]['kNum'].Integral()))
              currentsubdir = subdir.ReadObj()
              previoussample=''
              for sample in currentsubdir.GetListOfKeys():
                if sample.GetName()==previoussample:
                  continue
                previoussample = sample.GetName()
                # Numerator: subtract backgrounds
                if not 'histo_DY' in sample.GetName() and not 'histo_DATA' in sample.GetName():
                  K_ff_data[iRAndKff][iRegion][sample.GetName()] = Kfile[iRAndKff].Get(dirs.GetName()+'/'+subdir.GetName()+'/'+sample.GetName())
                  K_ff_data[iRAndKff][iRegion]['kNum'].Add(K_ff_data[iRAndKff][iRegion][sample.GetName()],-1)

          # K denominator
          if RAndKff[iRAndKff]['Regions'][iRegion]['kDen'] in dirs.GetName():
            currentdir = dirs.ReadObj()
            currentdir = dirs.ReadObj()
            for subdir in currentdir.GetListOfKeys():
              if subdir.GetName()!='events':
                continue
              # Denominator: starting with total data in opposite channel (mm or ee)
              K_ff_data[iRAndKff][iRegion]['DenDATA'] = Kfile[iRAndKff].Get(dirs.GetName()+'/'+subdir.GetName()+'/histo_DATA')
              K_ff_data[iRAndKff][iRegion]['kDen']    = TH1D.Clone(K_ff_data[iRAndKff][iRegion]['DenDATA'])
              currentsubdir = subdir.ReadObj()
              previoussample=''
              for sample in currentsubdir.GetListOfKeys():
                if sample.GetName()==previoussample:
                  continue
                previoussample = sample.GetName()
                # Denominator: subtract backgrounds
                if not 'histo_DY' in sample.GetName() and not 'histo_DATA' in sample.GetName():
                  K_ff_data[iRAndKff][iRegion][sample.GetName()] = Kfile[iRAndKff].Get(dirs.GetName()+'/'+subdir.GetName()+'/'+sample.GetName())
                  K_ff_data[iRAndKff][iRegion]['kDen'].Add(K_ff_data[iRAndKff][iRegion][sample.GetName()],-1)
                
        # Compute K
        K_ff_data[iRAndKff][iRegion]['val'] = TH1F("k_ff_data", "k_ff_data", 1, 0, 2)
        K_ff_data[iRAndKff][iRegion]['val'].Divide(K_ff_data[iRAndKff][iRegion]['kNum'], K_ff_data[iRAndKff][iRegion]['kDen'], 1, 1, "b")
        K_ff_data_value[iRAndKff][iRegion]['val'] = math.sqrt(K_ff_data[iRAndKff][iRegion]['val'].GetBinContent(1))
        k_err_num = K_ff_data[iRAndKff][iRegion]['kNum'].GetBinError(1) / K_ff_data[iRAndKff][iRegion]['kNum'].Integral()
        k_err_den = K_ff_data[iRAndKff][iRegion]['kDen'].GetBinError(1) / K_ff_data[iRAndKff][iRegion]['kDen'].Integral()
        K_ff_data_value[iRAndKff][iRegion]['err'] = 0.5 * math.sqrt(k_err_num*k_err_num + k_err_den*k_err_den) * K_ff_data_value[iRAndKff][iRegion]['val']

        print("DATA:")
        print("k numerator   = {} )".format(K_ff_data[iRAndKff][iRegion]['kNum'].Integral() ) )
        print("k denominator = {} )".format(K_ff_data[iRAndKff][iRegion]['kDen'].Integral() ) )
        print 'K from data = ', K_ff_data_value[iRAndKff][iRegion]['val'], ' +/- ', K_ff_data_value[iRAndKff][iRegion]['err'] 

        # Put the value computed in data into the variable used for MC
        K_ff[iRAndKff][iRegion]['val'] = K_ff_data_value[iRAndKff][iRegion]['val']
        K_ff[iRAndKff][iRegion]['err'] = K_ff_data_value[iRAndKff][iRegion]['err']


        # Compute R(out/in) and its uncertainty
        Rinout[iRAndKff][iRegion] = {}
        DataR[iRAndKff][iRegion]  = {}
        # Open input rootfile
        print 'file = ', RAndKff[iRAndKff]['RFile']
        Rfile[iRAndKff] = TFile(RAndKff[iRAndKff]['RFile'])
        thelist[iRAndKff] = Rfile[iRAndKff].GetListOfKeys()

        # Prepare numerator and denominator for R computation
        for dirs in thelist[iRAndKff] :
          # R numerator
          if RAndKff[iRAndKff]['Regions'][iRegion]['RNum'] in dirs.GetName():
            currentdir = dirs.ReadObj()
            for subdir in currentdir.GetListOfKeys():
              if subdir.GetName()!='events':
                continue
              # Numerator: starting with total data in OUT region
              DataR[iRAndKff][iRegion]['NumDATA'] = Rfile[iRAndKff].Get(dirs.GetName()+'/'+subdir.GetName()+'/histo_DATA')
              DataR[iRAndKff][iRegion]['RNum'] = TH1D.Clone(DataR[iRAndKff][iRegion]['NumDATA'])
              currentsubdir = subdir.ReadObj()
              previoussample=''
              for sample in currentsubdir.GetListOfKeys():
                if sample.GetName()==previoussample:
                  continue
                previoussample = sample.GetName()
                # Numerator: subtract backgrounds
                if not 'histo_DY' in sample.GetName() and not 'histo_DATA' in sample.GetName():
                  DataR[iRAndKff][iRegion][sample.GetName()]= Rfile[iRAndKff].Get(dirs.GetName()+'/'+subdir.GetName()+'/'+sample.GetName())
                  DataR[iRAndKff][iRegion]['RNum'].Add(DataR[iRAndKff][iRegion][sample.GetName()],-1)

          # R denominator
          if RAndKff[iRAndKff]['Regions'][iRegion]['RDen'] in dirs.GetName():
            currentdir = dirs.ReadObj()
            currentdir = dirs.ReadObj()
            for subdir in currentdir.GetListOfKeys():
              if subdir.GetName()!='events':
                continue
              # Denominator: starting with total data in IN region
              DataR[iRAndKff][iRegion]['DenDATA'] = Rfile[iRAndKff].Get(dirs.GetName()+'/'+subdir.GetName()+'/histo_DATA')
              DataR[iRAndKff][iRegion]['RDen'] = TH1D.Clone(DataR[iRAndKff][iRegion]['DenDATA'])
              currentsubdir = subdir.ReadObj()
              previoussample=''
              for sample in currentsubdir.GetListOfKeys():
                if sample.GetName()==previoussample:
                  continue
                previoussample = sample.GetName()
                # Denominator: subtract backgrounds
                if not 'histo_DY' in sample.GetName() and not 'histo_DATA' in sample.GetName():
                  DataR[iRAndKff][iRegion][sample.GetName()]= Rfile[iRAndKff].Get(dirs.GetName()+'/'+subdir.GetName()+'/'+sample.GetName())
                  DataR[iRAndKff][iRegion]['RDen'].Add(DataR[iRAndKff][iRegion][sample.GetName()],-1)

        # Compute R
        DataR[iRAndKff][iRegion]['val'] = TH1F("HR_outin_MC", "HR_outin_MC", 1, 0, 2)
        DataR[iRAndKff][iRegion]['val'].Divide(DataR[iRAndKff][iRegion]['RNum'],DataR[iRAndKff][iRegion]['RDen'], 1, 1, "b")
        Rinout[iRAndKff][iRegion]['val'] = DataR[iRAndKff][iRegion]['val'].GetBinContent(1)
        Rinout[iRAndKff][iRegion]['err'] = DataR[iRAndKff][iRegion]['val'].GetBinError(1)
        print 'R calc. Num = ',  DataR[iRAndKff][iRegion]['RNum'].Integral(), ' / Den = ', DataR[iRAndKff][iRegion]['RDen'].Integral(), ' | R(out/in) = ', Rinout[iRAndKff][iRegion]['val'], ' +/- ', Rinout[iRAndKff][iRegion]['err'] 

    print ' ----- Rinout -----'
    print Rinout
    print ' ----- K_ff -------'
    print K_ff 

    # ------------------- Apply Rinout and K_ff --------------------
    # Create Ouput file 
    outputFile = ROOT.TFile.Open( opt.outputFile , "RECREATE")

    # Read Input file
    inputFile  = ROOT.TFile.Open( opt.inputFile  , "READ")

    # Create output file structure
    for key in inputFile.GetListOfKeys() : 
      if key.IsFolder() : 
        baseDir = key.GetName()
        #print '---> folder: ',baseDir
        outputFile.mkdir(baseDir) 
        inputFile.cd(baseDir)
        for skey in ROOT.gDirectory.GetListOfKeys() :
          if skey.IsFolder():
            subDir = skey.GetName() 
            outputFile.mkdir(baseDir+'/'+subDir)
            inputFile.cd(baseDir+'/'+subDir)
            for hkey in ROOT.gDirectory.GetListOfKeys() :
              hName = hkey.GetName() 
              outputFile.cd(baseDir+'/'+subDir)
              hTmp = inputFile.Get(baseDir+'/'+subDir+'/'+hName).Clone()
              iDYestimKeep = 'NONE'
              for iDYestim in DYestim :
                if baseDir == iDYestim : 
                  iDYestimKeep = iDYestim
                  sName = ''
                  for i in range( 1, len(DYestim[iDYestim]['DYProc'].split('_'))+1 ) : 
                    if len(hName.split('_')) >= len(DYestim[iDYestim]['DYProc'].split('_'))+1 : 
                      if i==1 : sName+= hName.split('_')[i]
                      else    : sName+= '_' + hName.split('_')[i]
                  if sName == DYestim[iDYestim]['DYProc'] :
                   if not hName == 'histo_'+DYestim[iDYestim]['DYProc']+'_'+DYestim[iDYestim]['NPname']+'Up' and not hName == 'histo_'+DYestim[iDYestim]['DYProc']+'_'+DYestim[iDYestim]['NPname']+'Down' :
                    if hTmp.Integral() == 0 : 
                       nHisDummy = 0
                       print '!!!!!!!!!!!!!!!!!!!!! WARNING: Empty histogram -> Setting dummy input !!!!!!!!!!!!!!!!!!!!!!',hName
                       print '!!!!!!!!!!!!!!!!!!!!! Only works for 1 bin, see below !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!'
                       print '!!!!!!!!!!!!!!!!!!!!! nBin = ',hTmp.GetNbinsX()
                       for iBin in range(1,hTmp.GetNbinsX()+1) : 
                          nHisDummy += 1.
                          hTmp.SetBinContent(iBin,0.00001)
                          hTmp.SetBinError(iBin,0.00001)

                    # Create up/down systematic uncertainty histograms
                    if hName == 'histo_' + DYestim[iDYestim]['DYProc']:
                      hUp = hTmp.Clone('histo_'+DYestim[iDYestim]['DYProc']+'_'+DYestim[iDYestim]['NPname']+'Up')
                      hDo = hTmp.Clone('histo_'+DYestim[iDYestim]['DYProc']+'_'+DYestim[iDYestim]['NPname']+'Down')
                    print '--------- DY' , baseDir , hName , len(DYestim[iDYestim]['DYProc'].split('_'))
                    
                    # Standard case 
                    # Get yields and uncertainties
                    if not 'Nout' in DYestim[iDYestim] :
                      # Total SF Data IN  
                      Nin  = inputFile.Get(DYestim[iDYestim]['SFin']+'/events/histo_'+DYestim[iDYestim]['SFinDa']).Integral()
                      ENin = inputFile.Get(DYestim[iDYestim]['SFin']+'/events/histo_'+DYestim[iDYestim]['SFinDa']).GetBinError(1)
                      # Total DF Data IN (symmetric background, e.g., WW, Top, Wjets)
                      Ndf  = inputFile.Get(DYestim[iDYestim]['DFin']+'/events/histo_'+DYestim[iDYestim]['DFinDa']).Integral()
                      ENdf = inputFile.Get(DYestim[iDYestim]['DFin']+'/events/histo_'+DYestim[iDYestim]['DFinDa']).GetBinError(1)
                      Nvv  = 0
                      ENvv = 0
                      # VV SF backgrounds IN ('VZ','Vg','VgS_L','VgS_H')  
                      for iMC in DYestim[iDYestim]['SFinMC'] : 
                        try:
                          Nvv += inputFile.Get(DYestim[iDYestim]['SFin']+'/events/histo_'+iMC).Integral()
                          ENvv = ENvv + pow(inputFile.Get(DYestim[iDYestim]['SFin']+'/events/histo_'+iMC).GetBinError(1),2)
                        except:
                          print "Empty"
                      ENvv   = math.sqrt(ENvv)   
                      Nvvdf  = 0
                      ENvvdf = 0
                      # VV DF backgrounds IN ('VZ','Vg','VgS_L','VgS_H')  
                      for iMC in DYestim[iDYestim]['DFinMC'] : 
                        Nvvdf += inputFile.Get(DYestim[iDYestim]['DFin']+'/events/histo_'+iMC).Integral()
                        ENvvdf = ENvvdf + pow(inputFile.Get(DYestim[iDYestim]['DFin']+'/events/histo_'+iMC).GetBinError(1),2)
                      ENvvdf = math.sqrt(ENvvdf)
                      # Remove VV MC bkgs from VV Data bkgs in DF channel  
                      Neu    = Ndf - Nvvdf
                      ENeu   = math.sqrt(pow(Ndf,2)+pow(Nvvdf,2))
                      # Labels
                      rinout = DYestim[iDYestim]['rinout']
                      tag = DYestim[iDYestim]['njet'] + DYestim[iDYestim]['flavour']
                      # Retrieve R(out/in) value
                      R   = Rinout[rinout][tag]['val']
                      ER  = Rinout[rinout][tag]['err']
                      if 'rsyst' in DYestim[iDYestim] : ER = math.sqrt(pow(ER,2)+pow(DYestim[iDYestim]['rsyst'],2))
                      # Retrieve k value
                      k  = K_ff[rinout][tag]['val']
                      Ek = K_ff[rinout][tag]['err']
                      if 'ksyst' in DYestim[iDYestim] : Ek = math.sqrt(pow(Ek,2)+pow(DYestim[iDYestim]['ksyst'],2))
                      print 'R = ',R,' +- ',ER
                      print 'k = ',k,' +- ',Ek
                      print 'Nin =',Nin,' Neu = ',Neu,' Nvv = ',Nvv

                      # Get OUT yields and uncertainties from R(out/in) method
                      Nout = DYCalc.N_DY(R , Nin , k , Neu, Nvv)
                      #print R , Nin , k , Neu, Nvv, ER, ENin, Ek, ENeu, ENvv
                      Eout = DYCalc.EN_DY(R , Nin , k , Neu, Nvv, ER, ENin, Ek, ENeu, ENvv )
                      NUp  = Nout+Eout
                      # Protect against error giving negative yield
                      NDo  = max(Nout-Eout,Nout*0.000000001)
                      nHis = inputFile.Get(baseDir+'/'+subDir+'/histo_'+DYestim[iDYestim]['DYProc']).Integral()
                      if nHis == 0 : 
                        #nHis = nHisDummy
                        print '!!!!!!!!!!!!!!!!!!!!! WARNING: Empty histogram -> Setting dummy input !!!!!!!!!!!!!!!!!!!!!!'
                        nHis = 0.00001

                      # Finally, the acceptance (scale factor) value  
                      Acc  = 1.
                      EAcc = 0.01

                      # Computing acceptance using MC
                      if 'AccNum' in DYestim[iDYestim] and 'AccDen' in DYestim[iDYestim] :
                        hNum = inputFile.Get(DYestim[iDYestim]['AccNum']).Clone()
                        hDen = inputFile.Get(DYestim[iDYestim]['AccDen']).Clone()
                        hAcc = hNum.Clone("hAcc")
                        print("Acc Num = {}".format(hNum.Integral()))
                        print("Acc Den = {}".format(hDen.Integral()))
                        hAcc.Reset()                      
                        hAcc.Divide(hNum,hDen,1,1,"b") 
                        Acc  = hAcc.Integral()
                        EAcc = hAcc.GetBinError(1)
                        #Forcing non null acceptance due to low stats
                        if Acc == 0 : 
                          print 'LOW STATS FOR ACCEPTANCE! Setting Acc to 0.001 +/- 0.01'
                          Acc  = 0.001
                          EAcc = 0.01

                    # Case N_out already known
                    else:
                      Nout = DYestim[iDYestim]['Nout']
                      NUp  = Nout
                      NDo  = Nout
                      if 'NUp' in DYestim[iDYestim] : NUp = DYestim[iDYestim]['NUp']
                      if 'NDo' in DYestim[iDYestim] : NDo = DYestim[iDYestim]['NDo']
                      nHis = inputFile.Get(baseDir+'/'+subDir+'/histo_'+DYestim[iDYestim]['DYProc']).Integral()
                      if nHis == 0 :  
                        #nHis = nHisDummy
                        print '!!!!!!!!!!!!!!!!!!!!! WARNING: Empty histogram -> Setting dummy input !!!!!!!!!!!!!!!!!!!!!!'
                        nHis = 0.00001
                      Acc  = 1.
                      EAcc = 0.01
                      Eout = 0.5*((Nout-NDo)+(NUp-Nout))

                    # Systematic uncertainties  
                    if 'asyst' in DYestim[iDYestim] : EAcc = math.sqrt(pow(EAcc,2)+pow(DYestim[iDYestim]['asyst'],2))
                    print 'Acc = ', Acc, " +- ", EAcc

                    # Central value or systematics not related to DY ESTIM
                    if not hName == 'histo_'+DYestim[iDYestim]['DYProc']+'_'+DYestim[iDYestim]['NPname']+'Up' and not hName == 'histo_'+DYestim[iDYestim]['DYProc']+'_'+DYestim[iDYestim]['NPname']+'Down' :
                      Scale = Nout / nHis
                      if Scale < 0:
                        print '----------  NEGATIVE SCALE = ', Scale ,'. Setting scale to 1 ----------' 
                        Scale = 1
                        Nout = nHis
                      print 'Nout= ' , Nout , ' +- ',Eout, '(Nout_MC = ',nHis,') -> Scale = ',Scale 
                      print 'Nout*Acc= ' , Nout*Acc , iDYestim
                      for iBin in range(0,hTmp.GetNbinsX()+2) :
                        BinContent = hTmp.GetBinContent(iBin)
                        NewBinContent = BinContent*Scale*Acc
                        hTmp.SetBinContent(iBin,NewBinContent)
                        BinError = hTmp.GetBinError(iBin)
                        NewBinError = BinError * abs(Scale)*Acc
                        NewBinError = 0.
                        hTmp.SetBinError(iBin,NewBinError)
                        #print 'BinContent= ' , BinContent , ', NewBinContent = ',NewBinContent 
                        #print 'BinError  = ' , BinError   , ', NewBinError   = ',NewBinError 
                    # Compute Syst Error
                    if hName == 'histo_'+DYestim[iDYestim]['DYProc']:
                      print '---  UP  ---' 
                      outputFile.cd(baseDir+'/'+subDir)
                      Scale = NUp / nHis
                      if Scale < 0:
                        print '----------  NEGATIVE SCALE = ', Scale ,'. Setting scale to 1 ----------'
                        Scale = 1
                        NUp = nHis
                      print 'NUp= ' , NUp , '(Nout_MC = ',nHis,') -> Scale = ',Scale
                      print 'NUp*Acc = ' , NUp*(Acc+EAcc)
                      for iBin in range(0,hUp.GetNbinsX()+2) :
                        BinContent = hUp.GetBinContent(iBin)
                        NewBinContent = BinContent*Scale*(Acc+EAcc)
                        hUp.SetBinContent(iBin,NewBinContent)
                        BinError = hUp.GetBinError(iBin)
                        NewBinError = BinError*abs(Scale)*(Acc+EAcc)
                        NewBinError = 0.
                        hUp.SetBinError(iBin,NewBinError)
                        print 'BinContent= ' , BinContent , ', NewBinContent = ',NewBinContent
                        print 'BinError  = ' , BinError   , ', NewBinError   = ',NewBinError
                      hUp.Write()
                      print '---  DOWN  ---'
                      outputFile.cd(baseDir+'/'+subDir)
                      Scale = NDo / nHis
                      if Scale < 0:
                        print '----------  NEGATIVE SCALE = ', Scale ,'. Setting scale to 1 ----------'
                        Scale = 1
                        NDo = nHis
                      print 'NDo= ' , NDo , '(Nout_MC = ',nHis,') -> Scale = ',Scale
                      accDown = Acc-EAcc
                      if (Acc-EAcc) < 0:
                        accDown = 0.0001
                      print 'NDo*Acc= ' , NDo*accDown
                      for iBin in range(0,hDo.GetNbinsX()+2) :
                        BinContent = hDo.GetBinContent(iBin)
                        NewBinContent = BinContent*Scale*accDown
                        hDo.SetBinContent(iBin,NewBinContent)
                        BinError = hDo.GetBinError(iBin)
                        NewBinError = BinError*abs(Scale)*accDown
                        NewBinError = 0.
                        hDo.SetBinError(iBin,NewBinError)
                        print 'BinContent= ' , BinContent , ', NewBinContent = ',NewBinContent
                        print 'BinError  = ' , BinError   , ', NewBinError   = ',NewBinError
                      hDo.Write()

              if iDYestimKeep == 'NONE': hTmp.Write()
              else:
               if not ( hName == 'histo_'+DYestim[iDYestimKeep]['DYProc']+'_'+DYestim[iDYestimKeep]['NPname']+'Up' or hName == 'histo_'+DYestim[iDYestimKeep]['DYProc']+'_'+DYestim[iDYestimKeep]['NPname']+'Down' ) :
                hTmp.Write()

