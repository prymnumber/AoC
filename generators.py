import pdb
from itertools import permutations

def geo_progression(a,q):
    k=0
    while True:
        result = a*q**k
        if result < 100000:
            yield result
        else:
            return
        k+=1

def print_sqs(start,end):
    for n in range(start,end):
        yield n**2

def get_perms(some_list):
    perm_list = []
    l_list = list(some_list)
    while l_list:
        perm_list.append(l_list.pop())
        get_perms(l_list)
    return perm_list

def get_perms2(some_list):
    perm_list = list(permutations(some_list))
    return perm_list

def get_perms3(some_list):
    perm_list = list()
    l_list = list(some_list)
    #pdb.set_trace()
    for k in some_list:
        if len(l_list) <=1:
            return l_list

        for i in range(len(l_list)-1):
            idx1 = i
            idx2 = i+1
            swap1=l_list[idx1]
            swap2=l_list[idx2]

            l_list[idx2] = swap1
            l_list[idx1] = swap2
            xx = l_list[:]
            perm_list.append(xx)

    return perm_list

def get_perms4(some_list):
    perm_list = list()
    list(some_list)
    #pdb.set_trace()

    for g in some_list:
        l_list = list(some_list[:])
        x_list = list()
        if len(l_list) <=2 :
            x_list = get_perms3(l_list)
            for i in x_list:
            #pdb.set_trace()
                l_list.remove(g)
                i.insert(some_list.index(g)+1,g)
                xx = x_list[:]
                perm_list.append(xx)
        else:
            perm_list = get_perms4(l_list)

    return perm_list


'''
[
(' A', 'B', 'C'),
(' A', 'C', 'B'),
(' B', 'A', 'C'),
(' B', 'C', 'A'),
(' C', 'A', 'B'),
(' C', 'B', 'A')]
'''

l_list = ['a','b','c']
m_list = get_perms(l_list)
#print('Perm1:',m_list)


l_list2 = 'abcd'
m_list2 = get_perms2(l_list2)
m_list2.sort()
print('perm official')
for i in m_list2:
    print(i)
print('number of perms:',len(m_list2))
print('')

l_list3 = 'abc'
m_list3 = get_perms3(l_list3)
m_list3.sort()
print('Perm 3')
for i in m_list3:
   print(i)
print('number of perms:',len(m_list3))
print('')

l_list4 = 'abcd'
m_list4 = get_perms4(l_list4)
#m_list4.sort()
print('Perm 4',l_list4)
ct =0
for i in m_list4:
    for k in i:
        print(k)
        ct+=1
print('number of perms:',ct)
