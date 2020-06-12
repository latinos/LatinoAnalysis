import types

from PhysicsTools.NanoAODTools.postprocessing.framework.datamodel import Object, Collection
import LatinoAnalysis.NanoGardener.data.BranchMapping_cfg as config

class MappedEvent(object):
    def __init__(self, event, mapping={}, branches=[], suffix='', mapname=''):
        self._event = event
        self._swapmap = {}
        self._suffix = ''
        self._collectionmap = {}

        if mapname:
            data = config.branch_mapping[mapname]
            if 'mapping' in data:
                mapping = data['mapping']
            if 'branches' in data:
                branches = data['branches']
            if 'suffix' in data:
                suffix = data['suffix']

        # make sure we don't overwrite
        mapping = dict(mapping)

        if suffix:
            if len(branches) != 0:
                for branch in branches:
                    mapping[branch] = branch + suffix
            else:
                self._suffix = suffix
        
        for key, value in mapping.iteritems():
            if key.startswith('@'):
                self._collectionmap[key[1:]] = value
            else:
                self._swapmap[key] = value

    def __getattr__(self, name):
        try:
            name = self._swapmap[name]
        except KeyError:
            name += self._suffix
    
        return self._event.__getattr__(name)

    def __getitem__(self, attr):
        return self.__getattr__(attr)

Object._original_init = Object.__init__
def Object___init__(self, event, prefix, index=None):
    if type(event) is MappedEvent:
        try:
            prefix = event._collectionmap[prefix]
        except KeyError:
            pass

    Object._original_init(self, event, prefix, index=index)

Object.__init__ = Object___init__

Collection._original_init = Collection.__init__
def Collection___init__(self, event, prefix, lenVar=None):
    if type(event) is MappedEvent:
        try:
            prefix = event._collectionmap[prefix]
        except KeyError:
            pass

    Collection._original_init(self, event, prefix, lenVar=lenVar)

Collection.__init__ = Collection___init__    

class MappedOutputTree(object):
    def __init__(self, wrappedTree, mapping={}, branches=[], suffix='', mapname='', overwrite=False):
        self._tree = wrappedTree
        self._swapmap = {}
        self._suffix = ''

        if mapname:
            data = config.branch_mapping[mapname]
            if 'mapping' in data:
                mapping = data['mapping']
            if 'branches' in data:
                branches = data['branches']
            if 'suffix' in data:
                suffix = data['suffix']

        # make sure we don't overwrite
        mapping = dict(mapping)

        if suffix:
            if len(branches) != 0:
                for branch in branches:
                    mapping[branch] = branch + suffix
            else:
                self._suffix = suffix

        self._swapmap = dict(mapping)
            
        if overwrite:
            self._toskip = None
        else:
            self._toskip = set()

    def branch(self, name, rootBranchType, n=1, lenVar=None, title=None, limitedPrecision=False):
        try:
            name = self._swapmap[name]
        except KeyError:
            name += self._suffix

        if self._toskip is not None:
            # don't book this branch if it already exists
            try:
                branch = self._tree._branches[name]
            except KeyError:
                pass
            else:
                self._toskip.add(name)
                return branch

        return self._tree.branch(name, rootBranchType, n=n, lenVar=lenVar, title=title, limitedPrecision=limitedPrecision)

    def fillBranch(self, name, val):
        try:
            name = self._swapmap[name]
        except KeyError:
            name += self._suffix

        if not self._toskip is not None and name in self._toskip:
            return

        self._tree.fillBranch(name, val)

    def __getattr__(self, attr):
        return getattr(self._tree, attr)

def mappedEvent(event, mapping={}, branches=[], suffix='', mapname=''):
    if len(mapping) == 0 and not suffix and not mapname:
        return event
    else:
        return MappedEvent(event, mapping=mapping, branches=branches, suffix=suffix, mapname=mapname)

def mappedOutputTree(wrappedTree, mapping={}, branches=[], suffix='', mapname='', overwrite=False):
    if len(mapping) == 0 and not suffix and not mapname:
        return wrappedTree
    else:
        return MappedOutputTree(wrappedTree, mapping=mapping, branches=branches, suffix=suffix, mapname=mapname, overwrite=overwrite)
