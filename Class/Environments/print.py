def print_all(x):
    print(x)
    return print_all

print_all(1)(2)(3)

