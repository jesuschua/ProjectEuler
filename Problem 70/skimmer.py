from totient import *
from ispermutation import *
def skimmer(num):
    tot = totient(num)
    if ispermutation(tot,num):
        return [True, num, tot, tot/num]
    else:
        return [False]

#print (skimmer(9708131))
#print(skimmer(9708131))
