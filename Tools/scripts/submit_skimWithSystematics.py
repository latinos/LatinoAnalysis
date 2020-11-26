
# Common Tools & batch
import os
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
parser.add_argument("-d",'--dry-run', action="store_true")
args = parser.parse_args()

# get list of samples name
samples = [ ] 
exec(open(args.samples_file))

targetList = []
filesList = [ ] 

for sample in samples:
  files_list = getSampleFiles(os.path.join(args.basedir,args.step), sample, True, 'nanoLatino_')
  for i, file in enumerate(files_list):
    # keepingt only the file name
    targetList.append(( sample + "." + str(i)))
    filesList.append(file[  file.rfind("/")+1:] )


batchSplit = []
stepList=['ALL']

if targetList[0] != 'ALL':
  batchSplit.append('Targets')

# ...Check job status and remove duplicates
print "stepList", stepList
print "targetList", targetList
for iStep in stepList:
  for iTarget in targetList:
    tname = iTarget
    pidFile = jobDir+'mkShapes__skim/mkShapes__'+args.tag+'__'+iStep+'__'+tname+'.jid'
    #print pidFile
    if os.path.isfile(pidFile) :
      print '--> Job aready created : '+iStep+'__'+tname
      exit()


if 'slc7' in os.environ['SCRAM_ARCH'] and 'iihe' in os.uname()[1] : use_singularity = True
else : use_singularity = False

bpostFix=''
jobs = batchJobs('skim',args.tag,stepList,targetList,','.join(batchSplit),bpostFix,JOB_DIR_SPLIT_READY=True,USE_SINGULARITY=use_singularity)

jobs.AddPy2Sh()
jobs.InitPy("from LatinoAnalysis.Tools.skimWithSystematics import *")

for iTarget, iFile in zip(targetList, filesList):
  jobs.AddPy( "ALL", iTarget,  "skimmer = Skimmer('{}','{}','tmp_outputs','{}',{},'{}',{}, {}, {})".format(iFile, args.basedir,  
                                                args.step, "['"+"','".join(args.variations)+"']", 
                                                args.cut, args.dry_run, 
                                                "['"+"','".join(args.branches_keep)+"']",
                                                "['"+"','".join(args.branches_remove)+"']"))


                              
jobs.InitPy(
"""skimmer.compute_entrylist()
skimmer.copy_trees()"""
)

jobs.Add2All("rsync -avz tmp_outputs/ "+ args.targetdir)


#if not args.dry_run:
#
#    jobs.Sub(args.queue)