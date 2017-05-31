#!/usr/bin/env python

import json
import sys
from sys import exit
import ROOT
import optparse
import LatinoAnalysis.Gardener.hwwtools as hwwtools
import os.path
import string
import logging
import LatinoAnalysis.Gardener.odict as odict
import traceback
from array import array
from collections import OrderedDict
import math

import os

#import os.path



# ----------------------------------------------------- ShapeFactory --------------------------------------

class ShapeFactory:
    _logger = logging.getLogger('ShapeFactory')
 
    # _____________________________________________________________________________
    def __init__(self):

        cuts = {}
        self._cuts = cuts

        samples = OrderedDict()
        self._samples = samples

        outputDirPDF = {}
        self._outputDirPDF = outputDirPDF

    # _____________________________________________________________________________
    def _connectInputs(self, samples, inputDir, skipMissingFiles):
        inputs = {}
        histoName = 'list_vectors_weights'
        for process,filenames in samples.iteritems():
          histo = self._buildchainHisto(histoName,[ (inputDir + '/' + f) for f in filenames], skipMissingFiles)
          inputs[process] = histo 
          #print ' process -> ', process, ' => ', inputs[process]
        return inputs

    # _____________________________________________________________________________
    def _buildchainHisto(self, histoName, files, skipMissingFiles):
        
        self._outFile.cd()
        #histoSum = ROOT.TH1F
        isFirstOne = True
        for path in files:
            doesFileExist = True
            self._logger.debug('     '+str(os.path.exists(path))+' '+path)
            if "eos.cern.ch" not in path and "eosuser.cern.ch" not in path:
              if not os.path.exists(path):
                print 'File '+path+' doesn\'t exists'
                doesFileExist = False
                if not skipMissingFiles : raise RuntimeError('File '+path+' doesn\'t exists')
            else:
              if not self._testEosFile(path):
                doesFileExist = False
                if not skipMissingFiles : raise RuntimeError('File '+path+' doesn\'t exists')
            if doesFileExist :
              fileIn = ROOT.TFile(path)
              print " path = ", path
              if isFirstOne :
                self._outFile.cd()
                histoSum = (fileIn.Get(histoName)).Clone()   
                #print ' histogram found : ', histoSum, ' :: ', histoName
                isFirstOne = False
              else :
                histoSumTemp = fileIn.Get(histoName)   
                histoSum.Add(histoSumTemp)
                #print ' histogram found again: ', histoSum
              
        return histoSum


    # _____________________________________________________________________________
    def _testEosFile(self,path): 
      eoususer='/afs/cern.ch/project/eos/installation/0.3.84-aquamarine.user/bin/eos.select'
      if 'eosuser.cern.ch' in path: 
        if os.system(eoususer+' ls '+path.split('/eosuser.cern.ch/')[1]) == 0 : return True
      return False 



    # _____________________________________________________________________________
    def makePDF(self, inputFile, outputDirPDF, cuts, samples, inputDir, structureFile):

        print "================="
        print "==== makePDF ===="
        print "================="

        # NB: the samples have to be OF THE SAME GENERATOR
        #     you cannot get pdf/qcd uncertainty mixing different samples
        #     like mixing A+B, where A is powheg and B is MG5.
        #     If you want to do this
        #     you "mix" it by hand from the output of this code ;)
        #
        
        self._samples   = samples
        self._cuts      = cuts

        self._outputDirPDF = outputDirPDF
        os.system ("mkdir " + outputDirPDF + "/") 

        fileIn = ROOT.TFile(inputFile, "READ")

        self._outFile = ROOT.TFile.Open( self._outputDirPDF + '/results_unc.root', 'recreate')       
        #ROOT.TH1.SetDefaultSumw2(True)

        # get the pre-any-cut histogram
        list_of_trees_to_connect = {}
        for sampleName, sample in self._samples.iteritems():
          list_of_trees_to_connect[sampleName] = sample['name']
              
        #                                                                    skipMissingFiles
        preCutsHistograms = self._connectInputs( list_of_trees_to_connect, inputDir, False)
        
        print ' preCutsHistograms = ', preCutsHistograms
        
        for cutName in self._cuts :
          print "cut = ", cutName, " :: ", cuts[cutName]
          
          # creating qqbar files
          summaryNuisanceFileQCDqq = open(self._outputDirPDF + '/summary_nuisance_qcd_qq_' + cutName + '.py', 'w')

          summaryNuisanceFileQCDqq.write("nuisances['QCDscale_qqbar_accept']  = { \n")
          summaryNuisanceFileQCDqq.write("    'name'  : 'QCDscale_qqbar_accept', \n")
          summaryNuisanceFileQCDqq.write("    'type'  : 'lnN', \n")
          summaryNuisanceFileQCDqq.write("    'samples'  : { \n")
            


          summaryNuisanceFilePDFqq = open(self._outputDirPDF + '/summary_nuisance_pdf_qq_' + cutName + '.py', 'w')

          summaryNuisanceFilePDFqq.write("nuisances['pdf_qqbar_accept']  = { \n")
          summaryNuisanceFilePDFqq.write("    'name'  : 'pdf_qqbar_accept', \n")
          summaryNuisanceFilePDFqq.write("    'type'  : 'lnN', \n")
          summaryNuisanceFilePDFqq.write("    'samples'  : { \n")



          summaryNuisanceFileAlphaqq = open(self._outputDirPDF + '/summary_nuisance_alpha_qq_' + cutName + '.py', 'w')

          summaryNuisanceFileAlphaqq.write("nuisances['Alphascale_qqbar_accept']  = { \n")
          summaryNuisanceFileAlphaqq.write("    'name'  : 'Alphascale_qqbar_accept', \n")
          summaryNuisanceFileAlphaqq.write("    'type'  : 'lnN', \n")
          summaryNuisanceFileAlphaqq.write("    'samples'  : { \n")



          summaryNuisanceFileAlphaPDFqq = open(self._outputDirPDF + '/summary_nuisance_alpha_pdf_qq_' + cutName + '.py', 'w')

          summaryNuisanceFileAlphaPDFqq.write("nuisances['Alphascale_pdf_qqbar_accept']  = { \n")
          summaryNuisanceFileAlphaPDFqq.write("    'name'  : 'Alphascale_pdf_qqbar_accept', \n")
          summaryNuisanceFileAlphaPDFqq.write("    'type'  : 'lnN', \n")
          summaryNuisanceFileAlphaPDFqq.write("    'samples'  : { \n")


          # creating gg files
          summaryNuisanceFileQCDgg = open(self._outputDirPDF + '/summary_nuisance_qcd_gg_' + cutName + '.py', 'w')

          summaryNuisanceFileQCDgg.write("nuisances['QCDscale_gg_accept']  = { \n")
          summaryNuisanceFileQCDgg.write("    'name'  : 'QCDscale_gg_accept', \n")
          summaryNuisanceFileQCDgg.write("    'type'  : 'lnN', \n")
          summaryNuisanceFileQCDgg.write("    'samples'  : { \n")
            


          summaryNuisanceFilePDFgg = open(self._outputDirPDF + '/summary_nuisance_pdf_gg_' + cutName + '.py', 'w')

          summaryNuisanceFilePDFgg.write("nuisances['pdf_gg_accept']  = { \n")
          summaryNuisanceFilePDFgg.write("    'name'  : 'pdf_gg_accept', \n")
          summaryNuisanceFilePDFgg.write("    'type'  : 'lnN', \n")
          summaryNuisanceFilePDFgg.write("    'samples'  : { \n")



          summaryNuisanceFileAlphagg = open(self._outputDirPDF + '/summary_nuisance_alpha_gg_' + cutName + '.py', 'w')

          summaryNuisanceFileAlphagg.write("nuisances['Alphascale_gg_accept']  = { \n")
          summaryNuisanceFileAlphagg.write("    'name'  : 'Alphascale_gg_accept', \n")
          summaryNuisanceFileAlphagg.write("    'type'  : 'lnN', \n")
          summaryNuisanceFileAlphagg.write("    'samples'  : { \n")



          summaryNuisanceFileAlphaPDFgg = open(self._outputDirPDF + '/summary_nuisance_alpha_pdf_gg_' + cutName + '.py', 'w')

          summaryNuisanceFileAlphaPDFgg.write("nuisances['Alphascale_pdf_gg_accept']  = { \n")
          summaryNuisanceFileAlphaPDFgg.write("    'name'  : 'Alphascale_pdf_gg_accept', \n")
          summaryNuisanceFileAlphaPDFgg.write("    'type'  : 'lnN', \n")
          summaryNuisanceFileAlphaPDFgg.write("    'samples'  : { \n")


          for sampleName, sample in self._samples.iteritems():
            
              #if structureFile[sampleName]['isFromGluons'] == 0 :
              tcanvas  = ROOT.TCanvas( "c_unc_" + cutName + "_" + sampleName,      "cc"     , 800, 600 )

              nominalRatio = 1.

              # get the after-cut histogram

              # qcd uncertainty
              low_qcd = 1
              high_qcd = 1
              for ipdf in range(0,10):
                  if (ipdf == 0 or ipdf == 4 or ipdf == 8) :
                      
                      variableName = 'weight_' + str(ipdf)
                      shapeName = cutName+"/"+variableName+'/histo_' + sampleName
                      histoAfterCuts = fileIn.Get(shapeName)
                      totalWeighted = 0
                      for iBin in range(1, histoAfterCuts.GetNbinsX()+1):
                          totalWeighted += histoAfterCuts.GetBinContent(iBin) * histoAfterCuts.GetBinCenter(iBin)
                          #print 'totalWeighted = ' + str(totalWeighted) 
                
                      denominator = preCutsHistograms[sampleName].GetBinContent(ipdf+1)
                      #print 'denominator = ' + str(denominator)

                      if denominator != 0 and nominalRatio != 0 :
                          #print 'totalWeighted = ' + str(totalWeighted)
                          #print 'denominator = ' + str(denominator)
                          if ipdf == 0 :
                              nominalRatio = totalWeighted/denominator
                              #print 'nominalRatio QCD = ' + str(nominalRatio)
                          elif ipdf == 4:
                              low_qcd = totalWeighted/denominator/nominalRatio
                              #print 'low_qcd = ' + str(low_qcd)
                          elif ipdf == 8:
                              high_qcd = totalWeighted/denominator/nominalRatio
                              #print 'high_qcd = ' + str(high_qcd)
                          elif denominator == 0 :
                              print 'Denominator is 0 !!!!'
                          elif nominalRatio == 0:
                              print 'nominalRatio is 0 !!!!'

              string_to_write = "         '" +  sampleName +  "': '%4.3f/%4.3f' ,\n" %(low_qcd, high_qcd)
              if structureFile[sampleName]['isFromGluons'] == 0 :
                  summaryNuisanceFileQCDqq.write( string_to_write )
              elif structureFile[sampleName]['isFromGluons'] == 1 :
                  summaryNuisanceFileQCDgg.write( string_to_write )
 
 
              # alpha uncertainty
              low_alpha = 1
              high_alpha = 1
              for ipdf in range(109,112):
                  if (ipdf == 109 or ipdf == 110) :
                      
                      variableName = 'weight_' + str(ipdf)
                      shapeName = cutName+"/"+variableName+'/histo_' + sampleName
                      histoAfterCuts = fileIn.Get(shapeName)
                      totalWeighted = 0
                      for iBin in range(1, histoAfterCuts.GetNbinsX()+1):
                          totalWeighted += histoAfterCuts.GetBinContent(iBin) * histoAfterCuts.GetBinCenter(iBin)
                
                      denominator = preCutsHistograms[sampleName].GetBinContent(ipdf+1)
                              
                      if denominator != 0 and nominalRatio != 0 :
                          if ipdf == 109 :
                              low_alpha = totalWeighted/denominator/nominalRatio
                          elif ipdf == 110:
                              high_alpha = totalWeighted/denominator/nominalRatio
                          elif denominator == 0 : 
                              print 'Denominator is 0 !!!!'
                          elif nominalRatio == 0:
                              print 'nominalRatio is 0 !!!!'
                
              string_to_write = "         '" +  sampleName +  "': '%4.3f/%4.3f' ,\n" %(low_alpha, high_alpha)
              if structureFile[sampleName]['isFromGluons'] == 0 :
                  summaryNuisanceFileAlphaqq.write( string_to_write )
              if structureFile[sampleName]['isFromGluons'] == 1 :
                  summaryNuisanceFileAlphagg.write( string_to_write )
              

        
              # pdf uncertainty
              histoRatioPDF = ROOT.TH1F('ratio_pdf_', cutName + '_' + sampleName, 100,0, 2)
              for ipdf in range(10,109):
                  variableName = 'weight_' + str(ipdf)
                  shapeName = cutName+"/"+variableName+'/histo_' + sampleName
                  histoAfterCuts = fileIn.Get(shapeName)
                  totalWeighted = 0
                  for iBin in range(1, histoAfterCuts.GetNbinsX()+1):
                      totalWeighted += histoAfterCuts.GetBinContent(iBin) * histoAfterCuts.GetBinCenter(iBin)
              
                  denominator = preCutsHistograms[sampleName].GetBinContent(ipdf+1)
              
                  if denominator != 0 and nominalRatio != 0 :
                      histoRatioPDF.Fill(totalWeighted/denominator/nominalRatio)
                  elif denominator == 0 :
                      print 'Denominator is 0 !!!!'
                      

              histoRatioPDF.Draw()
              tcanvas.SaveAs(self._outputDirPDF + "/" + "c_unc_" + cutName + "_" + sampleName + ".png")
              tcanvas.SaveAs(self._outputDirPDF + "/" + "c_unc_" + cutName + "_" + sampleName + ".root")

              tcanvas.Write()

              string_to_write = "         '" +  sampleName +  "': '%4.3f',\n" %(1. + histoRatioPDF.GetRMS())
              if structureFile[sampleName]['isFromGluons'] == 0 :
                  summaryNuisanceFilePDFqq.write( string_to_write )
              if structureFile[sampleName]['isFromGluons'] == 1 :
                  summaryNuisanceFilePDFgg.write( string_to_write )


              # pdf and alpha_s combined uncertainty

              high_alpha_pdf = 1. + math.sqrt(histoRatioPDF.GetRMS() * histoRatioPDF.GetRMS() + (1. - high_alpha) * (1. - high_alpha))
              low_alpha_pdf  = 1. / (1. + math.sqrt(histoRatioPDF.GetRMS() * histoRatioPDF.GetRMS() + (1. - low_alpha)  * (1. - low_alpha)))
              
              string_to_write = "         '" +  sampleName +  "': '%4.3f/%4.3f' ,\n" %(low_alpha_pdf, high_alpha_pdf)
              if structureFile[sampleName]['isFromGluons'] == 0 :
                  summaryNuisanceFileAlphaPDFqq.write( string_to_write )
              if structureFile[sampleName]['isFromGluons'] == 1 :
                  summaryNuisanceFileAlphaPDFgg.write( string_to_write )


          # closing qqbar files
          summaryNuisanceFilePDFqq.write("    }, \n")
          summaryNuisanceFilePDFqq.write(" } \n")
          summaryNuisanceFilePDFqq.write("\n")
          summaryNuisanceFilePDFqq.write("\n")
          summaryNuisanceFilePDFqq.close()
              
          summaryNuisanceFileQCDqq.write("    }, \n")
          summaryNuisanceFileQCDqq.write(" } \n")
          summaryNuisanceFileQCDqq.write("\n")
          summaryNuisanceFileQCDqq.write("\n")
          summaryNuisanceFileQCDqq.close()
              
          summaryNuisanceFileAlphaqq.write("    }, \n")
          summaryNuisanceFileAlphaqq.write(" } \n")
          summaryNuisanceFileAlphaqq.write("\n")
          summaryNuisanceFileAlphaqq.write("\n")
          summaryNuisanceFileAlphaqq.close()
              
          summaryNuisanceFileAlphaPDFqq.write("    }, \n")
          summaryNuisanceFileAlphaPDFqq.write(" } \n")
          summaryNuisanceFileAlphaPDFqq.write("\n")
          summaryNuisanceFileAlphaPDFqq.write("\n")
          summaryNuisanceFileAlphaPDFqq.close()
          
          
          # closing gg files
          summaryNuisanceFilePDFgg.write("    }, \n")
          summaryNuisanceFilePDFgg.write(" } \n")
          summaryNuisanceFilePDFgg.write("\n")
          summaryNuisanceFilePDFgg.write("\n")
          summaryNuisanceFilePDFgg.close()
              
          summaryNuisanceFileQCDgg.write("    }, \n")
          summaryNuisanceFileQCDgg.write(" } \n")
          summaryNuisanceFileQCDgg.write("\n")
          summaryNuisanceFileQCDgg.write("\n")
          summaryNuisanceFileQCDgg.close()
              
          summaryNuisanceFileAlphagg.write("    }, \n")
          summaryNuisanceFileAlphagg.write(" } \n")
          summaryNuisanceFileAlphagg.write("\n")
          summaryNuisanceFileAlphagg.write("\n")
          summaryNuisanceFileAlphagg.close()
              
          summaryNuisanceFileAlphaPDFgg.write("    }, \n")
          summaryNuisanceFileAlphaPDFgg.write(" } \n")
          summaryNuisanceFileAlphaPDFgg.write("\n")
          summaryNuisanceFileAlphaPDFgg.write("\n")
          summaryNuisanceFileAlphaPDFgg.close()


          # merging and cleaning ;)

        for cutName in self._cuts :
            filenames = [self._outputDirPDF + '/summary_nuisance_pdf_gg_' + cutName + '.py',self._outputDirPDF + '/summary_nuisance_pdf_qq_' + cutName + '.py']
            with open(self._outputDirPDF + '/summary_nuisance_pdf_' + cutName + '.py', 'w') as outfile:
                for fname in filenames:
                    with open(fname) as infile:
                        outfile.write(infile.read())
            for fname in filenames:
                os.system('rm ' + fname)

            filenames = [self._outputDirPDF + '/summary_nuisance_qcd_gg_' + cutName + '.py',self._outputDirPDF + '/summary_nuisance_qcd_qq_' + cutName + '.py']
            with open(self._outputDirPDF + '/summary_nuisance_qcd_' + cutName + '.py', 'w') as outfile:
                for fname in filenames:
                    with open(fname) as infile:
                        outfile.write(infile.read())
            for fname in filenames:
                os.system('rm ' + fname)

            filenames = [self._outputDirPDF + '/summary_nuisance_alpha_gg_' + cutName + '.py',self._outputDirPDF + '/summary_nuisance_alpha_qq_' + cutName + '.py']
            with open(self._outputDirPDF + '/summary_nuisance_alpha_' + cutName + '.py', 'w') as outfile:
                for fname in filenames:
                    with open(fname) as infile:
                        outfile.write(infile.read())
            for fname in filenames:
                os.system('rm ' + fname)

            filenames = [self._outputDirPDF + '/summary_nuisance_alpha_pdf_gg_' + cutName + '.py',self._outputDirPDF + '/summary_nuisance_alpha_pdf_qq_' + cutName + '.py']
            with open(self._outputDirPDF + '/summary_nuisance_alpha_pdf_' + cutName + '.py', 'w') as outfile:
                for fname in filenames:
                    with open(fname) as infile:
                        outfile.write(infile.read())
            for fname in filenames:
                os.system('rm ' + fname)


        print " >> all but really all "
        


   # _____________________________________________________________________________
   # --- squared sum
    def SumQ(self, A, B):
       return math.sqrt(A*A + B*B)

   # _____________________________________________________________________________
   # --- Ratio: if denominator is zero, then put 0!
    def Ratio(self, A, B):
       if B == 0:
         #print "divide by 0"
         return 0.
       else :
         return A / B
 
                  
   # _____________________________________________________________________________
    def GetMaximumIncludingErrors(self, histo):
        maxWithErrors = 0.
        for iBin in range(1, histo.GetNbinsX()+1):
          binHeight = histo.GetBinContent (iBin) + histo.GetBinError (iBin)
          if binHeight > maxWithErrors :
            maxWithErrors = binHeight
      
        return maxWithErrors;

   # _____________________________________________________________________________
    def GetMinimum(self, histo):
        minimum = -1.
        for iBin in range(1, histo.GetNbinsX()+1):
          binHeight = histo.GetBinContent (iBin)
          if binHeight < minimum or minimum<0:
            minimum = binHeight
      
        return minimum;
 
 
    # _____________________________________________________________________________
    def defineStyle(self):

        print "=================="
        import LatinoAnalysis.ShapeAnalysis.tdrStyle as tdrStyle
        tdrStyle.setTDRStyle()
        
        ROOT.TGaxis.SetExponentOffset(-0.08, 0.00,"y")

        
   


