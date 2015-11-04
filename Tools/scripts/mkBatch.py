#!/usr/bin/env python
from optparse import OptionParser
from batchTools import *

# ------------------------ MAIN

parser = OptionParser(usage="usage: %prog [options] comb")
parser.add_option("-r", "--resub"   ,    dest="resub",        help="resub",                   default=False, action="store_true")
parser.add_option("-c", "--clean"   ,    dest="clean",        help="clean",                   default=False, action="store_true")
parser.add_option("-s", "--status"   ,   dest="status",       help="status",                  default=False, action="store_true")

(options, args) = parser.parse_args()
if options.resub  : batchResub()
elif options.clean  : batchClean()
elif options.status : batchStatus()
else: batchStatus()
