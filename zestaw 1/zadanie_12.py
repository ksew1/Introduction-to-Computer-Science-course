def nwd(a, b):
    while b != 0:
        b, a = a % b, b
    return a


n1 = int(input(">"))
n2 = int(input(">"))
n3 = int(input(">"))

print(nwd(nwd(n1, n2), n3))
