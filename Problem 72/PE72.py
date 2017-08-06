def PE72(n):
    from totient import totient
    tot_len = 0
    for i in range (0,n+1):
        print (tot_len)
        tot_len += totient(i)
    return(tot_len)

print(PE72(8))
