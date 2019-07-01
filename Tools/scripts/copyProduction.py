#!/usr/bin/env python

from optparse import OptionParser
import os,subprocess,re

import threading, Queue
import fcntl

class Worker(threading.Thread):
  def __init__(self, queue):
    threading.Thread.__init__(self)
    self.queue = queue
    self.status = -1

  def run(self):
    while True:
      try:

        params = self.queue.get()
        inputFile = params[0]
        targetFile = params[1]
        dochecksumCheck = params[2]
        if dochecksumCheck:
          commandCheckSum="gfal-sum "+inputFile + " ADLER32"
          out = subprocess.Popen([commandCheckSum] , stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)
          stdout,stderr = out.communicate()
          checksumin = stdout.split()
          commandCheckSum="gfal-sum "+targetFile + " ADLER32"
          out = subprocess.Popen([commandCheckSum] , stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)
          stdout,stderr = out.communicate()
          checksumout = stdout.split()
          if len(checksumout) != 2 or len(checksumin) != 2:
            with open ("transfer.in", "a") as output:
              #fcntl.flock(output, fcntl.LOCK_EX)
              output.write(inputFile+" "+targetFile+'\n')
              #fcntl.flock(output, fcntl.LOCK_UN)
              print "committing transfer of file",inputFile
          elif (checksumin[1] != checksumout[1]):
            with open ("transfer.in", "a") as output:
              #fcntl.flock(output, fcntl.LOCK_EX)
              output.write(inputFile+" "+targetFile+'\n')
              #fcntl.flock(output, fcntl.LOCK_UN)
              print "committing transfer of file",inputFile
        else:
          with open ("transfer.in", "a") as output:
            #fcntl.flock(output, fcntl.LOCK_EX)
            output.write(inputFile+" "+targetFile+'\n')
            #fcntl.flock(output, fcntl.LOCK_UN)
        self.queue.task_done()
        if (self.queue.qsize()%100 ==0 and self.queue.qsize()>0):
          print self.queue.qsize(),"remaining tasks"
      except Queue.Empty, e:
        break
      except Exception, e:
        print "Error: %s" % str(e)


parser = OptionParser(usage="usage: %prog production_name destination_T2")
parser.add_option("-b", "--copyFrom"    ,   dest="base",     help="local base path to copy from (default /eos/cms/store/group/phys_higgs/cmshww/amassiro/)",            default='/eos/cms/store/group/phys_higgs/cmshww/amassiro/'     , type='string', action='store' )
parser.add_option("-t", "--targetLFN"    ,   dest="tasklfn",     help="target LFN root (default /store/group/phys_higgs/cmshww/amassiro/)",            default='/store/group/phys_higgs/cmshww/amassiro/'     , type='string', action='store' )
parser.add_option("-k", "--kind"    ,   dest="kind",     help="latino or nano, default latino",            default='latino', type='string', action='store')
parser.add_option("-c", "--check"    ,   dest="check",     help="check the checksum before doing a copy (takes time, use for resubmissions)",            default=False, action='store_true')
parser.add_option("-n", "--dry_run"    ,   dest="pretend",     help="do not do it actually",            default=False, action='store_true') 

(opts, args) = parser.parse_args()

base=opts.base
commandLFN = 'lfn2srm --site='+args[1]+" "+opts.tasklfn
if opts.kind=='nano':
  base+="/HWWNano/"
  commandLFN+="/HWWNano/"
production=args[0]  
inpath=base+"/"+production
print commandLFN
out = subprocess.Popen([commandLFN] , stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)
stdout,stderr = out.communicate()
#outpath="srm://stormfe1.pi.infn.it:8444/srm/managerv2?SFN=/cms/store/group/phys_higgs/cmshww/amassiro/"#stdout.split()[0]
outpath=stdout.split()[0]
print outpath
print inpath
transferFile = ''
numThreads = int(os.sysconf('SC_NPROCESSORS_ONLN'))
print "number of threads = ", numThreads
queue = Queue.Queue()
for i in range(numThreads):
  proc = Worker(queue)
  proc.daemon = True
  proc.start()
os.system("rm transfer.in")  
for r,d,f in os.walk(inpath):
  for dir in d:
     targetpath=(os.path.join(r,dir).split(production))[1]
     commandMkdir = 'gfal-mkdir '+outpath+"/"+production+"/"+targetpath
     if opts.pretend:
       print commandMkdir
     else:
       out = subprocess.Popen([commandMkdir] , stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)
       stdout,stderr = out.communicate()
       print stdout,stderr 
  for file in f:
    if (i%10)==0:
      print "scanned",i,"files/",len(f)
    filein='gsiftp://eoscmsftp.cern.ch/'+os.path.join(r, file)
    
    targetpath=production+"/"+os.path.join(r,file).split(production)[1]
    #commandTransfer = 'fts-transfer-submit -s https://fts3-pilot.cern.ch:8446 '+filein+" "+outpath+targetpath
    #if opts.pretend:
    #  print commandTransfer
    #else:
    #  out = subprocess.Popen([commandTransfer] , stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)
    #  stdout,stderr = out.communicate()
    #  print os.path.join(r,file),stdout,stderr
    
    #commandCheckSum="gfal-sum "+filein + " ADLER32"
    #out = subprocess.Popen([commandCheckSum] , stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)
    #stdout,stderr = out.communicate()
    #checksumin = stdout.split()[1]
    #commandCheckSum="gfal-sum "+outpath+targetpath + " ADLER32"
    #out = subprocess.Popen([commandCheckSum] , stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)
    #stdout,stderr = out.communicate()
    queue.put( [filein, outpath+targetpath, opts.check] )
  #checksumout = stdout.split()[1]
  #if checksumin != checksumout:
  #  transferFile += filein+" "+outpath+targetpath+"\n"

queue.join()
#    print d





