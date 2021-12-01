nr = int(input(">"))

A = 0
n = 1
while A <= nr:

    A = n * n + n + 1
    print(A)
    if nr % A == 0:
        print("yes")
        break
    n += 1
else:
    print("no")

