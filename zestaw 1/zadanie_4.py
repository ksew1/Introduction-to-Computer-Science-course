nr = int(input(">"))

sum1, i = 1, 1
while sum1 < nr:
    i += 1
    sum1 += 1 + (i - 1) * 2
if sum1 == nr:
    print(i)
else:
    print("Ta liczba nie ma pierwiastka całkowitego")
