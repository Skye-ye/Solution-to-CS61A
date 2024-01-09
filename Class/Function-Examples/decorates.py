# Decorators

def trace1(fn):
    """Return a function equivalent to fn that also prints trace output.

    fn -- a function of one argument.
    """
    def traced(x):
        print('Calling', fn, 'on argument', x)
        return fn(x)
    return traced

@trace1
def square(x):
    return x*x

@trace1
def sum_squares_up_to(n):
    total, k = 0, 1
    while k <= n:
        total, k = total + square(k), k + 1
    return total
