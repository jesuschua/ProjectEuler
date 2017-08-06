#from skimmer import *
from totient import *
from ispermutation import *
from unique_primefactors import *
def P70(num1, num2):
    smallestquo = 2
    # for i in range(num1,num2,1):
    #     skimmerresult = skimmer(i)
    #     if skimmerresult[0] == True:
    #          if skimmerresult[3] < smallestquo:
    #                 smallestquo = skimmerresult[3]
    #                 print (skimmerresult)
    for i in range(num1, num2, 1):
        primefactors = sorted(prime_factors(i))
        if len(primefactors) == 2:
            if ispermutation(i,(primefactors[0]-1)*(primefactors[1]-1)):
                if smallestquo > i/totient(i):
                    smallestquo = i/totient(i)
                    print(True, i, totient(i), smallestquo)
    #input('End of Program. Press Enter')

P70(1,100000)
#input('End of Program. Press Enter')
