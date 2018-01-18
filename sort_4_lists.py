import heapq
import pdb


x1 = [1,1,2,3]
x2 = [1,3,4]
x3 = [1,3,6]
x4 = [3,6,7]

#complexity = big O(n)
xarr = dict(zip(range(0,4,1),[x1,x2,x3,x4]))

final_l = []
comp1 = list(xarr[0])


for i in range(len(xarr)-1):
    comp2 = list(xarr[i+1])
    final_l =[]

    while comp2:

        if comp1[0] < comp2[0]:
            final_l.append(comp1[0])
            comp1.pop(0)
        else:
            final_l.append(comp2[0])
            comp2.pop(0)
        if len(comp1) == 0:
            for k in comp2:
                final_l.append(k)
                comp2.pop()
            break
        elif len(comp2) == 0:
            for k in comp1:
                final_l.append(k)
                comp2.pop()
            break

    #pdb.set_trace()
    comp1 = final_l

print('original list:',x1+x2+x3+x4)
print('final list:',final_l)
print('length:',len(final_l))

print('Using sort()')
print('original list:',x1+x2+x3+x4)
sort_list = x1+x2+x3+x4
sort_list.sort()
print('sort_list:',sort_list)
