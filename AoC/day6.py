import pdb
import sys
from common import *

l_file = '/Users/iposton/GitHub/PyPractice/AoC/'+str(sys.argv[1])
init = map(int,get_file(l_file).split('\t'))

class memory_bank:
    blocks = 0
    id = None
    cycle = 0
    MaxBlock = False
    pattern = []

    def __init__(self,blocks,id,cycle):
        self.blocks = blocks
        self.id = id
        self.cycle = cycle
        self.MaxBlock = False
        self.pattern = []

def find_and_set_max_bank(banks):
    max_bank = max(banks,key=lambda b: b.blocks)
    max_bank.MaxBlock = True
    return max_bank

def redistribute(max_bank, banks):
    #pdb.set_trace()
    banks = banks
    max_block = max_bank.blocks
    id = max_bank.id
    banks[id].blocks = 0
    for i in range(max_block):
        if id == len(banks)-1:
            id = 0
        else:
            id +=1
        banks[id].blocks += 1

    pattern = []
    idx = None
    for i in banks:
        pattern.append(i.blocks)
        if i.MaxBlock == True:
            idx = i.id
    banks[idx].pattern = pattern

    return idx,banks

banks = []
i = 0
new_pattern = []
redist_cycles = 0
size_of_loop = 0

for bank in init:
    banks.append(memory_bank(bank,i,0))
    i+=1

while True:
    #pdb.set_trace()
    maxbank = find_and_set_max_bank(banks)
    idx,banks = redistribute(maxbank,banks)
    new_pattern.append(banks[idx].pattern)
    redist_cycles +=1
    if new_pattern.count(banks[idx].pattern) >1:
        loop_start = new_pattern.index(banks[idx].pattern)
        #print('loop_start:',loop_start)
        size_of_loop = abs(redist_cycles-loop_start)-1
        break


print('END Redist_cycle:',redist_cycles)
print('Size of loop:',size_of_loop)
