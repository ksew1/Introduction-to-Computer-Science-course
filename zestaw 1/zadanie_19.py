
epsilon = 0.0000001
e = 1
old_e = e + 10
n = 1
silnia = 1
while abs(e - old_e) > epsilon:
    old_e = e
    e += 1 / silnia
    n += 1
    silnia *= n

print(e)
