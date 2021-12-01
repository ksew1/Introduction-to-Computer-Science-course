def f(t, m, p=0, tab=[]):
    if p == len(t):
        return False
    if m == 0:
        print(tab)
        return True
    return f(t, m - t[p], p + 1, tab + [t[p]]) or f(t, m, p + 1, tab) or f(t, m + t[p], p + 1, tab + [-t[p]])


print(f([1, 3, 5, 7, 8], 10))
