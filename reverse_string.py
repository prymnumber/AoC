import pdb

x1 = list('The trouble is you think you have time.')
x2 = []
n = -1
pdb.set_trace()

print('Orig:',x1)

while x1:
    x2.append(x1.pop(n))
