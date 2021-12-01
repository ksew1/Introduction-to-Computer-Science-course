nr = int(input(">"))

if nr == 0:
    print("wszystko dzieli zero")
elif nr == 1:
    print(1)
elif nr == -1:
    print(-1)
else:
    if nr > 0:
        print(1)
        negative = False
    else:
        print(1)
        print(-1)
        nr = abs(nr)
        negative = True
    i = 2
    while nr > 1 and i**2 <=nr:
        if nr % i == 0:
            print(i)
            nr //= i
            if negative is True:
                print(-i)
        else:
            i += 1
    if nr > 1:
        print(nr)
        if negative is True:
            print(-nr)
    print("koniec")