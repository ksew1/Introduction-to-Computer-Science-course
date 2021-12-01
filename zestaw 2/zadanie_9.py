def f(x):
    return 1 / x


k = int(input(">"))
n = 1000
x = (k - 1) / n
s = 1 + x / 2
P = 0
for i in range(n):
    P += f(s + i*x)
print(P * x)
