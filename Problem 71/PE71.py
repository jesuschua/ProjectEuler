def farey_function(n, descending=False):
    """Print the nth Farey sequence, either ascending or descending."""
    a, b, c, d = 0, 1, 1, n
    if descending:
        a, c = 1, n-1
    print ("%d/%d" % (a,b))
    counterflag = False
    counter = 0
    while (c <= n and not descending) or (a > 0 and descending):
        k = int((n + b) / d)
        if counterflag == True:
            counter += 1
        if a == 1 and b == 3:
            counterflag = True
        if a == 1 and b == 2:
            counterflag = False
            print (counter-1)
        a, b, c, d = c, d, (k*c-a), (k*d-b)
        #print ("%d/%d" % (a,b))
farey_function(12000)
