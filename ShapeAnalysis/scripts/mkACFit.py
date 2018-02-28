#!/usr/bin/env python

import optparse
import LatinoAnalysis.Gardener.hwwtools as hwwtools

# functions used in everyday life ...
from LatinoAnalysis.Tools.commonTools import *

# ROOT
import ROOT

if __name__ == '__main__':

    usage = 'usage: %prog [options]'
    parser = optparse.OptionParser(usage)

    parser.add_option('--tag'            , dest='tag'            , help='Tag used for the shape file name'           , default=None)
    parser.add_option('--inputFile'      , dest='inputFile'      , help='input file with histograms'                 , default='DEFAULT')
    parser.add_option('--outputDir'      , dest='outputDir'      , help='output directory'                           , default='./')
    parser.add_option('--outputFile'     , dest='outputFile'     , help='output file with histograms'                 , default='DEFAULT')
    parser.add_option('--cutList'        , dest='cutList'        , help='cut list to process' , default=[], type='string' , action='callback' , callback=list_maker('cutList',',')) 
    parser.add_option('--varList'        , dest='varList'        , help='var list to process' , default=[], type='string' , action='callback' , callback=list_maker('varList',',')) 

    # read default parsing options as well
    hwwtools.addOptions(parser)
    hwwtools.loadOptDefaults(parser)
    (opt, args) = parser.parse_args()

    # Set Input file
    if opt.inputFile == 'DEFAULT' :
      opt.inputFile = opt.outputDir+'/plots_'+opt.tag+'.root'
    print " inputFile      =          ", opt.inputFile

    # Set Output file
    if opt.outputFile == 'DEFAULT' :
      opt.outputFile = opt.outputDir+'/plots_'+opt.tag+'_'+'ACCoupling'+'.root'
    print " outputFile    =          ", opt.outputFile

    # Create Needed dictionnary

    variables = {}
    if os.path.exists(opt.variablesFile) :
      handle = open(opt.variablesFile,'r')
      exec(handle)
      handle.close()
    if len(opt.varList)>0:
      var2del=[]
      for iVar in variables:
        if not iVar in opt.varList : var2del.append(iVar)
      for iVar in var2del : del variables[iVar]

    print variables

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
    if len(opt.cutList)>0:
      cut2del=[] 
      for iCut in cuts:
        if not iCut in opt.cutList : cut2del.append(iCut)
      for iCut in cut2del : del cuts[iCut]

    # Create Ouput file 
    outputFile = ROOT.TFile.Open( opt.outputFile , "RECREATE")

    # Read Input file and start loop
    inputFile  = ROOT.TFile.Open( opt.inputFile  , "READ")
    for key in inputFile.GetListOfKeys() :
      if key.IsFolder() and key.GetName() in cuts :
        baseDir = key.GetName()
        print 'baseDir= ', baseDir
        outputFile.mkdir(baseDir) 
        inputFile.cd(baseDir)
        for skey in ROOT.gDirectory.GetListOfKeys() :
          if skey.IsFolder() and skey.GetName() in variables :        
            subDir = skey.GetName()
            iVar   = subDir
            print 'subDir= ',subDir
            outputFile.mkdir(baseDir+'/'+subDir)
            inputFile.cd(baseDir+'/'+subDir)
            #for iVar in variables:
            if True:
              print 'iVar= ',iVar
              # 1D Scan
              if '1D' in acoupling['ScanConfig'] and len(acoupling['ScanConfig']['1D']) > 0 :
                for iScan in acoupling['Scans']['1D']:
                  operatorValues = sorted(acoupling['Scans']['1D'][iScan].keys(),key=float)
                  operatorValuesFloat = [float(x) for x in operatorValues] 
                  # ... Get AC binning (and check)
                  idxSM = operatorValuesFloat.index(0.)
                  binWOp = operatorValuesFloat[idxSM+1]-operatorValuesFloat[idxSM]
                  nBinOp = len(operatorValuesFloat)
                  xMinOp = operatorValuesFloat[0]-binWOp/2.
                  xMaxOp = operatorValuesFloat[nBinOp-1]+binWOp/2.
                  check_binW=True
                  for i in range(len(operatorValuesFloat)-1) :
                    if not operatorValuesFloat[i]+binWOp == operatorValuesFloat[i+1] : check_binW=False
                  if not check_binW:
                    print 'AC Grid Bin Width Error -> Exit !!!!'
                    exit()
                  
                  # ... Get All input histograms + binning
                  inputHistos = []
                  for opVal in operatorValues :
                    hName = 'histo_'+acoupling['sigName'].replace('${iWeight}',str(acoupling['Scans']['1D'][iScan][opVal]))
                    inputHistos.append(inputFile.Get(baseDir+'/'+subDir+'/'+hName).Clone())
                  nBinVar=inputHistos[0].GetNbinsX()
                  # ... Create & Fill output histograms
                  outputHistos = []
                  outputFile.mkdir(baseDir+'/'+subDir+'/'+iScan)
                  outputFile.cd(baseDir+'/'+subDir+'/'+iScan)
                  for iBinVar in range(nBinVar): 
                    #hName = 'histo_'+subDir+'_'+iScan+'_'+str(iBinVar)
                    hName = 'bin_content_par1_'+str(iBinVar+1)
                    outputHistos.append( ROOT.TH1D(hName,hName,nBinOp,xMinOp,xMaxOp) )
                    SMVal=inputHistos[idxSM].GetBinContent(iBinVar+1)
                    for opVal in operatorValues :
                      idx=operatorValues.index(opVal)
                      varVal=inputHistos[idx].GetBinContent(iBinVar+1)/SMVal
                      varErr=inputHistos[idx].GetBinError(iBinVar+1)/SMVal
                      outputHistos[iBinVar].SetBinContent(idx+1,varVal)
                      outputHistos[iBinVar].SetBinError(idx+1,varErr)
                  # ... Fitting model
                  outputFit = []
                  for iBinVar in range(nBinVar):
                    #fName = 'fit_'+subDir+'_'+iScan+'_'+str(iBinVar) 
                    fName = 'bin_content_par1_'+str(iBinVar+1)
                    outputFit.append( ROOT.TF1(fName,"[0]+[1]*x+[2]*x*x",xMinOp*3,xMaxOp*3) )  
                    outputHistos[iBinVar].Fit(outputFit[iBinVar],"RME")
                    #ROOT.gPad.WaitPrimitive()
                  # ... Save all  
                  for iHist in outputHistos : iHist.Write()
                  for iFit  in outputFit    : iFit.Write()

              # 2D Scan
              if '2D' in acoupling['ScanConfig'] and len(acoupling['ScanConfig']['2D']) > 0 :
                for iScan in acoupling['Scans']['2D']:
                  operatorValuesX = sorted(set([x.split(":")[0] for x in acoupling['Scans']['2D'][iScan].keys()]),key=float)
                  operatorValuesY = sorted(set([x.split(":")[1] for x in acoupling['Scans']['2D'][iScan].keys()]),key=float)
                  operatorValuesFloatX = [float(x) for x in operatorValuesX]
                  operatorValuesFloatY = [float(x) for x in operatorValuesY]
                  # ... Get AC binning (and check) --> X=1st operator 
                  idxSMX  = operatorValuesFloatX.index(0.)
                  binWOpX = operatorValuesFloatX[idxSMX+1]-operatorValuesFloatX[idxSMX]
                  nBinOpX = len(operatorValuesFloatX)
                  xMinOpX = operatorValuesFloatX[0]-binWOpX/2.
                  xMaxOpX = operatorValuesFloatX[nBinOpX-1]+binWOpX/2.
                  check_binW=True
                  for i in range(len(operatorValuesFloatX)-1) :
                    if not operatorValuesFloatX[i]+binWOpX == operatorValuesFloatX[i+1] : check_binW=False
                  if not check_binW:
                    print 'AC Grid Bin Width Error -> Exit !!!!'
                    exit()
                  # ... Get AC binning (and check) --> Y=2nd operator
                  idxSMY  = operatorValuesFloatY.index(0.)
                  binWOpY = operatorValuesFloatY[idxSMY+1]-operatorValuesFloatY[idxSMY]
                  nBinOpY = len(operatorValuesFloatY)
                  xMinOpY = operatorValuesFloatY[0]-binWOpY/2.
                  xMaxOpY = operatorValuesFloatY[nBinOpY-1]+binWOpY/2.
                  check_binW=True
                  for i in range(len(operatorValuesFloatY)-1) :
                    if not operatorValuesFloatY[i]+binWOpY == operatorValuesFloatY[i+1] : check_binW=False
                  if not check_binW:
                    print 'AC Grid Bin Width Error -> Exit !!!!'
                    exit()
                  # ... Get All input histograms + binning
                  inputHistos = []
                  iX=-1
                  for opValX in operatorValuesX :
                    inputHistos.append([])
                    iX+=1
                    for opValY in operatorValuesY :
                      hName = 'histo_'+acoupling['sigName'].replace('${iWeight}',str(acoupling['Scans']['2D'][iScan][opValX+':'+opValY]))
                      inputHistos[iX].append(inputFile.Get(baseDir+'/'+subDir+'/'+hName).Clone())
                  nBinVar=inputHistos[0][0].GetNbinsX()     
                  # ... Create & Fill output histograms
                  outputHistos = []
                  outputFile.mkdir(baseDir+'/'+subDir+'/'+iScan.replace(":","_"))
                  outputFile.cd(baseDir+'/'+subDir+'/'+iScan.replace(":","_"))
                  for iBinVar in range(nBinVar):
                    #hName = 'histo_'+subDir+'_'+iScan.replace(":","_")+'_'+str(iBinVar)
                    hName = 'bin_content_par1_par2_'+str(iBinVar+1)
                    outputHistos.append( ROOT.TH2D(hName,hName,nBinOpX,xMinOpX,xMaxOpX,nBinOpY,xMinOpY,xMaxOpY) )
                    SMVal=inputHistos[idxSMX][idxSMY].GetBinContent(iBinVar+1)
                    for opValX in operatorValuesX :
                      idxX=operatorValuesX.index(opValX)
                      for opValY in operatorValuesY :
                        idxY=operatorValuesY.index(opValY)
                        varVal=inputHistos[idxX][idxY].GetBinContent(iBinVar+1)/SMVal
                        varErr=inputHistos[idxX][idxY].GetBinError(iBinVar+1)/SMVal  
                        outputHistos[iBinVar].SetBinContent(idxX+1,idxY+1,varVal) 
                        outputHistos[iBinVar].SetBinError(idxX+1,idxY+1,varErr) 
                  # ... Fitting model
                  outputFit = []
                  for iBinVar in range(nBinVar):
                    #fName = 'fit_'+subDir+'_'+iScan.replace(":","_")+'_'+str(iBinVar)
                    fName = 'bin_content_par1_par2_'+str(iBinVar+1)
                    outputFit.append( ROOT.TF2(fName,"[0]+[1]*x+[2]*y+[3]*x*x+[4]*y*y+[5]*x*y",xMinOpX*3.,xMaxOpX*3.,xMinOpY*3.,xMaxOpY*3.) )
                    outputHistos[iBinVar].Fit(outputFit[iBinVar],"RME")
                    #ROOT.gPad.WaitPrimitive()

                  # ... Save all  
                  for iHist in outputHistos : iHist.Write()  
                  for iFit  in outputFit    : iFit.Write() 


              # 3D Scan
              if '3D' in acoupling['ScanConfig'] and len(acoupling['ScanConfig']['3D']) > 0 :
                for iScan in acoupling['Scans']['3D']:
                  operatorValuesX = sorted(set([x.split(":")[0] for x in acoupling['Scans']['3D'][iScan].keys()]),key=float)
                  operatorValuesY = sorted(set([x.split(":")[1] for x in acoupling['Scans']['3D'][iScan].keys()]),key=float)
                  operatorValuesZ = sorted(set([x.split(":")[2] for x in acoupling['Scans']['3D'][iScan].keys()]),key=float)
                  operatorValuesFloatX = [float(x) for x in operatorValuesX]
                  operatorValuesFloatY = [float(x) for x in operatorValuesY]
                  operatorValuesFloatZ = [float(x) for x in operatorValuesZ]
                  # ... Get AC binning (and check) --> X=1st operator 
                  idxSMX  = operatorValuesFloatX.index(0.)
                  binWOpX = operatorValuesFloatX[idxSMX+1]-operatorValuesFloatX[idxSMX]
                  nBinOpX = len(operatorValuesFloatX)
                  xMinOpX = operatorValuesFloatX[0]-binWOpX/2.
                  xMaxOpX = operatorValuesFloatX[nBinOpX-1]+binWOpX/2.
                  check_binW=True
                  for i in range(len(operatorValuesFloatX)-1) :
                    if not operatorValuesFloatX[i]+binWOpX == operatorValuesFloatX[i+1] : check_binW=False
                  if not check_binW:
                    print 'AC Grid Bin Width Error -> Exit !!!!'
                    exit()
                  # ... Get AC binning (and check) --> Y=2nd operator
                  idxSMY  = operatorValuesFloatY.index(0.)
                  binWOpY = operatorValuesFloatY[idxSMY+1]-operatorValuesFloatY[idxSMY]
                  nBinOpY = len(operatorValuesFloatY)
                  xMinOpY = operatorValuesFloatY[0]-binWOpY/2.
                  xMaxOpY = operatorValuesFloatY[nBinOpY-1]+binWOpY/2.
                  check_binW=True
                  for i in range(len(operatorValuesFloatY)-1) :
                    if not operatorValuesFloatY[i]+binWOpY == operatorValuesFloatY[i+1] : check_binW=False
                  if not check_binW:
                    print 'AC Grid Bin Width Error -> Exit !!!!'
                    exit()
                  # ... Get AC binning (and check) --> Z=3rd operator
                  idxSMZ  = operatorValuesFloatZ.index(0.)
                  binWOpZ = operatorValuesFloatZ[idxSMZ+1]-operatorValuesFloatZ[idxSMZ]
                  nBinOpZ = len(operatorValuesFloatZ)
                  xMinOpZ = operatorValuesFloatZ[0]-binWOpZ/2.
                  xMaxOpZ = operatorValuesFloatZ[nBinOpZ-1]+binWOpZ/2.
                  check_binW=True
                  for i in range(len(operatorValuesFloatZ)-1) :
                    if not operatorValuesFloatZ[i]+binWOpZ == operatorValuesFloatZ[i+1] : check_binW=False
                  if not check_binW:
                    print 'AC Grid Bin Width Error -> Exit !!!!'
                    exit()
                  # ... Get All input histograms + binning
                  inputHistos = []
                  iX=-1
                  for opValX in operatorValuesX :
                    inputHistos.append([])
                    iX+=1
                    iY=-1
                    for opValY in operatorValuesY :
                      inputHistos[iX].append([]) 
                      iY+=1
                      iZ=-1
                      for opValZ in operatorValuesZ :
                        iZ+=1
                        try: 
                          hName = 'histo_'+acoupling['sigName'].replace('${iWeight}',str(acoupling['Scans']['3D'][iScan][opValX+':'+opValY+':'+opValZ]))
                          inputHistos[iX][iY].append(inputFile.Get(baseDir+'/'+subDir+'/'+hName).Clone())
                        except:
                         #try:
                         #  Fix = acoupling['ScansFix']['3D'][iScan][opValX+':'+opValY+':'+opValZ]
                         #  print 'Missing point: ',opValX+':'+opValY+':'+opValZ,'--> Taking: ',Fix
                         #except:
                            print 'Missing point: ',opValX+':'+opValY+':'+opValZ,'--> Please provide acoupling[ScansFix] !!!!'
                            exit()
                         #hName = 'histo_'+acoupling['sigName'].replace('${iWeight}',str(acoupling['Scans']['3D'][iScan][Fix]))
                         #inputHistos[iX][iY].append(inputFile.Get(baseDir+'/'+subDir+'/'+hName).Clone())
                         #nBinVar=inputHistos[iX][iY][iZ].GetNbinsX()
                         #for iBinVar in range(nBinVar):
                         #  Err=inputHistos[iX][iY][iZ].GetBinContent(iBinVar+1)*0.99
                         #  inputHistos[iX][iY][iZ].SetBinError(iBinVar+1,Err)
                  nBinVar=inputHistos[0][0][0].GetNbinsX()     
                  # ... Create & Fill output histograms
                  outputHistos = []
                  outputFile.mkdir(baseDir+'/'+subDir+'/'+iScan.replace(":","_"))
                  outputFile.cd(baseDir+'/'+subDir+'/'+iScan.replace(":","_"))
                  for iBinVar in range(nBinVar):
                    #hName = 'histo_'+subDir+'_'+iScan.replace(":","_")+'_'+str(iBinVar)
                    hName = 'bin_content_par1_par2_par3_'+str(iBinVar+1)
                    outputHistos.append( ROOT.TH3D(hName,hName,nBinOpX,xMinOpX,xMaxOpX,nBinOpY,xMinOpY,xMaxOpY,nBinOpZ,xMinOpZ,xMaxOpZ) )
                    SMVal=inputHistos[idxSMX][idxSMY][idxSMZ].GetBinContent(iBinVar+1)
                    for opValX in operatorValuesX :
                      idxX=operatorValuesX.index(opValX)
                      for opValY in operatorValuesY :
                        idxY=operatorValuesY.index(opValY)
                        for opValZ in operatorValuesZ :
                          idxZ=operatorValuesZ.index(opValZ)
                          varVal=inputHistos[idxX][idxY][idxZ].GetBinContent(iBinVar+1)/SMVal
                          varErr=inputHistos[idxX][idxY][idxZ].GetBinError(iBinVar+1)/SMVal  
                          outputHistos[iBinVar].SetBinContent(idxX+1,idxY+1,idxZ+1,varVal) 
                          outputHistos[iBinVar].SetBinError(idxX+1,idxY+1,idxZ+1,varErr) 
                  # ... Fitting model
                  outputFit = []
                  for iBinVar in range(nBinVar):
                    #fName = 'fit_'+subDir+'_'+iScan.replace(":","_")+'_'+str(iBinVar)
                    fName = 'bin_content_par1_par2_par3_'+str(iBinVar+1)
                    outputFit.append( ROOT.TF3(fName,"[0]+[1]*x+[2]*y+[3]*x*x+[4]*y*y+[5]*x*y+[6]*z+[7]*z*z+[8]*x*z+[9]*y*z",xMinOpX*3.,xMaxOpX*3.,xMinOpY*3.,xMaxOpY*3.,xMinOpZ*3.,xMaxOpZ*3.) )
                    outputHistos[iBinVar].Fit(outputFit[iBinVar],"RME")

                  # ... Save all  
                  for iHist in outputHistos : iHist.Write()  
                  for iFit  in outputFit    : iFit.Write() 

    # Close Root Files
    inputFile.Close()
    outputFile.Close()
 
