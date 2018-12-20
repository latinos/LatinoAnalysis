#!/usr/bin/env python

import json
import sys
# bypass ROOT argv parsing
argv = sys.argv
sys.argv = argv[:1]
import ROOT
import optparse
import copy
#import hwwinfo
#import hwwsamples
#import hwwtools
import LatinoAnalysis.Gardener.hwwtools as hwwtools
import os.path
import string
import logging
import LatinoAnalysis.Gardener.odict as odict
#from HWWAnalysis.Misc.ROOTAndUtils import TH1AddDirSentry
import traceback
from array import array
import subprocess
import threading, Queue
from LatinoAnalysis.ShapeAnalysis.ShapeFactory import ShapeFactory

# Common Tools & batch
#from LatinoAnalysis.Tools.userConfig  import *
from LatinoAnalysis.Tools.commonTools import *
from LatinoAnalysis.Tools.batchTools  import *


# ----------------------------------------------------- Worker --------------------------------------

class Worker(threading.Thread):
  def __init__(self, queue):
    threading.Thread.__init__(self)
    self.queue = queue
    self.status = -1

  def run(self):
    while True:
      try:

        params = self.queue.get()
        inputDir = params[0]
        outputDir = params[1]
        variables = params[2]
        cuts = params[3]
        samples = params[4]
        nuisances = params[5]
        supercut = params[6]
        number = params[7]
        energy = params[8]
        lumi = params[9]
        tag = params[10]

        infile = ""
        infile += "from LatinoAnalysis.ShapeAnalysis.ShapeFactory import ShapeFactory\n\n"
        infile += "factory = ShapeFactory()\n"
        infile += "factory._treeName  = '"+opt.treeName+"'\n"
        infile += "factory._energy    = '"+str(energy)+"'\n"
        infile += "factory._lumi      = "+str(lumi)+"\n"
        infile += "factory._tag       = '"+str(tag)+"'\n"

        #infile += "factory.makeNominals('"+inputDir+"','"+outputDir+"',"+str(variables)+","+str(cuts)+","+str(samples)+","+str(nuisances)+",'"+supercut+"',"+str(number)+")\n"

        infile += "factory.makeNominals(   \n"
        infile += "     '" + inputDir+"',    \n"
        infile += "     '"+outputDir+"',     \n"
        infile += "      "+str(variables)+", \n"
        infile += "      "+str(cuts)+",      \n"
        infile += "      "+str(samples)+",   \n"
        infile += "      "+str(nuisances)+", \n"
        infile += "     '"+supercut+"',      \n"
        infile += "      "+str(number)+")    \n"


        sub_file = open("sub"+str(number)+".py","w")
        sub_file.write(infile)
        sub_file.close()

        theKey=samples.keys()[0]
        print 'task initiated --> '+str(cuts.keys())+' , '+str(samples.keys())+' , '+str(samples[theKey]['name'])

        logfile = open("log/log" + str(number) + "_" + str(cuts.keys()[0]) + "_" + str(samples.keys()[0]) + ".txt","w")
        command = "python "+sub_file.name
        process = subprocess.Popen(command, shell=True, stdout=logfile, stderr=logfile)
        process.wait()
        self.status = process.returncode
        #print 'task finished with exit code '+str(self.status)+'   [0 is good] --> '+str(cuts.keys())+' , '+str(samples.keys())+' , '+str(samples[theKey]['name'])
        
        if (self.status) == 0 :
          print 'task finished with exit code ' +str(self.status)+'   [0 is good] --> '+str(cuts.keys())+' , '+str(samples.keys())+' , '+str(samples[theKey]['name'])
        else :
          print 'task finished with exit code ' + '\x1b[0;30;41m' +  '   ' + str(self.status) +  '   ' +  '\x1b[0m' + '   [0 is good] --> '+str(cuts.keys())+' , '+str(samples.keys())+' , '+str(samples[theKey]['name'])





        self.queue.task_done()
      except Queue.Empty, e:
        break
      except Exception, e:
        print "Error: %s" % str(e)


def getEffectiveBaseW(histo, lumi):

  ### returns the effective baseW
  baseW = histo.Integral()/histo.GetEntries()/lumi if histo.GetEntries()>0 else 0.
  return baseW

