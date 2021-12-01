def f(t, m, p=0):
    if p == len(t):
        return False
    if m == 0:
        return True
    return f(t, m - t[p], p + 1) or f(t, m, p + 1) or f(t, m + t[p], p + 1)


print(f([1, 3, 5, 7, 8], 10))
