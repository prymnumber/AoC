from day12 import *

l_file = '/Users/iposton/GitHub/PyPractice/AoC/'+str(sys.argv[1])
path = get_file(l_file).split('\n')
#path = '0 <-> 2\n1 <-> 1\n2 <-> 0, 3, 4\n3 <-> 2, 4\n4 <-> 2, 3, 6\n5 <-> 6\n6 <-> 4, 5'
#print('path:',path)

start_id = 0
pipe_prog_list = []
for line in path:
    pipe_prog_list.append(pipe_prog(line))

print('')
all_connected_prog = []
#prog_set = find_progs_in_group(start_id,all_connected_prog,pipe_prog_list)
#prog_set = list(Set(all_connected_prog))
#prog_set = find_all_connected(start_id,pipe_prog_list)

#print('final prog set:',prog_set)
#print('number of progs in group:',len(prog_set))

prog_ct = find_number_of_groups(pipe_prog_list)
print('total number of groups:',prog_ct)
