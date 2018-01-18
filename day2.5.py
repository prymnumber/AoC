import heapq

x1 = [1,1,2,3]
x2 = [1,3,4]
x3 = [1,3,6]
x4 = [3,6,7]

xarr = dict(zip(range(0,4,1),[x1,x2,x3,x4]))

print('array len:',len(xarr))
#print('xarr[0]:',xarr[0])
#print('xarr[1][2]',xarr[1][2])
#print('xarr.keys():',xarr.keys())
#print('xarr.values():',xarr.values())
print('xarr.items():',xarr.items())

final_l = list(xarr[0])
