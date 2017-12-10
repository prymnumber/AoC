import sys
import pdb
import csv

def get_file(input_file):
    #l_input_file = sys.argv[1]
    fo = open(input_file,'r')
    l_data = fo.read().rstrip()
    fo.close()
    return l_data

def get_csv(input_file):
    with open(input_file,'r') as csvfile:
        #dialect = csv.Sniffer().sniff(csvfile.read(1024))
        l_file = csv.reader(csvfile,delimiter='\t')
        l_data = {}
        l_row = 0
        for row in l_file:
            l_data[l_row] = row
            l_row += 1

    return l_data
