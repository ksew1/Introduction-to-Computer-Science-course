def tab_sum(tab):
    s = 0
    for el in tab:
        s += el
    return s


def r(n, tab=[], p=0, z=1):
    if p == n:
        if tab_sum(tab) == n and len(tab) != 1:
            print(tab[0], end="")
            for i in range(1, len(tab)):
                print("+", tab[i], end="", sep="")

            print()
        return
    r(n, tab + [z], p + 1, 1)
    r(n, tab, p + 1, z + 1)


r(4)
