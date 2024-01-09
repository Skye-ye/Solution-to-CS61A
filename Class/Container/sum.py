def sum(L):
    if L == []:
        return 0
    else:
        return L[0] + sum(L[1:])
