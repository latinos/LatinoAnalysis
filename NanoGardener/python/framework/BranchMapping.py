import types

from PhysicsTools.NanoAODTools.postprocessing.framework.datamodel import Object, Collection

class MappedEvent(object):
    def __init__(self, event, mapping):
        self._event = event
        self._swapmap = {}
        self._collectionmap = {}
        for key, value in mapping.iteritems():
            if key.startswith('@'):
                self._collectionmap[key[1:]] = value
            else:
                self._swapmap[key] = value

    def __getattr__(self, name):
        try:
            name = self._swapmap[name]
        except KeyError:
            pass
    
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
    def __init__(self, wrappedTree, mapping={}, suffix='', overwrite=False):
        self._tree = wrappedTree
        self._swapmap = mapping
        self._suffix = suffix
        if overwrite:
            self._toskip = None
        else:
            self._toskip = set()

    def branch(self, name, rootBranchType, n=1, lenVar=None, title=None,limitedPrecision=False):
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

        return self._tree.branch(name, rootBranchType, n=n, lenVar=lenVar, title=title,limitedPrecision=limitedPrecision)

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

def mappedEvent(event, mapping={}):
    if len(mapping) == 0:
        return event
    else:
        return MappedEvent(event, mapping)

def mappedOutputTree(wrappedTree, mapping={}, suffix='', overwrite=False):
    if len(mapping) == 0 and not suffix:
        return wrappedTree
    else:
        return MappedOutputTree(wrappedTree, mapping=mapping, suffix=suffix, overwrite=overwrite)
