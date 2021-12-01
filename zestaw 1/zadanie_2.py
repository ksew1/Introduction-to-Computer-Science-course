year = 2020
best = (0, year)

for b in range(year//2):
    for a in range(b):
        while a + b < year:
            a, b = b, a + b
        if a + b == year:
            best = (a, b)
            break
    else:
        continue
    break
print(best)

suma = 10000
best = (2020, 0)

for i in range(2021):
    y = 2020
    x = i
    while y > x > 0:
        x, y = y-x, x
    if x + y < suma:
        suma = x + y
        best = (x, y)

print(suma, best)