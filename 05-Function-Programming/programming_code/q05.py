def flatten(lst):
    if not lst:
        return []
    return lst[0] + flatten(lst[1:])
