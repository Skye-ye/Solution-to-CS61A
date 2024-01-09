m operator import add

def curry2(f):
    def g(x):
        def h(y):
            return f(x, y)
        return h
    return g

m = curry2(add)
add_three = m(3)
add_three(3)

