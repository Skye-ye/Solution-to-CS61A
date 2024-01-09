def make_keeper(n):
    def keep_ints(cond):
        for i in range(1, n+1):
            if cond(i):
                print(i)
    return keep_ints
