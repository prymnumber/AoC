import pdb

k = 4
binary = []

#pdb.set_trace()
while k >0:
    binary.insert(0,k%2)
    k = k/2

#if k==0:
#    binary.append(0)
#else:
#    binary.append(1)

print('binary:',str(binary))
print('binary reversed:',binary[::-1])
