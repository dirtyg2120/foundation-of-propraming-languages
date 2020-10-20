from functools import reduce


def flatten_list_comp(lst):
    out_lst = []
    for e in lst:
        out_lst.extend(e)
    return out_lst


def flatten_recur(lst):
    if not lst:
        return []
    return lst[0] + flatten_recur(lst[1:])


def flatten_high_order(lst):
    out_lst = []
    out_lst = list(reduce(lambda x, y: x+y, lst))
    return out_lst


# lst = [[1, 2, 3], ['a', 'b', 'c'], [1.1, 2.1, 3.1]]

# print(flatten_list_comp(lst))
# print(flatten_recur(lst))
# print(flatten_high_order(lst))
# print(lst)
