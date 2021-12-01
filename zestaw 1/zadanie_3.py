raw_sum = int(input(">"))

a, b = 0, 1
sum1 = 0

while sum1 < raw_sum:
    sum1 += a
    a, b = b, a + b

a, b = 0, 1
while sum1 > raw_sum:
    sum1 -= a
    a, b = b, a + b
if sum1 == raw_sum:
    print(True)
else:
    print(False)
