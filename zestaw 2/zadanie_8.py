nr = int(input(">"))
nr += 1
a, b = 1, 1
bazowa_suma = 0
while True:
    suma = bazowa_suma
    while suma < nr:
        suma += a
        a, b = b, a + b
    bazowa_suma = suma
    c,d = 1, 1
    while suma > nr:
        suma -= c
        c, d = d, c + d
    if suma != nr:
        print(nr)
        break
    nr += 1

