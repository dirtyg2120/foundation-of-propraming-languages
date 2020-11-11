from functools import reduce


def flatten(lst):
    return list(reduce(lambda x, y: x+y, lst,[]))

lst = flatten([[1,2,3],[4,5],[6,7]])

print(lst)
print(flatten([[]]))
print(flatten([]))
