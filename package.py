def a(a=0,b=0,c=[]):
    a+=1
    b+=2
    c[0] = 3
    print('a:',a)
    print('b:',b)
    print('c:',c)

    b = 'this is a string'
    print('b reassigned:',b)

x = 1
y = 1
z = [1,2,3]

a(c=z,a=x,b=y)
print('outside')
print('x:',x)
print('y:',y)
print('x:',z)
