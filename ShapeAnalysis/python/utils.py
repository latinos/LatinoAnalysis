def flatten_samples(samples):
    ## flatten the subsamples (create full samples named sample_subsample)
    subsamplesmap = []
    for sname in samples.keys():
        sample = samples[sname]
        if 'subsamples' not in sample:
            continue
        
        subsamplesmap.append((sname, []))
        for sub in sample['subsamples']:
            samples['%s_%s' % (sname, sub)] = sample
            subsamplesmap[-1][1].append('%s_%s' % (sname, sub))

        sample.pop('subsamples')
        samples.pop(sname)

    return subsamplesmap

def flatten_cuts(cuts):
    ## flatten the categories (create full cuts named cut_category)
    categoriesmap = []
    for cname in cuts.keys():
        cut = cuts[cname]
        if 'categories' not in cut:
            continue
        
        categoriesmap.append((cname, []))
        for cat in cut['categories']:
            cuts['%s_%s' % (cname, cat)] = cut
            categoriesmap[-1][1].append('%s_%s' % (cname, cat))

        cut.pop('categories')
        cuts.pop(cname)

    return categoriesmap

def update_variables_with_categories(variables, categoriesmap):
    ## variables can have "cuts" specifications
    for variable in variables.itervalues():
        if 'cuts' not in variable:
            continue

        cutspec = variable['cuts']

        for cname, categories in categoriesmap:
            if cname not in cutspec:
                continue

            # original cut is in the spec
            cutspec.remove(cname)

            # if a category (subcut) is also in the spec, we won't touch this variable
            if len(set(cutspec) & set(categories)) != 0:
                continue
          
            # otherwise we replace the cut with all the categories
            cutspec.extend(categories)

def update_nuisances_with_subsamples(nuisances, subsamplesmap):
    for nuisance in nuisances.itervalues():
        if 'samples' not in nuisance:
            continue
        
        samplespec = nuisance['samples']
          
        for sname, subsamples in subsamplesmap:
            if sname not in samplespec:
                continue
            
            # original sample is in the spec
            sconfig = samplespec.pop(sname)

            # if a subsample is also in the spec, we won't toucn this any more
            if len(set(samplespec.iterkeys()) & set(subsamples)) != 0:
                continue
  
            # otherwise we replace the sample with all the subsamples
            samplespec.update((subsample, sconfig) for subsample in subsamples)

def update_nuisances_with_categories(nuisances, categoriesmap):
    for nuisance in nuisances.itervalues():
        if 'cuts' not in nuisance:
            continue
        
        cutspec = nuisance['cuts']

        for cname, categories in categoriesmap:
            if cname not in cutspec:
                continue
            
            # original cut is in the spec
            cutspec.remove(cname)

            # if a category (subcut) is also in the spec, we won't touch this nuisance
            if len(set(cutspec) & set(categories)) != 0:
                continue
  
            # otherwise we replace the cut with all the categories
            cutspec.extend(categories)
