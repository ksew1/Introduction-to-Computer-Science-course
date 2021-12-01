def dec_to_bin(n):
    k = 1
    new_n = 0
    while n > 0:
        new_n += (n % 2)*k
        k *= 10
        n //= 2
    return new_n


def function(n, b):
    new_n = 0
    k = 0
    for _ in range(4):
        if b % 10 == 1:
            new_n += (n % 10) * (10**k)
            k += 1
        b //= 10
        n //= 10
    if new_n % 7 == 0:
        return 1
    else:
        return 0


nr = int(input(">"))
counter = 0

for j in range(1, 16):
    counter += function(nr, dec_to_bin(j))
print(counter)
