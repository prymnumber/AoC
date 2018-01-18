import pdb
import sys
from common import *
#import math

class Program:
    name = None
    weight = None
    children = None
    parent = None
    total_weight = None
    level = None

    def __init__(self,name,weight,children,parent,level):
        self.name = name
        self.weight = weight
        self.level = level
        self.children = children
        self.parent = parent
        self.total_weight = None

program_list = []
def find_parent(name,program_list):
    prog_list = program_list
    for p in prog_list:
        if p.children and p.children.count(name):
            return p.name

def build_tree(init):
    for i in init:
        line = i.split(' ')
        name = line[0]
        weight = int(line[1][1:len(line[1])-1])
        arrow = None
        children = []
        parent = None
        level = 0

        if len(line) >2:
            arrow = line[2]
            children_str = line[3:]
            for j in children_str:
                j = j.replace(',','')
                children.append(j)
            level+=1

        p = Program(name,weight,children,parent,level)
        program_list.append(p)
    return program_list

def find_bottom(program_list):
    bottom = None
    for p in program_list:
        p.parent = find_parent(p.name,program_list)
        if p.parent == None:
            bottom = p.name
    return bottom

def find_sibling(prog, program_list):
    for p in program_list:
        if p.name != prog.name and p.parent == prog.parent:
            return p

def find_weights(prog,prog_list):
    wt = 0
    c_wt = 0
    wt_list = []
    if prog.children:
        wt += prog.weight
        for c in prog.children:
            wt+= find_weights(next(x for x in prog_list if x.name ==c),prog_list)
    else:
        wt= prog.weight

    prog.total_weight = wt
    return wt

def find_unbalanced_prog(bottom_prog,prog_list):
    unbal_weight = 0
    bal_weight = 0
    p_weight = 0
    ct_wt=[]
    ct_p = {}
    bot_prog = bottom_prog.name
    bot_wt = bottom_prog.total_weight

    for p in prog_list:
        ct_wt.append(p.total_weight)
        ct_p[p.total_weight] = p.name

    for wt in ct_wt:
        ct = ct_wt.count(wt)
        if ct == 1 and wt != bot_wt:
            unbal_weight = wt

    return next(x for x in prog_list if x.name==ct_p[unbal_weight] and x.name != bot_prog)


l_file = '/Users/iposton/GitHub/PyPractice/AoC/'+str(sys.argv[1])
init = get_file(l_file).split('\n')
program_list = build_tree(init)
bottom = find_bottom(program_list)
print('BOTTOM: ',bottom)
wt = 0
for p in program_list:
    wt= find_weights(p,program_list)

bottom_prog = next(x for x in program_list if x.name==bottom)
print('Final weight:',bottom_prog.total_weight)
unbal_prog = find_unbalanced_prog(bottom_prog,program_list)
print('unbal prog:',unbal_prog.name,'wt, total wt:',unbal_prog.weight,unbal_prog.total_weight)
sib = find_sibling(unbal_prog,program_list)
print('sibling:',sib.name,'wt, total wt:',sib.weight,sib.total_weight)
print('weight needed:',unbal_prog.weight-(unbal_prog.total_weight-sib.total_weight))

#print('final_bal_weight:',find_weight_diff(program_list))
#print(c_list)
