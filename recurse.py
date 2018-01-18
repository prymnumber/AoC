import pdb

def recursive_n(num):
    if num == 0 or num==1:
        return 1
    else:
        return num*(recursive_n(num-1))

pdb.set_trace()
def iterative_n(num):
    x = 1
    if num in (0,1):
        return x
    else:
        for i in range(num):
            x *=i+1
        return x

print('recursive fac:',recursive_n(5))
print('iterative fac:',iterative_n(5))
