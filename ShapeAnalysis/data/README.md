# mkTable

mkTable takes the output rootFile from Combine's FitDiagnostics method and returns a table containing the yeidls for every process in each of the defined categories. First, make sure to run FitDiagnostics including these options:

    combine -M FitDiagnostics -d WORKSPACE.root --saveNormalizations --saveWithUncertainties
    
After this, running

    mkTable.py fitDiagnostics.root

produces a .tex file containing a table odd all yields. In case you want to merge a set of processes and/or categories, you may specify a merging scheme following merging_map_template.py, and feeding the file through the `--mergingMap` option:

    mkTable.py fitDiagnostics.root --mergingMap merging_map.py
    
By default pre-fit, b-only fit and s+b fit results are included; use any combination of -e, -b and -s to select pre-fit, b-only and s+b fit results respectively. For example:

    mkTable.py fitDiagnostics.root -e -b
    
produces a table including pre-fit and b-only fit reults. In case you need the table to be in a "Process VS Category" format, use the `--fancyTable` option. In this case the s+b fit results are used, with the pre-fit values displayed in parenthesis.
    
Further options include:

    -u, --uncertainties: includes uncertainties in the table
    --csv: produces .csv file instead of .tex file
    --mergedOnly: restricts the table to only show the categories specified in the merging scheme
    
Hopefully writing those Analysis Notes willi be a little easier now!
