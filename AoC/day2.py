#sum (for each row, calc diff between max and min abs)
import pdb
import sys
from common import *

def get_min_max(num_list):
    max_num = max(num_list)
    min_num = min(num_list)
    return min_num, max_num

def get_mods(num, num_list):
    #num_list.sort(reverse=True)
    retval = 0
    for x in num_list:
        if int(num)%int(x) == 0:
            retval= float(num)/float(x)
            break
    return retval

def corruption_checksum(input_file,fn):
    l_checksum = 0
    #pdb.set_trace()
    if type(input_file) != dict:
        return
    for row in input_file:
        if fn == 'min_max':
            l_row = map(int,input_file[row])
            min_num,max_num = get_min_max(l_row)
            print('max:',max_num,'min_num:',min_num)
            l_checksum += (max_num - min_num)
        if fn == 'even_div':
            l_row = map(float,input_file[row])
            l_row.sort(reverse=True)
            for x in l_row:
                #pdb.set_trace()
                l_checksum += get_mods(x,l_row[l_row.index(x)+1:])

    return int(l_checksum)

l_file = '/Users/iposton/GitHub/PyPractice/AoC/'+str(sys.argv[1])
l_data = get_csv(l_file)
print(l_data)
#l_checksum = corruption_checksum(l_data,'min_max')
l_checksum = corruption_checksum(l_data,'even_div')
print('check_sum:',l_checksum)
