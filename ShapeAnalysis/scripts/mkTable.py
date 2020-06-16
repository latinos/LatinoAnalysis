#!/usr/bin/env python

from __future__ import print_function
import importlib
import os
import sys
import argparse
import subprocess
import pandas as pd
import numpy as np

pd.options.mode.chained_assignment = None

#------- Helper functions --------------------------------------------------------------------------------------------------------------------------------#

def merge_categories(tab, cats_to_merge, merged_name):

    for cat in cats_to_merge:
        if cat not in tab['category'].values:
            print('ERROR: requested category "{0}" for merging not found in input table. Please check merging_map!'.format(cat)); exit()

    new_df = tab[tab['category'] != cats_to_merge[0]]
    sub_df = tab[tab['category'] == cats_to_merge[0]]
    # Change category name to match merged one
    sub_df['category'].replace({cats_to_merge[0] : merged_name}, inplace=True)

    for cat in cats_to_merge[1:]:

        # Remove categories that have been merged
        new_df = new_df[new_df['category'] != cat]

        # Add yields to merged table
        for proc in tab[tab['category'] == cat]['process'].values:
            for label in ['pre_fit', 's+b_fit', 'b_only_fit']:
                sub_df.loc[sub_df['process'] == proc, label] += tab.loc[(tab['category'] == cat) & (tab['process'] == proc), label].values[0]
            for label in ['pre_fit_error', 's+b_fit_error', 'b_only_fit_error']:
                if len(sub_df.loc[sub_df['process'] == proc, label].values) > 0:
                    sub_df.loc[sub_df['process'] == proc, label] = np.sqrt(sub_df.loc[sub_df['process'] == proc, label].values[0]**2 +
                                                                           tab.loc[(tab['category'] == cat) & (tab['process'] == proc), label].values[0]**2)
                else: sub_df.loc[sub_df['process'] == proc, label] = tab.loc[(tab['category'] == cat) & (tab['process'] == proc), label].values[0]

    return pd.concat([new_df, sub_df], ignore_index=True)


def merge_processes(tab, procs_to_merge, merged_name):

    for proc in procs_to_merge:
        if proc not in tab['process'].values:
            print('ERROR: requested process "{0}" for merging not found in input table. Please check merging_map!'.format(proc)); exit()
    
    new_df = tab[tab['process'] != procs_to_merge[0]]
    sub_df = tab[tab['process'] == procs_to_merge[0]]
    # Change process name to match merged one
    sub_df['process'].replace({procs_to_merge[0] : merged_name}, inplace=True)

    for proc in procs_to_merge[1:]:

        # Remove processes that have been merged
        new_df = new_df[new_df['process'] != proc]

        # Add yields to merged table
        for cat in tab[tab['process'] == proc]['category'].values:
            for label in ['pre_fit', 's+b_fit', 'b_only_fit']:
                sub_df.loc[sub_df['category'] == cat, label] += tab.loc[(tab['category'] == cat) & (tab['process'] == proc), label].values[0]
            for label in ['pre_fit_error', 's+b_fit_error', 'b_only_fit_error']:
                if len(sub_df.loc[sub_df['category'] == cat, label].values) > 0:
                    sub_df.loc[sub_df['category'] == cat, label] = np.sqrt(sub_df.loc[sub_df['category'] == cat, label].values[0]**2 +
                                                                        tab.loc[(tab['category'] == cat) & (tab['process'] == proc), label].values[0]**2)
                else: sub_df.loc[sub_df['category'] == cat, label] = tab.loc[(tab['category'] == cat) & (tab['process'] == proc), label].values[0]

    return pd.concat([new_df, sub_df], ignore_index=True)


def get_latex(tab, pre_fit, b_only, s_b, do_csv, nDec):

    if not pre_fit and not b_only and not s_b: full = True
    else: full = False

    # Give the table the correct formatting
    formatted = []

    if full:
        for index, row in tab.iterrows():
            formatted.append({'category' : row['category'],
                            'process' : row['process'],
                            'pre_fit' : '{0:.{x}f} +/- {1:.{x}f}'.format(row["pre_fit"], row["pre_fit_error"], x=nDec),
                            's+b_fit' : '{0:.{x}f} +/- {1:.{x}f}'.format(row["s+b_fit"], row["s+b_fit_error"], x=nDec),
                            'b_only_fit' : '{0:.{x}f} +/- {1:.{x}f}'.format(row["b_only_fit"], row["b_only_fit_error"], x=nDec)})
    
    else:
        for index, row in tab.iterrows():
            entry = {}
            entry['category'] = row['category']
            entry['process'] = row['process']
            if pre_fit: entry['pre_fit'] = '{0:.{x}f} +/- {1:.{x}f}'.format(row["pre_fit"], row["pre_fit_error"], x=nDec)
            if s_b: entry['s+b_fit'] = '{0:.{x}f} +/- {1:.{x}f}'.format(row["s+b_fit"], row["s+b_fit_error"], x=nDec)
            if b_only: entry['b_only_fit'] = '{0:.{x}f} +/- {1:.{x}f}'.format(row["b_only_fit"], row["b_only_fit_error"], x=nDec)
            formatted.append(entry)

    if do_csv:
        with open('yields_table.csv','w') as outfile:
            outfile.write(pd.DataFrame(formatted)[formatted[0].keys()].to_latex(index=False))

    else:
        with open('yields_table.tex','w') as outfile:
            tmp = pd.DataFrame(formatted)[formatted[0].keys()].to_latex(index=False).replace('+/-', '$\pm$')
            for expr in ['\\toprule', '\\midrule', '\\bottomrule']:
                tmp = tmp.replace(expr, '\hline')
            outfile.write(tmp.replace('tabular', 'longtable'))


