nr = int(input(">"))
a, b = 0, 1

while a * b < nr:
    a, b = b, a + b
if a * b == nr:
    print(True)
else:
    print(False)
