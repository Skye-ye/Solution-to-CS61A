# Describing Functions

def likes(n):
    """Returns whether George Boole likes the non-negative integer n."""
    ...

def mystery1(n):
    k = 1
    while k < n:
        if likes(n):
            print(k)
        k = k + 2

def mystery2(n):
    i, j, k = 0, None, None
    while i < n:
        if likes(i):
            if j != None and (k == None or i - j < k):
                k = i - j
            j = i
        i = i + 1
    return k
