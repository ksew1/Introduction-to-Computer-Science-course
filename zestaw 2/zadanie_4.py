n = int(input(">"))

counter = 0
a = 1

while a <= n:
    b = a
    while b <= n:
        c = b
        while c <= n:
            counter += 1
            c *= 5
        b *= 3
    a *= 2
print(counter)


