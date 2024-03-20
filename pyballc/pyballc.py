import subprocess
import pandas as pd
import os
from .parser import parse_view, parse_mcrecords
from .settings import check_for_ballcools, get_ballcools_path, set_ballcools_path

def _wrapper(prog=None, 
             implicit=None, 
             explicit=None,
             switchable=None,
             postproc=None):
    try:
        p = subprocess.Popen(
            [os.path.join(get_ballcools_path(), "ballcools"),prog,'-h'],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        help_str = p.communicate()[0].decode()
    except OSError:#TODO this will never happen now. 
        not_implemented = True

    
        
    if implicit is not None:
        if not isinstance(implicit, list):
            implicit = [implicit]
    else:
        implicit = []
        
    if explicit is not None:
        if not isinstance(explicit, list):
            explicit = [explicit]
        explicit = set(explicit)
    else:
        explicit = set()

    if switchable is not None:
        if not isinstance(switchable, list):
            switchable = [switchable]
        switchable = set(switchable)
    else:
        switchable = set()
        
    def decorator(func):
        def wrapped(*args, **kwargs):
            if len(set(kwargs.keys())-explicit-switchable)>0:
                raise #TODO
            cmds = ['ballcools', prog] + list(args)
            for k in kwargs:
                if k in explicit:
                    cmds.extend([f'-{k}', kwargs[k]])
                elif k in switchable:
                    cmds.extend([f'-{k}'])
                    
            p = subprocess.Popen(cmds,
                                 stdout=subprocess.PIPE,
                                 stderr=subprocess.PIPE,
                                )
            stdout_data, stderr_data = p.communicate()
            stdout_data = stdout_data.decode()
            stderr_data = stderr_data.decode()

            if len(stderr_data)>0:
                raise Exception(stderr_data)
            if postproc is not None:
                return postproc(stdout_data, args, kwargs)
                
            return stdout_data
        
        
        wrapped.__doc__ = help_str
        return wrapped
    return decorator
            


class PyBallC:
    def __init__(self, ballcpath=''):
        set_ballcools_path(ballcpath)
        check_for_ballcools()

    @staticmethod
    @_wrapper(prog='view', implicit='ballcpath', switchable=['d','f'], postproc=parse_view)
    def view(*args, **kwargs):
        pass

    @staticmethod
    @_wrapper(prog='index', implicit='ballcpath')
    def index(*args, **kwargs):
        pass

    @staticmethod
    @_wrapper(prog='a2b', implicit=['allcpath','ballcpath','chrompath'], explicit=['a','n'], switchable='b')
    def allc_to_ballc(*args, **kwargs):
        pass

    @staticmethod
    @_wrapper(prog='b2a', implicit=['ballcpath','allcpath',], explicit='x')
    def ballc_to_allc(*args, **kwargs):
        pass

    @staticmethod
    @_wrapper(prog='meta', implicit=['fastapath','cmetapath',])
    def extract_cmeta(*args, **kwargs):
        pass

    @staticmethod
    @_wrapper(prog='query', implicit=['ballcpath','genomeranges',], explicit=['c','x','s','o'], postproc=parse_mcrecords)
    def query(*args, **kwargs):
        pass

    @staticmethod
    @_wrapper(prog='merge', implicit=['outputpath', 'ballcpaths',], explicit=['f','k'])
    def merge(*args, **kwargs):
        pass