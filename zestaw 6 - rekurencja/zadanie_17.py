def is_prime(nr):
    if nr == 2 or nr == 3:
        return True
    if nr <= 1 or nr % 2 == 0 or nr % 3 == 0:
        return False
    for i in range(6, int(nr**0.5)+2, 6):
        if nr % (i+1) == 0 or nr % (i-1) == 0:
            return False
    return True


def rek(n1, n2, new_n=0, p=0):
    if n1 == 0 and n2 == 0:
        if is_prime(new_n):
            print(new_n)
            global s
            s += 1
        return
    if n1 != 0:
        rek(n1 // 10, n2, new_n + (n1 % 10) * (10**p), p + 1)
    if n2 != 0:
        rek(n1, n2 // 10, new_n + (n2 % 10) * (10**p), p + 1)


s = 0
rek(2, 11)
print(s)
