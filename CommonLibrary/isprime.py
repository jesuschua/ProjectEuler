def isprime(num):
    primefactors = []
    if num < 4:
        return True
    if num % 2 == 0:
        return False
    for i in range (3, int(num**.5)+1, 2):
        if num % i == 0:
            primefactors.append(i)
            return False
    return True
