#from functools import reduce
def prime_factors(n):
    i = 2
    factors = []
    reciprocals = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return set(factors)

#print(prime_factors(36))
#print (sum(prime_factors(36)))

# def prod(iterable):
#     return reduce(operator.mul, iterable, 1)
#
# print(prod(prime_factors(36)))