#BUGFIX by Andrea: adding central distribution to variables in the function
def scaleHistoStat(histo, hvaried, direction, iBinToChange, lumi, zeroMCerror):
  integral = 0.
  integralVaried = 0.

  # how to handle the case when you have a bin with 0 MC
  # if the flag is activated, put the equivalent FC coverage 1.64 * 1 MC for the up variation
  basew = getEffectiveBaseW(histo, lumi)
  #print "###DEBUG: Effective baseW = ", basew
  for iBin in range(1, histo.GetNbinsX()+1):
    error = histo.GetBinError(iBin)
    value = histo.GetBinContent(iBin)
    integral += value
    if iBin == iBinToChange :
      if zeroMCerror==1:
        if value == 0:
          #print "###DEBUG: 0 MC stat --> value = ", value, " error = ", error
          if direction == 1:
            #print "###DEBUG: lumi = ", float(lumi), " basew = ", basew
            newvalue = 1.64*float(lumi)*basew
            #print "###DEBUG: new value up = ", newvalue
          else:
            #newvalue = 0
            #BUGFIX by Xavier: never put real Zero (BOGUS combine error)
            newvalue = float(lumi)*basew * 0.0001
        else:
          newvalue = value + direction * error
          #BUGFIX by Xavier: never put real Zero (BOGUS combine error)
          if newvalue == 0 : newvalue = value * 0.0001
      else:
        newvalue = value + direction * error
        #BUGFIX by Xavier: never put real Zero (BOGUS combine error)
        if newvalue == 0 : newvalue = value * 0.0001
    else :
      newvalue = value
    integralVaried += newvalue
    hvaried.SetBinContent(iBin, newvalue)
#BUGFIX by Andrea: The modified histograms now have the new values computed starting from the nominal ones



