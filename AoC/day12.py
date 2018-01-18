import sys
import pdb
from sets import Set
from common import *

class pipe_prog:
    id = 0
    comm_list = []
    connected_progs = {}

    def __init__(self,line):
        line = line.replace(',','')
        line = line.split(' ')
        self.id = int(line[0])
        self.comm_list = map(int,line[2:])
        self.connected_progs = {}

def find_progs_in_group(start_id,connected_progs,pipe_prog_list):
    connected_progs.append(start_id)
    for p in pipe_prog_list:
        if (p.id == start_id
        or p.id in connected_progs
        or p.comm_list in connected_progs
        or start_id in p.comm_list):
            for i in p.comm_list:
                connected_progs.append(i)
    return list(Set(connected_progs))

def find_all_connected(start_id,pipe_prog_list):
    connected_progs = []
    connected_progs = find_progs_in_group(start_id,connected_progs,pipe_prog_list)
    still_more = True
    len_progs = len(connected_progs)
    while still_more:
        for p in connected_progs:
            connected_progs = find_progs_in_group(p,connected_progs,pipe_prog_list)
        if len_progs < len(connected_progs):
            len_progs = len(connected_progs)
        else:
            still_more = False
    return list(Set(connected_progs))

def find_number_of_groups(pipe_prog_list):
    pid_list = Set()
    prog_ct = 0
    still_more = True
    for p in pipe_prog_list:
        pid_list.add(p.id)
    #print('Orig pid list:',pid_list)

    while still_more:
        prog_set = Set(find_all_connected( pid_list.pop(),pipe_prog_list))
        #print('prog_set:',prog_set)
        if len(pid_list) == 0:
            still_more = False

        if len(prog_set) >0:
            prog_ct +=1
            pid_list.difference_update(prog_set)
            #print('new pid list:',pid_list)
        else:
            stll_more = False
    return prog_ct
