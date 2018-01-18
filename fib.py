import pdb

#f(0)=0
#f(1)=1
#for any n>1, F(n) = f(n-1)+f(n+2)

def fib_gen(num):
    result = [0]
    next_n = 1
    while next_n <= num:
        result.append(next_n)
        next_n = sum(result[-2:])
    return result

print('fib_gen')
print(fib_gen(4))

def fib_gen_iter(num):
    yield 0
    if num == 0:
        return
    a = 0
    b = 1
    while b <= num:
        yield b
        a,b = b,a+b

print('fib_gen_iter')
for i in fib_gen_iter(4):
    print(i)

print('fib_gen_iter obj')
xx = fib_gen_iter(4)
print(next(xx))
print(next(xx))
print(next(xx))

def test_iter(some_string):
    #result = ['']

    #yield (n+n for n in some_string)
    #return
    #yield  (n**2 for n in range(start,end))
    for n in some_string:
        x=n+n
        yield x

print('test_iter')
xy = test_iter('abc')
for i in xy:
    #print(next(xy))
    print(i)

#print(list(next(xy)))