if __name__ == '__main__':
    sys.argv = argv

    print '''
--------------------------------------------------------------------------------------------------

   ___|   |                               \  |         |                
 \___ \   __ \    _` |  __ \    _ \      |\/ |   _` |  |  /   _ \   __| 
       |  | | |  (   |  |   |   __/      |   |  (   |    <    __/  |    
 _____/  _| |_| \__,_|  .__/  \___|     _|  _| \__,_| _|\_\ \___| _|    
                       _|                                               

--------------------------------------------------------------------------------------------------
'''    
    usage = 'usage: %prog [options]'
    parser = optparse.OptionParser(usage)

    parser.add_option('--treeName'       , dest='treeName'       , help='Name of the tree'                           , default='latino')
    parser.add_option('--tag'            , dest='tag'            , help='Tag used for the shape file name'           , default=None)
    parser.add_option('--sigset'         , dest='sigset'         , help='Signal samples [SM]'                        , default='SM')
    parser.add_option('--outputDir'      , dest='outputDir'      , help='output directory'                           , default='./')
    parser.add_option('--inputDir'       , dest='inputDir'       , help='input directory'                            , default='./data/')
    parser.add_option('--nuisancesFile'  , dest='nuisancesFile'  , help='file with nuisances configurations'         , default=None)
    parser.add_option('--doBatch'        , dest='doBatch'        , help='Run on batch'                               , default=False)
    parser.add_option('--batchQueue'     , dest='batchQueue'     , help='Queue on batch'                             , default='')
    parser.add_option('--batchSplit'     , dest="batchSplit"     , help="Splitting mode for batch jobs"              , default=[], type='string' , action='callback' , callback=list_maker('batchSplit',','))
    parser.add_option('--doHadd'         , dest='doHadd'         , help='Hadd for batch mode'                        , default=False)
    parser.add_option('--redoStat'       , dest='redoStat'        , help='redo stat uncertainty'                        , default=False)
    parser.add_option('--doThreads'      , dest='doThreads'      , help='switch to multi-threading mode'             , default=False)
    parser.add_option('--nThreads'       , dest='numThreads'     , help='number of threads for multi-threading'      , default=os.sysconf('SC_NPROCESSORS_ONLN'))
    parser.add_option('--doNotCleanup'   , dest='doNotCleanup'   , help='do not remove additional support files'     , action='store_true', default=False)
    parser.add_option("-W" , "--iihe-wall-time" , dest="IiheWallTime" , help="Requested IIHE queue Wall Time" , default='168:00:00')
          
    # read default parsing options as well
    hwwtools.addOptions(parser)
    hwwtools.loadOptDefaults(parser)
    (opt, args) = parser.parse_args()

    sys.argv.append( '-b' )
    ROOT.gROOT.SetBatch()


    print " configuration file = ", opt.pycfg
    print " treeName           = ", opt.treeName   
    print " lumi =               ", opt.lumi
    
    print " inputDir =           ", opt.inputDir
    print " outputDir =          ", opt.outputDir
 
    print "batchSplit: ",opt.batchSplit
    
    #TFormula.SetMaxima(1000000,10000,10000000)

    if not opt.debug:
        pass
    elif opt.debug == 2:
        print 'Logging level set to DEBUG (%d)' % opt.debug
        logging.basicConfig( level=logging.DEBUG )
    elif opt.debug == 1:
        print 'Logging level set to INFO (%d)' % opt.debug
        logging.basicConfig( level=logging.INFO )


    variables = {}
    print opt.variablesFile
    if os.path.exists(opt.variablesFile) :
      handle = open(opt.variablesFile,'r')
      exec(handle)
      handle.close()
      #in case some variables need a compiled function
      for variableName, variable in variables.iteritems():
          if variable.has_key('linesToAdd'):
            linesToAdd = variable['linesToAdd']
            for line in linesToAdd:
              ROOT.gROOT.ProcessLineSync(line)
    
    samples = {}
    if os.path.exists(opt.samplesFile) :
      handle = open(opt.samplesFile,'r')
      exec(handle)
      handle.close()
      #in case some samples need a compiled function
      for sampleName, sample in samples.iteritems():
          if sample.has_key('linesToAdd'):
            linesToAdd = sample['linesToAdd']
            for line in linesToAdd:
              ROOT.gROOT.ProcessLineSync(line)
   
    supercut = '1'
    cuts = {}
    if os.path.exists(opt.cutsFile) :
      handle = open(opt.cutsFile,'r')
      exec(handle)
      handle.close()

    nuisances = {}
    if opt.nuisancesFile == None :
      print " Please provide the nuisances structure if you want to add nuisances "      
    elif os.path.exists(opt.nuisancesFile) :
        handle = open(opt.nuisancesFile,'r')
        exec(handle)
        handle.close()
         

    batchSplit='' # This is needed to be defined here to be used at opt.doHadd case too
    if   opt.doBatch != 0:
            print "~~~~~~~~~~~ Running mkShape on Batch Queue"

            # Create Jobs Dictionary
            
            #batchSplit=''
 
            # ... Cuts
            stepList=[]
            if 'Cuts' in opt.batchSplit or "AsMuchAsPossible" in opt.batchSplit:
              batchSplit='Steps'   
              for iCut in cuts: stepList.append(iCut)
            else:
              stepList=['ALL']  
          
            # ... Samples
            targetList=[]
            if 'Samples' in opt.batchSplit :
              if 'Cuts' in opt.batchSplit : batchSplit+=','
              batchSplit+='Targets'
              for iSample in samples : targetList.append(iSample)
            elif 'AsMuchAsPossible' in opt.batchSplit :
              batchSplit+=',Targets'
              for sam_k,sam_v in samples.iteritems():
                filenumber=0
                #handle the case in which the configuration specifies how many files per job to run
                if "FilesPerJob" in sam_v.keys() and sam_v["FilesPerJob"] > 0:
                  filesPerJob = sam_v["FilesPerJob"]
                  fileListPerJob=[]
                  iCurJob=0
                  for filenumber, filename in enumerate(sam_v['name']) :
                    fileListPerJob.append(filename)
                    if (len(fileListPerJob) == filesPerJob) or filenumber==len(sam_v['name'])-1:
                      targetList.append(sam_k+str(iCurJob))
                      iCurJob+=1
                      fileListPerJob=[]
                      
                else:
                  targetList.append(sam_k)
            else:  
              targetList=['ALL']

            # ...Check job status and remove duplicates
	    print "stepList", stepList
	    print "targetList", targetList
            for iStep in stepList:
              for iTarget in targetList:
                pidFile = jobDir+'mkShapes__'+opt.tag+'/mkShapes__'+opt.tag+'__'+iStep+'__'+iTarget+'.jid'
                #print pidFile
                if os.path.isfile(pidFile) :
                  print '--> Job Running already : '+iStep+'__'+iTarget
                  exit()  
            
            bpostFix='' 
            jobs = batchJobs('mkShapes',opt.tag,stepList,targetList,batchSplit,bpostFix,True)            

            jobs.AddPy2Sh()
            jobs.InitPy("from LatinoAnalysis.ShapeAnalysis.ShapeFactory import ShapeFactory\n")
            jobs.InitPy("factory = ShapeFactory()")
            jobs.InitPy("factory._treeName  = '"+opt.treeName+"'")
            jobs.InitPy("factory._energy    = '"+str(opt.energy)+"'")
            jobs.InitPy("factory._lumi      = "+str(opt.lumi))
            jobs.InitPy("factory._tag       = '"+str(opt.tag)+"'")
            jobs.InitPy("\n")

            outputDir=os.getcwd()+'/'+opt.outputDir 

            if "AsMuchAsPossible" in opt.batchSplit:
              iStep='ALL'
              iTarget='ALL'
              for cut_k,cut_v in cuts.iteritems():
                cuts_new = {}
                cuts_new[cut_k] = cut_v
                for sam_k,sam_v in samples.iteritems():
                  thisSampleWeights=[]
                  if 'weights' in sam_v.keys():
                    thisSampleWeights=copy.deepcopy(sam_v['weights'])

                  if "FilesPerJob" in sam_v.keys() and sam_v["FilesPerJob"] > 0:
                    filesPerJob = sam_v["FilesPerJob"]
                    fileListPerJob=[]
                    weightListPerJob=[]
                    iCurJob = 0  
                    for filenumber, filename in enumerate(sam_v['name']) :
                      fileListPerJob.append(filename)
                      if len(thisSampleWeights) != 0:
                        weightListPerJob.append(thisSampleWeights[filenumber])
                      if (len(fileListPerJob) == filesPerJob) or filenumber==len(sam_v['name'])-1:
                        samples_new = {}
                        samples_new[sam_k] = copy.deepcopy(sam_v)
                        samples_new[sam_k]['name'] = fileListPerJob 
                        if len(thisSampleWeights) != 0:
                          samples_new[sam_k]['weights'] = weightListPerJob
                        iStep=cut_k
                        iTarget = sam_k+str(iCurJob)
                        jName = iStep + '_' + iTarget
                        instructions_for_configuration_file  = ""
                        instructions_for_configuration_file += "factory.makeNominals(   \n"
                        instructions_for_configuration_file += "     '" + opt.inputDir +"',    \n"
                        instructions_for_configuration_file += "     '" + outputDir + "',     \n"
                        instructions_for_configuration_file += "      " + str(variables) + ", \n"
                        instructions_for_configuration_file += "      " + str(cuts_new) + ",      \n"
                        instructions_for_configuration_file += "      " + str(samples_new) + ",   \n"
                        instructions_for_configuration_file += "      " + str(nuisances) + ", \n"
                        instructions_for_configuration_file += "     '" + supercut + "',      \n"
                        instructions_for_configuration_file += "     '" + jName + "')    \n"
                        jobs.AddPy (iStep, iTarget, instructions_for_configuration_file) 
                        fileListPerJob=[]
                        weightListPerJob=[]
                        iCurJob = iCurJob+1
                  else:
                    samples_new = {}
                    samples_new[sam_k] = sam_v
                    iStep=cut_k
                    iTarget = sam_k
                    jName = iStep + '_' + iTarget
                    instructions_for_configuration_file  = ""
                    instructions_for_configuration_file += "factory.makeNominals(   \n"
                    instructions_for_configuration_file += "     '" + opt.inputDir +"',    \n"
                    instructions_for_configuration_file += "     '" + outputDir + "',     \n"
                    instructions_for_configuration_file += "      " + str(variables) + ", \n"
                    instructions_for_configuration_file += "      " + str(cuts_new) + ",      \n"
                    instructions_for_configuration_file += "      " + str(samples_new) + ",   \n"
                    instructions_for_configuration_file += "      " + str(nuisances) + ", \n"
                    instructions_for_configuration_file += "     '" + supercut + "',      \n"
                    instructions_for_configuration_file += "     '" + jName + "')    \n"
                    jobs.AddPy (iStep, iTarget, instructions_for_configuration_file) 


            elif 'Cuts' in opt.batchSplit and 'Samples' in opt.batchSplit:
              iStep='ALL'
              iTarget='ALL'
              for cut_k,cut_v in cuts.iteritems():
                cuts_new = {}
                cuts_new[cut_k] = cut_v
                for sam_k,sam_v in samples.iteritems():
                  samples_new = {}
                  samples_new[sam_k] = sam_v

                  iStep=cut_k  
                
                  iTarget = sam_k
                
                  jName = iStep + '_' + iTarget

                  instructions_for_configuration_file  = ""
                  instructions_for_configuration_file += "factory.makeNominals(   \n"
                  instructions_for_configuration_file += "     '" + opt.inputDir +"',    \n"
                  instructions_for_configuration_file += "     '" + outputDir + "',     \n"
                  instructions_for_configuration_file += "      " + str(variables) + ", \n"
                  instructions_for_configuration_file += "      " + str(cuts_new) + ",      \n"
                  instructions_for_configuration_file += "      " + str(samples_new) + ",   \n"
                  instructions_for_configuration_file += "      " + str(nuisances) + ", \n"
                  instructions_for_configuration_file += "     '" + supercut + "',      \n"
                  instructions_for_configuration_file += "     '" + jName + "')    \n"

                  #jobs.AddPy(iStep,iTarget,"factory.makeNominals('"+opt.inputDir+"','"+outputDir+"',"+str(variables)+","+str(cuts_new)+","+str(samples_new)+","+str(nuisances)+",'"+supercut+"','"+jName+"')\n"    )
                  jobs.AddPy (iStep, iTarget, instructions_for_configuration_file)

            elif 'Cuts' in opt.batchSplit and not 'Samples' in opt.batchSplit:
              iStep='ALL'
              iTarget='ALL'
              for cut_k,cut_v in cuts.iteritems():
                cuts_new = {}
                cuts_new[cut_k] = cut_v

                iStep=cut_k  
                
                jName = iStep + '_' + iTarget

                instructions_for_configuration_file  = ""
                instructions_for_configuration_file += "factory.makeNominals(   \n"
                instructions_for_configuration_file += "     '" + opt.inputDir +"',    \n"
                instructions_for_configuration_file += "     '" + outputDir + "',     \n"
                instructions_for_configuration_file += "      " + str(variables) + ", \n"
                instructions_for_configuration_file += "      " + str(cuts_new) + ",      \n"
                instructions_for_configuration_file += "      " + str(samples) + ",   \n"
                instructions_for_configuration_file += "      " + str(nuisances) + ", \n"
                instructions_for_configuration_file += "     '" + supercut + "',      \n"
                instructions_for_configuration_file += "     '" + jName + "')    \n"

                jobs.AddPy (iStep, iTarget, instructions_for_configuration_file)
            elif not 'Cuts' in opt.batchSplit and 'Samples' in opt.batchSplit:
              iStep='ALL'
              iTarget='ALL'
              for sam_k,sam_v in samples.iteritems():
                samples_new = {}
                samples_new[sam_k] = sam_v

                iTarget = sam_k
                
                jName = iStep + '_' + iTarget

                instructions_for_configuration_file  = ""
                instructions_for_configuration_file += "factory.makeNominals(   \n"
                instructions_for_configuration_file += "     '" + opt.inputDir +"',    \n"
                instructions_for_configuration_file += "     '" + outputDir + "',     \n"
                instructions_for_configuration_file += "      " + str(variables) + ", \n"
                instructions_for_configuration_file += "      " + str(cuts) + ",      \n"
                instructions_for_configuration_file += "      " + str(samples_new) + ",   \n"
                instructions_for_configuration_file += "      " + str(nuisances) + ", \n"
                instructions_for_configuration_file += "     '" + supercut + "',      \n"
                instructions_for_configuration_file += "     '" + jName + "')    \n"

                jobs.AddPy (iStep, iTarget, instructions_for_configuration_file)
	    else :
              iStep='ALL'
              iTarget='ALL'
                
              jName = iStep + '_' + iTarget

              instructions_for_configuration_file  = ""
              instructions_for_configuration_file += "factory.makeNominals(   \n"
              instructions_for_configuration_file += "     '" + opt.inputDir +"',    \n"
              instructions_for_configuration_file += "     '" + outputDir + "',     \n"
              instructions_for_configuration_file += "      " + str(variables) + ", \n"
              instructions_for_configuration_file += "      " + str(cuts) + ",      \n"
              instructions_for_configuration_file += "      " + str(samples) + ",   \n"
              instructions_for_configuration_file += "      " + str(nuisances) + ", \n"
              instructions_for_configuration_file += "     '" + supercut + "',      \n"
              instructions_for_configuration_file += "     '" + jName + "')    \n"

              jobs.AddPy (iStep, iTarget, instructions_for_configuration_file)
                    
            #if 'knu' in os.uname()[1]:
              #jobs.Sub(opt.batchQueue)
            #else:
            #print " opt.batchQueue = ", opt.batchQueue
            jobs.Sub(opt.batchQueue,opt.IiheWallTime,True)


    elif opt.doHadd != 0 :
      
            print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
            print "~~~~~~~~~~~ mkShape on Batch : Hadd"
            print "     -> jobDir = ", jobDir
            print "     -> files  = ", jobDir+'mkShapes__'+opt.tag+'/mkShapes__'+opt.tag+'__'+'XXX'+'__'+'YYY'+'.jid'


            # ... Cuts
            stepList=[]
            if 'Cuts' in opt.batchSplit or "AsMuchAsPossible" in opt.batchSplit:
              batchSplit='Steps'
              for iCut in cuts: stepList.append(iCut)
            else:
              stepList=['ALL']

            # ... Samples
            targetList=[]
            if 'Samples' in opt.batchSplit :
              if 'Cuts' in opt.batchSplit : batchSplit+=','
              batchSplit+='Targets'
              for iSample in samples : targetList.append(iSample)
            elif 'AsMuchAsPossible' in opt.batchSplit :
              batchSplit+=',Targets'
              for sam_k,sam_v in samples.iteritems():
                filenumber=0
                #handle the case in which the configuration specifies how many files per job to run
                if "FilesPerJob" in sam_v.keys() and sam_v["FilesPerJob"] > 0:
                  filesPerJob = sam_v["FilesPerJob"]
                  fileListPerJob=[]
                  iCurJob=0
                  for filenumber, filename in enumerate(sam_v['name']) :
                    fileListPerJob.append(filename)
                    if (len(fileListPerJob) == filesPerJob) or filenumber==len(sam_v['name'])-1:
                      targetList.append(sam_k+str(iCurJob))
                      iCurJob+=1
                      fileListPerJob=[]

                else:
                  targetList.append(sam_k)
            else:
              targetList=['ALL'] 

            # ...Check job status and create command
            outputFile=os.getcwd()+'/'+opt.outputDir+'/plots_'+opt.tag+'.root'
            fileList = [] 
