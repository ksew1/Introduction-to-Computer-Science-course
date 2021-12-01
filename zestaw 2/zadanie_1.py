nr = int(input(">"))
a, b = 1, 1
statement = False
while a * a <= nr:
    if nr % a == 0:
        c, d = 1, 1
        while c < nr//a:
            c, d = d, c + d
        if c == nr // a:
            statement = True
            print(a, c)
            break
    a, b = b, a + b
print(statement)
