def print_delay(x):
    def delay_print(y):
        print(x)
        return print_delay(y)
    return delay_print
