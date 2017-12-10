import sys
import pdb

def get_file(input_file):
    #l_input_file = sys.argv[1]
    fo = open(input_file, 'r')
    l_data = fo.read().rstrip()
    fo.close()
    return l_data
