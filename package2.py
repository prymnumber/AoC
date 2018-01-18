import pdb

pdb.set_trace()
def min(*x):
    if x:
        mn = x[0]
        for value in x[1:]:
            if value <mn:
                mn = value
                print(mn)
        print('min:',mn)
        return mn

def max(*x):
    if x:
        mn=x[0]
        for value in x[1:]:
            if value >mn:
                mn=value
                print(mn)

        print('max:',mn)
        return mn

def func(**kwargs):
    print(kwargs)

d = {'a':1,'b':2}
e = dict(a=1,b=42)

func(a=1,b=2)

try:
    print('try d')
    func(**d)
except:
    print(Exception)
finally:
    None

try:
    print('try e')
    func(**e)
except:
    print(Exception)
finally:
    None
