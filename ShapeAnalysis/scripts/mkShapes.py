#!/usr/bin/env python

import json
import sys
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
from LatinoAnalysis.Tools.userConfig  import *
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
        print 'task finished with exit code '+str(self.status)+'   [0 is good] --> '+str(cuts.keys())+' , '+str(samples.keys())+' , '+str(samples[theKey]['name'])
        self.queue.task_done()
      except Queue.Empty, e:
        break
      except Exception, e:
        print "Error: %s" % str(e)


if __name__ == '__main__':
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

    parser.add_option('--tag'            , dest='tag'            , help='Tag used for the shape file name'           , default=None)
    parser.add_option('--sigset'         , dest='sigset'         , help='Signal samples [SM]'                        , default='SM')
    parser.add_option('--outputDir'      , dest='outputDir'      , help='output directory'                           , default='./')
    parser.add_option('--inputDir'       , dest='inputDir'       , help='input directory'                            , default='./data/')
    parser.add_option('--nuisancesFile'  , dest='nuisancesFile'  , help='file with nuisances configurations'         , default=None)
    parser.add_option('--doBatch'        , dest='doBatch'        , help='Run on batch'                               , default=False)
    parser.add_option('--batchQueue'     , dest='batchQueue'     , help='Queue on batch'                             , default='')
    parser.add_option('--batchSplit'     , dest="batchSplit"     , help="Splitting mode for batch jobs"              , default=[], type='string' , action='callback' , callback=list_maker('batchSplit',','))
    parser.add_option('--doHadd'         , dest='doHadd'         , help='Hadd for batch mode'                        , default=False)
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
    if os.path.exists(opt.variablesFile) :
      handle = open(opt.variablesFile,'r')
      exec(handle)
      handle.close()
    
    supercut = '1'
    cuts = {}
    if os.path.exists(opt.cutsFile) :
      handle = open(opt.cutsFile,'r')
      exec(handle)
      handle.close()
    
    samples = {}
    if os.path.exists(opt.samplesFile) :
      handle = open(opt.samplesFile,'r')
      exec(handle)
      handle.close()
    
    nuisances = {}
    if opt.nuisancesFile == None :
      print " Please provide the nuisances structure if you want to add nuisances "      
    elif os.path.exists(opt.nuisancesFile) :
        handle = open(opt.nuisancesFile,'r')
        exec(handle)
        handle.close()
         

    if   opt.doBatch != 0:
            print "~~~~~~~~~~~ Running mkShape on Batch Queue"

            # Create Jobs Dictionary
            
            batchSplit=''
 
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
            jobs.Sub(opt.batchQueue,opt.IiheWallTime)


    elif opt.doHadd != 0:
            print "~~~~~~~~~~~ mkShape on Batch : Hadd"

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
            cleanup = 'cd '+os.getcwd()+'/'+opt.outputDir+'; rm '
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
                  command += 'hadd -f temp'+str(istart)+'.root'
                  for i in range(istart*500,(istart+1)*500):
                    if i>=number: break
                    command += " "+fileList[i]
                    cleanup += " "+fileList[i]
#                  print command
                  os.system(command)
              os.system("cd "+os.getcwd()+"/"+opt.outputDir+"; "+"hadd -f plots_"+opt.tag+".root temp*")
#              print "cd "+os.getcwd()+"/"+opt.outputDir+"; "+"hadd plots_"+opt.tag+".root temp*"
              cleanup += " temp*"
              if not opt.doNotCleanup: os.system(cleanup) 



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
      factory._energy    = opt.energy
      factory._lumi      = opt.lumi
      factory._tag       = opt.tag
 
      factory.makeNominals( opt.inputDir ,opt.outputDir, variables, cuts, samples, nuisances, supercut)
