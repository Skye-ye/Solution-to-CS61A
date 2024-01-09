def multiply(m, n):
    if m == 1:
        return n
    else:
        return multiply(m - 1, n) + n
