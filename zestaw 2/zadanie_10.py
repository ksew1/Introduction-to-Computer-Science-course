nr = int(input(">"))
a = 2
div = False
while a <= nr:
    if nr % a == 0:
        div = True
        break
    a = 3 * a + 1
print(div)
