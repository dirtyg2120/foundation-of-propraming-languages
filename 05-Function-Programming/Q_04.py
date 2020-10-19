from functools import reduce


def compose_recur(*func):
    def compose(x):
        if func:
            res = compose_recur(*func[1:])(x)
            res = func[0](res)
        else:
            return x

        return res
    return compose


def compose_high_order(*func):
    def compose(f, g):
        return lambda x: f(g(x))
    return reduce(compose, func, lambda x: x)


def increase(x):
    return x + 1


def double(x):
    return x * 2


def square(x):
    return x**3
