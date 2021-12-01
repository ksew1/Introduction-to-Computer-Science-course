def f(tab, n, il, p=0, lista=[]):
    global counter
    if n == 1:
        for i in range(p, len(tab)):
            if tab[i] == il:
                counter += 1
                print(lista + [tab[i]])
    else:
        for i in range(p, len(tab)):
            if il % tab[i] == 0:
                f(tab, n - 1, il // tab[i], i + 1, lista + [tab[i]])


counter = 0
f([1, 3, 5, 3, 3, 1, 9, 3, 6], 3, 27)
print('counter', counter)
