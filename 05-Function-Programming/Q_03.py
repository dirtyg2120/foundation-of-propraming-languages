
def lessThan_list_comp(n, lst):
    a = []
    for i in lst:
        if(i < n):
            a.append(i)
    return a


def lessThan_recur(n, lst):
    m = len(lst)
    if (m == 0):
        return []
    if(lst[0] < n):
        return [lst[0]]+lessThan_recur(n, lst[1:])
    else:
        return lessThan_recur(n, lst[1:])


def lessThan_high_order(n, lst):
    return list(filter(lambda e: e < n, lst))
