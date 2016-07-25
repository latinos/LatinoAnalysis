#!/usr/bin/env python

import json
import sys
import ROOT
import optparse
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

        infile += "factory.makeNominals('"+inputDir+"','"+outputDir+"',"+str(variables)+","+str(cuts)+","+str(samples)+","+str(nuisances)+",'"+supercut+"',"+str(number)+")\n"
        sub_file = open("sub"+str(number)+".py","w")
        sub_file.write(infile)
        sub_file.close()

        print 'task initiated --> '+str(cuts.keys())+' , '+str(samples.keys())

        logfile = open("log/log" + str(number) + "_" + str(cuts.keys()[0]) + "_" + str(samples.keys()[0]) + ".txt","w")
        command = "python "+sub_file.name
        process = subprocess.Popen(command, shell=True, stdout=logfile, stderr=logfile)
        process.wait()
        self.status = process.returncode
        print 'task finished with exit code '+str(self.status)+'   [0 is good] --> '+str(cuts.keys())+' , '+str(samples.keys())
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
    parser.add_option('--doThreads'      , dest='doThreads'      , help='switch to multi-threading mode'             , default=False)
    parser.add_option('--nThreads'       , dest='numThreads'     , help='number of threads for multi-threading'      , default=os.sysconf('SC_NPROCESSORS_ONLN'))
    parser.add_option('--doClean'        , dest='doCleanup'      , help='remove additional support files'            , default=True)
          
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
         

    if opt.doThreads != 0:

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
                samples_new = {}
                samples_new[sam_k] = sam_v

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


            if opt.doCleanup=="True" :
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
