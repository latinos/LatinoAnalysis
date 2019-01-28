#  _____         _
# |_   _|___ ___| |___
#   | | / _ | _ \ (_-<
#   |_| \___|___/_/__/
#

import os.path
#import hwwinfo

#---
def confirm(prompt=None, resp=False):
    """prompts for yes or no response from the user. Returns True for yes and
    False for no.

    'resp' should be set to the default value assumed by the caller when
    user simply types ENTER.
    >>> confirm(prompt='Create Directory?', resp=True)
    Create Directory? [y]|n:
    True
    >>> confirm(prompt='Create Directory?', resp=False)
    Create Directory? [n]|y:
    False
    >>> confirm(prompt='Create Directory?', resp=False)
    Create Directory? [n]|y: y
    True
    """

    if prompt is None:
        prompt = 'Confirm'

    if resp:
        prompt = '%s [%s]|%s: ' % (prompt, 'y', 'n')
    else:
        prompt = '%s [%s]|%s: ' % (prompt, 'n', 'y')

    while True:
        ans = raw_input(prompt)
        if not ans:
            return resp
        if ans not in ['y', 'Y', 'n', 'N']:
            print 'please enter y or n.'
            continue
        if ans == 'y' or ans == 'Y':
            return True
        if ans == 'n' or ans == 'N':
            return False

#---
def hookDebugger(debugger='gdb'):
    '''debugging helper, hooks debugger to running interpreter process'''

    import os
    pid = os.spawnvp(os.P_NOWAIT,
                     debugger, [debugger, '-q', 'python', str(os.getpid())])

    # give debugger some time to attach to the python process
    import time
    time.sleep( 1 )

    # verify the process' existence (will raise OSError if failed)
    os.waitpid( pid, os.WNOHANG )
    os.kill( pid, 0 )
    return

#---
def ensuredir(directory):
    if not os.path.exists(directory):
        try:
            os.makedirs(directory)
        except OSError as e:
            if e.errno == 17:
                pass
            else:
                raise e
#---
def loadAndCompile(macro,options='g'):
    import ROOT
    import os
    try:
        code = ROOT.gROOT.LoadMacro(macro+'+'+options)
    except RuntimeError:
        code = ROOT.gROOT.LoadMacro(macro+'++'+options)
    return code

#---
def filterSamples( samples, voc ):

    filtered = {}

    # convert the vocabulary, which is a mixture of strings and 2d tuples, into a dictionary
    fullvoc = dict([ e if isinstance(e,tuple) else (e,e) for e in voc])
    for proc,label in fullvoc.iteritems():

        if label not in samples: continue

        filtered[proc] = samples[label]

    return filtered


#---
def getChain( sample, mass, path, tag='Data2011', tname='latino' ):
    import ROOT
    files = []
    try:
        all = hwwinfo.samples(mass, tag)
        files = all[sample]
    except Exception as e:
        print 'Exception',e
        return None

    chain = ROOT.TChain(tname)
    for f in files: chain.Add(os.path.join(path,f))

    return chain

# ---
def setDebugLevel(opt):
    import logging
    if not opt.debug:
        pass
    elif opt.debug >= 2:
        print 'Logging level set to DEBUG (%d)' % opt.debug
        logging.basicConfig(level=logging.DEBUG)
    elif opt.debug == 1:
        print 'Logging level set to INFO (%d)' % opt.debug
        logging.basicConfig(level=logging.INFO)

#---
def findopt(parser,dest):
    ''' find the option with dest as destination'''
    for o in parser.option_list:
        if hasattr(o,'dest') and o.dest==dest:
            return o
    return None

#---
def loadOptDefaults(parser, pycfg=None, quiet=False):
    '''
    Load the default options from the configuation file.
    The new defaults options shall be written in python, as they are interpreted
    '''

    print " loadOptDefaults::pycfg = ", pycfg

    if not pycfg:
        import sys
        import re
        try:
            # pre-parse the python cfg location
            pyexp = re.compile('--pycfg(=)+')
            j = max([i for i,a in enumerate(sys.argv) if pyexp.match(a) ])   # if more than one, only the last one is used
            dummy = [sys.argv[j]]
            try:
                dummy += [sys.argv[i+1]]
            except IndexError:
                pass

        except:
            dummy = []
        (opt,args) = parser.parse_args(dummy)

        pycfg = opt.pycfg

    #print " pycfg = ", pycfg
    
    if os.path.exists(pycfg):
        handle = open(pycfg,'r')
        vars = {}
        exec(handle,vars)
        handle.close()

        #print " vars = ", vars
        for opt_name, opt_value in vars.iteritems():
            if opt_name[0] == '-': continue

            #print " opt_name[0] = ", opt_name[0]
            #print " opt_name    = ", opt_name
            
            o = findopt(parser, opt_name)
            if o is None: continue

            o.default = opt_value
            parser.defaults[opt_name] = opt_value
            # it modifies the default values
            # if then not defined, these ones will be used
            
            if not quiet: print ' - new default value:',opt_name,'=',opt_value
        return


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


# def make_cat_list(option, opt_str, value, parser):

#     if not hasattr(parser.values,'cats'):
#         setattr(parser.values,'cats',[])

#     try:
#         cats = value.split(',')
#         parser.values.cats = cats

#     except:
#         print 'Malformed option (comma separated list expected):',value


def addOptions(parser):
    parser.add_option('--pycfg'          , dest='pycfg'       , help='configuration file (def=%default)' , default='configuration.py')
    parser.add_option('-d', '--debug'    , dest='debug'       , help='Debug level'                           , default=0      , action='count' )
    #parser.add_option('-c', '--chans'    , dest='chans'       , help='list of channels'                      , default=['0j'] , type='string' , action='callback' , callback=list_maker('chans'))
    parser.add_option('-E', '--energy'   , dest='energy'      , help='Energy (def=%default)'                 , default='13TeV' , type='string')
    parser.add_option('-l', '--lumi'     , dest='lumi'        , help='Luminosity'                            , default=None   , type='float'   )
    
    #parser.add_option('-v', '--variable' , dest='variable'    , help='variable'                              , default=None )
    #parser.add_option('-m', '--mass'     , dest='mass'        , help='run on one mass point only '           , default=hwwinfo.masses[:]      , type='string' , action='callback' , callback=list_maker('mass',',',int))

    parser.add_option('-A', '--aliasesFile',    dest='aliasesFile'      , help='optional file with TTreeFormula aliases'     , default=None )
    parser.add_option('-V', '--variablesFile' , dest='variablesFile'    , help='file with variables'                         , default=None )
    parser.add_option('-C', '--cutsFile' ,      dest='cutsFile'         , help='file with cuts'                              , default=None )
    parser.add_option('-S', '--samplesFile' ,   dest='samplesFile'      , help='file with cuts'                              , default=None )
    parser.add_option('-P', '--plotFile' ,      dest='plotFile'         , help='file with plot configurations'               , default=None )
