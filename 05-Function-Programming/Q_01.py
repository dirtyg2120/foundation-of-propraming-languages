def double_list_comp(lst):
    out_lst = []
    for e in lst:
        out_lst.append(e * 2)
    return out_lst


def double_recur(lst):
    n = len(lst)
    return [lst[0]*2] + double_recur(lst[1:]) if n > 0 else []


def double_high_order(lst):
    return list(map(lambda x: x * 2, lst))
