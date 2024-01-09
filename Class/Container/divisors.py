def divisors(n):
    return [1] + [x for x in range(2, n) if n % x == 0] + [n]
