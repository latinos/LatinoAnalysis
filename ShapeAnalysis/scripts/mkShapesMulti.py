#!/usr/bin/env python

import sys
# bypass ROOT argv parsing
argv = sys.argv
sys.argv = argv[:1]
import ROOT
import optparse
import copy
import collections
import LatinoAnalysis.Gardener.hwwtools as hwwtools
import os.path
import math
import logging
import tempfile
import subprocess
import threading, Queue
from LatinoAnalysis.ShapeAnalysis.ShapeFactoryMulti import ShapeFactory

# Common Tools & batch
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
        aliases = params[11]

        infile = ""
        infile += "from collections import OrderedDict\n"
        infile += "from LatinoAnalysis.ShapeAnalysis.ShapeFactoryMulti import ShapeFactory\n\n"
        infile += "factory = ShapeFactory()\n"
        infile += "factory._treeName  = '"+opt.treeName+"'\n"
        infile += "factory._energy    = '"+str(energy)+"'\n"
        infile += "factory._lumi      = "+str(lumi)+"\n"
        infile += "factory._tag       = '"+str(tag)+"'\n"
        infile += "factory._nThreads  = 1\n"
        infile += "factory.aliases    = "+aliases+"\n"

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

def makeTargetList(options, samples):
  """
  Return a list of draw targets or merge sources. Entry of the list can be a sample name string,
  a 2-tuple (sample name, fileblock), or a 3-tuple (sample name, fileblock, eventblock).
  """

  targetList=[]

  splitBySample = 'Samples' in options or 'AsMuchAsPossible' in options
  splitByFile = 'Files' in options or 'AsMuchAsPossible' in options
  splitByEvent = 'Events' in options or 'AsMuchAsPossible' in options

  if splitBySample:
    for sam_k, sam_v in samples.iteritems():

      if splitByFile and "FilesPerJob" in sam_v and sam_v["FilesPerJob"] > 0:
        filesPerJob = sam_v["FilesPerJob"]
        nFiles = len(sam_v['name'])
        nFileBlocks = int(math.ceil(float(nFiles) / filesPerJob))

        if splitByEvent and 'EventsPerJob' in sam_v and sam_v['EventsPerJob'] > 0:
          eventsPerJob = sam_v['EventsPerJob']

          for iFileBlock in range(nFileBlocks):
            treeType = os.path.basename(sam_v['name'][0]).split('_')[0]
            if treeType == 'latino':
              chain = ROOT.TChain('latino')
            elif treeType == 'nanoLatino':
              chain = ROOT.TChain('Events')
              
            for fname in sam_v['name'][iFileBlock * filesPerJob:(iFileBlock + 1) * filesPerJob]:
              chain.Add(fname)
            nEvents = chain.GetEntries()
            nEventBlocks = int(math.ceil(float(nEvents) / eventsPerJob))

            if nEventBlocks == 1:
              if nFileBlocks == 1:
                targetList.append(sam_k)
              else:
                targetList.append((sam_k, iFileBlock))
            else:
              targetList.extend((sam_k, iFileBlock, iEventBlock) for iEventBlock in range(nEventBlocks))

        else:
          if nFileBlocks == 1:
            targetList.append(sam_k)
          else:
            targetList.extend((sam_k, iFileBlock) for iFileBlock in range(nFileBlocks))

      else:
        targetList.append(sam_k)

  else:
    targetList=['ALL']

  return targetList


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
    parser.add_option('--nThreads'       , dest='numThreads'     , help='number of threads for multi-threading'      , default=1, type='int')
    parser.add_option('--doNotCleanup'   , dest='doNotCleanup'   , help='do not remove additional support files'     , action='store_true', default=False)
    parser.add_option("-n", "--dry-run"  , dest="dryRun"         , help="do not make shapes"                         , default=False, action="store_true")
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

    # MultiDraw should be loaded by importing ShapeFactoryMulti
    try:
      ROOT.multidraw.MultiDraw
    except:
      raise RuntimeError('Failed to load libMultiDraw')

    samples = collections.OrderedDict()
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

    aliases = collections.OrderedDict()
    if opt.aliasesFile and os.path.exists(opt.aliasesFile):
      handle = open(opt.aliasesFile,'r')
      exec(handle)
      handle.close()

    #in case some aliases need a compiled function 
    for aliasName, alias in aliases.iteritems():
      if alias.has_key('linesToAdd'):
        linesToAdd = alias['linesToAdd']
        for line in linesToAdd:
          ROOT.gROOT.ProcessLineSync(line)

    supercut = '1'
    cuts = collections.OrderedDict()
    if os.path.exists(opt.cutsFile) :
      handle = open(opt.cutsFile,'r')
      exec(handle)
      handle.close()

    variables = collections.OrderedDict()
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

    nuisances = collections.OrderedDict()
    if opt.nuisancesFile == None :
      print " Please provide the nuisances structure if you want to add nuisances "
    elif os.path.exists(opt.nuisancesFile) :
      handle = open(opt.nuisancesFile,'r')
      exec(handle)
      handle.close()

    for nuis in nuisances.itervalues():
      if 'samplespost' in nuis:
        nuis.pop('samplespost')
      if 'cutspost' in nuis:
        nuis.pop('cutspost')

    for vari in variables.itervalues():
      if 'cutspost' in vari:
        vari.pop('cutspost')

    if opt.doBatch != 0:
      print "~~~~~~~~~~~ Running mkShape on Batch Queue"

      # Create Jobs Dictionary

      batchSplit = []

      stepList=['ALL']

      targetList = makeTargetList(opt.batchSplit, samples)
      if targetList[0] != 'ALL':
        batchSplit.append('Targets')

      # ...Check job status and remove duplicates
      print "stepList", stepList
      print "targetList", targetList
      for iStep in stepList:
        for iTarget in targetList:
          if type(iTarget) is tuple:
            if len(iTarget) == 2:
              tname = '%s.%d' % iTarget
            else:
              tname = '%s.%d.%d' % iTarget
          else:
            tname = iTarget

          pidFile = jobDir+'mkShapes__'+opt.tag+'/mkShapes__'+opt.tag+'__'+iStep+'__'+tname+'.jid'
          #print pidFile
          if os.path.isfile(pidFile) :
            print '--> Job aready created : '+iStep+'__'+tname
            exit()

      nThreads = opt.numThreads

      bpostFix=''
      jobs = batchJobs('mkShapes',opt.tag,stepList,targetList,','.join(batchSplit),bpostFix,True)
      jobs.nThreads = nThreads

      jobs.AddPy2Sh()
      jobs.InitPy('from collections import OrderedDict')
      jobs.InitPy("from LatinoAnalysis.ShapeAnalysis.ShapeFactoryMulti import ShapeFactory\n")
      jobs.InitPy("factory = ShapeFactory()")
      jobs.InitPy("factory._treeName  = '"+opt.treeName+"'")
      jobs.InitPy("factory._energy    = '"+str(opt.energy)+"'")
      jobs.InitPy("factory._lumi      = "+str(opt.lumi))
      jobs.InitPy("factory._tag       = '"+str(opt.tag)+"'")
      jobs.InitPy("factory._nThreads  = "+str(nThreads))
      jobs.InitPy("factory.aliases    = "+str(aliases))

      jobs.InitPy("\n")

      outputDir=os.getcwd()+'/'+opt.outputDir

      for iStep in stepList:
        if iStep == 'ALL':
          job_cuts = cuts
        else:
          job_cuts = {iStep: cuts[iStep]}

        for iTarget in targetList:
          if iTarget == 'ALL':
            tname = iTarget
            job_targets = samples

          elif type(iTarget) is tuple:
            if len(iTarget) == 2:
              tname = '%s.%d' % iTarget
            else:
              tname = '%s.%d.%d' % iTarget

            sample = samples[iTarget[0]]
            iFileBlock = iTarget[1]
            filesPerJob = sample['FilesPerJob']

            clone = copy.deepcopy(sample)
            clone['name'] = sample['name'][filesPerJob * iFileBlock:filesPerJob * (iFileBlock + 1)]
            if 'weights' in sample:
              clone['weights'] = sample['weights'][filesPerJob * iFileBlock:filesPerJob * (iFileBlock + 1)]

            job_targets = {iTarget[0]: clone}

          else:
            tname = iTarget
            job_targets = {iTarget: samples[iTarget]}

          jName = iStep + '_' + tname

          instructions_for_configuration_file  = ""
          instructions_for_configuration_file += "factory.makeNominals(   \n"
          instructions_for_configuration_file += "     '" + opt.inputDir +"',    \n"
          instructions_for_configuration_file += "     '" + outputDir + "',     \n"
          instructions_for_configuration_file += "      " + str(variables) + ", \n"
          instructions_for_configuration_file += "      " + str(job_cuts) + ",      \n"
          instructions_for_configuration_file += "      " + str(job_targets) + ",   \n"
          instructions_for_configuration_file += "      " + str(nuisances) + ", \n"
          instructions_for_configuration_file += "     '" + supercut + "',      \n"
          instructions_for_configuration_file += "     '" + jName + "',\n"
          if type(iTarget) is tuple and len(iTarget) == 3:
            otherTargets = [t for t in targetList if t[:2] == iTarget[:2]]
            isLastEventBlock = (iTarget[2] == max(t[2] for t in otherTargets))

            eventsPerJob = sample['EventsPerJob']
            instructions_for_configuration_file += "     " + str(eventsPerJob * iTarget[2]) + ",\n"
            if isLastEventBlock:
              instructions_for_configuration_file += "     -1\n"
            else:
              instructions_for_configuration_file += "     " + str(eventsPerJob) + "\n"

          instructions_for_configuration_file += ")    \n"

          jobs.AddPy (iStep, iTarget, instructions_for_configuration_file)

      #if 'knu' in os.uname()[1]:
        #jobs.Sub(opt.batchQueue)
      #else:
      #print " opt.batchQueue = ", opt.batchQueue
      if not opt.dryRun:
        jobs.Sub(opt.batchQueue,opt.IiheWallTime,True)

    elif opt.doHadd != 0:

      print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
      print "~~~~~~~~~~~ mkShape on Batch : Hadd"
      print "     -> jobDir = ", jobDir
      print "     -> files  = ", jobDir+'mkShapes__'+opt.tag+'/mkShapes__'+opt.tag+'__'+'XXX'+'__'+'YYY'+'.jid'

      stepList=['ALL']

      targetList = makeTargetList(opt.batchSplit, samples)

      # ...Check job status and create command
      outputFile=os.getcwd()+'/'+opt.outputDir+'/plots_'+opt.tag+'.root'
      fileList = []
      cleanup = 'cd '+os.getcwd()+'/'+opt.outputDir+'; '
      allDone=True

      for iStep in stepList:
        for iTarget in targetList:
          if type(iTarget) is tuple:
            if len(iTarget) == 2:
              tname = '%s.%d' % iTarget
            else:
              tname = '%s.%d.%d' % iTarget
          else:
            tname = iTarget

          pidFile = jobDir+'mkShapes__'+opt.tag+'/mkShapes__'+opt.tag+'__'+iStep+'__'+tname+'.jid'
          if os.path.isfile(pidFile) :
            print '--> Job Running Still: '+iStep+'__'+tname
            allDone=False
          iFile='plots_'+opt.tag+'_'+iStep+'_'+tname+'.root'
          if not os.path.isfile(os.getcwd()+'/'+opt.outputDir+'/'+iFile) :
            print '--> Missing root file: '+iFile
            allDone=False
          fileList.append(iFile)

      if not allDone:
        sys.exit(1)

      nThreads = opt.numThreads

      finalname = "plots_"+opt.tag+".root"

      hadd = os.environ['CMSSW_BASE'] + '/src/LatinoAnalysis/Tools/scripts/haddfast'

      command = [hadd]
      if nThreads == 1:
        command.append('--compress')
      else:
        command.extend(['-j', str(nThreads)])
      command.append(os.path.join(os.getcwd(), opt.outputDir, finalname))
      command.extend(fileList)
      print ' '.join(command)
      if not opt.dryRun:
        subprocess.Popen(command, cwd = os.path.join(os.getcwd(), opt.outputDir)).communicate()
  
        if not opt.doNotCleanup:
          for fname in fileList:
            os.unlink(opt.outputDir + '/' + fname)

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

    elif opt.doThreads != 0:

      print "~~~~~~~~~~~ Running mkShape in multi-threading mode..."

      command = ""
      command += "rm -r log\n"
      command += "mkdir log"
      os.system(command)

      if opt.numThreads == 0:
        numThreads = os.sysconf('SC_NPROCESSORS_ONLN')
      else:
        numThreads = opt.numThreads
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
                queue.put( [opt.inputDir ,opt.outputDir, variables, cuts_new, samples_new, nuisances, supercut, number, opt.energy, opt.lumi, opt.tag, str(aliases)] )
                number += 1
                fileListPerJob=[]
                weightListPerJob=[]
          else:
            samples_new = {}
            samples_new[sam_k] = copy.deepcopy(sam_v)
            queue.put( [opt.inputDir ,opt.outputDir, variables, cuts_new, samples_new, nuisances, supercut, number, opt.energy, opt.lumi, opt.tag, str(aliases)] )
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
      factory._nThreads  = opt.numThreads
      factory.aliases    = aliases

      factory.makeNominals( opt.inputDir ,opt.outputDir, variables, cuts, samples, nuisances, supercut)
