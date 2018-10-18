#!/usr/bin/env python
from optparse import OptionParser
from LatinoAnalysis.Tools.commonTools import *
from LatinoAnalysis.Tools.crabTools import *

# ------------------------ MAIN

parser = OptionParser(usage="usage: %prog [options] comb")
parser.add_option("-t", "--tasks"    ,   dest="taskList",     help="task List",            default=[]     , type='string' , action='callback' , callback=list_maker('taskList',','))
parser.add_option("-s", "--status"   ,   dest="status",       help="Get Status",           default=False, action="store_true")
parser.add_option("-u", "--unpack"   ,   dest="unpack",       help="Unpack tarball",       default=False, action="store_true")
parser.add_option("-c", "--clean"    ,   dest="clean",        help="Clean Task(s) Output", default=False, action="store_true")


#parser.add_option("-r", "--resub"   ,    dest="resub",        help="resub",                   default=False, action="store_true")
#parser.add_option("-d", "--resubDir",    dest="resubDir",        help="resub directory",      default='ALL')
#parser.add_option("-q" , "--queue" ,  dest="queue"    , help="Batch Queue"  , default="8nh" , type='string' )
#parser.add_option("-c", "--clean"   ,    dest="clean",        help="clean",                   default=False, action="store_true")
#parser.add_option("-t", "--test"   ,   dest="test",       help="test",                  default=False, action="store_true")


(options, args) = parser.parse_args()

crab = crabMon(options.taskList)

if options.status :  crab.printStatus()
if options.unpack :  crab.unpackAll()
if options.clean  :  crab.cleanAll()
