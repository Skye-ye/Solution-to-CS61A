def print_sum(x):
    print(x)
    def next_sum(y):
        return print_sum(x + y)
    return next_sum

print_sum(1)(2)(3)
