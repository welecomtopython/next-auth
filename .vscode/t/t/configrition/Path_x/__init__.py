import enum
import os.path
from enum import  Enum

class Path(Enum):
    path:str=os.path.abspath(__file__)

    HOM:set=os.path.expanduser('~')

    var:str=path.split('\\')[:-3]
    root='\\'.join(var)

    bin=path.split('\\')[:-1]
    root_bin='\\'.join(bin)


