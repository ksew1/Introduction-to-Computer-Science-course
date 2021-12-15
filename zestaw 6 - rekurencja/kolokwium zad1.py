from random import randint


def essa(n):
    t = []
    for i in range(n):
        t.append([])
        for _ in range(n):
            t[i].append(randint(1, 9))
    return t


def tablica(t):
    for i in range(len(t)):
        for j in range(len(t)):
            print(t[i][j], end='\t')
        print('')
    print()


def convert_to_5(n):
    if n is None:
        return
    temp = n
    i = 0
    while temp > 0:
        if (temp % 5) % 2 == 0:
            i += 1
        temp //= 5
    return i


def check_tab1_with_main(tab1, main_t, max1, x, y):
    s = 0
    for i in range(max1):
        for j in range(max1):
            if convert_to_5(main_t[x+i][y+j]) == convert_to_5(tab1[i][j]):
                s += 1
    if s >= (max1**2) / 3:
        return True
    else:
        return False


def f(tab1, tab2):
    max1 = len(tab1)
    max2 = len(tab2)
    main_t = [[None for _ in range(max2 + 2 * max1 - 2)] for _ in range(max2 + 2 * max1 - 2)]
    for i in range(max2):
        for j in range(max2):
            main_t[i + max1 - 1][j + max1 - 1] = tab2[i][j]

    for i in range(len(main_t) - max1 - 1):
        for j in range(len(main_t) - max1 - 1):
            if check_tab1_with_main(tab1, main_t, max1, i, j):
                return True
    return False


a = essa(3)
tablica(a)
b = essa(5)
tablica(b)
print(f(a, b))
