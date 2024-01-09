def print_n(n):
    def inner_print(x):
        if n == 0:
            print("done")
        else:
            print(x)
        return print_n(n - 1)
    return inner_print
