def dist(lst, n):
    def dist_recur(lst):
        if not lst:
            return []
        return [(lst[0], n)] + list(dist_recur(lst[1:]))
    return (dist_recur(lst))


def dist_norm(lst, n):
    out = []
    for e in lst:
        out.append((e, n))
    return out


print(dist([1, 2, 3], 4))
print(dist_norm([1, 2, 3], 4))
