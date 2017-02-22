#!/usr/bin/env python

import optparse
import LatinoAnalysis.Gardener.hwwtools as hwwtools

# functions used in everyday life ...
from LatinoAnalysis.Tools.commonTools import *


if __name__ == '__main__':

    usage = 'usage: %prog [options]'
    parser = optparse.OptionParser(usage)
    
    parser.add_option('--dycfg'           , dest='dycfg'           , help='DY estimation dictionary'                  , default='dyestim.py') 
    parser.add_option('--outputDir'      , dest='outputDir'      , help='output directory'                           , default='./')
    parser.add_option('--tag'            , dest='tag'            , help='Tag used for the shape file name'           , default=None)
    parser.add_option('--DYtag'          , dest='DYtag'          , help='Tag added to the shape file name'           , default='DYEstim')
    parser.add_option('--inputFile'      , dest='inputFile'      , help='input file with histograms'                 , default='DEFAULT')
    parser.add_option('--outputFile'     , dest='outputFile'     , help='output file with histograms'                 , default='DEFAULT')
 
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
    print " ooutputFile    =          ", opt.outputFile

    # Create Needed dictionnary

    variables = {}
    if os.path.exists(opt.variablesFile) :
      handle = open(opt.variablesFile,'r')
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

    # Load C  
    cmssw_base = os.getenv('CMSSW_BASE')
    try:
      ROOT.gROOT.LoadMacro(cmssw_base+'/src/LatinoAnalysis/ShapeAnalysis/src/DYEST.C+g')
    except RuntimeError:
      ROOT.gROOT.LoadMacro(cmssw_base+'/src/LatinoAnalysis/ShapeAnalysis/src/DYEST.C++g')



    # Compute Rinout and K_ff
    Rinout = {}
    K_ff   = {}

    for iRAndKff in RAndKff :
      DY = ROOT.DY(RAndKff[iRAndKff]['KffFile'],RAndKff[iRAndKff]['RFile'])
      DY.Print()
      Rinout[iRAndKff] = {}
      Rinout[iRAndKff]['0jee'] = {}
      Rinout[iRAndKff]['0jmm'] = {}
      Rinout[iRAndKff]['1jee'] = {}
      Rinout[iRAndKff]['1jmm'] = {}
      Rinout[iRAndKff]['0jee']['val'] = DY.R_outin_MC_0j_ee()
      Rinout[iRAndKff]['0jmm']['val'] = DY.R_outin_MC_0j_uu()
      Rinout[iRAndKff]['1jee']['val'] = DY.R_outin_MC_1j_ee()
      Rinout[iRAndKff]['1jmm']['val'] = DY.R_outin_MC_1j_uu()
      Rinout[iRAndKff]['0jee']['err'] = DY.ER_outin_MC_0j_ee()
      Rinout[iRAndKff]['0jmm']['err'] = DY.ER_outin_MC_0j_uu()
      Rinout[iRAndKff]['1jee']['err'] = DY.ER_outin_MC_1j_ee()
      Rinout[iRAndKff]['1jmm']['err'] = DY.ER_outin_MC_1j_uu()
      K_ff[iRAndKff] = {}
      K_ff[iRAndKff]['0jee'] = {}
      K_ff[iRAndKff]['0jmm'] = {}
      K_ff[iRAndKff]['1jee'] = {}
      K_ff[iRAndKff]['1jmm'] = {}
      K_ff[iRAndKff]['0jee']['val'] = DY.k_MC_ee_0j()
      K_ff[iRAndKff]['0jmm']['val'] = DY.k_MC_uu_0j()
      K_ff[iRAndKff]['1jee']['val'] = DY.k_MC_ee_1j()
      K_ff[iRAndKff]['1jmm']['val'] = DY.k_MC_uu_1j()
      K_ff[iRAndKff]['0jee']['err'] = DY.Ek_MC_ee_0j()
      K_ff[iRAndKff]['0jmm']['err'] = DY.Ek_MC_uu_0j()
      K_ff[iRAndKff]['1jee']['err'] = DY.Ek_MC_ee_1j()
      K_ff[iRAndKff]['1jmm']['err'] = DY.Ek_MC_uu_1j()
      del DY

    print ' ----- Rinout -----'
    print Rinout
    print ' ----- K_ff -------'
    print K_ff 

    # ------------------- Apply Rinout and K_ff --------------------
    DYCalc = ROOT.DYCalc()
    # Create Ouput file 
    outputFile = ROOT.TFile.Open( opt.outputFile , "RECREATE")

    # Read Input file
    inputFile  = ROOT.TFile.Open( opt.inputFile  , "READ")
    for key in inputFile.GetListOfKeys() : 
      if key.IsFolder() : 
        baseDir = key.GetName()
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
              for iDYestim in DYestim :
                if baseDir == iDYestim : #and 'histo_'+DYestim[iDYestim]['Hist'] in hName : 
                  #nUnderscore=len(DYestim[iDYestim]['Hist'].split('_') 
                  sName=''
                  for i in range( 1, len(DYestim[iDYestim]['Hist'].split('_'))+1 ) : 
                    if len(hName.split('_')) >= len(DYestim[iDYestim]['Hist'].split('_'))+1 : 
                      if i==1 : sName+= hName.split('_')[i]
                      else    : sName+= '_' + hName.split('_')[i]
                  if sName == DYestim[iDYestim]['Hist'] :
                    print '--------- DY' , baseDir , hName , len(DYestim[iDYestim]['Hist'].split('_'))
                    try : Nin = inputFile.Get(DYestim[iDYestim]['SFin']+'/events/histo_DATA').GetBinContent(1)
                    except : Nin = 0
                    try : Neu = inputFile.Get(DYestim[iDYestim]['DFin']+'/events/histo_DATA').GetBinContent(1)
                    except : Neu = 0 
                    try : Nvv = inputFile.Get(DYestim[iDYestim]['SFin']+'/events/histo_VZ').GetBinContent(1)
                    except : Nvv = 0
                    try : Nvv+= inputFile.Get(DYestim[iDYestim]['SFin']+'/events/histo_Vg').GetBinContent(1)
                    except : Nvv+= 0
                    try : Nvv+= inputFile.Get(DYestim[iDYestim]['SFin']+'/events/histo_VgS').GetBinContent(1)
                    except : Nvv+= 0
                    print 'Nin = ' , Nin , ' Neu = ' , Neu , ' Nvv = ' , Nvv
                    rinout = DYestim[iDYestim]['rinout']
                    tag = DYestim[iDYestim]['njet']+DYestim[iDYestim]['flavour']
                    R  = Rinout[rinout][tag]['val']
                    ER = Rinout[rinout][tag]['err']
                    k  = K_ff[rinout][tag]['val']
                    Ek = K_ff[rinout][tag]['err']
                    print 'R = ',R,' +- ',ER
                    print 'k = ',k,' +- ',Ek
                    Nout = DYCalc.N_DY(R , Nin , k , Neu, Nvv )
                    nHis = (hTmp.Integral())
                    print 'Nout= ' , Nout , '(Nout_MC = ',nHis,' )' 
                    hTmp.Scale( Nout / nHis  )
              hTmp.Write()
               
              #print baseDir,subDir,hName.split('_')[1]
#    for iDYestim in DYestim :
#      print iDYestim

