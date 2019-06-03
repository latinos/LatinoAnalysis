#!/usr/bin/env python

from optparse import OptionParser
import os,subprocess,re


parser = OptionParser(usage="usage: %prog production_name destination_T2")
parser.add_option("-b", "--copyFrom"    ,   dest="base",     help="local base path to copy from (default /eos/cms/store/group/phys_higgs/cmshww/amassiro/)",            default='/eos/cms/store/group/phys_higgs/cmshww/amassiro/'     , type='string', action='store' )
parser.add_option("-t", "--targetLFN"    ,   dest="tasklfn",     help="target LFN root (default /store/group/phys_higgs/cmshww/amassiro/)",            default='/store/group/phys_higgs/cmshww/amassiro/'     , type='string', action='store' )
parser.add_option("-k", "--kind"    ,   dest="kind",     help="latino or nano, default latino",            default='latino', type='string', action='store')
parser.add_option("-n", "--dry_run"    ,   dest="pretend",     help="do not do it actually",            default=False, action='store_true') 

(opts, args) = parser.parse_args()

base=opts.base
commandLFN = 'lfn2srm --site='+args[1]+" "+opts.tasklfn
if opts.kind=='nano':
  base+="/HWWNano"
  commandLFN+="/HWWNano"
production=args[0]  
inpath=base+"/"+production
print commandLFN
out = subprocess.Popen([commandLFN] , stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)
stdout,stderr = out.communicate()
outpath=stdout.split()[0]
print outpath
print inpath
transferFile = ''
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
    filein='gsiftp://eoscmsftp.cern.ch/'+os.path.join(r, file)
    
    targetpath=production+"/"+os.path.join(r,file).split(production)[1]
    #commandTransfer = 'fts-transfer-submit -s https://fts3-pilot.cern.ch:8446 '+filein+" "+outpath+targetpath
    #if opts.pretend:
    #  print commandTransfer
    #else:
    #  out = subprocess.Popen([commandTransfer] , stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)
    #  stdout,stderr = out.communicate()
    #  print os.path.join(r,file),stdout,stderr
    transferFile += filein+" "+outpath+targetpath+"\n"

fileout = open("transfer.in", "w")
fileout.write(transferFile)
fileout.close()
#    print d





