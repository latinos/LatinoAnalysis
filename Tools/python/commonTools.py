#!/usr/bin/env python
import sys, re, os, os.path, string
import subprocess

#---
class list_maker:
    def __init__(self, var, sep=',', type=None ):
        self._type= type
        self._var = var
        self._sep = sep

    def __call__(self,option, opt_str, value, parser):
        if not hasattr(parser.values,self._var):
               setattr(parser.values,self._var,[])

        try:
           array = value.split(self._sep)
           if self._type:
               array = [ self._type(e) for e in array ]
           setattr(parser.values, self._var, array)

        except:
           print 'Malformed option (comma separated list expected):',value

