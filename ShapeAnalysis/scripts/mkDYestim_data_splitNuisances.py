#!/usr/bin/env python

import os, sys

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
    parser.add_option('--DYtag'          , dest='DYtag'          , help='Tag added to the shape file name'           , default='DYEstimDATA_breakdown')
    parser.add_option('--inputFile'      , dest='inputFile'      , help='input file with histograms'                 , default='DEFAULT')
    parser.add_option('--outputFile'     , dest='outputFile'     , help='output file with histograms'                , default='DEFAULT')
    parser.add_option('--year'           , dest='year'           , help='data-taking year'                           , default='2016')
 
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
              # print("Total data = {}".format(K_ff_data[iRAndKff][iRegion]['kNum'].Integral()))
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

        # Store k value and uncertainty
        K_ff[iRAndKff][iRegion] = {} 
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

    # Create output txt file to store nuisances values as lnN
    txt_file = open("Nuisances_file.txt", "w")
    txt_file.write("# Nuisances breakdown \n \n")

    # Create output file structure
    # e.g., hww2l2v_13TeV_0j_ee/events/histo_DY

    # hww2l2v_13TeV_0j_ee
    for key in inputFile.GetListOfKeys() : 
      if key.IsFolder() : 
        baseDir = key.GetName()
        outputFile.mkdir(baseDir) 
        inputFile.cd(baseDir)

        # hww2l2v_13TeV_0j_ee/events/
        for skey in ROOT.gDirectory.GetListOfKeys() :
          if skey.IsFolder():
            subDir = skey.GetName() 
            outputFile.mkdir(baseDir+'/'+subDir)
            inputFile.cd(baseDir+'/'+subDir)

            # hww2l2v_13TeV_0j_ee/events/histo_DY
            for hkey in ROOT.gDirectory.GetListOfKeys() :
              hName = hkey.GetName() 
              outputFile.cd(baseDir+'/'+subDir)
              hTmp = inputFile.Get(baseDir+'/'+subDir+'/'+hName).Clone()
              iDYestimKeep = 'NONE'

              for iDYestim in DYestim :
                if baseDir == iDYestim : 
                  iDYestimKeep = iDYestim
                  sName = ''

                  for i in range(1, len(DYestim[iDYestim]['DYProc'].split('_')) + 1) : 
                    if len(hName.split('_')) >= len(DYestim[iDYestim]['DYProc'].split('_')) + 1 : 
                      if i == 1 : sName += hName.split('_')[i]
                      else      : sName += '_' + hName.split('_')[i]
                  if sName == DYestim[iDYestim]['DYProc'] :
                   if not hName == 'histo_' + DYestim[iDYestim]['DYProc'] + '_' + DYestim[iDYestim]['NPname'] + 'Up' and not hName == 'histo_' + DYestim[iDYestim]['DYProc'] + '_' + DYestim[iDYestim]['NPname'] + 'Down' and not "norm" in hName:
                    if hTmp.Integral() == 0 : 
                       nHisDummy = 0
                       print '!!!!!!!!!!!!!!!!!!!!! WARNING: Empty histogram -> Setting dummy input !!!!!!!!!!!!!!!!!!!!!!',hName
                       print '!!!!!!!!!!!!!!!!!!!!! Only works for 1 bin, see below !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!'
                       print '!!!!!!!!!!!!!!!!!!!!! nBin = ',hTmp.GetNbinsX()
                       for iBin in range(1,hTmp.GetNbinsX()+1) : 
                          nHisDummy += 1.
                          hTmp.SetBinContent(iBin,0.00001)
                          hTmp.SetBinError(iBin,0.00001)

                    # Create up/down systematic uncertainty histograms:
                    # Just clone the dummy histograms already present in the rootfile
                    # with proper name but filled with nominal yields
                    if hName == 'histo_' + DYestim[iDYestim]['DYProc']:
                      hUp = hTmp.Clone('histo_' + DYestim[iDYestim]['DYProc'] + '_' + DYestim[iDYestim]['NPname'] + 'Up')
                      hDo = hTmp.Clone('histo_' + DYestim[iDYestim]['DYProc'] + '_' + DYestim[iDYestim]['NPname'] + 'Down')
                    print '--------- DY' , baseDir , hName , len(DYestim[iDYestim]['DYProc'].split('_'))
                    
                    # Standard case - Nout NOT know a priori 
                    # Get yields and uncertainties
                    if not 'Nout' in DYestim[iDYestim] :

                      # Total SF Data IN  
                      Nin  = inputFile.Get(DYestim[iDYestim]['SFin'] + '/events/histo_' + DYestim[iDYestim]['SFinDa']).Integral()
                      ENin = inputFile.Get(DYestim[iDYestim]['SFin'] + '/events/histo_' + DYestim[iDYestim]['SFinDa']).GetBinError(1)

                      # Total DF Data IN (symmetric background, e.g., WW, Top, Wjets)
                      Ndf  = inputFile.Get(DYestim[iDYestim]['DFin'] + '/events/histo_' + DYestim[iDYestim]['DFinDa']).Integral()
                      ENdf = inputFile.Get(DYestim[iDYestim]['DFin'] + '/events/histo_' + DYestim[iDYestim]['DFinDa']).GetBinError(1)

                      # VV SF backgrounds IN ('VZ','Vg','VgS_L','VgS_H') --> Get them from MC
                      Nvv  = 0
                      ENvv = 0
                      for iMC in DYestim[iDYestim]['SFinMC'] : 
                        try:
                          Nvv += inputFile.Get(DYestim[iDYestim]['SFin']+'/events/histo_'+iMC).Integral()
                          ENvv = ENvv + pow(inputFile.Get(DYestim[iDYestim]['SFin']+'/events/histo_'+iMC).GetBinError(1),2)
                        except:
                          print "Empty"
                      ENvv   = math.sqrt(ENvv)   

                      # VV DF backgrounds IN ('VZ','Vg','VgS_L','VgS_H') --> Get them from MC, too
                      Nvvdf  = 0
                      ENvvdf = 0
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
                      if 'rsyst' in DYestim[iDYestim] : 
                          ER = math.sqrt(pow(ER, 2) + pow(DYestim[iDYestim]['rsyst'], 2))

                      # Retrieve k value
                      k  = K_ff[rinout][tag]['val']
                      Ek = K_ff[rinout][tag]['err']
                      if 'ksyst' in DYestim[iDYestim] : 
                          Ek = math.sqrt(pow(Ek, 2) + pow(DYestim[iDYestim]['ksyst'], 2))
                      # print 'R = ',   R,   ' +- ', ER
                      # print 'k = ',   k,   ' +- ', Ek
                      # print 'Nin = ', Nin, ' Neu = ', Neu, ' Nvv = ', Nvv

                      # Get OUT yields and uncertainties from R(out/in) method
                      Nout = DYCalc.N_DY( R , Nin , k , Neu, Nvv)
                      Eout = DYCalc.EN_DY(R , Nin , k , Neu, Nvv, ER, ENin, Ek, ENeu, ENvv)
                      NUp  = Nout + Eout
                      # Protect against error giving negative yield
                      NDo  = max(Nout - Eout, Nout * 0.000000001)

                      # Printout different uncertainty sources
                      print("N out = {}".format(Nout))
                      print("Total uncertainty on N out = {} ({}%)".format(Eout, Eout/Nout*100))
                      
                      # Get DY yields before correction (in OUT region?)
                      nHis = inputFile.Get(baseDir + '/' + subDir + '/histo_' + DYestim[iDYestim]['DYProc']).Integral()
                      if nHis == 0 : 
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
                        # print("Acc Num = {}".format(hNum.Integral()))
                        # print("Acc Den = {}".format(hDen.Integral()))
                        hAcc.Reset()                      
                        hAcc.Divide(hNum,hDen,1,1,"b") 
                        Acc  = hAcc.Integral()
                        EAcc = hAcc.GetBinError(1)

                        #Forcing non null acceptance due to low stats
                        if Acc == 0 : 
                          print 'LOW STATS FOR ACCEPTANCE! Setting Acc to 0.001 +/- 0.01'
                          Acc  = 0.001
                          EAcc = 0.01

                    # Case N_out already known - typically not our case
                    # To use this feature, introduce the 'Nout' value in dyestim.py
                    else:
                      Nout = DYestim[iDYestim]['Nout']
                      NUp  = Nout
                      NDo  = Nout
                      if 'NUp' in DYestim[iDYestim] : 
                          NUp = DYestim[iDYestim]['NUp']
                      if 'NDo' in DYestim[iDYestim] : 
                          NDo = DYestim[iDYestim]['NDo']
                      nHis = inputFile.Get(baseDir + '/' + subDir + '/histo_' + DYestim[iDYestim]['DYProc']).Integral()
                      if nHis == 0 :  
                        print '!!!!!!!!!!!!!!!!!!!!! WARNING: Empty histogram -> Setting dummy input !!!!!!!!!!!!!!!!!!!!!!'
                        nHis = 0.00001
                      Acc  = 1.
                      EAcc = 0.01
                      Eout = 0.5*((Nout-NDo)+(NUp-Nout))

                    # Systematic uncertainties  
                    if 'asyst' in DYestim[iDYestim] : 
                        EAcc = math.sqrt(pow(EAcc, 2) + pow(DYestim[iDYestim]['asyst'], 2))
                    print 'Acc = ', Acc, " +- ", EAcc

                    # Print results to txt file
                    # txt_file.write('--------- DY {}, {}, {} \n'.format(baseDir, hName, len(DYestim[iDYestim]['DYProc'].split('_'))))
                    
                    # one nuisance correlated between ee and mm related to the N_eu part
                    Err_out_Neu = DYCalc.EN_DY(R , Nin , k , Neu, Nvv, 0, 0, 0, ENeu, 0)
                    print("Uncertainty on N out due to N(e,mu) uncertainty = {} ({}%)".format(Err_out_Neu, Err_out_Neu/Nout*100))
                    out_string = "Uncertainty on N out due to N(e,mu) uncertainty = {} ({}%) \n".format(Err_out_Neu, Err_out_Neu/Nout*100)
                    #txt_file.write(out_string)

                    # one nuisance anti-correlated between ee and mm related to k (which wil be very small)
                    Err_out_k = DYCalc.EN_DY(R , Nin , k , Neu, Nvv, 0, 0, Ek, 0, 0)
                    print("Uncertainty on N out due to k uncertainty = {} ({}%)".format(Err_out_k, Err_out_k/Nout*100))
                    out_string = "Uncertainty on N out due to k uncertainty = {} ({}%) \n".format(Err_out_k, Err_out_k/Nout*100)
                    #txt_file.write(out_string)

                    # one nuisance parameter uncorrelated between ee and mm related to the remaining uncertainties
                    Err_out_rest = DYCalc.EN_DY(R , Nin , k , Neu, Nvv, ER, ENin, 0, 0, ENvv)
                    print("Uncertainty on N out due to other sources (except Acc) = {} ({}%)".format(Err_out_rest, Err_out_rest/Nout*100))
                    out_string = "Uncertainty on N out due to other sources (except Acc) {} ({}%) \n".format(Err_out_rest, Err_out_rest/Nout*100)
                    #txt_file.write(out_string)

                    # Keep Acc separatd
                    print("Uncertainty on DY yields in signal region due to Acc = {} ({}%)".format(EAcc/Acc, EAcc/Acc*100))
                    out_string = "Uncertainty on DY yields in signal region due to Acc = {} ({}%) \n".format(EAcc/Acc, EAcc/Acc*100)
                    #txt_file.write(out_string)

                    # Now the output to plug in nuisances.py
                    if 'AccNum' in DYestim[iDYestim] and 'AccDen' in DYestim[iDYestim] :
                        if "wwAcc" in DYestim[iDYestim]['AccNum']:
                            txt_file.write("# {}_{} WW channel \n".format(DYestim[iDYestim]['njet'],DYestim[iDYestim]['flavour']))
                        else:
                            txt_file.write("# {}_{} channel \n".format(DYestim[iDYestim]['njet'],DYestim[iDYestim]['flavour']))

                    add_to_title = DYestim[iDYestim]['njet'] + "_" + DYestim[iDYestim]['flavour']
                    if 'AccNum' in DYestim[iDYestim] and 'AccDen' in DYestim[iDYestim] :
                        if "wwAcc" in DYestim[iDYestim]['AccNum']:
                            add_to_title = DYestim[iDYestim]['njet'] + "_" + DYestim[iDYestim]['flavour'] + "_WW"

                    print("XDDDDDDDDDDDDDDDDDDDDDDDDD")
                    print("Current basedir name: {}".format(baseDir))
                    print("Now split it!")
                    baseDir_split = items = baseDir.split('_')
                    print(baseDir_split)
                    print("Add the last two items to the add_to_title string!")
                    print("Add to title: {}_{}_{}".format(add_to_title,baseDir_split[-2],baseDir_split[-1]))
                    print("XDDDDDDDDDDDDDDDDDDDDDDDDD")

                    # Add more details to "add_to_title" to avoid repeated nuisances names
                    # Do this only in HTXS
                    if ("HTXS" in opt.dycfg or "STXS" in opt.dycfg):
                        add_to_title = add_to_title + "_" + baseDir
                        print("Add to title in case of HTXS: {}".format(add_to_title))

                    # k: anticorrelated between ee and mm
                    txt_file.write("nuisances['DYnorm_k_" + add_to_title + "'] = {\n")
                    txt_file.write("  'name': 'DYnorm_k_" + DYestim[iDYestim]['njet'] + "_" + opt.year + "',\n")
                    txt_file.write("  'type': 'lnN',\n")
                    txt_file.write("  'samples': {\n")
                    # Anticorrelate syst between ee and mm but we are using k_ee and k_mm --> some down/up variation --> anticorrelated with DY yields
                    txt_file.write("    'DY': '{0:.3f}/{1:.3f}',\n".format(1 + Err_out_k/Nout, 1 / (1 + Err_out_k/Nout)))
                    txt_file.write("  },\n")
                    txt_file.write("  'cuts' : ['" + baseDir + "'] \n")
                    txt_file.write("}\n")
                    txt_file.write("\n")

                    # N_eu: correlated between ee and mm --> anticorrelated with DY yields
                    txt_file.write("nuisances['DYnorm_em_" + add_to_title + "'] = {\n")
                    txt_file.write("  'name': 'DYnorm_em_" + DYestim[iDYestim]['njet'] + "_" + opt.year + "',\n")
                    txt_file.write("  'type': 'lnN',\n")
                    txt_file.write("  'samples': {\n")
                    txt_file.write("    'DY': '{0:.3f}/{1:.3f}',\n".format(1 + Err_out_Neu/Nout, 1 / (1 + Err_out_Neu/Nout)))
                    txt_file.write("  },\n")
                    txt_file.write("  'cuts' : ['" + baseDir + "'] \n")
                    txt_file.write("}\n")
                    txt_file.write("\n")

                    # R: uncorrelated between ee and mm --> correlated with DY yields
                    txt_file.write("nuisances['DYnorm_R_" + add_to_title + "'] = {\n")
                    txt_file.write("  'name': 'DYnorm_R_" + DYestim[iDYestim]['njet'] + "_" + DYestim[iDYestim]['flavour'] + "_" + opt.year + "',\n")
                    txt_file.write("  'type': 'lnN',\n")
                    txt_file.write("  'samples': {\n")
                    txt_file.write("    'DY': '{0:.3f}/{1:.3f}',\n".format(1 / (1 + Err_out_rest/Nout), 1 + Err_out_rest/Nout))
                    txt_file.write("  },\n")
                    txt_file.write("  'cuts' : ['" + baseDir + "'] \n")
                    txt_file.write("}\n")
                    txt_file.write("\n")

                    # Acc: uncorrelated between ee and mm --> correlated with DY yields
                    txt_file.write("nuisances['DYnorm_Acc_" + add_to_title + "'] = {\n")
                    txt_file.write("  'name': 'DYnorm_Acc_" + DYestim[iDYestim]['njet'] + "_" + DYestim[iDYestim]['flavour'] + "_" + opt.year + "',\n")
                    txt_file.write("  'type': 'lnN',\n")
                    txt_file.write("  'samples': {\n")
                    txt_file.write("    'DY': '{0:.3f}/{1:.3f}',\n".format(1 / (1 + EAcc/Acc), 1 + EAcc/Acc))
                    txt_file.write("  },\n")
                    txt_file.write("  'cuts' : ['" + baseDir + "'] \n")
                    txt_file.write("}\n")
                    txt_file.write("\n")


                    # Central value or systematics not related to DY ESTIM
                    if not hName == 'histo_' + DYestim[iDYestim]['DYProc'] + '_' + DYestim[iDYestim]['NPname'] + 'Up' and not hName == 'histo_' + DYestim[iDYestim]['DYProc'] + '_' + DYestim[iDYestim]['NPname'] + 'Down' :
                      # Nout  --> DY yields in OUT region estimated using R
                      # nHis  --> DY yields in OUT region from MC
                      # Scale --> correction to get Nout from nHis
                      Scale = Nout / nHis
                      if Scale < 0:
                        print '----------  NEGATIVE SCALE = ', Scale, '. Setting scale to 1 ----------' 
                        Scale = 1
                        Nout  = nHis
                      # print 'Nout = ', Nout, ' +- ', Eout, '(Nout_MC = ', nHis, ') -> Scale = ', Scale 
                      # print 'Nout * Acc = ' , Nout * Acc , iDYestim
                      for iBin in range(0, hTmp.GetNbinsX() + 2) :
                        BinContent    = hTmp.GetBinContent(iBin)
                        NewBinContent = BinContent * Scale * Acc
                        hTmp.SetBinContent(iBin, NewBinContent)
                        BinError    = hTmp.GetBinError(iBin)
                        NewBinError = BinError * abs(Scale) * Acc
                        NewBinError = 0.
                        hTmp.SetBinError(iBin, NewBinError)

                    # Compute Syst Error
                    if hName == 'histo_' + DYestim[iDYestim]['DYProc']:

                      # Up variation
                      # print '---  UP  ---' 
                      outputFile.cd(baseDir + '/' + subDir)
                      Scale = NUp / nHis
                      if Scale < 0 or math.isnan(NUp):
                        print '----------  NEGATIVE SCALE = ', Scale, '. Setting scale to 1 ----------'
                        Scale = 1
                        NUp   = nHis
                      # print 'NUp = ' , NUp , '(Nout_MC = ', nHis, ') -> Scale = ', Scale
                      # print 'NUp * Acc = ' , NUp * (Acc + EAcc)
                      for iBin in range(0, hUp.GetNbinsX() + 2) :
                        BinContent    = hUp.GetBinContent(iBin)
                        NewBinContent = BinContent * Scale * (Acc + EAcc)
                        hUp.SetBinContent(iBin, NewBinContent)
                        BinError    = hUp.GetBinError(iBin)
                        NewBinError = BinError * abs(Scale) * (Acc+EAcc)
                        NewBinError = 0.
                        hUp.SetBinError(iBin,NewBinError)
                        # print 'BinContent= ' , BinContent , ', NewBinContent = ', NewBinContent
                        # print 'BinError  = ' , BinError   , ', NewBinError   = ', NewBinError
                      hUp.Write()

                      # Down variation
                      # print '---  DOWN  ---'
                      outputFile.cd(baseDir + '/' + subDir)
                      Scale = NDo / nHis
                      if Scale < 0 or math.isnan(NUp):
                        print '----------  NEGATIVE SCALE = ', Scale ,'. Setting scale to 1 ----------'
                        Scale = 1
                        NDo   = nHis
                      # print 'NDo = ' , NDo, '(Nout_MC = ', nHis, ') -> Scale = ', Scale
                      accDown = Acc - EAcc
                      if (Acc - EAcc) < 0:
                        accDown = 0.0001
                      # print 'NDo * Acc= ' , NDo * accDown
                      for iBin in range(0, hDo.GetNbinsX() + 2) :
                        BinContent    = hDo.GetBinContent(iBin)
                        NewBinContent = BinContent * Scale * accDown
                        hDo.SetBinContent(iBin, NewBinContent)
                        BinError    = hDo.GetBinError(iBin)
                        NewBinError = BinError * abs(Scale) * accDown
                        NewBinError = 0.
                        hDo.SetBinError(iBin, NewBinError)
                        # print 'BinContent= ', BinContent, ', NewBinContent = ', NewBinContent
                        # print 'BinError  = ', BinError,   ', NewBinError = ',   NewBinError
                      hDo.Write()

              if iDYestimKeep == 'NONE': hTmp.Write()
              else:
               if not ( hName == 'histo_' + DYestim[iDYestimKeep]['DYProc'] + '_' + DYestim[iDYestimKeep]['NPname'] + 'Up' or hName == 'histo_' + DYestim[iDYestimKeep]['DYProc'] + '_' + DYestim[iDYestimKeep]['NPname'] + 'Down' ) :
                hTmp.Write()

    txt_file.close()
