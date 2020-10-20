from functools import reduce


def dist(lst, n):
    out = list(map(lambda x:x, lst))
    return out


print(dist([1, 2, 3], 4))
