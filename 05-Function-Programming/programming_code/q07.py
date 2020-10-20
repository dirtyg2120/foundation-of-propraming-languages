def dist(lst, n):
    if not lst:
        return []
    res = [lst[0],n]
    return res.append(dist(lst[1:],n))

print(dist([1,2,3],4))