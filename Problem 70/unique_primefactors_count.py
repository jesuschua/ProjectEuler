#from functools import reduce
#import operator
def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return len(set(factors))

#print(prime_factors(601))
#print (sum(prime_factors(36)))

# def prod(iterable):
#     return reduce(operator.mul, iterable, 1)
#
#print(prod(prime_factors(9708131)))
