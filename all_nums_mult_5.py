import pdb
from itertools import compress, count, permutations

def is_mult_of_5(num):
    return not num%5

def get_mult_of_5(num):
    special_attributes = [
    "__doc__",
    "__name__",
    #"__file__",
    "__dict__",
    "__closure__",
    #"__kwdefaults__",
    "__defaults__"
    ]
    for attribute in special_attributes:
        print(attribute,'->',getattr(get_mult_of_5,attribute))
    return (list(filter(is_mult_of_5,range(num))))

print('non_lambda:',get_mult_of_5(51))

def get_mult_of_5_v2(num):
    special_attributes = [
    "__doc__",
    "__name__",
    #"__file__",
    "__dict__",
    "__closure__",
    #"__kwdefaults__",
    "__defaults__"
    ]
    for attribute in special_attributes:
        print(attribute,'->',getattr(get_mult_of_5_v2,attribute))
    return(list(filter(lambda k:not k%5,range(num))))

print('lambda:',get_mult_of_5_v2(51))