def read_input(raw_input):
    
    table = []

    # Read the ouput from mlfitNormsToText, find the beginning of the actual table and digest it
    lines = raw_input.split('\n')[:-1]
    table_start_found=False
    for line in lines:
        if not table_start_found:
            if '------' in line: table_start_found=True
            continue
        entries = line.split()
        table.append({'category' : entries[0],
                      'process' : entries[1],
                      'pre_fit' : float(entries[2]),
                      'pre_fit_error' : float(entries[4]),
                      's+b_fit' : float(entries[5]),
                      's+b_fit_error' : float(entries[7]),
                      'b_only_fit' : float(entries[8]),
                      'b_only_fit_error' : float(entries[10])})

    # Create the DataFrame
    df = pd.DataFrame(table)

    ### The following fills empty rows in the table, i.e. cases in which process X has yield 0 in category Y
    ### In these cases the corresponding row is absent, leading to messes when merging processes. This simply
    ### adds back in the missing lines setting everything to 0.

    procs = []
    for proc in df['process'].values:
        if proc not in procs: procs.append(proc)
    
    cats =  []
    for cat in df['category'].values:
        if cat not in cats: cats.append(cat)

    hole_filler = []

    for cat in cats:
        for proc in procs:
            try: _ = df.loc[(df['category'] == cat) & (df['process'] == proc), 'pre_fit'].values[0]
            except:
                hole_filler.append({'category' : cat,
                                    'process' : proc,
                                    'pre_fit' : 0.0,
                                    'pre_fit_error' : 0.0,
                                    's+b_fit' : 0.0,
                                    's+b_fit_error' : 0.0,
                                    'b_only_fit' : 0.0,
                                    'b_only_fit_error' : 0.0})
            

    df = pd.concat([df, pd.DataFrame(hole_filler)], ignore_index=True)

    return df[table[0].keys()]


def get_latex_reduced(tab, do_merged_only, show_unc, do_csv, nDec):

    formatted = []
    procs = []

    for proc in tab['process'].values:
        if proc not in procs: procs.append(proc)

    if not do_merged_only:
        for proc in procs:
            entry = {'Process' : proc}
            for cat in df[df['process'] == proc]['category'].values:
                if show_unc:
                    try: post_fit = '{0:.{x}f} +/- '.format(df[(df['category'] == cat) & (df['process'] == proc)]['s+b_fit'].values[0], x=nDec)
                    except: post_fit = '0.0 +/- '
                    try: post_fit_error = '{0:.{x}f}'.format(df[(df['category'] == cat) & (df['process'] == proc)]['s+b_fit_error'].values[0], x=nDec)
                    except: post_fit_error = 'n.a.'
                    try: pre_fit = ' ({0:.{x}f} +/- '.format(df[(df['category'] == cat) & (df['process'] == proc)]['pre_fit'].values[0], x=nDec)
                    except: pre_fit = ' (0.0 +/- '
                    try: pre_fit_error = '{0:.{x}f})'.format(df[(df['category'] == cat) & (df['process'] == proc)]['pre_fit_error'].values[0], x=nDec)
                    except: 'n.a.)'
                    entry[cat] = post_fit+post_fit_error+pre_fit+pre_fit_error
                else:
                    try: post_fit = '{0:.{x}f}'.format(df[(df['category'] == cat) & (df['process'] == proc)]['s+b_fit'].values[0], x=nDec)
                    except: post_fit = '0.0'
                    try: pre_fit = ' ({0:.{x}f})'.format(df[(df['category'] == cat) & (df['process'] == proc)]['pre_fit'].values[0], x=nDec)
                    except: pre_fit = ' (0)'
                    entry[cat] = post_fit+pre_fit
            formatted.append(entry)
    
    else:
        if 'categories_to_merge' in globals():
            for proc in procs:
                entry = {'Process' : proc}
                for cat in [c['new_name'] for c in categories_to_merge]:
                    if show_unc:
                        try: post_fit = '{0:.{x}f} +/- '.format(df[(df['category'] == cat) & (df['process'] == proc)]['s+b_fit'].values[0], x=nDec)
                        except: post_fit = '0.0 +/- '
                        try: post_fit_error = '{0:.{x}f}'.format(df[(df['category'] == cat) & (df['process'] == proc)]['s+b_fit_error'].values[0], x=nDec)
                        except: post_fit_error = 'n.a.'
                        try: pre_fit = ' ({0:.{x}f} +/- '.format(df[(df['category'] == cat) & (df['process'] == proc)]['pre_fit'].values[0], x=nDec)
                        except: pre_fit = ' (0.0 +/- '
                        try: pre_fit_error = '{0:.{x}f})'.format(df[(df['category'] == cat) & (df['process'] == proc)]['pre_fit_error'].values[0], x=nDec)
                        except: 'n.a.)'
                        entry[cat] = post_fit+post_fit_error+pre_fit+pre_fit_error
                    else:
                        try: post_fit = '{0:.{x}f}'.format(df[(df['category'] == cat) & (df['process'] == proc)]['s+b_fit'].values[0], x=nDec)
                        except: post_fit = '0.0'
                        try: pre_fit = ' ({0:.{x}f})'.format(df[(df['category'] == cat) & (df['process'] == proc)]['pre_fit'].values[0], x=nDec)
                        except: pre_fit = ' (0)'
                        entry[cat] = post_fit+pre_fit
                formatted.append(entry)
        else: print('Reduced table with merged categories requested, but no categories to merge in merging_map!'); exit()

    if do_csv:
        with open('yields_table.csv','w') as outfile:
            outfile.write(pd.DataFrame(formatted).to_csv(index=False))

    else:
        with open('yields_table.tex','w') as outfile:
            tmp = pd.DataFrame(formatted).to_latex(index=False).replace('+/-', '$\pm$')
            for expr in ['\\toprule', '\\midrule', '\\bottomrule']:
                tmp = tmp.replace(expr, '\hline')
            outfile.write(tmp)


