import heapq

x1 = [1,1,2,3]
x2 = [1,3,4]
x3 = [1,3,6]
x4 = [3,6,7]

l = x1+x2+x3+x4
print("orig list:",l)

final_l = []
final_l2 = []

#while l:
    #final_l.append(heapq.heappop(l))
    #heapq.heappop(l))

#print('Heap list:',final_l)
#print('length:',len(final_l))

l1 = x1
l2 = x2
while l1 and l2:
    a = l1[0]
    b = l2[0]
    if a<=b:
        final_l2.append(a)
        del(l1[0])
        if len(l1) == 0:
            final_l2 +=l2
            #l1 = l3
            #l2 = x4
    else:
        final_l2.append(b)
        del(l2[0])
        if len(l2) == 0:
            fianl_l2 +=l1
            #l1 = x3s
            #l2 = x4

print('Custom list:',final_l2)
print('length:',len(final_l2))
