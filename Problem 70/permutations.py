# def getPermutations():
#     from itertools import permutations
#     set(itertools.permutations([9,9,9,1]))
#     #return [''.join(p) for p in permutations(str(num))]
#
# print (getPermutations())
def getPermutations(lst):
    import itertools
    return set(itertools.permutations(lst))

print (len((getPermutations([8,7,1,0,9]))))