if __name__ == '__main__':
    print '''
--------------------------------------------------------------------------------------------------



   _ \   __ \   ____|                                      |          _)         |          
  |   |  |   |  |          |   |  __ \    __|   _ \   __|  __|   _` |  |  __ \   __|  |   | 
  ___/   |   |  __|        |   |  |   |  (      __/  |     |    (   |  |  |   |  |    |   | 
 _|     ____/  _|         \__,_| _|  _| \___| \___| _|    \__| \__,_| _| _|  _| \__| \__, | 
                                                                                     ____/  

 
--------------------------------------------------------------------------------------------------
'''    
    usage = 'usage: %prog [options]'
    parser = optparse.OptionParser(usage)

    parser.add_option('--outputDirPDF'   , dest='outputDirPDF'   , help='output directory for values and plots'           , default='./')
    parser.add_option('--inputFile'      , dest='inputFile'      , help='input file with histograms'                      , default='input.root')
    parser.add_option('--inputDir'       , dest='inputDir'       , help='input directory where to find the default trees' , default='./data/')
    parser.add_option('--structureFile'      , dest='structureFile'     , help='file with datacard configurations'          , default=None )
          
    # read default parsing options as well
    hwwtools.addOptions(parser)
    hwwtools.loadOptDefaults(parser)
    (opt, args) = parser.parse_args()

    sys.argv.append( '-b' )
    ROOT.gROOT.SetBatch()


    print " configuration file = ", opt.pycfg
    
    print " inputFile          = ", opt.inputFile
    print " outputDirPDF       = ", opt.outputDirPDF
    print " inputDir           = ", opt.inputDir
     
    if not opt.debug:
        pass
    elif opt.debug == 2:
        print 'Logging level set to DEBUG (%d)' % opt.debug
        logging.basicConfig( level=logging.DEBUG )
    elif opt.debug == 1:
        print 'Logging level set to INFO (%d)' % opt.debug
        logging.basicConfig( level=logging.INFO )

      
    factory = ShapeFactory()
    
    cuts = {}
    if os.path.exists(opt.cutsFile) :
      handle = open(opt.cutsFile,'r')
      exec(handle)
      handle.close()
    
    samples = OrderedDict()
    if os.path.exists(opt.samplesFile) :
      handle = open(opt.samplesFile,'r')
      exec(handle)
      handle.close()
    
   
    # ~~~~
    structure = {}
    if opt.structureFile == None :
       print " Please provide the datacard structure "
       exit ()
       
    if os.path.exists(opt.structureFile) :
      handle = open(opt.structureFile,'r')
      exec(handle)
      handle.close()


    factory.makePDF( opt.inputFile ,opt.outputDirPDF, cuts, samples, opt.inputDir, structure)
    
    print '... and now closing ...'
        
       
