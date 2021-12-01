A = float(input(">"))
B = float(input(">"))
epsilon = 0.000001
while abs(B - A) > epsilon:
    old_A = A
    A, B = (A*B)**0.5, (A+B) / 2
print(A, B)
