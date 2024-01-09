def keep_ints(cond, n):
    for i in range(1, n + 1):
        if cond(i):
            print(i)

