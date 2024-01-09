def is_prime(n):
    if n < 2:
        return False
    return prime_helper(n, 2)

def prime_helper(n, divisor):
    if divisor * divisor > n:
        return True
    if n % divisor == 0:
        return False
    if is_prime(divisor):
        return prime_helper(n, divisor + 1)
    else:
        return prime_helper(n, divisor + 1)

