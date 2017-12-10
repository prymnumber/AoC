import pdb
import sys
from common import *

l_file = '/Users/iposton/GitHub/PyPractice/AoC/'+str(sys.argv[1])
l_data = get_file(l_file).split('\n')
#l_data = 'aa bb cc dd aaa'
#print(l_data)

def check_phrase(phrase):
    split_phrase = phrase.split(' ')
    sorted_phrase = map(lambda x: ''.join(sorted(list(x))),split_phrase)
    set_phrase = set(sorted_phrase)

    return len(split_phrase) == len(set_phrase)

ct = 0
for line in l_data:
    if check_phrase(line):
        ct +=1

print('Number of phrases:',ct)
