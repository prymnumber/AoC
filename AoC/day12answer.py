from collections import *
from common import *
import itertools
import sys

def main():
    l_file = '/Users/iposton/GitHub/PyPractice/AoC/'+str(sys.argv[1])
    stin = get_file(l_file).split('\n')
    graph = defaultdict(list)
    for line in stin:
        words = line.strip().split()
        a = int(words[0])
        bs = map(lambda x: int(x.strip(',')),words[2:])
        for b in bs:
            graph[a].append(b)
            graph[b].append(a)

    vis = set()
    ans = 0
    for i in range(2000):
        if i in vis:
            continue
        ans += 1
        q = [i]
        while q:
            a = q.pop()
            for b in graph[a]:
                if b not in vis:
                    vis.add(b)
                    q.append(b)

        print('group '+str(ans)+' has '+str(len(vis))+' number of elements')
    print('total groups:',ans)
main()
