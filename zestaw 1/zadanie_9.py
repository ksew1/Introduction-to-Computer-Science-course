nr = int(input(">"))
i = 2
while nr > 1 and i**2 <=nr:
    if nr % i == 0:
        print(i)
        nr //= i
    else:
        i += 1
if nr > 1:
    print(nr)
print("end")