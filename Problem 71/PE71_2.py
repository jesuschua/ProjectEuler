def PE71_2():
    a1, b1, c1, d1 = 5, 12, 3, 7
    while True:
        a2 = a1 + c1
        b2 = b1 + d1
        if b1 >= 999991:
            return (a1, b1, c1, d1)
        a1 = a2
        b1 = b2

print(PE71_2())
