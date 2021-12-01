def is_prime(n):
    if n == 2 or n == 3:
        return True
    if n <= 1 or n % 2 == 0 or n % 3 == 0:
        return False
    for i in range(6, int(n**0.5 + 1), 6):
        if n % (i - 1) == 0 or n % (i + 1) == 0:
            return False
    return True


def f(n, s, p=0):
    if p == len(n) or len(n) < 2:
        return
    if is_prime(int(n)) is True:
        s.add(n)
    f(n.replace(n[p], ""), s, p)
    f(n, s, p + 1)


def f_main(n):
    n = str(n)
    s = set()
    f(n, s)
    print(s)


f_main(1543)
