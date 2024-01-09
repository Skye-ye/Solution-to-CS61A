def fib(n):
    pred, curr = 0, 1
    k = 1
    while k < n:
        pred, curr = curr, pred + curr
        k += 1
    return curr

def main():
    print(fib(int(input())))

if __name__ == '__main__':
    main()
