def gcd(numSmall,numBig):
    for i in range (2, numSmall+1 ):
        if numBig % i == 0 and numSmall % i == 0:
            return 1
    return 0

#x = gcd(10,750)
#print(x)
