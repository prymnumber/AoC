import sys
import pdb
from common import *

cur_pos = 0
skip_size = 0
part2 = True
size = 0

def convert_to_hex(string):
    hex_string =''
    if len(string)>0 and string.count(',') >=1:
        string = string.split(',')
        string = map(int,string)
    for x in string:
        if x != ' ':
            h = hex(x)[2:]
            if len(h) != 2:
                h = '0'+h
            hex_string+=h
            print(h)
    return hex_string

def get_start_end(cur_pos,substring_size,string):
    start1 = cur_pos
    end1 = 0
    start2 = 0
    end2 = 0
    #print('substring_size: ',substring_size)
    #print('len(string[cur_pos:]): ',string[cur_pos:])

    if len(string[cur_pos:])<substring_size:
        end1 = len(string)
        start2 = 0
        end2 = substring_size-len(string[cur_pos:])
    else:
        end1 = cur_pos+substring_size
    #print('start end:',start1,end1,start2,end2)
    return start1,end1,start2,end2

def too_large(length, string):
    if length > len(string):
        return True
    else:
        return False

def break_and_condense(string):
    hashed_blocks = []
    string = map(int,string)
    #print('in break_and_condense:',string)
    for i in range(0,len(string),16):
        block = string[i:i+16]
        #print('')
        #print('block:',block)
        hs = block[0]^block[1]^block[2]^block[3]^block[4]^block[5]^block[6]^block[7]^block[8]^block[9]^block[10]^block[11]^block[12]^block[13]^block[14]^block[15]
        #print(i,'hashed number:',hs)
        hashed_blocks.append(hs)
    return hashed_blocks

def ascii_string(string):
    #print('in ascii_string.',string)
    return map(ord,string)


def single_knot_hash(lengths):
    global cur_pos
    global skip_size
    global size
    global part2

    #print('initial string:',string)
    #while number_of_rounds >0:
    for l in lengths:
        #print('')
        if not too_large(l,string):
            #print('length:',l)
            start1, end1, start2, end2 = get_start_end(cur_pos,l,string)
            substring1 = string[start1:end1]
            #print('substring1:',substring1)
            #substring1.reverse()

            if start2 or end2:
                substring2 = string[start2:end2]
                #print('substring2:',substring2)
                for c in substring2:
                    substring1.append(c)

            #print('substring1 before reverse:',substring1)
            substring1.reverse()
            #print('substring1 after reverse:',substring1)

            j = 0
            for i in range(start1,end1):
                #print('string[i]',string[i])
                #print('substring',)
                string[i] = substring1[j]
                j+=1

            for i in range(start2,end2):
                string[i] = substring1[j]
                j+=1

            #print('string after reverse',substring)
            cur_pos = (cur_pos+l+skip_size)%len(string)
            skip_size = (skip_size+1)%len(string)

    #number_of_rounds -=1
    #print('round left:'' reverse:',number_of_rounds)
    #print('current pos:',cur_pos)
    #print('skip size:',skip_size)
    #
    # print('first 2 numbers:',string[0],string[1])
    # print('final result:',string[0]*string[1])
    return string

def run_day10():
    number_of_rounds = 64
    test = False
    standard_suffix = '17,31,73,47,23'

    if test:
        size=5
    else:
        size = 256
    global string
    string = list(range(0,size))

    l_file = '/Users/iposton/GitHub/PyPractice/AoC/'+str(sys.argv[1])
    if part2:
        lengths = get_file(l_file)
        lengths = ascii_string(lengths)
        x = map(int,standard_suffix.split((',')))
        #for y in standard_suffix:
        lengths+=x
    else:
        lengths = get_file(l_file).split(',')
        lengths = map(int,lengths)

    #print('length:',lengths)
    #print('hashed string:',a_string)
    while number_of_rounds >0:
        #pass
        hashed_string = single_knot_hash(lengths)
        number_of_rounds-=1
        # print('current pos:',cur_pos)
        # print('skip size:',skip_size)
        #
        # print('first 2 numbers:',hashed_string[0],hashed_string[1])
        # #print('final result:',string[0]*string[1])
    #print('hashed_string:',hashed_string)

    hashed_blocks = break_and_condense(hashed_string)
    #print('break_and_condense result:',hashed_blocks)
    hexed_string = convert_to_hex(hashed_blocks)
    print('Final Hexed String:',hexed_string)

#dense_hashed_string = break_and_condense(hashed_string)
#print('dense_hashed_string:',dense_hashed_string)
#hex_string = convert_to_hex(dense_hashed_string)
#print('hexed string:',hex_string)
