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

#
#print(prime_factors(36))
