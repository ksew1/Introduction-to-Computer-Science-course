def is_prime(nr):
    if nr == 2 or nr == 3:
        return True
    if nr <= 1 or nr % 2 == 0 or nr % 3== 0:
        return False
    for i in range(6, int(nr**0.5)+1, 6):
        if nr % (i+1) == 0 or nr % (i-1) == 0:
            return False
    return True


def r(tab, n, p=0):

    if p == n:
        return True
    s = 0
    i = p
    print(p, s)
    while i < 30 and i < n:
        s = s * 2 + tab[i]
        if is_prime(s) and r(tab, n, i+1):
            return True
        i += 1
    return False


def main_f(tab):
    if tab[-1] == 0:
        return False
    return r(tab, len(tab))

print(main_f([1,1, 0,1,1]))
