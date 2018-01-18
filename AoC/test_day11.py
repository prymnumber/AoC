from day11 import *

l_file = '/Users/iposton/GitHub/PyPractice/AoC/'+str(sys.argv[1])
path = get_file(l_file).split(':')
path1 = 'ne,ne,ne'.split(',')
path2 = 'ne,ne,sw,sw'.split(',')
path3 = 'ne,ne,s,s'.split(',')
path4 = 'se,sw,se,sw,sw'.split(',')

num_steps = 0
h = hex(0,0,0)
start = hex(0,0,0)
dist = 0
max_dist = 0
print('Starting point:',h.x,h.y,h.z)

for step in path:
    dir = get_direction_coords(step)
    h.move(dir)
    num_steps += 1
    #print('after move',num_steps,': ',h.x,h.y,h.z)
    dist = get_distance(h,start)
    if dist > max_dist:
        max_dist = dist

print('End point:',h.x,h.y,h.z)
print('num of steps:',dist)
print('max dist:',max_dist)
