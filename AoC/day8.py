import pdb
import sys
from common import *

class reg_instruc:
    reg = None
    reg_value = 0
    inc_dec = None
    amount_inc_dec = None
    conditonal_reg = None
    condition = None
    conditional_amt = None

    def __init__(self,reg,inc_dec,amount_inc_dec,conditonal_reg,condition,conditional_amt):
        self.reg = reg
        self.inc_dec = inc_dec
        self.amount_inc_dec = amount_inc_dec
        self.conditonal_reg = conditonal_reg
        self.condition = condition
        self.conditional_amt = conditional_amt


def process_line(line):

    split_line = line.split(' ')
    reg = split_line[0]
    inc_dec = split_line[1]
    amount_inc_dec = split_line[2]
    if_stmt = split_line[3]
    conditonal_reg = split_line[4]
    condition = split_line[5]
    conditional_amt = split_line[6]
    r = reg_instruc(reg,inc_dec,amount_inc_dec,conditonal_reg,condition,conditional_amt)
    return r

def test_and_move_regs(init):
    reg_dict = {}
    max_val_ever = 0
    for line in init:
        new_instruc = process_line(line)
        if not reg_dict.has_key(new_instruc.conditonal_reg):
            reg_dict[new_instruc.conditonal_reg] = 0
        if not reg_dict.has_key(new_instruc.reg):
            reg_dict[new_instruc.reg] = 0

        if new_instruc.inc_dec == 'inc':
            stmt = '+='
        else:
            stmt = '-='
        cond = 'reg_dict[\''+new_instruc.conditonal_reg+'\']'+new_instruc.condition+new_instruc.conditional_amt
        instruc = 'reg_dict[\''+new_instruc.reg+'\']'+stmt+new_instruc.amount_inc_dec
        if eval(cond):
            exec(instruc)
            reg_vals = reg_dict.values()
            if max(reg_vals) > max_val_ever:
                max_val_ever = max(reg_vals)

    return reg_dict, max_val_ever

l_file = '/Users/iposton/GitHub/PyPractice/AoC/'+str(sys.argv[1])
init = get_file(l_file).split('\n')
final_results,max_val_ever = test_and_move_regs(init)
max_result = max(final_results.values())
print('max reg value at end of run:',max_result)
print('max val ever:',max_val_ever)
