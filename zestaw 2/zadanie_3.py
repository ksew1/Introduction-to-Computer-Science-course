def r(n):
    r_n = 0
    while n > 0:
        r_n = r_n * 10 + n % 10
        n //= 10
    return r_n


def decimal_to_bin(n):
    bin_n = ""
    while n > 0:
        bin_n += str(n % 2)
        n //= 2
    return bin_n[::-1]


nr = int(input(">"))
if nr == r(nr):
    print("palindrom")
if decimal_to_bin(nr) == decimal_to_bin(nr)[::-1]:
    print("palindrom binarny")