def remove_processes(tab, procs_to_remove):
    df = tab
    procs = []
    for proc in df['process'].values:
        if proc not in procs: procs.append(proc)
    for proc in procs_to_remove:
        if proc in procs:
            df = df[df['process'] != proc]
        else:
            print('WARNING: process {} found in processes_to_remove but absent in workspace, skipping')

    return df

#------- Command line parsing ----------------------------------------------------------------------------------------------------------------------------#

parser = argparse.ArgumentParser(description = 'Produce a LaTeX table form FitDiagnostics output.')
parser.add_argument('input_file', help='fitDiagnostics workspace')
parser.add_argument('--mergingMap', help='Specify file containing merging map to be used')
parser.add_argument('-e', '--expected', help='Add expected yields to table', action='store_true')
parser.add_argument('-b', '--background', help='Add yields from background only fit', action='store_true')
parser.add_argument('-s', '--signal', help='Add yields from signal+background fit', action='store_true')
parser.add_argument('--fancyTable', help='Produce table of yields in sample VS category format', action='store_true')
parser.add_argument('--mergedOnly', help='Use only categories that have been merged in the table', action='store_true')
parser.add_argument('-u', '--uncertainties', help='If --reducedTable is selected, adds uncertainties to the table', action='store_true')
parser.add_argument('--csv', help='Outputs table in .csv format', action='store_true')
parser.add_argument('--decimals', help='Number of decimals to be shown', type=int, default=2)
args = parser.parse_args()

#------- Main --------------------------------------------------------------------------------------------------------------------------------------------#

if __name__ == '__main__':

    # Check if input workspace exists
    if not os.path.exists(args.input_file):
        print('Error: specified input file does not exist!')
        exit()
    
    # Run mlFitNormsToText and save output
    df = read_input(subprocess.check_output(['mlfitNormsToText.py', args.input_file, '-u']))

    try: map_path = args.mergingMap
    except: map_path = None

    if not map_path is None:
        if os.path.exists(args.mergingMap):
            print('--> Performing category and/or sample merging as specified in {}'.format(args.mergingMap))
            sys.path.insert(1, os.getcwd())
            merging_map = importlib.import_module(args.mergingMap.replace('.py',''))

            try: categories_to_merge = merging_map.categories_to_merge
            except: print('--> categories_to_merge not found in {}, skipping'.format(args.mergingMap))

            try: processes_to_merge = merging_map.processes_to_merge
            except: print('--> processes_to_merge not found in {}, skipping'.format(args.mergingMap))

            try: processes_to_remove = merging_map.processes_to_remove
            except: pass

            if 'categories_to_merge' in locals():
                for cat_merge in categories_to_merge:
                    df = merge_categories(df, cat_merge['old_names'], cat_merge['new_name'])
                print('--> categories merged succesfully')
            
            if 'processes_to_merge' in locals():
                for proc_merge in processes_to_merge:
                    df = merge_processes(df, proc_merge['old_names'], proc_merge['new_name'])
                print('--> processes merged succesfully')

            if 'processes_to_remove' in locals():
                print('--> Removing unwanted processes')
                df = remove_processes(df, processes_to_remove)

    if not args.fancyTable: get_latex(df, args.expected, args.background, args.signal, args.csv, args.decimals)
    else: get_latex_reduced(df, args.mergedOnly, args.uncertainties, args.csv, args.decimals)