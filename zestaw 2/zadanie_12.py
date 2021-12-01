from math import log10

nr = int(input(">"))
leng = int(log10(nr)+1)
statement = False

while nr > 0:
    if nr % 10 == leng:
        statement = True
        break
    nr //= 10
print(statement)
