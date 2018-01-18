import pdb
import sys
from common import *

l_file = '/Users/iposton/GitHub/PyPractice/AoC/'+str(sys.argv[1])
init = get_file(l_file).split('\n')

def check_bang(l_stack):
    if len(l_stack) >=1 and l_stack[-1]=='!':
        return True

def find_group(stream):
    l_stack = []
    num_groups = 0
    scores = []
    score =0
    group_score = 0
    non_cancelled_chars = []
    for char in stream:
        if check_bang(l_stack):
            l_stack.pop()
            continue

        if char == '{':
            if len(l_stack)>=1 and l_stack.count('<')>=1:
                non_cancelled_chars.append(char)
            else:
                l_stack.append(char)
                score +=1
                scores.append(score)
        elif char == '}' and len(l_stack)>=1:
            if  l_stack.count('<')>=1:
                non_cancelled_chars.append(char)
            if l_stack[-1] == '{':
                num_groups += 1
                l_stack.pop()
                group_score+= scores.pop()
                score -=1
        elif char == '<':
            l_stack.append(char)
        elif char == '>' and len(l_stack)>=1:
            if l_stack.count('<')>=1:
                if l_stack[l_stack.index('<')+1:] <> []:
                    for i in l_stack[l_stack.index('<')+1:]:
                        non_cancelled_chars.append(i)
                l_stack = l_stack[:l_stack.index('<')]
        elif char == '!':
            l_stack.append(char)
        else:
            if l_stack.count('<')>=1:
                non_cancelled_chars.append(char)
    #print('number of groups in this stream:',num_groups)
    #print(l_stack)
    return group_score, non_cancelled_chars

total_char_ct = 0
group_score=0
score = 0
for s in init:
    print('')
    total_char_ct += len(s)
    score, non_cancelled_chars = find_group(s)
    group_score += score

print('final group score:',group_score)
print('total_char_ct:',total_char_ct)

print('non_cancelled_chars:',non_cancelled_chars)
print('num of non_cancelled_chars:',len(non_cancelled_chars))
