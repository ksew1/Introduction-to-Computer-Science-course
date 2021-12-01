nr = int(input(">"))

for i in range(int(nr**0.5), 0, -1):
    if nr % i == 0:
        print(nr, '=', i, '*', nr//i)
        break
