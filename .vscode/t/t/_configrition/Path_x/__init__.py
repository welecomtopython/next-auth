import enum
import os.path
from enum import  Enum

class Path(Enum):
    path:str=os.path.abspath(__file__)

    hom:set=os.path.expanduser('~')
    var:str=path.split('\\')[:-3]
    root='\\'.join(var)

    bin=path.split('\\')[:-1]
    root_bin='\\'.join(bin)

#
# if __name__=='__main__':
#     print(Path.root_bin.value)



