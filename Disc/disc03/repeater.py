def make_func_repeater(f, x):
    def repeater(n):
        if n == 0:
            return x
        else:
            return f(repeater(n - 1))
    return repeater
