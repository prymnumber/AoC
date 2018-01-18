from time import sleep, time
from functools import wraps

def max_result2(threshold):
    def decorate(func):
        @wraps(func)
        def wrapper(*args,**kwargs):
            result = func(*args,**kwargs)
            if result > threshold:
                print('Result is too big %i. Max allowed is %i.' %(result,threshold))
            return result
        return wrapper
    return decorate

def measure(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        t=time()
        result = func(*args,**kwargs)
        print(func.__name__,'took:',time()-t)
        return result
    return wrapper

def max_result(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        result = func(*args,**kwargs)
        if result > 100:
            print('Result is too big %i. Max allowed is 100' %(result))
        return result
    return wrapper

def test_dec(func):
    @wraps(func)
    def xxx (*args):
        result = func(*args)
        if len(result)<= 10:
            print(result.join('abc'))
        return result
    return xxx

@measure
@max_result
def cube(n):
    return n**3

print(cube(2))
print(cube(12))

@test_dec
def str_cube(some_string):
    return (some_string+some_string+some_string)

print(str_cube('123'))

@max_result2(75)
@measure
def cube2(n):
    return n**3

print(cube2(2))
print(cube2(12))
