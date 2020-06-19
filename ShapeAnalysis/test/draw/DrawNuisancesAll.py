#!/usr/bin/env python

#import json
import sys
import os
import ROOT
import optparse



if __name__ == '__main__':
    print '''
--------------------------------------------------------------------------------------------------

  __ \                               \  |        _)                                       
  |   |   __|  _` | \ \  \   /        \ |  |   |  |   __|   _` |  __ \    __|   _ \   __| 
  |   |  |    (   |  \ \  \ /       |\  |  |   |  | \__ \  (   |  |   |  (      __/ \__ \ 
 ____/  _|   \__,_|   \_/\_/       _| \_| \__,_| _| ____/ \__,_| _|  _| \___| \___| ____/ 
                                                                                          
--------------------------------------------------------------------------------------------------
'''    

    usage = 'usage: %prog [options]'
    parser = optparse.OptionParser(usage)

    parser.add_option('--outputDirPlots' , dest='outputDirPlots' , help='output directory'                           , default='./')
    parser.add_option('--inputFile'      , dest='inputFile'      , help='input file with histograms'                 , default='input.root')
    parser.add_option('--nuisancesFile'  , dest='nuisancesFile'  , help='file with nuisances configurations'         , default=None )
    parser.add_option('--samplesFile'    , dest='samplesFile'    , help='file with samples'                          , default=None )
    parser.add_option('--cutName'        , dest='cutName'        , help='cut names'                                  , default=None )
    parser.add_option('--splitStat'      , dest='splitStat'      , help='draw statistics one bin per plot'           , default=None )
    parser.add_option('--dryRun'         , dest='dryRun'         , help='allow a dry run only '                      , default=None )
    parser.add_option('--drawYields'     , dest='drawYields'     , help='draw yields of the plots '                  , default='0' )
    parser.add_option('--joinSubsamples' , dest='joinSubsamples' , help='Add the histograms of subsamples'           , default='0' )
    parser.add_option('--onlySample'    , dest='onlySample'     , help='Only plot the requested sample '            , default=None )
    

    (opt, args) = parser.parse_args()

    sys.argv.append( '-b' )
    ROOT.gROOT.SetBatch()

    print " inputFile =           ", opt.inputFile
    print " nuisancesFile =       ", opt.nuisancesFile
    print " samplesFile =         ", opt.samplesFile
    print " outputDirPlots =      ", opt.outputDirPlots
    print " cutName =             ", opt.cutName
    print " splitStat =           ", opt.splitStat
    print " dryRun  =             ", opt.dryRun
    print " drawYields  =         ", opt.drawYields
    print " joinSubsamples  =     ", opt.joinSubsamples
    print " onlySample  =         ", opt.onlySample

    
    
    os.system ("mkdir " + opt.outputDirPlots + "/") 

    
    samples = {}
    if os.path.exists(opt.samplesFile) :
      handle = open(opt.samplesFile,'r')
      exec(handle)
      handle.close()

    if opt.joinSubsamples == '0':
      subsamples = {}
      for sampleName, sample in samples.items():
        if "subsamples" in sample: 
          for subs in sample["subsamples"]:
            subsamples[sampleName+"_"+subs] = {}
      samples.update(subsamples)
      

    nuisances = {}
    if os.path.exists(opt.nuisancesFile) :
      handle = open(opt.nuisancesFile,'r')
      exec(handle)
      handle.close()

    ROOTinputFile = ROOT.TFile.Open( opt.inputFile, 'READ')

    # for list_histos in ROOTinputFile.GetListOfKeys() :
    #     print " --> ", list_histos

    
    texOutputFile =  open( 'plot_' + opt.cutName + '.tex' ,"w")
    texOutputFile.write('\n')

    # loop over nuisances
    for sampleName, sample in samples.iteritems():
      if opt.onlySample and opt.onlySample not in sampleName: continue
    
      nameNominal = 'histo_' + sampleName
      nbins = 100
      if nameNominal in ROOTinputFile.GetListOfKeys() :
        histoNominal = ROOTinputFile.Get(nameNominal)
        nbins = histoNominal.GetNbinsX()

      print " nbins = ", nbins

      texOutputFile.write('\n')      
      texOutputFile.write('\n')
      texOutputFile.write('\\begin{figure*}[htbp]  \n')
      texOutputFile.write('\\centering \n')

      counterNuisance = 0

      for nuisanceName, nuisance in nuisances.iteritems(): 
        #print " nuisanceName = ", nuisanceName
        #print " nuisance = ", nuisance
        if 'name' in nuisance.keys() :
          
          if 'skipCMS' in nuisance and nuisance['skipCMS'] == 1:
            entryName = nuisance['name']
          else:
            entryName = 'CMS_' + nuisance['name']

          nameDown = 'histo_' + sampleName + '_' + entryName + 'Down'
          nameUp   = 'histo_' + sampleName + '_' + entryName + 'Up'          
          
          print " nameDown = ", nameDown
          print " nameUp   = ", nameUp
          
          if nameDown in ROOTinputFile.GetListOfKeys() :

            print ('root -b -q DrawNuisances.cxx\(\\\"' + opt.inputFile + '\\\",\\\"' + nameNominal + '\\\",\\\"' + nameUp + '\\\",\\\"' + nameDown + '\\\",\\\"' + opt.outputDirPlots + '\\\",\\\"' + opt.drawYields + '\\\"\) ')
            if opt.dryRun == None :
              os.system ('root -b -q DrawNuisances.cxx\(\\\"' + opt.inputFile + '\\\",\\\"' + nameNominal + '\\\",\\\"' + nameUp + '\\\",\\\"' + nameDown + '\\\",\\\"' + opt.outputDirPlots + '\\\",\\\"' + opt.drawYields + '\\\"\) ')

            texOutputFile.write('\\includegraphics[width=0.09\\textwidth]{Figs/Nuisance/'+ opt.outputDirPlots + '/cc_' + nameUp +'.png}')
            
            counterNuisance += 1
            if counterNuisance >= 9 :
              counterNuisance = 0
              texOutputFile.write('\\\\')
            texOutputFile.write('\n')

        else :
          if nuisanceName == 'stat' : # 'stat' has a separate treatment, it's the MC/data statistics
            if 'samples' in nuisance.keys():
              if sampleName in nuisance['samples'].keys() :
                if opt.splitStat == None :  
                  nameDown = 'histo_' + sampleName + '_CMS_' + opt.cutName + '_' + sampleName + '_ibin_'
                  nameUp   = 'histo_' + sampleName + '_CMS_' + opt.cutName + '_' + sampleName + '_ibin_'
                  print ('root -b -q DrawNuisancesStat.cxx\(\\\"' + opt.inputFile + '\\\",\\\"' + nameNominal + '\\\",\\\"' + nameUp + '\\\",\\\"' + nameDown + '\\\",\\\"' + opt.outputDirPlots + '\\\",\\\"' + opt.drawYields + '\\\"\) ')
                  if opt.dryRun == None :
                    os.system ('root -b -q DrawNuisancesStat.cxx\(\\\"' + opt.inputFile + '\\\",\\\"' + nameNominal + '\\\",\\\"' + nameUp + '\\\",\\\"' + nameDown + '\\\",\\\"' + opt.outputDirPlots + '\\\",\\\"' + opt.drawYields + '\\\"\) ')

                else :
                  for iBin in range(1, nbins): # max number of bins
                    print iBin
                    nameDown = 'histo_' + sampleName + '_CMS_' + opt.cutName + '_' + sampleName + '_ibin_' + str(iBin) + '_stat' + 'Down'
                    nameUp   = 'histo_' + sampleName + '_CMS_' + opt.cutName + '_' + sampleName + '_ibin_' + str(iBin) + '_stat' + 'Up'         
                    if nameDown in ROOTinputFile.GetListOfKeys() :
                      print ('root -b -q DrawNuisances.cxx\(\\\"' + opt.inputFile + '\\\",\\\"' + nameNominal + '\\\",\\\"' + nameUp + '\\\",\\\"' + nameDown + '\\\",\\\"' + opt.outputDirPlots + '\\\"\) ')
                      if opt.dryRun == None :
                        os.system ('root -b -q DrawNuisances.cxx\(\\\"' + opt.inputFile + '\\\",\\\"' + nameNominal + '\\\",\\\"' + nameUp + '\\\",\\\"' + nameDown + '\\\",\\\"' + opt.outputDirPlots + '\\\"\) ')
                      
                  texOutputFile.write('\\includegraphics[width=0.10\\textwidth]{Figs/Nuisance/'+ opt.outputDirPlots + '/cc_' + nameUp +'.png}')
                    
                  counterNuisance += 1
                  if counterNuisance >= 9 :
                    counterNuisance = 0
                    texOutputFile.write('\\\\')
                  texOutputFile.write('\n')
            
  
      texOutputFile.write('\\\\ \n')      
      texOutputFile.write('\\caption{ \n')
      texOutputFile.write('   Distributions for ' + (sampleName).replace('_', '-') + ' of nuisances effects for ' + (opt.cutName).replace('_', '-') + ' selections.\n')
      texOutputFile.write('} \n')
      texOutputFile.write('\\label{fig:' + sampleName + '_' + opt.cutName + '} \n')
      texOutputFile.write('\\end{figure*} \n')
      texOutputFile.write('\n')
      texOutputFile.write('\n')
    




