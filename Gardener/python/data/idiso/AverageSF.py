#!/usr/bin/env python

import json
import sys
from sys import exit
import ROOT
import optparse
import os.path
import string
import logging
import traceback
from array import array
from collections import OrderedDict
import math

import os




if __name__ == '__main__':
    print '''
--------------------------------------------------------------------------------------------------

             \                                            \ \     /       |                    
            _ \ \ \   /  _ \   __|  _` |   _` |   _ \      \ \   /  _` |  |  |   |   _ \   __| 
           ___ \ \ \ /   __/  |    (   |  (   |   __/       \ \ /  (   |  |  |   |   __/ \__ \ 
         _/    _\ \_/  \___| _|   \__,_| \__, | \___|        \_/  \__,_| _| \__,_| \___| ____/ 
                                         |___/                                                 
 
--------------------------------------------------------------------------------------------------
'''    

    usage = 'usage: %prog [options]'
    parser = optparse.OptionParser(usage)

    parser.add_option('--outputFile'     , dest='outputFile'     , help='output file with averaged values'           , default='test.txt')
          
    # read default parsing options as well
    #hwwtools.addOptions(parser)
    #hwwtools.loadOptDefaults(parser)
    (opt, args) = parser.parse_args()

    sys.argv.append( '-b' )
    ROOT.gROOT.SetBatch()

     
      
    print "list of trigger files"
    
    files_names_trigger = {}

    #files_names_trigger["ICHEP2016fullLumi/PartialRuns/muons_Run_271036_275783.txt"] = 6.274  
    #files_names_trigger["ICHEP2016fullLumi/PartialRuns/muons_Run_275784_276500.txt"] = 3.426 
    #files_names_trigger["ICHEP2016fullLumi/PartialRuns/muons_Run_276501_276811.txt"] = 3.191 
    #opt.outputFile = "ICHEP2016fullLumi/muons.txt"

    files_names_trigger["ICHEP2016fullLumi/PartialRuns/muons_iso_tight_Run_271036_275783.txt"] = 6.274 
    files_names_trigger["ICHEP2016fullLumi/PartialRuns/muons_iso_tight_Run_275784_276500.txt"] = 3.426 
    files_names_trigger["ICHEP2016fullLumi/PartialRuns/muons_iso_tight_Run_276501_276811.txt"] = 3.191 
    opt.outputFile = "ICHEP2016fullLumi/muons_iso_tight.txt"


    print " outputFile       = ", opt.outputFile

    print " files_names_trigger = ", files_names_trigger
    
    files_trigger = {}    
    for names in files_names_trigger :
       #print names
       ##print files_names_trigger[names]       
       
       files_trigger [names] = {
         'file' : open (names),
         'lumi' : files_names_trigger[names]
         }

      
   
    list_triggers = {}

    for names in files_trigger :
      list_triggers[names]  = {  
             'values' : [line.rstrip().split() for line in files_trigger[names]['file']        if '#' not in line] ,
             'lumi'   : files_trigger[names]['lumi']
          }
      




    outFile = open(opt.outputFile, 'w')

    outFile.write('#                                                 data                                                      MC                     \n')
    outFile.write('# etamin  etamax  ptmin   ptmax   eff     deff_high       deff_low                     eff          deff_high       deff_low       \n')

    first_key = list_triggers.keys()[0] 
    
    for point in list_triggers[first_key]['values']:
      outFile.write( '  {0:.2f}  {1:.2f}  {2:.2f}  {3:.2f} '.format(float(point[0]), float(point[1]), float(point[2]), float(point[3])) )



      data = float(point[4])
      mc   = float(point[7])
 
      sigma_up_data = float(point[5])
      sigma_up_mc   = float(point[8])
 
      sigma_do_data = float(point[6])
      sigma_do_mc   = float(point[9])
 
 

      
      luminosity = list_triggers[first_key]['lumi']
     
      all_lumi       =   luminosity
      
      
      data          =  data            *  luminosity
      mc            =  mc              *  luminosity
      sigma_up_data =  sigma_up_data   *  luminosity
      sigma_up_mc   =  sigma_up_mc     *  luminosity
      sigma_do_data =  sigma_do_data   *  luminosity
      sigma_do_mc   =  sigma_do_mc     *  luminosity
 
      
      for names in list_triggers :
        if names != first_key:
          for point_other in list_triggers[names]['values']:
            if    float(point_other[0]) == float(point[0]) \
              and float(point_other[1]) == float(point[1]) \
              and float(point_other[2]) == float(point[2]) \
              and float(point_other[3]) == float(point[3]) :

              new_data = float(point[4])
              new_mc   = float(point[7])
         
              new_sigma_up_data = float(point[5])
              new_sigma_up_mc   = float(point[8])
         
              new_sigma_do_data = float(point[6])
              new_sigma_do_mc   = float(point[9])
         
        
              luminosity = list_triggers[names]['lumi']



              data          =  data           +    luminosity * new_data         
              mc            =  mc             +    luminosity * new_mc           
              sigma_up_data =  sigma_up_data  +    luminosity * new_sigma_up_data
              sigma_up_mc   =  sigma_up_mc    +    luminosity * new_sigma_up_mc  
              sigma_do_data =  sigma_do_data  +    luminosity * new_sigma_do_data
              sigma_do_mc   =  sigma_do_mc    +    luminosity * new_sigma_do_mc  


              all_lumi       =   all_lumi     + luminosity
              
      
      
      data             =    data             /   all_lumi
      mc               =    mc               /   all_lumi
      sigma_up_data    =    sigma_up_data    /   all_lumi
      sigma_up_mc      =    sigma_up_mc      /   all_lumi
      sigma_do_data    =    sigma_do_data    /   all_lumi
      sigma_do_mc      =    sigma_do_mc      /   all_lumi
      
      
      outFile.write( '        {0:.4f}  {1:.4f}  {2:.4f}       {3:.4f}   {4:.4f}   {5:.4f}  \n'.format(float(data), float(sigma_up_data), float(sigma_do_data),  float(mc), float(sigma_up_mc), float(sigma_do_mc)) )
    
      
  
    print " outputFile       = ", opt.outputFile