#            command = 'cd '+os.getcwd()+'/'+opt.outputDir+'; hadd -f '+outputFile
            cleanup = 'cd '+os.getcwd()+'/'+opt.outputDir+'; '
            allDone=True
            for iStep in stepList:
              for iTarget in targetList:
                pidFile = jobDir+'mkShapes__'+opt.tag+'/mkShapes__'+opt.tag+'__'+iStep+'__'+iTarget+'.jid'
                if os.path.isfile(pidFile) :
                  print '--> Job Running Still: '+iStep+'__'+iTarget
                  allDone=False
                iFile='plots_'+opt.tag+'_'+iStep+'_'+iTarget+'.root' 
                if not os.path.isfile(os.getcwd()+'/'+opt.outputDir+'/'+iFile) :
                  print '--> Missing root file: '+iFile 
                  allDone=False
                fileList.append(iFile)
#                command+=' '+iFile
#                cleanup+='rm '+iFile+' ; '
            if allDone:
              number = len(fileList)
              if number > 500:
                print "WARNING: you are trying to hadd more than 500 files. hadd will proceed by steps of 500 files (otherwise it may silently fail)."
              for istart in range(0,int(float(number)/500+1)):
                  command = 'cd '+os.getcwd()+'/'+opt.outputDir+'; '
                  command += 'hadd -f plots_'+opt.tag+'_temp'+str(istart)+'.root'
                  for i in range(istart*500,(istart+1)*500):
                    if i>=number: break
                    command += " "+fileList[i]
                    cleanup += "rm "+fileList[i]+" ; "
