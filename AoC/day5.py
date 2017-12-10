from common import *
import pdb
import sys

l_file = '/Users/iposton/GitHub/PyPractice/AoC/'+str(sys.argv[1])
maze = map(int,get_file(l_file).split('\n'))


idx = 0
number_of_steps = 0
part_2 = True

while True:
    if idx >= len(maze):
        print('number of steps:',number_of_steps)
        break

    xstep = maze[idx]

    number_of_steps +=1
    if part_2:
        if maze[idx]>= 3:
            maze[idx] -=1
        else:
            maze[idx] += 1
    else:
        maze[idx] += 1

    idx += xstep
