def lstSquare(n):
    if n == 0:
        return []
    return lstSquare(n-1) + [n ** 2]

print(lstSquare(3))