#                  print command
                  os.system(command)
              os.chdir(os.getcwd()+"/"+opt.outputDir)
              os.system("hadd -f plots_"+opt.tag+".root plots_"+opt.tag+"_temp*")
              cleanup += "rm plots_"+opt.tag+"_temp*"
              if not opt.doNotCleanup: os.system(cleanup) 
    elif opt.doHadd != 0 or opt.redoStat != 0:       
            ## Fix the MC stat nuisances that are not treated correctly in case of AsMuchAsPossible option 
            if ('AsMuchAsPossible' in opt.batchSplit and opt.doHadd != 0) or opt.redoStat != 0:
              ## do this only if we want to add the MC stat nuisances in the old way
              if 'stat' in nuisances.keys()  and  not nuisances['stat']['samples']=={} :
                os.chdir(os.getcwd()+"/"+opt.outputDir)
                filein=ROOT.TFile('plots_'+opt.tag+'.root', 'update')
                for sample in samples.keys():
                  if sample == "DATA":
                    continue
                  zeroMCerror = 0
                  if sample in nuisances['stat']['samples'].keys():
                    if 'zeroMCError' in nuisances['stat']['samples'][sample].keys():
                      if nuisances['stat']['samples'][sample]['zeroMCError'] == '1':
                        zeroMCerror = 1
                    if zeroMCerror == 1:
                      print "special treatment of 0 MC events active for sample", sample
                    for cut in cuts.keys():
                      for variable in variables.keys():
                        hcentral = filein.Get(cut+"/"+variable+"/histo_"+sample)
                        if hcentral == None:
                          print "Warning, missing", sample, cut, variable
                          continue
                        else:
                          print "Found", sample, cut, variable
                        for ibin in range(1, hcentral.GetNbinsX()+1):
                          filein.cd(cut+"/"+variable)
                          tag = "_ibin_"
                          print nuisances['stat']['samples'][sample]
                          if 'correlate' in nuisances['stat']['samples'][sample].keys():
                            #specify the sample that is source of the variation
                            tag = "_ibin"+sample+"_"
                          hup = filein.Get(cut+"/"+variable+"/histo_"+sample+tag + str(ibin) + "_statUp")
                          hdo = filein.Get(cut+"/"+variable+"/histo_"+sample+tag + str(ibin) + "_statDown")
                          if hup == None:
                            print "Adding previously missing", hcentral.GetName()+ tag + str(ibin) + "_statUp"
                            hup = hcentral.Clone(hcentral.GetName()+ tag + str(ibin) + "_statUp")
                          if hdo ==None:
                            print "Adding previously missing", hcentral.GetName()+ tag + str(ibin) + "_statDown"
                            hdo = hcentral.Clone(hcentral.GetName()+ tag + str(ibin) + "_statDown")
                          if 'correlate' in nuisances['stat']['samples'][sample].keys():
                            othersup = {}
                            othersdo = {}
                            othersce = {}
                            for other in nuisances['stat']['samples'][sample]['correlate']:  
                              hupother = filein.Get(cut+"/"+variable+"/histo_"+other+tag + str(ibin) + "_statUp")
                              hdoother = filein.Get(cut+"/"+variable+"/histo_"+other+tag + str(ibin) + "_statDown")
                              hcentralother = filein.Get(cut+"/"+variable+"/histo_"+other)
                              if hupother == None:
                                hupother = hcentralother.Clone(hcentralother.GetName()+ tag + str(ibin) + "_statUp")
                              if hdoother == None:
                                hdoother = hcentralother.Clone(hcentralother.GetName()+ tag + str(ibin) + "_statDown") 
                              othersup[other] = hupother
                              othersdo[other] = hdoother
                              othersce[other] = hcentralother    
                          scaleHistoStat(hcentral, hup,  1, ibin, opt.lumi, zeroMCerror)
                          scaleHistoStat(hcentral, hdo, -1, ibin, opt.lumi, zeroMCerror)
                          hcentral.SetBinError(ibin, 0)
                          if 'correlate' in nuisances['stat']['samples'][sample].keys():
                            for other in nuisances['stat']['samples'][sample]['correlate']:
                              othersup[other].SetBinContent(ibin, max(0, othersce[other].GetBinContent(ibin)+hup.GetBinContent(ibin)-hcentral.GetBinContent(ibin)))
                              othersdo[other].SetBinContent(ibin, max(0, othersce[other].GetBinContent(ibin)+hdo.GetBinContent(ibin)-hcentral.GetBinContent(ibin)))
                              othersce[other].SetBinError(ibin,0)
                          #BUGFIX by Andrea: hcentral is now the firt variable in the function
                          #original text: scaleHistoStat(hup,  1, ibin, lumi, zeroMCerror)
                          hcentral.Write("",ROOT.TObject.kOverwrite)
                          print "Saviing histogram ", cut+"/"+variable+"/histo_"+sample+tag + str(ibin) + "_statUp"
                          hup.Write("",ROOT.TObject.kOverwrite)
                          print "Saving histogram ", cut+"/"+variable+"/histo_"+sample+tag + str(ibin) + "_statDown"
                          hdo.Write("",ROOT.TObject.kOverwrite)
                          if 'correlate' in nuisances['stat']['samples'][sample].keys():
                            for other in nuisances['stat']['samples'][sample]['correlate']:  
                              print "Also saving correlated variation", cut+"/"+variable+"/histo_"+other+tag + str(ibin) + "_statUp"  
                              othersup[other].Write("",ROOT.TObject.kOverwrite)
                              print "Also saving correlated variation", cut+"/"+variable+"/histo_"+other+tag + str(ibin) + "_statDown"
                              othersdo[other].Write("",ROOT.TObject.kOverwrite)
                              othersce[other].Write("",ROOT.TObject.kOverwrite)
                          

              print "All done!"
