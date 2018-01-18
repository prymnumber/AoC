import pdb

def list_all(num):
    x = []
    for i in range(1,num,1):
        #print('i:',i)
        x.append(i)
    x.reverse()
    return x

#print('final:',print_reverse_list(11))
def list_primes(num):
    prime_num = []

    for k in range(2,num+1):
        is_prime = True
        for divisor in range(2,k):
            if k%divisor == 0:
                is_prime = False
                break
        if is_prime:
            prime_num.append(k)
    return(prime_num)

print('list_primes:',list_primes(25))

def list_primes2(num):
    prime_num = []

    for k in range(2,num+1):
        for divisor in range(2,k):
            if k%divisor == 0:
                break
        else:
            prime_num.append(k)
    return(prime_num)

print('list_primes2:',list_primes2(25))
