from common import *
import sys

class firewall:
    depth = None
    range = None
    scanner_loc = None

    def __init__(self, depth, range,scanner_loc):
        self.depth = depth
        self.range = range
        self.scanner_loc = scanner_loc
        self.direction = 1

    def move(self):
        if self.scanner_loc == self.range-1:
            self.direction = -1
        elif self.scanner_loc == 0:
            self.direction = 1

        self.scanner_loc += self.direction

    def reset(self):
        self.scanner_loc = 0
        self.direction = 1

class Packet:
    cur_layer = None
    total_penalty = None

    def __init__(self):
        self.cur_layer = -1
        self.total_penalty =0

    def move(self):
        self.cur_layer += 1

    def reset(self):
        self.cur_layer = -1
        self.total_penalty =0

def build_firewall(wall_raw):

    layers = []
    i = 0
    for layer in wall_raw:
        d, r = layer.split(': ')
        for x in range(int(d)-i):
            l = firewall(i, 0,0)
            layers.append(l)
            i+=1
        if i == int(d):
            l = firewall(int(d),int(r),0)
            layers.append(l)
            i+=1
    return layers

def print_layers(layers):
    for k in layers:
        print('-- Layer:',k.depth)
        for r in range(k.range):
            if k.scanner_loc == r:
                print('[s] -- ',r)
            else:
                print('[ ]')

def travel_through_firewall(layers,packet,delay_secs,part2):

    num_layers = len(layers)
    i = 0
    for secs in range(delay_secs):
        for k in layers:
            k.move()

    #print_layers(layers)
    while True:
        if i >=num_layers :
            break
        packet.move()

        for k in layers:
            if k.depth == packet.cur_layer and k.scanner_loc == 0:
                if part2:
                    packet.total_penalty += (k.depth*k.range)+1
                else:
                    packet.total_penalty += k.depth*k.range
            k.move()
        i+=1

    return packet.total_penalty
