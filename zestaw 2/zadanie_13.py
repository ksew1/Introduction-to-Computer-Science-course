nr = int(input(">"))
k = nr % 10
nr //= 10
unique = True
while nr > 0:
    if nr % 10 == k:
        unique = False
        break
    nr //= 10
print(unique)
