def split(n):
    return n // 10, n % 10

def merge(n1, n2):
    if n1 == 0:
        return n2
    if n2 == 0:
        return n1

    n1_all_but_last, n1_last = split(n1)
    n2_all_but_last, n2_last = split(n2)

    if n1_all_but_last == 0 and n2_all_but_last == 0:
        return n1 * 10 + n2 if n1 > n2 else n2 * 10 + n1

    if n1_last < n2_last:
        return n1_last + merge(n1_all_but_last, n2) * 10
    else:
        return n2_last + merge(n1, n2_all_but_last) * 10
