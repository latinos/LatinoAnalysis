
# Common Tools & batch
import os
import math
import argparse
from LatinoAnalysis.Tools.commonTools import *
from LatinoAnalysis.Tools.batchTools  import *

parser = argparse.ArgumentParser()
parser.add_argument("--tag", type=str, default="ntuples")
parser.add_argument("--basedir", type=str, required=True)
parser.add_argument("--targetdir", type=str, required=True)
parser.add_argument("--step", type=str, required=True)
parser.add_argument("--samples-file", type=str, help="File containing the list of samples to elaborate", required=True)
parser.add_argument("-v",'--variations', nargs="+", type=str, required=True)
parser.add_argument("-br",'--branches-remove', nargs="+", type=str, default = [])
parser.add_argument("-bk",'--branches-keep', nargs="+", type=str, default=['*'])
parser.add_argument("-c",'--cut', type=str, required=True)
parser.add_argument("-q",'--queue', type=str, required=True)
parser.add_argument("-fj",'--files-per-job', type=int, default=1)
parser.add_argument('--do-hadd', action="store_true")
parser.add_argument('--dry-run', action="store_true")
args = parser.parse_args()

# get list of samples name
samples = [ ] 
exec(open(args.samples_file))

filesPerJob = args.files_per_job

def makeTargetList(samples):
  """
  Return a list of draw targets or merge sources. Entry of the list can be a sample name string,
  a 2-tuple (sample name, fileblock), or a 3-tuple (sample name, fileblock, eventblock).
  """

  targetList=[]
  for sam_k, sam_v in samples.iteritems():

    nFiles = len(sam_v)
    nFileBlocks = int(math.ceil(float(nFiles) / filesPerJob))

    if nFileBlocks == 1:
      targetList.append(sam_k)
    else:
      targetList.extend((sam_k, iFileBlock) for iFileBlock in range(nFileBlocks))
  return targetList

samples_dict = {}
for sample in samples:
  files_list = getSampleFiles(os.path.join(args.basedir,args.step), sample, True, 'nanoLatino_')
  samples_dict[sample] = [ file[file.rfind("/")+1:] for file in files_list]

# Create job target list
targetList = makeTargetList(samples_dict)

batchSplit = []
stepList=['ALL']
if targetList[0] != 'ALL':
  batchSplit.append('Targets')

# ...Check job status and remove duplicates
print "stepList", stepList
print "targetList", targetList
for iStep in stepList:
  for iTarget in targetList:
    tname = '%s.%d' % iTarget
    pidFile = jobDir+'mkShapes__skim/mkShapes__'+args.tag+'__'+iStep+'__'+tname+'.jid'
    #print pidFile
    if os.path.isfile(pidFile) :
      print '--> Job aready created : '+iStep+'__'+tname
      exit()


if 'slc7' in os.environ['SCRAM_ARCH'] and 'iihe' in os.uname()[1] : use_singularity = True
else : use_singularity = False

bpostFix=''
jobs = batchJobs('skim',args.tag,stepList,targetList,','.join(batchSplit),bpostFix,JOB_DIR_SPLIT_READY=True,USE_SINGULARITY=use_singularity)

_haddnano  = 'PhysicsTools/NanoAODTools/scripts/haddnano.py'
_cmsswBasedir = os.environ["CMSSW_BASE"]
jobs.Add2All('cp '+_cmsswBasedir+'/src/'+ _haddnano+' .')

jobs.AddPy2Sh()
jobs.InitPy("from LatinoAnalysis.Tools.skimWithSystematics import *")


for iTarget in targetList:
  tname = '%s.%d' % iTarget
  samples_files = samples_dict[iTarget[0]]
  iFileBlock = iTarget[1]
  files = samples_files[filesPerJob * iFileBlock:filesPerJob * (iFileBlock + 1)]

  jobs.AddPy( "ALL", iTarget,  "skimmer = Skimmer({},'{}','outputs_tmp','{}',{},'{}',{}, {}, {})".format(
                                              "['"+"','".join(files)+"']", args.basedir,  
                                                args.step, "['"+"','".join(args.variations)+"']", 
                                                args.cut, args.dry_run, 
                                                "['"+"','".join(args.branches_keep)+"']",
                                                "['"+"','".join(args.branches_remove)+"']"))


jobs.InitPy(
"""skimmer.compute_entrylist()
skimmer.copy_trees()"""
)

if args.do_hadd:
  for iTarget in targetList:
    outputfile = 'nanoLatino_%s__part%d.root' % iTarget
    jobs.AddPy("ALL", iTarget, "skimmer.hadd('{}','{}','{}')".format('outputs_hadd', outputfile, 'haddnano.py'))

  jobs.Add2All("rsync -avz outputs_hadd/ "+ args.targetdir)

else:
  jobs.Add2All("rsync -avz outputs_tmp/ "+ args.targetdir)

if not args.dry_run:
   jobs.Sub(args.queue)