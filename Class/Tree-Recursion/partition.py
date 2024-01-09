def count_partitions(n, m):
    """Count the partitions of n using parts up to size m.

    >>> count_partitions(6, 4)
    9
    >>> count_partitions(10, 10)
    42
    """
    if n == 0:
        return 1
    elif n < 0:
        return 0
    elif m == 0:
        return 0
    else:
        with_m = count_partitions(n-m, m)
        without_m = count_partitions(n, m-1)
        return with_m + without_m
