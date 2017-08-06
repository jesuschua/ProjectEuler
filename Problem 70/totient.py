# import sys
# sys.path.append('D:\\Users\\Jesus Chua\\Documents\\GitHub\\ProjectEuler\\CommonLibrary')
from unique_primefactors import *
def totient(num):
    prod = 1
    print(prime_factors(num))
    for i in prime_factors(num):
        prod = prod * (i-1)
    return prod

print(totient(35))
