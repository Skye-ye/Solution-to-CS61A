def fact_times(n, k):
    if n == 0:
        return k
    else:
        return fact_times(n - 1, k * n)

print(fact_times(10, 5))
