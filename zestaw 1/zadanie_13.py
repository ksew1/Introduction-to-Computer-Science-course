def nww(a, b):
    ab = a * b
    while b != 0:
        b, a = a % b, b
    return ab // a


n1 = int(input(">"))
n2 = int(input(">"))
n3 = int(input(">"))

print(nww(nww(n1, n2), n3))
