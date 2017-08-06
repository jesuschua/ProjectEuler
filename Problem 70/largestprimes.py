def largestPrimes(num):
    import sys
    sys.path.append('D:\\Users\\Jesus Chua\\Documents\\GitHub\\ProjectEuler\\CommonLibrary')
    from isprime import isprime
    largestPrimes = []
    for i in range (num,1,-1):
        if isprime(i):
            largestPrimes.append(i)
            if len(largestPrimes) >= 10:
                return largestPrimes
    return largestPrimes

#print(largestPrimes(10000000))
