import sys
import pdb
from common import *

class hex:
    x = None
    y = None
    z = None

    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z

    def move(self,dir):
        self.x += dir.x
        self.y += dir.y
        self.z += dir.z


def get_distance(hex1,hex2):
        return (max(abs(hex1.x-hex2.x),abs(hex1.y-hex2.y),abs(hex1.z-hex2.z)))

def get_direction_coords(dir_str):
    # (x,y,z)
    n  = hex(0,1,-1)
    ne = hex(1,0,-1)
    se = hex(1,-1,0)
    s  = hex(0,-1,1)
    sw = hex(-1,0,1)
    nw = hex(-1,1,0)

    if dir_str == 'n':
        return n
    elif dir_str == 'ne':
        return ne
    elif dir_str == 'se':
        return se
    elif dir_str == 's':
        return s
    elif dir_str == 'sw':
        return sw
    elif dir_str == 'nw':
        return nw
    else:
        return None
