V = int(input(">"))

a = V
b = 1
while abs(a - b) > 0.000001:
    b = (a + b) / 2
    a = V / b**2
print(a)
