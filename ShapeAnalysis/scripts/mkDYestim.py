#!/usr/bin/env python

import optparse
import LatinoAnalysis.Gardener.hwwtools as hwwtools
import math

# functions used in everyday life ...
from LatinoAnalysis.Tools.commonTools import *


if __name__ == '__main__':

    usage = 'usage: %prog [options]'
    parser = optparse.OptionParser(usage)
    
    parser.add_option('--dycfg'          , dest='dycfg'          , help='DY estimation dictionary'                   , default='dyestim.py') 
    parser.add_option('--outputDir'      , dest='outputDir'      , help='output directory'                           , default='./')
    parser.add_option('--tag'            , dest='tag'            , help='Tag used for the shape file name'           , default=None)
    parser.add_option('--DYtag'          , dest='DYtag'          , help='Tag added to the shape file name'           , default='DYEstim')
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
    Rinout = {}
    K_ff   = {}

    for iRAndKff in RAndKff :
      Rinout[iRAndKff] = {}
      K_ff[iRAndKff] = {}

      print iRAndKff

      for iRegion in RAndKff[iRAndKff]['Regions']: 
        print iRegion
#       print iRegion ,' k = ' , DYCalc.k_MC(RAndKff[iRAndKff]['KffFile'],RAndKff[iRAndKff]['Regions'][iRegion]['kNum'],RAndKff[iRAndKff]['Regions'][iRegion]['kDen']),' +/- ', DYCalc.Ek_MC(RAndKff[iRAndKff]['KffFile'],RAndKff[iRAndKff]['Regions'][iRegion]['kNum'],RAndKff[iRAndKff]['Regions'][iRegion]['kDen'])
#       print iRegion ,' R = ' , DYCalc.R_outin_MC(RAndKff[iRAndKff]['RFile'],RAndKff[iRAndKff]['Regions'][iRegion]['RNum'],RAndKff[iRAndKff]['Regions'][iRegion]['RDen']),' +/- ', DYCalc.ER_outin_MC(RAndKff[iRAndKff]['RFile'],RAndKff[iRAndKff]['Regions'][iRegion]['RNum'],RAndKff[iRAndKff]['Regions'][iRegion]['RDen'])
        K_ff[iRAndKff][iRegion] = {}
        K_ff[iRAndKff][iRegion]['val'] = DYCalc.k_MC(RAndKff[iRAndKff]['KffFile'],RAndKff[iRAndKff]['Regions'][iRegion]['kNum'],RAndKff[iRAndKff]['Regions'][iRegion]['kDen'])
        K_ff[iRAndKff][iRegion]['err'] = DYCalc.Ek_MC(RAndKff[iRAndKff]['KffFile'],RAndKff[iRAndKff]['Regions'][iRegion]['kNum'],RAndKff[iRAndKff]['Regions'][iRegion]['kDen'])
        Rinout[iRAndKff][iRegion] = {} 
        Rinout[iRAndKff][iRegion]['val'] = DYCalc.R_outin_MC(RAndKff[iRAndKff]['RFile'],RAndKff[iRAndKff]['Regions'][iRegion]['RNum'],RAndKff[iRAndKff]['Regions'][iRegion]['RDen'])
        Rinout[iRAndKff][iRegion]['err'] = DYCalc.ER_outin_MC(RAndKff[iRAndKff]['RFile'],RAndKff[iRAndKff]['Regions'][iRegion]['RNum'],RAndKff[iRAndKff]['Regions'][iRegion]['RDen'])
        print 'R calc. Num = ',  RAndKff[iRAndKff]['Regions'][iRegion]['RNum'], ' / Den = ', RAndKff[iRAndKff]['Regions'][iRegion]['RDen']

    print ' ----- Rinout -----'
    print Rinout
    print ' ----- K_ff -------'
    print K_ff 

    # ------------------- Apply Rinout and K_ff --------------------
    # Create Ouput file 
    outputFile = ROOT.TFile.Open( opt.outputFile , "RECREATE")

    # Read Input file
    inputFile  = ROOT.TFile.Open( opt.inputFile  , "READ")
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
                  sName=''
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
                          hTmp.SetBinContent(iBin,1.)
                          hTmp.SetBinError(iBin,1.)
                    if hName == 'histo_'+DYestim[iDYestim]['DYProc']:
                      hUp = hTmp.Clone('histo_'+DYestim[iDYestim]['DYProc']+'_'+DYestim[iDYestim]['NPname']+'Up')
                      hDo = hTmp.Clone('histo_'+DYestim[iDYestim]['DYProc']+'_'+DYestim[iDYestim]['NPname']+'Down')
                    print '--------- DY' , baseDir , hName , len(DYestim[iDYestim]['DYProc'].split('_'))
                    if not 'Nout' in DYestim[iDYestim] :
                      Nin = inputFile.Get(DYestim[iDYestim]['SFin']+'/events/histo_'+DYestim[iDYestim]['SFinDa']).Integral()
                      ENin = inputFile.Get(DYestim[iDYestim]['SFin']+'/events/histo_'+DYestim[iDYestim]['SFinDa']).GetBinError(1)
                      Ndf = inputFile.Get(DYestim[iDYestim]['DFin']+'/events/histo_'+DYestim[iDYestim]['DFinDa']).Integral()
                      ENdf = inputFile.Get(DYestim[iDYestim]['DFin']+'/events/histo_'+DYestim[iDYestim]['DFinDa']).GetBinError(1)
                      Nvv = 0
                      ENvv = 0
                      for iMC in DYestim[iDYestim]['SFinMC'] : 
                        try:
                          Nvv+= inputFile.Get(DYestim[iDYestim]['SFin']+'/events/histo_'+iMC).Integral()
                          ENvv= ENvv + pow(inputFile.Get(DYestim[iDYestim]['SFin']+'/events/histo_'+iMC).GetBinError(1),2)
                        except:
                          print "Empty"
                      ENvv = math.sqrt(ENvv)   
                      Nvvdf = 0
                      ENvvdf = 0
                      for iMC in DYestim[iDYestim]['DFinMC'] : 
                        Nvvdf+= inputFile.Get(DYestim[iDYestim]['DFin']+'/events/histo_'+iMC).Integral()
                        ENvvdf= ENvvdf + pow(inputFile.Get(DYestim[iDYestim]['DFin']+'/events/histo_'+iMC).GetBinError(1),2)
                      ENvvdf = math.sqrt(ENvvdf)
                      Neu = Ndf - Nvvdf
                      ENeu = math.sqrt(pow(Ndf,2)+pow(Nvvdf,2))
                      rinout = DYestim[iDYestim]['rinout']
                      tag = DYestim[iDYestim]['njet']+DYestim[iDYestim]['flavour']
                      R  = Rinout[rinout][tag]['val']
                      ER = Rinout[rinout][tag]['err']
                      if 'rsyst' in DYestim[iDYestim] : ER = math.sqrt(pow(ER,2)+pow(DYestim[iDYestim]['rsyst'],2))
                      k  = K_ff[rinout][tag]['val']
                      Ek = K_ff[rinout][tag]['err']
                      if 'ksyst' in DYestim[iDYestim] : Ek = math.sqrt(pow(Ek,2)+pow(DYestim[iDYestim]['ksyst'],2))
                      print 'R = ',R,' +- ',ER
                      print 'k = ',k,' +- ',Ek
                      print 'Nin =',Nin,' Neu = ',Neu,' Nvv = ',Nvv
                      Nout = DYCalc.N_DY(R , Nin , k , Neu, Nvv )
                      #print R , Nin , k , Neu, Nvv, ER, ENin, Ek, ENeu, ENvv
                      Eout = DYCalc.EN_DY(R , Nin , k , Neu, Nvv, ER, ENin, Ek, ENeu, ENvv )
                      NUp  = Nout+Eout
                      # Protect against error giving negative yield
                      NDo  = max(Nout-Eout,Nout*0.000000001)
                      nHis = inputFile.Get(baseDir+'/'+subDir+'/histo_'+DYestim[iDYestim]['DYProc']).Integral()
                      if nHis == 0 : nHis = nHisDummy
                      Acc  = 1.
                      EAcc = 0.
                      if 'AccNum' in DYestim[iDYestim] and 'AccDen' in DYestim[iDYestim] :
                        hNum = inputFile.Get(DYestim[iDYestim]['AccNum']).Clone()
                        hDen = inputFile.Get(DYestim[iDYestim]['AccDen']).Clone()
                        hAcc = hNum.Clone("hAcc")
                        hAcc.Reset()                      
                        hAcc.Divide(hNum,hDen,1,1,"b") 
                        Acc  = hAcc.Integral()
                        EAcc = hAcc.GetBinError(1)
                    else:
                      Nout = DYestim[iDYestim]['Nout']
                      NUp  = Nout
                      NDo  = Nout
                      if 'NUp' in DYestim[iDYestim] : NUp = DYestim[iDYestim]['NUp']
                      if 'NDo' in DYestim[iDYestim] : NDo = DYestim[iDYestim]['NDo']
                      nHis = inputFile.Get(baseDir+'/'+subDir+'/histo_'+DYestim[iDYestim]['DYProc']).Integral()
                      if nHis == 0 : nHis = nHisDummy
                      Acc  = 1.
                      EAcc = 0.
                      Eout = 0.5*((Nout-NDo)+(NUp-Nout))
                    if 'asyst' in DYestim[iDYestim] : EAcc = math.sqrt(pow(EAcc,2)+pow(DYestim[iDYestim]['asyst'],2)) 
                    print 'Acc = ',Acc," +- ",EAcc
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
                        NewBinError = BinError*abs(Scale)*Acc
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
                        #print 'BinContent= ' , BinContent , ', NewBinContent = ',NewBinContent
                        #print 'BinError  = ' , BinError   , ', NewBinError   = ',NewBinError
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
                        #print 'BinContent= ' , BinContent , ', NewBinContent = ',NewBinContent
                        #print 'BinError  = ' , BinError   , ', NewBinError   = ',NewBinError
                      hDo.Write()

              if iDYestimKeep == 'NONE': hTmp.Write()
              else:
               if not ( hName == 'histo_'+DYestim[iDYestimKeep]['DYProc']+'_'+DYestim[iDYestimKeep]['NPname']+'Up' or hName == 'histo_'+DYestim[iDYestimKeep]['DYProc']+'_'+DYestim[iDYestimKeep]['NPname']+'Down' ) :
                hTmp.Write()