#              os.system(command)
#              if not opt.doNotCleanup: os.system(cleanup)
#              os.system('cd ..')
 
    elif opt.doThreads != 0:

            print "~~~~~~~~~~~ Running mkShape in multi-threading mode..."

            command = ""
            command += "rm -r log\n"
            command += "mkdir log"
            os.system(command)


            os.system(command)
 
            numThreads = int(opt.numThreads)
            print "number of threads = ", numThreads

	    queue = Queue.Queue()
             
	    for i in range(numThreads):
              proc = Worker(queue)
              proc.daemon = True
              proc.start()

            number = 0

            for cut_k,cut_v in cuts.iteritems():

              cuts_new = {}
              cuts_new[cut_k] = cut_v

              for sam_k,sam_v in samples.iteritems():
                thisSampleWeights=[]
                if 'weights' in sam_v.keys():
                  thisSampleWeights=copy.deepcopy(sam_v['weights'])
                if "FilesPerJob" in sam_v.keys() and sam_v["FilesPerJob"] > 0:
                  filesPerJob = sam_v["FilesPerJob"]
                  fileListPerJob=[]
                  weightListPerJob=[]
                  iCurJob = 0
                  for filenumber, filename in enumerate(sam_v['name']) :
                    fileListPerJob.append(filename)
                    if len(thisSampleWeights) != 0:
                      weightListPerJob.append(thisSampleWeights[filenumber])
                    if (len(fileListPerJob) == filesPerJob) or filenumber==len(sam_v['name'])-1:
                      samples_new = {}
                      samples_new[sam_k] = copy.deepcopy(sam_v)
                      samples_new[sam_k]['name'] = fileListPerJob
                      if len(thisSampleWeights) != 0:
                        samples_new[sam_k]['weights'] = weightListPerJob   
                      queue.put( [opt.inputDir ,opt.outputDir, variables, cuts_new, samples_new, nuisances, supercut, number, opt.energy, opt.lumi, opt.tag] )
                      number += 1
                      fileListPerJob=[]
                      weightListPerJob=[]
                else:
                  samples_new = {}
                  samples_new[sam_k] = copy.deepcopy(sam_v)
                  queue.put( [opt.inputDir ,opt.outputDir, variables, cuts_new, samples_new, nuisances, supercut, number, opt.energy, opt.lumi, opt.tag] )
                  number += 1
            queue.join()

            command = ""
            command += "rm "+opt.outputDir+'/plots_'+opt.tag+".root"
            print command
            os.system(command)

            if number<1000:
              command = ""
              command += "hadd "+opt.outputDir+'/plots_'+opt.tag+".root"
              for i in xrange(number):
                command += " "+opt.outputDir+'/plots_'+opt.tag+"_"+str(i)+".root"
              print command
              os.system(command)
            else:
              print "WARNING: you are trying to hadd more than 1000 files. hadd will proceed by steps of 500 files (otherwise it may silently fail)."
              for istart in range(0,int(float(number)/500+1)):
                command = ""
                command += "hadd "+opt.outputDir+"/plots_"+opt.tag+"_temp"+str(istart)+".root"
                for i in range(istart*500,(istart+1)*500):
                  if i>=number: break
                  command += " "+opt.outputDir+"/plots_"+opt.tag+"_"+str(i)+".root"
                print command
                os.system(command)
              os.system("hadd "+opt.outputDir+'/plots_'+opt.tag+".root "+opt.outputDir+"/plots_"+opt.tag+"_temp*")


            if not opt.doNotCleanup:
              os.system("rm "+opt.outputDir+'/plots_'+opt.tag+"_temp*.root")
              for i in xrange(number):
                os.system("rm sub"+str(i)+".py")
                os.system("rm "+opt.outputDir+'/plots_'+opt.tag+"_"+str(i)+".root")
            
      
    else:
      print "~~~~~~~~~~~ Running mkShape in normal mode..."
      factory = ShapeFactory()
      factory._treeName  = opt.treeName
      factory._energy    = opt.energy
      factory._lumi      = opt.lumi
      factory._tag       = opt.tag
 
      factory.makeNominals( opt.inputDir ,opt.outputDir, variables, cuts, samples, nuisances, supercut)
