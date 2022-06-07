#!/usr/bin/env python

import sys
import shutil

infile = open(sys.argv[1])

outfileContent = ''

for line in infile.readlines():
    linesplit = line.split(',')
    if linesplit[0] == 'L':
      linesplit[0] = '0'
    elif linesplit[0] == 'M':  
      linesplit[0] = '1'
    elif linesplit[0] == 'T':
      linesplit[0] = '2'
    elif linesplit[0] == 'shape':
      linesplit[0] = '3'

    if linesplit[3] == '5':
      linesplit[3] = '0'
    elif linesplit[3] == '4':  
      linesplit[3] = '1'
    elif linesplit[3] == '0':
      linesplit[3] = '2'

    outfileContent += ','.join(linesplit)
infile.close()

shutil.copyfile(sys.argv[1], sys.argv[1]+".orig")
    
with open(sys.argv[1], 'w') as f:
  f.write(outfileContent)
