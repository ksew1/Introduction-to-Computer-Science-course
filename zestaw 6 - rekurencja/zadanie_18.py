from random import randint

t = []
for i in range(8):
    t.append([])
    for _ in range(8):
        t[i].append(randint(10, 100))


def get_first_digit(num):
    while num > 9:
        num //= 10

    return num


def rek(tab, w, k):
    if w == 7 and k == 7:
        return True
    if w < 7:
        if tab[w][k] % 10 < get_first_digit(tab[w][w + 1]):
            if rek(tab, w + 1, k):
                return True
    if k < 7:
        if tab[w][k] % 10 < get_first_digit(tab[w][k + 1]):
            if rek(tab, w, k + 1):
                return True
    if k < 7 and w < 7:
        if tab[w][k] % 10 < get_first_digit(tab[w + 1][k + 1]):
            if rek(tab, w + 1, k + 1):
                return True
    return False


board = [
    [1, 4, 6, 2, 3, 5, 35, 2],
    [1, 4, 6, 2, 3, 5, 35, 2],
    [1, 4, 6, 82, 3, 5, 35, 2],
    [1, 4, 6, 2, 3, 5, 35, 2],
    [1, 4, 6, 2, 3, 5, 91, 2],
    [1, 4, 6, 82, 3, 5, 24, 2],
    [1, 4, 6, 2, 3, 5, 35, 7],
    [1, 4, 6, 2, 3, 5, 35, 8],
]
print(rek(t, 0, 0))
