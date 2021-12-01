nr = int(input(">"))
statement = True

last_nr = 11

while nr > 0:
    if nr % 10 < last_nr:
        last_nr = nr % 10
    else:
        statement = False
        break
    nr //= 10
print(statement)
