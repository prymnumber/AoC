students = [
    dict(id=0, credits=dict(math=9, physics=6, history=7)),
    dict(id=1, credits=dict(math=6, physics=7, latin=10)),
    dict(id=2, credits=dict(history=8, physics=9, chemistry=10)),
    dict(id=3, credits=dict(math=5, physics=5, geography=7)),
]

def decorate(student):
    x = sum(student['credits'].values())
    return(x,student['id'])


def undecorate(decorated_student):
    return(decorated_student[1])


students = sorted(map(decorate,students),reverse=True)
print('decorated:',students)

students = list(map(undecorate,students))
print('undecorated:',students)
print('')

def fn(num):
    x = num*2
    return x

def fn2(num):
    if num > 0:
        return True

x = list(range(5))
print('before map fn :',x)

y = map(fn,x)
print('after map fn :',y)

x = list(range(-2,2))
print('before filter fn:',x)

y = filter(fn2,x)
print('after filter fn :',y)

y = filter(None, x)
print('after filter fn 2:',y)
