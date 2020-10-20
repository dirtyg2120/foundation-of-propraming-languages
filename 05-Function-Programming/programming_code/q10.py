from functools import reduce


def compose(*func):
    def inner_compose(f,g):
        return lambda x: f(g(x))
    return reduce(inner_compose, func, lambda x: x)

def increase(x):
    return x + 1


def double(x):
    return x * 2


def square(x):
    return x**3

tmp = compose(double, increase)
print(tmp(1))