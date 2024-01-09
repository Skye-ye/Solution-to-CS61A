from math import sqrt
from math import floor

def find_divisor(x):
    for i in range(floor(sqrt(x)), 0, -1):
        if x % i == 0:
            return i
    return 1

def is_prime(n):
    return find_divisor(n) == 1 and n > 1
