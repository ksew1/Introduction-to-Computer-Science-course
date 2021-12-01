a = int(input(">"))
b = int(input(">"))
n = int(input(">"))

print(a // b, end="")
if a % b != 0:
    print(".", end="")
r = a % b
for _ in range(n):
    if r == 0:
        break
    r *= 10
    print(r//b, end='')
    r = r % b
