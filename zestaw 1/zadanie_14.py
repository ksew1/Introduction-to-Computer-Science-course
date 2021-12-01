def silnia(nr):
    a = 1
    for i in range(2, nr + 1):
        a *= i
    return a


x = float(input(">"))
epsilon = 0.000001
old_cos_x = 10
new_cos_x = 1
n = 1
while abs(old_cos_x - new_cos_x) > epsilon:
    old_cos_x = new_cos_x
    new_cos_x += ((-1)**n) * (x**(n*2)) / silnia(n*2)
    print(new_cos_x, n)

    n += 1
print(new_cos_x)
