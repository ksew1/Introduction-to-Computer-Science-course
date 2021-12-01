def is_prime(n):
    if n == 2 or n == 3:
        return True
    if n <= 1 or n % 2 == 0 or n % 3 == 0:
        return False
    for i in range(6, int(n**0.5 + 1), 6):
        if n % (i - 1) == 0 or n % (i + 1) == 0:
            return False
    return True


def f(n, new_n=0, p=0, one_deleted=False):
    if n == 0:
        if new_n > 9 and is_prime(new_n) and one_deleted:
            print(new_n)
        return
    f(n // 10, new_n + (n % 10) * 10**p, p + 1, one_deleted)
    f(n // 10, new_n, p, True)


f(1543)
