def f(tab, n, il, p=0,):
    global counter
    if n == 1:
        for i in range(p, len(tab)):
            if tab[i] == il:
                counter += 1
    else:
        for i in range(p, len(tab)):
            if il % tab[i] == 0:
                f(tab, n - 1, il // tab[i], i + 1)


counter = 0
f([1, 3, 5, 3, 6], 2, 3)
print(counter)
