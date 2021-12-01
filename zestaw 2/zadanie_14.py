from math import log10


def dec_to_bin(n):
    k = 1
    new_n = 0
    while n > 0:
        new_n += (n % 2) * k
        k *= 10
        n //= 2
    return new_n


def prime(n):
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True


def count_0_1(b, len0, len1):
    c0 = 0
    c1 = 0
    while b > 0:
        if b % 10 == 1:
            c1 += 1

        else:
            c0 += 1
        b //= 10

    if c0 == len0 and c1 == len1:
        return True
    else:
        return False


def main_f(b, n0, n1):
    new_n = 0
    k = 1
    while b > 0:
        if b % 10 == 0:
            new_n += (n0 % 10) * k
            n0 //= 10
        else:
            new_n += (n1 % 10) * k
            n1 //= 10
        k *= 10
        b //= 10
    print(new_n)
    if prime(new_n) is True:

        return 1
    else:
        return 0


n0 = int(input(">"))
print(prime(n0))
n1 = int(input(">"))
len0 = int(log10(n0)) + 1
len1 = int(log10(n1)) + 1
counter = 0
for i in range(2**(len0 + len1 -1), 2**(len0 + len1) - 1):
    b = dec_to_bin(i)
    if count_0_1(b, len0, len1) is True:
        print(b)
        counter += main_f(b, n0, n1)
print(counter)
