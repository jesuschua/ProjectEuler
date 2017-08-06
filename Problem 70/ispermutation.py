def ispermutation(num1, num2):
    # str1 = str(num1)
    # str2 = str(num2)
    # if len (str1) != len (str2):
    #     return False
    # for i in str2:
    #     if i not in str1:
    #         return False
    # return True


    counter = [0,0,0,0,0,0,0,0,0,0]
    for i in str(num1):
        counter[int(i)] += 1
    for i in str(num2):
        counter[(int(i))] -= 1
    if min(counter) == 0:
        if max(counter) == 0:
            return (True)
    return (False)

#print(ispermutation(9708131, 9701831))
