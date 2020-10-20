def dist(lst, n):
    if not lst:
        return []
    return [(lst[0], n)] + list(dist(lst[1:], n))


def dist_norm(lst, n):
    out = []
    for e in lst:
        out.append((e, n))
    return out


print(dist([1, 2, 3], 4))
print(dist_norm([1, 2, 3], 4))
